# NI OSS SOURCE SNAPSHOT: nimi-python

<!--NI_OSS_SNAPSHOT repo=ni/nimi-python commit=6511f8025f072f7f7021953888b916bbdc31aa2a -->

<!--NI_OSS_SOURCE repo=nimi-python path=docs/niscope/class.rst sha256=e1558ef7544a742c9dc5fb556b6bbdb9dcf477a7c8ec3d9dde1b4cc35bd45ddc bytes=308248 -->
## FILE: docs/niscope/class.rst

- repository: `ni/nimi-python`
- source_path: `docs/niscope/class.rst`
- sha256: `e1558ef7544a742c9dc5fb556b6bbdb9dcf477a7c8ec3d9dde1b4cc35bd45ddc`
- bytes: 308248

````rst
.. py:module:: niscope

Session
=======

.. py:class:: Session(self, resource_name, id_query=False, reset_device=False, options={}, *, grpc_options=None)

    

    Performs the following initialization actions:

    -  Creates a new IVI instrument driver and optionally sets the initial
       state of the following session properties: Range Check, Cache,
       Simulate, Record Value Coercions
    -  Opens a session to the specified device using the interface and
       address you specify for the **resourceName**
    -  Resets the digitizer to a known state if **resetDevice** is set to
       True
    -  Queries the instrument ID and verifies that it is valid for this
       instrument driver if the **IDQuery** is set to True
    -  Returns an instrument handle that you use to identify the instrument
       in all subsequent instrument driver method calls

    



    :param resource_name:
        

        .. caution:: Traditional NI-DAQ and NI-DAQmx device names are not case-sensitive.
            However, all IVI names, such as logical names, are case-sensitive. If
            you use logical names, driver session names, or virtual names in your
            program, you must make sure that the name you use matches the name in
            the IVI Configuration Store file exactly, without any variations in the
            case of the characters.

        | Specifies the resource name of the device to initialize

        For Traditional NI-DAQ devices, the syntax is DAQ::\ *n*, where *n* is
        the device number assigned by MAX, as shown in Example 1.

        For NI-DAQmx devices, the syntax is just the device name specified in
        MAX, as shown in Example 2. Typical default names for NI-DAQmx devices
        in MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by
        right-clicking on the name in MAX and entering a new name.

        An alternate syntax for NI-DAQmx devices consists of DAQ::NI-DAQmx
        device name, as shown in Example 3. This naming convention allows for
        the use of an NI-DAQmx device in an application that was originally
        designed for a Traditional NI-DAQ device. For example, if the
        application expects DAQ::1, you can rename the NI-DAQmx device to 1 in
        MAX and pass in DAQ::1 for the resource name, as shown in Example 4.

        If you use the DAQ::\ *n* syntax and an NI-DAQmx device name already
        exists with that same name, the NI-DAQmx device is matched first.

        You can also pass in the name of an IVI logical name or an IVI virtual
        name configured with the IVI Configuration utility, as shown in Example
        5. A logical name identifies a particular virtual instrument. A virtual
        name identifies a specific device and specifies the initial settings for
        the session.

        +---------+--------------------------------------+--------------------------------------------------+
        | Example | Device Type                          | Syntax                                           |
        +=========+======================================+==================================================+
        | 1       | Traditional NI-DAQ device            | DAQ::1 (1 = device number)                       |
        +---------+--------------------------------------+--------------------------------------------------+
        | 2       | NI-DAQmx device                      | myDAQmxDevice (myDAQmxDevice = device name)      |
        +---------+--------------------------------------+--------------------------------------------------+
        | 3       | NI-DAQmx device                      | DAQ::myDAQmxDevice (myDAQmxDevice = device name) |
        +---------+--------------------------------------+--------------------------------------------------+
        | 4       | NI-DAQmx device                      | DAQ::2 (2 = device name)                         |
        +---------+--------------------------------------+--------------------------------------------------+
        | 5       | IVI logical name or IVI virtual name | myLogicalName (myLogicalName = name)             |
        +---------+--------------------------------------+--------------------------------------------------+


    :type resource_name: str

    :param id_query:
        

        Specify whether to perform an ID query.

        When you set this parameter to True, NI-SCOPE verifies that the
        device you initialize is a type that it supports.

        When you set this parameter to False, the method initializes the
        device without performing an ID query.

        **Defined Values**

        | True—Perform ID query
        | False—Skip ID query

        **Default Value**: True

        


    :type id_query: bool

    :param reset_device:
        

        Specify whether to reset the device during the initialization process.

        Default Value: True

        **Defined Values**

        True (1)—Reset device

        False (0)—Do not reset device

        

        .. note:: For the NI 5112, repeatedly resetting the device may cause excessive
            wear on the electromechanical relays. Refer to `NI 5112
            Electromechanical Relays <REPLACE_DRIVER_SPECIFIC_URL_1(5112_relays)>`__
            for recommended programming practices.


    :type reset_device: bool

    :param options:
        

        Specifies the initial value of certain properties for the session. The
        syntax for **options** is a dictionary of properties with an assigned
        value. For example:

        { 'simulate': False }

        You do not have to specify a value for all the properties. If you do not
        specify a value for a property, the default value is used.

        Advanced Example:
        { 'simulate': True, 'driver_setup': { 'Model': '<model number>',  'BoardType': '<type>' } }

        +-------------------------+---------+
        | Property                | Default |
        +=========================+=========+
        | range_check             | True    |
        +-------------------------+---------+
        | query_instrument_status | False   |
        +-------------------------+---------+
        | cache                   | True    |
        +-------------------------+---------+
        | simulate                | False   |
        +-------------------------+---------+
        | record_value_coersions  | False   |
        +-------------------------+---------+
        | driver_setup            | {}      |
        +-------------------------+---------+


    :type options: dict

    :param grpc_options:
        

        MeasurementLink gRPC session options

        


    :type grpc_options: niscope.GrpcSessionOptions


Methods
=======

abort
-----

    .. py:currentmodule:: niscope.Session

    .. py:method:: abort()

            Aborts an acquisition and returns the digitizer to the Idle state. Call
            this method if the digitizer times out waiting for a trigger.

            



acquisition_status
------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: acquisition_status()

            Returns status information about the acquisition to the **status**
            output parameter.

            



            :rtype: :py:data:`niscope.AcquisitionStatus`
            :return:


                    Returns whether the acquisition is complete, in progress, or unknown.

                    **Defined Values**

                    :py:data:`~niscope.AcquisitionStatus.COMPLETE`

                    :py:data:`~niscope.AcquisitionStatus.IN_PROGRESS`

                    :py:data:`~niscope.AcquisitionStatus.STATUS_UNKNOWN`

                    



add_waveform_processing
-----------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: add_waveform_processing(meas_function)

            Adds one measurement to the list of processing steps that are completed
            before the measurement. The processing is added on a per channel basis,
            and the processing measurements are completed in the same order they are
            registered. All measurement library parameters—the properties starting
            with "meas_"—are cached at the time of registering the
            processing, and this set of parameters is used during the processing
            step. The processing measurements are streamed, so the result of the
            first processing step is used as the input for the next step. The
            processing is done before any other measurements.

            


            .. tip:: This method can be called on specific channels within your :py:class:`niscope.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].add_waveform_processing`

                To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

                Example: :py:meth:`my_session.add_waveform_processing`


            :param meas_function:


                The `array
                measurement <REPLACE_DRIVER_SPECIFIC_URL_2(array_measurements_refs)>`__
                to add.

                


            :type meas_function: :py:data:`niscope.ArrayMeasurement`

auto_setup
----------

    .. py:currentmodule:: niscope.Session

    .. py:method:: auto_setup()

            Automatically configures the instrument. When you call this method,
            the digitizer senses the input signal and automatically configures many
            of the instrument settings. If a signal is detected on a channel, the
            driver chooses the smallest available vertical range that is larger than
            the signal range. For example, if the signal is a 1.2 V\ :sub:`pk-pk`
            sine wave, and the device supports 1 V and 2 V vertical ranges, the
            driver will choose the 2 V vertical range for that channel.

            If no signal is found on any analog input channel, a warning is
            returned, and all channels are enabled. A channel is considered to have
            a signal present if the signal is at least 10% of the smallest vertical
            range available for that channel.

            The following settings are changed:

            +--------------------+-----------------------------------------------+
            | **General**        |                                               |
            +--------------------+-----------------------------------------------+
            | Acquisition mode   | Normal                                        |
            +--------------------+-----------------------------------------------+
            | Reference clock    | Internal                                      |
            +--------------------+-----------------------------------------------+
            | **Vertical**       |                                               |
            +--------------------+-----------------------------------------------+
            | Vertical coupling  | AC (DC for NI 5621)                           |
            +--------------------+-----------------------------------------------+
            | Vertical bandwidth | Full                                          |
            +--------------------+-----------------------------------------------+
            | Vertical range     | Changed by auto setup                         |
            +--------------------+-----------------------------------------------+
            | Vertical offset    | 0 V                                           |
            +--------------------+-----------------------------------------------+
            | Probe attenuation  | Unchanged by auto setup                       |
            +--------------------+-----------------------------------------------+
            | Input impedance    | Unchanged by auto setup                       |
            +--------------------+-----------------------------------------------+
            | **Horizontal**     |                                               |
            +--------------------+-----------------------------------------------+
            | Sample rate        | Changed by auto setup                         |
            +--------------------+-----------------------------------------------+
            | Min record length  | Changed by auto setup                         |
            +--------------------+-----------------------------------------------+
            | Enforce realtime   | True                                          |
            +--------------------+-----------------------------------------------+
            | Number of Records  | Changed to 1                                  |
            +--------------------+-----------------------------------------------+
            | **Triggering**     |                                               |
            +--------------------+-----------------------------------------------+
            | Trigger type       | Edge if signal present, otherwise immediate   |
            +--------------------+-----------------------------------------------+
            | Trigger channel    | Lowest numbered channel with a signal present |
            +--------------------+-----------------------------------------------+
            | Trigger slope      | Positive                                      |
            +--------------------+-----------------------------------------------+
            | Trigger coupling   | DC                                            |
            +--------------------+-----------------------------------------------+
            | Reference position | 50%                                           |
            +--------------------+-----------------------------------------------+
            | Trigger level      | 50% of signal on trigger channel              |
            +--------------------+-----------------------------------------------+
            | Trigger delay      | 0                                             |
            +--------------------+-----------------------------------------------+
            | Trigger holdoff    | 0                                             |
            +--------------------+-----------------------------------------------+
            | Trigger output     | None                                          |
            +--------------------+-----------------------------------------------+



clear_waveform_measurement_stats
--------------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: clear_waveform_measurement_stats(clearable_measurement_function=niscope.ClearableMeasurement.ALL_MEASUREMENTS)

            Clears the waveform stats on the channel and measurement you specify. If
            you want to clear all of the measurements, use
            :py:data:`~niscope.ClearableMeasurement.ALL_MEASUREMENTS` in the **clearableMeasurementFunction**
            parameter.

            Every time a measurement is called, the statistics information is
            updated, including the min, max, mean, standard deviation, and number of
            updates. This information is fetched with
            :py:meth:`niscope.Session._fetch_measurement_stats`. The multi-acquisition array measurements
            are also cleared with this method.

            


            .. tip:: This method can be called on specific channels within your :py:class:`niscope.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].clear_waveform_measurement_stats`

                To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

                Example: :py:meth:`my_session.clear_waveform_measurement_stats`


            :param clearable_measurement_function:


                The `scalar
                measurement <REPLACE_DRIVER_SPECIFIC_URL_2(scalar_measurements_refs)>`__
                or `array
                measurement <REPLACE_DRIVER_SPECIFIC_URL_2(array_measurements_refs)>`__
                to clear the stats for.

                


            :type clearable_measurement_function: :py:data:`niscope.ClearableMeasurement`

clear_waveform_processing
-------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: clear_waveform_processing()

            Clears the list of processing steps assigned to the given channel. The
            processing is added using the :py:meth:`niscope.Session.add_waveform_processing` method,
            where the processing steps are completed in the same order in which they
            are registered. The processing measurements are streamed, so the result
            of the first processing step is used as the input for the next step. The
            processing is also done before any other measurements.

            


            .. tip:: This method can be called on specific channels within your :py:class:`niscope.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].clear_waveform_processing`

                To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

                Example: :py:meth:`my_session.clear_waveform_processing`


close
-----

    .. py:currentmodule:: niscope.Session

    .. py:method:: close()

            When you are finished using an instrument driver session, you must call
            this method to perform the following actions:

            -  Closes the instrument I/O session.
            -  Destroys the IVI session and all of its properties.
            -  Deallocates any memory resources used by the IVI session.

            

            .. note:: This method is not needed when using the session context manager



commit
------

    .. py:currentmodule:: niscope.Session

    .. py:method:: commit()

            Commits to hardware all the parameter settings associated with the task.
            Use this method if you want a parameter change to be immediately
            reflected in the hardware. This method is not supported for
            Traditional NI-DAQ (Legacy) devices.

            



configure_chan_characteristics
------------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: configure_chan_characteristics(input_impedance, max_input_frequency)

            Configures the properties that control the electrical characteristics of
            the channel—the input impedance and the bandwidth.

            


            .. tip:: This method can be called on specific channels within your :py:class:`niscope.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].configure_chan_characteristics`

                To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

                Example: :py:meth:`my_session.configure_chan_characteristics`


            :param input_impedance:


                The input impedance for the channel; NI-SCOPE sets
                :py:attr:`niscope.Session.input_impedance` to this value.

                


            :type input_impedance: float
            :param max_input_frequency:


                The bandwidth for the channel; NI-SCOPE sets
                :py:attr:`niscope.Session.max_input_frequency` to this value. Pass 0 for this
                value to use the hardware default bandwidth. Pass –1 for this value to
                achieve full bandwidth.

                


            :type max_input_frequency: float

configure_equalization_filter_coefficients
------------------------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: configure_equalization_filter_coefficients(coefficients)

            Configures the custom coefficients for the equalization FIR filter on
            the device. This filter is designed to compensate the input signal for
            artifacts introduced to the signal outside of the digitizer. Because
            this filter is a generic FIR filter, any coefficients are valid.
            Coefficient values should be between +1 and –1.

            


            .. tip:: This method can be called on specific channels within your :py:class:`niscope.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].configure_equalization_filter_coefficients`

                To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

                Example: :py:meth:`my_session.configure_equalization_filter_coefficients`


            :param coefficients:


                The custom coefficients for the equalization FIR filter on the device.
                These coefficients should be between +1 and –1. You can obtain the
                number of coefficients from the
                `:py:attr:`niscope.Session.equalization_num_coefficients` <cvi:py:attr:`niscope.Session.equalization_num_coefficients`.html>`__
                property. The
                `:py:attr:`niscope.Session.equalization_filter_enabled` <cvi:py:attr:`niscope.Session.equalization_filter_enabled`.html>`__
                property must be set to TRUE to enable the filter.

                


            :type coefficients: list of float

configure_horizontal_timing
---------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: configure_horizontal_timing(min_sample_rate, min_num_pts, ref_position, num_records, enforce_realtime)

            Configures the common properties of the horizontal subsystem for a
            multirecord acquisition in terms of minimum sample rate.

            



            :param min_sample_rate:


                The sampling rate for the acquisition. Refer to
                :py:attr:`niscope.Session.min_sample_rate` for more information.

                


            :type min_sample_rate: float
            :param min_num_pts:


                The minimum number of points you need in the record for each channel;
                call :py:meth:`niscope.Session.ActualRecordLength` to obtain the actual record length
                used.

                Valid Values: Greater than 1; limited by available memory

                

                .. note:: One or more of the referenced methods are not in the Python API for this driver.


            :type min_num_pts: int
            :param ref_position:


                The position of the Reference Event in the waveform record specified as
                a percentage.

                


            :type ref_position: float
            :param num_records:


                The number of records to acquire

                


            :type num_records: int
            :param enforce_realtime:


                Indicates whether the digitizer enforces real-time measurements or
                allows equivalent-time (RIS) measurements; not all digitizers support
                RIS—refer to `Features Supported by
                Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
                more information.

                Default value: True

                **Defined Values**

                True—Allow real-time acquisitions only

                False—Allow real-time and equivalent-time acquisitions

                


            :type enforce_realtime: bool

configure_trigger_digital
-------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: configure_trigger_digital(trigger_source, slope=niscope.TriggerSlope.POSITIVE, holdoff=hightime.timedelta(seconds=0.0), delay=hightime.timedelta(seconds=0.0))

            Configures the common properties of a digital trigger.

            When you initiate an acquisition, the digitizer waits for the start
            trigger, which is configured through the :py:attr:`niscope.Session.acq_arm_source`
            (Start Trigger Source) property. The default is immediate. Upon
            receiving the start trigger the digitizer begins sampling pretrigger
            points. After the digitizer finishes sampling pretrigger points, the
            digitizer waits for a reference (stop) trigger that you specify with a
            method such as this one. Upon receiving the reference trigger the
            digitizer finishes the acquisition after completing posttrigger
            sampling. With each Configure Trigger method, you specify
            configuration parameters such as the trigger source and the amount of
            trigger delay.

            

            .. note:: For multirecord acquisitions, all records after the first record are
                started by using the Advance Trigger Source. The default is immediate.

                You can adjust the amount of pre-trigger and post-trigger samples using
                the reference position parameter on the
                :py:meth:`niscope.Session.configure_horizontal_timing` method. The default is half of the
                record length.

                Some features are not supported by all digitizers. Refer to `Features
                Supported by
                Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
                more information.

                Digital triggering is not supported in RIS mode.



            :param trigger_source:


                Specifies the trigger source. Refer to :py:attr:`niscope.Session.trigger_source`
                for defined values.

                


            :type trigger_source: str
            :param slope:


                Specifies whether you want a rising edge or a falling edge to trigger
                the digitizer. Refer to :py:attr:`niscope.Session.trigger_slope` for more
                information.

                


            :type slope: :py:data:`niscope.TriggerSlope`
            :param holdoff:


                The length of time the digitizer waits after detecting a trigger before
                enabling NI-SCOPE to detect another trigger. Refer to
                :py:attr:`niscope.Session.trigger_holdoff` for more information.

                


            :type holdoff: hightime.timedelta, datetime.timedelta, or float in seconds
            :param delay:


                How long the digitizer waits after receiving the trigger to start
                acquiring data. Refer to :py:attr:`niscope.Session.trigger_delay_time` for more
                information.

                


            :type delay: hightime.timedelta, datetime.timedelta, or float in seconds

configure_trigger_edge
----------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: configure_trigger_edge(trigger_source, level, trigger_coupling, slope=niscope.TriggerSlope.POSITIVE, holdoff=hightime.timedelta(seconds=0.0), delay=hightime.timedelta(seconds=0.0))

            Configures common properties for analog edge triggering.

            When you initiate an acquisition, the digitizer waits for the start
            trigger, which is configured through the :py:attr:`niscope.Session.acq_arm_source`
            (Start Trigger Source) property. The default is immediate. Upon
            receiving the start trigger the digitizer begins sampling pretrigger
            points. After the digitizer finishes sampling pretrigger points, the
            digitizer waits for a reference (stop) trigger that you specify with a
            method such as this one. Upon receiving the reference trigger the
            digitizer finishes the acquisition after completing posttrigger
            sampling. With each Configure Trigger method, you specify
            configuration parameters such as the trigger source and the amount of
            trigger delay.

            

            .. note:: Some features are not supported by all digitizers. Refer to `Features
                Supported by
                Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
                more information.



            :param trigger_source:


                Specifies the trigger source. Refer to :py:attr:`niscope.Session.trigger_source`
                for defined values.

                


            :type trigger_source: str
            :param level:


                The voltage threshold for the trigger. Refer to
                :py:attr:`niscope.Session.trigger_level` for more information.

                


            :type level: float
            :param trigger_coupling:


                Applies coupling and filtering options to the trigger signal. Refer to
                :py:attr:`niscope.Session.trigger_coupling` for more information.

                


            :type trigger_coupling: :py:data:`niscope.TriggerCoupling`
            :param slope:


                Specifies whether you want a rising edge or a falling edge to trigger
                the digitizer. Refer to :py:attr:`niscope.Session.trigger_slope` for more
                information.

                


            :type slope: :py:data:`niscope.TriggerSlope`
            :param holdoff:


                The length of time the digitizer waits after detecting a trigger before
                enabling NI-SCOPE to detect another trigger. Refer to
                :py:attr:`niscope.Session.trigger_holdoff` for more information.

                


            :type holdoff: hightime.timedelta, datetime.timedelta, or float in seconds
            :param delay:


                How long the digitizer waits after receiving the trigger to start
                acquiring data. Refer to :py:attr:`niscope.Session.trigger_delay_time` for more
                information.

                


            :type delay: hightime.timedelta, datetime.timedelta, or float in seconds

configure_trigger_hysteresis
----------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: configure_trigger_hysteresis(trigger_source, level, hysteresis, trigger_coupling, slope=niscope.TriggerSlope.POSITIVE, holdoff=hightime.timedelta(seconds=0.0), delay=hightime.timedelta(seconds=0.0))

            Configures common properties for analog hysteresis triggering. This kind
            of trigger specifies an additional value, specified in the
            **hysteresis** parameter, that a signal must pass through before a
            trigger can occur. This additional value acts as a kind of buffer zone
            that keeps noise from triggering an acquisition.

            When you initiate an acquisition, the digitizer waits for the start
            trigger, which is configured through the
            :py:attr:`niscope.Session.acq_arm_source`. The default is immediate. Upon
            receiving the start trigger the digitizer begins sampling pretrigger
            points. After the digitizer finishes sampling pretrigger points, the
            digitizer waits for a reference (stop) trigger that you specify with a
            method such as this one. Upon receiving the reference trigger the
            digitizer finishes the acquisition after completing posttrigger
            sampling. With each Configure Trigger method, you specify
            configuration parameters such as the trigger source and the amount of
            trigger delay.

            

            .. note:: Some features are not supported by all digitizers. Refer to `Features
                Supported by
                Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
                more information.



            :param trigger_source:


                Specifies the trigger source. Refer to :py:attr:`niscope.Session.trigger_source`
                for defined values.

                


            :type trigger_source: str
            :param level:


                The voltage threshold for the trigger. Refer to
                :py:attr:`niscope.Session.trigger_level` for more information.

                


            :type level: float
            :param hysteresis:


                The size of the hysteresis window on either side of the **level** in
                volts; the digitizer triggers when the trigger signal passes through the
                hysteresis value you specify with this parameter, has the slope you
                specify with **slope**, and passes through the **level**. Refer to
                :py:attr:`niscope.Session.trigger_hysteresis` for defined values.

                


            :type hysteresis: float
            :param trigger_coupling:


                Applies coupling and filtering options to the trigger signal. Refer to
                :py:attr:`niscope.Session.trigger_coupling` for more information.

                


            :type trigger_coupling: :py:data:`niscope.TriggerCoupling`
            :param slope:


                Specifies whether you want a rising edge or a falling edge to trigger
                the digitizer. Refer to :py:attr:`niscope.Session.trigger_slope` for more
                information.

                


            :type slope: :py:data:`niscope.TriggerSlope`
            :param holdoff:


                The length of time the digitizer waits after detecting a trigger before
                enabling NI-SCOPE to detect another trigger. Refer to
                :py:attr:`niscope.Session.trigger_holdoff` for more information.

                


            :type holdoff: hightime.timedelta, datetime.timedelta, or float in seconds
            :param delay:


                How long the digitizer waits after receiving the trigger to start
                acquiring data. Refer to :py:attr:`niscope.Session.trigger_delay_time` for more
                information.

                


            :type delay: hightime.timedelta, datetime.timedelta, or float in seconds

configure_trigger_immediate
---------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: configure_trigger_immediate()

            Configures common properties for immediate triggering. Immediate
            triggering means the digitizer triggers itself.

            When you initiate an acquisition, the digitizer waits for a trigger. You
            specify the type of trigger that the digitizer waits for with a
            Configure Trigger method, such as :py:meth:`niscope.Session.configure_trigger_immediate`.

            



configure_trigger_software
--------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: configure_trigger_software(holdoff=hightime.timedelta(seconds=0.0), delay=hightime.timedelta(seconds=0.0))

            Configures common properties for software triggering.

            When you initiate an acquisition, the digitizer waits for the start
            trigger, which is configured through the :py:attr:`niscope.Session.acq_arm_source`
            (Start Trigger Source) property. The default is immediate. Upon
            receiving the start trigger the digitizer begins sampling pretrigger
            points. After the digitizer finishes sampling pretrigger points, the
            digitizer waits for a reference (stop) trigger that you specify with a
            method such as this one. Upon receiving the reference trigger the
            digitizer finishes the acquisition after completing posttrigger
            sampling. With each Configure Trigger method, you specify
            configuration parameters such as the trigger source and the amount of
            trigger delay.

            To trigger the acquisition, use :py:meth:`niscope.Session.send_software_trigger_edge`.

            

            .. note:: Some features are not supported by all digitizers. Refer to `Features
                Supported by
                Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
                more information.



            :param holdoff:


                The length of time the digitizer waits after detecting a trigger before
                enabling NI-SCOPE to detect another trigger. Refer to
                :py:attr:`niscope.Session.trigger_holdoff` for more information.

                


            :type holdoff: hightime.timedelta, datetime.timedelta, or float in seconds
            :param delay:


                How long the digitizer waits after receiving the trigger to start
                acquiring data. Refer to :py:attr:`niscope.Session.trigger_delay_time` for more
                information.

                


            :type delay: hightime.timedelta, datetime.timedelta, or float in seconds

configure_trigger_video
-----------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: configure_trigger_video(trigger_source, signal_format, event, polarity, trigger_coupling, enable_dc_restore=False, line_number=1, holdoff=hightime.timedelta(seconds=0.0), delay=hightime.timedelta(seconds=0.0))

            Configures the common properties for video triggering, including the
            signal format, TV event, line number, polarity, and enable DC restore. A
            video trigger occurs when the digitizer finds a valid video signal sync.

            When you initiate an acquisition, the digitizer waits for the start
            trigger, which is configured through the :py:attr:`niscope.Session.acq_arm_source`
            (Start Trigger Source) property. The default is immediate. Upon
            receiving the start trigger the digitizer begins sampling pretrigger
            points. After the digitizer finishes sampling pretrigger points, the
            digitizer waits for a reference (stop) trigger that you specify with a
            method such as this one. Upon receiving the reference trigger the
            digitizer finishes the acquisition after completing posttrigger
            sampling. With each Configure Trigger method, you specify
            configuration parameters such as the trigger source and the amount of
            trigger delay.

            

            .. note:: Some features are not supported by all digitizers. Refer to `Features
                Supported by
                Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
                more information.



            :param trigger_source:


                Specifies the trigger source. Refer to :py:attr:`niscope.Session.trigger_source`
                for defined values.

                


            :type trigger_source: str
            :param signal_format:


                Specifies the type of video signal sync the digitizer should look for.
                Refer to :py:attr:`niscope.Session.tv_trigger_signal_format` for more
                information.

                


            :type signal_format: :py:data:`niscope.VideoSignalFormat`
            :param event:


                Specifies the TV event you want to trigger on. You can trigger on a
                specific or on the next coming line or field of the signal.

                


            :type event: :py:data:`niscope.VideoTriggerEvent`
            :param polarity:


                Specifies the polarity of the video signal sync.

                


            :type polarity: :py:data:`niscope.VideoPolarity`
            :param trigger_coupling:


                Applies coupling and filtering options to the trigger signal. Refer to
                :py:attr:`niscope.Session.trigger_coupling` for more information.

                


            :type trigger_coupling: :py:data:`niscope.TriggerCoupling`
            :param enable_dc_restore:


                Offsets each video line so the clamping level (the portion of the video
                line between the end of the color burst and the beginning of the active
                image) is moved to zero volt. Refer to
                :py:attr:`niscope.Session.enable_dc_restore` for defined values.

                


            :type enable_dc_restore: bool
            :param line_number:


                Selects the line number to trigger on. The line number range covers an
                entire frame and is referenced as shown on `Vertical Blanking and
                Synchronization
                Signal <REPLACE_DRIVER_SPECIFIC_URL_1(gray_scale_image)>`__. Refer to
                :py:attr:`niscope.Session.tv_trigger_line_number` for more information.

                Default value: 1

                


            :type line_number: int
            :param holdoff:


                The length of time the digitizer waits after detecting a trigger before
                enabling NI-SCOPE to detect another trigger. Refer to
                :py:attr:`niscope.Session.trigger_holdoff` for more information.

                


            :type holdoff: hightime.timedelta, datetime.timedelta, or float in seconds
            :param delay:


                How long the digitizer waits after receiving the trigger to start
                acquiring data. Refer to :py:attr:`niscope.Session.trigger_delay_time` for more
                information.

                


            :type delay: hightime.timedelta, datetime.timedelta, or float in seconds

configure_trigger_window
------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: configure_trigger_window(trigger_source, low_level, high_level, window_mode, trigger_coupling, holdoff=hightime.timedelta(seconds=0.0), delay=hightime.timedelta(seconds=0.0))

            Configures common properties for analog window triggering. A window
            trigger occurs when a signal enters or leaves a window you specify with
            the **high level** or **low level** parameters.

            When you initiate an acquisition, the digitizer waits for the start
            trigger, which is configured through the :py:attr:`niscope.Session.acq_arm_source`
            (Start Trigger Source) property. The default is immediate. Upon
            receiving the start trigger the digitizer begins sampling pretrigger
            points. After the digitizer finishes sampling pretrigger points, the
            digitizer waits for a reference (stop) trigger that you specify with a
            method such as this one. Upon receiving the reference trigger the
            digitizer finishes the acquisition after completing posttrigger
            sampling. With each Configure Trigger method, you specify
            configuration parameters such as the trigger source and the amount of
            trigger delay.

            To trigger the acquisition, use :py:meth:`niscope.Session.send_software_trigger_edge`.

            

            .. note:: Some features are not supported by all digitizers.



            :param trigger_source:


                Specifies the trigger source. Refer to :py:attr:`niscope.Session.trigger_source`
                for defined values.

                


            :type trigger_source: str
            :param low_level:


                Passes the voltage threshold you want the digitizer to use for low
                triggering.

                


            :type low_level: float
            :param high_level:


                Passes the voltage threshold you want the digitizer to use for high
                triggering.

                


            :type high_level: float
            :param window_mode:


                Specifies whether you want the trigger to occur when the signal enters
                or leaves a window.

                


            :type window_mode: :py:data:`niscope.TriggerWindowMode`
            :param trigger_coupling:


                Applies coupling and filtering options to the trigger signal. Refer to
                :py:attr:`niscope.Session.trigger_coupling` for more information.

                


            :type trigger_coupling: :py:data:`niscope.TriggerCoupling`
            :param holdoff:


                The length of time the digitizer waits after detecting a trigger before
                enabling NI-SCOPE to detect another trigger. Refer to
                :py:attr:`niscope.Session.trigger_holdoff` for more information.

                


            :type holdoff: hightime.timedelta, datetime.timedelta, or float in seconds
            :param delay:


                How long the digitizer waits after receiving the trigger to start
                acquiring data. Refer to :py:attr:`niscope.Session.trigger_delay_time` for more
                information.

                


            :type delay: hightime.timedelta, datetime.timedelta, or float in seconds

configure_vertical
------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: configure_vertical(range, coupling, offset=0.0, probe_attenuation=1.0, enabled=True)

            Configures the most commonly configured properties of the digitizer
            vertical subsystem, such as the range, offset, coupling, probe
            attenuation, and the channel.

            


            .. tip:: This method can be called on specific channels within your :py:class:`niscope.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].configure_vertical`

                To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

                Example: :py:meth:`my_session.configure_vertical`


            :param range:


                Specifies the vertical range Refer to :py:attr:`niscope.Session.vertical_range` for
                more information.

                


            :type range: float
            :param coupling:


                Specifies how to couple the input signal. Refer to
                :py:attr:`niscope.Session.vertical_coupling` for more information.

                


            :type coupling: :py:data:`niscope.VerticalCoupling`
            :param offset:


                Specifies the vertical offset. Refer to :py:attr:`niscope.Session.vertical_offset`
                for more information.

                


            :type offset: float
            :param probe_attenuation:


                Specifies the probe attenuation. Refer to
                :py:attr:`niscope.Session.probe_attenuation` for valid values.

                


            :type probe_attenuation: float
            :param enabled:


                Specifies whether the channel is enabled for acquisition. Refer to
                :py:attr:`niscope.Session.channel_enabled` for more information.

                


            :type enabled: bool

disable
-------

    .. py:currentmodule:: niscope.Session

    .. py:method:: disable()

            Aborts any current operation, opens data channel relays, and releases
            RTSI and PFI lines.

            



export_attribute_configuration_buffer
-------------------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: export_attribute_configuration_buffer()

            Exports the property configuration of the session to a configuration
            buffer.

            You can export and import session property configurations only between
            devices with identical model numbers, channel counts, and onboard memory
            sizes.

            This method verifies that the properties you have configured for the
            session are valid. If the configuration is invalid, NI‑SCOPE returns an
            error.

            **Related Topics:**

            `Properties and Property
            Methods <REPLACE_DRIVER_SPECIFIC_URL_1(attributes_and_attribute_functions)>`__

            `Setting Properties Before Reading
            Properties <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

            



            :rtype: bytes
            :return:


                    Specifies the byte array buffer to be populated with the exported
                    property configuration.

                    



export_attribute_configuration_file
-----------------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: export_attribute_configuration_file(file_path)

            Exports the property configuration of the session to the specified
            file.

            You can export and import session property configurations only between
            devices with identical model numbers, channel counts, and onboard memory
            sizes.

            This method verifies that the properties you have configured for the
            session are valid. If the configuration is invalid, NI‑SCOPE returns an
            error.

            **Related Topics:**

            `Properties and Property
            Methods <REPLACE_DRIVER_SPECIFIC_URL_1(attributes_and_attribute_functions)>`__

            `Setting Properties Before Reading
            Properties <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

            



            :param file_path:


                Specifies the absolute path to the file to contain the exported
                property configuration. If you specify an empty or relative path, this
                method returns an error.
                **Default file extension:** .niscopeconfig

                


            :type file_path: str

fetch
-----

    .. py:currentmodule:: niscope.Session

    .. py:method:: fetch(num_samples=None, relative_to=niscope.FetchRelativeTo.PRETRIGGER, offset=0, record_number=0, num_records=None, timeout=hightime.timedelta(seconds=5.0))

            Returns the waveform from a previously initiated acquisition that the
            digitizer acquires for the specified channel. This method returns
            scaled voltage waveforms.

            This method may return multiple waveforms depending on the number of
            channels, the acquisition type, and the number of records you specify.

            

            .. note:: Some functionality, such as time stamping, is not supported in all digitizers.


            .. tip:: This method can be called on specific channels within your :py:class:`niscope.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].fetch`

                To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

                Example: :py:meth:`my_session.fetch`


            :param num_samples:


                The maximum number of samples to fetch for each waveform. If the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. If it fails to complete within the timeout period, the method raises.

                


            :type num_samples: int
            :param relative_to:


                Position to start fetching within one record.

                


            :type relative_to: :py:data:`niscope.FetchRelativeTo`
            :param offset:


                Offset in samples to start fetching data within each record. The offset can be positive or negative.

                


            :type offset: int
            :param record_number:


                Zero-based index of the first record to fetch.

                


            :type record_number: int
            :param num_records:


                Number of records to fetch. Use -1 to fetch all configured records.

                


            :type num_records: int
            :param timeout:


                The time to wait for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 seconds for this parameter implies infinite timeout.

                


            :type timeout: hightime.timedelta, datetime.timedelta, or float in seconds

            :rtype: list of WaveformInfo
            :return:


                    Returns a list of class instances with the following timing and scaling information about each waveform:

                    -  **relative_initial_x** (float) the time (in seconds) from the trigger to the first sample in the fetched waveform
                    -  **absolute_initial_x** (float) timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output.
                    -  **x_increment** (float) the time between points in the acquired waveform in seconds
                    -  **channel** (str) channel name this waveform was acquired from
                    -  **record** (int) record number of this waveform
                    -  **gain** (float) the gain factor of the given channel; useful for scaling binary data with the following formula:

                        .. math::

                            voltage = binary data * gain factor + offset

                    -  **offset** (float) the offset factor of the given channel; useful for scaling binary data with the following formula:

                        .. math::

                            voltage = binary data * gain factor + offset

                    - **samples** (array of float) floating point array of samples. Length will be of the actual samples acquired

                    



fetch_array_measurement
-----------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: fetch_array_measurement(array_meas_function, meas_wfm_size=None, relative_to=niscope.FetchRelativeTo.PRETRIGGER, offset=0, record_number=0, num_records=None, meas_num_samples=None, timeout=hightime.timedelta(seconds=5.0))

            Obtains a waveform from the digitizer and returns the specified
            measurement array. This method may return multiple waveforms depending
            on the number of channels, the acquisition type, and the number of
            records you specify.

            

            .. note:: Some functionality, such as time stamping, is not supported in all
                digitizers.


            .. tip:: This method can be called on specific channels within your :py:class:`niscope.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].fetch_array_measurement`

                To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

                Example: :py:meth:`my_session.fetch_array_measurement`


            :param array_meas_function:


                The array measurement to perform.

                


            :type array_meas_function: :py:data:`niscope.ArrayMeasurement`
            :param meas_wfm_size:


                The maximum number of samples returned in the measurement waveform array
                for each waveform measurement. Default Value: None (returns all available samples).

                


            :type meas_wfm_size: int
            :param relative_to:


                Position to start fetching within one record.

                


            :type relative_to: :py:data:`niscope.FetchRelativeTo`
            :param offset:


                Offset in samples to start fetching data within each record. The offset can be positive or negative.

                


            :type offset: int
            :param record_number:


                Zero-based index of the first record to fetch.

                


            :type record_number: int
            :param num_records:


                Number of records to fetch. Use `None` to fetch all configured records.

                


            :type num_records: int
            :param meas_num_samples:


                Number of samples to fetch when performing a measurement. Use `None` to fetch the actual record length.

                


            :type meas_num_samples: int
            :param timeout:


                The time to wait in seconds for data to be acquired; using 0 for this
                parameter tells NI-SCOPE to fetch whatever is currently available. Using
                -1 for this parameter implies infinite timeout.

                


            :type timeout: hightime.timedelta, datetime.timedelta, or float in seconds

            :rtype: list of WaveformInfo
            :return:


                    Returns a list of class instances with the following timing and scaling
                    information about each waveform:

                    -  **relativeInitialX**—the time (in seconds) from the trigger to the
                       first sample in the fetched waveform
                    -  **absoluteInitialX**—timestamp (in seconds) of the first fetched
                       sample. This timestamp is comparable between records and
                       acquisitions; devices that do not support this parameter use 0 for
                       this output.
                    -  **xIncrement**—the time between points in the acquired waveform in
                       seconds
                    -  **channel**-channel name this waveform was acquired from
                    -  **record**-record number of this waveform
                    -  **gain**—the gain factor of the given channel; useful for scaling
                       binary data with the following formula:

                    voltage = binary data × gain factor + offset

                    -  **offset**—the offset factor of the given channel; useful for scaling
                       binary data with the following formula:

                    voltage = binary data × gain factor + offset

                    -  **samples**-floating point array of samples. Length will be of actual samples acquired.

                    



fetch_into
----------

    .. py:currentmodule:: niscope.Session

    .. py:method:: fetch_into(waveform, relative_to=niscope.FetchRelativeTo.PRETRIGGER, offset=0, record_number=0, num_records=None, timeout=hightime.timedelta(seconds=5.0))

            Returns the waveform from a previously initiated acquisition that the
            digitizer acquires for the specified channel. This method returns
            scaled voltage waveforms.

            This method may return multiple waveforms depending on the number of
            channels, the acquisition type, and the number of records you specify.

            

            .. note:: Some functionality, such as time stamping, is not supported in all digitizers.


            .. tip:: This method can be called on specific channels within your :py:class:`niscope.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].fetch`

                To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

                Example: :py:meth:`my_session.fetch`


            :param waveform:


                numpy array of the appropriate type and size that should be acquired as a 1D array. Size should be **num_samples** times number of waveforms. Call :py:meth:`niscope.Session._actual_num_wfms` to determine the number of waveforms.

                Types supported are

                - `numpy.float64`
                - `numpy.int8`
                - `numpy.in16`
                - `numpy.int32`

                Example:

                .. code-block:: python

                    waveform = numpy.ndarray(num_samples * session.actual_num_wfms(), dtype=numpy.float64)
                    wfm_info = session['0,1'].fetch_into(waveform, timeout=5.0)

                


            :type waveform: array.array("d")
            :param relative_to:


                Position to start fetching within one record.

                


            :type relative_to: :py:data:`niscope.FetchRelativeTo`
            :param offset:


                Offset in samples to start fetching data within each record.The offset can be positive or negative.

                


            :type offset: int
            :param record_number:


                Zero-based index of the first record to fetch.

                


            :type record_number: int
            :param num_records:


                Number of records to fetch. Use -1 to fetch all configured records.

                


            :type num_records: int
            :param timeout:


                The time to wait in seconds for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout.

                


            :type timeout: hightime.timedelta, datetime.timedelta, or float in seconds

            :rtype: list of WaveformInfo
            :return:


                    Returns a list of class instances with the following timing and scaling information about each waveform:

                    -  **relative_initial_x** (float) the time (in seconds) from the trigger to the first sample in the fetched waveform
                    -  **absolute_initial_x** (float) timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output.
                    -  **x_increment** (float) the time between points in the acquired waveform in seconds
                    -  **channel** (str) channel name this waveform was acquired from
                    -  **record** (int) record number of this waveform
                    -  **gain** (float) the gain factor of the given channel; useful for scaling binary data with the following formula:

                        .. math::

                            voltage = binary data * gain factor + offset

                    -  **offset** (float) the offset factor of the given channel; useful for scaling binary data with the following formula:

                        .. math::

                            voltage = binary data * gain factor + offset

                    - **samples** (array of float) floating point array of samples. Length will be of the actual samples acquired

                    



fetch_measurement_stats
-----------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: fetch_measurement_stats(scalar_meas_function, relative_to=niscope.FetchRelativeTo.PRETRIGGER, offset=0, record_number=0, num_records=None, timeout=hightime.timedelta(seconds=5.0))

            Obtains a waveform measurement and returns the measurement value. This
            method may return multiple statistical results depending on the number
            of channels, the acquisition type, and the number of records you
            specify.

            You specify a particular measurement type, such as rise time, frequency,
            or voltage peak-to-peak. The waveform on which the digitizer calculates
            the waveform measurement is from an acquisition that you previously
            initiated. The statistics for the specified measurement method are
            returned, where the statistics are updated once every acquisition when
            the specified measurement is fetched by any of the Fetch Measurement
            methods. If a Fetch Measurement method has not been called, this
            method fetches the data on which to perform the measurement. The
            statistics are cleared by calling
            :py:meth:`niscope.Session.clear_waveform_measurement_stats`.

            Many of the measurements use the low, mid, and high reference levels.
            You configure the low, mid, and high references with
            :py:attr:`niscope.Session.meas_chan_low_ref_level`,
            :py:attr:`niscope.Session.meas_chan_mid_ref_level`, and
            :py:attr:`niscope.Session.meas_chan_high_ref_level` to set each channel
            differently.

            


            .. tip:: This method can be called on specific channels within your :py:class:`niscope.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].fetch_measurement_stats`

                To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

                Example: :py:meth:`my_session.fetch_measurement_stats`


            :param scalar_meas_function:


                The scalar measurement to be performed on each fetched waveform.

                


            :type scalar_meas_function: :py:data:`niscope.ScalarMeasurement`
            :param relative_to:


                Position to start fetching within one record.

                


            :type relative_to: :py:data:`niscope.FetchRelativeTo`
            :param offset:


                Offset in samples to start fetching data within each record. The offset can be positive or negative.

                


            :type offset: int
            :param record_number:


                Zero-based index of the first record to fetch.

                


            :type record_number: int
            :param num_records:


                Number of records to fetch. Use `None` to fetch all configured records.

                


            :type num_records: int
            :param timeout:


                The time to wait in seconds for data to be acquired; using 0 for this
                parameter tells NI-SCOPE to fetch whatever is currently available. Using
                -1 for this parameter implies infinite timeout.

                


            :type timeout: hightime.timedelta, datetime.timedelta, or float in seconds

            :rtype: list of MeasurementStats
            :return:


                    Returns a list of class instances with the following measurement statistics
                    about the specified measurement:

                    -	**result** (float): the resulting measurement
                    -	**mean** (float): the mean scalar value, which is obtained by
                    averaging each fetch_measurement_stats call
                    -	**stdev** (float): the standard deviations of the most recent
                    **numInStats** measurements
                    -	**min_val** (float): the smallest scalar value acquired (the minimum
                    of the **numInStats** measurements)
                    -	**max_val** (float): the largest scalar value acquired (the maximum
                    of the **numInStats** measurements)
                    -	**num_in_stats** (int): the number of times fetch_measurement_stats has been called
                    -	**channel** (str): channel name this result was acquired from
                    -	**record** (int): record number of this result

                    



get_channel_names
-----------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: get_channel_names(indices)

            Returns a list of channel names for given channel indices.

            



            :param indices:


                Index list for the channels in the session. Valid values are from zero to the total number of channels in the session minus one. The index string can be one of the following formats:

                -   A comma-separated list—for example, "0,2,3,1"
                -   A range using a hyphen—for example, "0-3"
                -   A range using a colon—for example, "0:3 "

                You can combine comma-separated lists and ranges that use a hyphen or colon. Both out-of-order and repeated indices are supported ("2,3,0", "1,2,2,3"). White space characters, including spaces, tabs, feeds, and carriage returns, are allowed between characters. Ranges can be incrementing or decrementing.

                


            :type indices: basic sequence types, str, or int

            :rtype: list of str
            :return:


                    The channel name(s) at the specified indices.

                    



get_equalization_filter_coefficients
------------------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: get_equalization_filter_coefficients()

            Retrieves the custom coefficients for the equalization FIR filter on the device. This filter is designed to compensate the input signal for artifacts introduced to the signal outside of the digitizer. Because this filter is a generic FIR filter, any coefficients are valid. Coefficient values should be between +1 and –1.

            


            .. tip:: This method can be called on specific channels within your :py:class:`niscope.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].get_equalization_filter_coefficients`

                To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

                Example: :py:meth:`my_session.get_equalization_filter_coefficients`


get_ext_cal_last_date_and_time
------------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: get_ext_cal_last_date_and_time()

            Returns the date and time of the last external calibration performed.

            



            :rtype: hightime.timedelta, datetime.timedelta, or float in seconds
            :return:


                    Indicates the **date** of the last calibration. A hightime.datetime object is returned, but only contains resolution to the day.

                    



get_ext_cal_last_temp
---------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: get_ext_cal_last_temp()

            Returns the onboard temperature, in degrees Celsius, of an oscilloscope at the time of the last successful external calibration.
            The temperature returned by this node is an onboard temperature read from a sensor on the surface of the oscilloscope. This temperature should not be confused with the environmental temperature of the oscilloscope surroundings. During operation, the onboard temperature is normally higher than the environmental temperature.
            Temperature-sensitive parameters are calibrated during self-calibration. Therefore, the self-calibration temperature is usually more important to read than the external calibration temperature.

            



            :rtype: float
            :return:


                    Returns the **temperature** in degrees Celsius during the last calibration.

                    



get_self_cal_last_date_and_time
-------------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: get_self_cal_last_date_and_time()

            Returns the date and time of the last self calibration performed.

            



            :rtype: hightime.timedelta, datetime.timedelta, or float in seconds
            :return:


                    Indicates the **date** of the last calibration. A hightime.datetime object is returned, but only contains resolution to the day.

                    



get_self_cal_last_temp
----------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: get_self_cal_last_temp()

            Returns the onboard temperature, in degrees Celsius, of an oscilloscope at the time of the last successful self calibration.
            The temperature returned by this node is an onboard temperature read from a sensor on the surface of the oscilloscope. This temperature should not be confused with the environmental temperature of the oscilloscope surroundings. During operation, the onboard temperature is normally higher than the environmental temperature.
            Temperature-sensitive parameters are calibrated during self-calibration. Therefore, the self-calibration temperature is usually more important to read than the external calibration temperature.

            



            :rtype: float
            :return:


                    Returns the **temperature** in degrees Celsius during the last calibration.

                    



import_attribute_configuration_buffer
-------------------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: import_attribute_configuration_buffer(configuration)

            Imports a property configuration to the session from the specified
            configuration buffer.

            You can export and import session property configurations only between
            devices with identical model numbers, channel counts, and onboard memory
            sizes.

            **Related Topics:**

            `Properties and Property
            Methods <REPLACE_DRIVER_SPECIFIC_URL_1(attributes_and_attribute_functions)>`__

            `Setting Properties Before Reading
            Properties <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

            

            .. note:: You cannot call this method while the session is in a running state,
                such as while acquiring a signal.



            :param configuration:


                Specifies the byte array buffer that contains the property
                configuration to import.

                


            :type configuration: bytes

import_attribute_configuration_file
-----------------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: import_attribute_configuration_file(file_path)

            Imports a property configuration to the session from the specified
            file.

            You can export and import session property configurations only between
            devices with identical model numbers, channel counts, and onboard memory
            sizes.

            **Related Topics:**

            `Properties and Property
            Methods <REPLACE_DRIVER_SPECIFIC_URL_1(attributes_and_attribute_functions)>`__

            `Setting Properties Before Reading
            Properties <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

            

            .. note:: You cannot call this method while the session is in a running state,
                such as while acquiring a signal.



            :param file_path:


                Specifies the absolute path to the file containing the property
                configuration to import. If you specify an empty or relative path, this
                method returns an error.
                **Default File Extension:** .niscopeconfig

                


            :type file_path: str

initiate
--------

    .. py:currentmodule:: niscope.Session

    .. py:method:: initiate()

            Initiates a waveform acquisition.

            After calling this method, the digitizer leaves the Idle state and
            waits for a trigger. The digitizer acquires a waveform for each channel
            you enable with :py:meth:`niscope.Session.configure_vertical`.

            

            .. note:: This method will return a Python context manager that will initiate on entering and abort on exit.



lock
----

    .. py:currentmodule:: niscope.Session

.. py:method:: lock()

    Obtains a multithread lock on the device session. Before doing so, the
    software waits until all other execution threads release their locks
    on the device session.

    Other threads may have obtained a lock on this session for the
    following reasons:

        -  The application called the :py:meth:`niscope.Session.lock` method.
        -  A call to NI-SCOPE locked the session.
        -  After a call to the :py:meth:`niscope.Session.lock` method returns
           successfully, no other threads can access the device session until
           you call the :py:meth:`niscope.Session.unlock` method or exit out of the with block when using
           lock context manager.
        -  Use the :py:meth:`niscope.Session.lock` method and the
           :py:meth:`niscope.Session.unlock` method around a sequence of calls to
           instrument driver methods if you require that the device retain its
           settings through the end of the sequence.

    You can safely make nested calls to the :py:meth:`niscope.Session.lock` method
    within the same thread. To completely unlock the session, you must
    balance each call to the :py:meth:`niscope.Session.lock` method with a call to
    the :py:meth:`niscope.Session.unlock` method.

    One method for ensuring there are the same number of unlock method calls as there is lock calls
    is to use lock as a context manager

        .. code:: python

            with niscope.Session('dev1') as session:
                with session.lock():
                    # Calls to session within a single lock context

        The first `with` block ensures the session is closed regardless of any exceptions raised

        The second `with` block ensures that unlock is called regardless of any exceptions raised

    :rtype: context manager
    :return:
        When used in a `with` statement, :py:meth:`niscope.Session.lock` acts as
        a context manager and unlock will be called when the `with` block is exited

probe_compensation_signal_start
-------------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: probe_compensation_signal_start()

            Starts the 1 kHz square wave output on PFI 1 for probe compensation.

            



probe_compensation_signal_stop
------------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: probe_compensation_signal_stop()

            Stops the 1 kHz square wave output on PFI 1 for probe compensation.

            



read
----

    .. py:currentmodule:: niscope.Session

    .. py:method:: read(num_samples=None, relative_to=niscope.FetchRelativeTo.PRETRIGGER, offset=0, record_number=0, num_records=None, timeout=hightime.timedelta(seconds=5.0))

            Initiates an acquisition, waits for it to complete, and retrieves the
            data. The process is similar to calling :py:meth:`niscope.Session._initiate_acquisition`,
            :py:meth:`niscope.Session.acquisition_status`, and :py:meth:`niscope.Session.fetch`. The only difference is
            that with :py:meth:`niscope.Session.read`, you enable all channels specified with
            **channelList** before the acquisition; in the other method, you enable
            the channels with :py:meth:`niscope.Session.configure_vertical`.

            This method may return multiple waveforms depending on the number of
            channels, the acquisition type, and the number of records you specify.

            

            .. note:: Some functionality, such as time stamping, is not supported in all digitizers.


            .. tip:: This method can be called on specific channels within your :py:class:`niscope.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].read`

                To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

                Example: :py:meth:`my_session.read`


            :param num_samples:


                The maximum number of samples to fetch for each waveform. If the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. If it fails to complete within the timeout period, the method raises.

                


            :type num_samples: int
            :param relative_to:


                Position to start fetching within one record.

                


            :type relative_to: :py:data:`niscope.FetchRelativeTo`
            :param offset:


                Offset in samples to start fetching data within each record. The offset can be positive or negative.

                


            :type offset: int
            :param record_number:


                Zero-based index of the first record to fetch.

                


            :type record_number: int
            :param num_records:


                Number of records to fetch. Use -1 to fetch all configured records.

                


            :type num_records: int
            :param timeout:


                The time to wait for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 seconds for this parameter implies infinite timeout.

                


            :type timeout: hightime.timedelta, datetime.timedelta, or float in seconds

            :rtype: list of WaveformInfo
            :return:


                    Returns a list of class instances with the following timing and scaling information about each waveform:

                    -  **relative_initial_x** (float) the time (in seconds) from the trigger to the first sample in the fetched waveform
                    -  **absolute_initial_x** (float) timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output.
                    -  **x_increment** (float) the time between points in the acquired waveform in seconds
                    -  **channel** (str) channel name this waveform was acquired from
                    -  **record** (int) record number of this waveform
                    -  **gain** (float) the gain factor of the given channel; useful for scaling binary data with the following formula:

                        .. math::

                            voltage = binary data * gain factor + offset

                    -  **offset** (float) the offset factor of the given channel; useful for scaling binary data with the following formula:

                        .. math::

                            voltage = binary data * gain factor + offset

                    - **samples** (array of float) floating point array of samples. Length will be of the actual samples acquired

                    



reset
-----

    .. py:currentmodule:: niscope.Session

    .. py:method:: reset()

            Stops the acquisition, releases routes, and all session properties are
            reset to their `default
            states <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cviattribute_defaults)>`__.

            



reset_device
------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: reset_device()

            Performs a hard reset of the device. Acquisition stops, all routes are
            released, RTSI and PFI lines are tristated, hardware is configured to
            its default state, and all session properties are reset to their default
            state.

            -  `Thermal Shutdown <digitizers.chm::/Thermal_Shutdown.html>`__

            



reset_with_defaults
-------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: reset_with_defaults()

            Performs a software reset of the device, returning it to the default
            state and applying any initial default settings from the IVI
            Configuration Store.

            



self_cal
--------

    .. py:currentmodule:: niscope.Session

    .. py:method:: self_cal(option=niscope.Option.SELF_CALIBRATE_ALL_CHANNELS)

            Self-calibrates most NI digitizers, including all SMC-based devices and
            most Traditional NI-DAQ (Legacy) devices. To verify that your digitizer
            supports self-calibration, refer to `Features Supported by
            Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__.

            For SMC-based digitizers, if the self-calibration is performed
            successfully in a regular session, the calibration constants are
            immediately stored in the self-calibration area of the EEPROM. If the
            self-calibration is performed in an external calibration session, the
            calibration constants take effect immediately for the duration of the
            session. However, they are not stored in the EEPROM until
            :py:meth:`niscope.Session.CalEnd` is called with **action** set to
            :py:data:`~niscope.NISCOPE_VAL_ACTION_STORE` and no errors occur.

            

            .. note:: One or more of the referenced methods are not in the Python API for this driver.

            .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            .. tip:: This method can be called on specific channels within your :py:class:`niscope.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].self_cal`

                To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

                Example: :py:meth:`my_session.self_cal`


            :param option:


                The calibration option. Use VI_NULL for a normal self-calibration
                operation or :py:data:`~niscope.NISCOPE_VAL_CAL_RESTORE_EXTERNAL_CALIBRATION` to
                restore the previous calibration.

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type option: :py:data:`niscope.Option`

self_test
---------

    .. py:currentmodule:: niscope.Session

    .. py:method:: self_test()

            Runs the instrument self-test routine and returns the test result(s). Refer to the
            device-specific help topics for an explanation of the message contents.

            Raises `SelfTestError` on self test failure. Properties on exception object:

            - code - failure code from driver
            - message - status message from driver

            +----------------+------------------+
            | Self-Test Code | Description      |
            +================+==================+
            | 0              | Passed self-test |
            +----------------+------------------+
            | 1              | Self-test failed |
            +----------------+------------------+



send_software_trigger_edge
--------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: send_software_trigger_edge(which_trigger)

            Sends the selected trigger to the digitizer. Call this method if you
            called :py:meth:`niscope.Session.configure_trigger_software` when you want the Reference
            trigger to occur. You can also call this method to override a misused
            edge, digital, or hysteresis trigger. If you have configured
            :py:attr:`niscope.Session.acq_arm_source`, :py:attr:`niscope.Session.arm_ref_trig_src`, or
            :py:attr:`niscope.Session.adv_trig_src`, call this method when you want to send
            the corresponding trigger to the digitizer.

            



            :param which_trigger:


                Specifies the type of trigger to send to the digitizer.

                **Defined Values**

                | :py:data:`~niscope.WhichTrigger.START` (0L)
                |  :py:data:`~niscope.WhichTrigger.ARM_REFERENCE` (1L)
                | :py:data:`~niscope.WhichTrigger.REFERENCE` (2L)
                | :py:data:`~niscope.WhichTrigger.ADVANCE` (3L)

                


            :type which_trigger: :py:data:`niscope.WhichTrigger`

unlock
------

    .. py:currentmodule:: niscope.Session

.. py:method:: unlock()

    Releases a lock that you acquired on an device session using
    :py:meth:`niscope.Session.lock`. Refer to :py:meth:`niscope.Session.unlock` for additional
    information on session locks.


Properties
==========

absolute_sample_clock_offset
----------------------------

    .. py:attribute:: absolute_sample_clock_offset

        Gets or sets the absolute time offset of the sample clock relative to
        the reference clock in terms of seconds.



        .. note:: Configures the sample clock relationship with respect to the reference
            clock. This parameter is factored into NI-TClk adjustments and is
            typically used to improve the repeatability of NI-TClk Synchronization.
            When this parameter is read, the currently programmed value is returned.
            The range of the absolute sample clock offset is [-.5 sample clock
            periods, .5 sample clock periods]. The default absolute sample clock
            offset is 0s.

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------------------------------+
            | Characteristic        | Value                                                       |
            +=======================+=============================================================+
            | Datatype              | hightime.timedelta, datetime.timedelta, or float in seconds |
            +-----------------------+-------------------------------------------------------------+
            | Permissions           | read-write                                                  |
            +-----------------------+-------------------------------------------------------------+
            | Repeated Capabilities | None                                                        |
            +-----------------------+-------------------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocking:Advanced:Absolute Sample Clock Offset**
                - C Attribute: **NISCOPE_ATTR_ABSOLUTE_SAMPLE_CLOCK_OFFSET**

acquisition_start_time
----------------------

    .. py:attribute:: acquisition_start_time

        Specifies the length of time from the trigger event to the first point in the waveform record in seconds.  If the value is positive, the first point in the waveform record occurs after the trigger event (same as specifying :py:attr:`niscope.Session.trigger_delay_time`).  If the value is negative, the first point in the waveform record occurs before the trigger event (same as specifying :py:attr:`niscope.Session.horz_record_ref_position`).

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------------------------------+
            | Characteristic        | Value                                                       |
            +=======================+=============================================================+
            | Datatype              | hightime.timedelta, datetime.timedelta, or float in seconds |
            +-----------------------+-------------------------------------------------------------+
            | Permissions           | read-write                                                  |
            +-----------------------+-------------------------------------------------------------+
            | Repeated Capabilities | None                                                        |
            +-----------------------+-------------------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Horizontal:Advanced:Acquisition Start Time**
                - C Attribute: **NISCOPE_ATTR_ACQUISITION_START_TIME**

acquisition_type
----------------

    .. py:attribute:: acquisition_type

        Specifies how the digitizer acquires data and fills the waveform record.

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------+
            | Characteristic        | Value                 |
            +=======================+=======================+
            | Datatype              | enums.AcquisitionType |
            +-----------------------+-----------------------+
            | Permissions           | read-write            |
            +-----------------------+-----------------------+
            | Repeated Capabilities | None                  |
            +-----------------------+-----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Acquisition Type**
                - C Attribute: **NISCOPE_ATTR_ACQUISITION_TYPE**

acq_arm_source
--------------

    .. py:attribute:: acq_arm_source

        Specifies the source the digitizer monitors for a start (acquisition arm) trigger.  When the start trigger is received, the digitizer begins acquiring pretrigger samples.
        Valid Values:
        :py:data:`~niscope.NISCOPE_VAL_IMMEDIATE`     ('VAL_IMMEDIATE')    - Triggers immediately
        :py:data:`~niscope.NISCOPE_VAL_RTSI_0`        ('VAL_RTSI_0')       - RTSI 0
        :py:data:`~niscope.NISCOPE_VAL_RTSI_1`        ('VAL_RTSI_1')       - RTSI 1
        :py:data:`~niscope.NISCOPE_VAL_RTSI_2`        ('VAL_RTSI_2')       - RTSI 2
        :py:data:`~niscope.NISCOPE_VAL_RTSI_3`        ('VAL_RTSI_3')       - RTSI 3
        :py:data:`~niscope.NISCOPE_VAL_RTSI_4`        ('VAL_RTSI_4')       - RTSI 4
        :py:data:`~niscope.NISCOPE_VAL_RTSI_5`        ('VAL_RTSI_5')       - RTSI 5
        :py:data:`~niscope.NISCOPE_VAL_RTSI_6`        ('VAL_RTSI_6')       - RTSI 6
        :py:data:`~niscope.NISCOPE_VAL_PFI_0`         ('VAL_PFI_0')        - PFI 0
        :py:data:`~niscope.NISCOPE_VAL_PFI_1`         ('VAL_PFI_1')        - PFI 1
        :py:data:`~niscope.NISCOPE_VAL_PFI_2`         ('VAL_PFI_2')        - PFI 2
        :py:data:`~niscope.NISCOPE_VAL_PXI_STAR`      ('VAL_PXI_STAR')     - PXI Star Trigger



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Synchronization:Start Trigger (Acq. Arm):Source**
                - C Attribute: **NISCOPE_ATTR_ACQ_ARM_SOURCE**

advance_trigger_terminal_name
-----------------------------

    .. py:attribute:: advance_trigger_terminal_name

        Returns the fully qualified name for the Advance Trigger terminal.  You can use this terminal as the source for another trigger.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Synchronization:Advance Trigger:Terminal Name**
                - C Attribute: **NISCOPE_ATTR_ADVANCE_TRIGGER_TERMINAL_NAME**

adv_trig_src
------------

    .. py:attribute:: adv_trig_src

        Specifies the source the digitizer monitors for an advance trigger.  When the advance trigger is received, the digitizer begins acquiring pretrigger samples.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Synchronization:Advance Trigger:Source**
                - C Attribute: **NISCOPE_ATTR_ADV_TRIG_SRC**

allow_more_records_than_memory
------------------------------

    .. py:attribute:: allow_more_records_than_memory

        Indicates whether more records can be configured with :py:meth:`niscope.Session.configure_horizontal_timing` than fit in the onboard memory. If this property is set to True, it is necessary to fetch records while the acquisition is in progress.  Eventually, some of the records will be overwritten.  An error is returned from the fetch method if you attempt to fetch a record that has been overwritten.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Horizontal:Enable Records > Memory**
                - C Attribute: **NISCOPE_ATTR_ALLOW_MORE_RECORDS_THAN_MEMORY**

arm_ref_trig_src
----------------

    .. py:attribute:: arm_ref_trig_src

        Specifies the source the digitizer monitors for an arm reference trigger.  When the arm reference trigger is received, the digitizer begins looking for a reference (stop) trigger from the user-configured trigger source.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Synchronization:Arm Reference Trigger:Source**
                - C Attribute: **NISCOPE_ATTR_ARM_REF_TRIG_SRC**

backlog
-------

    .. py:attribute:: backlog

        Returns the number of samples (:py:attr:`niscope.Session.points_done`) that have been acquired but not fetched for the record specified by :py:attr:`niscope.Session.fetch_record_number`.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Fetch:Fetch Backlog**
                - C Attribute: **NISCOPE_ATTR_BACKLOG**

bandpass_filter_enabled
-----------------------

    .. py:attribute:: bandpass_filter_enabled

        Enables the bandpass filter on the specificed channel.  The default value is FALSE.




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].bandpass_filter_enabled`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.bandpass_filter_enabled`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Advanced:Bandpass Filter Enabled**
                - C Attribute: **NISCOPE_ATTR_BANDPASS_FILTER_ENABLED**

binary_sample_width
-------------------

    .. py:attribute:: binary_sample_width

        Indicates the bit width of the binary data in the acquired waveform.  Useful for determining which Binary Fetch method to use. Compare to :py:attr:`niscope.Session.resolution`.
        To configure the device to store samples with a lower resolution that the native, set this property to the desired binary width.
        This can be useful for streaming at faster speeds at the cost of resolution. The least significant bits will be lost with this configuration.
        Valid Values: 8, 16, 32

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Binary Sample Width**
                - C Attribute: **NISCOPE_ATTR_BINARY_SAMPLE_WIDTH**

cable_sense_mode
----------------

    .. py:attribute:: cable_sense_mode

        Specifies whether and how the oscilloscope is configured to generate a CableSense signal on the specified channels when the :py:meth:`niscope.Session.CableSenseSignalStart` method is called.

        Device-Specific Behavior:
            PXIe-5160/5162
                - The value of this property must be identical across all channels whose input impedance is set to 50 ohms.
                - If this property is set to a value other than :py:data:`~niscope.CableSenseMode.DISABLED` for any channel(s), the input impedance of all channels for which this property is set to :py:data:`~niscope.CableSenseMode.DISABLED` must be set to 1 M Ohm.

        +-----------------------+
        | **Supported Devices** |
        +-----------------------+
        | PXIe-5110             |
        +-----------------------+
        | PXIe-5111             |
        +-----------------------+
        | PXIe-5113             |
        +-----------------------+
        | PXIe-5160             |
        +-----------------------+
        | PXIe-5162             |
        +-----------------------+

        .. note:: the input impedance of the channel(s) to convey the CableSense signal must be set to 50 ohms.

        .. note:: One or more of the referenced methods are not in the Python API for this driver.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------+
            | Characteristic        | Value                |
            +=======================+======================+
            | Datatype              | enums.CableSenseMode |
            +-----------------------+----------------------+
            | Permissions           | read-write           |
            +-----------------------+----------------------+
            | Repeated Capabilities | None                 |
            +-----------------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_CABLE_SENSE_MODE**

cable_sense_signal_enable
-------------------------

    .. py:attribute:: cable_sense_signal_enable

        TBD

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_CABLE_SENSE_SIGNAL_ENABLE**

cable_sense_voltage
-------------------

    .. py:attribute:: cable_sense_voltage

        Returns the voltage of the CableSense signal that is written to the EEPROM of the oscilloscope during factory calibration.

        +-----------------------+
        | **Supported Devices** |
        +-----------------------+
        | PXIe-5110             |
        +-----------------------+
        | PXIe-5111             |
        +-----------------------+
        | PXIe-5113             |
        +-----------------------+
        | PXIe-5160             |
        +-----------------------+
        | PXIe-5162             |
        +-----------------------+

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_CABLE_SENSE_VOLTAGE**

channel_count
-------------

    .. py:attribute:: channel_count

        Indicates the number of channels that the specific instrument driver supports.
        For channel-based properties, the IVI engine maintains a separate cache value for each channel.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Capabilities:Channel Count**
                - C Attribute: **NISCOPE_ATTR_CHANNEL_COUNT**

channel_enabled
---------------

    .. py:attribute:: channel_enabled

        Specifies whether the digitizer acquires a waveform for the channel.
        Valid Values:
        True  (1) - Acquire data on this channel
        False (0) - Don't acquire data on this channel




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].channel_enabled`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.channel_enabled`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Channel Enabled**
                - C Attribute: **NISCOPE_ATTR_CHANNEL_ENABLED**

channel_terminal_configuration
------------------------------

    .. py:attribute:: channel_terminal_configuration

        Specifies the terminal configuration for the channel.




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].channel_terminal_configuration`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.channel_terminal_configuration`

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------------+
            | Characteristic        | Value                       |
            +=======================+=============================+
            | Datatype              | enums.TerminalConfiguration |
            +-----------------------+-----------------------------+
            | Permissions           | read-write                  |
            +-----------------------+-----------------------------+
            | Repeated Capabilities | channels                    |
            +-----------------------+-----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Channel Terminal Configuration**
                - C Attribute: **NISCOPE_ATTR_CHANNEL_TERMINAL_CONFIGURATION**

data_transfer_block_size
------------------------

    .. py:attribute:: data_transfer_block_size

        Specifies the maximum number of samples to transfer at one time from the device to host memory. Increasing this number should result in better fetching performance because the driver does not need to restart the transfers as often. However, increasing this number may also increase the amount of page-locked memory required from the system.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Fetch:Data Transfer Block Size**
                - C Attribute: **NISCOPE_ATTR_DATA_TRANSFER_BLOCK_SIZE**

data_transfer_maximum_bandwidth
-------------------------------

    .. py:attribute:: data_transfer_maximum_bandwidth

        This property specifies the maximum bandwidth that the device is allowed to consume.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Fetch:Advanced:Maximum Bandwidth**
                - C Attribute: **NISCOPE_ATTR_DATA_TRANSFER_MAXIMUM_BANDWIDTH**

data_transfer_preferred_packet_size
-----------------------------------

    .. py:attribute:: data_transfer_preferred_packet_size

        This property specifies the size of (read request|memory write) data payload. Due to alignment of the data buffers, the hardware may not always generate a packet of this size.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Fetch:Advanced:Preferred Packet Size**
                - C Attribute: **NISCOPE_ATTR_DATA_TRANSFER_PREFERRED_PACKET_SIZE**

device_temperature
------------------

    .. py:attribute:: device_temperature

        Returns the temperature of the device in degrees Celsius from the onboard sensor.




        .. tip:: This property can be set/get on specific instruments within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container instruments to specify a subset.

            Example: :py:attr:`my_session.instruments[ ... ].device_temperature`

            To set/get on all instruments, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.device_temperature`

        The following table lists the characteristics of this property.

            +-----------------------+-------------+
            | Characteristic        | Value       |
            +=======================+=============+
            | Datatype              | float       |
            +-----------------------+-------------+
            | Permissions           | read only   |
            +-----------------------+-------------+
            | Repeated Capabilities | instruments |
            +-----------------------+-------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device:Temperature**
                - C Attribute: **NISCOPE_ATTR_DEVICE_TEMPERATURE**

enabled_channels
----------------

    .. py:attribute:: enabled_channels

        Returns a comma-separated list of the channels enabled for the session in ascending order.

        If no channels are enabled, this property returns an empty string, "".
        If all channels are enabled, this property enumerates all of the channels.

        Because this property returns channels in ascending order, but the order in which you specify channels for the input is important, the value of this property may not necessarily reflect the order in which NI-SCOPE performs certain actions.

        Refer to Channel String Syntax in the NI High-Speed Digitizers Help for more information on the effects of channel order in NI-SCOPE.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_ENABLED_CHANNELS**

enable_dc_restore
-----------------

    .. py:attribute:: enable_dc_restore

        Restores the video-triggered data retrieved by the digitizer to the video signal's zero reference point.
        Valid Values:
        True - Enable DC restore
        False - Disable DC restore

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Video:Enable DC Restore**
                - C Attribute: **NISCOPE_ATTR_ENABLE_DC_RESTORE**

enable_time_interleaved_sampling
--------------------------------

    .. py:attribute:: enable_time_interleaved_sampling

        Specifies whether the digitizer acquires the waveform using multiple ADCs for the channel enabling a higher maximum real-time sampling rate.
        Valid Values:
        True  (1) - Use multiple interleaved ADCs on this channel
        False (0) - Use only this channel's ADC to acquire data for this channel




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].enable_time_interleaved_sampling`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.enable_time_interleaved_sampling`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Horizontal:Enable Time Interleaved Sampling**
                - C Attribute: **NISCOPE_ATTR_ENABLE_TIME_INTERLEAVED_SAMPLING**

end_of_acquisition_event_output_terminal
----------------------------------------

    .. py:attribute:: end_of_acquisition_event_output_terminal

        Specifies the destination for the End of Acquisition Event.    When this event is asserted, the digitizer has completed sampling for all records.
        Consult your device documentation for a specific list of valid destinations.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Synchronization:End of Acquisition:Output Terminal**
                - C Attribute: **NISCOPE_ATTR_END_OF_ACQUISITION_EVENT_OUTPUT_TERMINAL**

end_of_acquisition_event_terminal_name
--------------------------------------

    .. py:attribute:: end_of_acquisition_event_terminal_name

        Returns the fully qualified name for the End of Acquisition Event terminal.    You can use this terminal as the source for a trigger.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Synchronization:End of Acquisition:Terminal Name**
                - C Attribute: **NISCOPE_ATTR_END_OF_ACQUISITION_EVENT_TERMINAL_NAME**

end_of_record_event_output_terminal
-----------------------------------

    .. py:attribute:: end_of_record_event_output_terminal

        Specifies the destination for the End of Record Event.    When this event is asserted, the digitizer has completed sampling for the current record.
        Consult your device documentation for a specific list of valid destinations.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Synchronization:End of Record:Output Terminal**
                - C Attribute: **NISCOPE_ATTR_END_OF_RECORD_EVENT_OUTPUT_TERMINAL**

end_of_record_event_terminal_name
---------------------------------

    .. py:attribute:: end_of_record_event_terminal_name

        Returns the fully qualified name for the End of Record Event terminal.    You can use this terminal as the source for a trigger.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Synchronization:End of Record:Terminal Name**
                - C Attribute: **NISCOPE_ATTR_END_OF_RECORD_EVENT_TERMINAL_NAME**

end_of_record_to_advance_trigger_holdoff
----------------------------------------

    .. py:attribute:: end_of_record_to_advance_trigger_holdoff

        End of Record to Advance Trigger Holdoff is the length of time (in
        seconds) that a device waits between the completion of one record and
        the acquisition of pre-trigger samples for the next record. During this
        time, the acquisition engine state delays the transition to the Wait for
        Advance Trigger state, and will not store samples in onboard memory,
        accept an Advance Trigger, or trigger on the input signal..
        **Supported Devices**: NI 5185/5186

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------------------------------+
            | Characteristic        | Value                                                       |
            +=======================+=============================================================+
            | Datatype              | hightime.timedelta, datetime.timedelta, or float in seconds |
            +-----------------------+-------------------------------------------------------------+
            | Permissions           | read-write                                                  |
            +-----------------------+-------------------------------------------------------------+
            | Repeated Capabilities | None                                                        |
            +-----------------------+-------------------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:End of Record to Advance Trigger Holdoff**
                - C Attribute: **NISCOPE_ATTR_END_OF_RECORD_TO_ADVANCE_TRIGGER_HOLDOFF**

equalization_filter_enabled
---------------------------

    .. py:attribute:: equalization_filter_enabled

        Enables the onboard signal processing FIR block. This block is connected directly to the input signal.  This filter is designed to compensate the input signal for artifacts introduced to the signal outside of the digitizer. However, since this is a generic FIR filter any coefficients are valid.  Coefficients should be between +1 and -1 in value.




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].equalization_filter_enabled`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.equalization_filter_enabled`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Onboard Signal Processing:Equalization:Equalization Filter Enabled**
                - C Attribute: **NISCOPE_ATTR_EQUALIZATION_FILTER_ENABLED**

equalization_num_coefficients
-----------------------------

    .. py:attribute:: equalization_num_coefficients

        Returns the number of coefficients that the FIR filter can accept.  This filter is designed to compensate the input signal for artifacts introduced to the signal outside of the digitizer.  However, since this is a generic FIR filter any coefficients are valid.  Coefficients should be between +1 and -1 in value.




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].equalization_num_coefficients`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.equalization_num_coefficients`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | channels  |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Onboard Signal Processing:Equalization:Equalization Num Coefficients**
                - C Attribute: **NISCOPE_ATTR_EQUALIZATION_NUM_COEFFICIENTS**

exported_advance_trigger_output_terminal
----------------------------------------

    .. py:attribute:: exported_advance_trigger_output_terminal

        Specifies the destination to export the advance trigger.  When the advance trigger is received, the digitizer begins acquiring samples for the Nth record.
        Consult your device documentation for a specific list of valid destinations.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Synchronization:Advance Trigger:Output Terminal**
                - C Attribute: **NISCOPE_ATTR_EXPORTED_ADVANCE_TRIGGER_OUTPUT_TERMINAL**

exported_ref_trigger_output_terminal
------------------------------------

    .. py:attribute:: exported_ref_trigger_output_terminal

        Specifies the destination export for the reference (stop) trigger.
        Consult your device documentation for a specific list of valid destinations.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Output Terminal**
                - C Attribute: **NISCOPE_ATTR_EXPORTED_REF_TRIGGER_OUTPUT_TERMINAL**

exported_start_trigger_output_terminal
--------------------------------------

    .. py:attribute:: exported_start_trigger_output_terminal

        Specifies the destination to export the Start trigger.  When the start trigger is received, the digitizer begins acquiring samples.
        Consult your device documentation for a specific list of valid destinations.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Synchronization:Start Trigger (Acq. Arm):Output Terminal**
                - C Attribute: **NISCOPE_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL**

flex_fir_antialias_filter_type
------------------------------

    .. py:attribute:: flex_fir_antialias_filter_type

        The NI 5922 flexible-resolution digitizer uses an onboard FIR lowpass antialias filter.
        Use this property to select from several types of filters to achieve desired filtering characteristics.




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].flex_fir_antialias_filter_type`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.flex_fir_antialias_filter_type`

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------------+
            | Characteristic        | Value                            |
            +=======================+==================================+
            | Datatype              | enums.FlexFIRAntialiasFilterType |
            +-----------------------+----------------------------------+
            | Permissions           | read-write                       |
            +-----------------------+----------------------------------+
            | Repeated Capabilities | channels                         |
            +-----------------------+----------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Advanced:Flex FIR Antialias Filter Type**
                - C Attribute: **NISCOPE_ATTR_FLEX_FIR_ANTIALIAS_FILTER_TYPE**

fpga_bitfile_path
-----------------

    .. py:attribute:: fpga_bitfile_path

        Gets the absolute file path to the bitfile loaded on the FPGA.



        .. note:: Gets the absolute file path to the bitfile loaded on the FPGA.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device:FPGA Bitfile Path**
                - C Attribute: **NISCOPE_ATTR_FPGA_BITFILE_PATH**

glitch_condition
----------------

    .. py:attribute:: glitch_condition

        Specifies whether the oscilloscope triggers on pulses of duration less than or greater than the value specified by the :py:attr:`niscope.Session.glitch_width` property.

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------+
            | Characteristic        | Value                 |
            +=======================+=======================+
            | Datatype              | enums.GlitchCondition |
            +-----------------------+-----------------------+
            | Permissions           | read-write            |
            +-----------------------+-----------------------+
            | Repeated Capabilities | None                  |
            +-----------------------+-----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_GLITCH_CONDITION**

glitch_polarity
---------------

    .. py:attribute:: glitch_polarity

        Specifies the polarity of pulses that trigger the oscilloscope for glitch triggering.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------+
            | Characteristic        | Value                |
            +=======================+======================+
            | Datatype              | enums.GlitchPolarity |
            +-----------------------+----------------------+
            | Permissions           | read-write           |
            +-----------------------+----------------------+
            | Repeated Capabilities | None                 |
            +-----------------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_GLITCH_POLARITY**

glitch_width
------------

    .. py:attribute:: glitch_width

        Specifies the glitch duration, in seconds.

        The oscilloscope triggers when it detects of pulse of duration either less than or greater than this value depending on the value of the :py:attr:`niscope.Session.glitch_condition` property.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_GLITCH_WIDTH**

high_pass_filter_frequency
--------------------------

    .. py:attribute:: high_pass_filter_frequency

        Specifies the frequency for the highpass filter in Hz. The device uses
        one of the valid values listed below. If an invalid value is specified,
        no coercion occurs. The default value is 0.
        **(PXIe-5164) Valid Values:**
        0 90 450
        **Related topics:**
        `Digital Filtering <digitizers.chm::/Digital_Filtering_Overview.html>`__




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].high_pass_filter_frequency`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.high_pass_filter_frequency`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Advanced:High Pass Filter Frequency**
                - C Attribute: **NISCOPE_ATTR_HIGH_PASS_FILTER_FREQUENCY**

horz_enforce_realtime
---------------------

    .. py:attribute:: horz_enforce_realtime

        Indicates whether the digitizer enforces real-time measurements or allows equivalent-time measurements.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Horizontal:Enforce Realtime**
                - C Attribute: **NISCOPE_ATTR_HORZ_ENFORCE_REALTIME**

horz_min_num_pts
----------------

    .. py:attribute:: horz_min_num_pts

        Specifies the minimum number of points you require in the waveform record for each channel.  NI-SCOPE uses the value you specify to configure the record length that the digitizer uses for waveform acquisition. :py:attr:`niscope.Session.horz_record_length` returns the actual record length.
        Valid Values: 1 - available onboard memory

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Horizontal:Min Number of Points**
                - C Attribute: **NISCOPE_ATTR_HORZ_MIN_NUM_PTS**

horz_num_records
----------------

    .. py:attribute:: horz_num_records

        Specifies the number of records to acquire. Can be used for multi-record acquisition and single-record acquisitions. Setting this to 1 indicates a single-record acquisition.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Horizontal:Number of Records**
                - C Attribute: **NISCOPE_ATTR_HORZ_NUM_RECORDS**

horz_record_length
------------------

    .. py:attribute:: horz_record_length

        Returns the actual number of points the digitizer acquires for each channel.  The value is equal to or greater than the minimum number of points you specify with :py:attr:`niscope.Session.horz_min_num_pts`.
        Allocate a ViReal64 array of this size or greater to pass as the WaveformArray parameter of the Read and Fetch methods. This property is only valid after a call to the one of the Configure Horizontal methods.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Horizontal:Actual Record Length**
                - C Attribute: **NISCOPE_ATTR_HORZ_RECORD_LENGTH**

horz_record_ref_position
------------------------

    .. py:attribute:: horz_record_ref_position

        Specifies the position of the Reference Event in the waveform record.  When the digitizer detects a trigger, it waits the length of time the :py:attr:`niscope.Session.trigger_delay_time` property specifies. The event that occurs when the delay time elapses is the Reference Event. The Reference Event is relative to the start of the record and is a percentage of the record length. For example, the value 50.0 corresponds to the center of the waveform record and 0.0 corresponds to the first element in the waveform record.
        Valid Values: 0.0 - 100.0

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Horizontal:Reference Position**
                - C Attribute: **NISCOPE_ATTR_HORZ_RECORD_REF_POSITION**

horz_sample_rate
----------------

    .. py:attribute:: horz_sample_rate

        Returns the effective sample rate using the current configuration. The units are samples per second.  This property is only valid after a call to the one of the Configure Horizontal methods.
        Units: Hertz (Samples / Second)

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Horizontal:Actual Sample Rate**
                - C Attribute: **NISCOPE_ATTR_HORZ_SAMPLE_RATE**

horz_time_per_record
--------------------

    .. py:attribute:: horz_time_per_record

        Specifies the length of time that corresponds to the record length.
        Units: Seconds

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------------------------------+
            | Characteristic        | Value                                                       |
            +=======================+=============================================================+
            | Datatype              | hightime.timedelta, datetime.timedelta, or float in seconds |
            +-----------------------+-------------------------------------------------------------+
            | Permissions           | read-write                                                  |
            +-----------------------+-------------------------------------------------------------+
            | Repeated Capabilities | None                                                        |
            +-----------------------+-------------------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Horizontal:Advanced:Time Per Record**
                - C Attribute: **NISCOPE_ATTR_HORZ_TIME_PER_RECORD**

input_clock_source
------------------

    .. py:attribute:: input_clock_source

        Specifies the input source for the PLL reference clock (the 1 MHz to 20 MHz clock on the NI 5122, the 10 MHz clock for the NI 5112/5620/5621/5911) to which the digitizer will be phase-locked; for the NI 5102, this is the source of the board clock.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocking:Reference (Input) Clock Source**
                - C Attribute: **NISCOPE_ATTR_INPUT_CLOCK_SOURCE**

input_impedance
---------------

    .. py:attribute:: input_impedance

        Specifies the input impedance for the channel in Ohms.




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].input_impedance`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.input_impedance`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Input Impedance**
                - C Attribute: **NISCOPE_ATTR_INPUT_IMPEDANCE**

instrument_firmware_revision
----------------------------

    .. py:attribute:: instrument_firmware_revision

        A string that contains the firmware revision information for the instrument you are currently using.




        .. tip:: This property can be set/get on specific instruments within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container instruments to specify a subset.

            Example: :py:attr:`my_session.instruments[ ... ].instrument_firmware_revision`

            To set/get on all instruments, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.instrument_firmware_revision`

        The following table lists the characteristics of this property.

            +-----------------------+-------------+
            | Characteristic        | Value       |
            +=======================+=============+
            | Datatype              | str         |
            +-----------------------+-------------+
            | Permissions           | read only   |
            +-----------------------+-------------+
            | Repeated Capabilities | instruments |
            +-----------------------+-------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Firmware Revision**
                - C Attribute: **NISCOPE_ATTR_INSTRUMENT_FIRMWARE_REVISION**

instrument_manufacturer
-----------------------

    .. py:attribute:: instrument_manufacturer

        A string that contains the name of the instrument manufacturer.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Manufacturer**
                - C Attribute: **NISCOPE_ATTR_INSTRUMENT_MANUFACTURER**

instrument_model
----------------

    .. py:attribute:: instrument_model

        A string that contains the model number of the current instrument.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Model**
                - C Attribute: **NISCOPE_ATTR_INSTRUMENT_MODEL**

interleaving_offset_correction_enabled
--------------------------------------

    .. py:attribute:: interleaving_offset_correction_enabled

        Enables the interleaving offset correction on the specified channel. The
        default value is TRUE.
        **Related topics:**
        `Timed Interleaved
        Sampling <digitizers.chm::/TimeInterleavedSampling.html>`__



        .. note:: If disabled, warranted specifications are not guaranteed.


        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].interleaving_offset_correction_enabled`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.interleaving_offset_correction_enabled`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Advanced:Interleaving Offset Correction Enabled**
                - C Attribute: **NISCOPE_ATTR_INTERLEAVING_OFFSET_CORRECTION_ENABLED**

io_resource_descriptor
----------------------

    .. py:attribute:: io_resource_descriptor

        Indicates the resource descriptor the driver uses to identify the physical device.  If you initialize the driver with a logical name, this property contains the resource descriptor that corresponds to the entry in the IVI Configuration utility.
        If you initialize the instrument driver with the resource descriptor, this property contains that value.You can pass a logical name to :py:meth:`niscope.Session.Init` or :py:meth:`niscope.Session.__init__`. The IVI Configuration utility must contain an entry for the logical name. The logical name entry refers to a virtual instrument section in the IVI Configuration file. The virtual instrument section specifies a physical device and initial user options.



        .. note:: One or more of the referenced methods are not in the Python API for this driver.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Advanced Session Information:Resource Descriptor**
                - C Attribute: **NISCOPE_ATTR_IO_RESOURCE_DESCRIPTOR**

is_probe_comp_on
----------------

    .. py:attribute:: is_probe_comp_on

        .. tip:: This property can be set/get on specific instruments within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container instruments to specify a subset.

            Example: :py:attr:`my_session.instruments[ ... ].is_probe_comp_on`

            To set/get on all instruments, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.is_probe_comp_on`

        The following table lists the characteristics of this property.

            +-----------------------+-------------+
            | Characteristic        | Value       |
            +=======================+=============+
            | Datatype              | bool        |
            +-----------------------+-------------+
            | Permissions           | read only   |
            +-----------------------+-------------+
            | Repeated Capabilities | instruments |
            +-----------------------+-------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_IS_PROBE_COMP_ON**

logical_name
------------

    .. py:attribute:: logical_name

        A string containing the logical name you specified when opening the current IVI session.  You can pass a logical name to :py:meth:`niscope.Session.Init` or :py:meth:`niscope.Session.__init__`. The IVI Configuration utility must contain an entry for the logical name. The logical name entry refers to a virtual instrument section in the IVI Configuration file. The virtual instrument section specifies a physical device and initial user options.



        .. note:: One or more of the referenced methods are not in the Python API for this driver.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Advanced Session Information:Logical Name**
                - C Attribute: **NISCOPE_ATTR_LOGICAL_NAME**

master_enable
-------------

    .. py:attribute:: master_enable

        Specifies whether you want the device to be a master or a slave. The master typically originates the trigger signal and clock sync pulse. For a standalone device, set this property to False.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Synchronization:Master Enable**
                - C Attribute: **NISCOPE_ATTR_MASTER_ENABLE**

max_input_frequency
-------------------

    .. py:attribute:: max_input_frequency

        Specifies the bandwidth of the channel. Express this value as the frequency at which the input circuitry attenuates the input signal by 3 dB. The units are hertz.
        Defined Values:
        :py:data:`~niscope.NISCOPE_VAL_BANDWIDTH_FULL` (-1.0)
        :py:data:`~niscope.NISCOPE_VAL_BANDWIDTH_DEVICE_DEFAULT` (0.0)
        :py:data:`~niscope.NISCOPE_VAL_20MHZ_BANDWIDTH` (20000000.0)
        :py:data:`~niscope.NISCOPE_VAL_100MHZ_BANDWIDTH` (100000000.0)
        :py:data:`~niscope.NISCOPE_VAL_20MHZ_MAX_INPUT_FREQUENCY` (20000000.0)
        :py:data:`~niscope.NISCOPE_VAL_100MHZ_MAX_INPUT_FREQUENCY` (100000000.0)



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].max_input_frequency`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.max_input_frequency`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Maximum Input Frequency**
                - C Attribute: **NISCOPE_ATTR_MAX_INPUT_FREQUENCY**

max_real_time_sampling_rate
---------------------------

    .. py:attribute:: max_real_time_sampling_rate

        Returns the maximum real time sample rate in Hz.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Horizontal:Maximum Real Time Sample Rate**
                - C Attribute: **NISCOPE_ATTR_MAX_REAL_TIME_SAMPLING_RATE**

max_ris_rate
------------

    .. py:attribute:: max_ris_rate

        Returns the maximum sample rate in RIS mode in Hz.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Horizontal:Maximum RIS Rate**
                - C Attribute: **NISCOPE_ATTR_MAX_RIS_RATE**

meas_array_gain
---------------

    .. py:attribute:: meas_array_gain

        Every element of an array is multiplied by this scalar value during the Array Gain measurement.  Refer to :py:data:`~niscope.ArrayMeasurement.ARRAY_GAIN` for more information.
        Default: 1.0




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].meas_array_gain`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.meas_array_gain`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Waveform Measurement:Array Gain**
                - C Attribute: **NISCOPE_ATTR_MEAS_ARRAY_GAIN**

meas_array_offset
-----------------

    .. py:attribute:: meas_array_offset

        Every element of an array is added to this scalar value during the Array Offset measurement. Refer to :py:data:`~niscope.ArrayMeasurement.ARRAY_OFFSET` for more information.
        Default: 0.0




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].meas_array_offset`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.meas_array_offset`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Waveform Measurement:Array Offset**
                - C Attribute: **NISCOPE_ATTR_MEAS_ARRAY_OFFSET**

meas_chan_high_ref_level
------------------------

    .. py:attribute:: meas_chan_high_ref_level

        Stores the high reference level used in many scalar measurements. Different channels may have different reference levels. Do not use the IVI-defined, nonchannel-based properties such as :py:attr:`niscope.Session.meas_high_ref` if you use this property to set various channels to different values.
        Default: 90%




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].meas_chan_high_ref_level`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.meas_chan_high_ref_level`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Waveform Measurement:Reference Levels:Channel Based High Ref Level**
                - C Attribute: **NISCOPE_ATTR_MEAS_CHAN_HIGH_REF_LEVEL**

meas_chan_low_ref_level
-----------------------

    .. py:attribute:: meas_chan_low_ref_level

        Stores the low reference level used in many scalar measurements. Different channels may have different reference levels. Do not use the IVI-defined, nonchannel-based properties such as :py:attr:`niscope.Session.meas_low_ref` if you use this property to set various channels to different values.
        Default: 10%




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].meas_chan_low_ref_level`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.meas_chan_low_ref_level`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Waveform Measurement:Reference Levels:Channel Based Low Ref Level**
                - C Attribute: **NISCOPE_ATTR_MEAS_CHAN_LOW_REF_LEVEL**

meas_chan_mid_ref_level
-----------------------

    .. py:attribute:: meas_chan_mid_ref_level

        Stores the mid reference level used in many scalar measurements. Different channels may have different reference levels. Do not use the IVI-defined, nonchannel-based properties such as :py:attr:`niscope.Session.meas_mid_ref` if you use this property to set various channels to different values.
        Default: 50%




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].meas_chan_mid_ref_level`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.meas_chan_mid_ref_level`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Waveform Measurement:Reference Levels:Channel Based Mid Ref Level**
                - C Attribute: **NISCOPE_ATTR_MEAS_CHAN_MID_REF_LEVEL**

meas_filter_center_freq
-----------------------

    .. py:attribute:: meas_filter_center_freq

        The center frequency in hertz for filters of type bandpass and bandstop. The width of the filter is specified by :py:attr:`niscope.Session.meas_filter_width`, where the cutoff frequencies are the center ± width.
        Default: 1.0e6 Hz




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].meas_filter_center_freq`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.meas_filter_center_freq`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Waveform Measurement:Filter:Center Frequency**
                - C Attribute: **NISCOPE_ATTR_MEAS_FILTER_CENTER_FREQ**

meas_filter_cutoff_freq
-----------------------

    .. py:attribute:: meas_filter_cutoff_freq

        Specifies the cutoff frequency in hertz for filters of type lowpass and highpass. The cutoff frequency definition varies depending on the filter.
        Default: 1.0e6 Hz




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].meas_filter_cutoff_freq`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.meas_filter_cutoff_freq`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Waveform Measurement:Filter:Cutoff Frequency**
                - C Attribute: **NISCOPE_ATTR_MEAS_FILTER_CUTOFF_FREQ**

meas_filter_order
-----------------

    .. py:attribute:: meas_filter_order

        Specifies the order of an IIR filter. All positive integers are valid.
        Default: 2




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].meas_filter_order`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.meas_filter_order`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Waveform Measurement:Filter:IIR Order**
                - C Attribute: **NISCOPE_ATTR_MEAS_FILTER_ORDER**

meas_filter_ripple
------------------

    .. py:attribute:: meas_filter_ripple

        Specifies the amount of ripple in the passband in units of decibels (positive values). Used only for Chebyshev filters. The more ripple allowed gives a sharper cutoff for a given filter order.
        Default: 0.1 dB




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].meas_filter_ripple`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.meas_filter_ripple`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Waveform Measurement:Filter:Ripple**
                - C Attribute: **NISCOPE_ATTR_MEAS_FILTER_RIPPLE**

meas_filter_taps
----------------

    .. py:attribute:: meas_filter_taps

        Defines the number of taps (coefficients) for an FIR filter.
        Default: 25




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].meas_filter_taps`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.meas_filter_taps`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Waveform Measurement:Filter:FIR Taps**
                - C Attribute: **NISCOPE_ATTR_MEAS_FILTER_TAPS**

meas_filter_transient_waveform_percent
--------------------------------------

    .. py:attribute:: meas_filter_transient_waveform_percent

        The percentage (0 - 100%) of the IIR filtered waveform to eliminate from the beginning of the waveform. This allows eliminating the transient portion of the waveform that is undefined due to the assumptions necessary at the boundary condition.
        Default: 20.0%




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].meas_filter_transient_waveform_percent`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.meas_filter_transient_waveform_percent`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Waveform Measurement:Filter:Percent Waveform Transient**
                - C Attribute: **NISCOPE_ATTR_MEAS_FILTER_TRANSIENT_WAVEFORM_PERCENT**

meas_filter_type
----------------

    .. py:attribute:: meas_filter_type

        Specifies the type of filter, for both IIR and FIR filters. The allowed values are the following:
        ·  :py:data:`~niscope.NISCOPE_VAL_MEAS_LOWPASS`
        ·  :py:data:`~niscope.NISCOPE_VAL_MEAS_HIGHPASS`
        ·  :py:data:`~niscope.NISCOPE_VAL_MEAS_BANDPASS`
        ·  :py:data:`~niscope.NISCOPE_VAL_MEAS_BANDSTOP`
        Default: :py:data:`~niscope.NISCOPE_VAL_MEAS_LOWPASS`



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].meas_filter_type`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.meas_filter_type`

        The following table lists the characteristics of this property.

            +-----------------------+------------------+
            | Characteristic        | Value            |
            +=======================+==================+
            | Datatype              | enums.FilterType |
            +-----------------------+------------------+
            | Permissions           | read-write       |
            +-----------------------+------------------+
            | Repeated Capabilities | channels         |
            +-----------------------+------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Waveform Measurement:Filter:Type**
                - C Attribute: **NISCOPE_ATTR_MEAS_FILTER_TYPE**

meas_filter_width
-----------------

    .. py:attribute:: meas_filter_width

        Specifies the width of bandpass and bandstop type filters in hertz. The cutoff frequencies occur at :py:attr:`niscope.Session.meas_filter_center_freq` ± one-half width.
        Default: 1.0e3 Hz




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].meas_filter_width`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.meas_filter_width`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Waveform Measurement:Filter:Width**
                - C Attribute: **NISCOPE_ATTR_MEAS_FILTER_WIDTH**

meas_fir_filter_window
----------------------

    .. py:attribute:: meas_fir_filter_window

        Specifies the FIR window type. The possible choices are:
        :py:data:`~niscope.FIRFilterWindow.NONE`
        :py:data:`~niscope.ArrayMeasurement.HANNING_WINDOW`
        :py:data:`~niscope.ArrayMeasurement.HAMMING_WINDOW`
        :py:data:`~niscope.ArrayMeasurement.TRIANGLE_WINDOW`
        :py:data:`~niscope.ArrayMeasurement.FLAT_TOP_WINDOW`
        :py:data:`~niscope.ArrayMeasurement.BLACKMAN_WINDOW`
        The symmetric windows are applied to the FIR filter coefficients to limit passband ripple in FIR filters.
        Default: :py:data:`~niscope.FIRFilterWindow.NONE`




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].meas_fir_filter_window`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.meas_fir_filter_window`

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------+
            | Characteristic        | Value                 |
            +=======================+=======================+
            | Datatype              | enums.FIRFilterWindow |
            +-----------------------+-----------------------+
            | Permissions           | read-write            |
            +-----------------------+-----------------------+
            | Repeated Capabilities | channels              |
            +-----------------------+-----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Waveform Measurement:Filter:FIR Window**
                - C Attribute: **NISCOPE_ATTR_MEAS_FIR_FILTER_WINDOW**

meas_high_ref
-------------

    .. py:attribute:: meas_high_ref

        

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_MEAS_HIGH_REF**

meas_hysteresis_percent
-----------------------

    .. py:attribute:: meas_hysteresis_percent

        Digital hysteresis that is used in several of the scalar waveform measurements. This property specifies the percentage of the full-scale vertical range for the hysteresis window size.
        Default: 2%




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].meas_hysteresis_percent`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.meas_hysteresis_percent`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Waveform Measurement:Hysteresis Percent**
                - C Attribute: **NISCOPE_ATTR_MEAS_HYSTERESIS_PERCENT**

meas_interpolation_sampling_factor
----------------------------------

    .. py:attribute:: meas_interpolation_sampling_factor

        The new number of points for polynomial interpolation is the sampling factor times the input number of points. For example, if you acquire 1,000 points with the digitizer and set this property to 2.5, calling :py:meth:`niscope.Session.FetchWaveformMeasurementArray` with the :py:data:`~niscope.ArrayMeasurement.POLYNOMIAL_INTERPOLATION` measurement resamples the waveform to 2,500 points.
        Default: 2.0



        .. note:: One or more of the referenced methods are not in the Python API for this driver.


        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].meas_interpolation_sampling_factor`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.meas_interpolation_sampling_factor`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Waveform Measurement:Interpolation:Sampling Factor**
                - C Attribute: **NISCOPE_ATTR_MEAS_INTERPOLATION_SAMPLING_FACTOR**

meas_last_acq_histogram_size
----------------------------

    .. py:attribute:: meas_last_acq_histogram_size

        Specifies the size (that is, the number of bins) in the last acquisition histogram. This histogram is used to determine several scalar measurements, most importantly voltage low and voltage high.
        Default: 256




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].meas_last_acq_histogram_size`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.meas_last_acq_histogram_size`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Waveform Measurement:Last Acq. Histogram Size**
                - C Attribute: **NISCOPE_ATTR_MEAS_LAST_ACQ_HISTOGRAM_SIZE**

meas_low_ref
------------

    .. py:attribute:: meas_low_ref

        

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_MEAS_LOW_REF**

meas_mid_ref
------------

    .. py:attribute:: meas_mid_ref

        

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_MEAS_MID_REF**

meas_other_channel
------------------

    .. py:attribute:: meas_other_channel

        Specifies the second channel for two-channel measurements, such as :py:data:`~niscope.ArrayMeasurement.ADD_CHANNELS`. If processing steps are registered with this channel, the processing is done before the waveform is used in a two-channel measurement.
        Default: '0'




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].meas_other_channel`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.meas_other_channel`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str or int |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Waveform Measurement:Other Channel**
                - C Attribute: **NISCOPE_ATTR_MEAS_OTHER_CHANNEL**

meas_percentage_method
----------------------

    .. py:attribute:: meas_percentage_method

        Specifies the method used to map percentage reference units to voltages for the reference. Possible values are:
        :py:data:`~niscope.NISCOPE_VAL_MEAS_LOW_HIGH`
        :py:data:`~niscope.NISCOPE_VAL_MEAS_MIN_MAX`
        :py:data:`~niscope.NISCOPE_VAL_MEAS_BASE_TOP`
        Default: :py:data:`~niscope.NISCOPE_VAL_MEAS_BASE_TOP`



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].meas_percentage_method`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.meas_percentage_method`

        The following table lists the characteristics of this property.

            +-----------------------+------------------------+
            | Characteristic        | Value                  |
            +=======================+========================+
            | Datatype              | enums.PercentageMethod |
            +-----------------------+------------------------+
            | Permissions           | read-write             |
            +-----------------------+------------------------+
            | Repeated Capabilities | channels               |
            +-----------------------+------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Waveform Measurement:Reference Levels:Percentage Units Method**
                - C Attribute: **NISCOPE_ATTR_MEAS_PERCENTAGE_METHOD**

meas_polynomial_interpolation_order
-----------------------------------

    .. py:attribute:: meas_polynomial_interpolation_order

        Specifies the polynomial order used for the polynomial interpolation measurement. For example, an order of 1 is linear interpolation whereas an order of 2 specifies parabolic interpolation. Any positive integer is valid.
        Default: 1




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].meas_polynomial_interpolation_order`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.meas_polynomial_interpolation_order`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Waveform Measurement:Interpolation:Polynomial Interpolation Order**
                - C Attribute: **NISCOPE_ATTR_MEAS_POLYNOMIAL_INTERPOLATION_ORDER**

meas_ref_level_units
--------------------

    .. py:attribute:: meas_ref_level_units

        Specifies the units of the reference levels.
        :py:data:`~niscope.NISCOPE_VAL_MEAS_VOLTAGE`--Specifies that the reference levels are given in units of volts
        :py:data:`~niscope.NISCOPE_VAL_MEAS_PERCENTAGE`--Percentage units, where the measurements voltage low and voltage high represent 0% and 100%, respectively.
        Default: :py:data:`~niscope.NISCOPE_VAL_MEAS_PERCENTAGE`



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].meas_ref_level_units`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.meas_ref_level_units`

        The following table lists the characteristics of this property.

            +-----------------------+---------------------+
            | Characteristic        | Value               |
            +=======================+=====================+
            | Datatype              | enums.RefLevelUnits |
            +-----------------------+---------------------+
            | Permissions           | read-write          |
            +-----------------------+---------------------+
            | Repeated Capabilities | channels            |
            +-----------------------+---------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Waveform Measurement:Reference Levels:Units**
                - C Attribute: **NISCOPE_ATTR_MEAS_REF_LEVEL_UNITS**

meas_time_histogram_high_time
-----------------------------

    .. py:attribute:: meas_time_histogram_high_time

        Specifies the highest time value included in the multiple acquisition time histogram. The units are always seconds.
        Default: 5.0e-4 seconds




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].meas_time_histogram_high_time`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.meas_time_histogram_high_time`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------------------------------+
            | Characteristic        | Value                                                       |
            +=======================+=============================================================+
            | Datatype              | hightime.timedelta, datetime.timedelta, or float in seconds |
            +-----------------------+-------------------------------------------------------------+
            | Permissions           | read-write                                                  |
            +-----------------------+-------------------------------------------------------------+
            | Repeated Capabilities | channels                                                    |
            +-----------------------+-------------------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Waveform Measurement:Time Histogram:High Time**
                - C Attribute: **NISCOPE_ATTR_MEAS_TIME_HISTOGRAM_HIGH_TIME**

meas_time_histogram_high_volts
------------------------------

    .. py:attribute:: meas_time_histogram_high_volts

        Specifies the highest voltage value included in the multiple-acquisition time histogram. The units are always volts.
        Default: 10.0 V




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].meas_time_histogram_high_volts`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.meas_time_histogram_high_volts`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Waveform Measurement:Time Histogram:High Volts**
                - C Attribute: **NISCOPE_ATTR_MEAS_TIME_HISTOGRAM_HIGH_VOLTS**

meas_time_histogram_low_time
----------------------------

    .. py:attribute:: meas_time_histogram_low_time

        Specifies the lowest time value included in the multiple-acquisition time histogram. The units are always seconds.
        Default: -5.0e-4 seconds




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].meas_time_histogram_low_time`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.meas_time_histogram_low_time`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------------------------------+
            | Characteristic        | Value                                                       |
            +=======================+=============================================================+
            | Datatype              | hightime.timedelta, datetime.timedelta, or float in seconds |
            +-----------------------+-------------------------------------------------------------+
            | Permissions           | read-write                                                  |
            +-----------------------+-------------------------------------------------------------+
            | Repeated Capabilities | channels                                                    |
            +-----------------------+-------------------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Waveform Measurement:Time Histogram:Low Time**
                - C Attribute: **NISCOPE_ATTR_MEAS_TIME_HISTOGRAM_LOW_TIME**

meas_time_histogram_low_volts
-----------------------------

    .. py:attribute:: meas_time_histogram_low_volts

        Specifies the lowest voltage value included in the multiple acquisition time histogram. The units are always volts.
        Default: -10.0 V




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].meas_time_histogram_low_volts`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.meas_time_histogram_low_volts`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Waveform Measurement:Time Histogram:Low Volts**
                - C Attribute: **NISCOPE_ATTR_MEAS_TIME_HISTOGRAM_LOW_VOLTS**

meas_time_histogram_size
------------------------

    .. py:attribute:: meas_time_histogram_size

        Determines the multiple acquisition voltage histogram size. The size is set during the first call to a time histogram measurement after clearing the measurement history with :py:meth:`niscope.Session.clear_waveform_measurement_stats`.
        Default: 256




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].meas_time_histogram_size`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.meas_time_histogram_size`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Waveform Measurement:Time Histogram:Size**
                - C Attribute: **NISCOPE_ATTR_MEAS_TIME_HISTOGRAM_SIZE**

meas_voltage_histogram_high_volts
---------------------------------

    .. py:attribute:: meas_voltage_histogram_high_volts

        Specifies the highest voltage value included in the multiple acquisition voltage histogram. The units are always volts.
        Default: 10.0 V




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].meas_voltage_histogram_high_volts`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.meas_voltage_histogram_high_volts`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Waveform Measurement:Voltage Histogram:High Volts**
                - C Attribute: **NISCOPE_ATTR_MEAS_VOLTAGE_HISTOGRAM_HIGH_VOLTS**

meas_voltage_histogram_low_volts
--------------------------------

    .. py:attribute:: meas_voltage_histogram_low_volts

        Specifies the lowest voltage value included in the multiple-acquisition voltage histogram. The units are always volts.
        Default: -10.0 V




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].meas_voltage_histogram_low_volts`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.meas_voltage_histogram_low_volts`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Waveform Measurement:Voltage Histogram:Low Volts**
                - C Attribute: **NISCOPE_ATTR_MEAS_VOLTAGE_HISTOGRAM_LOW_VOLTS**

meas_voltage_histogram_size
---------------------------

    .. py:attribute:: meas_voltage_histogram_size

        Determines the multiple acquisition voltage histogram size. The size is set the first time a voltage histogram measurement is called after clearing the measurement history with the method :py:meth:`niscope.Session.clear_waveform_measurement_stats`.
        Default: 256




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].meas_voltage_histogram_size`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.meas_voltage_histogram_size`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Waveform Measurement:Voltage Histogram:Size**
                - C Attribute: **NISCOPE_ATTR_MEAS_VOLTAGE_HISTOGRAM_SIZE**

min_sample_rate
---------------

    .. py:attribute:: min_sample_rate

        Specify the sampling rate for the acquisition in Samples per second.
        Valid Values:
        The combination of sampling rate and min record length must allow the digitizer to sample at a valid sampling rate for the acquisition type specified in :py:meth:`niscope.Session.ConfigureAcquisition` and not require more memory than the onboard memory module allows.



        .. note:: One or more of the referenced methods are not in the Python API for this driver.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Horizontal:Min Sample Rate**
                - C Attribute: **NISCOPE_ATTR_MIN_SAMPLE_RATE**

onboard_memory_size
-------------------

    .. py:attribute:: onboard_memory_size

        Returns the total combined amount of onboard memory for all channels in bytes.




        .. tip:: This property can be set/get on specific instruments within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container instruments to specify a subset.

            Example: :py:attr:`my_session.instruments[ ... ].onboard_memory_size`

            To set/get on all instruments, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.onboard_memory_size`

        The following table lists the characteristics of this property.

            +-----------------------+-------------+
            | Characteristic        | Value       |
            +=======================+=============+
            | Datatype              | int         |
            +-----------------------+-------------+
            | Permissions           | read only   |
            +-----------------------+-------------+
            | Repeated Capabilities | instruments |
            +-----------------------+-------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Horizontal:Memory Size**
                - C Attribute: **NISCOPE_ATTR_ONBOARD_MEMORY_SIZE**

output_clock_source
-------------------

    .. py:attribute:: output_clock_source

        Specifies the output source for the 10 MHz clock to which another digitizer's sample clock can be phased-locked.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocking:Output Clock Source**
                - C Attribute: **NISCOPE_ATTR_OUTPUT_CLOCK_SOURCE**

pll_lock_status
---------------

    .. py:attribute:: pll_lock_status

        If TRUE, the PLL has remained locked to the external reference clock since it was last checked. If FALSE,  the PLL has become unlocked from the external reference clock since it was last checked.




        .. tip:: This property can be set/get on specific instruments within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container instruments to specify a subset.

            Example: :py:attr:`my_session.instruments[ ... ].pll_lock_status`

            To set/get on all instruments, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.pll_lock_status`

        The following table lists the characteristics of this property.

            +-----------------------+-------------+
            | Characteristic        | Value       |
            +=======================+=============+
            | Datatype              | bool        |
            +-----------------------+-------------+
            | Permissions           | read only   |
            +-----------------------+-------------+
            | Repeated Capabilities | instruments |
            +-----------------------+-------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocking:PLL Lock Status**
                - C Attribute: **NISCOPE_ATTR_PLL_LOCK_STATUS**

points_done
-----------

    .. py:attribute:: points_done

        Actual number of samples acquired in the record specified by :py:attr:`niscope.Session.fetch_record_number` from the :py:attr:`niscope.Session.fetch_relative_to` and :py:attr:`niscope.Session.fetch_offset` properties.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Fetch:Points Done**
                - C Attribute: **NISCOPE_ATTR_POINTS_DONE**

poll_interval
-------------

    .. py:attribute:: poll_interval

        Specifies the poll interval in milliseconds to use during RIS acquisitions to check whether the acquisition is complete.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_POLL_INTERVAL**

probe_attenuation
-----------------

    .. py:attribute:: probe_attenuation

        Specifies the probe attenuation for the input channel. For example, for a 10:1 probe,  set this property to 10.0.
        Valid Values:
        Any positive real number. Typical values are 1, 10, and 100.




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].probe_attenuation`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.probe_attenuation`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Probe Attenuation**
                - C Attribute: **NISCOPE_ATTR_PROBE_ATTENUATION**

ready_for_advance_event_output_terminal
---------------------------------------

    .. py:attribute:: ready_for_advance_event_output_terminal

        Specifies the destination for the Ready for Advance Event.    When this event is asserted, the digitizer is ready to receive an advance trigger.
        Consult your device documentation for a specific list of valid destinations.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Synchronization:Ready for Advance:Output Terminal**
                - C Attribute: **NISCOPE_ATTR_READY_FOR_ADVANCE_EVENT_OUTPUT_TERMINAL**

ready_for_advance_event_terminal_name
-------------------------------------

    .. py:attribute:: ready_for_advance_event_terminal_name

        Returns the fully qualified name for the Ready for Advance Event terminal.    You can use this terminal as the source for a trigger.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Synchronization:Ready for Advance:Terminal Name**
                - C Attribute: **NISCOPE_ATTR_READY_FOR_ADVANCE_EVENT_TERMINAL_NAME**

ready_for_ref_event_output_terminal
-----------------------------------

    .. py:attribute:: ready_for_ref_event_output_terminal

        Specifies the destination for the Ready for Reference Event.  When this event is asserted, the digitizer is ready to receive a reference trigger.
        Consult your device documentation for a specific list of valid destinations.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Synchronization:Ready for Reference:Output Terminal**
                - C Attribute: **NISCOPE_ATTR_READY_FOR_REF_EVENT_OUTPUT_TERMINAL**

ready_for_ref_event_terminal_name
---------------------------------

    .. py:attribute:: ready_for_ref_event_terminal_name

        Returns the fully qualified name for the Ready for Reference Event terminal.    You can use this terminal as the source for a trigger.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Synchronization:Ready for Reference:Terminal Name**
                - C Attribute: **NISCOPE_ATTR_READY_FOR_REF_EVENT_TERMINAL_NAME**

ready_for_start_event_output_terminal
-------------------------------------

    .. py:attribute:: ready_for_start_event_output_terminal

        Specifies the destination for the Ready for Start Event.  When this event is asserted, the digitizer is ready to receive a start trigger.
        Consult your device documentation for a specific list of valid destinations.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Synchronization:Ready for Start:Output Terminal**
                - C Attribute: **NISCOPE_ATTR_READY_FOR_START_EVENT_OUTPUT_TERMINAL**

ready_for_start_event_terminal_name
-----------------------------------

    .. py:attribute:: ready_for_start_event_terminal_name

        Returns the fully qualified name for the Ready for Start Event terminal.    You can use this terminal as the source for a trigger.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Synchronization:Ready for Start:Terminal Name**
                - C Attribute: **NISCOPE_ATTR_READY_FOR_START_EVENT_TERMINAL_NAME**

records_done
------------

    .. py:attribute:: records_done

        Specifies the number of records that have been completely acquired.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Fetch:Records Done**
                - C Attribute: **NISCOPE_ATTR_RECORDS_DONE**

record_arm_source
-----------------

    .. py:attribute:: record_arm_source

        Specifies the record arm source.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Synchronization:Record Arm Source**
                - C Attribute: **NISCOPE_ATTR_RECORD_ARM_SOURCE**

ref_clk_rate
------------

    .. py:attribute:: ref_clk_rate

        If :py:attr:`niscope.Session.input_clock_source` is an external source, this property specifies the frequency of the input,  or reference clock, to which the internal sample clock timebase is synchronized. The frequency is in hertz.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocking:Reference Clock Rate**
                - C Attribute: **NISCOPE_ATTR_REF_CLK_RATE**

ref_trigger_detector_location
-----------------------------

    .. py:attribute:: ref_trigger_detector_location

        Indicates which analog compare circuitry to use on the device.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------------+
            | Characteristic        | Value                            |
            +=======================+==================================+
            | Datatype              | enums.RefTriggerDetectorLocation |
            +-----------------------+----------------------------------+
            | Permissions           | read-write                       |
            +-----------------------+----------------------------------+
            | Repeated Capabilities | None                             |
            +-----------------------+----------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Onboard Signal Processing:Ref Trigger Detection Location**
                - C Attribute: **NISCOPE_ATTR_REF_TRIGGER_DETECTOR_LOCATION**

ref_trigger_minimum_quiet_time
------------------------------

    .. py:attribute:: ref_trigger_minimum_quiet_time

        The amount of time the trigger circuit must not detect a signal above the trigger level before the trigger is armed.  This property is useful for triggering at the beginning and not in the middle of signal bursts.

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------------------------------+
            | Characteristic        | Value                                                       |
            +=======================+=============================================================+
            | Datatype              | hightime.timedelta, datetime.timedelta, or float in seconds |
            +-----------------------+-------------------------------------------------------------+
            | Permissions           | read-write                                                  |
            +-----------------------+-------------------------------------------------------------+
            | Repeated Capabilities | None                                                        |
            +-----------------------+-------------------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Onboard Signal Processing:Ref Trigger Min Quiet Time**
                - C Attribute: **NISCOPE_ATTR_REF_TRIGGER_MINIMUM_QUIET_TIME**

ref_trigger_terminal_name
-------------------------

    .. py:attribute:: ref_trigger_terminal_name

        Returns the fully qualified name for the Reference Trigger terminal.  You can use this terminal as the source for another trigger.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Terminal Name**
                - C Attribute: **NISCOPE_ATTR_REF_TRIGGER_TERMINAL_NAME**

ref_trig_tdc_enable
-------------------

    .. py:attribute:: ref_trig_tdc_enable

        This property controls whether the TDC is used to compute an accurate trigger.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Horizontal:Advanced:Enable TDC**
                - C Attribute: **NISCOPE_ATTR_REF_TRIG_TDC_ENABLE**

resolution
----------

    .. py:attribute:: resolution

        Indicates the bit width of valid data (as opposed to padding bits) in the acquired waveform. Compare to :py:attr:`niscope.Session.binary_sample_width`.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Resolution**
                - C Attribute: **NISCOPE_ATTR_RESOLUTION**

ris_in_auto_setup_enable
------------------------

    .. py:attribute:: ris_in_auto_setup_enable

        Indicates whether the digitizer should use RIS sample rates when searching for a frequency in autosetup.
        Valid Values:
        True  (1) - Use RIS sample rates in autosetup
        False (0) - Do not use RIS sample rates in autosetup

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Advanced:Enable RIS in Auto Setup**
                - C Attribute: **NISCOPE_ATTR_RIS_IN_AUTO_SETUP_ENABLE**

ris_method
----------

    .. py:attribute:: ris_method

        Specifies the algorithm for random-interleaved sampling, which is used if the sample rate exceeds the value of :py:attr:`niscope.Session.max_real_time_sampling_rate`.

        The following table lists the characteristics of this property.

            +-----------------------+-----------------+
            | Characteristic        | Value           |
            +=======================+=================+
            | Datatype              | enums.RISMethod |
            +-----------------------+-----------------+
            | Permissions           | read-write      |
            +-----------------------+-----------------+
            | Repeated Capabilities | None            |
            +-----------------------+-----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Horizontal:RIS Method**
                - C Attribute: **NISCOPE_ATTR_RIS_METHOD**

ris_num_averages
----------------

    .. py:attribute:: ris_num_averages

        The number of averages for each bin in an RIS acquisition.  The number of averages times the oversampling factor is the minimum number of real-time acquisitions necessary to reconstruct the RIS waveform.  Averaging is useful in RIS because the trigger times are not evenly spaced, so adjacent points in the reconstructed waveform not be accurately spaced.  By averaging, the errors in both time and voltage are smoothed.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Horizontal:RIS Num Avg**
                - C Attribute: **NISCOPE_ATTR_RIS_NUM_AVERAGES**

runt_high_threshold
-------------------

    .. py:attribute:: runt_high_threshold

        Specifies the higher of two thresholds, in volts, that bound the vertical range to examine for runt pulses.

        The runt threshold that causes the oscilloscope to trigger depends on the runt polarity you select. Refer to the :py:attr:`niscope.Session.runt_polarity` property for more information.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_RUNT_HIGH_THRESHOLD**

runt_low_threshold
------------------

    .. py:attribute:: runt_low_threshold

        Specifies the lower of two thresholds, in volts, that bound the vertical range to examine for runt pulses.

        The runt threshold that causes the oscilloscope to trigger depends on the runt polarity you select. Refer to the :py:attr:`niscope.Session.runt_polarity` property for more information.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_RUNT_LOW_THRESHOLD**

runt_polarity
-------------

    .. py:attribute:: runt_polarity

        Specifies the polarity of pulses that trigger the oscilloscope for runt triggering.

        When set to :py:data:`~niscope.RuntPolarity.POSITIVE`, the oscilloscope triggers when the following conditions are met:
            * The leading edge of a pulse crosses the :py:attr:`niscope.Session.runt_low_threshold` in a positive direction;
            * The trailing edge of the pulse crosses the :py:attr:`niscope.Session.runt_low_threshold` in a negative direction; and
            * No portion of the pulse crosses the :py:attr:`niscope.Session.runt_high_threshold`.

        When set to :py:data:`~niscope.RuntPolarity.NEGATIVE`, the oscilloscope triggers when the following conditions are met:
            * The leading edge of a pulse crosses the :py:attr:`niscope.Session.runt_high_threshold` in a negative direction;
            * The trailing edge of the pulse crosses the :py:attr:`niscope.Session.runt_high_threshold` in a positive direction; and
            * No portion of the pulse crosses the :py:attr:`niscope.Session.runt_low_threshold`.

        When set to :py:data:`~niscope.RuntPolarity.EITHER`, the oscilloscope triggers in either case.

        The following table lists the characteristics of this property.

            +-----------------------+--------------------+
            | Characteristic        | Value              |
            +=======================+====================+
            | Datatype              | enums.RuntPolarity |
            +-----------------------+--------------------+
            | Permissions           | read-write         |
            +-----------------------+--------------------+
            | Repeated Capabilities | None               |
            +-----------------------+--------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_RUNT_POLARITY**

runt_time_condition
-------------------

    .. py:attribute:: runt_time_condition

        Specifies whether runt triggers are time qualified, and if so, how the oscilloscope triggers in relation to the duration range bounded by the :py:attr:`niscope.Session.runt_time_low_limit` and :py:attr:`niscope.Session.runt_time_high_limit` properties.

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------+
            | Characteristic        | Value                   |
            +=======================+=========================+
            | Datatype              | enums.RuntTimeCondition |
            +-----------------------+-------------------------+
            | Permissions           | read-write              |
            +-----------------------+-------------------------+
            | Repeated Capabilities | None                    |
            +-----------------------+-------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_RUNT_TIME_CONDITION**

runt_time_high_limit
--------------------

    .. py:attribute:: runt_time_high_limit

        Specifies, in seconds, the high runt threshold time.

        This property sets the upper bound on the duration of runt pulses that may trigger the oscilloscope. The :py:attr:`niscope.Session.runt_time_condition` property determines how the oscilloscope triggers in relation to the runt time limits.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_RUNT_TIME_HIGH_LIMIT**

runt_time_low_limit
-------------------

    .. py:attribute:: runt_time_low_limit

        Specifies, in seconds, the low runt threshold time.

        This property sets the lower bound on the duration of runt pulses that may trigger the oscilloscope. The :py:attr:`niscope.Session.runt_time_condition` property determines how the oscilloscope triggers in relation to the runt time limits.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_RUNT_TIME_LOW_LIMIT**

sample_mode
-----------

    .. py:attribute:: sample_mode

        Indicates the sample mode the digitizer is currently using.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Sample Mode**
                - C Attribute: **NISCOPE_ATTR_SAMPLE_MODE**

samp_clk_timebase_div
---------------------

    .. py:attribute:: samp_clk_timebase_div

        If :py:attr:`niscope.Session.samp_clk_timebase_src` is an external source, specifies the ratio between the sample clock timebase rate and the actual sample rate, which can be slower.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocking:Sample Clock Timebase Divisor**
                - C Attribute: **NISCOPE_ATTR_SAMP_CLK_TIMEBASE_DIV**

sample_clock_timebase_multiplier
--------------------------------

    .. py:attribute:: sample_clock_timebase_multiplier

        If :py:attr:`niscope.Session.samp_clk_timebase_src` is an external source, this property specifies the ratio between the :py:attr:`niscope.Session.samp_clk_timebase_rate` and the actual sample rate, which can be higher. This property can be used in conjunction with :py:attr:`niscope.Session.samp_clk_timebase_div`.
        Some devices use multiple ADCs to sample the same channel at an effective sample rate that is greater than the specified clock rate. When providing an external sample clock use this property to indicate when you want a higher sample rate. Valid values for this property vary by device and current configuration.

        **Related topics:**
        `Sample Clock <digitizers.chm::/Sample_Clock.html>`__

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_SAMP_CLK_TIMEBASE_MULT**

samp_clk_timebase_rate
----------------------

    .. py:attribute:: samp_clk_timebase_rate

        If :py:attr:`niscope.Session.samp_clk_timebase_src` is an external source, specifies the frequency in hertz of the external clock used as the timebase source.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocking:Sample Clock Timebase Rate**
                - C Attribute: **NISCOPE_ATTR_SAMP_CLK_TIMEBASE_RATE**

samp_clk_timebase_src
---------------------

    .. py:attribute:: samp_clk_timebase_src

        Specifies the source of the sample clock timebase, which is the timebase used to control waveform sampling.  The actual sample rate may be the timebase itself or a divided version of the timebase, depending on the :py:attr:`niscope.Session.min_sample_rate` (for internal sources) or the :py:attr:`niscope.Session.samp_clk_timebase_div` (for external sources).

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocking:Sample Clock Timebase Source**
                - C Attribute: **NISCOPE_ATTR_SAMP_CLK_TIMEBASE_SRC**

serial_number
-------------

    .. py:attribute:: serial_number

        Returns the serial number of the device.




        .. tip:: This property can be set/get on specific instruments within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container instruments to specify a subset.

            Example: :py:attr:`my_session.instruments[ ... ].serial_number`

            To set/get on all instruments, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.serial_number`

        The following table lists the characteristics of this property.

            +-----------------------+-------------+
            | Characteristic        | Value       |
            +=======================+=============+
            | Datatype              | str         |
            +-----------------------+-------------+
            | Permissions           | read only   |
            +-----------------------+-------------+
            | Repeated Capabilities | instruments |
            +-----------------------+-------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device:Serial Number**
                - C Attribute: **NISCOPE_ATTR_SERIAL_NUMBER**

accessory_gain
--------------

    .. py:attribute:: accessory_gain

        Returns the calibration gain for the current device configuration.

        **Related topics:**
        `NI 5122/5124/5142 Calibration <digitizers.chm::/5122_Calibration.html>`__



        .. note:: This property is supported only by the NI PXI-5900 differential amplifier.


        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].accessory_gain`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.accessory_gain`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | channels  |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_SIGNAL_COND_GAIN**

accessory_offset
----------------

    .. py:attribute:: accessory_offset

        Returns the calibration offset for the current device configuration.

        **Related topics:**
        `NI 5122/5124/5142 Calibration <digitizers.chm::/5122_Calibration.html>`__



        .. note:: This property is supported only by the NI PXI-5900 differential amplifier.


        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].accessory_offset`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.accessory_offset`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | channels  |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_SIGNAL_COND_OFFSET**

simulate
--------

    .. py:attribute:: simulate

        Specifies whether or not to simulate instrument driver I/O operations.  If simulation is enabled, instrument driver methods perform range checking and call Ivi_GetAttribute and Ivi_SetAttribute methods, but they do not perform instrument I/O.  For output parameters that represent instrument data, the instrument driver methods return calculated values.
        The default value is False.  Use the :py:meth:`niscope.Session.__init__` method to override this value.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:User Options:Simulate**
                - C Attribute: **NISCOPE_ATTR_SIMULATE**

specific_driver_description
---------------------------

    .. py:attribute:: specific_driver_description

        A string that contains a brief description of the specific driver

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Description**
                - C Attribute: **NISCOPE_ATTR_SPECIFIC_DRIVER_DESCRIPTION**

specific_driver_revision
------------------------

    .. py:attribute:: specific_driver_revision

        A string that contains additional version information about this instrument driver.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Revision**
                - C Attribute: **NISCOPE_ATTR_SPECIFIC_DRIVER_REVISION**

specific_driver_vendor
----------------------

    .. py:attribute:: specific_driver_vendor

        A string that contains the name of the vendor that supplies this driver.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Driver Vendor**
                - C Attribute: **NISCOPE_ATTR_SPECIFIC_DRIVER_VENDOR**

start_to_ref_trigger_holdoff
----------------------------

    .. py:attribute:: start_to_ref_trigger_holdoff

        Pass the length of time you want the digitizer to wait after it starts acquiring data until the digitizer enables the trigger system to detect a reference (stop) trigger.
        Units: Seconds
        Valid Values: 0.0 - 171.8

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------------------------------+
            | Characteristic        | Value                                                       |
            +=======================+=============================================================+
            | Datatype              | hightime.timedelta, datetime.timedelta, or float in seconds |
            +-----------------------+-------------------------------------------------------------+
            | Permissions           | read-write                                                  |
            +-----------------------+-------------------------------------------------------------+
            | Repeated Capabilities | None                                                        |
            +-----------------------+-------------------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Start To Ref Trigger Holdoff**
                - C Attribute: **NISCOPE_ATTR_START_TO_REF_TRIGGER_HOLDOFF**

start_trigger_terminal_name
---------------------------

    .. py:attribute:: start_trigger_terminal_name

        Returns the fully qualified name for the Start Trigger terminal.  You can use this terminal as the source for another trigger.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Synchronization:Start Trigger (Acq. Arm):Terminal Name**
                - C Attribute: **NISCOPE_ATTR_START_TRIGGER_TERMINAL_NAME**

supported_instrument_models
---------------------------

    .. py:attribute:: supported_instrument_models

        A string that contains a comma-separated list of the instrument model numbers supported by this driver.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models**
                - C Attribute: **NISCOPE_ATTR_SUPPORTED_INSTRUMENT_MODELS**

trigger_auto_triggered
----------------------

    .. py:attribute:: trigger_auto_triggered

        Specifies if the last acquisition was auto triggered.  You can use the Auto Triggered property to find out if the last acquisition was triggered.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | bool      |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Auto Triggered**
                - C Attribute: **NISCOPE_ATTR_TRIGGER_AUTO_TRIGGERED**

trigger_coupling
----------------

    .. py:attribute:: trigger_coupling

        Specifies how the digitizer couples the trigger source. This property affects instrument operation only when :py:attr:`niscope.Session.trigger_type` is set to :py:data:`~niscope.TriggerType.EDGE`, :py:data:`~niscope.TriggerType.HYSTERESIS`, or :py:data:`~niscope.TriggerType.WINDOW`.

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------+
            | Characteristic        | Value                 |
            +=======================+=======================+
            | Datatype              | enums.TriggerCoupling |
            +-----------------------+-----------------------+
            | Permissions           | read-write            |
            +-----------------------+-----------------------+
            | Repeated Capabilities | None                  |
            +-----------------------+-----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Coupling**
                - C Attribute: **NISCOPE_ATTR_TRIGGER_COUPLING**

trigger_delay_time
------------------

    .. py:attribute:: trigger_delay_time

        Specifies the trigger delay time in seconds. The trigger delay time is the length of time the digitizer waits after it receives the trigger. The event that occurs when the trigger delay elapses is the Reference Event.
        Valid Values: 0.0 - 171.8

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------------------------------+
            | Characteristic        | Value                                                       |
            +=======================+=============================================================+
            | Datatype              | hightime.timedelta, datetime.timedelta, or float in seconds |
            +-----------------------+-------------------------------------------------------------+
            | Permissions           | read-write                                                  |
            +-----------------------+-------------------------------------------------------------+
            | Repeated Capabilities | None                                                        |
            +-----------------------+-------------------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Delay**
                - C Attribute: **NISCOPE_ATTR_TRIGGER_DELAY_TIME**

trigger_holdoff
---------------

    .. py:attribute:: trigger_holdoff

        Specifies the length of time (in seconds) the digitizer waits after detecting a trigger before enabling the trigger subsystem to detect another trigger. This property affects instrument operation only when the digitizer requires multiple acquisitions to build a complete waveform. The digitizer requires multiple waveform acquisitions when it uses equivalent-time sampling or when the digitizer is configured for a multi-record acquisition through a call to :py:meth:`niscope.Session.configure_horizontal_timing`.
        Valid Values: 0.0 - 171.8

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------------------------------+
            | Characteristic        | Value                                                       |
            +=======================+=============================================================+
            | Datatype              | hightime.timedelta, datetime.timedelta, or float in seconds |
            +-----------------------+-------------------------------------------------------------+
            | Permissions           | read-write                                                  |
            +-----------------------+-------------------------------------------------------------+
            | Repeated Capabilities | None                                                        |
            +-----------------------+-------------------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Holdoff**
                - C Attribute: **NISCOPE_ATTR_TRIGGER_HOLDOFF**

trigger_hysteresis
------------------

    .. py:attribute:: trigger_hysteresis

        Specifies the size of the hysteresis window on either side of the trigger level.  The digitizer triggers when the trigger signal passes through the threshold you specify with the Trigger Level parameter, has the slope you specify with the Trigger Slope parameter,  and passes through the hysteresis window that you specify with this parameter.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Hysteresis**
                - C Attribute: **NISCOPE_ATTR_TRIGGER_HYSTERESIS**

trigger_impedance
-----------------

    .. py:attribute:: trigger_impedance

        Specifies the input impedance for the external analog trigger channel in Ohms.
        Valid Values:
        50      - 50 ohms
        1000000 - 1 mega ohm

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Impedance**
                - C Attribute: **NISCOPE_ATTR_TRIGGER_IMPEDANCE**

trigger_level
-------------

    .. py:attribute:: trigger_level

        Specifies the voltage threshold for the trigger subsystem. The units are volts.  This property affects instrument behavior only when the :py:attr:`niscope.Session.trigger_type` is set to :py:data:`~niscope.TriggerType.EDGE`, :py:data:`~niscope.TriggerType.HYSTERESIS`, or :py:data:`~niscope.TriggerType.WINDOW`.
        Valid Values:
        The values of the range and offset parameters in :py:meth:`niscope.Session.configure_vertical` determine the valid range for the trigger level on the channel you use as the Trigger Source. The value you pass for this parameter must meet the following conditions:

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Level**
                - C Attribute: **NISCOPE_ATTR_TRIGGER_LEVEL**

trigger_modifier
----------------

    .. py:attribute:: trigger_modifier

        Configures the device to automatically complete an acquisition if a trigger has not been received.
        Valid Values:
        None (1)         - Normal triggering
        Auto Trigger (2) - Auto trigger acquisition if no trigger arrives

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------+
            | Characteristic        | Value                 |
            +=======================+=======================+
            | Datatype              | enums.TriggerModifier |
            +-----------------------+-----------------------+
            | Permissions           | read-write            |
            +-----------------------+-----------------------+
            | Repeated Capabilities | None                  |
            +-----------------------+-----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Modifier**
                - C Attribute: **NISCOPE_ATTR_TRIGGER_MODIFIER**

trigger_slope
-------------

    .. py:attribute:: trigger_slope

        Specifies if a rising or a falling edge triggers the digitizer.  This property affects instrument operation only when :py:attr:`niscope.Session.trigger_type` is set to :py:data:`~niscope.TriggerType.EDGE`, :py:data:`~niscope.TriggerType.HYSTERESIS`, or :py:data:`~niscope.TriggerType.WINDOW`.

        The following table lists the characteristics of this property.

            +-----------------------+--------------------+
            | Characteristic        | Value              |
            +=======================+====================+
            | Datatype              | enums.TriggerSlope |
            +-----------------------+--------------------+
            | Permissions           | read-write         |
            +-----------------------+--------------------+
            | Repeated Capabilities | None               |
            +-----------------------+--------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Slope**
                - C Attribute: **NISCOPE_ATTR_TRIGGER_SLOPE**

trigger_source
--------------

    .. py:attribute:: trigger_source

        Specifies the source the digitizer monitors for the trigger event.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Source**
                - C Attribute: **NISCOPE_ATTR_TRIGGER_SOURCE**

trigger_type
------------

    .. py:attribute:: trigger_type

        Specifies the type of trigger to use.

        The following table lists the characteristics of this property.

            +-----------------------+-------------------+
            | Characteristic        | Value             |
            +=======================+===================+
            | Datatype              | enums.TriggerType |
            +-----------------------+-------------------+
            | Permissions           | read-write        |
            +-----------------------+-------------------+
            | Repeated Capabilities | None              |
            +-----------------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Type**
                - C Attribute: **NISCOPE_ATTR_TRIGGER_TYPE**

trigger_window_high_level
-------------------------

    .. py:attribute:: trigger_window_high_level

        Pass the upper voltage threshold you want the digitizer to use for window triggering.
        The digitizer triggers when the trigger signal enters or leaves the window you specify with :py:attr:`niscope.Session.trigger_window_low_level` and :py:attr:`niscope.Session.trigger_window_high_level`
        Valid Values:
        The values of the Vertical Range and Vertical Offset parameters in :py:meth:`niscope.Session.configure_vertical` determine the valid range for the High Window Level on the channel you use as the Trigger Source parameter in :py:meth:`niscope.Session.ConfigureTriggerSource`.  The value you pass for this parameter must meet the following conditions.
        High Trigger Level <= Vertical Range/2 + Vertical Offset
        High Trigger Level >= (-Vertical Range/2) + Vertical Offset
        High Trigger Level > Low Trigger Level



        .. note:: One or more of the referenced methods are not in the Python API for this driver.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Window:High Level**
                - C Attribute: **NISCOPE_ATTR_TRIGGER_WINDOW_HIGH_LEVEL**

trigger_window_low_level
------------------------

    .. py:attribute:: trigger_window_low_level

        Pass the lower voltage threshold you want the digitizer to use for window triggering.
        The digitizer triggers when the trigger signal enters or leaves the window you specify with :py:attr:`niscope.Session.trigger_window_low_level` and :py:attr:`niscope.Session.trigger_window_high_level`.
        Units: Volts
        Valid Values:
        The values of the Vertical Range and Vertical Offset parameters in :py:meth:`niscope.Session.configure_vertical` determine the valid range for the Low Window Level on the channel you use as the Trigger Source parameter in :py:meth:`niscope.Session.ConfigureTriggerSource`.  The value you pass for this parameter must meet the following conditions.
        Low Trigger Level <= Vertical Range/2 + Vertical Offset
        Low Trigger Level >= (-Vertical Range/2) + Vertical Offset
        Low Trigger Level < High Trigger Level



        .. note:: One or more of the referenced methods are not in the Python API for this driver.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Window:Low Level**
                - C Attribute: **NISCOPE_ATTR_TRIGGER_WINDOW_LOW_LEVEL**

trigger_window_mode
-------------------

    .. py:attribute:: trigger_window_mode

        Specifies whether you want a trigger to occur when the signal enters or leaves the window specified by :py:attr:`niscope.Session.trigger_window_low_level`, or :py:attr:`niscope.Session.trigger_window_high_level`.

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------+
            | Characteristic        | Value                   |
            +=======================+=========================+
            | Datatype              | enums.TriggerWindowMode |
            +-----------------------+-------------------------+
            | Permissions           | read-write              |
            +-----------------------+-------------------------+
            | Repeated Capabilities | None                    |
            +-----------------------+-------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Window:Window Mode**
                - C Attribute: **NISCOPE_ATTR_TRIGGER_WINDOW_MODE**

tv_trigger_event
----------------

    .. py:attribute:: tv_trigger_event

        Specifies the condition in the video signal that causes the digitizer to trigger.

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------+
            | Characteristic        | Value                   |
            +=======================+=========================+
            | Datatype              | enums.VideoTriggerEvent |
            +-----------------------+-------------------------+
            | Permissions           | read-write              |
            +-----------------------+-------------------------+
            | Repeated Capabilities | None                    |
            +-----------------------+-------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Video:Event**
                - C Attribute: **NISCOPE_ATTR_TV_TRIGGER_EVENT**

tv_trigger_line_number
----------------------

    .. py:attribute:: tv_trigger_line_number

        Specifies the line on which to trigger, if :py:attr:`niscope.Session.tv_trigger_event` is set to line number. The valid ranges of the property depend on the signal format selected.  M-NTSC has a valid range of 1 to 525.  B/G-PAL, SECAM, 576i, and 576p have a valid range of 1 to 625. 720p has a valid range of 1 to 750. 1080i and 1080p have a valid range of 1125.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | int        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Video:Line Number**
                - C Attribute: **NISCOPE_ATTR_TV_TRIGGER_LINE_NUMBER**

tv_trigger_polarity
-------------------

    .. py:attribute:: tv_trigger_polarity

        Specifies whether the video signal sync is positive or negative.

        The following table lists the characteristics of this property.

            +-----------------------+---------------------+
            | Characteristic        | Value               |
            +=======================+=====================+
            | Datatype              | enums.VideoPolarity |
            +-----------------------+---------------------+
            | Permissions           | read-write          |
            +-----------------------+---------------------+
            | Repeated Capabilities | None                |
            +-----------------------+---------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Video:Polarity**
                - C Attribute: **NISCOPE_ATTR_TV_TRIGGER_POLARITY**

tv_trigger_signal_format
------------------------

    .. py:attribute:: tv_trigger_signal_format

        Specifies the type of video signal, such as NTSC, PAL, or SECAM.

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------+
            | Characteristic        | Value                   |
            +=======================+=========================+
            | Datatype              | enums.VideoSignalFormat |
            +-----------------------+-------------------------+
            | Permissions           | read-write              |
            +-----------------------+-------------------------+
            | Repeated Capabilities | None                    |
            +-----------------------+-------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Video:Signal Format**
                - C Attribute: **NISCOPE_ATTR_TV_TRIGGER_SIGNAL_FORMAT**

use_spec_initial_x
------------------

    .. py:attribute:: use_spec_initial_x

        

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_USE_SPEC_INITIAL_X**

vertical_coupling
-----------------

    .. py:attribute:: vertical_coupling

        Specifies how the digitizer couples the input signal for the channel.  When input coupling changes, the input stage takes a finite amount of time to settle.




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].vertical_coupling`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.vertical_coupling`

        The following table lists the characteristics of this property.

            +-----------------------+------------------------+
            | Characteristic        | Value                  |
            +=======================+========================+
            | Datatype              | enums.VerticalCoupling |
            +-----------------------+------------------------+
            | Permissions           | read-write             |
            +-----------------------+------------------------+
            | Repeated Capabilities | channels               |
            +-----------------------+------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Vertical Coupling**
                - C Attribute: **NISCOPE_ATTR_VERTICAL_COUPLING**

vertical_offset
---------------

    .. py:attribute:: vertical_offset

        Specifies the location of the center of the range. The value is with respect to ground and is in volts.  For example, to acquire a sine wave that spans between 0.0 and 10.0 V, set this property to 5.0 V.



        .. note:: This property is not supported by all digitizers.Refer to the NI High-Speed Digitizers Help for a list of vertical offsets supported for each device.


        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].vertical_offset`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.vertical_offset`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Vertical Offset**
                - C Attribute: **NISCOPE_ATTR_VERTICAL_OFFSET**

vertical_range
--------------

    .. py:attribute:: vertical_range

        Specifies the absolute value of the input range for a channel in volts.  For example, to acquire a sine wave that spans between -5 and +5 V, set this property to 10.0 V.
        Refer to the NI High-Speed Digitizers Help for a list of supported vertical ranges for each device.  If the specified range is not supported by a device, the value is coerced up to the next valid range.




        .. tip:: This property can be set/get on specific channels within your :py:class:`niscope.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].vertical_range`

            To set/get on all channels, you can call the property directly on the :py:class:`niscope.Session`.

            Example: :py:attr:`my_session.vertical_range`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Vertical Range**
                - C Attribute: **NISCOPE_ATTR_VERTICAL_RANGE**

width_condition
---------------

    .. py:attribute:: width_condition

        Specifies whether the oscilloscope triggers on pulses within or outside the duration range bounded by the :py:attr:`niscope.Session.width_low_threshold` and :py:attr:`niscope.Session.width_high_threshold` properties.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------+
            | Characteristic        | Value                |
            +=======================+======================+
            | Datatype              | enums.WidthCondition |
            +-----------------------+----------------------+
            | Permissions           | read-write           |
            +-----------------------+----------------------+
            | Repeated Capabilities | None                 |
            +-----------------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_WIDTH_CONDITION**

width_high_threshold
--------------------

    .. py:attribute:: width_high_threshold

        Specifies the high width threshold, in seconds.

        This properties sets the upper bound on the duration range that triggers the oscilloscope. The :py:attr:`niscope.Session.width_condition` property determines how the oscilloscope triggers in relation to the width thresholds.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_WIDTH_HIGH_THRESHOLD**

width_low_threshold
-------------------

    .. py:attribute:: width_low_threshold

        Specifies the low width threshold, in seconds.

        This property sets the lower bound on the duration range that triggers the oscilloscope. The :py:attr:`niscope.Session.width_condition` property determines how the oscilloscope triggers in relation to the width thresholds.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_WIDTH_LOW_THRESHOLD**

width_polarity
--------------

    .. py:attribute:: width_polarity

        Specifies the polarity of pulses that trigger the oscilloscope for width triggering.

        The following table lists the characteristics of this property.

            +-----------------------+---------------------+
            | Characteristic        | Value               |
            +=======================+=====================+
            | Datatype              | enums.WidthPolarity |
            +-----------------------+---------------------+
            | Permissions           | read-write          |
            +-----------------------+---------------------+
            | Repeated Capabilities | None                |
            +-----------------------+---------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_WIDTH_POLARITY**


NI-TClk Support
===============

    .. py:attribute:: tclk

        This is used to get and set NI-TClk attributes on the session.

        .. seealso:: See :py:class:`nitclk.SessionReference` for a complete list of attributes.


.. contents:: Session
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/niscope/conf.py sha256=5368c92e17999d444490abf62b245c7b9263df6b612ebe2297b51f0ebf6b894f bytes=6538 -->
## FILE: docs/niscope/conf.py

- repository: `ni/nimi-python`
- source_path: `docs/niscope/conf.py`
- sha256: `5368c92e17999d444490abf62b245c7b9263df6b612ebe2297b51f0ebf6b894f`
- bytes: 6538

````python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# NI-SCOPE Python API documentation build configuration file, created by
# sphinx-quickstart on Fri Jul 14 13:04:36 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../generated'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.doctest',
              'sphinx.ext.intersphinx',
              'sphinx.ext.todo',
              'sphinx.ext.coverage',
              'sphinx.ext.mathjax',
              'sphinx.ext.ifconfig',
              'sphinx.ext.viewcode',
              'sphinx.ext.githubpages']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'NI-SCOPE Python API'
copyright = '2017-2026, National Instruments Corporation'
author = 'NI'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags.
release = '1.4.10.dev0'
# The short X.Y version.
version = release[:3]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'navigation_depth': -1,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../_static']

# Fix wide tables of RTD per https://github.com/rtfd/sphinx_rtd_theme/issues/117#issuecomment-41571653
def setup(app):
    app.add_css_file('theme_overrides.css')

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
        'donate.html',
    ]
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'NIModularInstrumentsPythonAPIdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'NISCOPEPythonAPI.tex', 'NI-SCOPE Python API Documentation',
     'NI', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'niscopepythonapi', 'NI-SCOPE Python API Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'NISCOPEPythonAPI', 'NI-SCOPE Python API Documentation',
     author, 'NISCOPEPythonAPI', 'One line description of project.',
     'Miscellaneous'),
]

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'nidcpower': ('https://nidcpower.readthedocs.io/en/latest/', None),
    'nidigital': ('https://nidigital.readthedocs.io/en/latest/', None),
    'nidmm': ('https://nidmm.readthedocs.io/en/latest/', None),
    'nifgen': ('https://nifgen.readthedocs.io/en/latest/', None),
    'nimodinst': ('https://nimodinst.readthedocs.io/en/latest/', None),
    'nirfsg': ('https://nirfsg.readthedocs.io/en/latest/', None),
    'nise': ('https://nise.readthedocs.io/en/latest/', None),
    'niswitch': ('https://niswitch.readthedocs.io/en/latest/', None),
    'nitclk': ('https://nitclk.readthedocs.io/en/latest/', None),
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/niscope/enums.rst sha256=cf3bdde9bf4199218b85fdb82cdde5a2c5d3431874e4800c5db93ccf48d07a41 bytes=28044 -->
## FILE: docs/niscope/enums.rst

- repository: `ni/nimi-python`
- source_path: `docs/niscope/enums.rst`
- sha256: `cf3bdde9bf4199218b85fdb82cdde5a2c5d3431874e4800c5db93ccf48d07a41`
- bytes: 28044

````rst
Enums
=====

Enums used in NI-SCOPE

.. py:currentmodule:: niscope


AcquisitionStatus
-----------------

.. py:class:: AcquisitionStatus

    .. py:attribute:: AcquisitionStatus.COMPLETE



    .. py:attribute:: AcquisitionStatus.IN_PROGRESS



    .. py:attribute:: AcquisitionStatus.STATUS_UNKNOWN



AcquisitionType
---------------

.. py:class:: AcquisitionType

    .. py:attribute:: AcquisitionType.NORMAL



        Sets the digitizer to normal resolution mode. The digitizer can use real-time sampling or equivalent-time sampling.

        



    .. py:attribute:: AcquisitionType.FLEXRES



        Sets the digitizer to flexible resolution mode if supported.  The digitizer uses different hardware configurations to change the resolution depending on the sampling rate used.

        



    .. py:attribute:: AcquisitionType.DDC



        Sets the digitizer to DDC mode on the NI 5620/5621.

        



ArrayMeasurement
----------------

.. py:class:: ArrayMeasurement

    .. py:attribute:: ArrayMeasurement.NO_MEASUREMENT



        None

        



    .. py:attribute:: ArrayMeasurement.LAST_ACQ_HISTOGRAM



        Last Acquisition Histogram

        



    .. py:attribute:: ArrayMeasurement.FFT_PHASE_SPECTRUM



        FFT Phase Spectrum

        



    .. py:attribute:: ArrayMeasurement.FFT_AMP_SPECTRUM_VOLTS_RMS



        FFT Amp. Spectrum (Volts RMS)

        



    .. py:attribute:: ArrayMeasurement.MULTI_ACQ_VOLTAGE_HISTOGRAM



        Multi Acquisition Voltage Histogram

        



    .. py:attribute:: ArrayMeasurement.MULTI_ACQ_TIME_HISTOGRAM



        Multi Acquisition Time Histogram

        



    .. py:attribute:: ArrayMeasurement.ARRAY_INTEGRAL



        Array Integral

        



    .. py:attribute:: ArrayMeasurement.DERIVATIVE



        Derivative

        



    .. py:attribute:: ArrayMeasurement.INVERSE



        Inverse

        



    .. py:attribute:: ArrayMeasurement.HANNING_WINDOW



        Hanning Window

        



    .. py:attribute:: ArrayMeasurement.FLAT_TOP_WINDOW



        Flat Top Window

        



    .. py:attribute:: ArrayMeasurement.POLYNOMIAL_INTERPOLATION



        Polynomial Interpolation

        



    .. py:attribute:: ArrayMeasurement.MULTIPLY_CHANNELS



        Multiply Channels

        



    .. py:attribute:: ArrayMeasurement.ADD_CHANNELS



        Add Channels

        



    .. py:attribute:: ArrayMeasurement.SUBTRACT_CHANNELS



        Subtract Channels

        



    .. py:attribute:: ArrayMeasurement.DIVIDE_CHANNELS



        Divide Channels

        



    .. py:attribute:: ArrayMeasurement.MULTI_ACQ_AVERAGE



        Multi Acquisition Average

        



    .. py:attribute:: ArrayMeasurement.BUTTERWORTH_FILTER



        Butterworth IIR Filter

        



    .. py:attribute:: ArrayMeasurement.CHEBYSHEV_FILTER



        Chebyshev IIR Filter

        



    .. py:attribute:: ArrayMeasurement.FFT_AMP_SPECTRUM_DB



        FFT Amp. Spectrum (dB)

        



    .. py:attribute:: ArrayMeasurement.HAMMING_WINDOW



        Hamming Window

        



    .. py:attribute:: ArrayMeasurement.WINDOWED_FIR_FILTER



        FIR Windowed Filter

        



    .. py:attribute:: ArrayMeasurement.BESSEL_FILTER



        Bessel IIR Filter

        



    .. py:attribute:: ArrayMeasurement.TRIANGLE_WINDOW



        Triangle Window

        



    .. py:attribute:: ArrayMeasurement.BLACKMAN_WINDOW



        Blackman Window

        



    .. py:attribute:: ArrayMeasurement.ARRAY_OFFSET



        Array Offset

        



    .. py:attribute:: ArrayMeasurement.ARRAY_GAIN



        Array Gain

        



CableSenseMode
--------------

.. py:class:: CableSenseMode

    .. py:attribute:: CableSenseMode.DISABLED



        The oscilloscope is not configured to emit a CableSense signal.

        



    .. py:attribute:: CableSenseMode.ON_DEMAND



        The oscilloscope is configured to emit a single CableSense pulse.

        



ClearableMeasurement
--------------------

.. py:class:: ClearableMeasurement

    .. py:attribute:: ClearableMeasurement.ALL_MEASUREMENTS



    .. py:attribute:: ClearableMeasurement.MULTI_ACQ_VOLTAGE_HISTOGRAM



    .. py:attribute:: ClearableMeasurement.MULTI_ACQ_TIME_HISTOGRAM



    .. py:attribute:: ClearableMeasurement.MULTI_ACQ_AVERAGE



    .. py:attribute:: ClearableMeasurement.FREQUENCY



    .. py:attribute:: ClearableMeasurement.AVERAGE_FREQUENCY



    .. py:attribute:: ClearableMeasurement.FFT_FREQUENCY



    .. py:attribute:: ClearableMeasurement.PERIOD



    .. py:attribute:: ClearableMeasurement.AVERAGE_PERIOD



    .. py:attribute:: ClearableMeasurement.RISE_TIME



    .. py:attribute:: ClearableMeasurement.FALL_TIME



    .. py:attribute:: ClearableMeasurement.RISE_SLEW_RATE



    .. py:attribute:: ClearableMeasurement.FALL_SLEW_RATE



    .. py:attribute:: ClearableMeasurement.OVERSHOOT



    .. py:attribute:: ClearableMeasurement.PRESHOOT



    .. py:attribute:: ClearableMeasurement.VOLTAGE_RMS



    .. py:attribute:: ClearableMeasurement.VOLTAGE_CYCLE_RMS



    .. py:attribute:: ClearableMeasurement.AC_ESTIMATE



    .. py:attribute:: ClearableMeasurement.FFT_AMPLITUDE



    .. py:attribute:: ClearableMeasurement.VOLTAGE_AVERAGE



    .. py:attribute:: ClearableMeasurement.VOLTAGE_CYCLE_AVERAGE



    .. py:attribute:: ClearableMeasurement.DC_ESTIMATE



    .. py:attribute:: ClearableMeasurement.VOLTAGE_MAX



    .. py:attribute:: ClearableMeasurement.VOLTAGE_MIN



    .. py:attribute:: ClearableMeasurement.VOLTAGE_PEAK_TO_PEAK



    .. py:attribute:: ClearableMeasurement.VOLTAGE_HIGH



    .. py:attribute:: ClearableMeasurement.VOLTAGE_LOW



    .. py:attribute:: ClearableMeasurement.AMPLITUDE



    .. py:attribute:: ClearableMeasurement.VOLTAGE_TOP



    .. py:attribute:: ClearableMeasurement.VOLTAGE_BASE



    .. py:attribute:: ClearableMeasurement.VOLTAGE_BASE_TO_TOP



    .. py:attribute:: ClearableMeasurement.WIDTH_NEG



    .. py:attribute:: ClearableMeasurement.WIDTH_POS



    .. py:attribute:: ClearableMeasurement.DUTY_CYCLE_NEG



    .. py:attribute:: ClearableMeasurement.DUTY_CYCLE_POS



    .. py:attribute:: ClearableMeasurement.INTEGRAL



    .. py:attribute:: ClearableMeasurement.AREA



    .. py:attribute:: ClearableMeasurement.CYCLE_AREA



    .. py:attribute:: ClearableMeasurement.TIME_DELAY



    .. py:attribute:: ClearableMeasurement.PHASE_DELAY



    .. py:attribute:: ClearableMeasurement.LOW_REF_VOLTS



    .. py:attribute:: ClearableMeasurement.MID_REF_VOLTS



    .. py:attribute:: ClearableMeasurement.HIGH_REF_VOLTS



    .. py:attribute:: ClearableMeasurement.VOLTAGE_HISTOGRAM_MEAN



    .. py:attribute:: ClearableMeasurement.VOLTAGE_HISTOGRAM_STDEV



    .. py:attribute:: ClearableMeasurement.VOLTAGE_HISTOGRAM_MEDIAN



    .. py:attribute:: ClearableMeasurement.VOLTAGE_HISTOGRAM_MODE



    .. py:attribute:: ClearableMeasurement.VOLTAGE_HISTOGRAM_MAX



    .. py:attribute:: ClearableMeasurement.VOLTAGE_HISTOGRAM_MIN



    .. py:attribute:: ClearableMeasurement.VOLTAGE_HISTOGRAM_PEAK_TO_PEAK



    .. py:attribute:: ClearableMeasurement.VOLTAGE_HISTOGRAM_MEAN_PLUS_STDEV



    .. py:attribute:: ClearableMeasurement.VOLTAGE_HISTOGRAM_MEAN_PLUS_2_STDEV



    .. py:attribute:: ClearableMeasurement.VOLTAGE_HISTOGRAM_MEAN_PLUS_3_STDEV



    .. py:attribute:: ClearableMeasurement.VOLTAGE_HISTOGRAM_HITS



    .. py:attribute:: ClearableMeasurement.VOLTAGE_HISTOGRAM_NEW_HITS



    .. py:attribute:: ClearableMeasurement.TIME_HISTOGRAM_MEAN



    .. py:attribute:: ClearableMeasurement.TIME_HISTOGRAM_STDEV



    .. py:attribute:: ClearableMeasurement.TIME_HISTOGRAM_MEDIAN



    .. py:attribute:: ClearableMeasurement.TIME_HISTOGRAM_MODE



    .. py:attribute:: ClearableMeasurement.TIME_HISTOGRAM_MAX



    .. py:attribute:: ClearableMeasurement.TIME_HISTOGRAM_MIN



    .. py:attribute:: ClearableMeasurement.TIME_HISTOGRAM_PEAK_TO_PEAK



    .. py:attribute:: ClearableMeasurement.TIME_HISTOGRAM_MEAN_PLUS_STDEV



    .. py:attribute:: ClearableMeasurement.TIME_HISTOGRAM_MEAN_PLUS_2_STDEV



    .. py:attribute:: ClearableMeasurement.TIME_HISTOGRAM_MEAN_PLUS_3_STDEV



    .. py:attribute:: ClearableMeasurement.TIME_HISTOGRAM_HITS



    .. py:attribute:: ClearableMeasurement.TIME_HISTOGRAM_NEW_HITS



FIRFilterWindow
---------------

.. py:class:: FIRFilterWindow

    .. py:attribute:: FIRFilterWindow.NONE



        No window.

        



    .. py:attribute:: FIRFilterWindow.HANNING



        Specifies a Hanning window.

        



    .. py:attribute:: FIRFilterWindow.FLAT_TOP



        Specifies a Flat Top window.

        



    .. py:attribute:: FIRFilterWindow.HAMMING



        Specifies a Hamming window.

        



    .. py:attribute:: FIRFilterWindow.TRIANGLE



        Specifies a Triangle window.

        



    .. py:attribute:: FIRFilterWindow.BLACKMAN



        Specifies a Blackman window.

        



FetchRelativeTo
---------------

.. py:class:: FetchRelativeTo

    .. py:attribute:: FetchRelativeTo.READ_POINTER



        The read pointer is set to zero when a new acquisition is initiated. After every fetch the read pointer is incremeted to be the sample after the last sample retrieved.  Therefore, you can repeatedly fetch relative to the read pointer for a continuous acquisition program.

        



    .. py:attribute:: FetchRelativeTo.PRETRIGGER



        Fetches relative to the first pretrigger point requested with :py:meth:`niscope.Session.configure_horizontal_timing`.

        



    .. py:attribute:: FetchRelativeTo.NOW



        Fetch data at the last sample acquired.

        



    .. py:attribute:: FetchRelativeTo.START



        Fetch data starting at the first point sampled by the digitizer.

        



    .. py:attribute:: FetchRelativeTo.TRIGGER



        Fetch at the first posttrigger sample.

        



FilterType
----------

.. py:class:: FilterType

    .. py:attribute:: FilterType.LOWPASS



        Specifies lowpass as the filter type.

        



    .. py:attribute:: FilterType.HIGHPASS



        Specifies highpass as the filter type.

        



    .. py:attribute:: FilterType.BANDPASS



        Specifies bandpass as the filter type.

        



    .. py:attribute:: FilterType.BANDSTOP



        Specifies bandstop as the filter type.

        



FlexFIRAntialiasFilterType
--------------------------

.. py:class:: FlexFIRAntialiasFilterType

    .. py:attribute:: FlexFIRAntialiasFilterType.FOURTYEIGHT_TAP_STANDARD



        This filter is optimized for alias protection and frequency-domain flatness

        



    .. py:attribute:: FlexFIRAntialiasFilterType.FOURTYEIGHT_TAP_HANNING



        This filter is optimized for the lowest possible bandwidth for a 48 tap filter and maximizes the SNR

        



    .. py:attribute:: FlexFIRAntialiasFilterType.SIXTEEN_TAP_HANNING



        This filter is optimized for the lowest possible bandwidth for a 16 tap filter and maximizes the SNR

        



    .. py:attribute:: FlexFIRAntialiasFilterType.EIGHT_TAP_HANNING



        This filter is optimized for the lowest possible bandwidth for a 8 tap filter and maximizes the SNR

        



GlitchCondition
---------------

.. py:class:: GlitchCondition

    .. py:attribute:: GlitchCondition.GREATER



        Trigger on pulses with a duration greater than the specified glitch width.

        



    .. py:attribute:: GlitchCondition.LESS



        Trigger on pulses with a duration shorter than the specified glitch width.

        



GlitchPolarity
--------------

.. py:class:: GlitchPolarity

    .. py:attribute:: GlitchPolarity.POSITIVE



        Trigger on pulses of positive polarity relative to the trigger threshold.

        



    .. py:attribute:: GlitchPolarity.NEGATIVE



        Trigger on pulses of negative polarity relative to the trigger threshold.

        



    .. py:attribute:: GlitchPolarity.EITHER



        Trigger on pulses of either positive or negative polarity.

        



Option
------

.. py:class:: Option

    .. py:attribute:: Option.SELF_CALIBRATE_ALL_CHANNELS



        Self Calibrating all Channels

        



    .. py:attribute:: Option.RESTORE_EXTERNAL_CALIBRATION



        Restore External Calibration.

        



PercentageMethod
----------------

.. py:class:: PercentageMethod

    .. py:attribute:: PercentageMethod.LOWHIGH



        Specifies that the reference level percentages should be computed using
        the low/high method,

        



    .. py:attribute:: PercentageMethod.MINMAX



        Reference level percentages are computed using the min/max method.

        



    .. py:attribute:: PercentageMethod.BASETOP



        Reference level percentages are computed using the base/top method.

        



RISMethod
---------

.. py:class:: RISMethod

    .. py:attribute:: RISMethod.EXACT_NUM_AVERAGES



        Acquires exactly the specified number of records for each bin in the RIS acquisition.  An error is returned from the fetch method if the RIS acquisition does not successfully acquire the specified number of waveforms within the timeout period.  You may call the fetch method again to allow more time for the acquisition to finish.

        



    .. py:attribute:: RISMethod.MIN_NUM_AVERAGES



        Each RIS sample is the average of a least a minimum number of randomly
        distributed points.

        



    .. py:attribute:: RISMethod.INCOMPLETE



        Returns the RIS waveform after the specified timeout even if it is incomplete.  If no waveforms have been acquired in certain bins, these bins will have a NaN (when fetching scaled data) or a zero (when fetching binary data). A warning (positive error code) is returned from the fetch method if the RIS acquisition did not finish.  The acquisition aborts when data is returned.

        



    .. py:attribute:: RISMethod.LIMITED_BIN_WIDTH



        Limits the waveforms in the various bins to be within 200 ps of the center of the bin.

        



RefLevelUnits
-------------

.. py:class:: RefLevelUnits

    .. py:attribute:: RefLevelUnits.VOLTS



        Specifies that the reference levels are given in units of volts.

        



    .. py:attribute:: RefLevelUnits.PERCENTAGE



        (Default) Specifies that the reference levels are given in percentage
        units.

        



RefTriggerDetectorLocation
--------------------------

.. py:class:: RefTriggerDetectorLocation

    .. py:attribute:: RefTriggerDetectorLocation.ANALOG_DETECTION_CIRCUIT



        use the hardware analog circuitry to implement the reference trigger.  This option will trigger before any onboard signal processing.

        



    .. py:attribute:: RefTriggerDetectorLocation.DDC_OUTPUT



        use the onboard signal processing logic to implement the reference trigger.  This option will trigger based on the onboard signal processed data.

        



RuntPolarity
------------

.. py:class:: RuntPolarity

    .. py:attribute:: RuntPolarity.POSITIVE



        Trigger on pulses of positive polarity relative to :py:attr:`niscope.Session.runt_low_threshold` that do not cross :py:attr:`niscope.Session.runt_high_threshold`.

        



    .. py:attribute:: RuntPolarity.NEGATIVE



        Trigger on pulses of negative polarity relative to :py:attr:`niscope.Session.runt_high_threshold` that do not cross :py:attr:`niscope.Session.runt_low_threshold`.

        



    .. py:attribute:: RuntPolarity.EITHER



        Trigger on pulses of either positive or negative polarity.

        



RuntTimeCondition
-----------------

.. py:class:: RuntTimeCondition

    .. py:attribute:: RuntTimeCondition.NONE



        Time qualification is disabled. Trigger on runt pulses based solely on the voltage level of the pulses.

        



    .. py:attribute:: RuntTimeCondition.WITHIN



        Trigger on pulses that, in addition to meeting runt voltage criteria, have a duration within the range bounded by :py:attr:`niscope.Session.runt_time_low_limit` and :py:attr:`niscope.Session.runt_time_high_limit`.

        



    .. py:attribute:: RuntTimeCondition.OUTSIDE



        Trigger on pulses that, in addition to meeting runt voltage criteria, have a duration not within the range bounded by :py:attr:`niscope.Session.runt_time_low_limit` and :py:attr:`niscope.Session.runt_time_high_limit`.

        



ScalarMeasurement
-----------------

.. py:class:: ScalarMeasurement

    .. py:attribute:: ScalarMeasurement.NO_MEASUREMENT



        None

        



    .. py:attribute:: ScalarMeasurement.RISE_TIME



    .. py:attribute:: ScalarMeasurement.FALL_TIME



    .. py:attribute:: ScalarMeasurement.FREQUENCY



    .. py:attribute:: ScalarMeasurement.PERIOD



    .. py:attribute:: ScalarMeasurement.VOLTAGE_RMS



    .. py:attribute:: ScalarMeasurement.VOLTAGE_PEAK_TO_PEAK



    .. py:attribute:: ScalarMeasurement.VOLTAGE_MAX



    .. py:attribute:: ScalarMeasurement.VOLTAGE_MIN



    .. py:attribute:: ScalarMeasurement.VOLTAGE_HIGH



    .. py:attribute:: ScalarMeasurement.VOLTAGE_LOW



    .. py:attribute:: ScalarMeasurement.VOLTAGE_AVERAGE



    .. py:attribute:: ScalarMeasurement.WIDTH_NEG



    .. py:attribute:: ScalarMeasurement.WIDTH_POS



    .. py:attribute:: ScalarMeasurement.DUTY_CYCLE_NEG



    .. py:attribute:: ScalarMeasurement.DUTY_CYCLE_POS



    .. py:attribute:: ScalarMeasurement.AMPLITUDE



    .. py:attribute:: ScalarMeasurement.VOLTAGE_CYCLE_RMS



    .. py:attribute:: ScalarMeasurement.VOLTAGE_CYCLE_AVERAGE



    .. py:attribute:: ScalarMeasurement.OVERSHOOT



    .. py:attribute:: ScalarMeasurement.PRESHOOT



    .. py:attribute:: ScalarMeasurement.LOW_REF_VOLTS



    .. py:attribute:: ScalarMeasurement.MID_REF_VOLTS



    .. py:attribute:: ScalarMeasurement.HIGH_REF_VOLTS



    .. py:attribute:: ScalarMeasurement.AREA



    .. py:attribute:: ScalarMeasurement.CYCLE_AREA



    .. py:attribute:: ScalarMeasurement.INTEGRAL



    .. py:attribute:: ScalarMeasurement.VOLTAGE_BASE



    .. py:attribute:: ScalarMeasurement.VOLTAGE_TOP



    .. py:attribute:: ScalarMeasurement.FFT_FREQUENCY



    .. py:attribute:: ScalarMeasurement.FFT_AMPLITUDE



    .. py:attribute:: ScalarMeasurement.RISE_SLEW_RATE



    .. py:attribute:: ScalarMeasurement.FALL_SLEW_RATE



    .. py:attribute:: ScalarMeasurement.AC_ESTIMATE



    .. py:attribute:: ScalarMeasurement.DC_ESTIMATE



    .. py:attribute:: ScalarMeasurement.TIME_DELAY



    .. py:attribute:: ScalarMeasurement.AVERAGE_PERIOD



    .. py:attribute:: ScalarMeasurement.AVERAGE_FREQUENCY



    .. py:attribute:: ScalarMeasurement.VOLTAGE_BASE_TO_TOP



    .. py:attribute:: ScalarMeasurement.PHASE_DELAY



TerminalConfiguration
---------------------

.. py:class:: TerminalConfiguration

    .. py:attribute:: TerminalConfiguration.SINGLE_ENDED



        Channel is single ended

        



    .. py:attribute:: TerminalConfiguration.UNBALANCED_DIFFERENTIAL



        Channel is unbalanced differential

        



    .. py:attribute:: TerminalConfiguration.DIFFERENTIAL



        Channel is differential

        



TriggerCoupling
---------------

.. py:class:: TriggerCoupling

    .. py:attribute:: TriggerCoupling.AC



        AC coupling

        



    .. py:attribute:: TriggerCoupling.DC



        DC coupling

        



    .. py:attribute:: TriggerCoupling.HF_REJECT



        Highpass filter coupling

        



    .. py:attribute:: TriggerCoupling.LF_REJECT



        Lowpass filter coupling

        



    .. py:attribute:: TriggerCoupling.AC_PLUS_HF_REJECT



        Highpass and lowpass filter coupling

        



TriggerModifier
---------------

.. py:class:: TriggerModifier

    .. py:attribute:: TriggerModifier.NO_TRIGGER_MOD



        Normal triggering.

        



    .. py:attribute:: TriggerModifier.AUTO



        Software will trigger an acquisition automatically if no trigger arrives
        after a certain amount of time.

        



    .. py:attribute:: TriggerModifier.AUTO_LEVEL



TriggerSlope
------------

.. py:class:: TriggerSlope

    .. py:attribute:: TriggerSlope.NEGATIVE



        Falling edge

        



    .. py:attribute:: TriggerSlope.POSITIVE



        Rising edge

        



    .. py:attribute:: TriggerSlope.SLOPE_EITHER



        Either edge

        



TriggerType
-----------

.. py:class:: TriggerType

    .. py:attribute:: TriggerType.EDGE



        Configures the digitizer for edge triggering.  An edge trigger occurs when the trigger signal crosses the trigger level specified with the set trigger slope.  You configure the trigger level and slope with :py:meth:`niscope.Session.configure_trigger_edge`.

        



    .. py:attribute:: TriggerType.HYSTERESIS



        Configures the digitizer for hysteresis triggering.  A hysteresis trigger occurs when the trigger signal crosses the trigger level with the specified slope and passes through the hysteresis window you specify. You configure the trigger level, slope, and hysteresis with :py:meth:`niscope.Session.configure_trigger_hysteresis`.

        



    .. py:attribute:: TriggerType.DIGITAL



        Configures the digitizer for digital triggering. A digital trigger occurs when the trigger signal has the specified slope. You configure the trigger slope with :py:meth:`niscope.Session.configure_trigger_digital`.

        



    .. py:attribute:: TriggerType.WINDOW



        Configures the digitizer for window triggering.  A window trigger occurs when the trigger signal enters or leaves the window defined by the values you specify with the Low Window Level, High Window Level, and Window Mode Parameters.  You configure the low window level high window level, and window mode with :py:meth:`niscope.Session.configure_trigger_window`.

        



    .. py:attribute:: TriggerType.SOFTWARE



        Configures the digitizer for software triggering.  A software trigger occurs when :py:meth:`niscope.Session.SendSoftwareTrigger` is called.

        



    .. py:attribute:: TriggerType.TV



        Configures the digitizer for video/TV triggering.   You configure the video trigger parameters like signal Format, Line to trigger off of, Polarity, and Enable DC Restore with :py:meth:`niscope.Session.configure_trigger_video`.

        



    .. py:attribute:: TriggerType.GLITCH



    .. py:attribute:: TriggerType.WIDTH



    .. py:attribute:: TriggerType.RUNT



    .. py:attribute:: TriggerType.IMMEDIATE



        Configures the digitizer for immediate triggering.   An immediate trigger occurs as soon as the pretrigger samples are acquired.

        



TriggerWindowMode
-----------------

.. py:class:: TriggerWindowMode

    .. py:attribute:: TriggerWindowMode.ENTERING



        Trigger upon entering the window

        



    .. py:attribute:: TriggerWindowMode.LEAVING



        Trigger upon leaving the window

        



    .. py:attribute:: TriggerWindowMode.ENTERING_OR_LEAVING



VerticalCoupling
----------------

.. py:class:: VerticalCoupling

    .. py:attribute:: VerticalCoupling.AC



        AC coupling

        



    .. py:attribute:: VerticalCoupling.DC



        DC coupling

        



    .. py:attribute:: VerticalCoupling.GND



        GND coupling

        



VideoPolarity
-------------

.. py:class:: VideoPolarity

    .. py:attribute:: VideoPolarity.POSITIVE



        Specifies that the video signal has positive polarity.

        



    .. py:attribute:: VideoPolarity.NEGATIVE



        Specifies that the video signal has negative polarity.

        



VideoSignalFormat
-----------------

.. py:class:: VideoSignalFormat

    .. py:attribute:: VideoSignalFormat.NTSC



        NTSC signal format supports line numbers from 1 to 525

        



    .. py:attribute:: VideoSignalFormat.PAL



        PAL signal format supports line numbers from 1 to 625

        



    .. py:attribute:: VideoSignalFormat.SECAM



        SECAM signal format supports line numbers from 1 to 625

        



    .. py:attribute:: VideoSignalFormat.M_PAL



        M-PAL signal format supports line numbers from 1 to 525

        



    .. py:attribute:: VideoSignalFormat.VIDEO_480I_59_94_FIELDS_PER_SECOND



        480 lines, interlaced, 59.94 fields per second

        



    .. py:attribute:: VideoSignalFormat.VIDEO_480I_60_FIELDS_PER_SECOND



        480 lines, interlaced, 60 fields per second

        



    .. py:attribute:: VideoSignalFormat.VIDEO_480P_59_94_FRAMES_PER_SECOND



        480 lines, progressive, 59.94 frames per second

        



    .. py:attribute:: VideoSignalFormat.VIDEO_480P_60_FRAMES_PER_SECOND



        480 lines, progressive,60 frames per second

        



    .. py:attribute:: VideoSignalFormat.VIDEO_576I_50_FIELDS_PER_SECOND



        576 lines, interlaced, 50 fields per second

        



    .. py:attribute:: VideoSignalFormat.VIDEO_576P_50_FRAMES_PER_SECOND



        576 lines, progressive, 50 frames per second

        



    .. py:attribute:: VideoSignalFormat.VIDEO_720P_50_FRAMES_PER_SECOND



        720 lines, progressive, 50 frames per second

        



    .. py:attribute:: VideoSignalFormat.VIDEO_720P_59_94_FRAMES_PER_SECOND



        720 lines, progressive, 59.94 frames per second

        



    .. py:attribute:: VideoSignalFormat.VIDEO_720P_60_FRAMES_PER_SECOND



        720 lines, progressive, 60 frames per second

        



    .. py:attribute:: VideoSignalFormat.VIDEO_1080I_50_FIELDS_PER_SECOND



        1,080 lines, interlaced, 50 fields per second

        



    .. py:attribute:: VideoSignalFormat.VIDEO_1080I_59_94_FIELDS_PER_SECOND



        1,080 lines, interlaced, 59.94 fields per second

        



    .. py:attribute:: VideoSignalFormat.VIDEO_1080I_60_FIELDS_PER_SECOND



        1,080 lines, interlaced, 60 fields per second

        



    .. py:attribute:: VideoSignalFormat.VIDEO_1080P_24_FRAMES_PER_SECOND



        1,080 lines, progressive, 24 frames per second

        



VideoTriggerEvent
-----------------

.. py:class:: VideoTriggerEvent

    .. py:attribute:: VideoTriggerEvent.FIELD1



        Trigger on field 1 of the signal

        



    .. py:attribute:: VideoTriggerEvent.FIELD2



        Trigger on field 2 of the signal

        



    .. py:attribute:: VideoTriggerEvent.ANY_FIELD



        Trigger on the first field acquired

        



    .. py:attribute:: VideoTriggerEvent.ANY_LINE



        Trigger on the first line acquired

        



    .. py:attribute:: VideoTriggerEvent.LINE_NUMBER



        Trigger on a specific line of a video signal.  Valid values vary depending on the signal format configured.

        



WhichTrigger
------------

.. py:class:: WhichTrigger

    .. py:attribute:: WhichTrigger.START



    .. py:attribute:: WhichTrigger.ARM_REFERENCE



    .. py:attribute:: WhichTrigger.REFERENCE



    .. py:attribute:: WhichTrigger.ADVANCE



WidthCondition
--------------

.. py:class:: WidthCondition

    .. py:attribute:: WidthCondition.WITHIN



        Trigger on pulses with a duration within the range bounded by :py:attr:`niscope.Session.width_low_threshold` and :py:attr:`niscope.Session.width_high_threshold`.

        



    .. py:attribute:: WidthCondition.OUTSIDE



        Trigger on pulses with a duration not within the range bounded by :py:attr:`niscope.Session.width_low_threshold` and :py:attr:`niscope.Session.width_high_threshold`.

        



WidthPolarity
-------------

.. py:class:: WidthPolarity

    .. py:attribute:: WidthPolarity.POSITIVE



        Trigger on pulses of positive polarity relative to the trigger threshold.

        



    .. py:attribute:: WidthPolarity.NEGATIVE



        Trigger on pulses of negative polarity relative to the trigger threshold.

        



    .. py:attribute:: WidthPolarity.EITHER



        Trigger on pulses of either positive or negative polarity.

        
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/niscope/errors.rst sha256=4670047b1252e491e2484600f72e51b3f9c6b774e4613e5951eb7a2a46252a39 bytes=1910 -->
## FILE: docs/niscope/errors.rst

- repository: `ni/nimi-python`
- source_path: `docs/niscope/errors.rst`
- sha256: `4670047b1252e491e2484600f72e51b3f9c6b774e4613e5951eb7a2a46252a39`
- bytes: 1910

````rst
Exceptions and Warnings
=======================

Error
-----

    .. py:currentmodule:: niscope.errors

    .. exception:: Error

        Base exception type that all NI-SCOPE exceptions derive from


DriverError
-----------

    .. py:currentmodule:: niscope.errors

    .. exception:: DriverError

        An error originating from the NI-SCOPE driver


UnsupportedConfigurationError
-----------------------------

    .. py:currentmodule:: niscope.errors

    .. exception:: UnsupportedConfigurationError

        An error due to using this module in an usupported platform.

DriverNotInstalledError
-----------------------

    .. py:currentmodule:: niscope.errors

    .. exception:: DriverNotInstalledError

        An error due to using this module without the driver runtime installed.

DriverTooOldError
-----------------

    .. py:currentmodule:: niscope.errors

    .. exception:: DriverTooOldError

        An error due to using this module with an older version of the NI-SCOPE driver runtime.

DriverTooNewError
-----------------

    .. py:currentmodule:: niscope.errors

    .. exception:: DriverTooNewError

        An error due to the NI-SCOPE driver runtime being too new for this module.

InvalidRepeatedCapabilityError
------------------------------

    .. py:currentmodule:: niscope.errors

    .. exception:: InvalidRepeatedCapabilityError

        An error due to an invalid character in a repeated capability


SelfTestError
-------------

    .. py:currentmodule:: niscope.errors

    .. exception:: SelfTestError

        An error due to a failed self-test


RpcError
--------

    .. py:currentmodule:: niscope.errors

    .. exception:: RpcError

        An error specific to sessions to the NI gRPC Device Server


DriverWarning
-------------

    .. py:currentmodule:: niscope.errors

    .. exception:: DriverWarning

        A warning originating from the NI-SCOPE driver
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/niscope/examples.rst sha256=b54c237e19d98c6d5959d6a6c841fd7cdce2b71bc2ca982430f804e40829531b bytes=1322 -->
## FILE: docs/niscope/examples.rst

- repository: `ni/nimi-python`
- source_path: `docs/niscope/examples.rst`
- sha256: `b54c237e19d98c6d5959d6a6c841fd7cdce2b71bc2ca982430f804e40829531b`
- bytes: 1322

````rst
Examples
========

`You can download all niscope examples for latest version here <https://github.com/ni/nimi-python/releases/download/1.4.9/niscope_examples.zip>`_

niscope_fetch.py
----------------

.. literalinclude:: ../../src/niscope/examples/niscope_fetch.py
   :language: python
   :linenos:
   :encoding: utf8
   :caption: `(niscope_fetch.py) <https://github.com/ni/nimi-python/blob/master/src/niscope/examples/niscope_fetch.py>`_

niscope_fetch_forever.py
------------------------

.. literalinclude:: ../../src/niscope/examples/niscope_fetch_forever.py
   :language: python
   :linenos:
   :encoding: utf8
   :caption: `(niscope_fetch_forever.py) <https://github.com/ni/nimi-python/blob/master/src/niscope/examples/niscope_fetch_forever.py>`_

niscope_fetch_into.py
---------------------

.. literalinclude:: ../../src/niscope/examples/niscope_fetch_into.py
   :language: python
   :linenos:
   :encoding: utf8
   :caption: `(niscope_fetch_into.py) <https://github.com/ni/nimi-python/blob/master/src/niscope/examples/niscope_fetch_into.py>`_

niscope_read.py
---------------

.. literalinclude:: ../../src/niscope/examples/niscope_read.py
   :language: python
   :linenos:
   :encoding: utf8
   :caption: `(niscope_read.py) <https://github.com/ni/nimi-python/blob/master/src/niscope/examples/niscope_read.py>`_
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/niscope/grpc_session_options.rst sha256=532cfd88dc52a6205e1215c58f79e0323999554777d2e47c3b7e6b407d7319c2 bytes=2890 -->
## FILE: docs/niscope/grpc_session_options.rst

- repository: `ni/nimi-python`
- source_path: `docs/niscope/grpc_session_options.rst`
- sha256: `532cfd88dc52a6205e1215c58f79e0323999554777d2e47c3b7e6b407d7319c2`
- bytes: 2890

````rst
gRPC Support
============

Support for using NI-SCOPE over gRPC

.. py:currentmodule:: niscope



SessionInitializationBehavior
-----------------------------

.. py:class:: SessionInitializationBehavior

    .. py:attribute:: SessionInitializationBehavior.AUTO


        The NI gRPC Device Server will attach to an existing session with the specified name if it exists,
        otherwise the server will initialize a new session.

        .. note:: When using the Session as a context manager and the context exits, the behavior depends on what happened when the constructor
            was called. If it resulted in a new session being initialized on the NI gRPC Device Server, then it will automatically close the
            server session. If it instead attached to an existing session, then it will detach from the server session and leave it open.


    .. py:attribute:: SessionInitializationBehavior.INITIALIZE_SERVER_SESSION


        Require the NI gRPC Device Server to initialize a new session with the specified name.

        .. note:: When using the Session as a context manager and the context exits, it will automatically close the
            server session.


    .. py:attribute:: SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION


        Require the NI gRPC Device Server to attach to an existing session with the specified name.

        .. note:: When using the Session as a context manager and the context exits, it will detach from the server session
            and leave it open.



GrpcSessionOptions
------------------


.. py:class:: GrpcSessionOptions(self, grpc_channel, session_name, initialization_behavior=SessionInitializationBehavior.AUTO)


    Collection of options that specifies session behaviors related to gRPC.

    Creates and returns an object you can pass to a Session constructor.


    :param grpc_channel:
        

        Specifies the channel to the NI gRPC Device Server.

        

    :type grpc_channel: grpc.Channel


    :param session_name:
        

        User-specified name that identifies the driver session on the NI gRPC Device Server.

        This is different from the resource name parameter many APIs take as a separate
        parameter. Specifying a name makes it easy to share sessions across multiple gRPC clients.
        You can use an empty string if you want to always initialize a new session on the server.
        To attach to an existing session, you must specify the session name it was initialized with.

        

    :type session_name: str


    :param initialization_behavior:
        

        Specifies whether it is acceptable to initialize a new session or attach to an existing one, or if only one of the behaviors is desired.

        The driver session exists on the NI gRPC Device Server.

        

    :type initialization_behavior: :py:data:`niscope.SessionInitializationBehavior`
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/niscope/index.rst sha256=7e01d40964a2d33ff348e6999b860e775960d8677e4938f9082ea1481b4901bc bytes=690 -->
## FILE: docs/niscope/index.rst

- repository: `ni/nimi-python`
- source_path: `docs/niscope/index.rst`
- sha256: `7e01d40964a2d33ff348e6999b860e775960d8677e4938f9082ea1481b4901bc`
- bytes: 690

````rst

NI-SCOPE Python API Documentation
=================================

.. include:: about_niscope.inc

.. include:: ../_static/contributing.inc

.. include:: ../_static/support.inc

.. toctree::
   :maxdepth: 3
   :caption: Documentation

   niscope

Additional Documentation
------------------------

Refer to your driver documentation for device-specific information and detailed API documentation.

Refer to the `nimi-python Read the Docs project <https://nimi-python.readthedocs.io/en/stable/>`_ for documentation of versions 1.4.4 of the module or earlier.

.. include:: ../_static/license.inc

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/niscope/installation.inc sha256=80c57871a769e05714a243fb64bedaf70befaeb75ddfc58706ccccc3a27287f0 bytes=425 -->
## FILE: docs/niscope/installation.inc

- repository: `ni/nimi-python`
- source_path: `docs/niscope/installation.inc`
- sha256: `80c57871a769e05714a243fb64bedaf70befaeb75ddfc58706ccccc3a27287f0`
- bytes: 425

````text

.. _niscope_installation-section:

Installation
------------

As a prerequisite to using the **niscope** module, you must install the NI-SCOPE runtime on your system. Visit `ni.com/downloads <http://www.ni.com/downloads/>`_ to download the driver runtime for your devices.

The nimi-python modules (i.e. for **NI-SCOPE**) can be installed with `pip <http://pypi.python.org/pypi/pip>`_::

  $ python -m pip install niscope
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/niscope/niscope.rst sha256=44a7b0d6e92518933968e21155fefcbb73db37f1f4f6be17cbe83037e8b435b9 bytes=127 -->
## FILE: docs/niscope/niscope.rst

- repository: `ni/nimi-python`
- source_path: `docs/niscope/niscope.rst`
- sha256: `44a7b0d6e92518933968e21155fefcbb73db37f1f4f6be17cbe83037e8b435b9`
- bytes: 127

````rst
niscope module
==============

.. include:: installation.inc

.. include:: ../_static/niscope_usage.inc

.. include:: toc.inc
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/niscope/rep_caps.rst sha256=7171d25df0fe09ae1e81aa46f54ef08cf960d37abcbcc8bf098b8236d9f6369b bytes=1450 -->
## FILE: docs/niscope/rep_caps.rst

- repository: `ni/nimi-python`
- source_path: `docs/niscope/rep_caps.rst`
- sha256: `7171d25df0fe09ae1e81aa46f54ef08cf960d37abcbcc8bf098b8236d9f6369b`
- bytes: 1450

````rst
.. py:module:: niscope
    :noindex:

.. py:currentmodule:: niscope.Session

.. role:: c(code)
    :language: c

.. role:: python(code)
    :language: python

Repeated Capabilities
=====================

    Repeated capabilities attributes are used to set the `channel_string` parameter to the
    underlying driver function call. This can be the actual function based on the :py:class:`Session`
    method being called, or it can be the appropriate Get/Set Attribute function, such as :c:`niScope_SetAttributeViInt32()`.

    Repeated capabilities attributes use the indexing operator :python:`[]` to indicate the repeated capabilities.
    The parameter can be a string, list, tuple, or slice (range). Each element of those can be a string or
    an integer. If it is a string, you can indicate a range using the same format as the driver: :python:`'0-2'` or
    :python:`'0:2'`

    Some repeated capabilities use a prefix before the number and this is optional

channels
--------

    .. py:attribute:: niscope.Session.channels[]

        .. code:: python

            session.channels['0-2'].channel_enabled = True

        passes a string of :python:`'0, 1, 2'` to the set attribute function.


instruments
-----------

    .. py:attribute:: niscope.Session.instruments[]

        .. code:: python

            session.instruments['0-2'].channel_enabled = True

        passes a string of :python:`'0, 1, 2'` to the set attribute function.
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/niscope/status.inc sha256=4d97e756ab38a44b6762c672bf6cde5a4e1c696eacb3a99f6357f62f4bc1e0ea bytes=1945 -->
## FILE: docs/niscope/status.inc

- repository: `ni/nimi-python`
- source_path: `docs/niscope/status.inc`
- sha256: `4d97e756ab38a44b6762c672bf6cde5a4e1c696eacb3a99f6357f62f4bc1e0ea`
- bytes: 1945

````text

NI-SCOPE Python API Status
--------------------------

+-------------------------------+------------------------+
| NI-SCOPE (niscope)            |                        |
+===============================+========================+
| Driver Version Tested Against | 2025 Q4                |
+-------------------------------+------------------------+
| PyPI Version                  | |niscopeLatestVersion| |
+-------------------------------+------------------------+
| Supported Python Version      | |niscopePythonVersion| |
+-------------------------------+------------------------+
| Documentation                 | |niscopeDocs|          |
+-------------------------------+------------------------+
| Open Issues                   | |niscopeOpenIssues|    |
+-------------------------------+------------------------+
| Open Pull Requests            | |niscopeOpenPRs|       |
+-------------------------------+------------------------+


.. |niscopeLatestVersion| image:: http://img.shields.io/pypi/v/niscope.svg
    :alt: Latest NI-SCOPE Version
    :target: http://pypi.python.org/pypi/niscope


.. |niscopePythonVersion| image:: http://img.shields.io/pypi/pyversions/niscope.svg
    :alt: NI-SCOPE supported Python versions
    :target: http://pypi.python.org/pypi/niscope


.. |niscopeDocs| image:: https://readthedocs.org/projects/niscope/badge/?version=latest
    :alt: NI-SCOPE Python API Documentation Status
    :target: https://niscope.readthedocs.io/en/latest


.. |niscopeOpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python/niscope.svg
    :alt: Open Issues + Pull Requests for NI-SCOPE
    :target: https://github.com/ni/nimi-python/issues?q=is%3Aopen+is%3Aissue+label%3Aniscope


.. |niscopeOpenPRs| image:: https://img.shields.io/github/issues-pr/ni/nimi-python/niscope.svg
    :alt: Pull Requests for NI-SCOPE
    :target: https://github.com/ni/nimi-python/pulls?q=is%3Aopen+is%3Aissue+label%3Aniscope
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/niscope/toc.inc sha256=4958d5597b4005305d15cdc9a09014d5afa552d460451b042172b99069952975 bytes=121 -->
## FILE: docs/niscope/toc.inc

- repository: `ni/nimi-python`
- source_path: `docs/niscope/toc.inc`
- sha256: `4958d5597b4005305d15cdc9a09014d5afa552d460451b042172b99069952975`
- bytes: 121

````text
API Reference
--------------

.. toctree::

   class
   rep_caps
   enums
   errors
   examples
   grpc_session_options
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nise/.readthedocs.yaml sha256=46969520b6b54aa665563e6218f3a77902e9ad255ed04f506e3cb10616c11aaa bytes=1870 -->
## FILE: docs/nise/.readthedocs.yaml

- repository: `ni/nimi-python`
- source_path: `docs/nise/.readthedocs.yaml`
- sha256: `46969520b6b54aa665563e6218f3a77902e9ad255ed04f506e3cb10616c11aaa`
- bytes: 1870

````yaml
# .readthedocs.yaml
# Read the Docs configuration file
# See https://docs.readthedocs.io/en/stable/config-file/v2.html for details

# Why Use A Configuration File?
# https://docs.readthedocs.io/en/stable/config-file/index.html
# The main advantages of using a configuration file over the web interface are:
# * Settings are per version rather than per project.
# * Settings live in your VCS.
# * They enable reproducible build environments over time.
# * Some settings are only available using a configuration file

# Required
version: 2

# Set the version of Python and other tools you might need
build:
  os: ubuntu-22.04
  tools:
    python: "3.11"
  jobs:
    # pre_build:
    #   # Check for broken external links
    #   - python -m sphinx -b linkcheck -D linkcheck_timeout=1 docs/ _build/linkcheck
    post_checkout:
      # https://docs.readthedocs.io/en/stable/build-customization.html#cancel-build-based-on-a-condition
      # Build-cancellation rules are recommended for monorepos.
      # Cancel building pull requests when there aren't changes in any of these paths: docs/_static/ docs/nise/.
      #
      # If there are no changes (git diff exits with 0) we force the command to return with 183.
      # This is a special exit code on Read the Docs that will cancel the build immediately.
      - |
        if [ "$READTHEDOCS_VERSION_TYPE" = "external" ] && git diff --quiet origin/master -- docs/_static/ docs/nise/;
        then
          exit 183;
        fi

# Have Read the Docs build documentation with Sphinx
sphinx:
  builder: html
  configuration: docs/nise/conf.py

# If using Sphinx, optionally build your docs in additional formats such as PDF
formats:
  - epub
  - pdf

# Declare the Python requirements required to build your docs
python:
  install:
  - requirements: docs/requirements.txt
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nise/about_nise.inc sha256=179e6ebe7967e3f1afce59e79b025212d54d5d3a9344d077e233ab46fb33dd04 bytes=503 -->
## FILE: docs/nise/about_nise.inc

- repository: `ni/nimi-python`
- source_path: `docs/nise/about_nise.inc`
- sha256: `179e6ebe7967e3f1afce59e79b025212d54d5d3a9344d077e233ab46fb33dd04`
- bytes: 503

````text
.. _about-section:

About
=====

The **nise** module provides a Python API for NI Switch Executive. The code is maintained in the Open Source repository for `nimi-python <https://github.com/ni/nimi-python>`_.

Support Policy
--------------
**nise** supports all the Operating Systems supported by NI Switch Executive.

It follows `Python Software Foundation <https://devguide.python.org/#status-of-python-branches>`_ support policy for different versions of CPython.

NI created and supports **nise**.
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nise/class.rst sha256=c65aab17c7f2f00bdf80a21d9594f7da099345ed1a3575dce623696a90bbdde1 bytes=31691 -->
## FILE: docs/nise/class.rst

- repository: `ni/nimi-python`
- source_path: `docs/nise/class.rst`
- sha256: `c65aab17c7f2f00bdf80a21d9594f7da099345ed1a3575dce623696a90bbdde1`
- bytes: 31691

````rst
.. py:module:: nise

Session
=======

.. py:class:: Session(self, virtual_device_name, options={})

    

    Opens a session to a specified NI Switch Executive virtual device. Opens
    communications with all of the IVI switches associated with the
    specified NI Switch Executive virtual device. Returns a session handle
    that you use to identify the virtual device in all subsequent NI Switch
    Executive method calls. NI Switch Executive uses a reference counting
    scheme to manage open session handles to an NI Switch Executive virtual
    device. Each call to :py:meth:`nise.Session.__init__` must be matched with a subsequent
    call to :py:meth:`nise.Session.close`. Successive calls to :py:meth:`nise.Session.__init__` with
    the same virtual device name always returns the same session handle. NI
    Switch Executive disconnects its communication with the IVI switches
    after all session handles are closed to a given virtual device. The
    session handles may be used safely in multiple threads of an
    application. Sessions may only be opened to a given NI Switch Executive
    virtual device from a single process at a time.

    



    :param virtual_device_name:
        

        The name of the NI Switch Executive virtual device.

        


    :type virtual_device_name: str

    :param options:
        

        Specifies the initial value of certain properties for the session. The
        syntax for **options** is a dictionary of properties with an assigned
        value. For example:

        { 'simulate': False }

        You do not have to specify a value for all the properties. If you do not
        specify a value for a property, the default value is used.

        Advanced Example:
        { 'simulate': True, 'driver_setup': { 'Model': '<model number>',  'BoardType': '<type>' } }

        +-------------------------+---------+
        | Property                | Default |
        +=========================+=========+
        | range_check             | True    |
        +-------------------------+---------+
        | query_instrument_status | False   |
        +-------------------------+---------+
        | cache                   | True    |
        +-------------------------+---------+
        | simulate                | False   |
        +-------------------------+---------+
        | record_value_coersions  | False   |
        +-------------------------+---------+
        | driver_setup            | {}      |
        +-------------------------+---------+


    :type options: dict


Methods
=======

close
-----

    .. py:currentmodule:: nise.Session

    .. py:method:: close()

            Reduces the reference count of open sessions by one. If the reference
            count goes to 0, the method deallocates any memory resources the
            driver uses and closes any open IVI switch sessions. After calling the
            :py:meth:`nise.Session.close` method, you should not use the NI Switch Executive
            virtual device again until you call :py:meth:`nise.Session.__init__`.

            

            .. note:: This method is not needed when using the session context manager



connect
-------

    .. py:currentmodule:: nise.Session

    .. py:method:: connect(connect_spec, multiconnect_mode=nise.MulticonnectMode.DEFAULT, wait_for_debounce=True)

            Connects the routes specified by the connection specification. When
            connecting, it may allow for multiconnection based on the
            multiconnection mode. In the event of an error, the call to
            :py:meth:`nise.Session.connect` will attempt to undo any connections made so that the
            system will be left in the same state that it was in before the call was
            made. Some errors can be caught before manipulating hardware, although
            it is feasible that a hardware call could fail causing some connections
            to be momentarily closed and then reopened. If the wait for debounce
            parameter is set, the method will not return until the switch system
            has debounced.

            



            :param connect_spec:


                String describing the connections to be made. The route specification
                strings are best summarized as a series of routes delimited by
                ampersands. The specified routes may be route names, route group names,
                or fully specified route paths delimited by square brackets. Some
                examples of route specification strings are: MyRoute MyRouteGroup
                MyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute & MyRouteGroup &
                [A->Switch1/r0->B] Refer to Route Specification Strings in the NI Switch
                Executive Help for more information.

                


            :type connect_spec: str
            :param multiconnect_mode:


                This value sets the connection mode for the method. The mode might be
                one of the following: :py:data:`~nise.NISE_VAL_USE_DEFAULT_MODE` (-1) - uses the mode
                selected as the default for the route in the NI Switch Executive virtual
                device configuration. If a mode has not been selected for the route in
                the NI Switch Executive virtual device, this parameter defaults to
                :py:data:`~nise.NISE_VAL_MULTICONNECT_ROUTES`. :py:data:`~nise.MulticonnectMode.NO_MULTICONNECT` (0) -
                routes specified in the connection specification must be disconnected
                before they can be reconnected. Calling Connect on a route that was
                connected using No Multiconnect mode results in an error condition.
                :py:data:`~nise.NISE_VAL_MULTICONNECT_ROUTES` (1)- routes specified in the connection
                specification can be connected multiple times. The first call to Connect
                performs the physical hardware connection. Successive calls to Connect
                increase a connection reference count. Similarly, calls to Disconnect
                decrease the reference count. Once it reaches 0, the hardware is
                physically disconnected. Multiconnecting routes applies to entire routes
                and not to route segments.

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type multiconnect_mode: :py:data:`nise.MulticonnectMode`
            :param wait_for_debounce:


                Waits (if true) for switches to debounce between its connect and
                disconnect operations. If false, it immediately begins the second
                operation after completing the first. The order of connect and
                disconnect operation is set by the Operation Order input.

                


            :type wait_for_debounce: bool

connect_and_disconnect
----------------------

    .. py:currentmodule:: nise.Session

    .. py:method:: connect_and_disconnect(connect_spec, disconnect_spec, multiconnect_mode=nise.MulticonnectMode.DEFAULT, operation_order=nise.OperationOrder.AFTER, wait_for_debounce=True)

            Connects routes and disconnects routes in a similar fashion to
            :py:meth:`nise.Session.connect` and :py:meth:`nise.Session.disconnect` except that the operations happen in
            the context of a single method call. This method is useful for
            switching from one state to another state. :py:meth:`nise.Session.connect_and_disconnect`
            manipulates the hardware connections and disconnections only when the
            routes are different between the connection and disconnection
            specifications. If any routes are common between the connection and
            disconnection specifications, NI Switch Executive determines whether or
            not the relays need to be switched. This functionality has the distinct
            advantage of increased throughput for shared connections, because
            hardware does not have to be involved and potentially increases relay
            lifetime by decreasing the number of times that the relay has to be
            switched. In the event of an error, the call to
            :py:meth:`nise.Session.connect_and_disconnect` attempts to undo any connections made, but
            does not attempt to reconnect disconnections. Some errors can be caught
            before manipulating hardware, although it is feasible that a hardware
            call could fail causing some connections to be momentarily closed and
            then reopened.

            



            :param connect_spec:


                String describing the connections to be made. The route specification
                strings are best summarized as a series of routes delimited by
                ampersands. The specified routes may be route names, route group names,
                or fully specified route paths delimited by square brackets. Some
                examples of route specification strings are: MyRoute MyRouteGroup
                MyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute & MyRouteGroup &
                [A->Switch1/r0->B] Refer to Route Specification Strings in the NI Switch
                Executive Help for more information.

                


            :type connect_spec: str
            :param disconnect_spec:


                String describing the disconnections to be made. The route specification
                strings are best summarized as a series of routes delimited by
                ampersands. The specified routes may be route names, route group names,
                or fully specified route paths delimited by square brackets. Some
                examples of route specification strings are: MyRoute MyRouteGroup
                MyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute & MyRouteGroup &
                [A->Switch1/r0->B] Refer to Route Specification Strings in the NI Switch
                Executive Help for more information.

                


            :type disconnect_spec: str
            :param multiconnect_mode:


                This value sets the connection mode for the method. The mode might be
                one of the following: :py:data:`~nise.NISE_VAL_USE_DEFAULT_MODE` (-1) - uses the mode
                selected as the default for the route in the NI Switch Executive virtual
                device configuration. If a mode has not been selected for the route in
                the NI Switch Executive virtual device, this parameter defaults to
                :py:data:`~nise.NISE_VAL_MULTICONNECT_ROUTES`. :py:data:`~nise.MulticonnectMode.NO_MULTICONNECT` (0) -
                routes specified in the connection specification must be disconnected
                before they can be reconnected. Calling Connect on a route that was
                connected using No Multiconnect mode results in an error condition.
                :py:data:`~nise.NISE_VAL_MULTICONNECT_ROUTES` (1) - routes specified in the connection
                specification can be connected multiple times. The first call to Connect
                performs the physical hardware connection. Successive calls to Connect
                increase a connection reference count. Similarly, calls to Disconnect
                decrease the reference count. Once it reaches 0, the hardware is
                physically disconnected. This behavior is slightly different with SPDT
                relays. For more information, refer to the Exclusions and SPDT Relays
                topic in the NI Switch Executive Help. Multiconnecting routes applies to
                entire routes and not to route segments.

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type multiconnect_mode: :py:data:`nise.MulticonnectMode`
            :param operation_order:


                Sets the order of the operation for the method. Defined values are
                Break Before Make and Break After Make. :py:data:`~nise.OperationOrder.BEFORE`
                (1) - The method disconnects the routes specified in the disconnect
                specification before connecting the routes specified in the connect
                specification. This is the typical mode of operation.
                :py:data:`~nise.OperationOrder.AFTER` (2) - The method connects the routes
                specified in the connection specification before connecting the routes
                specified in the disconnection specification. This mode of operation is
                normally used when you are switching current and want to ensure that a
                load is always connected to your source. The order of operation is to
                connect first or disconnect first.

                


            :type operation_order: :py:data:`nise.OperationOrder`
            :param wait_for_debounce:


                Waits (if true) for switches to debounce between its connect and
                disconnect operations. If false, it immediately begins the second
                operation after completing the first. The order of connect and
                disconnect operation is set by the Operation Order input.

                


            :type wait_for_debounce: bool

disconnect
----------

    .. py:currentmodule:: nise.Session

    .. py:method:: disconnect(disconnect_spec)

            Disconnects the routes specified in the Disconnection Specification. If
            any of the specified routes were originally connected in a
            multiconnected mode, the call to :py:meth:`nise.Session.disconnect` reduces the reference
            count on the route by 1. If the reference count reaches 0, it is
            disconnected. If a specified route does not exist, it is an error
            condition. In the event of an error, the call to :py:meth:`nise.Session.disconnect`
            continues to try to disconnect everything specified by the route
            specification string but reports the error on completion.

            



            :param disconnect_spec:


                String describing the disconnections to be made. The route specification
                strings are best summarized as a series of routes delimited by
                ampersands. The specified routes may be route names, route group names,
                or fully specified route paths delimited by square brackets. Some
                examples of route specification strings are: MyRoute MyRouteGroup
                MyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute & MyRouteGroup &
                [A->Switch1/r0->B] Refer to Route Specification Strings in the NI Switch
                Executive Help for more information.

                


            :type disconnect_spec: str

disconnect_all
--------------

    .. py:currentmodule:: nise.Session

    .. py:method:: disconnect_all()

            Disconnects all connections on every IVI switch device managed by the
            NISE session reference passed to this method. :py:meth:`nise.Session.disconnect_all`
            ignores all multiconnect modes. Calling :py:meth:`nise.Session.disconnect_all` resets all
            of the switch states for the system.

            



expand_route_spec
-----------------

    .. py:currentmodule:: nise.Session

    .. py:method:: expand_route_spec(route_spec, expand_action=nise.ExpandAction.ROUTES, expanded_route_spec_size=[1024])

            Expands a route spec string to yield more information about the routes
            and route groups within the spec. The route specification string
            returned from :py:meth:`nise.Session.expand_route_spec` can be passed to other Switch
            Executive API methods (such as :py:meth:`nise.Session.connect`, :py:meth:`nise.Session.disconnect`, and
            :py:meth:`nise.Session.connect_and_disconnect`) that use route specification strings.

            



            :param route_spec:


                String describing the routes and route groups to expand. The route
                specification strings are best summarized as a series of routes
                delimited by ampersands. The specified routes may be route names, route
                group names, or fully specified route paths delimited by square
                brackets. Some examples of route specification strings are: MyRoute
                MyRouteGroup MyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute &
                MyRouteGroup & [A->Switch1/r0->B] Refer to Route Specification Strings
                in the NI Switch Executive Help for more information.

                


            :type route_spec: str
            :param expand_action:


                This value sets the expand action for the method. The action might be
                one of the following: :py:data:`~nise.ExpandAction.ROUTES` (0) - expands the
                route spec to routes. Converts route groups to their constituent routes.
                :py:data:`~nise.ExpandAction.PATHS` (1) - expands the route spec to paths.
                Converts routes and route groups to their constituent square bracket
                route spec strings. Example: [Dev1/c0->Dev1/r0->Dev1/c1]

                


            :type expand_action: :py:data:`nise.ExpandAction`
            :param expanded_route_spec_size:


                The routeSpecSize is an ViInt32 that is passed by reference into the
                method. As an input, it is the size of the route spec string buffer
                being passed. If the route spec string is larger than the string buffer
                being passed, only the portion of the route spec string that can fit in
                the string buffer is copied into it. On return from the method,
                routeSpecSize holds the size required to hold the entire route spec
                string. Note that this size may be larger than the buffer size as the
                method always returns the size needed to hold the entire buffer. You
                may pass NULL for this parameter if you are not interested in the return
                value for routeSpecSize and routeSpec.

                


            :type expanded_route_spec_size: list of int

            :rtype: str
            :return:


                    The expanded route spec. Route specification strings can be directly
                    passed to :py:meth:`nise.Session.connect`, :py:meth:`nise.Session.disconnect`, or :py:meth:`nise.Session.connect_and_disconnect`
                    Refer to Route Specification Strings in the NI Switch Executive Help for
                    more information. You may pass NULL for this parameter if you are not
                    interested in the return value. To obtain the route specification
                    string, you should pass a buffer to this parameter. The size of the
                    buffer required may be obtained by calling the method with NULL for
                    this parameter and a valid ViInt32 to routeSpecSize. The routeSpecSize
                    will contain the size needed to hold the entire route specification
                    (including the NULL termination character). Common operation is to call
                    the method twice. The first time you call the method you can
                    determine the size needed to hold the route specification string.
                    Allocate a buffer of the appropriate size and then re-call the method
                    to obtain the entire buffer.

                    



find_route
----------

    .. py:currentmodule:: nise.Session

    .. py:method:: find_route(channel1, channel2, route_spec_size=[1024])

            Finds an existing or potential route between channel 1 and channel 2.
            The returned route specification contains the route specification and
            the route capability determines whether or not the route existed, is
            possible, or is not possible for various reasons. The route
            specification string returned from :py:meth:`nise.Session.find_route` can be passed to
            other Switch Executive API methods (such as :py:meth:`nise.Session.connect`,
            :py:meth:`nise.Session.disconnect`, and :py:meth:`nise.Session.connect_and_disconnect`) that use route
            specification strings.

            



            :param channel1:


                Channel name of one of the endpoints of the route to find. The channel
                name must either be a channel alias name or a name in the
                device/ivichannel syntax. Examples: MyChannel Switch1/R0

                


            :type channel1: str
            :param channel2:


                Channel name of one of the endpoints of the route to find. The channel
                name must either be a channel alias name or a name in the
                device/ivichannel syntax. Examples: MyChannel Switch1/R0

                


            :type channel2: str
            :param route_spec_size:


                The routeSpecSize is an ViInt32 that is passed by reference into the
                method. As an input, it is the size of the route string buffer being
                passed. If the route string is larger than the string buffer being
                passed, only the portion of the route string that can fit in the string
                buffer is copied into it. On return from the method, routeSpecSize
                holds the size required to hold the entire route string. Note that this
                size may be larger than the buffer size as the method always returns
                the size needed to hold the entire buffer. You may pass NULL for this
                parameter if you are not interested in the return value for
                routeSpecSize and routeSpec.

                


            :type route_spec_size: list of int

            :rtype: tuple (route_spec, path_capability)

                WHERE

                route_spec (str): 


                    The fully specified route path complete with delimiting square
                    brackets if the route exists or is possible. An example of a fully
                    specified route string is: [A->Switch1/r0->B] Route specification
                    strings can be directly passed to :py:meth:`nise.Session.connect`, :py:meth:`nise.Session.disconnect`, or
                    :py:meth:`nise.Session.connect_and_disconnect` Refer to Route Specification Strings in the
                    NI Switch Executive Help for more information. You may pass NULL for
                    this parameter if you are not interested in the return value. To obtain
                    the route specification string, you should pass a buffer to this
                    parameter. The size of the buffer required may be obtained by calling
                    the method with NULL for this parameter and a valid ViInt32 to
                    routeSpecSize. The routeSpecSize will contain the size needed to hold
                    the entire route specification (including the NULL termination
                    character). Common operation is to call the method twice. The first
                    time you call the method you can determine the size needed to hold the
                    route specification string. Allocate a buffer of the appropriate size
                    and then re-call the method to obtain the entire buffer.

                    


                path_capability (:py:data:`nise.PathCapability`): 


                    The return value which expresses the capability of finding a valid route
                    between Channel 1 and Channel 2. Refer to the table below for value
                    descriptions. You may pass NULL for this parameter if you are not
                    interested in the return value. Route capability might be one of the
                    following: Path Available (1) A path between channel 1 and channel 2 is
                    available. The route specification parameter returns a string describing
                    the available path. Path Exists (2) A path between channel 1 and channel
                    2 already exists. The route specification parameter returns a string
                    describing the existing path. Path Unsupported (3) There is no potential
                    path between channel 1 and channel 2 given the current configuration.
                    Resource In Use (4) There is a potential path between channel 1 and
                    channel 2, although a resource needed to complete the path is already in
                    use. Source Conflict (5) Channel 1 and channel 2 cannot be connected
                    because their connection would result in an exclusion violation. Channel
                    Not Available (6) One of the channels is not useable as an endpoint
                    channel. Make sure that it is not marked as a reserved for routing.
                    Channels Hardwired (7) The two channels reside on the same hardwire. An
                    implicit path already exists.

                    



get_all_connections
-------------------

    .. py:currentmodule:: nise.Session

    .. py:method:: get_all_connections(route_spec_size=[1024])

            Returns the top-level connected routes and route groups. The route
            specification string returned from :py:meth:`nise.Session.get_all_connections` can be passed
            to other Switch Executive API methods (such as :py:meth:`nise.Session.connect`,
            :py:meth:`nise.Session.disconnect`, :py:meth:`nise.Session.connect_and_disconnect`, and :py:meth:`nise.Session.expand_route_spec`)
            that use route specification strings.

            



            :param route_spec_size:


                The routeSpecSize is an ViInt32 that is passed by reference into the
                method. As an input, it is the size of the route spec string buffer
                being passed. If the route spec string is larger than the string buffer
                being passed, only the portion of the route spec string that can fit in
                the string buffer is copied into it. On return from the method,
                routeSpecSize holds the size required to hold the entire route spec
                string. Note that this size may be larger than the buffer size as the
                method always returns the size needed to hold the entire buffer. You
                may pass NULL for this parameter if you are not interested in the return
                value for routeSpecSize and routeSpec.

                


            :type route_spec_size: list of int

            :rtype: str
            :return:


                    The route spec of all currently connected routes and route groups. Route
                    specification strings can be directly passed to :py:meth:`nise.Session.connect`,
                    :py:meth:`nise.Session.disconnect`, :py:meth:`nise.Session.connect_and_disconnect`, or :py:meth:`nise.Session.expand_route_spec`
                    Refer to Route Specification Strings in the NI Switch Executive Help for
                    more information. You may pass NULL for this parameter if you are not
                    interested in the return value. To obtain the route specification
                    string, you should pass a buffer to this parameter. The size of the
                    buffer required may be obtained by calling the method with NULL for
                    this parameter and a valid ViInt32 to routeSpecSize. The routeSpecSize
                    will contain the size needed to hold the entire route specification
                    (including the NULL termination character). Common operation is to call
                    the method twice. The first time you call the method you can
                    determine the size needed to hold the route specification string.
                    Allocate a buffer of the appropriate size and then re-call the method
                    to obtain the entire buffer.

                    



is_connected
------------

    .. py:currentmodule:: nise.Session

    .. py:method:: is_connected(route_spec)

            Checks whether the specified routes and routes groups are connected. It
            returns true if connected.

            



            :param route_spec:


                String describing the connections to check. The route specification
                strings are best summarized as a series of routes delimited by
                ampersands. The specified routes may be route names, route group names,
                or fully specified route paths delimited by square brackets. Some
                examples of route specification strings are: MyRoute MyRouteGroup
                MyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute & MyRouteGroup &
                [A->Switch1/r0->B] Refer to Route Specification Strings in the NI Switch
                Executive Help for more information.

                


            :type route_spec: str

            :rtype: bool
            :return:


                    Returns TRUE if the routes and routes groups are connected or FALSE if
                    they are not.

                    



is_debounced
------------

    .. py:currentmodule:: nise.Session

    .. py:method:: is_debounced()

            Checks to see if the switching system is debounced or not. This method
            does not wait for debouncing to occur. It returns true if the system is
            fully debounced. This method is similar to the IviSwtch specific
            method.

            



            :rtype: bool
            :return:


                    Returns TRUE if the system is fully debounced or FALSE if it is still
                    settling.

                    



wait_for_debounce
-----------------

    .. py:currentmodule:: nise.Session

    .. py:method:: wait_for_debounce(maximum_time_ms=hightime.timedelta(milliseconds=-1))

            Waits for all of the switches in the NI Switch Executive virtual device
            to debounce. This method does not return until either the switching
            system is completely debounced and settled or the maximum time has
            elapsed and the system is not yet debounced. In the event that the
            maximum time elapses, the method returns an error indicating that a
            timeout has occurred. To ensure that all of the switches have settled,
            NI recommends calling :py:meth:`nise.Session.wait_for_debounce` after a series of connection
            or disconnection operations and before taking any measurements of the
            signals connected to the switching system.

            



            :param maximum_time_ms:


                The amount of time to wait (in milliseconds) for the debounce to
                complete. A value of 0 checks for debouncing once and returns an error
                if the system is not debounced at that time. A value of -1 means to
                block for an infinite period of time until the system is debounced.

                


            :type maximum_time_ms: hightime.timedelta, datetime.timedelta, or int in milliseconds



.. contents:: Session
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nise/conf.py sha256=b64ac77f756498584ddc72d38fb4f30e4341a247f7827f5905514fa6dd9ad889 bytes=6639 -->
## FILE: docs/nise/conf.py

- repository: `ni/nimi-python`
- source_path: `docs/nise/conf.py`
- sha256: `b64ac77f756498584ddc72d38fb4f30e4341a247f7827f5905514fa6dd9ad889`
- bytes: 6639

````python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# NI Switch Executive Python API documentation build configuration file, created by
# sphinx-quickstart on Fri Jul 14 13:04:36 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../generated'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.doctest',
              'sphinx.ext.intersphinx',
              'sphinx.ext.todo',
              'sphinx.ext.coverage',
              'sphinx.ext.mathjax',
              'sphinx.ext.ifconfig',
              'sphinx.ext.viewcode',
              'sphinx.ext.githubpages']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'NI Switch Executive Python API'
copyright = '2018-2026, National Instruments Corporation'
author = 'NI'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags.
release = '1.4.10.dev0'
# The short X.Y version.
version = release[:3]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'navigation_depth': -1,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../_static']

# Fix wide tables of RTD per https://github.com/rtfd/sphinx_rtd_theme/issues/117#issuecomment-41571653
def setup(app):
    app.add_css_file('theme_overrides.css')

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
        'donate.html',
    ]
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'NIModularInstrumentsPythonAPIdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'NISwitchExecutivePythonAPI.tex', 'NI Switch Executive Python API Documentation',
     'NI', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'niswitchexecutivepythonapi', 'NI Switch Executive Python API Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'NISwitchExecutivePythonAPI', 'NI Switch Executive Python API Documentation',
     author, 'NISwitchExecutivePythonAPI', 'One line description of project.',
     'Miscellaneous'),
]

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'nidcpower': ('https://nidcpower.readthedocs.io/en/latest/', None),
    'nidigital': ('https://nidigital.readthedocs.io/en/latest/', None),
    'nidmm': ('https://nidmm.readthedocs.io/en/latest/', None),
    'nifgen': ('https://nifgen.readthedocs.io/en/latest/', None),
    'nimodinst': ('https://nimodinst.readthedocs.io/en/latest/', None),
    'nirfsg': ('https://nirfsg.readthedocs.io/en/latest/', None),
    'niscope': ('https://niscope.readthedocs.io/en/latest/', None),
    'niswitch': ('https://niswitch.readthedocs.io/en/latest/', None),
    'nitclk': ('https://nitclk.readthedocs.io/en/latest/', None),
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nise/enums.rst sha256=3343aae19f19662691a81148df6a21e7a67de10c8a544f73b8fe6d499b937162 bytes=1801 -->
## FILE: docs/nise/enums.rst

- repository: `ni/nimi-python`
- source_path: `docs/nise/enums.rst`
- sha256: `3343aae19f19662691a81148df6a21e7a67de10c8a544f73b8fe6d499b937162`
- bytes: 1801

````rst
Enums
=====

Enums used in NI Switch Executive

.. py:currentmodule:: nise


ExpandAction
------------

.. py:class:: ExpandAction

    .. py:attribute:: ExpandAction.ROUTES



        Expand to routes

        



    .. py:attribute:: ExpandAction.PATHS



        Expand to paths

        



MulticonnectMode
----------------

.. py:class:: MulticonnectMode

    .. py:attribute:: MulticonnectMode.DEFAULT



        Default

        



    .. py:attribute:: MulticonnectMode.NO_MULTICONNECT



        No multiconnect

        



    .. py:attribute:: MulticonnectMode.MULTICONNECT



        Multiconnect

        



OperationOrder
--------------

.. py:class:: OperationOrder

    .. py:attribute:: OperationOrder.BEFORE



        Break before make

        



    .. py:attribute:: OperationOrder.AFTER



        Break after make

        



PathCapability
--------------

.. py:class:: PathCapability

    .. py:attribute:: PathCapability.PATH_NEEDS_HARDWIRE



        Path needs hardwire

        



    .. py:attribute:: PathCapability.PATH_NEEDS_CONFIG_CHANNEL



        Path needs config channel

        



    .. py:attribute:: PathCapability.PATH_AVAILABLE



        Path available

        



    .. py:attribute:: PathCapability.PATH_EXISTS



        Path exists

        



    .. py:attribute:: PathCapability.PATH_UNSUPPORTED



        Path Unsupported

        



    .. py:attribute:: PathCapability.RESOURCE_IN_USE



        Resource in use

        



    .. py:attribute:: PathCapability.EXCLUSION_CONFLICT



        Exclusion conflict

        



    .. py:attribute:: PathCapability.CHANNEL_NOT_AVAILABLE



        Channel not available

        



    .. py:attribute:: PathCapability.CHANNELS_HARDWIRED



        Channels hardwired

        
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nise/errors.rst sha256=20da5934da8baf8068abdf7e1631c17584ba5b8a83e239b4c0a93afa8051db5e bytes=1632 -->
## FILE: docs/nise/errors.rst

- repository: `ni/nimi-python`
- source_path: `docs/nise/errors.rst`
- sha256: `20da5934da8baf8068abdf7e1631c17584ba5b8a83e239b4c0a93afa8051db5e`
- bytes: 1632

````rst
Exceptions and Warnings
=======================

Error
-----

    .. py:currentmodule:: nise.errors

    .. exception:: Error

        Base exception type that all NI Switch Executive exceptions derive from


DriverError
-----------

    .. py:currentmodule:: nise.errors

    .. exception:: DriverError

        An error originating from the NI Switch Executive driver


UnsupportedConfigurationError
-----------------------------

    .. py:currentmodule:: nise.errors

    .. exception:: UnsupportedConfigurationError

        An error due to using this module in an usupported platform.

DriverNotInstalledError
-----------------------

    .. py:currentmodule:: nise.errors

    .. exception:: DriverNotInstalledError

        An error due to using this module without the driver runtime installed.

DriverTooOldError
-----------------

    .. py:currentmodule:: nise.errors

    .. exception:: DriverTooOldError

        An error due to using this module with an older version of the NI Switch Executive driver runtime.

DriverTooNewError
-----------------

    .. py:currentmodule:: nise.errors

    .. exception:: DriverTooNewError

        An error due to the NI Switch Executive driver runtime being too new for this module.

InvalidRepeatedCapabilityError
------------------------------

    .. py:currentmodule:: nise.errors

    .. exception:: InvalidRepeatedCapabilityError

        An error due to an invalid character in a repeated capability


DriverWarning
-------------

    .. py:currentmodule:: nise.errors

    .. exception:: DriverWarning

        A warning originating from the NI Switch Executive driver
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nise/examples.rst sha256=8dbc5d7954eb36ea86b88433ab8328cb66e17727fc8624899ce79bae117151bc bytes=453 -->
## FILE: docs/nise/examples.rst

- repository: `ni/nimi-python`
- source_path: `docs/nise/examples.rst`
- sha256: `8dbc5d7954eb36ea86b88433ab8328cb66e17727fc8624899ce79bae117151bc`
- bytes: 453

````rst
Examples
========

`You can download all nise examples for latest version here <https://github.com/ni/nimi-python/releases/download/1.4.9/nise_examples.zip>`_

nise_basic_example.py
---------------------

.. literalinclude:: ../../src/nise/examples/nise_basic_example.py
   :language: python
   :linenos:
   :encoding: utf8
   :caption: `(nise_basic_example.py) <https://github.com/ni/nimi-python/blob/master/src/nise/examples/nise_basic_example.py>`_
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nise/index.rst sha256=14f96777e5d65236c94c09858a9e716e4f77c9e4e59c7e92bc07cfd392fa9152 bytes=706 -->
## FILE: docs/nise/index.rst

- repository: `ni/nimi-python`
- source_path: `docs/nise/index.rst`
- sha256: `14f96777e5d65236c94c09858a9e716e4f77c9e4e59c7e92bc07cfd392fa9152`
- bytes: 706

````rst

NI Switch Executive Python API Documentation
============================================

.. include:: about_nise.inc

.. include:: ../_static/contributing.inc

.. include:: ../_static/support.inc

.. toctree::
   :maxdepth: 3
   :caption: Documentation

   nise

Additional Documentation
------------------------

Refer to your driver documentation for device-specific information and detailed API documentation.

Refer to the `nimi-python Read the Docs project <https://nimi-python.readthedocs.io/en/stable/>`_ for documentation of versions 1.4.4 of the module or earlier.

.. include:: ../_static/license.inc

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nise/installation.inc sha256=21d864011530d9eb38398601100776f2ca30a3cc76642dfa1a69ba1a28dbbda4 bytes=438 -->
## FILE: docs/nise/installation.inc

- repository: `ni/nimi-python`
- source_path: `docs/nise/installation.inc`
- sha256: `21d864011530d9eb38398601100776f2ca30a3cc76642dfa1a69ba1a28dbbda4`
- bytes: 438

````text

.. _nise_installation-section:

Installation
------------

As a prerequisite to using the **nise** module, you must install the NI Switch Executive runtime on your system. Visit `ni.com/downloads <http://www.ni.com/downloads/>`_ to download the driver runtime for your devices.

The nimi-python modules (i.e. for **NI Switch Executive**) can be installed with `pip <http://pypi.python.org/pypi/pip>`_::

  $ python -m pip install nise
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nise/nise.rst sha256=8f636d5953bdbc1806769a98184d87bf3a796bde52223492e84304c38bad28af bytes=118 -->
## FILE: docs/nise/nise.rst

- repository: `ni/nimi-python`
- source_path: `docs/nise/nise.rst`
- sha256: `8f636d5953bdbc1806769a98184d87bf3a796bde52223492e84304c38bad28af`
- bytes: 118

````rst
nise module
===========

.. include:: installation.inc

.. include:: ../_static/nise_usage.inc

.. include:: toc.inc
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nise/status.inc sha256=83167abaa6cb4e5e0301fcc8629ac20b999fdefc0aa5b3f8adba8f8a41f4440c bytes=1932 -->
## FILE: docs/nise/status.inc

- repository: `ni/nimi-python`
- source_path: `docs/nise/status.inc`
- sha256: `83167abaa6cb4e5e0301fcc8629ac20b999fdefc0aa5b3f8adba8f8a41f4440c`
- bytes: 1932

````text

NI Switch Executive Python API Status
-------------------------------------

+-------------------------------+---------------------+
| NI Switch Executive (nise)    |                     |
+===============================+=====================+
| Driver Version Tested Against | 2023 Q1             |
+-------------------------------+---------------------+
| PyPI Version                  | |niseLatestVersion| |
+-------------------------------+---------------------+
| Supported Python Version      | |nisePythonVersion| |
+-------------------------------+---------------------+
| Documentation                 | |niseDocs|          |
+-------------------------------+---------------------+
| Open Issues                   | |niseOpenIssues|    |
+-------------------------------+---------------------+
| Open Pull Requests            | |niseOpenPRs|       |
+-------------------------------+---------------------+


.. |niseLatestVersion| image:: http://img.shields.io/pypi/v/nise.svg
    :alt: Latest NI Switch Executive Version
    :target: http://pypi.python.org/pypi/nise


.. |nisePythonVersion| image:: http://img.shields.io/pypi/pyversions/nise.svg
    :alt: NI Switch Executive supported Python versions
    :target: http://pypi.python.org/pypi/nise


.. |niseDocs| image:: https://readthedocs.org/projects/nise/badge/?version=latest
    :alt: NI Switch Executive Python API Documentation Status
    :target: https://nise.readthedocs.io/en/latest


.. |niseOpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python/nise.svg
    :alt: Open Issues + Pull Requests for NI Switch Executive
    :target: https://github.com/ni/nimi-python/issues?q=is%3Aopen+is%3Aissue+label%3Anise


.. |niseOpenPRs| image:: https://img.shields.io/github/issues-pr/ni/nimi-python/nise.svg
    :alt: Pull Requests for NI Switch Executive
    :target: https://github.com/ni/nimi-python/pulls?q=is%3Aopen+is%3Aissue+label%3Anise
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nise/toc.inc sha256=9f626947b2ea26f414ba8e58ed5a7d81e67678fcaf3a517775058e962c8d53d0 bytes=85 -->
## FILE: docs/nise/toc.inc

- repository: `ni/nimi-python`
- source_path: `docs/nise/toc.inc`
- sha256: `9f626947b2ea26f414ba8e58ed5a7d81e67678fcaf3a517775058e962c8d53d0`
- bytes: 85

````text
API Reference
--------------

.. toctree::

   class
   enums
   errors
   examples
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/niswitch/.readthedocs.yaml sha256=637152fa3edb569794e9f38baf0093c29be3755c6f4fe395179c2df8b663d9b6 bytes=1882 -->
## FILE: docs/niswitch/.readthedocs.yaml

- repository: `ni/nimi-python`
- source_path: `docs/niswitch/.readthedocs.yaml`
- sha256: `637152fa3edb569794e9f38baf0093c29be3755c6f4fe395179c2df8b663d9b6`
- bytes: 1882

````yaml
# .readthedocs.yaml
# Read the Docs configuration file
# See https://docs.readthedocs.io/en/stable/config-file/v2.html for details

# Why Use A Configuration File?
# https://docs.readthedocs.io/en/stable/config-file/index.html
# The main advantages of using a configuration file over the web interface are:
# * Settings are per version rather than per project.
# * Settings live in your VCS.
# * They enable reproducible build environments over time.
# * Some settings are only available using a configuration file

# Required
version: 2

# Set the version of Python and other tools you might need
build:
  os: ubuntu-22.04
  tools:
    python: "3.11"
  jobs:
    # pre_build:
    #   # Check for broken external links
    #   - python -m sphinx -b linkcheck -D linkcheck_timeout=1 docs/ _build/linkcheck
    post_checkout:
      # https://docs.readthedocs.io/en/stable/build-customization.html#cancel-build-based-on-a-condition
      # Build-cancellation rules are recommended for monorepos.
      # Cancel building pull requests when there aren't changes in any of these paths: docs/_static/ docs/niswitch/.
      #
      # If there are no changes (git diff exits with 0) we force the command to return with 183.
      # This is a special exit code on Read the Docs that will cancel the build immediately.
      - |
        if [ "$READTHEDOCS_VERSION_TYPE" = "external" ] && git diff --quiet origin/master -- docs/_static/ docs/niswitch/;
        then
          exit 183;
        fi

# Have Read the Docs build documentation with Sphinx
sphinx:
  builder: html
  configuration: docs/niswitch/conf.py

# If using Sphinx, optionally build your docs in additional formats such as PDF
formats:
  - epub
  - pdf

# Declare the Python requirements required to build your docs
python:
  install:
  - requirements: docs/requirements.txt
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/niswitch/about_niswitch.inc sha256=20ebe1ec9765d5f39e4f6903c5f453026f7e35117fb86f3ab1026bf25f740a55 bytes=495 -->
## FILE: docs/niswitch/about_niswitch.inc

- repository: `ni/nimi-python`
- source_path: `docs/niswitch/about_niswitch.inc`
- sha256: `20ebe1ec9765d5f39e4f6903c5f453026f7e35117fb86f3ab1026bf25f740a55`
- bytes: 495

````text
.. _about-section:

About
=====

The **niswitch** module provides a Python API for NI-SWITCH. The code is maintained in the Open Source repository for `nimi-python <https://github.com/ni/nimi-python>`_.

Support Policy
--------------
**niswitch** supports all the Operating Systems supported by NI-SWITCH.

It follows `Python Software Foundation <https://devguide.python.org/#status-of-python-branches>`_ support policy for different versions of CPython.

NI created and supports **niswitch**.
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/niswitch/class.rst sha256=7d56270898ffb2f61b0139cc7fbe6e6554b38a7005eb12088578c6979f6b2c05 bytes=105915 -->
## FILE: docs/niswitch/class.rst

- repository: `ni/nimi-python`
- source_path: `docs/niswitch/class.rst`
- sha256: `7d56270898ffb2f61b0139cc7fbe6e6554b38a7005eb12088578c6979f6b2c05`
- bytes: 105915

````rst
.. py:module:: niswitch

Session
=======

.. py:class:: Session(self, resource_name, topology="Configured Topology", simulate=False, reset_device=False, *, grpc_options=None)

    

    Returns a session handle used to identify the switch in all subsequent
    instrument driver calls and sets the topology of the switch.
    :py:meth:`niswitch.Session.__init__` creates a new IVI instrument driver session
    for the switch specified in the resourceName parameter. The driver uses
    the topology specified in the topology parameter and overrides the
    topology specified in MAX. Note: When initializing an NI SwitchBlock
    device with topology, you must specify the topology created when you
    configured the device in MAX, using either
    "Configured Topology" or the topology string of the
    device. Refer to the Initializing with Topology for NI SwitchBlock
    Devices topic in the NI Switches Help for information about determining
    the topology string of an NI SwitchBlock device. By default, the switch
    is reset to a known state. Enable simulation by specifying the topology
    and setting the simulate parameter to True.

    



    :param resource_name:
        

        Resource name of the switch module to initialize. Default value: None
        Syntax: Optional fields are shown in square brackets ([]). Configured in
        MAX Under Valid Syntax Devices and Interfaces DeviceName Traditional
        NI-DAQ Devices SCXI[chassis ID]::slot number PXI System PXI[bus
        number]::device number TIP: IVI logical names are also valid for the
        resource name. Default values for optional fields: chassis ID = 1 bus
        number = 0 Example resource names: Resource Name Description SC1Mod3
        NI-DAQmx module in chassis "SC1" slot 3 MySwitch NI-DAQmx module renamed
        to "MySwitch" SCXI1::3 Traditional NI-DAQ module in chassis 1, slot 3
        SCXI::3 Traditional NI-DAQ module in chassis 1, slot 3 PXI0::16 PXI bus
        0, device number 16 PXI::16 PXI bus 0, device number 16

        


    :type resource_name: str

    :param topology:
        

        Pass the topology name you want to use for the switch you specify with
        Resource Name parameter. You can also pass
        "Configured Topology" to use the last topology that
        was configured for the device in MAX.
        Default Value:
        "Configured Topology"
        Valid Values:
        "Configured Topology"
        "2501/1-Wire 48x1 Mux"
        "2501/1-Wire 48x1 Amplified Mux"
        "2501/2-Wire 24x1 Mux"
        "2501/2-Wire 24x1 Amplified Mux"
        "2501/2-Wire Dual 12x1 Mux"
        "2501/2-Wire Quad 6x1 Mux"
        "2501/2-Wire 4x6 Matrix"
        "2501/4-Wire 12x1 Mux"
        "2503/1-Wire 48x1 Mux"
        "2503/2-Wire 24x1 Mux"
        "2503/2-Wire Dual 12x1 Mux"
        "2503/2-Wire Quad 6x1 Mux"
        "2503/2-Wire 4x6 Matrix"
        "2503/4-Wire 12x1 Mux"
        "2510/Independent"
        "2512/Independent"
        "2514/Independent"
        "2515/Independent"
        "2520/80-SPST"
        "2521/40-DPST"
        "2522/53-SPDT"
        "2523/26-DPDT"
        "2524/1-Wire 128x1 Mux"
        "2524/1-Wire Dual 64x1 Mux"
        "2524/1-Wire Quad 32x1 Mux"
        "2524/1-Wire Octal 16x1 Mux"
        "2524/1-Wire Sixteen 8x1 Mux"
        "2525/2-Wire 64x1 Mux"
        "2525/2-Wire Dual 32x1 Mux"
        "2525/2-Wire Quad 16x1 Mux"
        "2525/2-Wire Octal 8x1 Mux"
        "2525/2-Wire Sixteen 4x1 Mux"
        "2526/1-Wire 158x1 Mux"
        "2526/2-Wire 79x1 Mux"
        "2527/1-Wire 64x1 Mux"
        "2527/1-Wire Dual 32x1 Mux"
        "2527/2-Wire 32x1 Mux"
        "2527/2-Wire Dual 16x1 Mux"
        "2527/4-Wire 16x1 Mux"
        "2527/Independent"
        "2529/2-Wire Dual 4x16 Matrix"
        "2529/2-Wire 8x16 Matrix"
        "2529/2-Wire 4x32 Matrix"
        "2530/1-Wire 128x1 Mux"
        "2530/1-Wire Dual 64x1 Mux"
        "2530/1-Wire 4x32 Matrix"
        "2530/1-Wire 8x16 Matrix"
        "2530/1-Wire Octal 16x1 Mux"
        "2530/1-Wire Quad 32x1 Mux"
        "2530/2-Wire 4x16 Matrix"
        "2530/2-Wire 64x1 Mux"
        "2530/2-Wire Dual 32x1 Mux"
        "2530/2-Wire Quad 16x1 Mux"
        "2530/4-Wire 32x1 Mux"
        "2530/4-Wire Dual 16x1 Mux"
        "2530/Independent"
        "2531/1-Wire 4x128 Matrix"
        "2531/1-Wire 8x64 Matrix"
        "2531/1-Wire Dual 4x64 Matrix"
        "2531/1-Wire Dual 8x32 Matrix"
        "2531/2-Wire 4x64 Matrix"
        "2531/2-Wire 8x32 Matrix"
        "2532/1-Wire 16x32 Matrix"
        "2532/1-Wire 4x128 Matrix"
        "2532/1-Wire 8x64 Matrix"
        "2532/1-Wire Dual 16x16 Matrix"
        "2532/1-Wire Dual 4x64 Matrix"
        "2532/1-Wire Dual 8x32 Matrix"
        "2532/1-Wire Quad 4x32 Matrix"
        "2532/1-Wire Sixteen 2x16 Matrix"
        "2532/2-Wire 16x16 Matrix"
        "2532/2-Wire 4x64 Matrix"
        "2532/2-Wire 8x32 Matrix"
        "2532/2-Wire Dual 4x32 Matrix"
        "2533/1-Wire 4x64 Matrix"
        "2534/1-Wire 8x32 Matrix"
        "2535/1-Wire 4x136 Matrix"
        "2536/1-Wire 8x68 Matrix"
        "2540/1-Wire 8x9 Matrix"
        "2541/1-Wire 8x12 Matrix"
        "2542/Quad 2x1 Terminated Mux"
        "2543/Dual 4x1 Terminated Mux"
        "2544/8x1 Terminated Mux"
        "2545/4x1 Terminated Mux"
        "2546/Dual 4x1 Mux"
        "2547/8x1 Mux"
        "2548/4-SPDT"
        "2549/Terminated 2-SPDT"
        "2554/4x1 Mux"
        "2555/4x1 Terminated Mux"
        "2556/Dual 4x1 Mux"
        "2557/8x1 Mux"
        "2558/4-SPDT"
        "2559/Terminated 2-SPDT"
        "2564/16-SPST"
        "2564/8-DPST"
        "2565/16-SPST"
        "2566/16-SPDT"
        "2566/8-DPDT"
        "2567/Independent"
        "2568/15-DPST"
        "2568/31-SPST"
        "2569/100-SPST"
        "2569/50-DPST"
        "2570/20-DPDT"
        "2570/40-SPDT"
        "2571/66-SPDT"
        "2575/1-Wire 196x1 Mux"
        "2575/2-Wire 98x1 Mux"
        "2575/2-Wire 95x1 Mux"
        "2576/2-Wire 64x1 Mux"
        "2576/2-Wire Dual 32x1 Mux"
        "2576/2-Wire Octal 8x1 Mux"
        "2576/2-Wire Quad 16x1 Mux"
        "2576/2-Wire Sixteen 4x1 Mux"
        "2576/Independent"
        "2584/1-Wire 12x1 Mux"
        "2584/1-Wire Dual 6x1 Mux"
        "2584/2-Wire 6x1 Mux"
        "2584/Independent"
        "2585/1-Wire 10x1 Mux"
        "2586/10-SPST"
        "2586/5-DPST"
        "2590/4x1 Mux"
        "2591/4x1 Mux"
        "2593/16x1 Mux"
        "2593/8x1 Terminated Mux"
        "2593/Dual 8x1 Mux"
        "2593/Dual 4x1 Terminated Mux"
        "2593/Independent"
        "2594/4x1 Mux"
        "2595/4x1 Mux"
        "2596/Dual 6x1 Mux"
        "2597/6x1 Terminated Mux"
        "2598/Dual Transfer"
        "2599/2-SPDT"
        "2720/Independent"
        "2722/Independent"
        "2725/Independent"
        "2727/Independent"
        "2737/2-Wire 4x64 Matrix"
        "2738/2-Wire 8x32 Matrix"
        "2739/2-Wire 16x16 Matrix"
        "2746/Quad 4x1 Mux"
        "2747/Dual 8x1 Mux"
        "2748/16x1 Mux"
        "2790/Independent"
        "2796/Dual 6x1 Mux"
        "2797/6x1 Terminated Mux"
        "2798/Dual Transfer"
        "2799/2-SPDT"

        


    :type topology: str

    :param simulate:
        

        Enables simulation of the switch module specified in the resource name
        parameter. Valid Values: True - simulate False - Don't simulate
        (Default Value)

        


    :type simulate: bool

    :param reset_device:
        

        Specifies whether to reset the switch module during the initialization
        process. Valid Values: True - Reset Device (Default Value) False
        - Currently unsupported. The device will not reset.

        


    :type reset_device: bool

    :param grpc_options:
        

        MeasurementLink gRPC session options

        


    :type grpc_options: niswitch.GrpcSessionOptions


Methods
=======

abort
-----

    .. py:currentmodule:: niswitch.Session

    .. py:method:: abort()

            Aborts the scan in progress. Initiate a scan with
            :py:meth:`niswitch.Session.initiate`. If the switch module is not scanning,
            NISWITCH_ERROR_NO_SCAN_IN_PROGRESS error is returned.

            



can_connect
-----------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: can_connect(channel1, channel2)

            Verifies that a path between channel 1 and channel 2 can be created. If
            a path is possible in the switch module, the availability of that path
            is returned given the existing connections. If the path is possible but
            in use, a NISWITCH_WARN_IMPLICIT_CONNECTION_EXISTS warning is
            returned.

            



            :param channel1:


                Input one of the channel names of the desired path. Pass the other
                channel name as the channel 2 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: ""

                


            :type channel1: str
            :param channel2:


                Input one of the channel names of the desired path. Pass the other
                channel name as the channel 1 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: ""

                


            :type channel2: str

            :rtype: :py:data:`niswitch.PathCapability`
            :return:


                    Indicates whether a path is valid. Possible values include:

                    - :py:data:`~niswitch.PathCapability.PATH_AVAILABLE` 1
                    - :py:data:`~niswitch.PathCapability.PATH_EXISTS` 2
                    - :py:data:`~niswitch.PathCapability.PATH_UNSUPPORTED` 3
                    - :py:data:`~niswitch.PathCapability.RESOURCE_IN_USE` 4
                    - :py:data:`~niswitch.PathCapability.SOURCE_CONFLICT` 5
                    - :py:data:`~niswitch.PathCapability.CHANNEL_NOT_AVAILABLE` 6

                    Notes: (1)
                    :py:data:`~niswitch.PathCapability.PATH_AVAILABLE` indicates that the driver can create the
                    path at this time. (2) :py:data:`~niswitch.PathCapability.PATH_EXISTS` indicates that the
                    path already exists. (3) :py:data:`~niswitch.PathCapability.PATH_UNSUPPORTED` indicates that
                    the instrument is not capable of creating a path between the channels
                    you specify. (4) :py:data:`~niswitch.PathCapability.RESOURCE_IN_USE` indicates that although
                    the path is valid, the driver cannot create the path at this moment
                    because the switch device is currently using one or more of the required
                    channels to create another path. You must destroy the other path before
                    creating this one. (5) :py:data:`~niswitch.PathCapability.SOURCE_CONFLICT` indicates that
                    the instrument cannot create a path because both channels are connected
                    to a different source channel. (6)
                    :py:data:`~niswitch.PathCapability.CHANNEL_NOT_AVAILABLE` indicates that the driver cannot
                    create a path between the two channels because one of the channels is a
                    configuration channel and thus unavailable for external connections.

                    



close
-----

    .. py:currentmodule:: niswitch.Session

    .. py:method:: close()

            Terminates the NI-SWITCH session and all of its properties and
            deallocates any memory resources the driver uses. Notes: (1) You must
            unlock the session before calling :py:meth:`niswitch.Session._close`. (2) After calling
            :py:meth:`niswitch.Session._close`, you cannot use the instrument driver again until you
            call :py:meth:`niswitch.Session.init` or :py:meth:`niswitch.Session.InitWithOptions`.

            

            .. note:: One or more of the referenced methods are not in the Python API for this driver.

            .. note:: This method is not needed when using the session context manager



commit
------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: commit()

            Downloads the configured scan list and trigger settings to hardware.
            Calling :py:meth:`niswitch.Session.commit` optional as it is implicitly called during
            :py:meth:`niswitch.Session.initiate`. Use :py:meth:`niswitch.Session.commit` to arm triggers in a given
            order or to control when expensive hardware operations are performed.

            



connect
-------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: connect(channel1, channel2)

            Creates a path between channel 1 and channel 2. The driver calculates
            and uses the shortest path between the two channels. Refer to Immediate
            Operations for information about Channel Usage types. If a path is not
            available, the method returns one of the following errors: -
            NISWITCH_ERROR_EXPLICIT_CONNECTION_EXISTS, if the two channels are
            already explicitly connected by calling either the :py:meth:`niswitch.Session.connect` or
            :py:meth:`niswitch.Session.set_path` method. -
            NISWITCH_ERROR_IS_CONFIGURATION_CHANNEL, if a channel is a
            configuration channel. Error elaboration contains information about
            which of the two channels is a configuration channel. -
            NISWITCH_ERROR_ATTEMPT_TO_CONNECT_SOURCES, if both channels are
            connected to a different source. Error elaboration contains information
            about sources channel 1 and 2 connect to. -
            NISWITCH_ERROR_CANNOT_CONNECT_TO_ITSELF, if channels 1 and 2 are
            one and the same channel. - NISWITCH_ERROR_PATH_NOT_FOUND, if the
            driver cannot find a path between the two channels. Note: Paths are
            bidirectional. For example, if a path exists between channels CH1 and
            CH2, then the path also exists between channels CH2 and CH1.

            



            :param channel1:


                Input one of the channel names of the desired path. Pass the other
                channel name as the channel 2 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: None

                


            :type channel1: str
            :param channel2:


                Input one of the channel names of the desired path. Pass the other
                channel name as the channel 1 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: None

                


            :type channel2: str

connect_multiple
----------------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: connect_multiple(connection_list)

            Creates the connections between channels specified in Connection List.
            Specify connections with two endpoints only or the explicit path between
            two endpoints. NI-SWITCH calculates and uses the shortest path between
            the channels. Refer to Setting Source and Configuration Channels for
            information about channel usage types. In the event of an error,
            connecting stops at the point in the list where the error occurred. If a
            path is not available, the method returns one of the following errors:
            - NISWITCH_ERROR_EXPLICIT_CONNECTION_EXISTS, if the two channels are
            already explicitly connected. -
            NISWITCH_ERROR_IS_CONFIGURATION_CHANNEL, if a channel is a
            configuration channel. Error elaboration contains information about
            which of the two channels is a configuration channel. -
            NISWITCH_ERROR_ATTEMPT_TO_CONNECT_SOURCES, if both channels are
            connected to a different source. Error elaboration contains information
            about sources channel 1 and 2 to connect. -
            NISWITCH_ERROR_CANNOT_CONNECT_TO_ITSELF, if channels 1 and 2 are
            one and the same channel. - NISWITCH_ERROR_PATH_NOT_FOUND, if the
            driver cannot find a path between the two channels. Note: Paths are
            bidirectional. For example, if a path exists between channels ch1 and
            ch2, then the path also exists between channels ch1 and ch2.

            



            :param connection_list:


                Connection List specifies a list of connections between channels to
                make. NI-SWITCH validates the connection list, and aborts execution of
                the list if errors are returned. Refer to Connection and Disconnection
                List Syntax for valid connection list syntax and examples. Refer to
                Devices Overview for valid channel names for the switch module. Example
                of a valid connection list: c0 -> r1, [c2 -> r2 -> c3] In this example,
                r2 is a configuration channel. Default value: None

                


            :type connection_list: str

disable
-------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: disable()

            Places the switch module in a quiescent state where it has minimal or no
            impact on the system to which it is connected. All channels are
            disconnected and any scan in progress is aborted.

            



disconnect
----------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: disconnect(channel1, channel2)

            This method destroys the path between two channels that you create
            with the :py:meth:`niswitch.Session.connect` or :py:meth:`niswitch.Session.set_path` method. If a path is
            not connected or not available, the method returns the
            IVISWTCH_ERROR_NO_SUCH_PATH error.

            



            :param channel1:


                Input one of the channel names of the path to break. Pass the other
                channel name as the channel 2 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: None

                


            :type channel1: str
            :param channel2:


                Input one of the channel names of the path to break. Pass the other
                channel name as the channel 1 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: None

                


            :type channel2: str

disconnect_all
--------------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: disconnect_all()

            Breaks all existing paths. If the switch module cannot break all paths,
            NISWITCH_WARN_PATH_REMAINS warning is returned.

            



disconnect_multiple
-------------------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: disconnect_multiple(disconnection_list)

            Breaks the connections between channels specified in Disconnection List.
            If no connections exist between channels, NI-SWITCH returns an error. In
            the event of an error, the VI stops at the point in the list where the
            error occurred.

            



            :param disconnection_list:


                Disconnection List specifies a list of connections between channels to
                break. NI-SWITCH validates the disconnection list, and aborts execution
                of the list if errors are returned. Refer to Connection and
                Disconnection List Syntax for valid disconnection list syntax and
                examples. Refer to Devices Overview for valid channel names for the
                switch module. Example of a valid disconnection list: c0 -> r1, [c2 ->
                r2 -> c3] In this example, r2 is a configuration channel. Default value:
                None

                


            :type disconnection_list: str

get_channel_name
----------------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: get_channel_name(index)

            Returns the channel string that is in the channel table at the specified
            index. Use :py:meth:`niswitch.Session.get_channel_name` in a For Loop to get a complete list
            of valid channel names for the switch module. Use the Channel Count
            property to determine the number of channels.

            



            :param index:


                A 1-based index into the channel table. Default value: 1 Maximum value:
                Value of Channel Count property.

                


            :type index: int

            :rtype: str
            :return:


                    Returns the channel name that is in the channel table at the index you
                    specify.

                    



get_path
--------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: get_path(channel1, channel2)

            Returns a string that identifies the explicit path created with
            :py:meth:`niswitch.Session.connect`. Pass this string to :py:meth:`niswitch.Session.set_path` to establish
            the exact same path in future connections. In some cases, multiple paths
            are available between two channels. When you call :py:meth:`niswitch.Session.connect`, the
            driver selects an available path. With :py:meth:`niswitch.Session.connect`, there is no
            guarantee that the driver selected path will always be the same path
            through the switch module. :py:meth:`niswitch.Session.get_path` only returns those paths
            explicitly created by niSwitch Connect Channels or :py:meth:`niswitch.Session.set_path`.
            For example, if you connect channels CH1 and CH3,and then channels CH2
            and CH3, an explicit path between channels CH1 and CH2 does not exist an
            error is returned

            



            :param channel1:


                Input one of the channel names of the desired path. Pass the other
                channel name as the channel 2 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: ""

                


            :type channel1: str
            :param channel2:


                Input one of the channel names of the desired path. Pass the other
                channel name as the channel 1 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: ""

                


            :type channel2: str

            :rtype: str
            :return:


                    A string composed of comma-separated paths between channel 1 and channel
                    2. The first and last names in the path are the endpoints of the path.
                    All other channels in the path are configuration channels. Examples of
                    returned paths: ch0->com0, com0->ab0

                    



get_relay_count
---------------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: get_relay_count(relay_name)

            Returns the number of times the relay has changed from Closed to Open.
            Relay count is useful for tracking relay lifetime and usage. Call
            :py:meth:`niswitch.Session.wait_for_debounce` before :py:meth:`niswitch.Session.get_relay_count` to ensure an
            accurate count. Refer to the Relay Count topic in the NI Switches Help
            to determine if the switch module supports relay counting.

            



            :param relay_name:


                Name of the relay. Default value: None Examples of valid relay names:
                ch0, ab0, 1wire, hlselect Refer to Devices Overview for a list of valid
                relay names for the switch module.

                


            :type relay_name: str

            :rtype: int
            :return:


                    The number of relay cycles.

                    



get_relay_name
--------------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: get_relay_name(index)

            Returns the relay name string that is in the relay list at the specified
            index. Use :py:meth:`niswitch.Session.get_relay_name` in a For Loop to get a complete list
            of valid relay names for the switch module. Use the Number of Relays
            property to determine the number of relays.

            



            :param index:


                A 1-based index into the channel table. Default value: 1 Maximum value:
                Value of Channel Count property.

                


            :type index: int

            :rtype: str
            :return:


                    Returns the relay name for the index you specify.

                    



get_relay_position
------------------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: get_relay_position(relay_name)

            Returns the relay position for the relay specified in the Relay Name
            parameter.

            



            :param relay_name:


                Name of the relay. Default value: None Examples of valid relay names:
                ch0, ab0, 1wire, hlselect Refer to Devices Overview for a list of valid
                relay names for the switch module.

                


            :type relay_name: str

            :rtype: :py:data:`niswitch.RelayPosition`
            :return:


                    Indicates whether the relay is open or closed. :py:data:`~niswitch.RelayPosition.OPEN` 10
                    :py:data:`~niswitch.RelayPosition.CLOSED` 11

                    



initiate
--------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: initiate()

            Commits the configured scan list and trigger settings to hardware and
            initiates the scan. If niSwitch Commit was called earlier, niSwitch
            Initiate Scan only initiates the scan and returns immediately. Once the
            scanning operation begins, you cannot perform any other operation other
            than GetAttribute, AbortScan, or SendSoftwareTrigger. All other
            methods return NISWITCH_ERROR_SCAN_IN_PROGRESS. To stop the
            scanning operation, To stop the scanning operation, call
            :py:meth:`niswitch.Session.abort`.

            

            .. note:: This method will return a Python context manager that will initiate on entering and abort on exit.



lock
----

    .. py:currentmodule:: niswitch.Session

.. py:method:: lock()

    Obtains a multithread lock on the device session. Before doing so, the
    software waits until all other execution threads release their locks
    on the device session.

    Other threads may have obtained a lock on this session for the
    following reasons:

        -  The application called the :py:meth:`niswitch.Session.lock` method.
        -  A call to NI-SWITCH locked the session.
        -  After a call to the :py:meth:`niswitch.Session.lock` method returns
           successfully, no other threads can access the device session until
           you call the :py:meth:`niswitch.Session.unlock` method or exit out of the with block when using
           lock context manager.
        -  Use the :py:meth:`niswitch.Session.lock` method and the
           :py:meth:`niswitch.Session.unlock` method around a sequence of calls to
           instrument driver methods if you require that the device retain its
           settings through the end of the sequence.

    You can safely make nested calls to the :py:meth:`niswitch.Session.lock` method
    within the same thread. To completely unlock the session, you must
    balance each call to the :py:meth:`niswitch.Session.lock` method with a call to
    the :py:meth:`niswitch.Session.unlock` method.

    One method for ensuring there are the same number of unlock method calls as there is lock calls
    is to use lock as a context manager

        .. code:: python

            with niswitch.Session('dev1') as session:
                with session.lock():
                    # Calls to session within a single lock context

        The first `with` block ensures the session is closed regardless of any exceptions raised

        The second `with` block ensures that unlock is called regardless of any exceptions raised

    :rtype: context manager
    :return:
        When used in a `with` statement, :py:meth:`niswitch.Session.lock` acts as
        a context manager and unlock will be called when the `with` block is exited

relay_control
-------------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: relay_control(relay_name, relay_action)

            Controls individual relays of the switch. When controlling individual
            relays, the protection offered by setting the usage of source channels
            and configuration channels, and by enabling or disabling analog bus
            sharing on the NI SwitchBlock, does not apply. Refer to the device book
            for your switch in the NI Switches Help to determine if the switch
            supports individual relay control.

            



            :param relay_name:


                Name of the relay. Default value: None Examples of valid relay names:
                ch0, ab0, 1wire, hlselect Refer to Devices Overview for a list of valid
                relay names for the switch module.

                


            :type relay_name: str
            :param relay_action:


                Specifies whether to open or close a given relay. Default value: Relay
                Close Defined values: :py:data:`~niswitch.RelayAction.OPEN`
                :py:data:`~niswitch.RelayAction.CLOSE` (Default Value)

                


            :type relay_action: :py:data:`niswitch.RelayAction`

reset
-----

    .. py:currentmodule:: niswitch.Session

    .. py:method:: reset()

            Disconnects all created paths and returns the switch module to the state
            at initialization. Configuration channel and source channel settings
            remain unchanged.

            



reset_with_defaults
-------------------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: reset_with_defaults()

            Resets the switch module and applies initial user specified settings
            from the logical name used to initialize the session. If the session was
            created without a logical name, this method is equivalent to
            :py:meth:`niswitch.Session.reset`.

            



route_scan_advanced_output
--------------------------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: route_scan_advanced_output(scan_advanced_output_connector, scan_advanced_output_bus_line, invert=False)

            Routes the scan advanced output trigger from a trigger bus line (TTLx)
            to the front or rear connector.

            



            :param scan_advanced_output_connector:


                The scan advanced trigger destination. Valid locations are the
                :py:data:`~niswitch.ScanAdvancedOutput.FRONTCONNECTOR` and :py:data:`~niswitch.ScanAdvancedOutput.REARCONNECTOR`. Default
                value: :py:data:`~niswitch.ScanAdvancedOutput.FRONTCONNECTOR`

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type scan_advanced_output_connector: :py:data:`niswitch.ScanAdvancedOutput`
            :param scan_advanced_output_bus_line:


                The trigger line to route the scan advanced output trigger from the
                front or rear connector. Select :py:data:`~niswitch.ScanAdvancedOutput.NONE` to break an existing
                route. Default value: None Valid Values: :py:data:`~niswitch.ScanAdvancedOutput.NONE`
                :py:data:`~niswitch.ScanAdvancedOutput.TTL0` :py:data:`~niswitch.ScanAdvancedOutput.TTL1` :py:data:`~niswitch.ScanAdvancedOutput.TTL2`
                :py:data:`~niswitch.ScanAdvancedOutput.TTL3` :py:data:`~niswitch.ScanAdvancedOutput.TTL4` :py:data:`~niswitch.ScanAdvancedOutput.TTL5`
                :py:data:`~niswitch.ScanAdvancedOutput.TTL6` :py:data:`~niswitch.ScanAdvancedOutput.TTL7`

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type scan_advanced_output_bus_line: :py:data:`niswitch.ScanAdvancedOutput`
            :param invert:


                If True, inverts the input trigger signal from falling to rising or
                vice versa. Default value: False

                


            :type invert: bool

route_trigger_input
-------------------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: route_trigger_input(trigger_input_connector, trigger_input_bus_line, invert=False)

            Routes the input trigger from the front or rear connector to a trigger
            bus line (TTLx). To disconnect the route, call this method again and
            specify None for trigger bus line parameter.

            



            :param trigger_input_connector:


                The location of the input trigger source on the switch module. Valid
                locations are the :py:data:`~niswitch.TriggerInput.FRONTCONNECTOR` and
                :py:data:`~niswitch.TriggerInput.REARCONNECTOR`. Default value:
                :py:data:`~niswitch.TriggerInput.FRONTCONNECTOR`

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type trigger_input_connector: :py:data:`niswitch.TriggerInput`
            :param trigger_input_bus_line:


                The trigger line to route the input trigger. Select :py:data:`~niswitch.NISWITCH_VAL_NONE`
                to break an existing route. Default value: None Valid Values:
                :py:data:`~niswitch.NISWITCH_VAL_NONE` :py:data:`~niswitch.TriggerInput.TTL0` :py:data:`~niswitch.TriggerInput.TTL1`
                :py:data:`~niswitch.TriggerInput.TTL2` :py:data:`~niswitch.TriggerInput.TTL3` :py:data:`~niswitch.TriggerInput.TTL4`
                :py:data:`~niswitch.TriggerInput.TTL5` :py:data:`~niswitch.TriggerInput.TTL6` :py:data:`~niswitch.TriggerInput.TTL7`

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type trigger_input_bus_line: :py:data:`niswitch.TriggerInput`
            :param invert:


                If True, inverts the input trigger signal from falling to rising or
                vice versa. Default value: False

                


            :type invert: bool

self_test
---------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: self_test()

            Verifies that the driver can communicate with the switch module.

            Raises `SelfTestError` on self test failure. Properties on exception object:

            - code - failure code from driver
            - message - status message from driver

            +----------------+------------------+
            | Self-Test Code | Description      |
            +================+==================+
            | 0              | Passed self-test |
            +----------------+------------------+
            | 1              | Self-test failed |
            +----------------+------------------+



send_software_trigger
---------------------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: send_software_trigger()

            Sends a software trigger to the switch module specified in the NI-SWITCH
            session. When the trigger input is set to :py:data:`~niswitch.TriggerInput.SOFTWARE_TRIG`
            through either the :py:meth:`niswitch.Session.ConfigureScanTrigger` or the
            :py:attr:`niswitch.Session.trigger_input` property, the scan does not proceed from
            a semi-colon (wait for trigger) until :py:meth:`niswitch.Session.send_software_trigger` is
            called.

            

            .. note:: One or more of the referenced methods are not in the Python API for this driver.



set_path
--------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: set_path(path_list)

            Connects two channels by specifying an explicit path in the path list
            parameter. :py:meth:`niswitch.Session.set_path` is particularly useful where path
            repeatability is important, such as in calibrated signal paths. If this
            is not necessary, use :py:meth:`niswitch.Session.connect`.

            



            :param path_list:


                A string composed of comma-separated paths between channel 1 and channel
                2. The first and last names in the path are the endpoints of the path.
                Every other channel in the path are configuration channels. Example of a
                valid path list string: ch0->com0, com0->ab0. In this example, com0 is a
                configuration channel. Default value: None Obtain the path list for a
                previously created path with :py:meth:`niswitch.Session.get_path`.

                


            :type path_list: str

unlock
------

    .. py:currentmodule:: niswitch.Session

.. py:method:: unlock()

    Releases a lock that you acquired on an device session using
    :py:meth:`niswitch.Session.lock`. Refer to :py:meth:`niswitch.Session.unlock` for additional
    information on session locks.

wait_for_debounce
-----------------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: wait_for_debounce(maximum_time_ms=hightime.timedelta(milliseconds=5000))

            Pauses until all created paths have settled. If the time you specify
            with the Maximum Time (ms) parameter elapsed before the switch paths
            have settled, this method returns the
            NISWITCH_ERROR_MAX_TIME_EXCEEDED error.

            



            :param maximum_time_ms:


                Specifies the maximum length of time to wait for all relays in the
                switch module to activate or deactivate. If the specified time elapses
                before all relays active or deactivate, a timeout error is returned.
                Default Value:5000 ms

                


            :type maximum_time_ms: hightime.timedelta, datetime.timedelta, or int in milliseconds

wait_for_scan_complete
----------------------

    .. py:currentmodule:: niswitch.Session

    .. py:method:: wait_for_scan_complete(maximum_time_ms=hightime.timedelta(milliseconds=5000))

            Pauses until the switch module stops scanning or the maximum time has
            elapsed and returns a timeout error. If the time you specify with the
            Maximum Time (ms) parameter elapsed before the scanning operation has
            finished, this method returns the NISWITCH_ERROR_MAX_TIME_EXCEEDED
            error.

            



            :param maximum_time_ms:


                Specifies the maximum length of time to wait for the switch module to
                stop scanning. If the specified time elapses before the scan ends,
                NISWITCH_ERROR_MAX_TIME_EXCEEDED error is returned. Default
                Value:5000 ms

                


            :type maximum_time_ms: hightime.timedelta, datetime.timedelta, or int in milliseconds


Properties
==========

analog_bus_sharing_enable
-------------------------

    .. py:attribute:: analog_bus_sharing_enable

        Enables or disables sharing of an analog bus line so that multiple  NI SwitchBlock devices may connect to it simultaneously. To enable  multiple NI SwitchBlock devices to share an analog bus line, set this  property to True for each device on the channel that corresponds  with the shared analog bus line. The default value for all devices is  False, which disables sharing of the analog bus.
        Refer to the Using the Analog Bus on an NI SwitchBlock Carrier topic  in the NI Switches Help for more information about sharing the analog bus.




        .. tip:: This property can be set/get on specific channels within your :py:class:`niswitch.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].analog_bus_sharing_enable`

            To set/get on all channels, you can call the property directly on the :py:class:`niswitch.Session`.

            Example: :py:attr:`my_session.analog_bus_sharing_enable`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Channel Configuration:Analog Bus Sharing Enable**
                - C Attribute: **NISWITCH_ATTR_ANALOG_BUS_SHARING_ENABLE**

bandwidth
---------

    .. py:attribute:: bandwidth

        This channel-based property returns the bandwidth for the channel.
        The units are hertz.




        .. tip:: This property can be set/get on specific channels within your :py:class:`niswitch.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].bandwidth`

            To set/get on all channels, you can call the property directly on the :py:class:`niswitch.Session`.

            Example: :py:attr:`my_session.bandwidth`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | channels  |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Bandwidth**
                - C Attribute: **NISWITCH_ATTR_BANDWIDTH**

channel_count
-------------

    .. py:attribute:: channel_count

        Indicates the number of channels that the specific instrument  driver supports.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Capabilities:Channel Count**
                - C Attribute: **NISWITCH_ATTR_CHANNEL_COUNT**

characteristic_impedance
------------------------

    .. py:attribute:: characteristic_impedance

        This channel-based property returns the characteristic impedance for the  channel.
        The units are ohms.




        .. tip:: This property can be set/get on specific channels within your :py:class:`niswitch.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].characteristic_impedance`

            To set/get on all channels, you can call the property directly on the :py:class:`niswitch.Session`.

            Example: :py:attr:`my_session.characteristic_impedance`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | channels  |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Characteristic Impedance**
                - C Attribute: **NISWITCH_ATTR_CHARACTERISTIC_IMPEDANCE**

continuous_scan
---------------

    .. py:attribute:: continuous_scan

        When a switch device is scanning, the swich can either stop scanning when  the end of the scan (False) or continue scanning from the top of the  scan list again (True).
        Notice that if you set the scan to continuous (True), the Wait For Scan  Complete operation will always time out and you must call Abort to stop  the scan.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Scanning Configuration:Continuous Scan**
                - C Attribute: **NISWITCH_ATTR_CONTINUOUS_SCAN**

digital_filter_enable
---------------------

    .. py:attribute:: digital_filter_enable

        This property specifies whether to apply the pulse width filter to the  Trigger Input. Enabling the Digital Filter (True) prevents the switch  module from being triggered by pulses that are less than 150 ns on PXI  trigger lines 0–7.
        When Digital Filter is disabled (False), it is possible for the switch  module to be triggered by noise on the PXI trigger lines. If the device  triggering the switch is capable of sending pulses greater than 150 ns, you should not disable the Digital Filter.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Scanning Configuration:Digital Filter Enable**
                - C Attribute: **NISWITCH_ATTR_DIGITAL_FILTER_ENABLE**

driver_setup
------------

    .. py:attribute:: driver_setup

        This property indicates the Driver Setup string that the user  specified when initializing the driver.
        Some cases exist where the end-user must specify instrument driver  options at initialization time.  An example of this is specifying  a particular instrument model from among a family of instruments  that the driver supports.  This is useful when using simulation.   The end-user can specify driver-specific options through  the DriverSetup keyword in the optionsString parameter to the  :py:meth:`niswitch.Session.InitWithOptions` method, or through the IVI Configuration Utility.
        If the user does not specify a Driver Setup string, this property returns an empty string.



        .. note:: One or more of the referenced methods are not in the Python API for this driver.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Advanced Session Information:Driver Setup**
                - C Attribute: **NISWITCH_ATTR_DRIVER_SETUP**

handshaking_initiation
----------------------

    .. py:attribute:: handshaking_initiation

        

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------------+
            | Characteristic        | Value                       |
            +=======================+=============================+
            | Datatype              | enums.HandshakingInitiation |
            +-----------------------+-----------------------------+
            | Permissions           | read-write                  |
            +-----------------------+-----------------------------+
            | Repeated Capabilities | None                        |
            +-----------------------+-----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Scanning Configuration:Handshaking Initiation**
                - C Attribute: **NISWITCH_ATTR_HANDSHAKING_INITIATION**

instrument_firmware_revision
----------------------------

    .. py:attribute:: instrument_firmware_revision

        A string that contains the firmware revision information  for the instrument you are currently using.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Firmware Revision**
                - C Attribute: **NISWITCH_ATTR_INSTRUMENT_FIRMWARE_REVISION**

instrument_manufacturer
-----------------------

    .. py:attribute:: instrument_manufacturer

        A string that contains the name of the instrument manufacturer you are currently  using.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Manufacturer**
                - C Attribute: **NISWITCH_ATTR_INSTRUMENT_MANUFACTURER**

instrument_model
----------------

    .. py:attribute:: instrument_model

        A string that contains the model number or name of the instrument that you  are currently using.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Model**
                - C Attribute: **NISWITCH_ATTR_INSTRUMENT_MODEL**

io_resource_descriptor
----------------------

    .. py:attribute:: io_resource_descriptor

        Indicates the resource descriptor the driver  uses to identify the physical device.
        If you initialize the driver with a logical name, this  property contains the resource descriptor that corresponds  to the entry in the IVI Configuration utility.
        If you initialize the instrument driver with the resource  descriptor, this property contains that value.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Advanced Session Information:IO Resource Descriptor**
                - C Attribute: **NISWITCH_ATTR_IO_RESOURCE_DESCRIPTOR**

is_configuration_channel
------------------------

    .. py:attribute:: is_configuration_channel

        This channel-based property specifies whether to reserve the channel for  internal path creation.  A channel that is available for internal path  creation is called a configuration channel.  The driver may use  configuration channels to create paths between two channels you specify in  the :py:meth:`niswitch.Session.connect` method.  Configuration channels are not available  for external connections.
        Set this property to True to mark the channel as a configuration  channel.  Set this property to False to mark the channel as available  for external connections.
        After you identify a channel as a configuration channel, you cannot  use that channel for external connections.  The :py:meth:`niswitch.Session.connect` method  returns the NISWITCH_ERROR_IS_CONFIGURATION_CHANNEL error when you attempt  to establish a connection between a configuration channel and any other  channel.




        .. tip:: This property can be set/get on specific channels within your :py:class:`niswitch.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].is_configuration_channel`

            To set/get on all channels, you can call the property directly on the :py:class:`niswitch.Session`.

            Example: :py:attr:`my_session.is_configuration_channel`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Channel Configuration:Is Configuration Channel**
                - C Attribute: **NISWITCH_ATTR_IS_CONFIGURATION_CHANNEL**

is_debounced
------------

    .. py:attribute:: is_debounced

        This property indicates whether the entire switch device has settled  since the last switching command.  A value of True indicates that all  signals going through the switch device are valid.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | bool      |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Is Debounced**
                - C Attribute: **NISWITCH_ATTR_IS_DEBOUNCED**

is_scanning
-----------

    .. py:attribute:: is_scanning

        If True, the switch module is currently scanning through the scan list  (i.e. it is not in the Idle state). If False, the switch module is not  currently scanning through the scan list (i.e. it is in the Idle state).

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | bool      |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Scanning Configuration:Is Scanning**
                - C Attribute: **NISWITCH_ATTR_IS_SCANNING**

is_source_channel
-----------------

    .. py:attribute:: is_source_channel

        This channel-based property specifies whether you want to identify the  channel as a source channel.  Typically, you set this property to True  when you attach the channel to a power supply, a method generator, or an  active measurement point on the unit under test, and you do not want to  connect the channel to another source.  The driver prevents source  channels from connecting to each other.  The :py:meth:`niswitch.Session.connect` method  returns the NISWITCH_ERROR_ATTEMPT_TO_CONNECT_SOURCES when you attempt to  connect two channels that you identify as source channels.




        .. tip:: This property can be set/get on specific channels within your :py:class:`niswitch.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].is_source_channel`

            To set/get on all channels, you can call the property directly on the :py:class:`niswitch.Session`.

            Example: :py:attr:`my_session.is_source_channel`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | channels   |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Channel Configuration:Is Source Channel**
                - C Attribute: **NISWITCH_ATTR_IS_SOURCE_CHANNEL**

is_waiting_for_trig
-------------------

    .. py:attribute:: is_waiting_for_trig

        In a scan list, a semi-colon (;) is used to indicate that at that point in  the scan list, the scan engine should pause until a trigger is received  from the trigger input.  If that trigger is user generated through either  a hardware pulse or the Send SW Trigger operation, it is necessary for the  user to know  when the scan engine has reached such a state.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | bool      |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Scanning Configuration:Is Waiting for Trigger?**
                - C Attribute: **NISWITCH_ATTR_IS_WAITING_FOR_TRIG**

logical_name
------------

    .. py:attribute:: logical_name

        A string containing the logical name you specified when opening the  current IVI session.
        You may pass a logical name to the :py:meth:`niswitch.Session.init` or  :py:meth:`niswitch.Session.InitWithOptions` methods.   The IVI Configuration utility must contain an entry for the logical name.   The logical name entry refers to a virtual instrument section in the  IVI Configuration file.  The virtual instrument section specifies a physical  device and initial user options.



        .. note:: One or more of the referenced methods are not in the Python API for this driver.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Advanced Session Information:Logical Name**
                - C Attribute: **NISWITCH_ATTR_LOGICAL_NAME**

max_ac_voltage
--------------

    .. py:attribute:: max_ac_voltage

        This channel-based property returns the maximum AC voltage the channel  can switch.
        The units are volts RMS.




        .. tip:: This property can be set/get on specific channels within your :py:class:`niswitch.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].max_ac_voltage`

            To set/get on all channels, you can call the property directly on the :py:class:`niswitch.Session`.

            Example: :py:attr:`my_session.max_ac_voltage`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | channels  |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Maximum AC Voltage**
                - C Attribute: **NISWITCH_ATTR_MAX_AC_VOLTAGE**

max_carry_ac_current
--------------------

    .. py:attribute:: max_carry_ac_current

        This channel-based property returns the maximum AC current the channel  can carry.
        The units are amperes RMS.




        .. tip:: This property can be set/get on specific channels within your :py:class:`niswitch.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].max_carry_ac_current`

            To set/get on all channels, you can call the property directly on the :py:class:`niswitch.Session`.

            Example: :py:attr:`my_session.max_carry_ac_current`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | channels  |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Maximum Carry AC Current**
                - C Attribute: **NISWITCH_ATTR_MAX_CARRY_AC_CURRENT**

max_carry_ac_power
------------------

    .. py:attribute:: max_carry_ac_power

        This channel-based property returns the maximum AC power the channel can  carry.
        The units are volt-amperes.




        .. tip:: This property can be set/get on specific channels within your :py:class:`niswitch.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].max_carry_ac_power`

            To set/get on all channels, you can call the property directly on the :py:class:`niswitch.Session`.

            Example: :py:attr:`my_session.max_carry_ac_power`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | channels  |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Maximum Carry AC Power**
                - C Attribute: **NISWITCH_ATTR_MAX_CARRY_AC_POWER**

max_carry_dc_current
--------------------

    .. py:attribute:: max_carry_dc_current

        This channel-based property returns the maximum DC current the channel  can carry.
        The units are amperes.




        .. tip:: This property can be set/get on specific channels within your :py:class:`niswitch.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].max_carry_dc_current`

            To set/get on all channels, you can call the property directly on the :py:class:`niswitch.Session`.

            Example: :py:attr:`my_session.max_carry_dc_current`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | channels  |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Maximum Carry DC Current**
                - C Attribute: **NISWITCH_ATTR_MAX_CARRY_DC_CURRENT**

max_carry_dc_power
------------------

    .. py:attribute:: max_carry_dc_power

        This channel-based property returns the maximum DC power the channel can  carry.
        The units are watts.




        .. tip:: This property can be set/get on specific channels within your :py:class:`niswitch.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].max_carry_dc_power`

            To set/get on all channels, you can call the property directly on the :py:class:`niswitch.Session`.

            Example: :py:attr:`my_session.max_carry_dc_power`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | channels  |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Maximum Carry DC Power**
                - C Attribute: **NISWITCH_ATTR_MAX_CARRY_DC_POWER**

max_dc_voltage
--------------

    .. py:attribute:: max_dc_voltage

        This channel-based property returns the maximum DC voltage the channel  can switch.
        The units are volts.




        .. tip:: This property can be set/get on specific channels within your :py:class:`niswitch.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].max_dc_voltage`

            To set/get on all channels, you can call the property directly on the :py:class:`niswitch.Session`.

            Example: :py:attr:`my_session.max_dc_voltage`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | channels  |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Maximum DC Voltage**
                - C Attribute: **NISWITCH_ATTR_MAX_DC_VOLTAGE**

max_switching_ac_current
------------------------

    .. py:attribute:: max_switching_ac_current

        This channel-based property returns the maximum AC current the channel  can switch.
        The units are amperes RMS.




        .. tip:: This property can be set/get on specific channels within your :py:class:`niswitch.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].max_switching_ac_current`

            To set/get on all channels, you can call the property directly on the :py:class:`niswitch.Session`.

            Example: :py:attr:`my_session.max_switching_ac_current`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | channels  |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Maximum Switching AC Current**
                - C Attribute: **NISWITCH_ATTR_MAX_SWITCHING_AC_CURRENT**

max_switching_ac_power
----------------------

    .. py:attribute:: max_switching_ac_power

        This channel-based property returns the maximum AC power the channel can  switch.
        The units are volt-amperes.




        .. tip:: This property can be set/get on specific channels within your :py:class:`niswitch.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].max_switching_ac_power`

            To set/get on all channels, you can call the property directly on the :py:class:`niswitch.Session`.

            Example: :py:attr:`my_session.max_switching_ac_power`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | channels  |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Maximum Switching AC Power**
                - C Attribute: **NISWITCH_ATTR_MAX_SWITCHING_AC_POWER**

max_switching_dc_current
------------------------

    .. py:attribute:: max_switching_dc_current

        This channel-based property returns the maximum DC current the channel  can switch.
        The units are amperes.




        .. tip:: This property can be set/get on specific channels within your :py:class:`niswitch.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].max_switching_dc_current`

            To set/get on all channels, you can call the property directly on the :py:class:`niswitch.Session`.

            Example: :py:attr:`my_session.max_switching_dc_current`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | channels  |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Maximum Switching DC Current**
                - C Attribute: **NISWITCH_ATTR_MAX_SWITCHING_DC_CURRENT**

max_switching_dc_power
----------------------

    .. py:attribute:: max_switching_dc_power

        This channel-based property returns the maximum DC power the channel can  switch.
        The units are watts.




        .. tip:: This property can be set/get on specific channels within your :py:class:`niswitch.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].max_switching_dc_power`

            To set/get on all channels, you can call the property directly on the :py:class:`niswitch.Session`.

            Example: :py:attr:`my_session.max_switching_dc_power`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | channels  |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Maximum Switching DC Power**
                - C Attribute: **NISWITCH_ATTR_MAX_SWITCHING_DC_POWER**

number_of_relays
----------------

    .. py:attribute:: number_of_relays

        This property returns the number of relays.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Number of Relays**
                - C Attribute: **NISWITCH_ATTR_NUMBER_OF_RELAYS**

num_of_columns
--------------

    .. py:attribute:: num_of_columns

        This property returns the number of channels on the column of a matrix or  scanner.  If the switch device is a scanner, this value is the number of  input channels.
        The :py:attr:`niswitch.Session.wire_mode` property affects the number of available  columns.  For example, if your device has 8 input lines and you use the  four-wire mode, then the number of columns you have available is 2.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Matrix Configuration:Number of Columns**
                - C Attribute: **NISWITCH_ATTR_NUM_OF_COLUMNS**

num_of_rows
-----------

    .. py:attribute:: num_of_rows

        This property returns the number of channels on the row of a matrix or  scanner.  If the switch device is a scanner, this value is the number of  output channels.
        The :py:attr:`niswitch.Session.wire_mode` property affects the number of available  rows.  For example, if your device has 8 input lines and you use the  two-wire mode, then the number of columns you have available is 4.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Matrix Configuration:Number of Rows**
                - C Attribute: **NISWITCH_ATTR_NUM_OF_ROWS**

power_down_latching_relays_after_debounce
-----------------------------------------

    .. py:attribute:: power_down_latching_relays_after_debounce

        This property specifies whether to power down latching relays after  calling Wait For Debounce.
        When Power Down Latching Relays After Debounce is enabled (True),  a call to Wait For Debounce ensures that the relays are settled  and the latching relays are powered down.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Power Down Latching Relays After Debounce**
                - C Attribute: **NISWITCH_ATTR_POWER_DOWN_LATCHING_RELAYS_AFTER_DEBOUNCE**

scan_advanced_output
--------------------

    .. py:attribute:: scan_advanced_output

        This property specifies the method you want to use to notify another  instrument that all signals going through the switch device have settled  following the processing of one entry in the scan list.

        The following table lists the characteristics of this property.

            +-----------------------+--------------------------+
            | Characteristic        | Value                    |
            +=======================+==========================+
            | Datatype              | enums.ScanAdvancedOutput |
            +-----------------------+--------------------------+
            | Permissions           | read-write               |
            +-----------------------+--------------------------+
            | Repeated Capabilities | None                     |
            +-----------------------+--------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Scanning Configuration:Scan Advanced Output**
                - C Attribute: **NISWITCH_ATTR_SCAN_ADVANCED_OUTPUT**

scan_advanced_polarity
----------------------

    .. py:attribute:: scan_advanced_polarity

        

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------+
            | Characteristic        | Value                      |
            +=======================+============================+
            | Datatype              | enums.ScanAdvancedPolarity |
            +-----------------------+----------------------------+
            | Permissions           | read-write                 |
            +-----------------------+----------------------------+
            | Repeated Capabilities | None                       |
            +-----------------------+----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Scanning Configuration:Scan Advanced Polarity**
                - C Attribute: **NISWITCH_ATTR_SCAN_ADVANCED_POLARITY**

scan_delay
----------

    .. py:attribute:: scan_delay

        This property specifies the minimum amount of time the switch device  waits before it asserts the scan advanced output trigger after opening or  closing the switch.  The switch device always waits for debounce before  asserting the trigger. The units are seconds.
        the greater value of the settling time and the value you specify as the  scan delay.



        .. note:: NI PXI-2501/2503/2565/2590/2591 Users--the actual delay will always be

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------------------------------+
            | Characteristic        | Value                                                       |
            +=======================+=============================================================+
            | Datatype              | hightime.timedelta, datetime.timedelta, or float in seconds |
            +-----------------------+-------------------------------------------------------------+
            | Permissions           | read-write                                                  |
            +-----------------------+-------------------------------------------------------------+
            | Repeated Capabilities | None                                                        |
            +-----------------------+-------------------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Scanning Configuration:Scan Delay**
                - C Attribute: **NISWITCH_ATTR_SCAN_DELAY**

scan_list
---------

    .. py:attribute:: scan_list

        This property contains a scan list, which is a string that specifies  channel connections and trigger conditions.  The :py:meth:`niswitch.Session.initiate`  method makes or breaks connections and waits for triggers according to  the instructions in the scan list.
        The scan list is comprised of channel names that you separate with  special characters.  These special characters determine the operations the  scanner performs on the channels when it executes this scan list.
        To create a path between two channels, use the following character between  the two channel names:
        -> (a dash followed by a '>' sign)
        Example:  'CH1->CH2' tells the switch to make a path from channel CH1 to channel  CH2.
        To break or clear a path, use the following character as a prefix before  the path:
        ~ (tilde)
        Example:  '~CH1->CH2' tells the switch to break the path from channel CH1 to  channel CH2.
        To tell the switch device to wait for a trigger event, use the following  character as a separator between paths:
        ; (semi-colon)
        Example:  'CH1->CH2;CH3->CH4' tells the switch to make the path from channel CH1  to channel CH2, wait for a trigger, and then make the path from CH3 to  CH4.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Scanning Configuration:Scan List**
                - C Attribute: **NISWITCH_ATTR_SCAN_LIST**

scan_mode
---------

    .. py:attribute:: scan_mode

        This property specifies what happens to existing connections that  conflict with the connections you make in a scan list.  For example, if  CH1 is already connected to CH2 and the scan list instructs the switch  device to connect CH1 to CH3, this property specifies what happens to the  connection between CH1 and CH2.
        If the value of this property is :py:data:`~niswitch.ScanMode.NONE`, the switch device  takes no action on existing paths.  If the value is  :py:data:`~niswitch.ScanMode.BREAK_BEFORE_MAKE`, the switch device breaks conflicting paths  before making new ones.  If the value is :py:data:`~niswitch.ScanMode.BREAK_AFTER_MAKE`,  the switch device breaks conflicting paths after making new ones.
        Most switch devices support only one of the possible values.  In such  cases, this property serves as an indicator of the device's behavior.



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +-----------------------+----------------+
            | Characteristic        | Value          |
            +=======================+================+
            | Datatype              | enums.ScanMode |
            +-----------------------+----------------+
            | Permissions           | read-write     |
            +-----------------------+----------------+
            | Repeated Capabilities | None           |
            +-----------------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Scanning Configuration:Scan Mode**
                - C Attribute: **NISWITCH_ATTR_SCAN_MODE**

serial_number
-------------

    .. py:attribute:: serial_number

        This read-only property returns the serial number for the switch device  controlled by this instrument driver.  If the device does not return a  serial number, the driver returns the IVI_ERROR_ATTRIBUTE_NOT_SUPPORTED error.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Serial Number**
                - C Attribute: **NISWITCH_ATTR_SERIAL_NUMBER**

settling_time
-------------

    .. py:attribute:: settling_time

        This channel-based property returns the maximum length of time from after  you make a connection until the signal flowing through the channel  settles. The units are seconds.
        the greater value of the settling time and the value you specify as the  scan delay.



        .. note:: NI PXI-2501/2503/2565/2590/2591 Users--the actual delay will always be


        .. tip:: This property can be set/get on specific channels within your :py:class:`niswitch.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].settling_time`

            To set/get on all channels, you can call the property directly on the :py:class:`niswitch.Session`.

            Example: :py:attr:`my_session.settling_time`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------------------------------+
            | Characteristic        | Value                                                       |
            +=======================+=============================================================+
            | Datatype              | hightime.timedelta, datetime.timedelta, or float in seconds |
            +-----------------------+-------------------------------------------------------------+
            | Permissions           | read-write                                                  |
            +-----------------------+-------------------------------------------------------------+
            | Repeated Capabilities | channels                                                    |
            +-----------------------+-------------------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Settling Time**
                - C Attribute: **NISWITCH_ATTR_SETTLING_TIME**

simulate
--------

    .. py:attribute:: simulate

        Specifies whether or not to simulate instrument driver I/O operations.  If  simulation is enabled, instrument driver methods perform range checking  and call Ivi_GetAttribute and Ivi_SetAttribute methods, but they do not  perform instrument I/O.  For output parameters that represent instrument  data, the instrument driver methods return calculated values.
        The default value is False.   Use the :py:meth:`niswitch.Session.InitWithOptions`  method to override this value.



        .. note:: One or more of the referenced methods are not in the Python API for this driver.

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | bool       |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | None       |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:User Options:Simulate**
                - C Attribute: **NISWITCH_ATTR_SIMULATE**

specific_driver_description
---------------------------

    .. py:attribute:: specific_driver_description

        A string that contains a brief description of the specific  driver.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Description**
                - C Attribute: **NISWITCH_ATTR_SPECIFIC_DRIVER_DESCRIPTION**

specific_driver_revision
------------------------

    .. py:attribute:: specific_driver_revision

        A string that contains additional version information about this  instrument driver.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Revision**
                - C Attribute: **NISWITCH_ATTR_SPECIFIC_DRIVER_REVISION**

specific_driver_vendor
----------------------

    .. py:attribute:: specific_driver_vendor

        A string that contains the name of the vendor that supplies this driver.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Driver Vendor**
                - C Attribute: **NISWITCH_ATTR_SPECIFIC_DRIVER_VENDOR**

supported_instrument_models
---------------------------

    .. py:attribute:: supported_instrument_models

        Contains a comma-separated list of supported instrument models.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | str       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models**
                - C Attribute: **NISWITCH_ATTR_SUPPORTED_INSTRUMENT_MODELS**

temperature
-----------

    .. py:attribute:: temperature

        This property returns the temperature as read by the Switch module.     The units are degrees Celsius.

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | float     |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | None      |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Temperature**
                - C Attribute: **NISWITCH_ATTR_TEMPERATURE**

trigger_input
-------------

    .. py:attribute:: trigger_input

        This property specifies the source of the trigger for which the switch  device can wait when processing a scan list.  The switch device waits for  a trigger when it encounters a semi-colon in a scan list.  When the trigger  occurs, the switch device advances to the next entry in the scan list.

        The following table lists the characteristics of this property.

            +-----------------------+--------------------+
            | Characteristic        | Value              |
            +=======================+====================+
            | Datatype              | enums.TriggerInput |
            +-----------------------+--------------------+
            | Permissions           | read-write         |
            +-----------------------+--------------------+
            | Repeated Capabilities | None               |
            +-----------------------+--------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Scanning Configuration:Trigger Input**
                - C Attribute: **NISWITCH_ATTR_TRIGGER_INPUT**

trigger_input_polarity
----------------------

    .. py:attribute:: trigger_input_polarity

        Determines the behavior of the trigger Input.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------+
            | Characteristic        | Value                      |
            +=======================+============================+
            | Datatype              | enums.TriggerInputPolarity |
            +-----------------------+----------------------------+
            | Permissions           | read-write                 |
            +-----------------------+----------------------------+
            | Repeated Capabilities | None                       |
            +-----------------------+----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Scanning Configuration:Trigger Input Polarity**
                - C Attribute: **NISWITCH_ATTR_TRIGGER_INPUT_POLARITY**

wire_mode
---------

    .. py:attribute:: wire_mode

        This property returns the wire mode of the switch device.
        This property affects the values of the :py:attr:`niswitch.Session.num_of_rows` and  :py:attr:`niswitch.Session.num_of_columns` properties.   The actual number of input and  output lines on the switch device is fixed, but the number of channels  depends on how many lines constitute each channel.




        .. tip:: This property can be set/get on specific channels within your :py:class:`niswitch.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].wire_mode`

            To set/get on all channels, you can call the property directly on the :py:class:`niswitch.Session`.

            Example: :py:attr:`my_session.wire_mode`

        The following table lists the characteristics of this property.

            +-----------------------+-----------+
            | Characteristic        | Value     |
            +=======================+===========+
            | Datatype              | int       |
            +-----------------------+-----------+
            | Permissions           | read only |
            +-----------------------+-----------+
            | Repeated Capabilities | channels  |
            +-----------------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Module Characteristics:Wire mode**
                - C Attribute: **NISWITCH_ATTR_WIRE_MODE**


.. contents:: Session
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/niswitch/conf.py sha256=6223bde7672b678a0d9f6e09dfa6554c0626cb95442fe89bf3a2ff1677781d84 bytes=6545 -->
## FILE: docs/niswitch/conf.py

- repository: `ni/nimi-python`
- source_path: `docs/niswitch/conf.py`
- sha256: `6223bde7672b678a0d9f6e09dfa6554c0626cb95442fe89bf3a2ff1677781d84`
- bytes: 6545

````python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# NI-SWITCH Python API documentation build configuration file, created by
# sphinx-quickstart on Fri Jul 14 13:04:36 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../generated'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.doctest',
              'sphinx.ext.intersphinx',
              'sphinx.ext.todo',
              'sphinx.ext.coverage',
              'sphinx.ext.mathjax',
              'sphinx.ext.ifconfig',
              'sphinx.ext.viewcode',
              'sphinx.ext.githubpages']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'NI-SWITCH Python API'
copyright = '2017-2026, National Instruments Corporation'
author = 'NI'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags.
release = '1.4.10.dev0'
# The short X.Y version.
version = release[:3]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'navigation_depth': -1,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../_static']

# Fix wide tables of RTD per https://github.com/rtfd/sphinx_rtd_theme/issues/117#issuecomment-41571653
def setup(app):
    app.add_css_file('theme_overrides.css')

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
        'donate.html',
    ]
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'NIModularInstrumentsPythonAPIdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'NISWITCHPythonAPI.tex', 'NI-SWITCH Python API Documentation',
     'NI', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'niswitchpythonapi', 'NI-SWITCH Python API Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'NISWITCHPythonAPI', 'NI-SWITCH Python API Documentation',
     author, 'NISWITCHPythonAPI', 'One line description of project.',
     'Miscellaneous'),
]

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'nidcpower': ('https://nidcpower.readthedocs.io/en/latest/', None),
    'nidigital': ('https://nidigital.readthedocs.io/en/latest/', None),
    'nidmm': ('https://nidmm.readthedocs.io/en/latest/', None),
    'nifgen': ('https://nifgen.readthedocs.io/en/latest/', None),
    'nimodinst': ('https://nimodinst.readthedocs.io/en/latest/', None),
    'nirfsg': ('https://nirfsg.readthedocs.io/en/latest/', None),
    'niscope': ('https://niscope.readthedocs.io/en/latest/', None),
    'nise': ('https://nise.readthedocs.io/en/latest/', None),
    'nitclk': ('https://nitclk.readthedocs.io/en/latest/', None),
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/niswitch/enums.rst sha256=fb23c9f2888a3f9f72aa0e8258b8b80cfb4a369b3c005b2863c948c4da4bbcc2 bytes=17276 -->
## FILE: docs/niswitch/enums.rst

- repository: `ni/nimi-python`
- source_path: `docs/niswitch/enums.rst`
- sha256: `fb23c9f2888a3f9f72aa0e8258b8b80cfb4a369b3c005b2863c948c4da4bbcc2`
- bytes: 17276

````rst
Enums
=====

Enums used in NI-SWITCH

.. py:currentmodule:: niswitch


HandshakingInitiation
---------------------

.. py:class:: HandshakingInitiation

    .. py:attribute:: HandshakingInitiation.MEASUREMENT_DEVICE



        The `niSwitch Initiate
        Scan <switchviref.chm::/:py:meth:`niswitch.Session.Initiate_Scan`.html>`__ VI does not
        return until the switch hardware is waiting for a trigger input. This
        ensures that if you initiate the measurement device after calling the
        `niSwitch Initiate
        Scan <switchviref.chm::/:py:meth:`niswitch.Session.Initiate_Scan`.html>`__ VI , the switch
        is sure to receive the first measurement complete (MC) signal sent by
        the measurement device. The measurement device should be configured to
        first take a measurement, send MC, then wait for scanner advanced output
        signal. Thus, the first MC of the measurement device initiates
        handshaking.

        



    .. py:attribute:: HandshakingInitiation.SWITCH



        The `niSwitch Initiate
        Scan <switchviref.chm::/:py:meth:`niswitch.Session.Initiate_Scan`.html>`__ VI returns
        immediately after beginning scan list execution. It is assumed that the
        measurement device has already been configured and is waiting for the
        scanner advanced signal. The measurement should be configured to first
        wait for a trigger, then take a measurement. Thus, the first scanner
        advanced output signal of the switch module initiates handshaking.

        



PathCapability
--------------

.. py:class:: PathCapability

    .. py:attribute:: PathCapability.PATH_AVAILABLE



        Path Available

        



    .. py:attribute:: PathCapability.PATH_EXISTS



        Path Exists

        



    .. py:attribute:: PathCapability.PATH_UNSUPPORTED



        Path Unsupported

        



    .. py:attribute:: PathCapability.RESOURCE_IN_USE



        Resource in use

        



    .. py:attribute:: PathCapability.SOURCE_CONFLICT



        Source conflict

        



    .. py:attribute:: PathCapability.CHANNEL_NOT_AVAILABLE



        Channel not available

        



RelayAction
-----------

.. py:class:: RelayAction

    .. py:attribute:: RelayAction.OPEN



        Open Relay

        



    .. py:attribute:: RelayAction.CLOSE



        Close Relay

        



RelayPosition
-------------

.. py:class:: RelayPosition

    .. py:attribute:: RelayPosition.OPEN



        Open

        



    .. py:attribute:: RelayPosition.CLOSED



        Closed

        



ScanAdvancedOutput
------------------

.. py:class:: ScanAdvancedOutput

    .. py:attribute:: ScanAdvancedOutput.NONE



        The switch device does not produce a Scan Advanced Output trigger.

        



    .. py:attribute:: ScanAdvancedOutput.EXTERNAL



        External Trigger. The switch device produces the Scan Advanced Output  trigger on the external trigger output.

        



    .. py:attribute:: ScanAdvancedOutput.TTL0



        The switch device produces the Scan Advanced Output on the PXI TRIG0 line.

        



    .. py:attribute:: ScanAdvancedOutput.TTL1



        The switch device produces the Scan Advanced Output on the PXI TRIG1 line.

        



    .. py:attribute:: ScanAdvancedOutput.TTL2



        The switch device produces the Scan Advanced Output on the PXI TRIG2 line.

        



    .. py:attribute:: ScanAdvancedOutput.TTL3



        The switch device produces the Scan Advanced Output on the PXI TRIG3 line.

        



    .. py:attribute:: ScanAdvancedOutput.TTL4



        The switch device produces the Scan Advanced Output on the PXI TRIG4 line.

        



    .. py:attribute:: ScanAdvancedOutput.TTL5



        The switch device produces the Scan Advanced Output on the PXI TRIG5 line.

        



    .. py:attribute:: ScanAdvancedOutput.TTL6



        The switch device produces the Scan Advanced Output on the PXI TRIG6 line.

        



    .. py:attribute:: ScanAdvancedOutput.TTL7



        The switch device produces the Scan Advanced Output on the PXI TRIG7 line.

        



    .. py:attribute:: ScanAdvancedOutput.PXI_STAR



        The switch module produces the Scan Advanced Output Trigger on the PXI
        Star trigger bus before processing the next entry in the scan list.

        



    .. py:attribute:: ScanAdvancedOutput.REARCONNECTOR



        The switch device produces the Scan Advanced Output  trigger on the rear connector.

        



    .. py:attribute:: ScanAdvancedOutput.FRONTCONNECTOR



        The switch device produces the Scan Advanced Output  trigger on the front connector.

        



    .. py:attribute:: ScanAdvancedOutput.REARCONNECTOR_MODULE1



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 1.

        



    .. py:attribute:: ScanAdvancedOutput.REARCONNECTOR_MODULE2



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 2.

        



    .. py:attribute:: ScanAdvancedOutput.REARCONNECTOR_MODULE3



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 3.

        



    .. py:attribute:: ScanAdvancedOutput.REARCONNECTOR_MODULE4



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 4.

        



    .. py:attribute:: ScanAdvancedOutput.REARCONNECTOR_MODULE5



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 5.

        



    .. py:attribute:: ScanAdvancedOutput.REARCONNECTOR_MODULE6



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 6.

        



    .. py:attribute:: ScanAdvancedOutput.REARCONNECTOR_MODULE7



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 7.

        



    .. py:attribute:: ScanAdvancedOutput.REARCONNECTOR_MODULE8



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 8.

        



    .. py:attribute:: ScanAdvancedOutput.REARCONNECTOR_MODULE9



        The switch module produces the Scan Advanced Ouptut Trigger on the rear
        connector module 9.

        



    .. py:attribute:: ScanAdvancedOutput.REARCONNECTOR_MODULE10



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 10.

        



    .. py:attribute:: ScanAdvancedOutput.REARCONNECTOR_MODULE11



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 11.

        



    .. py:attribute:: ScanAdvancedOutput.REARCONNECTOR_MODULE12



        The switch module produces the Scan Advanced Output Trigger on the rear
        connector module 12.

        



    .. py:attribute:: ScanAdvancedOutput.FRONTCONNECTOR_MODULE1



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 1.

        



    .. py:attribute:: ScanAdvancedOutput.FRONTCONNECTOR_MODULE2



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 2.

        



    .. py:attribute:: ScanAdvancedOutput.FRONTCONNECTOR_MODULE3



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 3.

        



    .. py:attribute:: ScanAdvancedOutput.FRONTCONNECTOR_MODULE4



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 4.

        



    .. py:attribute:: ScanAdvancedOutput.FRONTCONNECTOR_MODULE5



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 5.

        



    .. py:attribute:: ScanAdvancedOutput.FRONTCONNECTOR_MODULE6



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 6.

        



    .. py:attribute:: ScanAdvancedOutput.FRONTCONNECTOR_MODULE7



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 7.

        



    .. py:attribute:: ScanAdvancedOutput.FRONTCONNECTOR_MODULE8



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 8.

        



    .. py:attribute:: ScanAdvancedOutput.FRONTCONNECTOR_MODULE9



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 9.

        



    .. py:attribute:: ScanAdvancedOutput.FRONTCONNECTOR_MODULE10



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 10.

        



    .. py:attribute:: ScanAdvancedOutput.FRONTCONNECTOR_MODULE11



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 11.

        



    .. py:attribute:: ScanAdvancedOutput.FRONTCONNECTOR_MODULE12



        The switch module produces the Scan Advanced Output Trigger on the front
        connector module 12.

        



ScanAdvancedPolarity
--------------------

.. py:class:: ScanAdvancedPolarity

    .. py:attribute:: ScanAdvancedPolarity.RISING



        The trigger occurs on the rising edge of the signal.

        



    .. py:attribute:: ScanAdvancedPolarity.FALLING



        The trigger occurs on the falling edge of the signal.

        



ScanMode
--------

.. py:class:: ScanMode

    .. py:attribute:: ScanMode.NONE



        No implicit action on connections when scanning.

        



    .. py:attribute:: ScanMode.BREAK_BEFORE_MAKE



        When scanning, the switch device breaks existing connections before  making new connections.

        



    .. py:attribute:: ScanMode.BREAK_AFTER_MAKE



        When scanning, the switch device breaks existing connections after making  new connections.

        



TriggerInput
------------

.. py:class:: TriggerInput

    .. py:attribute:: TriggerInput.IMMEDIATE



        Immediate Trigger. The switch device does not wait for a trigger before  processing the next entry in the scan list.

        



    .. py:attribute:: TriggerInput.EXTERNAL



        External Trigger. The switch device waits until it receives a trigger  from an external source through the external trigger input before  processing the next entry in the scan list.

        



    .. py:attribute:: TriggerInput.SOFTWARE_TRIG



        The switch device waits until you call the :py:meth:`niswitch.Session.send_software_trigger`  method before processing the next entry in the scan list.

        



    .. py:attribute:: TriggerInput.TTL0



        The switch device waits until it receives a trigger on the PXI TRIG0 line before processing the next entry in the scan list.

        



    .. py:attribute:: TriggerInput.TTL1



        The switch device waits until it receives a trigger on the PXI TRIG1 line before processing the next entry in the scan list.

        



    .. py:attribute:: TriggerInput.TTL2



        The switch device waits until it receives a trigger on the PXI TRIG2 line before processing the next entry in the scan list.

        



    .. py:attribute:: TriggerInput.TTL3



        The switch device waits until it receives a trigger on the PXI TRIG3 line before processing the next entry in the scan list.

        



    .. py:attribute:: TriggerInput.TTL4



        The switch device waits until it receives a trigger on the PXI TRIG4 line before processing the next entry in the scan list.

        



    .. py:attribute:: TriggerInput.TTL5



        The switch device waits until it receives a trigger on the PXI TRIG5 line before processing the next entry in the scan list.

        



    .. py:attribute:: TriggerInput.TTL6



        The switch device waits until it receives a trigger on the PXI TRIG6 line before processing the next entry in the scan list.

        



    .. py:attribute:: TriggerInput.TTL7



        The switch device waits until it receives a trigger on the PXI TRIG7 line before processing the next entry in the scan list.

        



    .. py:attribute:: TriggerInput.PXI_STAR



        The switch device waits until it receives a trigger on the PXI STAR  trigger bus before processing the next entry in the scan list.

        



    .. py:attribute:: TriggerInput.REARCONNECTOR



        The switch device waits until it receives a trigger on the  rear connector.

        



    .. py:attribute:: TriggerInput.FRONTCONNECTOR



        The switch device waits until it receives a trigger on the  front connector.

        



    .. py:attribute:: TriggerInput.REARCONNECTOR_MODULE1



        The switch module waits until it receives a trigger on the rear
        connector module 1.

        



    .. py:attribute:: TriggerInput.REARCONNECTOR_MODULE2



        The switch module waits until it receives a trigger on the rear
        connector module 2.

        



    .. py:attribute:: TriggerInput.REARCONNECTOR_MODULE3



        The switch module waits until it receives a trigger on the rear
        connector module 3.

        



    .. py:attribute:: TriggerInput.REARCONNECTOR_MODULE4



        The switch module waits until it receives a trigger on the rear
        connector module 4.

        



    .. py:attribute:: TriggerInput.REARCONNECTOR_MODULE5



        The switch module waits until it receives a trigger on the rear
        connector module 5.

        



    .. py:attribute:: TriggerInput.REARCONNECTOR_MODULE6



        The switch module waits until it receives a trigger on the rear
        connector module 6.

        



    .. py:attribute:: TriggerInput.REARCONNECTOR_MODULE7



        The switch module waits until it receives a trigger on the rear
        connector module 7.

        



    .. py:attribute:: TriggerInput.REARCONNECTOR_MODULE8



        The switch module waits until it receives a trigger on the rear
        connector module 8.

        



    .. py:attribute:: TriggerInput.REARCONNECTOR_MODULE9



        The switch module waits until it receives a trigger on the rear
        connector module 9.

        



    .. py:attribute:: TriggerInput.REARCONNECTOR_MODULE10



        The switch module waits until it receives a trigger on the rear
        connector module 10.

        



    .. py:attribute:: TriggerInput.REARCONNECTOR_MODULE11



        The switch module waits until it receives a trigger on the rear
        connector module 11.

        



    .. py:attribute:: TriggerInput.REARCONNECTOR_MODULE12



        The switch module waits until it receives a trigger on the rear
        connector module 12.

        



    .. py:attribute:: TriggerInput.FRONTCONNECTOR_MODULE1



        The switch module waits until it receives a trigger on the front
        connector module 1.

        



    .. py:attribute:: TriggerInput.FRONTCONNECTOR_MODULE2



        The switch module waits until it receives a trigger on the front
        connector module 2.

        



    .. py:attribute:: TriggerInput.FRONTCONNECTOR_MODULE3



        The switch module waits until it receives a trigger on the front
        connector module 3.

        



    .. py:attribute:: TriggerInput.FRONTCONNECTOR_MODULE4



        The switch module waits until it receives a trigger on the front
        connector module 4.

        



    .. py:attribute:: TriggerInput.FRONTCONNECTOR_MODULE5



        The switch module waits until it receives a trigger on the front
        connector module 5.

        



    .. py:attribute:: TriggerInput.FRONTCONNECTOR_MODULE6



        The switch module waits until it receives a trigger on the front
        connector module 6.

        



    .. py:attribute:: TriggerInput.FRONTCONNECTOR_MODULE7



        The switch module waits until it receives a trigger on the front
        connector module 7.

        



    .. py:attribute:: TriggerInput.FRONTCONNECTOR_MODULE8



        The switch module waits until it receives a trigger on the front
        connector module 8.

        



    .. py:attribute:: TriggerInput.FRONTCONNECTOR_MODULE9



        The switch module waits until it receives a trigger on the front
        connector module 9.

        



    .. py:attribute:: TriggerInput.FRONTCONNECTOR_MODULE10



        The switch module waits until it receives a trigger on the front
        connector module 10.

        



    .. py:attribute:: TriggerInput.FRONTCONNECTOR_MODULE11



        The switch module waits until it receives a trigger on the front
        connector module 11.

        



    .. py:attribute:: TriggerInput.FRONTCONNECTOR_MODULE12



        The switch module waits until it receives a trigger on the front
        connector module 12.

        



TriggerInputPolarity
--------------------

.. py:class:: TriggerInputPolarity

    .. py:attribute:: TriggerInputPolarity.RISING



        The trigger occurs on the rising edge of the signal.

        



    .. py:attribute:: TriggerInputPolarity.FALLING



        The trigger occurs on the falling edge of the signal.

        
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/niswitch/errors.rst sha256=f1371f10dcfa4d775cc656e3878cb5bcd4af49a04224853166d913228541997b bytes=1925 -->
## FILE: docs/niswitch/errors.rst

- repository: `ni/nimi-python`
- source_path: `docs/niswitch/errors.rst`
- sha256: `f1371f10dcfa4d775cc656e3878cb5bcd4af49a04224853166d913228541997b`
- bytes: 1925

````rst
Exceptions and Warnings
=======================

Error
-----

    .. py:currentmodule:: niswitch.errors

    .. exception:: Error

        Base exception type that all NI-SWITCH exceptions derive from


DriverError
-----------

    .. py:currentmodule:: niswitch.errors

    .. exception:: DriverError

        An error originating from the NI-SWITCH driver


UnsupportedConfigurationError
-----------------------------

    .. py:currentmodule:: niswitch.errors

    .. exception:: UnsupportedConfigurationError

        An error due to using this module in an usupported platform.

DriverNotInstalledError
-----------------------

    .. py:currentmodule:: niswitch.errors

    .. exception:: DriverNotInstalledError

        An error due to using this module without the driver runtime installed.

DriverTooOldError
-----------------

    .. py:currentmodule:: niswitch.errors

    .. exception:: DriverTooOldError

        An error due to using this module with an older version of the NI-SWITCH driver runtime.

DriverTooNewError
-----------------

    .. py:currentmodule:: niswitch.errors

    .. exception:: DriverTooNewError

        An error due to the NI-SWITCH driver runtime being too new for this module.

InvalidRepeatedCapabilityError
------------------------------

    .. py:currentmodule:: niswitch.errors

    .. exception:: InvalidRepeatedCapabilityError

        An error due to an invalid character in a repeated capability


SelfTestError
-------------

    .. py:currentmodule:: niswitch.errors

    .. exception:: SelfTestError

        An error due to a failed self-test


RpcError
--------

    .. py:currentmodule:: niswitch.errors

    .. exception:: RpcError

        An error specific to sessions to the NI gRPC Device Server


DriverWarning
-------------

    .. py:currentmodule:: niswitch.errors

    .. exception:: DriverWarning

        A warning originating from the NI-SWITCH driver
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/niswitch/examples.rst sha256=f8744278b2cae2b3308ab384b5d052eec7815692d128ae2468f7734c8aa48f14 bytes=1156 -->
## FILE: docs/niswitch/examples.rst

- repository: `ni/nimi-python`
- source_path: `docs/niswitch/examples.rst`
- sha256: `f8744278b2cae2b3308ab384b5d052eec7815692d128ae2468f7734c8aa48f14`
- bytes: 1156

````rst
Examples
========

`You can download all niswitch examples for latest version here <https://github.com/ni/nimi-python/releases/download/1.4.9/niswitch_examples.zip>`_

niswitch_connect_channels.py
----------------------------

.. literalinclude:: ../../src/niswitch/examples/niswitch_connect_channels.py
   :language: python
   :linenos:
   :encoding: utf8
   :caption: `(niswitch_connect_channels.py) <https://github.com/ni/nimi-python/blob/master/src/niswitch/examples/niswitch_connect_channels.py>`_

niswitch_get_device_info.py
---------------------------

.. literalinclude:: ../../src/niswitch/examples/niswitch_get_device_info.py
   :language: python
   :linenos:
   :encoding: utf8
   :caption: `(niswitch_get_device_info.py) <https://github.com/ni/nimi-python/blob/master/src/niswitch/examples/niswitch_get_device_info.py>`_

niswitch_relay_control.py
-------------------------

.. literalinclude:: ../../src/niswitch/examples/niswitch_relay_control.py
   :language: python
   :linenos:
   :encoding: utf8
   :caption: `(niswitch_relay_control.py) <https://github.com/ni/nimi-python/blob/master/src/niswitch/examples/niswitch_relay_control.py>`_
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/niswitch/grpc_session_options.rst sha256=040175a64d33f2e57565d6be4ce6e3d450fb7d346b28b01f52ca6e31745072ed bytes=2893 -->
## FILE: docs/niswitch/grpc_session_options.rst

- repository: `ni/nimi-python`
- source_path: `docs/niswitch/grpc_session_options.rst`
- sha256: `040175a64d33f2e57565d6be4ce6e3d450fb7d346b28b01f52ca6e31745072ed`
- bytes: 2893

````rst
gRPC Support
============

Support for using NI-SWITCH over gRPC

.. py:currentmodule:: niswitch



SessionInitializationBehavior
-----------------------------

.. py:class:: SessionInitializationBehavior

    .. py:attribute:: SessionInitializationBehavior.AUTO


        The NI gRPC Device Server will attach to an existing session with the specified name if it exists,
        otherwise the server will initialize a new session.

        .. note:: When using the Session as a context manager and the context exits, the behavior depends on what happened when the constructor
            was called. If it resulted in a new session being initialized on the NI gRPC Device Server, then it will automatically close the
            server session. If it instead attached to an existing session, then it will detach from the server session and leave it open.


    .. py:attribute:: SessionInitializationBehavior.INITIALIZE_SERVER_SESSION


        Require the NI gRPC Device Server to initialize a new session with the specified name.

        .. note:: When using the Session as a context manager and the context exits, it will automatically close the
            server session.


    .. py:attribute:: SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION


        Require the NI gRPC Device Server to attach to an existing session with the specified name.

        .. note:: When using the Session as a context manager and the context exits, it will detach from the server session
            and leave it open.



GrpcSessionOptions
------------------


.. py:class:: GrpcSessionOptions(self, grpc_channel, session_name, initialization_behavior=SessionInitializationBehavior.AUTO)


    Collection of options that specifies session behaviors related to gRPC.

    Creates and returns an object you can pass to a Session constructor.


    :param grpc_channel:
        

        Specifies the channel to the NI gRPC Device Server.

        

    :type grpc_channel: grpc.Channel


    :param session_name:
        

        User-specified name that identifies the driver session on the NI gRPC Device Server.

        This is different from the resource name parameter many APIs take as a separate
        parameter. Specifying a name makes it easy to share sessions across multiple gRPC clients.
        You can use an empty string if you want to always initialize a new session on the server.
        To attach to an existing session, you must specify the session name it was initialized with.

        

    :type session_name: str


    :param initialization_behavior:
        

        Specifies whether it is acceptable to initialize a new session or attach to an existing one, or if only one of the behaviors is desired.

        The driver session exists on the NI gRPC Device Server.

        

    :type initialization_behavior: :py:data:`niswitch.SessionInitializationBehavior`
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/niswitch/index.rst sha256=bc5518bb1dc479e6754918d23b68a9ebab5665d2dd8df9cdccfde93c36a99fcd bytes=694 -->
## FILE: docs/niswitch/index.rst

- repository: `ni/nimi-python`
- source_path: `docs/niswitch/index.rst`
- sha256: `bc5518bb1dc479e6754918d23b68a9ebab5665d2dd8df9cdccfde93c36a99fcd`
- bytes: 694

````rst

NI-SWITCH Python API Documentation
==================================

.. include:: about_niswitch.inc

.. include:: ../_static/contributing.inc

.. include:: ../_static/support.inc

.. toctree::
   :maxdepth: 3
   :caption: Documentation

   niswitch

Additional Documentation
------------------------

Refer to your driver documentation for device-specific information and detailed API documentation.

Refer to the `nimi-python Read the Docs project <https://nimi-python.readthedocs.io/en/stable/>`_ for documentation of versions 1.4.4 of the module or earlier.

.. include:: ../_static/license.inc

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/niswitch/installation.inc sha256=67bd9db4fb68a2aa14f3dbe25e1e3e14399246a916b29305413bd1a00fd6a16a bytes=430 -->
## FILE: docs/niswitch/installation.inc

- repository: `ni/nimi-python`
- source_path: `docs/niswitch/installation.inc`
- sha256: `67bd9db4fb68a2aa14f3dbe25e1e3e14399246a916b29305413bd1a00fd6a16a`
- bytes: 430

````text

.. _niswitch_installation-section:

Installation
------------

As a prerequisite to using the **niswitch** module, you must install the NI-SWITCH runtime on your system. Visit `ni.com/downloads <http://www.ni.com/downloads/>`_ to download the driver runtime for your devices.

The nimi-python modules (i.e. for **NI-SWITCH**) can be installed with `pip <http://pypi.python.org/pypi/pip>`_::

  $ python -m pip install niswitch
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/niswitch/niswitch.rst sha256=0d0e90f093767b2287a6fd8fa5416b77e0dc23fb51ca62c8938efe4a06f78794 bytes=130 -->
## FILE: docs/niswitch/niswitch.rst

- repository: `ni/nimi-python`
- source_path: `docs/niswitch/niswitch.rst`
- sha256: `0d0e90f093767b2287a6fd8fa5416b77e0dc23fb51ca62c8938efe4a06f78794`
- bytes: 130

````rst
niswitch module
===============

.. include:: installation.inc

.. include:: ../_static/niswitch_usage.inc

.. include:: toc.inc
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/niswitch/rep_caps.rst sha256=ac2a80e053a044f2eb95cf34ebe0940f7550f8e7c705af750b1cfc24c8c025b9 bytes=1207 -->
## FILE: docs/niswitch/rep_caps.rst

- repository: `ni/nimi-python`
- source_path: `docs/niswitch/rep_caps.rst`
- sha256: `ac2a80e053a044f2eb95cf34ebe0940f7550f8e7c705af750b1cfc24c8c025b9`
- bytes: 1207

````rst
.. py:module:: niswitch
    :noindex:

.. py:currentmodule:: niswitch.Session

.. role:: c(code)
    :language: c

.. role:: python(code)
    :language: python

Repeated Capabilities
=====================

    Repeated capabilities attributes are used to set the `channel_string` parameter to the
    underlying driver function call. This can be the actual function based on the :py:class:`Session`
    method being called, or it can be the appropriate Get/Set Attribute function, such as :c:`niSwitch_SetAttributeViInt32()`.

    Repeated capabilities attributes use the indexing operator :python:`[]` to indicate the repeated capabilities.
    The parameter can be a string, list, tuple, or slice (range). Each element of those can be a string or
    an integer. If it is a string, you can indicate a range using the same format as the driver: :python:`'0-2'` or
    :python:`'0:2'`

    Some repeated capabilities use a prefix before the number and this is optional

channels
--------

    .. py:attribute:: niswitch.Session.channels[]

        .. code:: python

            session.channels['0-2'].channel_enabled = True

        passes a string of :python:`'0, 1, 2'` to the set attribute function.
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/niswitch/status.inc sha256=27c04c9924a608972d6891e366987ed701f48e3808542e121495e0669c93d7b8 bytes=1982 -->
## FILE: docs/niswitch/status.inc

- repository: `ni/nimi-python`
- source_path: `docs/niswitch/status.inc`
- sha256: `27c04c9924a608972d6891e366987ed701f48e3808542e121495e0669c93d7b8`
- bytes: 1982

````text

NI-SWITCH Python API Status
---------------------------

+-------------------------------+-------------------------+
| NI-SWITCH (niswitch)          |                         |
+===============================+=========================+
| Driver Version Tested Against | 2025 Q4                 |
+-------------------------------+-------------------------+
| PyPI Version                  | |niswitchLatestVersion| |
+-------------------------------+-------------------------+
| Supported Python Version      | |niswitchPythonVersion| |
+-------------------------------+-------------------------+
| Documentation                 | |niswitchDocs|          |
+-------------------------------+-------------------------+
| Open Issues                   | |niswitchOpenIssues|    |
+-------------------------------+-------------------------+
| Open Pull Requests            | |niswitchOpenPRs|       |
+-------------------------------+-------------------------+


.. |niswitchLatestVersion| image:: http://img.shields.io/pypi/v/niswitch.svg
    :alt: Latest NI-SWITCH Version
    :target: http://pypi.python.org/pypi/niswitch


.. |niswitchPythonVersion| image:: http://img.shields.io/pypi/pyversions/niswitch.svg
    :alt: NI-SWITCH supported Python versions
    :target: http://pypi.python.org/pypi/niswitch


.. |niswitchDocs| image:: https://readthedocs.org/projects/niswitch/badge/?version=latest
    :alt: NI-SWITCH Python API Documentation Status
    :target: https://niswitch.readthedocs.io/en/latest


.. |niswitchOpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python/niswitch.svg
    :alt: Open Issues + Pull Requests for NI-SWITCH
    :target: https://github.com/ni/nimi-python/issues?q=is%3Aopen+is%3Aissue+label%3Aniswitch


.. |niswitchOpenPRs| image:: https://img.shields.io/github/issues-pr/ni/nimi-python/niswitch.svg
    :alt: Pull Requests for NI-SWITCH
    :target: https://github.com/ni/nimi-python/pulls?q=is%3Aopen+is%3Aissue+label%3Aniswitch
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/niswitch/toc.inc sha256=4958d5597b4005305d15cdc9a09014d5afa552d460451b042172b99069952975 bytes=121 -->
## FILE: docs/niswitch/toc.inc

- repository: `ni/nimi-python`
- source_path: `docs/niswitch/toc.inc`
- sha256: `4958d5597b4005305d15cdc9a09014d5afa552d460451b042172b99069952975`
- bytes: 121

````text
API Reference
--------------

.. toctree::

   class
   rep_caps
   enums
   errors
   examples
   grpc_session_options
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nitclk/.readthedocs.yaml sha256=56275b0b69762b0ab1d26fe575675db2acc97092389df74bc0f1ab4e6e709829 bytes=1876 -->
## FILE: docs/nitclk/.readthedocs.yaml

- repository: `ni/nimi-python`
- source_path: `docs/nitclk/.readthedocs.yaml`
- sha256: `56275b0b69762b0ab1d26fe575675db2acc97092389df74bc0f1ab4e6e709829`
- bytes: 1876

````yaml
# .readthedocs.yaml
# Read the Docs configuration file
# See https://docs.readthedocs.io/en/stable/config-file/v2.html for details

# Why Use A Configuration File?
# https://docs.readthedocs.io/en/stable/config-file/index.html
# The main advantages of using a configuration file over the web interface are:
# * Settings are per version rather than per project.
# * Settings live in your VCS.
# * They enable reproducible build environments over time.
# * Some settings are only available using a configuration file

# Required
version: 2

# Set the version of Python and other tools you might need
build:
  os: ubuntu-22.04
  tools:
    python: "3.11"
  jobs:
    # pre_build:
    #   # Check for broken external links
    #   - python -m sphinx -b linkcheck -D linkcheck_timeout=1 docs/ _build/linkcheck
    post_checkout:
      # https://docs.readthedocs.io/en/stable/build-customization.html#cancel-build-based-on-a-condition
      # Build-cancellation rules are recommended for monorepos.
      # Cancel building pull requests when there aren't changes in any of these paths: docs/_static/ docs/nitclk/.
      #
      # If there are no changes (git diff exits with 0) we force the command to return with 183.
      # This is a special exit code on Read the Docs that will cancel the build immediately.
      - |
        if [ "$READTHEDOCS_VERSION_TYPE" = "external" ] && git diff --quiet origin/master -- docs/_static/ docs/nitclk/;
        then
          exit 183;
        fi

# Have Read the Docs build documentation with Sphinx
sphinx:
  builder: html
  configuration: docs/nitclk/conf.py

# If using Sphinx, optionally build your docs in additional formats such as PDF
formats:
  - epub
  - pdf

# Declare the Python requirements required to build your docs
python:
  install:
  - requirements: docs/requirements.txt
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nitclk/about_nitclk.inc sha256=8886d57e41fe4824e487a3fab6fce4e7c9481e5535f77f2d9580762014afd55d bytes=485 -->
## FILE: docs/nitclk/about_nitclk.inc

- repository: `ni/nimi-python`
- source_path: `docs/nitclk/about_nitclk.inc`
- sha256: `8886d57e41fe4824e487a3fab6fce4e7c9481e5535f77f2d9580762014afd55d`
- bytes: 485

````text
.. _about-section:

About
=====

The **nitclk** module provides a Python API for NI-TClk. The code is maintained in the Open Source repository for `nimi-python <https://github.com/ni/nimi-python>`_.

Support Policy
--------------
**nitclk** supports all the Operating Systems supported by NI-TClk.

It follows `Python Software Foundation <https://devguide.python.org/#status-of-python-branches>`_ support policy for different versions of CPython.

NI created and supports **nitclk**.
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nitclk/class.rst sha256=f9a842ffba71e35b3c79b2a8e81d4f05a7e90daa3e711e72dce5a3ef0bfd6d22 bytes=33035 -->
## FILE: docs/nitclk/class.rst

- repository: `ni/nimi-python`
- source_path: `docs/nitclk/class.rst`
- sha256: `f9a842ffba71e35b3c79b2a8e81d4f05a7e90daa3e711e72dce5a3ef0bfd6d22`
- bytes: 33035

````rst

.. py:module:: nitclk

Public API
==========

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

configure_for_homogeneous_triggers
----------------------------------

    .. py:currentmodule:: nitclk

    .. py:function:: configure_for_homogeneous_triggers(sessions)

        Configures the properties commonly required for the TClk synchronization
        of device sessions with homogeneous triggers in a single PXI chassis or
        a single PC. Use :py:func:`nitclk.configure_for_homogeneous_triggers` to configure
        the properties for the reference clocks, start triggers, reference
        triggers, script triggers, and pause triggers. If
        :py:func:`nitclk.configure_for_homogeneous_triggers` cannot perform all the steps
        appropriate for the given sessions, it returns an error. If an error is
        returned, use the instrument driver methods and properties for signal
        routing, along with the following NI-TClk properties:
        :py:attr:`nitclk.SessionReference.start_trigger_master_session`
        :py:attr:`nitclk.SessionReference.ref_trigger_master_session`
        :py:attr:`nitclk.SessionReference.pause_trigger_master_session`
        :py:func:`nitclk.configure_for_homogeneous_triggers` affects the following clocks and
        triggers: - Reference clocks - Start triggers - Reference triggers -
        Script triggers - Pause triggers Reference Clocks
        :py:func:`nitclk.configure_for_homogeneous_triggers` configures the reference clocks
        if they are needed. Specifically, if the internal sample clocks or
        internal sample clock timebases are used, and the reference clock source
        is not configured--or is set to None (no trigger
        configured)--:py:func:`nitclk.configure_for_homogeneous_triggers` configures the
        following: PXI--The reference clock source on all devices is set to be
        the 10 MHz PXI backplane clock (PXI_CLK10). PCI--One of the devices
        exports its 10 MHz onboard reference clock to RTSI 7. The reference
        clock source on all devices is set to be RTSI 7. Note: If the reference
        clock source is set to a value other than None,
        :py:func:`nitclk.configure_for_homogeneous_triggers` cannot configure the reference
        clock source. Start Triggers If the start trigger is set to None (no
        trigger configured) for all sessions, the sessions are configured to
        share the start trigger. The start trigger is shared by: - Implicitly
        exporting the start trigger from one session - Configuring the other
        sessions for digital edge start triggers with sources corresponding to
        the exported start trigger - Setting
        :py:attr:`nitclk.SessionReference.start_trigger_master_session` to the session that is
        exporting the trigger for all sessions If the start triggers are None
        for all except one session, :py:func:`nitclk.configure_for_homogeneous_triggers`
        configures the sessions to share the start trigger from the one excepted
        session. The start trigger is shared by: - Implicitly exporting start
        trigger from the session with the start trigger that is not None -
        Configuring the other sessions for digital-edge start triggers with
        sources corresponding to the exported start trigger - Setting
        :py:attr:`nitclk.SessionReference.start_trigger_master_session` to the session that is
        exporting the trigger for all sessions If start triggers are configured
        for all sessions, :py:func:`nitclk.configure_for_homogeneous_triggers` does not
        affect the start triggers. Start triggers are considered to be
        configured for all sessions if either of the following conditions is
        true: - No session has a start trigger that is None - One session has a
        start trigger that is None, and all other sessions have start triggers
        other than None. The one session with the None trigger must have
        :py:attr:`nitclk.SessionReference.start_trigger_master_session` set to itself, indicating
        that the session itself is the start trigger master Reference Triggers
        :py:func:`nitclk.configure_for_homogeneous_triggers` configures sessions that support
        reference triggers to share the reference triggers if the reference
        triggers are None (no trigger configured) for all except one session.
        The reference triggers are shared by: - Implicitly exporting the
        reference trigger from the session whose reference trigger is not None -
        Configuring the other sessions that support the reference trigger for
        digital-edge reference triggers with sources corresponding to the
        exported reference trigger - Setting
        :py:attr:`nitclk.SessionReference.ref_trigger_master_session` to the session that is
        exporting the trigger for all sessions that support reference trigger If
        the reference triggers are configured for all sessions that support
        reference triggers, :py:func:`nitclk.configure_for_homogeneous_triggers` does not
        affect the reference triggers. Reference triggers are considered to be
        configured for all sessions if either one or the other of the following
        conditions is true: - No session has a reference trigger that is None -
        One session has a reference trigger that is None, and all other sessions
        have reference triggers other than None. The one session with the None
        trigger must have :py:attr:`nitclk.SessionReference.ref_trigger_master_session` set to
        itself, indicating that the session itself is the reference trigger
        master Reference Trigger Holdoffs Acquisition sessions may be configured
        with the reference trigger. For acquisition sessions, when the reference
        trigger is shared, :py:func:`nitclk.configure_for_homogeneous_triggers` configures
        the holdoff properties (which are instrument driver specific) on the
        reference trigger master session so that the session does not recognize
        the reference trigger before the other sessions are ready. This
        condition is only relevant when the sample clock rates, sample clock
        timebase rates, sample counts, holdoffs, and/or any delays for the
        acquisitions are different. When the sample clock rates, sample clock
        timebase rates, and/or the sample counts are different in acquisition
        sessions sharing the reference trigger, you should also set the holdoff
        properties for the reference trigger master using the instrument driver.
        Pause Triggers
        :py:func:`nitclk.configure_for_homogeneous_triggers` configures generation sessions
        that support pause triggers to share them, if the pause triggers are
        None (no trigger configured) for all except one session. The pause
        triggers are shared by: - Implicitly exporting the pause trigger from
        the session whose script trigger is not None - Configuring the other
        sessions that support the pause trigger for digital-edge pause triggers
        with sources corresponding to the exported pause trigger - Setting
        :py:attr:`nitclk.SessionReference.pause_trigger_master_session` to the session that is
        exporting the trigger for all sessions that support script triggers If
        the pause triggers are configured for all generation sessions that
        support pause triggers, :py:func:`nitclk.configure_for_homogeneous_triggers` does not
        affect pause triggers. Pause triggers are considered to be configured
        for all sessions if either one or the other of the following conditions
        is true: - No session has a pause trigger that is None - One session has
        a pause trigger that is None and all other sessions have pause triggers
        other than None. The one session with the None trigger must have
        :py:attr:`nitclk.SessionReference.pause_trigger_master_session` set to itself, indicating
        that the session itself is the pause trigger master Note: TClk
        synchronization is not supported for pause triggers on acquisition
        sessions.

        



        :param sessions:


            sessions is an array of sessions that are being synchronized.

            


        :type sessions: list of instrument-specific sessions or nitclk.SessionReference instances

finish_sync_pulse_sender_synchronize
------------------------------------

    .. py:currentmodule:: nitclk

    .. py:function:: finish_sync_pulse_sender_synchronize(sessions, min_time=hightime.timedelta(seconds=0.0))

        Finishes synchronizing the Sync Pulse Sender.

        



        :param sessions:


            sessions is an array of sessions that are being synchronized.

            


        :type sessions: list of instrument-specific sessions or nitclk.SessionReference instances
        :param min_time:


            Minimal period of TClk, expressed in seconds. Supported values are
            between 0.0 s and 0.050 s (50 ms). Minimal period for a single
            chassis/PC is 200 ns. If the specified value is less than 200 ns,
            NI-TClk automatically coerces minTime to 200 ns. For multichassis
            synchronization, adjust this value to account for propagation delays
            through the various devices and cables.

            


        :type min_time: hightime.timedelta, datetime.timedelta, or float in seconds

initiate
--------

    .. py:currentmodule:: nitclk

    .. py:function:: initiate(sessions)

        Initiates the acquisition or generation sessions specified, taking into
        consideration any special requirements needed for synchronization. For
        example, the session exporting the TClk-synchronized start trigger is
        not initiated until after :py:func:`nitclk.initiate` initiates all the sessions
        that import the TClk-synchronized start trigger.

        



        :param sessions:


            sessions is an array of sessions that are being synchronized.

            


        :type sessions: list of instrument-specific sessions or nitclk.SessionReference instances

is_done
-------

    .. py:currentmodule:: nitclk

    .. py:function:: is_done(sessions)

        Monitors the progress of the acquisitions and/or generations
        corresponding to sessions.

        



        :param sessions:


            sessions is an array of sessions that are being synchronized.

            


        :type sessions: list of instrument-specific sessions or nitclk.SessionReference instances

        :rtype: bool
        :return:


                Indicates that the operation is done. The operation is done when each
                session has completed without any errors or when any one of the sessions
                reports an error.

                



setup_for_sync_pulse_sender_synchronize
---------------------------------------

    .. py:currentmodule:: nitclk

    .. py:function:: setup_for_sync_pulse_sender_synchronize(sessions, min_time=hightime.timedelta(seconds=0.0))

        Configures the TClks on all the devices and prepares the Sync Pulse Sender for synchronization

        



        :param sessions:


            sessions is an array of sessions that are being synchronized.

            


        :type sessions: list of instrument-specific sessions or nitclk.SessionReference instances
        :param min_time:


            Minimal period of TClk, expressed in seconds. Supported values are
            between 0.0 s and 0.050 s (50 ms). Minimal period for a single
            chassis/PC is 200 ns. If the specified value is less than 200 ns,
            NI-TClk automatically coerces minTime to 200 ns. For multichassis
            synchronization, adjust this value to account for propagation delays
            through the various devices and cables.

            


        :type min_time: hightime.timedelta, datetime.timedelta, or float in seconds

synchronize
-----------

    .. py:currentmodule:: nitclk

    .. py:function:: synchronize(sessions, min_tclk_period=hightime.timedelta(seconds=0.0))

        Synchronizes the TClk signals on the given sessions. After
        :py:func:`nitclk.synchronize` executes, TClk signals from all sessions are
        synchronized. Note: Before using this NI-TClk method, verify that your
        system is configured as specified in the PXI Trigger Lines and RTSI
        Lines topic of the NI-TClk Synchronization Help. You can locate this
        help file at Start>>Programs>>National Instruments>>NI-TClk.

        



        :param sessions:


            sessions is an array of sessions that are being synchronized.

            


        :type sessions: list of instrument-specific sessions or nitclk.SessionReference instances
        :param min_tclk_period:


            Minimal period of TClk, expressed in seconds. Supported values are
            between 0.0 s and 0.050 s (50 ms). Minimal period for a single
            chassis/PC is 200 ns. If the specified value is less than 200 ns,
            NI-TClk automatically coerces minTime to 200 ns. For multichassis
            synchronization, adjust this value to account for propagation delays
            through the various devices and cables.

            


        :type min_tclk_period: hightime.timedelta, datetime.timedelta, or float in seconds

synchronize_to_sync_pulse_sender
--------------------------------

    .. py:currentmodule:: nitclk

    .. py:function:: synchronize_to_sync_pulse_sender(sessions, min_time=hightime.timedelta(seconds=0.0))

        Synchronizes the other devices to the Sync Pulse Sender.

        



        :param sessions:


            sessions is an array of sessions that are being synchronized.

            


        :type sessions: list of instrument-specific sessions or nitclk.SessionReference instances
        :param min_time:


            Minimal period of TClk, expressed in seconds. Supported values are
            between 0.0 s and 0.050 s (50 ms). Minimal period for a single
            chassis/PC is 200 ns. If the specified value is less than 200 ns,
            NI-TClk automatically coerces minTime to 200 ns. For multichassis
            synchronization, adjust this value to account for propagation delays
            through the various devices and cables.

            


        :type min_time: hightime.timedelta, datetime.timedelta, or float in seconds

wait_until_done
---------------

    .. py:currentmodule:: nitclk

    .. py:function:: wait_until_done(sessions, timeout=hightime.timedelta(seconds=0.0))

        Call this method to pause execution of your program until the
        acquisitions and/or generations corresponding to sessions are done or
        until the method returns a timeout error. :py:func:`nitclk.wait_until_done` is a
        blocking method that periodically checks the operation status. It
        returns control to the calling program if the operation completes
        successfully or an error occurs (including a timeout error). This
        method is most useful for finite data operations that you expect to
        complete within a certain time.

        



        :param sessions:


            sessions is an array of sessions that are being synchronized.

            


        :type sessions: list of instrument-specific sessions or nitclk.SessionReference instances
        :param timeout:


            The amount of time in seconds that :py:func:`nitclk.wait_until_done` waits for the
            sessions to complete. If timeout is exceeded, :py:func:`nitclk.wait_until_done`
            returns an error.

            


        :type timeout: hightime.timedelta, datetime.timedelta, or float in seconds


SessionReference
================
.. py:currentmodule:: nitclk

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


exported_sync_pulse_output_terminal
-----------------------------------

    .. py:currentmodule:: nitclk.SessionReference

    .. py:attribute:: exported_sync_pulse_output_terminal

        Specifies the destination of the Sync Pulse. This property is most often  used when synchronizing a multichassis system.
        Values
        Empty string. Empty string is a valid value, indicating that the signal is  not exported.
        PXI Devices -  'PXI_Trig0' through  'PXI_Trig7' and device-specific settings
        PCI Devices -  'RTSI_0' through  'RTSI_7' and device-specific settings
        Examples of Device-Specific Settings
        - NI PXI-5122 supports  'PFI0' and  'PFI1'
        - NI PXI-5421 supports  'PFI0',  'PFI1',  'PFI4', and  'PFI5'
        - NI PXI-6551/6552 supports  'PFI0',  'PFI1',  'PFI2', and  'PFI3'
        Default Value is empty string

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Export Sync Pulse Output Terminal**
                - C Attribute: **NITCLK_ATTR_EXPORTED_SYNC_PULSE_OUTPUT_TERMINAL**

exported_tclk_output_terminal
-----------------------------

    .. py:currentmodule:: nitclk.SessionReference

    .. py:attribute:: exported_tclk_output_terminal

        Specifies the destination of the device's TClk signal.
        Values
        Empty string. Empty string is a valid value, indicating that the signal is  not exported.
        PXI Devices -  'PXI_Trig0' through  'PXI_Trig7' and device-specific settings
        PCI Devices -  'RTSI_0' through  'RTSI_7' and device-specific settings
        Examples of Device-Specific Settings
        - NI PXI-5122 supports  'PFI0' and  'PFI1'
        - NI PXI-5421 supports  'PFI0',  'PFI1',  'PFI4', and  'PFI5'
        - NI PXI-6551/6552 supports  'PFI0',  'PFI1',  'PFI2', and  'PFI3'
        Default Value is empty string

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Output Terminal**
                - C Attribute: **NITCLK_ATTR_EXPORTED_TCLK_OUTPUT_TERMINAL**

pause_trigger_master_session
----------------------------

    .. py:currentmodule:: nitclk.SessionReference

    .. py:attribute:: pause_trigger_master_session

        Specifies the pause trigger master session.
        For external triggers, the session that originally receives the trigger.  For None (no trigger configured) or software triggers, the session that  originally generates the trigger.

        The following table lists the characteristics of this property.

            +----------------+-----------------------------------------------------------------------+
            | Characteristic | Value                                                                 |
            +================+=======================================================================+
            | Datatype       | instrument-specific session or an instance of nitclk.SessionReference |
            +----------------+-----------------------------------------------------------------------+
            | Permissions    | read-write                                                            |
            +----------------+-----------------------------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Pause Trigger Master Session**
                - C Attribute: **NITCLK_ATTR_PAUSE_TRIGGER_MASTER_SESSION**

ref_trigger_master_session
--------------------------

    .. py:currentmodule:: nitclk.SessionReference

    .. py:attribute:: ref_trigger_master_session

        Specifies the reference trigger master session.
        For external triggers, the session that originally receives the trigger.  For None (no trigger configured) or software triggers, the session that  originally generates the trigger.

        The following table lists the characteristics of this property.

            +----------------+-----------------------------------------------------------------------+
            | Characteristic | Value                                                                 |
            +================+=======================================================================+
            | Datatype       | instrument-specific session or an instance of nitclk.SessionReference |
            +----------------+-----------------------------------------------------------------------+
            | Permissions    | read-write                                                            |
            +----------------+-----------------------------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Reference Trigger Master Session**
                - C Attribute: **NITCLK_ATTR_REF_TRIGGER_MASTER_SESSION**

sample_clock_delay
------------------

    .. py:currentmodule:: nitclk.SessionReference

    .. py:attribute:: sample_clock_delay

        Specifies the sample clock delay.
        Specifies the delay, in seconds, to apply to the session sample clock  relative to the other synchronized sessions. During synchronization,  NI-TClk aligns the sample clocks on the synchronized devices. If you want  to delay the sample clocks, set this property before calling  :py:func:`nitclk.synchronize`.
        not supported for acquisition sessions.
        Values - Between minus one and plus one period of the sample clock.
        One sample clock period is equal to (1/sample clock rate). For example,  for a session with sample rate of 100 MS/s, you can specify sample clock  delays between -10.0 ns and +10.0 ns.
        Default Value is 0



        .. note:: Sample clock delay is supported for generation sessions only; it is

        The following table lists the characteristics of this property.

            +----------------+-------------------------------------------------------------+
            | Characteristic | Value                                                       |
            +================+=============================================================+
            | Datatype       | hightime.timedelta, datetime.timedelta, or float in seconds |
            +----------------+-------------------------------------------------------------+
            | Permissions    | read-write                                                  |
            +----------------+-------------------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Sample Clock Delay**
                - C Attribute: **NITCLK_ATTR_SAMPLE_CLOCK_DELAY**

sequencer_flag_master_session
-----------------------------

    .. py:currentmodule:: nitclk.SessionReference

    .. py:attribute:: sequencer_flag_master_session

        Specifies the sequencer flag master session.
        For external triggers, the session that originally receives the trigger.
        For None (no trigger configured) or software triggers, the session that
        originally generates the trigger.

        The following table lists the characteristics of this property.

            +----------------+-----------------------------------------------------------------------+
            | Characteristic | Value                                                                 |
            +================+=======================================================================+
            | Datatype       | instrument-specific session or an instance of nitclk.SessionReference |
            +----------------+-----------------------------------------------------------------------+
            | Permissions    | read-write                                                            |
            +----------------+-----------------------------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Sequencer Flag Master Session**
                - C Attribute: **NITCLK_ATTR_SEQUENCER_FLAG_MASTER_SESSION**

start_trigger_master_session
----------------------------

    .. py:currentmodule:: nitclk.SessionReference

    .. py:attribute:: start_trigger_master_session

        Specifies the start trigger master session.
        For external triggers, the session that originally receives the trigger.  For None (no trigger configured) or software triggers, the session that  originally generates the trigger.

        The following table lists the characteristics of this property.

            +----------------+-----------------------------------------------------------------------+
            | Characteristic | Value                                                                 |
            +================+=======================================================================+
            | Datatype       | instrument-specific session or an instance of nitclk.SessionReference |
            +----------------+-----------------------------------------------------------------------+
            | Permissions    | read-write                                                            |
            +----------------+-----------------------------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Start Trigger Master Session**
                - C Attribute: **NITCLK_ATTR_START_TRIGGER_MASTER_SESSION**

sync_pulse_clock_source
-----------------------

    .. py:currentmodule:: nitclk.SessionReference

    .. py:attribute:: sync_pulse_clock_source

        Specifies the Sync Pulse Clock source. This property is typically used to  synchronize PCI devices when you want to control RTSI 7 yourself. Make  sure that a 10 MHz clock is driven onto RTSI 7.
        Values
        PCI Devices -  'RTSI_7' and  'None'
        PXI Devices -  'PXI_CLK10' and  'None'
        Default Value -  'None' directs :py:func:`nitclk.synchronize` to create the necessary routes. For  PCI, one of the synchronized devices drives a 10 MHz clock on RTSI 7  unless that line is already being driven.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Sync Pulse Clock Source**
                - C Attribute: **NITCLK_ATTR_SYNC_PULSE_CLOCK_SOURCE**

sync_pulse_sender_sync_pulse_source
-----------------------------------

    .. py:currentmodule:: nitclk.SessionReference

    .. py:attribute:: sync_pulse_sender_sync_pulse_source

        Specifies the external sync pulse source for the Sync Pulse Sender.  You can use this source to synchronize  the Sync Pulse Sender with an external non-TClk source.
        Values
        Empty string. Empty string is a valid value, indicating that the signal is  not exported.
        PXI Devices -  'PXI_Trig0' through  'PXI_Trig7' and device-specific settings
        PCI Devices -  'RTSI_0' through  'RTSI_7' and device-specific settings
        Examples of Device-Specific Settings
        - NI PXI-5122 supports  'PFI0' and  'PFI1'
        - NI PXI-5421 supports  'PFI0',  'PFI1',  'PFI4', and  'PFI5'
        - NI PXI-6551/6552 supports  'PFI0',  'PFI1',  'PFI2', and  'PFI3'
        Default Value is empty string

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **External Pulse Source**
                - C Attribute: **NITCLK_ATTR_SYNC_PULSE_SENDER_SYNC_PULSE_SOURCE**

sync_pulse_source
-----------------

    .. py:currentmodule:: nitclk.SessionReference

    .. py:attribute:: sync_pulse_source

        Specifies the Sync Pulse source. This property is most often used when  synchronizing a multichassis system.
        Values
        Empty string
        PXI Devices -  'PXI_Trig0' through  'PXI_Trig7' and device-specific settings
        PCI Devices -  'RTSI_0' through  'RTSI_7' and device-specific settings
        Examples of Device-Specific Settings
        - NI PXI-5122 supports  'PFI0' and  'PFI1'
        - NI PXI-5421 supports  'PFI0',  'PFI1',  'PFI2', and  'PFI3'
        - NI PXI-6551/6552 supports  'PFI0',  'PFI1',  'PFI2', and  'PFI3'
        Default Value - Empty string. This default value directs  :py:func:`nitclk.synchronize` to set this property when all the synchronized devices  are in one PXI chassis. To synchronize a multichassis system, you must set  this property before calling :py:func:`nitclk.synchronize`.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Sync Pulse Source**
                - C Attribute: **NITCLK_ATTR_SYNC_PULSE_SOURCE**

tclk_actual_period
------------------

    .. py:currentmodule:: nitclk.SessionReference

    .. py:attribute:: tclk_actual_period

        Indicates the computed TClk period that will be used during the acquisition.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | float     |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Period**
                - C Attribute: **NITCLK_ATTR_TCLK_ACTUAL_PERIOD**


.. contents:: nitclk
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nitclk/conf.py sha256=0d152b1f534050003151b408789574c659a9e502c84ceade101a995b90891d08 bytes=6531 -->
## FILE: docs/nitclk/conf.py

- repository: `ni/nimi-python`
- source_path: `docs/nitclk/conf.py`
- sha256: `0d152b1f534050003151b408789574c659a9e502c84ceade101a995b90891d08`
- bytes: 6531

````python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# NI-TClk Python API documentation build configuration file, created by
# sphinx-quickstart on Fri Jul 14 13:04:36 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../generated'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.doctest',
              'sphinx.ext.intersphinx',
              'sphinx.ext.todo',
              'sphinx.ext.coverage',
              'sphinx.ext.mathjax',
              'sphinx.ext.ifconfig',
              'sphinx.ext.viewcode',
              'sphinx.ext.githubpages']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'NI-TClk Python API'
copyright = '2019-2026, National Instruments Corporation'
author = 'NI'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags.
release = '1.4.10.dev0'
# The short X.Y version.
version = release[:3]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'navigation_depth': -1,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../_static']

# Fix wide tables of RTD per https://github.com/rtfd/sphinx_rtd_theme/issues/117#issuecomment-41571653
def setup(app):
    app.add_css_file('theme_overrides.css')

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
        'donate.html',
    ]
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'NIModularInstrumentsPythonAPIdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'NITClkPythonAPI.tex', 'NI-TClk Python API Documentation',
     'NI', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'nitclkpythonapi', 'NI-TClk Python API Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'NITClkPythonAPI', 'NI-TClk Python API Documentation',
     author, 'NITClkPythonAPI', 'One line description of project.',
     'Miscellaneous'),
]

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'nidcpower': ('https://nidcpower.readthedocs.io/en/latest/', None),
    'nidigital': ('https://nidigital.readthedocs.io/en/latest/', None),
    'nidmm': ('https://nidmm.readthedocs.io/en/latest/', None),
    'nifgen': ('https://nifgen.readthedocs.io/en/latest/', None),
    'nimodinst': ('https://nimodinst.readthedocs.io/en/latest/', None),
    'nirfsg': ('https://nirfsg.readthedocs.io/en/latest/', None),
    'niscope': ('https://niscope.readthedocs.io/en/latest/', None),
    'nise': ('https://nise.readthedocs.io/en/latest/', None),
    'niswitch': ('https://niswitch.readthedocs.io/en/latest/', None),
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nitclk/errors.rst sha256=06d51c0c250476edcb44aff633ac265464fcdebc555f024cdb639f88f070b16c bytes=1361 -->
## FILE: docs/nitclk/errors.rst

- repository: `ni/nimi-python`
- source_path: `docs/nitclk/errors.rst`
- sha256: `06d51c0c250476edcb44aff633ac265464fcdebc555f024cdb639f88f070b16c`
- bytes: 1361

````rst
Exceptions and Warnings
=======================

Error
-----

    .. py:currentmodule:: nitclk.errors

    .. exception:: Error

        Base exception type that all NI-TClk exceptions derive from


DriverError
-----------

    .. py:currentmodule:: nitclk.errors

    .. exception:: DriverError

        An error originating from the NI-TClk driver


UnsupportedConfigurationError
-----------------------------

    .. py:currentmodule:: nitclk.errors

    .. exception:: UnsupportedConfigurationError

        An error due to using this module in an usupported platform.

DriverNotInstalledError
-----------------------

    .. py:currentmodule:: nitclk.errors

    .. exception:: DriverNotInstalledError

        An error due to using this module without the driver runtime installed.

DriverTooOldError
-----------------

    .. py:currentmodule:: nitclk.errors

    .. exception:: DriverTooOldError

        An error due to using this module with an older version of the NI-TClk driver runtime.

DriverTooNewError
-----------------

    .. py:currentmodule:: nitclk.errors

    .. exception:: DriverTooNewError

        An error due to the NI-TClk driver runtime being too new for this module.

DriverWarning
-------------

    .. py:currentmodule:: nitclk.errors

    .. exception:: DriverWarning

        A warning originating from the NI-TClk driver
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nitclk/examples.rst sha256=0d2ffa3385dadb9f1653d99264079a6444de217277ef2a4dfe2b5c67f52969ad bytes=566 -->
## FILE: docs/nitclk/examples.rst

- repository: `ni/nimi-python`
- source_path: `docs/nitclk/examples.rst`
- sha256: `0d2ffa3385dadb9f1653d99264079a6444de217277ef2a4dfe2b5c67f52969ad`
- bytes: 566

````rst
Examples
========

`You can download all nitclk examples for latest version here <https://github.com/ni/nimi-python/releases/download/1.4.9/nitclk_examples.zip>`_

nitclk_niscope_synchronize_with_trigger.py
------------------------------------------

.. literalinclude:: ../../src/nitclk/examples/nitclk_niscope_synchronize_with_trigger.py
   :language: python
   :linenos:
   :encoding: utf8
   :caption: `(nitclk_niscope_synchronize_with_trigger.py) <https://github.com/ni/nimi-python/blob/master/src/nitclk/examples/nitclk_niscope_synchronize_with_trigger.py>`_
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nitclk/index.rst sha256=2f5cacc7ad2785bb1c2d7f2774813ae03bd560320977b2e3de490091aa6d0903 bytes=686 -->
## FILE: docs/nitclk/index.rst

- repository: `ni/nimi-python`
- source_path: `docs/nitclk/index.rst`
- sha256: `2f5cacc7ad2785bb1c2d7f2774813ae03bd560320977b2e3de490091aa6d0903`
- bytes: 686

````rst

NI-TClk Python API Documentation
================================

.. include:: about_nitclk.inc

.. include:: ../_static/contributing.inc

.. include:: ../_static/support.inc

.. toctree::
   :maxdepth: 3
   :caption: Documentation

   nitclk

Additional Documentation
------------------------

Refer to your driver documentation for device-specific information and detailed API documentation.

Refer to the `nimi-python Read the Docs project <https://nimi-python.readthedocs.io/en/stable/>`_ for documentation of versions 1.4.4 of the module or earlier.

.. include:: ../_static/license.inc

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nitclk/installation.inc sha256=88c00b998f242449d6404373b03d1858535825a4a63716bca805e27d992ef566 bytes=420 -->
## FILE: docs/nitclk/installation.inc

- repository: `ni/nimi-python`
- source_path: `docs/nitclk/installation.inc`
- sha256: `88c00b998f242449d6404373b03d1858535825a4a63716bca805e27d992ef566`
- bytes: 420

````text

.. _nitclk_installation-section:

Installation
------------

As a prerequisite to using the **nitclk** module, you must install the NI-TClk runtime on your system. Visit `ni.com/downloads <http://www.ni.com/downloads/>`_ to download the driver runtime for your devices.

The nimi-python modules (i.e. for **NI-TClk**) can be installed with `pip <http://pypi.python.org/pypi/pip>`_::

  $ python -m pip install nitclk
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nitclk/nitclk.rst sha256=d3cf4690badf7beef942fa64bdb3b6b73d56672cd0ce00f244208da512e6b961 bytes=124 -->
## FILE: docs/nitclk/nitclk.rst

- repository: `ni/nimi-python`
- source_path: `docs/nitclk/nitclk.rst`
- sha256: `d3cf4690badf7beef942fa64bdb3b6b73d56672cd0ce00f244208da512e6b961`
- bytes: 124

````rst
nitclk module
=============

.. include:: installation.inc

.. include:: ../_static/nitclk_usage.inc

.. include:: toc.inc
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nitclk/status.inc sha256=1a1aa4e44b6256c309c756261b40dd4000a89de6cea5ae4c4c25bf68bd97a80b bytes=1908 -->
## FILE: docs/nitclk/status.inc

- repository: `ni/nimi-python`
- source_path: `docs/nitclk/status.inc`
- sha256: `1a1aa4e44b6256c309c756261b40dd4000a89de6cea5ae4c4c25bf68bd97a80b`
- bytes: 1908

````text

NI-TClk Python API Status
-------------------------

+-------------------------------+-----------------------+
| NI-TClk (nitclk)              |                       |
+===============================+=======================+
| Driver Version Tested Against | 2025 Q4               |
+-------------------------------+-----------------------+
| PyPI Version                  | |nitclkLatestVersion| |
+-------------------------------+-----------------------+
| Supported Python Version      | |nitclkPythonVersion| |
+-------------------------------+-----------------------+
| Documentation                 | |nitclkDocs|          |
+-------------------------------+-----------------------+
| Open Issues                   | |nitclkOpenIssues|    |
+-------------------------------+-----------------------+
| Open Pull Requests            | |nitclkOpenPRs|       |
+-------------------------------+-----------------------+


.. |nitclkLatestVersion| image:: http://img.shields.io/pypi/v/nitclk.svg
    :alt: Latest NI-TClk Version
    :target: http://pypi.python.org/pypi/nitclk


.. |nitclkPythonVersion| image:: http://img.shields.io/pypi/pyversions/nitclk.svg
    :alt: NI-TClk supported Python versions
    :target: http://pypi.python.org/pypi/nitclk


.. |nitclkDocs| image:: https://readthedocs.org/projects/nitclk/badge/?version=latest
    :alt: NI-TClk Python API Documentation Status
    :target: https://nitclk.readthedocs.io/en/latest


.. |nitclkOpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python/nitclk.svg
    :alt: Open Issues + Pull Requests for NI-TClk
    :target: https://github.com/ni/nimi-python/issues?q=is%3Aopen+is%3Aissue+label%3Anitclk


.. |nitclkOpenPRs| image:: https://img.shields.io/github/issues-pr/ni/nimi-python/nitclk.svg
    :alt: Pull Requests for NI-TClk
    :target: https://github.com/ni/nimi-python/pulls?q=is%3Aopen+is%3Aissue+label%3Anitclk
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nitclk/toc.inc sha256=a423b560d349bdc16bbc762ed9737d740a20c7f36ca493b6c40282bcfd93d8ea bytes=76 -->
## FILE: docs/nitclk/toc.inc

- repository: `ni/nimi-python`
- source_path: `docs/nitclk/toc.inc`
- sha256: `a423b560d349bdc16bbc762ed9737d740a20c7f36ca493b6c40282bcfd93d8ea`
- bytes: 76

````text
API Reference
--------------

.. toctree::

   class
   errors
   examples
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/requirements.txt sha256=a2f8e13c74d51b9e05bb31e45aa639f39b0cbac526edc960830497160d7544fe bytes=445 -->
## FILE: docs/requirements.txt

- repository: `ni/nimi-python`
- source_path: `docs/requirements.txt`
- sha256: `a2f8e13c74d51b9e05bb31e45aa639f39b0cbac526edc960830497160d7544fe`
- bytes: 445

````text
# This isn't a full-fledged requirements file, yet. It's just a single unpinned dependency that we needed to fix our documentation builds.
# TODO(ni-jfitzger): Create requirements file for docs to make builds reproducible. See https://github.com/ni/nimi-python/issues/1968
# Note: Our nimi-python readthedocs project used the defaults here: https://docs.readthedocs.io/en/stable/build-default-versions.html#external-dependencies
sphinx_rtd_theme
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidcpower/nidcpower/__init__.py sha256=e7315f87343b87ed596f2f6ab6a95a04fdde1f5cffb377958f512fcdfde99bfc bytes=3642 -->
## FILE: generated/nidcpower/nidcpower/__init__.py

- repository: `ni/nimi-python`
- source_path: `generated/nidcpower/nidcpower/__init__.py`
- sha256: `e7315f87343b87ed596f2f6ab6a95a04fdde1f5cffb377958f512fcdfde99bfc`
- bytes: 3642

````python
# -*- coding: utf-8 -*-
# This file was generated


__version__ = '1.5.1.dev0'

from nidcpower.enums import *  # noqa: F403,F401,H303
from nidcpower.errors import DriverWarning  # noqa: F401
from nidcpower.errors import Error  # noqa: F401
from nidcpower.grpc_session_options import *  # noqa: F403,F401,H303
from nidcpower.session import Session  # noqa: F401

from nidcpower.lcr_measurement import LCRMeasurement  # noqa: F401

from nidcpower.lcr_measurement import struct_NILCRMeasurement  # noqa: F401

from nidcpower.lcr_load_compensation_spot import LCRLoadCompensationSpot  # noqa: F401

from nidcpower.lcr_load_compensation_spot import struct_NILCRLoadCompensationSpot  # noqa: F401


def get_diagnostic_information():
    '''Get diagnostic information about the system state that is suitable for printing or logging

    returns: dict

    note: Python bitness may be incorrect when running in a virtual environment
    '''
    import importlib.metadata
    import os
    import platform
    import struct
    import sys

    def is_python_64bit():
        return (struct.calcsize("P") == 8)

    def is_os_64bit():
        return platform.machine().endswith('64')

    def is_venv():
        return 'VIRTUAL_ENV' in os.environ

    info = {}
    info['os'] = {}
    info['python'] = {}
    info['driver'] = {}
    info['module'] = {}
    if platform.system() == 'Windows':
        try:
            import winreg as winreg
        except ImportError:
            import _winreg as winreg

        os_name = 'Windows'
        try:
            driver_version_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\National Instruments\NI-DCPower\CurrentVersion")
            driver_version = winreg.QueryValueEx(driver_version_key, "Version")[0]
        except WindowsError:
            driver_version = 'Unknown'
    elif platform.system() == 'Linux':
        os_name = 'Linux'
        driver_version = 'Unknown'
    else:
        raise SystemError('Unsupported platform: {}'.format(platform.system()))

    installed_packages_names = [
        name
        for name_list in importlib.metadata.packages_distributions().values()
        for name in name_list
    ]
    installed_packages_names = set(installed_packages_names)
    installed_packages_list = [
        {'name': name, 'version': importlib.metadata.distribution(name).version}
        for name in sorted(installed_packages_names)
    ]

    info['os']['name'] = os_name
    info['os']['version'] = platform.version()
    info['os']['bits'] = '64' if is_os_64bit() else '32'
    info['driver']['name'] = "NI-DCPower"
    info['driver']['version'] = driver_version
    info['module']['name'] = 'nidcpower'
    info['module']['version'] = "1.5.1.dev0"
    info['python']['version'] = sys.version
    info['python']['bits'] = '64' if is_python_64bit() else '32'
    info['python']['is_venv'] = is_venv()
    info['python']['packages'] = installed_packages_list

    return info


def print_diagnostic_information():
    '''Print diagnostic information in a format suitable for issue report

    note: Python bitness may be incorrect when running in a virtual environment
    '''
    info = get_diagnostic_information()

    row_format = '    {:<10} {}'
    for type in ['OS', 'Driver', 'Module', 'Python']:
        typename = type.lower()
        print(type + ':')
        for item in info[typename]:
            if item != 'packages':
                print(row_format.format(item.title() + ':', info[typename][item]))
    print('    Installed Packages:')
    for p in info['python']['packages']:
        print((' ' * 8) + p['name'] + '==' + p['version'])

    return info
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidcpower/nidcpower/_attributes.py sha256=9798db88991ea5e0db435d1fadfc07eb17b77b7ad8c2dfccb798b298782d68fd bytes=6187 -->
## FILE: generated/nidcpower/nidcpower/_attributes.py

- repository: `ni/nimi-python`
- source_path: `generated/nidcpower/nidcpower/_attributes.py`
- sha256: `9798db88991ea5e0db435d1fadfc07eb17b77b7ad8c2dfccb798b298782d68fd`
- bytes: 6187

````python
# -*- coding: utf-8 -*-
# This file was generated
import nidcpower._converters as _converters
import nidcpower.errors as errors

import hightime


class Attribute(object):
    '''Base class for all typed attributes.'''

    def __init__(self, attribute_id):
        self._attribute_id = attribute_id


class AttributeViInt32(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_int32(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_int32(self._attribute_id, value)


class AttributeViInt32TimeDeltaMilliseconds(Attribute):

    def __get__(self, session, session_type):
        return hightime.timedelta(milliseconds=session._get_attribute_vi_int32(self._attribute_id))

    def __set__(self, session, value):
        session._set_attribute_vi_int32(self._attribute_id, _converters.convert_timedelta_to_milliseconds_int32(value))


class AttributeViInt32TimeDeltaMonths(Attribute):

    def __get__(self, session, session_type):
        return _converters.convert_month_to_timedelta(session._get_attribute_vi_int32(self._attribute_id))

    def __set__(self, session, value):
        session._set_attribute_vi_int32(self._attribute_id, _converters.convert_timedelta_to_months_int32(value))


class AttributeViInt64(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_int64(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_int64(self._attribute_id, value)


class AttributeViReal64(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_real64(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_real64(self._attribute_id, value)


class AttributeViReal64TimeDeltaSeconds(Attribute):

    def __get__(self, session, session_type):
        return hightime.timedelta(seconds=session._get_attribute_vi_real64(self._attribute_id))

    def __set__(self, session, value):
        session._set_attribute_vi_real64(self._attribute_id, _converters.convert_timedelta_to_seconds_real64(value))


class AttributeViString(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_string(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_string(self._attribute_id, value)


class AttributeViStringRepeatedCapability(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_string(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_string(self._attribute_id, _converters.convert_repeated_capabilities_without_prefix(value))


class AttributeViStringCommaSeparated(Attribute):

    def __get__(self, session, session_type):
        return _converters.convert_comma_separated_string_to_list(session._get_attribute_vi_string(self._attribute_id))

    def __set__(self, session, value):
        session._set_attribute_vi_string(self._attribute_id, _converters.convert_list_to_comma_separated_string(value))


class AttributeViBoolean(Attribute):

    def __get__(self, session, session_type):
        return session._get_attribute_vi_boolean(self._attribute_id)

    def __set__(self, session, value):
        session._set_attribute_vi_boolean(self._attribute_id, value)


class AttributeEnum(Attribute):

    def __init__(self, underlying_attribute_meta_class, enum_meta_class, attribute_id):
        super(AttributeEnum, self).__init__(attribute_id)
        self._underlying_attribute = underlying_attribute_meta_class(attribute_id)
        self._attribute_type = enum_meta_class

    def __get__(self, session, session_type):
        return self._attribute_type(self._underlying_attribute.__get__(session, session_type))

    def __set__(self, session, value):
        if type(value) is not self._attribute_type:
            raise TypeError('must be ' + str(self._attribute_type.__name__) + ' not ' + str(type(value).__name__))
        return self._underlying_attribute.__set__(session, value.value)


class AttributeEnumWithConverter(Attribute):
    '''Class for attributes that use enums internally but are exposed in the nidcpower Python module as something else, thus need conversion.'''

    def __init__(self, underlying_attribute_enum, getter_converter, setter_converter):
        '''Creates and returns an instance of AttributeEnumWithConverter attribute meta class.

        Args:
            underlying_attribute_enum (AttributeEnum): The AttributeEnum instance for the underlying
                enum

            getter_converter (function): The function that converts the enum value to its converted
                value

            setter_converter (function): The function that converts the converted value back to the
                enum value
        '''
        super(AttributeEnumWithConverter, self).__init__(underlying_attribute_enum._attribute_id)
        self._underlying_attribute_enum = underlying_attribute_enum
        self._getter_converter = getter_converter
        self._setter_converter = setter_converter

    def __get__(self, session, session_type):
        try:
            return self._getter_converter(
                self._underlying_attribute_enum.__get__(session, session_type)
            )
        except (KeyError, ValueError):
            raise errors.DriverTooNewError()

    def __set__(self, session, value):
        try:
            return self._underlying_attribute_enum.__set__(session, self._setter_converter(value))
        except KeyError:
            raise ValueError(f'Invalid value: {value}')


# nitclk specific attribute type
class AttributeSessionReference(Attribute):

    def __get__(self, session, session_type):
        # Import here to avoid a circular dependency when initial import happens
        from nidcpower.session import SessionReference
        return SessionReference(session._get_attribute_vi_session(self._attribute_id))

    def __set__(self, session, value):
        session._set_attribute_vi_session(self._attribute_id, _converters.convert_to_nitclk_session_number(value))
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidcpower/nidcpower/_converters.py sha256=c4298604b7d6c66e11318a92efa3a3337958d6ce177aa0e3a8f8e9f8bd4a0e46 bytes=15355 -->
## FILE: generated/nidcpower/nidcpower/_converters.py

- repository: `ni/nimi-python`
- source_path: `generated/nidcpower/nidcpower/_converters.py`
- sha256: `c4298604b7d6c66e11318a92efa3a3337958d6ce177aa0e3a8f8e9f8bd4a0e46`
- bytes: 15355

````python
# -*- coding: utf-8 -*-
# This file was generated
import nidcpower._visatype as _visatype
import nidcpower.enums as enums
import nidcpower.errors as errors

import array
import collections
import hightime
import numbers

from functools import singledispatch


@singledispatch
def _convert_repeated_capabilities(arg, prefix):  # noqa: F811
    '''Base version that should not be called

    Overall purpose is to convert the repeated capabilities to a list of strings with prefix from what ever form

    Supported types:
    - str - List (comma delimited)
    - str - Range (using '-' or ':')
    - str - single item
    - int
    - tuple
    - range
    - slice

    Each instance should return a list of strings, without prefix
    - '0' --> ['0']
    - 0 --> ['0']
    - '0, 1' --> ['0', '1']
    - 'ScriptTrigger0, ScriptTrigger1' --> ['0', '1']
    - '0-1' --> ['0', '1']
    - '0:1' --> ['0', '1']
    - '0-1,4' --> ['0', '1', '4']
    - range(0, 2) --> ['0', '1']
    - slice(0, 2) --> ['0', '1']
    - (0, 1, 4) --> ['0', '1', '4']
    - ('0-1', 4) --> ['0', '1', '4']
    - (slice(0, 1), '2', [4, '5-6'], '7-9', '11:14', '16, 17') -->
        ['0', '2', '4', '5', '6', '7', '8', '9', '11', '12', '13', '14', '16', '17']
    '''
    raise errors.InvalidRepeatedCapabilityError('Invalid type', type(arg))


@_convert_repeated_capabilities.register(numbers.Integral)  # noqa: F811
def _(repeated_capability, prefix):
    '''Integer version'''
    return [str(repeated_capability)]


# This parsing function duplicate the parsing in the driver, so if changes to the allowed format are made there, they will need to be replicated here.
@_convert_repeated_capabilities.register(str)  # noqa: F811
def _(repeated_capability, prefix):
    '''String version (this is the most complex)

    We need to deal with a range ('0-3' or '0:3'), a list ('0,1,2,3') and a single item
    '''
    # First we deal with a list
    rep_cap_list = repeated_capability.split(',')
    if len(rep_cap_list) > 1:
        # We have a list so call ourselves again to let the iterable instance handle it
        return _convert_repeated_capabilities(rep_cap_list, prefix)

    # Now we deal with ranges
    # We remove any prefix and change ':' to '-'
    r = repeated_capability.strip().replace(prefix, '').replace(':', '-')
    rc = r.split('-')
    if len(rc) > 1:
        if len(rc) > 2:
            raise errors.InvalidRepeatedCapabilityError("Multiple '-' or ':'", repeated_capability)
        try:
            start = int(rc[0])
            end = int(rc[1])
        except ValueError:
            # This exception is raised when repeated_capability is of the form "dev/0-1". rc[0] == "dev/0" in this case.
            # Just return the repeated_capability string as-is in that case.
            pass
        else:
            if end < start:
                rng = range(start, end - 1, -1)
            else:
                rng = range(start, end + 1)
            return _convert_repeated_capabilities(rng, prefix)

    # If we made it here, it must be a simple item so we remove any prefix and return
    return [repeated_capability.replace(prefix, '').strip()]


# We cannot use collections.abc.Iterable here because strings are also iterable and then this
# instance is what gets called instead of the string one.
@_convert_repeated_capabilities.register(list)  # noqa: F811
@_convert_repeated_capabilities.register(range)  # noqa: F811
@_convert_repeated_capabilities.register(tuple)  # noqa: F811
def _(repeated_capability, prefix):
    '''Iterable version - can handle lists, ranges, and tuples'''
    rep_cap_list = []
    for r in repeated_capability:
        rep_cap_list += _convert_repeated_capabilities(r, prefix)
    return rep_cap_list


@_convert_repeated_capabilities.register(slice)  # noqa: F811
def _(repeated_capability, prefix):
    '''slice version'''
    def ifnone(a, b):
        return b if a is None else a
    # Turn the slice into a list and call ourselves again to let the iterable instance handle it
    rng = range(ifnone(repeated_capability.start, 0), repeated_capability.stop, ifnone(repeated_capability.step, 1))
    return _convert_repeated_capabilities(rng, prefix)


def convert_repeated_capabilities(repeated_capability, prefix=''):
    '''Convert a repeated capabilities object to a comma delimited list

    Args:
        repeated_capability (str, list, tuple, slice, None) -
        prefix (str) - common prefix for all strings

    Returns:
        rep_cap_list (list of str) - list of each repeated capability item with ranges expanded and prefix added
    '''
    # We need to explicitly handle None here. Everything else we can pass on to the singledispatch functions
    if repeated_capability is None:
        return []
    return [prefix + r for r in _convert_repeated_capabilities(repeated_capability, prefix)]


def convert_repeated_capabilities_without_prefix(repeated_capability):
    '''Convert a repeated capabilities object, without any prefix, to a comma delimited list

    Args:
        repeated_capability - Supported types:
            - str - list (comma-delimited)
            - str - range (using '-' or ':')
            - str - single item
            - int
            - list of str
            - tuple of str
            - range of str
            - slice of str
            - None

    Returns:
        rep_cap (str) - comma delimited string of each repeated capability item with ranges expanded
    '''
    return ','.join(convert_repeated_capabilities(repeated_capability, ''))


def expand_channel_string(channel_string, all_channels_in_session):
    '''Expands a channel_string to a list of individual channel names.

    The individual channel names may or may not be fully qualified channel names as applicable for
    the session. In other words, the individual channel names will be a subset of
    all_channels_in_session.

    Examples:
        - expand_channel_string('1', ['0', '1', '2', '3']) --> ['1']
        - expand_channel_string('4,1:2', ['1', '2', '4']) --> ['4', '1', '2']
        - expand_channel_string('2:3,0', ['Dev1/0', 'Dev1/1', 'Dev1/2', 'Dev1/3'])
            --> ['Dev1/2', 'Dev1/3', 'Dev1/0']
        - expand_channel_string('Dev1/1', ['Dev1/0', 'Dev1/1', 'Dev1/2', 'Dev1/3'])
            --> ['Dev1/1']
        - expand_channel_string('4,Dev1/1:2', ['Dev1/1', 'Dev1/2', 'Dev1/4'])
            --> ['Dev1/4', 'Dev1/1', 'Dev1/2']
        - expand_channel_string('Dev1/4,Dev1/2,Dev1/3', ['Dev1/2', 'Dev1/3', 'Dev1/4'])
            --> ['Dev1/4', 'Dev1/2', 'Dev1/3']
        - expand_channel_string('Dev1/1,Dev2/2', ['Dev1/0', 'Dev1/1', 'Dev1/2', 'Dev1/3', 'Dev2/0', 'Dev2/1', 'Dev2/2', 'Dev2/3'])
            --> ['Dev1/1', 'Dev2/2']
        - expand_channel_string(' Dev1 / 1 : 2 , 4 ', ['Dev1/1', 'Dev1/2', 'Dev1/4'])
            --> ['Dev1/1', 'Dev1/2', 'Dev1/4']
        - expand_channel_string('DEV1/0-1    , Dev1/3', ['dev1/0', 'dev1/1', 'dev1/2', 'dev1/3'])
            --> ['dev1/0', 'dev1/1', 'dev1/3']

    Args:
        channel_string (str) - refer to _convert_repeated_capabilities() for the
            supported formats (this string is expected to be used as the index of session.channels)

        all_channels_in_session (list of str) - names of all the channels in the session as returned
            by get_channel_names()

    Returns:
        channel_names (list of str) - A list in which each element is the name of a single channel,
            with the exact capitalization used by the driver runtime.
    '''
    if channel_string.strip() == '':
        return all_channels_in_session

    # Rule 1: If all_channels_in_session is fully-qualified then returned channel names should be
    #         fully-qualified, otherwise returned channel names should not be fully-qualified.
    # Rule 2: If any channel in the input is not fully-qualified, but we need to return
    #         fully-qualified channels because of Rule 1, then use the channel qualifier obtained
    #         from all_channels_in_session. This can only happen on a single-instrument session,
    #         so all the channel qualifiers are the same and we pick the first one.

    instrument, separator, channel = all_channels_in_session[0].rpartition('/')
    default_channel_qualifier = instrument + separator

    expanded_channel_list = []
    for token in channel_string.split(','):
        instrument, separator, channel = token.rpartition('/')
        instrument = instrument.strip()
        channel_qualifier = instrument + separator if instrument else default_channel_qualifier
        expanded_channel_list.extend(
            convert_repeated_capabilities(channel.strip(), channel_qualifier)
        )

    # Convert the expanded channel names to their canonical form based on all_channels_in_session
    lowercase_channel_name_to_session_channel_name_dict = {
        channel_name.lower(): channel_name for channel_name in all_channels_in_session
    }
    return [
        lowercase_channel_name_to_session_channel_name_dict[channel_name.lower()]
        for channel_name in expanded_channel_list
    ]


def _convert_timedelta(value, library_type, scaling):
    try:
        # We first assume it is a timedelta object
        scaled_value = value.total_seconds() * scaling
    except AttributeError:
        # If that doesn't work, assume it is a value in seconds
        # cast to float so scaled_value is always a float. This allows `timeout=10` to work as expected
        scaled_value = float(value) * scaling

    # ctype integer types don't convert to int from float so we need to
    if library_type in [_visatype.ViInt64, _visatype.ViInt32, _visatype.ViUInt32, _visatype.ViInt16, _visatype.ViUInt16, _visatype.ViInt8]:
        scaled_value = int(scaled_value)

    return scaled_value


def convert_timedelta_to_seconds_real64(value):
    return _convert_timedelta(value, _visatype.ViReal64, 1)


def convert_timedelta_to_milliseconds_int32(value):
    return _convert_timedelta(value, _visatype.ViInt32, 1000)


def convert_timedeltas_to_seconds_real64(values):
    return [convert_timedelta_to_seconds_real64(i) for i in values]


def convert_seconds_real64_to_timedelta(value):
    return hightime.timedelta(seconds=value)


def convert_seconds_real64_to_timedeltas(values):
    return [convert_seconds_real64_to_timedelta(i) for i in values]


def convert_month_to_timedelta(months):
    return hightime.timedelta(days=(30.4167 * months))


# Scaling factor to apply on seconds to get months
# would be 1/(60 seconds * 60 minutes * 24 hours * 30.4167 days)
def convert_timedelta_to_months_int32(value):
    return _convert_timedelta(value, _visatype.ViInt32, 1.0 / (60 * 60 * 24 * 30.4167))


# This converter is not called from the normal codegen path for function. Instead it is
# call from init and is a special case.
def convert_init_with_options_dictionary(values):
    if type(values) is str:
        init_with_options_string = values
    else:
        good_keys = {
            'rangecheck': 'RangeCheck',
            'queryinstrstatus': 'QueryInstrStatus',
            'cache': 'Cache',
            'simulate': 'Simulate',
            'recordcoercions': 'RecordCoercions',
            'interchangecheck': 'InterchangeCheck',
            'driversetup': 'DriverSetup',
            'range_check': 'RangeCheck',
            'query_instr_status': 'QueryInstrStatus',
            'record_coercions': 'RecordCoercions',
            'interchange_check': 'InterchangeCheck',
            'driver_setup': 'DriverSetup',
        }
        init_with_options = []
        for k in sorted(values.keys()):
            value = None
            if k.lower() in good_keys and not good_keys[k.lower()] == 'DriverSetup':
                value = good_keys[k.lower()] + ('=1' if values[k] is True else '=0')
            elif k.lower() in good_keys and good_keys[k.lower()] == 'DriverSetup':
                if not isinstance(values[k], dict):
                    raise TypeError('DriverSetup must be a dictionary')
                value = 'DriverSetup=' + (';'.join([key + ':' + values[k][key] for key in sorted(values[k])]))
            else:
                value = k + ('=1' if values[k] is True else '=0')

            init_with_options.append(value)

        init_with_options_string = ','.join(init_with_options)

    return init_with_options_string


# convert value to bytes
@singledispatch
def _convert_to_bytes(value):  # noqa: F811
    pass


@_convert_to_bytes.register(list)  # noqa: F811
@_convert_to_bytes.register(bytes)  # noqa: F811
@_convert_to_bytes.register(bytearray)  # noqa: F811
@_convert_to_bytes.register(array.array)  # noqa: F811
def _(value):
    return value


@_convert_to_bytes.register(str)  # noqa: F811
def _(value):
    return value.encode()


def convert_to_bytes(value):  # noqa: F811
    return bytes(_convert_to_bytes(value))


def convert_comma_separated_string_to_list(comma_separated_string):
    return [x.strip() for x in comma_separated_string.split(',')]


def convert_list_to_comma_separated_string(list_of_strings):
    '''Convert a list or tuple of strings into a comma-separated string.

    Args:
        list_of_strings (list or tuple of str): List or tuple of strings.

    Returns:
        str: Comma-separated string.
    '''
    if not isinstance(list_of_strings, (list, tuple)) or not all(isinstance(item, str) for item in list_of_strings):
        raise TypeError('Input must be a list or tuple of str')
    return ','.join(list_of_strings)


def convert_chained_repeated_capability_to_parts(chained_repeated_capability):
    '''Convert a chained repeated capabilities string to a list of comma-delimited repeated capabilities string.

    Converter assumes that the input contains the full cartesian product of its parts.
    e.g. If chained_repeated_capability is 'site0/PinA,site0/PinB,site1/PinA,site1/PinB',
    ['site0,site1', 'PinA,PinB'] is returned.

    Args:
        chained_repeated_capability (str) - comma-delimited repeated capabilities string where each
        item is a chain of slash-delimited repeated capabilities

    Returns:
        rep_cap_list (list of str) - list of comma-delimited repeated capabilities string
    '''
    chained_repeated_capability_items = convert_comma_separated_string_to_list(chained_repeated_capability)
    repeated_capability_lists = [[] for _ in range(chained_repeated_capability_items[0].count('/') + 1)]
    for item in chained_repeated_capability_items:
        repeated_capability_lists = [x + [y] for x, y in zip(repeated_capability_lists, item.split('/'))]
    return [','.join(collections.OrderedDict.fromkeys(x)) for x in repeated_capability_lists]


def convert_from_isolation_state_enum(value):
    return {
        enums._IsolationState.ISOLATED: True,
        enums._IsolationState.NON_ISOLATED: False,
    }[value]


def convert_to_isolation_state_enum(value):
    return {
        True: enums._IsolationState.ISOLATED,
        False: enums._IsolationState.NON_ISOLATED,
    }[value]


def convert_from_lcr_impedance_auto_range_enum(value):
    return {
        enums._LCRImpedanceAutoRange.OFF: False,
        enums._LCRImpedanceAutoRange.ON: True,
    }[value]


def convert_to_lcr_impedance_auto_range_enum(value):
    return {
        False: enums._LCRImpedanceAutoRange.OFF,
        True: enums._LCRImpedanceAutoRange.ON,
    }[value]
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidcpower/nidcpower/_grpc_stub_interpreter.py sha256=c998ab4e00191a75f15d5f759c405e7306ecad03a0badbe9eb5937f69fcd3017 bytes=23991 -->
## FILE: generated/nidcpower/nidcpower/_grpc_stub_interpreter.py

- repository: `ni/nimi-python`
- source_path: `generated/nidcpower/nidcpower/_grpc_stub_interpreter.py`
- sha256: `c998ab4e00191a75f15d5f759c405e7306ecad03a0badbe9eb5937f69fcd3017`
- bytes: 23991

````python
# -*- coding: utf-8 -*-
# This file was generated

import grpc
import hightime  # noqa: F401
import session_pb2 as session_grpc_types
import threading
import warnings

from . import enums as enums  # noqa: F401
from . import errors as errors
from . import nidcpower_pb2 as grpc_types
from . import nidcpower_pb2_grpc as nidcpower_grpc

from . import lcr_measurement as lcr_measurement  # noqa: F401

from . import lcr_load_compensation_spot as lcr_load_compensation_spot  # noqa: F401


class GrpcStubInterpreter(object):
    '''Interpreter for interacting with a gRPC Stub class'''

    def __init__(self, grpc_options):
        self._grpc_options = grpc_options
        self._lock = threading.RLock()
        self._client = nidcpower_grpc.NiDCPowerStub(grpc_options.grpc_channel)
        self.set_session_handle()

    def set_session_handle(self, value=session_grpc_types.Session()):
        self._vi = value

    def get_session_handle(self):
        return self._vi

    def _invoke(self, func, request, metadata=None):
        try:
            response = func(request, metadata=metadata)
            error_code = response.status
            error_message = ''
        except grpc.RpcError as rpc_error:
            error_code = None
            error_message = rpc_error.details()
            for entry in rpc_error.trailing_metadata() or []:
                if entry.key == 'ni-error':
                    value = entry.value if isinstance(entry.value, str) else entry.value.decode('utf-8')
                    try:
                        error_code = int(value)
                    except ValueError:
                        error_message += f'\nError status: {value}'

            grpc_error = rpc_error.code()
            if grpc_error == grpc.StatusCode.NOT_FOUND:
                raise errors.DriverTooOldError() from None
            elif grpc_error == grpc.StatusCode.INVALID_ARGUMENT:
                raise ValueError(error_message) from None
            elif grpc_error == grpc.StatusCode.UNAVAILABLE:
                error_message = 'Failed to connect to server'
            elif grpc_error == grpc.StatusCode.UNIMPLEMENTED:
                error_message = (
                    'This operation is not supported by the NI gRPC Device Server being used. Upgrade NI gRPC Device Server.'
                )

            if error_code is None:
                raise errors.RpcError(grpc_error, error_message) from None

        if error_code < 0:
            raise errors.DriverError(error_code, error_message)
        elif error_code > 0:
            if not error_message:
                try:
                    error_message = self.error_message(error_code)
                except errors.Error:
                    error_message = 'Failed to retrieve error description.'
            warnings.warn(errors.DriverWarning(error_code, error_message))
        return response

    def abort(self, channel_name):  # noqa: N802
        self._invoke(
            self._client.AbortWithChannels,
            grpc_types.AbortWithChannelsRequest(vi=self._vi, channel_name=channel_name),
        )

    def self_cal(self, channel_name):  # noqa: N802
        self._invoke(
            self._client.CalSelfCalibrate,
            grpc_types.CalSelfCalibrateRequest(vi=self._vi, channel_name=channel_name),
        )

    def clear_latched_output_cutoff_state(self, channel_name, output_cutoff_reason):  # noqa: N802
        self._invoke(
            self._client.ClearLatchedOutputCutoffState,
            grpc_types.ClearLatchedOutputCutoffStateRequest(vi=self._vi, channel_name=channel_name, output_cutoff_reason_raw=output_cutoff_reason.value),
        )

    def commit(self, channel_name):  # noqa: N802
        self._invoke(
            self._client.CommitWithChannels,
            grpc_types.CommitWithChannelsRequest(vi=self._vi, channel_name=channel_name),
        )

    def configure_aperture_time(self, channel_name, aperture_time, units):  # noqa: N802
        self._invoke(
            self._client.ConfigureApertureTime,
            grpc_types.ConfigureApertureTimeRequest(vi=self._vi, channel_name=channel_name, aperture_time=aperture_time, units_raw=units.value),
        )

    def configure_lcr_compensation(self, channel_name, compensation_data):  # noqa: N802
        raise NotImplementedError('configure_lcr_compensation is not supported over gRPC')

    def configure_lcr_custom_cable_compensation(self, channel_name, custom_cable_compensation_data):  # noqa: N802
        self._invoke(
            self._client.ConfigureLCRCustomCableCompensation,
            grpc_types.ConfigureLCRCustomCableCompensationRequest(vi=self._vi, channel_name=channel_name, custom_cable_compensation_data=custom_cable_compensation_data),
        )

    def create_advanced_sequence_commit_step(self, channel_name, set_as_active_step):  # noqa: N802
        self._invoke(
            self._client.CreateAdvancedSequenceCommitStepWithChannels,
            grpc_types.CreateAdvancedSequenceCommitStepWithChannelsRequest(vi=self._vi, channel_name=channel_name, set_as_active_step=set_as_active_step),
        )

    def create_advanced_sequence_step(self, channel_name, set_as_active_step):  # noqa: N802
        self._invoke(
            self._client.CreateAdvancedSequenceStepWithChannels,
            grpc_types.CreateAdvancedSequenceStepWithChannelsRequest(vi=self._vi, channel_name=channel_name, set_as_active_step=set_as_active_step),
        )

    def create_advanced_sequence_with_channels(self, channel_name, sequence_name, attribute_ids, set_as_active_sequence):  # noqa: N802
        self._invoke(
            self._client.CreateAdvancedSequenceWithChannels,
            grpc_types.CreateAdvancedSequenceWithChannelsRequest(vi=self._vi, channel_name=channel_name, sequence_name=sequence_name, attribute_ids=attribute_ids, set_as_active_sequence=set_as_active_sequence),
        )

    def delete_advanced_sequence(self, channel_name, sequence_name):  # noqa: N802
        self._invoke(
            self._client.DeleteAdvancedSequenceWithChannels,
            grpc_types.DeleteAdvancedSequenceWithChannelsRequest(vi=self._vi, channel_name=channel_name, sequence_name=sequence_name),
        )

    def disable(self):  # noqa: N802
        self._invoke(
            self._client.Disable,
            grpc_types.DisableRequest(vi=self._vi),
        )

    def export_attribute_configuration_buffer(self):  # noqa: N802
        response = self._invoke(
            self._client.ExportAttributeConfigurationBuffer,
            grpc_types.ExportAttributeConfigurationBufferRequest(vi=self._vi),
        )
        return response.configuration

    def export_attribute_configuration_file(self, file_path):  # noqa: N802
        self._invoke(
            self._client.ExportAttributeConfigurationFile,
            grpc_types.ExportAttributeConfigurationFileRequest(vi=self._vi, file_path=file_path),
        )

    def fancy_initialize(self, resource_name, channels, reset, option_string, independent_channels):  # noqa: N802
        response = self._invoke(
            self._client.FancyInitialize,
            grpc_types.FancyInitializeRequest(resource_name=resource_name, channels=channels, reset=reset, option_string=option_string, independent_channels=independent_channels),
        )
        return response.vi

    def fetch_multiple(self, channel_name, timeout, count):  # noqa: N802
        response = self._invoke(
            self._client.FetchMultiple,
            grpc_types.FetchMultipleRequest(vi=self._vi, channel_name=channel_name, timeout=timeout, count=count),
        )
        return response.voltage_measurements, response.current_measurements, response.in_compliance

    def fetch_multiple_lcr(self, channel_name, timeout, count):  # noqa: N802
        response = self._invoke(
            self._client.FetchMultipleLCR,
            grpc_types.FetchMultipleLCRRequest(vi=self._vi, channel_name=channel_name, timeout=timeout, count=count),
        )
        return [lcr_measurement.LCRMeasurement(x) for x in response.measurements]

    def get_attribute_vi_boolean(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViBoolean,
            grpc_types.GetAttributeViBooleanRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
        )
        return response.attribute_value

    def get_attribute_vi_int32(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViInt32,
            grpc_types.GetAttributeViInt32Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
        )
        return response.attribute_value

    def get_attribute_vi_int64(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViInt64,
            grpc_types.GetAttributeViInt64Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
        )
        return response.attribute_value

    def get_attribute_vi_real64(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViReal64,
            grpc_types.GetAttributeViReal64Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
        )
        return response.attribute_value

    def get_attribute_vi_string(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViString,
            grpc_types.GetAttributeViStringRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
        )
        return response.attribute_value

    def get_channel_name(self, index):  # noqa: N802
        response = self._invoke(
            self._client.GetChannelName,
            grpc_types.GetChannelNameRequest(vi=self._vi, index=index),
        )
        return response.channel_name

    def get_channel_names(self, indices):  # noqa: N802
        response = self._invoke(
            self._client.GetChannelNameFromString,
            grpc_types.GetChannelNameFromStringRequest(vi=self._vi, index=indices),
        )
        return response.channel_name

    def get_error(self):  # noqa: N802
        response = self._invoke(
            self._client.GetError,
            grpc_types.GetErrorRequest(vi=self._vi),
        )
        return response.code, response.description

    def get_ext_cal_last_date_and_time(self):  # noqa: N802
        response = self._invoke(
            self._client.GetExtCalLastDateAndTime,
            grpc_types.GetExtCalLastDateAndTimeRequest(vi=self._vi),
        )
        return response.year, response.month, response.day, response.hour, response.minute

    def get_ext_cal_last_temp(self):  # noqa: N802
        response = self._invoke(
            self._client.GetExtCalLastTemp,
            grpc_types.GetExtCalLastTempRequest(vi=self._vi),
        )
        return response.temperature

    def get_ext_cal_recommended_interval(self):  # noqa: N802
        response = self._invoke(
            self._client.GetExtCalRecommendedInterval,
            grpc_types.GetExtCalRecommendedIntervalRequest(vi=self._vi),
        )
        return response.months

    def get_lcr_compensation_data(self, channel_name):  # noqa: N802
        raise NotImplementedError('get_lcr_compensation_data is not supported over gRPC')

    def get_lcr_compensation_last_date_and_time(self, channel_name, compensation_type):  # noqa: N802
        response = self._invoke(
            self._client.GetLCRCompensationLastDateAndTime,
            grpc_types.GetLCRCompensationLastDateAndTimeRequest(vi=self._vi, channel_name=channel_name, compensation_type_raw=compensation_type.value),
        )
        return response.year, response.month, response.day, response.hour, response.minute

    def get_lcr_custom_cable_compensation_data(self, channel_name):  # noqa: N802
        response = self._invoke(
            self._client.GetLCRCustomCableCompensationData,
            grpc_types.GetLCRCustomCableCompensationDataRequest(vi=self._vi, channel_name=channel_name),
        )
        return response.custom_cable_compensation_data

    def get_self_cal_last_date_and_time(self):  # noqa: N802
        response = self._invoke(
            self._client.GetSelfCalLastDateAndTime,
            grpc_types.GetSelfCalLastDateAndTimeRequest(vi=self._vi),
        )
        return response.year, response.month, response.day, response.hour, response.minute

    def get_self_cal_last_temp(self):  # noqa: N802
        response = self._invoke(
            self._client.GetSelfCalLastTemp,
            grpc_types.GetSelfCalLastTempRequest(vi=self._vi),
        )
        return response.temperature

    def import_attribute_configuration_buffer(self, configuration):  # noqa: N802
        self._invoke(
            self._client.ImportAttributeConfigurationBuffer,
            grpc_types.ImportAttributeConfigurationBufferRequest(vi=self._vi, configuration=configuration),
        )

    def import_attribute_configuration_file(self, file_path):  # noqa: N802
        self._invoke(
            self._client.ImportAttributeConfigurationFile,
            grpc_types.ImportAttributeConfigurationFileRequest(vi=self._vi, file_path=file_path),
        )

    def initialize_with_channels(self, resource_name, channels, reset, option_string):  # noqa: N802
        metadata = (
            ('ni-api-key', self._grpc_options.api_key),
        )
        response = self._invoke(
            self._client.InitializeWithChannels,
            grpc_types.InitializeWithChannelsRequest(resource_name=resource_name, channels=channels, reset=reset, option_string=option_string, session_name=self._grpc_options.session_name, initialization_behavior=self._grpc_options.initialization_behavior),
            metadata=metadata,
        )
        self._close_on_exit = response.new_session_initialized
        return response.vi

    def initialize_with_independent_channels(self, resource_name, reset, option_string):  # noqa: N802
        metadata = (
            ('ni-api-key', self._grpc_options.api_key),
        )
        response = self._invoke(
            self._client.InitializeWithIndependentChannels,
            grpc_types.InitializeWithIndependentChannelsRequest(resource_name=resource_name, reset=reset, option_string=option_string, session_name=self._grpc_options.session_name, initialization_behavior=self._grpc_options.initialization_behavior),
            metadata=metadata,
        )
        self._close_on_exit = response.new_session_initialized
        return response.vi

    def initiate_with_channels(self, channel_name):  # noqa: N802
        self._invoke(
            self._client.InitiateWithChannels,
            grpc_types.InitiateWithChannelsRequest(vi=self._vi, channel_name=channel_name),
        )

    def lock(self):  # noqa: N802
        self._lock.acquire()

    def measure(self, channel_name, measurement_type):  # noqa: N802
        response = self._invoke(
            self._client.Measure,
            grpc_types.MeasureRequest(vi=self._vi, channel_name=channel_name, measurement_type_raw=measurement_type.value),
        )
        return response.measurement

    def measure_multiple(self, channel_name):  # noqa: N802
        response = self._invoke(
            self._client.MeasureMultiple,
            grpc_types.MeasureMultipleRequest(vi=self._vi, channel_name=channel_name),
        )
        return response.voltage_measurements, response.current_measurements

    def measure_multiple_lcr(self, channel_name):  # noqa: N802
        response = self._invoke(
            self._client.MeasureMultipleLCR,
            grpc_types.MeasureMultipleLCRRequest(vi=self._vi, channel_name=channel_name),
        )
        return [lcr_measurement.LCRMeasurement(x) for x in response.measurements]

    def parse_channel_count(self, channels_string):  # noqa: N802
        raise NotImplementedError('parse_channel_count is not supported over gRPC')

    def perform_lcr_load_compensation(self, channel_name, compensation_spots):  # noqa: N802
        self._invoke(
            self._client.PerformLCRLoadCompensation,
            grpc_types.PerformLCRLoadCompensationRequest(vi=self._vi, channel_name=channel_name, compensation_spots=compensation_spots and [x._create_copy(grpc_types.NILCRLoadCompensationSpot) for x in compensation_spots]),
        )

    def perform_lcr_open_compensation(self, channel_name, additional_frequencies):  # noqa: N802
        self._invoke(
            self._client.PerformLCROpenCompensation,
            grpc_types.PerformLCROpenCompensationRequest(vi=self._vi, channel_name=channel_name, additional_frequencies=additional_frequencies),
        )

    def perform_lcr_open_custom_cable_compensation(self, channel_name):  # noqa: N802
        self._invoke(
            self._client.PerformLCROpenCustomCableCompensation,
            grpc_types.PerformLCROpenCustomCableCompensationRequest(vi=self._vi, channel_name=channel_name),
        )

    def perform_lcr_short_compensation(self, channel_name, additional_frequencies):  # noqa: N802
        self._invoke(
            self._client.PerformLCRShortCompensation,
            grpc_types.PerformLCRShortCompensationRequest(vi=self._vi, channel_name=channel_name, additional_frequencies=additional_frequencies),
        )

    def perform_lcr_short_custom_cable_compensation(self, channel_name):  # noqa: N802
        self._invoke(
            self._client.PerformLCRShortCustomCableCompensation,
            grpc_types.PerformLCRShortCustomCableCompensationRequest(vi=self._vi, channel_name=channel_name),
        )

    def query_in_compliance(self, channel_name):  # noqa: N802
        response = self._invoke(
            self._client.QueryInCompliance,
            grpc_types.QueryInComplianceRequest(vi=self._vi, channel_name=channel_name),
        )
        return response.in_compliance

    def query_latched_output_cutoff_state(self, channel_name, output_cutoff_reason):  # noqa: N802
        response = self._invoke(
            self._client.QueryLatchedOutputCutoffState,
            grpc_types.QueryLatchedOutputCutoffStateRequest(vi=self._vi, channel_name=channel_name, output_cutoff_reason_raw=output_cutoff_reason.value),
        )
        return response.output_cutoff_state

    def query_max_current_limit(self, channel_name, voltage_level):  # noqa: N802
        response = self._invoke(
            self._client.QueryMaxCurrentLimit,
            grpc_types.QueryMaxCurrentLimitRequest(vi=self._vi, channel_name=channel_name, voltage_level=voltage_level),
        )
        return response.max_current_limit

    def query_max_voltage_level(self, channel_name, current_limit):  # noqa: N802
        response = self._invoke(
            self._client.QueryMaxVoltageLevel,
            grpc_types.QueryMaxVoltageLevelRequest(vi=self._vi, channel_name=channel_name, current_limit=current_limit),
        )
        return response.max_voltage_level

    def query_min_current_limit(self, channel_name, voltage_level):  # noqa: N802
        response = self._invoke(
            self._client.QueryMinCurrentLimit,
            grpc_types.QueryMinCurrentLimitRequest(vi=self._vi, channel_name=channel_name, voltage_level=voltage_level),
        )
        return response.min_current_limit

    def query_output_state(self, channel_name, output_state):  # noqa: N802
        response = self._invoke(
            self._client.QueryOutputState,
            grpc_types.QueryOutputStateRequest(vi=self._vi, channel_name=channel_name, output_state_raw=output_state.value),
        )
        return response.in_state

    def read_current_temperature(self):  # noqa: N802
        response = self._invoke(
            self._client.ReadCurrentTemperature,
            grpc_types.ReadCurrentTemperatureRequest(vi=self._vi),
        )
        return response.temperature

    def reset_device(self):  # noqa: N802
        self._invoke(
            self._client.ResetDevice,
            grpc_types.ResetDeviceRequest(vi=self._vi),
        )

    def reset(self, channel_name):  # noqa: N802
        self._invoke(
            self._client.ResetWithChannels,
            grpc_types.ResetWithChannelsRequest(vi=self._vi, channel_name=channel_name),
        )

    def reset_with_defaults(self):  # noqa: N802
        self._invoke(
            self._client.ResetWithDefaults,
            grpc_types.ResetWithDefaultsRequest(vi=self._vi),
        )

    def send_software_edge_trigger(self, channel_name, trigger):  # noqa: N802
        self._invoke(
            self._client.SendSoftwareEdgeTriggerWithChannels,
            grpc_types.SendSoftwareEdgeTriggerWithChannelsRequest(vi=self._vi, channel_name=channel_name, trigger_raw=trigger.value),
        )

    def set_attribute_vi_boolean(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViBoolean,
            grpc_types.SetAttributeViBooleanRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, attribute_value=attribute_value),
        )

    def set_attribute_vi_int32(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViInt32,
            grpc_types.SetAttributeViInt32Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, attribute_value_raw=attribute_value),
        )

    def set_attribute_vi_int64(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViInt64,
            grpc_types.SetAttributeViInt64Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, attribute_value_raw=attribute_value),
        )

    def set_attribute_vi_real64(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViReal64,
            grpc_types.SetAttributeViReal64Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, attribute_value_raw=attribute_value),
        )

    def set_attribute_vi_string(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViString,
            grpc_types.SetAttributeViStringRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, attribute_value_raw=attribute_value),
        )

    def set_runtime_environment(self, environment, environment_version, reserved1, reserved2):  # noqa: N802
        raise NotImplementedError('set_runtime_environment is not supported over gRPC')

    def set_sequence(self, channel_name, values, source_delays):  # noqa: N802
        self._invoke(
            self._client.SetSequence,
            grpc_types.SetSequenceRequest(vi=self._vi, channel_name=channel_name, values=values, source_delays=source_delays),
        )

    def unlock(self):  # noqa: N802
        self._lock.release()

    def wait_for_event(self, channel_name, event_id, timeout):  # noqa: N802
        self._invoke(
            self._client.WaitForEventWithChannels,
            grpc_types.WaitForEventWithChannelsRequest(vi=self._vi, channel_name=channel_name, event_id_raw=event_id.value, timeout=timeout),
        )

    def close(self):  # noqa: N802
        self._invoke(
            self._client.Close,
            grpc_types.CloseRequest(vi=self._vi),
        )

    def error_message(self, error_code):  # noqa: N802
        response = self._invoke(
            self._client.ErrorMessage,
            grpc_types.ErrorMessageRequest(vi=self._vi, error_code=error_code),
        )
        return response.error_message

    def self_test(self):  # noqa: N802
        response = self._invoke(
            self._client.SelfTest,
            grpc_types.SelfTestRequest(vi=self._vi),
        )
        return response.self_test_result, response.self_test_message
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidcpower/nidcpower/_library.py sha256=455763be1f6758168f9ad30a19f752b023c5306bc9ed3ff5a7e957086239c659 bytes=52552 -->
## FILE: generated/nidcpower/nidcpower/_library.py

- repository: `ni/nimi-python`
- source_path: `generated/nidcpower/nidcpower/_library.py`
- sha256: `455763be1f6758168f9ad30a19f752b023c5306bc9ed3ff5a7e957086239c659`
- bytes: 52552

````python
# -*- coding: utf-8 -*-
# This file was generated

import ctypes
import nidcpower.errors as errors
import threading

from nidcpower._visatype import *  # noqa: F403,H303

import nidcpower.lcr_measurement as lcr_measurement  # noqa: F401

import nidcpower.lcr_load_compensation_spot as lcr_load_compensation_spot  # noqa: F401


class Library(object):
    '''Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    '''

    def __init__(self, ctypes_library):
        self._func_lock = threading.Lock()
        self._library = ctypes_library
        # We cache the cfunc object from the ctypes.CDLL object
        self.niDCPower_AbortWithChannels_cfunc = None
        self.niDCPower_CalSelfCalibrate_cfunc = None
        self.niDCPower_ClearLatchedOutputCutoffState_cfunc = None
        self.niDCPower_CommitWithChannels_cfunc = None
        self.niDCPower_ConfigureApertureTime_cfunc = None
        self.niDCPower_ConfigureLCRCompensation_cfunc = None
        self.niDCPower_ConfigureLCRCustomCableCompensation_cfunc = None
        self.niDCPower_CreateAdvancedSequenceCommitStepWithChannels_cfunc = None
        self.niDCPower_CreateAdvancedSequenceStepWithChannels_cfunc = None
        self.niDCPower_CreateAdvancedSequenceWithChannels_cfunc = None
        self.niDCPower_DeleteAdvancedSequenceWithChannels_cfunc = None
        self.niDCPower_Disable_cfunc = None
        self.niDCPower_ExportAttributeConfigurationBuffer_cfunc = None
        self.niDCPower_ExportAttributeConfigurationFile_cfunc = None
        self.niDCPower_FancyInitialize_cfunc = None
        self.niDCPower_FetchMultiple_cfunc = None
        self.niDCPower_FetchMultipleLCR_cfunc = None
        self.niDCPower_GetAttributeViBoolean_cfunc = None
        self.niDCPower_GetAttributeViInt32_cfunc = None
        self.niDCPower_GetAttributeViInt64_cfunc = None
        self.niDCPower_GetAttributeViReal64_cfunc = None
        self.niDCPower_GetAttributeViString_cfunc = None
        self.niDCPower_GetChannelName_cfunc = None
        self.niDCPower_GetChannelNameFromString_cfunc = None
        self.niDCPower_GetError_cfunc = None
        self.niDCPower_GetExtCalLastDateAndTime_cfunc = None
        self.niDCPower_GetExtCalLastTemp_cfunc = None
        self.niDCPower_GetExtCalRecommendedInterval_cfunc = None
        self.niDCPower_GetLCRCompensationData_cfunc = None
        self.niDCPower_GetLCRCompensationLastDateAndTime_cfunc = None
        self.niDCPower_GetLCRCustomCableCompensationData_cfunc = None
        self.niDCPower_GetSelfCalLastDateAndTime_cfunc = None
        self.niDCPower_GetSelfCalLastTemp_cfunc = None
        self.niDCPower_ImportAttributeConfigurationBuffer_cfunc = None
        self.niDCPower_ImportAttributeConfigurationFile_cfunc = None
        self.niDCPower_InitializeWithChannels_cfunc = None
        self.niDCPower_InitializeWithIndependentChannels_cfunc = None
        self.niDCPower_InitiateWithChannels_cfunc = None
        self.niDCPower_LockSession_cfunc = None
        self.niDCPower_Measure_cfunc = None
        self.niDCPower_MeasureMultiple_cfunc = None
        self.niDCPower_MeasureMultipleLCR_cfunc = None
        self.niDCPower_ParseChannelCount_cfunc = None
        self.niDCPower_PerformLCRLoadCompensation_cfunc = None
        self.niDCPower_PerformLCROpenCompensation_cfunc = None
        self.niDCPower_PerformLCROpenCustomCableCompensation_cfunc = None
        self.niDCPower_PerformLCRShortCompensation_cfunc = None
        self.niDCPower_PerformLCRShortCustomCableCompensation_cfunc = None
        self.niDCPower_QueryInCompliance_cfunc = None
        self.niDCPower_QueryLatchedOutputCutoffState_cfunc = None
        self.niDCPower_QueryMaxCurrentLimit_cfunc = None
        self.niDCPower_QueryMaxVoltageLevel_cfunc = None
        self.niDCPower_QueryMinCurrentLimit_cfunc = None
        self.niDCPower_QueryOutputState_cfunc = None
        self.niDCPower_ReadCurrentTemperature_cfunc = None
        self.niDCPower_ResetDevice_cfunc = None
        self.niDCPower_ResetWithChannels_cfunc = None
        self.niDCPower_ResetWithDefaults_cfunc = None
        self.niDCPower_SendSoftwareEdgeTriggerWithChannels_cfunc = None
        self.niDCPower_SetAttributeViBoolean_cfunc = None
        self.niDCPower_SetAttributeViInt32_cfunc = None
        self.niDCPower_SetAttributeViInt64_cfunc = None
        self.niDCPower_SetAttributeViReal64_cfunc = None
        self.niDCPower_SetAttributeViString_cfunc = None
        self.niDCPower_SetRuntimeEnvironment_cfunc = None
        self.niDCPower_SetSequence_cfunc = None
        self.niDCPower_UnlockSession_cfunc = None
        self.niDCPower_WaitForEventWithChannels_cfunc = None
        self.niDCPower_close_cfunc = None
        self.niDCPower_error_message_cfunc = None
        self.niDCPower_self_test_cfunc = None

    def _get_library_function(self, name):
        try:
            function = getattr(self._library, name)
        except AttributeError as e:
            raise errors.DriverTooOldError() from e
        return function

    def niDCPower_AbortWithChannels(self, vi, channel_name):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_AbortWithChannels_cfunc is None:
                self.niDCPower_AbortWithChannels_cfunc = self._get_library_function('niDCPower_AbortWithChannels')
                self.niDCPower_AbortWithChannels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_AbortWithChannels_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_AbortWithChannels_cfunc(vi, channel_name)

    def niDCPower_CalSelfCalibrate(self, vi, channel_name):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_CalSelfCalibrate_cfunc is None:
                self.niDCPower_CalSelfCalibrate_cfunc = self._get_library_function('niDCPower_CalSelfCalibrate')
                self.niDCPower_CalSelfCalibrate_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_CalSelfCalibrate_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_CalSelfCalibrate_cfunc(vi, channel_name)

    def niDCPower_ClearLatchedOutputCutoffState(self, vi, channel_name, output_cutoff_reason):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ClearLatchedOutputCutoffState_cfunc is None:
                self.niDCPower_ClearLatchedOutputCutoffState_cfunc = self._get_library_function('niDCPower_ClearLatchedOutputCutoffState')
                self.niDCPower_ClearLatchedOutputCutoffState_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niDCPower_ClearLatchedOutputCutoffState_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_ClearLatchedOutputCutoffState_cfunc(vi, channel_name, output_cutoff_reason)

    def niDCPower_CommitWithChannels(self, vi, channel_name):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_CommitWithChannels_cfunc is None:
                self.niDCPower_CommitWithChannels_cfunc = self._get_library_function('niDCPower_CommitWithChannels')
                self.niDCPower_CommitWithChannels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_CommitWithChannels_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_CommitWithChannels_cfunc(vi, channel_name)

    def niDCPower_ConfigureApertureTime(self, vi, channel_name, aperture_time, units):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigureApertureTime_cfunc is None:
                self.niDCPower_ConfigureApertureTime_cfunc = self._get_library_function('niDCPower_ConfigureApertureTime')
                self.niDCPower_ConfigureApertureTime_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32]  # noqa: F405
                self.niDCPower_ConfigureApertureTime_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_ConfigureApertureTime_cfunc(vi, channel_name, aperture_time, units)

    def niDCPower_ConfigureLCRCompensation(self, vi, channel_name, compensation_data_size, compensation_data):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigureLCRCompensation_cfunc is None:
                self.niDCPower_ConfigureLCRCompensation_cfunc = self._get_library_function('niDCPower_ConfigureLCRCompensation')
                self.niDCPower_ConfigureLCRCompensation_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niDCPower_ConfigureLCRCompensation_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_ConfigureLCRCompensation_cfunc(vi, channel_name, compensation_data_size, compensation_data)

    def niDCPower_ConfigureLCRCustomCableCompensation(self, vi, channel_name, custom_cable_compensation_data_size, custom_cable_compensation_data):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigureLCRCustomCableCompensation_cfunc is None:
                self.niDCPower_ConfigureLCRCustomCableCompensation_cfunc = self._get_library_function('niDCPower_ConfigureLCRCustomCableCompensation')
                self.niDCPower_ConfigureLCRCustomCableCompensation_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niDCPower_ConfigureLCRCustomCableCompensation_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_ConfigureLCRCustomCableCompensation_cfunc(vi, channel_name, custom_cable_compensation_data_size, custom_cable_compensation_data)

    def niDCPower_CreateAdvancedSequenceCommitStepWithChannels(self, vi, channel_name, set_as_active_step):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_CreateAdvancedSequenceCommitStepWithChannels_cfunc is None:
                self.niDCPower_CreateAdvancedSequenceCommitStepWithChannels_cfunc = self._get_library_function('niDCPower_CreateAdvancedSequenceCommitStepWithChannels')
                self.niDCPower_CreateAdvancedSequenceCommitStepWithChannels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViBoolean]  # noqa: F405
                self.niDCPower_CreateAdvancedSequenceCommitStepWithChannels_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_CreateAdvancedSequenceCommitStepWithChannels_cfunc(vi, channel_name, set_as_active_step)

    def niDCPower_CreateAdvancedSequenceStepWithChannels(self, vi, channel_name, set_as_active_step):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_CreateAdvancedSequenceStepWithChannels_cfunc is None:
                self.niDCPower_CreateAdvancedSequenceStepWithChannels_cfunc = self._get_library_function('niDCPower_CreateAdvancedSequenceStepWithChannels')
                self.niDCPower_CreateAdvancedSequenceStepWithChannels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViBoolean]  # noqa: F405
                self.niDCPower_CreateAdvancedSequenceStepWithChannels_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_CreateAdvancedSequenceStepWithChannels_cfunc(vi, channel_name, set_as_active_step)

    def niDCPower_CreateAdvancedSequenceWithChannels(self, vi, channel_name, sequence_name, attribute_id_count, attribute_ids, set_as_active_sequence):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_CreateAdvancedSequenceWithChannels_cfunc is None:
                self.niDCPower_CreateAdvancedSequenceWithChannels_cfunc = self._get_library_function('niDCPower_CreateAdvancedSequenceWithChannels')
                self.niDCPower_CreateAdvancedSequenceWithChannels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt32), ViBoolean]  # noqa: F405
                self.niDCPower_CreateAdvancedSequenceWithChannels_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_CreateAdvancedSequenceWithChannels_cfunc(vi, channel_name, sequence_name, attribute_id_count, attribute_ids, set_as_active_sequence)

    def niDCPower_DeleteAdvancedSequenceWithChannels(self, vi, channel_name, sequence_name):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_DeleteAdvancedSequenceWithChannels_cfunc is None:
                self.niDCPower_DeleteAdvancedSequenceWithChannels_cfunc = self._get_library_function('niDCPower_DeleteAdvancedSequenceWithChannels')
                self.niDCPower_DeleteAdvancedSequenceWithChannels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_DeleteAdvancedSequenceWithChannels_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_DeleteAdvancedSequenceWithChannels_cfunc(vi, channel_name, sequence_name)

    def niDCPower_Disable(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_Disable_cfunc is None:
                self.niDCPower_Disable_cfunc = self._get_library_function('niDCPower_Disable')
                self.niDCPower_Disable_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDCPower_Disable_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_Disable_cfunc(vi)

    def niDCPower_ExportAttributeConfigurationBuffer(self, vi, size, configuration):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ExportAttributeConfigurationBuffer_cfunc is None:
                self.niDCPower_ExportAttributeConfigurationBuffer_cfunc = self._get_library_function('niDCPower_ExportAttributeConfigurationBuffer')
                self.niDCPower_ExportAttributeConfigurationBuffer_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niDCPower_ExportAttributeConfigurationBuffer_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_ExportAttributeConfigurationBuffer_cfunc(vi, size, configuration)

    def niDCPower_ExportAttributeConfigurationFile(self, vi, file_path):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ExportAttributeConfigurationFile_cfunc is None:
                self.niDCPower_ExportAttributeConfigurationFile_cfunc = self._get_library_function('niDCPower_ExportAttributeConfigurationFile')
                self.niDCPower_ExportAttributeConfigurationFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_ExportAttributeConfigurationFile_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_ExportAttributeConfigurationFile_cfunc(vi, file_path)

    def niDCPower_FancyInitialize(self, resource_name, channels, reset, option_string, vi, independent_channels):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_FancyInitialize_cfunc is None:
                self.niDCPower_FancyInitialize_cfunc = self._get_library_function('niDCPower_FancyInitialize')
                self.niDCPower_FancyInitialize_cfunc.argtypes = [ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViBoolean, ctypes.POINTER(ViChar), ctypes.POINTER(ViSession), ViBoolean]  # noqa: F405
                self.niDCPower_FancyInitialize_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_FancyInitialize_cfunc(resource_name, channels, reset, option_string, vi, independent_channels)

    def niDCPower_FetchMultiple(self, vi, channel_name, timeout, count, voltage_measurements, current_measurements, in_compliance, actual_count):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_FetchMultiple_cfunc is None:
                self.niDCPower_FetchMultiple_cfunc = self._get_library_function('niDCPower_FetchMultiple')
                self.niDCPower_FetchMultiple_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViBoolean), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDCPower_FetchMultiple_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_FetchMultiple_cfunc(vi, channel_name, timeout, count, voltage_measurements, current_measurements, in_compliance, actual_count)

    def niDCPower_FetchMultipleLCR(self, vi, channel_name, timeout, count, measurements, actual_count):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_FetchMultipleLCR_cfunc is None:
                self.niDCPower_FetchMultipleLCR_cfunc = self._get_library_function('niDCPower_FetchMultipleLCR')
                self.niDCPower_FetchMultipleLCR_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ctypes.POINTER(lcr_measurement.struct_NILCRMeasurement), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDCPower_FetchMultipleLCR_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_FetchMultipleLCR_cfunc(vi, channel_name, timeout, count, measurements, actual_count)

    def niDCPower_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetAttributeViBoolean_cfunc is None:
                self.niDCPower_GetAttributeViBoolean_cfunc = self._get_library_function('niDCPower_GetAttributeViBoolean')
                self.niDCPower_GetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDCPower_GetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_GetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDCPower_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetAttributeViInt32_cfunc is None:
                self.niDCPower_GetAttributeViInt32_cfunc = self._get_library_function('niDCPower_GetAttributeViInt32')
                self.niDCPower_GetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDCPower_GetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_GetAttributeViInt32_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDCPower_GetAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetAttributeViInt64_cfunc is None:
                self.niDCPower_GetAttributeViInt64_cfunc = self._get_library_function('niDCPower_GetAttributeViInt64')
                self.niDCPower_GetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt64)]  # noqa: F405
                self.niDCPower_GetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_GetAttributeViInt64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDCPower_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetAttributeViReal64_cfunc is None:
                self.niDCPower_GetAttributeViReal64_cfunc = self._get_library_function('niDCPower_GetAttributeViReal64')
                self.niDCPower_GetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDCPower_GetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_GetAttributeViReal64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDCPower_GetAttributeViString(self, vi, channel_name, attribute_id, buffer_size, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetAttributeViString_cfunc is None:
                self.niDCPower_GetAttributeViString_cfunc = self._get_library_function('niDCPower_GetAttributeViString')
                self.niDCPower_GetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_GetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_GetAttributeViString_cfunc(vi, channel_name, attribute_id, buffer_size, attribute_value)

    def niDCPower_GetChannelName(self, vi, index, buffer_size, channel_name):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetChannelName_cfunc is None:
                self.niDCPower_GetChannelName_cfunc = self._get_library_function('niDCPower_GetChannelName')
                self.niDCPower_GetChannelName_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_GetChannelName_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_GetChannelName_cfunc(vi, index, buffer_size, channel_name)

    def niDCPower_GetChannelNameFromString(self, vi, indices, buffer_size, names):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetChannelNameFromString_cfunc is None:
                self.niDCPower_GetChannelNameFromString_cfunc = self._get_library_function('niDCPower_GetChannelNameFromString')
                self.niDCPower_GetChannelNameFromString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_GetChannelNameFromString_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_GetChannelNameFromString_cfunc(vi, indices, buffer_size, names)

    def niDCPower_GetError(self, vi, code, buffer_size, description):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetError_cfunc is None:
                self.niDCPower_GetError_cfunc = self._get_library_function('niDCPower_GetError')
                self.niDCPower_GetError_cfunc.argtypes = [ViSession, ctypes.POINTER(ViStatus), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_GetError_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_GetError_cfunc(vi, code, buffer_size, description)

    def niDCPower_GetExtCalLastDateAndTime(self, vi, year, month, day, hour, minute):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetExtCalLastDateAndTime_cfunc is None:
                self.niDCPower_GetExtCalLastDateAndTime_cfunc = self._get_library_function('niDCPower_GetExtCalLastDateAndTime')
                self.niDCPower_GetExtCalLastDateAndTime_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDCPower_GetExtCalLastDateAndTime_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_GetExtCalLastDateAndTime_cfunc(vi, year, month, day, hour, minute)

    def niDCPower_GetExtCalLastTemp(self, vi, temperature):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetExtCalLastTemp_cfunc is None:
                self.niDCPower_GetExtCalLastTemp_cfunc = self._get_library_function('niDCPower_GetExtCalLastTemp')
                self.niDCPower_GetExtCalLastTemp_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDCPower_GetExtCalLastTemp_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_GetExtCalLastTemp_cfunc(vi, temperature)

    def niDCPower_GetExtCalRecommendedInterval(self, vi, months):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetExtCalRecommendedInterval_cfunc is None:
                self.niDCPower_GetExtCalRecommendedInterval_cfunc = self._get_library_function('niDCPower_GetExtCalRecommendedInterval')
                self.niDCPower_GetExtCalRecommendedInterval_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDCPower_GetExtCalRecommendedInterval_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_GetExtCalRecommendedInterval_cfunc(vi, months)

    def niDCPower_GetLCRCompensationData(self, vi, channel_name, compensation_data_size, compensation_data):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetLCRCompensationData_cfunc is None:
                self.niDCPower_GetLCRCompensationData_cfunc = self._get_library_function('niDCPower_GetLCRCompensationData')
                self.niDCPower_GetLCRCompensationData_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niDCPower_GetLCRCompensationData_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_GetLCRCompensationData_cfunc(vi, channel_name, compensation_data_size, compensation_data)

    def niDCPower_GetLCRCompensationLastDateAndTime(self, vi, channel_name, compensation_type, year, month, day, hour, minute):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetLCRCompensationLastDateAndTime_cfunc is None:
                self.niDCPower_GetLCRCompensationLastDateAndTime_cfunc = self._get_library_function('niDCPower_GetLCRCompensationLastDateAndTime')
                self.niDCPower_GetLCRCompensationLastDateAndTime_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDCPower_GetLCRCompensationLastDateAndTime_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_GetLCRCompensationLastDateAndTime_cfunc(vi, channel_name, compensation_type, year, month, day, hour, minute)

    def niDCPower_GetLCRCustomCableCompensationData(self, vi, channel_name, custom_cable_compensation_data_size, custom_cable_compensation_data):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetLCRCustomCableCompensationData_cfunc is None:
                self.niDCPower_GetLCRCustomCableCompensationData_cfunc = self._get_library_function('niDCPower_GetLCRCustomCableCompensationData')
                self.niDCPower_GetLCRCustomCableCompensationData_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niDCPower_GetLCRCustomCableCompensationData_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_GetLCRCustomCableCompensationData_cfunc(vi, channel_name, custom_cable_compensation_data_size, custom_cable_compensation_data)

    def niDCPower_GetSelfCalLastDateAndTime(self, vi, year, month, day, hour, minute):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetSelfCalLastDateAndTime_cfunc is None:
                self.niDCPower_GetSelfCalLastDateAndTime_cfunc = self._get_library_function('niDCPower_GetSelfCalLastDateAndTime')
                self.niDCPower_GetSelfCalLastDateAndTime_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDCPower_GetSelfCalLastDateAndTime_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_GetSelfCalLastDateAndTime_cfunc(vi, year, month, day, hour, minute)

    def niDCPower_GetSelfCalLastTemp(self, vi, temperature):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetSelfCalLastTemp_cfunc is None:
                self.niDCPower_GetSelfCalLastTemp_cfunc = self._get_library_function('niDCPower_GetSelfCalLastTemp')
                self.niDCPower_GetSelfCalLastTemp_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDCPower_GetSelfCalLastTemp_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_GetSelfCalLastTemp_cfunc(vi, temperature)

    def niDCPower_ImportAttributeConfigurationBuffer(self, vi, size, configuration):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ImportAttributeConfigurationBuffer_cfunc is None:
                self.niDCPower_ImportAttributeConfigurationBuffer_cfunc = self._get_library_function('niDCPower_ImportAttributeConfigurationBuffer')
                self.niDCPower_ImportAttributeConfigurationBuffer_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niDCPower_ImportAttributeConfigurationBuffer_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_ImportAttributeConfigurationBuffer_cfunc(vi, size, configuration)

    def niDCPower_ImportAttributeConfigurationFile(self, vi, file_path):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ImportAttributeConfigurationFile_cfunc is None:
                self.niDCPower_ImportAttributeConfigurationFile_cfunc = self._get_library_function('niDCPower_ImportAttributeConfigurationFile')
                self.niDCPower_ImportAttributeConfigurationFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_ImportAttributeConfigurationFile_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_ImportAttributeConfigurationFile_cfunc(vi, file_path)

    def niDCPower_InitializeWithChannels(self, resource_name, channels, reset, option_string, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_InitializeWithChannels_cfunc is None:
                self.niDCPower_InitializeWithChannels_cfunc = self._get_library_function('niDCPower_InitializeWithChannels')
                self.niDCPower_InitializeWithChannels_cfunc.argtypes = [ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViBoolean, ctypes.POINTER(ViChar), ctypes.POINTER(ViSession)]  # noqa: F405
                self.niDCPower_InitializeWithChannels_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_InitializeWithChannels_cfunc(resource_name, channels, reset, option_string, vi)

    def niDCPower_InitializeWithIndependentChannels(self, resource_name, reset, option_string, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_InitializeWithIndependentChannels_cfunc is None:
                self.niDCPower_InitializeWithIndependentChannels_cfunc = self._get_library_function('niDCPower_InitializeWithIndependentChannels')
                self.niDCPower_InitializeWithIndependentChannels_cfunc.argtypes = [ctypes.POINTER(ViChar), ViBoolean, ctypes.POINTER(ViChar), ctypes.POINTER(ViSession)]  # noqa: F405
                self.niDCPower_InitializeWithIndependentChannels_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_InitializeWithIndependentChannels_cfunc(resource_name, reset, option_string, vi)

    def niDCPower_InitiateWithChannels(self, vi, channel_name):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_InitiateWithChannels_cfunc is None:
                self.niDCPower_InitiateWithChannels_cfunc = self._get_library_function('niDCPower_InitiateWithChannels')
                self.niDCPower_InitiateWithChannels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_InitiateWithChannels_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_InitiateWithChannels_cfunc(vi, channel_name)

    def niDCPower_LockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_LockSession_cfunc is None:
                self.niDCPower_LockSession_cfunc = self._get_library_function('niDCPower_LockSession')
                self.niDCPower_LockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDCPower_LockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_LockSession_cfunc(vi, caller_has_lock)

    def niDCPower_Measure(self, vi, channel_name, measurement_type, measurement):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_Measure_cfunc is None:
                self.niDCPower_Measure_cfunc = self._get_library_function('niDCPower_Measure')
                self.niDCPower_Measure_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDCPower_Measure_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_Measure_cfunc(vi, channel_name, measurement_type, measurement)

    def niDCPower_MeasureMultiple(self, vi, channel_name, voltage_measurements, current_measurements):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_MeasureMultiple_cfunc is None:
                self.niDCPower_MeasureMultiple_cfunc = self._get_library_function('niDCPower_MeasureMultiple')
                self.niDCPower_MeasureMultiple_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDCPower_MeasureMultiple_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_MeasureMultiple_cfunc(vi, channel_name, voltage_measurements, current_measurements)

    def niDCPower_MeasureMultipleLCR(self, vi, channel_name, measurements):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_MeasureMultipleLCR_cfunc is None:
                self.niDCPower_MeasureMultipleLCR_cfunc = self._get_library_function('niDCPower_MeasureMultipleLCR')
                self.niDCPower_MeasureMultipleLCR_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(lcr_measurement.struct_NILCRMeasurement)]  # noqa: F405
                self.niDCPower_MeasureMultipleLCR_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_MeasureMultipleLCR_cfunc(vi, channel_name, measurements)

    def niDCPower_ParseChannelCount(self, vi, channels_string, number_of_channels):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ParseChannelCount_cfunc is None:
                self.niDCPower_ParseChannelCount_cfunc = self._get_library_function('niDCPower_ParseChannelCount')
                self.niDCPower_ParseChannelCount_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViUInt32)]  # noqa: F405
                self.niDCPower_ParseChannelCount_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_ParseChannelCount_cfunc(vi, channels_string, number_of_channels)

    def niDCPower_PerformLCRLoadCompensation(self, vi, channel_name, num_compensation_spots, compensation_spots):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_PerformLCRLoadCompensation_cfunc is None:
                self.niDCPower_PerformLCRLoadCompensation_cfunc = self._get_library_function('niDCPower_PerformLCRLoadCompensation')
                self.niDCPower_PerformLCRLoadCompensation_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(lcr_load_compensation_spot.struct_NILCRLoadCompensationSpot)]  # noqa: F405
                self.niDCPower_PerformLCRLoadCompensation_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_PerformLCRLoadCompensation_cfunc(vi, channel_name, num_compensation_spots, compensation_spots)

    def niDCPower_PerformLCROpenCompensation(self, vi, channel_name, num_frequencies, additional_frequencies):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_PerformLCROpenCompensation_cfunc is None:
                self.niDCPower_PerformLCROpenCompensation_cfunc = self._get_library_function('niDCPower_PerformLCROpenCompensation')
                self.niDCPower_PerformLCROpenCompensation_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDCPower_PerformLCROpenCompensation_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_PerformLCROpenCompensation_cfunc(vi, channel_name, num_frequencies, additional_frequencies)

    def niDCPower_PerformLCROpenCustomCableCompensation(self, vi, channel_name):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_PerformLCROpenCustomCableCompensation_cfunc is None:
                self.niDCPower_PerformLCROpenCustomCableCompensation_cfunc = self._get_library_function('niDCPower_PerformLCROpenCustomCableCompensation')
                self.niDCPower_PerformLCROpenCustomCableCompensation_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_PerformLCROpenCustomCableCompensation_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_PerformLCROpenCustomCableCompensation_cfunc(vi, channel_name)

    def niDCPower_PerformLCRShortCompensation(self, vi, channel_name, num_frequencies, additional_frequencies):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_PerformLCRShortCompensation_cfunc is None:
                self.niDCPower_PerformLCRShortCompensation_cfunc = self._get_library_function('niDCPower_PerformLCRShortCompensation')
                self.niDCPower_PerformLCRShortCompensation_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDCPower_PerformLCRShortCompensation_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_PerformLCRShortCompensation_cfunc(vi, channel_name, num_frequencies, additional_frequencies)

    def niDCPower_PerformLCRShortCustomCableCompensation(self, vi, channel_name):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_PerformLCRShortCustomCableCompensation_cfunc is None:
                self.niDCPower_PerformLCRShortCustomCableCompensation_cfunc = self._get_library_function('niDCPower_PerformLCRShortCustomCableCompensation')
                self.niDCPower_PerformLCRShortCustomCableCompensation_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_PerformLCRShortCustomCableCompensation_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_PerformLCRShortCustomCableCompensation_cfunc(vi, channel_name)

    def niDCPower_QueryInCompliance(self, vi, channel_name, in_compliance):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_QueryInCompliance_cfunc is None:
                self.niDCPower_QueryInCompliance_cfunc = self._get_library_function('niDCPower_QueryInCompliance')
                self.niDCPower_QueryInCompliance_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDCPower_QueryInCompliance_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_QueryInCompliance_cfunc(vi, channel_name, in_compliance)

    def niDCPower_QueryLatchedOutputCutoffState(self, vi, channel_name, output_cutoff_reason, output_cutoff_state):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_QueryLatchedOutputCutoffState_cfunc is None:
                self.niDCPower_QueryLatchedOutputCutoffState_cfunc = self._get_library_function('niDCPower_QueryLatchedOutputCutoffState')
                self.niDCPower_QueryLatchedOutputCutoffState_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDCPower_QueryLatchedOutputCutoffState_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_QueryLatchedOutputCutoffState_cfunc(vi, channel_name, output_cutoff_reason, output_cutoff_state)

    def niDCPower_QueryMaxCurrentLimit(self, vi, channel_name, voltage_level, max_current_limit):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_QueryMaxCurrentLimit_cfunc is None:
                self.niDCPower_QueryMaxCurrentLimit_cfunc = self._get_library_function('niDCPower_QueryMaxCurrentLimit')
                self.niDCPower_QueryMaxCurrentLimit_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDCPower_QueryMaxCurrentLimit_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_QueryMaxCurrentLimit_cfunc(vi, channel_name, voltage_level, max_current_limit)

    def niDCPower_QueryMaxVoltageLevel(self, vi, channel_name, current_limit, max_voltage_level):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_QueryMaxVoltageLevel_cfunc is None:
                self.niDCPower_QueryMaxVoltageLevel_cfunc = self._get_library_function('niDCPower_QueryMaxVoltageLevel')
                self.niDCPower_QueryMaxVoltageLevel_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDCPower_QueryMaxVoltageLevel_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_QueryMaxVoltageLevel_cfunc(vi, channel_name, current_limit, max_voltage_level)

    def niDCPower_QueryMinCurrentLimit(self, vi, channel_name, voltage_level, min_current_limit):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_QueryMinCurrentLimit_cfunc is None:
                self.niDCPower_QueryMinCurrentLimit_cfunc = self._get_library_function('niDCPower_QueryMinCurrentLimit')
                self.niDCPower_QueryMinCurrentLimit_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDCPower_QueryMinCurrentLimit_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_QueryMinCurrentLimit_cfunc(vi, channel_name, voltage_level, min_current_limit)

    def niDCPower_QueryOutputState(self, vi, channel_name, output_state, in_state):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_QueryOutputState_cfunc is None:
                self.niDCPower_QueryOutputState_cfunc = self._get_library_function('niDCPower_QueryOutputState')
                self.niDCPower_QueryOutputState_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDCPower_QueryOutputState_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_QueryOutputState_cfunc(vi, channel_name, output_state, in_state)

    def niDCPower_ReadCurrentTemperature(self, vi, temperature):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ReadCurrentTemperature_cfunc is None:
                self.niDCPower_ReadCurrentTemperature_cfunc = self._get_library_function('niDCPower_ReadCurrentTemperature')
                self.niDCPower_ReadCurrentTemperature_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDCPower_ReadCurrentTemperature_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_ReadCurrentTemperature_cfunc(vi, temperature)

    def niDCPower_ResetDevice(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ResetDevice_cfunc is None:
                self.niDCPower_ResetDevice_cfunc = self._get_library_function('niDCPower_ResetDevice')
                self.niDCPower_ResetDevice_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDCPower_ResetDevice_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_ResetDevice_cfunc(vi)

    def niDCPower_ResetWithChannels(self, vi, channel_name):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ResetWithChannels_cfunc is None:
                self.niDCPower_ResetWithChannels_cfunc = self._get_library_function('niDCPower_ResetWithChannels')
                self.niDCPower_ResetWithChannels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_ResetWithChannels_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_ResetWithChannels_cfunc(vi, channel_name)

    def niDCPower_ResetWithDefaults(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ResetWithDefaults_cfunc is None:
                self.niDCPower_ResetWithDefaults_cfunc = self._get_library_function('niDCPower_ResetWithDefaults')
                self.niDCPower_ResetWithDefaults_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDCPower_ResetWithDefaults_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_ResetWithDefaults_cfunc(vi)

    def niDCPower_SendSoftwareEdgeTriggerWithChannels(self, vi, channel_name, trigger):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_SendSoftwareEdgeTriggerWithChannels_cfunc is None:
                self.niDCPower_SendSoftwareEdgeTriggerWithChannels_cfunc = self._get_library_function('niDCPower_SendSoftwareEdgeTriggerWithChannels')
                self.niDCPower_SendSoftwareEdgeTriggerWithChannels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niDCPower_SendSoftwareEdgeTriggerWithChannels_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_SendSoftwareEdgeTriggerWithChannels_cfunc(vi, channel_name, trigger)

    def niDCPower_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_SetAttributeViBoolean_cfunc is None:
                self.niDCPower_SetAttributeViBoolean_cfunc = self._get_library_function('niDCPower_SetAttributeViBoolean')
                self.niDCPower_SetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViBoolean]  # noqa: F405
                self.niDCPower_SetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_SetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDCPower_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_SetAttributeViInt32_cfunc is None:
                self.niDCPower_SetAttributeViInt32_cfunc = self._get_library_function('niDCPower_SetAttributeViInt32')
                self.niDCPower_SetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32]  # noqa: F405
                self.niDCPower_SetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_SetAttributeViInt32_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDCPower_SetAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_SetAttributeViInt64_cfunc is None:
                self.niDCPower_SetAttributeViInt64_cfunc = self._get_library_function('niDCPower_SetAttributeViInt64')
                self.niDCPower_SetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt64]  # noqa: F405
                self.niDCPower_SetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_SetAttributeViInt64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDCPower_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_SetAttributeViReal64_cfunc is None:
                self.niDCPower_SetAttributeViReal64_cfunc = self._get_library_function('niDCPower_SetAttributeViReal64')
                self.niDCPower_SetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViReal64]  # noqa: F405
                self.niDCPower_SetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_SetAttributeViReal64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDCPower_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_SetAttributeViString_cfunc is None:
                self.niDCPower_SetAttributeViString_cfunc = self._get_library_function('niDCPower_SetAttributeViString')
                self.niDCPower_SetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_SetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_SetAttributeViString_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDCPower_SetRuntimeEnvironment(self, environment, environment_version, reserved1, reserved2):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_SetRuntimeEnvironment_cfunc is None:
                self.niDCPower_SetRuntimeEnvironment_cfunc = self._get_library_function('niDCPower_SetRuntimeEnvironment')
                self.niDCPower_SetRuntimeEnvironment_cfunc.argtypes = [ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_SetRuntimeEnvironment_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_SetRuntimeEnvironment_cfunc(environment, environment_version, reserved1, reserved2)

    def niDCPower_SetSequence(self, vi, channel_name, values, source_delays, size):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_SetSequence_cfunc is None:
                self.niDCPower_SetSequence_cfunc = self._get_library_function('niDCPower_SetSequence')
                self.niDCPower_SetSequence_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ViUInt32]  # noqa: F405
                self.niDCPower_SetSequence_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_SetSequence_cfunc(vi, channel_name, values, source_delays, size)

    def niDCPower_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_UnlockSession_cfunc is None:
                self.niDCPower_UnlockSession_cfunc = self._get_library_function('niDCPower_UnlockSession')
                self.niDCPower_UnlockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDCPower_UnlockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_UnlockSession_cfunc(vi, caller_has_lock)

    def niDCPower_WaitForEventWithChannels(self, vi, channel_name, event_id, timeout):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_WaitForEventWithChannels_cfunc is None:
                self.niDCPower_WaitForEventWithChannels_cfunc = self._get_library_function('niDCPower_WaitForEventWithChannels')
                self.niDCPower_WaitForEventWithChannels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViReal64]  # noqa: F405
                self.niDCPower_WaitForEventWithChannels_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_WaitForEventWithChannels_cfunc(vi, channel_name, event_id, timeout)

    def niDCPower_close(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_close_cfunc is None:
                self.niDCPower_close_cfunc = self._get_library_function('niDCPower_close')
                self.niDCPower_close_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDCPower_close_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_close_cfunc(vi)

    def niDCPower_error_message(self, vi, error_code, error_message):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_error_message_cfunc is None:
                self.niDCPower_error_message_cfunc = self._get_library_function('niDCPower_error_message')
                self.niDCPower_error_message_cfunc.argtypes = [ViSession, ViStatus, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_error_message_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_error_message_cfunc(vi, error_code, error_message)

    def niDCPower_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_self_test_cfunc is None:
                self.niDCPower_self_test_cfunc = self._get_library_function('niDCPower_self_test')
                self.niDCPower_self_test_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_self_test_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_self_test_cfunc(vi, self_test_result, self_test_message)
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidcpower/nidcpower/_library_interpreter.py sha256=27f66ff5624b5b72bbba1162d283f0d6c5d78773dc379cb0343536512c18b6ff bytes=55753 -->
## FILE: generated/nidcpower/nidcpower/_library_interpreter.py

- repository: `ni/nimi-python`
- source_path: `generated/nidcpower/nidcpower/_library_interpreter.py`
- sha256: `27f66ff5624b5b72bbba1162d283f0d6c5d78773dc379cb0343536512c18b6ff`
- bytes: 55753

````python
# -*- coding: utf-8 -*-
# This file was generated

import array
import ctypes
import hightime  # noqa: F401
import platform

import nidcpower._library_singleton as _library_singleton
import nidcpower._visatype as _visatype
import nidcpower.enums as enums  # noqa: F401
import nidcpower.errors as errors

import nidcpower.lcr_measurement as lcr_measurement  # noqa: F401

import nidcpower.lcr_load_compensation_spot as lcr_load_compensation_spot  # noqa: F401


_was_runtime_environment_set = None


# Helper functions for creating ctypes needed for calling into the driver DLL
def _get_ctypes_pointer_for_buffer(value=None, library_type=None, size=None):
    if isinstance(value, array.array):
        assert library_type is not None, 'library_type is required for array.array'
        addr, _ = value.buffer_info()
        return ctypes.cast(addr, ctypes.POINTER(library_type))
    elif str(type(value)).find("'numpy.ndarray'") != -1:
        import numpy
        return numpy.ctypeslib.as_ctypes(value)
    elif isinstance(value, bytes):
        return ctypes.cast(value, ctypes.POINTER(library_type))
    elif isinstance(value, list):
        assert library_type is not None, 'library_type is required for list'
        return (library_type * len(value))(*value)
    else:
        if library_type is not None and size is not None:
            return (library_type * size)()
        else:
            return None


def _convert_to_array(value, array_type):
    if value is not None:
        if isinstance(value, array.array):
            value_array = value
        else:
            value_array = array.array(array_type, value)
    else:
        value_array = None

    return value_array


class LibraryInterpreter(object):
    '''Library C<->Python interpreter.

    This class is responsible for interpreting the Library's C API. It is responsible for:
    * Converting ctypes to native Python types.
    * Dealing with string encoding.
    * Allocating memory.
    * Converting errors returned by Library into Python exceptions.
    '''

    def __init__(self, encoding):
        self._encoding = encoding
        self._library = _library_singleton.get()
        global _was_runtime_environment_set
        if _was_runtime_environment_set is None:
            try:
                runtime_env = platform.python_implementation()
                version = platform.python_version()
                self.set_runtime_environment(
                    runtime_env,
                    version,
                    '',
                    ''
                )
            except errors.DriverTooOldError:
                pass
            finally:
                _was_runtime_environment_set = True
        # Initialize _vi to 0 for now.
        # Session will directly update it once the driver runtime init function has been called and
        # we have a valid session handle.
        self.set_session_handle()

    def set_session_handle(self, value=0):
        self._vi = value

    def get_session_handle(self):
        return self._vi

    def get_error_description(self, error_code):
        '''get_error_description

        Returns the error description.
        '''
        try:
            returned_error_code, error_string = self.get_error()
            if returned_error_code == error_code:
                return error_string
        except errors.Error:
            pass

        try:
            # get_error reads the session's error queue, which may have been overwritten,
            # causing it to return a mismatched error code. error_message takes the error
            # code directly as a parameter and looks up its description without reading the
            # queue, it will return the description for the specific error code.
            # Use error_message in current session before the handle reset in the next block.

            error_string = self.error_message(error_code)
            return error_string
        except errors.Error:
            pass

        save_vi = self.get_session_handle()
        try:
            # It is expected for get_error to raise when the session is invalid
            # (IVI spec requires GetError to fail).
            # Use error_message instead. It doesn't require a session.

            self.set_session_handle()
            error_string = self.error_message(error_code)
            return error_string
        except errors.Error:
            pass
        finally:
            self.set_session_handle(save_vi)
        return "Failed to retrieve error description."

    def abort(self, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        error_code = self._library.niDCPower_AbortWithChannels(vi_ctype, channel_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_cal(self, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        error_code = self._library.niDCPower_CalSelfCalibrate(vi_ctype, channel_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clear_latched_output_cutoff_state(self, channel_name, output_cutoff_reason):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        output_cutoff_reason_ctype = _visatype.ViInt32(output_cutoff_reason.value)  # case S130
        error_code = self._library.niDCPower_ClearLatchedOutputCutoffState(vi_ctype, channel_name_ctype, output_cutoff_reason_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def commit(self, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        error_code = self._library.niDCPower_CommitWithChannels(vi_ctype, channel_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_aperture_time(self, channel_name, aperture_time, units):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        aperture_time_ctype = _visatype.ViReal64(aperture_time)  # case S150
        units_ctype = _visatype.ViInt32(units.value)  # case S130
        error_code = self._library.niDCPower_ConfigureApertureTime(vi_ctype, channel_name_ctype, aperture_time_ctype, units_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_lcr_compensation(self, channel_name, compensation_data):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        compensation_data_size_ctype = _visatype.ViInt32(0 if compensation_data is None else len(compensation_data))  # case S160
        compensation_data_ctype = _get_ctypes_pointer_for_buffer(value=compensation_data, library_type=_visatype.ViInt8)  # case B550
        error_code = self._library.niDCPower_ConfigureLCRCompensation(vi_ctype, channel_name_ctype, compensation_data_size_ctype, compensation_data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_lcr_custom_cable_compensation(self, channel_name, custom_cable_compensation_data):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        custom_cable_compensation_data_size_ctype = _visatype.ViInt32(0 if custom_cable_compensation_data is None else len(custom_cable_compensation_data))  # case S160
        custom_cable_compensation_data_ctype = _get_ctypes_pointer_for_buffer(value=custom_cable_compensation_data, library_type=_visatype.ViInt8)  # case B550
        error_code = self._library.niDCPower_ConfigureLCRCustomCableCompensation(vi_ctype, channel_name_ctype, custom_cable_compensation_data_size_ctype, custom_cable_compensation_data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_advanced_sequence_commit_step(self, channel_name, set_as_active_step):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        set_as_active_step_ctype = _visatype.ViBoolean(set_as_active_step)  # case S150
        error_code = self._library.niDCPower_CreateAdvancedSequenceCommitStepWithChannels(vi_ctype, channel_name_ctype, set_as_active_step_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_advanced_sequence_step(self, channel_name, set_as_active_step):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        set_as_active_step_ctype = _visatype.ViBoolean(set_as_active_step)  # case S150
        error_code = self._library.niDCPower_CreateAdvancedSequenceStepWithChannels(vi_ctype, channel_name_ctype, set_as_active_step_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_advanced_sequence_with_channels(self, channel_name, sequence_name, attribute_ids, set_as_active_sequence):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        sequence_name_ctype = ctypes.create_string_buffer(sequence_name.encode(self._encoding))  # case C020
        attribute_id_count_ctype = _visatype.ViInt32(0 if attribute_ids is None else len(attribute_ids))  # case S160
        attribute_ids_ctype = _get_ctypes_pointer_for_buffer(value=attribute_ids, library_type=_visatype.ViInt32)  # case B550
        set_as_active_sequence_ctype = _visatype.ViBoolean(set_as_active_sequence)  # case S150
        error_code = self._library.niDCPower_CreateAdvancedSequenceWithChannels(vi_ctype, channel_name_ctype, sequence_name_ctype, attribute_id_count_ctype, attribute_ids_ctype, set_as_active_sequence_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def delete_advanced_sequence(self, channel_name, sequence_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        sequence_name_ctype = ctypes.create_string_buffer(sequence_name.encode(self._encoding))  # case C020
        error_code = self._library.niDCPower_DeleteAdvancedSequenceWithChannels(vi_ctype, channel_name_ctype, sequence_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDCPower_Disable(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def export_attribute_configuration_buffer(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        size_ctype = _visatype.ViInt32()  # case S170
        configuration_ctype = None  # case B580
        error_code = self._library.niDCPower_ExportAttributeConfigurationBuffer(vi_ctype, size_ctype, configuration_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        size_ctype = _visatype.ViInt32(error_code)  # case S180
        configuration_size = size_ctype.value  # case B590
        configuration_array = array.array("b", [0]) * configuration_size  # case B590
        configuration_ctype = _get_ctypes_pointer_for_buffer(value=configuration_array, library_type=_visatype.ViInt8)  # case B590
        error_code = self._library.niDCPower_ExportAttributeConfigurationBuffer(vi_ctype, size_ctype, configuration_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return configuration_array

    def export_attribute_configuration_file(self, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDCPower_ExportAttributeConfigurationFile(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def fancy_initialize(self, resource_name, channels, reset, option_string, independent_channels):  # noqa: N802
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case C020
        channels_ctype = ctypes.create_string_buffer(channels.encode(self._encoding))  # case C020
        reset_ctype = _visatype.ViBoolean(reset)  # case S150
        option_string_ctype = ctypes.create_string_buffer(option_string.encode(self._encoding))  # case C020
        vi_ctype = _visatype.ViSession()  # case S220
        independent_channels_ctype = _visatype.ViBoolean(independent_channels)  # case S150
        error_code = self._library.niDCPower_FancyInitialize(resource_name_ctype, channels_ctype, reset_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)), independent_channels_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(vi_ctype.value)

    def fetch_multiple(self, channel_name, timeout, count):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        count_ctype = _visatype.ViInt32(count)  # case S210
        voltage_measurements_size = count  # case B600
        voltage_measurements_array = array.array("d", [0]) * voltage_measurements_size  # case B600
        voltage_measurements_ctype = _get_ctypes_pointer_for_buffer(value=voltage_measurements_array, library_type=_visatype.ViReal64)  # case B600
        current_measurements_size = count  # case B600
        current_measurements_array = array.array("d", [0]) * current_measurements_size  # case B600
        current_measurements_ctype = _get_ctypes_pointer_for_buffer(value=current_measurements_array, library_type=_visatype.ViReal64)  # case B600
        in_compliance_size = count  # case B600
        in_compliance_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViBoolean, size=in_compliance_size)  # case B600
        actual_count_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDCPower_FetchMultiple(vi_ctype, channel_name_ctype, timeout_ctype, count_ctype, voltage_measurements_ctype, current_measurements_ctype, in_compliance_ctype, None if actual_count_ctype is None else (ctypes.pointer(actual_count_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return voltage_measurements_array, current_measurements_array, [bool(in_compliance_ctype[i]) for i in range(count_ctype.value)]

    def fetch_multiple_lcr(self, channel_name, timeout, count):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        count_ctype = _visatype.ViInt32(count)  # case S210
        measurements_size = count  # case B600
        measurements_ctype = _get_ctypes_pointer_for_buffer(library_type=lcr_measurement.struct_NILCRMeasurement, size=measurements_size)  # case B600
        actual_count_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDCPower_FetchMultipleLCR(vi_ctype, channel_name_ctype, timeout_ctype, count_ctype, measurements_ctype, None if actual_count_ctype is None else (ctypes.pointer(actual_count_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [lcr_measurement.LCRMeasurement(measurements_ctype[i]) for i in range(count_ctype.value)]

    def get_attribute_vi_boolean(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niDCPower_GetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(attribute_value_ctype.value)

    def get_attribute_vi_int32(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDCPower_GetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def get_attribute_vi_int64(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt64()  # case S220
        error_code = self._library.niDCPower_GetAttributeViInt64(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def get_attribute_vi_real64(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDCPower_GetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(attribute_value_ctype.value)

    def get_attribute_vi_string(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        attribute_value_ctype = None  # case C050
        error_code = self._library.niDCPower_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        attribute_value_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDCPower_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return attribute_value_ctype.value.decode(self._encoding)

    def get_channel_name(self, index):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        index_ctype = _visatype.ViInt32(index)  # case S150
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        channel_name_ctype = None  # case C050
        error_code = self._library.niDCPower_GetChannelName(vi_ctype, index_ctype, buffer_size_ctype, channel_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        channel_name_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDCPower_GetChannelName(vi_ctype, index_ctype, buffer_size_ctype, channel_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return channel_name_ctype.value.decode(self._encoding)

    def get_channel_names(self, indices):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        indices_ctype = ctypes.create_string_buffer(indices.encode(self._encoding))  # case C020
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        names_ctype = None  # case C050
        error_code = self._library.niDCPower_GetChannelNameFromString(vi_ctype, indices_ctype, buffer_size_ctype, names_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        names_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDCPower_GetChannelNameFromString(vi_ctype, indices_ctype, buffer_size_ctype, names_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return names_ctype.value.decode(self._encoding)

    def get_error(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        code_ctype = _visatype.ViStatus()  # case S220
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        description_ctype = None  # case C050
        error_code = self._library.niDCPower_GetError(vi_ctype, None if code_ctype is None else (ctypes.pointer(code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        description_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niDCPower_GetError(vi_ctype, None if code_ctype is None else (ctypes.pointer(code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return int(code_ctype.value), description_ctype.value.decode(self._encoding)

    def get_ext_cal_last_date_and_time(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        year_ctype = _visatype.ViInt32()  # case S220
        month_ctype = _visatype.ViInt32()  # case S220
        day_ctype = _visatype.ViInt32()  # case S220
        hour_ctype = _visatype.ViInt32()  # case S220
        minute_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDCPower_GetExtCalLastDateAndTime(vi_ctype, None if year_ctype is None else (ctypes.pointer(year_ctype)), None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(year_ctype.value), int(month_ctype.value), int(day_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    def get_ext_cal_last_temp(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        temperature_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDCPower_GetExtCalLastTemp(vi_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def get_ext_cal_recommended_interval(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        months_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDCPower_GetExtCalRecommendedInterval(vi_ctype, None if months_ctype is None else (ctypes.pointer(months_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(months_ctype.value)

    def get_lcr_compensation_data(self, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        compensation_data_size_ctype = _visatype.ViInt32()  # case S170
        compensation_data_ctype = None  # case B580
        error_code = self._library.niDCPower_GetLCRCompensationData(vi_ctype, channel_name_ctype, compensation_data_size_ctype, compensation_data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        compensation_data_size_ctype = _visatype.ViInt32(error_code)  # case S180
        compensation_data_size = compensation_data_size_ctype.value  # case B590
        compensation_data_array = array.array("b", [0]) * compensation_data_size  # case B590
        compensation_data_ctype = _get_ctypes_pointer_for_buffer(value=compensation_data_array, library_type=_visatype.ViInt8)  # case B590
        error_code = self._library.niDCPower_GetLCRCompensationData(vi_ctype, channel_name_ctype, compensation_data_size_ctype, compensation_data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return compensation_data_array

    def get_lcr_compensation_last_date_and_time(self, channel_name, compensation_type):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        compensation_type_ctype = _visatype.ViInt32(compensation_type.value)  # case S130
        year_ctype = _visatype.ViInt32()  # case S220
        month_ctype = _visatype.ViInt32()  # case S220
        day_ctype = _visatype.ViInt32()  # case S220
        hour_ctype = _visatype.ViInt32()  # case S220
        minute_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDCPower_GetLCRCompensationLastDateAndTime(vi_ctype, channel_name_ctype, compensation_type_ctype, None if year_ctype is None else (ctypes.pointer(year_ctype)), None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(year_ctype.value), int(month_ctype.value), int(day_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    def get_lcr_custom_cable_compensation_data(self, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        custom_cable_compensation_data_size_ctype = _visatype.ViInt32()  # case S170
        custom_cable_compensation_data_ctype = None  # case B580
        error_code = self._library.niDCPower_GetLCRCustomCableCompensationData(vi_ctype, channel_name_ctype, custom_cable_compensation_data_size_ctype, custom_cable_compensation_data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        custom_cable_compensation_data_size_ctype = _visatype.ViInt32(error_code)  # case S180
        custom_cable_compensation_data_size = custom_cable_compensation_data_size_ctype.value  # case B590
        custom_cable_compensation_data_array = array.array("b", [0]) * custom_cable_compensation_data_size  # case B590
        custom_cable_compensation_data_ctype = _get_ctypes_pointer_for_buffer(value=custom_cable_compensation_data_array, library_type=_visatype.ViInt8)  # case B590
        error_code = self._library.niDCPower_GetLCRCustomCableCompensationData(vi_ctype, channel_name_ctype, custom_cable_compensation_data_size_ctype, custom_cable_compensation_data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return custom_cable_compensation_data_array

    def get_self_cal_last_date_and_time(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        year_ctype = _visatype.ViInt32()  # case S220
        month_ctype = _visatype.ViInt32()  # case S220
        day_ctype = _visatype.ViInt32()  # case S220
        hour_ctype = _visatype.ViInt32()  # case S220
        minute_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niDCPower_GetSelfCalLastDateAndTime(vi_ctype, None if year_ctype is None else (ctypes.pointer(year_ctype)), None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(year_ctype.value), int(month_ctype.value), int(day_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    def get_self_cal_last_temp(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        temperature_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDCPower_GetSelfCalLastTemp(vi_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def import_attribute_configuration_buffer(self, configuration):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        size_ctype = _visatype.ViInt32(0 if configuration is None else len(configuration))  # case S160
        configuration_ctype = _get_ctypes_pointer_for_buffer(value=configuration, library_type=_visatype.ViInt8)  # case B550
        error_code = self._library.niDCPower_ImportAttributeConfigurationBuffer(vi_ctype, size_ctype, configuration_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def import_attribute_configuration_file(self, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niDCPower_ImportAttributeConfigurationFile(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def initialize_with_channels(self, resource_name, channels, reset, option_string):  # noqa: N802
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case C020
        channels_ctype = ctypes.create_string_buffer(channels.encode(self._encoding))  # case C020
        reset_ctype = _visatype.ViBoolean(reset)  # case S150
        option_string_ctype = ctypes.create_string_buffer(option_string.encode(self._encoding))  # case C020
        vi_ctype = _visatype.ViSession()  # case S220
        error_code = self._library.niDCPower_InitializeWithChannels(resource_name_ctype, channels_ctype, reset_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        self._close_on_exit = True
        return int(vi_ctype.value)

    def initialize_with_independent_channels(self, resource_name, reset, option_string):  # noqa: N802
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case C020
        reset_ctype = _visatype.ViBoolean(reset)  # case S150
        option_string_ctype = ctypes.create_string_buffer(option_string.encode(self._encoding))  # case C020
        vi_ctype = _visatype.ViSession()  # case S220
        error_code = self._library.niDCPower_InitializeWithIndependentChannels(resource_name_ctype, reset_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        self._close_on_exit = True
        return int(vi_ctype.value)

    def initiate_with_channels(self, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        error_code = self._library.niDCPower_InitiateWithChannels(vi_ctype, channel_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def lock(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDCPower_LockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def measure(self, channel_name, measurement_type):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        measurement_type_ctype = _visatype.ViInt32(measurement_type.value)  # case S130
        measurement_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDCPower_Measure(vi_ctype, channel_name_ctype, measurement_type_ctype, None if measurement_ctype is None else (ctypes.pointer(measurement_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(measurement_ctype.value)

    def measure_multiple(self, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        voltage_measurements_size = self.parse_channel_count(channel_name)  # case B560
        voltage_measurements_array = array.array("d", [0]) * voltage_measurements_size  # case B560
        voltage_measurements_ctype = _get_ctypes_pointer_for_buffer(value=voltage_measurements_array, library_type=_visatype.ViReal64)  # case B560
        current_measurements_size = self.parse_channel_count(channel_name)  # case B560
        current_measurements_array = array.array("d", [0]) * current_measurements_size  # case B560
        current_measurements_ctype = _get_ctypes_pointer_for_buffer(value=current_measurements_array, library_type=_visatype.ViReal64)  # case B560
        error_code = self._library.niDCPower_MeasureMultiple(vi_ctype, channel_name_ctype, voltage_measurements_ctype, current_measurements_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return voltage_measurements_array, current_measurements_array

    def measure_multiple_lcr(self, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        measurements_size = self.parse_channel_count(channel_name)  # case B560
        measurements_ctype = _get_ctypes_pointer_for_buffer(library_type=lcr_measurement.struct_NILCRMeasurement, size=measurements_size)  # case B560
        error_code = self._library.niDCPower_MeasureMultipleLCR(vi_ctype, channel_name_ctype, measurements_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [lcr_measurement.LCRMeasurement(measurements_ctype[i]) for i in range(self.parse_channel_count(channel_name))]

    def parse_channel_count(self, channels_string):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channels_string_ctype = ctypes.create_string_buffer(channels_string.encode(self._encoding))  # case C010
        number_of_channels_ctype = _visatype.ViUInt32()  # case S220
        error_code = self._library.niDCPower_ParseChannelCount(vi_ctype, channels_string_ctype, None if number_of_channels_ctype is None else (ctypes.pointer(number_of_channels_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(number_of_channels_ctype.value)

    def perform_lcr_load_compensation(self, channel_name, compensation_spots):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        num_compensation_spots_ctype = _visatype.ViInt32(0 if compensation_spots is None else len(compensation_spots))  # case S160
        compensation_spots_ctype = _get_ctypes_pointer_for_buffer([lcr_load_compensation_spot.struct_NILCRLoadCompensationSpot(c) for c in compensation_spots], library_type=lcr_load_compensation_spot.struct_NILCRLoadCompensationSpot)  # case B540
        error_code = self._library.niDCPower_PerformLCRLoadCompensation(vi_ctype, channel_name_ctype, num_compensation_spots_ctype, compensation_spots_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def perform_lcr_open_compensation(self, channel_name, additional_frequencies):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        num_frequencies_ctype = _visatype.ViInt32(0 if additional_frequencies is None else len(additional_frequencies))  # case S160
        additional_frequencies_ctype = _get_ctypes_pointer_for_buffer(value=additional_frequencies, library_type=_visatype.ViReal64)  # case B550
        error_code = self._library.niDCPower_PerformLCROpenCompensation(vi_ctype, channel_name_ctype, num_frequencies_ctype, additional_frequencies_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def perform_lcr_open_custom_cable_compensation(self, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        error_code = self._library.niDCPower_PerformLCROpenCustomCableCompensation(vi_ctype, channel_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def perform_lcr_short_compensation(self, channel_name, additional_frequencies):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        num_frequencies_ctype = _visatype.ViInt32(0 if additional_frequencies is None else len(additional_frequencies))  # case S160
        additional_frequencies_ctype = _get_ctypes_pointer_for_buffer(value=additional_frequencies, library_type=_visatype.ViReal64)  # case B550
        error_code = self._library.niDCPower_PerformLCRShortCompensation(vi_ctype, channel_name_ctype, num_frequencies_ctype, additional_frequencies_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def perform_lcr_short_custom_cable_compensation(self, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        error_code = self._library.niDCPower_PerformLCRShortCustomCableCompensation(vi_ctype, channel_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def query_in_compliance(self, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        in_compliance_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niDCPower_QueryInCompliance(vi_ctype, channel_name_ctype, None if in_compliance_ctype is None else (ctypes.pointer(in_compliance_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(in_compliance_ctype.value)

    def query_latched_output_cutoff_state(self, channel_name, output_cutoff_reason):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        output_cutoff_reason_ctype = _visatype.ViInt32(output_cutoff_reason.value)  # case S130
        output_cutoff_state_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niDCPower_QueryLatchedOutputCutoffState(vi_ctype, channel_name_ctype, output_cutoff_reason_ctype, None if output_cutoff_state_ctype is None else (ctypes.pointer(output_cutoff_state_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(output_cutoff_state_ctype.value)

    def query_max_current_limit(self, channel_name, voltage_level):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        voltage_level_ctype = _visatype.ViReal64(voltage_level)  # case S150
        max_current_limit_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDCPower_QueryMaxCurrentLimit(vi_ctype, channel_name_ctype, voltage_level_ctype, None if max_current_limit_ctype is None else (ctypes.pointer(max_current_limit_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(max_current_limit_ctype.value)

    def query_max_voltage_level(self, channel_name, current_limit):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        current_limit_ctype = _visatype.ViReal64(current_limit)  # case S150
        max_voltage_level_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDCPower_QueryMaxVoltageLevel(vi_ctype, channel_name_ctype, current_limit_ctype, None if max_voltage_level_ctype is None else (ctypes.pointer(max_voltage_level_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(max_voltage_level_ctype.value)

    def query_min_current_limit(self, channel_name, voltage_level):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        voltage_level_ctype = _visatype.ViReal64(voltage_level)  # case S150
        min_current_limit_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDCPower_QueryMinCurrentLimit(vi_ctype, channel_name_ctype, voltage_level_ctype, None if min_current_limit_ctype is None else (ctypes.pointer(min_current_limit_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(min_current_limit_ctype.value)

    def query_output_state(self, channel_name, output_state):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        output_state_ctype = _visatype.ViInt32(output_state.value)  # case S130
        in_state_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niDCPower_QueryOutputState(vi_ctype, channel_name_ctype, output_state_ctype, None if in_state_ctype is None else (ctypes.pointer(in_state_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(in_state_ctype.value)

    def read_current_temperature(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        temperature_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niDCPower_ReadCurrentTemperature(vi_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def reset_device(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDCPower_ResetDevice(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset(self, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        error_code = self._library.niDCPower_ResetWithChannels(vi_ctype, channel_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset_with_defaults(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDCPower_ResetWithDefaults(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def send_software_edge_trigger(self, channel_name, trigger):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        trigger_ctype = _visatype.ViInt32(trigger.value)  # case S130
        error_code = self._library.niDCPower_SendSoftwareEdgeTriggerWithChannels(vi_ctype, channel_name_ctype, trigger_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_boolean(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean(attribute_value)  # case S150
        error_code = self._library.niDCPower_SetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_int32(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32(attribute_value)  # case S150
        error_code = self._library.niDCPower_SetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_int64(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt64(attribute_value)  # case S150
        error_code = self._library.niDCPower_SetAttributeViInt64(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_real64(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64(attribute_value)  # case S150
        error_code = self._library.niDCPower_SetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_string(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = ctypes.create_string_buffer(attribute_value.encode(self._encoding))  # case C020
        error_code = self._library.niDCPower_SetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_runtime_environment(self, environment, environment_version, reserved1, reserved2):  # noqa: N802
        environment_ctype = ctypes.create_string_buffer(environment.encode(self._encoding))  # case C020
        environment_version_ctype = ctypes.create_string_buffer(environment_version.encode(self._encoding))  # case C020
        reserved1_ctype = ctypes.create_string_buffer(reserved1.encode(self._encoding))  # case C020
        reserved2_ctype = ctypes.create_string_buffer(reserved2.encode(self._encoding))  # case C020
        error_code = self._library.niDCPower_SetRuntimeEnvironment(environment_ctype, environment_version_ctype, reserved1_ctype, reserved2_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_sequence(self, channel_name, values, source_delays):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        values_ctype = _get_ctypes_pointer_for_buffer(value=values, library_type=_visatype.ViReal64)  # case B550
        source_delays_ctype = _get_ctypes_pointer_for_buffer(value=source_delays, library_type=_visatype.ViReal64)  # case B550
        size_ctype = _visatype.ViUInt32(0 if values is None else len(values))  # case S160
        error_code = self._library.niDCPower_SetSequence(vi_ctype, channel_name_ctype, values_ctype, source_delays_ctype, size_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def unlock(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDCPower_UnlockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def wait_for_event(self, channel_name, event_id, timeout):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        event_id_ctype = _visatype.ViInt32(event_id.value)  # case S130
        timeout_ctype = _visatype.ViReal64(timeout)  # case S150
        error_code = self._library.niDCPower_WaitForEventWithChannels(vi_ctype, channel_name_ctype, event_id_ctype, timeout_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def close(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niDCPower_close(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def error_message(self, error_code):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus(error_code)  # case S150
        error_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niDCPower_error_message(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(self._encoding)

    def self_test(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        self_test_result_ctype = _visatype.ViInt16()  # case S220
        self_test_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niDCPower_self_test(vi_ctype, None if self_test_result_ctype is None else (ctypes.pointer(self_test_result_ctype)), self_test_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(self_test_result_ctype.value), self_test_message_ctype.value.decode(self._encoding)
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidcpower/nidcpower/_library_singleton.py sha256=39e59a644416d821c4742cdad8ef5343110c88c1386329f20c621751c2a9e286 bytes=1711 -->
## FILE: generated/nidcpower/nidcpower/_library_singleton.py

- repository: `ni/nimi-python`
- source_path: `generated/nidcpower/nidcpower/_library_singleton.py`
- sha256: `39e59a644416d821c4742cdad8ef5343110c88c1386329f20c621751c2a9e286`
- bytes: 1711

````python
# -*- coding: utf-8 -*-
# This file was generated

import platform

import ctypes
import ctypes.util
import nidcpower._library as _library
import nidcpower.errors as errors
import threading


_instance = None
_instance_lock = threading.Lock()
_library_info = {'Linux': {'64bit': {'name': 'nidcpower', 'type': 'cdll'}},
                 'Windows': {'32bit': {'name': 'nidcpower_32.dll', 'type': 'windll'},
                             '64bit': {'name': 'nidcpower_64.dll', 'type': 'cdll'}}}


def _get_library_name():
    try:
        lib_name = ctypes.util.find_library(_library_info[platform.system()][platform.architecture()[0]]['name'])  # We find and return full path to the DLL
        if lib_name is None:
            raise errors.DriverNotInstalledError()
        return lib_name
    except KeyError:
        raise errors.UnsupportedConfigurationError


def _get_library_type():
    try:
        return _library_info[platform.system()][platform.architecture()[0]]['type']
    except KeyError:
        raise errors.UnsupportedConfigurationError


def get():
    '''get

    Returns the library.Library singleton for nidcpower.
    '''
    global _instance

    with _instance_lock:
        if _instance is None:
            try:
                library_type = _get_library_type()
                if library_type == 'windll':
                    ctypes_library = ctypes.WinDLL(_get_library_name())
                else:
                    assert library_type == 'cdll'
                    ctypes_library = ctypes.CDLL(_get_library_name())
            except OSError:
                raise errors.DriverNotInstalledError()
            _instance = _library.Library(ctypes_library)
        return _instance
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidcpower/nidcpower/_visatype.py sha256=ac436ae1613f5e807cd16d2df951c7a502f37996234e4d324c5412b3633e1c92 bytes=662 -->
## FILE: generated/nidcpower/nidcpower/_visatype.py

- repository: `ni/nimi-python`
- source_path: `generated/nidcpower/nidcpower/_visatype.py`
- sha256: `ac436ae1613f5e807cd16d2df951c7a502f37996234e4d324c5412b3633e1c92`
- bytes: 662

````python
import ctypes


'''Definitions of the VISA types used by the C API of the driver runtime.
These are aliased directly to ctypes types so can be used directly to call into the library.
'''


ViChar = ctypes.c_char
ViInt8 = ctypes.c_int8
ViUInt8 = ctypes.c_uint8
ViInt16 = ctypes.c_int16
ViUInt16 = ctypes.c_uint16
ViInt32 = ctypes.c_int32
ViUInt32 = ctypes.c_uint32
ViInt64 = ctypes.c_int64
ViUInt64 = ctypes.c_uint64
ViString = ctypes.c_char_p
ViReal32 = ctypes.c_float
ViReal64 = ctypes.c_double

# Types that are based on other visatypes
ViBoolean = ViUInt16
ViStatus = ViInt32
ViSession = ViUInt32
ViAttr = ViUInt32
ViConstString = ViString
ViRsrc = ViString
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidcpower/nidcpower/enums.py sha256=10d3fef3b381825a4e396e28b415048402aa5e63f155cbd63354107d772c8b54 bytes=19371 -->
## FILE: generated/nidcpower/nidcpower/enums.py

- repository: `ni/nimi-python`
- source_path: `generated/nidcpower/nidcpower/enums.py`
- sha256: `10d3fef3b381825a4e396e28b415048402aa5e63f155cbd63354107d772c8b54`
- bytes: 19371

````python
# -*- coding: utf-8 -*-
# This file was generated

from enum import Enum


class ApertureTimeAutoMode(Enum):
    OFF = 1135
    r'''
    Disables automatic aperture time scaling. The aperture_time property specifies the aperture time for all ranges.
    '''
    SHORT = 1136
    r'''
    Prioritizes measurement speed over measurement accuracy by quickly scaling down aperture time in larger current ranges. The aperture_time property specifies the aperture time for the minimum range.
    '''
    NORMAL = 1137
    r'''
    Balances measurement accuracy and speed by scaling down aperture time in larger current ranges. The aperture_time property specifies the aperture time for the minimum range.
    '''
    LONG = 1138
    r'''
    Prioritizes accuracy while still decreasing measurement time by slowly scaling down aperture time in larger current ranges. The aperture_time property specifies the aperture time for the minimum range.
    '''


class ApertureTimeUnits(Enum):
    SECONDS = 1028
    r'''
    Specifies aperture time in seconds.
    '''
    POWER_LINE_CYCLES = 1029
    r'''
    Specifies aperture time in power line cycles (PLCs).
    '''


class AutoZero(Enum):
    OFF = 0
    r'''
    Disables auto zero.
    '''
    ONCE = 1024
    r'''
    Makes zero conversions following the first measurement after initiating the device.  The device uses these zero conversions for the preceding measurement and future measurements until the device is reinitiated.
    '''
    ON = 1
    r'''
    Makes zero conversions for every measurement.
    '''


class AutorangeApertureTimeMode(Enum):
    AUTO = 1110
    r'''
    NI-DCPower optimizes the aperture time for the autorange algorithm based on the module range.
    '''
    CUSTOM = 1111
    r'''
    The user specifies a minimum aperture time for the algorithm using the autorange_minimum_aperture_time property and the corresponding autorange_minimum_aperture_time_units property.
    '''


class AutorangeBehavior(Enum):
    UP_TO_LIMIT_THEN_DOWN = 1107
    r'''
    Go to limit range then range down as needed until measured value is within thresholds.
    '''
    UP = 1108
    r'''
    go up one range when the upper threshold is reached.
    '''
    UP_AND_DOWN = 1109
    r'''
    go up or down one range when the upper/lower threshold is reached.
    '''


class AutorangeThresholdMode(Enum):
    NORMAL = 1112
    r'''
    Thresholds are selected based on a balance between accuracy and hysteresis.
    '''
    FAST_STEP = 1113
    r'''
    Optimized for faster changes in the measured signal. Thresholds are configured to be a smaller percentage of the range.
    '''
    HIGH_HYSTERESIS = 1114
    r'''
    Optimized for noisy signals to minimize frequent and unpredictable range changes. Thresholds are configured to be a larger percentage of the range.
    '''
    MEDIUM_HYSTERESIS = 1115
    r'''
    Optimized for noisy signals to minimize frequent and unpredictable range changes. Thresholds are configured to be a medium percentage of the range.
    '''
    HOLD = 1116
    r'''
    Attempt to maintain the active range. Thresholds will favor the active range.
    '''


class CableLength(Enum):
    ZERO_M = 1121
    r'''
    Uses predefined cable compensation data for a 0m cable (direct connection).
    '''
    NI_STANDARD_0_5M = 1153
    r'''
    Uses predefined cable compensation data for an NI standard 0.5m coaxial cable.
    '''
    NI_STANDARD_1M = 1122
    r'''
    Uses predefined cable compensation data for an NI standard 1m coaxial cable.
    '''
    NI_STANDARD_2M = 1123
    r'''
    Uses predefined cable compensation data for an NI standard 2m coaxial cable.
    '''
    NI_STANDARD_4M = 1124
    r'''
    Uses predefined cable compensation data for an NI standard 4m coaxial cable.
    '''
    NI_STANDARD_TRIAXIAL_1M = 1139
    r'''
    Uses predefined cable compensation data for an NI standard 1m triaxial cable.
    '''
    NI_STANDARD_TRIAXIAL_2M = 1140
    r'''
    Uses predefined cable compensation data for an NI standard 2m triaxial cable.
    '''
    NI_STANDARD_TRIAXIAL_4M = 1141
    r'''
    Uses predefined cable compensation data for an NI standard 4m triaxial cable.
    '''
    CUSTOM_ONBOARD_STORAGE = 1125
    r'''
    Uses previously generated custom cable compensation data from onboard storage. Only the most recently performed compensation data for each custom cable compensation type (open, short) is stored.
    '''
    CUSTOM_AS_CONFIGURED = 1126
    r'''
    Uses the custom cable compensation data supplied to configure_lcr_custom_cable_compensation. Use this option to manage multiple sets of custom cable compensation data.
    '''


class ComplianceLimitSymmetry(Enum):
    SYMMETRIC = 0
    r'''
    Compliance limits are specified symmetrically about 0.
    '''
    ASYMMETRIC = 1
    r'''
    Compliance limits can be specified asymmetrically with respect to 0.
    '''


class ConductionVoltageMode(Enum):
    AUTOMATIC = 1155
    r'''
    The conduction voltage feature is only enabled when you set the output_function property to OutputFunction.DC_CURRENT or OutputFunction.CONSTANT_POWER.
    '''
    ENABLED = 1156
    r'''
    The conduction voltage feature is enabled.
    '''
    DISABLED = 1157
    r'''
    The conduction voltage feature is disabled.
    '''


class CurrentLimitBehavior(Enum):
    REGULATE = 0
    r'''
    The channel acts to restrict the output current to the value of the Current Limit property when the actual output on the channel reaches or exceeds that value.
    '''
    TRIP = 1
    r'''
    The channel disables the output when the actual output current on the channel reaches or exceeds the value of the Current Limit property.
    '''


class DCNoiseRejection(Enum):
    SECOND_ORDER = 1043
    r'''
    Second-order rejection of DC noise.
    '''
    NORMAL = 1044
    r'''
    Normal rejection of DC noise.
    '''


class Event(Enum):
    SOURCE_COMPLETE = 1030
    r'''
    Specifies the Source Complete event.
    '''
    MEASURE_COMPLETE = 1031
    r'''
    Specifies the Measure Complete event.
    '''
    SEQUENCE_ITERATION_COMPLETE = 1032
    r'''
    Specifies the Sequence Iteration Complete event.
    '''
    SEQUENCE_ENGINE_DONE = 1033
    r'''
    Specifies the Sequence Engine Done event.
    '''
    PULSE_COMPLETE = 1051
    r'''
    Specifies the Pulse Complete event.
    '''
    READY_FOR_PULSE_TRIGGER = 1052
    r'''
    Specifies the Ready for Pulse Trigger event.
    '''


class EventOutputBehavior(Enum):
    PULSE = 1147
    r'''
    Output generates a pulse when the event is triggered.
    '''
    TOGGLE = 1148
    r'''
    Output toggles state when the event is triggered.
    '''


class EventToggleInitialState(Enum):
    LOW = 1149
    r'''
    The initial state is low.
    '''
    HIGH = 1150
    r'''
    The initial state is high.
    '''


class InstrumentMode(Enum):
    SMU_PS = 1061
    r'''
    The channel operates as an SMU/power supply.
    '''
    LCR = 1062
    r'''
    The channel operates as an LCR meter.
    '''
    E_LOAD = 1154
    r'''
    The channel operates as an electronic load (E-Load).
    '''


class _IsolationState(Enum):
    ISOLATED = 1128
    r'''
    The channel is disconnected from chassis ground.
    '''
    NON_ISOLATED = 1129
    r'''
    The channel is connected to chassis ground.
    '''


class LCRCompensationType(Enum):
    OPEN = 1130
    r'''
    Open LCR compensation.
    '''
    SHORT = 1131
    r'''
    Short LCR compensation.
    '''
    LOAD = 1132
    r'''
    Load LCR compensation.
    '''
    OPEN_CUSTOM_CABLE = 1133
    r'''
    Open custom cable compensation.
    '''
    SHORT_CUSTOM_CABLE = 1134
    r'''
    Short custom cable compensation.
    '''


class LCRDCBiasSource(Enum):
    OFF = 1065
    r'''
    Disables DC bias in LCR mode.
    '''
    VOLTAGE = 1066
    r'''
    Applies a constant voltage bias, as defined by the lcr_dc_bias_voltage_level property.
    '''
    CURRENT = 1067
    r'''
    Applies a constant current bias, as defined by the lcr_dc_bias_current_level property.
    '''


class LCRDCBiasTransientResponse(Enum):
    NORMAL = 1151
    r'''
    NI-DCPower automatically applies transient response values for DC bias.
    '''
    CUSTOM = 1152
    r'''
    NI-DCPower applies the transient response that you set manually with transient_response for DC bias. Search ni.com for information on configuring transient response.
    '''


class _LCRImpedanceAutoRange(Enum):
    OFF = 1068
    ON = 1070


class LCRImpedanceRangeSource(Enum):
    IMPEDANCE_RANGE = 1142
    r'''
    Uses the impedance range you specify with the lcr_impedance_range property.
    '''
    LOAD_CONFIGURATION = 1143
    r'''
    Computes the impedance range to select based on the values you supply to the lcr_load_resistance, lcr_load_inductance, and lcr_load_capacitance properties. NI-DCPower uses a series model of load resistance, load inductance, and load capacitance to compute the impedance range.
    '''


class LCRMeasurementTime(Enum):
    SHORT = 1071
    r'''
    Uses a short aperture time for LCR measurements.
    '''
    MEDIUM = 1072
    r'''
    Uses a medium aperture time for LCR measurements.
    '''
    LONG = 1073
    r'''
    Uses a long aperture time for LCR measurements.
    '''
    CUSTOM = 1117
    r'''
    Uses a custom aperture time for LCR measurements as specified by the lcr_custom_measurement_time property.
    '''


class LCROpenShortLoadCompensationDataSource(Enum):
    ONBOARD_STORAGE = 1074
    r'''
    Uses previously generated LCR compensation data. Only the most recently performed compensation data for each LCR compensation type (open, short, and load) is stored.
    '''
    AS_DEFINED = 1075
    r'''
    Uses the LCR compensation data represented by the relevant LCR compensation properties as generated by perform_lcr_open_compensation, perform_lcr_short_compensation, and perform_lcr_load_compensation. Use this option to manage multiple sets of LCR compensation data. This option applies compensation data from the following properties: lcr_open_conductance, lcr_open_susceptance, lcr_short_resistance, lcr_short_reactance, lcr_measured_load_resistance, lcr_measured_load_reactance, lcr_actual_load_resistance, lcr_actual_load_reactance.
    '''
    AS_CONFIGURED = 1146
    r'''
    Uses the LCR compensation data supplied to configure_lcr_compensation. Use this option to manage multiple sets of LCR compensation data.
    '''


class LCRReferenceValueType(Enum):
    IMPEDANCE = 1076
    r'''
    The actual impedance, comprising real resistance and imaginary reactance, of your DUT. Supply resistance, in ohms, to reference value A; supply reactance, in ohms, to reference value B.
    '''
    IDEAL_CAPACITANCE = 1077
    r'''
    The ideal capacitance of your DUT. Supply capacitance, in farads, to reference value A.
    '''
    IDEAL_INDUCTANCE = 1078
    r'''
    The ideal inductance of your DUT. Supply inductance, in henrys, to reference value A.
    '''
    IDEAL_RESISTANCE = 1079
    r'''
    The ideal resistance of your DUT. Supply resistance, in ohms, to reference value A.
    '''


class LCRSourceDelayMode(Enum):
    AUTOMATIC = 1144
    r'''
    NI-DCPower automatically applies source delay of sufficient duration to account for settling time.
    '''
    MANUAL = 1145
    r'''
    NI-DCPower applies the source delay that you set manually with source_delay. You can use this option to set a shorter delay to reduce measurement time at the possible expense of measurement accuracy.
    '''


class LCRStimulusFunction(Enum):
    VOLTAGE = 1063
    r'''
    Applies an AC voltage for LCR stimulus.
    '''
    CURRENT = 1064
    r'''
    Applies an AC current for LCR stimulus.
    '''


class MeasureWhen(Enum):
    AUTOMATICALLY_AFTER_SOURCE_COMPLETE = 1025
    r'''
    Acquires a measurement after each Source Complete event completes.
    '''
    ON_DEMAND = 1026
    r'''
    Acquires a measurement when the measure method or measure_multiple method is called.
    '''
    ON_MEASURE_TRIGGER = 1027
    r'''
    Acquires a measurement when a Measure trigger is received.
    '''


class MeasurementTypes(Enum):
    CURRENT = 0
    r'''
    The device measures current.
    '''
    VOLTAGE = 1
    r'''
    The device measures voltage.
    '''


class OutputCapacitance(Enum):
    LOW = 1010
    r'''
    Output Capacitance is low.
    '''
    HIGH = 1011
    r'''
    Output Capacitance is high.
    '''


class OutputCutoffReason(Enum):
    ALL = -1
    r'''
    Queries any output cutoff condition; clears all output cutoff conditions.
    '''
    VOLTAGE_OUTPUT_HIGH = 1
    r'''
    Queries or clears cutoff conditions when the output exceeded the high cutoff limit for voltage output.
    '''
    VOLTAGE_OUTPUT_LOW = 2
    r'''
    Queries or clears cutoff conditions when the output fell below the low cutoff limit for voltage output.
    '''
    CURRENT_MEASURE_HIGH = 4
    r'''
    Queries or clears cutoff conditions when the measured current exceeded the high cutoff limit for current output.
    '''
    CURRENT_MEASURE_LOW = 8
    r'''
    Queries or clears cutoff conditions when the measured current fell below the low cutoff limit for current output.
    '''
    VOLTAGE_CHANGE_HIGH = 16
    r'''
    Queries or clears cutoff conditions when the voltage slew rate increased beyond the positive change cutoff for voltage output.
    '''
    VOLTAGE_CHANGE_LOW = 32
    r'''
    Queries or clears cutoff conditions when the voltage slew rate decreased beyond the negative change cutoff for voltage output.
    '''
    CURRENT_CHANGE_HIGH = 64
    r'''
    Queries or clears cutoff conditions when the current slew rate increased beyond the positive change cutoff for current output.
    '''
    CURRENT_CHANGE_LOW = 128
    r'''
    Queries or clears cutoff conditions when the current slew rate decreased beyond the negative change cutoff for current output.
    '''
    CURRENT_SATURATED = 512
    r'''
    Queries or clears cutoff conditions when the measured current saturates the current range.
    '''
    VOLTAGE_MEASURE_HIGH = 1024
    r'''
    Queries or clears cutoff conditions when the measured voltage exceeded the high cutoff limit for voltage output.
    '''
    VOLTAGE_MEASURE_LOW = 2048
    r'''
    Queries or clears cutoff conditions when the measured voltage fell below the low cutoff limit for voltage output.
    '''


class OutputFunction(Enum):
    DC_VOLTAGE = 1006
    r'''
    Sets the output method to DC voltage.
    '''
    DC_CURRENT = 1007
    r'''
    Sets the output method to DC current.
    '''
    PULSE_VOLTAGE = 1049
    r'''
    Sets the output method to pulse voltage.
    '''
    PULSE_CURRENT = 1050
    r'''
    Sets the output method to pulse current.
    '''
    CONSTANT_RESISTANCE = 1161
    r'''
    Sets the output method to constant resistance.
    '''
    CONSTANT_POWER = 1162
    r'''
    Sets the output method to constant power.
    '''


class OutputStates(Enum):
    CONSTANT_VOLTAGE = 0
    r'''
    The channel maintains a constant voltage by adjusting the current.
    '''
    CONSTANT_CURRENT = 1
    r'''
    The channel maintains a constant current by adjusting the voltage.
    '''
    INHIBITED = 1163
    r'''
    The channel is in the inhibited state.
    '''


class Polarity(Enum):
    HIGH = 1018
    r'''
    A high pulse occurs when the event is generated.  The exported signal is low level both before and after the event is generated.
    '''
    LOW = 1019
    r'''
    A low pulse occurs when the event is generated.  The exported signal is high level both before and after the event is generated.
    '''


class PowerAllocationMode(Enum):
    DISABLED = 1058
    r'''
    The device attempts to source, on each active channel, the power that the present source configuration requires; NI-DCPower does not perform a sourcing power check. If the required power is greater than the maximum sourcing power, the device attempts to source the required amount and may shut down to prevent damage.
    '''
    AUTOMATIC = 1059
    r'''
    The device attempts to source, on each active channel, the power that the present source configuration requires; NI-DCPower performs a sourcing power check. If the required power is greater than the maximum sourcing power, the device does not exceed the maximum power, and NI-DCPower returns an error.
    '''
    MANUAL = 1060
    r'''
    The device attempts to source, on each active channel, the power you request with the requested_power_allocation property; NI-DCPower performs a sourcing power check. If the requested power is either less than the required power for the present source configuration or greater than the maximum sourcing power, the device does not exceed the requested or allowed power, respectively, and NI-DCPower returns an error.
    '''


class PowerSource(Enum):
    INTERNAL = 1003
    r'''
    Uses the PXI chassis power source.
    '''
    AUXILIARY = 1004
    r'''
    Uses the auxiliary power source connected to the device.
    '''
    AUTOMATIC = 1005
    r'''
    Uses the auxiliary power source if it is available; otherwise uses the PXI chassis power source.
    '''


class PowerSourceInUse(Enum):
    INTERNAL = 1003
    r'''
    Uses the PXI chassis power source.
    '''
    AUXILIARY = 1004
    r'''
    Uses the auxiliary power source connected to the device. Only the NI PXI-4110, NI PXIe-4112, NI PXIe-4113, and NI PXI-4130 support this value. This is the only supported value for the NI PXIe-4112 and NI PXIe-4113.
    '''


class SelfCalibrationPersistence(Enum):
    KEEP_IN_MEMORY = 1045
    r'''
    Keep new self calibration values in memory only.
    '''
    WRITE_TO_EEPROM = 1046
    r'''
    Write new self calibration values to hardware.
    '''


class SendSoftwareEdgeTriggerType(Enum):
    START = 1034
    r'''
    Asserts the Start trigger.
    '''
    SOURCE = 1035
    r'''
    Asserts the Source trigger.
    '''
    MEASURE = 1036
    r'''
    Asserts the Measure trigger.
    '''
    SEQUENCE_ADVANCE = 1037
    r'''
    Asserts the Sequence Advance trigger.
    '''
    PULSE = 1053
    r'''
    Asserts the Pulse trigger.
    '''
    SHUTDOWN = 1118
    r'''
    Asserts the Shutdown trigger.
    '''


class Sense(Enum):
    LOCAL = 1008
    r'''
    Local sensing is selected.
    '''
    REMOTE = 1009
    r'''
    Remote sensing is selected.
    '''


class SourceMode(Enum):
    SINGLE_POINT = 1020
    r'''
    The source unit applies a single source configuration.
    '''
    SEQUENCE = 1021
    r'''
    The source unit applies a list of voltage or current configurations sequentially.
    '''


class TransientResponse(Enum):
    NORMAL = 1038
    r'''
    The output responds to changes in load at a normal speed.
    '''
    FAST = 1039
    r'''
    The output responds to changes in load quickly.
    '''
    SLOW = 1041
    r'''
    The output responds to changes in load slowly.
    '''
    CUSTOM = 1042
    r'''
    The output responds to changes in load based on specified values.
    '''


class TriggerType(Enum):
    NONE = 1012
    r'''
    No trigger is configured.
    '''
    DIGITAL_EDGE = 1014
    r'''
    The data operation starts when a digital edge is detected.
    '''
    SOFTWARE_EDGE = 1015
    r'''
    The data operation starts when a software trigger occurs.
    '''
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidcpower/nidcpower/errors.py sha256=5d009b4314d2445ebffcec7ce14c6b83d911104fd7fd1cf26cb53242e5d643c6 bytes=4382 -->
## FILE: generated/nidcpower/nidcpower/errors.py

- repository: `ni/nimi-python`
- source_path: `generated/nidcpower/nidcpower/errors.py`
- sha256: `5d009b4314d2445ebffcec7ce14c6b83d911104fd7fd1cf26cb53242e5d643c6`
- bytes: 4382

````python
# -*- coding: utf-8 -*-
# This file was generated


import platform
import warnings


def _is_success(code):
    return (code == 0)


def _is_error(code):
    return (code < 0)


def _is_warning(code):
    return (code > 0)


class Error(Exception):
    '''Base error class for NI-DCPower'''

    def __init__(self, message):
        super(Error, self).__init__(message)


class DriverError(Error):
    '''An error originating from the NI-DCPower driver'''

    def __init__(self, code, description):
        assert _is_error(code), "Should not raise Error if code is not fatal."
        self.code = code
        self.description = description
        super(DriverError, self).__init__(str(self.code) + ": " + self.description)


class DriverWarning(Warning):
    '''A warning originating from the NI-DCPower driver'''

    def __init__(self, code, description):
        assert _is_warning(code), "Should not create Warning if code is not positive."
        super(DriverWarning, self).__init__('Warning {} occurred.\n\n{}'.format(code, description))


class RpcError(Error):
    '''An error specific to sessions to the NI gRPC Device Server'''

    def __init__(self, rpc_code, description):
        self.rpc_code = rpc_code
        self.description = description
        try:
            import grpc
            rpc_error = str(grpc.StatusCode(self.rpc_code))
        except Exception:
            rpc_error = str(self.rpc_code)
        super(RpcError, self).__init__(rpc_error + ": " + self.description)


class UnsupportedConfigurationError(Error):
    '''An error due to using this module in an usupported platform.'''

    def __init__(self):
        super(UnsupportedConfigurationError, self).__init__('System configuration is unsupported: ' + platform.architecture()[0] + ' ' + platform.system())


class DriverNotInstalledError(Error):
    '''An error due to using this module without the driver runtime installed.'''

    def __init__(self):
        super(DriverNotInstalledError, self).__init__('The NI-DCPower runtime could not be loaded. Make sure it is installed and its bitness matches that of your Python interpreter. Please visit http://www.ni.com/downloads/drivers/ to download and install it.')


class DriverTooOldError(Error):
    '''An error due to using this module with an older version of the NI-DCPower driver runtime.'''

    def __init__(self):
        super(DriverTooOldError, self).__init__('A function was not found in the NI-DCPower runtime. Please visit http://www.ni.com/downloads/drivers/ to download a newer version and install it.')


class DriverTooNewError(Error):
    '''An error due to the NI-DCPower driver runtime being too new for this module.'''

    def __init__(self):
        super(DriverTooNewError, self).__init__('The NI-DCPower runtime returned an unexpected value. This can occur if it is too new for the nidcpower Python module. Upgrade the nidcpower Python module.')


class InvalidRepeatedCapabilityError(Error):
    '''An error due to an invalid character in a repeated capability'''

    def __init__(self, invalid_character, invalid_string):
        super(InvalidRepeatedCapabilityError, self).__init__('An invalid character ({}) was found in repeated capability string ({})'.format(invalid_character, invalid_string))


class SelfTestError(Error):
    '''An error due to a failed self-test'''

    def __init__(self, code, msg):
        self.code = code
        self.message = msg
        super(SelfTestError, self).__init__('Self-test failed with code {}: {}'.format(code, msg))


def handle_error(library_interpreter, code, ignore_warnings, is_error_handling):
    '''handle_error

    Helper function for handling errors returned by nidcpower.Library.
    It calls back into the LibraryInterpreter to get the corresponding error
    description and raises if necessary.
    '''

    if _is_success(code) or (_is_warning(code) and ignore_warnings):
        return

    if is_error_handling:
        # The caller is in the midst of error handling and an error occurred.
        # Don't try to get the description or we'll start recursing until the stack overflows.
        description = ''
    else:
        description = library_interpreter.get_error_description(code)

    if _is_error(code):
        raise DriverError(code, description)

    assert _is_warning(code)
    warnings.warn(DriverWarning(code, description))
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidcpower/nidcpower/grpc_session_options.py sha256=31860a7c40b48748d2e2afcbf1b26155924d5bb928511270cbb757e84d15d968 bytes=3458 -->
## FILE: generated/nidcpower/nidcpower/grpc_session_options.py

- repository: `ni/nimi-python`
- source_path: `generated/nidcpower/nidcpower/grpc_session_options.py`
- sha256: `31860a7c40b48748d2e2afcbf1b26155924d5bb928511270cbb757e84d15d968`
- bytes: 3458

````python
# -*- coding: utf-8 -*-
# This file was generated

from enum import IntEnum


# This constant specifies the gRPC package and service used by this API.
# Customers can pass this value to the MeasurementLink discovery service to resolve the server instance that provides this interface.
GRPC_SERVICE_INTERFACE_NAME = 'nidcpower_grpc.NiDCPower'

# This constant specifies the API license key required by the NI gRPC Device Server that comes with
# MeasurementLink 2023 Q1.
MEASUREMENTLINK_23Q1_NIMI_PYTHON_API_KEY = 'DE10751B-3EE0-44EC-A93B-800E6A3C89E4'


class SessionInitializationBehavior(IntEnum):
    AUTO = 0
    r'''
    The NI gRPC Device Server will attach to an existing session with the specified name if it exists, otherwise the server
    will initialize a new session.

    Note:
    When using the Session as a context manager and the context exits, the behavior depends on what happened when the constructor
    was called. If it resulted in a new session being initialized on the NI gRPC Device Server, then it will automatically close the
    server session. If it instead attached to an existing session, then it will detach from the server session and leave it open.
    '''
    INITIALIZE_SERVER_SESSION = 1
    r'''
    Require the NI gRPC Device Server to initialize a new session with the specified name.

    Note:
    When using the Session as a context manager and the context exits, it will automatically close the
    server session.
    '''
    ATTACH_TO_SERVER_SESSION = 2
    r'''
    Require the NI gRPC Device Server to attach to an existing session with the specified name.

    Note:
    When using the Session as a context manager and the context exits, it will detach from the server session
    and leave it open.
    '''


class GrpcSessionOptions(object):
    '''Collection of options that specifies session behaviors related to gRPC.'''

    def __init__(
        self,
        grpc_channel,
        session_name,
        *,
        api_key=MEASUREMENTLINK_23Q1_NIMI_PYTHON_API_KEY,
        initialization_behavior=SessionInitializationBehavior.AUTO
    ):
        r'''Collection of options that specifies session behaviors related to gRPC.

        Creates and returns an object you can pass to a Session constructor.

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
        '''
        self.grpc_channel = grpc_channel
        self.session_name = session_name
        self.api_key = api_key
        self.initialization_behavior = initialization_behavior
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidcpower/nidcpower/lcr_load_compensation_spot.py sha256=b0b661a9866fa76df7d65a2db4d49161f4be4c664c87159f332d8b2cce1dcb69 bytes=4255 -->
## FILE: generated/nidcpower/nidcpower/lcr_load_compensation_spot.py

- repository: `ni/nimi-python`
- source_path: `generated/nidcpower/nidcpower/lcr_load_compensation_spot.py`
- sha256: `b0b661a9866fa76df7d65a2db4d49161f4be4c664c87159f332d8b2cce1dcb69`
- bytes: 4255

````python
import ctypes
import platform

import nidcpower._visatype
import nidcpower.enums as enums


# This class is an internal ctypes implementation detail that corresponds to
# NILCRLoadCompensationSpot in the C API
class struct_NILCRLoadCompensationSpot(ctypes.Structure):  # noqa N801
    if (platform.system() == "Windows" and platform.architecture()[0] == "64bit") or \
            platform.system() == "Linux" or platform.system() == "Darwin":
        _pack_ = 8
    else:
        _pack_ = 1
    _fields_ = [
        ("frequency", nidcpower._visatype.ViReal64),
        ("reference_value_type", nidcpower._visatype.ViInt32),
        ("reference_value_a", nidcpower._visatype.ViReal64),
        ("reference_value_b", nidcpower._visatype.ViReal64),
    ]

    def __init__(self, data):
        super(ctypes.Structure, self).__init__()
        self.frequency = data.frequency
        self.reference_value_type = enums.LCRReferenceValueType(data.reference_value_type).value
        if self.reference_value_type == enums.LCRReferenceValueType.IMPEDANCE.value:
            self.reference_value_a = data.reference_value.real
            self.reference_value_b = data.reference_value.imag
        else:
            self.reference_value_a = data.reference_value
            self.reference_value_b = 0.0


class LCRLoadCompensationSpot:
    """Specifies a DUT specification for a given frequency to use in LCR load compensation."""

    _lcr_reference_value_type_to_label_and_units = {
        enums.LCRReferenceValueType.IMPEDANCE: {
            "label": "Impedance        ",
            "unit": "Ω"
        },
        enums.LCRReferenceValueType.IDEAL_CAPACITANCE: {
            "label": "Ideal Capacitance",
            "unit": "F"
        },
        enums.LCRReferenceValueType.IDEAL_INDUCTANCE: {
            "label": "Ideal Inductance ",
            "unit": "H"
        },
        enums.LCRReferenceValueType.IDEAL_RESISTANCE: {
            "label": "Ideal Resistance ",
            "unit": "Ω"
        },
    }

    def __init__(self, frequency, reference_value_type, reference_value):
        """LCRLoadCompensationSpot

        Creates and returns an instance of LCRLoadCompensationSpot.

        Args:
            frequency (float): The spot frequency, in Hz.

            reference_value_type (enums.LCRReferenceValueType): A known specification value of your
                DUT to use as the basis for load compensation.

            reference_value (complex or float): A value that describes the reference_value_type
                specification. Use as indicated by the reference_value_type option you choose.
        """
        self.frequency = frequency
        self.reference_value_type = enums.LCRReferenceValueType(reference_value_type)
        self.reference_value = reference_value

    def _create_copy(self, target_class):
        try:
            return target_class(frequency=self.frequency, reference_value_type=self.reference_value_type.value, reference_value=self.reference_value)
        except ValueError:
            return target_class(frequency=self.frequency, reference_value_type=self.reference_value_type.value, reference_value_a=self.reference_value.real, reference_value_b=self.reference_value.imag)

    def __repr__(self):
        return "{}.{}(frequency={}, reference_value_type={}.{}.{}, reference_value={})".format(
            self.__class__.__module__,
            self.__class__.__qualname__,
            self.frequency,
            enums.LCRReferenceValueType.__module__,
            enums.LCRReferenceValueType.__qualname__,
            self.reference_value_type.name,
            self.reference_value,
        )

    def __str__(self):
        return "".join(
            [
                "Frequency        : {:,.6g} Hz\n{}: {:,.6g} {}\n".format(
                    self.frequency,
                    LCRLoadCompensationSpot._lcr_reference_value_type_to_label_and_units[
                        self.reference_value_type
                    ]["label"],
                    self.reference_value,
                    LCRLoadCompensationSpot._lcr_reference_value_type_to_label_and_units[
                        self.reference_value_type
                    ]["unit"],
                ),
            ]
        )
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nidcpower/nidcpower/lcr_measurement.py sha256=0187d6cf7359414026a0266469a8a176f389a6dc51c9a031a07a9f72adaf636f bytes=12166 -->
## FILE: generated/nidcpower/nidcpower/lcr_measurement.py

- repository: `ni/nimi-python`
- source_path: `generated/nidcpower/nidcpower/lcr_measurement.py`
- sha256: `0187d6cf7359414026a0266469a8a176f389a6dc51c9a031a07a9f72adaf636f`
- bytes: 12166

````python
from collections import namedtuple
import ctypes

import nidcpower._visatype
import nidcpower.enums as enums


# This class is an internal ctypes implementation detail that corresponds to
# NILCRMeasurement in the C API
class struct_NILCRMeasurement(ctypes.Structure):  # noqa N801
    _pack_ = 8
    _fields_ = [
        # field_name             field_ctype
        ("vdc"                 , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("idc"                 , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("stimulus_frequency"  , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("ac_voltage_real"     , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("ac_voltage_imaginary", nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("ac_current_real"     , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("ac_current_imaginary", nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("z_real"              , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("z_imaginary"         , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("z_magnitude"         , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("z_phase"             , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("y_real"              , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("y_imaginary"         , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("y_magnitude"         , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("y_phase"             , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("ls"                  , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("cs"                  , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("rs"                  , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("lp"                  , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("cp"                  , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("rp"                  , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("d"                   , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("q"                   , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("measurement_mode"    , nidcpower._visatype.ViUInt16 ),  # noqa: E202,E203
        ("dc_in_compliance"    , nidcpower._visatype.ViBoolean),  # noqa: E202,E203
        ("ac_in_compliance"    , nidcpower._visatype.ViBoolean),  # noqa: E202,E203
        ("unbalanced"          , nidcpower._visatype.ViBoolean),  # noqa: E202,E203
        ("reserved1"           , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("reserved2"           , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("reserved3"           , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("reserved4"           , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("reserved5"           , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("reserved6"           , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
        ("reserved7"           , nidcpower._visatype.ViReal64 ),  # noqa: E202,E203
    ]


class LCRMeasurement:
    """Specifies an LCR measurement.

    Data attributes:
        channel (str): The channel name associated with this LCRMeasurement.

        vdc (float): The measured DC voltage, in volts.

        idc (float): The measured DC current, in amps.

        stimulus_frequency (float): The frequency of the LCR test signal, in Hz.

        ac_voltage (complex): The measured AC voltage, in volts RMS.

        ac_current (complex): The measured AC current, in amps RMS.

        z (complex): The complex impedance.

        z_magnitude_and_phase (tuple of float): The magnitude, in ohms, and phase angle, in degrees,
            of the complex impedance.

        y (complex): The complex admittance.

        y_magnitude_and_phase (tuple of float): The magnitude, in siemens, and phase angle, in
            degrees, of the complex admittance.

        series_lcr (LCR): The inductance, in henrys, the capacitance, in farads, and the resistance,
            in ohms, as measured using a series circuit model.

        parallel_lcr (LCR): The inductance, in henrys, the capacitance, in farads, and the
            resistance, in ohms, as measured using a parallel circuit model.

        d (float): The dissipation factor of the circuit. The dimensionless dissipation factor is
            directly proportional to how quickly an oscillating system loses energy. D is the
            reciprocal of Q, the quality factor.

        q (float): The quality factor of the circuit. The dimensionless quality factor is inversely
            proportional to the degree of damping in a system. Q is the reciprocal of D, the
            dissipation factor.

        measurement_mode (enums.InstrumentMode): The measurement mode.
            **Defined Values**:

            +-----------------------+-----------------------------------------------------+
            | InstrumentMode.SMU_PS | The channel(s) are operating as a power supply/SMU. |
            +-----------------------+-----------------------------------------------------+
            | InstrumentMode.LCR    | The channel(s) are operating as an LCR meter.       |
            +-----------------------+-----------------------------------------------------+

        dc_in_compliance (bool): Indicates whether the output was in DC compliance at the time the
            measurement was taken.

        ac_in_compliance (bool): Indicates whether the output was in AC compliance at the time the
            measurement was taken.

        unbalanced (bool): Indicates whether the bridge was unbalanced at the time the measurement
            was taken.
    """
    LCR = namedtuple(typename="LCR", field_names=("inductance", "capacitance", "resistance"))

    _lcr_measurement_field_metadata = [
        # field_name              label(s)                                                                unit(s)
        ("channel"              , "Channel"                                                             , None           ),  # noqa: E202,E203
        ("vdc"                  , "DC voltage"                                                          , "V"            ),  # noqa: E202,E203
        ("idc"                  , "DC current"                                                          , "A"            ),  # noqa: E202,E203
        ("stimulus_frequency"   , "Stimulus frequency"                                                  , "Hz"           ),  # noqa: E202,E203
        ("ac_voltage"           , "AC voltage"                                                          , "V RMS"        ),  # noqa: E202,E203
        ("ac_current"           , "AC current"                                                          , "A RMS"        ),  # noqa: E202,E203
        ("z"                    , "Impedance"                                                           , "Ω"            ),  # noqa: E202,E203
        ("z_magnitude_and_phase", ("Impedance magnitude", "Impedance phase")                            , ("Ω", "°")     ),  # noqa: E202,E203
        ("y"                    , "Admittance"                                                          , "S"            ),  # noqa: E202,E203
        ("y_magnitude_and_phase", ("Admittance magnitude", "Admittance phase")                          , ("S", "°")     ),  # noqa: E202,E203
        ("series_lcr"           , ("Series inductance", "Series capacitance", "Series resistance")      , ("H", "F", "Ω")),  # noqa: E202,E203
        ("parallel_lcr"         , ("Parallel inductance", "Parallel capacitance", "Parallel resistance"), ("H", "F", "Ω")),  # noqa: E202,E203
        ("d"                    , "Dissipation factor"                                                  , None           ),  # noqa: E202,E203
        ("q"                    , "Quality factor"                                                      , None           ),  # noqa: E202,E203
        ("measurement_mode"     , "Measurement mode"                                                    , None           ),  # noqa: E202,E203
        ("dc_in_compliance"     , "DC in compliance"                                                    , None           ),  # noqa: E202,E203
        ("ac_in_compliance"     , "AC in compliance"                                                    , None           ),  # noqa: E202,E203
        ("unbalanced"           , "Unbalanced"                                                          , None           ),  # noqa: E202,E203
    ]

    def __init__(self, data):
        """LCRMeasurement

        Creates and returns an instance of LCRMeasurement.

        Args:
            data (struct_NILCRMeasurement): The LCR measurement ctypes instance returned by the driver.
        """
        self.channel = ""
        self.vdc = data.vdc
        self.idc = data.idc
        self.stimulus_frequency = data.stimulus_frequency
        if hasattr(data, "ac_voltage_real"):
            self.ac_voltage = complex(data.ac_voltage_real, data.ac_voltage_imaginary)
            self.ac_current = complex(data.ac_current_real, data.ac_current_imaginary)
            self.z = complex(data.z_real, data.z_imaginary)
            self.y = complex(data.y_real, data.y_imaginary)
        else:
            self.ac_voltage = complex(data.ac_voltage.real, data.ac_voltage.imaginary)
            self.ac_current = complex(data.ac_current.real, data.ac_current.imaginary)
            self.z = complex(data.z.real, data.z.imaginary)
            self.y = complex(data.y.real, data.y.imaginary)
        self.z_magnitude_and_phase = (data.z_magnitude, data.z_phase)
        self.y_magnitude_and_phase = (data.y_magnitude, data.y_phase)
        self.series_lcr = LCRMeasurement.LCR(
            inductance=data.ls, capacitance=data.cs, resistance=data.rs
        )
        self.parallel_lcr = LCRMeasurement.LCR(
            inductance=data.lp, capacitance=data.cp, resistance=data.rp
        )
        self.d = data.d
        self.q = data.q
        self.measurement_mode = enums.InstrumentMode(data.measurement_mode)
        self.dc_in_compliance = bool(data.dc_in_compliance)
        self.ac_in_compliance = bool(data.ac_in_compliance)
        self.unbalanced = bool(data.unbalanced)

    def __str__(self):
        max_field_label_len = max(
            len(max(field_label, key=len) if isinstance(field_label, tuple) else field_label)
            for _, field_label, _ in LCRMeasurement._lcr_measurement_field_metadata
        )
        field_value_strings = []
        for field_name, field_label, field_unit in LCRMeasurement._lcr_measurement_field_metadata:
            # Determines row_format
            if field_name in (
                "channel",
                "measurement_mode",
                "dc_in_compliance",
                "ac_in_compliance",
                "unbalanced"
            ):
                row_format = f"{{:<{max_field_label_len}}}: {{:}}{{}}\n"
            else:
                row_format = f"{{:<{max_field_label_len}}}: {{:,.6g}}{{}}\n"
            # Process namedtuple fields
            if isinstance(field_label, tuple) and isinstance(field_unit, tuple):
                for label, unit, value in zip(field_label, field_unit, getattr(self, field_name)):
                    unit_string = f" {unit}" if unit is not None else ""
                    field_value_strings.append(row_format.format(label, value, unit_string))
            else:
                field_value = getattr(self, field_name)
                if field_name == "measurement_mode":
                    field_value = enums.InstrumentMode(field_value).name
                elif field_name in ("dc_in_compliance", "ac_in_compliance", "unbalanced"):
                    field_value = bool(field_value)
                unit_string = f" {field_unit}" if field_unit is not None else ""
                field_value_strings.append(row_format.format(field_label, field_value, unit_string))
        return "".join(field_value_strings)
````
