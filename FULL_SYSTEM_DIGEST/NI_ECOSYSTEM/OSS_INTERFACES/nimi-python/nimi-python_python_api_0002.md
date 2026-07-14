# NI PYTHON API DIGEST: nimi-python

<!--NI_PYTHON_API_SNAPSHOT repo=ni/nimi-python commit=6511f8025f072f7f7021953888b916bbdc31aa2a -->

<!--NI_PYTHON_API repo=nimi-python path=generated/nidmm/nidmm/session.py -->
## PYTHON MODULE: generated/nidmm/nidmm/session.py

### `class _Acquisition(object)`

#### `def __init__(self, session)`

#### `def __enter__(self)`

#### `def __exit__(self, exc_type, exc_value, traceback)`

### `def ivi_synchronized(f)`

### `class _Lock(object)`

#### `def __init__(self, session)`

#### `def __enter__(self)`

#### `def __exit__(self, exc_type, exc_value, traceback)`

### `class _SessionBase(object)`

Base class for all NI-DMM sessions.

#### `def __init__(self, repeated_capability_list, all_channels_in_session, interpreter, freeze_it=False)`

#### `def __repr__(self)`

#### `def __setattr__(self, key, value)`

#### `def _get_attribute_vi_boolean(self, attribute_id)`

_get_attribute_vi_boolean

        Queries the value of a ViBoolean property. You can use this method to
        get the values of instrument-specific properties and inherent IVI
        properties.

        If the property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled, and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`nidmm.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`nidmm.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_boolean`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            attribute_value (bool): Returns the current value of the property. Pass the address of a
                ViBoolean variable.

        

#### `def _get_attribute_vi_int32(self, attribute_id)`

_get_attribute_vi_int32

        Queries the value of a ViInt32 property. You can use this method to
        get the values of instrument-specific properties and inherent IVI
        properties.

        If the property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled, and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`nidmm.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`nidmm.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_int32`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            attribute_value (int): Returns the current value of the property. Pass the address of a
                ViInt32 variable.

        

#### `def _get_attribute_vi_real64(self, attribute_id)`

_get_attribute_vi_real64

        Queries the value of a ViReal64 property. You can use this method to
        get the values of instrument-specific properties and inherent IVI
        properties.

        If the property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled, and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`nidmm.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nidmm.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_real64`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            attribute_value (float): Returns the current value of the property. Pass the address of a
                ViReal64 variable.

        

#### `def _get_attribute_vi_string(self, attribute_id)`

_get_attribute_vi_string

        Queries the value of a ViString property. You can use this method to
        get the values of instrument-specific properties and inherent IVI
        properties.

        If the property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled, and the currently cached value is invalid.
           You must provide a ViChar array to serve as a buffer for the value.
           You pass the number of bytes in the buffer as the Array Size
           parameter.

        Tip:
        This method can be called on specific channels within your :py:class:`nidmm.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nidmm.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_string`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            attribute_value (str): The buffer in which the method returns the current value of the
                property. The buffer must be of type ViChar and have at least as many
                bytes as indicated in the **Buffer_Size** parameter.

                If you specify 0 for the **Buffer_Size** parameter, you can pass
                VI_NULL for this parameter.

        

#### `def lock(self)`

lock

        Obtains a multithread lock on the device session. Before doing so, the
        software waits until all other execution threads release their locks
        on the device session.

        Other threads may have obtained a lock on this session for the
        following reasons:

            -  The application called the lock method.
            -  A call to NI-DMM locked the session.
            -  After a call to the lock method returns
               successfully, no other threads can access the device session until
               you call the unlock method or exit out of the with block when using
               lock context manager.
            -  Use the lock method and the
               unlock method around a sequence of calls to
               instrument driver methods if you require that the device retain its
               settings through the end of the sequence.

        You can safely make nested calls to the lock method
        within the same thread. To completely unlock the session, you must
        balance each call to the lock method with a call to
        the unlock method.

        Returns:
            lock (context manager): When used in a with statement, nidmm.Session.lock acts as
            a context manager and unlock will be called when the with block is exited
        

#### `def _set_attribute_vi_boolean(self, attribute_id, attribute_value)`

_set_attribute_vi_boolean

        This method sets the value of a ViBoolean property.

        This is a low-level method that you can use to set the values of
        instrument-specific properties and inherent IVI properties.

        If the property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled, and the currently cached value is invalid
           or is different than the value you specify.

        This instrument driver contains high-level methods that set most of
        the instrument properties. It is best to use the high-level driver
        methods as much as possible. They handle order dependencies and
        multithread locking for you. In addition, they perform status checking
        only after setting all of the properties.

        In contrast, when you set multiple properties using the SetAttribute
        methods, the methods check the instrument status after each call.
        Also, when state caching is enabled, the high-level methods that
        configure multiple properties perform instrument I/O only for the
        properties whose value you change. Thus, you can safely call the
        high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nidmm.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`nidmm.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_boolean`

        Args:
            attribute_id (int): Pass the ID of a property.

            attribute_value (bool): Pass the value that you want to set the property to.

        

#### `def _set_attribute_vi_int32(self, attribute_id, attribute_value)`

_set_attribute_vi_int32

        This method sets the value of a ViInt32 property.

        This is a low-level method that you can use to set the values of
        instrument-specific properties and inherent IVI properties.

        If the property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled, and the currently cached value is invalid
           or is different than the value you specify.

        This instrument driver contains high-level methods that set most of
        the instrument properties. It is best to use the high-level driver
        methods as much as possible. They handle order dependencies and
        multithread locking for you. In addition, they perform status checking
        only after setting all of the properties.

        In contrast, when you set multiple properties using the SetAttribute
        methods, the methods check the instrument status after each call.
        Also, when state caching is enabled, the high-level methods that
        configure multiple properties perform instrument I/O only for the
        properties whose value you change. Thus, you can safely call the
        high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nidmm.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`nidmm.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_int32`

        Args:
            attribute_id (int): Pass the ID of a property.

            attribute_value (int): Pass the value that you want to set the property to.

        

#### `def _set_attribute_vi_real64(self, attribute_id, attribute_value)`

_set_attribute_vi_real64

        This method sets the value of a ViReal64 property.

        This is a low-level method that you can use to set the values of
        instrument-specific properties and inherent IVI properties.

        If the property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled, and the currently cached value is invalid
           or is different than the value you specify.

        This instrument driver contains high-level methods that set most of
        the instrument properties. It is best to use the high-level driver
        methods as much as possible. They handle order dependencies and
        multithread locking for you. In addition, they perform status checking
        only after setting all of the properties.

        In contrast, when you set multiple properties using the SetAttribute
        methods, the methods check the instrument status after each call.
        Also, when state caching is enabled, the high-level methods that
        configure multiple properties perform instrument I/O only for the
        properties whose value you change. Thus, you can safely call the
        high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nidmm.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nidmm.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_real64`

        Args:
            attribute_id (int): Pass the ID of a property.

            attribute_value (float): Pass the value that you want to set the property to.

        

#### `def _set_attribute_vi_string(self, attribute_id, attribute_value)`

_set_attribute_vi_string

        This method sets the value of a ViString property.

        This is a low-level method that you can use to set the values of
        instrument-specific properties and inherent IVI properties.

        If the property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled, and the currently cached value is invalid
           or is different than the value you specify.

        This instrument driver contains high-level methods that set most of
        the instrument properties. It is best to use the high-level driver
        methods as much as possible. They handle order dependencies and
        multithread locking for you. In addition, they perform status checking
        only after setting all of the properties.

        In contrast, when you set multiple properties using the SetAttribute
        methods, the methods check the instrument status after each call.
        Also, when state caching is enabled, the high-level methods that
        configure multiple properties perform instrument I/O only for the
        properties whose value you change. Thus, you can safely call the
        high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nidmm.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nidmm.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_string`

        Args:
            attribute_id (int): Pass the ID of a property.

            attribute_value (str): Pass the value that you want to set the property to.

        

#### `def unlock(self)`

unlock

        Releases a lock that you acquired on an device session using
        lock. Refer to lock for additional
        information on session locks.
        

#### `def _error_message(self, error_code)`

_error_message

        Takes the **Error_Code** returned by the instrument driver methods,
        interprets it, and returns it as a user-readable string.

        Note:
        When using grpc-device, this method will call GetErrorMessage server-side while providing the same interface.

        Args:
            error_code (int): The **error_code** returned from the instrument. The default is 0,
                indicating VI_SUCCESS.


        Returns:
            error_message (str): The error information formatted into a string.

        

### `class Session(_SessionBase)`

An NI-DMM session to an NI digital multimeter

#### `def __init__(self, resource_name, id_query=False, reset_device=False, options={}, *, grpc_options=None)`

An NI-DMM session to an NI digital multimeter

        This method completes the following tasks:

        -  Creates a new IVI instrument driver session and, optionally, sets the
           initial state of the following session properties:
           RANGE_CHECK, QUERY_INSTR_STATUS,
           CACHE, simulate,
           RECORD_COERCIONS.
        -  Opens a session to the device you specify for the **Resource_Name**
           parameter. If the **ID_Query** parameter is set to True, this
           method queries the instrument ID and checks that it is valid for
           this instrument driver.
        -  If the **Reset_Device** parameter is set to True, this method
           resets the instrument to a known state. Sends initialization commands
           to set the instrument to the state necessary for the operation of the
           instrument driver.
        -  Returns a ViSession handle that you use to identify the instrument in
           all subsequent instrument driver method calls.

        Note:
        One or more of the referenced properties are not in the Python API for this driver.

        Args:
            resource_name (str): Caution:
                All IVI names for the **Resource_Name**, such as logical names or
                virtual names, are case-sensitive. If you use logical names, driver
                session names, or virtual names in your program, you must make sure that
                the name you use matches the name in the IVI Configuration Store file
                exactly, without any variations in the case of the characters in the
                name.

                | Contains the **resource_name** of the device to initialize. The
                  **resource_name** is assigned in Measurement & Automation Explorer
                  (MAX). Refer to `Related
                  Documentation <REPLACE_DRIVER_SPECIFIC_URL_1(related_documentation)>`__
                  for the *NI Digital Multimeters Getting Started Guide* for more
                  information about configuring and testing the DMM in MAX.
                | Valid Syntax:

                -  NI-DAQmx name
                -  DAQ::NI-DAQmx name[::INSTR]
                -  DAQ::Traditional NI-DAQ device number[::INSTR]
                -  IVI logical name

            id_query (bool): Verifies that the device you initialize is one that the driver supports.
                NI-DMM automatically performs this query, so setting this parameter is
                not necessary.
                Defined Values:

                +----------------+---+------------------+
                | True (default) | 1 | Perform ID Query |
                +----------------+---+------------------+
                | False          | 0 | Skip ID Query    |
                +----------------+---+------------------+

            reset_device (bool): Specifies whether to reset the instrument during the initialization
                procedure.
                Defined Values:

                +----------------+---+--------------+
                | True (default) | 1 | Reset Device |
                +----------------+---+--------------+
                | False          | 0 | Don't Reset  |
                +----------------+---+--------------+

            options (dict): Specifies the initial value of certain properties for the session. The
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

            grpc_options (nidmm.grpc_session_options.GrpcSessionOptions): MeasurementLink gRPC session options


        Returns:
            session (nidmm.Session): A session object representing the device.

        

#### `def __enter__(self)`

#### `def __exit__(self, exc_type, exc_value, traceback)`

#### `def initiate(self)`

initiate

        Initiates an acquisition. After you call this method, the DMM leaves
        the Idle state and enters the Wait-for-Trigger state. If trigger is set
        to Immediate mode, the DMM begins acquiring measurement data. Use
        fetch, fetch_multi_point, or fetch_waveform to
        retrieve the measurement data.

        Note:
        This method will return a Python context manager that will initiate on entering and abort on exit.
        

#### `def close(self)`

close

        Closes the specified session and deallocates resources that it reserved.

        Note:
        This method is not needed when using the session context manager
        

#### `def abort(self)`

abort

        Aborts a previously initiated measurement and returns the DMM to the
        Idle state.
        

#### `def configure_measurement_absolute(self, measurement_function, range, resolution_absolute)`

configure_measurement_absolute

        Configures the common properties of the measurement. These properties
        include method, range, and
        resolution_absolute.

        Args:
            measurement_function (enums.Function): Specifies the **measurement_function** used to acquire the measurement.
                The driver sets method to this value.

            range (float): Specifies the **range** for the method specified in the
                **Measurement_Function** parameter. When frequency is specified in the
                **Measurement_Function** parameter, you must supply the minimum
                frequency expected in the **range** parameter. For example, you must
                type in 100 Hz if you are measuring 101 Hz or higher.
                For all other methods, you must supply a **range** that exceeds the
                value that you are measuring. For example, you must type in 10 V if you
                are measuring 9 V. **range** values are coerced up to the closest input
                **range**. Refer to the `Devices
                Overview <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__ for a list of valid
                ranges. The driver sets range to this value. The default is
                0.02 V.

                +---------------------------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIDMM_VAL_AUTO_RANGE_ON   | -1.0 | NI-DMM performs an Auto Range before acquiring the measurement.                                                                                                                         |
                +---------------------------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIDMM_VAL_AUTO_RANGE_OFF  | -2.0 | NI-DMM sets the Range to the current auto_range_value and uses this range for all subsequent measurements until the measurement configuration is changed.                               |
                +---------------------------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIDMM_VAL_AUTO_RANGE_ONCE | -3.0 | NI-DMM performs an Auto Range before acquiring the measurement. The auto_range_value is stored and used for all subsequent measurements until the measurement configuration is changed. |
                +---------------------------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

                Note:
                The NI 4050, NI 4060, and NI 4065 only support Auto Range when the
                trigger and sample trigger are set to IMMEDIATE.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            resolution_absolute (float): Specifies the absolute resolution for the measurement. NI-DMM sets
                resolution_absolute to this value. The PXIe-4080/4081/4082
                uses the resolution you specify. The NI 4065 and NI 4070/4071/4072
                ignore this parameter when the **Range** parameter is set to
                NIDMM_VAL_AUTO_RANGE_ON (-1.0) or NIDMM_VAL_AUTO_RANGE_ONCE
                (-3.0). The default is 0.001 V.

                Note:
                NI-DMM ignores this parameter for capacitance and inductance
                measurements on the NI 4072. To achieve better resolution for such
                measurements, use the lc_number_meas_to_average
                property.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        

#### `def configure_measurement_digits(self, measurement_function, range, resolution_digits)`

configure_measurement_digits

        Configures the common properties of the measurement. These properties
        include method, range, and
        resolution_digits.

        Args:
            measurement_function (enums.Function): Specifies the **measurement_function** used to acquire the measurement.
                The driver sets method to this value.

            range (float): Specifies the range for the method specified in the
                **Measurement_Function** parameter. When frequency is specified in the
                **Measurement_Function** parameter, you must supply the minimum
                frequency expected in the **range** parameter. For example, you must
                type in 100 Hz if you are measuring 101 Hz or higher.
                For all other methods, you must supply a range that exceeds the value
                that you are measuring. For example, you must type in 10 V if you are
                measuring 9 V. range values are coerced up to the closest input range.
                Refer to the `Devices
                Overview <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__ for a list of valid
                ranges. The driver sets range to this value. The default is
                0.02 V.

                +---------------------------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIDMM_VAL_AUTO_RANGE_ON   | -1.0 | NI-DMM performs an Auto Range before acquiring the measurement.                                                                                                                         |
                +---------------------------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIDMM_VAL_AUTO_RANGE_OFF  | -2.0 | NI-DMM sets the Range to the current auto_range_value and uses this range for all subsequent measurements until the measurement configuration is changed.                               |
                +---------------------------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | NIDMM_VAL_AUTO_RANGE_ONCE | -3.0 | NI-DMM performs an Auto Range before acquiring the measurement. The auto_range_value is stored and used for all subsequent measurements until the measurement configuration is changed. |
                +---------------------------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

                Note:
                The NI 4050, NI 4060, and NI 4065 only support Auto Range when the
                trigger and sample trigger are set to IMMEDIATE.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            resolution_digits (float): Specifies the resolution of the measurement in digits. The driver sets
                the `Devices Overview <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__ for a
                list of valid ranges. The driver sets resolution_digits
                property to this value. The PXIe-4080/4081/4082 uses the resolution you
                specify. The NI 4065 and NI 4070/4071/4072 ignore this parameter when
                the **Range** parameter is set to NIDMM_VAL_AUTO_RANGE_ON (-1.0) or
                NIDMM_VAL_AUTO_RANGE_ONCE (-3.0). The default is 5½.

                Note:
                NI-DMM ignores this parameter for capacitance and inductance
                measurements on the NI 4072. To achieve better resolution for such
                measurements, use the lc_number_meas_to_average
                property.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        

#### `def configure_multi_point(self, trigger_count, sample_count, sample_trigger=enums.SampleTrigger.IMMEDIATE, sample_interval=hightime.timedelta(seconds=-1))`

configure_multi_point

        Configures the properties for multipoint measurements. These properties
        include trigger_count, sample_count,
        sample_trigger, and sample_interval.

        For continuous acquisitions, set trigger_count or
        sample_count to zero. For more information, refer to
        `Multiple Point
        Acquisitions <REPLACE_DRIVER_SPECIFIC_URL_1(multi_point)>`__,
        `Triggering <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__, and `Using
        Switches <REPLACE_DRIVER_SPECIFIC_URL_1(switch_selection)>`__.

        Args:
            trigger_count (int): Sets the number of triggers you want the DMM to receive before returning
                to the Idle state. The driver sets trigger_count to this
                value. The default value is 1.

            sample_count (int): Sets the number of measurements the DMM makes in each measurement
                sequence initiated by a trigger. The driver sets
                sample_count to this value. The default value is 1.

            sample_trigger (enums.SampleTrigger): Specifies the **sample_trigger** source you want to use. The driver
                sets sample_trigger to this value. The default is
                Immediate.

                Note:
                To determine which values are supported by each device, refer to the
                `LabWindows/CVI Trigger
                Routing <REPLACE_DRIVER_SPECIFIC_URL_1(cvitrigger_routing)>`__ section.

            sample_interval (hightime.timedelta, datetime.timedelta, or float in seconds): Sets the amount of time in seconds the DMM waits between measurement
                cycles. The driver sets sample_interval to this value.
                Specify a sample interval to add settling time between measurement
                cycles or to decrease the measurement rate. **sample_interval** only
                applies when the **Sample_Trigger** is set to INTERVAL.

                On the NI 4060, the **sample_interval** value is used as the settling
                time. When sample interval is set to 0, the DMM does not settle between
                measurement cycles. The NI 4065 and NI 4070/4071/4072 use the value
                specified in **sample_interval** as additional delay. The default value
                (-1) ensures that the DMM settles for a recommended time. This is the
                same as using an Immediate trigger.

                Note: This property is not used on the NI 4080/4081/4082 and the NI 4050.

        

#### `def configure_rtd_custom(self, rtd_a, rtd_b, rtd_c)`

configure_rtd_custom

        Configures the A, B, and C parameters for a custom RTD.

        Args:
            rtd_a (float): Specifies the Callendar-Van Dusen A coefficient for RTD scaling when RTD
                Type parameter is set to Custom in the configure_rtd_type method.
                The default is 3.9083e-3 (Pt3851)

            rtd_b (float): Specifies the Callendar-Van Dusen B coefficient for RTD scaling when RTD
                Type parameter is set to Custom in the configure_rtd_type method.
                The default is -5.775e-7 (Pt3851).

            rtd_c (float): Specifies the Callendar-Van Dusen C coefficient for RTD scaling when RTD
                Type parameter is set to Custom in the configure_rtd_type method.
                The default is -4.183e-12 (Pt3851).

        

#### `def configure_rtd_type(self, rtd_type, rtd_resistance)`

configure_rtd_type

        Configures the RTD Type and RTD Resistance parameters for an RTD.

        Args:
            rtd_type (enums.RTDType): Specifies the type of RTD used to measure the temperature resistance.
                NI-DMM uses this value to set the RTD Type property. The default is
                RTDType.PT3851.

                +---------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | Enum                            | Standards                                     | Material | TCR (α) | Typical R\ :sub:`0` (Ω) | Notes                                                                         |                               |
                +=================================+===============================================+==========+=========+=========================+===============================================================================+===============================+
                | Callendar-Van Dusen Coefficient |                                               |          |         |                         |                                                                               |                               |
                +---------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | RTDType.PT3851                  | IEC-751 DIN 43760 BS 1904 ASTM-E1137 EN-60751 | Platinum | .003851 | 100 Ω 1000 Ω            | A = 3.9083 × 10\ :sup:`–3` B = –5.775×10:sup:`–7` C = –4.183×10:sup:`–12`     | Most common RTDs              |
                +---------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | RTDType.PT3750                  | Low-cost vendor compliant RTD\*               | Platinum | .003750 | 1000 Ω                  | A = 3.81 × 10\ :sup:`–3` B = –6.02×10:sup:`–7` C = –6.0×10:sup:`–12`          | Low-cost RTD                  |
                +---------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | RTDType.PT3916                  | JISC 1604                                     | Platinum | .003916 | 100 Ω                   | A = 3.9739 × 10\ :sup:`–3` B = –5.870×10:sup:`–7` C = –4.4 ×10\ :sup:`–12`    | Used in primarily in Japan    |
                +---------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | RTDType.PT3920                  | US Industrial Standard D-100 American         | Platinum | .003920 | 100 Ω                   | A = 3.9787 × 10\ :sup:`–3` B = –5.8686×10:sup:`–7` C = –4.167 ×10\ :sup:`–12` | Low-cost RTD                  |
                +---------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | RTDType.PT3911                  | US Industrial Standard American               | Platinum | .003911 | 100 Ω                   | A = 3.9692 × 10\ :sup:`–3` B = –5.8495×10:sup:`–7` C = –4.233 ×10\ :sup:`–12` | Low-cost RTD                  |
                +---------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | RTDType.PT3928                  | ITS-90                                        | Platinum | .003928 | 100 Ω                   | A = 3.9888 × 10\ :sup:`–3` B = –5.915×10:sup:`–7` C = –3.85 ×10\ :sup:`–12`   | The definition of temperature |
                +---------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | \*No standard. Check the TCR.   |                                               |          |         |                         |                                                                               |                               |
                +---------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+

            rtd_resistance (float): Specifies the RTD resistance in ohms at 0 °C. NI-DMM uses this value to
                set the RTD Resistance property. The default is 100 (Ω).

        

#### `def configure_thermistor_custom(self, thermistor_a, thermistor_b, thermistor_c)`

configure_thermistor_custom

        Configures the A, B, and C parameters for a custom thermistor.

        Args:
            thermistor_a (float): Specifies the Steinhart-Hart A coefficient for thermistor scaling when
                Thermistor Type is set to Custom in the ConfigureThermistorType
                method. The default is 1.0295e-3 (44006).

                Note:
                One or more of the referenced methods are not in the Python API for this driver.

            thermistor_b (float): Specifies the Steinhart-Hart B coefficient for thermistor scaling when
                Thermistor Type is set to Custom in the ConfigureThermistorType
                method. The default is 2.391e-4 (44006).

                Note:
                One or more of the referenced methods are not in the Python API for this driver.

            thermistor_c (float): Specifies the Steinhart-Hart C coefficient for thermistor scaling when
                Thermistor Type is set to Custom in the ConfigureThermistorType
                method. The default is 1.568e-7 (44006).

                Note:
                One or more of the referenced methods are not in the Python API for this driver.

        

#### `def configure_thermocouple(self, thermocouple_type, reference_junction_type=enums.ThermocoupleReferenceJunctionType.FIXED)`

configure_thermocouple

        Configures the thermocouple type and reference junction type for a
        chosen thermocouple.

        Args:
            thermocouple_type (enums.ThermocoupleType): Specifies the type of thermocouple used to measure the temperature.
                NI-DMM uses this value to set the Thermocouple Type property. The
                default is ThermocoupleType.J.

                +--------------------+---------------------+
                | ThermocoupleType.B | Thermocouple type B |
                +--------------------+---------------------+
                | ThermocoupleType.E | Thermocouple type E |
                +--------------------+---------------------+
                | ThermocoupleType.J | Thermocouple type J |
                +--------------------+---------------------+
                | ThermocoupleType.K | Thermocouple type K |
                +--------------------+---------------------+
                | ThermocoupleType.N | Thermocouple type N |
                +--------------------+---------------------+
                | ThermocoupleType.R | Thermocouple type R |
                +--------------------+---------------------+
                | ThermocoupleType.S | Thermocouple type S |
                +--------------------+---------------------+
                | ThermocoupleType.T | Thermocouple type T |
                +--------------------+---------------------+

            reference_junction_type (enums.ThermocoupleReferenceJunctionType): Specifies the type of reference junction to be used in the reference
                junction compensation of a thermocouple measurement. NI-DMM uses this
                value to set the Reference Junction Type property. The only supported
                value is ThermocoupleReferenceJunctionType.FIXED.

        

#### `def configure_trigger(self, trigger_source, trigger_delay=hightime.timedelta(seconds=-1))`

configure_trigger

        Configures the DMM **Trigger_Source** and **Trigger_Delay**. Refer to
        `Triggering <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__ and `Using
        Switches <REPLACE_DRIVER_SPECIFIC_URL_1(switch_selection)>`__ for more
        information.

        Args:
            trigger_source (enums.TriggerSource): Specifies the **trigger_source** that initiates the acquisition. The
                driver sets trigger_source to this value. Software
                configures the DMM to wait until send_software_trigger is called
                before triggering the DMM.

                Note:
                To determine which values are supported by each device, refer to the
                `LabWindows/CVI Trigger
                Routing <REPLACE_DRIVER_SPECIFIC_URL_1(cvitrigger_routing)>`__ section.

            trigger_delay (hightime.timedelta, datetime.timedelta, or float in seconds): Specifies the time that the DMM waits after it has received a trigger
                before taking a measurement. The driver sets the
                trigger_delay property to this value. By default,
                **trigger_delay** is NIDMM_VAL_AUTO_DELAY (-1), which means the DMM
                waits an appropriate settling time before taking the measurement. On the
                NI 4060, if you set **trigger_delay** to 0, the DMM does not settle
                before taking the measurement. The NI 4065 and NI 4070/4071/4072 use the
                value specified in **trigger_delay** as additional settling time.

                Note:
                When using the NI 4050, **Trigger_Delay** must be set to
                NIDMM_VAL_AUTO_DELAY (-1).

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        

#### `def configure_waveform_acquisition(self, measurement_function, range, rate, waveform_points)`

configure_waveform_acquisition

        Configures the DMM for waveform acquisitions. This feature is supported
        on the NI 4080/4081/4082 and the NI 4070/4071/4072.

        Args:
            measurement_function (enums.Function): Specifies the **measurement_function** used in a waveform acquisition.
                The driver sets method to this value.

                +-----------------------------------+------+------------------+
                | Method.WAVEFORM_VOLTAGE (default) | 1003 | Voltage Waveform |
                +-----------------------------------+------+------------------+
                | Method.WAVEFORM_CURRENT           | 1004 | Current Waveform |
                +-----------------------------------+------+------------------+

            range (float): Specifies the expected maximum amplitude of the input signal and sets
                the **range** for the **Measurement_Function**. NI-DMM sets
                range to this value. **range** values are coerced up to the
                closest input **range**. The default is 10.0.

                For valid ranges refer to the topics in
                `Devices <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__.

                Auto-ranging is not supported during waveform acquisitions.

            rate (float): Specifies the **rate** of the acquisition in samples per second. NI-DMM
                sets waveform_rate to this value.

                The valid **Range** is 10.0–1,800,000 S/s. **rate** values are coerced
                to the closest integer divisor of 1,800,000. The default value is
                1,800,000.

            waveform_points (int): Specifies the number of points to acquire before the waveform
                acquisition completes. NI-DMM sets waveform_points to this
                value.

                To calculate the maximum and minimum number of waveform points that you
                can acquire in one acquisition, refer to the `Waveform Acquisition
                Measurement Cycle <REPLACE_DRIVER_SPECIFIC_URL_1(waveform_cycle)>`__.

                The default value is 500.

        

#### `def disable(self)`

disable

        Places the instrument in a quiescent state where it has minimal or no
        impact on the system to which it is connected. If a measurement is in
        progress when this method is called, the measurement is aborted.
        

#### `def export_attribute_configuration_buffer(self)`

export_attribute_configuration_buffer

        Exports the property configuration of the session to the specified
        configuration buffer.

        You can export and import session property configurations only between
        devices with identical model numbers.

        This method verifies that the properties you have configured for the
        session are valid. If the configuration is invalid, NI‑DMM returns an
        error.

        **Coercion Behavior for Certain Devices**

        Imported and exported property configurations contain coerced values
        for the following NI‑DMM devices:

        -  PXI/PCI/PCIe/USB‑4065
        -  PXI/PCI‑4070
        -  PXI‑4071
        -  PXI‑4072

        NI‑DMM coerces property values when the value you set is within the
        allowed range for the property but is not one of the discrete valid
        values the property supports. For example, for a property that
        coerces values up, if you choose a value of 4 when the adjacent valid
        values are 1 and 10, the property coerces the value to 10.

        **Related Topics:**

        `Using Properties and Properties with
        NI‑DMM <REPLACE_DRIVER_SPECIFIC_URL_1(properties)>`__

        `Setting Properties Before Reading
        Properties <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

        Note: Not supported on the PCMCIA‑4050 or the PXI/PCI‑4060.

        Returns:
            configuration (bytes): Specifies the byte array buffer to be populated with the exported
                property configuration.

        

#### `def export_attribute_configuration_file(self, file_path)`

export_attribute_configuration_file

        Exports the property configuration of the session to the specified
        file.

        You can export and import session property configurations only between
        devices with identical model numbers.

        This method verifies that the properties you have configured for the
        session are valid. If the configuration is invalid, NI‑DMM returns an
        error.

        **Coercion Behavior for Certain Devices**

        Imported and exported property configurations contain coerced values
        for the following NI‑DMM devices:

        -  PXI/PCI/PCIe/USB‑4065
        -  PXI/PCI‑4070
        -  PXI‑4071
        -  PXI‑4072

        NI‑DMM coerces property values when the value you set is within the
        allowed range for the property but is not one of the discrete valid
        values the property supports. For example, for a property that
        coerces values up, if you choose a value of 4 when the adjacent valid
        values are 1 and 10, the property coerces the value to 10.

        **Related Topics:**

        `Using Properties and Properties with
        NI‑DMM <REPLACE_DRIVER_SPECIFIC_URL_1(properties)>`__

        `Setting Properties Before Reading
        Properties <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

        Note: Not supported on the PCMCIA‑4050 or the PXI/PCI‑4060.

        Args:
            file_path (str): Specifies the absolute path to the file to contain the exported
                property configuration. If you specify an empty or relative path, this
                method returns an error.
                **Default file extension:**\  .nidmmconfig

        

#### `def fetch(self, maximum_time=hightime.timedelta(milliseconds=-1))`

fetch

        Returns the value from a previously initiated measurement. You must call
        _initiate before calling this method. Value is in base units.

        Args:
            maximum_time (hightime.timedelta, datetime.timedelta, or int in milliseconds): Specifies the **maximum_time** allowed for this method to complete in
                milliseconds. If the method does not complete within this time
                interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout
                automatically.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        Returns:
            reading (float): The measured value returned from the DMM.

        

#### `def fetch_multi_point(self, array_size, maximum_time=hightime.timedelta(milliseconds=-1))`

fetch_multi_point

        Returns an array of values from a previously initiated multipoint
        measurement. The number of measurements the DMM makes is determined by
        the values you specify for the **Trigger_Count** and **Sample_Count**
        parameters of configure_multi_point. You must first call
        _initiate to initiate a measurement before calling this method. Values are in base units.

        Args:
            array_size (int): Specifies the number of measurements to acquire. The maximum number of
                measurements for a finite acquisition is the (**Trigger Count** x
                **Sample Count**) parameters in configure_multi_point.

                For continuous acquisitions, up to 100,000 points can be returned at
                once. The number of measurements can be a subset. The valid range is any
                positive ViInt32. The default value is 1.

            maximum_time (hightime.timedelta, datetime.timedelta, or int in milliseconds): Specifies the **maximum_time** allowed for this method to complete in
                milliseconds. If the method does not complete within this time
                interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout
                automatically.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        Returns:
            reading_array (array.array("d")): An array of measurement values.

                Note:
                The size of the **Reading_Array** must be at least the size that you
                specify for the **Array_Size** parameter.

        

#### `def fetch_waveform(self, array_size, maximum_time=hightime.timedelta(milliseconds=-1))`

fetch_waveform

        For the NI 4080/4081/4082 and the NI 4070/4071/4072, returns an array of
        values from a previously initiated waveform acquisition. You must call
        _initiate before calling this method.

        Args:
            array_size (int): Specifies the number of waveform points to return. You specify the total
                number of points that the DMM acquires in the **Waveform Points**
                parameter of configure_waveform_acquisition. The default value is
                1.

            maximum_time (hightime.timedelta, datetime.timedelta, or int in milliseconds): Specifies the **maximum_time** allowed for this method to complete in
                milliseconds. If the method does not complete within this time
                interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout
                automatically.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        Returns:
            waveform_array (array.array("d")): **Waveform Array** is an array of measurement values stored in waveform
                data type.

        

#### `def fetch_waveform_into(self, waveform_array, maximum_time=hightime.timedelta(milliseconds=-1))`

fetch_waveform_into

        For the NI 4080/4081/4082 and the NI 4070/4071/4072, returns an array of
        values from a previously initiated waveform acquisition. You must call
        _initiate before calling this method.

        Args:
            waveform_array (numpy.array(dtype=numpy.float64)): **Waveform Array** is an array of measurement values stored in waveform
                data type.

            maximum_time (hightime.timedelta, datetime.timedelta, or int in milliseconds): Specifies the **maximum_time** allowed for this method to complete in
                milliseconds. If the method does not complete within this time
                interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout
                automatically.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        

#### `def _get_cal_date_and_time(self, cal_type)`

_get_cal_date_and_time

        Returns the date and time of the last calibration performed.

        Note: The NI 4050 and NI 4060 are not supported.

        Args:
            cal_type (int): Specifies the type of calibration performed (external or
                self-calibration).

                +-----------------------------------+---+----------------------+
                | NIDMM_VAL_INTERNAL_AREA (default) | 0 | Self-Calibration     |
                +-----------------------------------+---+----------------------+
                | NIDMM_VAL_EXTERNAL_AREA           | 1 | External Calibration |
                +-----------------------------------+---+----------------------+

                Note: The NI 4065 does not support self-calibration.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        Returns:
            month (int): Indicates the **month** of the last calibration.

            day (int): Indicates the **day** of the last calibration.

            year (int): Indicates the **year** of the last calibration.

            hour (int): Indicates the **hour** of the last calibration.

            minute (int): Indicates the **minute** of the last calibration.

        

#### `def get_dev_temp(self, options='')`

get_dev_temp

        Returns the current **Temperature** of the device.

        Note: The NI 4050 and NI 4060 are not supported.

        Args:
            options (str): Reserved.


        Returns:
            temperature (float): Returns the current **temperature** of the device.

        

#### `def get_ext_cal_recommended_interval(self)`

get_ext_cal_recommended_interval

        Returns the recommended interval between external recalibration in
        **Months**.

        Note: The NI 4050 and NI 4060 are not supported.

        Returns:
            months (hightime.timedelta): Returns the recommended number of **months** between external
                calibrations.

        

#### `def get_cal_date_and_time(self, cal_type)`

get_cal_date_and_time

        Returns the date and time of the last calibration performed.

        Note: The NI 4050 and NI 4060 are not supported.

        Args:
            cal_type (int): Specifies the type of calibration performed (external or self-calibration).

                +-----------------------------------+---+----------------------+
                | NIDMM_VAL_INTERNAL_AREA (default) | 0 | Self-Calibration     |
                +-----------------------------------+---+----------------------+
                | NIDMM_VAL_EXTERNAL_AREA           | 1 | External Calibration |
                +-----------------------------------+---+----------------------+

                Note: The NI 4065 does not support self-calibration.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        Returns:
            last_cal_datetime (hightime.datetime): Indicates date and time of the last calibration.

        

#### `def get_last_cal_temp(self, cal_type)`

get_last_cal_temp

        Returns the **Temperature** during the last calibration procedure.

        Note: The NI 4050 and NI 4060 are not supported.

        Args:
            cal_type (int): Specifies the type of calibration performed (external or
                self-calibration).

                +-----------------------------------+---+----------------------+
                | NIDMM_VAL_INTERNAL_AREA (default) | 0 | Self-Calibration     |
                +-----------------------------------+---+----------------------+
                | NIDMM_VAL_EXTERNAL_AREA           | 1 | External Calibration |
                +-----------------------------------+---+----------------------+

                Note: The NI 4065 does not support self-calibration.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        Returns:
            temperature (float): Returns the **temperature** during the last calibration.

        

#### `def get_self_cal_supported(self)`

get_self_cal_supported

        Returns a Boolean value that expresses whether or not the DMM that you
        are using can perform self-calibration.

        Returns:
            self_cal_supported (bool): Returns whether Self Cal is supported for the device specified by the
                given session.

                +-------+---+-------------------------------------------------------------+
                | True  | 1 | The DMM that you are using can perform self-calibration.    |
                +-------+---+-------------------------------------------------------------+
                | False | 0 | The DMM that you are using cannot perform self-calibration. |
                +-------+---+-------------------------------------------------------------+

        

#### `def import_attribute_configuration_buffer(self, configuration)`

import_attribute_configuration_buffer

        Imports a property configuration to the session from the specified
        configuration buffer.

        You can export and import session property configurations only between
        devices with identical model numbers.

        **Coercion Behavior for Certain Devices**

        Imported and exported property configurations contain coerced values
        for the following NI‑DMM devices:

        -  PXI/PCI/PCIe/USB‑4065
        -  PXI/PCI‑4070
        -  PXI‑4071
        -  PXI‑4072

        NI‑DMM coerces property values when the value you set is within the
        allowed range for the property but is not one of the discrete valid
        values the property supports. For example, for a property that
        coerces values up, if you choose a value of 4 when the adjacent valid
        values are 1 and 10, the property coerces the value to 10.

        **Related Topics:**

        `Using Properties and Properties with
        NI‑DMM <REPLACE_DRIVER_SPECIFIC_URL_1(properties)>`__

        `Setting Properties Before Reading
        Properties <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

        Note: Not supported on the PCMCIA‑4050 or the PXI/PCI‑4060.

        Args:
            configuration (bytes): Specifies the byte array buffer that contains the property
                configuration to import.

        

#### `def import_attribute_configuration_file(self, file_path)`

import_attribute_configuration_file

        Imports a property configuration to the session from the specified
        file.

        You can export and import session property configurations only between
        devices with identical model numbers.

        **Coercion Behavior for Certain Devices**

        Imported and exported property configurations contain coerced values
        for the following NI‑DMM devices:

        -  PXI/PCI/PCIe/USB‑4065
        -  PXI/PCI‑4070
        -  PXI‑4071
        -  PXI‑4072

        NI‑DMM coerces property values when the value you set is within the
        allowed range for the property but is not one of the discrete valid
        values the property supports. For example, for a property that
        coerces values up, if you choose a value of 4 when the adjacent valid
        values are 1 and 10, the property coerces the value to 10.

        **Related Topics:**

        `Using Properties and Properties with
        NI‑DMM <REPLACE_DRIVER_SPECIFIC_URL_1(properties)>`__

        `Setting Properties Before Reading
        Properties <javascript:LaunchHelp('DMM.chm::/setting_before_reading_attributes')>`__

        Note: Not supported on the PCMCIA‑4050 or the PXI/PCI‑4060.

        Args:
            file_path (str): Specifies the absolute path to the file containing the property
                configuration to import. If you specify an empty or relative path, this
                method returns an error.
                **Default File Extension:**\  .nidmmconfig

        

#### `def _init_with_options(self, resource_name, id_query=False, reset_device=False, option_string='')`

_init_with_options

        This method completes the following tasks:

        -  Creates a new IVI instrument driver session and, optionally, sets the
           initial state of the following session properties:
           RANGE_CHECK, QUERY_INSTR_STATUS,
           CACHE, simulate,
           RECORD_COERCIONS.
        -  Opens a session to the device you specify for the **Resource_Name**
           parameter. If the **ID_Query** parameter is set to True, this
           method queries the instrument ID and checks that it is valid for
           this instrument driver.
        -  If the **Reset_Device** parameter is set to True, this method
           resets the instrument to a known state. Sends initialization commands
           to set the instrument to the state necessary for the operation of the
           instrument driver.
        -  Returns a ViSession handle that you use to identify the instrument in
           all subsequent instrument driver method calls.

        Note:
        One or more of the referenced properties are not in the Python API for this driver.

        Args:
            resource_name (str): Caution:
                All IVI names for the **Resource_Name**, such as logical names or
                virtual names, are case-sensitive. If you use logical names, driver
                session names, or virtual names in your program, you must make sure that
                the name you use matches the name in the IVI Configuration Store file
                exactly, without any variations in the case of the characters in the
                name.

                | Contains the **resource_name** of the device to initialize. The
                  **resource_name** is assigned in Measurement & Automation Explorer
                  (MAX). Refer to `Related
                  Documentation <REPLACE_DRIVER_SPECIFIC_URL_1(related_documentation)>`__
                  for the *NI Digital Multimeters Getting Started Guide* for more
                  information about configuring and testing the DMM in MAX.
                | Valid Syntax:

                -  NI-DAQmx name
                -  DAQ::NI-DAQmx name[::INSTR]
                -  DAQ::Traditional NI-DAQ device number[::INSTR]
                -  IVI logical name

            id_query (bool): Verifies that the device you initialize is one that the driver supports.
                NI-DMM automatically performs this query, so setting this parameter is
                not necessary.
                Defined Values:

                +----------------+---+------------------+
                | True (default) | 1 | Perform ID Query |
                +----------------+---+------------------+
                | False          | 0 | Skip ID Query    |
                +----------------+---+------------------+

            reset_device (bool): Specifies whether to reset the instrument during the initialization
                procedure.
                Defined Values:

                +----------------+---+--------------+
                | True (default) | 1 | Reset Device |
                +----------------+---+--------------+
                | False          | 0 | Don't Reset  |
                +----------------+---+--------------+

            option_string (dict): | Sets the initial value of certain properties for the session. The
                  following table specifies the property name, property constant, and
                  default value for each property that you can use in this parameter:

                The format of this string is, "AttributeName=Value." To set multiple
                properties, separate their assignments with a comma.

                If you pass NULL or an empty string for this parameter, the session uses
                the default values for the properties. You can override the default
                values by assigning a value explicitly in an **option_string**
                parameter. You do not have to specify all of the properties and may
                leave any of them out (those left out use the default value).

                Refer to `Simulating NI Digital
                Multimeters <REPLACE_DRIVER_SPECIFIC_URL_1(simulation)>`__ for more
                information.

                +------------------+--------------------+-------------------+----+
                | Check            | RANGE_CHECK        | True              | 1  |
                +------------------+--------------------+-------------------+----+
                | QueryInstrStatus | QUERY_INSTR_STATUS | False             | 0  |
                +------------------+--------------------+-------------------+----+
                | Cache            | CACHE              | True              | 1  |
                +------------------+--------------------+-------------------+----+
                | Simulate         | simulate           | False             | 0  |
                +------------------+--------------------+-------------------+----+
                | RecordCoercions  | RECORD_COERCIONS   | False             | 0  |
                +------------------+--------------------+-------------------+----+
                | DriverSetup      | driver_setup       | "" (empty string) | "" |
                +------------------+--------------------+-------------------+----+

                Note:
                One or more of the referenced properties are not in the Python API for this driver.


        Returns:
            vi (int): Returns a ViSession handle that you use to identify the instrument in
                all subsequent instrument driver method calls.

        

#### `def _initiate(self)`

_initiate

        Initiates an acquisition. After you call this method, the DMM leaves
        the Idle state and enters the Wait-for-Trigger state. If trigger is set
        to Immediate mode, the DMM begins acquiring measurement data. Use
        fetch, fetch_multi_point, or fetch_waveform to
        retrieve the measurement data.
        

#### `def perform_open_cable_comp(self)`

perform_open_cable_comp

        For the NI 4082 and NI 4072 only, performs the open cable compensation
        measurements for the current capacitance/inductance range, and returns
        open cable compensation **Conductance** and **Susceptance** values. You
        can use the return values of this method as inputs to
        ConfigureOpenCableCompValues.

        This method returns an error if the value of the method
        property is not set to Method.CAPACITANCE (1005) or
        Method.INDUCTANCE (1006).

        Note:
        One or more of the referenced methods are not in the Python API for this driver.

        Returns:
            conductance (float): **conductance** is the measured value of open cable compensation
                **conductance**.

            susceptance (float): **susceptance** is the measured value of open cable compensation
                **susceptance**.

        

#### `def perform_short_cable_comp(self)`

perform_short_cable_comp

        Performs the short cable compensation measurements for the current
        capacitance/inductance range, and returns short cable compensation
        **Resistance** and **Reactance** values. You can use the return values
        of this method as inputs to ConfigureShortCableCompValues.

        This method returns an error if the value of the method
        property is not set to Method.CAPACITANCE (1005) or
        Method.INDUCTANCE (1006).

        Note:
        One or more of the referenced methods are not in the Python API for this driver.

        Returns:
            resistance (float): **resistance** is the measured value of short cable compensation
                **resistance**.

            reactance (float): **reactance** is the measured value of short cable compensation
                **reactance**.

        

#### `def read(self, maximum_time=hightime.timedelta(milliseconds=-1))`

read

        Acquires a single measurement and returns the measured value in base units.

        Args:
            maximum_time (hightime.timedelta, datetime.timedelta, or int in milliseconds): Specifies the **maximum_time** allowed for this method to complete in
                milliseconds. If the method does not complete within this time
                interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout
                automatically.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        Returns:
            reading (float): The measured value returned from the DMM.

        

#### `def read_multi_point(self, array_size, maximum_time=hightime.timedelta(milliseconds=-1))`

read_multi_point

        Acquires multiple measurements and returns an array of measured values.
        The number of measurements the DMM makes is determined by the values you
        specify for the **Trigger_Count** and **Sample_Count** parameters in
        configure_multi_point.

        Args:
            array_size (int): Specifies the number of measurements to acquire. The maximum number of
                measurements for a finite acquisition is the (**Trigger Count** x
                **Sample Count**) parameters in configure_multi_point.

                For continuous acquisitions, up to 100,000 points can be returned at
                once. The number of measurements can be a subset. The valid range is any
                positive ViInt32. The default value is 1.

            maximum_time (hightime.timedelta, datetime.timedelta, or int in milliseconds): Specifies the **maximum_time** allowed for this method to complete in
                milliseconds. If the method does not complete within this time
                interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout
                automatically.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        Returns:
            reading_array (array.array("d")): An array of measurement values.

                Note:
                The size of the **Reading_Array** must be at least the size that you
                specify for the **Array_Size** parameter.

        

#### `def read_status(self)`

read_status

        Returns measurement backlog and acquisition status. Use this method to
        determine how many measurements are available before calling
        fetch, fetch_multi_point, or fetch_waveform.

        Note: The NI 4050 is not supported.

        Returns:
            acquisition_backlog (int): The number of measurements available to be read. If the backlog
                continues to increase, data is eventually overwritten, resulting in an
                error.

                Note:
                On the NI 4060, the **Backlog** does not increase when autoranging. On
                the NI 4065, the **Backlog** does not increase when Range is set to AUTO
                RANGE ON (-1), or before the first point is fetched when Range is set to
                AUTO RANGE ONCE (-3). These behaviors are due to the autorange model of
                the devices.

            acquisition_status (enums.AcquisitionStatus): Indicates status of the acquisition. The following table shows the
                acquisition states:

                +---+----------------------------+
                | 0 | Running                    |
                +---+----------------------------+
                | 1 | Finished with backlog      |
                +---+----------------------------+
                | 2 | Finished with no backlog   |
                +---+----------------------------+
                | 3 | Paused                     |
                +---+----------------------------+
                | 4 | No acquisition in progress |
                +---+----------------------------+

        

#### `def read_waveform(self, array_size, maximum_time=hightime.timedelta(milliseconds=-1))`

read_waveform

        For the NI 4080/4081/4082 and the NI 4070/4071/4072, acquires a waveform
        and returns data as an array of values or as a waveform data type. The
        number of elements in the **Waveform_Array** is determined by the
        values you specify for the **Waveform_Points** parameter in
        configure_waveform_acquisition.

        Args:
            array_size (int): Specifies the number of waveform points to return. You specify the total
                number of points that the DMM acquires in the **Waveform Points**
                parameter of configure_waveform_acquisition. The default value is
                1.

            maximum_time (hightime.timedelta, datetime.timedelta, or int in milliseconds): Specifies the **maximum_time** allowed for this method to complete in
                milliseconds. If the method does not complete within this time
                interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                NIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout
                automatically.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        Returns:
            waveform_array (array.array("d")): An array of measurement values.

                Note:
                The size of the **Waveform_Array** must be at least the size that you
                specify for the **Array_Size** parameter.

        

#### `def reset_with_defaults(self)`

reset_with_defaults

        Resets the instrument to a known state and sends initialization commands
        to the DMM. The initialization commands set the DMM settings to the
        state necessary for the operation of NI-DMM. All user-defined default
        values associated with a logical name are applied after setting the DMM.
        

#### `def self_cal(self)`

self_cal

        For the NI 4080/4081/4082 and the NI 4070/4071/4072, executes the
        self-calibration routine to maintain measurement accuracy.

        Note:
        This method calls reset, and any configurations previous to
        the call will be lost. All properties will be set to their default
        values after the call returns.
        

#### `def send_software_trigger(self)`

send_software_trigger

        Sends a command to trigger the DMM. Call this method if you have
        configured either the trigger_source or
        sample_trigger properties. If the
        trigger_source and/or sample_trigger
        properties are set to NIDMM_VAL_EXTERNAL or NIDMM_VAL_TTL\ *n*, you
        can use this method to override the trigger source that you configured
        and trigger the device. The NI 4050 and NI 4060 are not supported.

        Note:
        One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
        

#### `def _close(self)`

_close

        Closes the specified session and deallocates resources that it reserved.
        

#### `def self_test(self)`

self_test

        Performs a self-test on the DMM to ensure that the DMM is functioning
        properly. Self-test does not calibrate the DMM. Zero
        indicates success.

        On the NI 4080/4082 and NI 4070/4072, the error code 1013 indicates that
        you should check the fuse and replace it, if necessary.

        Raises `SelfTestError` on self test failure. Properties on exception object:

        - code - failure code from driver
        - message - status message from driver

        Note: Self-test does not check the fuse on the NI 4065, NI 4071, and NI 4081. Hence, even if the fuse is blown on the device, self-test does not return error code 1013.

        Note: This method calls reset, and any configurations previous to the call will be lost. All properties will be set to their default values after the call returns.
        

#### `def reset(self)`

reset

        Resets the instrument to a known state and sends initialization commands
        to the instrument. The initialization commands set instrument settings
        to the state necessary for the operation of the instrument driver.
        

#### `def _self_test(self)`

_self_test

        Performs a self-test on the DMM to ensure that the DMM is functioning
        properly. Self-test does not calibrate the DMM.

        Note:
        This method calls reset, and any configurations previous to
        the call will be lost. All properties will be set to their default
        values after the call returns.

        Returns:
            self_test_result (int): Contains the value returned from the instrument self-test. Zero
                indicates success.

                On the NI 4080/4082 and NI 4070/4072, the error code 1013 indicates that
                you should check the fuse and replace it, if necessary.

                Note:
                Self-test does not check the fuse on the NI 4065, NI 4071, and
                NI 4081. Hence, even if the fuse is blown on the device, self-test does
                not return error code 1013.

            self_test_message (str): This parameter contains the string returned from the instrument
                self-test. The array must contain at least 256 elements.

                For the NI 4050 and NI 4060, the error codes returned for self-test
                failures include the following:

                -  NIDMM_ERROR_AC_TEST_FAILURE
                -  NIDMM_ERROR_DC_TEST_FAILURE
                -  NIDMM_ERROR_RESISTANCE_TEST_FAILURE

                These error codes indicate that the DMM should be repaired.

                For the NI 4080/4081/4082 and the NI 4070/4071/4072, the error code
                returned for a self-test failure is NIDMM_ERROR_SELF_TEST_FAILURE.
                This error code indicates that the DMM should be repaired.

        

<!--NI_PYTHON_API repo=nimi-python path=generated/nidmm/nidmm/unit_tests/_matchers.py -->
## PYTHON MODULE: generated/nidmm/nidmm/unit_tests/_matchers.py

### MODULE DOCSTRING

Matcher classes used by unit tests in order to set mock expectations.
These work well with our visatype definitions.


### `class _ScalarMatcher(object)`

#### `def __init__(self, expected_type, expected_value)`

#### `def __eq__(self, other)`

#### `def __repr__(self)`

### `class _PointerMatcher(object)`

#### `def __init__(self, expected_type)`

#### `def __eq__(self, other)`

#### `def __repr__(self)`

### `class _BufferMatcher(object)`

#### `def __init__(self, expected_element_type, expected_size_or_value)`

#### `def __eq__(self, other)`

#### `def __repr__(self)`

#### `def __str__(self)`

### `class ViStringMatcher(object)`

#### `def __init__(self, expected_string_value)`

#### `def __eq__(self, other)`

#### `def __repr__(self)`

### `def _compare_ctype_structs(expected, actual)`

### `class CustomTypeMatcher(object)`

#### `def __init__(self, expected_type, expected_value)`

#### `def __eq__(self, actual)`

#### `def __repr__(self)`

### `class CustomTypeBufferMatcher(object)`

#### `def __init__(self, expected_element_type, expected_value)`

#### `def __eq__(self, actual)`

#### `def __repr__(self)`

#### `def __str__(self)`

### `class ViBooleanMatcher(_ScalarMatcher)`

#### `def __init__(self, expected_value)`

### `class ViSessionMatcher(_ScalarMatcher)`

#### `def __init__(self, expected_value)`

### `class ViInt16Matcher(_ScalarMatcher)`

#### `def __init__(self, expected_value)`

### `class ViInt32Matcher(_ScalarMatcher)`

#### `def __init__(self, expected_value)`

### `class ViUInt32Matcher(_ScalarMatcher)`

#### `def __init__(self, expected_value)`

### `class ViAttrMatcher(_ScalarMatcher)`

#### `def __init__(self, expected_value)`

### `class ViInt64Matcher(_ScalarMatcher)`

#### `def __init__(self, expected_value)`

### `class ViReal64Matcher(_ScalarMatcher)`

#### `def __init__(self, expected_value)`

### `class ViBooleanPointerMatcher(_PointerMatcher)`

#### `def __init__(self)`

### `class ViSessionPointerMatcher(_PointerMatcher)`

#### `def __init__(self)`

### `class ViInt16PointerMatcher(_PointerMatcher)`

#### `def __init__(self)`

### `class ViInt32PointerMatcher(_PointerMatcher)`

#### `def __init__(self)`

### `class ViInt64PointerMatcher(_PointerMatcher)`

#### `def __init__(self)`

### `class ViReal64PointerMatcher(_PointerMatcher)`

#### `def __init__(self)`

### `class ViBooleanBufferMatcher(_BufferMatcher)`

#### `def __init__(self, expected_size_or_value)`

### `class ViCharBufferMatcher(_BufferMatcher)`

#### `def __init__(self, expected_size_or_value)`

### `class ViInt8BufferMatcher(_BufferMatcher)`

#### `def __init__(self, expected_size_or_value)`

### `class ViInt16BufferMatcher(_BufferMatcher)`

#### `def __init__(self, expected_size_or_value)`

### `class ViInt32BufferMatcher(_BufferMatcher)`

#### `def __init__(self, expected_size_or_value)`

### `class ViInt64BufferMatcher(_BufferMatcher)`

#### `def __init__(self, expected_size_or_value)`

### `class ViReal64BufferMatcher(_BufferMatcher)`

#### `def __init__(self, expected_size_or_value)`

### `class ViSessionBufferMatcher(_BufferMatcher)`

#### `def __init__(self, expected_size_or_value)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nidmm/nidmm/unit_tests/_mock_helper.py -->
## PYTHON MODULE: generated/nidmm/nidmm/unit_tests/_mock_helper.py

### `class MockFunctionCallError(Exception)`

#### `def __init__(self, function, param=None)`

### `class SideEffectsHelper(object)`

#### `def __init__(self)`

#### `def __getitem__(self, func)`

#### `def __setitem__(self, func, val)`

#### `def niDMM_Abort(self, vi)`

#### `def niDMM_ConfigureMeasurementAbsolute(self, vi, measurement_function, range, resolution_absolute)`

#### `def niDMM_ConfigureMeasurementDigits(self, vi, measurement_function, range, resolution_digits)`

#### `def niDMM_ConfigureMultiPoint(self, vi, trigger_count, sample_count, sample_trigger, sample_interval)`

#### `def niDMM_ConfigureRTDCustom(self, vi, rtd_a, rtd_b, rtd_c)`

#### `def niDMM_ConfigureRTDType(self, vi, rtd_type, rtd_resistance)`

#### `def niDMM_ConfigureThermistorCustom(self, vi, thermistor_a, thermistor_b, thermistor_c)`

#### `def niDMM_ConfigureThermocouple(self, vi, thermocouple_type, reference_junction_type)`

#### `def niDMM_ConfigureTrigger(self, vi, trigger_source, trigger_delay)`

#### `def niDMM_ConfigureWaveformAcquisition(self, vi, measurement_function, range, rate, waveform_points)`

#### `def niDMM_Disable(self, vi)`

#### `def niDMM_ExportAttributeConfigurationBuffer(self, vi, size, configuration)`

#### `def niDMM_ExportAttributeConfigurationFile(self, vi, file_path)`

#### `def niDMM_Fetch(self, vi, maximum_time, reading)`

#### `def niDMM_FetchMultiPoint(self, vi, maximum_time, array_size, reading_array, actual_number_of_points)`

#### `def niDMM_FetchWaveform(self, vi, maximum_time, array_size, waveform_array, actual_number_of_points)`

#### `def niDMM_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niDMM_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niDMM_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niDMM_GetAttributeViString(self, vi, channel_name, attribute_id, buffer_size, attribute_value)`

#### `def niDMM_GetCalDateAndTime(self, vi, cal_type, month, day, year, hour, minute)`

#### `def niDMM_GetDevTemp(self, vi, options, temperature)`

#### `def niDMM_GetError(self, vi, error_code, buffer_size, description)`

#### `def niDMM_GetExtCalRecommendedInterval(self, vi, months)`

#### `def niDMM_GetLastCalTemp(self, vi, cal_type, temperature)`

#### `def niDMM_GetSelfCalSupported(self, vi, self_cal_supported)`

#### `def niDMM_ImportAttributeConfigurationBuffer(self, vi, size, configuration)`

#### `def niDMM_ImportAttributeConfigurationFile(self, vi, file_path)`

#### `def niDMM_InitWithOptions(self, resource_name, id_query, reset_device, option_string, vi)`

#### `def niDMM_Initiate(self, vi)`

#### `def niDMM_LockSession(self, vi, caller_has_lock)`

#### `def niDMM_PerformOpenCableComp(self, vi, conductance, susceptance)`

#### `def niDMM_PerformShortCableComp(self, vi, resistance, reactance)`

#### `def niDMM_Read(self, vi, maximum_time, reading)`

#### `def niDMM_ReadMultiPoint(self, vi, maximum_time, array_size, reading_array, actual_number_of_points)`

#### `def niDMM_ReadStatus(self, vi, acquisition_backlog, acquisition_status)`

#### `def niDMM_ReadWaveform(self, vi, maximum_time, array_size, waveform_array, actual_number_of_points)`

#### `def niDMM_ResetWithDefaults(self, vi)`

#### `def niDMM_SelfCal(self, vi)`

#### `def niDMM_SendSoftwareTrigger(self, vi)`

#### `def niDMM_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niDMM_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niDMM_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niDMM_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niDMM_SetRuntimeEnvironment(self, environment, environment_version, reserved1, reserved2)`

#### `def niDMM_UnlockSession(self, vi, caller_has_lock)`

#### `def niDMM_close(self, vi)`

#### `def niDMM_error_message(self, vi, error_code, error_message)`

#### `def niDMM_reset(self, vi)`

#### `def niDMM_self_test(self, vi, self_test_result, self_test_message)`

#### `def set_side_effects_and_return_values(self, mock_library)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nidmm/setup.py -->
## PYTHON MODULE: generated/nidmm/setup.py

### `def read_contents(file_to_read)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nifake/nifake/__init__.py -->
## PYTHON MODULE: generated/nifake/nifake/__init__.py

### `def get_diagnostic_information()`

Get diagnostic information about the system state that is suitable for printing or logging

    returns: dict

    note: Python bitness may be incorrect when running in a virtual environment
    

### `def print_diagnostic_information()`

Print diagnostic information in a format suitable for issue report

    note: Python bitness may be incorrect when running in a virtual environment
    

<!--NI_PYTHON_API repo=nimi-python path=generated/nifake/nifake/_attributes.py -->
## PYTHON MODULE: generated/nifake/nifake/_attributes.py

### `class Attribute(object)`

Base class for all typed attributes.

#### `def __init__(self, attribute_id)`

### `class AttributeViInt32(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeViInt32TimeDeltaMilliseconds(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeViInt32TimeDeltaMonths(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeViInt64(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeViReal64(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeViReal64TimeDeltaSeconds(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeViString(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeViStringRepeatedCapability(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeViStringCommaSeparated(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeViBoolean(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeEnum(Attribute)`

#### `def __init__(self, underlying_attribute_meta_class, enum_meta_class, attribute_id)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeEnumWithConverter(Attribute)`

Class for attributes that use enums internally but are exposed in the nifake Python module as something else, thus need conversion.

#### `def __init__(self, underlying_attribute_enum, getter_converter, setter_converter)`

Creates and returns an instance of AttributeEnumWithConverter attribute meta class.

        Args:
            underlying_attribute_enum (AttributeEnum): The AttributeEnum instance for the underlying
                enum

            getter_converter (function): The function that converts the enum value to its converted
                value

            setter_converter (function): The function that converts the converted value back to the
                enum value
        

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeSessionReference(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nifake/nifake/_complextype.py -->
## PYTHON MODULE: generated/nifake/nifake/_complextype.py

### `class NIComplexNumber(ctypes.Structure)`

### `class NIComplexNumberF32(ctypes.Structure)`

### `class NIComplexI16(ctypes.Structure)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nifake/nifake/_converters.py -->
## PYTHON MODULE: generated/nifake/nifake/_converters.py

### `def _convert_repeated_capabilities(arg, prefix)`

Base version that should not be called

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
    

### `def _(repeated_capability, prefix)`

Integer version

### `def _(repeated_capability, prefix)`

String version (this is the most complex)

    We need to deal with a range ('0-3' or '0:3'), a list ('0,1,2,3') and a single item
    

### `def _(repeated_capability, prefix)`

Iterable version - can handle lists, ranges, and tuples

### `def _(repeated_capability, prefix)`

slice version

### `def convert_repeated_capabilities(repeated_capability, prefix='')`

Convert a repeated capabilities object to a comma delimited list

    Args:
        repeated_capability (str, list, tuple, slice, None) -
        prefix (str) - common prefix for all strings

    Returns:
        rep_cap_list (list of str) - list of each repeated capability item with ranges expanded and prefix added
    

### `def convert_repeated_capabilities_without_prefix(repeated_capability)`

Convert a repeated capabilities object, without any prefix, to a comma delimited list

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
    

### `def expand_channel_string(channel_string, all_channels_in_session)`

Expands a channel_string to a list of individual channel names.

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
    

### `def _convert_timedelta(value, library_type, scaling)`

### `def convert_timedelta_to_seconds_real64(value)`

### `def convert_timedelta_to_milliseconds_int32(value)`

### `def convert_timedeltas_to_seconds_real64(values)`

### `def convert_seconds_real64_to_timedelta(value)`

### `def convert_seconds_real64_to_timedeltas(values)`

### `def convert_month_to_timedelta(months)`

### `def convert_timedelta_to_months_int32(value)`

### `def convert_init_with_options_dictionary(values)`

### `def _convert_to_bytes(value)`

### `def _(value)`

### `def _(value)`

### `def convert_to_bytes(value)`

### `def convert_comma_separated_string_to_list(comma_separated_string)`

### `def convert_list_to_comma_separated_string(list_of_strings)`

Convert a list or tuple of strings into a comma-separated string.

    Args:
        list_of_strings (list or tuple of str): List or tuple of strings.

    Returns:
        str: Comma-separated string.
    

### `def convert_chained_repeated_capability_to_parts(chained_repeated_capability)`

Convert a chained repeated capabilities string to a list of comma-delimited repeated capabilities string.

    Converter assumes that the input contains the full cartesian product of its parts.
    e.g. If chained_repeated_capability is 'site0/PinA,site0/PinB,site1/PinA,site1/PinB',
    ['site0,site1', 'PinA,PinB'] is returned.

    Args:
        chained_repeated_capability (str) - comma-delimited repeated capabilities string where each
        item is a chain of slash-delimited repeated capabilities

    Returns:
        rep_cap_list (list of str) - list of comma-delimited repeated capabilities string
    

### `def convert_double_each_element(numbers)`

### `def convert_from_enum_with_converter_enum(value)`

### `def convert_to_enum_with_converter_enum(value)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nifake/nifake/_grpc_stub_interpreter.py -->
## PYTHON MODULE: generated/nifake/nifake/_grpc_stub_interpreter.py

### `class GrpcStubInterpreter(object)`

Interpreter for interacting with a gRPC Stub class

#### `def __init__(self, grpc_options)`

#### `def set_session_handle(self, value=session_grpc_types.Session())`

#### `def get_session_handle(self)`

#### `def _invoke(self, func, request, metadata=None)`

#### `def abort(self)`

#### `def accept_list_of_durations_in_seconds(self, delays)`

#### `def bool_array_output_function(self, number_of_elements)`

#### `def configure_abc(self)`

#### `def custom_nested_struct_roundtrip(self, nested_custom_type_in)`

#### `def double_all_the_nums(self, numbers)`

#### `def enum_array_output_function(self, number_of_elements)`

#### `def enum_input_function_with_defaults(self, a_turtle)`

#### `def export_attribute_configuration_buffer(self)`

#### `def fetch_waveform(self, number_of_samples)`

#### `def fetch_waveform_into(self, number_of_samples)`

#### `def function_with_3d_numpy_array_of_numpy_complex128_input_parameter(self, multidimensional_array)`

#### `def function_with_intflag_parameter(self, flag)`

#### `def function_with_repeated_capability_type(self, site_list)`

#### `def get_a_boolean(self)`

#### `def get_a_number(self)`

#### `def get_a_string_of_fixed_maximum_size(self)`

#### `def get_a_string_using_python_code(self, a_number)`

#### `def get_an_ivi_dance_char_array(self)`

#### `def get_an_ivi_dance_with_a_twist_string(self)`

#### `def get_array_for_python_code_custom_type(self)`

#### `def get_array_for_python_code_double(self)`

#### `def get_array_size_for_python_code(self)`

#### `def get_array_using_ivi_dance(self)`

#### `def get_attribute_vi_boolean(self, channel_name, attribute_id)`

#### `def get_attribute_vi_int32(self, channel_name, attribute_id)`

#### `def get_attribute_vi_int64(self, channel_name, attribute_id)`

#### `def get_attribute_vi_real64(self, channel_name, attribute_id)`

#### `def get_attribute_vi_string(self, channel_name, attribute_id)`

#### `def get_cal_date_and_time(self, cal_type)`

#### `def get_cal_interval(self)`

#### `def get_channel_names(self, indices)`

#### `def get_custom_type(self)`

#### `def get_custom_type_array(self, number_of_elements)`

#### `def get_custom_type_typedef(self)`

#### `def get_enum_value(self)`

#### `def get_error(self)`

#### `def get_parameter_with_overridden_grpc_name(self, enum_parameter)`

#### `def import_attribute_configuration_buffer(self, configuration)`

#### `def import_attribute_configuration_buffer_ex(self, configuration)`

#### `def init_with_options(self, resource_name, id_query, reset_device, option_string)`

#### `def initiate(self)`

#### `def lock(self)`

#### `def method_using_whole_and_fractional_numbers(self)`

#### `def method_with_grpc_only_param(self, simple_param)`

#### `def method_with_proto_only_parameter(self, attribute_value)`

#### `def mixed_ivi_dance_and_len_mechanism(self, input_values)`

#### `def multiple_array_types(self, output_array_size, input_array_of_floats, input_array_of_integers)`

#### `def multiple_arrays_different_size(self, values_array, data_array)`

#### `def multiple_arrays_same_size(self, values1, values2, values3, values4)`

#### `def one_input_function(self, a_number)`

#### `def parameters_are_multiple_types(self, a_boolean, an_int32, an_int64, an_int_enum, a_float, a_float_enum, a_string)`

#### `def simple_function(self)`

#### `def read(self, maximum_time)`

#### `def read_from_channel(self, channel_name, maximum_time)`

#### `def return_a_number_and_a_string(self)`

#### `def return_duration_in_seconds(self)`

#### `def return_list_of_durations_in_seconds(self, number_of_elements)`

#### `def return_multiple_types(self, array_size)`

#### `def set_attribute_vi_boolean(self, channel_name, attribute_id, attribute_value)`

#### `def set_attribute_vi_int32(self, channel_name, attribute_id, attribute_value)`

#### `def set_attribute_vi_int64(self, channel_name, attribute_id, attribute_value)`

#### `def set_attribute_vi_real64(self, channel_name, attribute_id, attribute_value)`

#### `def set_attribute_vi_string(self, channel_name, attribute_id, attribute_value)`

#### `def set_custom_type(self, cs)`

#### `def set_custom_type_array(self, cs)`

#### `def set_runtime_environment(self, environment, environment_version, reserved1, reserved2)`

#### `def string_valued_enum_input_function_with_defaults(self, a_mobile_os_name)`

#### `def two_input_function(self, a_number, a_string)`

#### `def unlock(self)`

#### `def use64_bit_number(self, input)`

#### `def write_waveform(self, waveform)`

#### `def write_waveform_numpy(self, waveform)`

#### `def write_waveform_numpy_complex128(self, waveform_data_array)`

#### `def write_waveform_numpy_complex64(self, waveform_data_array)`

#### `def write_waveform_numpy_complex_interleaved_i16(self, waveform_data_array)`

#### `def close(self)`

#### `def error_message(self, error_code)`

#### `def self_test(self)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nifake/nifake/_library.py -->
## PYTHON MODULE: generated/nifake/nifake/_library.py

### `class Library(object)`

Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    

#### `def __init__(self, ctypes_library)`

#### `def _get_library_function(self, name)`

#### `def niFake_Abort(self, vi)`

#### `def niFake_AcceptListOfDurationsInSeconds(self, vi, count, delays)`

#### `def niFake_BoolArrayOutputFunction(self, vi, number_of_elements, an_array)`

#### `def niFake_ConfigureABC(self, vi)`

#### `def niFake_CustomNestedStructRoundtrip(self, nested_custom_type_in, nested_custom_type_out)`

#### `def niFake_DoubleAllTheNums(self, vi, number_count, numbers)`

#### `def niFake_EnumArrayOutputFunction(self, vi, number_of_elements, an_array)`

#### `def niFake_EnumInputFunctionWithDefaults(self, vi, a_turtle)`

#### `def niFake_ExportAttributeConfigurationBuffer(self, vi, size_in_bytes, configuration)`

#### `def niFake_FetchWaveform(self, vi, number_of_samples, waveform_data, actual_number_of_samples)`

#### `def niFake_FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter(self, vi, multidimensional_array)`

#### `def niFake_FunctionWithIntflagParameter(self, vi, flag)`

#### `def niFake_FunctionWithRepeatedCapabilityType(self, vi, site_list)`

#### `def niFake_GetABoolean(self, vi, a_boolean)`

#### `def niFake_GetANumber(self, vi, a_number)`

#### `def niFake_GetAStringOfFixedMaximumSize(self, vi, a_string)`

#### `def niFake_GetAStringUsingPythonCode(self, vi, a_number, a_string)`

#### `def niFake_GetAnIviDanceCharArray(self, vi, buffer_size, char_array)`

#### `def niFake_GetAnIviDanceWithATwistString(self, vi, buffer_size, a_string, actual_size)`

#### `def niFake_GetArrayForPythonCodeCustomType(self, vi, number_of_elements, array_out)`

#### `def niFake_GetArrayForPythonCodeDouble(self, vi, number_of_elements, array_out)`

#### `def niFake_GetArraySizeForPythonCode(self, vi, size_out)`

#### `def niFake_GetArrayUsingIviDance(self, vi, array_size, array_out)`

#### `def niFake_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niFake_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niFake_GetAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niFake_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niFake_GetAttributeViString(self, vi, channel_name, attribute_id, buffer_size, attribute_value)`

#### `def niFake_GetCalDateAndTime(self, vi, cal_type, month, day, year, hour, minute)`

#### `def niFake_GetCalInterval(self, vi, months)`

#### `def niFake_GetChannelNames(self, vi, indices, name_size, names)`

#### `def niFake_GetCustomType(self, vi, cs)`

#### `def niFake_GetCustomTypeArray(self, vi, number_of_elements, cs)`

#### `def niFake_GetCustomTypeTypedef(self, vi, cst, csnt)`

#### `def niFake_GetEnumValue(self, vi, a_quantity, a_turtle)`

#### `def niFake_GetError(self, vi, error_code, buffer_size, description)`

#### `def niFake_GetParameterWithOverriddenGrpcName(self, vi, original_parameter, enum_parameter)`

#### `def niFake_ImportAttributeConfigurationBuffer(self, vi, size_in_bytes, configuration)`

#### `def niFake_ImportAttributeConfigurationBufferEx(self, vi, size, configuration)`

#### `def niFake_InitWithOptions(self, resource_name, id_query, reset_device, option_string, vi)`

#### `def niFake_Initiate(self, vi)`

#### `def niFake_LockSession(self, vi, caller_has_lock)`

#### `def niFake_MethodUsingWholeAndFractionalNumbers(self, whole_number, fractional_number)`

#### `def niFake_MethodWithGrpcOnlyParam(self, simple_param)`

#### `def niFake_MethodWithProtoOnlyParameter(self, attribute_value)`

#### `def niFake_MixedIviDanceAndLenMechanism(self, vi, input_values, input_values_size, output_size, output_array)`

#### `def niFake_MultipleArrayTypes(self, vi, output_array_size, output_array, output_array_of_fixed_length, input_array_sizes, input_array_of_floats, input_array_of_integers)`

#### `def niFake_MultipleArraysDifferentSize(self, vi, values_array, values_array_size, data_array, data_array_size)`

#### `def niFake_MultipleArraysSameSize(self, vi, values1, values2, values3, values4, size)`

#### `def niFake_OneInputFunction(self, vi, a_number)`

#### `def niFake_ParametersAreMultipleTypes(self, vi, a_boolean, an_int32, an_int64, an_int_enum, a_float, a_float_enum, a_string)`

#### `def niFake_PoorlyNamedSimpleFunction(self, vi)`

#### `def niFake_Read(self, vi, maximum_time, reading)`

#### `def niFake_ReadFromChannel(self, vi, channel_name, maximum_time, reading)`

#### `def niFake_ReturnANumberAndAString(self, vi, a_number, a_string)`

#### `def niFake_ReturnDurationInSeconds(self, vi, timedelta)`

#### `def niFake_ReturnListOfDurationsInSeconds(self, vi, number_of_elements, timedeltas)`

#### `def niFake_ReturnMultipleTypes(self, vi, a_boolean, an_int32, an_int64, an_int_enum, a_float, a_float_enum, array_size, an_array, string_size, a_string)`

#### `def niFake_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niFake_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niFake_SetAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niFake_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niFake_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niFake_SetCustomType(self, vi, cs)`

#### `def niFake_SetCustomTypeArray(self, vi, number_of_elements, cs)`

#### `def niFake_SetRuntimeEnvironment(self, environment, environment_version, reserved1, reserved2)`

#### `def niFake_StringValuedEnumInputFunctionWithDefaults(self, vi, a_mobile_os_name)`

#### `def niFake_TwoInputFunction(self, vi, a_number, a_string)`

#### `def niFake_UnlockSession(self, vi, caller_has_lock)`

#### `def niFake_Use64BitNumber(self, vi, input, output)`

#### `def niFake_WriteWaveform(self, vi, number_of_samples, waveform)`

#### `def niFake_WriteWaveformNumpyComplex128(self, vi, number_of_samples, waveform_data_array)`

#### `def niFake_WriteWaveformNumpyComplex64(self, vi, number_of_samples, waveform_data_array)`

#### `def niFake_WriteWaveformNumpyComplexInterleavedI16(self, vi, number_of_samples, waveform_data_array)`

#### `def niFake_close(self, vi)`

#### `def niFake_error_message(self, vi, error_code, error_message)`

#### `def niFake_self_test(self, vi, self_test_result, self_test_message)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nifake/nifake/_library_interpreter.py -->
## PYTHON MODULE: generated/nifake/nifake/_library_interpreter.py

### `def _get_ctypes_pointer_for_buffer(value=None, library_type=None, size=None)`

### `def _convert_to_array(value, array_type)`

### `class LibraryInterpreter(object)`

Library C<->Python interpreter.

    This class is responsible for interpreting the Library's C API. It is responsible for:
    * Converting ctypes to native Python types.
    * Dealing with string encoding.
    * Allocating memory.
    * Converting errors returned by Library into Python exceptions.
    

#### `def __init__(self, encoding)`

#### `def set_session_handle(self, value=0)`

#### `def get_session_handle(self)`

#### `def get_error_description(self, error_code)`

get_error_description

        Returns the error description.
        

#### `def abort(self)`

#### `def accept_list_of_durations_in_seconds(self, delays)`

#### `def bool_array_output_function(self, number_of_elements)`

#### `def configure_abc(self)`

#### `def custom_nested_struct_roundtrip(self, nested_custom_type_in)`

#### `def double_all_the_nums(self, numbers)`

#### `def enum_array_output_function(self, number_of_elements)`

#### `def enum_input_function_with_defaults(self, a_turtle)`

#### `def export_attribute_configuration_buffer(self)`

#### `def fetch_waveform(self, number_of_samples)`

#### `def fetch_waveform_into(self, waveform_data)`

#### `def function_with_3d_numpy_array_of_numpy_complex128_input_parameter(self, multidimensional_array)`

#### `def function_with_intflag_parameter(self, flag)`

#### `def function_with_repeated_capability_type(self, site_list)`

#### `def get_a_boolean(self)`

#### `def get_a_number(self)`

#### `def get_a_string_of_fixed_maximum_size(self)`

#### `def get_a_string_using_python_code(self, a_number)`

#### `def get_an_ivi_dance_char_array(self)`

#### `def get_an_ivi_dance_with_a_twist_string(self)`

#### `def get_array_for_python_code_custom_type(self)`

#### `def get_array_for_python_code_double(self)`

#### `def get_array_size_for_python_code(self)`

#### `def get_array_using_ivi_dance(self)`

#### `def get_attribute_vi_boolean(self, channel_name, attribute_id)`

#### `def get_attribute_vi_int32(self, channel_name, attribute_id)`

#### `def get_attribute_vi_int64(self, channel_name, attribute_id)`

#### `def get_attribute_vi_real64(self, channel_name, attribute_id)`

#### `def get_attribute_vi_string(self, channel_name, attribute_id)`

#### `def get_cal_date_and_time(self, cal_type)`

#### `def get_cal_interval(self)`

#### `def get_channel_names(self, indices)`

#### `def get_custom_type(self)`

#### `def get_custom_type_array(self, number_of_elements)`

#### `def get_custom_type_typedef(self)`

#### `def get_enum_value(self)`

#### `def get_error(self)`

#### `def get_parameter_with_overridden_grpc_name(self, enum_parameter)`

#### `def import_attribute_configuration_buffer(self, configuration)`

#### `def import_attribute_configuration_buffer_ex(self, configuration)`

#### `def init_with_options(self, resource_name, id_query, reset_device, option_string)`

#### `def initiate(self)`

#### `def lock(self)`

#### `def method_using_whole_and_fractional_numbers(self)`

#### `def method_with_grpc_only_param(self, simple_param)`

#### `def method_with_proto_only_parameter(self, attribute_value)`

#### `def mixed_ivi_dance_and_len_mechanism(self, input_values)`

#### `def multiple_array_types(self, output_array_size, input_array_of_floats, input_array_of_integers)`

#### `def multiple_arrays_different_size(self, values_array, data_array)`

#### `def multiple_arrays_same_size(self, values1, values2, values3, values4)`

#### `def one_input_function(self, a_number)`

#### `def parameters_are_multiple_types(self, a_boolean, an_int32, an_int64, an_int_enum, a_float, a_float_enum, a_string)`

#### `def simple_function(self)`

#### `def read(self, maximum_time)`

#### `def read_from_channel(self, channel_name, maximum_time)`

#### `def return_a_number_and_a_string(self)`

#### `def return_duration_in_seconds(self)`

#### `def return_list_of_durations_in_seconds(self, number_of_elements)`

#### `def return_multiple_types(self, array_size)`

#### `def set_attribute_vi_boolean(self, channel_name, attribute_id, attribute_value)`

#### `def set_attribute_vi_int32(self, channel_name, attribute_id, attribute_value)`

#### `def set_attribute_vi_int64(self, channel_name, attribute_id, attribute_value)`

#### `def set_attribute_vi_real64(self, channel_name, attribute_id, attribute_value)`

#### `def set_attribute_vi_string(self, channel_name, attribute_id, attribute_value)`

#### `def set_custom_type(self, cs)`

#### `def set_custom_type_array(self, cs)`

#### `def set_runtime_environment(self, environment, environment_version, reserved1, reserved2)`

#### `def string_valued_enum_input_function_with_defaults(self, a_mobile_os_name)`

#### `def two_input_function(self, a_number, a_string)`

#### `def unlock(self)`

#### `def use64_bit_number(self, input)`

#### `def write_waveform(self, waveform)`

#### `def write_waveform_numpy(self, waveform)`

#### `def write_waveform_numpy_complex128(self, waveform_data_array)`

#### `def write_waveform_numpy_complex64(self, waveform_data_array)`

#### `def write_waveform_numpy_complex_interleaved_i16(self, waveform_data_array)`

#### `def close(self)`

#### `def error_message(self, error_code)`

#### `def self_test(self)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nifake/nifake/_library_singleton.py -->
## PYTHON MODULE: generated/nifake/nifake/_library_singleton.py

### `def _get_library_name()`

### `def _get_library_type()`

### `def get()`

get

    Returns the library.Library singleton for nifake.
    

<!--NI_PYTHON_API repo=nimi-python path=generated/nifake/nifake/custom_struct.py -->
## PYTHON MODULE: generated/nifake/nifake/custom_struct.py

### `class struct_CustomStruct(ctypes.Structure)`

#### `def __init__(self, data=None, struct_int=0, struct_double=0.0)`

#### `def __repr__(self)`

#### `def __str__(self)`

### `class CustomStruct()`

#### `def __init__(self, data=None, struct_int=0, struct_double=0.0)`

#### `def _create_copy(self, target_class)`

#### `def __repr__(self)`

#### `def __str__(self)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nifake/nifake/custom_struct_nested_typedef.py -->
## PYTHON MODULE: generated/nifake/nifake/custom_struct_nested_typedef.py

### `class struct_CustomStructNestedTypedef(ctypes.Structure)`

#### `def __init__(self, data=None)`

### `class CustomStructNestedTypedef()`

#### `def __init__(self, data=None, struct_custom_struct=custom_struct.CustomStruct(), struct_custom_struct_typedef=custom_struct_typedef.CustomStructTypedef())`

#### `def _create_copy(self, target_class)`

#### `def __repr__(self)`

#### `def __str__(self)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nifake/nifake/custom_struct_typedef.py -->
## PYTHON MODULE: generated/nifake/nifake/custom_struct_typedef.py

### `class struct_CustomStructTypedef(ctypes.Structure)`

#### `def __init__(self, data=None)`

### `class CustomStructTypedef()`

#### `def __init__(self, data=None, struct_int=0, struct_double=0.0)`

#### `def _create_copy(self, target_class)`

#### `def __repr__(self)`

#### `def __str__(self)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nifake/nifake/enums.py -->
## PYTHON MODULE: generated/nifake/nifake/enums.py

### `class Color(Enum)`

### `class EnumWithConverter(Enum)`

### `class FloatEnum(Enum)`

### `class IntFlagEnum(IntFlag)`

### `class MobileOSNames(Enum)`

### `class Turtle(Enum)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nifake/nifake/errors.py -->
## PYTHON MODULE: generated/nifake/nifake/errors.py

### `def _is_success(code)`

### `def _is_error(code)`

### `def _is_warning(code)`

### `class Error(Exception)`

Base error class for NI-FAKE

#### `def __init__(self, message)`

### `class DriverError(Error)`

An error originating from the NI-FAKE driver

#### `def __init__(self, code, description)`

### `class DriverWarning(Warning)`

A warning originating from the NI-FAKE driver

#### `def __init__(self, code, description)`

### `class RpcError(Error)`

An error specific to sessions to the NI gRPC Device Server

#### `def __init__(self, rpc_code, description)`

### `class UnsupportedConfigurationError(Error)`

An error due to using this module in an usupported platform.

#### `def __init__(self)`

### `class DriverNotInstalledError(Error)`

An error due to using this module without the driver runtime installed.

#### `def __init__(self)`

### `class DriverTooOldError(Error)`

An error due to using this module with an older version of the NI-FAKE driver runtime.

#### `def __init__(self)`

### `class DriverTooNewError(Error)`

An error due to the NI-FAKE driver runtime being too new for this module.

#### `def __init__(self)`

### `class InvalidRepeatedCapabilityError(Error)`

An error due to an invalid character in a repeated capability

#### `def __init__(self, invalid_character, invalid_string)`

### `class SelfTestError(Error)`

An error due to a failed self-test

#### `def __init__(self, code, msg)`

### `def handle_error(library_interpreter, code, ignore_warnings, is_error_handling)`

handle_error

    Helper function for handling errors returned by nifake.Library.
    It calls back into the LibraryInterpreter to get the corresponding error
    description and raises if necessary.
    

<!--NI_PYTHON_API repo=nimi-python path=generated/nifake/nifake/grpc_session_options.py -->
## PYTHON MODULE: generated/nifake/nifake/grpc_session_options.py

- `GRPC_SERVICE_INTERFACE_NAME = 'nifake_grpc.NiFake'`

- `MEASUREMENTLINK_23Q1_NIMI_PYTHON_API_KEY = 'DE10751B-3EE0-44EC-A93B-800E6A3C89E4'`

### `class SessionInitializationBehavior(IntEnum)`

### `class GrpcSessionOptions(object)`

Collection of options that specifies session behaviors related to gRPC.

#### `def __init__(self, grpc_channel, session_name, *, api_key=MEASUREMENTLINK_23Q1_NIMI_PYTHON_API_KEY, initialization_behavior=SessionInitializationBehavior.AUTO)`

Collection of options that specifies session behaviors related to gRPC.

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
        

<!--NI_PYTHON_API repo=nimi-python path=generated/nifake/nifake/nidevice_pb2.py -->
## PYTHON MODULE: generated/nifake/nifake/nidevice_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0enidevice.proto\x12\rnidevice_grpc"2\n\x0fNIComplexNumber\x12\x0c\n\x04real\x18\x01 \x01(\x01\x12\x11\n\timaginary\x18\x02 \x01(\x01"5\n\x12NIComplexNumberF32\x12\x0c\n\x04real\x18\x01 \x01(\x02\x12\x11\n\timaginary\x18\x02 \x01(\x02"/\n\x0cNIComplexI16\x12\x0c\n\x04real\x18\x01 \x01(\x11\x12\x11\n\timaginary\x18\x02 \x01(\x11"r\n\x0fSmtSpectrumInfo\x12\x15\n\rspectrum_type\x18\x01 \x01(\r\x12\x11\n\tlinear_db\x18\x02 \x01(\r\x12\x0e\n\x06window\x18\x03 \x01(\r\x12\x13\n\x0bwindow_size\x18\x04 \x01(\x11\x12\x10\n\x08fft_size\x18\x05 \x01(\x11BB\n\x12com.ni.grpc.deviceB\x08NiDeviceP\x01\xaa\x02\x1fNationalInstruments.Grpc.Deviceb\x06proto3')`

<!--NI_PYTHON_API repo=nimi-python path=generated/nifake/nifake/nidevice_pb2_grpc.py -->
## PYTHON MODULE: generated/nifake/nifake/nidevice_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

<!--NI_PYTHON_API repo=nimi-python path=generated/nifake/nifake/nifake_pb2.py -->
## PYTHON MODULE: generated/nifake/nifake/nifake_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cnifake.proto\x12\x0bnifake_grpc\x1a\rsession.proto"=\n\x10FakeCustomStruct\x12\x12\n\nstruct_int\x18\x01 \x01(\x11\x12\x15\n\rstruct_double\x18\x02 \x01(\x01"\xa0\x01\n\x19CustomStructNestedTypedef\x12;\n\x14struct_custom_struct\x18\x01 \x01(\x0b2\x1d.nifake_grpc.FakeCustomStruct\x12F\n\x1cstruct_custom_struct_typedef\x18\x02 \x01(\x0b2 .nifake_grpc.CustomStructTypedef"@\n\x13CustomStructTypedef\x12\x12\n\nstruct_int\x18\x01 \x01(\x11\x12\x15\n\rstruct_double\x18\x02 \x01(\x01"6\n\x13NIComplexI16_struct\x12\x0c\n\x04real\x18\x01 \x01(\x11\x12\x11\n\timaginary\x18\x02 \x01(\x11"9\n\x16NIComplexNumber_struct\x12\x0c\n\x04real\x18\x01 \x01(\x01\x12\x11\n\timaginary\x18\x02 \x01(\x01"<\n\x19NIComplexNumberF32_struct\x12\x0c\n\x04real\x18\x01 \x01(\x02\x12\x11\n\timaginary\x18\x02 \x01(\x02"J\n\x0fStringAndTurtle\x12\x12\n\nstring_arg\x18\x01 \x01(\t\x12#\n\x06turtle\x18\x02 \x01(\x0e2\x13.nifake_grpc.Turtle"%\n\x0fCustomNamedType\x12\x12\n\nstring_arg\x18\x01 \x01(\t"2\n\x0cAbortRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\x1f\n\rAbortResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"`\n\x1eBoolArrayOutputFunctionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12number_of_elements\x18\x02 \x01(\x11"C\n\x1fBoolArrayOutputFunctionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x10\n\x08an_array\x18\x02 \x03(\x08"2\n\x0cCloseRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\x1f\n\rCloseResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"`\n\x1eEnumArrayOutputFunctionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12number_of_elements\x18\x02 \x01(\x11"n\n\x1fEnumArrayOutputFunctionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12%\n\x08an_array\x18\x02 \x03(\x0e2\x13.nifake_grpc.Turtle\x12\x14\n\x0can_array_raw\x18\x03 \x03(\x11"\x9c\x01\n$EnumInputFunctionWithDefaultsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\'\n\x08a_turtle\x18\x02 \x01(\x0e2\x13.nifake_grpc.TurtleH\x00\x12\x16\n\x0ca_turtle_raw\x18\x03 \x01(\x11H\x00B\x0f\n\ra_turtle_enum"7\n%EnumInputFunctionWithDefaultsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xce\x01\n0StringValuedEnumInputFunctionWithDefaultsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12=\n\x17a_mobile_os_name_mapped\x18\x02 \x01(\x0e2\x1a.nifake_grpc.MobileOSNamesH\x00\x12\x1e\n\x14a_mobile_os_name_raw\x18\x03 \x01(\tH\x00B\x17\n\x15a_mobile_os_name_enum"C\n1StringValuedEnumInputFunctionWithDefaultsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"M\n\x13ErrorMessageRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x12\n\nerror_code\x18\x02 \x01(\x11"=\n\x14ErrorMessageResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rerror_message\x18\x02 \x01(\t"U\n\x14FetchWaveformRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x19\n\x11number_of_samples\x18\x02 \x01(\x11"`\n\x15FetchWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rwaveform_data\x18\x02 \x03(\x01\x12 \n\x18actual_number_of_samples\x18\x03 \x01(\x11"8\n\x12GetABooleanRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"8\n\x13GetABooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x11\n\ta_boolean\x18\x02 \x01(\x08"7\n\x11GetANumberRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"6\n\x12GetANumberResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x10\n\x08a_number\x18\x02 \x01(\x11"I\n#GetAStringOfFixedMaximumSizeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"H\n$GetAStringOfFixedMaximumSizeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x10\n\x08a_string\x18\x02 \x01(\t"C\n\x1dGetAnIviDanceCharArrayRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"D\n\x1eGetAnIviDanceCharArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nchar_array\x18\x02 \x01(\t"B\n\x1cGetArrayUsingIviDanceRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"B\n\x1dGetArrayUsingIviDanceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x11\n\tarray_out\x18\x02 \x03(\x01"\x8c\x01\n\x1cGetAttributeViBooleanRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nifake_grpc.NiFakeAttribute"H\n\x1dGetAttributeViBooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fattribute_value\x18\x02 \x01(\x08"\x8a\x01\n\x1aGetAttributeViInt32Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nifake_grpc.NiFakeAttribute"F\n\x1bGetAttributeViInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fattribute_value\x18\x02 \x01(\x11"\x8a\x01\n\x1aGetAttributeViInt64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nifake_grpc.NiFakeAttribute"F\n\x1bGetAttributeViInt64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fattribute_value\x18\x02 \x01(\x03"\x8b\x01\n\x1bGetAttributeViReal64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nifake_grpc.NiFakeAttribute"G\n\x1cGetAttributeViReal64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fattribute_value\x18\x02 \x01(\x01"\x8c\x01\n\x1cGetAttributeViSessionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nifake_grpc.NiFakeAttribute"`\n\x1dGetAttributeViSessionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12/\n\x0fattribute_value\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session"\x8b\x01\n\x1bGetAttributeViStringRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nifake_grpc.NiFakeAttribute"G\n\x1cGetAttributeViStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fattribute_value\x18\x02 \x01(\t"P\n\x18GetCalDateAndTimeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x10\n\x08cal_type\x18\x02 \x01(\x11"s\n\x19GetCalDateAndTimeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05month\x18\x02 \x01(\x11\x12\x0b\n\x03day\x18\x03 \x01(\x11\x12\x0c\n\x04year\x18\x04 \x01(\x11\x12\x0c\n\x04hour\x18\x05 \x01(\x11\x12\x0e\n\x06minute\x18\x06 \x01(\x11";\n\x15GetCalIntervalRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"8\n\x16GetCalIntervalResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0e\n\x06months\x18\x02 \x01(\x11"9\n\x13GetEnumValueRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"w\n\x14GetEnumValueResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\na_quantity\x18\x02 \x01(\x11\x12%\n\x08a_turtle\x18\x03 \x01(\x0e2\x13.nifake_grpc.Turtle\x12\x14\n\x0ca_turtle_raw\x18\x04 \x01(\x11"5\n\x0fGetErrorRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"K\n\x10GetErrorResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nerror_code\x18\x02 \x01(\x11\x12\x13\n\x0bdescription\x18\x03 \x01(\t"\xd3\x01\n\x16InitWithOptionsRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\x10\n\x08id_query\x18\x03 \x01(\x08\x12\x14\n\x0creset_device\x18\x04 \x01(\x08\x12\x15\n\roption_string\x18\x05 \x01(\t\x12M\n\x17initialization_behavior\x18\x06 \x01(\x0e2,.nidevice_grpc.SessionInitializationBehavior"n\n\x17InitWithOptionsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12"\n\x02vi\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1f\n\x17new_session_initialized\x18\x03 \x01(\x08"\x9a\x01\n\x19MultipleArrayTypesRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x19\n\x11output_array_size\x18\x02 \x01(\x11\x12\x1d\n\x15input_array_of_floats\x18\x03 \x03(\x01\x12\x1f\n\x17input_array_of_integers\x18\x04 \x03(\x11"h\n\x1aMultipleArrayTypesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x14\n\x0coutput_array\x18\x02 \x03(\x01\x12$\n\x1coutput_array_of_fixed_length\x18\x03 \x03(\x01"\x87\x01\n\x1dMultipleArraysSameSizeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07values1\x18\x02 \x03(\x01\x12\x0f\n\x07values2\x18\x03 \x03(\x01\x12\x0f\n\x07values3\x18\x04 \x03(\x01\x12\x0f\n\x07values4\x18\x05 \x03(\x01"0\n\x1eMultipleArraysSameSizeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"r\n"MultipleArraysDifferentSizeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cvalues_array\x18\x02 \x03(\x01\x12\x12\n\ndata_array\x18\x03 \x03(\x11"5\n#MultipleArraysDifferentSizeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"_\n#MixedIviDanceAndLenMechanismRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cinput_values\x18\x02 \x03(\x01"L\n$MixedIviDanceAndLenMechanismResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x14\n\x0coutput_array\x18\x02 \x03(\x11"O\n\x17OneInputFunctionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x10\n\x08a_number\x18\x02 \x01(\x11"*\n\x18OneInputFunctionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xe4\x02\n!ParametersAreMultipleTypesRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\ta_boolean\x18\x02 \x01(\x08\x12\x10\n\x08an_int32\x18\x03 \x01(\x11\x12\x10\n\x08an_int64\x18\x04 \x01(\x03\x12*\n\x0ban_int_enum\x18\x05 \x01(\x0e2\x13.nifake_grpc.TurtleH\x00\x12\x19\n\x0fan_int_enum_raw\x18\x06 \x01(\x11H\x00\x12\x0f\n\x07a_float\x18\x07 \x01(\x01\x125\n\x13a_float_enum_mapped\x18\x08 \x01(\x0e2\x16.nifake_grpc.FloatEnumH\x01\x12\x1a\n\x10a_float_enum_raw\x18\t \x01(\x01H\x01\x12\x10\n\x08a_string\x18\n \x01(\tB\x12\n\x10an_int_enum_enumB\x13\n\x11a_float_enum_enum"4\n"ParametersAreMultipleTypesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"F\n PoorlyNamedSimpleFunctionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"3\n!PoorlyNamedSimpleFunctionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"G\n\x0bReadRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cmaximum_time\x18\x02 \x01(\x01"/\n\x0cReadResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07reading\x18\x02 \x01(\x01"h\n\x16ReadFromChannelRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x14\n\x0cmaximum_time\x18\x03 \x01(\x11":\n\x17ReadFromChannelResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07reading\x18\x02 \x01(\x01"D\n\x1eReturnANumberAndAStringRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"U\n\x1fReturnANumberAndAStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x10\n\x08a_number\x18\x02 \x01(\x11\x12\x10\n\x08a_string\x18\x03 \x01(\t"T\n\x1aReturnMultipleTypesRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x12\n\narray_size\x18\x02 \x01(\x11"\xab\x02\n\x1bReturnMultipleTypesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x11\n\ta_boolean\x18\x02 \x01(\x08\x12\x10\n\x08an_int32\x18\x03 \x01(\x11\x12\x10\n\x08an_int64\x18\x04 \x01(\x03\x12(\n\x0ban_int_enum\x18\x05 \x01(\x0e2\x13.nifake_grpc.Turtle\x12\x17\n\x0fan_int_enum_raw\x18\x06 \x01(\x11\x12\x0f\n\x07a_float\x18\x07 \x01(\x01\x123\n\x13a_float_enum_mapped\x18\x08 \x01(\x0e2\x16.nifake_grpc.FloatEnum\x12\x18\n\x10a_float_enum_raw\x18\t \x01(\x01\x12\x10\n\x08an_array\x18\n \x03(\x01\x12\x10\n\x08a_string\x18\x0b \x01(\t"\xa5\x01\n\x1cSetAttributeViBooleanRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nifake_grpc.NiFakeAttribute\x12\x17\n\x0fattribute_value\x18\x04 \x01(\x08"/\n\x1dSetAttributeViBooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x85\x02\n\x1aSetAttributeViInt32Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nifake_grpc.NiFakeAttribute\x12B\n\x0fattribute_value\x18\x04 \x01(\x0e2\'.nifake_grpc.NiFakeInt32AttributeValuesH\x00\x12\x1d\n\x13attribute_value_raw\x18\x05 \x01(\x11H\x00B\x16\n\x14attribute_value_enum"-\n\x1bSetAttributeViInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa7\x01\n\x1aSetAttributeViInt64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nifake_grpc.NiFakeAttribute\x12\x1b\n\x13attribute_value_raw\x18\x04 \x01(\x03"-\n\x1bSetAttributeViInt64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xd9\x02\n\x1bSetAttributeViReal64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nifake_grpc.NiFakeAttribute\x12C\n\x0fattribute_value\x18\x04 \x01(\x0e2(.nifake_grpc.NiFakeReal64AttributeValuesH\x00\x12P\n\x16attribute_value_mapped\x18\x05 \x01(\x0e2..nifake_grpc.NiFakeReal64AttributeValuesMappedH\x00\x12\x1d\n\x13attribute_value_raw\x18\x06 \x01(\x01H\x00B\x16\n\x14attribute_value_enum".\n\x1cSetAttributeViReal64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa8\x01\n\x1bSetAttributeViStringRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nifake_grpc.NiFakeAttribute\x12\x1b\n\x13attribute_value_raw\x18\x04 \x01(\t".\n\x1cSetAttributeViStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"a\n\x17TwoInputFunctionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x10\n\x08a_number\x18\x02 \x01(\x01\x12\x10\n\x08a_string\x18\x03 \x01(\t"*\n\x18TwoInputFunctionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"J\n\x15Use64BitNumberRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\r\n\x05input\x18\x02 \x01(\x03"8\n\x16Use64BitNumberResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0e\n\x06output\x18\x02 \x01(\x03"L\n\x14WriteWaveformRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x10\n\x08waveform\x18\x02 \x03(\x01"\'\n\x15WriteWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x8b\x01\n#WriteWaveformNumpyComplex128Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12@\n\x13waveform_data_array\x18\x02 \x03(\x0b2#.nifake_grpc.NIComplexNumber_struct"6\n$WriteWaveformNumpyComplex128Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x8d\x01\n"WriteWaveformNumpyComplex64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12C\n\x13waveform_data_array\x18\x02 \x03(\x0b2&.nifake_grpc.NIComplexNumberF32_struct"5\n#WriteWaveformNumpyComplex64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x93\x01\n.WriteWaveformNumpyComplexInterleavedI16Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12=\n\x13waveform_data_array\x18\x02 \x03(\x0b2 .nifake_grpc.NIComplexI16_struct"A\n/WriteWaveformNumpyComplexInterleavedI16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"e\n\x14SetCustomTypeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12)\n\x02cs\x18\x02 \x01(\x0b2\x1d.nifake_grpc.FakeCustomStruct"\'\n\x15SetCustomTypeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"j\n\x19SetCustomTypeArrayRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12)\n\x02cs\x18\x02 \x03(\x0b2\x1d.nifake_grpc.FakeCustomStruct",\n\x1aSetCustomTypeArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05":\n\x14GetCustomTypeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"R\n\x15GetCustomTypeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12)\n\x02cs\x18\x02 \x01(\x0b2\x1d.nifake_grpc.FakeCustomStruct"[\n\x19GetCustomTypeArrayRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12number_of_elements\x18\x02 \x01(\x11"W\n\x1aGetCustomTypeArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12)\n\x02cs\x18\x02 \x03(\x0b2\x1d.nifake_grpc.FakeCustomStruct"[\n#GetAnIviDanceWithATwistArrayRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x10\n\x08a_string\x18\x02 \x01(\t"^\n$GetAnIviDanceWithATwistArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x11\n\tarray_out\x18\x02 \x03(\x11\x12\x13\n\x0bactual_size\x18\x03 \x01(\x11"J\n$GetAnIviDanceWithATwistStringRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"^\n%GetAnIviDanceWithATwistStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x10\n\x08a_string\x18\x02 \x01(\t\x12\x13\n\x0bactual_size\x18\x03 \x01(\x11"N\n\x17DoubleAllTheNumsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07numbers\x18\x02 \x03(\x01"*\n\x18DoubleAllTheNumsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"[\n%AcceptListOfDurationsInSecondsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0e\n\x06delays\x18\x02 \x03(\x01"8\n&AcceptListOfDurationsInSecondsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"D\n\x1eReturnDurationInSecondsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"D\n\x1fReturnDurationInSecondsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x11\n\ttimedelta\x18\x02 \x01(\x01"g\n%ReturnListOfDurationsInSecondsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12number_of_elements\x18\x02 \x01(\x11"L\n&ReturnListOfDurationsInSecondsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\ntimedeltas\x18\x02 \x03(\x01"9\n\x13ConfigureAbcRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"&\n\x14ConfigureAbcResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x8d\x02\n\x15ConfigureEnumsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x120\n\x0csample_count\x18\x02 \x01(\x0e2\x18.nifake_grpc.SampleCountH\x00\x12\x1a\n\x10sample_count_raw\x18\x03 \x01(\x11H\x00\x126\n\x0fsample_interval\x18\x04 \x01(\x0e2\x1b.nifake_grpc.SampleIntervalH\x01\x12\x1d\n\x13sample_interval_raw\x18\x05 \x01(\x01H\x01B\x13\n\x11sample_count_enumB\x16\n\x14sample_interval_enum"(\n\x16ConfigureEnumsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"Q\n+ExportAttributeConfigurationBufferExRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"U\n,ExportAttributeConfigurationBufferExResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rconfiguration\x18\x02 \x01(\x0c"h\n+ImportAttributeConfigurationBufferExRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rconfiguration\x18\x02 \x01(\x0c">\n,ImportAttributeConfigurationBufferExResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"x\n\x1aFetchWithCustomSizeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1b\n\x13number_of_waveforms\x18\x02 \x01(\x11\x12\x19\n\x11number_of_samples\x18\x03 \x01(\x11"D\n\x1bFetchWithCustomSizeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rwaveform_data\x18\x02 \x03(\x01"\xbf\x01\n)GetParameterWithOverriddenGrpcNameRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x121\n\x12enum_parameter_raw\x18\x02 \x01(\x0e2\x13.nifake_grpc.TurtleH\x00\x12 \n\x16enum_parameter_raw_raw\x18\x03 \x01(\x11H\x00B\x19\n\x17enum_parameter_raw_enum"Z\n*GetParameterWithOverriddenGrpcNameResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1c\n\x14overridden_parameter\x18\x02 \x01(\x11"`\n:IviDanceWithTwistWithMultipleArraysAndOneBufferSizeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\x9a\x01\n;IviDanceWithTwistWithMultipleArraysAndOneBufferSizeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0e\n\x06array1\x18\x02 \x03(\x11\x12\x0e\n\x06array2\x18\x03 \x03(\x11\x12\x0e\n\x06array3\x18\x04 \x03(\x11\x12\x1b\n\x13actual_num_elements\x18\x05 \x01(\x11"M\n\'FunctionWithOverriddenGrpcName2xRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session":\n(FunctionWithOverriddenGrpcName2xResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa9\x01\n>FunctionWith3dNumpyArrayOfNumpyComplex128InputParameterRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12C\n\x16multidimensional_array\x18\x02 \x03(\x0b2#.nifake_grpc.NIComplexNumber_struct"Q\n?FunctionWith3dNumpyArrayOfNumpyComplex128InputParameterResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"c\n&StringValuedEnumNoEnumGeneratedRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\ra_string_enum\x18\x02 \x01(\t"9\n\'StringValuedEnumNoEnumGeneratedResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"P\n*IviDanceWithATwistCalculatedSizeOutRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\x8e\x01\n+IviDanceWithATwistCalculatedSizeOutResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04data\x18\x02 \x03(\r\x12\x1c\n\x14actual_num_waveforms\x18\x03 \x01(\x11\x12#\n\x1bactual_samples_per_waveform\x18\x04 \x01(\x11"f\n)ImportAttributeConfigurationBufferRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rconfiguration\x18\x02 \x01(\x0c"<\n*ImportAttributeConfigurationBufferResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"O\n)ExportAttributeConfigurationBufferRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"S\n*ExportAttributeConfigurationBufferResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rconfiguration\x18\x02 \x01(\x0c"B\n\x12Control4022Request\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x15\n\rconfiguration\x18\x02 \x01(\x11"%\n\x13Control4022Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"c\n\x1bAcceptViSessionArrayRequest\x12\x15\n\rsession_count\x18\x01 \x01(\r\x12-\n\rsession_array\x18\x02 \x03(\x0b2\x16.nidevice_grpc.Session".\n\x1cAcceptViSessionArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"W\n\x1aAcceptViUInt32ArrayRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\ru_int32_array\x18\x02 \x03(\r"-\n\x1bAcceptViUInt32ArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"q\n\x1dBoolArrayInputFunctionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12number_of_elements\x18\x02 \x01(\x11\x12\x10\n\x08an_array\x18\x03 \x03(\x08"0\n\x1eBoolArrayInputFunctionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"H\n\x12CloseExtCalRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0e\n\x06action\x18\x02 \x01(\x11"%\n\x13CloseExtCalResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"E\n\x1fCommandWithReservedParamRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"2\n CommandWithReservedParamResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"Z\n\x1eCreateConfigurationListRequest\x128\n\x12list_attribute_ids\x18\x01 \x03(\x0e2\x1c.nifake_grpc.NiFakeAttribute"1\n\x1fCreateConfigurationListResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"k\n"CustomNestedStructRoundtripRequest\x12E\n\x15nested_custom_type_in\x18\x01 \x01(\x0b2&.nifake_grpc.CustomStructNestedTypedef"}\n#CustomNestedStructRoundtripResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12F\n\x16nested_custom_type_out\x18\x02 \x01(\x0b2&.nifake_grpc.CustomStructNestedTypedef"\x1f\n\x1dGetBitfieldAsEnumArrayRequest"o\n\x1eGetBitfieldAsEnumArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12*\n\x0bflags_array\x18\x02 \x03(\x0e2\x15.nifake_grpc.Bitfield\x12\x11\n\tflags_raw\x18\x03 \x01(\x03"U\n/GetAnIviDanceWithATwistArrayOfCustomTypeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\x89\x01\n0GetAnIviDanceWithATwistArrayOfCustomTypeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x120\n\tarray_out\x18\x02 \x03(\x0b2\x1d.nifake_grpc.FakeCustomStruct\x12\x13\n\x0bactual_size\x18\x03 \x01(\x11"D\n1GetAnIviDanceWithATwistArrayWithInputArrayRequest\x12\x0f\n\x07data_in\x18\x01 \x03(\x11"l\n2GetAnIviDanceWithATwistArrayWithInputArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x11\n\tarray_out\x18\x02 \x03(\x11\x12\x13\n\x0bactual_size\x18\x03 \x01(\x11")\n\'GetAnIviDanceWithATwistByteArrayRequest"b\n(GetAnIviDanceWithATwistByteArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x11\n\tarray_out\x18\x02 \x01(\x0c\x12\x13\n\x0bactual_size\x18\x03 \x01(\x11"/\n-GetAnIviDanceWithATwistStringStrlenBugRequest"i\n.GetAnIviDanceWithATwistStringStrlenBugResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nstring_out\x18\x02 \x01(\t\x12\x13\n\x0bactual_size\x18\x03 \x01(\x11"F\n GetArraySizeForCustomCodeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"E\n!GetArraySizeForCustomCodeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x10\n\x08size_out\x18\x02 \x01(\x11"W\n\x1eGetArrayViUInt8WithEnumRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tarray_len\x18\x02 \x01(\x11"\x8b\x01\n\x1fGetArrayViUInt8WithEnumResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x129\n\x11u_int8_enum_array\x18\x02 \x03(\x0e2\x1e.nifake_grpc.GrpcColorOverride\x12\x1d\n\x15u_int8_enum_array_raw\x18\x03 \x01(\x0c"7\n\x11GetViUInt8Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"<\n\x12GetViUInt8Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x16\n\x0ea_uint8_number\x18\x02 \x01(\r"O\n\x16GetViInt32ArrayRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tarray_len\x18\x02 \x01(\x11">\n\x17GetViInt32ArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0bint32_array\x18\x02 \x03(\x11"P\n\x17GetViUInt32ArrayRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tarray_len\x18\x02 \x01(\x11"A\n\x18GetViUInt32ArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\ru_int32_array\x18\x02 \x03(\r"\x92\x01\n(MethodUsingEnumWithGrpcNameValuesRequest\x129\n\nusing_enum\x18\x01 \x01(\x0e2#.nifake_grpc.EnumWithGrpcNameValuesH\x00\x12\x18\n\x0eusing_enum_raw\x18\x02 \x01(\x11H\x00B\x11\n\x0fusing_enum_enum";\n)MethodUsingEnumWithGrpcNameValuesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"$\n"MethodWithGetLastErrorParamRequest"M\n#MethodWithGetLastErrorParamResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x16\n\nlast_error\x18\x02 \x01(\tB\x02\x18\x01"6\n\x1eMethodWithGrpcOnlyParamRequest\x12\x14\n\x0csimple_param\x18\x01 \x01(\x11"J\n\x1fMethodWithGrpcOnlyParamResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fgrpc_only_param\x18\x02 \x01(\x11"-\n+MethodUsingWholeAndFractionalNumbersRequest"\xf1\x01\n,MethodUsingWholeAndFractionalNumbersResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x125\n\x0cwhole_number\x18\x02 \x01(\x0e2\x1f.nifake_grpc.DecimalWholeNumber\x12\x18\n\x10whole_number_raw\x18\x03 \x01(\x11\x12A\n\x18fractional_number_mapped\x18\x04 \x01(\x0e2\x1f.nifake_grpc.DecimalMixedNumber\x12\x1d\n\x15fractional_number_raw\x18\x05 \x01(\x01"&\n$MethodUsingWholeMappedNumbersRequest"\x95\x01\n%MethodUsingWholeMappedNumbersResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12B\n\x13whole_number_mapped\x18\x02 \x01(\x0e2%.nifake_grpc.DecimalWholeNumberMapped\x12\x18\n\x10whole_number_raw\x18\x03 \x01(\x01";\n MethodWithGrpcFieldNumberRequest\x12\x17\n\x0fattribute_value\x18\x05 \x01(\x11"3\n!MethodWithGrpcFieldNumberResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05">\n#MethodWithProtoOnlyParameterRequest\x12\x17\n\x0fattribute_value\x18\x01 \x01(\x11"6\n$MethodWithProtoOnlyParameterResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05""\n ReadDataWithInOutIviTwistRequest"V\n!ReadDataWithInOutIviTwistResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04data\x18\x02 \x03(\x11\x12\x13\n\x0bbuffer_size\x18\x03 \x01(\x11".\n,ReadDataWithMultipleIviTwistParamSetsRequest"\x9b\x01\n-ReadDataWithMultipleIviTwistParamSetsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x11\n\tarray_out\x18\x02 \x03(\x11\x12\x13\n\x0bactual_size\x18\x03 \x01(\x11\x12\x17\n\x0fother_array_out\x18\x04 \x03(\x11\x12\x19\n\x11other_actual_size\x18\x05 \x01(\x11"^\n\x11InitExtCalRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\x1c\n\x14calibration_password\x18\x03 \x01(\t"H\n\x12InitExtCalResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12"\n\x02vi\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session"|\n\x16InitWithVarArgsRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x125\n\x0fname_and_turtle\x18\x03 \x03(\x0b2\x1c.nifake_grpc.StringAndTurtle"M\n\x17InitWithVarArgsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12"\n\x02vi\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session"\xc3\x01\n)MultipleArraysSameSizeWithOptionalRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07values1\x18\x02 \x03(\x01\x12\x0f\n\x07values2\x18\x03 \x03(\x01\x12\x0f\n\x07values3\x18\x04 \x03(\x01\x12\x0f\n\x07values4\x18\x05 \x03(\x01\x12.\n\x07values5\x18\x06 \x03(\x0b2\x1d.nifake_grpc.FakeCustomStruct"<\n*MultipleArraysSameSizeWithOptionalResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"l\n UseATwoDimensionParameterRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\r\n\x05array\x18\x02 \x03(\x11\x12\x15\n\rarray_lengths\x18\x03 \x03(\x11"3\n!UseATwoDimensionParameterResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"t\n ViUInt8ArrayInputFunctionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12number_of_elements\x18\x02 \x01(\x11\x12\x10\n\x08an_array\x18\x03 \x01(\x0c"3\n!ViUInt8ArrayInputFunctionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"c\n!ViUInt8ArrayOutputFunctionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12number_of_elements\x18\x02 \x01(\x11"F\n"ViUInt8ArrayOutputFunctionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x10\n\x08an_array\x18\x02 \x01(\x0c"X\n ViInt16ArrayInputFunctionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x10\n\x08an_array\x18\x02 \x03(\x11"3\n!ViInt16ArrayInputFunctionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05*\x9e\x05\n\x0fNiFakeAttribute\x12 \n\x1cNIFAKE_ATTRIBUTE_UNSPECIFIED\x10\x00\x12&\n NIFAKE_ATTRIBUTE_READ_WRITE_BOOL\x10\xc0\x84=\x12(\n"NIFAKE_ATTRIBUTE_READ_WRITE_DOUBLE\x10\xc1\x84=\x12(\n"NIFAKE_ATTRIBUTE_READ_WRITE_STRING\x10\xc2\x84=\x12\'\n!NIFAKE_ATTRIBUTE_READ_WRITE_COLOR\x10\xc3\x84=\x12)\n#NIFAKE_ATTRIBUTE_READ_WRITE_INTEGER\x10\xc4\x84=\x12/\n)NIFAKE_ATTRIBUTE_FLOAT_ENUM_NAME_OVERRIDE\x10\xc5\x84=\x12\'\n!NIFAKE_ATTRIBUTE_READ_WRITE_INT64\x10\xc6\x84=\x127\n1NIFAKE_ATTRIBUTE_READ_WRITE_DOUBLE_WITH_CONVERTER\x10\xc7\x84=\x128\n2NIFAKE_ATTRIBUTE_READ_WRITE_INTEGER_WITH_CONVERTER\x10\xc8\x84=\x12A\n;NIFAKE_ATTRIBUTE_READ_WRITE_DOUBLE_WITH_REPEATED_CAPABILITY\x10\xc9\x84=\x12<\n6NIFAKE_ATTRIBUTE_READ_WRITE_STRING_REPEATED_CAPABILITY\x10\xca\x84=\x12#\n\x1dNIFAKE_ATTRIBUTE_SAMPLE_COUNT\x10\xcc\x84=\x12&\n NIFAKE_ATTRIBUTE_SAMPLE_INTERVAL\x10\xcd\x84=*\xb2\x01\n\x11GrpcColorOverride\x12#\n\x1fGRPC_COLOR_OVERRIDE_UNSPECIFIED\x10\x00\x12\x1b\n\x17GRPC_COLOR_OVERRIDE_RED\x10\x01\x12\x1c\n\x18GRPC_COLOR_OVERRIDE_BLUE\x10\x02\x12\x1e\n\x1aGRPC_COLOR_OVERRIDE_YELLOW\x10\x05\x12\x1d\n\x19GRPC_COLOR_OVERRIDE_BLACK\x10**\xc8\x01\n\tFloatEnum\x12\x1a\n\x16FLOAT_ENUM_UNSPECIFIED\x10\x00\x12\x1f\n\x1bFLOAT_ENUM_THREE_POINT_FIVE\x10\x01\x12\x1e\n\x1aFLOAT_ENUM_FOUR_POINT_FIVE\x10\x02\x12\x1e\n\x1aFLOAT_ENUM_FIVE_POINT_FIVE\x10\x03\x12\x1d\n\x19FLOAT_ENUM_SIX_POINT_FIVE\x10\x04\x12\x1f\n\x1bFLOAT_ENUM_SEVEN_POINT_FIVE\x10\x05*`\n\x06Turtle\x12\x13\n\x0fTURTLE_LEONARDO\x10\x00\x12\x14\n\x10TURTLE_DONATELLO\x10\x01\x12\x12\n\x0eTURTLE_RAPHAEL\x10\x02\x12\x17\n\x13TURTLE_MICHELANGELO\x10\x03*\x80\x01\n\rMobileOSNames\x12\x1f\n\x1bMOBILE_OS_NAMES_UNSPECIFIED\x10\x00\x12\x1b\n\x17MOBILE_OS_NAMES_ANDROID\x10\x01\x12\x17\n\x13MOBILE_OS_NAMES_IOS\x10\x02\x12\x18\n\x14MOBILE_OS_NAMES_NONE\x10\x03*x\n\x08Bitfield\x12\x18\n\x14BITFIELD_UNSPECIFIED\x10\x00\x12\x13\n\x0fBITFIELD_FLAG_A\x10\x01\x12\x13\n\x0fBITFIELD_FLAG_B\x10\x02\x12\x13\n\x0fBITFIELD_FLAG_C\x10\x04\x12\x13\n\x0fBITFIELD_FLAG_D\x10\x08*\x88\x01\n\x12DecimalWholeNumber\x12\x1d\n\x19DECIMAL_WHOLE_NUMBER_ZERO\x10\x00\x12.\n!DECIMAL_WHOLE_NUMBER_NEGATIVE_ONE\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12#\n\x1fDECIMAL_WHOLE_NUMBER_TWENTY_TWO\x10\x16*\xc7\x01\n\x18DecimalWholeNumberMapped\x12+\n\'DECIMAL_WHOLE_NUMBER_MAPPED_UNSPECIFIED\x10\x00\x12$\n DECIMAL_WHOLE_NUMBER_MAPPED_ZERO\x10\x01\x12,\n(DECIMAL_WHOLE_NUMBER_MAPPED_NEGATIVE_ONE\x10\x02\x12*\n&DECIMAL_WHOLE_NUMBER_MAPPED_TWENTY_TWO\x10\x03*\xd7\x02\n\x12DecimalMixedNumber\x12$\n DECIMAL_MIXED_NUMBER_UNSPECIFIED\x10\x00\x12#\n\x1fDECIMAL_MIXED_NUMBER_TWENTY_TWO\x10\x01\x12&\n"DECIMAL_MIXED_NUMBER_TWO_POINT_TWO\x10\x02\x12\'\n#DECIMAL_MIXED_NUMBER_NEGATIVE_THREE\x10\x03\x12#\n\x1fDECIMAL_MIXED_NUMBER_MAX_INT_32\x10\x04\x12,\n(DECIMAL_MIXED_NUMBER_MAX_INT_32_PLUS_ONE\x10\x05\x12#\n\x1fDECIMAL_MIXED_NUMBER_MIN_INT_32\x10\x06\x12-\n)DECIMAL_MIXED_NUMBER_MIN_INT_32_MINUS_ONE\x10\x07*\x9e\x01\n\x16EnumWithGrpcNameValues\x12*\n&ENUM_WITH_GRPC_NAME_VALUES_UNSPECIFIED\x10\x00\x124\n0ENUM_WITH_GRPC_NAME_VALUES_ALTERED_GRPC_NAME_ONE\x10\x01\x12"\n\x1eENUM_WITH_GRPC_NAME_VALUES_TWO\x10\x02*5\n\x0bSampleCount\x12&\n"SAMPLE_COUNT_SAMPLE_COUNT_INFINITE\x10\x00*Z\n\x0eSampleInterval\x12\x1f\n\x1bSAMPLE_INTERVAL_UNSPECIFIED\x10\x00\x12\'\n\x1aSAMPLE_INTERVAL_AUTO_DELAY\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01*\xa1\x02\n\x1aNiFakeInt32AttributeValues\x12\x1c\n\x18NIFAKE_INT32_UNSPECIFIED\x10\x00\x12(\n$NIFAKE_INT32_GRPC_COLOR_OVERRIDE_RED\x10\x01\x12)\n%NIFAKE_INT32_GRPC_COLOR_OVERRIDE_BLUE\x10\x02\x12+\n\'NIFAKE_INT32_GRPC_COLOR_OVERRIDE_YELLOW\x10\x05\x12*\n&NIFAKE_INT32_GRPC_COLOR_OVERRIDE_BLACK\x10*\x123\n/NIFAKE_INT32_SAMPLE_COUNT_SAMPLE_COUNT_INFINITE\x10\x00\x1a\x02\x10\x01*s\n\x1bNiFakeReal64AttributeValues\x12\x1d\n\x19NIFAKE_REAL64_UNSPECIFIED\x10\x00\x125\n(NIFAKE_REAL64_SAMPLE_INTERVAL_AUTO_DELAY\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01*\xb0\x02\n!NiFakeReal64AttributeValuesMapped\x12$\n NIFAKE_REAL64_MAPPED_UNSPECIFIED\x10\x00\x12-\n)NIFAKE_REAL64_FLOAT_ENUM_THREE_POINT_FIVE\x10\x01\x12,\n(NIFAKE_REAL64_FLOAT_ENUM_FOUR_POINT_FIVE\x10\x02\x12,\n(NIFAKE_REAL64_FLOAT_ENUM_FIVE_POINT_FIVE\x10\x03\x12+\n\'NIFAKE_REAL64_FLOAT_ENUM_SIX_POINT_FIVE\x10\x04\x12-\n)NIFAKE_REAL64_FLOAT_ENUM_SEVEN_POINT_FIVE\x10\x052\xad_\n\x06NiFake\x12>\n\x05Abort\x12\x19.nifake_grpc.AbortRequest\x1a\x1a.nifake_grpc.AbortResponse\x12t\n\x17BoolArrayOutputFunction\x12+.nifake_grpc.BoolArrayOutputFunctionRequest\x1a,.nifake_grpc.BoolArrayOutputFunctionResponse\x12>\n\x05Close\x12\x19.nifake_grpc.CloseRequest\x1a\x1a.nifake_grpc.CloseResponse\x12t\n\x17EnumArrayOutputFunction\x12+.nifake_grpc.EnumArrayOutputFunctionRequest\x1a,.nifake_grpc.EnumArrayOutputFunctionResponse\x12\x86\x01\n\x1dEnumInputFunctionWithDefaults\x121.nifake_grpc.EnumInputFunctionWithDefaultsRequest\x1a2.nifake_grpc.EnumInputFunctionWithDefaultsResponse\x12\xaa\x01\n)StringValuedEnumInputFunctionWithDefaults\x12=.nifake_grpc.StringValuedEnumInputFunctionWithDefaultsRequest\x1a>.nifake_grpc.StringValuedEnumInputFunctionWithDefaultsResponse\x12S\n\x0cErrorMessage\x12 .nifake_grpc.ErrorMessageRequest\x1a!.nifake_grpc.ErrorMessageResponse\x12V\n\rFetchWaveform\x12!.nifake_grpc.FetchWaveformRequest\x1a".nifake_grpc.FetchWaveformResponse\x12P\n\x0bGetABoolean\x12\x1f.nifake_grpc.GetABooleanRequest\x1a .nifake_grpc.GetABooleanResponse\x12M\n\nGetANumber\x12\x1e.nifake_grpc.GetANumberRequest\x1a\x1f.nifake_grpc.GetANumberResponse\x12\x83\x01\n\x1cGetAStringOfFixedMaximumSize\x120.nifake_grpc.GetAStringOfFixedMaximumSizeRequest\x1a1.nifake_grpc.GetAStringOfFixedMaximumSizeResponse\x12q\n\x16GetAnIviDanceCharArray\x12*.nifake_grpc.GetAnIviDanceCharArrayRequest\x1a+.nifake_grpc.GetAnIviDanceCharArrayResponse\x12n\n\x15GetArrayUsingIviDance\x12).nifake_grpc.GetArrayUsingIviDanceRequest\x1a*.nifake_grpc.GetArrayUsingIviDanceResponse\x12n\n\x15GetAttributeViBoolean\x12).nifake_grpc.GetAttributeViBooleanRequest\x1a*.nifake_grpc.GetAttributeViBooleanResponse\x12h\n\x13GetAttributeViInt32\x12\'.nifake_grpc.GetAttributeViInt32Request\x1a(.nifake_grpc.GetAttributeViInt32Response\x12h\n\x13GetAttributeViInt64\x12\'.nifake_grpc.GetAttributeViInt64Request\x1a(.nifake_grpc.GetAttributeViInt64Response\x12k\n\x14GetAttributeViReal64\x12(.nifake_grpc.GetAttributeViReal64Request\x1a).nifake_grpc.GetAttributeViReal64Response\x12n\n\x15GetAttributeViSession\x12).nifake_grpc.GetAttributeViSessionRequest\x1a*.nifake_grpc.GetAttributeViSessionResponse\x12k\n\x14GetAttributeViString\x12(.nifake_grpc.GetAttributeViStringRequest\x1a).nifake_grpc.GetAttributeViStringResponse\x12b\n\x11GetCalDateAndTime\x12%.nifake_grpc.GetCalDateAndTimeRequest\x1a&.nifake_grpc.GetCalDateAndTimeResponse\x12Y\n\x0eGetCalInterval\x12".nifake_grpc.GetCalIntervalRequest\x1a#.nifake_grpc.GetCalIntervalResponse\x12S\n\x0cGetEnumValue\x12 .nifake_grpc.GetEnumValueRequest\x1a!.nifake_grpc.GetEnumValueResponse\x12G\n\x08GetError\x12\x1c.nifake_grpc.GetErrorRequest\x1a\x1d.nifake_grpc.GetErrorResponse\x12\\\n\x0fInitWithOptions\x12#.nifake_grpc.InitWithOptionsRequest\x1a$.nifake_grpc.InitWithOptionsResponse\x12e\n\x12MultipleArrayTypes\x12&.nifake_grpc.MultipleArrayTypesRequest\x1a\'.nifake_grpc.MultipleArrayTypesResponse\x12q\n\x16MultipleArraysSameSize\x12*.nifake_grpc.MultipleArraysSameSizeRequest\x1a+.nifake_grpc.MultipleArraysSameSizeResponse\x12\x80\x01\n\x1bMultipleArraysDifferentSize\x12/.nifake_grpc.MultipleArraysDifferentSizeRequest\x1a0.nifake_grpc.MultipleArraysDifferentSizeResponse\x12\x83\x01\n\x1cMixedIviDanceAndLenMechanism\x120.nifake_grpc.MixedIviDanceAndLenMechanismRequest\x1a1.nifake_grpc.MixedIviDanceAndLenMechanismResponse\x12_\n\x10OneInputFunction\x12$.nifake_grpc.OneInputFunctionRequest\x1a%.nifake_grpc.OneInputFunctionResponse\x12}\n\x1aParametersAreMultipleTypes\x12..nifake_grpc.ParametersAreMultipleTypesRequest\x1a/.nifake_grpc.ParametersAreMultipleTypesResponse\x12z\n\x19PoorlyNamedSimpleFunction\x12-.nifake_grpc.PoorlyNamedSimpleFunctionRequest\x1a..nifake_grpc.PoorlyNamedSimpleFunctionResponse\x12;\n\x04Read\x12\x18.nifake_grpc.ReadRequest\x1a\x19.nifake_grpc.ReadResponse\x12\\\n\x0fReadFromChannel\x12#.nifake_grpc.ReadFromChannelRequest\x1a$.nifake_grpc.ReadFromChannelResponse\x12t\n\x17ReturnANumberAndAString\x12+.nifake_grpc.ReturnANumberAndAStringRequest\x1a,.nifake_grpc.ReturnANumberAndAStringResponse\x12h\n\x13ReturnMultipleTypes\x12\'.nifake_grpc.ReturnMultipleTypesRequest\x1a(.nifake_grpc.ReturnMultipleTypesResponse\x12n\n\x15SetAttributeViBoolean\x12).nifake_grpc.SetAttributeViBooleanRequest\x1a*.nifake_grpc.SetAttributeViBooleanResponse\x12h\n\x13SetAttributeViInt32\x12\'.nifake_grpc.SetAttributeViInt32Request\x1a(.nifake_grpc.SetAttributeViInt32Response\x12h\n\x13SetAttributeViInt64\x12\'.nifake_grpc.SetAttributeViInt64Request\x1a(.nifake_grpc.SetAttributeViInt64Response\x12k\n\x14SetAttributeViReal64\x12(.nifake_grpc.SetAttributeViReal64Request\x1a).nifake_grpc.SetAttributeViReal64Response\x12k\n\x14SetAttributeViString\x12(.nifake_grpc.SetAttributeViStringRequest\x1a).nifake_grpc.SetAttributeViStringResponse\x12_\n\x10TwoInputFunction\x12$.nifake_grpc.TwoInputFunctionRequest\x1a%.nifake_grpc.TwoInputFunctionResponse\x12Y\n\x0eUse64BitNumber\x12".nifake_grpc.Use64BitNumberRequest\x1a#.nifake_grpc.Use64BitNumberResponse\x12V\n\rWriteWaveform\x12!.nifake_grpc.WriteWaveformRequest\x1a".nifake_grpc.WriteWaveformResponse\x12\x83\x01\n\x1cWriteWaveformNumpyComplex128\x120.nifake_grpc.WriteWaveformNumpyComplex128Request\x1a1.nifake_grpc.WriteWaveformNumpyComplex128Response\x12\x80\x01\n\x1bWriteWaveformNumpyComplex64\x12/.nifake_grpc.WriteWaveformNumpyComplex64Request\x1a0.nifake_grpc.WriteWaveformNumpyComplex64Response\x12\xa4\x01\n\'WriteWaveformNumpyComplexInterleavedI16\x12;.nifake_grpc.WriteWaveformNumpyComplexInterleavedI16Request\x1a<.nifake_grpc.WriteWaveformNumpyComplexInterleavedI16Response\x12V\n\rSetCustomType\x12!.nifake_grpc.SetCustomTypeRequest\x1a".nifake_grpc.SetCustomTypeResponse\x12e\n\x12SetCustomTypeArray\x12&.nifake_grpc.SetCustomTypeArrayRequest\x1a\'.nifake_grpc.SetCustomTypeArrayResponse\x12V\n\rGetCustomType\x12!.nifake_grpc.GetCustomTypeRequest\x1a".nifake_grpc.GetCustomTypeResponse\x12e\n\x12GetCustomTypeArray\x12&.nifake_grpc.GetCustomTypeArrayRequest\x1a\'.nifake_grpc.GetCustomTypeArrayResponse\x12\x83\x01\n\x1cGetAnIviDanceWithATwistArray\x120.nifake_grpc.GetAnIviDanceWithATwistArrayRequest\x1a1.nifake_grpc.GetAnIviDanceWithATwistArrayResponse\x12\x86\x01\n\x1dGetAnIviDanceWithATwistString\x121.nifake_grpc.GetAnIviDanceWithATwistStringRequest\x1a2.nifake_grpc.GetAnIviDanceWithATwistStringResponse\x12_\n\x10DoubleAllTheNums\x12$.nifake_grpc.DoubleAllTheNumsRequest\x1a%.nifake_grpc.DoubleAllTheNumsResponse\x12\x89\x01\n\x1eAcceptListOfDurationsInSeconds\x122.nifake_grpc.AcceptListOfDurationsInSecondsRequest\x1a3.nifake_grpc.AcceptListOfDurationsInSecondsResponse\x12t\n\x17ReturnDurationInSeconds\x12+.nifake_grpc.ReturnDurationInSecondsRequest\x1a,.nifake_grpc.ReturnDurationInSecondsResponse\x12\x89\x01\n\x1eReturnListOfDurationsInSeconds\x122.nifake_grpc.ReturnListOfDurationsInSecondsRequest\x1a3.nifake_grpc.ReturnListOfDurationsInSecondsResponse\x12S\n\x0cConfigureAbc\x12 .nifake_grpc.ConfigureAbcRequest\x1a!.nifake_grpc.ConfigureAbcResponse\x12Y\n\x0eConfigureEnums\x12".nifake_grpc.ConfigureEnumsRequest\x1a#.nifake_grpc.ConfigureEnumsResponse\x12\x9b\x01\n$ExportAttributeConfigurationBufferEx\x128.nifake_grpc.ExportAttributeConfigurationBufferExRequest\x1a9.nifake_grpc.ExportAttributeConfigurationBufferExResponse\x12\x9b\x01\n$ImportAttributeConfigurationBufferEx\x128.nifake_grpc.ImportAttributeConfigurationBufferExRequest\x1a9.nifake_grpc.ImportAttributeConfigurationBufferExResponse\x12h\n\x13FetchWithCustomSize\x12\'.nifake_grpc.FetchWithCustomSizeRequest\x1a(.nifake_grpc.FetchWithCustomSizeResponse\x12\x95\x01\n"GetParameterWithOverriddenGrpcName\x126.nifake_grpc.GetParameterWithOverriddenGrpcNameRequest\x1a7.nifake_grpc.GetParameterWithOverriddenGrpcNameResponse\x12\xc8\x01\n3IviDanceWithTwistWithMultipleArraysAndOneBufferSize\x12G.nifake_grpc.IviDanceWithTwistWithMultipleArraysAndOneBufferSizeRequest\x1aH.nifake_grpc.IviDanceWithTwistWithMultipleArraysAndOneBufferSizeResponse\x12\x8f\x01\n FunctionWithOverriddenGrpcName2x\x124.nifake_grpc.FunctionWithOverriddenGrpcName2xRequest\x1a5.nifake_grpc.FunctionWithOverriddenGrpcName2xResponse\x12\xd4\x01\n7FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter\x12K.nifake_grpc.FunctionWith3dNumpyArrayOfNumpyComplex128InputParameterRequest\x1aL.nifake_grpc.FunctionWith3dNumpyArrayOfNumpyComplex128InputParameterResponse\x12\x8c\x01\n\x1fStringValuedEnumNoEnumGenerated\x123.nifake_grpc.StringValuedEnumNoEnumGeneratedRequest\x1a4.nifake_grpc.StringValuedEnumNoEnumGeneratedResponse\x12\x98\x01\n#IviDanceWithATwistCalculatedSizeOut\x127.nifake_grpc.IviDanceWithATwistCalculatedSizeOutRequest\x1a8.nifake_grpc.IviDanceWithATwistCalculatedSizeOutResponse\x12\x95\x01\n"ImportAttributeConfigurationBuffer\x126.nifake_grpc.ImportAttributeConfigurationBufferRequest\x1a7.nifake_grpc.ImportAttributeConfigurationBufferResponse\x12\x95\x01\n"ExportAttributeConfigurationBuffer\x126.nifake_grpc.ExportAttributeConfigurationBufferRequest\x1a7.nifake_grpc.ExportAttributeConfigurationBufferResponse\x12P\n\x0bControl4022\x12\x1f.nifake_grpc.Control4022Request\x1a .nifake_grpc.Control4022Response\x12k\n\x14AcceptViSessionArray\x12(.nifake_grpc.AcceptViSessionArrayRequest\x1a).nifake_grpc.AcceptViSessionArrayResponse\x12h\n\x13AcceptViUInt32Array\x12\'.nifake_grpc.AcceptViUInt32ArrayRequest\x1a(.nifake_grpc.AcceptViUInt32ArrayResponse\x12q\n\x16BoolArrayInputFunction\x12*.nifake_grpc.BoolArrayInputFunctionRequest\x1a+.nifake_grpc.BoolArrayInputFunctionResponse\x12P\n\x0bCloseExtCal\x12\x1f.nifake_grpc.CloseExtCalRequest\x1a .nifake_grpc.CloseExtCalResponse\x12w\n\x18CommandWithReservedParam\x12,.nifake_grpc.CommandWithReservedParamRequest\x1a-.nifake_grpc.CommandWithReservedParamResponse\x12t\n\x17CreateConfigurationList\x12+.nifake_grpc.CreateConfigurationListRequest\x1a,.nifake_grpc.CreateConfigurationListResponse\x12\x80\x01\n\x1bCustomNestedStructRoundtrip\x12/.nifake_grpc.CustomNestedStructRoundtripRequest\x1a0.nifake_grpc.CustomNestedStructRoundtripResponse\x12q\n\x16GetBitfieldAsEnumArray\x12*.nifake_grpc.GetBitfieldAsEnumArrayRequest\x1a+.nifake_grpc.GetBitfieldAsEnumArrayResponse\x12\xa7\x01\n(GetAnIviDanceWithATwistArrayOfCustomType\x12<.nifake_grpc.GetAnIviDanceWithATwistArrayOfCustomTypeRequest\x1a=.nifake_grpc.GetAnIviDanceWithATwistArrayOfCustomTypeResponse\x12\xad\x01\n*GetAnIviDanceWithATwistArrayWithInputArray\x12>.nifake_grpc.GetAnIviDanceWithATwistArrayWithInputArrayRequest\x1a?.nifake_grpc.GetAnIviDanceWithATwistArrayWithInputArrayResponse\x12\x8f\x01\n GetAnIviDanceWithATwistByteArray\x124.nifake_grpc.GetAnIviDanceWithATwistByteArrayRequest\x1a5.nifake_grpc.GetAnIviDanceWithATwistByteArrayResponse\x12\xa1\x01\n&GetAnIviDanceWithATwistStringStrlenBug\x12:.nifake_grpc.GetAnIviDanceWithATwistStringStrlenBugRequest\x1a;.nifake_grpc.GetAnIviDanceWithATwistStringStrlenBugResponse\x12z\n\x19GetArraySizeForCustomCode\x12-.nifake_grpc.GetArraySizeForCustomCodeRequest\x1a..nifake_grpc.GetArraySizeForCustomCodeResponse\x12t\n\x17GetArrayViUInt8WithEnum\x12+.nifake_grpc.GetArrayViUInt8WithEnumRequest\x1a,.nifake_grpc.GetArrayViUInt8WithEnumResponse\x12M\n\nGetViUInt8\x12\x1e.nifake_grpc.GetViUInt8Request\x1a\x1f.nifake_grpc.GetViUInt8Response\x12\\\n\x0fGetViInt32Array\x12#.nifake_grpc.GetViInt32ArrayRequest\x1a$.nifake_grpc.GetViInt32ArrayResponse\x12_\n\x10GetViUInt32Array\x12$.nifake_grpc.GetViUInt32ArrayRequest\x1a%.nifake_grpc.GetViUInt32ArrayResponse\x12\x92\x01\n!MethodUsingEnumWithGrpcNameValues\x125.nifake_grpc.MethodUsingEnumWithGrpcNameValuesRequest\x1a6.nifake_grpc.MethodUsingEnumWithGrpcNameValuesResponse\x12\x80\x01\n\x1bMethodWithGetLastErrorParam\x12/.nifake_grpc.MethodWithGetLastErrorParamRequest\x1a0.nifake_grpc.MethodWithGetLastErrorParamResponse\x12t\n\x17MethodWithGrpcOnlyParam\x12+.nifake_grpc.MethodWithGrpcOnlyParamRequest\x1a,.nifake_grpc.MethodWithGrpcOnlyParamResponse\x12\x9b\x01\n$MethodUsingWholeAndFractionalNumbers\x128.nifake_grpc.MethodUsingWholeAndFractionalNumbersRequest\x1a9.nifake_grpc.MethodUsingWholeAndFractionalNumbersResponse\x12\x86\x01\n\x1dMethodUsingWholeMappedNumbers\x121.nifake_grpc.MethodUsingWholeMappedNumbersRequest\x1a2.nifake_grpc.MethodUsingWholeMappedNumbersResponse\x12z\n\x19MethodWithGrpcFieldNumber\x12-.nifake_grpc.MethodWithGrpcFieldNumberRequest\x1a..nifake_grpc.MethodWithGrpcFieldNumberResponse\x12\x83\x01\n\x1cMethodWithProtoOnlyParameter\x120.nifake_grpc.MethodWithProtoOnlyParameterRequest\x1a1.nifake_grpc.MethodWithProtoOnlyParameterResponse\x12z\n\x19ReadDataWithInOutIviTwist\x12-.nifake_grpc.ReadDataWithInOutIviTwistRequest\x1a..nifake_grpc.ReadDataWithInOutIviTwistResponse\x12\x9e\x01\n%ReadDataWithMultipleIviTwistParamSets\x129.nifake_grpc.ReadDataWithMultipleIviTwistParamSetsRequest\x1a:.nifake_grpc.ReadDataWithMultipleIviTwistParamSetsResponse\x12M\n\nInitExtCal\x12\x1e.nifake_grpc.InitExtCalRequest\x1a\x1f.nifake_grpc.InitExtCalResponse\x12\\\n\x0fInitWithVarArgs\x12#.nifake_grpc.InitWithVarArgsRequest\x1a$.nifake_grpc.InitWithVarArgsResponse\x12\x95\x01\n"MultipleArraysSameSizeWithOptional\x126.nifake_grpc.MultipleArraysSameSizeWithOptionalRequest\x1a7.nifake_grpc.MultipleArraysSameSizeWithOptionalResponse\x12z\n\x19UseATwoDimensionParameter\x12-.nifake_grpc.UseATwoDimensionParameterRequest\x1a..nifake_grpc.UseATwoDimensionParameterResponse\x12z\n\x19ViUInt8ArrayInputFunction\x12-.nifake_grpc.ViUInt8ArrayInputFunctionRequest\x1a..nifake_grpc.ViUInt8ArrayInputFunctionResponse\x12}\n\x1aViUInt8ArrayOutputFunction\x12..nifake_grpc.ViUInt8ArrayOutputFunctionRequest\x1a/.nifake_grpc.ViUInt8ArrayOutputFunctionResponse\x12z\n\x19ViInt16ArrayInputFunction\x12-.nifake_grpc.ViInt16ArrayInputFunctionRequest\x1a..nifake_grpc.ViInt16ArrayInputFunctionResponseB<\n\x10com.ni.grpc.fakeB\x06NiFakeP\x01\xaa\x02\x1dNationalInstruments.Grpc.Fakeb\x06proto3')`

<!--NI_PYTHON_API repo=nimi-python path=generated/nifake/nifake/nifake_pb2_grpc.py -->
## PYTHON MODULE: generated/nifake/nifake/nifake_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

### `class NiFakeStub(object)`

Missing associated documentation comment in .proto file.

#### `def __init__(self, channel)`

Constructor.

        Args:
            channel: A grpc.Channel.
        

### `class NiFakeServicer(object)`

Missing associated documentation comment in .proto file.

#### `def Abort(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BoolArrayOutputFunction(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Close(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def EnumArrayOutputFunction(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def EnumInputFunctionWithDefaults(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def StringValuedEnumInputFunctionWithDefaults(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ErrorMessage(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def FetchWaveform(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetABoolean(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetANumber(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAStringOfFixedMaximumSize(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAnIviDanceCharArray(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetArrayUsingIviDance(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViBoolean(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViInt64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViReal64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViSession(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetCalDateAndTime(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetCalInterval(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetEnumValue(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetError(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def InitWithOptions(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def MultipleArrayTypes(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def MultipleArraysSameSize(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def MultipleArraysDifferentSize(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def MixedIviDanceAndLenMechanism(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def OneInputFunction(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ParametersAreMultipleTypes(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def PoorlyNamedSimpleFunction(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Read(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadFromChannel(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReturnANumberAndAString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReturnMultipleTypes(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViBoolean(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViInt64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViReal64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def TwoInputFunction(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Use64BitNumber(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteWaveform(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteWaveformNumpyComplex128(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteWaveformNumpyComplex64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteWaveformNumpyComplexInterleavedI16(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetCustomType(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetCustomTypeArray(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetCustomType(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetCustomTypeArray(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAnIviDanceWithATwistArray(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAnIviDanceWithATwistString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DoubleAllTheNums(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def AcceptListOfDurationsInSeconds(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReturnDurationInSeconds(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReturnListOfDurationsInSeconds(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureAbc(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureEnums(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ExportAttributeConfigurationBufferEx(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ImportAttributeConfigurationBufferEx(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def FetchWithCustomSize(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetParameterWithOverriddenGrpcName(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def IviDanceWithTwistWithMultipleArraysAndOneBufferSize(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def FunctionWithOverriddenGrpcName2x(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def StringValuedEnumNoEnumGenerated(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def IviDanceWithATwistCalculatedSizeOut(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ImportAttributeConfigurationBuffer(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ExportAttributeConfigurationBuffer(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Control4022(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def AcceptViSessionArray(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def AcceptViUInt32Array(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BoolArrayInputFunction(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CloseExtCal(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CommandWithReservedParam(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateConfigurationList(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CustomNestedStructRoundtrip(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetBitfieldAsEnumArray(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAnIviDanceWithATwistArrayOfCustomType(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAnIviDanceWithATwistArrayWithInputArray(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAnIviDanceWithATwistByteArray(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAnIviDanceWithATwistStringStrlenBug(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetArraySizeForCustomCode(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetArrayViUInt8WithEnum(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetViUInt8(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetViInt32Array(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetViUInt32Array(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def MethodUsingEnumWithGrpcNameValues(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def MethodWithGetLastErrorParam(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def MethodWithGrpcOnlyParam(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def MethodUsingWholeAndFractionalNumbers(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def MethodUsingWholeMappedNumbers(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def MethodWithGrpcFieldNumber(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def MethodWithProtoOnlyParameter(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadDataWithInOutIviTwist(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadDataWithMultipleIviTwistParamSets(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def InitExtCal(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def InitWithVarArgs(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def MultipleArraysSameSizeWithOptional(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def UseATwoDimensionParameter(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ViUInt8ArrayInputFunction(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ViUInt8ArrayOutputFunction(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ViInt16ArrayInputFunction(self, request, context)`

Missing associated documentation comment in .proto file.

### `def add_NiFakeServicer_to_server(servicer, server)`

### `class NiFake(object)`

Missing associated documentation comment in .proto file.

#### `def Abort(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BoolArrayOutputFunction(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Close(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def EnumArrayOutputFunction(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def EnumInputFunctionWithDefaults(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def StringValuedEnumInputFunctionWithDefaults(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ErrorMessage(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def FetchWaveform(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetABoolean(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetANumber(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAStringOfFixedMaximumSize(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAnIviDanceCharArray(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetArrayUsingIviDance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViBoolean(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViInt64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViReal64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViSession(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetCalDateAndTime(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetCalInterval(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetEnumValue(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetError(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def InitWithOptions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def MultipleArrayTypes(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def MultipleArraysSameSize(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def MultipleArraysDifferentSize(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def MixedIviDanceAndLenMechanism(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def OneInputFunction(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ParametersAreMultipleTypes(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def PoorlyNamedSimpleFunction(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Read(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadFromChannel(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReturnANumberAndAString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReturnMultipleTypes(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViBoolean(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViInt64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViReal64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def TwoInputFunction(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Use64BitNumber(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteWaveform(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteWaveformNumpyComplex128(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteWaveformNumpyComplex64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteWaveformNumpyComplexInterleavedI16(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetCustomType(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetCustomTypeArray(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetCustomType(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetCustomTypeArray(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAnIviDanceWithATwistArray(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAnIviDanceWithATwistString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DoubleAllTheNums(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def AcceptListOfDurationsInSeconds(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReturnDurationInSeconds(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReturnListOfDurationsInSeconds(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureAbc(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureEnums(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ExportAttributeConfigurationBufferEx(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ImportAttributeConfigurationBufferEx(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def FetchWithCustomSize(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetParameterWithOverriddenGrpcName(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def IviDanceWithTwistWithMultipleArraysAndOneBufferSize(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def FunctionWithOverriddenGrpcName2x(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def StringValuedEnumNoEnumGenerated(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def IviDanceWithATwistCalculatedSizeOut(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ImportAttributeConfigurationBuffer(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ExportAttributeConfigurationBuffer(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Control4022(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def AcceptViSessionArray(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def AcceptViUInt32Array(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BoolArrayInputFunction(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CloseExtCal(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CommandWithReservedParam(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateConfigurationList(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CustomNestedStructRoundtrip(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetBitfieldAsEnumArray(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAnIviDanceWithATwistArrayOfCustomType(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAnIviDanceWithATwistArrayWithInputArray(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAnIviDanceWithATwistByteArray(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAnIviDanceWithATwistStringStrlenBug(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetArraySizeForCustomCode(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetArrayViUInt8WithEnum(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetViUInt8(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetViInt32Array(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetViUInt32Array(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def MethodUsingEnumWithGrpcNameValues(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def MethodWithGetLastErrorParam(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def MethodWithGrpcOnlyParam(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def MethodUsingWholeAndFractionalNumbers(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def MethodUsingWholeMappedNumbers(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def MethodWithGrpcFieldNumber(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def MethodWithProtoOnlyParameter(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadDataWithInOutIviTwist(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadDataWithMultipleIviTwistParamSets(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def InitExtCal(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def InitWithVarArgs(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def MultipleArraysSameSizeWithOptional(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def UseATwoDimensionParameter(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ViUInt8ArrayInputFunction(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ViUInt8ArrayOutputFunction(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ViInt16ArrayInputFunction(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nifake/nifake/session.py -->
## PYTHON MODULE: generated/nifake/nifake/session.py

### `class _Acquisition(object)`

#### `def __init__(self, session)`

#### `def __enter__(self)`

#### `def __exit__(self, exc_type, exc_value, traceback)`

### `def ivi_synchronized(f)`

### `class _Lock(object)`

#### `def __init__(self, session)`

#### `def __enter__(self)`

#### `def __exit__(self, exc_type, exc_value, traceback)`

### `class _RepeatedCapabilities(object)`

#### `def __init__(self, session, prefix, current_repeated_capability_list)`

#### `def __getitem__(self, repeated_capability)`

Set/get properties or call methods with a repeated capability (i.e. channels)

### `class _NoChannel(object)`

#### `def __init__(self, session)`

#### `def __enter__(self)`

#### `def __exit__(self, exc_type, exc_value, traceback)`

### `class _SessionBase(object)`

Base class for all NI-FAKE sessions.

#### `def __init__(self, repeated_capability_list, all_channels_in_session, interpreter, freeze_it=False)`

#### `def __repr__(self)`

#### `def __setattr__(self, key, value)`

#### `def function_with_repeated_capability_type(self)`

function_with_repeated_capability_type

        A method with a parameter that specifies repeated_capability_type.

        Tip:
        This method can be called on specific sites within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ].function_with_repeated_capability_type`

        To call the method on all sites, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session.function_with_repeated_capability_type`
        

#### `def _get_attribute_vi_boolean(self, attribute_id)`

_get_attribute_vi_boolean

        Queries the value of a ViBoolean property.

        Tip:
        This method can be called on specific channels within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_boolean`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            attribute_value (bool): Returns the value of the property.

        

#### `def _get_attribute_vi_int32(self, attribute_id)`

_get_attribute_vi_int32

        Queries the value of a ViInt32 property.

        Tip:
        This method can be called on specific channels within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_int32`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            attribute_value (int): Returns the value of the property.

        

#### `def _get_attribute_vi_int64(self, attribute_id)`

_get_attribute_vi_int64

        Queries the value of a ViInt64 property.

        Tip:
        This method can be called on specific channels within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_int64`

        To call the method on all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_int64`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            attribute_value (int): Returns the value of the property.

        

#### `def _get_attribute_vi_real64(self, attribute_id)`

_get_attribute_vi_real64

        Queries the value of a ViReal property.

        Tip:
        This method can be called on specific channels within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_real64`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            attribute_value (float): Returns the value of the property.

        

#### `def _get_attribute_vi_string(self, attribute_id)`

_get_attribute_vi_string

        Queries the value of a ViBoolean property.

        Tip:
        This method can be called on specific channels within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_string`

        Args:
            attribute_id (int): Pass the ID of a property.


        Returns:
            attribute_value (str): Returns the value of the property.

        

#### `def _get_channel_names(self, indices)`

_get_channel_names

        Returns a list of channel names for the given channel indices.

        Args:
            indices (basic sequence types or str or int): Index list for the channels in the session. Valid values are from zero to the total number of channels in the session minus one. The index string can be one of the following formats:

                -   A comma-separated list—for example, "0,2,3,1"
                -   A range using a hyphen—for example, "0-3"
                -   A range using a colon—for example, "0:3 "

                You can combine comma-separated lists and ranges that use a hyphen or colon. Both out-of-order and repeated indices are supported ("2,3,0," "1,2,2,3"). White space characters, including spaces, tabs, feeds, and carriage returns, are allowed between characters. Ranges can be incrementing or decrementing.


        Returns:
            names (list of str): The channel name(s) at the specified indices.

        

#### `def lock(self)`

lock

        Obtains a multithread lock on the device session. Before doing so, the
        software waits until all other execution threads release their locks
        on the device session.

        Other threads may have obtained a lock on this session for the
        following reasons:

            -  The application called the lock method.
            -  A call to NI-FAKE locked the session.
            -  After a call to the lock method returns
               successfully, no other threads can access the device session until
               you call the unlock method or exit out of the with block when using
               lock context manager.
            -  Use the lock method and the
               unlock method around a sequence of calls to
               instrument driver methods if you require that the device retain its
               settings through the end of the sequence.

        You can safely make nested calls to the lock method
        within the same thread. To completely unlock the session, you must
        balance each call to the lock method with a call to
        the unlock method.

        Returns:
            lock (context manager): When used in a with statement, nifake.Session.lock acts as
            a context manager and unlock will be called when the with block is exited
        

#### `def get_channel_names(self, indices)`

get_channel_names

        Returns a list of channel names for the given channel indices.

        Args:
            indices (basic sequence types or str or int): Index list for the channels in the session. Valid values are from zero to the total number of channels in the session minus one. The index string can be one of the following formats:

                -   A comma-separated list—for example, "0,2,3,1"
                -   A range using a hyphen—for example, "0-3"
                -   A range using a colon—for example, "0:3 "

                You can combine comma-separated lists and ranges that use a hyphen or colon. Both out-of-order and repeated indices are supported ("2,3,0," "1,2,2,3"). White space characters, including spaces, tabs, feeds, and carriage returns, are allowed between characters. Ranges can be incrementing or decrementing.


        Returns:
            names (list of str): The channel name(s) at the specified indices.

        

#### `def read_from_channel(self, maximum_time)`

read_from_channel

        Acquires a single measurement and returns the measured value.

        Tip:
        This method can be called on specific channels within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].read_from_channel`

        To call the method on all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session.read_from_channel`

        Args:
            maximum_time (hightime.timedelta): Specifies the **maximum_time** allowed in milliseconds.


        Returns:
            reading (float): The measured value.

        

#### `def _set_attribute_vi_boolean(self, attribute_id, attribute_value)`

_set_attribute_vi_boolean

        This method sets the value of a ViBoolean property.

        Tip:
        This method can be called on specific channels within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_boolean`

        Args:
            attribute_id (int): Pass the ID of a property.

            attribute_value (bool): Pass the value that you want to set the property to.

        

#### `def _set_attribute_vi_int32(self, attribute_id, attribute_value)`

_set_attribute_vi_int32

        This method sets the value of a ViInt32 property.

        Tip:
        This method can be called on specific channels within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_int32`

        Args:
            attribute_id (int): Pass the ID of a property.

            attribute_value (int): Pass the value that you want to set the property to.

        

#### `def _set_attribute_vi_int64(self, attribute_id, attribute_value)`

_set_attribute_vi_int64

        This method sets the value of a ViInt64 property.

        Tip:
        This method can be called on specific channels within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_int64`

        To call the method on all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_int64`

        Args:
            attribute_id (int): Pass the ID of a property.

            attribute_value (int): Pass the value that you want to set the property to.

        

#### `def _set_attribute_vi_real64(self, attribute_id, attribute_value)`

_set_attribute_vi_real64

        This method sets the value of a ViReal64 property.

        Tip:
        This method can be called on specific channels within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_real64`

        Args:
            attribute_id (int): Pass the ID of a property.

            attribute_value (float): Pass the value that you want to set the property to.

        

#### `def _set_attribute_vi_string(self, attribute_id, attribute_value)`

_set_attribute_vi_string

        This method sets the value of a ViString property.

        Tip:
        This method can be called on specific channels within your :py:class:`nifake.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nifake.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_string`

        Args:
            attribute_id (int): Pass the ID of a property.

            attribute_value (str): Pass the value that you want to set the property to.

        

#### `def unlock(self)`

unlock

        Releases a lock that you acquired on an device session using
        lock. Refer to lock for additional
        information on session locks.
        

#### `def _error_message(self, error_code)`

_error_message

        Takes the errorCode returned by a functiona and returns it as a user-readable string.

        Args:
            error_code (int): The errorCode returned from the instrument.


        Returns:
            error_message (str): The error information formatted into a string.

        

### `class Session(_SessionBase)`

An NI-FAKE session to a fake MI driver whose sole purpose is to test nimi-python code generation

#### `def __init__(self, resource_name, options={}, id_query=False, reset_device=False, *, grpc_options=None)`

An NI-FAKE session to a fake MI driver whose sole purpose is to test nimi-python code generation

        Creates a new IVI instrument driver session.

        Args:
            resource_name (str): Caution: This is just some string.

                Contains the **resource_name** of the device to initialize.

            options (dict): Specifies the initial value of certain properties for the session. The
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

            id_query (bool): NI-FAKE is probably not needed.

                +----------------+---+------------------+
                | True (default) | 1 | Perform ID Query |
                +----------------+---+------------------+
                | False          | 0 | Skip ID Query    |
                +----------------+---+------------------+

            reset_device (bool): Specifies whether to reset

                +----------------+---+--------------+
                | True (default) | 1 | Reset Device |
                +----------------+---+--------------+
                | False          | 0 | Don't Reset  |
                +----------------+---+--------------+

            grpc_options (nifake.grpc_session_options.GrpcSessionOptions): MeasurementLink gRPC session options


        Returns:
            session (nifake.Session): A session object representing the device.

        

#### `def __enter__(self)`

#### `def __exit__(self, exc_type, exc_value, traceback)`

#### `def initiate(self)`

initiate

        Initiates a thingie.

        Note:
        This method will return a Python context manager that will initiate on entering and abort on exit.
        

#### `def close(self)`

close

        Closes the specified session and deallocates resources that it reserved.

        Note:
        This method is not needed when using the session context manager
        

#### `def abort(self)`

abort

        Aborts a previously initiated thingie.
        

#### `def accept_list_of_durations_in_seconds(self, delays)`

accept_list_of_durations_in_seconds

        Accepts list of hightime.timedelta or datetime.timedelta or float instances representing time delays.

        Args:
            delays (hightime.timedelta, datetime.timedelta, or float in seconds): A collection of time delay values.

        

#### `def bool_array_output_function(self, number_of_elements)`

bool_array_output_function

        This method returns an array of booleans.

        Args:
            number_of_elements (int): Number of elements in the array.


        Returns:
            an_array (list of bool): Contains an array of booleans

        

#### `def configure_abc(self)`

configure_abc

        TBD
        

#### `def custom_nested_struct_roundtrip(self, nested_custom_type_in)`

custom_nested_struct_roundtrip

        TBD

        Args:
            nested_custom_type_in (CustomStructNestedTypedef):


        Returns:
            nested_custom_type_out (CustomStructNestedTypedef):

        

#### `def double_all_the_nums(self, numbers)`

double_all_the_nums

        Test for buffer with converter

        Args:
            numbers (list of float): numbers is an array of numbers we want to double.

        

#### `def enum_array_output_function(self, number_of_elements)`

enum_array_output_function

        This method returns an array of enums, stored as 16 bit integers under the hood.

        Args:
            number_of_elements (int): Number of elements in the array.


        Returns:
            an_array (list of enums.Turtle): Contains an array of enums, stored as 16 bit integers under the hood

        

#### `def enum_input_function_with_defaults(self, a_turtle=enums.Turtle.LEONARDO)`

enum_input_function_with_defaults

        This method takes one parameter other than the session, which happens to be an enum and has a default value.

        Args:
            a_turtle (enums.Turtle): Indicates a ninja turtle

                +---+---------------+
                | 0 | Leonardo      |
                +---+---------------+
                | 1 | Donatello     |
                +---+---------------+
                | 2 | Raphael       |
                +---+---------------+
                | 3 | Mich elangelo |
                +---+---------------+

        

#### `def export_attribute_configuration_buffer(self)`

export_attribute_configuration_buffer

        Export configuration buffer.

        Returns:
            configuration (bytes):

        

#### `def fetch_waveform(self, number_of_samples)`

fetch_waveform

        Returns waveform data.

        Args:
            number_of_samples (int): Number of samples to return


        Returns:
            waveform_data (array.array("d")): Samples fetched from the device. Array should be numberOfSamples big.

        

#### `def fetch_waveform_into(self, waveform_data)`

fetch_waveform_into

        Returns waveform data.

        Args:
            waveform_data (numpy.array(dtype=numpy.float64)): Samples fetched from the device. Array should be numberOfSamples big.

        

#### `def function_with_3d_numpy_array_of_numpy_complex128_input_parameter(self, multidimensional_array)`

function_with_3d_numpy_array_of_numpy_complex128_input_parameter

        Method that takes a 3D numpy array of numpy complex128 as an input parameter.

        Args:
            multidimensional_array (numpy.array(dtype=numpy.complex128)): Specifies the 3D array of numpy complex numbers to write.

        

#### `def function_with_intflag_parameter(self, flag)`

function_with_intflag_parameter

        Calls a method that takes a flag parameter which can be OR'd from multiple enum values.

        Args:
            flag (enums.IntFlagEnum): A flag parameter that can be a combination (bitwise OR) of IntFlagEnum values.

        

#### `def get_a_boolean(self)`

get_a_boolean

        Returns a boolean.

        Note: This method rules!

        Returns:
            a_boolean (bool): Contains a boolean.

        

#### `def get_a_number(self)`

get_a_number

        Returns a number.

        Note: This method rules!

        Returns:
            a_number (int): Contains a number.

        

#### `def get_a_string_of_fixed_maximum_size(self)`

get_a_string_of_fixed_maximum_size

        Illustrates returning a string of fixed size.

        Returns:
            a_string (str): String comes back here. Buffer must be 256 big.

        

#### `def get_a_string_using_python_code(self, a_number)`

get_a_string_using_python_code

        Returns a number and a string.

        Note: This method rules!

        Args:
            a_number (int): Contains a number.


        Returns:
            a_string (str): Contains a string of length aNumber.

        

#### `def get_an_ivi_dance_char_array(self)`

get_an_ivi_dance_char_array

        TBD

        Returns:
            char_array (str):

        

#### `def get_an_ivi_dance_with_a_twist_string(self)`

get_an_ivi_dance_with_a_twist_string

        TBD

        Returns:
            a_string (str):

        

#### `def get_array_for_python_code_custom_type(self)`

get_array_for_python_code_custom_type

        This method returns an array for use in python-code size mechanism.

        Returns:
            array_out (list of CustomStruct): Array of custom type using python-code size mechanism

        

#### `def get_array_for_python_code_double(self)`

get_array_for_python_code_double

        This method returns an array for use in python-code size mechanism.

        Returns:
            array_out (list of float): Array of double using python-code size mechanism

        

#### `def get_array_size_for_python_code(self)`

get_array_size_for_python_code

        This method returns the size of the array for use in python-code size mechanism.

        Returns:
            size_out (int): Size of array

        

#### `def get_array_using_ivi_dance(self)`

get_array_using_ivi_dance

        This method returns an array of float whose size is determined with the IVI dance.

        Returns:
            array_out (list of float): The array returned by this method

        

#### `def _get_cal_date_and_time(self, cal_type)`

_get_cal_date_and_time

        Returns the date and time of the last calibration performed.

        Args:
            cal_type (int): Specifies the type of calibration performed (external or self-calibration).


        Returns:
            month (int): Indicates the **month** of the last calibration.

            day (int): Indicates the **day** of the last calibration.

            year (int): Indicates the **year** of the last calibration.

            hour (int): Indicates the **hour** of the last calibration.

            minute (int): Indicates the **minute** of the last calibration.

        

#### `def get_cal_interval(self)`

get_cal_interval

        Returns the recommended maximum interval, in **months**, between external calibrations.

        Returns:
            months (hightime.timedelta): Specifies the recommended maximum interval, in **months**, between external calibrations.

        

#### `def get_custom_type(self)`

get_custom_type

        This method returns a custom type.

        Returns:
            cs (CustomStruct): Set using custom type

        

#### `def get_custom_type_array(self, number_of_elements)`

get_custom_type_array

        This method returns a custom type.

        Args:
            number_of_elements (int): Number of elements in the array.


        Returns:
            cs (list of CustomStruct): Get using custom type

        

#### `def get_custom_type_typedef(self)`

get_custom_type_typedef

        This method returns a custom type with typedef and a custom type with nested typedef.

        Returns:
            cst (CustomStructTypedef): An object of a custom type with typedef

            csnt (CustomStructNestedTypedef): An object of a custom type with nested typedef

        

#### `def get_enum_value(self)`

get_enum_value

        Returns an enum value

        Note: Splinter is not supported.

        Returns:
            a_quantity (int): This is an amount.

                Note: The amount will be between -2^31 and (2^31-1)

            a_turtle (enums.Turtle): Indicates a ninja turtle

                +---+---------------+
                | 0 | Leonardo      |
                +---+---------------+
                | 1 | Donatello     |
                +---+---------------+
                | 2 | Raphael       |
                +---+---------------+
                | 3 | Mich elangelo |
                +---+---------------+

        

#### `def get_cal_date_and_time(self, cal_type)`

get_cal_date_and_time

        Returns the date and time of the last calibration performed.

        Args:
            cal_type (int): Specifies the type of calibration performed (external or self-calibration).


        Returns:
            last_cal_datetime (hightime.datetime): Indicates date and time of the last calibration.

        

#### `def get_parameter_with_overridden_grpc_name(self, enum_parameter)`

get_parameter_with_overridden_grpc_name

        TBD

        Args:
            enum_parameter (enums.Turtle):


        Returns:
            original_parameter (int):

        

#### `def import_attribute_configuration_buffer(self, configuration)`

import_attribute_configuration_buffer

        Import configuration buffer.

        Args:
            configuration (bytes):

        

#### `def import_attribute_configuration_buffer_ex(self, configuration)`

import_attribute_configuration_buffer_ex

        TBD

        Args:
            configuration (list of ViAddr):

        

#### `def _init_with_options(self, resource_name, option_string, id_query=False, reset_device=False)`

_init_with_options

        Creates a new IVI instrument driver session.

        Args:
            resource_name (str): Caution: This is just some string.

                Contains the **resource_name** of the device to initialize.

            option_string (dict): Some options

            id_query (bool): NI-FAKE is probably not needed.

                +----------------+---+------------------+
                | True (default) | 1 | Perform ID Query |
                +----------------+---+------------------+
                | False          | 0 | Skip ID Query    |
                +----------------+---+------------------+

            reset_device (bool): Specifies whether to reset

                +----------------+---+--------------+
                | True (default) | 1 | Reset Device |
                +----------------+---+--------------+
                | False          | 0 | Don't Reset  |
                +----------------+---+--------------+


        Returns:
            vi (int): Returns a ViSession handle that you use.

        

#### `def _initiate(self)`

_initiate

        Initiates a thingie.
        

#### `def method_using_whole_and_fractional_numbers(self)`

method_using_whole_and_fractional_numbers

        TBD

        Returns:
            whole_number (int):

            fractional_number (float):

        

#### `def method_with_grpc_only_param(self, simple_param)`

method_with_grpc_only_param

        TBD

        Args:
            simple_param (int):

        

#### `def method_with_proto_only_parameter(self, attribute_value)`

method_with_proto_only_parameter

        TBD

        Args:
            attribute_value (int):

        

#### `def mixed_ivi_dance_and_len_mechanism(self, input_values)`

mixed_ivi_dance_and_len_mechanism

        Test method with mixed size mechanisms: one len-sized input array and one IVI-dance output array.

        Args:
            input_values (list of float): Input array of doubles using len size mechanism.


        Returns:
            output_array (list of int): Output array using IVI-dance size mechanism.

        

#### `def multiple_array_types(self, output_array_size, input_array_of_floats, input_array_of_integers=None)`

multiple_array_types

        Receives and returns multiple types of arrays.

        Args:
            output_array_size (int): Size of the array that will be returned.

            input_array_of_floats (list of float): Array of floats

            input_array_of_integers (list of int): Array of integers. Optional. If passed in then size must match that of inputArrayOfFloats.


        Returns:
            output_array (list of float): Array that will be returned.

                Note: The size must be at least outputArraySize.

            output_array_of_fixed_length (list of float): An array of doubles with fixed size.

        

#### `def multiple_arrays_different_size(self, values_array, data_array)`

multiple_arrays_different_size

        Test method with multiple arrays that have different size parameters. This tests the length handling mechanism where different array parameters can reference different size parameters.

        Args:
            values_array (list of float): Array of double values with its own size parameter.

            data_array (list of int): Array of integer values with a different size parameter.

        

#### `def multiple_arrays_same_size(self, values1, values2, values3, values4)`

multiple_arrays_same_size

        Method to test multiple arrays that use the same size

        Args:
            values1 (list of float): Array 1 of same size.

            values2 (list of float): Array 2 of same size.

            values3 (list of float): Array 3 of same size.

            values4 (list of float): Array 4 of same size.

        

#### `def one_input_function(self, a_number)`

one_input_function

        This method takes one parameter other than the session.

        Args:
            a_number (int): Contains a number

        

#### `def parameters_are_multiple_types(self, a_boolean, an_int32, an_int64, an_int_enum, a_float, a_float_enum, a_string)`

parameters_are_multiple_types

        Has parameters of multiple types.

        Args:
            a_boolean (bool): Contains a boolean.

            an_int32 (int): Contains a 32-bit integer.

            an_int64 (int): Contains a 64-bit integer.

            an_int_enum (enums.Turtle): Indicates a ninja turtle

                +---+---------------+
                | 0 | Leonardo      |
                +---+---------------+
                | 1 | Donatello     |
                +---+---------------+
                | 2 | Raphael       |
                +---+---------------+
                | 3 | Mich elangelo |
                +---+---------------+

            a_float (float): The measured value.

            a_float_enum (enums.FloatEnum): A float enum.

            a_string (str): An IVI dance string.

        

#### `def simple_function(self)`

simple_function

        This method takes no parameters other than the session.
        

#### `def read(self, maximum_time)`

read

        Acquires a single measurement and returns the measured value.

        Args:
            maximum_time (hightime.timedelta): Specifies the **maximum_time** allowed in seconds.


        Returns:
            reading (float): The measured value.

        

#### `def return_a_number_and_a_string(self)`

return_a_number_and_a_string

        Returns a number and a string.

        Note: This method rules!

        Returns:
            a_number (int): Contains a number.

            a_string (str): Contains a string. Buffer must be 256 bytes or larger.

        

#### `def return_duration_in_seconds(self)`

return_duration_in_seconds

        Returns a hightime.timedelta instance.

        Returns:
            timedelta (hightime.timedelta): Duration in seconds.

        

#### `def return_list_of_durations_in_seconds(self, number_of_elements)`

return_list_of_durations_in_seconds

        Returns a list of hightime.timedelta instances.

        Args:
            number_of_elements (int): Number of elements in output.


        Returns:
            timedeltas (hightime.timedelta): Contains a list of hightime.timedelta instances.

        

#### `def return_multiple_types(self, array_size)`

return_multiple_types

        Returns multiple types.

        Args:
            array_size (int): Number of measurements to acquire.


        Returns:
            a_boolean (bool): Contains a boolean.

            an_int32 (int): Contains a 32-bit integer.

            an_int64 (int): Contains a 64-bit integer.

            an_int_enum (enums.Turtle): Indicates a ninja turtle

                +---+---------------+
                | 0 | Leonardo      |
                +---+---------------+
                | 1 | Donatello     |
                +---+---------------+
                | 2 | Raphael       |
                +---+---------------+
                | 3 | Mich elangelo |
                +---+---------------+

            a_float (float): The measured value.

            a_float_enum (enums.FloatEnum): A float enum.

            an_array (list of float): An array of measurement values.

                Note: The size must be at least arraySize.

            a_string (str): An IVI dance string.

        

#### `def set_custom_type(self, cs)`

set_custom_type

        This method takes a custom type.

        Args:
            cs (CustomStruct): Set using custom type

        

#### `def set_custom_type_array(self, cs)`

set_custom_type_array

        This method takes an array of custom types.

        Args:
            cs (list of CustomStruct): Set using custom type

        

#### `def string_valued_enum_input_function_with_defaults(self, a_mobile_os_name=enums.MobileOSNames.ANDROID)`

string_valued_enum_input_function_with_defaults

        This method takes one parameter other than the session, which happens to be a string-valued enum and has a default value.

        Args:
            a_mobile_os_name (enums.MobileOSNames): Indicates a Mobile OS

                +---------+---------+
                | ANDROID | Android |
                +---------+---------+
                | IOS     | iOS     |
                +---------+---------+
                | NONE    | None    |
                +---------+---------+

        

#### `def two_input_function(self, a_number, a_string)`

two_input_function

        This method takes two parameters other than the session.

        Args:
            a_number (float): Contains a number

            a_string (str): Contains a string

        

#### `def use64_bit_number(self, input)`

use64_bit_number

        Returns a number and a string.

        Note: This method rules!

        Args:
            input (int): A big number on its way in.


        Returns:
            output (int): A big number on its way out.

        

#### `def write_waveform(self, waveform)`

write_waveform

        Writes waveform to the driver

        Args:
            waveform (array.array("d")): Waveform data.

        

#### `def write_waveform_numpy(self, waveform)`

write_waveform_numpy

        Writes waveform to the driver

        Args:
            waveform (numpy.array(dtype=numpy.float64)): Waveform data.

        

#### `def write_waveform_numpy_complex128(self, waveform_data_array)`

write_waveform_numpy_complex128

        A method that writes a waveform of numpy complex128 samples.

        Args:
            waveform_data_array (numpy.array(dtype=numpy.complex128)): Specifies the array of data to load into the waveform.

        

#### `def write_waveform_numpy_complex64(self, waveform_data_array)`

write_waveform_numpy_complex64

        A method that writes a waveform of numpy complex64 samples.

        Args:
            waveform_data_array (numpy.array(dtype=numpy.complex64)): Specifies the array of data to load into the waveform.

        

#### `def write_waveform_numpy_complex_interleaved_i16(self, waveform_data_array)`

write_waveform_numpy_complex_interleaved_i16

        A method that writes a waveform of numpy complex i16 samples.

        Args:
            waveform_data_array (numpy.array(dtype=numpy.int16)): Specifies the array of data to load into the waveform.

        

#### `def _close(self)`

_close

        Closes the specified session and deallocates resources that it reserved.
        

#### `def self_test(self)`

self_test

        Performs a self-test
        

#### `def _self_test(self)`

_self_test

        Performs a self-test.

        Returns:
            self_test_result (int): Contains the value returned from the instrument self-test. Zero indicates success.

            self_test_message (str): This parameter contains the string returned from the instrument self-test. The array must contain at least 256 elements.

        

<!--NI_PYTHON_API repo=nimi-python path=generated/nifake/nifake/unit_tests/_matchers.py -->
## PYTHON MODULE: generated/nifake/nifake/unit_tests/_matchers.py

### MODULE DOCSTRING

Matcher classes used by unit tests in order to set mock expectations.
These work well with our visatype definitions.


### `class _ScalarMatcher(object)`

#### `def __init__(self, expected_type, expected_value)`

#### `def __eq__(self, other)`

#### `def __repr__(self)`

### `class _PointerMatcher(object)`

#### `def __init__(self, expected_type)`

#### `def __eq__(self, other)`

#### `def __repr__(self)`

### `class _BufferMatcher(object)`

#### `def __init__(self, expected_element_type, expected_size_or_value)`

#### `def __eq__(self, other)`

#### `def __repr__(self)`

#### `def __str__(self)`

### `class ViStringMatcher(object)`

#### `def __init__(self, expected_string_value)`

#### `def __eq__(self, other)`

#### `def __repr__(self)`

### `def _compare_ctype_structs(expected, actual)`

### `class CustomTypeMatcher(object)`

#### `def __init__(self, expected_type, expected_value)`

#### `def __eq__(self, actual)`

#### `def __repr__(self)`

### `class CustomTypeBufferMatcher(object)`

#### `def __init__(self, expected_element_type, expected_value)`

#### `def __eq__(self, actual)`

#### `def __repr__(self)`

#### `def __str__(self)`

### `class ViBooleanMatcher(_ScalarMatcher)`

#### `def __init__(self, expected_value)`

### `class ViSessionMatcher(_ScalarMatcher)`

#### `def __init__(self, expected_value)`

### `class ViInt16Matcher(_ScalarMatcher)`

#### `def __init__(self, expected_value)`

### `class ViInt32Matcher(_ScalarMatcher)`

#### `def __init__(self, expected_value)`

### `class ViUInt32Matcher(_ScalarMatcher)`

#### `def __init__(self, expected_value)`

### `class ViAttrMatcher(_ScalarMatcher)`

#### `def __init__(self, expected_value)`

### `class ViInt64Matcher(_ScalarMatcher)`

#### `def __init__(self, expected_value)`

### `class ViReal64Matcher(_ScalarMatcher)`

#### `def __init__(self, expected_value)`

### `class ViBooleanPointerMatcher(_PointerMatcher)`

#### `def __init__(self)`

### `class ViSessionPointerMatcher(_PointerMatcher)`

#### `def __init__(self)`

### `class ViInt16PointerMatcher(_PointerMatcher)`

#### `def __init__(self)`

### `class ViInt32PointerMatcher(_PointerMatcher)`

#### `def __init__(self)`

### `class ViInt64PointerMatcher(_PointerMatcher)`

#### `def __init__(self)`

### `class ViReal64PointerMatcher(_PointerMatcher)`

#### `def __init__(self)`

### `def _compare_complex_number_arrays(expected, actual)`

### `class NIComplexNumberPointerMatcher(_PointerMatcher)`

#### `def __init__(self, expected_data, expected_size)`

#### `def __eq__(self, other)`

#### `def __repr__(self)`

### `class NIComplexNumberF32PointerMatcher(_PointerMatcher)`

#### `def __init__(self, expected_data, expected_size)`

#### `def __eq__(self, other)`

#### `def __repr__(self)`

### `class NIComplexI16PointerMatcher(_PointerMatcher)`

#### `def __init__(self, expected_data, expected_size)`

#### `def __eq__(self, other)`

#### `def __repr__(self)`

### `class ViBooleanBufferMatcher(_BufferMatcher)`

#### `def __init__(self, expected_size_or_value)`

### `class ViCharBufferMatcher(_BufferMatcher)`

#### `def __init__(self, expected_size_or_value)`

### `class ViInt8BufferMatcher(_BufferMatcher)`

#### `def __init__(self, expected_size_or_value)`

### `class ViInt16BufferMatcher(_BufferMatcher)`

#### `def __init__(self, expected_size_or_value)`

### `class ViInt32BufferMatcher(_BufferMatcher)`

#### `def __init__(self, expected_size_or_value)`

### `class ViInt64BufferMatcher(_BufferMatcher)`

#### `def __init__(self, expected_size_or_value)`

### `class ViReal64BufferMatcher(_BufferMatcher)`

#### `def __init__(self, expected_size_or_value)`

### `class ViSessionBufferMatcher(_BufferMatcher)`

#### `def __init__(self, expected_size_or_value)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nifake/nifake/unit_tests/_mock_helper.py -->
## PYTHON MODULE: generated/nifake/nifake/unit_tests/_mock_helper.py

### `class MockFunctionCallError(Exception)`

#### `def __init__(self, function, param=None)`

### `class SideEffectsHelper(object)`

#### `def __init__(self)`

#### `def __getitem__(self, func)`

#### `def __setitem__(self, func, val)`

#### `def niFake_Abort(self, vi)`

#### `def niFake_AcceptListOfDurationsInSeconds(self, vi, count, delays)`

#### `def niFake_BoolArrayOutputFunction(self, vi, number_of_elements, an_array)`

#### `def niFake_ConfigureABC(self, vi)`

#### `def niFake_CustomNestedStructRoundtrip(self, nested_custom_type_in, nested_custom_type_out)`

#### `def niFake_DoubleAllTheNums(self, vi, number_count, numbers)`

#### `def niFake_EnumArrayOutputFunction(self, vi, number_of_elements, an_array)`

#### `def niFake_EnumInputFunctionWithDefaults(self, vi, a_turtle)`

#### `def niFake_ExportAttributeConfigurationBuffer(self, vi, size_in_bytes, configuration)`

#### `def niFake_FetchWaveform(self, vi, number_of_samples, waveform_data, actual_number_of_samples)`

#### `def niFake_FunctionWith3dNumpyArrayOfNumpyComplex128InputParameter(self, vi, multidimensional_array)`

#### `def niFake_FunctionWithIntflagParameter(self, vi, flag)`

#### `def niFake_FunctionWithRepeatedCapabilityType(self, vi, site_list)`

#### `def niFake_GetABoolean(self, vi, a_boolean)`

#### `def niFake_GetANumber(self, vi, a_number)`

#### `def niFake_GetAStringOfFixedMaximumSize(self, vi, a_string)`

#### `def niFake_GetAStringUsingPythonCode(self, vi, a_number, a_string)`

#### `def niFake_GetAnIviDanceCharArray(self, vi, buffer_size, char_array)`

#### `def niFake_GetAnIviDanceWithATwistString(self, vi, buffer_size, a_string, actual_size)`

#### `def niFake_GetArrayForPythonCodeCustomType(self, vi, number_of_elements, array_out)`

#### `def niFake_GetArrayForPythonCodeDouble(self, vi, number_of_elements, array_out)`

#### `def niFake_GetArraySizeForPythonCode(self, vi, size_out)`

#### `def niFake_GetArrayUsingIviDance(self, vi, array_size, array_out)`

#### `def niFake_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niFake_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niFake_GetAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niFake_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niFake_GetAttributeViString(self, vi, channel_name, attribute_id, buffer_size, attribute_value)`

#### `def niFake_GetCalDateAndTime(self, vi, cal_type, month, day, year, hour, minute)`

#### `def niFake_GetCalInterval(self, vi, months)`

#### `def niFake_GetChannelNames(self, vi, indices, name_size, names)`

#### `def niFake_GetCustomType(self, vi, cs)`

#### `def niFake_GetCustomTypeArray(self, vi, number_of_elements, cs)`

#### `def niFake_GetCustomTypeTypedef(self, vi, cst, csnt)`

#### `def niFake_GetEnumValue(self, vi, a_quantity, a_turtle)`

#### `def niFake_GetError(self, vi, error_code, buffer_size, description)`

#### `def niFake_GetParameterWithOverriddenGrpcName(self, vi, original_parameter, enum_parameter)`

#### `def niFake_ImportAttributeConfigurationBuffer(self, vi, size_in_bytes, configuration)`

#### `def niFake_ImportAttributeConfigurationBufferEx(self, vi, size, configuration)`

#### `def niFake_InitWithOptions(self, resource_name, id_query, reset_device, option_string, vi)`

#### `def niFake_Initiate(self, vi)`

#### `def niFake_LockSession(self, vi, caller_has_lock)`

#### `def niFake_MethodUsingWholeAndFractionalNumbers(self, whole_number, fractional_number)`

#### `def niFake_MethodWithGrpcOnlyParam(self, simple_param)`

#### `def niFake_MethodWithProtoOnlyParameter(self, attribute_value)`

#### `def niFake_MixedIviDanceAndLenMechanism(self, vi, input_values, input_values_size, output_size, output_array)`

#### `def niFake_MultipleArrayTypes(self, vi, output_array_size, output_array, output_array_of_fixed_length, input_array_sizes, input_array_of_floats, input_array_of_integers)`

#### `def niFake_MultipleArraysDifferentSize(self, vi, values_array, values_array_size, data_array, data_array_size)`

#### `def niFake_MultipleArraysSameSize(self, vi, values1, values2, values3, values4, size)`

#### `def niFake_OneInputFunction(self, vi, a_number)`

#### `def niFake_ParametersAreMultipleTypes(self, vi, a_boolean, an_int32, an_int64, an_int_enum, a_float, a_float_enum, a_string)`

#### `def niFake_PoorlyNamedSimpleFunction(self, vi)`

#### `def niFake_Read(self, vi, maximum_time, reading)`

#### `def niFake_ReadFromChannel(self, vi, channel_name, maximum_time, reading)`

#### `def niFake_ReturnANumberAndAString(self, vi, a_number, a_string)`

#### `def niFake_ReturnDurationInSeconds(self, vi, timedelta)`

#### `def niFake_ReturnListOfDurationsInSeconds(self, vi, number_of_elements, timedeltas)`

#### `def niFake_ReturnMultipleTypes(self, vi, a_boolean, an_int32, an_int64, an_int_enum, a_float, a_float_enum, array_size, an_array, string_size, a_string)`

#### `def niFake_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niFake_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niFake_SetAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niFake_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niFake_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niFake_SetCustomType(self, vi, cs)`

#### `def niFake_SetCustomTypeArray(self, vi, number_of_elements, cs)`

#### `def niFake_SetRuntimeEnvironment(self, environment, environment_version, reserved1, reserved2)`

#### `def niFake_StringValuedEnumInputFunctionWithDefaults(self, vi, a_mobile_os_name)`

#### `def niFake_TwoInputFunction(self, vi, a_number, a_string)`

#### `def niFake_UnlockSession(self, vi, caller_has_lock)`

#### `def niFake_Use64BitNumber(self, vi, input, output)`

#### `def niFake_WriteWaveform(self, vi, number_of_samples, waveform)`

#### `def niFake_WriteWaveformNumpyComplex128(self, vi, number_of_samples, waveform_data_array)`

#### `def niFake_WriteWaveformNumpyComplex64(self, vi, number_of_samples, waveform_data_array)`

#### `def niFake_WriteWaveformNumpyComplexInterleavedI16(self, vi, number_of_samples, waveform_data_array)`

#### `def niFake_close(self, vi)`

#### `def niFake_error_message(self, vi, error_code, error_message)`

#### `def niFake_self_test(self, vi, self_test_result, self_test_message)`

#### `def set_side_effects_and_return_values(self, mock_library)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nifake/nifake/unit_tests/test_converters.py -->
## PYTHON MODULE: generated/nifake/nifake/unit_tests/test_converters.py

### `def test_convert_init_with_options_dictionary()`

### `def test_convert_timedelta_to_seconds_double()`

### `def test_convert_timedelta_to_milliseconds_int32()`

### `def test_convert_timedeltas_to_seconds_real64()`

### `def test_convert_timedelta_to_months_int32()`

### `def test_convert_seconds_real64_to_timedelta()`

### `def test_convert_seconds_real64_to_timedeltas()`

### `def test_repeated_capabilities_string_channel()`

### `def test_repeated_capabilities_string_prefix()`

### `def test_repeated_capabilities_list_channel()`

### `def test_repeated_capabilities_list_prefix()`

### `def test_repeated_capabilities_tuple_channel()`

### `def test_repeated_capabilities_tuple_prefix()`

### `def test_repeated_capabilities_unicode()`

### `def test_repeated_capabilities_raw()`

### `def test_repeated_capabilities_slice_channel()`

### `def test_repeated_capabilities_mixed_channel()`

### `def test_repeated_capabilities_mixed_prefix()`

### `def test_invalid_repeated_capabilities()`

### `def test_repeated_capabilities_slice_prefix()`

### `def test_repeated_capabilities_without_prefix()`

### `def test_repeated_capabilities_string_resource_name()`

### `def test_repeated_capabilities_list_resource_name()`

### `def test_repeated_capabilities_tuple_resource_name()`

### `def test_repeated_capabilities_mixed_resource_name()`

### `def test_repeated_capabilities_invalid_resource_names()`

### `def test_expand_channel_string_non_fully_qualified_channel_names()`

### `def test_expand_channel_string_fully_qualified_channel_names()`

### `def test_convert_chained_repeated_capability_to_parts_three_parts()`

### `def test_convert_chained_repeated_capability_to_parts_single_part()`

### `def test_convert_chained_repeated_capability_to_parts_empty_string()`

### `def test_string_to_list_channel()`

### `def test_string_to_list_prefix()`

### `def test_convert_comma_separated_string_to_list()`

### `def test_convert_list_to_comma_separated_string()`

### `def test_convert_list_to_comma_separated_string_invalid_input()`

<!--NI_PYTHON_API repo=nimi-python path=generated/nifake/nifake/unit_tests/test_grpc.py -->
## PYTHON MODULE: generated/nifake/nifake/unit_tests/test_grpc.py

- `GRPC_SESSION_OBJECT_FOR_TEST = session_pb2.Session(name='TestSession', id=42)`

### `class MyRpcError(grpc.RpcError)`

#### `def __init__(self, error_code, error_message, grpc_error=grpc.StatusCode.UNKNOWN)`

#### `def code(self)`

#### `def details(self)`

#### `def trailing_metadata(self)`

### `class TestGrpcStubInterpreter()`

#### `def setup_method(self, method)`

#### `def teardown_method(self, method)`

#### `def _get_initialized_stub_interpreter(self, grpc_channel=object())`

#### `def _check_fields(self, response_class, **kwargs)`

#### `def _set_side_effect(self, function_name, side_effect=None, **kwargs)`

#### `def _assert_call(self, function_name, request_object, metadata=None)`

#### `def test_server_unavailable(self)`

#### `def test_function_not_implemented(self)`

#### `def test_api_key_sent_to_init(self)`

#### `def test_new_session_already_exists(self)`

#### `def test_attach_to_non_existent_session(self)`

#### `def test_lock_unlock(self)`

#### `def test_simple_function(self)`

#### `def test_get_a_number(self)`

#### `def test_one_input_function(self)`

#### `def test_vi_int_64_function(self)`

#### `def test_two_input_function(self)`

#### `def test_get_enum_value(self)`

#### `def test_get_a_list_enums(self)`

#### `def test_get_a_boolean(self)`

#### `def test_get_a_list_booleans(self)`

#### `def test_single_point_read_nan(self)`

#### `def test_fetch_waveform(self)`

#### `def test_fetch_waveform_into(self)`

#### `def test_write_waveform(self)`

#### `def test_write_waveform_numpy(self)`

#### `def test_write_waveform_numpy_complex128(self)`

#### `def test_write_waveform_numpy_complex64(self)`

#### `def test_write_waveform_numpy_complex_interleaved_i16(self)`

#### `def test_function_with_3d_numpy_array_of_numpy_complex128_input_parameter(self)`

#### `def test_return_multiple_types(self)`

#### `def test_multiple_array_types(self)`

#### `def test_multiple_array_types_none_input(self)`

#### `def test_multiple_arrays_same_size(self)`

#### `def test_multiple_arrays_same_size_none_input(self)`

#### `def test_multiple_arrays_different_size(self)`

#### `def test_multiple_arrays_different_size_none_input(self)`

#### `def test_mixed_ivi_dance_and_len_mechanism(self)`

#### `def test_multiple_arrays_same_size_wrong_size(self)`

#### `def test_parameters_are_multiple_types(self)`

#### `def test_method_with_error(self)`

#### `def test_call_not_enough_parameters_error(self)`

#### `def test_invalid_method_call_wrong_type_error(self)`

#### `def test_method_with_warning(self)`

#### `def test_read_with_warning(self)`

#### `def test_get_a_string_of_fixed_maximum_size(self)`

#### `def test_return_a_number_and_a_string(self)`

#### `def test_get_an_ivi_dance_char_array(self)`

#### `def test_get_string_ivi_dance_error(self)`

#### `def test_get_an_ivi_dance_with_a_twist_string(self)`

#### `def test_get_array_using_ivi_dance(self)`

#### `def test_get_attribute_int32(self)`

#### `def test_set_attribute_int32(self)`

#### `def test_get_attribute_real64(self)`

#### `def test_set_attribute_real64(self)`

#### `def test_get_attribute_string(self)`

#### `def test_set_attribute_string(self)`

#### `def test_get_attribute_boolean(self)`

#### `def test_set_attribute_boolean(self)`

#### `def test_get_attribute_int64(self)`

#### `def test_set_attribute_int64(self)`

#### `def test_error_message_returns_error(self)`

#### `def test_set_custom_type(self)`

#### `def test_get_custom_type(self)`

#### `def test_set_custom_type_array(self)`

#### `def test_get_custom_type_array(self)`

#### `def test_get_custom_type_typedef(self)`

#### `def test_get_cal_date_time(self)`

#### `def test_import_attribute_configuration_buffer(self)`

#### `def test_missing_function(self)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nifake/nifake/unit_tests/test_library_interpreter.py -->
## PYTHON MODULE: generated/nifake/nifake/unit_tests/test_library_interpreter.py

- `SESSION_NUM_FOR_TEST = 42`

### `class TestLibraryInterpreter()`

#### `def setup_method(self, method)`

#### `def teardown_method(self, method)`

#### `def get_initialized_library_interpreter(self)`

#### `def niFake_read_warning(self, vi, maximum_time, reading)`

#### `def get_ctypes_pointer_for_buffer_side_effect(self, value, library_type=None)`

#### `def test_simple_function(self)`

#### `def test_get_a_number(self)`

#### `def test_one_input_function(self)`

#### `def test_vi_int_64_function(self)`

#### `def test_two_input_function(self)`

#### `def test_get_enum_value(self)`

#### `def test_get_a_list_enums(self)`

#### `def test_get_a_boolean(self)`

#### `def test_get_a_list_booleans(self)`

#### `def test_single_point_read_nan(self)`

#### `def test_fetch_waveform(self)`

#### `def test_fetch_waveform_into(self)`

#### `def test_write_waveform(self)`

#### `def test_write_waveform_numpy(self)`

#### `def test_return_multiple_types(self)`

#### `def test_multiple_array_types(self)`

#### `def test_multiple_array_types_none_input(self)`

#### `def test_multiple_arrays_same_size(self)`

#### `def test_multiple_arrays_same_size_none_input(self)`

#### `def test_multiple_arrays_different_size(self)`

#### `def test_multiple_arrays_different_size_none_input(self)`

#### `def test_mixed_ivi_dance_and_len_mechanism(self)`

#### `def test_parameters_are_multiple_types(self)`

#### `def test_method_with_error(self)`

#### `def test_call_not_enough_parameters_error(self)`

#### `def test_invalid_method_call_wrong_type_error(self)`

#### `def test_method_with_warning(self)`

#### `def test_read_with_warning(self)`

#### `def test_library_interpreter_always_uses_same_library_instance(self)`

#### `def test_set_runtime_environment_is_called_once_if_present(self)`

#### `def test_set_runtime_environment_not_present_in_driver_runtime(self)`

#### `def test_get_a_string_of_fixed_maximum_size(self)`

#### `def test_get_a_string_of_size_python_code(self)`

#### `def test_return_a_number_and_a_string(self)`

#### `def test_get_an_ivi_dance_char_array(self)`

#### `def test_get_string_ivi_dance_error(self)`

#### `def test_get_an_ivi_dance_with_a_twist_string(self)`

#### `def test_get_array_using_ivi_dance(self)`

#### `def test_get_attribute_int32(self)`

#### `def test_set_attribute_int32(self)`

#### `def test_get_attribute_real64(self)`

#### `def test_set_attribute_real64(self)`

#### `def test_get_attribute_string(self)`

#### `def test_set_attribute_string(self)`

#### `def test_get_attribute_boolean(self)`

#### `def test_set_attribute_boolean(self)`

#### `def test_get_attribute_int64(self)`

#### `def test_set_attribute_int64(self)`

#### `def test_get_error_returns_mismatched_error_code(self)`

#### `def test_get_error_and_error_message_returns_error(self)`

#### `def test_get_error_description_error_message_error(self)`

#### `def test_get_error_description_error_message_after_session_reset(self)`

#### `def test_set_custom_type(self)`

#### `def test_get_custom_type(self)`

#### `def test_set_custom_type_array(self)`

#### `def test_get_custom_type_array(self)`

#### `def test_get_custom_type_typedef(self)`

#### `def test_get_array_using_python_code_double(self)`

#### `def test_get_array_using_python_code_custom_type(self)`

#### `def test_get_cal_date_time(self)`

#### `def test_import_attribute_configuration_buffer_list_i8(self)`

#### `def test_import_attribute_configuration_buffer_bytes(self)`

#### `def test_import_attribute_configuration_buffer_bytearray(self)`

#### `def test_import_attribute_configuration_buffer_array_bytes(self)`

#### `def test_import_attribute_configuration_buffer_str(self)`

#### `def test_write_waveform_numpy_complex128_valid_input(self)`

#### `def test_write_waveform_numpy_complex64_valid_input(self)`

#### `def test_write_waveform_numpy_complex_interleaved_i16_valid_input(self)`

#### `def test_write_3d_numpy_array_of_numpy_complex128(self)`

#### `def test_no_memorycopy_with_multi_dimensional_numpy_complex128_array(self)`

#### `def test_no_memorycopy_with_numpy_complex64_array(self)`

#### `def test_matcher_prints(self)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nifake/nifake/unit_tests/test_library_singleton.py -->
## PYTHON MODULE: generated/nifake/nifake/unit_tests/test_library_singleton.py

### `def test_driver_runtime_not_installed_raises_driver_not_installed_error()`

<!--NI_PYTHON_API repo=nimi-python path=generated/nifake/nifake/unit_tests/test_session.py -->
## PYTHON MODULE: generated/nifake/nifake/unit_tests/test_session.py

- `SESSION_NUM_FOR_TEST = 42`

- `GRPC_SESSION_OBJECT_FOR_TEST = object()`

### `class TestSession()`

#### `def setup_method(self, method)`

#### `def teardown_method(self, method)`

#### `def test_init_with_options_and_close(self)`

#### `def test_init_with_options_nondefault_and_close(self)`

#### `def test_close(self)`

#### `def test_session_context_manager(self)`

#### `def test_init_with_error(self)`

#### `def test_close_with_error(self)`

#### `def test_session_context_manager_init_with_error(self)`

#### `def test_session_context_manager_close_with_error(self)`

#### `def test_lock_session_none(self)`

#### `def test_unlock_session_none(self)`

#### `def test_lock_context_manager(self)`

#### `def test_lock_context_manager_abnormal_exit(self)`

#### `def test_self_test(self)`

#### `def test_self_test_fail(self)`

#### `def test_acquisition_context_manager(self)`

#### `def test_acquisition_no_context_manager(self)`

#### `def test_single_point_read_timedelta(self)`

#### `def test_enum_input_function_with_defaults(self)`

#### `def test_string_valued_enum_input_function_with_defaults(self)`

#### `def test_fetch_waveform_into_wrong_type(self)`

#### `def test_parameters_are_multiple_types_error(self)`

#### `def test_error_with_rep_cap(self)`

#### `def test_call_not_enough_parameters_error(self)`

#### `def test_enum_input_function_with_defaults_bad_type_error(self)`

#### `def test_get_channel_names(self)`

#### `def test_repeated_capability_method_on_session_timedelta(self)`

#### `def test_repeated_capability_method_on_specific_channel(self)`

#### `def test_device_method_not_exist_on_repeated_capability_error(self)`

#### `def test_repeated_capabilities_list(self)`

#### `def test_chained_repeated_capabilities_list(self)`

#### `def test_chained_repeated_capability_method_on_specific_channel(self)`

#### `def test_function_with_repeated_capability_type(self)`

#### `def test_get_attribute_int32(self)`

#### `def test_set_attribute_int32(self)`

#### `def test_get_attribute_int32_with_converter(self)`

#### `def test_set_attribute_int32_with_converter(self)`

#### `def test_get_attribute_int32_with_month_converter(self)`

#### `def test_set_attribute_int32_with_month_converter(self)`

#### `def test_get_attribute_real64(self)`

#### `def test_set_attribute_real64(self)`

#### `def test_get_attribute_real64_with_converter(self)`

#### `def test_set_attribute_real64_with_converter(self)`

#### `def test_get_attribute_string(self)`

#### `def test_set_attribute_string(self)`

#### `def test_get_attribute_comma_separated_string(self)`

#### `def test_set_attribute_comma_separated_string(self)`

#### `def test_get_attribute_string_with_converter(self)`

#### `def test_set_attribute_string_with_converter(self)`

#### `def test_get_attribute_boolean(self)`

#### `def test_set_attribute_boolean(self)`

#### `def test_get_attribute_enum_int32(self)`

#### `def test_set_attribute_enum_int32(self)`

#### `def test_get_attribute_enum_real64(self)`

#### `def test_set_attribute_enum_real64(self)`

#### `def test_get_attribute_enum_with_converter(self)`

#### `def test_get_attribute_enum_with_converter_invalid_value_from_driver(self)`

#### `def test_set_attribute_enum_with_converter(self)`

#### `def test_set_attribute_enum_with_converter_invalid_input(self)`

#### `def test_get_attribute_channel(self)`

#### `def test_set_attribute_channel(self)`

#### `def test_get_attribute_int64(self)`

#### `def test_set_attribute_int64(self)`

#### `def test_get_attribute_error(self)`

#### `def test_set_attribute_error(self)`

#### `def test_add_properties_to_session_error_set(self)`

#### `def test_add_properties_to_session_error_get(self)`

#### `def test_add_properties_to_repeated_capability_error_set(self)`

#### `def test_add_properties_to_repeated_capability_error_get(self)`

#### `def test_set_enum_attribute_int32_error(self)`

#### `def test_set_wrong_enum_attribute_int32_error(self)`

#### `def test_multiple_arrays_same_size_wrong_size_2(self)`

#### `def test_multiple_arrays_same_size_wrong_size_3(self)`

#### `def test_multiple_arrays_same_size_wrong_size_4(self)`

#### `def test_multiple_arrays_different_size_none_input(self)`

#### `def test_get_cal_date_time(self)`

#### `def test_get_cal_interval(self)`

#### `def test_import_attribute_configuration_buffer_list_i8_big(self)`

#### `def test_import_attribute_configuration_buffer_list_i8_float(self)`

#### `def test_import_attribute_configuration_buffer_list_i8_big_float(self)`

#### `def test_export_attribute_configuration_buffer(self)`

#### `def test_channel_on_session(self)`

#### `def test_function_name(self)`

#### `def test_buffer_converter(self)`

#### `def test_nitclk_integration(self)`

#### `def test_accept_list_of_time_values_as_floats(self)`

#### `def test_accept_array_of_time_values_as_floats(self)`

#### `def test_accept_list_of_time_values_as_timedelta_instances(self)`

#### `def test_return_timedelta(self)`

#### `def test_return_timedeltas(self)`

#### `def test_with_valid_intflag_parameter(self)`

#### `def test_with_intflag_parameter_invalid(self)`

#### `def test_session_write_waveform_numpy_complex64_invalid_dtype(self)`

#### `def test_session_write_waveform_numpy_complex128_invalid_dtype(self)`

#### `def test_session_write_waveform_numpy_complex_interleaved_i16_invalid_dtype(self)`

### `class TestGrpcSession()`

#### `def setup_method(self, method)`

#### `def teardown_method(self, method)`

#### `def test_init_with_options_and_close(self)`

#### `def test_lock_session_none(self)`

#### `def test_unlock_session_none(self)`

#### `def test_lock_context_manager(self)`

#### `def test_lock_context_manager_abnormal_exit(self)`

#### `def test_self_test(self)`

#### `def test_export_attribute_configuration_buffer(self)`

#### `def test_get_attribute_int32(self)`

### `def test_diagnostic_information()`

### `def test_dunder_version()`

<!--NI_PYTHON_API repo=nimi-python path=generated/nifake/setup.py -->
## PYTHON MODULE: generated/nifake/setup.py

### `def read_contents(file_to_read)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nifgen/nifgen/__init__.py -->
## PYTHON MODULE: generated/nifgen/nifgen/__init__.py

### `def get_diagnostic_information()`

Get diagnostic information about the system state that is suitable for printing or logging

    returns: dict

    note: Python bitness may be incorrect when running in a virtual environment
    

### `def print_diagnostic_information()`

Print diagnostic information in a format suitable for issue report

    note: Python bitness may be incorrect when running in a virtual environment
    

<!--NI_PYTHON_API repo=nimi-python path=generated/nifgen/nifgen/_attributes.py -->
## PYTHON MODULE: generated/nifgen/nifgen/_attributes.py

### `class Attribute(object)`

Base class for all typed attributes.

#### `def __init__(self, attribute_id)`

### `class AttributeViInt32(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeViInt32TimeDeltaMilliseconds(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeViInt32TimeDeltaMonths(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeViInt64(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeViReal64(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeViReal64TimeDeltaSeconds(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeViString(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeViStringRepeatedCapability(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeViStringCommaSeparated(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeViBoolean(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeEnum(Attribute)`

#### `def __init__(self, underlying_attribute_meta_class, enum_meta_class, attribute_id)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeEnumWithConverter(Attribute)`

Class for attributes that use enums internally but are exposed in the nifgen Python module as something else, thus need conversion.

#### `def __init__(self, underlying_attribute_enum, getter_converter, setter_converter)`

Creates and returns an instance of AttributeEnumWithConverter attribute meta class.

        Args:
            underlying_attribute_enum (AttributeEnum): The AttributeEnum instance for the underlying
                enum

            getter_converter (function): The function that converts the enum value to its converted
                value

            setter_converter (function): The function that converts the converted value back to the
                enum value
        

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeSessionReference(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nifgen/nifgen/_converters.py -->
## PYTHON MODULE: generated/nifgen/nifgen/_converters.py

### `def _convert_repeated_capabilities(arg, prefix)`

Base version that should not be called

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
    

### `def _(repeated_capability, prefix)`

Integer version

### `def _(repeated_capability, prefix)`

String version (this is the most complex)

    We need to deal with a range ('0-3' or '0:3'), a list ('0,1,2,3') and a single item
    

### `def _(repeated_capability, prefix)`

Iterable version - can handle lists, ranges, and tuples

### `def _(repeated_capability, prefix)`

slice version

### `def convert_repeated_capabilities(repeated_capability, prefix='')`

Convert a repeated capabilities object to a comma delimited list

    Args:
        repeated_capability (str, list, tuple, slice, None) -
        prefix (str) - common prefix for all strings

    Returns:
        rep_cap_list (list of str) - list of each repeated capability item with ranges expanded and prefix added
    

### `def convert_repeated_capabilities_without_prefix(repeated_capability)`

Convert a repeated capabilities object, without any prefix, to a comma delimited list

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
    

### `def expand_channel_string(channel_string, all_channels_in_session)`

Expands a channel_string to a list of individual channel names.

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
    

### `def _convert_timedelta(value, library_type, scaling)`

### `def convert_timedelta_to_seconds_real64(value)`

### `def convert_timedelta_to_milliseconds_int32(value)`

### `def convert_timedeltas_to_seconds_real64(values)`

### `def convert_seconds_real64_to_timedelta(value)`

### `def convert_seconds_real64_to_timedeltas(values)`

### `def convert_month_to_timedelta(months)`

### `def convert_timedelta_to_months_int32(value)`

### `def convert_init_with_options_dictionary(values)`

### `def _convert_to_bytes(value)`

### `def _(value)`

### `def _(value)`

### `def convert_to_bytes(value)`

### `def convert_comma_separated_string_to_list(comma_separated_string)`

### `def convert_list_to_comma_separated_string(list_of_strings)`

Convert a list or tuple of strings into a comma-separated string.

    Args:
        list_of_strings (list or tuple of str): List or tuple of strings.

    Returns:
        str: Comma-separated string.
    

### `def convert_chained_repeated_capability_to_parts(chained_repeated_capability)`

Convert a chained repeated capabilities string to a list of comma-delimited repeated capabilities string.

    Converter assumes that the input contains the full cartesian product of its parts.
    e.g. If chained_repeated_capability is 'site0/PinA,site0/PinB,site1/PinA,site1/PinB',
    ['site0,site1', 'PinA,PinB'] is returned.

    Args:
        chained_repeated_capability (str) - comma-delimited repeated capabilities string where each
        item is a chain of slash-delimited repeated capabilities

    Returns:
        rep_cap_list (list of str) - list of comma-delimited repeated capabilities string
    

<!--NI_PYTHON_API repo=nimi-python path=generated/nifgen/nifgen/_grpc_stub_interpreter.py -->
## PYTHON MODULE: generated/nifgen/nifgen/_grpc_stub_interpreter.py

### `class GrpcStubInterpreter(object)`

Interpreter for interacting with a gRPC Stub class

#### `def __init__(self, grpc_options)`

#### `def set_session_handle(self, value=session_grpc_types.Session())`

#### `def get_session_handle(self)`

#### `def _invoke(self, func, request, metadata=None)`

#### `def abort(self)`

#### `def allocate_named_waveform(self, channel_name, waveform_name, waveform_size)`

#### `def allocate_waveform(self, channel_name, waveform_size)`

#### `def clear_arb_memory(self)`

#### `def clear_arb_sequence(self, sequence_handle)`

#### `def clear_arb_waveform(self, waveform_handle)`

#### `def clear_freq_list(self, frequency_list_handle)`

#### `def clear_user_standard_waveform(self, channel_name)`

#### `def commit(self)`

#### `def configure_arb_sequence(self, channel_name, sequence_handle, gain, offset)`

#### `def configure_arb_waveform(self, channel_name, waveform_handle, gain, offset)`

#### `def configure_freq_list(self, channel_name, frequency_list_handle, amplitude, dc_offset, start_phase)`

#### `def configure_standard_waveform(self, channel_name, waveform, amplitude, dc_offset, frequency, start_phase)`

#### `def create_advanced_arb_sequence(self, waveform_handles_array, loop_counts_array, sample_counts_array, marker_location_array)`

#### `def create_arb_sequence(self, waveform_handles_array, loop_counts_array)`

#### `def create_freq_list(self, waveform, frequency_array, duration_array)`

#### `def create_waveform_f64(self, channel_name, waveform_data_array)`

#### `def create_waveform_f64_numpy(self, channel_name, waveform_data_array)`

#### `def create_waveform_from_file_f64(self, channel_name, file_name, byte_order)`

#### `def create_waveform_from_file_i16(self, channel_name, file_name, byte_order)`

#### `def create_waveform_i16_numpy(self, channel_name, waveform_data_array)`

#### `def define_user_standard_waveform(self, channel_name, waveform_data_array)`

#### `def delete_named_waveform(self, channel_name, waveform_name)`

#### `def delete_script(self, channel_name, script_name)`

#### `def disable(self)`

#### `def export_attribute_configuration_buffer(self)`

#### `def export_attribute_configuration_file(self, file_path)`

#### `def get_attribute_vi_boolean(self, channel_name, attribute_id)`

#### `def get_attribute_vi_int32(self, channel_name, attribute_id)`

#### `def get_attribute_vi_real64(self, channel_name, attribute_id)`

#### `def get_attribute_vi_string(self, channel_name, attribute_id)`

#### `def get_channel_name(self, index)`

#### `def get_error(self)`

#### `def get_ext_cal_last_date_and_time(self)`

#### `def get_ext_cal_last_temp(self)`

#### `def get_ext_cal_recommended_interval(self)`

#### `def get_hardware_state(self)`

#### `def get_self_cal_last_date_and_time(self)`

#### `def get_self_cal_last_temp(self)`

#### `def get_self_cal_supported(self)`

#### `def import_attribute_configuration_buffer(self, configuration)`

#### `def import_attribute_configuration_file(self, file_path)`

#### `def initialize_with_channels(self, resource_name, channel_name, reset_device, option_string)`

#### `def initiate_generation(self)`

#### `def is_done(self)`

#### `def lock(self)`

#### `def query_arb_seq_capabilities(self)`

#### `def query_arb_wfm_capabilities(self)`

#### `def query_freq_list_capabilities(self)`

#### `def read_current_temperature(self)`

#### `def reset_device(self)`

#### `def reset_with_defaults(self)`

#### `def self_cal(self)`

#### `def send_software_edge_trigger(self, trigger, trigger_id)`

#### `def set_attribute_vi_boolean(self, channel_name, attribute_id, attribute_value)`

#### `def set_attribute_vi_int32(self, channel_name, attribute_id, attribute_value)`

#### `def set_attribute_vi_real64(self, channel_name, attribute_id, attribute_value)`

#### `def set_attribute_vi_string(self, channel_name, attribute_id, attribute_value)`

#### `def set_named_waveform_next_write_position(self, channel_name, waveform_name, relative_to, offset)`

#### `def set_runtime_environment(self, environment, environment_version, reserved1, reserved2)`

#### `def set_waveform_next_write_position(self, channel_name, waveform_handle, relative_to, offset)`

#### `def unlock(self)`

#### `def wait_until_done(self, max_time)`

#### `def write_binary16_waveform_numpy(self, channel_name, waveform_handle, data)`

#### `def write_named_waveform_f64(self, channel_name, waveform_name, data)`

#### `def write_named_waveform_f64_numpy(self, channel_name, waveform_name, data)`

#### `def write_named_waveform_i16_numpy(self, channel_name, waveform_name, data)`

#### `def write_script(self, channel_name, script)`

#### `def write_waveform(self, channel_name, waveform_handle, data)`

#### `def write_waveform_numpy(self, channel_name, waveform_handle, data)`

#### `def close(self)`

#### `def error_message(self, error_code)`

#### `def reset(self)`

#### `def self_test(self)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nifgen/nifgen/_library.py -->
## PYTHON MODULE: generated/nifgen/nifgen/_library.py

### `class Library(object)`

Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    

#### `def __init__(self, ctypes_library)`

#### `def _get_library_function(self, name)`

#### `def niFgen_AbortGeneration(self, vi)`

#### `def niFgen_AllocateNamedWaveform(self, vi, channel_name, waveform_name, waveform_size)`

#### `def niFgen_AllocateWaveform(self, vi, channel_name, waveform_size, waveform_handle)`

#### `def niFgen_ClearArbMemory(self, vi)`

#### `def niFgen_ClearArbSequence(self, vi, sequence_handle)`

#### `def niFgen_ClearArbWaveform(self, vi, waveform_handle)`

#### `def niFgen_ClearFreqList(self, vi, frequency_list_handle)`

#### `def niFgen_ClearUserStandardWaveform(self, vi, channel_name)`

#### `def niFgen_Commit(self, vi)`

#### `def niFgen_ConfigureArbSequence(self, vi, channel_name, sequence_handle, gain, offset)`

#### `def niFgen_ConfigureArbWaveform(self, vi, channel_name, waveform_handle, gain, offset)`

#### `def niFgen_ConfigureFreqList(self, vi, channel_name, frequency_list_handle, amplitude, dc_offset, start_phase)`

#### `def niFgen_ConfigureStandardWaveform(self, vi, channel_name, waveform, amplitude, dc_offset, frequency, start_phase)`

#### `def niFgen_CreateAdvancedArbSequence(self, vi, sequence_length, waveform_handles_array, loop_counts_array, sample_counts_array, marker_location_array, coerced_markers_array, sequence_handle)`

#### `def niFgen_CreateArbSequence(self, vi, sequence_length, waveform_handles_array, loop_counts_array, sequence_handle)`

#### `def niFgen_CreateFreqList(self, vi, waveform, frequency_list_length, frequency_array, duration_array, frequency_list_handle)`

#### `def niFgen_CreateWaveformF64(self, vi, channel_name, waveform_size, waveform_data_array, waveform_handle)`

#### `def niFgen_CreateWaveformFromFileF64(self, vi, channel_name, file_name, byte_order, waveform_handle)`

#### `def niFgen_CreateWaveformFromFileI16(self, vi, channel_name, file_name, byte_order, waveform_handle)`

#### `def niFgen_CreateWaveformI16(self, vi, channel_name, waveform_size, waveform_data_array, waveform_handle)`

#### `def niFgen_DefineUserStandardWaveform(self, vi, channel_name, waveform_size, waveform_data_array)`

#### `def niFgen_DeleteNamedWaveform(self, vi, channel_name, waveform_name)`

#### `def niFgen_DeleteScript(self, vi, channel_name, script_name)`

#### `def niFgen_Disable(self, vi)`

#### `def niFgen_ExportAttributeConfigurationBuffer(self, vi, size_in_bytes, configuration)`

#### `def niFgen_ExportAttributeConfigurationFile(self, vi, file_path)`

#### `def niFgen_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niFgen_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niFgen_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niFgen_GetAttributeViString(self, vi, channel_name, attribute_id, array_size, attribute_value)`

#### `def niFgen_GetChannelName(self, vi, index, buffer_size, channel_string)`

#### `def niFgen_GetError(self, vi, error_code, error_description_buffer_size, error_description)`

#### `def niFgen_GetExtCalLastDateAndTime(self, vi, year, month, day, hour, minute)`

#### `def niFgen_GetExtCalLastTemp(self, vi, temperature)`

#### `def niFgen_GetExtCalRecommendedInterval(self, vi, months)`

#### `def niFgen_GetHardwareState(self, vi, state)`

#### `def niFgen_GetSelfCalLastDateAndTime(self, vi, year, month, day, hour, minute)`

#### `def niFgen_GetSelfCalLastTemp(self, vi, temperature)`

#### `def niFgen_GetSelfCalSupported(self, vi, self_cal_supported)`

#### `def niFgen_ImportAttributeConfigurationBuffer(self, vi, size_in_bytes, configuration)`

#### `def niFgen_ImportAttributeConfigurationFile(self, vi, file_path)`

#### `def niFgen_InitializeWithChannels(self, resource_name, channel_name, reset_device, option_string, vi)`

#### `def niFgen_InitiateGeneration(self, vi)`

#### `def niFgen_IsDone(self, vi, done)`

#### `def niFgen_LockSession(self, vi, caller_has_lock)`

#### `def niFgen_QueryArbSeqCapabilities(self, vi, maximum_number_of_sequences, minimum_sequence_length, maximum_sequence_length, maximum_loop_count)`

#### `def niFgen_QueryArbWfmCapabilities(self, vi, maximum_number_of_waveforms, waveform_quantum, minimum_waveform_size, maximum_waveform_size)`

#### `def niFgen_QueryFreqListCapabilities(self, vi, maximum_number_of_freq_lists, minimum_frequency_list_length, maximum_frequency_list_length, minimum_frequency_list_duration, maximum_frequency_list_duration, frequency_list_duration_quantum)`

#### `def niFgen_ReadCurrentTemperature(self, vi, temperature)`

#### `def niFgen_ResetDevice(self, vi)`

#### `def niFgen_ResetWithDefaults(self, vi)`

#### `def niFgen_SelfCal(self, vi)`

#### `def niFgen_SendSoftwareEdgeTrigger(self, vi, trigger, trigger_id)`

#### `def niFgen_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niFgen_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niFgen_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niFgen_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niFgen_SetNamedWaveformNextWritePosition(self, vi, channel_name, waveform_name, relative_to, offset)`

#### `def niFgen_SetRuntimeEnvironment(self, environment, environment_version, reserved1, reserved2)`

#### `def niFgen_SetWaveformNextWritePosition(self, vi, channel_name, waveform_handle, relative_to, offset)`

#### `def niFgen_UnlockSession(self, vi, caller_has_lock)`

#### `def niFgen_WaitUntilDone(self, vi, max_time)`

#### `def niFgen_WriteBinary16Waveform(self, vi, channel_name, waveform_handle, size, data)`

#### `def niFgen_WriteNamedWaveformF64(self, vi, channel_name, waveform_name, size, data)`

#### `def niFgen_WriteNamedWaveformI16(self, vi, channel_name, waveform_name, size, data)`

#### `def niFgen_WriteScript(self, vi, channel_name, script)`

#### `def niFgen_WriteWaveform(self, vi, channel_name, waveform_handle, size, data)`

#### `def niFgen_close(self, vi)`

#### `def niFgen_error_message(self, vi, error_code, error_message)`

#### `def niFgen_reset(self, vi)`

#### `def niFgen_self_test(self, vi, self_test_result, self_test_message)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nifgen/nifgen/_library_interpreter.py -->
## PYTHON MODULE: generated/nifgen/nifgen/_library_interpreter.py

### `def _get_ctypes_pointer_for_buffer(value=None, library_type=None, size=None)`

### `def _convert_to_array(value, array_type)`

### `class LibraryInterpreter(object)`

Library C<->Python interpreter.

    This class is responsible for interpreting the Library's C API. It is responsible for:
    * Converting ctypes to native Python types.
    * Dealing with string encoding.
    * Allocating memory.
    * Converting errors returned by Library into Python exceptions.
    

#### `def __init__(self, encoding)`

#### `def set_session_handle(self, value=0)`

#### `def get_session_handle(self)`

#### `def get_error_description(self, error_code)`

get_error_description

        Returns the error description.
        

#### `def abort(self)`

#### `def allocate_named_waveform(self, channel_name, waveform_name, waveform_size)`

#### `def allocate_waveform(self, channel_name, waveform_size)`

#### `def clear_arb_memory(self)`

#### `def clear_arb_sequence(self, sequence_handle)`

#### `def clear_arb_waveform(self, waveform_handle)`

#### `def clear_freq_list(self, frequency_list_handle)`

#### `def clear_user_standard_waveform(self, channel_name)`

#### `def commit(self)`

#### `def configure_arb_sequence(self, channel_name, sequence_handle, gain, offset)`

#### `def configure_arb_waveform(self, channel_name, waveform_handle, gain, offset)`

#### `def configure_freq_list(self, channel_name, frequency_list_handle, amplitude, dc_offset, start_phase)`

#### `def configure_standard_waveform(self, channel_name, waveform, amplitude, dc_offset, frequency, start_phase)`

#### `def create_advanced_arb_sequence(self, waveform_handles_array, loop_counts_array, sample_counts_array, marker_location_array)`

#### `def create_arb_sequence(self, waveform_handles_array, loop_counts_array)`

#### `def create_freq_list(self, waveform, frequency_array, duration_array)`

#### `def create_waveform_f64(self, channel_name, waveform_data_array)`

#### `def create_waveform_f64_numpy(self, channel_name, waveform_data_array)`

#### `def create_waveform_from_file_f64(self, channel_name, file_name, byte_order)`

#### `def create_waveform_from_file_i16(self, channel_name, file_name, byte_order)`

#### `def create_waveform_i16_numpy(self, channel_name, waveform_data_array)`

#### `def define_user_standard_waveform(self, channel_name, waveform_data_array)`

#### `def delete_named_waveform(self, channel_name, waveform_name)`

#### `def delete_script(self, channel_name, script_name)`

#### `def disable(self)`

#### `def export_attribute_configuration_buffer(self)`

#### `def export_attribute_configuration_file(self, file_path)`

#### `def get_attribute_vi_boolean(self, channel_name, attribute_id)`

#### `def get_attribute_vi_int32(self, channel_name, attribute_id)`

#### `def get_attribute_vi_real64(self, channel_name, attribute_id)`

#### `def get_attribute_vi_string(self, channel_name, attribute_id)`

#### `def get_channel_name(self, index)`

#### `def get_error(self)`

#### `def get_ext_cal_last_date_and_time(self)`

#### `def get_ext_cal_last_temp(self)`

#### `def get_ext_cal_recommended_interval(self)`

#### `def get_hardware_state(self)`

#### `def get_self_cal_last_date_and_time(self)`

#### `def get_self_cal_last_temp(self)`

#### `def get_self_cal_supported(self)`

#### `def import_attribute_configuration_buffer(self, configuration)`

#### `def import_attribute_configuration_file(self, file_path)`

#### `def initialize_with_channels(self, resource_name, channel_name, reset_device, option_string)`

#### `def initiate_generation(self)`

#### `def is_done(self)`

#### `def lock(self)`

#### `def query_arb_seq_capabilities(self)`

#### `def query_arb_wfm_capabilities(self)`

#### `def query_freq_list_capabilities(self)`

#### `def read_current_temperature(self)`

#### `def reset_device(self)`

#### `def reset_with_defaults(self)`

#### `def self_cal(self)`

#### `def send_software_edge_trigger(self, trigger, trigger_id)`

#### `def set_attribute_vi_boolean(self, channel_name, attribute_id, attribute_value)`

#### `def set_attribute_vi_int32(self, channel_name, attribute_id, attribute_value)`

#### `def set_attribute_vi_real64(self, channel_name, attribute_id, attribute_value)`

#### `def set_attribute_vi_string(self, channel_name, attribute_id, attribute_value)`

#### `def set_named_waveform_next_write_position(self, channel_name, waveform_name, relative_to, offset)`

#### `def set_runtime_environment(self, environment, environment_version, reserved1, reserved2)`

#### `def set_waveform_next_write_position(self, channel_name, waveform_handle, relative_to, offset)`

#### `def unlock(self)`

#### `def wait_until_done(self, max_time)`

#### `def write_binary16_waveform_numpy(self, channel_name, waveform_handle, data)`

#### `def write_named_waveform_f64(self, channel_name, waveform_name, data)`

#### `def write_named_waveform_f64_numpy(self, channel_name, waveform_name, data)`

#### `def write_named_waveform_i16_numpy(self, channel_name, waveform_name, data)`

#### `def write_script(self, channel_name, script)`

#### `def write_waveform(self, channel_name, waveform_handle, data)`

#### `def write_waveform_numpy(self, channel_name, waveform_handle, data)`

#### `def close(self)`

#### `def error_message(self, error_code)`

#### `def reset(self)`

#### `def self_test(self)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nifgen/nifgen/_library_singleton.py -->
## PYTHON MODULE: generated/nifgen/nifgen/_library_singleton.py

### `def _get_library_name()`

### `def _get_library_type()`

### `def get()`

get

    Returns the library.Library singleton for nifgen.
    

<!--NI_PYTHON_API repo=nimi-python path=generated/nifgen/nifgen/enums.py -->
## PYTHON MODULE: generated/nifgen/nifgen/enums.py

### `class AnalogPath(Enum)`

### `class BusType(Enum)`

### `class ByteOrder(Enum)`

### `class ClockMode(Enum)`

### `class DataMarkerEventLevelPolarity(Enum)`

### `class EventPulseWidthUnits(Enum)`

### `class HardwareState(Enum)`

### `class IdleBehavior(Enum)`

### `class OutputMode(Enum)`

### `class ReferenceClockSource(Enum)`

### `class RelativeTo(Enum)`

### `class SampleClockSource(Enum)`

### `class SampleClockTimebaseSource(Enum)`

### `class ScriptTriggerDigitalEdgeEdge(Enum)`

### `class ScriptTriggerType(Enum)`

### `class StartTriggerDigitalEdgeEdge(Enum)`

### `class StartTriggerType(Enum)`

### `class TerminalConfiguration(Enum)`

### `class Trigger(Enum)`

### `class TriggerMode(Enum)`

### `class WaitBehavior(Enum)`

### `class Waveform(Enum)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nifgen/nifgen/errors.py -->
## PYTHON MODULE: generated/nifgen/nifgen/errors.py

### `def _is_success(code)`

### `def _is_error(code)`

### `def _is_warning(code)`

### `class Error(Exception)`

Base error class for NI-FGEN

#### `def __init__(self, message)`

### `class DriverError(Error)`

An error originating from the NI-FGEN driver

#### `def __init__(self, code, description)`

### `class DriverWarning(Warning)`

A warning originating from the NI-FGEN driver

#### `def __init__(self, code, description)`

### `class RpcError(Error)`

An error specific to sessions to the NI gRPC Device Server

#### `def __init__(self, rpc_code, description)`

### `class UnsupportedConfigurationError(Error)`

An error due to using this module in an usupported platform.

#### `def __init__(self)`

### `class DriverNotInstalledError(Error)`

An error due to using this module without the driver runtime installed.

#### `def __init__(self)`

### `class DriverTooOldError(Error)`

An error due to using this module with an older version of the NI-FGEN driver runtime.

#### `def __init__(self)`

### `class DriverTooNewError(Error)`

An error due to the NI-FGEN driver runtime being too new for this module.

#### `def __init__(self)`

### `class InvalidRepeatedCapabilityError(Error)`

An error due to an invalid character in a repeated capability

#### `def __init__(self, invalid_character, invalid_string)`

### `class SelfTestError(Error)`

An error due to a failed self-test

#### `def __init__(self, code, msg)`

### `def handle_error(library_interpreter, code, ignore_warnings, is_error_handling)`

handle_error

    Helper function for handling errors returned by nifgen.Library.
    It calls back into the LibraryInterpreter to get the corresponding error
    description and raises if necessary.
    

<!--NI_PYTHON_API repo=nimi-python path=generated/nifgen/nifgen/grpc_session_options.py -->
## PYTHON MODULE: generated/nifgen/nifgen/grpc_session_options.py

- `GRPC_SERVICE_INTERFACE_NAME = 'nifgen_grpc.NiFgen'`

- `MEASUREMENTLINK_23Q1_NIMI_PYTHON_API_KEY = 'DE10751B-3EE0-44EC-A93B-800E6A3C89E4'`

### `class SessionInitializationBehavior(IntEnum)`

### `class GrpcSessionOptions(object)`

Collection of options that specifies session behaviors related to gRPC.

#### `def __init__(self, grpc_channel, session_name, *, api_key=MEASUREMENTLINK_23Q1_NIMI_PYTHON_API_KEY, initialization_behavior=SessionInitializationBehavior.AUTO)`

Collection of options that specifies session behaviors related to gRPC.

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
        

<!--NI_PYTHON_API repo=nimi-python path=generated/nifgen/nifgen/nidevice_pb2.py -->
## PYTHON MODULE: generated/nifgen/nifgen/nidevice_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0enidevice.proto\x12\rnidevice_grpc"2\n\x0fNIComplexNumber\x12\x0c\n\x04real\x18\x01 \x01(\x01\x12\x11\n\timaginary\x18\x02 \x01(\x01"5\n\x12NIComplexNumberF32\x12\x0c\n\x04real\x18\x01 \x01(\x02\x12\x11\n\timaginary\x18\x02 \x01(\x02"/\n\x0cNIComplexI16\x12\x0c\n\x04real\x18\x01 \x01(\x11\x12\x11\n\timaginary\x18\x02 \x01(\x11"r\n\x0fSmtSpectrumInfo\x12\x15\n\rspectrum_type\x18\x01 \x01(\r\x12\x11\n\tlinear_db\x18\x02 \x01(\r\x12\x0e\n\x06window\x18\x03 \x01(\r\x12\x13\n\x0bwindow_size\x18\x04 \x01(\x11\x12\x10\n\x08fft_size\x18\x05 \x01(\x11BB\n\x12com.ni.grpc.deviceB\x08NiDeviceP\x01\xaa\x02\x1fNationalInstruments.Grpc.Deviceb\x06proto3')`

<!--NI_PYTHON_API repo=nimi-python path=generated/nifgen/nifgen/nidevice_pb2_grpc.py -->
## PYTHON MODULE: generated/nifgen/nifgen/nidevice_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

<!--NI_PYTHON_API repo=nimi-python path=generated/nifgen/nifgen/nifgen_pb2.py -->
## PYTHON MODULE: generated/nifgen/nifgen/nifgen_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cnifgen.proto\x12\x0bnifgen_grpc\x1a\x0enidevice.proto\x1a\rsession.proto"\xb1\x01\n\x0bInitRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\x10\n\x08id_query\x18\x03 \x01(\x08\x12\x14\n\x0creset_device\x18\x04 \x01(\x08\x12M\n\x17initialization_behavior\x18\x05 \x01(\x0e2,.nidevice_grpc.SessionInitializationBehavior"~\n\x0cInitResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12"\n\x02vi\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x19\n\rerror_message\x18\x03 \x01(\tB\x02\x18\x01\x12\x1f\n\x17new_session_initialized\x18\x04 \x01(\x08"\xd3\x01\n\x16InitWithOptionsRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\x10\n\x08id_query\x18\x03 \x01(\x08\x12\x14\n\x0creset_device\x18\x04 \x01(\x08\x12\x15\n\roption_string\x18\x05 \x01(\t\x12M\n\x17initialization_behavior\x18\x06 \x01(\x0e2,.nidevice_grpc.SessionInitializationBehavior"\x89\x01\n\x17InitWithOptionsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12"\n\x02vi\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x19\n\rerror_message\x18\x03 \x01(\tB\x02\x18\x01\x12\x1f\n\x17new_session_initialized\x18\x04 \x01(\x08"\xde\x01\n\x1dInitializeWithChannelsRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\x14\n\x0cchannel_name\x18\x03 \x01(\t\x12\x14\n\x0creset_device\x18\x04 \x01(\x08\x12\x15\n\roption_string\x18\x05 \x01(\t\x12M\n\x17initialization_behavior\x18\x06 \x01(\x0e2,.nidevice_grpc.SessionInitializationBehavior"\x90\x01\n\x1eInitializeWithChannelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12"\n\x02vi\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x19\n\rerror_message\x18\x03 \x01(\tB\x02\x18\x01\x12\x1f\n\x17new_session_initialized\x18\x04 \x01(\x08"2\n\x0cCloseRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\x1f\n\rCloseResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"2\n\x0cResetRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\x1f\n\rResetResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"5\n\x0fSelfTestRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"W\n\x10SelfTestResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x18\n\x10self_test_result\x18\x02 \x01(\x11\x12\x19\n\x11self_test_message\x18\x03 \x01(\t"7\n\x11ErrorQueryRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"O\n\x12ErrorQueryResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nerror_code\x18\x02 \x01(\x11\x12\x15\n\rerror_message\x18\x03 \x01(\t"M\n\x13ErrorMessageRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x12\n\nerror_code\x18\x02 \x01(\x11"=\n\x14ErrorMessageResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rerror_message\x18\x02 \x01(\t":\n\x14RevisionQueryRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"f\n\x15RevisionQueryResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12"\n\x1ainstrument_driver_revision\x18\x02 \x01(\t\x12\x19\n\x11firmware_revision\x18\x03 \x01(\t"5\n\x0fGetErrorRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"Q\n\x10GetErrorResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nerror_code\x18\x02 \x01(\x11\x12\x19\n\x11error_description\x18\x03 \x01(\t"7\n\x11ClearErrorRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"$\n\x12ClearErrorResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"M\n\x13ErrorHandlerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x12\n\nerror_code\x18\x02 \x01(\x11"=\n\x14ErrorHandlerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rerror_message\x18\x02 \x01(\t"J\n\x15GetChannelNameRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\r\n\x05index\x18\x02 \x01(\x11"@\n\x16GetChannelNameResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x16\n\x0echannel_string\x18\x02 \x01(\t"B\n\x1cResetInterchangeCheckRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"/\n\x1dResetInterchangeCheckResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"E\n\x1fClearInterchangeWarningsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"2\n ClearInterchangeWarningsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"D\n\x1eInvalidateAllAttributesRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"1\n\x1fInvalidateAllAttributesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05">\n\x18ResetWithDefaultsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"+\n\x19ResetWithDefaultsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"4\n\x0eDisableRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"!\n\x0fDisableResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"3\n\rCommitRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session" \n\x0eCommitResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"=\n\x17GetHardwareStateRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"h\n\x18GetHardwareStateResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12)\n\x05state\x18\x02 \x01(\x0e2\x1a.nifgen_grpc.HardwareState\x12\x11\n\tstate_raw\x18\x03 \x01(\x11"L\n\x14WaitUntilDoneRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x10\n\x08max_time\x18\x02 \x01(\x11"\'\n\x15WaitUntilDoneResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"3\n\rIsDoneRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session".\n\x0eIsDoneResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04done\x18\x02 \x01(\x08"8\n\x12ResetDeviceRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"%\n\x13ResetDeviceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"q\n\x1dConfigureOperationModeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x16\n\x0eoperation_mode\x18\x03 \x01(\x11"0\n\x1eConfigureOperationModeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x9f\x01\n\x1aConfigureOutputModeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12.\n\x0boutput_mode\x18\x02 \x01(\x0e2\x17.nifgen_grpc.OutputModeH\x00\x12\x19\n\x0foutput_mode_raw\x18\x03 \x01(\x11H\x00B\x12\n\x10output_mode_enum"-\n\x1bConfigureOutputModeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x87\x01\n\x1eConfigureReferenceClockRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1e\n\x16reference_clock_source\x18\x02 \x01(\t\x12!\n\x19reference_clock_frequency\x18\x03 \x01(\x01"1\n\x1fConfigureReferenceClockResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"n\n\x1fConfigureOutputImpedanceRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x11\n\timpedance\x18\x03 \x01(\x01"2\n ConfigureOutputImpedanceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"j\n\x1dConfigureOutputEnabledRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x0f\n\x07enabled\x18\x03 \x01(\x08"0\n\x1eConfigureOutputEnabledResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"P\n\x18ConfigureChannelsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x10\n\x08channels\x18\x02 \x01(\t"+\n\x19ConfigureChannelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"?\n\x19InitiateGenerationRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session",\n\x1aInitiateGenerationResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"<\n\x16AbortGenerationRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session")\n\x17AbortGenerationResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xfe\x01\n ConfigureStandardWaveformRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12)\n\x08waveform\x18\x03 \x01(\x0e2\x15.nifgen_grpc.WaveformH\x00\x12\x16\n\x0cwaveform_raw\x18\x04 \x01(\x11H\x00\x12\x11\n\tamplitude\x18\x05 \x01(\x01\x12\x11\n\tdc_offset\x18\x06 \x01(\x01\x12\x11\n\tfrequency\x18\x07 \x01(\x01\x12\x13\n\x0bstart_phase\x18\x08 \x01(\x01B\x0f\n\rwaveform_enum"3\n!ConfigureStandardWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"z\n!DefineUserStandardWaveformRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x1b\n\x13waveform_data_array\x18\x03 \x03(\x01"4\n"DefineUserStandardWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\\\n ClearUserStandardWaveformRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t"3\n!ClearUserStandardWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"h\n\x19ConfigureFrequencyRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x11\n\tfrequency\x18\x03 \x01(\x01",\n\x1aConfigureFrequencyResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"h\n\x19ConfigureAmplitudeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x11\n\tamplitude\x18\x03 \x01(\x01",\n\x1aConfigureAmplitudeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"D\n\x1eQueryArbWfmCapabilitiesRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\xae\x01\n\x1fQueryArbWfmCapabilitiesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12#\n\x1bmaximum_number_of_waveforms\x18\x02 \x01(\x11\x12\x18\n\x10waveform_quantum\x18\x03 \x01(\x11\x12\x1d\n\x15minimum_waveform_size\x18\x04 \x01(\x11\x12\x1d\n\x15maximum_waveform_size\x18\x05 \x01(\x11"q\n\x18CreateWaveformF64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x1b\n\x13waveform_data_array\x18\x03 \x03(\x01"D\n\x19CreateWaveformF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fwaveform_handle\x18\x02 \x01(\x11"q\n\x18CreateWaveformI16Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x1b\n\x13waveform_data_array\x18\x03 \x03(\x11"D\n\x19CreateWaveformI16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fwaveform_handle\x18\x02 \x01(\x11"\x98\x01\n\x1fCreateWaveformComplexF64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12;\n\x13waveform_data_array\x18\x03 \x03(\x0b2\x1e.nidevice_grpc.NIComplexNumber"K\n CreateWaveformComplexF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fwaveform_handle\x18\x02 \x01(\x11"\xca\x01\n CreateWaveformFromFileI16Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x11\n\tfile_name\x18\x03 \x01(\t\x12,\n\nbyte_order\x18\x04 \x01(\x0e2\x16.nifgen_grpc.ByteOrderH\x00\x12\x18\n\x0ebyte_order_raw\x18\x05 \x01(\x11H\x00B\x11\n\x0fbyte_order_enum"L\n!CreateWaveformFromFileI16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fwaveform_handle\x18\x02 \x01(\x11"\xca\x01\n CreateWaveformFromFileF64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x11\n\tfile_name\x18\x03 \x01(\t\x12,\n\nbyte_order\x18\x04 \x01(\x0e2\x16.nifgen_grpc.ByteOrderH\x00\x12\x18\n\x0ebyte_order_raw\x18\x05 \x01(\x11H\x00B\x11\n\x0fbyte_order_enum"L\n!CreateWaveformFromFileF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fwaveform_handle\x18\x02 \x01(\x11"U\n\x1aConfigureSampleRateRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x13\n\x0bsample_rate\x18\x02 \x01(\x01"-\n\x1bConfigureSampleRateResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x8e\x01\n\x1bConfigureArbWaveformRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x17\n\x0fwaveform_handle\x18\x03 \x01(\x11\x12\x0c\n\x04gain\x18\x04 \x01(\x01\x12\x0e\n\x06offset\x18\x05 \x01(\x01".\n\x1cConfigureArbWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xac\x01\n\x17ClearArbWaveformRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x126\n\x0fwaveform_handle\x18\x02 \x01(\x0e2\x1b.nifgen_grpc.WaveformHandleH\x00\x12\x1d\n\x13waveform_handle_raw\x18\x03 \x01(\x11H\x00B\x16\n\x14waveform_handle_enum"*\n\x18ClearArbWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x86\x01\n\x1cAllocateNamedWaveformRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x15\n\rwaveform_name\x18\x03 \x01(\t\x12\x15\n\rwaveform_size\x18\x04 \x01(\x11"/\n\x1dAllocateNamedWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xea\x01\n(SetNamedWaveformNextWritePositionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x15\n\rwaveform_name\x18\x03 \x01(\t\x12.\n\x0brelative_to\x18\x04 \x01(\x0e2\x17.nifgen_grpc.RelativeToH\x00\x12\x19\n\x0frelative_to_raw\x18\x05 \x01(\x11H\x00\x12\x0e\n\x06offset\x18\x06 \x01(\x11B\x12\n\x10relative_to_enum";\n)SetNamedWaveformNextWritePositionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"}\n\x1cWriteNamedWaveformF64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x15\n\rwaveform_name\x18\x03 \x01(\t\x12\x0c\n\x04data\x18\x04 \x03(\x01"/\n\x1dWriteNamedWaveformF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"}\n\x1cWriteNamedWaveformI16Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x15\n\rwaveform_name\x18\x03 \x01(\t\x12\x0c\n\x04data\x18\x04 \x03(\x11"/\n\x1dWriteNamedWaveformI16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa4\x01\n#WriteNamedWaveformComplexF64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x15\n\rwaveform_name\x18\x03 \x01(\t\x12,\n\x04data\x18\x04 \x03(\x0b2\x1e.nidevice_grpc.NIComplexNumber"6\n$WriteNamedWaveformComplexF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa1\x01\n#WriteNamedWaveformComplexI16Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x15\n\rwaveform_name\x18\x03 \x01(\t\x12)\n\x04data\x18\x04 \x03(\x0b2\x1b.nidevice_grpc.NIComplexI16"6\n$WriteNamedWaveformComplexI16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"m\n\x1aDeleteNamedWaveformRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x15\n\rwaveform_name\x18\x03 \x01(\t"-\n\x1bDeleteNamedWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"D\n\x1eQueryArbSeqCapabilitiesRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\xb4\x01\n\x1fQueryArbSeqCapabilitiesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12#\n\x1bmaximum_number_of_sequences\x18\x02 \x01(\x11\x12\x1f\n\x17minimum_sequence_length\x18\x03 \x01(\x11\x12\x1f\n\x17maximum_sequence_length\x18\x04 \x01(\x11\x12\x1a\n\x12maximum_loop_count\x18\x05 \x01(\x11"y\n\x18CreateArbSequenceRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1e\n\x16waveform_handles_array\x18\x02 \x03(\x11\x12\x19\n\x11loop_counts_array\x18\x03 \x03(\x11"D\n\x19CreateArbSequenceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fsequence_handle\x18\x02 \x01(\x11"\xbd\x01\n CreateAdvancedArbSequenceRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1e\n\x16waveform_handles_array\x18\x02 \x03(\x11\x12\x19\n\x11loop_counts_array\x18\x03 \x03(\x11\x12\x1b\n\x13sample_counts_array\x18\x04 \x03(\x11\x12\x1d\n\x15marker_location_array\x18\x05 \x03(\x11"k\n!CreateAdvancedArbSequenceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1d\n\x15coerced_markers_array\x18\x02 \x03(\x11\x12\x17\n\x0fsequence_handle\x18\x03 \x01(\x11"\x8e\x01\n\x1bConfigureArbSequenceRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x17\n\x0fsequence_handle\x18\x03 \x01(\x11\x12\x0c\n\x04gain\x18\x04 \x01(\x01\x12\x0e\n\x06offset\x18\x05 \x01(\x01".\n\x1cConfigureArbSequenceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xac\x01\n\x17ClearArbSequenceRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x126\n\x0fsequence_handle\x18\x02 \x01(\x0e2\x1b.nifgen_grpc.SequenceHandleH\x00\x12\x1d\n\x13sequence_handle_raw\x18\x03 \x01(\x11H\x00B\x16\n\x14sequence_handle_enum"*\n\x18ClearArbSequenceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05";\n\x15ClearArbMemoryRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"(\n\x16ClearArbMemoryResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"F\n QueryFreqListCapabilitiesRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\xa2\x02\n!QueryFreqListCapabilitiesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12$\n\x1cmaximum_number_of_freq_lists\x18\x02 \x01(\x11\x12%\n\x1dminimum_frequency_list_length\x18\x03 \x01(\x11\x12%\n\x1dmaximum_frequency_list_length\x18\x04 \x01(\x11\x12\'\n\x1fminimum_frequency_list_duration\x18\x05 \x01(\x01\x12\'\n\x1fmaximum_frequency_list_duration\x18\x06 \x01(\x01\x12\'\n\x1ffrequency_list_duration_quantum\x18\x07 \x01(\x01"\xc0\x01\n\x15CreateFreqListRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12)\n\x08waveform\x18\x02 \x01(\x0e2\x15.nifgen_grpc.WaveformH\x00\x12\x16\n\x0cwaveform_raw\x18\x03 \x01(\x11H\x00\x12\x17\n\x0ffrequency_array\x18\x04 \x03(\x01\x12\x16\n\x0eduration_array\x18\x05 \x03(\x01B\x0f\n\rwaveform_enum"G\n\x16CreateFreqListResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1d\n\x15frequency_list_handle\x18\x02 \x01(\x11"\xae\x01\n\x18ConfigureFreqListRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x1d\n\x15frequency_list_handle\x18\x03 \x01(\x11\x12\x11\n\tamplitude\x18\x04 \x01(\x01\x12\x11\n\tdc_offset\x18\x05 \x01(\x01\x12\x13\n\x0bstart_phase\x18\x06 \x01(\x01"+\n\x19ConfigureFreqListResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xc1\x01\n\x14ClearFreqListRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12B\n\x15frequency_list_handle\x18\x02 \x01(\x0e2!.nifgen_grpc.FrequencyListOptionsH\x00\x12#\n\x19frequency_list_handle_raw\x18\x03 \x01(\x11H\x00B\x1c\n\x1afrequency_list_handle_enum"\'\n\x15ClearFreqListResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"^\n\x12WriteScriptRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x0e\n\x06script\x18\x03 \x01(\t"%\n\x13WriteScriptResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"d\n\x13DeleteScriptRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x13\n\x0bscript_name\x18\x03 \x01(\t"&\n\x14DeleteScriptResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb9\x01\n\x13ExportSignalRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12%\n\x06signal\x18\x02 \x01(\x0e2\x13.nifgen_grpc.SignalH\x00\x12\x14\n\nsignal_raw\x18\x03 \x01(\x11H\x00\x12\x19\n\x11signal_identifier\x18\x04 \x01(\t\x12\x17\n\x0foutput_terminal\x18\x05 \x01(\tB\r\n\x0bsignal_enum"&\n\x14ExportSignalResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb5\x02\n\x15RouteSignalOutRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x129\n\x11route_signal_from\x18\x03 \x01(\x0e2\x1c.nifgen_grpc.RouteSignalFromH\x00\x12\x1f\n\x15route_signal_from_raw\x18\x04 \x01(\x11H\x00\x125\n\x0froute_signal_to\x18\x05 \x01(\x0e2\x1a.nifgen_grpc.RouteSignalToH\x01\x12\x1d\n\x13route_signal_to_raw\x18\x06 \x01(\x11H\x01B\x18\n\x16route_signal_from_enumB\x16\n\x14route_signal_to_enum"(\n\x16RouteSignalOutResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa8\x01\n\x1eSendSoftwareEdgeTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\'\n\x07trigger\x18\x02 \x01(\x0e2\x14.nifgen_grpc.TriggerH\x00\x12\x15\n\x0btrigger_raw\x18\x03 \x01(\x11H\x00\x12\x12\n\ntrigger_id\x18\x04 \x01(\tB\x0e\n\x0ctrigger_enum"1\n\x1fSendSoftwareEdgeTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"k\n\'ConfigureDigitalEdgeStartTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0e\n\x06source\x18\x02 \x01(\t\x12\x0c\n\x04edge\x18\x03 \x01(\x11":\n(ConfigureDigitalEdgeStartTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"N\n(ConfigureSoftwareEdgeStartTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session";\n)ConfigureSoftwareEdgeStartTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"@\n\x1aDisableStartTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"-\n\x1bDisableStartTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"z\n/ConfigureP2PEndpointFullnessStartTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12#\n\x1bp2p_endpoint_fullness_level\x18\x02 \x01(\x11"B\n0ConfigureP2PEndpointFullnessStartTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x80\x01\n(ConfigureDigitalEdgeScriptTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x12\n\ntrigger_id\x18\x02 \x01(\t\x12\x0e\n\x06source\x18\x03 \x01(\t\x12\x0c\n\x04edge\x18\x04 \x01(\x11";\n)ConfigureDigitalEdgeScriptTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xd6\x01\n)ConfigureDigitalLevelScriptTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x12\n\ntrigger_id\x18\x02 \x01(\t\x12\x0e\n\x06source\x18\x03 \x01(\t\x120\n\x0ctrigger_when\x18\x04 \x01(\x0e2\x18.nifgen_grpc.TriggerWhenH\x00\x12\x1a\n\x10trigger_when_raw\x18\x05 \x01(\x11H\x00B\x13\n\x11trigger_when_enum"<\n*ConfigureDigitalLevelScriptTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"c\n)ConfigureSoftwareEdgeScriptTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x12\n\ntrigger_id\x18\x02 \x01(\t"<\n*ConfigureSoftwareEdgeScriptTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"U\n\x1bDisableScriptTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x12\n\ntrigger_id\x18\x02 \x01(\t".\n\x1cDisableScriptTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x9a\x01\n\x19ConfigureClockModeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12,\n\nclock_mode\x18\x02 \x01(\x0e2\x16.nifgen_grpc.ClockModeH\x00\x12\x18\n\x0eclock_mode_raw\x18\x03 \x01(\x11H\x00B\x11\n\x0fclock_mode_enum",\n\x1aConfigureClockModeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"d\n%AdjustSampleClockRelativeDelayRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x17\n\x0fadjustment_time\x18\x02 \x01(\x01"8\n&AdjustSampleClockRelativeDelayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"j\n\x17AllocateWaveformRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x15\n\rwaveform_size\x18\x03 \x01(\x11"C\n\x18AllocateWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fwaveform_handle\x18\x02 \x01(\x11"\xe7\x01\n#SetWaveformNextWritePositionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x17\n\x0fwaveform_handle\x18\x03 \x01(\x11\x12.\n\x0brelative_to\x18\x04 \x01(\x0e2\x17.nifgen_grpc.RelativeToH\x00\x12\x19\n\x0frelative_to_raw\x18\x05 \x01(\x11H\x00\x12\x0e\n\x06offset\x18\x06 \x01(\x11B\x12\n\x10relative_to_enum"6\n$SetWaveformNextWritePositionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"w\n\x14WriteWaveformRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x17\n\x0fwaveform_handle\x18\x03 \x01(\x11\x12\x0c\n\x04data\x18\x04 \x03(\x01"\'\n\x15WriteWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x7f\n\x1cWriteBinary16WaveformRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x17\n\x0fwaveform_handle\x18\x03 \x01(\x11\x12\x0c\n\x04data\x18\x04 \x03(\x11"/\n\x1dWriteBinary16WaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa1\x01\n\x1eWriteWaveformComplexF64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12,\n\x04data\x18\x03 \x03(\x0b2\x1e.nidevice_grpc.NIComplexNumber\x12\x17\n\x0fwaveform_handle\x18\x04 \x01(\x11"1\n\x1fWriteWaveformComplexF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa3\x01\n#WriteComplexBinary16WaveformRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x17\n\x0fwaveform_handle\x18\x03 \x01(\x11\x12)\n\x04data\x18\x04 \x03(\x0b2\x1b.nidevice_grpc.NIComplexI16"6\n$WriteComplexBinary16WaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"4\n\x0eSelfCalRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"!\n\x0fSelfCalResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"@\n\x1aGetSelfCalSupportedRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"I\n\x1bGetSelfCalSupportedResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1a\n\x12self_cal_supported\x18\x02 \x01(\x08"F\n GetSelfCalLastDateAndTimeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"{\n!GetSelfCalLastDateAndTimeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04year\x18\x02 \x01(\x11\x12\r\n\x05month\x18\x03 \x01(\x11\x12\x0b\n\x03day\x18\x04 \x01(\x11\x12\x0c\n\x04hour\x18\x05 \x01(\x11\x12\x0e\n\x06minute\x18\x06 \x01(\x11"E\n\x1fGetExtCalLastDateAndTimeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"z\n GetExtCalLastDateAndTimeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04year\x18\x02 \x01(\x11\x12\r\n\x05month\x18\x03 \x01(\x11\x12\x0b\n\x03day\x18\x04 \x01(\x11\x12\x0c\n\x04hour\x18\x05 \x01(\x11\x12\x0e\n\x06minute\x18\x06 \x01(\x11"?\n\x19GetSelfCalLastTempRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"A\n\x1aGetSelfCalLastTempResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0btemperature\x18\x02 \x01(\x01">\n\x18GetExtCalLastTempRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"@\n\x19GetExtCalLastTempResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0btemperature\x18\x02 \x01(\x01"I\n#GetExtCalRecommendedIntervalRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"F\n$GetExtCalRecommendedIntervalResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0e\n\x06months\x18\x02 \x01(\x11"C\n\x1dReadCurrentTemperatureRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"E\n\x1eReadCurrentTemperatureResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0btemperature\x18\x02 \x01(\x01"\x83\x01\n+ConfigureCustomFIRFilterCoefficientsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x1a\n\x12coefficients_array\x18\x03 \x03(\x01">\n,ConfigureCustomFIRFilterCoefficientsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"[\n\x1fGetFIRFilterCoefficientsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t"s\n GetFIRFilterCoefficientsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1a\n\x12coefficients_array\x18\x02 \x03(\x01\x12#\n\x1bnumber_of_coefficients_read\x18\x03 \x01(\x11"]\n\x1eGetStreamEndpointHandleRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x17\n\x0fstream_endpoint\x18\x02 \x01(\t"H\n\x1fGetStreamEndpointHandleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rreader_handle\x18\x02 \x01(\r"n\n\x1aWriteP2PEndpointI16Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rendpoint_name\x18\x02 \x01(\t\x12\x15\n\rendpoint_data\x18\x03 \x03(\x11"-\n\x1bWriteP2PEndpointI16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"{\n\x1fConfigureSynchronizationRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x1e\n\x16synchronization_source\x18\x03 \x01(\x11"2\n ConfigureSynchronizationResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"Z\n\x1eEnableDigitalPatterningRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t"1\n\x1fEnableDigitalPatterningResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"[\n\x1fDisableDigitalPatterningRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t"2\n DisableDigitalPatterningResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"V\n\x1aEnableDigitalFilterRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t"-\n\x1bEnableDigitalFilterResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"W\n\x1bDisableDigitalFilterRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t".\n\x1cDisableDigitalFilterResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"z\n\x19EnableAnalogFilterRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12#\n\x1bfilter_correction_frequency\x18\x03 \x01(\x01",\n\x1aEnableAnalogFilterResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"V\n\x1aDisableAnalogFilterRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t"-\n\x1bDisableAnalogFilterResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"d\n!ConfigureSampleClockSourceRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1b\n\x13sample_clock_source\x18\x02 \x01(\t"4\n"ConfigureSampleClockSourceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xba\x01\n\x1bConfigureTriggerModeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x120\n\x0ctrigger_mode\x18\x03 \x01(\x0e2\x18.nifgen_grpc.TriggerModeH\x00\x12\x1a\n\x10trigger_mode_raw\x18\x04 \x01(\x11H\x00B\x13\n\x11trigger_mode_enum".\n\x1cConfigureTriggerModeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"`\n\'ImportAttributeConfigurationFileRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tfile_path\x18\x02 \x01(\t":\n(ImportAttributeConfigurationFileResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"`\n\'ExportAttributeConfigurationFileRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tfile_path\x18\x02 \x01(\t":\n(ExportAttributeConfigurationFileResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"f\n)ImportAttributeConfigurationBufferRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rconfiguration\x18\x02 \x01(\x0c"<\n*ImportAttributeConfigurationBufferResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"O\n)ExportAttributeConfigurationBufferRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"S\n*ExportAttributeConfigurationBufferResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rconfiguration\x18\x02 \x01(\x0c"\xa7\x01\n\x1aSetAttributeViInt64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nifgen_grpc.NiFgenAttribute\x12\x1b\n\x13attribute_value_raw\x18\x04 \x01(\x03"-\n\x1bSetAttributeViInt64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa9\x01\n\x1cCheckAttributeViInt64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nifgen_grpc.NiFgenAttribute\x12\x1b\n\x13attribute_value_raw\x18\x04 \x01(\x03"/\n\x1dCheckAttributeViInt64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x8a\x01\n\x1aGetAttributeViInt64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nifgen_grpc.NiFgenAttribute"F\n\x1bGetAttributeViInt64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fattribute_value\x18\x02 \x01(\x03"\x85\x02\n\x1aSetAttributeViInt32Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nifgen_grpc.NiFgenAttribute\x12B\n\x0fattribute_value\x18\x04 \x01(\x0e2\'.nifgen_grpc.NiFgenInt32AttributeValuesH\x00\x12\x1d\n\x13attribute_value_raw\x18\x05 \x01(\x11H\x00B\x16\n\x14attribute_value_enum"-\n\x1bSetAttributeViInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x87\x02\n\x1bSetAttributeViReal64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nifgen_grpc.NiFgenAttribute\x12C\n\x0fattribute_value\x18\x04 \x01(\x0e2(.nifgen_grpc.NiFgenReal64AttributeValuesH\x00\x12\x1d\n\x13attribute_value_raw\x18\x05 \x01(\x01H\x00B\x16\n\x14attribute_value_enum".\n\x1cSetAttributeViReal64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x94\x02\n\x1bSetAttributeViStringRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nifgen_grpc.NiFgenAttribute\x12\x1d\n\x13attribute_value_raw\x18\x04 \x01(\tH\x00\x12P\n\x16attribute_value_mapped\x18\x05 \x01(\x0e2..nifgen_grpc.NiFgenStringAttributeValuesMappedH\x00B\x16\n\x14attribute_value_enum".\n\x1cSetAttributeViStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa5\x01\n\x1cSetAttributeViBooleanRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nifgen_grpc.NiFgenAttribute\x12\x17\n\x0fattribute_value\x18\x04 \x01(\x08"/\n\x1dSetAttributeViBooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xbd\x01\n\x1cSetAttributeViSessionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nifgen_grpc.NiFgenAttribute\x12/\n\x0fattribute_value\x18\x04 \x01(\x0b2\x16.nidevice_grpc.Session"/\n\x1dSetAttributeViSessionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x87\x02\n\x1cCheckAttributeViInt32Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nifgen_grpc.NiFgenAttribute\x12B\n\x0fattribute_value\x18\x04 \x01(\x0e2\'.nifgen_grpc.NiFgenInt32AttributeValuesH\x00\x12\x1d\n\x13attribute_value_raw\x18\x05 \x01(\x11H\x00B\x16\n\x14attribute_value_enum"/\n\x1dCheckAttributeViInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x89\x02\n\x1dCheckAttributeViReal64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nifgen_grpc.NiFgenAttribute\x12C\n\x0fattribute_value\x18\x04 \x01(\x0e2(.nifgen_grpc.NiFgenReal64AttributeValuesH\x00\x12\x1d\n\x13attribute_value_raw\x18\x05 \x01(\x01H\x00B\x16\n\x14attribute_value_enum"0\n\x1eCheckAttributeViReal64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x96\x02\n\x1dCheckAttributeViStringRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nifgen_grpc.NiFgenAttribute\x12\x1d\n\x13attribute_value_raw\x18\x04 \x01(\tH\x00\x12P\n\x16attribute_value_mapped\x18\x05 \x01(\x0e2..nifgen_grpc.NiFgenStringAttributeValuesMappedH\x00B\x16\n\x14attribute_value_enum"0\n\x1eCheckAttributeViStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa7\x01\n\x1eCheckAttributeViBooleanRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nifgen_grpc.NiFgenAttribute\x12\x17\n\x0fattribute_value\x18\x04 \x01(\x08"1\n\x1fCheckAttributeViBooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xbf\x01\n\x1eCheckAttributeViSessionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nifgen_grpc.NiFgenAttribute\x12/\n\x0fattribute_value\x18\x04 \x01(\x0b2\x16.nidevice_grpc.Session"1\n\x1fCheckAttributeViSessionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x8a\x01\n\x1aGetAttributeViInt32Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nifgen_grpc.NiFgenAttribute"F\n\x1bGetAttributeViInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fattribute_value\x18\x02 \x01(\x11"\x8b\x01\n\x1bGetAttributeViReal64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nifgen_grpc.NiFgenAttribute"G\n\x1cGetAttributeViReal64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fattribute_value\x18\x02 \x01(\x01"\x8b\x01\n\x1bGetAttributeViStringRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nifgen_grpc.NiFgenAttribute"G\n\x1cGetAttributeViStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fattribute_value\x18\x02 \x01(\t"\x8c\x01\n\x1cGetAttributeViBooleanRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nifgen_grpc.NiFgenAttribute"H\n\x1dGetAttributeViBooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fattribute_value\x18\x02 \x01(\x08"\x8c\x01\n\x1cGetAttributeViSessionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nifgen_grpc.NiFgenAttribute"`\n\x1dGetAttributeViSessionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12/\n\x0fattribute_value\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session"\x85\x01\n\x15ResetAttributeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nifgen_grpc.NiFgenAttribute"(\n\x16ResetAttributeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"Y\n\x1cManualEnableP2PStreamRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rendpoint_name\x18\x02 \x01(\t"/\n\x1dManualEnableP2PStreamResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xba\x01\n CreateWaveformFromFileHWSRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x11\n\tfile_name\x18\x03 \x01(\t\x12\x1e\n\x16use_rate_from_waveform\x18\x04 \x01(\x08\x12)\n!use_gain_and_offset_from_waveform\x18\x05 \x01(\x08"L\n!CreateWaveformFromFileHWSResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fwaveform_handle\x18\x02 \x01(\x11*\xa9S\n\x0fNiFgenAttribute\x12 \n\x1cNIFGEN_ATTRIBUTE_UNSPECIFIED\x10\x00\x12"\n\x1cNIFGEN_ATTRIBUTE_OUTPUT_MODE\x10\xd1\xa5L\x12%\n\x1fNIFGEN_ATTRIBUTE_OUTPUT_ENABLED\x10\xd3\xa5L\x12#\n\x1dNIFGEN_ATTRIBUTE_DIGITAL_GAIN\x10\xae\x9aF\x12"\n\x1cNIFGEN_ATTRIBUTE_ANALOG_PATH\x10\x8e\x9aF\x12%\n\x1fNIFGEN_ATTRIBUTE_LOAD_IMPEDANCE\x10\x8c\x9aF\x12\'\n!NIFGEN_ATTRIBUTE_OUTPUT_IMPEDANCE\x10\xd4\xa5L\x12-\n\'NIFGEN_ATTRIBUTE_TERMINAL_CONFIGURATION\x10\x9d\x9bF\x12)\n#NIFGEN_ATTRIBUTE_COMMON_MODE_OFFSET\x10\x9e\x9bF\x12$\n\x1eNIFGEN_ATTRIBUTE_CHANNEL_DELAY\x10\xa1\x9bF\x12%\n\x1fNIFGEN_ATTRIBUTE_ABSOLUTE_DELAY\x10\xcd\x9bF\x12,\n&NIFGEN_ATTRIBUTE_ANALOG_FILTER_ENABLED\x10\x97\x99F\x12-\n\'NIFGEN_ATTRIBUTE_DIGITAL_FILTER_ENABLED\x10\x96\x99F\x12:\n4NIFGEN_ATTRIBUTE_DIGITAL_FILTER_INTERPOLATION_FACTOR\x10\x8a\x9aF\x122\n,NIFGEN_ATTRIBUTE_FLATNESS_CORRECTION_ENABLED\x10\xf3\x9aF\x12\'\n!NIFGEN_ATTRIBUTE_ANALOG_DATA_MASK\x10\x9a\x9aF\x12*\n$NIFGEN_ATTRIBUTE_ANALOG_STATIC_VALUE\x10\x9b\x9aF\x12(\n"NIFGEN_ATTRIBUTE_DIGITAL_DATA_MASK\x10\x9c\x9aF\x12+\n%NIFGEN_ATTRIBUTE_DIGITAL_STATIC_VALUE\x10\x9d\x9aF\x12.\n(NIFGEN_ATTRIBUTE_DIGITAL_PATTERN_ENABLED\x10\x95\x99F\x12(\n"NIFGEN_ATTRIBUTE_AUX_POWER_ENABLED\x10\xcb\x9bF\x12$\n\x1eNIFGEN_ATTRIBUTE_IDLE_BEHAVIOR\x10\xa9\x9bF\x12!\n\x1bNIFGEN_ATTRIBUTE_IDLE_VALUE\x10\xaa\x9bF\x12$\n\x1eNIFGEN_ATTRIBUTE_WAIT_BEHAVIOR\x10\xab\x9bF\x12!\n\x1bNIFGEN_ATTRIBUTE_WAIT_VALUE\x10\xac\x9bF\x12\x1f\n\x19NIFGEN_ATTRIBUTE_ARB_GAIN\x10\x9a\xa7L\x12!\n\x1bNIFGEN_ATTRIBUTE_ARB_OFFSET\x10\x9b\xa7L\x12\'\n!NIFGEN_ATTRIBUTE_WAVEFORM_QUANTUM\x10\x9e\xa7L\x12(\n"NIFGEN_ATTRIBUTE_MAX_NUM_WAVEFORMS\x10\x9d\xa7L\x12(\n"NIFGEN_ATTRIBUTE_MIN_WAVEFORM_SIZE\x10\x9f\xa7L\x12(\n"NIFGEN_ATTRIBUTE_MAX_WAVEFORM_SIZE\x10\xa0\xa7L\x12*\n$NIFGEN_ATTRIBUTE_ARB_WAVEFORM_HANDLE\x10\x99\xa7L\x12*\n$NIFGEN_ATTRIBUTE_ARB_MARKER_POSITION\x10\xf7\x9aF\x12\'\n!NIFGEN_ATTRIBUTE_ARB_REPEAT_COUNT\x10\xf8\x9aF\x12*\n$NIFGEN_ATTRIBUTE_ARB_SEQUENCE_HANDLE\x10\xa3\xa7L\x12(\n"NIFGEN_ATTRIBUTE_MAX_NUM_SEQUENCES\x10\xa4\xa7L\x12*\n$NIFGEN_ATTRIBUTE_MIN_SEQUENCE_LENGTH\x10\xa5\xa7L\x12*\n$NIFGEN_ATTRIBUTE_MAX_SEQUENCE_LENGTH\x10\xa6\xa7L\x12%\n\x1fNIFGEN_ATTRIBUTE_MAX_LOOP_COUNT\x10\xa7\xa7L\x12)\n#NIFGEN_ATTRIBUTE_SCRIPT_TO_GENERATE\x10\xbe\x9aF\x12/\n)NIFGEN_ATTRIBUTE_FILE_TRANSFER_BLOCK_SIZE\x10\xa0\x9aF\x12/\n)NIFGEN_ATTRIBUTE_DATA_TRANSFER_BLOCK_SIZE\x10\xa1\x9aF\x126\n0NIFGEN_ATTRIBUTE_DATA_TRANSFER_MAXIMUM_BANDWIDTH\x10\xa5\x9bF\x12)\n#NIFGEN_ATTRIBUTE_DIRECT_DMA_ENABLED\x10\xa4\x9aF\x12-\n\'NIFGEN_ATTRIBUTE_DIRECT_DMA_WINDOW_SIZE\x10\xa5\x9aF\x120\n*NIFGEN_ATTRIBUTE_DIRECT_DMA_WINDOW_ADDRESS\x10\xc2\x9aF\x12.\n(NIFGEN_ATTRIBUTE_STREAMING_WAVEFORM_NAME\x10\xf6\x9aF\x120\n*NIFGEN_ATTRIBUTE_STREAMING_WAVEFORM_HANDLE\x10\xf4\x9aF\x12<\n6NIFGEN_ATTRIBUTE_STREAMING_SPACE_AVAILABLE_IN_WAVEFORM\x10\xf5\x9aF\x12.\n(NIFGEN_ATTRIBUTE_STREAMING_WRITE_TIMEOUT\x10\xc9\x9bF\x12:\n4NIFGEN_ATTRIBUTE_DATA_TRANSFER_PREFERRED_PACKET_SIZE\x10\xa6\x9bF\x12<\n6NIFGEN_ATTRIBUTE_DATA_TRANSFER_MAXIMUM_IN_FLIGHT_READS\x10\xa7\x9bF\x124\n.NIFGEN_ATTRIBUTE_PCI_DMA_OPTIMIZATIONS_ENABLED\x10\x9a\x9bF\x12"\n\x1cNIFGEN_ATTRIBUTE_OSP_ENABLED\x10\xa6\x9aF\x12"\n\x1cNIFGEN_ATTRIBUTE_OSP_IQ_RATE\x10\xa8\x9aF\x12/\n)NIFGEN_ATTRIBUTE_OSP_DATA_PROCESSING_MODE\x10\xa7\x9aF\x12\x1f\n\x19NIFGEN_ATTRIBUTE_OSP_MODE\x10\xa2\x9bF\x12*\n$NIFGEN_ATTRIBUTE_OSP_FREQUENCY_SHIFT\x10\xa3\x9bF\x12*\n$NIFGEN_ATTRIBUTE_OSP_CARRIER_ENABLED\x10\xa9\x9aF\x12,\n&NIFGEN_ATTRIBUTE_OSP_CARRIER_FREQUENCY\x10\xaa\x9aF\x12*\n$NIFGEN_ATTRIBUTE_OSP_CARRIER_PHASE_I\x10\xab\x9aF\x12*\n$NIFGEN_ATTRIBUTE_OSP_CARRIER_PHASE_Q\x10\xac\x9aF\x12<\n6NIFGEN_ATTRIBUTE_OSP_COMPENSATE_FOR_FILTER_GROUP_DELAY\x10\xb5\x9bF\x12*\n$NIFGEN_ATTRIBUTE_OSP_FIR_FILTER_TYPE\x10\xad\x9aF\x12-\n\'NIFGEN_ATTRIBUTE_OSP_FIR_FILTER_ENABLED\x10\xaf\x9aF\x123\n-NIFGEN_ATTRIBUTE_OSP_FIR_FILTER_INTERPOLATION\x10\xb0\x9aF\x12-\n\'NIFGEN_ATTRIBUTE_OSP_CIC_FILTER_ENABLED\x10\xb1\x9aF\x123\n-NIFGEN_ATTRIBUTE_OSP_CIC_FILTER_INTERPOLATION\x10\xb2\x9aF\x12>\n8NIFGEN_ATTRIBUTE_OSP_FIR_FILTER_ROOT_RAISED_COSINE_ALPHA\x10\xb3\x9aF\x129\n3NIFGEN_ATTRIBUTE_OSP_FIR_FILTER_RAISED_COSINE_ALPHA\x10\xb4\x9aF\x123\n-NIFGEN_ATTRIBUTE_OSP_FIR_FILTER_FLAT_PASSBAND\x10\xb5\x9aF\x121\n+NIFGEN_ATTRIBUTE_OSP_FIR_FILTER_GAUSSIAN_BT\x10\xb6\x9aF\x12*\n$NIFGEN_ATTRIBUTE_OSP_CIC_FILTER_GAIN\x10\xb7\x9aF\x12,\n&NIFGEN_ATTRIBUTE_OSP_PRE_FILTER_GAIN_I\x10\xb8\x9aF\x12,\n&NIFGEN_ATTRIBUTE_OSP_PRE_FILTER_GAIN_Q\x10\xb9\x9aF\x12.\n(NIFGEN_ATTRIBUTE_OSP_PRE_FILTER_OFFSET_I\x10\xba\x9aF\x12.\n(NIFGEN_ATTRIBUTE_OSP_PRE_FILTER_OFFSET_Q\x10\xbb\x9aF\x123\n-NIFGEN_ATTRIBUTE_OSP_OVERFLOW_ERROR_REPORTING\x10\xbc\x9aF\x12*\n$NIFGEN_ATTRIBUTE_OSP_OVERFLOW_STATUS\x10\xbd\x9aF\x12"\n\x1cNIFGEN_ATTRIBUTE_P2P_ENABLED\x10\xb7\x9bF\x12/\n)NIFGEN_ATTRIBUTE_P2P_DESTINATION_CHANNELS\x10\xb8\x9bF\x12(\n"NIFGEN_ATTRIBUTE_P2P_ENDPOINT_SIZE\x10\xb9\x9bF\x126\n0NIFGEN_ATTRIBUTE_P2P_SPACE_AVAILABLE_IN_ENDPOINT\x10\xba\x9bF\x12;\n5NIFGEN_ATTRIBUTE_P2P_MOST_SPACE_AVAILABLE_IN_ENDPOINT\x10\xbb\x9bF\x12)\n#NIFGEN_ATTRIBUTE_P2P_ENDPOINT_COUNT\x10\xbc\x9bF\x12<\n6NIFGEN_ATTRIBUTE_P2P_DATA_TRANSFER_PERMISSION_INTERVAL\x10\xc0\x9bF\x12C\n=NIFGEN_ATTRIBUTE_P2P_DATA_TRANSFER_PERMISSION_INITIAL_CREDITS\x10\xc8\x9bF\x127\n1NIFGEN_ATTRIBUTE_P2P_MANUAL_CONFIGURATION_ENABLED\x10\xbd\x9bF\x12;\n5NIFGEN_ATTRIBUTE_P2P_DATA_TRANSFER_PERMISSION_ADDRESS\x10\xbe\x9bF\x12@\n:NIFGEN_ATTRIBUTE_P2P_DATA_TRANSFER_PERMISSION_ADDRESS_TYPE\x10\xbf\x9bF\x122\n,NIFGEN_ATTRIBUTE_P2P_ENDPOINT_WINDOW_ADDRESS\x10\xc1\x9bF\x127\n1NIFGEN_ATTRIBUTE_P2P_ENDPOINT_WINDOW_ADDRESS_TYPE\x10\xc2\x9bF\x12/\n)NIFGEN_ATTRIBUTE_P2P_ENDPOINT_WINDOW_SIZE\x10\xc3\x9bF\x12@\n:NIFGEN_ATTRIBUTE_P2P_ENDPOINT_FULLNESS_START_TRIGGER_LEVEL\x10\xca\x9bF\x124\n.NIFGEN_ATTRIBUTE_P2P_DONE_NOTIFICATION_ADDRESS\x10\xc5\x9bF\x129\n3NIFGEN_ATTRIBUTE_P2P_DONE_NOTIFICATION_ADDRESS_TYPE\x10\xc6\x9bF\x122\n,NIFGEN_ATTRIBUTE_P2P_DONE_NOTIFICATION_VALUE\x10\xc7\x9bF\x12$\n\x1eNIFGEN_ATTRIBUTE_FUNC_WAVEFORM\x10\xb5\xa6L\x12%\n\x1fNIFGEN_ATTRIBUTE_FUNC_AMPLITUDE\x10\xb6\xa6L\x12%\n\x1fNIFGEN_ATTRIBUTE_FUNC_DC_OFFSET\x10\xb7\xa6L\x12\'\n!NIFGEN_ATTRIBUTE_FUNC_START_PHASE\x10\xb9\xa6L\x12+\n%NIFGEN_ATTRIBUTE_FUNC_DUTY_CYCLE_HIGH\x10\xba\xa6L\x12+\n%NIFGEN_ATTRIBUTE_SYNC_DUTY_CYCLE_HIGH\x10\x99\x99F\x12/\n)NIFGEN_ATTRIBUTE_SYNC_OUT_OUTPUT_TERMINAL\x10\xfa\x9aF\x12%\n\x1fNIFGEN_ATTRIBUTE_FUNC_FREQUENCY\x10\xb8\xa6L\x12\'\n!NIFGEN_ATTRIBUTE_FUNC_BUFFER_SIZE\x10\x9e\x9aF\x12+\n%NIFGEN_ATTRIBUTE_FUNC_MAX_BUFFER_SIZE\x10\x9f\x9aF\x12\'\n!NIFGEN_ATTRIBUTE_FREQ_LIST_HANDLE\x10\x80\x9aF\x12)\n#NIFGEN_ATTRIBUTE_MAX_NUM_FREQ_LISTS\x10\x81\x9aF\x12+\n%NIFGEN_ATTRIBUTE_MIN_FREQ_LIST_LENGTH\x10\x82\x9aF\x12+\n%NIFGEN_ATTRIBUTE_MAX_FREQ_LIST_LENGTH\x10\x83\x9aF\x12-\n\'NIFGEN_ATTRIBUTE_MIN_FREQ_LIST_DURATION\x10\x84\x9aF\x12-\n\'NIFGEN_ATTRIBUTE_MAX_FREQ_LIST_DURATION\x10\x85\x9aF\x121\n+NIFGEN_ATTRIBUTE_FREQ_LIST_DURATION_QUANTUM\x10\x86\x9aF\x12-\n\'NIFGEN_ATTRIBUTE_REFERENCE_CLOCK_SOURCE\x10\xa1\x99F\x12*\n$NIFGEN_ATTRIBUTE_REF_CLOCK_FREQUENCY\x10\x9b\x99F\x12?\n9NIFGEN_ATTRIBUTE_EXPORTED_REFERENCE_CLOCK_OUTPUT_TERMINAL\x10\xf1\x9aF\x12G\nANIFGEN_ATTRIBUTE_EXPORTED_ONBOARD_REFERENCE_CLOCK_OUTPUT_TERMINAL\x10\xf2\x9aF\x12&\n NIFGEN_ATTRIBUTE_ARB_SAMPLE_RATE\x10\x9c\xa7L\x12!\n\x1bNIFGEN_ATTRIBUTE_CLOCK_MODE\x10\x9e\x99F\x12*\n$NIFGEN_ATTRIBUTE_SAMPLE_CLOCK_SOURCE\x10\xa0\x99F\x12<\n6NIFGEN_ATTRIBUTE_EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL\x10\xf0\x9aF\x124\n.NIFGEN_ATTRIBUTE_EXPORTED_SAMPLE_CLOCK_DIVISOR\x10\x8b\x9aF\x123\n-NIFGEN_ATTRIBUTE_SAMPLE_CLOCK_TIMEBASE_SOURCE\x10\x9f\x9bF\x121\n+NIFGEN_ATTRIBUTE_SAMPLE_CLOCK_TIMEBASE_RATE\x10\xa0\x9bF\x12E\n?NIFGEN_ATTRIBUTE_EXPORTED_SAMPLE_CLOCK_TIMEBASE_OUTPUT_TERMINAL\x10\xf9\x9aF\x12=\n7NIFGEN_ATTRIBUTE_EXPORTED_SAMPLE_CLOCK_TIMEBASE_DIVISOR\x10\x96\x9aF\x127\n1NIFGEN_ATTRIBUTE_EXTERNAL_SAMPLE_CLOCK_MULTIPLIER\x10\xa8\x9bF\x122\n,NIFGEN_ATTRIBUTE_SAMPLE_CLOCK_ABSOLUTE_DELAY\x10\x97\x9aF\x121\n+NIFGEN_ATTRIBUTE_OSCILLATOR_PHASE_DAC_VALUE\x10\x98\x9aF\x128\n2NIFGEN_ATTRIBUTE_EXTERNAL_CLOCK_DELAY_BINARY_VALUE\x10\x99\x9aF\x123\n-NIFGEN_ATTRIBUTE_MARKER_EVENT_OUTPUT_TERMINAL\x10\xe8\x9aF\x123\n-NIFGEN_ATTRIBUTE_MARKER_EVENT_OUTPUT_BEHAVIOR\x10\x86\x9bF\x122\n,NIFGEN_ATTRIBUTE_MARKER_EVENT_PULSE_POLARITY\x10\xe9\x9aF\x12/\n)NIFGEN_ATTRIBUTE_MARKER_EVENT_PULSE_WIDTH\x10\x84\x9bF\x125\n/NIFGEN_ATTRIBUTE_MARKER_EVENT_PULSE_WIDTH_UNITS\x10\x85\x9bF\x128\n2NIFGEN_ATTRIBUTE_MARKER_EVENT_TOGGLE_INITIAL_STATE\x10\x87\x9bF\x12)\n#NIFGEN_ATTRIBUTE_MARKER_EVENT_DELAY\x10\x92\x9bF\x12/\n)NIFGEN_ATTRIBUTE_MARKER_EVENT_DELAY_UNITS\x10\x93\x9bF\x124\n.NIFGEN_ATTRIBUTE_ALL_MARKER_EVENTS_LIVE_STATUS\x10\x88\x9bF\x12/\n)NIFGEN_ATTRIBUTE_MARKER_EVENT_LIVE_STATUS\x10\x89\x9bF\x127\n1NIFGEN_ATTRIBUTE_ALL_MARKER_EVENTS_LATCHED_STATUS\x10\x8d\x9bF\x122\n,NIFGEN_ATTRIBUTE_MARKER_EVENT_LATCHED_STATUS\x10\x8e\x9bF\x128\n2NIFGEN_ATTRIBUTE_DATA_MARKER_EVENT_DATA_BIT_NUMBER\x10\x81\x9bF\x127\n1NIFGEN_ATTRIBUTE_DATA_MARKER_EVENT_LEVEL_POLARITY\x10\x82\x9bF\x128\n2NIFGEN_ATTRIBUTE_DATA_MARKER_EVENT_OUTPUT_TERMINAL\x10\x83\x9bF\x12<\n6NIFGEN_ATTRIBUTE_READY_FOR_START_EVENT_OUTPUT_TERMINAL\x10\xe6\x9aF\x12?\n9NIFGEN_ATTRIBUTE_READY_FOR_START_EVENT_LEVEL_ACTIVE_LEVEL\x10\xe7\x9aF\x128\n2NIFGEN_ATTRIBUTE_READY_FOR_START_EVENT_LIVE_STATUS\x10\x8c\x9bF\x124\n.NIFGEN_ATTRIBUTE_STARTED_EVENT_OUTPUT_TERMINAL\x10\xea\x9aF\x124\n.NIFGEN_ATTRIBUTE_STARTED_EVENT_OUTPUT_BEHAVIOR\x10\xfb\x9aF\x127\n1NIFGEN_ATTRIBUTE_STARTED_EVENT_LEVEL_ACTIVE_LEVEL\x10\xec\x9aF\x123\n-NIFGEN_ATTRIBUTE_STARTED_EVENT_PULSE_POLARITY\x10\xee\x9aF\x126\n0NIFGEN_ATTRIBUTE_STARTED_EVENT_PULSE_WIDTH_UNITS\x10\xfd\x9aF\x120\n*NIFGEN_ATTRIBUTE_STARTED_EVENT_PULSE_WIDTH\x10\xff\x9aF\x12*\n$NIFGEN_ATTRIBUTE_STARTED_EVENT_DELAY\x10\x94\x9bF\x120\n*NIFGEN_ATTRIBUTE_STARTED_EVENT_DELAY_UNITS\x10\x95\x9bF\x123\n-NIFGEN_ATTRIBUTE_STARTED_EVENT_LATCHED_STATUS\x10\x90\x9bF\x121\n+NIFGEN_ATTRIBUTE_DONE_EVENT_OUTPUT_TERMINAL\x10\xeb\x9aF\x121\n+NIFGEN_ATTRIBUTE_DONE_EVENT_OUTPUT_BEHAVIOR\x10\xfc\x9aF\x124\n.NIFGEN_ATTRIBUTE_DONE_EVENT_LEVEL_ACTIVE_LEVEL\x10\xed\x9aF\x120\n*NIFGEN_ATTRIBUTE_DONE_EVENT_PULSE_POLARITY\x10\xef\x9aF\x123\n-NIFGEN_ATTRIBUTE_DONE_EVENT_PULSE_WIDTH_UNITS\x10\xfe\x9aF\x12-\n\'NIFGEN_ATTRIBUTE_DONE_EVENT_PULSE_WIDTH\x10\x80\x9bF\x12\'\n!NIFGEN_ATTRIBUTE_DONE_EVENT_DELAY\x10\x96\x9bF\x12-\n\'NIFGEN_ATTRIBUTE_DONE_EVENT_DELAY_UNITS\x10\x97\x9bF\x120\n*NIFGEN_ATTRIBUTE_DONE_EVENT_LATCHED_STATUS\x10\x8f\x9bF\x12#\n\x1dNIFGEN_ATTRIBUTE_TRIGGER_MODE\x10\x9c\x99F\x12"\n\x1cNIFGEN_ATTRIBUTE_BURST_COUNT\x10\xae\xa8L\x12)\n#NIFGEN_ATTRIBUTE_START_TRIGGER_TYPE\x10\xc8\x9aF\x128\n2NIFGEN_ATTRIBUTE_DIGITAL_EDGE_START_TRIGGER_SOURCE\x10\xc9\x9aF\x126\n0NIFGEN_ATTRIBUTE_DIGITAL_EDGE_START_TRIGGER_EDGE\x10\xca\x9aF\x12=\n7NIFGEN_ATTRIBUTE_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL\x10\xcb\x9aF\x12*\n$NIFGEN_ATTRIBUTE_SCRIPT_TRIGGER_TYPE\x10\xd2\x9aF\x129\n3NIFGEN_ATTRIBUTE_DIGITAL_EDGE_SCRIPT_TRIGGER_SOURCE\x10\xd3\x9aF\x127\n1NIFGEN_ATTRIBUTE_DIGITAL_EDGE_SCRIPT_TRIGGER_EDGE\x10\xd4\x9aF\x12:\n4NIFGEN_ATTRIBUTE_DIGITAL_LEVEL_SCRIPT_TRIGGER_SOURCE\x10\xd5\x9aF\x12@\n:NIFGEN_ATTRIBUTE_DIGITAL_LEVEL_SCRIPT_TRIGGER_ACTIVE_LEVEL\x10\xd6\x9aF\x12>\n8NIFGEN_ATTRIBUTE_EXPORTED_SCRIPT_TRIGGER_OUTPUT_TERMINAL\x10\xd7\x9aF\x12\x1f\n\x19NIFGEN_ATTRIBUTE_BUS_TYPE\x10\x87\x9aF\x12"\n\x1cNIFGEN_ATTRIBUTE_MEMORY_SIZE\x10\xa2\x9aF\x12$\n\x1eNIFGEN_ATTRIBUTE_SERIAL_NUMBER\x10\xa3\x9aF\x12*\n$NIFGEN_ATTRIBUTE_MARKER_EVENTS_COUNT\x10\xbf\x9aF\x12/\n)NIFGEN_ATTRIBUTE_DATA_MARKER_EVENTS_COUNT\x10\xc1\x9aF\x12,\n&NIFGEN_ATTRIBUTE_SCRIPT_TRIGGERS_COUNT\x10\xc0\x9aF\x12*\n$NIFGEN_ATTRIBUTE_VIDEO_WAVEFORM_TYPE\x10\x88\x9aF\x12(\n"NIFGEN_ATTRIBUTE_FPGA_BITFILE_PATH\x10\xcc\x9bF\x122\n,NIFGEN_ATTRIBUTE_FILTER_CORRECTION_FREQUENCY\x10\x98\x99F\x12%\n\x1fNIFGEN_ATTRIBUTE_TRIGGER_SOURCE\x10\xfe\xa7L\x12&\n NIFGEN_ATTRIBUTE_SYNCHRONIZATION\x10\x9f\x99F\x12(\n"NIFGEN_ATTRIBUTE_ID_QUERY_RESPONSE\x10\xb1\x98F\x12%\n\x1fNIFGEN_ATTRIBUTE_GAIN_DAC_VALUE\x10\x8f\x9aF\x12\'\n!NIFGEN_ATTRIBUTE_OFFSET_DAC_VALUE\x10\x90\x9aF\x120\n*NIFGEN_ATTRIBUTE_OSCILLATOR_FREQ_DAC_VALUE\x10\x91\x9aF\x120\n*NIFGEN_ATTRIBUTE_PRE_AMPLIFIER_ATTENUATION\x10\x94\x9aF\x121\n+NIFGEN_ATTRIBUTE_POST_AMPLIFIER_ATTENUATION\x10\x95\x9aF\x12\x1c\n\x16NIFGEN_ATTRIBUTE_CACHE\x10\x94\x8b@\x12"\n\x1cNIFGEN_ATTRIBUTE_RANGE_CHECK\x10\x92\x8b@\x12.\n(NIFGEN_ATTRIBUTE_QUERY_INSTRUMENT_STATUS\x10\x93\x8b@\x12\'\n!NIFGEN_ATTRIBUTE_RECORD_COERCIONS\x10\x96\x8b@\x12\x1f\n\x19NIFGEN_ATTRIBUTE_SIMULATE\x10\x95\x8b@\x12(\n"NIFGEN_ATTRIBUTE_INTERCHANGE_CHECK\x10\xa5\x8b@\x122\n,NIFGEN_ATTRIBUTE_SPECIFIC_DRIVER_DESCRIPTION\x10\x92\x8f@\x12-\n\'NIFGEN_ATTRIBUTE_SPECIFIC_DRIVER_PREFIX\x10\xbe\x8d@\x12-\n\'NIFGEN_ATTRIBUTE_SPECIFIC_DRIVER_VENDOR\x10\x91\x8f@\x12/\n)NIFGEN_ATTRIBUTE_SPECIFIC_DRIVER_REVISION\x10\xb7\x8f@\x12?\n9NIFGEN_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION\x10\x93\x8f@\x12?\n9NIFGEN_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION\x10\x94\x8f@\x122\n,NIFGEN_ATTRIBUTE_SUPPORTED_INSTRUMENT_MODELS\x10\xd7\x8d@\x12)\n#NIFGEN_ATTRIBUTE_GROUP_CAPABILITIES\x10\xa1\x8e@\x12$\n\x1eNIFGEN_ATTRIBUTE_CHANNEL_COUNT\x10\xdb\x8c@\x12.\n(NIFGEN_ATTRIBUTE_INSTRUMENT_MANUFACTURER\x10\x8f\x8f@\x12\'\n!NIFGEN_ATTRIBUTE_INSTRUMENT_MODEL\x10\x90\x8f@\x123\n-NIFGEN_ATTRIBUTE_INSTRUMENT_FIRMWARE_REVISION\x10\x8e\x8f@\x12&\n NIFGEN_ATTRIBUTE_MODULE_REVISION\x10\xb6\x9bF\x12-\n\'NIFGEN_ATTRIBUTE_IO_RESOURCE_DESCRIPTOR\x10\xc0\x8d@\x12#\n\x1dNIFGEN_ATTRIBUTE_LOGICAL_NAME\x10\xc1\x8d@\x12#\n\x1dNIFGEN_ATTRIBUTE_DRIVER_SETUP\x10\x97\x8b@\x124\n.NIFGEN_ATTRIBUTE_SPECIFIC_DRIVER_MAJOR_VERSION\x10\x87\x8f@\x124\n.NIFGEN_ATTRIBUTE_SPECIFIC_DRIVER_MINOR_VERSION\x10\x88\x8f@\x12*\n$NIFGEN_ATTRIBUTE_UPDATE_CLOCK_SOURCE\x10\x9a\x99F*\xd9\x01\n\nOutputMode\x12&\n"OUTPUT_MODE_NIFGEN_VAL_OUTPUT_FUNC\x10\x00\x12%\n!OUTPUT_MODE_NIFGEN_VAL_OUTPUT_ARB\x10\x01\x12%\n!OUTPUT_MODE_NIFGEN_VAL_OUTPUT_SEQ\x10\x02\x12+\n\'OUTPUT_MODE_NIFGEN_VAL_OUTPUT_FREQ_LIST\x10e\x12(\n$OUTPUT_MODE_NIFGEN_VAL_OUTPUT_SCRIPT\x10f*\xc1\x02\n\x08Waveform\x12\x18\n\x14WAVEFORM_UNSPECIFIED\x10\x00\x12 \n\x1cWAVEFORM_NIFGEN_VAL_WFM_SINE\x10\x01\x12"\n\x1eWAVEFORM_NIFGEN_VAL_WFM_SQUARE\x10\x02\x12$\n WAVEFORM_NIFGEN_VAL_WFM_TRIANGLE\x10\x03\x12#\n\x1fWAVEFORM_NIFGEN_VAL_WFM_RAMP_UP\x10\x04\x12%\n!WAVEFORM_NIFGEN_VAL_WFM_RAMP_DOWN\x10\x05\x12\x1e\n\x1aWAVEFORM_NIFGEN_VAL_WFM_DC\x10\x06\x12!\n\x1dWAVEFORM_NIFGEN_VAL_WFM_NOISE\x10e\x12 \n\x1cWAVEFORM_NIFGEN_VAL_WFM_USER\x10f*\xa0\x04\n\x06Signal\x12\x16\n\x12SIGNAL_UNSPECIFIED\x10\x00\x12.\n)SIGNAL_NIFGEN_VAL_ONBOARD_REFERENCE_CLOCK\x10\xfb\x07\x12\x1f\n\x1aSIGNAL_NIFGEN_VAL_SYNC_OUT\x10\xea\x07\x12$\n\x1fSIGNAL_NIFGEN_VAL_START_TRIGGER\x10\xec\x07\x12#\n\x1eSIGNAL_NIFGEN_VAL_MARKER_EVENT\x10\xe9\x07\x12,\n\'SIGNAL_NIFGEN_VAL_SAMPLE_CLOCK_TIMEBASE\x10\xee\x07\x12&\n!SIGNAL_NIFGEN_VAL_SYNCHRONIZATION\x10\xef\x07\x12"\n\x1eSIGNAL_NIFGEN_VAL_SAMPLE_CLOCK\x10e\x12%\n!SIGNAL_NIFGEN_VAL_REFERENCE_CLOCK\x10f\x12$\n SIGNAL_NIFGEN_VAL_SCRIPT_TRIGGER\x10g\x12+\n\'SIGNAL_NIFGEN_VAL_READY_FOR_START_EVENT\x10i\x12#\n\x1fSIGNAL_NIFGEN_VAL_STARTED_EVENT\x10j\x12 \n\x1cSIGNAL_NIFGEN_VAL_DONE_EVENT\x10k\x12\'\n#SIGNAL_NIFGEN_VAL_DATA_MARKER_EVENT\x10l*\xbf\x01\n\x0bTriggerMode\x12\x1c\n\x18TRIGGER_MODE_UNSPECIFIED\x10\x00\x12"\n\x1eTRIGGER_MODE_NIFGEN_VAL_SINGLE\x10\x01\x12&\n"TRIGGER_MODE_NIFGEN_VAL_CONTINUOUS\x10\x02\x12#\n\x1fTRIGGER_MODE_NIFGEN_VAL_STEPPED\x10\x03\x12!\n\x1dTRIGGER_MODE_NIFGEN_VAL_BURST\x10\x04*\x82\x01\n\tClockMode\x12)\n%CLOCK_MODE_NIFGEN_VAL_HIGH_RESOLUTION\x10\x00\x12%\n!CLOCK_MODE_NIFGEN_VAL_DIVIDE_DOWN\x10\x01\x12#\n\x1fCLOCK_MODE_NIFGEN_VAL_AUTOMATIC\x10\x02*v\n\nRelativeTo\x122\n.RELATIVE_TO_NIFGEN_VAL_WAVEFORM_POSITION_START\x10\x00\x124\n0RELATIVE_TO_NIFGEN_VAL_WAVEFORM_POSITION_CURRENT\x10\x01*\xe8\x01\n\rHardwareState\x12"\n\x1eHARDWARE_STATE_NIFGEN_VAL_IDLE\x10\x00\x127\n3HARDWARE_STATE_NIFGEN_VAL_WAITING_FOR_START_TRIGGER\x10d\x12&\n!HARDWARE_STATE_NIFGEN_VAL_RUNNING\x10\xc8\x01\x12#\n\x1eHARDWARE_STATE_NIFGEN_VAL_DONE\x10\xd8\x04\x12-\n(HARDWARE_STATE_NIFGEN_VAL_HARDWARE_ERROR\x10\xe8\x07*Z\n\tByteOrder\x12\'\n#BYTE_ORDER_NIFGEN_VAL_LITTLE_ENDIAN\x10\x00\x12$\n BYTE_ORDER_NIFGEN_VAL_BIG_ENDIAN\x10\x01*|\n\x0bTriggerWhen\x12\x1c\n\x18TRIGGER_WHEN_UNSPECIFIED\x10\x00\x12\'\n#TRIGGER_WHEN_NIFGEN_VAL_ACTIVE_HIGH\x10e\x12&\n"TRIGGER_WHEN_NIFGEN_VAL_ACTIVE_LOW\x10f*p\n\x07Trigger\x12\x17\n\x13TRIGGER_UNSPECIFIED\x10\x00\x12%\n TRIGGER_NIFGEN_VAL_START_TRIGGER\x10\xec\x07\x12%\n!TRIGGER_NIFGEN_VAL_SCRIPT_TRIGGER\x10g*y\n\x14FrequencyListOptions\x12&\n"FREQUENCY_LIST_OPTIONS_UNSPECIFIED\x10\x00\x129\n,FREQUENCY_LIST_OPTIONS_NIFGEN_VAL_ALL_FLISTS\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01*\x89\x07\n\x0fRouteSignalFrom\x12!\n\x1dROUTE_SIGNAL_FROM_UNSPECIFIED\x10\x00\x12(\n#ROUTE_SIGNAL_FROM_NIFGEN_VAL_MARKER\x10\xe9\x07\x12*\n%ROUTE_SIGNAL_FROM_NIFGEN_VAL_SYNC_OUT\x10\xea\x07\x123\n.ROUTE_SIGNAL_FROM_NIFGEN_VAL_OUT_START_TRIGGER\x10\xec\x07\x12-\n(ROUTE_SIGNAL_FROM_NIFGEN_VAL_BOARD_CLOCK\x10\xee\x07\x121\n,ROUTE_SIGNAL_FROM_NIFGEN_VAL_SYNCHRONIZATION\x10\xef\x07\x12.\n*ROUTE_SIGNAL_FROM_NIFGEN_VAL_SOFTWARE_TRIG\x10\x02\x12)\n$ROUTE_SIGNAL_FROM_NIFGEN_VAL_REF_OUT\x10\xf0\x07\x12+\n&ROUTE_SIGNAL_FROM_NIFGEN_VAL_CLOCK_OUT\x10\xf1\x07\x12*\n%ROUTE_SIGNAL_FROM_NIFGEN_VAL_PXI_STAR\x10\x83\x01\x12\'\n"ROUTE_SIGNAL_FROM_NIFGEN_VAL_PFI_0\x10\xf3\x07\x12(\n#ROUTE_SIGNAL_FROM_NIFGEN_VAL_RTSI_0\x10\x8d\x01\x12(\n#ROUTE_SIGNAL_FROM_NIFGEN_VAL_RTSI_1\x10\x8e\x01\x12(\n#ROUTE_SIGNAL_FROM_NIFGEN_VAL_RTSI_2\x10\x8f\x01\x12(\n#ROUTE_SIGNAL_FROM_NIFGEN_VAL_RTSI_3\x10\x90\x01\x12(\n#ROUTE_SIGNAL_FROM_NIFGEN_VAL_RTSI_4\x10\x91\x01\x12(\n#ROUTE_SIGNAL_FROM_NIFGEN_VAL_RTSI_5\x10\x92\x01\x12(\n#ROUTE_SIGNAL_FROM_NIFGEN_VAL_RTSI_6\x10\x93\x01\x12(\n#ROUTE_SIGNAL_FROM_NIFGEN_VAL_RTSI_7\x10\xf2\x07\x129\n4ROUTE_SIGNAL_FROM_NIFGEN_VAL_ONBOARD_REFERENCE_CLOCK\x10\xfb\x07*\x91\x04\n\rRouteSignalTo\x12\x1f\n\x1bROUTE_SIGNAL_TO_UNSPECIFIED\x10\x00\x12&\n!ROUTE_SIGNAL_TO_NIFGEN_VAL_RTSI_0\x10\x8d\x01\x12&\n!ROUTE_SIGNAL_TO_NIFGEN_VAL_RTSI_1\x10\x8e\x01\x12&\n!ROUTE_SIGNAL_TO_NIFGEN_VAL_RTSI_2\x10\x8f\x01\x12&\n!ROUTE_SIGNAL_TO_NIFGEN_VAL_RTSI_3\x10\x90\x01\x12&\n!ROUTE_SIGNAL_TO_NIFGEN_VAL_RTSI_4\x10\x91\x01\x12&\n!ROUTE_SIGNAL_TO_NIFGEN_VAL_RTSI_5\x10\x92\x01\x12&\n!ROUTE_SIGNAL_TO_NIFGEN_VAL_RTSI_6\x10\x93\x01\x12&\n!ROUTE_SIGNAL_TO_NIFGEN_VAL_RTSI_7\x10\xf2\x07\x12\'\n"ROUTE_SIGNAL_TO_NIFGEN_VAL_REF_OUT\x10\xf0\x07\x12%\n ROUTE_SIGNAL_TO_NIFGEN_VAL_PFI_0\x10\xf3\x07\x12%\n ROUTE_SIGNAL_TO_NIFGEN_VAL_PFI_1\x10\xf4\x07\x12(\n#ROUTE_SIGNAL_TO_NIFGEN_VAL_PXI_STAR\x10\x83\x01*h\n\x0eSequenceHandle\x12\x1f\n\x1bSEQUENCE_HANDLE_UNSPECIFIED\x10\x00\x125\n(SEQUENCE_HANDLE_NIFGEN_VAL_ALL_SEQUENCES\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01*h\n\x0eWaveformHandle\x12\x1f\n\x1bWAVEFORM_HANDLE_UNSPECIFIED\x10\x00\x125\n(WAVEFORM_HANDLE_NIFGEN_VAL_ALL_WAVEFORMS\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01*\xc1Q\n\x1aNiFgenInt32AttributeValues\x12\x1c\n\x18NIFGEN_INT32_UNSPECIFIED\x10\x00\x12/\n+NIFGEN_INT32_ADDRESS_TYPE_VAL_ADDR_PHYSICAL\x10\x00\x12.\n*NIFGEN_INT32_ADDRESS_TYPE_VAL_ADDR_VIRTUAL\x10\x01\x121\n-NIFGEN_INT32_ANALOG_PATH_VAL_MAIN_ANALOG_PATH\x10\x00\x123\n/NIFGEN_INT32_ANALOG_PATH_VAL_DIRECT_ANALOG_PATH\x10\x01\x12;\n7NIFGEN_INT32_ANALOG_PATH_VAL_FIXED_LOW_GAIN_ANALOG_PATH\x10\x02\x12<\n8NIFGEN_INT32_ANALOG_PATH_VAL_FIXED_HIGH_GAIN_ANALOG_PATH\x10\x03\x12F\n@NIFGEN_INT32_ARBITRARY_SEQUENCE_HANDLE_VAL_FIRST_SEQUENCE_HANDLE\x10\xa0\x8d\x06\x12E\n?NIFGEN_INT32_ARBITRARY_SEQUENCE_HANDLE_VAL_LAST_SEQUENCE_HANDLE\x10\xaf\xdb\x06\x12C\n6NIFGEN_INT32_ARBITRARY_SEQUENCE_HANDLE_VAL_NO_SEQUENCE\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12E\n@NIFGEN_INT32_ARBITRARY_WAVEFORM_HANDLE_VAL_FIRST_WAVEFORM_HANDLE\x10\x90N\x12D\n?NIFGEN_INT32_ARBITRARY_WAVEFORM_HANDLE_VAL_LAST_WAVEFORM_HANDLE\x10\xf7U\x12C\n6NIFGEN_INT32_ARBITRARY_WAVEFORM_HANDLE_VAL_NO_WAVEFORM\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12=\n0NIFGEN_INT32_BURST_COUNT_VAL_GENERATE_CONTINUOUS\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12)\n%NIFGEN_INT32_BUS_TYPE_VAL_BUS_INVALID\x10\x00\x12$\n NIFGEN_INT32_BUS_TYPE_VAL_BUS_AT\x10\x01\x12%\n!NIFGEN_INT32_BUS_TYPE_VAL_BUS_PCI\x10\x02\x12%\n!NIFGEN_INT32_BUS_TYPE_VAL_BUS_PXI\x10\x03\x12%\n!NIFGEN_INT32_BUS_TYPE_VAL_BUS_VXI\x10\x04\x12(\n$NIFGEN_INT32_BUS_TYPE_VAL_BUS_PCMCIA\x10\x05\x12&\n"NIFGEN_INT32_BUS_TYPE_VAL_BUS_PXIE\x10\x06\x12/\n+NIFGEN_INT32_CLOCK_MODE_VAL_HIGH_RESOLUTION\x10\x00\x12+\n\'NIFGEN_INT32_CLOCK_MODE_VAL_DIVIDE_DOWN\x10\x01\x12)\n%NIFGEN_INT32_CLOCK_MODE_VAL_AUTOMATIC\x10\x02\x12A\n=NIFGEN_INT32_DATA_MARKER_EVENT_LEVEL_POLARITY_VAL_ACTIVE_HIGH\x10e\x12@\n<NIFGEN_INT32_DATA_MARKER_EVENT_LEVEL_POLARITY_VAL_ACTIVE_LOW\x10f\x122\n.NIFGEN_INT32_DATA_PROCESSING_MODE_VAL_OSP_REAL\x10\x00\x125\n1NIFGEN_INT32_DATA_PROCESSING_MODE_VAL_OSP_COMPLEX\x10\x01\x128\n4NIFGEN_INT32_DONE_EVENT_ACTIVE_LEVEL_VAL_ACTIVE_HIGH\x10e\x127\n3NIFGEN_INT32_DONE_EVENT_ACTIVE_LEVEL_VAL_ACTIVE_LOW\x10f\x12@\n<NIFGEN_INT32_DONE_EVENT_DELAY_UNITS_VAL_SAMPLE_CLOCK_PERIODS\x10e\x123\n/NIFGEN_INT32_DONE_EVENT_DELAY_UNITS_VAL_SECONDS\x10f\x125\n1NIFGEN_INT32_DONE_EVENT_OUTPUT_BEHAVIOR_VAL_PULSE\x10e\x125\n1NIFGEN_INT32_DONE_EVENT_OUTPUT_BEHAVIOR_VAL_LEVEL\x10f\x12:\n6NIFGEN_INT32_DONE_EVENT_PULSE_POLARITY_VAL_ACTIVE_HIGH\x10e\x129\n5NIFGEN_INT32_DONE_EVENT_PULSE_POLARITY_VAL_ACTIVE_LOW\x10f\x12F\nBNIFGEN_INT32_DONE_EVENT_PULSE_WIDTH_UNITS_VAL_SAMPLE_CLOCK_PERIODS\x10e\x129\n5NIFGEN_INT32_DONE_EVENT_PULSE_WIDTH_UNITS_VAL_SECONDS\x10f\x12)\n%NIFGEN_INT32_FILTER_TYPE_VAL_OSP_FLAT\x10\x00\x122\n.NIFGEN_INT32_FILTER_TYPE_VAL_OSP_RAISED_COSINE\x10\x01\x127\n3NIFGEN_INT32_FILTER_TYPE_VAL_OSP_ROOT_RAISED_COSINE\x10\x02\x12-\n)NIFGEN_INT32_FILTER_TYPE_VAL_OSP_GAUSSIAN\x10\x03\x12+\n\'NIFGEN_INT32_FILTER_TYPE_VAL_OSP_CUSTOM\x10\x04\x12C\n=NIFGEN_INT32_FREQUENCY_LIST_HANDLE_VAL_FIRST_FREQ_LIST_HANDLE\x10\xc0\x9a\x0c\x12B\n<NIFGEN_INT32_FREQUENCY_LIST_HANDLE_VAL_LAST_FREQ_LIST_HANDLE\x10\xcf\xe8\x0c\x12@\n3NIFGEN_INT32_FREQUENCY_LIST_HANDLE_VAL_NO_FREQ_LIST\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x123\n.NIFGEN_INT32_IDLE_BEHAVIOR_VAL_HOLD_LAST_VALUE\x10\x90\x03\x121\n,NIFGEN_INT32_IDLE_BEHAVIOR_VAL_JUMP_TO_VALUE\x10\x91\x03\x12B\n>NIFGEN_INT32_MARKER_EVENT_DELAY_UNITS_VAL_SAMPLE_CLOCK_PERIODS\x10e\x125\n1NIFGEN_INT32_MARKER_EVENT_DELAY_UNITS_VAL_SECONDS\x10f\x127\n3NIFGEN_INT32_MARKER_EVENT_OUTPUT_BEHAVIOR_VAL_PULSE\x10e\x127\n3NIFGEN_INT32_MARKER_EVENT_OUTPUT_BEHAVIOR_VAL_LEVEL\x10f\x128\n4NIFGEN_INT32_MARKER_EVENT_OUTPUT_BEHAVIOR_VAL_TOGGLE\x10g\x12<\n8NIFGEN_INT32_MARKER_EVENT_PULSE_POLARITY_VAL_ACTIVE_HIGH\x10e\x12;\n7NIFGEN_INT32_MARKER_EVENT_PULSE_POLARITY_VAL_ACTIVE_LOW\x10f\x12H\nDNIFGEN_INT32_MARKER_EVENT_PULSE_WIDTH_UNITS_VAL_SAMPLE_CLOCK_PERIODS\x10e\x12;\n7NIFGEN_INT32_MARKER_EVENT_PULSE_WIDTH_UNITS_VAL_SECONDS\x10f\x12;\n7NIFGEN_INT32_MARKER_EVENT_TOGGLE_INITIAL_STATE_VAL_HIGH\x10e\x12:\n6NIFGEN_INT32_MARKER_EVENT_TOGGLE_INITIAL_STATE_VAL_LOW\x10f\x12$\n NIFGEN_INT32_OSP_MODE_VAL_OSP_IF\x10\x00\x12*\n&NIFGEN_INT32_OSP_MODE_VAL_OSP_BASEBAND\x10\x01\x12G\nCNIFGEN_INT32_OSP_OVERFLOW_ERROR_REPORTING_VAL_ERROR_REPORTING_ERROR\x10\x00\x12J\nFNIFGEN_INT32_OSP_OVERFLOW_ERROR_REPORTING_VAL_ERROR_REPORTING_DISABLED\x10\x02\x12:\n6NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_NONE\x10\x00\x12G\nCNIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_PRE_FILTER_GAIN_I\x10\x01\x12G\nCNIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_PRE_FILTER_GAIN_Q\x10\x02\x12I\nENIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_PRE_FILTER_OFFSET_I\x10\x04\x12I\nENIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_PRE_FILTER_OFFSET_Q\x10\x08\x12B\n>NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_FIR_FILTER_I\x10\x10\x12C\n?NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_PFIR_FILTER_I\x10\x10\x12B\n>NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_FIR_FILTER_Q\x10 \x12C\n?NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_PFIR_FILTER_Q\x10 \x12B\n>NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_CIC_FILTER_I\x10@\x12C\n>NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_CIC_FILTER_Q\x10\x80\x01\x12C\n>NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_COMPLEX_DATA\x10\x80\x02\x12D\n?NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_CFIR_FILTER_I\x10\x80\x04\x12D\n?NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_CFIR_FILTER_Q\x10\x80\x08\x12@\n;NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_EQUALIZER\x10\x80\x10\x12,\n(NIFGEN_INT32_OUTPUT_MODE_VAL_OUTPUT_FUNC\x10\x00\x12+\n\'NIFGEN_INT32_OUTPUT_MODE_VAL_OUTPUT_ARB\x10\x01\x12+\n\'NIFGEN_INT32_OUTPUT_MODE_VAL_OUTPUT_SEQ\x10\x02\x121\n-NIFGEN_INT32_OUTPUT_MODE_VAL_OUTPUT_FREQ_LIST\x10e\x12.\n*NIFGEN_INT32_OUTPUT_MODE_VAL_OUTPUT_SCRIPT\x10f\x12C\n?NIFGEN_INT32_READY_FOR_START_EVENT_ACTIVE_LEVEL_VAL_ACTIVE_HIGH\x10e\x12B\n>NIFGEN_INT32_READY_FOR_START_EVENT_ACTIVE_LEVEL_VAL_ACTIVE_LOW\x10f\x12A\n=NIFGEN_INT32_SCRIPT_TRIGGER_DIGITAL_EDGE_EDGE_VAL_RISING_EDGE\x10e\x12B\n>NIFGEN_INT32_SCRIPT_TRIGGER_DIGITAL_EDGE_EDGE_VAL_FALLING_EDGE\x10f\x12J\nFNIFGEN_INT32_SCRIPT_TRIGGER_DIGITAL_LEVEL_ACTIVE_LEVEL_VAL_ACTIVE_HIGH\x10e\x12I\nENIFGEN_INT32_SCRIPT_TRIGGER_DIGITAL_LEVEL_ACTIVE_LEVEL_VAL_ACTIVE_LOW\x10f\x122\n.NIFGEN_INT32_SCRIPT_TRIGGER_TYPE_VAL_TRIG_NONE\x10e\x125\n1NIFGEN_INT32_SCRIPT_TRIGGER_TYPE_VAL_DIGITAL_EDGE\x10f\x126\n2NIFGEN_INT32_SCRIPT_TRIGGER_TYPE_VAL_DIGITAL_LEVEL\x10g\x126\n2NIFGEN_INT32_SCRIPT_TRIGGER_TYPE_VAL_SOFTWARE_EDGE\x10h\x12@\n<NIFGEN_INT32_START_TRIGGER_DIGITAL_EDGE_EDGE_VAL_RISING_EDGE\x10e\x12A\n=NIFGEN_INT32_START_TRIGGER_DIGITAL_EDGE_EDGE_VAL_FALLING_EDGE\x10f\x121\n-NIFGEN_INT32_START_TRIGGER_TYPE_VAL_TRIG_NONE\x10e\x124\n0NIFGEN_INT32_START_TRIGGER_TYPE_VAL_DIGITAL_EDGE\x10f\x125\n1NIFGEN_INT32_START_TRIGGER_TYPE_VAL_SOFTWARE_EDGE\x10h\x12=\n9NIFGEN_INT32_START_TRIGGER_TYPE_VAL_P2P_ENDPOINT_FULLNESS\x10j\x12;\n7NIFGEN_INT32_STARTED_EVENT_ACTIVE_LEVEL_VAL_ACTIVE_HIGH\x10e\x12:\n6NIFGEN_INT32_STARTED_EVENT_ACTIVE_LEVEL_VAL_ACTIVE_LOW\x10f\x12C\n?NIFGEN_INT32_STARTED_EVENT_DELAY_UNITS_VAL_SAMPLE_CLOCK_PERIODS\x10e\x126\n2NIFGEN_INT32_STARTED_EVENT_DELAY_UNITS_VAL_SECONDS\x10f\x128\n4NIFGEN_INT32_STARTED_EVENT_OUTPUT_BEHAVIOR_VAL_PULSE\x10e\x128\n4NIFGEN_INT32_STARTED_EVENT_OUTPUT_BEHAVIOR_VAL_LEVEL\x10f\x12=\n9NIFGEN_INT32_STARTED_EVENT_PULSE_POLARITY_VAL_ACTIVE_HIGH\x10e\x12<\n8NIFGEN_INT32_STARTED_EVENT_PULSE_POLARITY_VAL_ACTIVE_LOW\x10f\x12I\nENIFGEN_INT32_STARTED_EVENT_PULSE_WIDTH_UNITS_VAL_SAMPLE_CLOCK_PERIODS\x10e\x12<\n8NIFGEN_INT32_STARTED_EVENT_PULSE_WIDTH_UNITS_VAL_SECONDS\x10f\x120\n,NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_TTL0\x10o\x120\n,NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_TTL1\x10p\x120\n,NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_TTL2\x10q\x120\n,NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_TTL3\x10r\x120\n,NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_TTL4\x10s\x120\n,NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_TTL5\x10t\x120\n,NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_TTL6\x10u\x123\n.NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_RTSI_0\x10\x8d\x01\x123\n.NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_RTSI_1\x10\x8e\x01\x123\n.NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_RTSI_2\x10\x8f\x01\x123\n.NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_RTSI_3\x10\x90\x01\x123\n.NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_RTSI_4\x10\x91\x01\x123\n.NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_RTSI_5\x10\x92\x01\x123\n.NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_RTSI_6\x10\x93\x01\x121\n,NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_NONE\x10\xe8\x07\x129\n4NIFGEN_INT32_TERMINAL_CONFIGURATION_VAL_SINGLE_ENDED\x10\xac\x02\x129\n4NIFGEN_INT32_TERMINAL_CONFIGURATION_VAL_DIFFERENTIAL\x10\xad\x02\x12(\n$NIFGEN_INT32_TRIGGER_MODE_VAL_SINGLE\x10\x01\x12,\n(NIFGEN_INT32_TRIGGER_MODE_VAL_CONTINUOUS\x10\x02\x12)\n%NIFGEN_INT32_TRIGGER_MODE_VAL_STEPPED\x10\x03\x12\'\n#NIFGEN_INT32_TRIGGER_MODE_VAL_BURST\x10\x04\x12-\n)NIFGEN_INT32_TRIGGER_SOURCE_VAL_IMMEDIATE\x10\x00\x12,\n(NIFGEN_INT32_TRIGGER_SOURCE_VAL_EXTERNAL\x10\x01\x121\n-NIFGEN_INT32_TRIGGER_SOURCE_VAL_SOFTWARE_TRIG\x10\x02\x12(\n$NIFGEN_INT32_TRIGGER_SOURCE_VAL_TTL0\x10o\x12(\n$NIFGEN_INT32_TRIGGER_SOURCE_VAL_TTL1\x10p\x12(\n$NIFGEN_INT32_TRIGGER_SOURCE_VAL_TTL2\x10q\x12(\n$NIFGEN_INT32_TRIGGER_SOURCE_VAL_TTL3\x10r\x12(\n$NIFGEN_INT32_TRIGGER_SOURCE_VAL_TTL4\x10s\x12(\n$NIFGEN_INT32_TRIGGER_SOURCE_VAL_TTL5\x10t\x12(\n$NIFGEN_INT32_TRIGGER_SOURCE_VAL_TTL6\x10u\x12-\n(NIFGEN_INT32_TRIGGER_SOURCE_VAL_PXI_STAR\x10\x83\x01\x12+\n&NIFGEN_INT32_TRIGGER_SOURCE_VAL_RTSI_0\x10\x8d\x01\x12+\n&NIFGEN_INT32_TRIGGER_SOURCE_VAL_RTSI_1\x10\x8e\x01\x12+\n&NIFGEN_INT32_TRIGGER_SOURCE_VAL_RTSI_2\x10\x8f\x01\x12+\n&NIFGEN_INT32_TRIGGER_SOURCE_VAL_RTSI_3\x10\x90\x01\x12+\n&NIFGEN_INT32_TRIGGER_SOURCE_VAL_RTSI_4\x10\x91\x01\x12+\n&NIFGEN_INT32_TRIGGER_SOURCE_VAL_RTSI_5\x10\x92\x01\x12+\n&NIFGEN_INT32_TRIGGER_SOURCE_VAL_RTSI_6\x10\x93\x01\x12+\n&NIFGEN_INT32_TRIGGER_SOURCE_VAL_RTSI_7\x10\xf2\x07\x12*\n%NIFGEN_INT32_TRIGGER_SOURCE_VAL_PFI_0\x10\xf3\x07\x12*\n%NIFGEN_INT32_TRIGGER_SOURCE_VAL_PFI_1\x10\xf4\x07\x12*\n%NIFGEN_INT32_TRIGGER_SOURCE_VAL_PFI_2\x10\xf5\x07\x12*\n%NIFGEN_INT32_TRIGGER_SOURCE_VAL_PFI_3\x10\xf6\x07\x123\n.NIFGEN_INT32_TRIGGER_SOURCE_VAL_OTHER_TERMINAL\x10\xfa\x07\x121\n-NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_INTERNAL\x10\x00\x121\n-NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_EXTERNAL\x10\x01\x12-\n)NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_TTL1\x10p\x12-\n)NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_TTL2\x10q\x12-\n)NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_TTL3\x10r\x12-\n)NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_TTL4\x10s\x12-\n)NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_TTL5\x10t\x12-\n)NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_TTL6\x10u\x122\n-NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_PXI_STAR\x10\x83\x01\x120\n+NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_RTSI_0\x10\x8d\x01\x120\n+NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_RTSI_1\x10\x8e\x01\x120\n+NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_RTSI_2\x10\x8f\x01\x120\n+NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_RTSI_3\x10\x90\x01\x120\n+NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_RTSI_4\x10\x91\x01\x120\n+NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_RTSI_5\x10\x92\x01\x120\n+NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_RTSI_6\x10\x93\x01\x120\n+NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_RTSI_7\x10\xf2\x07\x128\n3NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_OTHER_TERMINAL\x10\xfa\x07\x120\n+NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_CLK_IN\x10\xb2\t\x124\n/NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_DDC_CLK_IN\x10\xb3\t\x12.\n*NIFGEN_INT32_VIDEO_WAVEFORM_TYPE_VAL_PAL_B\x10\x00\x12.\n*NIFGEN_INT32_VIDEO_WAVEFORM_TYPE_VAL_PAL_D\x10\x01\x12.\n*NIFGEN_INT32_VIDEO_WAVEFORM_TYPE_VAL_PAL_G\x10\x02\x12.\n*NIFGEN_INT32_VIDEO_WAVEFORM_TYPE_VAL_PAL_H\x10\x03\x12.\n*NIFGEN_INT32_VIDEO_WAVEFORM_TYPE_VAL_PAL_I\x10\x04\x12.\n*NIFGEN_INT32_VIDEO_WAVEFORM_TYPE_VAL_PAL_M\x10\x05\x12.\n*NIFGEN_INT32_VIDEO_WAVEFORM_TYPE_VAL_PAL_N\x10\x06\x12/\n+NIFGEN_INT32_VIDEO_WAVEFORM_TYPE_VAL_NTSC_M\x10\x07\x123\n.NIFGEN_INT32_WAIT_BEHAVIOR_VAL_HOLD_LAST_VALUE\x10\x90\x03\x121\n,NIFGEN_INT32_WAIT_BEHAVIOR_VAL_JUMP_TO_VALUE\x10\x91\x03\x12&\n"NIFGEN_INT32_WAVEFORM_VAL_WFM_SINE\x10\x01\x12(\n$NIFGEN_INT32_WAVEFORM_VAL_WFM_SQUARE\x10\x02\x12*\n&NIFGEN_INT32_WAVEFORM_VAL_WFM_TRIANGLE\x10\x03\x12)\n%NIFGEN_INT32_WAVEFORM_VAL_WFM_RAMP_UP\x10\x04\x12+\n\'NIFGEN_INT32_WAVEFORM_VAL_WFM_RAMP_DOWN\x10\x05\x12$\n NIFGEN_INT32_WAVEFORM_VAL_WFM_DC\x10\x06\x12\'\n#NIFGEN_INT32_WAVEFORM_VAL_WFM_NOISE\x10e\x12&\n"NIFGEN_INT32_WAVEFORM_VAL_WFM_USER\x10f\x1a\x02\x10\x01*\xa7\x02\n\x1bNiFgenReal64AttributeValues\x12\x1d\n\x19NIFGEN_REAL64_UNSPECIFIED\x10\x00\x12D\n7NIFGEN_REAL64_LOAD_IMPEDANCE_VAL_MATCHED_LOAD_IMPEDANCE\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12.\n*NIFGEN_REAL64_OUTPUT_IMPEDANCE_VAL_50_OHMS\x102\x12.\n*NIFGEN_REAL64_OUTPUT_IMPEDANCE_VAL_75_OHMS\x10K\x12?\n2NIFGEN_REAL64_SAMPLE_RATE_VAL_EXTERNAL_SAMPLE_RATE\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x1a\x02\x10\x01*\xcf\n\n!NiFgenStringAttributeValuesMapped\x12$\n NIFGEN_STRING_MAPPED_UNSPECIFIED\x10\x00\x12I\nENIFGEN_STRING_REFERENCE_CLOCK_SOURCE_VAL_CLOCK_IN_COLLISION_AVOIDANCE\x10\x01\x12E\nANIFGEN_STRING_REFERENCE_CLOCK_SOURCE_VAL_NONE_COLLISION_AVOIDANCE\x10\x02\x12X\nTNIFGEN_STRING_REFERENCE_CLOCK_SOURCE_VAL_ONBOARD_REFERENCE_CLOCK_COLLISION_AVOIDANCE\x10\x03\x12J\nFNIFGEN_STRING_REFERENCE_CLOCK_SOURCE_VAL_PXI_CLOCK_COLLISION_AVOIDANCE\x10\x04\x12G\nCNIFGEN_STRING_REFERENCE_CLOCK_SOURCE_VAL_RTSI_7_COLLISION_AVOIDANCE\x10\x05\x122\n.NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_CLOCK_IN\x10\x06\x126\n2NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_DDC_CLOCK_IN\x10\x07\x127\n3NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_ONBOARD_CLOCK\x10\x08\x127\n3NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_STAR_LINE\x10\t\x12C\n?NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_0_RTSI_0\x10\n\x12C\n?NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_1_RTSI_1\x10\x0b\x12C\n?NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_2_RTSI_2\x10\x0c\x12C\n?NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_3_RTSI_3\x10\r\x12C\n?NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_4_RTSI_4\x10\x0e\x12C\n?NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_5_RTSI_5\x10\x0f\x12C\n?NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_6_RTSI_6\x10\x10\x12C\n?NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_7_RTSI_7\x10\x11\x12;\n7NIFGEN_STRING_SAMPLE_CLOCK_TIMEBASE_SOURCE_VAL_CLOCK_IN\x10\x12\x12@\n<NIFGEN_STRING_SAMPLE_CLOCK_TIMEBASE_SOURCE_VAL_ONBOARD_CLOCK\x10\x132\xdbn\n\x06NiFgen\x12;\n\x04Init\x12\x18.nifgen_grpc.InitRequest\x1a\x19.nifgen_grpc.InitResponse\x12\\\n\x0fInitWithOptions\x12#.nifgen_grpc.InitWithOptionsRequest\x1a$.nifgen_grpc.InitWithOptionsResponse\x12q\n\x16InitializeWithChannels\x12*.nifgen_grpc.InitializeWithChannelsRequest\x1a+.nifgen_grpc.InitializeWithChannelsResponse\x12>\n\x05Close\x12\x19.nifgen_grpc.CloseRequest\x1a\x1a.nifgen_grpc.CloseResponse\x12>\n\x05Reset\x12\x19.nifgen_grpc.ResetRequest\x1a\x1a.nifgen_grpc.ResetResponse\x12G\n\x08SelfTest\x12\x1c.nifgen_grpc.SelfTestRequest\x1a\x1d.nifgen_grpc.SelfTestResponse\x12M\n\nErrorQuery\x12\x1e.nifgen_grpc.ErrorQueryRequest\x1a\x1f.nifgen_grpc.ErrorQueryResponse\x12S\n\x0cErrorMessage\x12 .nifgen_grpc.ErrorMessageRequest\x1a!.nifgen_grpc.ErrorMessageResponse\x12V\n\rRevisionQuery\x12!.nifgen_grpc.RevisionQueryRequest\x1a".nifgen_grpc.RevisionQueryResponse\x12G\n\x08GetError\x12\x1c.nifgen_grpc.GetErrorRequest\x1a\x1d.nifgen_grpc.GetErrorResponse\x12M\n\nClearError\x12\x1e.nifgen_grpc.ClearErrorRequest\x1a\x1f.nifgen_grpc.ClearErrorResponse\x12S\n\x0cErrorHandler\x12 .nifgen_grpc.ErrorHandlerRequest\x1a!.nifgen_grpc.ErrorHandlerResponse\x12Y\n\x0eGetChannelName\x12".nifgen_grpc.GetChannelNameRequest\x1a#.nifgen_grpc.GetChannelNameResponse\x12n\n\x15ResetInterchangeCheck\x12).nifgen_grpc.ResetInterchangeCheckRequest\x1a*.nifgen_grpc.ResetInterchangeCheckResponse\x12w\n\x18ClearInterchangeWarnings\x12,.nifgen_grpc.ClearInterchangeWarningsRequest\x1a-.nifgen_grpc.ClearInterchangeWarningsResponse\x12t\n\x17InvalidateAllAttributes\x12+.nifgen_grpc.InvalidateAllAttributesRequest\x1a,.nifgen_grpc.InvalidateAllAttributesResponse\x12b\n\x11ResetWithDefaults\x12%.nifgen_grpc.ResetWithDefaultsRequest\x1a&.nifgen_grpc.ResetWithDefaultsResponse\x12D\n\x07Disable\x12\x1b.nifgen_grpc.DisableRequest\x1a\x1c.nifgen_grpc.DisableResponse\x12A\n\x06Commit\x12\x1a.nifgen_grpc.CommitRequest\x1a\x1b.nifgen_grpc.CommitResponse\x12_\n\x10GetHardwareState\x12$.nifgen_grpc.GetHardwareStateRequest\x1a%.nifgen_grpc.GetHardwareStateResponse\x12V\n\rWaitUntilDone\x12!.nifgen_grpc.WaitUntilDoneRequest\x1a".nifgen_grpc.WaitUntilDoneResponse\x12A\n\x06IsDone\x12\x1a.nifgen_grpc.IsDoneRequest\x1a\x1b.nifgen_grpc.IsDoneResponse\x12P\n\x0bResetDevice\x12\x1f.nifgen_grpc.ResetDeviceRequest\x1a .nifgen_grpc.ResetDeviceResponse\x12q\n\x16ConfigureOperationMode\x12*.nifgen_grpc.ConfigureOperationModeRequest\x1a+.nifgen_grpc.ConfigureOperationModeResponse\x12h\n\x13ConfigureOutputMode\x12\'.nifgen_grpc.ConfigureOutputModeRequest\x1a(.nifgen_grpc.ConfigureOutputModeResponse\x12t\n\x17ConfigureReferenceClock\x12+.nifgen_grpc.ConfigureReferenceClockRequest\x1a,.nifgen_grpc.ConfigureReferenceClockResponse\x12w\n\x18ConfigureOutputImpedance\x12,.nifgen_grpc.ConfigureOutputImpedanceRequest\x1a-.nifgen_grpc.ConfigureOutputImpedanceResponse\x12q\n\x16ConfigureOutputEnabled\x12*.nifgen_grpc.ConfigureOutputEnabledRequest\x1a+.nifgen_grpc.ConfigureOutputEnabledResponse\x12b\n\x11ConfigureChannels\x12%.nifgen_grpc.ConfigureChannelsRequest\x1a&.nifgen_grpc.ConfigureChannelsResponse\x12e\n\x12InitiateGeneration\x12&.nifgen_grpc.InitiateGenerationRequest\x1a\'.nifgen_grpc.InitiateGenerationResponse\x12\\\n\x0fAbortGeneration\x12#.nifgen_grpc.AbortGenerationRequest\x1a$.nifgen_grpc.AbortGenerationResponse\x12z\n\x19ConfigureStandardWaveform\x12-.nifgen_grpc.ConfigureStandardWaveformRequest\x1a..nifgen_grpc.ConfigureStandardWaveformResponse\x12}\n\x1aDefineUserStandardWaveform\x12..nifgen_grpc.DefineUserStandardWaveformRequest\x1a/.nifgen_grpc.DefineUserStandardWaveformResponse\x12z\n\x19ClearUserStandardWaveform\x12-.nifgen_grpc.ClearUserStandardWaveformRequest\x1a..nifgen_grpc.ClearUserStandardWaveformResponse\x12e\n\x12ConfigureFrequency\x12&.nifgen_grpc.ConfigureFrequencyRequest\x1a\'.nifgen_grpc.ConfigureFrequencyResponse\x12e\n\x12ConfigureAmplitude\x12&.nifgen_grpc.ConfigureAmplitudeRequest\x1a\'.nifgen_grpc.ConfigureAmplitudeResponse\x12t\n\x17QueryArbWfmCapabilities\x12+.nifgen_grpc.QueryArbWfmCapabilitiesRequest\x1a,.nifgen_grpc.QueryArbWfmCapabilitiesResponse\x12b\n\x11CreateWaveformF64\x12%.nifgen_grpc.CreateWaveformF64Request\x1a&.nifgen_grpc.CreateWaveformF64Response\x12b\n\x11CreateWaveformI16\x12%.nifgen_grpc.CreateWaveformI16Request\x1a&.nifgen_grpc.CreateWaveformI16Response\x12w\n\x18CreateWaveformComplexF64\x12,.nifgen_grpc.CreateWaveformComplexF64Request\x1a-.nifgen_grpc.CreateWaveformComplexF64Response\x12z\n\x19CreateWaveformFromFileI16\x12-.nifgen_grpc.CreateWaveformFromFileI16Request\x1a..nifgen_grpc.CreateWaveformFromFileI16Response\x12z\n\x19CreateWaveformFromFileF64\x12-.nifgen_grpc.CreateWaveformFromFileF64Request\x1a..nifgen_grpc.CreateWaveformFromFileF64Response\x12h\n\x13ConfigureSampleRate\x12\'.nifgen_grpc.ConfigureSampleRateRequest\x1a(.nifgen_grpc.ConfigureSampleRateResponse\x12k\n\x14ConfigureArbWaveform\x12(.nifgen_grpc.ConfigureArbWaveformRequest\x1a).nifgen_grpc.ConfigureArbWaveformResponse\x12_\n\x10ClearArbWaveform\x12$.nifgen_grpc.ClearArbWaveformRequest\x1a%.nifgen_grpc.ClearArbWaveformResponse\x12n\n\x15AllocateNamedWaveform\x12).nifgen_grpc.AllocateNamedWaveformRequest\x1a*.nifgen_grpc.AllocateNamedWaveformResponse\x12\x92\x01\n!SetNamedWaveformNextWritePosition\x125.nifgen_grpc.SetNamedWaveformNextWritePositionRequest\x1a6.nifgen_grpc.SetNamedWaveformNextWritePositionResponse\x12n\n\x15WriteNamedWaveformF64\x12).nifgen_grpc.WriteNamedWaveformF64Request\x1a*.nifgen_grpc.WriteNamedWaveformF64Response\x12n\n\x15WriteNamedWaveformI16\x12).nifgen_grpc.WriteNamedWaveformI16Request\x1a*.nifgen_grpc.WriteNamedWaveformI16Response\x12\x83\x01\n\x1cWriteNamedWaveformComplexF64\x120.nifgen_grpc.WriteNamedWaveformComplexF64Request\x1a1.nifgen_grpc.WriteNamedWaveformComplexF64Response\x12\x83\x01\n\x1cWriteNamedWaveformComplexI16\x120.nifgen_grpc.WriteNamedWaveformComplexI16Request\x1a1.nifgen_grpc.WriteNamedWaveformComplexI16Response\x12h\n\x13DeleteNamedWaveform\x12\'.nifgen_grpc.DeleteNamedWaveformRequest\x1a(.nifgen_grpc.DeleteNamedWaveformResponse\x12t\n\x17QueryArbSeqCapabilities\x12+.nifgen_grpc.QueryArbSeqCapabilitiesRequest\x1a,.nifgen_grpc.QueryArbSeqCapabilitiesResponse\x12b\n\x11CreateArbSequence\x12%.nifgen_grpc.CreateArbSequenceRequest\x1a&.nifgen_grpc.CreateArbSequenceResponse\x12z\n\x19CreateAdvancedArbSequence\x12-.nifgen_grpc.CreateAdvancedArbSequenceRequest\x1a..nifgen_grpc.CreateAdvancedArbSequenceResponse\x12k\n\x14ConfigureArbSequence\x12(.nifgen_grpc.ConfigureArbSequenceRequest\x1a).nifgen_grpc.ConfigureArbSequenceResponse\x12_\n\x10ClearArbSequence\x12$.nifgen_grpc.ClearArbSequenceRequest\x1a%.nifgen_grpc.ClearArbSequenceResponse\x12Y\n\x0eClearArbMemory\x12".nifgen_grpc.ClearArbMemoryRequest\x1a#.nifgen_grpc.ClearArbMemoryResponse\x12z\n\x19QueryFreqListCapabilities\x12-.nifgen_grpc.QueryFreqListCapabilitiesRequest\x1a..nifgen_grpc.QueryFreqListCapabilitiesResponse\x12Y\n\x0eCreateFreqList\x12".nifgen_grpc.CreateFreqListRequest\x1a#.nifgen_grpc.CreateFreqListResponse\x12b\n\x11ConfigureFreqList\x12%.nifgen_grpc.ConfigureFreqListRequest\x1a&.nifgen_grpc.ConfigureFreqListResponse\x12V\n\rClearFreqList\x12!.nifgen_grpc.ClearFreqListRequest\x1a".nifgen_grpc.ClearFreqListResponse\x12P\n\x0bWriteScript\x12\x1f.nifgen_grpc.WriteScriptRequest\x1a .nifgen_grpc.WriteScriptResponse\x12S\n\x0cDeleteScript\x12 .nifgen_grpc.DeleteScriptRequest\x1a!.nifgen_grpc.DeleteScriptResponse\x12S\n\x0cExportSignal\x12 .nifgen_grpc.ExportSignalRequest\x1a!.nifgen_grpc.ExportSignalResponse\x12Y\n\x0eRouteSignalOut\x12".nifgen_grpc.RouteSignalOutRequest\x1a#.nifgen_grpc.RouteSignalOutResponse\x12t\n\x17SendSoftwareEdgeTrigger\x12+.nifgen_grpc.SendSoftwareEdgeTriggerRequest\x1a,.nifgen_grpc.SendSoftwareEdgeTriggerResponse\x12\x8f\x01\n ConfigureDigitalEdgeStartTrigger\x124.nifgen_grpc.ConfigureDigitalEdgeStartTriggerRequest\x1a5.nifgen_grpc.ConfigureDigitalEdgeStartTriggerResponse\x12\x92\x01\n!ConfigureSoftwareEdgeStartTrigger\x125.nifgen_grpc.ConfigureSoftwareEdgeStartTriggerRequest\x1a6.nifgen_grpc.ConfigureSoftwareEdgeStartTriggerResponse\x12h\n\x13DisableStartTrigger\x12\'.nifgen_grpc.DisableStartTriggerRequest\x1a(.nifgen_grpc.DisableStartTriggerResponse\x12\xa7\x01\n(ConfigureP2PEndpointFullnessStartTrigger\x12<.nifgen_grpc.ConfigureP2PEndpointFullnessStartTriggerRequest\x1a=.nifgen_grpc.ConfigureP2PEndpointFullnessStartTriggerResponse\x12\x92\x01\n!ConfigureDigitalEdgeScriptTrigger\x125.nifgen_grpc.ConfigureDigitalEdgeScriptTriggerRequest\x1a6.nifgen_grpc.ConfigureDigitalEdgeScriptTriggerResponse\x12\x95\x01\n"ConfigureDigitalLevelScriptTrigger\x126.nifgen_grpc.ConfigureDigitalLevelScriptTriggerRequest\x1a7.nifgen_grpc.ConfigureDigitalLevelScriptTriggerResponse\x12\x95\x01\n"ConfigureSoftwareEdgeScriptTrigger\x126.nifgen_grpc.ConfigureSoftwareEdgeScriptTriggerRequest\x1a7.nifgen_grpc.ConfigureSoftwareEdgeScriptTriggerResponse\x12k\n\x14DisableScriptTrigger\x12(.nifgen_grpc.DisableScriptTriggerRequest\x1a).nifgen_grpc.DisableScriptTriggerResponse\x12e\n\x12ConfigureClockMode\x12&.nifgen_grpc.ConfigureClockModeRequest\x1a\'.nifgen_grpc.ConfigureClockModeResponse\x12\x89\x01\n\x1eAdjustSampleClockRelativeDelay\x122.nifgen_grpc.AdjustSampleClockRelativeDelayRequest\x1a3.nifgen_grpc.AdjustSampleClockRelativeDelayResponse\x12_\n\x10AllocateWaveform\x12$.nifgen_grpc.AllocateWaveformRequest\x1a%.nifgen_grpc.AllocateWaveformResponse\x12\x83\x01\n\x1cSetWaveformNextWritePosition\x120.nifgen_grpc.SetWaveformNextWritePositionRequest\x1a1.nifgen_grpc.SetWaveformNextWritePositionResponse\x12V\n\rWriteWaveform\x12!.nifgen_grpc.WriteWaveformRequest\x1a".nifgen_grpc.WriteWaveformResponse\x12n\n\x15WriteBinary16Waveform\x12).nifgen_grpc.WriteBinary16WaveformRequest\x1a*.nifgen_grpc.WriteBinary16WaveformResponse\x12t\n\x17WriteWaveformComplexF64\x12+.nifgen_grpc.WriteWaveformComplexF64Request\x1a,.nifgen_grpc.WriteWaveformComplexF64Response\x12\x83\x01\n\x1cWriteComplexBinary16Waveform\x120.nifgen_grpc.WriteComplexBinary16WaveformRequest\x1a1.nifgen_grpc.WriteComplexBinary16WaveformResponse\x12D\n\x07SelfCal\x12\x1b.nifgen_grpc.SelfCalRequest\x1a\x1c.nifgen_grpc.SelfCalResponse\x12h\n\x13GetSelfCalSupported\x12\'.nifgen_grpc.GetSelfCalSupportedRequest\x1a(.nifgen_grpc.GetSelfCalSupportedResponse\x12z\n\x19GetSelfCalLastDateAndTime\x12-.nifgen_grpc.GetSelfCalLastDateAndTimeRequest\x1a..nifgen_grpc.GetSelfCalLastDateAndTimeResponse\x12w\n\x18GetExtCalLastDateAndTime\x12,.nifgen_grpc.GetExtCalLastDateAndTimeRequest\x1a-.nifgen_grpc.GetExtCalLastDateAndTimeResponse\x12e\n\x12GetSelfCalLastTemp\x12&.nifgen_grpc.GetSelfCalLastTempRequest\x1a\'.nifgen_grpc.GetSelfCalLastTempResponse\x12b\n\x11GetExtCalLastTemp\x12%.nifgen_grpc.GetExtCalLastTempRequest\x1a&.nifgen_grpc.GetExtCalLastTempResponse\x12\x83\x01\n\x1cGetExtCalRecommendedInterval\x120.nifgen_grpc.GetExtCalRecommendedIntervalRequest\x1a1.nifgen_grpc.GetExtCalRecommendedIntervalResponse\x12q\n\x16ReadCurrentTemperature\x12*.nifgen_grpc.ReadCurrentTemperatureRequest\x1a+.nifgen_grpc.ReadCurrentTemperatureResponse\x12\x9b\x01\n$ConfigureCustomFIRFilterCoefficients\x128.nifgen_grpc.ConfigureCustomFIRFilterCoefficientsRequest\x1a9.nifgen_grpc.ConfigureCustomFIRFilterCoefficientsResponse\x12w\n\x18GetFIRFilterCoefficients\x12,.nifgen_grpc.GetFIRFilterCoefficientsRequest\x1a-.nifgen_grpc.GetFIRFilterCoefficientsResponse\x12t\n\x17GetStreamEndpointHandle\x12+.nifgen_grpc.GetStreamEndpointHandleRequest\x1a,.nifgen_grpc.GetStreamEndpointHandleResponse\x12h\n\x13WriteP2PEndpointI16\x12\'.nifgen_grpc.WriteP2PEndpointI16Request\x1a(.nifgen_grpc.WriteP2PEndpointI16Response\x12w\n\x18ConfigureSynchronization\x12,.nifgen_grpc.ConfigureSynchronizationRequest\x1a-.nifgen_grpc.ConfigureSynchronizationResponse\x12t\n\x17EnableDigitalPatterning\x12+.nifgen_grpc.EnableDigitalPatterningRequest\x1a,.nifgen_grpc.EnableDigitalPatterningResponse\x12w\n\x18DisableDigitalPatterning\x12,.nifgen_grpc.DisableDigitalPatterningRequest\x1a-.nifgen_grpc.DisableDigitalPatterningResponse\x12h\n\x13EnableDigitalFilter\x12\'.nifgen_grpc.EnableDigitalFilterRequest\x1a(.nifgen_grpc.EnableDigitalFilterResponse\x12k\n\x14DisableDigitalFilter\x12(.nifgen_grpc.DisableDigitalFilterRequest\x1a).nifgen_grpc.DisableDigitalFilterResponse\x12e\n\x12EnableAnalogFilter\x12&.nifgen_grpc.EnableAnalogFilterRequest\x1a\'.nifgen_grpc.EnableAnalogFilterResponse\x12h\n\x13DisableAnalogFilter\x12\'.nifgen_grpc.DisableAnalogFilterRequest\x1a(.nifgen_grpc.DisableAnalogFilterResponse\x12}\n\x1aConfigureSampleClockSource\x12..nifgen_grpc.ConfigureSampleClockSourceRequest\x1a/.nifgen_grpc.ConfigureSampleClockSourceResponse\x12k\n\x14ConfigureTriggerMode\x12(.nifgen_grpc.ConfigureTriggerModeRequest\x1a).nifgen_grpc.ConfigureTriggerModeResponse\x12\x8f\x01\n ImportAttributeConfigurationFile\x124.nifgen_grpc.ImportAttributeConfigurationFileRequest\x1a5.nifgen_grpc.ImportAttributeConfigurationFileResponse\x12\x8f\x01\n ExportAttributeConfigurationFile\x124.nifgen_grpc.ExportAttributeConfigurationFileRequest\x1a5.nifgen_grpc.ExportAttributeConfigurationFileResponse\x12\x95\x01\n"ImportAttributeConfigurationBuffer\x126.nifgen_grpc.ImportAttributeConfigurationBufferRequest\x1a7.nifgen_grpc.ImportAttributeConfigurationBufferResponse\x12\x95\x01\n"ExportAttributeConfigurationBuffer\x126.nifgen_grpc.ExportAttributeConfigurationBufferRequest\x1a7.nifgen_grpc.ExportAttributeConfigurationBufferResponse\x12h\n\x13SetAttributeViInt64\x12\'.nifgen_grpc.SetAttributeViInt64Request\x1a(.nifgen_grpc.SetAttributeViInt64Response\x12n\n\x15CheckAttributeViInt64\x12).nifgen_grpc.CheckAttributeViInt64Request\x1a*.nifgen_grpc.CheckAttributeViInt64Response\x12h\n\x13GetAttributeViInt64\x12\'.nifgen_grpc.GetAttributeViInt64Request\x1a(.nifgen_grpc.GetAttributeViInt64Response\x12h\n\x13SetAttributeViInt32\x12\'.nifgen_grpc.SetAttributeViInt32Request\x1a(.nifgen_grpc.SetAttributeViInt32Response\x12k\n\x14SetAttributeViReal64\x12(.nifgen_grpc.SetAttributeViReal64Request\x1a).nifgen_grpc.SetAttributeViReal64Response\x12k\n\x14SetAttributeViString\x12(.nifgen_grpc.SetAttributeViStringRequest\x1a).nifgen_grpc.SetAttributeViStringResponse\x12n\n\x15SetAttributeViBoolean\x12).nifgen_grpc.SetAttributeViBooleanRequest\x1a*.nifgen_grpc.SetAttributeViBooleanResponse\x12n\n\x15SetAttributeViSession\x12).nifgen_grpc.SetAttributeViSessionRequest\x1a*.nifgen_grpc.SetAttributeViSessionResponse\x12n\n\x15CheckAttributeViInt32\x12).nifgen_grpc.CheckAttributeViInt32Request\x1a*.nifgen_grpc.CheckAttributeViInt32Response\x12q\n\x16CheckAttributeViReal64\x12*.nifgen_grpc.CheckAttributeViReal64Request\x1a+.nifgen_grpc.CheckAttributeViReal64Response\x12q\n\x16CheckAttributeViString\x12*.nifgen_grpc.CheckAttributeViStringRequest\x1a+.nifgen_grpc.CheckAttributeViStringResponse\x12t\n\x17CheckAttributeViBoolean\x12+.nifgen_grpc.CheckAttributeViBooleanRequest\x1a,.nifgen_grpc.CheckAttributeViBooleanResponse\x12t\n\x17CheckAttributeViSession\x12+.nifgen_grpc.CheckAttributeViSessionRequest\x1a,.nifgen_grpc.CheckAttributeViSessionResponse\x12h\n\x13GetAttributeViInt32\x12\'.nifgen_grpc.GetAttributeViInt32Request\x1a(.nifgen_grpc.GetAttributeViInt32Response\x12k\n\x14GetAttributeViReal64\x12(.nifgen_grpc.GetAttributeViReal64Request\x1a).nifgen_grpc.GetAttributeViReal64Response\x12k\n\x14GetAttributeViString\x12(.nifgen_grpc.GetAttributeViStringRequest\x1a).nifgen_grpc.GetAttributeViStringResponse\x12n\n\x15GetAttributeViBoolean\x12).nifgen_grpc.GetAttributeViBooleanRequest\x1a*.nifgen_grpc.GetAttributeViBooleanResponse\x12n\n\x15GetAttributeViSession\x12).nifgen_grpc.GetAttributeViSessionRequest\x1a*.nifgen_grpc.GetAttributeViSessionResponse\x12Y\n\x0eResetAttribute\x12".nifgen_grpc.ResetAttributeRequest\x1a#.nifgen_grpc.ResetAttributeResponse\x12n\n\x15ManualEnableP2PStream\x12).nifgen_grpc.ManualEnableP2PStreamRequest\x1a*.nifgen_grpc.ManualEnableP2PStreamResponse\x12z\n\x19CreateWaveformFromFileHWS\x12-.nifgen_grpc.CreateWaveformFromFileHWSRequest\x1a..nifgen_grpc.CreateWaveformFromFileHWSResponseB<\n\x10com.ni.grpc.fgenB\x06NiFgenP\x01\xaa\x02\x1dNationalInstruments.Grpc.Fgenb\x06proto3')`

<!--NI_PYTHON_API repo=nimi-python path=generated/nifgen/nifgen/nifgen_pb2_grpc.py -->
## PYTHON MODULE: generated/nifgen/nifgen/nifgen_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

### `class NiFgenStub(object)`

Missing associated documentation comment in .proto file.

#### `def __init__(self, channel)`

Constructor.

        Args:
            channel: A grpc.Channel.
        

### `class NiFgenServicer(object)`

Missing associated documentation comment in .proto file.

#### `def Init(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def InitWithOptions(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def InitializeWithChannels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Close(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Reset(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SelfTest(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ErrorQuery(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ErrorMessage(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def RevisionQuery(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetError(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ClearError(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ErrorHandler(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetChannelName(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ResetInterchangeCheck(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ClearInterchangeWarnings(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def InvalidateAllAttributes(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ResetWithDefaults(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Disable(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Commit(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetHardwareState(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WaitUntilDone(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def IsDone(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ResetDevice(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureOperationMode(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureOutputMode(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureReferenceClock(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureOutputImpedance(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureOutputEnabled(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureChannels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def InitiateGeneration(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def AbortGeneration(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureStandardWaveform(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DefineUserStandardWaveform(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ClearUserStandardWaveform(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureFrequency(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureAmplitude(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def QueryArbWfmCapabilities(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateWaveformF64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateWaveformI16(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateWaveformComplexF64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateWaveformFromFileI16(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateWaveformFromFileF64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureSampleRate(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureArbWaveform(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ClearArbWaveform(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def AllocateNamedWaveform(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetNamedWaveformNextWritePosition(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteNamedWaveformF64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteNamedWaveformI16(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteNamedWaveformComplexF64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteNamedWaveformComplexI16(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DeleteNamedWaveform(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def QueryArbSeqCapabilities(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateArbSequence(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAdvancedArbSequence(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureArbSequence(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ClearArbSequence(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ClearArbMemory(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def QueryFreqListCapabilities(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateFreqList(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureFreqList(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ClearFreqList(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteScript(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DeleteScript(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ExportSignal(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def RouteSignalOut(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SendSoftwareEdgeTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureDigitalEdgeStartTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureSoftwareEdgeStartTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DisableStartTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureP2PEndpointFullnessStartTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureDigitalEdgeScriptTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureDigitalLevelScriptTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureSoftwareEdgeScriptTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DisableScriptTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureClockMode(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def AdjustSampleClockRelativeDelay(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def AllocateWaveform(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetWaveformNextWritePosition(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteWaveform(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteBinary16Waveform(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteWaveformComplexF64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteComplexBinary16Waveform(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SelfCal(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetSelfCalSupported(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetSelfCalLastDateAndTime(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetExtCalLastDateAndTime(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetSelfCalLastTemp(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetExtCalLastTemp(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetExtCalRecommendedInterval(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadCurrentTemperature(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureCustomFIRFilterCoefficients(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetFIRFilterCoefficients(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetStreamEndpointHandle(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteP2PEndpointI16(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureSynchronization(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def EnableDigitalPatterning(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DisableDigitalPatterning(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def EnableDigitalFilter(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DisableDigitalFilter(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def EnableAnalogFilter(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DisableAnalogFilter(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureSampleClockSource(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureTriggerMode(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ImportAttributeConfigurationFile(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ExportAttributeConfigurationFile(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ImportAttributeConfigurationBuffer(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ExportAttributeConfigurationBuffer(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViInt64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CheckAttributeViInt64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViInt64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViReal64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViBoolean(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViSession(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CheckAttributeViInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CheckAttributeViReal64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CheckAttributeViString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CheckAttributeViBoolean(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CheckAttributeViSession(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViReal64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViBoolean(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViSession(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ResetAttribute(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ManualEnableP2PStream(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateWaveformFromFileHWS(self, request, context)`

Missing associated documentation comment in .proto file.

### `def add_NiFgenServicer_to_server(servicer, server)`

### `class NiFgen(object)`

Missing associated documentation comment in .proto file.

#### `def Init(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def InitWithOptions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def InitializeWithChannels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Close(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Reset(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SelfTest(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ErrorQuery(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ErrorMessage(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def RevisionQuery(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetError(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ClearError(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ErrorHandler(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetChannelName(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ResetInterchangeCheck(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ClearInterchangeWarnings(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def InvalidateAllAttributes(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ResetWithDefaults(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Disable(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Commit(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetHardwareState(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WaitUntilDone(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def IsDone(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ResetDevice(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureOperationMode(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureOutputMode(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureReferenceClock(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureOutputImpedance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureOutputEnabled(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureChannels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def InitiateGeneration(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def AbortGeneration(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureStandardWaveform(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DefineUserStandardWaveform(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ClearUserStandardWaveform(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureFrequency(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureAmplitude(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def QueryArbWfmCapabilities(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateWaveformF64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateWaveformI16(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateWaveformComplexF64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateWaveformFromFileI16(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateWaveformFromFileF64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureSampleRate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureArbWaveform(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ClearArbWaveform(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def AllocateNamedWaveform(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetNamedWaveformNextWritePosition(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteNamedWaveformF64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteNamedWaveformI16(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteNamedWaveformComplexF64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteNamedWaveformComplexI16(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DeleteNamedWaveform(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def QueryArbSeqCapabilities(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateArbSequence(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAdvancedArbSequence(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureArbSequence(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ClearArbSequence(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ClearArbMemory(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def QueryFreqListCapabilities(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateFreqList(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureFreqList(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ClearFreqList(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteScript(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DeleteScript(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ExportSignal(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def RouteSignalOut(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SendSoftwareEdgeTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureDigitalEdgeStartTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureSoftwareEdgeStartTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DisableStartTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureP2PEndpointFullnessStartTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureDigitalEdgeScriptTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureDigitalLevelScriptTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureSoftwareEdgeScriptTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DisableScriptTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureClockMode(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def AdjustSampleClockRelativeDelay(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def AllocateWaveform(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetWaveformNextWritePosition(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteWaveform(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteBinary16Waveform(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteWaveformComplexF64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteComplexBinary16Waveform(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SelfCal(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetSelfCalSupported(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetSelfCalLastDateAndTime(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetExtCalLastDateAndTime(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetSelfCalLastTemp(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetExtCalLastTemp(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetExtCalRecommendedInterval(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadCurrentTemperature(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureCustomFIRFilterCoefficients(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetFIRFilterCoefficients(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetStreamEndpointHandle(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteP2PEndpointI16(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureSynchronization(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def EnableDigitalPatterning(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DisableDigitalPatterning(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def EnableDigitalFilter(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DisableDigitalFilter(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def EnableAnalogFilter(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DisableAnalogFilter(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureSampleClockSource(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureTriggerMode(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ImportAttributeConfigurationFile(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ExportAttributeConfigurationFile(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ImportAttributeConfigurationBuffer(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ExportAttributeConfigurationBuffer(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViInt64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CheckAttributeViInt64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViInt64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViReal64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViBoolean(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViSession(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CheckAttributeViInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CheckAttributeViReal64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CheckAttributeViString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CheckAttributeViBoolean(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CheckAttributeViSession(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViReal64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViBoolean(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViSession(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ResetAttribute(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ManualEnableP2PStream(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateWaveformFromFileHWS(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nifgen/nifgen/session.py -->
## PYTHON MODULE: generated/nifgen/nifgen/session.py

### `class _Generation(object)`

#### `def __init__(self, session)`

#### `def __enter__(self)`

#### `def __exit__(self, exc_type, exc_value, traceback)`

### `def ivi_synchronized(f)`

### `class _Lock(object)`

#### `def __init__(self, session)`

#### `def __enter__(self)`

#### `def __exit__(self, exc_type, exc_value, traceback)`

### `class _RepeatedCapabilities(object)`

#### `def __init__(self, session, prefix, current_repeated_capability_list)`

#### `def __getitem__(self, repeated_capability)`

Set/get properties or call methods with a repeated capability (i.e. channels)

### `class _NoChannel(object)`

#### `def __init__(self, session)`

#### `def __enter__(self)`

#### `def __exit__(self, exc_type, exc_value, traceback)`

### `class _SessionBase(object)`

Base class for all NI-FGEN sessions.

#### `def __init__(self, repeated_capability_list, all_channels_in_session, interpreter, freeze_it=False)`

#### `def __repr__(self)`

#### `def __setattr__(self, key, value)`

#### `def allocate_named_waveform(self, waveform_name, waveform_size)`

allocate_named_waveform

        Specifies the size of a named waveform up front so that it can be
        allocated in onboard memory before loading the associated data. Data can
        then be loaded in smaller blocks with the niFgen Write (Binary16)
        Waveform methods.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].allocate_named_waveform`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session.allocate_named_waveform`

        Args:
            waveform_name (str): Specifies the name to associate with the allocated waveform.

            waveform_size (int): Specifies the size of the waveform to allocate in samples.

                **Default Value**: "4096"

        

#### `def allocate_waveform(self, waveform_size)`

allocate_waveform

        Specifies the size of a waveform so that it can be allocated in onboard
        memory before loading the associated data. Data can then be loaded in
        smaller blocks with the Write Binary 16 Waveform methods.

        Note:
        The signal generator must not be in the Generating state when you call
        this method.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].allocate_waveform`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session.allocate_waveform`

        Args:
            waveform_size (int): Specifies, in samples, the size of the waveform to allocate.


        Returns:
            waveform_handle (int): The handle that identifies the new waveform. This handle is used later
                when referring to this waveform.

        

#### `def clear_user_standard_waveform(self)`

clear_user_standard_waveform

        Clears the user-defined waveform created by the
        define_user_standard_waveform method.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].clear_user_standard_waveform`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session.clear_user_standard_waveform`
        

#### `def configure_arb_sequence(self, sequence_handle, gain, offset)`

configure_arb_sequence

        Configures the signal generator properties that affect arbitrary
        sequence generation. Sets the arb_sequence_handle,
        arb_gain, and arb_offset properties.

        Note:
        The signal generator must not be in the Generating state when you call
        this method.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_arb_sequence`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session.configure_arb_sequence`

        Args:
            sequence_handle (int): Specifies the handle of the arbitrary sequence that you want the signal
                generator to produce. NI-FGEN sets the
                arb_sequence_handle property to this value. You can
                create an arbitrary sequence using the create_arb_sequence or
                create_advanced_arb_sequence method. These methods return a
                handle that you use to identify the sequence.

                **Default Value**: None

            gain (float): Specifies the factor by which the signal generator scales the arbitrary
                waveforms in the sequence. When you create an arbitrary waveform, you
                must first normalize the data points to a range of –1.00 to +1.00. You
                can use this parameter to scale the waveform to other ranges. The gain
                is applied before the offset is added.

                For example, to configure the output signal to range from –2.00 to
                +2.00 V, set **gain** to 2.00.

                **Units**: unitless

                **Default Value**: None

            offset (float): Specifies the value the signal generator adds to the arbitrary waveform
                data. When you create arbitrary waveforms, you must first normalize the
                data points to a range of –1.00 to +1.00 V. You can use this parameter
                to shift the range of the arbitrary waveform. NI-FGEN sets the
                arb_offset property to this value.

                For example, to configure the output signal to range from 0.00 to 2.00 V
                instead of –1.00 to 1.00 V, set the offset to 1.00.

                **Units**: volts

                **Default Value**: None

        

#### `def configure_arb_waveform(self, waveform_handle, gain, offset)`

configure_arb_waveform

        Configures the properties of the signal generator that affect arbitrary
        waveform generation. Sets the arb_waveform_handle,
        arb_gain, and arb_offset properties.

        Note:
        The signal generator must not be in the Generating state when you call
        this method.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_arb_waveform`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session.configure_arb_waveform`

        Args:
            waveform_handle (int): Specifies the handle of the arbitrary waveform you want the signal
                generator to produce. NI-FGEN sets the
                arb_waveform_handle property to this value. You can
                create an arbitrary waveform using one of the following niFgen Create
                Waveform methods:

                -  create_waveform
                -  create_waveform
                -  create_waveform_from_file_i16
                -  create_waveform_from_file_f64

                These methods return a handle that you use to identify the waveform.

                **Default Value**: None

            gain (float): Specifies the factor by which the signal generator scales the arbitrary
                waveforms in the sequence. When you create an arbitrary waveform, you
                must first normalize the data points to a range of –1.00 to +1.00. You
                can use this parameter to scale the waveform to other ranges. The gain
                is applied before the offset is added.

                For example, to configure the output signal to range from –2.00 to
                +2.00 V, set **gain** to 2.00.

                **Units**: unitless

                **Default Value**: None

            offset (float): Specifies the value the signal generator adds to the arbitrary waveform
                data. When you create arbitrary waveforms, you must first normalize the
                data points to a range of –1.00 to +1.00 V. You can use this parameter
                to shift the range of the arbitrary waveform. NI-FGEN sets the
                arb_offset property to this value.

                For example, to configure the output signal to range from 0.00 to 2.00 V
                instead of –1.00 to 1.00 V, set the offset to 1.00.

                **Units**: volts

                **Default Value**: None

        

#### `def configure_freq_list(self, frequency_list_handle, amplitude, dc_offset=0.0, start_phase=0.0)`

configure_freq_list

        Configures the properties of the signal generator that affect frequency
        list generation (the freq_list_handle,
        func_amplitude, func_dc_offset, and
        func_start_phase properties).

        Note:
        The signal generator must not be in the Generating state when you call
        this method.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_freq_list`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session.configure_freq_list`

        Args:
            frequency_list_handle (int): Specifies the handle of the frequency list that you want the signal
                generator to produce. NI-FGEN sets the freq_list_handle
                property to this value. You can create a frequency list using the
                create_freq_list method, which returns a handle that you use to
                identify the list.
                **Default Value**: None

            amplitude (float): Specifies the amplitude of the standard waveform that you want the
                signal generator to produce. This value is the amplitude at the output
                terminal. NI-FGEN sets the func_amplitude property to
                this value.

                For example, to produce a waveform ranging from –5.00 V to +5.00 V, set
                the amplitude to 10.00 V.

                **Units**: peak-to-peak voltage

                **Default Value**: None

                Note:
                This parameter does not affect signal generator behavior when you set
                the **waveform** parameter of the configure_standard_waveform
                method to Waveform.DC.

            dc_offset (float): Specifies the DC offset of the standard waveform that you want the
                signal generator to produce. The value is the offset from ground to the
                center of the waveform you specify with the **waveform** parameter,
                observed at the output terminal. For example, to configure a waveform
                with an amplitude of 10.00 V to range from 0.00 V to +10.00 V, set the
                **dcOffset** to 5.00 V. NI-FGEN sets the func_dc_offset
                property to this value.

                **Units**: volts

                **Default Value**: None

            start_phase (float): Specifies the horizontal offset of the standard waveform you want the
                signal generator to produce. Specify this property in degrees of one
                waveform cycle. NI-FGEN sets the func_start_phase
                property to this value. A start phase of 180 degrees means output
                generation begins halfway through the waveform. A start phase of 360
                degrees offsets the output by an entire waveform cycle, which is
                identical to a start phase of 0 degrees.

                **Units**: degrees of one cycle

                **Default Value**: None degrees

                Note:
                This parameter does not affect signal generator behavior when you set
                the **waveform** parameter to Waveform.DC.

        

#### `def configure_standard_waveform(self, waveform, amplitude, frequency, dc_offset=0.0, start_phase=0.0)`

configure_standard_waveform

        Configures the following properties of the signal generator that affect
        standard waveform generation:

        -  func_waveform
        -  func_amplitude
        -  func_dc_offset
        -  func_frequency
        -  func_start_phase

        Note:
        You must call the ConfigureOutputMode method with the
        **outputMode** parameter set to OutputMode.FUNC before calling
        this method.

        Note:
        One or more of the referenced methods are not in the Python API for this driver.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_standard_waveform`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session.configure_standard_waveform`

        Args:
            waveform (enums.Waveform): Specifies the standard waveform that you want the signal generator to
                produce. NI-FGEN sets the func_waveform property to this
                value.

                ****Defined Values****

                **Default Value**: Waveform.SINE

                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.SINE      | Specifies that the signal generator produces a sinusoid waveform.                                                              |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.SQUARE    | Specifies that the signal generator produces a square waveform.                                                                |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.TRIANGLE  | Specifies that the signal generator produces a triangle waveform.                                                              |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.RAMP_UP   | Specifies that the signal generator produces a positive ramp waveform.                                                         |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.RAMP_DOWN | Specifies that the signal generator produces a negative ramp waveform.                                                         |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.DC        | Specifies that the signal generator produces a constant voltage.                                                               |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.NOISE     | Specifies that the signal generator produces white noise.                                                                      |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.USER      | Specifies that the signal generator produces a user-defined waveform as defined with the define_user_standard_waveform method. |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+

            amplitude (float): Specifies the amplitude of the standard waveform that you want the
                signal generator to produce. This value is the amplitude at the output
                terminal. NI-FGEN sets the func_amplitude property to
                this value.

                For example, to produce a waveform ranging from –5.00 V to +5.00 V, set
                the amplitude to 10.00 V.

                **Units**: peak-to-peak voltage

                **Default Value**: None

                Note:
                This parameter does not affect signal generator behavior when you set
                the **waveform** parameter of the configure_standard_waveform
                method to Waveform.DC.

            frequency (float): | Specifies the frequency of the standard waveform that you want the
                  signal generator to produce. NI-FGEN sets the
                  func_frequency property to this value.

                **Units**: hertz

                **Default Value**: None

                Note:
                This parameter does not affect signal generator behavior when you set
                the **waveform** parameter of the configure_standard_waveform
                method to Waveform.DC.

            dc_offset (float): Specifies the DC offset of the standard waveform that you want the
                signal generator to produce. The value is the offset from ground to the
                center of the waveform you specify with the **waveform** parameter,
                observed at the output terminal. For example, to configure a waveform
                with an amplitude of 10.00 V to range from 0.00 V to +10.00 V, set the
                **dcOffset** to 5.00 V. NI-FGEN sets the func_dc_offset
                property to this value.

                **Units**: volts

                **Default Value**: None

            start_phase (float): Specifies the horizontal offset of the standard waveform that you want
                the signal generator to produce. Specify this parameter in degrees of
                one waveform cycle. NI-FGEN sets the func_start_phase
                property to this value. A start phase of 180 degrees means output
                generation begins halfway through the waveform. A start phase of 360
                degrees offsets the output by an entire waveform cycle, which is
                identical to a start phase of 0 degrees.

                **Units**: degrees of one cycle

                **Default Value**: 0.00

                Note:
                This parameter does not affect signal generator behavior when you set
                the **waveform** parameter to Waveform.DC.

        

#### `def create_waveform(self, waveform_data_array)`

create_waveform

        Creates an onboard waveform for use in Arbitrary Waveform output mode or Arbitrary Sequence output mode.

        Note: You must set output_mode to OutputMode.ARB or OutputMode.SEQ before calling this method.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].create_waveform`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session.create_waveform`

        Args:
            waveform_data_array (iterable of float or int16): Array of data for the new arbitrary waveform. This may be an iterable of float or int16, or for best performance a numpy.ndarray of dtype int16 or float64.


        Returns:
            waveform_handle (int): The handle that identifies the new waveform. This handle is used in other methods when referring to this waveform.

        

#### `def _create_waveform_f64(self, waveform_data_array)`

_create_waveform_f64

        Creates an onboard waveform from binary F64 (floating point double) data
        for use in Arbitrary Waveform output mode or Arbitrary Sequence output
        mode. The **waveformHandle** returned can later be used for setting the
        active waveform, changing the data in the waveform, building sequences
        of waveforms, or deleting the waveform when it is no longer needed.

        Note:
        You must call the ConfigureOutputMode method to set the
        **outputMode** parameter to OutputMode.ARB or
        OutputMode.SEQ before calling this method.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._create_waveform_f64`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._create_waveform_f64`

        Args:
            waveform_data_array (array.array("d")): Specifies the array of data you want to use for the new arbitrary
                waveform. The array must have at least as many elements as the value
                that you specify in **waveformSize**.

                You must normalize the data points in the array to be between –1.00 and
                +1.00.

                **Default Value**: None


        Returns:
            waveform_handle (int): The handle that identifies the new waveform. This handle is used later
                when referring to this waveform.

        

#### `def _create_waveform_f64_numpy(self, waveform_data_array)`

_create_waveform_f64_numpy

        Creates an onboard waveform from binary F64 (floating point double) data
        for use in Arbitrary Waveform output mode or Arbitrary Sequence output
        mode. The **waveformHandle** returned can later be used for setting the
        active waveform, changing the data in the waveform, building sequences
        of waveforms, or deleting the waveform when it is no longer needed.

        Note:
        You must call the ConfigureOutputMode method to set the
        **outputMode** parameter to OutputMode.ARB or
        OutputMode.SEQ before calling this method.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._create_waveform_f64`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._create_waveform_f64`

        Args:
            waveform_data_array (numpy.array(dtype=numpy.float64)): Specifies the array of data you want to use for the new arbitrary
                waveform. The array must have at least as many elements as the value
                that you specify in **waveformSize**.

                You must normalize the data points in the array to be between –1.00 and
                +1.00.

                **Default Value**: None


        Returns:
            waveform_handle (int): The handle that identifies the new waveform. This handle is used later
                when referring to this waveform.

        

#### `def create_waveform_from_file_f64(self, file_name, byte_order)`

create_waveform_from_file_f64

        This method takes the floating point double (F64) data from the
        specified file and creates an onboard waveform for use in Arbitrary
        Waveform or Arbitrary Sequence output mode. The **waveformHandle**
        returned by this method can later be used for setting the active
        waveform, changing the data in the waveform, building sequences of
        waveforms, or deleting the waveform when it is no longer needed.

        Note:
        The F64 data must be between –1.0 and +1.0 V. Use the
        digital_gain property to generate different voltage
        outputs.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].create_waveform_from_file_f64`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session.create_waveform_from_file_f64`

        Args:
            file_name (str): The full path and name of the file where the waveform data resides.

            byte_order (enums.ByteOrder): Specifies the byte order of the data in the file.

                ****Defined Values****

                |
                | ****Default Value**:** ByteOrder.LITTLE

                +------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
                | ByteOrder.LITTLE | Little Endian Data—The least significant bit is stored at the lowest address, followed by the other bits, in order of increasing significance. |
                +------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
                | ByteOrder.BIG    | Big Endian Data—The most significant bit is stored at the lowest address, followed by the other bits, in order of decreasing significance.     |
                +------------------+------------------------------------------------------------------------------------------------------------------------------------------------+

                Note:
                Data written by most applications in Windows (including
                LabWindows™/CVI™) is in Little Endian format. Data written to a file
                from LabVIEW is in Big Endian format by default on all platforms. Big
                Endian and Little Endian refer to the way data is stored in memory,
                which can differ on different processors.


        Returns:
            waveform_handle (int): The handle that identifies the new waveform. This handle is used later
                when referring to this waveform.

        

#### `def create_waveform_from_file_i16(self, file_name, byte_order)`

create_waveform_from_file_i16

        Takes the binary 16-bit signed integer (I16) data from the specified
        file and creates an onboard waveform for use in Arbitrary Waveform or
        Arbitrary Sequence output mode. The **waveformHandle** returned by this
        method can later be used for setting the active waveform, changing the
        data in the waveform, building sequences of waveforms, or deleting the
        waveform when it is no longer needed.

        Note:
        The I16 data (values between –32768 and +32767) is assumed to
        represent –1 to +1 V. Use the digital_gain property to
        generate different voltage outputs.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].create_waveform_from_file_i16`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session.create_waveform_from_file_i16`

        Args:
            file_name (str): The full path and name of the file where the waveform data resides.

            byte_order (enums.ByteOrder): Specifies the byte order of the data in the file.

                ****Defined Values****

                |
                | ****Default Value**:** ByteOrder.LITTLE

                +------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
                | ByteOrder.LITTLE | Little Endian Data—The least significant bit is stored at the lowest address, followed by the other bits, in order of increasing significance. |
                +------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
                | ByteOrder.BIG    | Big Endian Data—The most significant bit is stored at the lowest address, followed by the other bits, in order of decreasing significance.     |
                +------------------+------------------------------------------------------------------------------------------------------------------------------------------------+

                Note:
                Data written by most applications in Windows (including
                LabWindows™/CVI™) is in Little Endian format. Data written to a file
                from LabVIEW is in Big Endian format by default on all platforms. Big
                Endian and Little Endian refer to the way data is stored in memory,
                which can differ on different processors.


        Returns:
            waveform_handle (int): The handle that identifies the new waveform. This handle is used later
                when referring to this waveform.

        

#### `def _create_waveform_i16_numpy(self, waveform_data_array)`

_create_waveform_i16_numpy

        Creates an onboard waveform from binary 16-bit signed integer (I16) data
        for use in Arbitrary Waveform or Arbitrary Sequence output mode. The
        **waveformHandle** returned can later be used for setting the active
        waveform, changing the data in the waveform, building sequences of
        waveforms, or deleting the waveform when it is no longer needed.

        Note:
        You must call the ConfigureOutputMode method to set the
        **outputMode** parameter to OutputMode.ARB or
        OutputMode.SEQ before calling this method.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._create_waveform_i16`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._create_waveform_i16`

        Args:
            waveform_data_array (numpy.array(dtype=numpy.int16)): Specify the array of data that you want to use for the new arbitrary
                waveform. The array must have at least as many elements as the value
                that you specify in the Waveform Size parameter.
                You must normalize the data points in the array to be between -32768 and
                +32767.
                ****Default Value**:** None


        Returns:
            waveform_handle (int): The handle that identifies the new waveform. This handle is used later
                when referring to this waveform.

        

#### `def define_user_standard_waveform(self, waveform_data_array)`

define_user_standard_waveform

        Defines a user waveform for use in either Standard Method or Frequency
        List output mode.

        To select the waveform, set the **waveform** parameter to
        Waveform.USER with either the configure_standard_waveform
        or the create_freq_list method.

        The waveform data must be scaled between –1.0 and 1.0. Use the
        **amplitude** parameter in the configure_standard_waveform
        method to generate different output voltages.

        Note:
        You must call the ConfigureOutputMode method to set the
        **outputMode** parameter to OutputMode.FUNC or
        OutputMode.FREQ_LIST before calling this method.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].define_user_standard_waveform`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session.define_user_standard_waveform`

        Args:
            waveform_data_array (list of float): Specifies the array of data you want to use for the new arbitrary
                waveform. The array must have at least as many elements as the value
                that you specify in **waveformSize**.

                You must normalize the data points in the array to be between –1.00 and
                +1.00.

                **Default Value**: None

        

#### `def _delete_named_waveform(self, waveform_name)`

_delete_named_waveform

        Removes a previously created arbitrary waveform from the signal
        generator memory and invalidates the waveform handle.

        Note:
        The signal generator must not be in the Generating state when you call
        this method.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._delete_named_waveform`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._delete_named_waveform`

        Args:
            waveform_name (str): Specifies the name to associate with the allocated waveform.

        

#### `def delete_script(self, script_name)`

delete_script

        Deletes the specified script from onboard memory.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].delete_script`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session.delete_script`

        Args:
            script_name (str): Specifies the name of the script you want to delete. The script name
                appears in the text of the script following the script keyword.

        

#### `def delete_waveform(self, waveform_name_or_handle)`

delete_waveform

        Removes a previously created arbitrary waveform from the signal generator memory.

        Note: The signal generator must not be in the Generating state when you call this method.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].delete_waveform`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session.delete_waveform`

        Args:
            waveform_name_or_handle (str or int): The name (str) or handle (int) of an arbitrary waveform previously allocated with allocate_named_waveform, allocate_waveform or create_waveform.

        

#### `def _get_attribute_vi_boolean(self, attribute_id)`

_get_attribute_vi_boolean

        Queries the value of a ViBoolean property.

        You can use this method to get the values of instrument-specific
        properties and inherent IVI properties. If the property represents an
        instrument state, this method performs instrument I/O in the following
        cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_boolean`

        Args:
            attribute_id (int): Specifies the ID of a property.


        Returns:
            attribute_value (bool): Returns the current value of the property. Pass the address of a
                ViBoolean variable.

        

#### `def _get_attribute_vi_int32(self, attribute_id)`

_get_attribute_vi_int32

        Queries the value of a ViInt32 property. You can use this method to
        get the values of instrument-specific properties and inherent IVI
        properties. If the property represents an instrument state, this
        method performs instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_int32`

        Args:
            attribute_id (int): Specifies the ID of a property.


        Returns:
            attribute_value (int): Returns the current value of the property. Pass the address of a
                ViInt32 variable.

        

#### `def _get_attribute_vi_real64(self, attribute_id)`

_get_attribute_vi_real64

        Queries the value of a ViReal64 property.

        You can use this method to get the values of instrument-specific
        properties and inherent IVI properties. If the property represents an
        instrument state, this method performs instrument I/O in the following
        cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_real64`

        Args:
            attribute_id (int): Specifies the ID of a property.


        Returns:
            attribute_value (float): Returns the current value of the property. Pass the address of a
                ViReal64 variable.

        

#### `def _get_attribute_vi_string(self, attribute_id)`

_get_attribute_vi_string

        Queries the value of a ViString property.

        You can use this method to get the values of instrument-specific
        properties and inherent IVI properties. If the property represents an
        instrument state, this method performs instrument I/O in the following
        cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid.

        You must provide a ViChar array to serve as a buffer for the value. You
        pass the number of bytes in the buffer as the **arraySize** parameter.
        If the current value of the property, including the terminating NUL
        byte, is larger than the size you indicate in the **arraySize**
        parameter, the method copies **arraySize** – 1 bytes into the buffer,
        places an ASCII NUL byte at the end of the buffer, and returns the array
        size you must pass to get the entire value. For example, if the value is
        123456 and **arraySize** is 4, the method places 123 into the buffer
        and returns 7.

        If you want to call this method just to get the required array size,
        you can pass 0 for **arraySize** and VI_NULL for the **attributeValue**
        buffer.

        If you want the method to fill in the buffer regardless of the number
        of bytes in the value, pass a negative number for the **arraySize**
        parameter.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_string`

        Args:
            attribute_id (int): Specifies the ID of a property.


        Returns:
            attribute_value (str): The buffer in which the method returns the current value of the
                property. The buffer must be a ViChar data type and have at least as
                many bytes as indicated in the **arraySize** parameter.

                If the current value of the property, including the terminating NUL
                byte, contains more bytes than you indicate in this parameter, the
                method copies **arraySize** – 1 bytes into the buffer, places an ASCII
                NUL byte at the end of the buffer, and returns the array size you must
                pass to get the entire value. For example, if the value is 123456 and
                **arraySize** is 4, the method places 123 into the buffer and returns
                7.

                If you specify 0 for the **arraySize** parameter, you can pass VI_NULL
                for this parameter.

        

#### `def lock(self)`

lock

        Obtains a multithread lock on the device session. Before doing so, the
        software waits until all other execution threads release their locks
        on the device session.

        Other threads may have obtained a lock on this session for the
        following reasons:

            -  The application called the lock method.
            -  A call to NI-FGEN locked the session.
            -  After a call to the lock method returns
               successfully, no other threads can access the device session until
               you call the unlock method or exit out of the with block when using
               lock context manager.
            -  Use the lock method and the
               unlock method around a sequence of calls to
               instrument driver methods if you require that the device retain its
               settings through the end of the sequence.

        You can safely make nested calls to the lock method
        within the same thread. To completely unlock the session, you must
        balance each call to the lock method with a call to
        the unlock method.

        Returns:
            lock (context manager): When used in a with statement, nifgen.Session.lock acts as
            a context manager and unlock will be called when the with block is exited
        

#### `def send_software_edge_trigger(self, trigger=None, trigger_id=None)`

send_software_edge_trigger

        Sends a command to trigger the signal generator. This VI can act as an
        override for an external edge trigger.

        Note:
        This VI does not override external digital edge triggers of the
        NI 5401/5411/5431.

        Args:
            trigger (enums.Trigger): Trigger specifies the type of software trigger to send

                +----------------+
                | Defined Values |
                +================+
                | Trigger.START  |
                +----------------+
                | Trigger.SCRIPT |
                +----------------+

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            trigger_id (str): Trigger ID specifies the Script Trigger to use for triggering.

        

#### `def _set_attribute_vi_boolean(self, attribute_id, attribute_value)`

_set_attribute_vi_boolean

        Sets the value of a ViBoolean property.

        This is a low-level method that you can use to set the values of
        instrument-specific properties and inherent IVI properties. If the
        property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid or
           is different than the value you specify.

        NI-FGEN contains high-level methods that set most of the instrument
        properties. NI recommends that you use the high-level driver methods
        as much as possible. They handle order dependencies and multithread
        locking for you. In addition, they perform status checking only after
        setting all of the properties. In contrast, when you set multiple
        properties using the Set Property methods, the methods check the
        instrument status after each call.

        Also, when state caching is enabled, the high-level methods that
        configure multiple properties perform instrument I/O only for the
        properties whose value you change. Thus, you can safely call the
        high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_boolean`

        Args:
            attribute_id (int): Specifies the ID of a property.

            attribute_value (bool): Specifies the value to which you want to set the property. **Default
                Value**: None

                Note:
                Some of the values might not be valid depending on the current
                settings of the instrument session.

        

#### `def _set_attribute_vi_int32(self, attribute_id, attribute_value)`

_set_attribute_vi_int32

        Sets the value of a ViInt32 property.

        This is a low-level method that you can use to set the values of
        instrument-specific properties and inherent IVI properties. If the
        property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid or
           is different than the value you specify.

        NI-FGEN contains high-level methods that set most of the instrument
        properties. NI recommends that you use the high-level driver methods
        as much as possible. They handle order dependencies and multithread
        locking for you. In addition, they perform status checking only after
        setting all of the properties. In contrast, when you set multiple
        properties using the Set Property methods, the methods check the
        instrument status after each call.

        Also, when state caching is enabled, the high-level methods that
        configure multiple properties perform instrument I/O only for the
        properties whose value you change. Thus, you can safely call the
        high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_int32`

        Args:
            attribute_id (int): Specifies the ID of a property.

            attribute_value (int): Specifies the value to which you want to set the property. **Default
                Value**: None

                Note:
                Some of the values might not be valid depending on the current
                settings of the instrument session.

        

#### `def _set_attribute_vi_real64(self, attribute_id, attribute_value)`

_set_attribute_vi_real64

        Sets the value of a ViReal64 property.

        This is a low-level method that you can use to set the values of
        instrument-specific properties and inherent IVI properties. If the
        property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid or
           is different than the value you specify.

        NI-FGEN contains high-level methods that set most of the instrument
        properties. NI recommends that you use the high-level driver methods
        as much as possible. They handle order dependencies and multithread
        locking for you. In addition, they perform status checking only after
        setting all of the properties. In contrast, when you set multiple
        properties using the Set Property methods, the methods check the
        instrument status after each call.

        Also, when state caching is enabled, the high-level methods that
        configure multiple properties perform instrument I/O only for the
        properties whose value you change. Thus, you can safely call the
        high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_real64`

        Args:
            attribute_id (int): Specifies the ID of a property.

            attribute_value (float): Specifies the value to which you want to set the property. **Default
                Value**: None

                Note:
                Some of the values might not be valid depending on the current
                settings of the instrument session.

        

#### `def _set_attribute_vi_string(self, attribute_id, attribute_value)`

_set_attribute_vi_string

        Sets the value of a ViString property.

        This is a low-level method that you can use to set the values of
        instrument-specific properties and inherent IVI properties. If the
        property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid or
           is different than the value you specify.

        NI-FGEN contains high-level methods that set most of the instrument
        properties. NI recommends that you use the high-level driver methods
        as much as possible. They handle order dependencies and multithread
        locking for you. In addition, they perform status checking only after
        setting all of the properties. In contrast, when you set multiple
        properties using the Set Property methods, the methods check the
        instrument status after each call.

        Also, when state caching is enabled, the high-level methods that
        configure multiple properties perform instrument I/O only for the
        properties whose value you change. Thus, you can safely call the
        high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_string`

        Args:
            attribute_id (int): Specifies the ID of a property.

            attribute_value (str): Specifies the value to which you want to set the property. **Default
                Value**: None

                Note:
                Some of the values might not be valid depending on the current
                settings of the instrument session.

        

#### `def _set_named_waveform_next_write_position(self, waveform_name, relative_to, offset)`

_set_named_waveform_next_write_position

        Sets the position in the waveform to which data is written at the next
        write. This method allows you to write to arbitrary locations within
        the waveform. These settings apply only to the next write to the
        waveform specified by the **waveformHandle** parameter. Subsequent
        writes to that waveform begin where the last write left off, unless this
        method is called again. The **waveformHandle** passed in must have
        been created with a call to one of the following methods:

        -  allocate_waveform
        -  create_waveform
        -  create_waveform
        -  create_waveform_from_file_i16
        -  create_waveform_from_file_f64

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_named_waveform_next_write_position`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._set_named_waveform_next_write_position`

        Args:
            waveform_name (str): Specifies the name to associate with the allocated waveform.

            relative_to (enums.RelativeTo): Specifies the reference position in the waveform. This position and
                **offset** together determine where to start loading data into the
                waveform.

                ****Defined Values****

                +------------------------+-------------------------------------------------------------------------+
                | RelativeTo.START (0)   | Use the start of the waveform as the reference position.                |
                +------------------------+-------------------------------------------------------------------------+
                | RelativeTo.CURRENT (1) | Use the current position within the waveform as the reference position. |
                +------------------------+-------------------------------------------------------------------------+

            offset (int): Specifies the offset from the **relativeTo** parameter at which to start
                loading the data into the waveform.

        

#### `def set_next_write_position(self, waveform_name_or_handle, relative_to, offset)`

set_next_write_position

        Sets the position in the waveform at which the next waveform data is
        written. This method allows you to write to arbitrary locations within
        the waveform. These settings apply only to the next write to the
        waveform specified by the waveformHandle parameter. Subsequent writes to
        that waveform begin where the last write left off, unless this method
        is called again. The waveformHandle passed in must have been created by
        a call to the allocate_waveform method or one of the following
        create_waveform method.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].set_next_write_position`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session.set_next_write_position`

        Args:
            waveform_name_or_handle (str or int): The name (str) or handle (int) of an arbitrary waveform previously allocated with allocate_named_waveform, allocate_waveform or create_waveform.

            relative_to (enums.RelativeTo): Specifies the reference position in the waveform. This position and
                **offset** together determine where to start loading data into the
                waveform.

                ****Defined Values****

                +------------------------+-------------------------------------------------------------------------+
                | RelativeTo.START (0)   | Use the start of the waveform as the reference position.                |
                +------------------------+-------------------------------------------------------------------------+
                | RelativeTo.CURRENT (1) | Use the current position within the waveform as the reference position. |
                +------------------------+-------------------------------------------------------------------------+

            offset (int): Specifies the offset from **relativeTo** at which to start loading the
                data into the waveform.

        

#### `def _set_waveform_next_write_position(self, waveform_handle, relative_to, offset)`

_set_waveform_next_write_position

        Sets the position in the waveform at which the next waveform data is
        written. This method allows you to write to arbitrary locations within
        the waveform. These settings apply only to the next write to the
        waveform specified by the waveformHandle parameter. Subsequent writes to
        that waveform begin where the last write left off, unless this method
        is called again. The waveformHandle passed in must have been created by
        a call to the allocate_waveform method or one of the following
        niFgen CreateWaveform methods:

        -  create_waveform
        -  create_waveform
        -  create_waveform_from_file_i16
        -  create_waveform_from_file_f64

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_waveform_next_write_position`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._set_waveform_next_write_position`

        Args:
            waveform_handle (int): Specifies the handle of the arbitrary waveform previously allocated with
                the allocate_waveform method.

            relative_to (enums.RelativeTo): Specifies the reference position in the waveform. This position and
                **offset** together determine where to start loading data into the
                waveform.

                ****Defined Values****

                +------------------------+-------------------------------------------------------------------------+
                | RelativeTo.START (0)   | Use the start of the waveform as the reference position.                |
                +------------------------+-------------------------------------------------------------------------+
                | RelativeTo.CURRENT (1) | Use the current position within the waveform as the reference position. |
                +------------------------+-------------------------------------------------------------------------+

            offset (int): Specifies the offset from **relativeTo** at which to start loading the
                data into the waveform.

        

#### `def unlock(self)`

unlock

        Releases a lock that you acquired on an device session using
        lock. Refer to lock for additional
        information on session locks.
        

#### `def _write_binary16_waveform_numpy(self, waveform_handle, data)`

_write_binary16_waveform_numpy

        Writes binary data to the waveform in onboard memory. The waveform
        handle passed must have been created by a call to the
        allocate_waveform or the create_waveform method.

        By default, the subsequent call to the write_waveform
        method continues writing data from the position of the last sample
        written. You can set the write position and offset by calling the
        set_next_write_position method. If streaming is enabled,
        you can write more data than the allocated waveform size in onboard
        memory. Refer to the
        `Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
        information about streaming data.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._write_binary16_waveform`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._write_binary16_waveform`

        Args:
            waveform_handle (int): Specifies the handle of the arbitrary waveform previously allocated with
                the allocate_waveform method.

            data (numpy.array(dtype=numpy.int16)): Specifies the array of data to load into the waveform. The array must
                have at least as many elements as the value in **size**. The binary data
                is left-justified.

        

#### `def _write_named_waveform_f64(self, waveform_name, data)`

_write_named_waveform_f64

        Writes floating-point data to the waveform in onboard memory. The
        waveform handle passed in must have been created by a call to the
        allocate_waveform method or to one of the following niFgen
        Create Waveform methods:

        -  create_waveform
        -  create_waveform
        -  create_waveform_from_file_i16
        -  create_waveform_from_file_f64

        By default, the subsequent call to the write_waveform
        method continues writing data from the position of the last sample
        written. You can set the write position and offset by calling the
        set_next_write_position method. If streaming is
        enabled, you can write more data than the allocated waveform size in
        onboard memory. Refer to the
        `Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
        information about streaming data.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._write_named_waveform_f64`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._write_named_waveform_f64`

        Args:
            waveform_name (str): Specifies the name to associate with the allocated waveform.

            data (array.array("d")): Specifies the array of data to load into the waveform. The array must
                have at least as many elements as the value in **size**.

        

#### `def _write_named_waveform_f64_numpy(self, waveform_name, data)`

_write_named_waveform_f64_numpy

        Writes floating-point data to the waveform in onboard memory. The
        waveform handle passed in must have been created by a call to the
        allocate_waveform method or to one of the following niFgen
        Create Waveform methods:

        -  create_waveform
        -  create_waveform
        -  create_waveform_from_file_i16
        -  create_waveform_from_file_f64

        By default, the subsequent call to the write_waveform
        method continues writing data from the position of the last sample
        written. You can set the write position and offset by calling the
        set_next_write_position method. If streaming is
        enabled, you can write more data than the allocated waveform size in
        onboard memory. Refer to the
        `Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
        information about streaming data.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._write_named_waveform_f64`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._write_named_waveform_f64`

        Args:
            waveform_name (str): Specifies the name to associate with the allocated waveform.

            data (numpy.array(dtype=numpy.float64)): Specifies the array of data to load into the waveform. The array must
                have at least as many elements as the value in **size**.

        

#### `def _write_named_waveform_i16_numpy(self, waveform_name, data)`

_write_named_waveform_i16_numpy

        Writes binary data to the named waveform in onboard memory.

        By default, the subsequent call to the write_waveform
        method continues writing data from the position of the last sample
        written. You can set the write position and offset by calling the
        set_next_write_position method. If streaming is
        enabled, you can write more data than the allocated waveform size in
        onboard memory. Refer to the
        `Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
        information about streaming data.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._write_named_waveform_i16`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._write_named_waveform_i16`

        Args:
            waveform_name (str): Specifies the name to associate with the allocated waveform.

            data (numpy.array(dtype=numpy.int16)): Specifies the array of data to load into the waveform. The array must
                have at least as many elements as the value in **size**.

        

#### `def write_script(self, script)`

write_script

        Writes a string containing one or more scripts that govern the
        generation of waveforms.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].write_script`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session.write_script`

        Args:
            script (str): Contains the text of the script you want to use for your generation
                operation. Refer to `scripting
                Instructions <REPLACE_DRIVER_SPECIFIC_URL_2(niscripted.chm',%20'scripting_instructions)>`__
                for more information about writing scripts.

        

#### `def _write_waveform(self, waveform_handle, data)`

_write_waveform

        Writes floating-point data to the waveform in onboard memory. The
        waveform handle passed in must have been created by a call to the
        allocate_waveform method or one of the following niFgen
        CreateWaveform methods:

        -  create_waveform
        -  create_waveform
        -  create_waveform_from_file_i16
        -  create_waveform_from_file_f64

        By default, the subsequent call to the write_waveform method
        continues writing data from the position of the last sample written. You
        can set the write position and offset by calling the
        set_next_write_position method. If streaming is enabled,
        you can write more data than the allocated waveform size in onboard
        memory. Refer to the
        `Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
        information about streaming data.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._write_waveform`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._write_waveform`

        Args:
            waveform_handle (int): Specifies the handle of the arbitrary waveform previously allocated with
                the allocate_waveform method.

            data (array.array("d")): Specifies the array of data to load into the waveform. The array must
                have at least as many elements as the value in **size**.

        

#### `def _write_waveform_numpy(self, waveform_handle, data)`

_write_waveform_numpy

        Writes floating-point data to the waveform in onboard memory. The
        waveform handle passed in must have been created by a call to the
        allocate_waveform method or one of the following niFgen
        CreateWaveform methods:

        -  create_waveform
        -  create_waveform
        -  create_waveform_from_file_i16
        -  create_waveform_from_file_f64

        By default, the subsequent call to the write_waveform method
        continues writing data from the position of the last sample written. You
        can set the write position and offset by calling the
        set_next_write_position method. If streaming is enabled,
        you can write more data than the allocated waveform size in onboard
        memory. Refer to the
        `Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
        information about streaming data.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._write_waveform`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._write_waveform`

        Args:
            waveform_handle (int): Specifies the handle of the arbitrary waveform previously allocated with
                the allocate_waveform method.

            data (numpy.array(dtype=numpy.float64)): Specifies the array of data to load into the waveform. The array must
                have at least as many elements as the value in **size**.

        

#### `def write_waveform(self, waveform_name_or_handle, data)`

write_waveform

        Writes data to the waveform in onboard memory.

        By default, subsequent calls to this method
        continue writing data from the position of the last sample written. You
        can set the write position and offset by calling the set_next_write_position
        set_next_write_position method.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].write_waveform`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session.write_waveform`

        Args:
            waveform_name_or_handle (str or int): The name (str) or handle (int) of an arbitrary waveform previously allocated with allocate_named_waveform, allocate_waveform or create_waveform.

            data (list of float): Array of data to load into the waveform. This may be an iterable of float, or for best performance a numpy.ndarray of dtype int16 or float64.

        

#### `def _error_message(self, error_code)`

_error_message

        Converts a status code returned by an NI-FGEN method into a
        user-readable string.

        Args:
            error_code (int): Specifies the **status** parameter that is returned from any of the
                NI-FGEN methods.

                **Default Value**: 0 (VI_SUCCESS)


        Returns:
            error_message (str): Returns the error message string read from the instrument error message
                queue.

                You must pass a ViChar array with at least 256 bytes.

        

### `class Session(_SessionBase)`

An NI-FGEN session to an NI signal generator.

#### `def __init__(self, resource_name, channel_name=None, reset_device=False, options={}, *, grpc_options=None)`

An NI-FGEN session to an NI signal generator.

        Creates and returns a new NI-FGEN session to the specified channel of a
        waveform generator that is used in all subsequent NI-FGEN method
        calls.

        Args:
            resource_name (str): Caution:
                Traditional NI-DAQ and NI-DAQmx device names are not case-sensitive.
                However, all IVI names, such as logical names, are case-sensitive. If
                you use logical names, driver session names, or virtual names in your
                program, you must ensure that the name you use matches the name in the
                IVI Configuration Store file exactly, without any variations in the case
                of the characters.

                | Specifies the resource name of the device to initialize.

                For Traditional NI-DAQ devices, the syntax is DAQ::\ *n*, where *n* is
                the device number assigned by MAX, as shown in Example 1.

                For NI-DAQmx devices, the syntax is just the device name specified in
                MAX, as shown in Example 2. Typical default names for NI-DAQmx devices
                in MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by
                right-clicking on the name in MAX and entering a new name.

                An alternate syntax for NI-DAQmx devices consists of DAQ::\ *NI-DAQmx
                device name*, as shown in Example 3. This naming convention allows for
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

                +-----------+--------------------------------------+------------------------+---------------------------------+
                | Example # | Device Type                          | Syntax                 | Variable                        |
                +===========+======================================+========================+=================================+
                | 1         | Traditional NI-DAQ device            | DAQ::\ *1*             | (*1* = device number)           |
                +-----------+--------------------------------------+------------------------+---------------------------------+
                | 2         | NI-DAQmx device                      | *myDAQmxDevice*        | (*myDAQmxDevice* = device name) |
                +-----------+--------------------------------------+------------------------+---------------------------------+
                | 3         | NI-DAQmx device                      | DAQ::\ *myDAQmxDevice* | (*myDAQmxDevice* = device name) |
                +-----------+--------------------------------------+------------------------+---------------------------------+
                | 4         | NI-DAQmx device                      | DAQ::\ *2*             | (*2* = device name)             |
                +-----------+--------------------------------------+------------------------+---------------------------------+
                | 5         | IVI logical name or IVI virtual name | *myLogicalName*        | (*myLogicalName* = name)        |
                +-----------+--------------------------------------+------------------------+---------------------------------+

            channel_name (str, list, range, tuple): Specifies the channel that this VI uses.

                **Default Value**: "0"

            reset_device (bool): Specifies whether you want to reset the device during the initialization
                procedure. True specifies that the device is reset and performs the
                same method as the Reset method.

                ****Defined Values****

                **Default Value**: False

                +-------+---------------------+
                | True  | Reset device        |
                +-------+---------------------+
                | False | Do not reset device |
                +-------+---------------------+

            options (dict): Specifies the initial value of certain properties for the session. The
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

            grpc_options (nifgen.grpc_session_options.GrpcSessionOptions): MeasurementLink gRPC session options


        Returns:
            session (nifgen.Session): A session object representing the device.

        

#### `def __enter__(self)`

#### `def __exit__(self, exc_type, exc_value, traceback)`

#### `def initiate(self)`

initiate

        Initiates signal generation. If you want to abort signal generation,
        call the abort method. After the signal generation
        is aborted, you can call the initiate method to
        cause the signal generator to produce a signal again.

        Note:
        This method will return a Python context manager that will initiate on entering and abort on exit.
        

#### `def close(self)`

close

        Performs the following operations:

        -  Closes the instrument I/O session.
        -  Destroys the NI-FGEN session and all of its properties.
        -  Deallocates any memory resources NI-FGEN uses.

        Not all signal routes established by calling the ExportSignal
        and RouteSignalOut methods are released when the NI-FGEN
        session is closed. The following table shows what happens to a signal
        route on your device when you call the _close method.

        +--------------------+-------------------+------------------+
        | Routes To          | NI 5401/5411/5431 | Other Devices    |
        +====================+===================+==================+
        | Front Panel        | Remain connected  | Remain connected |
        +--------------------+-------------------+------------------+
        | RTSI/PXI Backplane | Remain connected  | Disconnected     |
        +--------------------+-------------------+------------------+

        Note:
        After calling _close, you cannot use NI-FGEN again until you
        call the init or InitWithOptions methods.

        Note:
        This method is not needed when using the session context manager
        

#### `def abort(self)`

abort

        Aborts any previously initiated signal generation. Call the
        initiate method to cause the signal generator to
        produce a signal again.
        

#### `def clear_arb_memory(self)`

clear_arb_memory

        Removes all previously created arbitrary waveforms, sequences, and
        scripts from the signal generator memory and invalidates all waveform
        handles, sequence handles, and waveform names.

        Note:
        The signal generator must not be in the Generating state when you
        call this method.
        

#### `def clear_arb_sequence(self, sequence_handle)`

clear_arb_sequence

        Removes a previously created arbitrary sequence from the signal
        generator memory and invalidates the sequence handle.

        Note:
        The signal generator must not be in the Generating state when you
        call this method.

        Args:
            sequence_handle (int): Specifies the handle of the arbitrary sequence that you want the signal
                generator to remove. You can create an arbitrary sequence using the
                create_arb_sequence or create_advanced_arb_sequence method.
                These methods return a handle that you use to identify the sequence.

                | **Defined Value**:
                | NIFGEN_VAL_ALL_SEQUENCES—Remove all sequences from the signal
                  generator

                **Default Value**: None

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        

#### `def _clear_arb_waveform(self, waveform_handle)`

_clear_arb_waveform

        Removes a previously created arbitrary waveform from the signal
        generator memory and invalidates the waveform handle.

        Note:
        The signal generator must not be in the Generating state when you
        call this method.

        Args:
            waveform_handle (int): Specifies the handle of the arbitrary waveform that you want the signal
                generator to remove.

                You can create multiple arbitrary waveforms using one of the following
                niFgen Create Waveform methods:

                -  create_waveform
                -  create_waveform
                -  create_waveform_from_file_i16
                -  create_waveform_from_file_f64

                **Defined Value**:

                NIFGEN_VAL_ALL_WAVEFORMS—Remove all waveforms from the signal
                generator.

                **Default Value**: None

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        

#### `def clear_freq_list(self, frequency_list_handle)`

clear_freq_list

        Removes a previously created frequency list from the signal generator
        memory and invalidates the frequency list handle.

        Note:
        The signal generator must not be in the Generating state when you
        call this method.

        Args:
            frequency_list_handle (int): Specifies the handle of the frequency list you want the signal generator
                to remove. You create multiple frequency lists using
                create_freq_list. create_freq_list returns a handle that you
                use to identify each list. Specify a value of -1 to clear all frequency
                lists.

                **Defined Value**

                NIFGEN_VAL_ALL_FLISTS—Remove all frequency lists from the signal
                generator.

                **Default Value**: None

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        

#### `def commit(self)`

commit

        Causes a transition to the Committed state. This method verifies
        property values, reserves the device, and commits the property values
        to the device. If the property values are all valid, NI-FGEN sets the
        device hardware configuration to match the session configuration. This
        method does not support the NI 5401/5404/5411/5431 signal generators.

        In the Committed state, you can load waveforms, scripts, and sequences
        into memory. If any properties are changed, NI-FGEN implicitly
        transitions back to the Idle state, where you can program all session
        properties before applying them to the device. This method has no
        effect if the device is already in the Committed or Generating state and
        returns a successful status value.

        Calling this VI before the niFgen Initiate Generation VI is optional but
        has the following benefits:

        -  Routes are committed, so signals are exported or imported.
        -  Any Reference Clock and external clock circuits are phase-locked.
        -  A subsequent initiate method can run faster
           because the device is already configured.
        

#### `def create_advanced_arb_sequence(self, waveform_handles_array, loop_counts_array, sample_counts_array=None, marker_location_array=None)`

create_advanced_arb_sequence

        Creates an arbitrary sequence from an array of waveform handles and an
        array of corresponding loop counts. This method returns a handle that
        identifies the sequence. You pass this handle to the
        configure_arb_sequence method to specify what arbitrary sequence
        you want the signal generator to produce.

        The create_advanced_arb_sequence method extends on the
        create_arb_sequence method by adding the ability to set the
        number of samples in each sequence step and to set marker locations.

        An arbitrary sequence consists of multiple waveforms. For each waveform,
        you specify the number of times the signal generator produces the
        waveform before proceeding to the next waveform. The number of times to
        repeat a specific waveform is called the loop count.

        Note:
        The signal generator must not be in the Generating state when you call
        this method.
        You must call the ConfigureOutputMode method to set the
        **outputMode** parameter to OutputMode.SEQ before calling this
        method.

        Args:
            waveform_handles_array (list of int): Specifies the array of waveform handles from which you want to create a
                new arbitrary sequence. The array must have at least as many elements as
                the value that you specify in **sequenceLength**. Each
                **waveformHandlesArray** element has a corresponding **loopCountsArray**
                element that indicates how many times that waveform is repeated. You
                obtain waveform handles when you create arbitrary waveforms with the
                allocate_waveform method or one of the following niFgen
                CreateWaveform methods:

                -  create_waveform
                -  create_waveform
                -  create_waveform_from_file_i16
                -  create_waveform_from_file_f64

                **Default Value**: None

            loop_counts_array (list of int): Specifies the array of loop counts you want to use to create a new
                arbitrary sequence. The array must have at least as many elements as the
                value that you specify in the **sequenceLength** parameter. Each
                **loopCountsArray** element corresponds to a **waveformHandlesArray**
                element and indicates how many times to repeat that waveform. Each
                element of the **loopCountsArray** must be less than or equal to the
                maximum number of loop counts that the signal generator allows. You can
                obtain the maximum loop count from **maximumLoopCount** in the
                query_arb_seq_capabilities method.

                **Default Value**: None

            sample_counts_array (list of int): Specifies the array of sample counts that you want to use to create a
                new arbitrary sequence. The array must have at least as many elements as
                the value you specify in the **sequenceLength** parameter. Each
                **sampleCountsArray** element corresponds to a **waveformHandlesArray**
                element and indicates the subset, in samples, of the given waveform to
                generate. Each element of the **sampleCountsArray** must be larger than
                the minimum waveform size, a multiple of the waveform quantum and no
                larger than the number of samples in the corresponding waveform. You can
                obtain these values by calling the query_arb_wfm_capabilities
                method.

                **Default Value**: None

            marker_location_array (list of int): Specifies the array of marker locations to where you want a marker to be
                generated in the sequence. The array must have at least as many elements
                as the value you specify in the **sequenceLength** parameter. Each
                **markerLocationArray** element corresponds to a
                **waveformHandlesArray** element and indicates where in the waveform a
                marker is to generate. The marker location must be less than the size of
                the waveform the marker is in. The markers are coerced to the nearest
                marker quantum and the coerced values are returned in the
                **coercedMarkersArray** parameter.

                If you do not want a marker generated for a particular sequence stage,
                set this parameter to NIFGEN_VAL_NO_MARKER.

                **Defined Value**: NIFGEN_VAL_NO_MARKER

                **Default Value**: None

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        Returns:
            coerced_markers_array (list of int): Returns an array of all given markers that are coerced (rounded) to the
                nearest marker quantum. Not all devices coerce markers.

                **Default Value**: None

            sequence_handle (int): Returns the handle that identifies the new arbitrary sequence. You can
                pass this handle to configure_arb_sequence to generate the
                arbitrary sequence.

        

#### `def create_arb_sequence(self, waveform_handles_array, loop_counts_array)`

create_arb_sequence

        Creates an arbitrary sequence from an array of waveform handles and an
        array of corresponding loop counts. This method returns a handle that
        identifies the sequence. You pass this handle to the
        configure_arb_sequence method to specify what arbitrary sequence
        you want the signal generator to produce.

        An arbitrary sequence consists of multiple waveforms. For each waveform,
        you can specify the number of times that the signal generator produces
        the waveform before proceeding to the next waveform. The number of times
        to repeat a specific waveform is called the loop count.

        Note:
        You must call the ConfigureOutputMode method to set the
        **outputMode** parameter to OutputMode.SEQ before calling this
        method.

        Args:
            waveform_handles_array (list of int): Specifies the array of waveform handles from which you want to create a
                new arbitrary sequence. The array must have at least as many elements as
                the value that you specify in **sequenceLength**. Each
                **waveformHandlesArray** element has a corresponding **loopCountsArray**
                element that indicates how many times that waveform is repeated. You
                obtain waveform handles when you create arbitrary waveforms with the
                allocate_waveform method or one of the following niFgen
                CreateWaveform methods:

                -  create_waveform
                -  create_waveform
                -  create_waveform_from_file_i16
                -  create_waveform_from_file_f64

                **Default Value**: None

            loop_counts_array (list of int): Specifies the array of loop counts you want to use to create a new
                arbitrary sequence. The array must have at least as many elements as the
                value that you specify in the **sequenceLength** parameter. Each
                **loopCountsArray** element corresponds to a **waveformHandlesArray**
                element and indicates how many times to repeat that waveform. Each
                element of the **loopCountsArray** must be less than or equal to the
                maximum number of loop counts that the signal generator allows. You can
                obtain the maximum loop count from **maximumLoopCount** in the
                query_arb_seq_capabilities method.

                **Default Value**: None


        Returns:
            sequence_handle (int): Returns the handle that identifies the new arbitrary sequence. You can
                pass this handle to configure_arb_sequence to generate the
                arbitrary sequence.

        

#### `def create_freq_list(self, waveform, frequency_array, duration_array)`

create_freq_list

        Creates a frequency list from an array of frequencies
        (**frequencyArray**) and an array of durations (**durationArray**). The
        two arrays should have the same number of elements, and this value must
        also be the size of the **frequencyListLength**. The method returns a
        handle that identifies the frequency list (the **frequencyListHandle**).
        You can pass this handle to configure_freq_list to specify what
        frequency list you want the signal generator to produce.

        A frequency list consists of a list of frequencies and durations. The
        signal generator generates each frequency for the given amount of time
        and then proceeds to the next frequency. When the end of the list is
        reached, the signal generator starts over at the beginning of the list.

        Note:
        The signal generator must not be in the Generating state when you call
        this method.

        Args:
            waveform (enums.Waveform): Specifies the standard waveform that you want the signal generator to
                produce. NI-FGEN sets the func_waveform property to this
                value.

                ****Defined Values****

                **Default Value**: Waveform.SINE

                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.SINE      | Specifies that the signal generator produces a sinusoid waveform.                                                              |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.SQUARE    | Specifies that the signal generator produces a square waveform.                                                                |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.TRIANGLE  | Specifies that the signal generator produces a triangle waveform.                                                              |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.RAMP_UP   | Specifies that the signal generator produces a positive ramp waveform.                                                         |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.RAMP_DOWN | Specifies that the signal generator produces a negative ramp waveform.                                                         |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.DC        | Specifies that the signal generator produces a constant voltage.                                                               |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.NOISE     | Specifies that the signal generator produces white noise.                                                                      |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.USER      | Specifies that the signal generator produces a user-defined waveform as defined with the define_user_standard_waveform method. |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+

            frequency_array (list of float): Specifies the array of frequencies to form the frequency list. The array
                must have at least as many elements as the value you specify in
                **frequencyListLength**. Each **frequencyArray** element has a
                corresponding **durationArray** element that indicates how long that
                frequency is repeated.

                **Units**: hertz

                **Default Value**: None

            duration_array (list of float): Specifies the array of durations to form the frequency list. The array
                must have at least as many elements as the value that you specify in
                **frequencyListLength**. Each **durationArray** element has a
                corresponding **frequencyArray** element and indicates how long in
                seconds to generate the corresponding frequency.

                **Units**: seconds

                **Default Value**: None


        Returns:
            frequency_list_handle (int): Returns the handle that identifies the new frequency list. You can pass
                this handle to configure_freq_list to generate the arbitrary
                sequence.

        

#### `def disable(self)`

disable

        Places the instrument in a quiescent state where it has minimal or no
        impact on the system to which it is connected. The analog output and all
        exported signals are disabled.
        

#### `def export_attribute_configuration_buffer(self)`

export_attribute_configuration_buffer

        Exports the property configuration of the session to a configuration
        buffer.

        You can export and import session property configurations only between
        devices with identical model numbers, channel counts, and onboard memory
        sizes.

        This method verifies that the properties you have configured for the
        session are valid. If the configuration is invalid, NI‑FGEN returns an
        error.

        Returns:
            configuration (bytes): Specifies the byte array buffer to be populated with the exported
                property configuration.

        

#### `def export_attribute_configuration_file(self, file_path)`

export_attribute_configuration_file

        Exports the property configuration of the session to the specified
        file.

        You can export and import session property configurations only between
        devices with identical model numbers, channel counts, and onboard memory
        sizes.

        This method verifies that the properties you have configured for the
        session are valid. If the configuration is invalid, NI‑FGEN returns an
        error.

        Args:
            file_path (str): Specifies the absolute path to the file to contain the exported
                property configuration. If you specify an empty or relative path, this
                method returns an error.
                **Default file extension:** .nifgenconfig

        

#### `def get_channel_name(self, index)`

get_channel_name

        Returns the channel string that is in the channel table at an index you
        specify.

        Note:
        This method is included for compliance with the IviFgen Class
        Specification.

        Args:
            index (int): A 1-based index into the channel table.


        Returns:
            channel_string (str): Returns the channel string that is in the channel table at the index you
                specify. Do not modify the contents of the channel string.

        

#### `def _get_ext_cal_last_date_and_time(self)`

_get_ext_cal_last_date_and_time

        Returns the date and time of the last successful external calibration.
        The time returned is 24-hour (military) local time; for example, if the
        device was calibrated at 2:30 PM, this method returns 14 for the
        **hour** parameter and 30 for the **minute** parameter.

        Returns:
            year (int): Specifies the year of the last successful calibration.

            month (int): Specifies the month of the last successful calibration.

            day (int): Specifies the day of the last successful calibration.

            hour (int): Specifies the hour of the last successful calibration.

            minute (int): Specifies the minute of the last successful calibration.

        

#### `def get_ext_cal_last_temp(self)`

get_ext_cal_last_temp

        Returns the temperature at the last successful external calibration. The
        temperature is returned in degrees Celsius.

        Returns:
            temperature (float): Specifies the temperature at the last successful calibration in degrees
                Celsius.

        

#### `def get_ext_cal_recommended_interval(self)`

get_ext_cal_recommended_interval

        Returns the recommended interval between external calibrations in
        months.

        Returns:
            months (hightime.timedelta): Specifies the recommended interval between external calibrations in
                months.

        

#### `def get_hardware_state(self)`

get_hardware_state

        Returns the current hardware state of the device and, if the device is
        in the hardware error state, the current hardware error.

        Note: Hardware states do not necessarily correspond to NI-FGEN states.

        Returns:
            state (enums.HardwareState): Returns the hardware state of the signal generator.

                **Defined Values**

                +-----------------------------------------+--------------------------------------------+
                | HardwareState.IDLE                      | The device is in the Idle state.           |
                +-----------------------------------------+--------------------------------------------+
                | HardwareState.WAITING_FOR_START_TRIGGER | The device is waiting for Start Trigger.   |
                +-----------------------------------------+--------------------------------------------+
                | HardwareState.RUNNING                   | The device is in the Running state.        |
                +-----------------------------------------+--------------------------------------------+
                | HardwareState.DONE                      | The generation has completed successfully. |
                +-----------------------------------------+--------------------------------------------+
                | HardwareState.HARDWARE_ERROR            | There is a hardware error.                 |
                +-----------------------------------------+--------------------------------------------+

        

#### `def get_ext_cal_last_date_and_time(self)`

get_ext_cal_last_date_and_time

        Returns the date and time of the last successful external calibration. The time returned is 24-hour (military) local time; for example, if the device was calibrated at 2:30 PM, this method returns 14 for the **hour** parameter and 30 for the **minute** parameter.

        Returns:
            last_cal_datetime (hightime.datetime): Indicates date and time of the last calibration.

        

#### `def get_self_cal_last_date_and_time(self)`

get_self_cal_last_date_and_time

        Returns the date and time of the last successful self-calibration.

        Returns:
            last_cal_datetime (hightime.datetime): Returns the date and time the device was last calibrated.

        

#### `def _get_self_cal_last_date_and_time(self)`

_get_self_cal_last_date_and_time

        Returns the date and time of the last successful self-calibration.

        All values are returned as separate parameters. Each parameter is
        returned as an integer, including the year, month, day, hour, minute,
        and second. For example, if the device is calibrated in September 2013,
        this method returns 9 for the **month** parameter and 2013 for the
        **year** parameter.

        The time returned is 24-hour (military) local time. For example, if the
        device was calibrated at 2:30 PM, this method returns 14 for the
        **hours** parameter and 30 for the **minutes** parameter.

        Returns:
            year (int): Specifies the year of the last successful calibration.

            month (int): Specifies the month of the last successful calibration.

            day (int): Specifies the day of the last successful calibration.

            hour (int): Specifies the hour of the last successful calibration.

            minute (int): Specifies the minute of the last successful calibration.

        

#### `def get_self_cal_last_temp(self)`

get_self_cal_last_temp

        Returns the temperature at the last successful self-calibration. The
        temperature is returned in degrees Celsius.

        Returns:
            temperature (float): Specifies the temperature at the last successful calibration in degrees
                Celsius.

        

#### `def get_self_cal_supported(self)`

get_self_cal_supported

        Returns whether the device supports self–calibration.

        Returns:
            self_cal_supported (bool): Returns whether the device supports self-calibration.

                ****Defined Values****

                +-------+------------------------------------+
                | True  | Self–calibration is supported.     |
                +-------+------------------------------------+
                | False | Self–calibration is not supported. |
                +-------+------------------------------------+

        

#### `def import_attribute_configuration_buffer(self, configuration)`

import_attribute_configuration_buffer

        Imports a property configuration to the session from the specified
        configuration buffer.

        You can export and import session property configurations only between
        devices with identical model numbers, channel counts, and onboard memory
        sizes.

        Note:
        You cannot call this method while the session is in a running state,
        such as while generating a signal.

        Args:
            configuration (bytes): Specifies the byte array buffer that contains the property
                configuration to import.

        

#### `def import_attribute_configuration_file(self, file_path)`

import_attribute_configuration_file

        Imports a property configuration to the session from the specified
        file.

        You can export and import session property configurations only between
        devices with identical model numbers, channel counts, and onboard memory
        sizes.

        Note:
        You cannot call this method while the session is in a running state,
        such as while generating a signal.

        Args:
            file_path (str): Specifies the absolute path to the file containing the property
                configuration to import. If you specify an empty or relative path, this
                method returns an error.
                **Default File Extension:** .nifgenconfig

        

#### `def _initialize_with_channels(self, resource_name, channel_name=None, reset_device=False, option_string='')`

_initialize_with_channels

        Creates and returns a new NI-FGEN session to the specified channel of a
        waveform generator that is used in all subsequent NI-FGEN method
        calls.

        Args:
            resource_name (str): Caution:
                Traditional NI-DAQ and NI-DAQmx device names are not case-sensitive.
                However, all IVI names, such as logical names, are case-sensitive. If
                you use logical names, driver session names, or virtual names in your
                program, you must ensure that the name you use matches the name in the
                IVI Configuration Store file exactly, without any variations in the case
                of the characters.

                | Specifies the resource name of the device to initialize.

                For Traditional NI-DAQ devices, the syntax is DAQ::\ *n*, where *n* is
                the device number assigned by MAX, as shown in Example 1.

                For NI-DAQmx devices, the syntax is just the device name specified in
                MAX, as shown in Example 2. Typical default names for NI-DAQmx devices
                in MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by
                right-clicking on the name in MAX and entering a new name.

                An alternate syntax for NI-DAQmx devices consists of DAQ::\ *NI-DAQmx
                device name*, as shown in Example 3. This naming convention allows for
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

                +-----------+--------------------------------------+------------------------+---------------------------------+
                | Example # | Device Type                          | Syntax                 | Variable                        |
                +===========+======================================+========================+=================================+
                | 1         | Traditional NI-DAQ device            | DAQ::\ *1*             | (*1* = device number)           |
                +-----------+--------------------------------------+------------------------+---------------------------------+
                | 2         | NI-DAQmx device                      | *myDAQmxDevice*        | (*myDAQmxDevice* = device name) |
                +-----------+--------------------------------------+------------------------+---------------------------------+
                | 3         | NI-DAQmx device                      | DAQ::\ *myDAQmxDevice* | (*myDAQmxDevice* = device name) |
                +-----------+--------------------------------------+------------------------+---------------------------------+
                | 4         | NI-DAQmx device                      | DAQ::\ *2*             | (*2* = device name)             |
                +-----------+--------------------------------------+------------------------+---------------------------------+
                | 5         | IVI logical name or IVI virtual name | *myLogicalName*        | (*myLogicalName* = name)        |
                +-----------+--------------------------------------+------------------------+---------------------------------+

            channel_name (str, list, range, tuple): Specifies the channel that this VI uses.

                **Default Value**: "0"

            reset_device (bool): Specifies whether you want to reset the device during the initialization
                procedure. True specifies that the device is reset and performs the
                same method as the Reset method.

                ****Defined Values****

                **Default Value**: False

                +-------+---------------------+
                | True  | Reset device        |
                +-------+---------------------+
                | False | Do not reset device |
                +-------+---------------------+

            option_string (dict): Sets the initial value of certain session properties.

                The syntax for **optionString** is

                <*attributeName*> = <*value*>

                where

                *attributeName* is the name of the property and *value* is the value to
                which the property is set

                To set multiple properties, separate them with a comma.

                If you pass NULL or an empty string for this parameter, the session uses
                the default values for these properties. You can override the default
                values by assigning a value explicitly in a string that you pass for
                this parameter.

                You do not have to specify all of the properties and may leave any of
                them out. However, if you do not specify one of the properties, its
                default value is used.

                If simulation is enabled (Simulate=1), you may specify the device that
                you want to simulate. To specify a device, enter the following syntax in
                **optionString**.

                DriverSetup=Model:<*driver model number*>;Channels:<*channel
                names*>;BoardType:<*module type*>;MemorySize:<*size of onboard memory in
                bytes*>

                **Syntax Examples**

                **Properties and **Defined Values****

                **Default Values**: "Simulate=0,RangeCheck=1,QueryInstrStatus=1,Cache=1"

                +------------------+-------------------------+-------------+
                | Property Name    | Property                | Values      |
                +==================+=========================+=============+
                | RangeCheck       | RANGE_CHECK             | True, False |
                +------------------+-------------------------+-------------+
                | QueryInstrStatus | QUERY_INSTRUMENT_STATUS | True, False |
                +------------------+-------------------------+-------------+
                | Cache            | CACHE                   | True, False |
                +------------------+-------------------------+-------------+
                | Simulate         | simulate                | True, False |
                +------------------+-------------------------+-------------+

                Note:
                One or more of the referenced properties are not in the Python API for this driver.


        Returns:
            vi (int): Returns a session handle that you can use to identify the device in all
                subsequent NI-FGEN method calls.

        

#### `def _initiate_generation(self)`

_initiate_generation

        Initiates signal generation. If you want to abort signal generation,
        call the abort method. After the signal generation
        is aborted, you can call the initiate method to
        cause the signal generator to produce a signal again.
        

#### `def is_done(self)`

is_done

        Determines whether the current generation is complete. This method
        sets the **done** parameter to True if the session is in the Idle or
        Committed states.

        Note:
        NI-FGEN only reports the **done** parameter as True after the
        current generation is complete in Single trigger mode.

        Returns:
            done (bool): Returns information about the completion of waveform generation.

                **Defined Values**

                +-------+-----------------------------+
                | True  | Generation is complete.     |
                +-------+-----------------------------+
                | False | Generation is not complete. |
                +-------+-----------------------------+

        

#### `def query_arb_seq_capabilities(self)`

query_arb_seq_capabilities

        Returns the properties of the signal generator that are related to
        creating arbitrary sequences (the max_num_sequences,
        min_sequence_length,
        max_sequence_length, and max_loop_count
        properties).

        Returns:
            maximum_number_of_sequences (int): Returns the maximum number of arbitrary waveform sequences that the
                signal generator allows. NI-FGEN obtains this value from the
                max_num_sequences property.

            minimum_sequence_length (int): Returns the minimum number of arbitrary waveforms the signal generator
                allows in a sequence. NI-FGEN obtains this value from the
                min_sequence_length property.

            maximum_sequence_length (int): Returns the maximum number of arbitrary waveforms the signal generator
                allows in a sequence. NI-FGEN obtains this value from the
                max_sequence_length property.

            maximum_loop_count (int): Returns the maximum number of times the signal generator can repeat an
                arbitrary waveform in a sequence. NI-FGEN obtains this value from the
                max_loop_count property.

        

#### `def query_arb_wfm_capabilities(self)`

query_arb_wfm_capabilities

        Returns the properties of the signal generator that are related to
        creating arbitrary waveforms. These properties are the maximum number of
        waveforms, waveform quantum, minimum waveform size, and maximum waveform
        size.

        Note:
        If you do not want to obtain the waveform quantum, pass a value of
        VI_NULL for this parameter.

        Returns:
            maximum_number_of_waveforms (int): Returns the maximum number of arbitrary waveforms that the signal
                generator allows. NI-FGEN obtains this value from the
                max_num_waveforms property.

            waveform_quantum (int): The size (number of points) of each waveform must be a multiple of a
                constant quantum value. This parameter obtains the quantum value that
                the signal generator uses. NI-FGEN returns this value from the
                waveform_quantum property.

                For example, when this property returns a value of 8, all waveform
                sizes must be a multiple of 8.

            minimum_waveform_size (int): Returns the minimum number of points that the signal generator allows in
                a waveform. NI-FGEN obtains this value from the
                min_waveform_size property.

            maximum_waveform_size (int): Returns the maximum number of points that the signal generator allows in
                a waveform. NI-FGEN obtains this value from the
                max_waveform_size property.

        

#### `def query_freq_list_capabilities(self)`

query_freq_list_capabilities

        Returns the properties of the signal generator that are related to
        creating frequency lists. These properties are
        max_num_freq_lists,
        min_freq_list_length,
        max_freq_list_length,
        min_freq_list_duration,
        max_freq_list_duration, and
        freq_list_duration_quantum.

        Returns:
            maximum_number_of_freq_lists (int): Returns the maximum number of frequency lists that the signal generator
                allows. NI-FGEN obtains this value from the
                max_num_freq_lists property.

            minimum_frequency_list_length (int): Returns the minimum number of steps that the signal generator allows in
                a frequency list. NI-FGEN obtains this value from the
                min_freq_list_length property.

            maximum_frequency_list_length (int): Returns the maximum number of steps that the signal generator allows in
                a frequency list. NI-FGEN obtains this value from the
                max_freq_list_length property.

            minimum_frequency_list_duration (float): Returns the minimum duration that the signal generator allows in a step
                of a frequency list. NI-FGEN obtains this value from the
                min_freq_list_duration property.

            maximum_frequency_list_duration (float): Returns the maximum duration that the signal generator allows in a step
                of a frequency list. NI-FGEN obtains this value from the
                max_freq_list_duration property.

            frequency_list_duration_quantum (float): Returns the quantum of which all durations must be a multiple in a
                frequency list. NI-FGEN obtains this value from the
                freq_list_duration_quantum property.

        

#### `def read_current_temperature(self)`

read_current_temperature

        Reads the current onboard temperature of the device. The temperature is
        returned in degrees Celsius.

        Returns:
            temperature (float): Returns the current temperature read from onboard temperature sensors,
                in degrees Celsius.

        

#### `def reset_device(self)`

reset_device

        Performs a hard reset on the device. Generation is stopped, all routes
        are released, external bidirectional terminals are tristated, FPGAs are
        reset, hardware is configured to its default state, and all session
        properties are reset to their default states.
        

#### `def reset_with_defaults(self)`

reset_with_defaults

        Resets the instrument and reapplies initial user–specified settings from
        the logical name that was used to initialize the session. If the session
        was created without a logical name, this method is equivalent to the
        reset method.
        

#### `def self_cal(self)`

self_cal

        Performs a full internal self-calibration on the device. If the
        calibration is successful, new calibration data and constants are stored
        in the onboard EEPROM.
        

#### `def wait_until_done(self, max_time=hightime.timedelta(seconds=10.0))`

wait_until_done

        Waits until the device is done generating or until the maximum time has
        expired.

        Args:
            max_time (hightime.timedelta, datetime.timedelta, or int in milliseconds): Specifies the timeout value in milliseconds.

        

#### `def _close(self)`

_close

        Performs the following operations:

        -  Closes the instrument I/O session.
        -  Destroys the NI-FGEN session and all of its properties.
        -  Deallocates any memory resources NI-FGEN uses.

        Not all signal routes established by calling the ExportSignal
        and RouteSignalOut methods are released when the NI-FGEN
        session is closed. The following table shows what happens to a signal
        route on your device when you call the _close method.

        +--------------------+-------------------+------------------+
        | Routes To          | NI 5401/5411/5431 | Other Devices    |
        +====================+===================+==================+
        | Front Panel        | Remain connected  | Remain connected |
        +--------------------+-------------------+------------------+
        | RTSI/PXI Backplane | Remain connected  | Disconnected     |
        +--------------------+-------------------+------------------+

        Note:
        After calling _close, you cannot use NI-FGEN again until you
        call the init or InitWithOptions methods.
        

#### `def self_test(self)`

self_test

        Runs the instrument self-test routine and returns the test result(s).

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

        Note:
        When used on some signal generators, the device is reset after the
        self_test method runs. If you use the self_test
        method, your device may not be in its previously configured state
        after the method runs.
        

#### `def reset(self)`

reset

        Resets the instrument to a known state. This method aborts the
        generation, clears all routes, and resets session properties to the
        default values. This method does not, however, commit the session
        properties or configure the device hardware to its default state.

        Note:
        For the NI 5401/5404/5411/5431, this method exhibits the same
        behavior as the reset_device method.
        

#### `def _self_test(self)`

_self_test

        Runs the instrument self-test routine and returns the test result(s).

        Note:
        When used on some signal generators, the device is reset after the
        self_test method runs. If you use the self_test
        method, your device may not be in its previously configured state
        after the method runs.

        Returns:
            self_test_result (int): Contains the value returned from the instrument self-test. A value of 0
                indicates success.

                +----------------+------------------+
                | Self-Test Code | Description      |
                +================+==================+
                | 0              | Passed self-test |
                +----------------+------------------+
                | 1              | Self-test failed |
                +----------------+------------------+

            self_test_message (str): Returns the self-test response string from the instrument.

                You must pass a ViChar array with at least 256 bytes.

        

<!--NI_PYTHON_API repo=nimi-python path=generated/nifgen/nifgen/unit_tests/_matchers.py -->
## PYTHON MODULE: generated/nifgen/nifgen/unit_tests/_matchers.py

### MODULE DOCSTRING

Matcher classes used by unit tests in order to set mock expectations.
These work well with our visatype definitions.


### `class _ScalarMatcher(object)`

#### `def __init__(self, expected_type, expected_value)`

#### `def __eq__(self, other)`

#### `def __repr__(self)`

### `class _PointerMatcher(object)`

#### `def __init__(self, expected_type)`

#### `def __eq__(self, other)`

#### `def __repr__(self)`

### `class _BufferMatcher(object)`

#### `def __init__(self, expected_element_type, expected_size_or_value)`

#### `def __eq__(self, other)`

#### `def __repr__(self)`

#### `def __str__(self)`

### `class ViStringMatcher(object)`

#### `def __init__(self, expected_string_value)`

#### `def __eq__(self, other)`

#### `def __repr__(self)`

### `def _compare_ctype_structs(expected, actual)`

### `class CustomTypeMatcher(object)`

#### `def __init__(self, expected_type, expected_value)`

#### `def __eq__(self, actual)`

#### `def __repr__(self)`

### `class CustomTypeBufferMatcher(object)`

#### `def __init__(self, expected_element_type, expected_value)`

#### `def __eq__(self, actual)`

#### `def __repr__(self)`

#### `def __str__(self)`

### `class ViBooleanMatcher(_ScalarMatcher)`

#### `def __init__(self, expected_value)`

### `class ViSessionMatcher(_ScalarMatcher)`

#### `def __init__(self, expected_value)`

### `class ViInt16Matcher(_ScalarMatcher)`

#### `def __init__(self, expected_value)`

### `class ViInt32Matcher(_ScalarMatcher)`

#### `def __init__(self, expected_value)`

### `class ViUInt32Matcher(_ScalarMatcher)`

#### `def __init__(self, expected_value)`

### `class ViAttrMatcher(_ScalarMatcher)`

#### `def __init__(self, expected_value)`

### `class ViInt64Matcher(_ScalarMatcher)`

#### `def __init__(self, expected_value)`

### `class ViReal64Matcher(_ScalarMatcher)`

#### `def __init__(self, expected_value)`

### `class ViBooleanPointerMatcher(_PointerMatcher)`

#### `def __init__(self)`

### `class ViSessionPointerMatcher(_PointerMatcher)`

#### `def __init__(self)`

### `class ViInt16PointerMatcher(_PointerMatcher)`

#### `def __init__(self)`

### `class ViInt32PointerMatcher(_PointerMatcher)`

#### `def __init__(self)`

### `class ViInt64PointerMatcher(_PointerMatcher)`

#### `def __init__(self)`

### `class ViReal64PointerMatcher(_PointerMatcher)`

#### `def __init__(self)`

### `class ViBooleanBufferMatcher(_BufferMatcher)`

#### `def __init__(self, expected_size_or_value)`

### `class ViCharBufferMatcher(_BufferMatcher)`

#### `def __init__(self, expected_size_or_value)`

### `class ViInt8BufferMatcher(_BufferMatcher)`

#### `def __init__(self, expected_size_or_value)`

### `class ViInt16BufferMatcher(_BufferMatcher)`

#### `def __init__(self, expected_size_or_value)`

### `class ViInt32BufferMatcher(_BufferMatcher)`

#### `def __init__(self, expected_size_or_value)`

### `class ViInt64BufferMatcher(_BufferMatcher)`

#### `def __init__(self, expected_size_or_value)`

### `class ViReal64BufferMatcher(_BufferMatcher)`

#### `def __init__(self, expected_size_or_value)`

### `class ViSessionBufferMatcher(_BufferMatcher)`

#### `def __init__(self, expected_size_or_value)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nifgen/nifgen/unit_tests/_mock_helper.py -->
## PYTHON MODULE: generated/nifgen/nifgen/unit_tests/_mock_helper.py

### `class MockFunctionCallError(Exception)`

#### `def __init__(self, function, param=None)`

### `class SideEffectsHelper(object)`

#### `def __init__(self)`

#### `def __getitem__(self, func)`

#### `def __setitem__(self, func, val)`

#### `def niFgen_AbortGeneration(self, vi)`

#### `def niFgen_AllocateNamedWaveform(self, vi, channel_name, waveform_name, waveform_size)`

#### `def niFgen_AllocateWaveform(self, vi, channel_name, waveform_size, waveform_handle)`

#### `def niFgen_ClearArbMemory(self, vi)`

#### `def niFgen_ClearArbSequence(self, vi, sequence_handle)`

#### `def niFgen_ClearArbWaveform(self, vi, waveform_handle)`

#### `def niFgen_ClearFreqList(self, vi, frequency_list_handle)`

#### `def niFgen_ClearUserStandardWaveform(self, vi, channel_name)`

#### `def niFgen_Commit(self, vi)`

#### `def niFgen_ConfigureArbSequence(self, vi, channel_name, sequence_handle, gain, offset)`

#### `def niFgen_ConfigureArbWaveform(self, vi, channel_name, waveform_handle, gain, offset)`

#### `def niFgen_ConfigureFreqList(self, vi, channel_name, frequency_list_handle, amplitude, dc_offset, start_phase)`

#### `def niFgen_ConfigureStandardWaveform(self, vi, channel_name, waveform, amplitude, dc_offset, frequency, start_phase)`

#### `def niFgen_CreateAdvancedArbSequence(self, vi, sequence_length, waveform_handles_array, loop_counts_array, sample_counts_array, marker_location_array, coerced_markers_array, sequence_handle)`

#### `def niFgen_CreateArbSequence(self, vi, sequence_length, waveform_handles_array, loop_counts_array, sequence_handle)`

#### `def niFgen_CreateFreqList(self, vi, waveform, frequency_list_length, frequency_array, duration_array, frequency_list_handle)`

#### `def niFgen_CreateWaveformF64(self, vi, channel_name, waveform_size, waveform_data_array, waveform_handle)`

#### `def niFgen_CreateWaveformFromFileF64(self, vi, channel_name, file_name, byte_order, waveform_handle)`

#### `def niFgen_CreateWaveformFromFileI16(self, vi, channel_name, file_name, byte_order, waveform_handle)`

#### `def niFgen_CreateWaveformI16(self, vi, channel_name, waveform_size, waveform_data_array, waveform_handle)`

#### `def niFgen_DefineUserStandardWaveform(self, vi, channel_name, waveform_size, waveform_data_array)`

#### `def niFgen_DeleteNamedWaveform(self, vi, channel_name, waveform_name)`

#### `def niFgen_DeleteScript(self, vi, channel_name, script_name)`

#### `def niFgen_Disable(self, vi)`

#### `def niFgen_ExportAttributeConfigurationBuffer(self, vi, size_in_bytes, configuration)`

#### `def niFgen_ExportAttributeConfigurationFile(self, vi, file_path)`

#### `def niFgen_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niFgen_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niFgen_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niFgen_GetAttributeViString(self, vi, channel_name, attribute_id, array_size, attribute_value)`

#### `def niFgen_GetChannelName(self, vi, index, buffer_size, channel_string)`

#### `def niFgen_GetError(self, vi, error_code, error_description_buffer_size, error_description)`

#### `def niFgen_GetExtCalLastDateAndTime(self, vi, year, month, day, hour, minute)`

#### `def niFgen_GetExtCalLastTemp(self, vi, temperature)`

#### `def niFgen_GetExtCalRecommendedInterval(self, vi, months)`

#### `def niFgen_GetHardwareState(self, vi, state)`

#### `def niFgen_GetSelfCalLastDateAndTime(self, vi, year, month, day, hour, minute)`

#### `def niFgen_GetSelfCalLastTemp(self, vi, temperature)`

#### `def niFgen_GetSelfCalSupported(self, vi, self_cal_supported)`

#### `def niFgen_ImportAttributeConfigurationBuffer(self, vi, size_in_bytes, configuration)`

#### `def niFgen_ImportAttributeConfigurationFile(self, vi, file_path)`

#### `def niFgen_InitializeWithChannels(self, resource_name, channel_name, reset_device, option_string, vi)`

#### `def niFgen_InitiateGeneration(self, vi)`

#### `def niFgen_IsDone(self, vi, done)`

#### `def niFgen_LockSession(self, vi, caller_has_lock)`

#### `def niFgen_QueryArbSeqCapabilities(self, vi, maximum_number_of_sequences, minimum_sequence_length, maximum_sequence_length, maximum_loop_count)`

#### `def niFgen_QueryArbWfmCapabilities(self, vi, maximum_number_of_waveforms, waveform_quantum, minimum_waveform_size, maximum_waveform_size)`

#### `def niFgen_QueryFreqListCapabilities(self, vi, maximum_number_of_freq_lists, minimum_frequency_list_length, maximum_frequency_list_length, minimum_frequency_list_duration, maximum_frequency_list_duration, frequency_list_duration_quantum)`

#### `def niFgen_ReadCurrentTemperature(self, vi, temperature)`

#### `def niFgen_ResetDevice(self, vi)`

#### `def niFgen_ResetWithDefaults(self, vi)`

#### `def niFgen_SelfCal(self, vi)`

#### `def niFgen_SendSoftwareEdgeTrigger(self, vi, trigger, trigger_id)`

#### `def niFgen_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niFgen_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niFgen_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niFgen_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niFgen_SetNamedWaveformNextWritePosition(self, vi, channel_name, waveform_name, relative_to, offset)`

#### `def niFgen_SetRuntimeEnvironment(self, environment, environment_version, reserved1, reserved2)`

#### `def niFgen_SetWaveformNextWritePosition(self, vi, channel_name, waveform_handle, relative_to, offset)`

#### `def niFgen_UnlockSession(self, vi, caller_has_lock)`

#### `def niFgen_WaitUntilDone(self, vi, max_time)`

#### `def niFgen_WriteBinary16Waveform(self, vi, channel_name, waveform_handle, size, data)`

#### `def niFgen_WriteNamedWaveformF64(self, vi, channel_name, waveform_name, size, data)`

#### `def niFgen_WriteNamedWaveformI16(self, vi, channel_name, waveform_name, size, data)`

#### `def niFgen_WriteScript(self, vi, channel_name, script)`

#### `def niFgen_WriteWaveform(self, vi, channel_name, waveform_handle, size, data)`

#### `def niFgen_close(self, vi)`

#### `def niFgen_error_message(self, vi, error_code, error_message)`

#### `def niFgen_reset(self, vi)`

#### `def niFgen_self_test(self, vi, self_test_result, self_test_message)`

#### `def set_side_effects_and_return_values(self, mock_library)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nifgen/setup.py -->
## PYTHON MODULE: generated/nifgen/setup.py

### `def read_contents(file_to_read)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nimodinst/nimodinst/__init__.py -->
## PYTHON MODULE: generated/nimodinst/nimodinst/__init__.py

### `def get_diagnostic_information()`

Get diagnostic information about the system state that is suitable for printing or logging

    returns: dict

    note: Python bitness may be incorrect when running in a virtual environment
    

### `def print_diagnostic_information()`

Print diagnostic information in a format suitable for issue report

    note: Python bitness may be incorrect when running in a virtual environment
    

<!--NI_PYTHON_API repo=nimi-python path=generated/nimodinst/nimodinst/_converters.py -->
## PYTHON MODULE: generated/nimodinst/nimodinst/_converters.py

### `def _convert_repeated_capabilities(arg, prefix)`

Base version that should not be called

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
    

### `def _(repeated_capability, prefix)`

Integer version

### `def _(repeated_capability, prefix)`

String version (this is the most complex)

    We need to deal with a range ('0-3' or '0:3'), a list ('0,1,2,3') and a single item
    

### `def _(repeated_capability, prefix)`

Iterable version - can handle lists, ranges, and tuples

### `def _(repeated_capability, prefix)`

slice version

### `def convert_repeated_capabilities(repeated_capability, prefix='')`

Convert a repeated capabilities object to a comma delimited list

    Args:
        repeated_capability (str, list, tuple, slice, None) -
        prefix (str) - common prefix for all strings

    Returns:
        rep_cap_list (list of str) - list of each repeated capability item with ranges expanded and prefix added
    

### `def convert_repeated_capabilities_without_prefix(repeated_capability)`

Convert a repeated capabilities object, without any prefix, to a comma delimited list

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
    

### `def expand_channel_string(channel_string, all_channels_in_session)`

Expands a channel_string to a list of individual channel names.

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
    

### `def _convert_timedelta(value, library_type, scaling)`

### `def convert_timedelta_to_seconds_real64(value)`

### `def convert_timedelta_to_milliseconds_int32(value)`

### `def convert_timedeltas_to_seconds_real64(values)`

### `def convert_seconds_real64_to_timedelta(value)`

### `def convert_seconds_real64_to_timedeltas(values)`

### `def convert_month_to_timedelta(months)`

### `def convert_timedelta_to_months_int32(value)`

### `def convert_init_with_options_dictionary(values)`

### `def _convert_to_bytes(value)`

### `def _(value)`

### `def _(value)`

### `def convert_to_bytes(value)`

### `def convert_comma_separated_string_to_list(comma_separated_string)`

### `def convert_list_to_comma_separated_string(list_of_strings)`

Convert a list or tuple of strings into a comma-separated string.

    Args:
        list_of_strings (list or tuple of str): List or tuple of strings.

    Returns:
        str: Comma-separated string.
    

### `def convert_chained_repeated_capability_to_parts(chained_repeated_capability)`

Convert a chained repeated capabilities string to a list of comma-delimited repeated capabilities string.

    Converter assumes that the input contains the full cartesian product of its parts.
    e.g. If chained_repeated_capability is 'site0/PinA,site0/PinB,site1/PinA,site1/PinB',
    ['site0,site1', 'PinA,PinB'] is returned.

    Args:
        chained_repeated_capability (str) - comma-delimited repeated capabilities string where each
        item is a chain of slash-delimited repeated capabilities

    Returns:
        rep_cap_list (list of str) - list of comma-delimited repeated capabilities string
    

<!--NI_PYTHON_API repo=nimi-python path=generated/nimodinst/nimodinst/_library.py -->
## PYTHON MODULE: generated/nimodinst/nimodinst/_library.py

### `class Library(object)`

Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    

#### `def __init__(self, ctypes_library)`

#### `def _get_library_function(self, name)`

#### `def niModInst_CloseInstalledDevicesSession(self, handle)`

#### `def niModInst_GetExtendedErrorInfo(self, error_info_buffer_size, error_info)`

#### `def niModInst_GetInstalledDeviceAttributeViInt32(self, handle, index, attribute_id, attribute_value)`

#### `def niModInst_GetInstalledDeviceAttributeViString(self, handle, index, attribute_id, attribute_value_buffer_size, attribute_value)`

#### `def niModInst_OpenInstalledDevicesSession(self, driver, handle, device_count)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nimodinst/nimodinst/_library_interpreter.py -->
## PYTHON MODULE: generated/nimodinst/nimodinst/_library_interpreter.py

### `def _get_ctypes_pointer_for_buffer(value=None, library_type=None, size=None)`

### `def _convert_to_array(value, array_type)`

### `class LibraryInterpreter(object)`

Library C<->Python interpreter.

    This class is responsible for interpreting the Library's C API. It is responsible for:
    * Converting ctypes to native Python types.
    * Dealing with string encoding.
    * Allocating memory.
    * Converting errors returned by Library into Python exceptions.
    

#### `def __init__(self, encoding)`

#### `def set_session_handle(self, value=0)`

#### `def get_session_handle(self)`

#### `def get_error_description(self, error_code)`

get_error_description

        Returns the error description.
        

#### `def close_installed_devices_session(self)`

#### `def get_extended_error_info(self)`

#### `def get_installed_device_attribute_vi_int32(self, index, attribute_id)`

#### `def get_installed_device_attribute_vi_string(self, index, attribute_id)`

#### `def open_installed_devices_session(self, driver)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nimodinst/nimodinst/_library_singleton.py -->
## PYTHON MODULE: generated/nimodinst/nimodinst/_library_singleton.py

### `def _get_library_name()`

### `def _get_library_type()`

### `def get()`

get

    Returns the library.Library singleton for nimodinst.
    

<!--NI_PYTHON_API repo=nimi-python path=generated/nimodinst/nimodinst/errors.py -->
## PYTHON MODULE: generated/nimodinst/nimodinst/errors.py

### `def _is_success(code)`

### `def _is_error(code)`

### `def _is_warning(code)`

### `class Error(Exception)`

Base error class for NI-ModInst

#### `def __init__(self, message)`

### `class DriverError(Error)`

An error originating from the NI-ModInst driver

#### `def __init__(self, code, description)`

### `class DriverWarning(Warning)`

A warning originating from the NI-ModInst driver

#### `def __init__(self, code, description)`

### `class UnsupportedConfigurationError(Error)`

An error due to using this module in an usupported platform.

#### `def __init__(self)`

### `class DriverNotInstalledError(Error)`

An error due to using this module without the driver runtime installed.

#### `def __init__(self)`

### `class DriverTooOldError(Error)`

An error due to using this module with an older version of the NI-ModInst driver runtime.

#### `def __init__(self)`

### `class DriverTooNewError(Error)`

An error due to the NI-ModInst driver runtime being too new for this module.

#### `def __init__(self)`

### `def handle_error(library_interpreter, code, ignore_warnings, is_error_handling)`

handle_error

    Helper function for handling errors returned by nimodinst.Library.
    It calls back into the LibraryInterpreter to get the corresponding error
    description and raises if necessary.
    

<!--NI_PYTHON_API repo=nimi-python path=generated/nimodinst/nimodinst/session.py -->
## PYTHON MODULE: generated/nimodinst/nimodinst/session.py

### `class AttributeViInt32(object)`

#### `def __init__(self, owner, attribute_id, index)`

#### `def __getitem__(self, index)`

### `class AttributeViString(object)`

#### `def __init__(self, owner, attribute_id, index)`

#### `def __getitem__(self, index)`

### `class _Device(object)`

#### `def __init__(self, owner, index)`

#### `def __repr__(self)`

#### `def __str__(self)`

#### `def __getattribute__(self, name)`

#### `def __setattr__(self, name, value)`

### `class _DeviceIterable(object)`

#### `def __init__(self, owner, count)`

#### `def _get_next(self)`

#### `def next(self)`

#### `def __next__(self)`

#### `def __repr__(self)`

#### `def __str__(self)`

### `class Session(object)`

A NI-ModInst session to get device information

#### `def __init__(self, driver)`

#### `def __repr__(self)`

#### `def __str__(self)`

#### `def __setattr__(self, key, value)`

#### `def __enter__(self)`

#### `def __exit__(self, exc_type, exc_value, traceback)`

#### `def __len__(self)`

#### `def __iter__(self)`

#### `def close(self)`

#### `def _close_installed_devices_session(self)`

_close_installed_devices_session

        Cleans up the NI-ModInst session created by a call to
        _open_installed_devices_session. Call this method when you are
        finished using the session handle and do not use this handle again.
        

#### `def _get_installed_device_attribute_vi_int32(self, index, attribute_id)`

_get_installed_device_attribute_vi_int32

        Returns an integer property specified by the attributeID parameter for
        a device specified by the handle and index parameters. The handle
        parameter is expected to be a valid handle returned by
        _open_installed_devices_session. It therefore acts as a handle to
        a list of installed devices. The index parameter specifies the device in
        the list for which you want the property.

        Args:
            index (int): A zero-based index that specifies the device for which you want the
                property. This index parameter should be between 0 and (deviceCount -
                1), inclusive, where deviceCount is the number of installed devices
                returned by _open_installed_devices_session.

            attribute_id (int): The ID of the integer property you want to query. Valid Values Slot
                Number--the slot (for example, in a PXI chassis) in which the device is
                installed. This property can only be queried for PXI devices installed
                in a chassis that has been properly identified in MAX. Chassis
                Number--the number of the chassis in which the device is installed. This
                property can only be queried for PXI devices installed in a chassis
                that has been properly identified in MAX. Bus Number--the bus on which
                the device has been enumerated. Socket Number--the socket number on
                which the device has been enumerated. Notes The bus number and socket
                number can be used to form a VISA resource string for this device, of
                the form "PXI::::INSTR". Traditional NI-DAQ devices do not support the
                chassis number, bus number, and socket number properties.


        Returns:
            attribute_value (int): A pointer to a signed 32-bit integer variable that receives the value of
                the requested property.

        

#### `def _get_installed_device_attribute_vi_string(self, index, attribute_id)`

_get_installed_device_attribute_vi_string

        Returns a string property specified by the attributeID parameter for a
        device specified by the handle and index parameters. The handle
        parameter is expected to be a valid handle returned by
        _open_installed_devices_session. Therefore, it acts as a handle
        to a list of installed devices. The index parameter specifies for which
        device in the list you want the property. To find out the length of the
        device name string before you allocate a buffer for it, simply call this
        method and pass 0 as the attributeValueBufferSize parameter or NULL as
        the attributeValue parameter. When you do this, the method returns the
        size of the buffer required to hold the property value string as its
        return value. You can then allocate an appropriately sized character
        buffer and call this method again.

        Args:
            index (int): A zero-based index that specifies the device for which you want the
                property. This index parameter should be between 0 and (deviceCount -
                1), inclusive, where deviceCount is the number of installed devices
                returned by _open_installed_devices_session.

            attribute_id (int): The ID of the string property you want to query. Valid Values
                device_name--the name of the device, which can be used
                to open an instrument driver session for that device
                device_model--the model of the device (for example, NI
                PXI-5122) serial_number--the serial number of the
                device


        Returns:
            attribute_value (str): The character buffer into which the property value string is copied.

        

#### `def _open_installed_devices_session(self, driver)`

_open_installed_devices_session

        Creates a handle to a list of installed devices supported by the
        specified driver. Call this method and pass in the name of an NI
        instrument driver, such as "NI-SCOPE". This method
        searches the system and constructs a list of all the installed devices
        that are supported by that driver, and then returns both a handle to
        this list and the number of devices found. The handle is used with other
        methods to query for properties such as device name and model, and to
        safely discard the list when finished. Note This handle reflects the
        system state when the handle is created (that is, when you call this
        method. If you remove devices from the system or rename them in
        Measurement & Automation Explorer (MAX), this handle may not refer to an
        accurate list of devices. You should destroy the handle using
        _close_installed_devices_session and create a new handle using
        this method.

        Args:
            driver (str): A string specifying the driver whose supported devices you want to find.
                This string is not case-sensitive. Some examples are: NI-SCOPE niScope
                NI-FGEN niFgen NI-HSDIO niHSDIO NI-DMM niDMM NI-SWITCH niSwitch Note If
                you use the empty string for this parameter, NI-ModInst creates a list
                of all Modular Instruments devices installed in the system.


        Returns:
            handle (int): A pointer to a ViSession variable that receives the value of the
                NI-ModInst session handle. This value acts as a handle to the list of
                installed devices and is used in other NI-ModInst methods.

            device_count (int): A pointer to an integer variable that receives the number of devices
                found in the system that are supported by the driver specified in the
                driver parameter.

        

<!--NI_PYTHON_API repo=nimi-python path=generated/nimodinst/nimodinst/unit_tests/_matchers.py -->
## PYTHON MODULE: generated/nimodinst/nimodinst/unit_tests/_matchers.py

### MODULE DOCSTRING

Matcher classes used by unit tests in order to set mock expectations.
These work well with our visatype definitions.


### `class _ScalarMatcher(object)`

#### `def __init__(self, expected_type, expected_value)`

#### `def __eq__(self, other)`

#### `def __repr__(self)`

### `class _PointerMatcher(object)`

#### `def __init__(self, expected_type)`

#### `def __eq__(self, other)`

#### `def __repr__(self)`

### `class _BufferMatcher(object)`

#### `def __init__(self, expected_element_type, expected_size_or_value)`

#### `def __eq__(self, other)`

#### `def __repr__(self)`

#### `def __str__(self)`

### `class ViStringMatcher(object)`

#### `def __init__(self, expected_string_value)`

#### `def __eq__(self, other)`

#### `def __repr__(self)`

### `def _compare_ctype_structs(expected, actual)`

### `class CustomTypeMatcher(object)`

#### `def __init__(self, expected_type, expected_value)`

#### `def __eq__(self, actual)`

#### `def __repr__(self)`

### `class CustomTypeBufferMatcher(object)`

#### `def __init__(self, expected_element_type, expected_value)`

#### `def __eq__(self, actual)`

#### `def __repr__(self)`

#### `def __str__(self)`

### `class ViBooleanMatcher(_ScalarMatcher)`

#### `def __init__(self, expected_value)`

### `class ViSessionMatcher(_ScalarMatcher)`

#### `def __init__(self, expected_value)`

### `class ViInt16Matcher(_ScalarMatcher)`

#### `def __init__(self, expected_value)`

### `class ViInt32Matcher(_ScalarMatcher)`

#### `def __init__(self, expected_value)`

### `class ViUInt32Matcher(_ScalarMatcher)`

#### `def __init__(self, expected_value)`

### `class ViAttrMatcher(_ScalarMatcher)`

#### `def __init__(self, expected_value)`

### `class ViInt64Matcher(_ScalarMatcher)`

#### `def __init__(self, expected_value)`

### `class ViReal64Matcher(_ScalarMatcher)`

#### `def __init__(self, expected_value)`

### `class ViBooleanPointerMatcher(_PointerMatcher)`

#### `def __init__(self)`

### `class ViSessionPointerMatcher(_PointerMatcher)`

#### `def __init__(self)`

### `class ViInt16PointerMatcher(_PointerMatcher)`

#### `def __init__(self)`

### `class ViInt32PointerMatcher(_PointerMatcher)`

#### `def __init__(self)`

### `class ViInt64PointerMatcher(_PointerMatcher)`

#### `def __init__(self)`

### `class ViReal64PointerMatcher(_PointerMatcher)`

#### `def __init__(self)`

### `class ViBooleanBufferMatcher(_BufferMatcher)`

#### `def __init__(self, expected_size_or_value)`

### `class ViCharBufferMatcher(_BufferMatcher)`

#### `def __init__(self, expected_size_or_value)`

### `class ViInt8BufferMatcher(_BufferMatcher)`

#### `def __init__(self, expected_size_or_value)`

### `class ViInt16BufferMatcher(_BufferMatcher)`

#### `def __init__(self, expected_size_or_value)`

### `class ViInt32BufferMatcher(_BufferMatcher)`

#### `def __init__(self, expected_size_or_value)`

### `class ViInt64BufferMatcher(_BufferMatcher)`

#### `def __init__(self, expected_size_or_value)`

### `class ViReal64BufferMatcher(_BufferMatcher)`

#### `def __init__(self, expected_size_or_value)`

### `class ViSessionBufferMatcher(_BufferMatcher)`

#### `def __init__(self, expected_size_or_value)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nimodinst/nimodinst/unit_tests/_mock_helper.py -->
## PYTHON MODULE: generated/nimodinst/nimodinst/unit_tests/_mock_helper.py

### `class MockFunctionCallError(Exception)`

#### `def __init__(self, function, param=None)`

### `class SideEffectsHelper(object)`

#### `def __init__(self)`

#### `def __getitem__(self, func)`

#### `def __setitem__(self, func, val)`

#### `def niModInst_CloseInstalledDevicesSession(self, handle)`

#### `def niModInst_GetExtendedErrorInfo(self, error_info_buffer_size, error_info)`

#### `def niModInst_GetInstalledDeviceAttributeViInt32(self, handle, index, attribute_id, attribute_value)`

#### `def niModInst_GetInstalledDeviceAttributeViString(self, handle, index, attribute_id, attribute_value_buffer_size, attribute_value)`

#### `def niModInst_OpenInstalledDevicesSession(self, driver, handle, device_count)`

#### `def set_side_effects_and_return_values(self, mock_library)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nimodinst/nimodinst/unit_tests/test_modinst.py -->
## PYTHON MODULE: generated/nimodinst/nimodinst/unit_tests/test_modinst.py

- `SESSION_NUM_FOR_TEST = 42`

### `class TestSession()`

#### `def setup_method(self, method)`

#### `def teardown_method(self, method)`

#### `def niModInst_GetInstalledDeviceAttributeViString_looping(self, handle, index, attribute_id, attribute_value_buffer_size, attribute_value)`

#### `def niModInst_GetInstalledDeviceAttributeViInt32_looping(self, handle, index, attribute_id, attribute_value)`

#### `def test_open_and_close(self)`

#### `def test_close(self)`

#### `def test_context_manager(self)`

#### `def test_iterating_for(self)`

#### `def test_iterating_for_empty(self)`

#### `def test_get_extended_error_info(self)`

#### `def test_get_error_description_fails(self)`

#### `def test_get_attribute_session(self)`

#### `def test_get_attribute_vi_int32_for_loop_index(self)`

#### `def test_get_attribute_vi_string_for_loop_index(self)`

#### `def test_get_attribute_session_no_index(self)`

#### `def test_get_attribute_vi_int32_for_loop_multiple_devices(self)`

#### `def test_get_attribute_vi_string_for_loop_multiple_devices(self)`

#### `def test_cannot_add_properties_to_session_set(self)`

#### `def test_cannot_add_properties_to_session_get(self)`

#### `def test_cannot_add_properties_to_device_set(self)`

#### `def test_cannot_add_properties_to_device_get(self)`

#### `def test_vi_int32_attribute_read_only(self)`

#### `def test_vi_string_attribute_read_only(self)`

#### `def test_int_attribute_error(self)`

#### `def test_int_attribute_warning(self)`

#### `def test_repr_and_str(self)`

### `def test_diagnostic_information()`

<!--NI_PYTHON_API repo=nimi-python path=generated/nimodinst/setup.py -->
## PYTHON MODULE: generated/nimodinst/setup.py

### `def read_contents(file_to_read)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nirfsg/nirfsg/__init__.py -->
## PYTHON MODULE: generated/nirfsg/nirfsg/__init__.py

### `def get_diagnostic_information()`

Get diagnostic information about the system state that is suitable for printing or logging

    returns: dict

    note: Python bitness may be incorrect when running in a virtual environment
    

### `def print_diagnostic_information()`

Print diagnostic information in a format suitable for issue report

    note: Python bitness may be incorrect when running in a virtual environment
    

<!--NI_PYTHON_API repo=nimi-python path=generated/nirfsg/nirfsg/_attributes.py -->
## PYTHON MODULE: generated/nirfsg/nirfsg/_attributes.py

### `class Attribute(object)`

Base class for all typed attributes.

#### `def __init__(self, attribute_id)`

### `class AttributeViInt32(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeViInt32TimeDeltaMilliseconds(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeViInt32TimeDeltaMonths(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeViInt64(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeViReal64(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeViReal64TimeDeltaSeconds(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeViString(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeViStringRepeatedCapability(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeViStringCommaSeparated(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeViBoolean(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeEnum(Attribute)`

#### `def __init__(self, underlying_attribute_meta_class, enum_meta_class, attribute_id)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeEnumWithConverter(Attribute)`

Class for attributes that use enums internally but are exposed in the nirfsg Python module as something else, thus need conversion.

#### `def __init__(self, underlying_attribute_enum, getter_converter, setter_converter)`

Creates and returns an instance of AttributeEnumWithConverter attribute meta class.

        Args:
            underlying_attribute_enum (AttributeEnum): The AttributeEnum instance for the underlying
                enum

            getter_converter (function): The function that converts the enum value to its converted
                value

            setter_converter (function): The function that converts the converted value back to the
                enum value
        

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

### `class AttributeSessionReference(Attribute)`

#### `def __get__(self, session, session_type)`

#### `def __set__(self, session, value)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nirfsg/nirfsg/_complextype.py -->
## PYTHON MODULE: generated/nirfsg/nirfsg/_complextype.py

### `class NIComplexNumber(ctypes.Structure)`

### `class NIComplexNumberF32(ctypes.Structure)`

### `class NIComplexI16(ctypes.Structure)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nirfsg/nirfsg/_converters.py -->
## PYTHON MODULE: generated/nirfsg/nirfsg/_converters.py

### `def _convert_repeated_capabilities(arg, prefix)`

Base version that should not be called

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
    

### `def _(repeated_capability, prefix)`

Integer version

### `def _(repeated_capability, prefix)`

String version (this is the most complex)

    We need to deal with a range ('0-3' or '0:3'), a list ('0,1,2,3') and a single item
    

### `def _(repeated_capability, prefix)`

Iterable version - can handle lists, ranges, and tuples

### `def _(repeated_capability, prefix)`

slice version

### `def convert_repeated_capabilities(repeated_capability, prefix='')`

Convert a repeated capabilities object to a comma delimited list

    Args:
        repeated_capability (str, list, tuple, slice, None) -
        prefix (str) - common prefix for all strings

    Returns:
        rep_cap_list (list of str) - list of each repeated capability item with ranges expanded and prefix added
    

### `def convert_repeated_capabilities_without_prefix(repeated_capability)`

Convert a repeated capabilities object, without any prefix, to a comma delimited list

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
    

### `def expand_channel_string(channel_string, all_channels_in_session)`

Expands a channel_string to a list of individual channel names.

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
    

### `def _convert_timedelta(value, library_type, scaling)`

### `def convert_timedelta_to_seconds_real64(value)`

### `def convert_timedelta_to_milliseconds_int32(value)`

### `def convert_timedeltas_to_seconds_real64(values)`

### `def convert_seconds_real64_to_timedelta(value)`

### `def convert_seconds_real64_to_timedeltas(values)`

### `def convert_month_to_timedelta(months)`

### `def convert_timedelta_to_months_int32(value)`

### `def convert_init_with_options_dictionary(values)`

### `def _convert_to_bytes(value)`

### `def _(value)`

### `def _(value)`

### `def convert_to_bytes(value)`

### `def convert_comma_separated_string_to_list(comma_separated_string)`

### `def convert_list_to_comma_separated_string(list_of_strings)`

Convert a list or tuple of strings into a comma-separated string.

    Args:
        list_of_strings (list or tuple of str): List or tuple of strings.

    Returns:
        str: Comma-separated string.
    

### `def convert_chained_repeated_capability_to_parts(chained_repeated_capability)`

Convert a chained repeated capabilities string to a list of comma-delimited repeated capabilities string.

    Converter assumes that the input contains the full cartesian product of its parts.
    e.g. If chained_repeated_capability is 'site0/PinA,site0/PinB,site1/PinA,site1/PinB',
    ['site0,site1', 'PinA,PinB'] is returned.

    Args:
        chained_repeated_capability (str) - comma-delimited repeated capabilities string where each
        item is a chain of slash-delimited repeated capabilities

    Returns:
        rep_cap_list (list of str) - list of comma-delimited repeated capabilities string
    

<!--NI_PYTHON_API repo=nimi-python path=generated/nirfsg/nirfsg/_grpc_stub_interpreter.py -->
## PYTHON MODULE: generated/nirfsg/nirfsg/_grpc_stub_interpreter.py

### `class GrpcStubInterpreter(object)`

Interpreter for interacting with a gRPC Stub class

#### `def __init__(self, grpc_options)`

#### `def set_session_handle(self, value=session_grpc_types.Session())`

#### `def get_session_handle(self)`

#### `def _invoke(self, func, request, metadata=None)`

#### `def abort(self)`

#### `def allocate_arb_waveform(self, waveform_name, size_in_samples)`

#### `def change_external_calibration_password(self, old_password, new_password)`

#### `def check_generation_status(self)`

#### `def check_if_script_exists(self, script_name)`

#### `def check_if_waveform_exists(self, waveform_name)`

#### `def clear_all_arb_waveforms(self)`

#### `def clear_arb_waveform(self, waveform_name)`

#### `def clear_self_calibrate_range(self)`

#### `def commit(self)`

#### `def configure_deembedding_table_interpolation_linear(self, port, table_name, format)`

#### `def configure_deembedding_table_interpolation_nearest(self, port, table_name)`

#### `def configure_deembedding_table_interpolation_spline(self, port, table_name)`

#### `def configure_digital_edge_script_trigger(self, trigger_id, source, edge)`

#### `def configure_digital_edge_start_trigger(self, source, edge)`

#### `def configure_digital_level_script_trigger(self, trigger_id, source, level)`

#### `def configure_rf(self, frequency, power_level)`

#### `def configure_ref_clock(self, ref_clock_source, ref_clock_rate)`

#### `def configure_software_script_trigger(self, trigger_id)`

#### `def configure_software_start_trigger(self)`

#### `def create_deembedding_sparameter_table_array(self, port, table_name, frequencies, sparameter_table, number_of_ports, sparameter_orientation)`

#### `def create_deembedding_sparameter_table_s2p_file(self, port, table_name, s2p_file_path, sparameter_orientation)`

#### `def delete_all_deembedding_tables(self)`

#### `def delete_deembedding_table(self, port, table_name)`

#### `def delete_script(self, script_name)`

#### `def disable_script_trigger(self, trigger_id)`

#### `def disable_start_trigger(self)`

#### `def error_message(self, error_code)`

#### `def get_all_named_waveform_names(self)`

#### `def get_all_script_names(self)`

#### `def get_attribute_vi_boolean(self, channel_name, attribute)`

#### `def get_attribute_vi_int32(self, channel_name, attribute)`

#### `def get_attribute_vi_int64(self, channel_name, attribute)`

#### `def get_attribute_vi_real64(self, channel_name, attribute)`

#### `def get_attribute_vi_session(self, channel_name, attribute)`

#### `def get_attribute_vi_string(self, channel_name, attribute)`

#### `def get_deembedding_sparameters(self)`

#### `def get_deembedding_table_number_of_ports(self)`

#### `def get_error(self)`

#### `def get_external_calibration_last_date_and_time(self)`

#### `def get_max_settable_power(self)`

#### `def get_script(self, script_name)`

#### `def get_self_calibration_date_and_time(self, module)`

#### `def get_self_calibration_temperature(self, module)`

#### `def get_terminal_name(self, signal, signal_identifier)`

#### `def get_waveform_burst_start_locations(self, channel_name)`

#### `def get_waveform_burst_stop_locations(self, channel_name)`

#### `def get_waveform_marker_event_locations(self, channel_name)`

#### `def init_with_options(self, resource_name, id_query, reset_device, option_string)`

#### `def initiate(self)`

#### `def load_configurations_from_file(self, channel_name, file_path)`

#### `def lock(self)`

#### `def perform_power_search(self)`

#### `def perform_thermal_correction(self)`

#### `def query_arb_waveform_capabilities(self)`

#### `def read_and_download_waveform_from_file_tdms(self, waveform_name, file_path, waveform_index)`

#### `def reset_device(self)`

#### `def reset_with_defaults(self)`

#### `def reset_with_options(self, steps_to_omit)`

#### `def save_configurations_to_file(self, channel_name, file_path)`

#### `def select_arb_waveform(self, waveform_name)`

#### `def self_cal(self)`

#### `def self_calibrate_range(self, steps_to_omit, min_frequency, max_frequency, min_power_level, max_power_level)`

#### `def send_software_edge_trigger(self, trigger, trigger_identifier)`

#### `def set_arb_waveform_next_write_position(self, waveform_name, relative_to, offset)`

#### `def set_attribute_vi_boolean(self, channel_name, attribute, value)`

#### `def set_attribute_vi_int32(self, channel_name, attribute, value)`

#### `def set_attribute_vi_int64(self, channel_name, attribute, value)`

#### `def set_attribute_vi_real64(self, channel_name, attribute, value)`

#### `def set_attribute_vi_session(self, channel_name, attribute)`

#### `def set_attribute_vi_string(self, channel_name, attribute, value)`

#### `def set_waveform_burst_start_locations(self, channel_name, locations)`

#### `def set_waveform_burst_stop_locations(self, channel_name, locations)`

#### `def set_waveform_marker_event_locations(self, channel_name, locations)`

#### `def unlock(self)`

#### `def wait_until_settled(self, max_time_milliseconds)`

#### `def write_arb_waveform_complex_f32(self, waveform_name, waveform_data_array, more_data_pending)`

#### `def write_arb_waveform_complex_f64(self, waveform_name, waveform_data_array, more_data_pending)`

#### `def write_arb_waveform_complex_i16(self, waveform_name, waveform_data_array)`

#### `def write_script(self, script)`

#### `def close(self)`

#### `def reset(self)`

#### `def self_test(self)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nirfsg/nirfsg/_library.py -->
## PYTHON MODULE: generated/nirfsg/nirfsg/_library.py

### `class Library(object)`

Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    

#### `def __init__(self, ctypes_library)`

#### `def _get_library_function(self, name)`

#### `def niRFSG_Abort(self, vi)`

#### `def niRFSG_AllocateArbWaveform(self, vi, waveform_name, size_in_samples)`

#### `def niRFSG_ChangeExternalCalibrationPassword(self, vi, old_password, new_password)`

#### `def niRFSG_CheckGenerationStatus(self, vi, is_done)`

#### `def niRFSG_CheckIfScriptExists(self, vi, script_name, script_exists)`

#### `def niRFSG_CheckIfWaveformExists(self, vi, waveform_name, waveform_exists)`

#### `def niRFSG_ClearAllArbWaveforms(self, vi)`

#### `def niRFSG_ClearArbWaveform(self, vi, waveform_name)`

#### `def niRFSG_ClearSelfCalibrateRange(self, vi)`

#### `def niRFSG_Commit(self, vi)`

#### `def niRFSG_ConfigureDeembeddingTableInterpolationLinear(self, vi, port, table_name, format)`

#### `def niRFSG_ConfigureDeembeddingTableInterpolationNearest(self, vi, port, table_name)`

#### `def niRFSG_ConfigureDeembeddingTableInterpolationSpline(self, vi, port, table_name)`

#### `def niRFSG_ConfigureDigitalEdgeScriptTrigger(self, vi, trigger_id, source, edge)`

#### `def niRFSG_ConfigureDigitalEdgeStartTrigger(self, vi, source, edge)`

#### `def niRFSG_ConfigureDigitalLevelScriptTrigger(self, vi, trigger_id, source, level)`

#### `def niRFSG_ConfigureRF(self, vi, frequency, power_level)`

#### `def niRFSG_ConfigureRefClock(self, vi, ref_clock_source, ref_clock_rate)`

#### `def niRFSG_ConfigureSoftwareScriptTrigger(self, vi, trigger_id)`

#### `def niRFSG_ConfigureSoftwareStartTrigger(self, vi)`

#### `def niRFSG_CreateDeembeddingSparameterTableArray(self, vi, port, table_name, frequencies, frequencies_size, sparameter_table, sparameter_table_size, number_of_ports, sparameter_orientation)`

#### `def niRFSG_CreateDeembeddingSparameterTableS2PFile(self, vi, port, table_name, s2p_file_path, sparameter_orientation)`

#### `def niRFSG_DeleteAllDeembeddingTables(self, vi)`

#### `def niRFSG_DeleteDeembeddingTable(self, vi, port, table_name)`

#### `def niRFSG_DeleteScript(self, vi, script_name)`

#### `def niRFSG_DisableScriptTrigger(self, vi, trigger_id)`

#### `def niRFSG_DisableStartTrigger(self, vi)`

#### `def niRFSG_ErrorMessage(self, vi, error_code, error_message)`

#### `def niRFSG_GetAllNamedWaveformNames(self, vi, waveform_names, buffer_size, actual_buffer_size)`

#### `def niRFSG_GetAllScriptNames(self, vi, script_names, buffer_size, actual_buffer_size)`

#### `def niRFSG_GetAttributeViBoolean(self, vi, channel_name, attribute, value)`

#### `def niRFSG_GetAttributeViInt32(self, vi, channel_name, attribute, value)`

#### `def niRFSG_GetAttributeViInt64(self, vi, channel_name, attribute, value)`

#### `def niRFSG_GetAttributeViReal64(self, vi, channel_name, attribute, value)`

#### `def niRFSG_GetAttributeViSession(self, vi, channel_name, attribute, value)`

#### `def niRFSG_GetAttributeViString(self, vi, channel_name, attribute, buf_size, value)`

#### `def niRFSG_GetDeembeddingSparameters(self, vi, sparameters, sparameters_array_size, number_of_sparameters, number_of_ports)`

#### `def niRFSG_GetDeembeddingTableNumberOfPorts(self, vi, number_of_ports)`

#### `def niRFSG_GetError(self, vi, error_code, error_description_buffer_size, error_description)`

#### `def niRFSG_GetExternalCalibrationLastDateAndTime(self, vi, year, month, day, hour, minute, second)`

#### `def niRFSG_GetMaxSettablePower(self, vi, value)`

#### `def niRFSG_GetScript(self, vi, script_name, script, buffer_size, actual_buffer_size)`

#### `def niRFSG_GetSelfCalibrationDateAndTime(self, vi, module, year, month, day, hour, minute, second)`

#### `def niRFSG_GetSelfCalibrationTemperature(self, vi, module, temperature)`

#### `def niRFSG_GetTerminalName(self, vi, signal, signal_identifier, buffer_size, terminal_name)`

#### `def niRFSG_GetWaveformBurstStartLocations(self, vi, channel_name, number_of_locations, locations, required_size)`

#### `def niRFSG_GetWaveformBurstStopLocations(self, vi, channel_name, number_of_locations, locations, required_size)`

#### `def niRFSG_GetWaveformMarkerEventLocations(self, vi, channel_name, number_of_locations, locations, required_size)`

#### `def niRFSG_InitWithOptions(self, resource_name, id_query, reset_device, option_string, new_vi)`

#### `def niRFSG_Initiate(self, vi)`

#### `def niRFSG_LoadConfigurationsFromFile(self, vi, channel_name, file_path)`

#### `def niRFSG_LockSession(self, vi, caller_has_lock)`

#### `def niRFSG_PerformPowerSearch(self, vi)`

#### `def niRFSG_PerformThermalCorrection(self, vi)`

#### `def niRFSG_QueryArbWaveformCapabilities(self, vi, max_number_waveforms, waveform_quantum, min_waveform_size, max_waveform_size)`

#### `def niRFSG_ReadAndDownloadWaveformFromFileTDMS(self, vi, waveform_name, file_path, waveform_index)`

#### `def niRFSG_ResetDevice(self, vi)`

#### `def niRFSG_ResetWithDefaults(self, vi)`

#### `def niRFSG_ResetWithOptions(self, vi, steps_to_omit)`

#### `def niRFSG_SaveConfigurationsToFile(self, vi, channel_name, file_path)`

#### `def niRFSG_SelectArbWaveform(self, vi, waveform_name)`

#### `def niRFSG_SelfCal(self, vi)`

#### `def niRFSG_SelfCalibrateRange(self, vi, steps_to_omit, min_frequency, max_frequency, min_power_level, max_power_level)`

#### `def niRFSG_SendSoftwareEdgeTrigger(self, vi, trigger, trigger_identifier)`

#### `def niRFSG_SetArbWaveformNextWritePosition(self, vi, waveform_name, relative_to, offset)`

#### `def niRFSG_SetAttributeViBoolean(self, vi, channel_name, attribute, value)`

#### `def niRFSG_SetAttributeViInt32(self, vi, channel_name, attribute, value)`

#### `def niRFSG_SetAttributeViInt64(self, vi, channel_name, attribute, value)`

#### `def niRFSG_SetAttributeViReal64(self, vi, channel_name, attribute, value)`

#### `def niRFSG_SetAttributeViSession(self, vi, channel_name, attribute, value)`

#### `def niRFSG_SetAttributeViString(self, vi, channel_name, attribute, value)`

#### `def niRFSG_SetWaveformBurstStartLocations(self, vi, channel_name, number_of_locations, locations)`

#### `def niRFSG_SetWaveformBurstStopLocations(self, vi, channel_name, number_of_locations, locations)`

#### `def niRFSG_SetWaveformMarkerEventLocations(self, vi, channel_name, number_of_locations, locations)`

#### `def niRFSG_UnlockSession(self, vi, caller_has_lock)`

#### `def niRFSG_WaitUntilSettled(self, vi, max_time_milliseconds)`

#### `def niRFSG_WriteArbWaveformComplexF32(self, vi, waveform_name, number_of_samples, waveform_data_array, more_data_pending)`

#### `def niRFSG_WriteArbWaveformComplexF64(self, vi, waveform_name, number_of_samples, waveform_data_array, more_data_pending)`

#### `def niRFSG_WriteArbWaveformComplexI16(self, vi, waveform_name, number_of_samples, waveform_data_array)`

#### `def niRFSG_WriteScript(self, vi, script)`

#### `def niRFSG_close(self, vi)`

#### `def niRFSG_reset(self, vi)`

#### `def niRFSG_self_test(self, vi, self_test_result, self_test_message)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nirfsg/nirfsg/_library_interpreter.py -->
## PYTHON MODULE: generated/nirfsg/nirfsg/_library_interpreter.py

### `def _get_ctypes_pointer_for_buffer(value=None, library_type=None, size=None)`

### `def _convert_to_array(value, array_type)`

### `class LibraryInterpreter(object)`

Library C<->Python interpreter.

    This class is responsible for interpreting the Library's C API. It is responsible for:
    * Converting ctypes to native Python types.
    * Dealing with string encoding.
    * Allocating memory.
    * Converting errors returned by Library into Python exceptions.
    

#### `def __init__(self, encoding)`

#### `def set_session_handle(self, value=0)`

#### `def get_session_handle(self)`

#### `def get_error_description(self, error_code)`

get_error_description

        Returns the error description.
        

#### `def abort(self)`

#### `def allocate_arb_waveform(self, waveform_name, size_in_samples)`

#### `def change_external_calibration_password(self, old_password, new_password)`

#### `def check_generation_status(self)`

#### `def check_if_script_exists(self, script_name)`

#### `def check_if_waveform_exists(self, waveform_name)`

#### `def clear_all_arb_waveforms(self)`

#### `def clear_arb_waveform(self, waveform_name)`

#### `def clear_self_calibrate_range(self)`

#### `def commit(self)`

#### `def configure_deembedding_table_interpolation_linear(self, port, table_name, format)`

#### `def configure_deembedding_table_interpolation_nearest(self, port, table_name)`

#### `def configure_deembedding_table_interpolation_spline(self, port, table_name)`

#### `def configure_digital_edge_script_trigger(self, trigger_id, source, edge)`

#### `def configure_digital_edge_start_trigger(self, source, edge)`

#### `def configure_digital_level_script_trigger(self, trigger_id, source, level)`

#### `def configure_rf(self, frequency, power_level)`

#### `def configure_ref_clock(self, ref_clock_source, ref_clock_rate)`

#### `def configure_software_script_trigger(self, trigger_id)`

#### `def configure_software_start_trigger(self)`

#### `def create_deembedding_sparameter_table_array(self, port, table_name, frequencies, sparameter_table, number_of_ports, sparameter_orientation)`

#### `def create_deembedding_sparameter_table_s2p_file(self, port, table_name, s2p_file_path, sparameter_orientation)`

#### `def delete_all_deembedding_tables(self)`

#### `def delete_deembedding_table(self, port, table_name)`

#### `def delete_script(self, script_name)`

#### `def disable_script_trigger(self, trigger_id)`

#### `def disable_start_trigger(self)`

#### `def error_message(self, error_code)`

#### `def get_all_named_waveform_names(self)`

#### `def get_all_script_names(self)`

#### `def get_attribute_vi_boolean(self, channel_name, attribute)`

#### `def get_attribute_vi_int32(self, channel_name, attribute)`

#### `def get_attribute_vi_int64(self, channel_name, attribute)`

#### `def get_attribute_vi_real64(self, channel_name, attribute)`

#### `def get_attribute_vi_session(self, channel_name, attribute)`

#### `def get_attribute_vi_string(self, channel_name, attribute)`

#### `def get_deembedding_sparameters(self)`

#### `def get_deembedding_table_number_of_ports(self)`

#### `def get_error(self)`

#### `def get_external_calibration_last_date_and_time(self)`

#### `def get_max_settable_power(self)`

#### `def get_script(self, script_name)`

#### `def get_self_calibration_date_and_time(self, module)`

#### `def get_self_calibration_temperature(self, module)`

#### `def get_terminal_name(self, signal, signal_identifier)`

#### `def get_waveform_burst_start_locations(self, channel_name)`

#### `def get_waveform_burst_stop_locations(self, channel_name)`

#### `def get_waveform_marker_event_locations(self, channel_name)`

#### `def init_with_options(self, resource_name, id_query, reset_device, option_string)`

#### `def initiate(self)`

#### `def load_configurations_from_file(self, channel_name, file_path)`

#### `def lock(self)`

#### `def perform_power_search(self)`

#### `def perform_thermal_correction(self)`

#### `def query_arb_waveform_capabilities(self)`

#### `def read_and_download_waveform_from_file_tdms(self, waveform_name, file_path, waveform_index)`

#### `def reset_device(self)`

#### `def reset_with_defaults(self)`

#### `def reset_with_options(self, steps_to_omit)`

#### `def save_configurations_to_file(self, channel_name, file_path)`

#### `def select_arb_waveform(self, waveform_name)`

#### `def self_cal(self)`

#### `def self_calibrate_range(self, steps_to_omit, min_frequency, max_frequency, min_power_level, max_power_level)`

#### `def send_software_edge_trigger(self, trigger, trigger_identifier)`

#### `def set_arb_waveform_next_write_position(self, waveform_name, relative_to, offset)`

#### `def set_attribute_vi_boolean(self, channel_name, attribute, value)`

#### `def set_attribute_vi_int32(self, channel_name, attribute, value)`

#### `def set_attribute_vi_int64(self, channel_name, attribute, value)`

#### `def set_attribute_vi_real64(self, channel_name, attribute, value)`

#### `def set_attribute_vi_session(self, channel_name, attribute)`

#### `def set_attribute_vi_string(self, channel_name, attribute, value)`

#### `def set_waveform_burst_start_locations(self, channel_name, locations)`

#### `def set_waveform_burst_stop_locations(self, channel_name, locations)`

#### `def set_waveform_marker_event_locations(self, channel_name, locations)`

#### `def unlock(self)`

#### `def wait_until_settled(self, max_time_milliseconds)`

#### `def write_arb_waveform_complex_f32(self, waveform_name, waveform_data_array, more_data_pending)`

#### `def write_arb_waveform_complex_f64(self, waveform_name, waveform_data_array, more_data_pending)`

#### `def write_arb_waveform_complex_i16(self, waveform_name, waveform_data_array)`

#### `def write_script(self, script)`

#### `def close(self)`

#### `def reset(self)`

#### `def self_test(self)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nirfsg/nirfsg/_library_singleton.py -->
## PYTHON MODULE: generated/nirfsg/nirfsg/_library_singleton.py

### `def _get_library_name()`

### `def _get_library_type()`

### `def get()`

get

    Returns the library.Library singleton for nirfsg.
    

<!--NI_PYTHON_API repo=nimi-python path=generated/nirfsg/nirfsg/enums.py -->
## PYTHON MODULE: generated/nirfsg/nirfsg/enums.py

### `class AllowOutOfSpecificationUserSettings(Enum)`

### `class AmpPath(Enum)`

### `class AnalogModulationFmBand(Enum)`

### `class AnalogModulationFmNarrowbandIntegrator(Enum)`

### `class AnalogModulationPmMode(Enum)`

### `class AnalogModulationType(Enum)`

### `class ArbOnboardSampleClockMode(Enum)`

### `class ArbSampleClockSource(Enum)`

### `class AutomaticLevelControl(Enum)`

### `class AutomaticPowerSearch(Enum)`

### `class AutomaticThermalCorrection(Enum)`

### `class DeembeddingType(Enum)`

### `class DigitalEqualizationEnabled(Enum)`

### `class DirectDownload(Enum)`

### `class Format(Enum)`

### `class FrequencySettlingUnits(Enum)`

### `class GenerationMode(Enum)`

### `class IQOutPortTerminalConfiguration(Enum)`

### `class LoOutExportConfigureFromRfsaEnable(Enum)`

### `class LoPllFractionalModeEnabled(Enum)`

### `class LoSource(Enum)`

### `class LoadConfigurationResetOptions(Enum)`

### `class LoadOptions(Enum)`

### `class LoopBandwidth(Enum)`

### `class MarkerEventOutputBehavior(Enum)`

### `class MarkerEventPulseWidthUnits(Enum)`

### `class MarkerEventToggleInitialState(Enum)`

### `class Module(Enum)`

### `class OffsetUnits(Enum)`

### `class OutputPort(Enum)`

### `class OverflowErrorReporting(Enum)`

### `class PhaseContinuityEnabled(Enum)`

### `class PowerLevelType(Enum)`

### `class PulseModulationMode(Enum)`

### `class PulseModulationOutputTerminal(Enum)`

### `class PulseModulationSource(Enum)`

### `class RFBlanking(Enum)`

### `class RFInLoExportEnabled(Enum)`

### `class ReferenceClockExportOutputTerminal(Enum)`

### `class ReferenceClockSource(Enum)`

### `class ReferencePllBandwidth(Enum)`

### `class RelativeTo(Enum)`

### `class ResetWithOptionsStepsToOmit(IntFlag)`

### `class ScriptTriggerDigitalEdgeEdge(Enum)`

### `class ScriptTriggerDigitalLevelActiveLevel(Enum)`

### `class ScriptTriggerType(Enum)`

### `class SelfCalibrateRangeStepsToOmit(IntFlag)`

### `class Signal(Enum)`

### `class SoftwareTriggerType(Enum)`

### `class SparameterOrientation(Enum)`

### `class StartTriggerDigitalEdgeEdge(Enum)`

### `class StartTriggerType(Enum)`

### `class TriggerIdentifier(Enum)`

### `class UpconverterFrequencyOffsetMode(Enum)`

### `class WriteWaveformBurstDetection(Enum)`

### `class WriteWaveformBurstDetectionMode(Enum)`

### `class WriteWaveformNormalization(Enum)`

### `class YigMainCoilDrive(Enum)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nirfsg/nirfsg/errors.py -->
## PYTHON MODULE: generated/nirfsg/nirfsg/errors.py

### `def _is_success(code)`

### `def _is_error(code)`

### `def _is_warning(code)`

### `class Error(Exception)`

Base error class for NI-RFSG

#### `def __init__(self, message)`

### `class DriverError(Error)`

An error originating from the NI-RFSG driver

#### `def __init__(self, code, description)`

### `class DriverWarning(Warning)`

A warning originating from the NI-RFSG driver

#### `def __init__(self, code, description)`

### `class RpcError(Error)`

An error specific to sessions to the NI gRPC Device Server

#### `def __init__(self, rpc_code, description)`

### `class UnsupportedConfigurationError(Error)`

An error due to using this module in an usupported platform.

#### `def __init__(self)`

### `class DriverNotInstalledError(Error)`

An error due to using this module without the driver runtime installed.

#### `def __init__(self)`

### `class DriverTooOldError(Error)`

An error due to using this module with an older version of the NI-RFSG driver runtime.

#### `def __init__(self)`

### `class DriverTooNewError(Error)`

An error due to the NI-RFSG driver runtime being too new for this module.

#### `def __init__(self)`

### `class InvalidRepeatedCapabilityError(Error)`

An error due to an invalid character in a repeated capability

#### `def __init__(self, invalid_character, invalid_string)`

### `class SelfTestError(Error)`

An error due to a failed self-test

#### `def __init__(self, code, msg)`

### `def handle_error(library_interpreter, code, ignore_warnings, is_error_handling)`

handle_error

    Helper function for handling errors returned by nirfsg.Library.
    It calls back into the LibraryInterpreter to get the corresponding error
    description and raises if necessary.
    

<!--NI_PYTHON_API repo=nimi-python path=generated/nirfsg/nirfsg/grpc_session_options.py -->
## PYTHON MODULE: generated/nirfsg/nirfsg/grpc_session_options.py

- `GRPC_SERVICE_INTERFACE_NAME = 'nirfsg_grpc.NiRFSG'`

- `MEASUREMENTLINK_23Q1_NIMI_PYTHON_API_KEY = 'DE10751B-3EE0-44EC-A93B-800E6A3C89E4'`

### `class SessionInitializationBehavior(IntEnum)`

### `class GrpcSessionOptions(object)`

Collection of options that specifies session behaviors related to gRPC.

#### `def __init__(self, grpc_channel, session_name, *, api_key=MEASUREMENTLINK_23Q1_NIMI_PYTHON_API_KEY, initialization_behavior=SessionInitializationBehavior.AUTO)`

Collection of options that specifies session behaviors related to gRPC.

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
        

<!--NI_PYTHON_API repo=nimi-python path=generated/nirfsg/nirfsg/nidevice_pb2.py -->
## PYTHON MODULE: generated/nirfsg/nirfsg/nidevice_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0enidevice.proto\x12\rnidevice_grpc"2\n\x0fNIComplexNumber\x12\x0c\n\x04real\x18\x01 \x01(\x01\x12\x11\n\timaginary\x18\x02 \x01(\x01"5\n\x12NIComplexNumberF32\x12\x0c\n\x04real\x18\x01 \x01(\x02\x12\x11\n\timaginary\x18\x02 \x01(\x02"/\n\x0cNIComplexI16\x12\x0c\n\x04real\x18\x01 \x01(\x11\x12\x11\n\timaginary\x18\x02 \x01(\x11"r\n\x0fSmtSpectrumInfo\x12\x15\n\rspectrum_type\x18\x01 \x01(\r\x12\x11\n\tlinear_db\x18\x02 \x01(\r\x12\x0e\n\x06window\x18\x03 \x01(\r\x12\x13\n\x0bwindow_size\x18\x04 \x01(\x11\x12\x10\n\x08fft_size\x18\x05 \x01(\x11BB\n\x12com.ni.grpc.deviceB\x08NiDeviceP\x01\xaa\x02\x1fNationalInstruments.Grpc.Deviceb\x06proto3')`

<!--NI_PYTHON_API repo=nimi-python path=generated/nirfsg/nirfsg/nidevice_pb2_grpc.py -->
## PYTHON MODULE: generated/nirfsg/nirfsg/nidevice_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

<!--NI_PYTHON_API repo=nimi-python path=generated/nirfsg/nirfsg/nirfsg_pb2.py -->
## PYTHON MODULE: generated/nirfsg/nirfsg/nirfsg_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cnirfsg.proto\x12\x0bnirfsg_grpc\x1a\x0enidevice.proto\x1a\rsession.proto"2\n\x0cAbortRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\x1f\n\rAbortResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"p\n\x1aAllocateArbWaveformRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rwaveform_name\x18\x02 \x01(\t\x12\x17\n\x0fsize_in_samples\x18\x03 \x01(\x11"-\n\x1bAllocateArbWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x9d\x01\n\x1eCheckAttributeViBooleanRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nirfsg_grpc.NiRFSGAttribute\x12\r\n\x05value\x18\x04 \x01(\x08"1\n\x1fCheckAttributeViBooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xe9\x01\n\x1cCheckAttributeViInt32Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nirfsg_grpc.NiRFSGAttribute\x128\n\x05value\x18\x04 \x01(\x0e2\'.nirfsg_grpc.NiRFSGInt32AttributeValuesH\x00\x12\x13\n\tvalue_raw\x18\x05 \x01(\x11H\x00B\x0c\n\nvalue_enum"/\n\x1dCheckAttributeViInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x9f\x01\n\x1cCheckAttributeViInt64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nirfsg_grpc.NiRFSGAttribute\x12\x11\n\tvalue_raw\x18\x04 \x01(\x03"/\n\x1dCheckAttributeViInt64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xeb\x01\n\x1dCheckAttributeViReal64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nirfsg_grpc.NiRFSGAttribute\x129\n\x05value\x18\x04 \x01(\x0e2(.nirfsg_grpc.NiRFSGReal64AttributeValuesH\x00\x12\x13\n\tvalue_raw\x18\x05 \x01(\x01H\x00B\x0c\n\nvalue_enum"0\n\x1eCheckAttributeViReal64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb5\x01\n\x1eCheckAttributeViSessionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nirfsg_grpc.NiRFSGAttribute\x12%\n\x05value\x18\x04 \x01(\x0b2\x16.nidevice_grpc.Session"1\n\x1fCheckAttributeViSessionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xf8\x01\n\x1dCheckAttributeViStringRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nirfsg_grpc.NiRFSGAttribute\x12F\n\x0cvalue_mapped\x18\x04 \x01(\x0e2..nirfsg_grpc.NiRFSGStringAttributeValuesMappedH\x00\x12\x13\n\tvalue_raw\x18\x05 \x01(\tH\x00B\x0c\n\nvalue_enum"0\n\x1eCheckAttributeViStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"B\n\x1cCheckGenerationStatusRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"@\n\x1dCheckGenerationStatusResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07is_done\x18\x02 \x01(\x08"^\n%CheckIfConfigurationListExistsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tlist_name\x18\x02 \x01(\t"M\n&CheckIfConfigurationListExistsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0blist_exists\x18\x02 \x01(\x08"U\n\x1aCheckIfScriptExistsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x13\n\x0bscript_name\x18\x02 \x01(\t"D\n\x1bCheckIfScriptExistsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rscript_exists\x18\x02 \x01(\x08"Y\n\x1cCheckIfWaveformExistsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rwaveform_name\x18\x02 \x01(\t"H\n\x1dCheckIfWaveformExistsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fwaveform_exists\x18\x02 \x01(\x08"A\n\x1bClearAllArbWaveformsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session".\n\x1cClearAllArbWaveformsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"K\n\x17ClearArbWaveformRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0c\n\x04name\x18\x02 \x01(\t"*\n\x18ClearArbWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"7\n\x11ClearErrorRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"$\n\x12ClearErrorResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"D\n\x1eClearSelfCalibrateRangeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"1\n\x1fClearSelfCalibrateRangeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"2\n\x0cCloseRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\x1f\n\rCloseResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"3\n\rCommitRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session" \n\x0eCommitResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xda\x01\n3ConfigureDeembeddingTableInterpolationLinearRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0c\n\x04port\x18\x02 \x01(\t\x12\x12\n\ntable_name\x18\x03 \x01(\t\x128\n\x06format\x18\x04 \x01(\x0e2&.nirfsg_grpc.LinearInterpolationFormatH\x00\x12\x14\n\nformat_raw\x18\x05 \x01(\x11H\x00B\r\n\x0bformat_enum"F\n4ConfigureDeembeddingTableInterpolationLinearResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"|\n4ConfigureDeembeddingTableInterpolationNearestRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0c\n\x04port\x18\x02 \x01(\t\x12\x12\n\ntable_name\x18\x03 \x01(\t"G\n5ConfigureDeembeddingTableInterpolationNearestResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"{\n3ConfigureDeembeddingTableInterpolationSplineRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0c\n\x04port\x18\x02 \x01(\t\x12\x12\n\ntable_name\x18\x03 \x01(\t"F\n4ConfigureDeembeddingTableInterpolationSplineResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa6\x02\n7ConfigureDigitalEdgeConfigurationListStepTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12S\n\rsource_mapped\x18\x02 \x01(\x0e2:.nirfsg_grpc.DigitalEdgeConfigurationListStepTriggerSourceH\x00\x12\x14\n\nsource_raw\x18\x03 \x01(\tH\x00\x12,\n\x04edge\x18\x04 \x01(\x0e2\x1c.nirfsg_grpc.DigitalEdgeEdgeH\x01\x12\x12\n\x08edge_raw\x18\x05 \x01(\x11H\x01B\r\n\x0bsource_enumB\x0b\n\tedge_enum"J\n8ConfigureDigitalEdgeConfigurationListStepTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xf2\x02\n(ConfigureDigitalEdgeScriptTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12L\n\x11trigger_id_mapped\x18\x02 \x01(\x0e2/.nirfsg_grpc.DigitalEdgeScriptTriggerIdentifierH\x00\x12\x18\n\x0etrigger_id_raw\x18\x03 \x01(\tH\x00\x123\n\rsource_mapped\x18\x04 \x01(\x0e2\x1a.nirfsg_grpc.TriggerSourceH\x01\x12\x14\n\nsource_raw\x18\x05 \x01(\tH\x01\x12,\n\x04edge\x18\x06 \x01(\x0e2\x1c.nirfsg_grpc.DigitalEdgeEdgeH\x02\x12\x12\n\x08edge_raw\x18\x07 \x01(\x11H\x02B\x11\n\x0ftrigger_id_enumB\r\n\x0bsource_enumB\x0b\n\tedge_enum";\n)ConfigureDigitalEdgeScriptTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xf6\x01\n\'ConfigureDigitalEdgeStartTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x123\n\rsource_mapped\x18\x02 \x01(\x0e2\x1a.nirfsg_grpc.TriggerSourceH\x00\x12\x14\n\nsource_raw\x18\x03 \x01(\tH\x00\x12,\n\x04edge\x18\x04 \x01(\x0e2\x1c.nirfsg_grpc.DigitalEdgeEdgeH\x01\x12\x12\n\x08edge_raw\x18\x05 \x01(\x11H\x01B\r\n\x0bsource_enumB\x0b\n\tedge_enum":\n(ConfigureDigitalEdgeStartTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xfe\x02\n)ConfigureDigitalLevelScriptTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12L\n\x11trigger_id_mapped\x18\x02 \x01(\x0e2/.nirfsg_grpc.DigitalEdgeScriptTriggerIdentifierH\x00\x12\x18\n\x0etrigger_id_raw\x18\x03 \x01(\tH\x00\x123\n\rsource_mapped\x18\x04 \x01(\x0e2\x1a.nirfsg_grpc.TriggerSourceH\x01\x12\x14\n\nsource_raw\x18\x05 \x01(\tH\x01\x125\n\x05level\x18\x06 \x01(\x0e2$.nirfsg_grpc.DigitalLevelActiveLevelH\x02\x12\x13\n\tlevel_raw\x18\x07 \x01(\x11H\x02B\x11\n\x0ftrigger_id_enumB\r\n\x0bsource_enumB\x0c\n\nlevel_enum"<\n*ConfigureDigitalLevelScriptTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"y\n4ConfigureDigitalModulationUserDefinedWaveformRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1d\n\x15user_defined_waveform\x18\x02 \x01(\x0c"G\n5ConfigureDigitalModulationUserDefinedWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb3\x01\n\x1eConfigureGenerationModeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x126\n\x0fgeneration_mode\x18\x02 \x01(\x0e2\x1b.nirfsg_grpc.GenerationModeH\x00\x12\x1d\n\x13generation_mode_raw\x18\x03 \x01(\x11H\x00B\x16\n\x14generation_mode_enum"1\n\x1fConfigureGenerationModeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"[\n\x1dConfigureOutputEnabledRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x16\n\x0eoutput_enabled\x18\x02 \x01(\x08"0\n\x1eConfigureOutputEnabledResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"z\n/ConfigureP2PEndpointFullnessStartTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12#\n\x1bp2p_endpoint_fullness_level\x18\x02 \x01(\x03"B\n0ConfigureP2PEndpointFullnessStartTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xbf\x01\n\x1fConfigurePXIChassisClk10Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12?\n\x17pxi_clk10_source_mapped\x18\x02 \x01(\x0e2\x1c.nirfsg_grpc.PXIChassisClk10H\x00\x12\x1e\n\x14pxi_clk10_source_raw\x18\x03 \x01(\tH\x00B\x17\n\x15pxi_clk10_source_enum"2\n ConfigurePXIChassisClk10Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb6\x01\n\x1eConfigurePowerLevelTypeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x127\n\x10power_level_type\x18\x02 \x01(\x0e2\x1b.nirfsg_grpc.PowerLevelTypeH\x00\x12\x1e\n\x14power_level_type_raw\x18\x03 \x01(\x11H\x00B\x17\n\x15power_level_type_enum"1\n\x1fConfigurePowerLevelTypeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"`\n\x12ConfigureRFRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tfrequency\x18\x02 \x01(\x01\x12\x13\n\x0bpower_level\x18\x03 \x01(\x01"%\n\x13ConfigureRFResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xcf\x01\n\x18ConfigureRefClockRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12>\n\x17ref_clock_source_mapped\x18\x02 \x01(\x0e2\x1b.nirfsg_grpc.RefClockSourceH\x00\x12\x1e\n\x14ref_clock_source_raw\x18\x03 \x01(\tH\x00\x12\x16\n\x0eref_clock_rate\x18\x04 \x01(\x01B\x17\n\x15ref_clock_source_enum"+\n\x19ConfigureRefClockResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"_\n\x1fConfigureSignalBandwidthRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10signal_bandwidth\x18\x02 \x01(\x01"2\n ConfigureSignalBandwidthResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xc6\x01\n%ConfigureSoftwareScriptTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12L\n\x11trigger_id_mapped\x18\x02 \x01(\x0e2/.nirfsg_grpc.DigitalEdgeScriptTriggerIdentifierH\x00\x12\x18\n\x0etrigger_id_raw\x18\x03 \x01(\tH\x00B\x11\n\x0ftrigger_id_enum"8\n&ConfigureSoftwareScriptTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"J\n$ConfigureSoftwareStartTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"7\n%ConfigureSoftwareStartTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x86\x01\n*ConfigureUpconverterPLLSettlingTimeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x19\n\x11pll_settling_time\x18\x02 \x01(\x01\x12\x19\n\x11ensure_pll_locked\x18\x03 \x01(\x08"=\n+ConfigureUpconverterPLLSettlingTimeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb8\x01\n\x1eCreateConfigurationListRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tlist_name\x18\x02 \x01(\t\x12C\n\x1dconfiguration_list_attributes\x18\x03 \x03(\x0e2\x1c.nirfsg_grpc.NiRFSGAttribute\x12\x1a\n\x12set_as_active_list\x18\x04 \x01(\x08"1\n\x1fCreateConfigurationListResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"d\n"CreateConfigurationListStepRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12set_as_active_step\x18\x02 \x01(\x08"5\n#CreateConfigurationListStepResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xe7\x02\n,CreateDeembeddingSparameterTableArrayRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0c\n\x04port\x18\x02 \x01(\t\x12\x12\n\ntable_name\x18\x03 \x01(\t\x12\x13\n\x0bfrequencies\x18\x04 \x03(\x01\x128\n\x10sparameter_table\x18\x05 \x03(\x0b2\x1e.nidevice_grpc.NIComplexNumber\x12\x17\n\x0fnumber_of_ports\x18\x06 \x01(\x11\x12D\n\x16sparameter_orientation\x18\x07 \x01(\x0e2".nirfsg_grpc.SParameterOrientationH\x00\x12$\n\x1asparameter_orientation_raw\x18\x08 \x01(\x11H\x00B\x1d\n\x1bsparameter_orientation_enum"?\n-CreateDeembeddingSparameterTableArrayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x98\x02\n.CreateDeembeddingSparameterTableS2PFileRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0c\n\x04port\x18\x02 \x01(\t\x12\x12\n\ntable_name\x18\x03 \x01(\t\x12\x15\n\rs2p_file_path\x18\x04 \x01(\t\x12D\n\x16sparameter_orientation\x18\x05 \x01(\x0e2".nirfsg_grpc.SParameterOrientationH\x00\x12$\n\x1asparameter_orientation_raw\x18\x06 \x01(\x11H\x00B\x1d\n\x1bsparameter_orientation_enum"A\n/CreateDeembeddingSparameterTableS2PFileResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"G\n!DeleteAllDeembeddingTablesRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"4\n"DeleteAllDeembeddingTablesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"W\n\x1eDeleteConfigurationListRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tlist_name\x18\x02 \x01(\t"1\n\x1fDeleteConfigurationListResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"e\n\x1dDeleteDeembeddingTableRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0c\n\x04port\x18\x02 \x01(\t\x12\x12\n\ntable_name\x18\x03 \x01(\t"0\n\x1eDeleteDeembeddingTableResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"N\n\x13DeleteScriptRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x13\n\x0bscript_name\x18\x02 \x01(\t"&\n\x14DeleteScriptResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"4\n\x0eDisableRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"!\n\x0fDisableResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"A\n\x1bDisableAllModulationRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session".\n\x1cDisableAllModulationResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"P\n*DisableConfigurationListStepTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"=\n+DisableConfigurationListStepTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xbc\x01\n\x1bDisableScriptTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12L\n\x11trigger_id_mapped\x18\x02 \x01(\x0e2/.nirfsg_grpc.DigitalEdgeScriptTriggerIdentifierH\x00\x12\x18\n\x0etrigger_id_raw\x18\x03 \x01(\tH\x00B\x11\n\x0ftrigger_id_enum".\n\x1cDisableScriptTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"@\n\x1aDisableStartTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"-\n\x1bDisableStartTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"M\n\x13ErrorMessageRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x12\n\nerror_code\x18\x02 \x01(\x11"=\n\x14ErrorMessageResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rerror_message\x18\x02 \x01(\t"7\n\x11ErrorQueryRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"O\n\x12ErrorQueryResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nerror_code\x18\x02 \x01(\x11\x12\x15\n\rerror_message\x18\x03 \x01(\t"\xfd\x02\n\x13ExportSignalRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12+\n\x06signal\x18\x02 \x01(\x0e2\x19.nirfsg_grpc.RoutedSignalH\x00\x12\x14\n\nsignal_raw\x18\x03 \x01(\x11H\x00\x12A\n\x18signal_identifier_mapped\x18\x04 \x01(\x0e2\x1d.nirfsg_grpc.SignalIdentifierH\x01\x12\x1f\n\x15signal_identifier_raw\x18\x05 \x01(\tH\x01\x12;\n\x16output_terminal_mapped\x18\x06 \x01(\x0e2\x19.nirfsg_grpc.OutputSignalH\x02\x12\x1d\n\x13output_terminal_raw\x18\x07 \x01(\tH\x02B\r\n\x0bsignal_enumB\x18\n\x16signal_identifier_enumB\x16\n\x14output_terminal_enum"&\n\x14ExportSignalResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"E\n\x1fGetAllNamedWaveformNamesRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"f\n GetAllNamedWaveformNamesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x16\n\x0ewaveform_names\x18\x02 \x01(\t\x12\x1a\n\x12actual_buffer_size\x18\x03 \x01(\x11">\n\x18GetAllScriptNamesRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"]\n\x19GetAllScriptNamesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x14\n\x0cscript_names\x18\x02 \x01(\t\x12\x1a\n\x12actual_buffer_size\x18\x03 \x01(\x11"K\n\x10GetScriptRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x13\n\x0bscript_name\x18\x02 \x01(\t"O\n\x11GetScriptResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0e\n\x06script\x18\x02 \x01(\t\x12\x1a\n\x12actual_buffer_size\x18\x03 \x01(\x11"\x8c\x01\n\x1cGetAttributeViBooleanRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nirfsg_grpc.NiRFSGAttribute">\n\x1dGetAttributeViBooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x08"\x8a\x01\n\x1aGetAttributeViInt32Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nirfsg_grpc.NiRFSGAttribute"<\n\x1bGetAttributeViInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x11"\x8a\x01\n\x1aGetAttributeViInt64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nirfsg_grpc.NiRFSGAttribute"<\n\x1bGetAttributeViInt64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x03"\x8b\x01\n\x1bGetAttributeViReal64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nirfsg_grpc.NiRFSGAttribute"=\n\x1cGetAttributeViReal64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x01"\x8c\x01\n\x1cGetAttributeViSessionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nirfsg_grpc.NiRFSGAttribute"V\n\x1dGetAttributeViSessionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12%\n\x05value\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session"\x8b\x01\n\x1bGetAttributeViStringRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nirfsg_grpc.NiRFSGAttribute"=\n\x1cGetAttributeViStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t"J\n\x15GetChannelNameRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\r\n\x05index\x18\x02 \x01(\x11"6\n\x16GetChannelNameResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t"F\n GetDeembeddingSparametersRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\xa0\x01\n!GetDeembeddingSparametersResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x123\n\x0bsparameters\x18\x02 \x03(\x0b2\x1e.nidevice_grpc.NIComplexNumber\x12\x1d\n\x15number_of_sparameters\x18\x03 \x01(\x11\x12\x17\n\x0fnumber_of_ports\x18\x04 \x01(\x11"5\n\x0fGetErrorRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"Q\n\x10GetErrorResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nerror_code\x18\x02 \x01(\x11\x12\x19\n\x11error_description\x18\x03 \x01(\t"R\n,GetExternalCalibrationLastDateAndTimeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\x97\x01\n-GetExternalCalibrationLastDateAndTimeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04year\x18\x02 \x01(\x11\x12\r\n\x05month\x18\x03 \x01(\x11\x12\x0b\n\x03day\x18\x04 \x01(\x11\x12\x0c\n\x04hour\x18\x05 \x01(\x11\x12\x0e\n\x06minute\x18\x06 \x01(\x11\x12\x0e\n\x06second\x18\x07 \x01(\x11"@\n\x1aGetMaxSettablePowerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"<\n\x1bGetMaxSettablePowerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x01"\x96\x01\n$GetSelfCalibrationDateAndTimeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12%\n\x06module\x18\x02 \x01(\x0e2\x13.nirfsg_grpc.ModuleH\x00\x12\x14\n\nmodule_raw\x18\x03 \x01(\x11H\x00B\r\n\x0bmodule_enum"\x8f\x01\n%GetSelfCalibrationDateAndTimeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04year\x18\x02 \x01(\x11\x12\r\n\x05month\x18\x03 \x01(\x11\x12\x0b\n\x03day\x18\x04 \x01(\x11\x12\x0c\n\x04hour\x18\x05 \x01(\x11\x12\x0e\n\x06minute\x18\x06 \x01(\x11\x12\x0e\n\x06second\x18\x07 \x01(\x11"\x96\x01\n$GetSelfCalibrationTemperatureRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12%\n\x06module\x18\x02 \x01(\x0e2\x13.nirfsg_grpc.ModuleH\x00\x12\x14\n\nmodule_raw\x18\x03 \x01(\x11H\x00B\r\n\x0bmodule_enum"L\n%GetSelfCalibrationTemperatureResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0btemperature\x18\x02 \x01(\x01"\x8c\x02\n\x16GetTerminalNameRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12+\n\x06signal\x18\x02 \x01(\x0e2\x19.nirfsg_grpc.RoutedSignalH\x00\x12\x14\n\nsignal_raw\x18\x03 \x01(\x11H\x00\x12A\n\x18signal_identifier_mapped\x18\x04 \x01(\x0e2\x1d.nirfsg_grpc.SignalIdentifierH\x01\x12\x1f\n\x15signal_identifier_raw\x18\x05 \x01(\tH\x01B\r\n\x0bsignal_enumB\x18\n\x16signal_identifier_enum"@\n\x17GetTerminalNameResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rterminal_name\x18\x02 \x01(\t"L\n\x12GetUserDataRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x12\n\nidentifier\x18\x02 \x01(\t"M\n\x13GetUserDataResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04data\x18\x02 \x01(\x0c\x12\x18\n\x10actual_data_size\x18\x03 \x01(\x11"a\n%GetWaveformBurstStartLocationsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t"b\n&GetWaveformBurstStartLocationsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x11\n\tlocations\x18\x02 \x03(\x01\x12\x15\n\rrequired_size\x18\x03 \x01(\x11"`\n$GetWaveformBurstStopLocationsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t"a\n%GetWaveformBurstStopLocationsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x11\n\tlocations\x18\x02 \x03(\x01\x12\x15\n\rrequired_size\x18\x03 \x01(\x11"b\n&GetWaveformMarkerEventLocationsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t"c\n\'GetWaveformMarkerEventLocationsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x11\n\tlocations\x18\x02 \x03(\x01\x12\x15\n\rrequired_size\x18\x03 \x01(\x11"\xb1\x01\n\x0bInitRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\x10\n\x08id_query\x18\x03 \x01(\x08\x12\x14\n\x0creset_device\x18\x04 \x01(\x08\x12M\n\x17initialization_behavior\x18\x05 \x01(\x0e2,.nidevice_grpc.SessionInitializationBehavior"\x82\x01\n\x0cInitResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12&\n\x06new_vi\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x19\n\rerror_message\x18\x03 \x01(\tB\x02\x18\x01\x12\x1f\n\x17new_session_initialized\x18\x04 \x01(\x08"\xd3\x01\n\x16InitWithOptionsRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\x10\n\x08id_query\x18\x03 \x01(\x08\x12\x14\n\x0creset_device\x18\x04 \x01(\x08\x12\x15\n\roption_string\x18\x05 \x01(\t\x12M\n\x17initialization_behavior\x18\x06 \x01(\x0e2,.nidevice_grpc.SessionInitializationBehavior"\x89\x01\n\x17InitWithOptionsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12"\n\x02vi\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x19\n\rerror_message\x18\x03 \x01(\tB\x02\x18\x01\x12\x1f\n\x17new_session_initialized\x18\x04 \x01(\x08"5\n\x0fInitiateRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session""\n\x10InitiateResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"D\n\x1eInvalidateAllAttributesRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"1\n\x1fInvalidateAllAttributesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"p\n!LoadConfigurationsFromFileRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x11\n\tfile_path\x18\x03 \x01(\t"4\n"LoadConfigurationsFromFileResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"?\n\x19PerformPowerSearchRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session",\n\x1aPerformPowerSearchResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"E\n\x1fPerformThermalCorrectionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"2\n PerformThermalCorrectionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"I\n#QueryArbWaveformCapabilitiesRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\xa4\x01\n$QueryArbWaveformCapabilitiesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1c\n\x14max_number_waveforms\x18\x02 \x01(\x11\x12\x18\n\x10waveform_quantum\x18\x03 \x01(\x11\x12\x19\n\x11min_waveform_size\x18\x04 \x01(\x11\x12\x19\n\x11max_waveform_size\x18\x05 \x01(\x11"\x92\x01\n*ReadAndDownloadWaveformFromFileTDMSRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rwaveform_name\x18\x02 \x01(\t\x12\x11\n\tfile_path\x18\x03 \x01(\t\x12\x16\n\x0ewaveform_index\x18\x04 \x01(\r"=\n+ReadAndDownloadWaveformFromFileTDMSResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"2\n\x0cResetRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\x1f\n\rResetResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x85\x01\n\x15ResetAttributeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nirfsg_grpc.NiRFSGAttribute"(\n\x16ResetAttributeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"8\n\x12ResetDeviceRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"%\n\x13ResetDeviceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05">\n\x18ResetWithDefaultsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"+\n\x19ResetWithDefaultsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb3\x01\n\x17ResetWithOptionsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12A\n\rsteps_to_omit\x18\x02 \x01(\x0e2(.nirfsg_grpc.ResetWithOptionsStepsToOmitH\x00\x12\x1b\n\x11steps_to_omit_raw\x18\x03 \x01(\x04H\x00B\x14\n\x12steps_to_omit_enum"*\n\x18ResetWithOptionsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05":\n\x14RevisionQueryRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"f\n\x15RevisionQueryResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12"\n\x1ainstrument_driver_revision\x18\x02 \x01(\t\x12\x19\n\x11firmware_revision\x18\x03 \x01(\t"n\n\x1fSaveConfigurationsToFileRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x11\n\tfile_path\x18\x03 \x01(\t"2\n SaveConfigurationsToFileResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"L\n\x18SelectArbWaveformRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0c\n\x04name\x18\x02 \x01(\t"+\n\x19SelectArbWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"4\n\x0eSelfCalRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"!\n\x0fSelfCalResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x97\x02\n\x19SelfCalibrateRangeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12C\n\rsteps_to_omit\x18\x02 \x01(\x0e2*.nirfsg_grpc.SelfCalibrateRangeStepsToOmitH\x00\x12\x1b\n\x11steps_to_omit_raw\x18\x03 \x01(\x03H\x00\x12\x15\n\rmin_frequency\x18\x04 \x01(\x01\x12\x15\n\rmax_frequency\x18\x05 \x01(\x01\x12\x17\n\x0fmin_power_level\x18\x06 \x01(\x01\x12\x17\n\x0fmax_power_level\x18\x07 \x01(\x01B\x14\n\x12steps_to_omit_enum",\n\x1aSelfCalibrateRangeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"5\n\x0fSelfTestRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"W\n\x10SelfTestResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x18\n\x10self_test_result\x18\x02 \x01(\x11\x12\x19\n\x11self_test_message\x18\x03 \x01(\t"\x9a\x02\n\x1eSendSoftwareEdgeTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12,\n\x07trigger\x18\x02 \x01(\x0e2\x19.nirfsg_grpc.RoutedSignalH\x00\x12\x15\n\x0btrigger_raw\x18\x03 \x01(\x11H\x00\x12B\n\x19trigger_identifier_mapped\x18\x04 \x01(\x0e2\x1d.nirfsg_grpc.SignalIdentifierH\x01\x12 \n\x16trigger_identifier_raw\x18\x05 \x01(\tH\x01B\x0e\n\x0ctrigger_enumB\x19\n\x17trigger_identifier_enum"1\n\x1fSendSoftwareEdgeTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xd2\x01\n&SetArbWaveformNextWritePositionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rwaveform_name\x18\x02 \x01(\t\x12.\n\x0brelative_to\x18\x03 \x01(\x0e2\x17.nirfsg_grpc.RelativeToH\x00\x12\x19\n\x0frelative_to_raw\x18\x04 \x01(\x11H\x00\x12\x0e\n\x06offset\x18\x05 \x01(\x11B\x12\n\x10relative_to_enum"9\n\'SetArbWaveformNextWritePositionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x9b\x01\n\x1cSetAttributeViBooleanRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nirfsg_grpc.NiRFSGAttribute\x12\r\n\x05value\x18\x04 \x01(\x08"/\n\x1dSetAttributeViBooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xe7\x01\n\x1aSetAttributeViInt32Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nirfsg_grpc.NiRFSGAttribute\x128\n\x05value\x18\x04 \x01(\x0e2\'.nirfsg_grpc.NiRFSGInt32AttributeValuesH\x00\x12\x13\n\tvalue_raw\x18\x05 \x01(\x11H\x00B\x0c\n\nvalue_enum"-\n\x1bSetAttributeViInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x9d\x01\n\x1aSetAttributeViInt64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nirfsg_grpc.NiRFSGAttribute\x12\x11\n\tvalue_raw\x18\x04 \x01(\x03"-\n\x1bSetAttributeViInt64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xe9\x01\n\x1bSetAttributeViReal64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nirfsg_grpc.NiRFSGAttribute\x129\n\x05value\x18\x04 \x01(\x0e2(.nirfsg_grpc.NiRFSGReal64AttributeValuesH\x00\x12\x13\n\tvalue_raw\x18\x05 \x01(\x01H\x00B\x0c\n\nvalue_enum".\n\x1cSetAttributeViReal64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb3\x01\n\x1cSetAttributeViSessionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nirfsg_grpc.NiRFSGAttribute\x12%\n\x05value\x18\x04 \x01(\x0b2\x16.nidevice_grpc.Session"/\n\x1dSetAttributeViSessionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xf6\x01\n\x1bSetAttributeViStringRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1c.nirfsg_grpc.NiRFSGAttribute\x12F\n\x0cvalue_mapped\x18\x04 \x01(\x0e2..nirfsg_grpc.NiRFSGStringAttributeValuesMappedH\x00\x12\x13\n\tvalue_raw\x18\x05 \x01(\tH\x00B\x0c\n\nvalue_enum".\n\x1cSetAttributeViStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"Z\n\x12SetUserDataRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x12\n\nidentifier\x18\x02 \x01(\t\x12\x0c\n\x04data\x18\x03 \x01(\x0c"%\n\x13SetUserDataResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"t\n%SetWaveformBurstStartLocationsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x11\n\tlocations\x18\x03 \x03(\x01"8\n&SetWaveformBurstStartLocationsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"s\n$SetWaveformBurstStopLocationsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x11\n\tlocations\x18\x03 \x03(\x01"7\n%SetWaveformBurstStopLocationsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"u\n&SetWaveformMarkerEventLocationsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x11\n\tlocations\x18\x03 \x03(\x01"9\n\'SetWaveformMarkerEventLocationsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\\\n\x17WaitUntilSettledRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1d\n\x15max_time_milliseconds\x18\x02 \x01(\x11"*\n\x18WaitUntilSettledResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x8f\x01\n\x17WriteArbWaveformRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rwaveform_name\x18\x02 \x01(\t\x12\x0e\n\x06i_data\x18\x03 \x03(\x01\x12\x0e\n\x06q_data\x18\x04 \x03(\x01\x12\x19\n\x11more_data_pending\x18\x05 \x01(\x08"*\n\x18WriteArbWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xae\x01\n!WriteArbWaveformComplexF32Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rwaveform_name\x18\x02 \x01(\t\x123\n\x08wfm_data\x18\x03 \x03(\x0b2!.nidevice_grpc.NIComplexNumberF32\x12\x19\n\x11more_data_pending\x18\x04 \x01(\x08"4\n"WriteArbWaveformComplexF32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xab\x01\n!WriteArbWaveformComplexF64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rwaveform_name\x18\x02 \x01(\t\x120\n\x08wfm_data\x18\x03 \x03(\x0b2\x1e.nidevice_grpc.NIComplexNumber\x12\x19\n\x11more_data_pending\x18\x04 \x01(\x08"4\n"WriteArbWaveformComplexF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x8d\x01\n!WriteArbWaveformComplexI16Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rwaveform_name\x18\x02 \x01(\t\x12-\n\x08wfm_data\x18\x03 \x03(\x0b2\x1b.nidevice_grpc.NIComplexI16"4\n"WriteArbWaveformComplexI16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x92\x01\n\x1aWriteArbWaveformF32Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rwaveform_name\x18\x02 \x01(\t\x12\x0e\n\x06i_data\x18\x03 \x03(\x02\x12\x0e\n\x06q_data\x18\x04 \x03(\x02\x12\x19\n\x11more_data_pending\x18\x05 \x01(\x08"-\n\x1bWriteArbWaveformF32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"H\n\x12WriteScriptRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0e\n\x06script\x18\x02 \x01(\t"%\n\x13WriteScriptResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05*\xdda\n\x0fNiRFSGAttribute\x12 \n\x1cNIRFSG_ATTRIBUTE_UNSPECIFIED\x10\x00\x12"\n\x1cNIRFSG_ATTRIBUTE_RANGE_CHECK\x10\x92\x8b@\x12.\n(NIRFSG_ATTRIBUTE_QUERY_INSTRUMENT_STATUS\x10\x93\x8b@\x12\x1c\n\x16NIRFSG_ATTRIBUTE_CACHE\x10\x94\x8b@\x12\x1f\n\x19NIRFSG_ATTRIBUTE_SIMULATE\x10\x95\x8b@\x12\'\n!NIRFSG_ATTRIBUTE_RECORD_COERCIONS\x10\x96\x8b@\x12#\n\x1dNIRFSG_ATTRIBUTE_DRIVER_SETUP\x10\x97\x8b@\x12(\n"NIRFSG_ATTRIBUTE_INTERCHANGE_CHECK\x10\xa5\x8b@\x12\x1a\n\x14NIRFSG_ATTRIBUTE_SPY\x10\xa6\x8b@\x12.\n(NIRFSG_ATTRIBUTE_USE_SPECIFIC_SIMULATION\x10\xa7\x8b@\x12$\n\x1eNIRFSG_ATTRIBUTE_CHANNEL_COUNT\x10\xdb\x8c@\x12-\n\'NIRFSG_ATTRIBUTE_SPECIFIC_DRIVER_PREFIX\x10\xbe\x8d@\x12-\n\'NIRFSG_ATTRIBUTE_IO_RESOURCE_DESCRIPTOR\x10\xc0\x8d@\x12#\n\x1dNIRFSG_ATTRIBUTE_LOGICAL_NAME\x10\xc1\x8d@\x122\n,NIRFSG_ATTRIBUTE_SUPPORTED_INSTRUMENT_MODELS\x10\xd7\x8d@\x12)\n#NIRFSG_ATTRIBUTE_GROUP_CAPABILITIES\x10\xa1\x8e@\x12,\n&NIRFSG_ATTRIBUTE_FUNCTION_CAPABILITIES\x10\xa2\x8e@\x123\n-NIRFSG_ATTRIBUTE_INSTRUMENT_FIRMWARE_REVISION\x10\x8e\x8f@\x12.\n(NIRFSG_ATTRIBUTE_INSTRUMENT_MANUFACTURER\x10\x8f\x8f@\x12\'\n!NIRFSG_ATTRIBUTE_INSTRUMENT_MODEL\x10\x90\x8f@\x12-\n\'NIRFSG_ATTRIBUTE_SPECIFIC_DRIVER_VENDOR\x10\x91\x8f@\x122\n,NIRFSG_ATTRIBUTE_SPECIFIC_DRIVER_DESCRIPTION\x10\x92\x8f@\x12?\n9NIRFSG_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION\x10\x93\x8f@\x12?\n9NIRFSG_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION\x10\x94\x8f@\x12/\n)NIRFSG_ATTRIBUTE_SPECIFIC_DRIVER_REVISION\x10\xb7\x8f@\x12\'\n!NIRFSG_ATTRIBUTE_REF_CLOCK_SOURCE\x10\xb1\x98F\x128\n2NIRFSG_ATTRIBUTE_DIGITAL_EDGE_START_TRIGGER_SOURCE\x10\xb2\x98F\x12=\n7NIRFSG_ATTRIBUTE_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL\x10\xb3\x98F\x12/\n)NIRFSG_ATTRIBUTE_PXI_CHASSIS_CLK10_SOURCE\x10\xb4\x98F\x12/\n)NIRFSG_ATTRIBUTE_PHASE_CONTINUITY_ENABLED\x10\xb5\x98F\x12*\n$NIRFSG_ATTRIBUTE_FREQUENCY_TOLERANCE\x10\xb6\x98F\x12\'\n!NIRFSG_ATTRIBUTE_SIGNAL_BANDWIDTH\x10\xb7\x98F\x123\n-NIRFSG_ATTRIBUTE_AUTOMATIC_THERMAL_CORRECTION\x10\xb8\x98F\x12.\n(NIRFSG_ATTRIBUTE_ATTENUATOR_HOLD_ENABLED\x10\xb9\x98F\x120\n*NIRFSG_ATTRIBUTE_ATTENUATOR_HOLD_MAX_POWER\x10\xba\x98F\x12*\n$NIRFSG_ATTRIBUTE_PEAK_ENVELOPE_POWER\x10\xbb\x98F\x123\n-NIRFSG_ATTRIBUTE_DIGITAL_EQUALIZATION_ENABLED\x10\xbc\x98F\x12%\n\x1fNIRFSG_ATTRIBUTE_LO_OUT_ENABLED\x10\xbd\x98F\x12?\n9NIRFSG_ATTRIBUTE_ALLOW_OUT_OF_SPECIFICATION_USER_SETTINGS\x10\xbe\x98F\x12,\n&NIRFSG_ATTRIBUTE_ARB_CARRIER_FREQUENCY\x10\xbf\x98F\x12 \n\x1aNIRFSG_ATTRIBUTE_ARB_POWER\x10\xc0\x98F\x12)\n#NIRFSG_ATTRIBUTE_DEVICE_TEMPERATURE\x10\xc1\x98F\x12&\n NIRFSG_ATTRIBUTE_GENERATION_MODE\x10\xc2\x98F\x12*\n$NIRFSG_ATTRIBUTE_SCRIPT_TRIGGER_TYPE\x10\xc3\x98F\x129\n3NIRFSG_ATTRIBUTE_DIGITAL_EDGE_SCRIPT_TRIGGER_SOURCE\x10\xc4\x98F\x127\n1NIRFSG_ATTRIBUTE_DIGITAL_EDGE_SCRIPT_TRIGGER_EDGE\x10\xc5\x98F\x12>\n8NIRFSG_ATTRIBUTE_EXPORTED_SCRIPT_TRIGGER_OUTPUT_TERMINAL\x10\xc6\x98F\x12&\n NIRFSG_ATTRIBUTE_SELECTED_SCRIPT\x10\xc7\x98F\x12#\n\x1dNIRFSG_ATTRIBUTE_PHASE_OFFSET\x10\xc8\x98F\x12*\n$NIRFSG_ATTRIBUTE_ARB_PRE_FILTER_GAIN\x10\xc9\x98F\x12$\n\x1eNIRFSG_ATTRIBUTE_SERIAL_NUMBER\x10\xca\x98F\x12%\n\x1fNIRFSG_ATTRIBUTE_LOOP_BANDWIDTH\x10\xcb\x98F\x124\n.NIRFSG_ATTRIBUTE_ARB_ONBOARD_SAMPLE_CLOCK_MODE\x10\xcd\x98F\x12.\n(NIRFSG_ATTRIBUTE_ARB_SAMPLE_CLOCK_SOURCE\x10\xce\x98F\x12,\n&NIRFSG_ATTRIBUTE_ARB_SAMPLE_CLOCK_RATE\x10\xcf\x98F\x12-\n\'NIRFSG_ATTRIBUTE_ANALOG_MODULATION_TYPE\x10\xd0\x98F\x126\n0NIRFSG_ATTRIBUTE_ANALOG_MODULATION_WAVEFORM_TYPE\x10\xd1\x98F\x12;\n5NIRFSG_ATTRIBUTE_ANALOG_MODULATION_WAVEFORM_FREQUENCY\x10\xd2\x98F\x125\n/NIRFSG_ATTRIBUTE_ANALOG_MODULATION_FM_DEVIATION\x10\xd3\x98F\x12.\n(NIRFSG_ATTRIBUTE_DIGITAL_MODULATION_TYPE\x10\xd4\x98F\x125\n/NIRFSG_ATTRIBUTE_DIGITAL_MODULATION_SYMBOL_RATE\x10\xd5\x98F\x127\n1NIRFSG_ATTRIBUTE_DIGITAL_MODULATION_WAVEFORM_TYPE\x10\xd6\x98F\x124\n.NIRFSG_ATTRIBUTE_DIGITAL_MODULATION_PRBS_ORDER\x10\xd7\x98F\x123\n-NIRFSG_ATTRIBUTE_DIGITAL_MODULATION_PRBS_SEED\x10\xd8\x98F\x127\n1NIRFSG_ATTRIBUTE_DIGITAL_MODULATION_FSK_DEVIATION\x10\xd9\x98F\x12&\n NIRFSG_ATTRIBUTE_DIRECT_DOWNLOAD\x10\xda\x98F\x12\'\n!NIRFSG_ATTRIBUTE_POWER_LEVEL_TYPE\x10\xdb\x98F\x12&\n NIRFSG_ATTRIBUTE_DIGITAL_PATTERN\x10\xdc\x98F\x12(\n"NIRFSG_ATTRIBUTE_STREAMING_ENABLED\x10\xdd\x98F\x12.\n(NIRFSG_ATTRIBUTE_STREAMING_WAVEFORM_NAME\x10\xde\x98F\x12<\n6NIRFSG_ATTRIBUTE_STREAMING_SPACE_AVAILABLE_IN_WAVEFORM\x10\xdf\x98F\x12/\n)NIRFSG_ATTRIBUTE_DATA_TRANSFER_BLOCK_SIZE\x10\xe0\x98F\x12;\n5NIRFSG_ATTRIBUTE_ARB_WAVEFORM_SOFTWARE_SCALING_FACTOR\x10\xe4\x98F\x129\n3NIRFSG_ATTRIBUTE_EXPORTED_REF_CLOCK_OUTPUT_TERMINAL\x10\xe5\x98F\x12:\n4NIRFSG_ATTRIBUTE_DIGITAL_LEVEL_SCRIPT_TRIGGER_SOURCE\x10\xe6\x98F\x12@\n:NIRFSG_ATTRIBUTE_DIGITAL_LEVEL_SCRIPT_TRIGGER_ACTIVE_LEVEL\x10\xe7\x98F\x12&\n NIRFSG_ATTRIBUTE_ARB_FILTER_TYPE\x10\xe8\x98F\x12:\n4NIRFSG_ATTRIBUTE_ARB_FILTER_ROOT_RAISED_COSINE_ALPHA\x10\xe9\x98F\x12=\n7NIRFSG_ATTRIBUTE_UPCONVERTER_CENTER_FREQUENCY_INCREMENT\x10\xea\x98F\x12D\n>NIRFSG_ATTRIBUTE_UPCONVERTER_CENTER_FREQUENCY_INCREMENT_ANCHOR\x10\xeb\x98F\x125\n/NIRFSG_ATTRIBUTE_ARB_FILTER_RAISED_COSINE_ALPHA\x10\xec\x98F\x12"\n\x1cNIRFSG_ATTRIBUTE_MEMORY_SIZE\x10\xed\x98F\x125\n/NIRFSG_ATTRIBUTE_ANALOG_MODULATION_PM_DEVIATION\x10\xee\x98F\x12:\n4NIRFSG_ATTRIBUTE_EXPORTED_DONE_EVENT_OUTPUT_TERMINAL\x10\xef\x98F\x12<\n6NIRFSG_ATTRIBUTE_EXPORTED_MARKER_EVENT_OUTPUT_TERMINAL\x10\xf0\x98F\x12=\n7NIRFSG_ATTRIBUTE_EXPORTED_STARTED_EVENT_OUTPUT_TERMINAL\x10\xf1\x98F\x12#\n\x1dNIRFSG_ATTRIBUTE_LO_OUT_POWER\x10\xf2\x98F\x12"\n\x1cNIRFSG_ATTRIBUTE_LO_IN_POWER\x10\xf3\x98F\x12&\n NIRFSG_ATTRIBUTE_ARB_TEMPERATURE\x10\xf4\x98F\x12,\n&NIRFSG_ATTRIBUTE_IQ_IMPAIRMENT_ENABLED\x10\xf5\x98F\x12"\n\x1cNIRFSG_ATTRIBUTE_IQ_I_OFFSET\x10\xf6\x98F\x12"\n\x1cNIRFSG_ATTRIBUTE_IQ_Q_OFFSET\x10\xf7\x98F\x12(\n"NIRFSG_ATTRIBUTE_IQ_GAIN_IMBALANCE\x10\xf8\x98F\x12\x1e\n\x18NIRFSG_ATTRIBUTE_IQ_SKEW\x10\xf9\x98F\x12%\n\x1fNIRFSG_ATTRIBUTE_LO_TEMPERATURE\x10\xfb\x98F\x12@\n:NIRFSG_ATTRIBUTE_EXTERNAL_CALIBRATION_RECOMMENDED_INTERVAL\x10\xfc\x98F\x127\n1NIRFSG_ATTRIBUTE_EXTERNAL_CALIBRATION_TEMPERATURE\x10\xfd\x98F\x12=\n7NIRFSG_ATTRIBUTE_EXTERNAL_CALIBRATION_USER_DEFINED_INFO\x10\xfe\x98F\x12F\n@NIRFSG_ATTRIBUTE_EXTERNAL_CALIBRATION_USER_DEFINED_INFO_MAX_SIZE\x10\xff\x98F\x12&\n NIRFSG_ATTRIBUTE_IQ_OFFSET_UNITS\x10\x81\x99F\x12/\n)NIRFSG_ATTRIBUTE_FREQUENCY_SETTLING_UNITS\x10\x82\x99F\x12)\n#NIRFSG_ATTRIBUTE_FREQUENCY_SETTLING\x10\x83\x99F\x12&\n NIRFSG_ATTRIBUTE_MODULE_REVISION\x10\x84\x99F\x12$\n\x1eNIRFSG_ATTRIBUTE_EXTERNAL_GAIN\x10\x85\x99F\x126\n0NIRFSG_ATTRIBUTE_DATA_TRANSFER_MAXIMUM_BANDWIDTH\x10\x86\x99F\x12:\n4NIRFSG_ATTRIBUTE_DATA_TRANSFER_PREFERRED_PACKET_SIZE\x10\x87\x99F\x12<\n6NIRFSG_ATTRIBUTE_DATA_TRANSFER_MAXIMUM_IN_FLIGHT_READS\x10\x88\x99F\x125\n/NIRFSG_ATTRIBUTE_ARB_OSCILLATOR_PHASE_DAC_VALUE\x10\x89\x99F\x120\n*NIRFSG_ATTRIBUTE_ACTIVE_CONFIGURATION_LIST\x10\x90\x99F\x125\n/NIRFSG_ATTRIBUTE_ACTIVE_CONFIGURATION_LIST_STEP\x10\x91\x99F\x12;\n5NIRFSG_ATTRIBUTE_CONFIGURATION_LIST_STEP_TRIGGER_TYPE\x10\x92\x99F\x12J\nDNIRFSG_ATTRIBUTE_DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE\x10\x93\x99F\x12+\n%NIRFSG_ATTRIBUTE_TIMER_EVENT_INTERVAL\x10\x94\x99F\x120\n*NIRFSG_ATTRIBUTE_CONFIGURATION_LIST_REPEAT\x10\x96\x99F\x12H\nBNIRFSG_ATTRIBUTE_DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_EDGE\x10\x97\x99F\x12-\n\'NIRFSG_ATTRIBUTE_CORRECTION_TEMPERATURE\x10\x98\x99F\x12O\nINIRFSG_ATTRIBUTE_EXPORTED_CONFIGURATION_LIST_STEP_TRIGGER_OUTPUT_TERMINAL\x10\x99\x99F\x122\n,NIRFSG_ATTRIBUTE_STARTED_EVENT_TERMINAL_NAME\x10\xa0\x99F\x12/\n)NIRFSG_ATTRIBUTE_DONE_EVENT_TERMINAL_NAME\x10\xa1\x99F\x122\n,NIRFSG_ATTRIBUTE_START_TRIGGER_TERMINAL_NAME\x10\xa2\x99F\x121\n+NIRFSG_ATTRIBUTE_MARKER_EVENT_TERMINAL_NAME\x10\xa3\x99F\x123\n-NIRFSG_ATTRIBUTE_SCRIPT_TRIGGER_TERMINAL_NAME\x10\xa4\x99F\x12D\n>NIRFSG_ATTRIBUTE_CONFIGURATION_LIST_STEP_TRIGGER_TERMINAL_NAME\x10\xa5\x99F\x12*\n$NIRFSG_ATTRIBUTE_YIG_MAIN_COIL_DRIVE\x10\xa6\x99F\x12:\n4NIRFSG_ATTRIBUTE_CONFIGURATION_LIST_STEP_IN_PROGRESS\x10\xaa\x99F\x12"\n\x1cNIRFSG_ATTRIBUTE_P2P_ENABLED\x10\xab\x99F\x12(\n"NIRFSG_ATTRIBUTE_P2P_ENDPOINT_SIZE\x10\xac\x99F\x126\n0NIRFSG_ATTRIBUTE_P2P_SPACE_AVAILABLE_IN_ENDPOINT\x10\xad\x99F\x12;\n5NIRFSG_ATTRIBUTE_P2P_MOST_SPACE_AVAILABLE_IN_ENDPOINT\x10\xae\x99F\x12)\n#NIRFSG_ATTRIBUTE_P2P_ENDPOINT_COUNT\x10\xaf\x99F\x12@\n:NIRFSG_ATTRIBUTE_P2P_ENDPOINT_FULLNESS_START_TRIGGER_LEVEL\x10\xb0\x99F\x12K\nENIRFSG_ATTRIBUTE_EXPORTED_CONFIGURATION_SETTLED_EVENT_OUTPUT_TERMINAL\x10\xb1\x99F\x12,\n&NIRFSG_ATTRIBUTE_PEAK_POWER_ADJUSTMENT\x10\xb4\x99F\x12(\n"NIRFSG_ATTRIBUTE_REF_PLL_BANDWIDTH\x10\xb5\x99F\x12<\n6NIRFSG_ATTRIBUTE_P2P_DATA_TRANSFER_PERMISSION_INTERVAL\x10\xb6\x99F\x12C\n=NIRFSG_ATTRIBUTE_P2P_DATA_TRANSFER_PERMISSION_INITIAL_CREDITS\x10\xb7\x99F\x123\n-NIRFSG_ATTRIBUTE_SELF_CALIBRATION_TEMPERATURE\x10\xb8\x99F\x12)\n#NIRFSG_ATTRIBUTE_AMPLITUDE_SETTLING\x10\xb9\x99F\x12.\n(NIRFSG_ATTRIBUTE_STREAMING_WRITE_TIMEOUT\x10\xbc\x99F\x128\n2NIRFSG_ATTRIBUTE_PEAK_POWER_ADJUSTMENT_INHERITANCE\x10\xbd\x99F\x121\n+NIRFSG_ATTRIBUTE_SYNC_SCRIPT_TRIGGER_MASTER\x10\xbe\x99F\x124\n.NIRFSG_ATTRIBUTE_SYNC_SCRIPT_TRIGGER_DIST_LINE\x10\xbf\x99F\x12"\n\x1cNIRFSG_ATTRIBUTE_OUTPUT_PORT\x10\xc0\x99F\x124\n.NIRFSG_ATTRIBUTE_IQ_OUT_PORT_CARRIER_FREQUENCY\x10\xc1\x99F\x129\n3NIRFSG_ATTRIBUTE_IQ_OUT_PORT_TERMINAL_CONFIGURATION\x10\xc2\x99F\x12(\n"NIRFSG_ATTRIBUTE_IQ_OUT_PORT_LEVEL\x10\xc3\x99F\x125\n/NIRFSG_ATTRIBUTE_IQ_OUT_PORT_COMMON_MODE_OFFSET\x10\xc4\x99F\x12)\n#NIRFSG_ATTRIBUTE_IQ_OUT_PORT_OFFSET\x10\xc5\x99F\x12 \n\x1aNIRFSG_ATTRIBUTE_LO_SOURCE\x10\xc6\x99F\x12-\n\'NIRFSG_ATTRIBUTE_LO_FREQUENCY_STEP_SIZE\x10\xc7\x99F\x125\n/NIRFSG_ATTRIBUTE_LO_PLL_FRACTIONAL_MODE_ENABLED\x10\xc8\x99F\x12*\n$NIRFSG_ATTRIBUTE_INTERPOLATION_DELAY\x10\xc9\x99F\x12#\n\x1dNIRFSG_ATTRIBUTE_EVENTS_DELAY\x10\xca\x99F\x120\n*NIRFSG_ATTRIBUTE_SYNC_START_TRIGGER_MASTER\x10\xcb\x99F\x123\n-NIRFSG_ATTRIBUTE_SYNC_START_TRIGGER_DIST_LINE\x10\xcc\x99F\x12:\n4NIRFSG_ATTRIBUTE_ARB_WAVEFORM_REPEAT_COUNT_IS_FINITE\x10\xcd\x99F\x120\n*NIRFSG_ATTRIBUTE_ARB_WAVEFORM_REPEAT_COUNT\x10\xce\x99F\x123\n-NIRFSG_ATTRIBUTE_UPCONVERTER_FREQUENCY_OFFSET\x10\xd0\x99F\x12.\n(NIRFSG_ATTRIBUTE_IQ_OUT_PORT_TEMPERATURE\x10\xd1\x99F\x12)\n#NIRFSG_ATTRIBUTE_RF_BLANKING_SOURCE\x10\xd2\x99F\x121\n+NIRFSG_ATTRIBUTE_IQ_OUT_PORT_LOAD_IMPEDANCE\x10\xd3\x99F\x12A\n;NIRFSG_ATTRIBUTE_ANALOG_MODULATION_FM_NARROWBAND_INTEGRATOR\x10\xd5\x99F\x127\n1NIRFSG_ATTRIBUTE_ANALOG_MODULATION_FM_SENSITIVITY\x10\xd6\x99F\x127\n1NIRFSG_ATTRIBUTE_ANALOG_MODULATION_AM_SENSITIVITY\x10\xd7\x99F\x127\n1NIRFSG_ATTRIBUTE_ANALOG_MODULATION_PM_SENSITIVITY\x10\xd8\x99F\x12)\n#NIRFSG_ATTRIBUTE_ATTENUATOR_SETTING\x10\xdd\x99F\x121\n+NIRFSG_ATTRIBUTE_CONFIGURATION_LIST_IS_DONE\x10\xdf\x99F\x12/\n)NIRFSG_ATTRIBUTE_SYNC_SAMPLE_CLOCK_MASTER\x10\xe4\x99F\x122\n,NIRFSG_ATTRIBUTE_SYNC_SAMPLE_CLOCK_DIST_LINE\x10\xe5\x99F\x12%\n\x1fNIRFSG_ATTRIBUTE_AE_TEMPERATURE\x10\xe6\x99F\x12\x1f\n\x19NIRFSG_ATTRIBUTE_AMP_PATH\x10\xe9\x99F\x12(\n"NIRFSG_ATTRIBUTE_FPGA_BITFILE_PATH\x10\xea\x99F\x12)\n#NIRFSG_ATTRIBUTE_FAST_TUNING_OPTION\x10\xec\x99F\x12,\n&NIRFSG_ATTRIBUTE_PULSE_MODULATION_MODE\x10\xee\x99F\x120\n*NIRFSG_ATTRIBUTE_ANALOG_MODULATION_FM_BAND\x10\xef\x99F\x120\n*NIRFSG_ATTRIBUTE_ANALOG_MODULATION_PM_MODE\x10\xf0\x99F\x12@\n:NIRFSG_ATTRIBUTE_CONFIGURATION_SETTLED_EVENT_TERMINAL_NAME\x10\xf2\x99F\x12"\n\x1cNIRFSG_ATTRIBUTE_ALC_CONTROL\x10\xf3\x99F\x12(\n"NIRFSG_ATTRIBUTE_AUTO_POWER_SEARCH\x10\xf4\x99F\x12#\n\x1dNIRFSG_ATTRIBUTE_LO_FREQUENCY\x10\xf7\x99F\x12\'\n!NIRFSG_ATTRIBUTE_ARB_DIGITAL_GAIN\x10\xfc\x99F\x123\n-NIRFSG_ATTRIBUTE_MARKER_EVENT_OUTPUT_BEHAVIOR\x10\xfe\x99F\x12/\n)NIRFSG_ATTRIBUTE_MARKER_EVENT_PULSE_WIDTH\x10\xff\x99F\x125\n/NIRFSG_ATTRIBUTE_MARKER_EVENT_PULSE_WIDTH_UNITS\x10\x80\x9aF\x128\n2NIRFSG_ATTRIBUTE_MARKER_EVENT_TOGGLE_INITIAL_STATE\x10\x81\x9aF\x12/\n)NIRFSG_ATTRIBUTE_MODULE_POWER_CONSUMPTION\x10\x82\x9aF\x12\'\n!NIRFSG_ATTRIBUTE_FPGA_TEMPERATURE\x10\x83\x9aF\x120\n*NIRFSG_ATTRIBUTE_TEMPERATURE_READ_INTERVAL\x10\x84\x9aF\x12/\n)NIRFSG_ATTRIBUTE_P2P_IS_FINITE_GENERATION\x10\x89\x9aF\x128\n2NIRFSG_ATTRIBUTE_P2P_NUMBER_OF_SAMPLES_TO_GENERATE\x10\x8a\x9aF\x129\n3NIRFSG_ATTRIBUTE_P2P_GENERATION_FIFO_SAMPLE_QUANTUM\x10\x8b\x9aF\x12%\n\x1fNIRFSG_ATTRIBUTE_RELATIVE_DELAY\x10\x8c\x9aF\x12%\n\x1fNIRFSG_ATTRIBUTE_ABSOLUTE_DELAY\x10\x91\x9aF\x125\n/NIRFSG_ATTRIBUTE_DEVICE_INSTANTANEOUS_BANDWIDTH\x10\x92\x9aF\x12/\n)NIRFSG_ATTRIBUTE_OVERFLOW_ERROR_REPORTING\x10\x94\x9aF\x12+\n%NIRFSG_ATTRIBUTE_HOST_DMA_BUFFER_SIZE\x10\x9f\x9aF\x12%\n\x1fNIRFSG_ATTRIBUTE_SELECTED_PORTS\x10\xa1\x9aF\x128\n2NIRFSG_ATTRIBUTE_LO_OUT_EXPORT_CONFIGURE_FROM_RFSA\x10\xa2\x9aF\x12.\n(NIRFSG_ATTRIBUTE_RF_IN_LO_EXPORT_ENABLED\x10\xa3\x9aF\x12@\n:NIRFSG_ATTRIBUTE_THERMAL_CORRECTION_TEMPERATURE_RESOLUTION\x10\xa4\x9aF\x128\n2NIRFSG_ATTRIBUTE_UPCONVERTER_FREQUENCY_OFFSET_MODE\x10\xa8\x9aF\x12&\n NIRFSG_ATTRIBUTE_AVAILABLE_PORTS\x10\xa9\x9aF\x12\'\n!NIRFSG_ATTRIBUTE_FPGA_TARGET_NAME\x10\xab\x9aF\x12\'\n!NIRFSG_ATTRIBUTE_DEEMBEDDING_TYPE\x10\xac\x9aF\x121\n+NIRFSG_ATTRIBUTE_DEEMBEDDING_SELECTED_TABLE\x10\xad\x9aF\x121\n+NIRFSG_ATTRIBUTE_LO_VCO_FREQUENCY_STEP_SIZE\x10\xb1\x9aF\x128\n2NIRFSG_ATTRIBUTE_THERMAL_CORRECTION_HEADROOM_RANGE\x10\xb2\x9aF\x12\'\n!NIRFSG_ATTRIBUTE_WAVEFORM_IQ_RATE\x10\xb7\x9aF\x120\n*NIRFSG_ATTRIBUTE_WAVEFORM_SIGNAL_BANDWIDTH\x10\xb8\x9aF\x12/\n)NIRFSG_ATTRIBUTE_WAVEFORM_RUNTIME_SCALING\x10\xb9\x9aF\x12$\n\x1eNIRFSG_ATTRIBUTE_WAVEFORM_PAPR\x10\xba\x9aF\x125\n/NIRFSG_ATTRIBUTE_FIXED_GROUP_DELAY_ACROSS_PORTS\x10\xbf\x9aF\x12(\n"NIRFSG_ATTRIBUTE_WAVEFORM_FILEPATH\x10\xc0\x9aF\x125\n/NIRFSG_ATTRIBUTE_WRITE_WAVEFORM_BURST_DETECTION\x10\xc1\x9aF\x12:\n4NIRFSG_ATTRIBUTE_WRITE_WAVEFORM_BURST_DETECTION_MODE\x10\xc2\x9aF\x12H\nBNIRFSG_ATTRIBUTE_WRITE_WAVEFORM_BURST_DETECTION_MINIMUM_QUIET_TIME\x10\xc3\x9aF\x12E\n?NIRFSG_ATTRIBUTE_WRITE_WAVEFORM_BURST_DETECTION_POWER_THRESHOLD\x10\xc4\x9aF\x12H\nBNIRFSG_ATTRIBUTE_WRITE_WAVEFORM_BURST_DETECTION_MINIMUM_BURST_TIME\x10\xc5\x9aF\x12+\n%NIRFSG_ATTRIBUTE_WAVEFORM_RF_BLANKING\x10\xc6\x9aF\x124\n.NIRFSG_ATTRIBUTE_DEEMBEDDING_COMPENSATION_GAIN\x10\xd1\x9aF\x12A\n;NIRFSG_ATTRIBUTE_LOAD_CONFIGURATIONS_FROM_FILE_LOAD_OPTIONS\x10\xd2\x9aF\x12B\n<NIRFSG_ATTRIBUTE_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS\x10\xd3\x9aF\x12.\n(NIRFSG_ATTRIBUTE_EXPORTED_REF_CLOCK_RATE\x10\xd4\x9aF\x123\n-NIRFSG_ATTRIBUTE_WRITE_WAVEFORM_NORMALIZATION\x10\xd5\x9aF\x12-\n\'NIRFSG_ATTRIBUTE_WAVEFORM_WAVEFORM_SIZE\x10\xd9\x9aF\x124\n.NIRFSG_ATTRIBUTE_PULSE_MODULATION_ACTIVE_LEVEL\x10\xe3\x9aF\x12.\n(NIRFSG_ATTRIBUTE_PULSE_MODULATION_SOURCE\x10\xe4\x9aF\x12F\n@NIRFSG_ATTRIBUTE_EXPORTED_PULSE_MODULATION_EVENT_OUTPUT_TERMINAL\x10\xe5\x9aF\x12C\n=NIRFSG_ATTRIBUTE_EXPORTED_PULSE_MODULATION_EVENT_ACTIVE_LEVEL\x10\xe6\x9aF\x12$\n\x1eNIRFSG_ATTRIBUTE_SELECTED_PATH\x10\xe7\x9aF\x12&\n NIRFSG_ATTRIBUTE_AVAILABLE_PATHS\x10\xe8\x9aF\x128\n2NIRFSG_ATTRIBUTE_COMPENSATE_FOR_FILTER_GROUP_DELAY\x10\xc0\xaeF\x12\'\n!NIRFSG_ATTRIBUTE_UPCONVERTER_GAIN\x10\xb1\xb8F\x123\n-NIRFSG_ATTRIBUTE_UPCONVERTER_CENTER_FREQUENCY\x10\xb2\xb8F\x12 \n\x1aNIRFSG_ATTRIBUTE_FREQUENCY\x10\xd1\xa5L\x12"\n\x1cNIRFSG_ATTRIBUTE_POWER_LEVEL\x10\xd2\xa5L\x12%\n\x1fNIRFSG_ATTRIBUTE_OUTPUT_ENABLED\x10\xd4\xa5L\x12/\n)NIRFSG_ATTRIBUTE_PULSE_MODULATION_ENABLED\x10\x83\xa6L\x12%\n\x1fNIRFSG_ATTRIBUTE_REF_CLOCK_RATE\x10\x92\xa8L\x12!\n\x1bNIRFSG_ATTRIBUTE_IQ_ENABLED\x10\xe1\xa8L\x12)\n#NIRFSG_ATTRIBUTE_IQ_NOMINAL_VOLTAGE\x10\xe2\xa8L\x12&\n NIRFSG_ATTRIBUTE_IQ_SWAP_ENABLED\x10\xe4\xa8L\x12,\n&NIRFSG_ATTRIBUTE_ARB_SELECTED_WAVEFORM\x10\x93\xa9L\x12\x1e\n\x18NIRFSG_ATTRIBUTE_IQ_RATE\x10\x94\xa9L\x12+\n%NIRFSG_ATTRIBUTE_ARB_FILTER_FREQUENCY\x10\x95\xa9L\x12/\n)NIRFSG_ATTRIBUTE_ARB_MAX_NUMBER_WAVEFORMS\x10\x96\xa9L\x12+\n%NIRFSG_ATTRIBUTE_ARB_WAVEFORM_QUANTUM\x10\x97\xa9L\x12,\n&NIRFSG_ATTRIBUTE_ARB_WAVEFORM_SIZE_MIN\x10\x98\xa9L\x12,\n&NIRFSG_ATTRIBUTE_ARB_WAVEFORM_SIZE_MAX\x10\x99\xa9L\x12)\n#NIRFSG_ATTRIBUTE_START_TRIGGER_TYPE\x10\x9a\xa9L\x126\n0NIRFSG_ATTRIBUTE_DIGITAL_EDGE_START_TRIGGER_EDGE\x10\x9b\xa9L*\xe8\n\n-DigitalEdgeConfigurationListStepTriggerSource\x12C\n?DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_UNSPECIFIED\x10\x00\x12<\n8DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PFI0\x10\x01\x12<\n8DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PFI1\x10\x02\x12<\n8DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PFI2\x10\x03\x12<\n8DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PFI3\x10\x04\x12A\n=DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PXI_TRIG0\x10\x05\x12A\n=DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PXI_TRIG1\x10\x06\x12A\n=DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PXI_TRIG2\x10\x07\x12A\n=DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PXI_TRIG3\x10\x08\x12A\n=DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PXI_TRIG4\x10\t\x12A\n=DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PXI_TRIG5\x10\n\x12A\n=DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PXI_TRIG6\x10\x0b\x12A\n=DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PXI_TRIG7\x10\x0c\x12@\n<DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_PXI_STAR\x10\r\x12E\nADIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_MARKER0_EVENT\x10\x0e\x12E\nADIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_MARKER1_EVENT\x10\x0f\x12E\nADIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_MARKER2_EVENT\x10\x10\x12E\nADIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_MARKER3_EVENT\x10\x11\x12C\n?DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_TIMER_EVENT\x10\x12\x12?\n;DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE_TRIG_IN\x10\x13*X\n\x0fDigitalEdgeEdge\x12!\n\x1dDIGITAL_EDGE_EDGE_RISING_EDGE\x10\x00\x12"\n\x1eDIGITAL_EDGE_EDGE_FALLING_EDGE\x10\x01*\xcc\x02\n"DigitalEdgeScriptTriggerIdentifier\x126\n2DIGITAL_EDGE_SCRIPT_TRIGGER_IDENTIFIER_UNSPECIFIED\x10\x00\x12:\n6DIGITAL_EDGE_SCRIPT_TRIGGER_IDENTIFIER_SCRIPT_TRIGGER0\x10\x01\x12:\n6DIGITAL_EDGE_SCRIPT_TRIGGER_IDENTIFIER_SCRIPT_TRIGGER1\x10\x02\x12:\n6DIGITAL_EDGE_SCRIPT_TRIGGER_IDENTIFIER_SCRIPT_TRIGGER2\x10\x03\x12:\n6DIGITAL_EDGE_SCRIPT_TRIGGER_IDENTIFIER_SCRIPT_TRIGGER3\x10\x04*\x9e\x01\n\x17DigitalLevelActiveLevel\x12*\n&DIGITAL_LEVEL_ACTIVE_LEVEL_UNSPECIFIED\x10\x00\x12+\n&DIGITAL_LEVEL_ACTIVE_LEVEL_ACTIVE_HIGH\x10\xa8F\x12*\n%DIGITAL_LEVEL_ACTIVE_LEVEL_ACTIVE_LOW\x10\xa9F*\x8a\x01\n\x0eGenerationMode\x12\x1f\n\x1bGENERATION_MODE_UNSPECIFIED\x10\x00\x12\x17\n\x12GENERATION_MODE_CW\x10\xe8\x07\x12!\n\x1cGENERATION_MODE_ARB_WAVEFORM\x10\xe9\x07\x12\x1b\n\x16GENERATION_MODE_SCRIPT\x10\xea\x07*\xef\x01\n\x19LinearInterpolationFormat\x12+\n\'LINEAR_INTERPOLATION_FORMAT_UNSPECIFIED\x10\x00\x124\n.LINEAR_INTERPOLATION_FORMAT_REAL_AND_IMAGINARY\x10\x90\xcb\x01\x125\n/LINEAR_INTERPOLATION_FORMAT_MAGNITUDE_AND_PHASE\x10\x91\xcb\x01\x128\n2LINEAR_INTERPOLATION_FORMAT_MAGNITUDE_DB_AND_PHASE\x10\x92\xcb\x01*]\n\x06Module\x12\x16\n\x12MODULE_UNSPECIFIED\x10\x00\x12\x1a\n\x15MODULE_PRIMARY_MODULE\x10\xc8e\x12\x0f\n\nMODULE_AWG\x10\xc9e\x12\x0e\n\tMODULE_LO\x10\xcae*\xe8\x03\n\x0cOutputSignal\x12\x1d\n\x19OUTPUT_SIGNAL_UNSPECIFIED\x10\x00\x12\x1f\n\x1bOUTPUT_SIGNAL_DO_NOT_EXPORT\x10\x01\x12\x16\n\x12OUTPUT_SIGNAL_PFI0\x10\x02\x12\x16\n\x12OUTPUT_SIGNAL_PFI1\x10\x03\x12\x16\n\x12OUTPUT_SIGNAL_PFI4\x10\x04\x12\x16\n\x12OUTPUT_SIGNAL_PFI5\x10\x05\x12\x1a\n\x16OUTPUT_SIGNAL_PXI_STAR\x10\x06\x12\x1b\n\x17OUTPUT_SIGNAL_PXI_TRIG0\x10\x07\x12\x1b\n\x17OUTPUT_SIGNAL_PXI_TRIG1\x10\x08\x12\x1b\n\x17OUTPUT_SIGNAL_PXI_TRIG2\x10\t\x12\x1b\n\x17OUTPUT_SIGNAL_PXI_TRIG3\x10\n\x12\x1b\n\x17OUTPUT_SIGNAL_PXI_TRIG4\x10\x0b\x12\x1b\n\x17OUTPUT_SIGNAL_PXI_TRIG5\x10\x0c\x12\x1b\n\x17OUTPUT_SIGNAL_PXI_TRIG6\x10\r\x12\x1a\n\x16OUTPUT_SIGNAL_REF_OUT2\x10\x0e\x12\x19\n\x15OUTPUT_SIGNAL_REF_OUT\x10\x0f\x12\x1a\n\x16OUTPUT_SIGNAL_TRIG_OUT\x10\x10*\x93\x01\n\x0fPXIChassisClk10\x12!\n\x1dPXI_CHASSIS_CLK10_UNSPECIFIED\x10\x00\x12\x1a\n\x16PXI_CHASSIS_CLK10_NONE\x10\x01\x12#\n\x1fPXI_CHASSIS_CLK10_ONBOARD_CLOCK\x10\x02\x12\x1c\n\x18PXI_CHASSIS_CLK10_REF_IN\x10\x03*y\n\x0ePowerLevelType\x12 \n\x1cPOWER_LEVEL_TYPE_UNSPECIFIED\x10\x00\x12#\n\x1ePOWER_LEVEL_TYPE_AVERAGE_POWER\x10\xd86\x12 \n\x1bPOWER_LEVEL_TYPE_PEAK_POWER\x10\xd96*\xf2\x01\n\x0eRefClockSource\x12 \n\x1cREF_CLOCK_SOURCE_UNSPECIFIED\x10\x00\x12"\n\x1eREF_CLOCK_SOURCE_ONBOARD_CLOCK\x10\x01\x12\x1b\n\x17REF_CLOCK_SOURCE_REF_IN\x10\x02\x12\x1c\n\x18REF_CLOCK_SOURCE_PXI_CLK\x10\x03\x12\x1b\n\x17REF_CLOCK_SOURCE_CLK_IN\x10\x04\x12\x1d\n\x19REF_CLOCK_SOURCE_REF_IN_2\x10\x05\x12#\n\x1fREF_CLOCK_SOURCE_PXI_CLK_MASTER\x10\x06*p\n\nRelativeTo\x12\x1b\n\x17RELATIVE_TO_UNSPECIFIED\x10\x00\x12"\n\x1dRELATIVE_TO_START_OF_WAVEFORM\x10\xc0>\x12!\n\x1cRELATIVE_TO_CURRENT_POSITION\x10\xc1>*\x8c\x02\n\x1bResetWithOptionsStepsToOmit\x12)\n%RESET_WITH_OPTIONS_STEPS_TO_OMIT_NONE\x10\x00\x12.\n*RESET_WITH_OPTIONS_STEPS_TO_OMIT_WAVEFORMS\x10\x01\x12,\n(RESET_WITH_OPTIONS_STEPS_TO_OMIT_SCRIPTS\x10\x02\x12+\n\'RESET_WITH_OPTIONS_STEPS_TO_OMIT_ROUTES\x10\x04\x127\n3RESET_WITH_OPTIONS_STEPS_TO_OMIT_DEEMBEDDING_TABLES\x10\x08*\xaf\x02\n\x0cRoutedSignal\x12\x1f\n\x1bROUTED_SIGNAL_START_TRIGGER\x10\x00\x121\n-ROUTED_SIGNAL_CONFIGURATION_LIST_STEP_TRIGGER\x10\x06\x12-\n)ROUTED_SIGNAL_CONFIGURATION_SETTLED_EVENT\x10\x07\x12\x1c\n\x18ROUTED_SIGNAL_DONE_EVENT\x10\x05\x12\x1e\n\x1aROUTED_SIGNAL_MARKER_EVENT\x10\x02\x12\x1b\n\x17ROUTED_SIGNAL_REF_CLOCK\x10\x03\x12 \n\x1cROUTED_SIGNAL_SCRIPT_TRIGGER\x10\x01\x12\x1f\n\x1bROUTED_SIGNAL_STARTED_EVENT\x10\x04*\xa2\x01\n\x15SParameterOrientation\x12\'\n#S_PARAMETER_ORIENTATION_UNSPECIFIED\x10\x00\x12/\n)S_PARAMETER_ORIENTATION_PORT1_TOWARDS_DUT\x10\xc0\xbb\x01\x12/\n)S_PARAMETER_ORIENTATION_PORT2_TOWARDS_DUT\x10\xc1\xbb\x01*\xf4\x02\n\x1dSelfCalibrateRangeStepsToOmit\x120\n,SELF_CALIBRATE_RANGE_STEPS_TO_OMIT_OMIT_NONE\x10\x00\x122\n.SELF_CALIBRATE_RANGE_STEPS_TO_OMIT_LO_SELF_CAL\x10\x01\x12;\n7SELF_CALIBRATE_RANGE_STEPS_TO_OMIT_POWER_LEVEL_ACCURACY\x10\x02\x128\n4SELF_CALIBRATE_RANGE_STEPS_TO_OMIT_RESIDUAL_LO_POWER\x10\x04\x128\n4SELF_CALIBRATE_RANGE_STEPS_TO_OMIT_IMAGE_SUPPRESSION\x10\x08\x12<\n8SELF_CALIBRATE_RANGE_STEPS_TO_OMIT_SYNTHESIZER_ALIGNMENT\x10\x10*\xe9\x02\n\x10SignalIdentifier\x12!\n\x1dSIGNAL_IDENTIFIER_UNSPECIFIED\x10\x00\x12\x1a\n\x16SIGNAL_IDENTIFIER_NONE\x10\x01\x12%\n!SIGNAL_IDENTIFIER_SCRIPT_TRIGGER0\x10\x02\x12%\n!SIGNAL_IDENTIFIER_SCRIPT_TRIGGER1\x10\x03\x12%\n!SIGNAL_IDENTIFIER_SCRIPT_TRIGGER2\x10\x04\x12%\n!SIGNAL_IDENTIFIER_SCRIPT_TRIGGER3\x10\x05\x12\x1d\n\x19SIGNAL_IDENTIFIER_MARKER0\x10\x06\x12\x1d\n\x19SIGNAL_IDENTIFIER_MARKER1\x10\x07\x12\x1d\n\x19SIGNAL_IDENTIFIER_MARKER2\x10\x08\x12\x1d\n\x19SIGNAL_IDENTIFIER_MARKER3\x10\t*\x90\x06\n\rTriggerSource\x12\x1e\n\x1aTRIGGER_SOURCE_UNSPECIFIED\x10\x00\x12\x17\n\x13TRIGGER_SOURCE_PFI0\x10\x01\x12\x17\n\x13TRIGGER_SOURCE_PFI1\x10\x02\x12\x17\n\x13TRIGGER_SOURCE_PFI2\x10\x03\x12\x17\n\x13TRIGGER_SOURCE_PFI3\x10\x04\x12\x1c\n\x18TRIGGER_SOURCE_PXI_TRIG0\x10\x05\x12\x1c\n\x18TRIGGER_SOURCE_PXI_TRIG1\x10\x06\x12\x1c\n\x18TRIGGER_SOURCE_PXI_TRIG2\x10\x07\x12\x1c\n\x18TRIGGER_SOURCE_PXI_TRIG3\x10\x08\x12\x1c\n\x18TRIGGER_SOURCE_PXI_TRIG4\x10\t\x12\x1c\n\x18TRIGGER_SOURCE_PXI_TRIG5\x10\n\x12\x1c\n\x18TRIGGER_SOURCE_PXI_TRIG6\x10\x0b\x12\x1c\n\x18TRIGGER_SOURCE_PXI_TRIG7\x10\x0c\x12\x1b\n\x17TRIGGER_SOURCE_PXI_STAR\x10\r\x12\x1e\n\x1aTRIGGER_SOURCE_PXIE_DSTARB\x10\x0e\x12%\n!TRIGGER_SOURCE_SYNC_START_TRIGGER\x10\x0f\x12&\n"TRIGGER_SOURCE_SYNC_SCRIPT_TRIGGER\x10\x10\x12\x1a\n\x16TRIGGER_SOURCE_TRIG_IN\x10\x11\x12\x1b\n\x17TRIGGER_SOURCE_PULSE_IN\x10\x12\x12\x17\n\x13TRIGGER_SOURCE_DIO0\x10\x13\x12\x17\n\x13TRIGGER_SOURCE_DIO1\x10\x14\x12\x17\n\x13TRIGGER_SOURCE_DIO2\x10\x15\x12\x17\n\x13TRIGGER_SOURCE_DIO3\x10\x16\x12\x17\n\x13TRIGGER_SOURCE_DIO4\x10\x17\x12\x17\n\x13TRIGGER_SOURCE_DIO5\x10\x18\x12\x17\n\x13TRIGGER_SOURCE_DIO6\x10\x19\x12\x17\n\x13TRIGGER_SOURCE_DIO7\x10\x1a*\x85)\n\x1aNiRFSGInt32AttributeValues\x12\x1c\n\x18NIRFSG_INT32_UNSPECIFIED\x10\x00\x12%\n NIRFSG_INT32_AMP_PATH_HIGH_POWER\x10\x80}\x12\'\n"NIRFSG_INT32_AMP_PATH_LOW_HARMONIC\x10\x81}\x127\n1NIRFSG_INT32_ANALOG_MODULATION_FM_BAND_NARROWBAND\x10\xe8\x84\x01\x125\n/NIRFSG_INT32_ANALOG_MODULATION_FM_BAND_WIDEBAND\x10\xe9\x84\x01\x12M\nGNIRFSG_INT32_ANALOG_MODULATION_FM_NARROWBAND_INTEGRATOR_100_HZ_TO_1_KHZ\x10\xd0\x8c\x01\x12M\nGNIRFSG_INT32_ANALOG_MODULATION_FM_NARROWBAND_INTEGRATOR_1_KHZ_TO_10_KHZ\x10\xd1\x8c\x01\x12O\nINIRFSG_INT32_ANALOG_MODULATION_FM_NARROWBAND_INTEGRATOR_10_KHZ_TO_100_KHZ\x10\xd2\x8c\x01\x12;\n5NIRFSG_INT32_ANALOG_MODULATION_PM_MODE_HIGH_DEVIATION\x10\xb8\x94\x01\x12<\n6NIRFSG_INT32_ANALOG_MODULATION_PM_MODE_LOW_PHASE_NOISE\x10\xb9\x94\x01\x12,\n(NIRFSG_INT32_ANALOG_MODULATION_TYPE_NONE\x10\x00\x12+\n&NIRFSG_INT32_ANALOG_MODULATION_TYPE_FM\x10\xd0\x0f\x12+\n&NIRFSG_INT32_ANALOG_MODULATION_TYPE_PM\x10\xd1\x0f\x12+\n&NIRFSG_INT32_ANALOG_MODULATION_TYPE_AM\x10\xd2\x0f\x126\n1NIRFSG_INT32_ANALOG_MODULATION_WAVEFORM_TYPE_SINE\x10\xb8\x17\x128\n3NIRFSG_INT32_ANALOG_MODULATION_WAVEFORM_TYPE_SQUARE\x10\xb9\x17\x12:\n5NIRFSG_INT32_ANALOG_MODULATION_WAVEFORM_TYPE_TRIANGLE\x10\xba\x17\x12&\n!NIRFSG_INT32_ARB_FILTER_TYPE_NONE\x10\x90N\x124\n/NIRFSG_INT32_ARB_FILTER_TYPE_ROOT_RAISED_COSINE\x10\x91N\x12/\n*NIRFSG_INT32_ARB_FILTER_TYPE_RAISED_COSINE\x10\x92N\x12?\n:NIRFSG_INT32_ARB_ONBOARD_SAMPLE_CLOCK_MODE_HIGH_RESOLUTION\x10\xf0.\x12;\n6NIRFSG_INT32_ARB_ONBOARD_SAMPLE_CLOCK_MODE_DIVIDE_DOWN\x10\xf1.\x12>\n:NIRFSG_INT32_CONFIG_LIST_TRIGGER_DIG_EDGE_EDGE_RISING_EDGE\x10\x00\x12O\nKNIRFSG_INT32_CONFIGURATION_LIST_REPEAT_CONFIGURATION_LIST_REPEAT_CONTINUOUS\x10\x00\x12K\nGNIRFSG_INT32_CONFIGURATION_LIST_REPEAT_CONFIGURATION_LIST_REPEAT_SINGLE\x10\x01\x12(\n"NIRFSG_INT32_DEEMBEDDING_TYPE_NONE\x10\xa8\xc3\x01\x12*\n$NIRFSG_INT32_DEEMBEDDING_TYPE_SCALAR\x10\xa9\xc3\x01\x12*\n$NIRFSG_INT32_DEEMBEDDING_TYPE_VECTOR\x10\xaa\xc3\x01\x12.\n*NIRFSG_INT32_DIGITAL_EDGE_EDGE_RISING_EDGE\x10\x00\x12/\n+NIRFSG_INT32_DIGITAL_EDGE_EDGE_FALLING_EDGE\x10\x01\x128\n3NIRFSG_INT32_DIGITAL_LEVEL_ACTIVE_LEVEL_ACTIVE_HIGH\x10\xa8F\x127\n2NIRFSG_INT32_DIGITAL_LEVEL_ACTIVE_LEVEL_ACTIVE_LOW\x10\xa9F\x12-\n)NIRFSG_INT32_DIGITAL_MODULATION_TYPE_NONE\x10\x00\x12-\n(NIRFSG_INT32_DIGITAL_MODULATION_TYPE_FSK\x10\xa0\x1f\x12-\n(NIRFSG_INT32_DIGITAL_MODULATION_TYPE_OOK\x10\xa1\x1f\x12-\n(NIRFSG_INT32_DIGITAL_MODULATION_TYPE_PSK\x10\xa2\x1f\x127\n2NIRFSG_INT32_DIGITAL_MODULATION_WAVEFORM_TYPE_PRBS\x10\x88\'\x12?\n:NIRFSG_INT32_DIGITAL_MODULATION_WAVEFORM_TYPE_USER_DEFINED\x10\x89\'\x12&\n"NIRFSG_INT32_ENABLE_VALUES_DISABLE\x10\x00\x12%\n!NIRFSG_INT32_ENABLE_VALUES_ENABLE\x10\x01\x12:\n5NIRFSG_INT32_FREQUENCY_SETTLING_UNITS_TIME_AFTER_LOCK\x10\xe0]\x128\n3NIRFSG_INT32_FREQUENCY_SETTLING_UNITS_TIME_AFTER_IO\x10\xe1]\x12.\n)NIRFSG_INT32_FREQUENCY_SETTLING_UNITS_PPM\x10\xe2]\x12$\n\x1fNIRFSG_INT32_GENERATION_MODE_CW\x10\xe8\x07\x12.\n)NIRFSG_INT32_GENERATION_MODE_ARB_WAVEFORM\x10\xe9\x07\x12(\n#NIRFSG_INT32_GENERATION_MODE_SCRIPT\x10\xea\x07\x12)\n$NIRFSG_INT32_IQ_OFFSET_UNITS_PERCENT\x10\xf8U\x12\'\n"NIRFSG_INT32_IQ_OFFSET_UNITS_VOLTS\x10\xf9U\x126\n1NIRFSG_INT32_IQ_OUT_PORT_TERM_CONFIG_DIFFERENTIAL\x10\x98u\x126\n1NIRFSG_INT32_IQ_OUT_PORT_TERM_CONFIG_SINGLE_ENDED\x10\x99u\x12,\n(NIRFSG_INT32_LIST_STEP_TRIGGER_TYPE_NONE\x10\x00\x124\n0NIRFSG_INT32_LIST_STEP_TRIGGER_TYPE_DIGITAL_EDGE\x10\x01\x12\'\n#NIRFSG_INT32_LOAD_OPTIONS_SKIP_NONE\x10\x00\x12,\n(NIRFSG_INT32_LOAD_OPTIONS_SKIP_WAVEFORMS\x10\x01\x12&\n"NIRFSG_INT32_LOOP_BANDWIDTH_NARROW\x10\x00\x12&\n"NIRFSG_INT32_LOOP_BANDWIDTH_MEDIUM\x10\x01\x12$\n NIRFSG_INT32_LOOP_BANDWIDTH_WIDE\x10\x02\x125\n/NIRFSG_INT32_MARKER_EVENT_OUTPUT_BEHAVIOR_PULSE\x10\xd8\xb3\x01\x126\n0NIRFSG_INT32_MARKER_EVENT_OUTPUT_BEHAVIOR_TOGGLE\x10\xd9\xb3\x01\x129\n3NIRFSG_INT32_MARKER_EVENT_PULSE_WIDTH_UNITS_SECONDS\x10\xf0\xab\x01\x12F\n@NIRFSG_INT32_MARKER_EVENT_PULSE_WIDTH_UNITS_SAMPLE_CLOCK_PERIODS\x10\xf1\xab\x01\x12@\n:NIRFSG_INT32_MARKER_EVENT_TOGGLE_INITIAL_STATE_DIGITAL_LOW\x10\x88\xa4\x01\x12A\n;NIRFSG_INT32_MARKER_EVENT_TOGGLE_INITIAL_STATE_DIGITAL_HIGH\x10\x89\xa4\x01\x12$\n\x1fNIRFSG_INT32_OUTPUT_PORT_RF_OUT\x10\xb0m\x12$\n\x1fNIRFSG_INT32_OUTPUT_PORT_IQ_OUT\x10\xb1m\x12%\n NIRFSG_INT32_OUTPUT_PORT_CAL_OUT\x10\xb2m\x12$\n\x1fNIRFSG_INT32_OUTPUT_PORT_I_ONLY\x10\xb3m\x122\n-NIRFSG_INT32_OVERFLOW_ERROR_REPORTING_WARNING\x10\x95\n\x123\n.NIRFSG_INT32_OVERFLOW_ERROR_REPORTING_DISABLED\x10\x96\n\x123\n/NIRFSG_INT32_PPA_SCRIPT_INHERITANCE_EXACT_MATCH\x10\x00\x12/\n+NIRFSG_INT32_PPA_SCRIPT_INHERITANCE_MINIMUM\x10\x01\x12/\n+NIRFSG_INT32_PPA_SCRIPT_INHERITANCE_MAXIMUM\x10\x02\x12)\n%NIRFSG_INT32_PHASE_CONTINUITY_DISABLE\x10\x00\x12/\n"NIRFSG_INT32_PHASE_CONTINUITY_AUTO\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12(\n$NIRFSG_INT32_PHASE_CONTINUITY_ENABLE\x10\x01\x120\n+NIRFSG_INT32_POWER_LEVEL_TYPE_AVERAGE_POWER\x10\xd86\x12-\n(NIRFSG_INT32_POWER_LEVEL_TYPE_PEAK_POWER\x10\xd96\x126\n0NIRFSG_INT32_PULSE_MODULATION_MODE_OPTIMAL_MATCH\x10\xa0\x9c\x01\x127\n1NIRFSG_INT32_PULSE_MODULATION_MODE_HIGH_ISOLATION\x10\xa1\x9c\x01\x12(\n$NIRFSG_INT32_RESET_OPTIONS_SKIP_NONE\x10\x00\x12-\n)NIRFSG_INT32_RESET_OPTIONS_SKIP_WAVEFORMS\x10\x01\x12+\n\'NIRFSG_INT32_RESET_OPTIONS_SKIP_SCRIPTS\x10\x02\x125\n1NIRFSG_INT32_RESET_OPTIONS_SKIP_DEEMBEDING_TABLES\x10\x08\x120\n,NIRFSG_INT32_RF_IN_LO_EXPORT_ENABLED_DISABLE\x10\x00\x12=\n0NIRFSG_INT32_RF_IN_LO_EXPORT_ENABLED_UNSPECIFIED\x10\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12/\n+NIRFSG_INT32_RF_IN_LO_EXPORT_ENABLED_ENABLE\x10\x01\x12)\n%NIRFSG_INT32_SCRIPT_TRIGGER_TYPE_NONE\x10\x00\x121\n-NIRFSG_INT32_SCRIPT_TRIGGER_TYPE_DIGITAL_EDGE\x10\x01\x123\n.NIRFSG_INT32_SCRIPT_TRIGGER_TYPE_DIGITAL_LEVEL\x10\xc0>\x12-\n)NIRFSG_INT32_SCRIPT_TRIGGER_TYPE_SOFTWARE\x10\x02\x12(\n$NIRFSG_INT32_START_TRIGGER_TYPE_NONE\x10\x00\x120\n,NIRFSG_INT32_START_TRIGGER_TYPE_DIGITAL_EDGE\x10\x01\x12,\n(NIRFSG_INT32_START_TRIGGER_TYPE_SOFTWARE\x10\x02\x12:\n6NIRFSG_INT32_START_TRIGGER_TYPE_P2_P_ENDPOINT_FULLNESS\x10\x03\x12@\n3NIRFSG_INT32_UPCONVERTER_FREQUENCY_OFFSET_MODE_AUTO\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x129\n5NIRFSG_INT32_UPCONVERTER_FREQUENCY_OFFSET_MODE_ENABLE\x10\x01\x12@\n;NIRFSG_INT32_UPCONVERTER_FREQUENCY_OFFSET_MODE_USER_DEFINED\x10\x89\'\x12;\n7NIRFSG_INT32_WRITE_WAVEFORM_BURST_DETECTION_MODE_MANUAL\x10\x00\x12B\n5NIRFSG_INT32_WRITE_WAVEFORM_BURST_DETECTION_MODE_AUTO\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12#\n\x1fNIRFSG_INT32_YIG_MAIN_COIL_SLOW\x10\x00\x12#\n\x1fNIRFSG_INT32_YIG_MAIN_COIL_FAST\x10\x01\x1a\x02\x10\x01*\x98\x01\n\x1bNiRFSGReal64AttributeValues\x12\x1d\n\x19NIRFSG_REAL64_UNSPECIFIED\x10\x00\x12*\n#NIRFSG_REAL64_REF_CLOCK_RATE_10_MHZ\x10\x80\xad\xe2\x04\x12.\n!NIRFSG_REAL64_REF_CLOCK_RATE_AUTO\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01*\xd00\n!NiRFSGStringAttributeValuesMapped\x12$\n NIRFSG_STRING_MAPPED_UNSPECIFIED\x10\x00\x126\n2NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_DO_NOT_EXPORT\x10\x01\x12-\n)NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PFI0\x10\x02\x12-\n)NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PFI1\x10\x03\x12-\n)NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PFI4\x10\x04\x12-\n)NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PFI5\x10\x05\x122\n.NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PXI_TRIG0\x10\x06\x122\n.NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PXI_TRIG1\x10\x07\x122\n.NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PXI_TRIG2\x10\x08\x122\n.NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PXI_TRIG3\x10\t\x122\n.NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PXI_TRIG4\x10\n\x122\n.NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PXI_TRIG5\x10\x0b\x122\n.NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PXI_TRIG6\x10\x0c\x124\n0NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_PXIE_DSTARC\x10\r\x121\n-NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_TRIG_OUT\x10\x0e\x127\n3NIRFSG_STRING_ARB_SAMPLE_CLOCK_SOURCE_ONBOARD_CLOCK\x10\x0f\x120\n,NIRFSG_STRING_ARB_SAMPLE_CLOCK_SOURCE_CLK_IN\x10\x10\x12<\n8NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_DO_NOT_EXPORT\x10\x11\x123\n/NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_PFI0\x10\x12\x123\n/NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_PFI1\x10\x13\x128\n4NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_PXI_TRIG0\x10\x14\x128\n4NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_PXI_TRIG1\x10\x15\x128\n4NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_PXI_TRIG2\x10\x16\x128\n4NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_PXI_TRIG3\x10\x17\x128\n4NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_PXI_TRIG4\x10\x18\x128\n4NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_PXI_TRIG5\x10\x19\x128\n4NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_PXI_TRIG6\x10\x1a\x12:\n6NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_PXIE_DSTARC\x10\x1b\x127\n3NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_TRIG_OUT\x10\x1c\x12.\n*NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_PFI0\x10\x1d\x12.\n*NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_PFI1\x10\x1e\x123\n/NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_PXI_TRIG0\x10\x1f\x123\n/NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_PXI_TRIG1\x10 \x123\n/NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_PXI_TRIG2\x10!\x123\n/NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_PXI_TRIG3\x10"\x123\n/NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_PXI_TRIG4\x10#\x123\n/NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_PXI_TRIG5\x10$\x123\n/NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_PXI_TRIG6\x10%\x123\n/NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_PXI_TRIG7\x10&\x125\n1NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_PXIE_DSTARB\x10\'\x127\n3NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_MARKER0_EVENT\x10(\x127\n3NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_MARKER1_EVENT\x10)\x127\n3NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_MARKER2_EVENT\x10*\x127\n3NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_MARKER3_EVENT\x10+\x125\n1NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_TIMER_EVENT\x10,\x121\n-NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_TRIG_IN\x10-\x12@\n<NIRFSG_STRING_CONFIG_SETTLED_EVENT_OUTPUT_TERM_DO_NOT_EXPORT\x10.\x12<\n8NIRFSG_STRING_CONFIG_SETTLED_EVENT_OUTPUT_TERM_PXI_TRIG0\x10/\x12<\n8NIRFSG_STRING_CONFIG_SETTLED_EVENT_OUTPUT_TERM_PXI_TRIG1\x100\x12<\n8NIRFSG_STRING_CONFIG_SETTLED_EVENT_OUTPUT_TERM_PXI_TRIG2\x101\x12<\n8NIRFSG_STRING_CONFIG_SETTLED_EVENT_OUTPUT_TERM_PXI_TRIG3\x102\x12<\n8NIRFSG_STRING_CONFIG_SETTLED_EVENT_OUTPUT_TERM_PXI_TRIG4\x103\x12<\n8NIRFSG_STRING_CONFIG_SETTLED_EVENT_OUTPUT_TERM_PXI_TRIG5\x104\x12<\n8NIRFSG_STRING_CONFIG_SETTLED_EVENT_OUTPUT_TERM_PXI_TRIG6\x105\x12>\n:NIRFSG_STRING_CONFIG_SETTLED_EVENT_OUTPUT_TERM_PXIE_DSTARC\x106\x12;\n7NIRFSG_STRING_CONFIG_SETTLED_EVENT_OUTPUT_TERM_TRIG_OUT\x107\x12#\n\x1fNIRFSG_STRING_LO_SOURCE_ONBOARD\x108\x12!\n\x1dNIRFSG_STRING_LO_SOURCE_LO_IN\x109\x12%\n!NIRFSG_STRING_LO_SOURCE_SECONDARY\x10:\x12(\n$NIRFSG_STRING_LO_SOURCE_SG_SA_SHARED\x10;\x122\n.NIRFSG_STRING_LO_SOURCE_AUTOMATIC_SG_SA_SHARED\x10<\x12(\n$NIRFSG_STRING_PXI_CHASSIS_CLK10_NONE\x10=\x121\n-NIRFSG_STRING_PXI_CHASSIS_CLK10_ONBOARD_CLOCK\x10>\x12*\n&NIRFSG_STRING_PXI_CHASSIS_CLK10_REF_IN\x10?\x125\n1NIRFSG_STRING_REF_CLOCK_OUTPUT_TERM_DO_NOT_EXPORT\x10@\x12/\n+NIRFSG_STRING_REF_CLOCK_OUTPUT_TERM_REF_OUT\x10A\x120\n,NIRFSG_STRING_REF_CLOCK_OUTPUT_TERM_REF_OUT2\x10B\x12/\n+NIRFSG_STRING_REF_CLOCK_OUTPUT_TERM_CLK_OUT\x10C\x120\n,NIRFSG_STRING_REF_CLOCK_SOURCE_ONBOARD_CLOCK\x10D\x12)\n%NIRFSG_STRING_REF_CLOCK_SOURCE_REF_IN\x10E\x12*\n&NIRFSG_STRING_REF_CLOCK_SOURCE_PXI_CLK\x10F\x12)\n%NIRFSG_STRING_REF_CLOCK_SOURCE_CLK_IN\x10G\x12+\n\'NIRFSG_STRING_REF_CLOCK_SOURCE_REF_IN_2\x10H\x121\n-NIRFSG_STRING_REF_CLOCK_SOURCE_PXI_CLK_MASTER\x10I\x12%\n!NIRFSG_STRING_TRIGGER_SOURCE_PFI0\x10J\x12%\n!NIRFSG_STRING_TRIGGER_SOURCE_PFI1\x10K\x12%\n!NIRFSG_STRING_TRIGGER_SOURCE_PFI2\x10L\x12%\n!NIRFSG_STRING_TRIGGER_SOURCE_PFI3\x10M\x12*\n&NIRFSG_STRING_TRIGGER_SOURCE_PXI_TRIG0\x10N\x12*\n&NIRFSG_STRING_TRIGGER_SOURCE_PXI_TRIG1\x10O\x12*\n&NIRFSG_STRING_TRIGGER_SOURCE_PXI_TRIG2\x10P\x12*\n&NIRFSG_STRING_TRIGGER_SOURCE_PXI_TRIG3\x10Q\x12*\n&NIRFSG_STRING_TRIGGER_SOURCE_PXI_TRIG4\x10R\x12*\n&NIRFSG_STRING_TRIGGER_SOURCE_PXI_TRIG5\x10S\x12*\n&NIRFSG_STRING_TRIGGER_SOURCE_PXI_TRIG6\x10T\x12*\n&NIRFSG_STRING_TRIGGER_SOURCE_PXI_TRIG7\x10U\x12)\n%NIRFSG_STRING_TRIGGER_SOURCE_PXI_STAR\x10V\x12,\n(NIRFSG_STRING_TRIGGER_SOURCE_PXIE_DSTARB\x10W\x123\n/NIRFSG_STRING_TRIGGER_SOURCE_SYNC_START_TRIGGER\x10X\x124\n0NIRFSG_STRING_TRIGGER_SOURCE_SYNC_SCRIPT_TRIGGER\x10Y\x12(\n$NIRFSG_STRING_TRIGGER_SOURCE_TRIG_IN\x10Z\x12-\n)NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_DIO0\x10[\x12-\n)NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_DIO1\x10\\\x12-\n)NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_DIO2\x10]\x12-\n)NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_DIO3\x10^\x12-\n)NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_DIO4\x10_\x12-\n)NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_DIO5\x10`\x12-\n)NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_DIO6\x10a\x12-\n)NIRFSG_STRING_ANY_SIGNAL_OUTPUT_TERM_DIO7\x10b\x123\n/NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_DIO0\x10c\x123\n/NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_DIO1\x10d\x123\n/NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_DIO2\x10e\x123\n/NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_DIO3\x10f\x123\n/NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_DIO4\x10g\x123\n/NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_DIO5\x10h\x123\n/NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_DIO6\x10i\x123\n/NIRFSG_STRING_CONFIG_LIST_TRIG_OUTPUT_TERM_DIO7\x10j\x12.\n*NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_DIO0\x10k\x12.\n*NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_DIO1\x10l\x12.\n*NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_DIO2\x10m\x12.\n*NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_DIO3\x10n\x12.\n*NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_DIO4\x10o\x12.\n*NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_DIO5\x10p\x12.\n*NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_DIO6\x10q\x12.\n*NIRFSG_STRING_CONFIG_LIST_TRIG_SOURCE_DIO7\x10r\x12)\n%NIRFSG_STRING_TRIGGER_SOURCE_PULSE_IN\x10s\x12%\n!NIRFSG_STRING_TRIGGER_SOURCE_DIO0\x10t\x12%\n!NIRFSG_STRING_TRIGGER_SOURCE_DIO1\x10u\x12%\n!NIRFSG_STRING_TRIGGER_SOURCE_DIO2\x10v\x12%\n!NIRFSG_STRING_TRIGGER_SOURCE_DIO3\x10w\x12%\n!NIRFSG_STRING_TRIGGER_SOURCE_DIO4\x10x\x12%\n!NIRFSG_STRING_TRIGGER_SOURCE_DIO5\x10y\x12%\n!NIRFSG_STRING_TRIGGER_SOURCE_DIO6\x10z\x12%\n!NIRFSG_STRING_TRIGGER_SOURCE_DIO7\x10{2\xafe\n\x06NiRFSG\x12>\n\x05Abort\x12\x19.nirfsg_grpc.AbortRequest\x1a\x1a.nirfsg_grpc.AbortResponse\x12h\n\x13AllocateArbWaveform\x12\'.nirfsg_grpc.AllocateArbWaveformRequest\x1a(.nirfsg_grpc.AllocateArbWaveformResponse\x12t\n\x17CheckAttributeViBoolean\x12+.nirfsg_grpc.CheckAttributeViBooleanRequest\x1a,.nirfsg_grpc.CheckAttributeViBooleanResponse\x12n\n\x15CheckAttributeViInt32\x12).nirfsg_grpc.CheckAttributeViInt32Request\x1a*.nirfsg_grpc.CheckAttributeViInt32Response\x12n\n\x15CheckAttributeViInt64\x12).nirfsg_grpc.CheckAttributeViInt64Request\x1a*.nirfsg_grpc.CheckAttributeViInt64Response\x12q\n\x16CheckAttributeViReal64\x12*.nirfsg_grpc.CheckAttributeViReal64Request\x1a+.nirfsg_grpc.CheckAttributeViReal64Response\x12t\n\x17CheckAttributeViSession\x12+.nirfsg_grpc.CheckAttributeViSessionRequest\x1a,.nirfsg_grpc.CheckAttributeViSessionResponse\x12q\n\x16CheckAttributeViString\x12*.nirfsg_grpc.CheckAttributeViStringRequest\x1a+.nirfsg_grpc.CheckAttributeViStringResponse\x12n\n\x15CheckGenerationStatus\x12).nirfsg_grpc.CheckGenerationStatusRequest\x1a*.nirfsg_grpc.CheckGenerationStatusResponse\x12\x89\x01\n\x1eCheckIfConfigurationListExists\x122.nirfsg_grpc.CheckIfConfigurationListExistsRequest\x1a3.nirfsg_grpc.CheckIfConfigurationListExistsResponse\x12h\n\x13CheckIfScriptExists\x12\'.nirfsg_grpc.CheckIfScriptExistsRequest\x1a(.nirfsg_grpc.CheckIfScriptExistsResponse\x12n\n\x15CheckIfWaveformExists\x12).nirfsg_grpc.CheckIfWaveformExistsRequest\x1a*.nirfsg_grpc.CheckIfWaveformExistsResponse\x12k\n\x14ClearAllArbWaveforms\x12(.nirfsg_grpc.ClearAllArbWaveformsRequest\x1a).nirfsg_grpc.ClearAllArbWaveformsResponse\x12_\n\x10ClearArbWaveform\x12$.nirfsg_grpc.ClearArbWaveformRequest\x1a%.nirfsg_grpc.ClearArbWaveformResponse\x12M\n\nClearError\x12\x1e.nirfsg_grpc.ClearErrorRequest\x1a\x1f.nirfsg_grpc.ClearErrorResponse\x12t\n\x17ClearSelfCalibrateRange\x12+.nirfsg_grpc.ClearSelfCalibrateRangeRequest\x1a,.nirfsg_grpc.ClearSelfCalibrateRangeResponse\x12>\n\x05Close\x12\x19.nirfsg_grpc.CloseRequest\x1a\x1a.nirfsg_grpc.CloseResponse\x12A\n\x06Commit\x12\x1a.nirfsg_grpc.CommitRequest\x1a\x1b.nirfsg_grpc.CommitResponse\x12\xb3\x01\n,ConfigureDeembeddingTableInterpolationLinear\x12@.nirfsg_grpc.ConfigureDeembeddingTableInterpolationLinearRequest\x1aA.nirfsg_grpc.ConfigureDeembeddingTableInterpolationLinearResponse\x12\xb6\x01\n-ConfigureDeembeddingTableInterpolationNearest\x12A.nirfsg_grpc.ConfigureDeembeddingTableInterpolationNearestRequest\x1aB.nirfsg_grpc.ConfigureDeembeddingTableInterpolationNearestResponse\x12\xb3\x01\n,ConfigureDeembeddingTableInterpolationSpline\x12@.nirfsg_grpc.ConfigureDeembeddingTableInterpolationSplineRequest\x1aA.nirfsg_grpc.ConfigureDeembeddingTableInterpolationSplineResponse\x12\xbf\x01\n0ConfigureDigitalEdgeConfigurationListStepTrigger\x12D.nirfsg_grpc.ConfigureDigitalEdgeConfigurationListStepTriggerRequest\x1aE.nirfsg_grpc.ConfigureDigitalEdgeConfigurationListStepTriggerResponse\x12\x92\x01\n!ConfigureDigitalEdgeScriptTrigger\x125.nirfsg_grpc.ConfigureDigitalEdgeScriptTriggerRequest\x1a6.nirfsg_grpc.ConfigureDigitalEdgeScriptTriggerResponse\x12\x8f\x01\n ConfigureDigitalEdgeStartTrigger\x124.nirfsg_grpc.ConfigureDigitalEdgeStartTriggerRequest\x1a5.nirfsg_grpc.ConfigureDigitalEdgeStartTriggerResponse\x12\x95\x01\n"ConfigureDigitalLevelScriptTrigger\x126.nirfsg_grpc.ConfigureDigitalLevelScriptTriggerRequest\x1a7.nirfsg_grpc.ConfigureDigitalLevelScriptTriggerResponse\x12\xb6\x01\n-ConfigureDigitalModulationUserDefinedWaveform\x12A.nirfsg_grpc.ConfigureDigitalModulationUserDefinedWaveformRequest\x1aB.nirfsg_grpc.ConfigureDigitalModulationUserDefinedWaveformResponse\x12t\n\x17ConfigureGenerationMode\x12+.nirfsg_grpc.ConfigureGenerationModeRequest\x1a,.nirfsg_grpc.ConfigureGenerationModeResponse\x12q\n\x16ConfigureOutputEnabled\x12*.nirfsg_grpc.ConfigureOutputEnabledRequest\x1a+.nirfsg_grpc.ConfigureOutputEnabledResponse\x12\xa7\x01\n(ConfigureP2PEndpointFullnessStartTrigger\x12<.nirfsg_grpc.ConfigureP2PEndpointFullnessStartTriggerRequest\x1a=.nirfsg_grpc.ConfigureP2PEndpointFullnessStartTriggerResponse\x12w\n\x18ConfigurePXIChassisClk10\x12,.nirfsg_grpc.ConfigurePXIChassisClk10Request\x1a-.nirfsg_grpc.ConfigurePXIChassisClk10Response\x12t\n\x17ConfigurePowerLevelType\x12+.nirfsg_grpc.ConfigurePowerLevelTypeRequest\x1a,.nirfsg_grpc.ConfigurePowerLevelTypeResponse\x12P\n\x0bConfigureRF\x12\x1f.nirfsg_grpc.ConfigureRFRequest\x1a .nirfsg_grpc.ConfigureRFResponse\x12b\n\x11ConfigureRefClock\x12%.nirfsg_grpc.ConfigureRefClockRequest\x1a&.nirfsg_grpc.ConfigureRefClockResponse\x12w\n\x18ConfigureSignalBandwidth\x12,.nirfsg_grpc.ConfigureSignalBandwidthRequest\x1a-.nirfsg_grpc.ConfigureSignalBandwidthResponse\x12\x89\x01\n\x1eConfigureSoftwareScriptTrigger\x122.nirfsg_grpc.ConfigureSoftwareScriptTriggerRequest\x1a3.nirfsg_grpc.ConfigureSoftwareScriptTriggerResponse\x12\x86\x01\n\x1dConfigureSoftwareStartTrigger\x121.nirfsg_grpc.ConfigureSoftwareStartTriggerRequest\x1a2.nirfsg_grpc.ConfigureSoftwareStartTriggerResponse\x12\x98\x01\n#ConfigureUpconverterPLLSettlingTime\x127.nirfsg_grpc.ConfigureUpconverterPLLSettlingTimeRequest\x1a8.nirfsg_grpc.ConfigureUpconverterPLLSettlingTimeResponse\x12t\n\x17CreateConfigurationList\x12+.nirfsg_grpc.CreateConfigurationListRequest\x1a,.nirfsg_grpc.CreateConfigurationListResponse\x12\x80\x01\n\x1bCreateConfigurationListStep\x12/.nirfsg_grpc.CreateConfigurationListStepRequest\x1a0.nirfsg_grpc.CreateConfigurationListStepResponse\x12\x9e\x01\n%CreateDeembeddingSparameterTableArray\x129.nirfsg_grpc.CreateDeembeddingSparameterTableArrayRequest\x1a:.nirfsg_grpc.CreateDeembeddingSparameterTableArrayResponse\x12\xa4\x01\n\'CreateDeembeddingSparameterTableS2PFile\x12;.nirfsg_grpc.CreateDeembeddingSparameterTableS2PFileRequest\x1a<.nirfsg_grpc.CreateDeembeddingSparameterTableS2PFileResponse\x12}\n\x1aDeleteAllDeembeddingTables\x12..nirfsg_grpc.DeleteAllDeembeddingTablesRequest\x1a/.nirfsg_grpc.DeleteAllDeembeddingTablesResponse\x12t\n\x17DeleteConfigurationList\x12+.nirfsg_grpc.DeleteConfigurationListRequest\x1a,.nirfsg_grpc.DeleteConfigurationListResponse\x12q\n\x16DeleteDeembeddingTable\x12*.nirfsg_grpc.DeleteDeembeddingTableRequest\x1a+.nirfsg_grpc.DeleteDeembeddingTableResponse\x12S\n\x0cDeleteScript\x12 .nirfsg_grpc.DeleteScriptRequest\x1a!.nirfsg_grpc.DeleteScriptResponse\x12D\n\x07Disable\x12\x1b.nirfsg_grpc.DisableRequest\x1a\x1c.nirfsg_grpc.DisableResponse\x12k\n\x14DisableAllModulation\x12(.nirfsg_grpc.DisableAllModulationRequest\x1a).nirfsg_grpc.DisableAllModulationResponse\x12\x98\x01\n#DisableConfigurationListStepTrigger\x127.nirfsg_grpc.DisableConfigurationListStepTriggerRequest\x1a8.nirfsg_grpc.DisableConfigurationListStepTriggerResponse\x12k\n\x14DisableScriptTrigger\x12(.nirfsg_grpc.DisableScriptTriggerRequest\x1a).nirfsg_grpc.DisableScriptTriggerResponse\x12h\n\x13DisableStartTrigger\x12\'.nirfsg_grpc.DisableStartTriggerRequest\x1a(.nirfsg_grpc.DisableStartTriggerResponse\x12S\n\x0cErrorMessage\x12 .nirfsg_grpc.ErrorMessageRequest\x1a!.nirfsg_grpc.ErrorMessageResponse\x12M\n\nErrorQuery\x12\x1e.nirfsg_grpc.ErrorQueryRequest\x1a\x1f.nirfsg_grpc.ErrorQueryResponse\x12S\n\x0cExportSignal\x12 .nirfsg_grpc.ExportSignalRequest\x1a!.nirfsg_grpc.ExportSignalResponse\x12w\n\x18GetAllNamedWaveformNames\x12,.nirfsg_grpc.GetAllNamedWaveformNamesRequest\x1a-.nirfsg_grpc.GetAllNamedWaveformNamesResponse\x12b\n\x11GetAllScriptNames\x12%.nirfsg_grpc.GetAllScriptNamesRequest\x1a&.nirfsg_grpc.GetAllScriptNamesResponse\x12J\n\tGetScript\x12\x1d.nirfsg_grpc.GetScriptRequest\x1a\x1e.nirfsg_grpc.GetScriptResponse\x12n\n\x15GetAttributeViBoolean\x12).nirfsg_grpc.GetAttributeViBooleanRequest\x1a*.nirfsg_grpc.GetAttributeViBooleanResponse\x12h\n\x13GetAttributeViInt32\x12\'.nirfsg_grpc.GetAttributeViInt32Request\x1a(.nirfsg_grpc.GetAttributeViInt32Response\x12h\n\x13GetAttributeViInt64\x12\'.nirfsg_grpc.GetAttributeViInt64Request\x1a(.nirfsg_grpc.GetAttributeViInt64Response\x12k\n\x14GetAttributeViReal64\x12(.nirfsg_grpc.GetAttributeViReal64Request\x1a).nirfsg_grpc.GetAttributeViReal64Response\x12n\n\x15GetAttributeViSession\x12).nirfsg_grpc.GetAttributeViSessionRequest\x1a*.nirfsg_grpc.GetAttributeViSessionResponse\x12k\n\x14GetAttributeViString\x12(.nirfsg_grpc.GetAttributeViStringRequest\x1a).nirfsg_grpc.GetAttributeViStringResponse\x12Y\n\x0eGetChannelName\x12".nirfsg_grpc.GetChannelNameRequest\x1a#.nirfsg_grpc.GetChannelNameResponse\x12z\n\x19GetDeembeddingSparameters\x12-.nirfsg_grpc.GetDeembeddingSparametersRequest\x1a..nirfsg_grpc.GetDeembeddingSparametersResponse\x12G\n\x08GetError\x12\x1c.nirfsg_grpc.GetErrorRequest\x1a\x1d.nirfsg_grpc.GetErrorResponse\x12\x9e\x01\n%GetExternalCalibrationLastDateAndTime\x129.nirfsg_grpc.GetExternalCalibrationLastDateAndTimeRequest\x1a:.nirfsg_grpc.GetExternalCalibrationLastDateAndTimeResponse\x12h\n\x13GetMaxSettablePower\x12\'.nirfsg_grpc.GetMaxSettablePowerRequest\x1a(.nirfsg_grpc.GetMaxSettablePowerResponse\x12\x86\x01\n\x1dGetSelfCalibrationDateAndTime\x121.nirfsg_grpc.GetSelfCalibrationDateAndTimeRequest\x1a2.nirfsg_grpc.GetSelfCalibrationDateAndTimeResponse\x12\x86\x01\n\x1dGetSelfCalibrationTemperature\x121.nirfsg_grpc.GetSelfCalibrationTemperatureRequest\x1a2.nirfsg_grpc.GetSelfCalibrationTemperatureResponse\x12\\\n\x0fGetTerminalName\x12#.nirfsg_grpc.GetTerminalNameRequest\x1a$.nirfsg_grpc.GetTerminalNameResponse\x12P\n\x0bGetUserData\x12\x1f.nirfsg_grpc.GetUserDataRequest\x1a .nirfsg_grpc.GetUserDataResponse\x12\x89\x01\n\x1eGetWaveformBurstStartLocations\x122.nirfsg_grpc.GetWaveformBurstStartLocationsRequest\x1a3.nirfsg_grpc.GetWaveformBurstStartLocationsResponse\x12\x86\x01\n\x1dGetWaveformBurstStopLocations\x121.nirfsg_grpc.GetWaveformBurstStopLocationsRequest\x1a2.nirfsg_grpc.GetWaveformBurstStopLocationsResponse\x12\x8c\x01\n\x1fGetWaveformMarkerEventLocations\x123.nirfsg_grpc.GetWaveformMarkerEventLocationsRequest\x1a4.nirfsg_grpc.GetWaveformMarkerEventLocationsResponse\x12;\n\x04Init\x12\x18.nirfsg_grpc.InitRequest\x1a\x19.nirfsg_grpc.InitResponse\x12\\\n\x0fInitWithOptions\x12#.nirfsg_grpc.InitWithOptionsRequest\x1a$.nirfsg_grpc.InitWithOptionsResponse\x12G\n\x08Initiate\x12\x1c.nirfsg_grpc.InitiateRequest\x1a\x1d.nirfsg_grpc.InitiateResponse\x12t\n\x17InvalidateAllAttributes\x12+.nirfsg_grpc.InvalidateAllAttributesRequest\x1a,.nirfsg_grpc.InvalidateAllAttributesResponse\x12}\n\x1aLoadConfigurationsFromFile\x12..nirfsg_grpc.LoadConfigurationsFromFileRequest\x1a/.nirfsg_grpc.LoadConfigurationsFromFileResponse\x12e\n\x12PerformPowerSearch\x12&.nirfsg_grpc.PerformPowerSearchRequest\x1a\'.nirfsg_grpc.PerformPowerSearchResponse\x12w\n\x18PerformThermalCorrection\x12,.nirfsg_grpc.PerformThermalCorrectionRequest\x1a-.nirfsg_grpc.PerformThermalCorrectionResponse\x12\x83\x01\n\x1cQueryArbWaveformCapabilities\x120.nirfsg_grpc.QueryArbWaveformCapabilitiesRequest\x1a1.nirfsg_grpc.QueryArbWaveformCapabilitiesResponse\x12\x98\x01\n#ReadAndDownloadWaveformFromFileTDMS\x127.nirfsg_grpc.ReadAndDownloadWaveformFromFileTDMSRequest\x1a8.nirfsg_grpc.ReadAndDownloadWaveformFromFileTDMSResponse\x12>\n\x05Reset\x12\x19.nirfsg_grpc.ResetRequest\x1a\x1a.nirfsg_grpc.ResetResponse\x12Y\n\x0eResetAttribute\x12".nirfsg_grpc.ResetAttributeRequest\x1a#.nirfsg_grpc.ResetAttributeResponse\x12P\n\x0bResetDevice\x12\x1f.nirfsg_grpc.ResetDeviceRequest\x1a .nirfsg_grpc.ResetDeviceResponse\x12b\n\x11ResetWithDefaults\x12%.nirfsg_grpc.ResetWithDefaultsRequest\x1a&.nirfsg_grpc.ResetWithDefaultsResponse\x12_\n\x10ResetWithOptions\x12$.nirfsg_grpc.ResetWithOptionsRequest\x1a%.nirfsg_grpc.ResetWithOptionsResponse\x12V\n\rRevisionQuery\x12!.nirfsg_grpc.RevisionQueryRequest\x1a".nirfsg_grpc.RevisionQueryResponse\x12w\n\x18SaveConfigurationsToFile\x12,.nirfsg_grpc.SaveConfigurationsToFileRequest\x1a-.nirfsg_grpc.SaveConfigurationsToFileResponse\x12b\n\x11SelectArbWaveform\x12%.nirfsg_grpc.SelectArbWaveformRequest\x1a&.nirfsg_grpc.SelectArbWaveformResponse\x12D\n\x07SelfCal\x12\x1b.nirfsg_grpc.SelfCalRequest\x1a\x1c.nirfsg_grpc.SelfCalResponse\x12e\n\x12SelfCalibrateRange\x12&.nirfsg_grpc.SelfCalibrateRangeRequest\x1a\'.nirfsg_grpc.SelfCalibrateRangeResponse\x12G\n\x08SelfTest\x12\x1c.nirfsg_grpc.SelfTestRequest\x1a\x1d.nirfsg_grpc.SelfTestResponse\x12t\n\x17SendSoftwareEdgeTrigger\x12+.nirfsg_grpc.SendSoftwareEdgeTriggerRequest\x1a,.nirfsg_grpc.SendSoftwareEdgeTriggerResponse\x12\x8c\x01\n\x1fSetArbWaveformNextWritePosition\x123.nirfsg_grpc.SetArbWaveformNextWritePositionRequest\x1a4.nirfsg_grpc.SetArbWaveformNextWritePositionResponse\x12n\n\x15SetAttributeViBoolean\x12).nirfsg_grpc.SetAttributeViBooleanRequest\x1a*.nirfsg_grpc.SetAttributeViBooleanResponse\x12h\n\x13SetAttributeViInt32\x12\'.nirfsg_grpc.SetAttributeViInt32Request\x1a(.nirfsg_grpc.SetAttributeViInt32Response\x12h\n\x13SetAttributeViInt64\x12\'.nirfsg_grpc.SetAttributeViInt64Request\x1a(.nirfsg_grpc.SetAttributeViInt64Response\x12k\n\x14SetAttributeViReal64\x12(.nirfsg_grpc.SetAttributeViReal64Request\x1a).nirfsg_grpc.SetAttributeViReal64Response\x12n\n\x15SetAttributeViSession\x12).nirfsg_grpc.SetAttributeViSessionRequest\x1a*.nirfsg_grpc.SetAttributeViSessionResponse\x12k\n\x14SetAttributeViString\x12(.nirfsg_grpc.SetAttributeViStringRequest\x1a).nirfsg_grpc.SetAttributeViStringResponse\x12P\n\x0bSetUserData\x12\x1f.nirfsg_grpc.SetUserDataRequest\x1a .nirfsg_grpc.SetUserDataResponse\x12\x89\x01\n\x1eSetWaveformBurstStartLocations\x122.nirfsg_grpc.SetWaveformBurstStartLocationsRequest\x1a3.nirfsg_grpc.SetWaveformBurstStartLocationsResponse\x12\x86\x01\n\x1dSetWaveformBurstStopLocations\x121.nirfsg_grpc.SetWaveformBurstStopLocationsRequest\x1a2.nirfsg_grpc.SetWaveformBurstStopLocationsResponse\x12\x8c\x01\n\x1fSetWaveformMarkerEventLocations\x123.nirfsg_grpc.SetWaveformMarkerEventLocationsRequest\x1a4.nirfsg_grpc.SetWaveformMarkerEventLocationsResponse\x12_\n\x10WaitUntilSettled\x12$.nirfsg_grpc.WaitUntilSettledRequest\x1a%.nirfsg_grpc.WaitUntilSettledResponse\x12_\n\x10WriteArbWaveform\x12$.nirfsg_grpc.WriteArbWaveformRequest\x1a%.nirfsg_grpc.WriteArbWaveformResponse\x12}\n\x1aWriteArbWaveformComplexF32\x12..nirfsg_grpc.WriteArbWaveformComplexF32Request\x1a/.nirfsg_grpc.WriteArbWaveformComplexF32Response\x12}\n\x1aWriteArbWaveformComplexF64\x12..nirfsg_grpc.WriteArbWaveformComplexF64Request\x1a/.nirfsg_grpc.WriteArbWaveformComplexF64Response\x12}\n\x1aWriteArbWaveformComplexI16\x12..nirfsg_grpc.WriteArbWaveformComplexI16Request\x1a/.nirfsg_grpc.WriteArbWaveformComplexI16Response\x12h\n\x13WriteArbWaveformF32\x12\'.nirfsg_grpc.WriteArbWaveformF32Request\x1a(.nirfsg_grpc.WriteArbWaveformF32Response\x12P\n\x0bWriteScript\x12\x1f.nirfsg_grpc.WriteScriptRequest\x1a .nirfsg_grpc.WriteScriptResponseB@\n\x12com.ni.grpc.nirfsgB\x06NiRFSGP\x01\xaa\x02\x1fNationalInstruments.Grpc.NiRFSGb\x06proto3')`

<!--NI_PYTHON_API repo=nimi-python path=generated/nirfsg/nirfsg/nirfsg_pb2_grpc.py -->
## PYTHON MODULE: generated/nirfsg/nirfsg/nirfsg_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

### `class NiRFSGStub(object)`

Missing associated documentation comment in .proto file.

#### `def __init__(self, channel)`

Constructor.

        Args:
            channel: A grpc.Channel.
        

### `class NiRFSGServicer(object)`

Missing associated documentation comment in .proto file.

#### `def Abort(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def AllocateArbWaveform(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CheckAttributeViBoolean(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CheckAttributeViInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CheckAttributeViInt64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CheckAttributeViReal64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CheckAttributeViSession(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CheckAttributeViString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CheckGenerationStatus(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CheckIfConfigurationListExists(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CheckIfScriptExists(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CheckIfWaveformExists(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ClearAllArbWaveforms(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ClearArbWaveform(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ClearError(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ClearSelfCalibrateRange(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Close(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Commit(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureDeembeddingTableInterpolationLinear(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureDeembeddingTableInterpolationNearest(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureDeembeddingTableInterpolationSpline(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureDigitalEdgeConfigurationListStepTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureDigitalEdgeScriptTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureDigitalEdgeStartTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureDigitalLevelScriptTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureDigitalModulationUserDefinedWaveform(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureGenerationMode(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureOutputEnabled(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureP2PEndpointFullnessStartTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigurePXIChassisClk10(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigurePowerLevelType(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureRF(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureRefClock(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureSignalBandwidth(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureSoftwareScriptTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureSoftwareStartTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureUpconverterPLLSettlingTime(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateConfigurationList(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateConfigurationListStep(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateDeembeddingSparameterTableArray(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateDeembeddingSparameterTableS2PFile(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DeleteAllDeembeddingTables(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DeleteConfigurationList(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DeleteDeembeddingTable(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DeleteScript(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Disable(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DisableAllModulation(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DisableConfigurationListStepTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DisableScriptTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DisableStartTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ErrorMessage(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ErrorQuery(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ExportSignal(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAllNamedWaveformNames(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAllScriptNames(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetScript(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViBoolean(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViInt64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViReal64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViSession(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetChannelName(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetDeembeddingSparameters(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetError(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetExternalCalibrationLastDateAndTime(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetMaxSettablePower(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetSelfCalibrationDateAndTime(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetSelfCalibrationTemperature(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetTerminalName(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetUserData(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetWaveformBurstStartLocations(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetWaveformBurstStopLocations(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetWaveformMarkerEventLocations(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Init(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def InitWithOptions(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Initiate(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def InvalidateAllAttributes(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def LoadConfigurationsFromFile(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def PerformPowerSearch(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def PerformThermalCorrection(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def QueryArbWaveformCapabilities(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadAndDownloadWaveformFromFileTDMS(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Reset(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ResetAttribute(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ResetDevice(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ResetWithDefaults(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ResetWithOptions(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def RevisionQuery(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SaveConfigurationsToFile(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SelectArbWaveform(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SelfCal(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SelfCalibrateRange(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SelfTest(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SendSoftwareEdgeTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetArbWaveformNextWritePosition(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViBoolean(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViInt64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViReal64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViSession(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetUserData(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetWaveformBurstStartLocations(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetWaveformBurstStopLocations(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetWaveformMarkerEventLocations(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WaitUntilSettled(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteArbWaveform(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteArbWaveformComplexF32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteArbWaveformComplexF64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteArbWaveformComplexI16(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteArbWaveformF32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteScript(self, request, context)`

Missing associated documentation comment in .proto file.

### `def add_NiRFSGServicer_to_server(servicer, server)`

### `class NiRFSG(object)`

Missing associated documentation comment in .proto file.

#### `def Abort(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def AllocateArbWaveform(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CheckAttributeViBoolean(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CheckAttributeViInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CheckAttributeViInt64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CheckAttributeViReal64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CheckAttributeViSession(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CheckAttributeViString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CheckGenerationStatus(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CheckIfConfigurationListExists(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CheckIfScriptExists(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CheckIfWaveformExists(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ClearAllArbWaveforms(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ClearArbWaveform(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ClearError(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ClearSelfCalibrateRange(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Close(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Commit(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureDeembeddingTableInterpolationLinear(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureDeembeddingTableInterpolationNearest(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureDeembeddingTableInterpolationSpline(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureDigitalEdgeConfigurationListStepTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureDigitalEdgeScriptTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureDigitalEdgeStartTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureDigitalLevelScriptTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureDigitalModulationUserDefinedWaveform(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureGenerationMode(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureOutputEnabled(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureP2PEndpointFullnessStartTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigurePXIChassisClk10(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigurePowerLevelType(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureRF(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureRefClock(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureSignalBandwidth(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureSoftwareScriptTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureSoftwareStartTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureUpconverterPLLSettlingTime(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateConfigurationList(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateConfigurationListStep(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateDeembeddingSparameterTableArray(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateDeembeddingSparameterTableS2PFile(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DeleteAllDeembeddingTables(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DeleteConfigurationList(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DeleteDeembeddingTable(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DeleteScript(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Disable(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DisableAllModulation(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DisableConfigurationListStepTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DisableScriptTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DisableStartTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ErrorMessage(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ErrorQuery(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ExportSignal(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAllNamedWaveformNames(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAllScriptNames(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetScript(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViBoolean(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViInt64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViReal64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViSession(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetChannelName(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetDeembeddingSparameters(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetError(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetExternalCalibrationLastDateAndTime(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetMaxSettablePower(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetSelfCalibrationDateAndTime(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetSelfCalibrationTemperature(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTerminalName(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetUserData(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetWaveformBurstStartLocations(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetWaveformBurstStopLocations(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetWaveformMarkerEventLocations(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Init(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def InitWithOptions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Initiate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def InvalidateAllAttributes(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def LoadConfigurationsFromFile(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def PerformPowerSearch(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def PerformThermalCorrection(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def QueryArbWaveformCapabilities(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadAndDownloadWaveformFromFileTDMS(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Reset(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ResetAttribute(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ResetDevice(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ResetWithDefaults(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ResetWithOptions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def RevisionQuery(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SaveConfigurationsToFile(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SelectArbWaveform(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SelfCal(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SelfCalibrateRange(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SelfTest(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SendSoftwareEdgeTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetArbWaveformNextWritePosition(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViBoolean(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViInt64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViReal64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViSession(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetUserData(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetWaveformBurstStartLocations(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetWaveformBurstStopLocations(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetWaveformMarkerEventLocations(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WaitUntilSettled(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteArbWaveform(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteArbWaveformComplexF32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteArbWaveformComplexF64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteArbWaveformComplexI16(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteArbWaveformF32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteScript(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`
