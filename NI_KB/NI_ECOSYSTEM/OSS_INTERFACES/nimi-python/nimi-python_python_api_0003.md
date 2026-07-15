# NI PYTHON API DIGEST: nimi-python

<!--NI_PYTHON_API_SNAPSHOT repo=ni/nimi-python commit=6511f8025f072f7f7021953888b916bbdc31aa2a -->

<!--NI_PYTHON_API repo=nimi-python path=generated/nirfsg/nirfsg/session.py -->
## PYTHON MODULE: generated/nirfsg/nirfsg/session.py

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

Base class for all NI-RFSG sessions.

#### `def __init__(self, repeated_capability_list, all_channels_in_session, interpreter, freeze_it=False)`

#### `def __repr__(self)`

#### `def __setattr__(self, key, value)`

#### `def configure_digital_edge_script_trigger(self, source, edge)`

configure_digital_edge_script_trigger

        Configures the specified Script Trigger for digital edge triggering.

        The NI-RFSG device must be in the Configuration state before calling this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_

        `Digital Edge Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_edge.html>`_

        Tip:
        This method can be called on specific script_triggers within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container script_triggers to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.script_triggers[ ... ].configure_digital_edge_script_trigger`

        To call the method on all script_triggers, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.configure_digital_edge_script_trigger`

        Args:
            source (str): Specifies the source terminal for the digital edge Script Trigger. NI-RFSG sets the digital_edge_script_trigger_source property to this value.

            edge (enums.ScriptTriggerDigitalEdgeEdge): Specifies the active edge for the digital edge Script Trigger. NI-RFSG sets the digital_edge_script_trigger_edge property to this value.

        

#### `def configure_digital_level_script_trigger(self, source, level)`

configure_digital_level_script_trigger

        Configures a specified Script Trigger for digital level triggering.

        The NI-RFSG device must be in the Configuration state before calling this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_

        `Digital Level Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_level.html>`_

        Tip:
        This method can be called on specific script_triggers within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container script_triggers to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.script_triggers[ ... ].configure_digital_level_script_trigger`

        To call the method on all script_triggers, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.configure_digital_level_script_trigger`

        Args:
            source (str): Specifies the trigger source terminal for the digital level Script Trigger. NI-RFSG sets the digital_level_script_trigger_source property to this value.

            level (int): Specifies the active level for the digital level Script Trigger. NI-RFSG sets the digital_level_script_trigger_active_level property to this value.

        

#### `def configure_software_script_trigger(self)`

configure_software_script_trigger

        Configures the Script Trigger for software triggering.

        Refer to the send_software_edge_trigger method for more information about using the software Script Trigger. The NI-RFSG device must be in the Configuration state before calling this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_

        `Trigger Types <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_types.html>`_

        Tip:
        This method can be called on specific script_triggers within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container script_triggers to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.script_triggers[ ... ].configure_software_script_trigger`

        To call the method on all script_triggers, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.configure_software_script_trigger`
        

#### `def disable_script_trigger(self)`

disable_script_trigger

        Configures the device not to wait for the specified Script Trigger.

        Call this method only if you previously configured a Script Trigger and now want it disabled. The NI-RFSG device must be in the Configuration state before you call this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Script Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/script_triggers.html>`_

        Tip:
        This method can be called on specific script_triggers within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container script_triggers to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.script_triggers[ ... ].disable_script_trigger`

        To call the method on all script_triggers, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.disable_script_trigger`
        

#### `def error_message(self, error_code)`

error_message

        Converts an error code returned by an NI-RFSG method into a user-readable string.

        **Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Args:
            error_code (int): Pass the status parameter that is returned from any NI-RFSG method.

                **Default Value** : 0 (VI_SUCCESS)


        Returns:
            error_message (str): Returns the user-readable message string that corresponds to the status code you specify.

        

#### `def _get_attribute_vi_boolean(self, attribute)`

_get_attribute_vi_boolean

        Queries the value of a ViBoolean property.

        Use this low-level method to get the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_boolean`

        Args:
            attribute (int): Pass the ID of a property.


        Returns:
            value (bool): Returns the current value of the property. Pass the address of a ViBoolean variable.

        

#### `def _get_attribute_vi_int32(self, attribute)`

_get_attribute_vi_int32

        Queries the value of a ViInt32 property.

        Use this low-level method to get the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_int32`

        Args:
            attribute (int): Pass the ID of a property.


        Returns:
            value (int): Returns the current value of the property. Pass the address of a ViInt32 variable.

        

#### `def _get_attribute_vi_int64(self, attribute)`

_get_attribute_vi_int64

        Queries the value of a ViInt64 property.

        You can use this low-level method to get the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_int64`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_int64`

        Args:
            attribute (int): Pass the ID of a property.


        Returns:
            value (int): Returns the current value of the property. Pass the address of a ViInt64 variable.

        

#### `def _get_attribute_vi_real64(self, attribute)`

_get_attribute_vi_real64

        Queries the value of a ViReal64 property.

        Use this low-level method to get the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_real64`

        Args:
            attribute (int): Pass the ID of a property.


        Returns:
            value (float): Returns the current value of the property. Pass the address of a ViReal64 variable.

        

#### `def _get_attribute_vi_session(self, attribute)`

_get_attribute_vi_session

        Queries the value of a ViSession property.

        Use this low-level method to get the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_session`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_session`

        Args:
            attribute (int): Pass the ID of a property.


        Returns:
            value (int): Returns the current value of the property. Pass the address of a ViSession variable.

        

#### `def _get_attribute_vi_string(self, attribute)`

_get_attribute_vi_string

        Queries the value of a ViString property.

        Use this low-level method to get the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid.

        You must provide a ViString (ViChar array) to serve as a buffer for the value. Pass the number of bytes in the buffer as the Buffer Size parameter. If the current value of the property, including the terminating NULL byte, is larger than the size you indicate in the buffer size parameter, the method copies buffer size-1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the method places "123" into the buffer and returns 7.

        To call this method to get only the required buffer size, pass 0 for the buffer size and VI_NULL for the property value buffer.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_string`

        Args:
            attribute (int): Pass the ID of a property.


        Returns:
            value (str): The buffer in which the method returns the current value of the property. The buffer must be of type ViChar and have at least as many bytes as indicated in the **bufferSize** parameter.

                If you specify 0 for the **bufferSize** parameter, you can pass VI_NULL for this parameter.

        

#### `def get_waveform_burst_start_locations(self)`

get_waveform_burst_start_locations

        Returns the burst start locations of the waveform stored in the NI-RFSG session.

        **Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842

        Tip:
        This method can be called on specific waveforms within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container waveforms to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.waveforms[ ... ].get_waveform_burst_start_locations`

        To call the method on all waveforms, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.get_waveform_burst_start_locations`

        Returns:
            locations (list of float): Returns the burst start locations stored in the NI-RFSG session for the waveform that you specified in the CHANNEL_NAME parameter. This value is expressed in samples.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

        

#### `def get_waveform_burst_stop_locations(self)`

get_waveform_burst_stop_locations

        Returns the burst stop locations of the waveform stored in the NI-RFSG session.

        **Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842

        Tip:
        This method can be called on specific waveforms within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container waveforms to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.waveforms[ ... ].get_waveform_burst_stop_locations`

        To call the method on all waveforms, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.get_waveform_burst_stop_locations`

        Returns:
            locations (list of float): Returns the burst start locations stored in the NI-RFSG session for the waveform that you specified in the CHANNEL_NAME parameter. This value is expressed in samples.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

        

#### `def get_waveform_marker_event_locations(self)`

get_waveform_marker_event_locations

        Returns the marker locations associated with the waveform and the marker stored in the NI-RFSG session.

        **Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842

        Tip:
        This method can be called on specific markers within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container markers to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.markers[ ... ].get_waveform_marker_event_locations`

        To call the method on all markers, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.get_waveform_marker_event_locations`

        Returns:
            locations (list of float): Returns the marker locations stored in the NI-RFSG database for the channel you specified in the CHANNEL_NAME parameter. This value is expressed in samples.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

        

#### `def load_configurations_from_file(self, file_path)`

load_configurations_from_file

        Loads the configurations from the specified file to the NI-RFSG driver session.

        The VI does an implicit reset before loading the configurations from the file.

        **Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].load_configurations_from_file`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.load_configurations_from_file`

        Args:
            file_path (str): Specifies the absolute path of the file from which the NI-RFSG loads the configurations.

        

#### `def lock(self)`

lock

        Obtains a multithread lock on the device session. Before doing so, the
        software waits until all other execution threads release their locks
        on the device session.

        Other threads may have obtained a lock on this session for the
        following reasons:

            -  The application called the lock method.
            -  A call to NI-RFSG locked the session.
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
            lock (context manager): When used in a with statement, nirfsg.Session.lock acts as
            a context manager and unlock will be called when the with block is exited
        

#### `def save_configurations_to_file(self, file_path)`

save_configurations_to_file

        Saves the configurations of the session to the specified file.

        **Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].save_configurations_to_file`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.save_configurations_to_file`

        Args:
            file_path (str): Specifies the absolute path of the file to which the NI-RFSG saves the configurations.

        

#### `def send_software_edge_trigger(self, trigger, trigger_identifier)`

send_software_edge_trigger

        Forces a trigger to occur.

        The specified trigger generates regardless of whether the trigger has been configured as a software trigger.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Triggers <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/triggers.html>`_

        Args:
            trigger (enums.SoftwareTriggerType): Specifies the trigger to send.

                **Default Value:** SoftwareTriggerType.START

                **Defined Values:**

                +----------------------------+---------+-------------------------------+
                | Name                       | Value   | Description                   |
                +============================+=========+===============================+
                | SoftwareTriggerType.START  | 0 (0x0) | Specifies the Start Trigger.  |
                +----------------------------+---------+-------------------------------+
                | SoftwareTriggerType.SCRIPT | 1 (0x1) | Specifies the Script Trigger. |
                +----------------------------+---------+-------------------------------+

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            trigger_identifier (enums.TriggerIdentifier): Specifies the Script Trigger to configure. This parameter is valid only when you set the TRIGGER parameter to NIRFSG_VAL_START_TRIGGER. Otherwise, set the TRIGGER_IDENTIFIER parameter to "" (empty string).

                **Default Value:** "" (empty string)

                **Possible Values:**

                +----------------+-----------------------------+
                | Possible Value | Description                 |
                +================+=============================+
                | scriptTrigger0 | Specifies Script Trigger 0. |
                +----------------+-----------------------------+
                | scriptTrigger1 | Specifies Script Trigger 1. |
                +----------------+-----------------------------+
                | scriptTrigger2 | Specifies Script Trigger 2. |
                +----------------+-----------------------------+
                | scriptTrigger3 | Specifies Script Trigger 3. |
                +----------------+-----------------------------+
                |                | None (no signal to export)  |
                +----------------+-----------------------------+

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        

#### `def _set_attribute_vi_boolean(self, attribute, value)`

_set_attribute_vi_boolean

        Sets the value of a ViBoolean property.

        Use this low-level method to set the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid or is different than the value you specify.

        NI-RFSG contains high-level methods that set most of the instrument properties. Use the high-level driver methods as much as possible, as they handle order dependencies and multithread locking. The high-level methods also perform status checking only after setting all of the properties. In contrast, when you set multiple properties using the SetAttribute methods, the methods check the instrument status after each call.

        Also, when state caching is enabled, the high-level methods that configure multiple properties perform instrument I/O only for the properties whose value you change. Thus, you can safely call the high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_boolean`

        Args:
            attribute (int): Pass the ID of a property.

            value (bool): Pass the value to which you want to set the property.

                Note: Some values may not be valid. The allowed values depend on the current settings of the instrument session.

        

#### `def _set_attribute_vi_int32(self, attribute, value)`

_set_attribute_vi_int32

        Sets the value of a ViInt32 property.

        Use this low-level method to set the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid or is different than the value you specify.

        NI-RFSG contains high-level methods that set most of the instrument properties. Use the high-level driver methods as much as possible, as they handle order dependencies and multithread locking. The high-level methods also perform status checking only after setting all of the properties. In contrast, when you set multiple properties using the SetAttribute methods, the methods check the instrument status after each call.

        Also, when state caching is enabled, the high-level methods that configure multiple properties perform instrument I/O only for the properties whose value you change. Thus, you can safely call the high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_int32`

        Args:
            attribute (int): Pass the ID of a property.

            value (int): Specifies the value to which you want to set the property.

                Note: Some values may not be valid. The allowed values depend on the current settings of the instrument session.

        

#### `def _set_attribute_vi_int64(self, attribute, value)`

_set_attribute_vi_int64

        Sets the value of a ViInt64 property.

        Use this low-level method to set the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid or is different than the value you specify.

        NI-RFSG contains high-level methods that set most of the instrument properties. Use the high-level driver methods as much as possible, as they handle order dependencies and multithread locking. The high-level methods also perform status checking only after setting all of the properties. In contrast, when you set multiple properties using the SetAttribute methods, the methods check the instrument status after each call.

        Also, when state caching is enabled, the high-level methods that configure multiple properties perform instrument I/O only for the properties whose value you change. Thus, you can safely call the high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_int64`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_int64`

        Args:
            attribute (int): Pass the ID of a property.

            value (int): Pass the value to which you want to set the property.

                <blockquote>
                Some values may not be valid. The allowed values depend on the current settings of the instrument session.
                </blockquote>

        

#### `def _set_attribute_vi_real64(self, attribute, value)`

_set_attribute_vi_real64

        Sets the value of a ViReal64 property.

        Use this low-level method to set the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid or is different than the value you specify.

        NI-RFSG contains high-level methods that set most of the instrument properties. Use the high-level driver methods as much as possible, as they handle order dependencies and multithread locking. The high-level methods also perform status checking only after setting all of the properties. In contrast, when you set multiple properties using the SetAttribute methods, the methods check the instrument status after each call.

        Also, when state caching is enabled, the high-level methods that configure multiple properties perform instrument I/O only for the properties whose value you change. Thus, you can safely call the high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_real64`

        Args:
            attribute (int): Pass the ID of a property.

            value (float): Pass the value to which you want to set the property.

                Note: Some values may not be valid. The allowed values depend on the current settings of the instrument session.

        

#### `def _set_attribute_vi_session(self, attribute)`

_set_attribute_vi_session

        Sets the value of a ViSession property.

        Use this low-level method to set the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid or is different than the value you specify.

        NI-RFSG contains high-level methods that set most of the instrument properties. Use the high-level driver methods as much as possible, as they handle order dependencies and multithread locking. The high-level methods also perform status checking only after setting all of the properties. In contrast, when you set multiple properties using the SetAttribute methods, the methods check the instrument status after each call.

        Also, when state caching is enabled, the high-level methods that configure multiple properties perform instrument I/O only for the properties whose value you change. Thus, you can safely call the high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_session`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_session`

        Args:
            attribute (int): Pass the ID of a property.

        

#### `def _set_attribute_vi_string(self, attribute, value)`

_set_attribute_vi_string

        Sets the value of a ViString property.

        Use this low-level method to set the values of inherent IVI properties, class-defined properties, and instrument-specific properties. If the property represents an instrument state, this method performs instrument I/O in the following cases:

        - State caching is disabled for the entire session or for the particular property.
        - State caching is enabled, and the currently cached value is invalid or is different than the value you specify.

        NI-RFSG contains high-level methods that set most of the instrument properties. Use the high-level driver methods as much as possible, as they handle order dependencies and multithread locking. The high-level methods also perform status checking only after setting all of the properties. In contrast, when you set multiple properties using the SetAttribute methods, the methods check the instrument status after each call.

        Also, when state caching is enabled, the high-level methods that configure multiple properties perform instrument I/O only for the properties whose value you change. Thus, you can safely call the high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_string`

        Args:
            attribute (int): Pass the ID of a property.

            value (str): Pass the value to which you want to set the property.

                Note: Some values may not be valid. The allowed values depend on the current settings of the instrument session.

        

#### `def set_waveform_burst_start_locations(self, locations)`

set_waveform_burst_start_locations

        Configures the start location of the burst in samples where the burst refers to the active portion of a waveform.

        **Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842

        Tip:
        This method can be called on specific waveforms within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container waveforms to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.waveforms[ ... ].set_waveform_burst_start_locations`

        To call the method on all waveforms, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.set_waveform_burst_start_locations`

        Args:
            locations (list of float): Returns the burst start locations stored in the NI-RFSG session for the waveform that you specified in the CHANNEL_NAME parameter. This value is expressed in samples.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

        

#### `def set_waveform_burst_stop_locations(self, locations)`

set_waveform_burst_stop_locations

        Configures the stop location of the burst in samples where the burst refers to the active portion of a waveform.

        **Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842

        Tip:
        This method can be called on specific waveforms within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container waveforms to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.waveforms[ ... ].set_waveform_burst_stop_locations`

        To call the method on all waveforms, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.set_waveform_burst_stop_locations`

        Args:
            locations (list of float): Specifies the burst stop locations, in samples, to store in the NI-RFSG session.

        

#### `def set_waveform_marker_event_locations(self, locations)`

set_waveform_marker_event_locations

        Configures the marker locations associated with waveform and marker in the NI-RFSG session.

        **Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842

        Tip:
        This method can be called on specific markers within your :py:class:`nirfsg.Session` instance.
        Use Python index notation on the repeated capabilities container markers to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.markers[ ... ].set_waveform_marker_event_locations`

        To call the method on all markers, you can call it directly on the :py:class:`nirfsg.Session`.

        Example: :py:meth:`my_session.set_waveform_marker_event_locations`

        Args:
            locations (list of float): Specifies the marker location, in samples, to store in the NI-RFSG database.

        

#### `def unlock(self)`

unlock

        Releases a lock that you acquired on an device session using
        lock. Refer to lock for additional
        information on session locks.
        

### `class Session(_SessionBase)`

An NI-RFSG session to the NI-RFSG driver

#### `def __init__(self, resource_name, id_query=False, reset_device=False, options={}, *, grpc_options=None)`

An NI-RFSG session to the NI-RFSG driver

        Opens a session to the device you specify as the RESOURCE_NAME and returns a ViSession handle that you use to identify the NI-RFSG device in all subsequent NI-RFSG method calls.

        This method also configures the device through the OPTION_STRING input.

        **Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Simulating an NI RF Signal Generator <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/simulate.html>`_

        Note: For multichannel devices such as the PXIe-5860, the resource name must include the channel number to use. The channel number is specified by appending /*ChannelNumber* to the device name, where *ChannelNumber* is the channel number (0, 1, etc.). For example, if the device name is PXI1Slot2 and you want to use channel 0, use the resource name PXI1Slot2/0.

        Note:
        One or more of the referenced properties are not in the Python API for this driver.

        Args:
            resource_name (str): Specifies the resource name of the device to initialize.

                For NI-DAQmx devices, the syntax is the device name specified in MAX. Typical default names for NI-DAQmx devices in MAX are Dev2 or PXISlot2. You can rename an NI-DAQmx device in MAX.

                You can also specify the name of an IVI logical name configured with the IVI Configuration utility. Refer to the *IVI* topic of the *Measurement & Automation Explorer Help* for more information.

                Note: NI-RFSG device names are not case-sensitive. However, all IVI names, such as logical names, are case-sensitive. If you use an IVI logical name, make sure the name is identical to the name shown in the IVI Configuration Utility.

            id_query (bool): Specifies whether you want NI-RFSG to perform an ID query.

                **Defined Values** :

                +-----------+--------------------------+
                | Value     | Description              |
                +===========+==========================+
                | True (1)  | Perform ID query.        |
                +-----------+--------------------------+
                | False (0) | Do not perform ID query. |
                +-----------+--------------------------+

            reset_device (bool): Specifies whether you want to reset the NI-RFSG device during the initialization procedure.

                **Defined Values** :

                +-----------+----------------------+
                | Value     | Description          |
                +===========+======================+
                | True (1)  | Reset device.        |
                +-----------+----------------------+
                | False (0) | Do not reset device. |
                +-----------+----------------------+

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

            grpc_options (nirfsg.grpc_session_options.GrpcSessionOptions): MeasurementLink gRPC session options


        Returns:
            new_vi (int): Returns a ViSession handle that you use to identify the NI-RFSG device in all subsequent NI-RFSG method calls.

        

#### `def __enter__(self)`

#### `def __exit__(self, exc_type, exc_value, traceback)`

#### `def initiate(self)`

initiate

        Initiates signal generation, causing the NI-RFSG device to leave the Configuration state and enter the Generation state.

        If the settings have not been committed to the device before you call this method, they are committed by this method. The operation returns when the RF output signal settles. To return to the Configuration state, call the abort method.

        **Supported Devices** : PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`_

        Note:
        This method will return a Python context manager that will initiate on entering and abort on exit.
        

#### `def close(self)`

close

        Aborts any signal generation in progress and destroys the instrument driver session.

        **Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`_

        `NI-RFSG Programming State Model <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5670_programming_state_model.html>`_

        Note:
        This method is not needed when using the session context manager
        

#### `def abort(self)`

abort

        Stops signal generation.

        **Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `NI-RFSG Programming State Model <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5670_programming_state_model.html>`_
        

#### `def allocate_arb_waveform(self, waveform_name, size_in_samples)`

allocate_arb_waveform

        Allocates onboard memory space for the arbitrary waveform.

        Use this method to specify the total size of a waveform before writing the data. Use this method only if you are calling the WriteArbWaveform method multiple times to write a large waveform in smaller blocks.

        The NI-RFSG device must be in the Configuration state before you call this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Streaming Waveform Data <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/streaming_waveform_data.html>`_

        Args:
            waveform_name (str): Specifies the name used to identify the waveform. This string is case-insensitive and alphanumeric, and it does not use reserved words.

            size_in_samples (int): Specifies the number of samples to reserve in the onboard memory for the specified waveform. Each I/Q pair is considered one sample.

        

#### `def change_external_calibration_password(self, old_password, new_password)`

change_external_calibration_password

        Changes the external calibration password of the device.

        **Supported Devices:** PXIe-5611, PXIe-5653/5654, PXIe-5673/5673E, PXIe-5696, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Args:
            old_password (str): Specifies the old (current) external calibration password. This password is case sensitive.

            new_password (str): Specifies the new (desired) external calibration password.

        

#### `def check_generation_status(self)`

check_generation_status

        Checks the status of the generation.

        Call this method to check for any errors that might occur during the signal generation or to check whether the device has finished generating.

        **Supported Devices** : PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`

        Returns:
            is_done (bool): Returns information about the completion of signal generation.

                **Defined Values** :

                +-------+---------------------------------+
                | Value | Description                     |
                +=======+=================================+
                | True  | Signal generation is complete.  |
                +-------+---------------------------------+
                | False | Signal generation is occurring. |
                +-------+---------------------------------+

        

#### `def check_if_script_exists(self, script_name)`

check_if_script_exists

        Returns whether the script that you specify as SCRIPT_NAME exists.

        **Supported Devices** : PXIe-5673/5673E. PXIe-5830/5831/5840/5841/5842/5860

        Note:
        One or more of the referenced properties are not in the Python API for this driver.

        Args:
            script_name (str): Specifies the name of the script. This string is case-insensitive.


        Returns:
            script_exists (bool): Returns True if the script exists.

                **Defined Values** :

                +-------+----------------------------+
                | Value | Description                |
                +=======+============================+
                | True  | The script exists.         |
                +-------+----------------------------+
                | False | The script does not exist. |
                +-------+----------------------------+

        

#### `def check_if_waveform_exists(self, waveform_name)`

check_if_waveform_exists

        Returns whether the waveform that you specify as WAVEFORM_NAME exists.

        **Supported Devices** : PXIe-5673/5673E, PXIe-5830/5831/5840/5841/5842/5860

        Note:
        One or more of the referenced properties are not in the Python API for this driver.

        Args:
            waveform_name (str): Specifies the name used to store the waveform. This string is case-insensitive.


        Returns:
            waveform_exists (bool): Returns True if the waveform exists.

                **Defined Values** :

                +-------+------------------------------+
                | Value | Description                  |
                +=======+==============================+
                | True  | The waveform exists.         |
                +-------+------------------------------+
                | False | The waveform does not exist. |
                +-------+------------------------------+

        

#### `def clear_all_arb_waveforms(self)`

clear_all_arb_waveforms

        Deletes all currently defined waveforms and scripts.

        The NI-RFSG device must be in the Configuration state before you call this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860
        

#### `def clear_arb_waveform(self, waveform_name)`

clear_arb_waveform

        Deletes a specified waveform from the pool of currently defined waveforms.

        The NI-RFSG device must be in the Configuration state before you call this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Args:
            waveform_name (str): Name of the stored waveform to delete.

        

#### `def clear_self_calibrate_range(self)`

clear_self_calibrate_range

        Clears the data obtained from the self_calibrate_range method.

        **Supported Devices** : PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842
        

#### `def commit(self)`

commit

        Programs the device with the correct settings.

        Calling this method moves the NI-RFSG device from the Configuration state to the Committed state. After this method executes, a change to any property reverts the NI-RFSG device to the Configuration state.

        **Supported devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `NI-RFSG Programming State Model <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5670_programming_state_model.html>`_
        

#### `def configure_deembedding_table_interpolation_linear(self, port, table_name, format)`

configure_deembedding_table_interpolation_linear

        Selects the linear interpolation method.

        If the carrier frequency does not match a row in the de-embedding table, NI-RFSG performs a linear interpolation based on the entries in the de-embedding table to determine the parameters to use for de-embedding.

        **Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860

        Args:
            port (str): Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).

            table_name (str): Specifies the name of the table.

            format (enums.Format): Specifies the format of parameters to interpolate. **Defined Values** :

                +-------------------------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
                | Name                          | Value          | Description                                                                                                                             |
                +===============================+================+=========================================================================================================================================+
                | Format.REAL_AND_IMAGINARY     | 26000 (0x6590) | Results in a linear interpolation of the real portion of the complex number and a separate linear interpolation of the complex portion. |
                +-------------------------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
                | Format.MAGNITUDE_AND_PHASE    | 26001 (0x6591) | Results in a linear interpolation of the magnitude and a separate linear interpolation of the phase.                                    |
                +-------------------------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
                | Format.MAGNITUDE_DB_AND_PHASE | 26002 (0x6592) | Results in a linear interpolation of the magnitude, in decibels, and a separate linear interpolation of the phase.                      |
                +-------------------------------+----------------+-----------------------------------------------------------------------------------------------------------------------------------------+

        

#### `def configure_deembedding_table_interpolation_nearest(self, port, table_name)`

configure_deembedding_table_interpolation_nearest

        Selects the nearest interpolation method.

        NI-RFSG uses the parameters of the table nearest to the carrier frequency for de-embedding.

        **Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860

        Args:
            port (str): Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).

            table_name (str): Specifies the name of the table.

        

#### `def configure_deembedding_table_interpolation_spline(self, port, table_name)`

configure_deembedding_table_interpolation_spline

        Selects the spline interpolation method.

        If the carrier frequency does not match a row in the de-embedding table, NI-RFSG performs a spline interpolation based on the entries in the de-embedding table to determine the parameters to use for de-embedding.

        **Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860

        Args:
            port (str): Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).

            table_name (str): Specifies the name of the table.

        

#### `def configure_digital_edge_start_trigger(self, source, edge)`

configure_digital_edge_start_trigger

        Configures the Start Trigger for digital edge triggering.

        The NI-RFSG device must be in the Configuration state before calling this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_

        `Digital Edge Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_edge.html>`_

        Note: For the PXIe-5654/5654 with PXIe-5696, the Start Trigger is valid only with a timer-based list when RF list mode is enabled.

        Args:
            source (str): Specifies the source terminal for the digital edge trigger. NI-RFSG sets the digital_edge_start_trigger_source property to this value.

            edge (enums.StartTriggerDigitalEdgeEdge): Specifies the active edge for the Start Trigger. NI-RFSG sets the digital_edge_start_trigger_edge property to this value.

        

#### `def configure_rf(self, frequency, power_level)`

configure_rf

        Configures the frequency and power level of the RF output signal.

        The PXI-5670/5671, PXIe-5672, and PXIe-5860 device must be in the Configuration state before calling this method. The PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXIe-5673/5673E, and PXIe-5830/5831/5832/5840/5841/5842 device can be in the Configuration or Generation state when you call this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`_

        Args:
            frequency (float): Specifies the frequency of the generated RF signal, in hertz. For arbitrary waveform generation, this parameter specifies the center frequency of the signal.

                **Units** : hertz (Hz)

            power_level (float): Specifies either the average power level or peak power level of the generated RF signal, depending on the power_level_type property.

                **Units** : dBm

        

#### `def configure_ref_clock(self, ref_clock_source, ref_clock_rate)`

configure_ref_clock

        Configures the NI-RFSG device Reference Clock.

        The Reference Clock ensures that the NI-RFSG devices are operating from a common timebase. The NI-RFSG device must be in the Configuration state before calling this method.

        **Supported Devices** : PXI-5610, PXIe-5644/5645/5646, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `PXIe-5672 Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/timing_configurations.html>`_

        `PXIe-5673 Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/10mhzreference_phase1.html>`_

        `PXIe-5673E Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/10mhzreference.html>`_

        `PXIe-5830 Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/timing_configurations.html>`_

        `PXIe-5831 Timing Configurations <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/timing_configurations.html>`_

        Args:
            ref_clock_source (str): Specifies the source of Reference Clock signal.

                +-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | Possible Values | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
                +=================+=================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
                | "OnboardClock"  |  Uses the onboard Reference Clock as the clock source. **PXIe-5830/5831/5832** :For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For the PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. **PXIe-5831 with PXIe-5653** :Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. **PXIe-5832 with PXIe-5653** :Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. **PXIe-5841 with PXIe-5655** :Lock to the PXIe-5655 onboard clock. Connect the REF OUT connector on the PXIe-5655 to the PXIe-5841 REF IN connector. **PXIe-5842** :Lock to the PXIe-5655 onboard clock. Cables between modules are required as shown in the Getting Started Guide for the instrument.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
                +-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | "RefIn"         | Uses the clock signal present at the front panel REF IN connector as the clock source. **PXIe-5830/5831/5832** :For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For the PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. For the PXIe-5830, lock the external signal to the PXIe-3621 REF IN connector. For the PXIe-5831, lock the external signal to the PXIe-3622 REF IN connector. For the PXIe-5832, lock the external signal to the PXIe-3623 REF IN connector. **PXIe-5831 with PXIe-5653** :Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. **PXIe-5832 with PXIe-5653** :Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector.  **PXIe-5841 with PXIe-5655** :Lock to the signal at the REF IN connector on the associated PXIe-5655. Connect the PXIe-5655 REF OUT connector to the PXIe-5841 REF IN connector. **PXIe-5842** :Lock to the signal at the REF IN connector on the associated PXIe-5655. Cables between modules are required as shown in the Getting Started Guide for the instrument. |
                +-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | "PXI_CLK"       | Uses the PXI_CLK signal, which is present on the PXI backplane, as the clock source.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
                +-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | "ClkIn"         | Uses the clock signal present at the front panel CLK IN connector as the clock source. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841/5841 with PXIe-5655/5842.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
                +-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | "RefIn2"        | \-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
                +-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | "PXI_ClkMaster" | This value is valid on only the PXIe-5831 with PXIe-5653 and PXIe-5832 with PXIe-5653. **PXIe-5831 with PXIe-5653** :NI-RFSG configures the PXIe-5653 to export the Reference clock and configures the PXIe-5820 and PXIe-3622 to use PXI_Clk as the Reference Clock source. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. **PXIe-5832 with PXIe-5653** :NI-RFSG configures the PXIe-5653 to export the Reference clock and configures the PXIe-5820 and PXIe-3623 to use PXI_Clk as the Reference Clock source. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
                +-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

            ref_clock_rate (float): Specifies the Reference Clock rate, in hertz (Hz), of the signal present at the REF IN or CLK IN connector. The default value is NIRFSG_VAL_AUTO, which allows NI-RFSG to use the default Reference Clock rate for the device or automatically detect the Reference Clock rate, if supported. This parameter is only valid when the ref_clock_source parameter is set to ClkIn, RefIn or RefIn2. Refer to the ref_clock_rate property for possible values.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        

#### `def configure_software_start_trigger(self)`

configure_software_start_trigger

        Configures the Start Trigger for software triggering.

        Refer to the send_software_edge_trigger method for more information about using a software trigger. The NI-RFSG device must be in the Configuration state before calling this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_

        `Trigger Types <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/trigger_types.html>`_
        

#### `def _create_deembedding_sparameter_table_array(self, port, table_name, frequencies, sparameter_table, number_of_ports, sparameter_orientation)`

_create_deembedding_sparameter_table_array

        Creates an s-parameter de-embedding table for the port from the input data.

        If you only create one table for a port, NI-RFSG automatically selects that table to de-embed the measurement.

        **Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `De-embedding Overview <https://www.ni.com/docs/en-US/bundle/pxie-5840/page/de-embedding-overview.html>`_

        Args:
            port (str): Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).

            table_name (str): Specifies the name of the table. The name must be unique for a given port, but not across ports. If you use the same name as an existing table, the table is replaced.

            frequencies (numpy.array(dtype=numpy.float64)): Specifies the frequencies for the SPARAMETER_TABLE rows. Frequencies must be unique and in ascending order.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

            sparameter_table (numpy.array(dtype=numpy.complex128)): Specifies the S-parameters for each frequency. S-parameters for each frequency are placed in the array in the following order: s11, s12, s21, s22.

            sparameter_orientation (enums.SparameterOrientation): Specifies the orientation of the input data relative to the port on the DUT port.

                **Defined Values** :

                +-----------------------------------------+----------------+-----------------------------------------------------+
                | Name                                    | Value          | Description                                         |
                +=========================================+================+=====================================================+
                | SparameterOrientation.PORT1_TOWARDS_DUT | 24000 (0x5dc0) | Port 1 of the S2P is oriented towards the DUT port. |
                +-----------------------------------------+----------------+-----------------------------------------------------+
                | SparameterOrientation.PORT2_TOWARDS_DUT | 24001 (0x5dc1) | Port 2 of the S2P is oriented towards the DUT port. |
                +-----------------------------------------+----------------+-----------------------------------------------------+

        

#### `def create_deembedding_sparameter_table_s2p_file(self, port, table_name, s2p_file_path, sparameter_orientation)`

create_deembedding_sparameter_table_s2p_file

        Creates an S-parameter de-embedding table for the port based on the specified S2P file.

        If you only create one table for a port, NI-RFSG automatically selects that table to de-embed the measurement.

        **Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `De-embedding Overview <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/de_embedding_overview.html>`_

        `S-parameters <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/s_parameters.html>`_

        Args:
            port (str): Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842 is empty string.

            table_name (str): Specifies the name of the table. The name must be unique for a given port, but not across ports. If you use the same name as an existing table, the table is replaced.

            s2p_file_path (str): Specifies the path to the S2P file that contains de-embedding information for the specified port.

            sparameter_orientation (enums.SparameterOrientation): Specifies the orientation of the data in the S2P file relative to the port on the DUT port. **Defined Values** :

                +-----------------------------------------+----------------+-----------------------------------------------------+
                | Name                                    | Value          | Description                                         |
                +=========================================+================+=====================================================+
                | SparameterOrientation.PORT1_TOWARDS_DUT | 24000 (0x5dc0) | Port 1 of the S2P is oriented towards the DUT port. |
                +-----------------------------------------+----------------+-----------------------------------------------------+
                | SparameterOrientation.PORT2_TOWARDS_DUT | 24001 (0x5dc1) | Port 2 of the S2P is oriented towards the DUT port. |
                +-----------------------------------------+----------------+-----------------------------------------------------+

        

#### `def delete_all_deembedding_tables(self)`

delete_all_deembedding_tables

        Deletes all configured de-embedding tables for the session.

        **Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860
        

#### `def delete_deembedding_table(self, port, table_name)`

delete_deembedding_table

        Deletes the selected de-embedding table for a given port.

        **Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860

        Args:
            port (str): Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).

            table_name (str): Specifies the name of the table.

        

#### `def delete_script(self, script_name)`

delete_script

        Deletes a specified script from the pool of currently defined scripts. The NI-RFSG device must be in the Configuration state before you call this method.

        **Supported Devices** :PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Args:
            script_name (str): Specifies the name of the script to delete. This string is case-insensitive.

        

#### `def disable_start_trigger(self)`

disable_start_trigger

        Configures the device not to wait for a Start Trigger.

        This method is necessary only if you previously configured a Start Trigger and now want it disabled. The NI-RFSG device must be in the Configuration state before calling this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXIe-5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Start Trigger <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/start_triggers.html>`_
        

#### `def create_deembedding_sparameter_table_array(self, port, table_name, frequencies, sparameter_table, sparameter_orientation)`

create_deembedding_sparameter_table_array

        Creates an s-parameter de-embedding table for the port from the input data.

        If you only create one table for a port, NI-RFSG automatically selects that table to de-embed the measurement.

        **Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `De-embedding Overview<https://www.ni.com/docs/en-US/bundle/pxie-5840/page/de-embedding-overview.html>`_

        Args:
            port (str): Specifies the name of the port. The only valid value for the PXIe-5840/5841/5842/5860 is "" (empty string).

            table_name (str): Specifies the name of the table. The name must be unique for a given port, but not across ports. If you use the same name as an existing table, the table is replaced.

            frequencies (numpy.array(dtype=numpy.float64)): Specifies the frequencies for the SPARAMETER_TABLE rows. Frequencies must be unique and in ascending order.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

            sparameter_table (numpy.array(dtype=numpy.complex128)): Specifies the S-parameters for each frequency. S-parameters for each frequency are placed in the array in the following order: s11, s12, s21, s22.

            sparameter_orientation (enums.SparameterOrientation): Specifies the orientation of the input data relative to the port on the DUT port.

                **Defined Values** :

                +-----------------------------------------+----------------+-----------------------------------------------------+
                | Name                                    | Value          | Description                                         |
                +=========================================+================+=====================================================+
                | SparameterOrientation.PORT1_TOWARDS_DUT | 24000 (0x5dc0) | Port 1 of the S2P is oriented towards the DUT port. |
                +-----------------------------------------+----------------+-----------------------------------------------------+
                | SparameterOrientation.PORT2_TOWARDS_DUT | 24001 (0x5dc1) | Port 2 of the S2P is oriented towards the DUT port. |
                +-----------------------------------------+----------------+-----------------------------------------------------+

        

#### `def get_deembedding_sparameters(self)`

get_deembedding_sparameters

        Returns the S-parameters used for de-embedding a measurement on the selected port.

        This includes interpolation of the parameters based on the configured carrier frequency. This method returns an empty array if no de-embedding is done.

        If you want to call this method just to get the required buffer size, you can pass 0 for **S-parameter Size** and VI_NULL for the **S-parameters** buffer.

        **Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860

        Note: The port orientation for the returned S-parameters is normalized to SparameterOrientation.PORT1_TOWARDS_DUT.

        Returns:
            sparameters (numpy.array(dtype=numpy.complex128)): Returns an array of S-parameters. The S-parameters are returned in the following order: s11, s12, s21, s22.

        

#### `def get_all_named_waveform_names(self)`

get_all_named_waveform_names

        Return names of the waveforms present in the memory.

        **Supported Devices** :PXIe-5830/5831/5840/5841/5842E

        Returns:
            waveform_names (list of str): Returns a list of string having waveform names.

        

#### `def get_all_script_names(self)`

get_all_script_names

        Return names of the scripts present in the memory.

        **Supported Devices** :PXIe-5830/5831/5840/5841/5842E

        Returns:
            script_names (list of str): Returns a list of string having script names.

        

#### `def _get_external_calibration_last_date_and_time(self)`

_get_external_calibration_last_date_and_time

        Returns the date and time of the last successful external calibration.

        The time returned is 24-hour (military) local time; for example, if the device was calibrated at 2:30PM, this method returns

        14 for the hours parameter and

        30 for the minutes parameter.

        **Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5696, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Returns:
            year (int): Returns the year of the last successful calibration.

            month (int): Returns the month of the last successful calibration.

            day (int): Returns the day of the last successful calibration.

            hour (int): Returns the hour of the last successful calibration.

            minute (int): Returns the minute of the last successful calibration.

            second (int): Returns the second of the last successful calibration.

        

#### `def get_ext_cal_last_date_and_time(self)`

get_ext_cal_last_date_and_time

        Returns the date and time of the last successful external calibration.

        The time returned is 24-hour (military) local time; for example, if the device was calibrated at 2:30PM, this method returns

        14 for the hours parameter and

        30 for the minutes parameter.

        **Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5696, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Returns:
            last_cal_datetime (hightime.datetime):

        

#### `def get_self_cal_last_date_and_time(self, module=enums.Module.PRIMARY_MODULE)`

get_self_cal_last_date_and_time

        Returns the date and time of the last successful self-calibration.

        The time returned is 24-hour local time. For example, if the device was calibrated at 2:30PM, this method returns

        14 for the hours parameter and

        30 for the minutes parameter.

        **Supported Devices** : PXI-5610, PXIe-5644/5645/5646, PXIe-5653, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Args:
            module (enums.Module): Specifies from which stand-alone module to retrieve the last successful self-calibration date and time.


        Returns:
            last_cal_datetime (hightime.datetime):

        

#### `def get_max_settable_power(self)`

get_max_settable_power

        Returns the maximum settable output power level for the current configuration.

        **Supported Devices** : PXIe-5830/5831/5832/5840/5841/5842/5860

        Returns:
            value (float): Returns maximum settable power level in dBm.

        

#### `def get_script(self, script_name)`

get_script

        Returns the content of specified script.

        **Supported Devices** :PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Args:
            script_name (str): Specifies the name of the script. This string is case-insensitive.


        Returns:
            script (str): Returns the script.

        

#### `def _get_self_calibration_date_and_time(self, module)`

_get_self_calibration_date_and_time

        Returns the date and time of the last successful self-calibration.

        The time returned is 24-hour local time. For example, if the device was calibrated at 2:30PM, this method returns

        14 for the hours parameter and

        30 for the minutes parameter.

        **Supported Devices** : PXI-5610, PXIe-5644/5645/5646, PXIe-5653, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Args:
            module (enums.Module): Specifies from which stand-alone module to retrieve the last successful self-calibration date and time.


        Returns:
            year (int): Returns the year of the last successful calibration.

            month (int): Returns the month of the last successful calibration.

            day (int): Returns the day of the last successful calibration.

            hour (int): Returns the hour of the last successful calibration.

            minute (int): Returns the minute of the last successful calibration.

            second (int): Returns the second of the last successful calibration.

        

#### `def get_self_calibration_temperature(self, module=enums.Module.PRIMARY_MODULE)`

get_self_calibration_temperature

        Returns the temperature, in degrees Celsius, of the device at the last successful self-calibration.

        **Supported Devices** : PXI-5610, PXIe-5653, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831 (IF only)/5832 (IF only)/5840/5841/5842/5860

        Args:
            module (enums.Module): Specifies from which stand-alone module to retrieve the last successful self-calibration temperature.
                                    **Default Value** : Module.PRIMARY_MODULE
                                    **Defined Values** :

                +-----------------------+----------------+---------------------------------------------------------------------+
                | Name                  | Value          | Description                                                         |
                +=======================+================+=====================================================================+
                | Module.PRIMARY_MODULE | 13000 (0x32c8) | The stand-alone device or the main module in a multi-module device. |
                +-----------------------+----------------+---------------------------------------------------------------------+
                | Module.AWG            | 13001 (0x32c9) | The AWG associated with the primary module.                         |
                +-----------------------+----------------+---------------------------------------------------------------------+
                | Module.LO             | 13002 (0x32ca) | The LO associated with the primary module.                          |
                +-----------------------+----------------+---------------------------------------------------------------------+


        Returns:
            temperature (float): Returns the temperature, in degrees Celsius, of the device at the last successful self-calibration.

        

#### `def get_terminal_name(self, signal, signal_identifier)`

get_terminal_name

        Returns the fully-qualified name of the specified signal.

        The fully-qualified name is helpful to automatically route signals in a multisegment chassis.

        **Supported Devices** : PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Triggers <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/triggers.html>`_

        `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_

        `Syntax for Terminal Names <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/syntax_for_terminal_names.html>`_

        Args:
            signal (enums.Signal): Specifies the signal to query. **Defined Values** :

                +--------------------------------------------+---------+--------------------------------------------+
                | Name                                       | Value   | Description                                |
                +============================================+=========+============================================+
                | Signal.START_TRIGGER                       | 0 (0x0) | Exports a Start Trigger.                   |
                +--------------------------------------------+---------+--------------------------------------------+
                | Signal.SCRIPT_TRIGGER                      | 1 (0x1) | Exports a Script Trigger.                  |
                +--------------------------------------------+---------+--------------------------------------------+
                | Signal.MARKER_EVENT                        | 2 (0x2) | Exports a Marker Event.                    |
                +--------------------------------------------+---------+--------------------------------------------+
                | Signal.REF_CLOCK                           | 3 (0x3) | Exports the Reference Clock.               |
                +--------------------------------------------+---------+--------------------------------------------+
                | Signal.STARTED_EVENT                       | 4 (0x4) | Exports a Started Event.                   |
                +--------------------------------------------+---------+--------------------------------------------+
                | Signal.DONE_EVENT                          | 5 (0x5) | Exports a Done Event.                      |
                +--------------------------------------------+---------+--------------------------------------------+
                | NIRFSG_VAL_CONFIGURATION_LIST_STEP_TRIGGER | 6 (0x6) | Exports a Configuration List Step Trigger. |
                +--------------------------------------------+---------+--------------------------------------------+
                | NIRFSG_VAL_CONFIGURATION_SETTLED_EVENT     | 7 (0x7) | Exports a Configuration Settled Event.     |
                +--------------------------------------------+---------+--------------------------------------------+

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            signal_identifier (str): Specifies which instance of the selected signal to query. This parameter is necessary when you set the SIGNAL parameter to NIRFSG_VAL_SCRIPT_TRIGGER or Signal.MARKER_EVENT  . Otherwise, set the SIGNAL_IDENTIFIER parameter to "" (empty string). **Possible Values** :

                +------------------+-----------------------------+
                | Possible Value   | Description                 |
                +==================+=============================+
                | "marker0"        | Specifies Marker 0.         |
                +------------------+-----------------------------+
                | "marker1"        | Specifies Marker 1.         |
                +------------------+-----------------------------+
                | "marker2"        | Specifies Marker 2.         |
                +------------------+-----------------------------+
                | "marker3"        | Specifies Marker 3.         |
                +------------------+-----------------------------+
                | "scriptTrigger0" | Specifies Script Trigger 0. |
                +------------------+-----------------------------+
                | "scriptTrigger1" | Specifies Script Trigger 1. |
                +------------------+-----------------------------+
                | "scriptTrigger2" | Specifies Script Trigger 2. |
                +------------------+-----------------------------+
                | "scriptTrigger3" | Specifies Script Trigger 3. |
                +------------------+-----------------------------+

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        Returns:
            terminal_name (str): Returns the string to use as the source for other devices.

        

#### `def _init_with_options(self, resource_name, id_query=False, reset_device=False, option_string='')`

_init_with_options

        Opens a session to the device you specify as the RESOURCE_NAME and returns a ViSession handle that you use to identify the NI-RFSG device in all subsequent NI-RFSG method calls.

        This method also configures the device through the OPTION_STRING input.

        **Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Simulating an NI RF Signal Generator <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/simulate.html>`_

        Note: For multichannel devices such as the PXIe-5860, the resource name must include the channel number to use. The channel number is specified by appending /*ChannelNumber* to the device name, where *ChannelNumber* is the channel number (0, 1, etc.). For example, if the device name is PXI1Slot2 and you want to use channel 0, use the resource name PXI1Slot2/0.

        Note:
        One or more of the referenced properties are not in the Python API for this driver.

        Args:
            resource_name (str): Specifies the resource name of the device to initialize.

                For NI-DAQmx devices, the syntax is the device name specified in MAX. Typical default names for NI-DAQmx devices in MAX are Dev2 or PXISlot2. You can rename an NI-DAQmx device in MAX.

                You can also specify the name of an IVI logical name configured with the IVI Configuration utility. Refer to the *IVI* topic of the *Measurement & Automation Explorer Help* for more information.

                Note: NI-RFSG device names are not case-sensitive. However, all IVI names, such as logical names, are case-sensitive. If you use an IVI logical name, make sure the name is identical to the name shown in the IVI Configuration Utility.

            id_query (bool): Specifies whether you want NI-RFSG to perform an ID query.

                **Defined Values** :

                +-----------+--------------------------+
                | Value     | Description              |
                +===========+==========================+
                | True (1)  | Perform ID query.        |
                +-----------+--------------------------+
                | False (0) | Do not perform ID query. |
                +-----------+--------------------------+

            reset_device (bool): Specifies whether you want to reset the NI-RFSG device during the initialization procedure.

                **Defined Values** :

                +-----------+----------------------+
                | Value     | Description          |
                +===========+======================+
                | True (1)  | Reset device.        |
                +-----------+----------------------+
                | False (0) | Do not reset device. |
                +-----------+----------------------+

            option_string (dict): Specifies the initial value of certain properties for the session. The following table lists the properties and the name you pass in this parameter to identify the property.

                The format of this string consists of the following relations:
                "AttributeName=Value"

                where
                *AttributeName* is the name of the property and *Value* is the value to which the property is set. To set multiple properties, separate their assignments with a comma, as shown in the following option string:

                "RangeCheck=1,QueryInstrStatus=0,Cache=1,DriverSetup=AWG:pxi1slot4"

                The `DriverSetup string <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/driver_setup_string.html>`_ is required in order to simulate a specific device.


        Returns:
            new_vi (int): Returns a ViSession handle that you use to identify the NI-RFSG device in all subsequent NI-RFSG method calls.

        

#### `def _initiate(self)`

_initiate

        Initiates signal generation, causing the NI-RFSG device to leave the Configuration state and enter the Generation state.

        If the settings have not been committed to the device before you call this method, they are committed by this method. The operation returns when the RF output signal settles. To return to the Configuration state, call the abort method.

        **Supported Devices** : PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`_
        

#### `def perform_power_search(self)`

perform_power_search

        Performs a power search if the alc_control property is disabled.

        Calling this method disables modulation for a short time while the device levels the output signal.

        **Supported Devices** : PXIe-5654 with PXIe-5696

        **Related Topics**

        `Power Search <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5654_power_search.html>`_

        Note: Power search temporarily enables the ALC, so ensure the appropriate included cable is connected between the PXIe-5654 ALCIN connector and the PXIe-5696 ALCOUT connector to successfully perform a power search.
        

#### `def perform_thermal_correction(self)`

perform_thermal_correction

        Corrects for any signal drift due to environmental temperature variation when generating the same signal for extended periods of time without a parameter change.

        Under normal circumstances of short-term signal generation, NI-RFSG performs thermal correction automatically by ensuring stable power levels, and you do not need to call this method.

        Use this method when generating the same signal for an extended period of time in a temperature-fluctuating environment. The NI-RFSG device must be in the Generation state before calling this method.

        **Supported Devices** : PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Thermal Management <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/thermal_management.html>`_

        `Impairment Calibration <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/vector_calibration.html>`_
        

#### `def query_arb_waveform_capabilities(self)`

query_arb_waveform_capabilities

        Queries and returns the waveform capabilities of the NI-RFSG device.

        These capabilities are related to the current device configuration. The NI-RFSG device must be in the Configuration or the Generation state before calling this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Returns:
            max_number_waveforms (int): Returns the value of the arb_max_number_waveforms property. This value is the maximum number of waveforms you can write.

            waveform_quantum (int): Returns the value of the arb_waveform_quantum property. If the waveform quantum is *q*, then the size of the waveform that you write should be a multiple of *q*. The units are expressed in samples.

            min_waveform_size (int): Returns the value of the arb_waveform_size_min property. The number of samples of the waveform that you write must be greater than or equal to this value.

            max_waveform_size (int): Returns the value of the arb_waveform_size_max property. The number of samples of the waveform that you write must be less than or equal to this value.

        

#### `def read_and_download_waveform_from_file_tdms(self, waveform_name, file_path, waveform_index)`

read_and_download_waveform_from_file_tdms

        Reads the waveforms from a TDMS file and downloads one waveform into each of the NI RF vector signal generators.

        This method reads the following information from the TDMS file and writes it into the NI-RFSG session:

        - Sample Rate
        - PAPR
        - Runtime Scaling
        - RF Blanking Marker Locations
        - RF Blanking Enabled
        - Burst Start Locations
        - Burst Stop Locations
        - RF Blanking Marker Source
        - Signal Bandwidth
        - Waveform Size

        If RF blanking marker locations are present in the file but burst locations are not present, burst locations are calculated from RF blanking marker locations and stored in the NI-RFSG session.

        **Supported Devices** : PXIe-5820/5830/5831/5832/5840/5841/5842

        Args:
            waveform_name (str): Specifies the name used to store the waveform. This string is case-insensitive.

                Example:

                "waveform::waveform0"

            file_path (str): Specifies the absolute path to the TDMS file from which the NI-RFSG reads the waveforms.

            waveform_index (int): Specifies the index of the waveform to be read from the TDMS file.

        

#### `def reset_device(self)`

reset_device

        Performs a hard reset on the device which consists of the following actions:

        - Signal generation is stopped.
        - All routes are released.
        - External bidirectional terminals are tristated.
        - FPGAs are reset.
        - Hardware is configured to its default state.
        - All session properties are reset to their default states.

        During a device reset, routes of signals between this and other devices are released, regardless of which device created the route.

        - PXI-5610, PXI-5670/5671, PXIe-5672-- After calling this method, the device requires 25 seconds before returning to full functionality. NI-RFSG enforces this condition by adding a wait, if needed, the next time you try to access the device.

        **Supported Devices** : PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E

        **Related Topics**

        `Thermal Shutdown <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/thermal_shutdown_monitoring_5650_5651_5652.html>`_

        Note: You must call the reset_device method if the NI-RFSG device has shut down because of a high-temperature condition.
        

#### `def reset_with_defaults(self)`

reset_with_defaults

        Performs a software reset of the device, returning it to the default state and applying any initial default settings from the IVI Configuration Store.

        **Supported Devices** : PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696,PXI-5670/5671, PXIe-5672/5673/5673E
        

#### `def reset_with_options(self, steps_to_omit)`

reset_with_options

        Resets all properties to default values and specifies steps to omit during the reset process, such as signal routes.

        By default, this method exhibits the same behavior as Reset. You can specify steps to omit using the steps to omit parameter. For example, if you specify ResetWithOptionsStepsToOmit.ROUTES for the STEPS_TO_OMIT parameter, this method does not release signal routes during the reset process.

        When routes of signals between two devices are released, they are released regardless of which device created the route.

        To avoid resetting routes on PXIe-5820/5830/5831/5832/5840/5841/5842/5860 that are in use by NI-RFSA sessions, NI recommends using this method instead of Reset, with STEPS_TO_OMIT set to ResetWithOptionsStepsToOmit.ROUTES.

        **Supported Devices** : PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Triggers <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/triggers.html>`_

        `Events <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/events.html>`_

        Note:
        One or more of the referenced properties are not in the Python API for this driver.

        Args:
            steps_to_omit (Bitwise combination of enums.ResetWithOptionsStepsToOmit flags): Specifies a list of steps to skip during the reset process. The default value is ResetWithOptionsStepsToOmit.NONE, which specifies that no step is omitted during reset. **Defined Values** :

                +------------------------------------------------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | Name                                           | Value   | Description                                                                                                                                                                                                |
                +================================================+=========+============================================================================================================================================================================================================+
                | ResetWithOptionsStepsToOmit.NONE               | 0 (0x0) | No step is omitted during reset.                                                                                                                                                                           |
                +------------------------------------------------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ResetWithOptionsStepsToOmit.WAVEFORMS          | 1 (0x1) | Omits clearing waveforms.                                                                                                                                                                                  |
                +------------------------------------------------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ResetWithOptionsStepsToOmit.SCRIPTS            | 2 (0x2) | Omits clearing scripts.                                                                                                                                                                                    |
                +------------------------------------------------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ResetWithOptionsStepsToOmit.ROUTES             | 4 (0x4) | Omits the routing reset step. Routing is preserved after a reset. However, routing related properties are reset to default, and routing is released if the default properties are committed after a reset. |
                +------------------------------------------------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ResetWithOptionsStepsToOmit.DEEMBEDDING_TABLES | 8 (0x8) | Omits deleting de-embedding tables. This step is valid only for the PXIe-5830/5831/5832/5840.                                                                                                              |
                +------------------------------------------------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

                Note: ResetWithOptionsStepsToOmit.ROUTES is not supported in external calibration or alignment sessions.
                You can combine multiple enums.ResetWithOptionsStepsToOmit flags using the bitwise OR (|) operator.

        

#### `def select_arb_waveform(self, waveform_name)`

select_arb_waveform

        Specifies the waveform that is generated upon a call to the _initiate method when the generation_mode property is set to GenerationMode.ARB_WAVEFORM.

        You must specify a waveform using the NAME parameter if you have written multiple waveforms. The NI-RFSG device must be in the Configuration state before you call this method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/assigning_properties_or_attributes_to_a_waveform.html>`_

        Note:
        One or more of the referenced properties are not in the Python API for this driver.

        Args:
            waveform_name (str): Specifies the name of the stored waveform to generate. This is a case-insensitive alphanumeric string that does not use reserved words. NI-RFSG sets the arb_selected_waveform property to this value.

        

#### `def self_cal(self)`

self_cal

        Performs an internal self-calibration on the device and associated modules that support self-calibration.

        If the calibration is successful, new calibration data and constants are stored in the onboard nonvolatile memory of the module.

        The PXIe-5841 maintains separate self-calibration data for both the PXIe-5841 standalone and when associated with the PXIe-5655. Use this method once for each intended configuration.

        **Supported Devices** : PXI-5610, PXIe-5653, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Note: If there is an existing NI-RFSA session open for the same PXIe-5820/5830/5831/5832/5840/5841/5842/5860 while this method runs, it may remain open but cannot be used for operations that access the hardware, for example niRFSA_Commit or niRFSA_Initiate. For the existing open session to use the new self-calibration data, the session will need to be closed and reopened.

        **PXIe-5860**

        While this VI is running on one channel, if there are any existing NI-RFSG or NI-RFSA sessions open on the other channel, they may remain open but cannot be used for operations that access the hardware, for example niRFSG Commit or niRFSG Initiate or niRFSA Commit or niRFSA Initiate. For the existing open session to use the new self-calibration data, the session will need to be closed and reopened.
        

#### `def self_calibrate_range(self, steps_to_omit, min_frequency, max_frequency, min_power_level, max_power_level)`

self_calibrate_range

        Self-calibrates all configurations within the specified frequency and peak power level limits.

        Self-calibration range data is valid until you restart the system or call the clear_self_calibrate_range method.

        NI recommends that no external signals are present on the RF In or IQ In ports during the calibration.

        For best results, NI recommends that you perform self-calibration without omitting any steps. However, if certain aspects of performance are less important for your application, you can omit certain steps for faster calibration.

        **Supported Devices** : PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842

        Note: - This method does not update self-calibration date and temperature.

         - If there is an existing NI-RFSA session open for the same PXIe-5644/5645/5646, it may remain open but cannot be used while this method runs.

         - If there is an existing NI-RFSA session open for the same PXIe-5820/5830/5831/5832/5840/5841/5842 while this method runs, it may remain open but cannot be used for operations that access the hardware, for example niRFSA_Commit or niRFSA_Initiate.

        Args:
            steps_to_omit (Bitwise combination of enums.SelfCalibrateRangeStepsToOmit flags): Specifies which calibration steps to skip during the self-calibration process. The default value is an empty array, which indicates that no calibration steps are omitted.

                **Default Value** : SelfCalibrateRangeStepsToOmit.OMIT_NONE

                **Defined Values:**

                +-----------------------------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
                | Name                                                | Value     | Description                                                                                                         |
                +=====================================================+===========+=====================================================================================================================+
                | SelfCalibrateRangeStepsToOmit.OMIT_NONE             | 0 (0x0)   | No calibration steps are omitted.                                                                                   |
                +-----------------------------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
                | SelfCalibrateRangeStepsToOmit.LO_SELF_CAL           | 1 (0x1)   | Omits the LO Self Cal step. If you omit this step, the power level of the LO is not adjusted.                       |
                +-----------------------------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
                | SelfCalibrateRangeStepsToOmit.POWER_LEVEL_ACCURACY  | 2 (0x2)   | Omits the Power Level Accuracy step. If you omit this step, the power level accuracy of the device is not adjusted. |
                +-----------------------------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
                | SelfCalibrateRangeStepsToOmit.RESIDUAL_LO_POWER     | 4 (0x4)   | Omits the Residual LO Power step. If you omit this step, the Residual LO Power performance is not adjusted.         |
                +-----------------------------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
                | SelfCalibrateRangeStepsToOmit.IMAGE_SUPPRESSION     | 8 (0x8)   | Omits the Image Suppression step. If you omit this step, the Residual Sideband Image performance is not adjusted.   |
                +-----------------------------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
                | SelfCalibrateRangeStepsToOmit.SYNTHESIZER_ALIGNMENT | 16 (0x10) | Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.    |
                +-----------------------------------------------------+-----------+---------------------------------------------------------------------------------------------------------------------+

                Note: You can combine multiple enums.SelfCalibrateRangeStepsToOmit flags using the bitwise OR (|) operator.

            min_frequency (float): Specifies the minimum frequency to calibrate.

            max_frequency (float): Specifies the maximum frequency to calibrate.

            min_power_level (float): Specifies the minimum power level to calibrate.

            max_power_level (float): Specifies the maximum power level to calibrate.

        

#### `def set_arb_waveform_next_write_position(self, waveform_name, relative_to, offset)`

set_arb_waveform_next_write_position

        Configures the start position to use for writing a waveform before calling the WriteArbWaveform method.

        This method allows you to write to arbitrary locations within the waveform. These settings apply only to the next write to the waveform specified by the **name** input of the allocate_arb_waveform method or the WriteArbWaveform method. Subsequent writes to that waveform begin where the last write ended, unless this method is called again.

        **Supported Devices** : PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Note: If you use this method to write the waveform that is currently generating, an undefined output may result.

        Args:
            waveform_name (str): Specifies the name of the waveform. This string is case-insensitive and alphanumeric, and it cannot use `reserved words <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/scripting_instructions.html>`_.

            relative_to (enums.RelativeTo): Specifies the reference position in the waveform. The position and OFFSET together determine where to start loading data into the waveform.

                **Defined Values:**

                +------------------------------+---------------+------------------------------------------------------------------+
                | Name                         | Value         | Description                                                      |
                +==============================+===============+==================================================================+
                | RelativeTo.START_OF_WAVEFORM | 8000 (0x1f40) | The reference position is relative to the start of the waveform. |
                +------------------------------+---------------+------------------------------------------------------------------+
                | RelativeTo.CURRENT_POSITION  | 8001 (0x1f41) | The reference position is relative to the current position.      |
                +------------------------------+---------------+------------------------------------------------------------------+

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

            offset (int): Specifies the offset from the **relative to** parameter at which to start loading the data into the waveform.

        

#### `def wait_until_settled(self, max_time_milliseconds=hightime.timedelta(seconds=10.0))`

wait_until_settled

        Waits until the RF output signal has settled. This method is useful for devices that support changes while in the Generation state.

        Call this method after making a dynamic change to wait for the output signal to settle.

        You can also call this method after calling the commit method to wait for changes to settle. The wait_until_settled method is not required after calling the _initiate method because the _initiate automatically waits for the output to settle.

        **Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Args:
            max_time_milliseconds (hightime.timedelta, datetime.timedelta, or int in milliseconds): Specifies the maximum time the method waits for the output to settle. If the maximum time is exceeded, this method returns an error. The units are expressed in milliseconds.

                **Default Value** : 10000

        

#### `def _write_arb_waveform_complex_f32(self, waveform_name, waveform_data_array, more_data_pending)`

_write_arb_waveform_complex_f32

        Writes an arbitrary waveform to the NI-RFSG device starting at the position of the last data written in onboard memory.

        This method accepts the complex baseband data in the form of complex singles. If the waveform to write is already allocated using the allocate_arb_waveform method, the more_data_pending parameter is ignored. The PXI-5670/5671 must be in the Configuration state before you call this method. When streaming is enabled, you can call this method when the PXIe-5672/5673/5673E or PXIe-5820/5830/5831/5832/5840/5841/5842/5860 is in the Generation state.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Streaming <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/streaming.html>`_

        `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/assigning-properties-or-properties-to-a-wavef.html>`_

        Note: On the PXIe-5644/5645/5646, PXIe-5672/5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860, the more_data_pending parameter is always ignored. To write data in blocks on these devices, you must allocate the waveform before writing it.

        Args:
            waveform_name (str): Specifies the name used to identify the waveform. This string is case-insensitive and alphanumeric, and it does not use reserved words.

            waveform_data_array (numpy.array(dtype=numpy.complex64)): Specifies the array of data to load into the waveform. The array must have at least as many elements as the value in the **size_in_samples** parameter in the allocate_arb_waveform method.

            more_data_pending (bool): Specifies whether or not the data block contains the end of the waveform. Set this parameter to True to allow data to be appended later to the waveform. Splitting the waveform into multiple data blocks can reduce the memory requirements of the write operation. Append data to a previously written waveform by using the same waveform in the WAVEFORM_NAME parameter. Set more_data_pending to False to indicate that this data block contains the end of the waveform. If the waveform is already allocated, this parameter is ignored.

                Note:
                One or more of the referenced properties are not in the Python API for this driver.

        

#### `def _write_arb_waveform_complex_f64(self, waveform_name, waveform_data_array, more_data_pending)`

_write_arb_waveform_complex_f64

        Writes an arbitrary waveform to the NI-RFSG device starting at the position of the last data written in onboard memory.

        This method accepts the complex baseband data in the form of complex doubles. If the waveform to write is already allocated using the allocate_arb_waveform, the more_data_pending parameter is ignored. The PXI-5670/5671 must be in the Configuration state before you call this method. When streaming is enabled, you can call this method when the PXIe-5672/5673/5673E or PXIe-5820/5830/5831/5832/5840/5841/5842 is in the Generation state.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842

        **Related Topics**

        `Streaming <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/streaming.html>`_

        `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/assigning-properties-or-properties-to-a-wavef.html>`_

        Note: On the PXIe-5644/5645/5646, PXIe-5672/5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842, the more_data_pending parameter is always ignored. To write data in blocks on these devices, you must allocate the waveform before writing it.

        Args:
            waveform_name (str): Specifies the name used to identify the waveform. This string is case-insensitive and alphanumeric, and it does not use reserved words.

            waveform_data_array (numpy.array(dtype=numpy.complex128)): Specifies the array of data to load into the waveform. The array must have at least as many elements as the value in the **size_in_samples** parameter in the allocate_arb_waveform method.

            more_data_pending (bool): Specifies whether or not the data block contains the end of the waveform. Set this parameter to True to allow data to be appended later to the waveform. Splitting the waveform into multiple data blocks can reduce the memory requirements of the write operation. Append data to a previously written waveform by using the same waveform in the **name** parameter. Set more_data_pending to False to indicate that this data block contains the end of the waveform. If the waveform is already allocated, this parameter is ignored.

        

#### `def _write_arb_waveform_complex_i16(self, waveform_name, waveform_data_array)`

_write_arb_waveform_complex_i16

        Writes an arbitrary waveform to the NI-RFSG device starting at the position of the last data written in onboard memory.

        This method accepts the interleaved I/Q data of a complex baseband signal. The PXI-5670/5671 must be in the Configuration state before you call this method. When streaming is enabled, this method can be called when the PXIe-5672/5673/5673E or PXIe-5820/5830/5831/5832/5840/5841/5842/5860 is in the Generation state.

        **Supported Devices** : PXIe-5644/5645/5646, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Streaming <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/streaming.html>`_

        `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/assigning-properties-or-properties-to-a-wavef.html>`_

        Note: This method only supports PowerLevelType.PEAK mode as specified in the power_level_type property. If you download a waveform when using this method, you cannot set the power_level_type to PowerLevelType.AVERAGE without causing error in the output.

        Args:
            waveform_name (str): Specifies the name used to identify the waveform. This string is case-insensitive and alphanumeric, and it does not use reserved words.

            waveform_data_array (numpy.array(dtype=numpy.int16)): Specifies the array of data to load into the waveform. The array must have at least as many elements as the value in the **size_in_samples** parameter in the allocate_arb_waveform method.

        

#### `def write_arb_waveform(self, waveform_name, waveform_data_array, more_data_pending=False)`

write_arb_waveform

        Writes an arbitrary waveform to the NI-RFSG device starting at the position of the last data written in onboard memory.

        This method accepts the complex baseband data in the form of numpy array of numpy.complex64 or numpy.complex128 or interleaved numpy array of numpy.int16. If the waveform to write is already allocated using the allocate_arb_waveform, the more_data_pending parameter is ignored. The PXI-5670/5671 must be in the Configuration state before you call this method. When streaming is enabled, you can call this method when the PXIe-5672/5673/5673E or PXIe-5820/5830/5831/5832/5840/5841/5842/5860 is in the Generation state.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Streaming <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/streaming.html>`_

        `Assigning Properties or Properties to a Waveform <https://www.ni.com/docs/en-US/bundle/ni-rfsg/page/assigning-properties-or-properties-to-a-wavef.html>`_

        Note: On the PXIe-5644/5645/5646, PXIe-5672/5673/5673E, and PXIe-5820/5830/5831/5832/5840/5841/5842/5860, the more_data_pending parameter is always ignored. To write data in blocks on these devices, you must allocate the waveform before writing it.
        If you are writing interleaved numpy array of numpy.int16, then this method only supports PowerLevelType.PEAK mode as specified in the power_level_type property. If you download a waveform as interleaved numpy array of numpy.int16 when using this method, you cannot set the power_level_type to PowerLevelType.AVERAGE without causing error in the output.

        Args:
            waveform_name (str): Specifies the name used to identify the waveform. This string is case-insensitive and alphanumeric, and it does not use reserved words.

            waveform_data_array (numpy array of numpy.complex64, numpy array of numpy.complex128 or interleaved complex data in the form of numpy array of numpy.int16): Specifies the array of data to load into the waveform. The array must have at least as many elements as the value in the **size_in_samples** parameter in the allocate_arb_waveform method.

            more_data_pending (bool): Specifies whether or not the data block contains the end of the waveform. Set this parameter to True to allow data to be appended later to the waveform. Splitting the waveform into multiple data blocks can reduce the memory requirements of the write operation. Append data to a previously written waveform by using the same waveform in the **name** parameter. Set more_data_pending to False to indicate that this data block contains the end of the waveform. If the waveform is already allocated, this parameter is ignored.

        

#### `def write_script(self, script)`

write_script

        Writes a script to the device to control waveform generation in Script mode.

        First, configure your device for Script mode by setting the generation_mode property. The NI-RFSG device must be in the Configuration state before calling the write_script method.

        **Supported Devices** : PXIe-5644/5645/5646, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Scripting Instructions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/scripting_instructions.html>`_--Refer to this topic for more information about VST restrictions on scripts.

        `Common Scripting Use Cases <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/scripting_use_cases.html>`_

        Note: If you are using an RF vector signal transceiver (VST) device, some script instructions may not be supported.

        Args:
            script (str): Specifies a string containing a syntactically correct script. NI-RFSG supports multiple scripts that are selected with the selected_script property. Refer to `Scripting Instructions <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/scripting_instructions.html>`_ for more information about using scripts.

        

#### `def _close(self)`

_close

        Aborts any signal generation in progress and destroys the instrument driver session.

        **Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `NI-RFSG Instrument Driver Programming Flow <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/progflow.html>`_

        `NI-RFSG Programming State Model <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/ni_5670_programming_state_model.html>`_
        

#### `def self_test(self)`

self_test

        Performs a self-test on the NI-RFSG device and returns the test results.

        This method performs a simple series of tests to ensure that the NI-RFSG device is powered up and responding.

        This method does not affect external I/O connections or connections between devices. Complete functional testing and calibration are not performed by this method. The NI-RFSG device must be in the Configuration state before you call this method.

        **Supported Devices** : PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Device Warm-Up <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/warmup.html>`_

        +----------------+------------------+
        | Self-Test Code | Description      |
        +================+==================+
        | 0              | Passed self-test |
        +----------------+------------------+
        | 1              | Self-test failed |
        +----------------+------------------+
        

#### `def reset(self)`

reset

        Resets all properties to their default values and moves the NI-RFSG device to the Configuration state.

        This method aborts the generation, deletes all de-embedding tables, clears all routes, and resets session properties to their initial values. During a reset, routes of signals between this and other devices are released, regardless of which device created the route.

        Generally, calling this method instead of the reset_device method is acceptable. The Reset method executes faster than the reset_device method.

        To avoid resetting routes on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860 that are in use by NI-RFSA sessions, NI recommends using the reset_with_options method, with **stepsToOmit** set to ResetWithOptionsStepsToOmit.ROUTES .

        **Supported Devices** : PXI-5610, PXIe-5611, PXIe-5644/5645/5646, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        Note: This method resets all configured routes for the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860 in NI-RFSA and NI-RFSG.
        

#### `def _self_test(self)`

_self_test

        Performs a self-test on the NI-RFSG device and returns the test results.

        This method performs a simple series of tests to ensure that the NI-RFSG device is powered up and responding.

        This method does not affect external I/O connections or connections between devices. Complete functional testing and calibration are not performed by this method. The NI-RFSG device must be in the Configuration state before you call this method.

        **Supported Devices** : PXI-5610, PXIe-5611, PXI/PXIe-5650/5651/5652, PXIe-5653/5654/5654 with PXIe-5696, PXI-5670/5671, PXIe-5672/5673/5673E, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

        **Related Topics**

        `Device Warm-Up <https://www.ni.com/docs/en-US/bundle/rfsg/page/rfsg/warmup.html>`_

        Returns:
            self_test_result (int): This parameter contains the value returned from the NI-RFSG device self test.

                +----------------+------------------+
                | Self-Test Code | Description      |
                +================+==================+
                | 0              | Self test passed |
                +----------------+------------------+
                | 1              | Self test failed |
                +----------------+------------------+

            self_test_message (str): Returns the self-test response string from the NI-RFSG device. For an explanation of the string contents, refer to the **status** parameter of this method.

                You must pass a ViChar array with at least 256 bytes.

        

<!--NI_PYTHON_API repo=nimi-python path=generated/nirfsg/nirfsg/unit_tests/_matchers.py -->
## PYTHON MODULE: generated/nirfsg/nirfsg/unit_tests/_matchers.py

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

<!--NI_PYTHON_API repo=nimi-python path=generated/nirfsg/nirfsg/unit_tests/_mock_helper.py -->
## PYTHON MODULE: generated/nirfsg/nirfsg/unit_tests/_mock_helper.py

### `class MockFunctionCallError(Exception)`

#### `def __init__(self, function, param=None)`

### `class SideEffectsHelper(object)`

#### `def __init__(self)`

#### `def __getitem__(self, func)`

#### `def __setitem__(self, func, val)`

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

#### `def set_side_effects_and_return_values(self, mock_library)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nirfsg/setup.py -->
## PYTHON MODULE: generated/nirfsg/setup.py

### `def read_contents(file_to_read)`

<!--NI_PYTHON_API repo=nimi-python path=generated/niscope/niscope/__init__.py -->
## PYTHON MODULE: generated/niscope/niscope/__init__.py

### `def get_diagnostic_information()`

Get diagnostic information about the system state that is suitable for printing or logging

    returns: dict

    note: Python bitness may be incorrect when running in a virtual environment
    

### `def print_diagnostic_information()`

Print diagnostic information in a format suitable for issue report

    note: Python bitness may be incorrect when running in a virtual environment
    

<!--NI_PYTHON_API repo=nimi-python path=generated/niscope/niscope/_attributes.py -->
## PYTHON MODULE: generated/niscope/niscope/_attributes.py

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

Class for attributes that use enums internally but are exposed in the niscope Python module as something else, thus need conversion.

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

<!--NI_PYTHON_API repo=nimi-python path=generated/niscope/niscope/_converters.py -->
## PYTHON MODULE: generated/niscope/niscope/_converters.py

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
    

<!--NI_PYTHON_API repo=nimi-python path=generated/niscope/niscope/_grpc_stub_interpreter.py -->
## PYTHON MODULE: generated/niscope/niscope/_grpc_stub_interpreter.py

### `class GrpcStubInterpreter(object)`

Interpreter for interacting with a gRPC Stub class

#### `def __init__(self, grpc_options)`

#### `def set_session_handle(self, value=session_grpc_types.Session())`

#### `def get_session_handle(self)`

#### `def _invoke(self, func, request, metadata=None)`

#### `def abort(self)`

#### `def acquisition_status(self)`

#### `def actual_meas_wfm_size(self, array_meas_function)`

#### `def actual_num_wfms(self, channel_list)`

#### `def add_waveform_processing(self, channel_list, meas_function)`

#### `def auto_setup(self)`

#### `def cal_fetch_date(self, which_one)`

#### `def cal_fetch_temperature(self, which_one)`

#### `def self_cal(self, channel_list, option)`

#### `def clear_waveform_measurement_stats(self, channel_list, clearable_measurement_function)`

#### `def clear_waveform_processing(self, channel_list)`

#### `def commit(self)`

#### `def configure_chan_characteristics(self, channel_list, input_impedance, max_input_frequency)`

#### `def configure_equalization_filter_coefficients(self, channel_list, coefficients)`

#### `def configure_horizontal_timing(self, min_sample_rate, min_num_pts, ref_position, num_records, enforce_realtime)`

#### `def configure_ref_levels(self, low, mid, high)`

#### `def configure_trigger_digital(self, trigger_source, slope, holdoff, delay)`

#### `def configure_trigger_edge(self, trigger_source, level, slope, trigger_coupling, holdoff, delay)`

#### `def configure_trigger_hysteresis(self, trigger_source, level, hysteresis, slope, trigger_coupling, holdoff, delay)`

#### `def configure_trigger_immediate(self)`

#### `def configure_trigger_software(self, holdoff, delay)`

#### `def configure_trigger_video(self, trigger_source, enable_dc_restore, signal_format, event, line_number, polarity, trigger_coupling, holdoff, delay)`

#### `def configure_trigger_window(self, trigger_source, low_level, high_level, window_mode, trigger_coupling, holdoff, delay)`

#### `def configure_vertical(self, channel_list, range, offset, coupling, probe_attenuation, enabled)`

#### `def disable(self)`

#### `def export_attribute_configuration_buffer(self)`

#### `def export_attribute_configuration_file(self, file_path)`

#### `def fetch(self, channel_list, timeout, num_samples)`

#### `def fetch_into_numpy(self, channel_list, timeout, num_samples)`

#### `def fetch_array_measurement(self, channel_list, timeout, array_meas_function, measurement_waveform_size)`

#### `def fetch_binary16_into_numpy(self, channel_list, timeout, num_samples)`

#### `def fetch_binary32_into_numpy(self, channel_list, timeout, num_samples)`

#### `def fetch_binary8_into_numpy(self, channel_list, timeout, num_samples)`

#### `def fetch_measurement_stats(self, channel_list, timeout, scalar_meas_function)`

#### `def get_attribute_vi_boolean(self, channel_list, attribute_id)`

#### `def get_attribute_vi_int32(self, channel_list, attribute_id)`

#### `def get_attribute_vi_int64(self, channel_list, attribute_id)`

#### `def get_attribute_vi_real64(self, channel_list, attribute_id)`

#### `def get_attribute_vi_string(self, channel_list, attribute_id)`

#### `def get_channel_names(self, indices)`

#### `def get_equalization_filter_coefficients(self, channel, number_of_coefficients)`

#### `def get_error(self)`

#### `def import_attribute_configuration_buffer(self, configuration)`

#### `def import_attribute_configuration_file(self, file_path)`

#### `def init_with_options(self, resource_name, id_query, reset_device, option_string)`

#### `def initiate_acquisition(self)`

#### `def lock(self)`

#### `def probe_compensation_signal_start(self)`

#### `def probe_compensation_signal_stop(self)`

#### `def read(self, channel_list, timeout, num_samples)`

#### `def reset_device(self)`

#### `def reset_with_defaults(self)`

#### `def send_software_trigger_edge(self, which_trigger)`

#### `def set_attribute_vi_boolean(self, channel_list, attribute_id, value)`

#### `def set_attribute_vi_int32(self, channel_list, attribute_id, value)`

#### `def set_attribute_vi_int64(self, channel_list, attribute_id, value)`

#### `def set_attribute_vi_real64(self, channel_list, attribute_id, value)`

#### `def set_attribute_vi_string(self, channel_list, attribute_id, value)`

#### `def set_runtime_environment(self, environment, environment_version, reserved1, reserved2)`

#### `def unlock(self)`

#### `def close(self)`

#### `def error_message(self, error_code)`

#### `def reset(self)`

#### `def self_test(self)`

<!--NI_PYTHON_API repo=nimi-python path=generated/niscope/niscope/_library.py -->
## PYTHON MODULE: generated/niscope/niscope/_library.py

### `class Library(object)`

Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    

#### `def __init__(self, ctypes_library)`

#### `def _get_library_function(self, name)`

#### `def niScope_Abort(self, vi)`

#### `def niScope_AcquisitionStatus(self, vi, acquisition_status)`

#### `def niScope_ActualMeasWfmSize(self, vi, array_meas_function, meas_waveform_size)`

#### `def niScope_ActualNumWfms(self, vi, channel_list, num_wfms)`

#### `def niScope_AddWaveformProcessing(self, vi, channel_list, meas_function)`

#### `def niScope_AutoSetup(self, vi)`

#### `def niScope_CalFetchDate(self, vi, which_one, year, month, day)`

#### `def niScope_CalFetchTemperature(self, vi, which_one, temperature)`

#### `def niScope_CalSelfCalibrate(self, vi, channel_list, option)`

#### `def niScope_ClearWaveformMeasurementStats(self, vi, channel_list, clearable_measurement_function)`

#### `def niScope_ClearWaveformProcessing(self, vi, channel_list)`

#### `def niScope_Commit(self, vi)`

#### `def niScope_ConfigureChanCharacteristics(self, vi, channel_list, input_impedance, max_input_frequency)`

#### `def niScope_ConfigureEqualizationFilterCoefficients(self, vi, channel_list, number_of_coefficients, coefficients)`

#### `def niScope_ConfigureHorizontalTiming(self, vi, min_sample_rate, min_num_pts, ref_position, num_records, enforce_realtime)`

#### `def niScope_ConfigureRefLevels(self, vi, low, mid, high)`

#### `def niScope_ConfigureTriggerDigital(self, vi, trigger_source, slope, holdoff, delay)`

#### `def niScope_ConfigureTriggerEdge(self, vi, trigger_source, level, slope, trigger_coupling, holdoff, delay)`

#### `def niScope_ConfigureTriggerHysteresis(self, vi, trigger_source, level, hysteresis, slope, trigger_coupling, holdoff, delay)`

#### `def niScope_ConfigureTriggerImmediate(self, vi)`

#### `def niScope_ConfigureTriggerSoftware(self, vi, holdoff, delay)`

#### `def niScope_ConfigureTriggerVideo(self, vi, trigger_source, enable_dc_restore, signal_format, event, line_number, polarity, trigger_coupling, holdoff, delay)`

#### `def niScope_ConfigureTriggerWindow(self, vi, trigger_source, low_level, high_level, window_mode, trigger_coupling, holdoff, delay)`

#### `def niScope_ConfigureVertical(self, vi, channel_list, range, offset, coupling, probe_attenuation, enabled)`

#### `def niScope_Disable(self, vi)`

#### `def niScope_ExportAttributeConfigurationBuffer(self, vi, size_in_bytes, configuration)`

#### `def niScope_ExportAttributeConfigurationFile(self, vi, file_path)`

#### `def niScope_Fetch(self, vi, channel_list, timeout, num_samples, waveform, wfm_info)`

#### `def niScope_FetchArrayMeasurement(self, vi, channel_list, timeout, array_meas_function, measurement_waveform_size, meas_wfm, wfm_info)`

#### `def niScope_FetchBinary16(self, vi, channel_list, timeout, num_samples, waveform, wfm_info)`

#### `def niScope_FetchBinary32(self, vi, channel_list, timeout, num_samples, waveform, wfm_info)`

#### `def niScope_FetchBinary8(self, vi, channel_list, timeout, num_samples, waveform, wfm_info)`

#### `def niScope_FetchMeasurementStats(self, vi, channel_list, timeout, scalar_meas_function, result, mean, stdev, min, max, num_in_stats)`

#### `def niScope_GetAttributeViBoolean(self, vi, channel_list, attribute_id, value)`

#### `def niScope_GetAttributeViInt32(self, vi, channel_list, attribute_id, value)`

#### `def niScope_GetAttributeViInt64(self, vi, channel_list, attribute_id, value)`

#### `def niScope_GetAttributeViReal64(self, vi, channel_list, attribute_id, value)`

#### `def niScope_GetAttributeViString(self, vi, channel_list, attribute_id, buf_size, value)`

#### `def niScope_GetChannelNameFromString(self, vi, indices, buffer_size, names)`

#### `def niScope_GetEqualizationFilterCoefficients(self, vi, channel, number_of_coefficients, coefficients)`

#### `def niScope_GetError(self, vi, error_code, buffer_size, description)`

#### `def niScope_ImportAttributeConfigurationBuffer(self, vi, size_in_bytes, configuration)`

#### `def niScope_ImportAttributeConfigurationFile(self, vi, file_path)`

#### `def niScope_InitWithOptions(self, resource_name, id_query, reset_device, option_string, vi)`

#### `def niScope_InitiateAcquisition(self, vi)`

#### `def niScope_LockSession(self, vi, caller_has_lock)`

#### `def niScope_ProbeCompensationSignalStart(self, vi)`

#### `def niScope_ProbeCompensationSignalStop(self, vi)`

#### `def niScope_Read(self, vi, channel_list, timeout, num_samples, waveform, wfm_info)`

#### `def niScope_ResetDevice(self, vi)`

#### `def niScope_ResetWithDefaults(self, vi)`

#### `def niScope_SendSoftwareTriggerEdge(self, vi, which_trigger)`

#### `def niScope_SetAttributeViBoolean(self, vi, channel_list, attribute_id, value)`

#### `def niScope_SetAttributeViInt32(self, vi, channel_list, attribute_id, value)`

#### `def niScope_SetAttributeViInt64(self, vi, channel_list, attribute_id, value)`

#### `def niScope_SetAttributeViReal64(self, vi, channel_list, attribute_id, value)`

#### `def niScope_SetAttributeViString(self, vi, channel_list, attribute_id, value)`

#### `def niScope_SetRuntimeEnvironment(self, environment, environment_version, reserved1, reserved2)`

#### `def niScope_UnlockSession(self, vi, caller_has_lock)`

#### `def niScope_close(self, vi)`

#### `def niScope_error_message(self, vi, error_code, error_message)`

#### `def niScope_reset(self, vi)`

#### `def niScope_self_test(self, vi, self_test_result, self_test_message)`

<!--NI_PYTHON_API repo=nimi-python path=generated/niscope/niscope/_library_interpreter.py -->
## PYTHON MODULE: generated/niscope/niscope/_library_interpreter.py

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

#### `def acquisition_status(self)`

#### `def actual_meas_wfm_size(self, array_meas_function)`

#### `def actual_num_wfms(self, channel_list)`

#### `def add_waveform_processing(self, channel_list, meas_function)`

#### `def auto_setup(self)`

#### `def cal_fetch_date(self, which_one)`

#### `def cal_fetch_temperature(self, which_one)`

#### `def self_cal(self, channel_list, option)`

#### `def clear_waveform_measurement_stats(self, channel_list, clearable_measurement_function)`

#### `def clear_waveform_processing(self, channel_list)`

#### `def commit(self)`

#### `def configure_chan_characteristics(self, channel_list, input_impedance, max_input_frequency)`

#### `def configure_equalization_filter_coefficients(self, channel_list, coefficients)`

#### `def configure_horizontal_timing(self, min_sample_rate, min_num_pts, ref_position, num_records, enforce_realtime)`

#### `def configure_ref_levels(self, low, mid, high)`

#### `def configure_trigger_digital(self, trigger_source, slope, holdoff, delay)`

#### `def configure_trigger_edge(self, trigger_source, level, slope, trigger_coupling, holdoff, delay)`

#### `def configure_trigger_hysteresis(self, trigger_source, level, hysteresis, slope, trigger_coupling, holdoff, delay)`

#### `def configure_trigger_immediate(self)`

#### `def configure_trigger_software(self, holdoff, delay)`

#### `def configure_trigger_video(self, trigger_source, enable_dc_restore, signal_format, event, line_number, polarity, trigger_coupling, holdoff, delay)`

#### `def configure_trigger_window(self, trigger_source, low_level, high_level, window_mode, trigger_coupling, holdoff, delay)`

#### `def configure_vertical(self, channel_list, range, offset, coupling, probe_attenuation, enabled)`

#### `def disable(self)`

#### `def export_attribute_configuration_buffer(self)`

#### `def export_attribute_configuration_file(self, file_path)`

#### `def fetch(self, channel_list, timeout, num_samples)`

#### `def fetch_into_numpy(self, channel_list, num_samples, waveform, timeout)`

#### `def fetch_array_measurement(self, channel_list, timeout, array_meas_function, measurement_waveform_size)`

#### `def fetch_binary16_into_numpy(self, channel_list, num_samples, waveform, timeout)`

#### `def fetch_binary32_into_numpy(self, channel_list, num_samples, waveform, timeout)`

#### `def fetch_binary8_into_numpy(self, channel_list, num_samples, waveform, timeout)`

#### `def fetch_measurement_stats(self, channel_list, timeout, scalar_meas_function)`

#### `def get_attribute_vi_boolean(self, channel_list, attribute_id)`

#### `def get_attribute_vi_int32(self, channel_list, attribute_id)`

#### `def get_attribute_vi_int64(self, channel_list, attribute_id)`

#### `def get_attribute_vi_real64(self, channel_list, attribute_id)`

#### `def get_attribute_vi_string(self, channel_list, attribute_id)`

#### `def get_channel_names(self, indices)`

#### `def get_equalization_filter_coefficients(self, channel, number_of_coefficients)`

#### `def get_error(self)`

#### `def import_attribute_configuration_buffer(self, configuration)`

#### `def import_attribute_configuration_file(self, file_path)`

#### `def init_with_options(self, resource_name, id_query, reset_device, option_string)`

#### `def initiate_acquisition(self)`

#### `def lock(self)`

#### `def probe_compensation_signal_start(self)`

#### `def probe_compensation_signal_stop(self)`

#### `def read(self, channel_list, timeout, num_samples)`

#### `def reset_device(self)`

#### `def reset_with_defaults(self)`

#### `def send_software_trigger_edge(self, which_trigger)`

#### `def set_attribute_vi_boolean(self, channel_list, attribute_id, value)`

#### `def set_attribute_vi_int32(self, channel_list, attribute_id, value)`

#### `def set_attribute_vi_int64(self, channel_list, attribute_id, value)`

#### `def set_attribute_vi_real64(self, channel_list, attribute_id, value)`

#### `def set_attribute_vi_string(self, channel_list, attribute_id, value)`

#### `def set_runtime_environment(self, environment, environment_version, reserved1, reserved2)`

#### `def unlock(self)`

#### `def close(self)`

#### `def error_message(self, error_code)`

#### `def reset(self)`

#### `def self_test(self)`

<!--NI_PYTHON_API repo=nimi-python path=generated/niscope/niscope/_library_singleton.py -->
## PYTHON MODULE: generated/niscope/niscope/_library_singleton.py

### `def _get_library_name()`

### `def _get_library_type()`

### `def get()`

get

    Returns the library.Library singleton for niscope.
    

<!--NI_PYTHON_API repo=nimi-python path=generated/niscope/niscope/enums.py -->
## PYTHON MODULE: generated/niscope/niscope/enums.py

### `class AcquisitionStatus(Enum)`

### `class AcquisitionType(Enum)`

### `class ArrayMeasurement(Enum)`

### `class CableSenseMode(Enum)`

### `class _CalibrationTypes(Enum)`

### `class ClearableMeasurement(Enum)`

### `class FIRFilterWindow(Enum)`

### `class FetchRelativeTo(Enum)`

### `class FilterType(Enum)`

### `class FlexFIRAntialiasFilterType(Enum)`

### `class GlitchCondition(Enum)`

### `class GlitchPolarity(Enum)`

### `class Option(Enum)`

### `class PercentageMethod(Enum)`

### `class RISMethod(Enum)`

### `class RefLevelUnits(Enum)`

### `class RefTriggerDetectorLocation(Enum)`

### `class RuntPolarity(Enum)`

### `class RuntTimeCondition(Enum)`

### `class ScalarMeasurement(Enum)`

### `class TerminalConfiguration(Enum)`

### `class TriggerCoupling(Enum)`

### `class TriggerModifier(Enum)`

### `class TriggerSlope(Enum)`

### `class TriggerType(Enum)`

### `class TriggerWindowMode(Enum)`

### `class VerticalCoupling(Enum)`

### `class VideoPolarity(Enum)`

### `class VideoSignalFormat(Enum)`

### `class VideoTriggerEvent(Enum)`

### `class WhichTrigger(Enum)`

### `class WidthCondition(Enum)`

### `class WidthPolarity(Enum)`

<!--NI_PYTHON_API repo=nimi-python path=generated/niscope/niscope/errors.py -->
## PYTHON MODULE: generated/niscope/niscope/errors.py

### `def _is_success(code)`

### `def _is_error(code)`

### `def _is_warning(code)`

### `class Error(Exception)`

Base error class for NI-SCOPE

#### `def __init__(self, message)`

### `class DriverError(Error)`

An error originating from the NI-SCOPE driver

#### `def __init__(self, code, description)`

### `class DriverWarning(Warning)`

A warning originating from the NI-SCOPE driver

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

An error due to using this module with an older version of the NI-SCOPE driver runtime.

#### `def __init__(self)`

### `class DriverTooNewError(Error)`

An error due to the NI-SCOPE driver runtime being too new for this module.

#### `def __init__(self)`

### `class InvalidRepeatedCapabilityError(Error)`

An error due to an invalid character in a repeated capability

#### `def __init__(self, invalid_character, invalid_string)`

### `class SelfTestError(Error)`

An error due to a failed self-test

#### `def __init__(self, code, msg)`

### `def handle_error(library_interpreter, code, ignore_warnings, is_error_handling)`

handle_error

    Helper function for handling errors returned by niscope.Library.
    It calls back into the LibraryInterpreter to get the corresponding error
    description and raises if necessary.
    

<!--NI_PYTHON_API repo=nimi-python path=generated/niscope/niscope/grpc_session_options.py -->
## PYTHON MODULE: generated/niscope/niscope/grpc_session_options.py

- `GRPC_SERVICE_INTERFACE_NAME = 'niscope_grpc.NiScope'`

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
        

<!--NI_PYTHON_API repo=nimi-python path=generated/niscope/niscope/measurement_stats.py -->
## PYTHON MODULE: generated/niscope/niscope/measurement_stats.py

### `class MeasurementStats()`

#### `def __init__(self, result=0.0, mean=0.0, stdev=0.0, min_val=0.0, max_val=0.0, num_in_stats=0)`

#### `def __repr__(self)`

#### `def __str__(self)`

<!--NI_PYTHON_API repo=nimi-python path=generated/niscope/niscope/nidevice_pb2.py -->
## PYTHON MODULE: generated/niscope/niscope/nidevice_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0enidevice.proto\x12\rnidevice_grpc"2\n\x0fNIComplexNumber\x12\x0c\n\x04real\x18\x01 \x01(\x01\x12\x11\n\timaginary\x18\x02 \x01(\x01"5\n\x12NIComplexNumberF32\x12\x0c\n\x04real\x18\x01 \x01(\x02\x12\x11\n\timaginary\x18\x02 \x01(\x02"/\n\x0cNIComplexI16\x12\x0c\n\x04real\x18\x01 \x01(\x11\x12\x11\n\timaginary\x18\x02 \x01(\x11"r\n\x0fSmtSpectrumInfo\x12\x15\n\rspectrum_type\x18\x01 \x01(\r\x12\x11\n\tlinear_db\x18\x02 \x01(\r\x12\x0e\n\x06window\x18\x03 \x01(\r\x12\x13\n\x0bwindow_size\x18\x04 \x01(\x11\x12\x10\n\x08fft_size\x18\x05 \x01(\x11BB\n\x12com.ni.grpc.deviceB\x08NiDeviceP\x01\xaa\x02\x1fNationalInstruments.Grpc.Deviceb\x06proto3')`

<!--NI_PYTHON_API repo=nimi-python path=generated/niscope/niscope/nidevice_pb2_grpc.py -->
## PYTHON MODULE: generated/niscope/niscope/nidevice_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

<!--NI_PYTHON_API repo=nimi-python path=generated/niscope/niscope/niscope_pb2.py -->
## PYTHON MODULE: generated/niscope/niscope/niscope_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rniscope.proto\x12\x0cniscope_grpc\x1a\x0enidevice.proto\x1a\rsession.proto"\xb7\x01\n\x0cWaveformInfo\x12\x1a\n\x12absolute_initial_x\x18\x01 \x01(\x01\x12\x1a\n\x12relative_initial_x\x18\x02 \x01(\x01\x12\x13\n\x0bx_increment\x18\x03 \x01(\x01\x12\x16\n\x0eactual_samples\x18\x04 \x01(\x11\x12\x0e\n\x06offset\x18\x05 \x01(\x01\x12\x0c\n\x04gain\x18\x06 \x01(\x01\x12\x11\n\treserved1\x18\x07 \x01(\x01\x12\x11\n\treserved2\x18\x08 \x01(\x01"U\n\x0fCoefficientInfo\x12\x0e\n\x06offset\x18\x01 \x01(\x01\x12\x0c\n\x04gain\x18\x02 \x01(\x01\x12\x11\n\treserved1\x18\x03 \x01(\x01\x12\x11\n\treserved2\x18\x04 \x01(\x01"\xb1\x01\n\x0bInitRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\x10\n\x08id_query\x18\x03 \x01(\x08\x12\x14\n\x0creset_device\x18\x04 \x01(\x08\x12M\n\x17initialization_behavior\x18\x05 \x01(\x0e2,.nidevice_grpc.SessionInitializationBehavior"~\n\x0cInitResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12"\n\x02vi\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x19\n\rerror_message\x18\x03 \x01(\tB\x02\x18\x01\x12\x1f\n\x17new_session_initialized\x18\x04 \x01(\x08"\xd3\x01\n\x16InitWithOptionsRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\x10\n\x08id_query\x18\x03 \x01(\x08\x12\x14\n\x0creset_device\x18\x04 \x01(\x08\x12\x15\n\roption_string\x18\x05 \x01(\t\x12M\n\x17initialization_behavior\x18\x06 \x01(\x0e2,.nidevice_grpc.SessionInitializationBehavior"\x89\x01\n\x17InitWithOptionsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12"\n\x02vi\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x19\n\rerror_message\x18\x03 \x01(\tB\x02\x18\x01\x12\x1f\n\x17new_session_initialized\x18\x04 \x01(\x08"2\n\x0cCloseRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\x1f\n\rCloseResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"6\n\x10AutoSetupRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"#\n\x11AutoSetupResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xfc\x01\n\x18ConfigureVerticalRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12\r\n\x05range\x18\x03 \x01(\x01\x12\x0e\n\x06offset\x18\x04 \x01(\x01\x122\n\x08coupling\x18\x05 \x01(\x0e2\x1e.niscope_grpc.VerticalCouplingH\x00\x12\x16\n\x0ccoupling_raw\x18\x06 \x01(\x11H\x00\x12\x19\n\x11probe_attenuation\x18\x07 \x01(\x01\x12\x0f\n\x07enabled\x18\x08 \x01(\x08B\x0f\n\rcoupling_enum"+\n\x19ConfigureVerticalResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x95\x01\n#ConfigureChanCharacteristicsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12\x17\n\x0finput_impedance\x18\x03 \x01(\x01\x12\x1b\n\x13max_input_frequency\x18\x04 \x01(\x01"6\n$ConfigureChanCharacteristicsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb9\x01\n ConfigureHorizontalTimingRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x17\n\x0fmin_sample_rate\x18\x02 \x01(\x01\x12\x13\n\x0bmin_num_pts\x18\x03 \x01(\x11\x12\x14\n\x0cref_position\x18\x04 \x01(\x01\x12\x13\n\x0bnum_records\x18\x05 \x01(\x11\x12\x18\n\x10enforce_realtime\x18\x06 \x01(\x08"3\n!ConfigureHorizontalTimingResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xfd\x03\n\x15ConfigureClockRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12 \n\x16input_clock_source_raw\x18\x02 \x01(\tH\x00\x12I\n\x19input_clock_source_mapped\x18\x06 \x01(\x0e2$.niscope_grpc.ClockingTerminalValuesH\x00\x12!\n\x17output_clock_source_raw\x18\x03 \x01(\tH\x01\x12J\n\x1aoutput_clock_source_mapped\x18\x07 \x01(\x0e2$.niscope_grpc.ClockingTerminalValuesH\x01\x12%\n\x1bclock_sync_pulse_source_raw\x18\x04 \x01(\tH\x02\x12N\n\x1eclock_sync_pulse_source_mapped\x18\x08 \x01(\x0e2$.niscope_grpc.ClockingTerminalValuesH\x02\x12\x16\n\x0emaster_enabled\x18\x05 \x01(\x08B\x19\n\x17input_clock_source_enumB\x1a\n\x18output_clock_source_enumB\x1e\n\x1cclock_sync_pulse_source_enum"(\n\x16ConfigureClockResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xab\x02\n\x13ExportSignalRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x121\n\x06signal\x18\x02 \x01(\x0e2\x1f.niscope_grpc.ExportableSignalsH\x00\x12\x14\n\nsignal_raw\x18\x03 \x01(\x11H\x00\x12\x19\n\x11signal_identifier\x18\x04 \x01(\t\x12F\n\x16output_terminal_mapped\x18\x05 \x01(\x0e2$.niscope_grpc.ClockingTerminalValuesH\x01\x12\x1d\n\x13output_terminal_raw\x18\x06 \x01(\tH\x01B\r\n\x0bsignal_enumB\x16\n\x14output_terminal_enum"&\n\x14ExportSignalResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"Z\n%AdjustSampleClockRelativeDelayRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\r\n\x05delay\x18\x02 \x01(\x01"8\n&AdjustSampleClockRelativeDelayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xcc\x02\n\x1bConfigureTriggerEdgeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x16\n\x0etrigger_source\x18\x02 \x01(\t\x12\r\n\x05level\x18\x03 \x01(\x01\x12+\n\x05slope\x18\x04 \x01(\x0e2\x1a.niscope_grpc.TriggerSlopeH\x00\x12\x13\n\tslope_raw\x18\x05 \x01(\x11H\x00\x129\n\x10trigger_coupling\x18\x06 \x01(\x0e2\x1d.niscope_grpc.TriggerCouplingH\x01\x12\x1e\n\x14trigger_coupling_raw\x18\x07 \x01(\x11H\x01\x12\x0f\n\x07holdoff\x18\x08 \x01(\x01\x12\r\n\x05delay\x18\t \x01(\x01B\x0c\n\nslope_enumB\x17\n\x15trigger_coupling_enum".\n\x1cConfigureTriggerEdgeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xdc\x03\n\x1dConfigureTriggerGlitchRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x16\n\x0etrigger_source\x18\x02 \x01(\t\x12\r\n\x05level\x18\x03 \x01(\x01\x12\r\n\x05width\x18\x04 \x01(\x01\x120\n\x08polarity\x18\x05 \x01(\x0e2\x1c.niscope_grpc.GlitchPolarityH\x00\x12\x16\n\x0cpolarity_raw\x18\x06 \x01(\x11H\x00\x129\n\x10glitch_condition\x18\x07 \x01(\x0e2\x1d.niscope_grpc.GlitchConditionH\x01\x12\x1e\n\x14glitch_condition_raw\x18\x08 \x01(\x11H\x01\x129\n\x10trigger_coupling\x18\t \x01(\x0e2\x1d.niscope_grpc.TriggerCouplingH\x02\x12\x1e\n\x14trigger_coupling_raw\x18\n \x01(\x11H\x02\x12\x0f\n\x07holdoff\x18\x0b \x01(\x01\x12\r\n\x05delay\x18\x0c \x01(\x01B\x0f\n\rpolarity_enumB\x17\n\x15glitch_condition_enumB\x17\n\x15trigger_coupling_enum"0\n\x1eConfigureTriggerGlitchResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xe6\x02\n!ConfigureTriggerHysteresisRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x16\n\x0etrigger_source\x18\x02 \x01(\t\x12\r\n\x05level\x18\x03 \x01(\x01\x12\x12\n\nhysteresis\x18\x04 \x01(\x01\x12+\n\x05slope\x18\x05 \x01(\x0e2\x1a.niscope_grpc.TriggerSlopeH\x00\x12\x13\n\tslope_raw\x18\x06 \x01(\x11H\x00\x129\n\x10trigger_coupling\x18\x07 \x01(\x0e2\x1d.niscope_grpc.TriggerCouplingH\x01\x12\x1e\n\x14trigger_coupling_raw\x18\x08 \x01(\x11H\x01\x12\x0f\n\x07holdoff\x18\t \x01(\x01\x12\r\n\x05delay\x18\n \x01(\x01B\x0c\n\nslope_enumB\x17\n\x15trigger_coupling_enum"4\n"ConfigureTriggerHysteresisResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xfd\x02\n\x1dConfigureTriggerWindowRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x16\n\x0etrigger_source\x18\x02 \x01(\t\x12\x11\n\tlow_level\x18\x03 \x01(\x01\x12\x12\n\nhigh_level\x18\x04 \x01(\x01\x126\n\x0bwindow_mode\x18\x05 \x01(\x0e2\x1f.niscope_grpc.TriggerWindowModeH\x00\x12\x19\n\x0fwindow_mode_raw\x18\x06 \x01(\x11H\x00\x129\n\x10trigger_coupling\x18\x07 \x01(\x0e2\x1d.niscope_grpc.TriggerCouplingH\x01\x12\x1e\n\x14trigger_coupling_raw\x18\x08 \x01(\x11H\x01\x12\x0f\n\x07holdoff\x18\t \x01(\x01\x12\r\n\x05delay\x18\n \x01(\x01B\x12\n\x10window_mode_enumB\x17\n\x15trigger_coupling_enum"0\n\x1eConfigureTriggerWindowResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"e\n\x1fConfigureTriggerSoftwareRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07holdoff\x18\x02 \x01(\x01\x12\r\n\x05delay\x18\x03 \x01(\x01"2\n ConfigureTriggerSoftwareResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xac\x01\n\x1eSendSoftwareTriggerEdgeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x123\n\rwhich_trigger\x18\x02 \x01(\x0e2\x1a.niscope_grpc.WhichTriggerH\x00\x12\x1b\n\x11which_trigger_raw\x18\x03 \x01(\x11H\x00B\x14\n\x12which_trigger_enum"1\n\x1fSendSoftwareTriggerEdgeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"F\n ConfigureTriggerImmediateRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"3\n!ConfigureTriggerImmediateResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xf5\x02\n\x1bConfigureTriggerRuntRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x16\n\x0etrigger_source\x18\x02 \x01(\t\x12\x15\n\rlow_threshold\x18\x03 \x01(\x01\x12\x16\n\x0ehigh_threshold\x18\x04 \x01(\x01\x12.\n\x08polarity\x18\x05 \x01(\x0e2\x1a.niscope_grpc.RuntPolarityH\x00\x12\x16\n\x0cpolarity_raw\x18\x06 \x01(\x11H\x00\x129\n\x10trigger_coupling\x18\x07 \x01(\x0e2\x1d.niscope_grpc.TriggerCouplingH\x01\x12\x1e\n\x14trigger_coupling_raw\x18\x08 \x01(\x11H\x01\x12\x0f\n\x07holdoff\x18\t \x01(\x01\x12\r\n\x05delay\x18\n \x01(\x01B\x0f\n\rpolarity_enumB\x17\n\x15trigger_coupling_enum".\n\x1cConfigureTriggerRuntResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xcc\x01\n\x1eConfigureTriggerDigitalRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x16\n\x0etrigger_source\x18\x02 \x01(\t\x12+\n\x05slope\x18\x03 \x01(\x0e2\x1a.niscope_grpc.TriggerSlopeH\x00\x12\x13\n\tslope_raw\x18\x04 \x01(\x11H\x00\x12\x0f\n\x07holdoff\x18\x05 \x01(\x01\x12\r\n\x05delay\x18\x06 \x01(\x01B\x0c\n\nslope_enum"1\n\x1fConfigureTriggerDigitalResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xba\x04\n\x1cConfigureTriggerVideoRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x16\n\x0etrigger_source\x18\x02 \x01(\t\x12\x19\n\x11enable_dc_restore\x18\x03 \x01(\x08\x128\n\rsignal_format\x18\x04 \x01(\x0e2\x1f.niscope_grpc.VideoSignalFormatH\x00\x12\x1b\n\x11signal_format_raw\x18\x05 \x01(\x11H\x00\x120\n\x05event\x18\x06 \x01(\x0e2\x1f.niscope_grpc.VideoTriggerEventH\x01\x12\x13\n\tevent_raw\x18\x07 \x01(\x11H\x01\x12\x13\n\x0bline_number\x18\x08 \x01(\x11\x12/\n\x08polarity\x18\t \x01(\x0e2\x1b.niscope_grpc.VideoPolarityH\x02\x12\x16\n\x0cpolarity_raw\x18\n \x01(\x11H\x02\x129\n\x10trigger_coupling\x18\x0b \x01(\x0e2\x1d.niscope_grpc.TriggerCouplingH\x03\x12\x1e\n\x14trigger_coupling_raw\x18\x0c \x01(\x11H\x03\x12\x0f\n\x07holdoff\x18\r \x01(\x01\x12\r\n\x05delay\x18\x0e \x01(\x01B\x14\n\x12signal_format_enumB\x0c\n\nevent_enumB\x0f\n\rpolarity_enumB\x17\n\x15trigger_coupling_enum"/\n\x1dConfigureTriggerVideoResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xe4\x03\n\x1cConfigureTriggerWidthRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x16\n\x0etrigger_source\x18\x02 \x01(\t\x12\r\n\x05level\x18\x03 \x01(\x01\x12\x15\n\rlow_threshold\x18\x04 \x01(\x01\x12\x16\n\x0ehigh_threshold\x18\x05 \x01(\x01\x12/\n\x08polarity\x18\x06 \x01(\x0e2\x1b.niscope_grpc.WidthPolarityH\x00\x12\x16\n\x0cpolarity_raw\x18\x07 \x01(\x11H\x00\x121\n\tcondition\x18\x08 \x01(\x0e2\x1c.niscope_grpc.WidthConditionH\x01\x12\x17\n\rcondition_raw\x18\t \x01(\x11H\x01\x129\n\x10trigger_coupling\x18\n \x01(\x0e2\x1d.niscope_grpc.TriggerCouplingH\x02\x12\x1e\n\x14trigger_coupling_raw\x18\x0b \x01(\x11H\x02\x12\x0f\n\x07holdoff\x18\x0c \x01(\x01\x12\r\n\x05delay\x18\r \x01(\x01B\x0f\n\rpolarity_enumB\x10\n\x0econdition_enumB\x17\n\x15trigger_coupling_enum"/\n\x1dConfigureTriggerWidthResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x80\x01\n.ConfigureEqualizationFilterCoefficientsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12\x14\n\x0ccoefficients\x18\x03 \x03(\x01"A\n/ConfigureEqualizationFilterCoefficientsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x7f\n(GetEqualizationFilterCoefficientsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07channel\x18\x02 \x01(\t\x12\x1e\n\x16number_of_coefficients\x18\x03 \x01(\x11"Q\n)GetEqualizationFilterCoefficientsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x14\n\x0ccoefficients\x18\x02 \x03(\x01"g\n\x1bGetFrequencyResponseRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07channel\x18\x02 \x01(\t\x12\x13\n\x0bbuffer_size\x18\x03 \x01(\x11"\x86\x01\n\x1cGetFrequencyResponseResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0bfrequencies\x18\x02 \x03(\x01\x12\x12\n\namplitudes\x18\x03 \x03(\x01\x12\x0e\n\x06phases\x18\x04 \x03(\x01\x12\x1d\n\x15number_of_frequencies\x18\x05 \x01(\x11"[\n\x1bConfigureAcquisitionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x18\n\x10acquisition_type\x18\x02 \x01(\x11".\n\x1cConfigureAcquisitionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"@\n\x1aInitiateAcquisitionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"-\n\x1bInitiateAcquisitionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"2\n\x0cAbortRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\x1f\n\rAbortResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"3\n\rCommitRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session" \n\x0eCommitResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"m\n\x0bReadRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12\x13\n\x0bnum_samples\x18\x04 \x01(\x11"^\n\x0cReadResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x10\n\x08waveform\x18\x02 \x03(\x01\x12,\n\x08wfm_info\x18\x03 \x03(\x0b2\x1a.niscope_grpc.WaveformInfo"n\n\x0cFetchRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12\x13\n\x0bnum_samples\x18\x04 \x01(\x11"_\n\rFetchResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x10\n\x08waveform\x18\x02 \x03(\x01\x12,\n\x08wfm_info\x18\x03 \x03(\x0b2\x1a.niscope_grpc.WaveformInfo"u\n\x13FetchBinary8Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12\x13\n\x0bnum_samples\x18\x04 \x01(\x11"f\n\x14FetchBinary8Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x10\n\x08waveform\x18\x02 \x01(\x0c\x12,\n\x08wfm_info\x18\x03 \x03(\x0b2\x1a.niscope_grpc.WaveformInfo"v\n\x14FetchBinary16Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12\x13\n\x0bnum_samples\x18\x04 \x01(\x11"g\n\x15FetchBinary16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x10\n\x08waveform\x18\x02 \x03(\x11\x12,\n\x08wfm_info\x18\x03 \x03(\x0b2\x1a.niscope_grpc.WaveformInfo"v\n\x14FetchBinary32Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12\x13\n\x0bnum_samples\x18\x04 \x01(\x11"g\n\x15FetchBinary32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x10\n\x08waveform\x18\x02 \x03(\x11\x12,\n\x08wfm_info\x18\x03 \x03(\x0b2\x1a.niscope_grpc.WaveformInfo"u\n\x13FetchComplexRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12\x13\n\x0bnum_samples\x18\x04 \x01(\x11"\x81\x01\n\x14FetchComplexResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12+\n\x03wfm\x18\x02 \x03(\x0b2\x1e.nidevice_grpc.NIComplexNumber\x12,\n\x08wfm_info\x18\x03 \x03(\x0b2\x1a.niscope_grpc.WaveformInfo"}\n\x1bFetchComplexBinary16Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12\x13\n\x0bnum_samples\x18\x04 \x01(\x11"\x86\x01\n\x1cFetchComplexBinary16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12(\n\x03wfm\x18\x02 \x03(\x0b2\x1b.nidevice_grpc.NIComplexI16\x12,\n\x08wfm_info\x18\x03 \x03(\x0b2\x1a.niscope_grpc.WaveformInfo">\n\x18AcquisitionStatusRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\x88\x01\n\x19AcquisitionStatusResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12;\n\x12acquisition_status\x18\x02 \x01(\x0e2\x1f.niscope_grpc.AcquisitionStatus\x12\x1e\n\x16acquisition_status_raw\x18\x03 \x01(\x11"P\n\x14ActualNumWfmsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t"9\n\x15ActualNumWfmsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x10\n\x08num_wfms\x18\x02 \x01(\x11"\xbc\x01\n\x18ActualMeasWfmSizeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12=\n\x13array_meas_function\x18\x02 \x01(\x0e2\x1e.niscope_grpc.ArrayMeasurementH\x00\x12!\n\x17array_meas_function_raw\x18\x03 \x01(\x11H\x00B\x1a\n\x18array_meas_function_enum"G\n\x19ActualMeasWfmSizeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1a\n\x12meas_waveform_size\x18\x02 \x01(\x11"?\n\x19ActualRecordLengthRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"C\n\x1aActualRecordLengthResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rrecord_length\x18\x02 \x01(\x11"7\n\x11SampleRateRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"9\n\x12SampleRateResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0bsample_rate\x18\x02 \x01(\x01"7\n\x11SampleModeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"9\n\x12SampleModeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0bsample_mode\x18\x02 \x01(\x11"\xc4\x01\n\x1cAddWaveformProcessingRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x127\n\rmeas_function\x18\x03 \x01(\x0e2\x1e.niscope_grpc.ArrayMeasurementH\x00\x12\x1b\n\x11meas_function_raw\x18\x04 \x01(\x11H\x00B\x14\n\x12meas_function_enum"/\n\x1dAddWaveformProcessingResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"Z\n\x1eClearWaveformProcessingRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t"1\n\x1fClearWaveformProcessingResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x83\x02\n$ClearWaveformMeasurementStatsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12L\n\x1eclearable_measurement_function\x18\x03 \x01(\x0e2".niscope_grpc.ClearableMeasurementH\x00\x12,\n"clearable_measurement_function_raw\x18\x04 \x01(\x11H\x00B%\n#clearable_measurement_function_enum"7\n%ClearWaveformMeasurementStatsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xe5\x01\n\x16ReadMeasurementRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12?\n\x14scalar_meas_function\x18\x04 \x01(\x0e2\x1f.niscope_grpc.ScalarMeasurementH\x00\x12"\n\x18scalar_meas_function_raw\x18\x05 \x01(\x11H\x00B\x1b\n\x19scalar_meas_function_enum"9\n\x17ReadMeasurementResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0e\n\x06result\x18\x02 \x03(\x01"\xe6\x01\n\x17FetchMeasurementRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12?\n\x14scalar_meas_function\x18\x04 \x01(\x0e2\x1f.niscope_grpc.ScalarMeasurementH\x00\x12"\n\x18scalar_meas_function_raw\x18\x05 \x01(\x11H\x00B\x1b\n\x19scalar_meas_function_enum":\n\x18FetchMeasurementResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0e\n\x06result\x18\x02 \x03(\x01"\xeb\x01\n\x1cFetchMeasurementStatsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12?\n\x14scalar_meas_function\x18\x04 \x01(\x0e2\x1f.niscope_grpc.ScalarMeasurementH\x00\x12"\n\x18scalar_meas_function_raw\x18\x05 \x01(\x11H\x00B\x1b\n\x19scalar_meas_function_enum"\x8c\x01\n\x1dFetchMeasurementStatsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0e\n\x06result\x18\x02 \x03(\x01\x12\x0c\n\x04mean\x18\x03 \x03(\x01\x12\r\n\x05stdev\x18\x04 \x03(\x01\x12\x0b\n\x03min\x18\x05 \x03(\x01\x12\x0b\n\x03max\x18\x06 \x03(\x01\x12\x14\n\x0cnum_in_stats\x18\x07 \x03(\x11"\x95\x02\n\x1cFetchArrayMeasurementRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12=\n\x13array_meas_function\x18\x04 \x01(\x0e2\x1e.niscope_grpc.ArrayMeasurementH\x00\x12!\n\x17array_meas_function_raw\x18\x05 \x01(\x11H\x00\x12\x1a\n\rmeas_wfm_size\x18\x06 \x01(\x11H\x01\x88\x01\x01B\x1a\n\x18array_meas_function_enumB\x10\n\x0e_meas_wfm_size"o\n\x1dFetchArrayMeasurementResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x10\n\x08meas_wfm\x18\x02 \x03(\x01\x12,\n\x08wfm_info\x18\x03 \x03(\x0b2\x1a.niscope_grpc.WaveformInfo"2\n\x0cResetRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\x1f\n\rResetResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"5\n\x0fSelfTestRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"W\n\x10SelfTestResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x18\n\x10self_test_result\x18\x02 \x01(\x11\x12\x19\n\x11self_test_message\x18\x03 \x01(\t"4\n\x0eDisableRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"!\n\x0fDisableResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"8\n\x12ResetDeviceRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"%\n\x13ResetDeviceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa0\x01\n\x17CalSelfCalibrateRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12&\n\x06option\x18\x03 \x01(\x0e2\x14.niscope_grpc.OptionH\x00\x12\x14\n\noption_raw\x18\x04 \x01(\x11H\x00B\r\n\x0boption_enum"*\n\x18CalSelfCalibrateResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05":\n\x14RevisionQueryRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"[\n\x15RevisionQueryResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fdriver_revision\x18\x02 \x01(\t\x12\x19\n\x11firmware_revision\x18\x03 \x01(\t"I\n#ProbeCompensationSignalStartRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"6\n$ProbeCompensationSignalStartResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"H\n"ProbeCompensationSignalStopRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"5\n#ProbeCompensationSignalStopResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"B\n\x1cCableSenseSignalStartRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"/\n\x1dCableSenseSignalStartResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"A\n\x1bCableSenseSignalStopRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session".\n\x1cCableSenseSignalStopResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"J\n\x15GetChannelNameRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\r\n\x05index\x18\x02 \x01(\x11"@\n\x16GetChannelNameResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x16\n\x0echannel_string\x18\x02 \x01(\t"T\n\x1fGetChannelNameFromStringRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\r\n\x05index\x18\x02 \x01(\t"@\n GetChannelNameFromStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t"c\n\x13ErrorHandlerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x12\n\nerror_code\x18\x02 \x01(\x11\x12\x14\n\x0cerror_source\x18\x03 \x01(\t"A\n\x14ErrorHandlerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x19\n\x11error_description\x18\x02 \x01(\t"5\n\x0fGetErrorRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"K\n\x10GetErrorResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nerror_code\x18\x02 \x01(\x11\x12\x13\n\x0bdescription\x18\x03 \x01(\t"P\n\x16GetErrorMessageRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x12\n\nerror_code\x18\x02 \x01(\x11"@\n\x17GetErrorMessageResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rerror_message\x18\x02 \x01(\t"\x8c\x01\n\x1aGetAttributeViInt32Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x124\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1e.niscope_grpc.NiScopeAttribute"<\n\x1bGetAttributeViInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x11"\xeb\x01\n\x1aSetAttributeViInt32Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x124\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1e.niscope_grpc.NiScopeAttribute\x12\x13\n\tvalue_raw\x18\x04 \x01(\x11H\x00\x12:\n\x05value\x18\x05 \x01(\x0e2).niscope_grpc.NiScopeInt32AttributeValuesH\x00B\x0c\n\nvalue_enum"-\n\x1bSetAttributeViInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xed\x01\n\x1cCheckAttributeViInt32Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x124\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1e.niscope_grpc.NiScopeAttribute\x12\x13\n\tvalue_raw\x18\x04 \x01(\x11H\x00\x12:\n\x05value\x18\x05 \x01(\x0e2).niscope_grpc.NiScopeInt32AttributeValuesH\x00B\x0c\n\nvalue_enum"/\n\x1dCheckAttributeViInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x8c\x01\n\x1aGetAttributeViInt64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x124\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1e.niscope_grpc.NiScopeAttribute"<\n\x1bGetAttributeViInt64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x03"\x9f\x01\n\x1aSetAttributeViInt64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x124\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1e.niscope_grpc.NiScopeAttribute\x12\x11\n\tvalue_raw\x18\x04 \x01(\x03"-\n\x1bSetAttributeViInt64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa1\x01\n\x1cCheckAttributeViInt64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x124\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1e.niscope_grpc.NiScopeAttribute\x12\x11\n\tvalue_raw\x18\x04 \x01(\x03"/\n\x1dCheckAttributeViInt64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x8d\x01\n\x1bGetAttributeViReal64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x124\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1e.niscope_grpc.NiScopeAttribute"=\n\x1cGetAttributeViReal64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x01"\xb7\x02\n\x1bSetAttributeViReal64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x124\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1e.niscope_grpc.NiScopeAttribute\x12\x13\n\tvalue_raw\x18\x04 \x01(\x01H\x00\x12;\n\x05value\x18\x05 \x01(\x0e2*.niscope_grpc.NiScopeReal64AttributeValuesH\x00\x12H\n\x0cvalue_mapped\x18\x06 \x01(\x0e20.niscope_grpc.NiScopeReal64AttributeValuesMappedH\x00B\x0c\n\nvalue_enum".\n\x1cSetAttributeViReal64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb9\x02\n\x1dCheckAttributeViReal64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x124\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1e.niscope_grpc.NiScopeAttribute\x12\x13\n\tvalue_raw\x18\x04 \x01(\x01H\x00\x12;\n\x05value\x18\x05 \x01(\x0e2*.niscope_grpc.NiScopeReal64AttributeValuesH\x00\x12H\n\x0cvalue_mapped\x18\x06 \x01(\x0e20.niscope_grpc.NiScopeReal64AttributeValuesMappedH\x00B\x0c\n\nvalue_enum"0\n\x1eCheckAttributeViReal64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x8d\x01\n\x1bGetAttributeViStringRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x124\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1e.niscope_grpc.NiScopeAttribute"=\n\x1cGetAttributeViStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t"\xfa\x01\n\x1bSetAttributeViStringRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x124\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1e.niscope_grpc.NiScopeAttribute\x12H\n\x0cvalue_mapped\x18\x04 \x01(\x0e20.niscope_grpc.NiScopeStringAttributeValuesMappedH\x00\x12\x13\n\tvalue_raw\x18\x05 \x01(\tH\x00B\x0c\n\nvalue_enum".\n\x1cSetAttributeViStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xfc\x01\n\x1dCheckAttributeViStringRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x124\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1e.niscope_grpc.NiScopeAttribute\x12H\n\x0cvalue_mapped\x18\x04 \x01(\x0e20.niscope_grpc.NiScopeStringAttributeValuesMappedH\x00\x12\x13\n\tvalue_raw\x18\x05 \x01(\tH\x00B\x0c\n\nvalue_enum"0\n\x1eCheckAttributeViStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x8e\x01\n\x1cGetAttributeViSessionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x124\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1e.niscope_grpc.NiScopeAttribute"V\n\x1dGetAttributeViSessionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12%\n\x05value\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session"\xb5\x01\n\x1cSetAttributeViSessionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x124\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1e.niscope_grpc.NiScopeAttribute\x12%\n\x05value\x18\x04 \x01(\x0b2\x16.nidevice_grpc.Session"/\n\x1dSetAttributeViSessionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb7\x01\n\x1eCheckAttributeViSessionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x124\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1e.niscope_grpc.NiScopeAttribute\x12%\n\x05value\x18\x04 \x01(\x0b2\x16.nidevice_grpc.Session"1\n\x1fCheckAttributeViSessionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x8e\x01\n\x1cGetAttributeViBooleanRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x124\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1e.niscope_grpc.NiScopeAttribute">\n\x1dGetAttributeViBooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x08"\x9d\x01\n\x1cSetAttributeViBooleanRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x124\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1e.niscope_grpc.NiScopeAttribute\x12\r\n\x05value\x18\x04 \x01(\x08"/\n\x1dSetAttributeViBooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x9f\x01\n\x1eCheckAttributeViBooleanRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x124\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1e.niscope_grpc.NiScopeAttribute\x12\r\n\x05value\x18\x04 \x01(\x08"1\n\x1fCheckAttributeViBooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"f\n)ImportAttributeConfigurationBufferRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rconfiguration\x18\x02 \x01(\x0c"<\n*ImportAttributeConfigurationBufferResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"O\n)ExportAttributeConfigurationBufferRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"S\n*ExportAttributeConfigurationBufferResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rconfiguration\x18\x02 \x01(\x0c"`\n\'ImportAttributeConfigurationFileRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tfile_path\x18\x02 \x01(\t":\n(ImportAttributeConfigurationFileResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"`\n\'ExportAttributeConfigurationFileRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tfile_path\x18\x02 \x01(\t":\n(ExportAttributeConfigurationFileResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"Y\n\x1dGetScalingCoefficientsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t"\x8d\x01\n\x1eGetScalingCoefficientsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x127\n\x10coefficient_info\x18\x02 \x03(\x0b2\x1d.niscope_grpc.CoefficientInfo\x12"\n\x1anumber_of_coefficient_sets\x18\x03 \x01(\x11"_\n#GetNormalizationCoefficientsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t"\x93\x01\n$GetNormalizationCoefficientsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x127\n\x10coefficient_info\x18\x02 \x03(\x0b2\x1d.niscope_grpc.CoefficientInfo\x12"\n\x1anumber_of_coefficient_sets\x18\x03 \x01(\x11"Y\n\x1eGetStreamEndpointHandleRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x13\n\x0bstream_name\x18\x02 \x01(\t"H\n\x1fGetStreamEndpointHandleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rwriter_handle\x18\x02 \x01(\r"\x99\x01\n\x13CalFetchDateRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x123\n\twhich_one\x18\x02 \x01(\x0e2\x1e.niscope_grpc.CalibrationTypesH\x00\x12\x17\n\rwhich_one_raw\x18\x03 \x01(\x11H\x00B\x10\n\x0ewhich_one_enum"P\n\x14CalFetchDateResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04year\x18\x02 \x01(\x11\x12\r\n\x05month\x18\x03 \x01(\x11\x12\x0b\n\x03day\x18\x04 \x01(\x11"\xa0\x01\n\x1aCalFetchTemperatureRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x123\n\twhich_one\x18\x02 \x01(\x0e2\x1e.niscope_grpc.CalibrationTypesH\x00\x12\x17\n\rwhich_one_raw\x18\x03 \x01(\x11H\x00B\x10\n\x0ewhich_one_enum"B\n\x1bCalFetchTemperatureResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0btemperature\x18\x02 \x01(\x01*\xe0Q\n\x10NiScopeAttribute\x12!\n\x1dNISCOPE_ATTRIBUTE_UNSPECIFIED\x10\x00\x12%\n\x1fNISCOPE_ATTRIBUTE_MEAS_HIGH_REF\x10\xaf\xaaL\x12$\n\x1eNISCOPE_ATTRIBUTE_MEAS_LOW_REF\x10\xb0\xaaL\x12\x1d\n\x17NISCOPE_ATTRIBUTE_CACHE\x10\x94\x8b@\x12$\n\x1eNISCOPE_ATTRIBUTE_MEAS_MID_REF\x10\xb1\xaaL\x12#\n\x1dNISCOPE_ATTRIBUTE_RANGE_CHECK\x10\x92\x8b@\x12/\n)NISCOPE_ATTRIBUTE_QUERY_INSTRUMENT_STATUS\x10\x93\x8b@\x12(\n"NISCOPE_ATTRIBUTE_RECORD_COERCIONS\x10\x96\x8b@\x12 \n\x1aNISCOPE_ATTRIBUTE_SIMULATE\x10\x95\x8b@\x12)\n#NISCOPE_ATTRIBUTE_INTERCHANGE_CHECK\x10\xa5\x8b@\x12%\n\x1fNISCOPE_ATTRIBUTE_CHANNEL_COUNT\x10\xdb\x8c@\x123\n-NISCOPE_ATTRIBUTE_SUPPORTED_INSTRUMENT_MODELS\x10\xd7\x8d@\x12*\n$NISCOPE_ATTRIBUTE_GROUP_CAPABILITIES\x10\xa1\x8e@\x123\n-NISCOPE_ATTRIBUTE_SPECIFIC_DRIVER_DESCRIPTION\x10\x92\x8f@\x12.\n(NISCOPE_ATTRIBUTE_SPECIFIC_DRIVER_PREFIX\x10\xbe\x8d@\x12.\n(NISCOPE_ATTRIBUTE_SPECIFIC_DRIVER_VENDOR\x10\x91\x8f@\x12@\n:NISCOPE_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION\x10\x93\x8f@\x12@\n:NISCOPE_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION\x10\x94\x8f@\x120\n*NISCOPE_ATTRIBUTE_SPECIFIC_DRIVER_REVISION\x10\xb7\x8f@\x12/\n)NISCOPE_ATTRIBUTE_INSTRUMENT_MANUFACTURER\x10\x8f\x8f@\x12(\n"NISCOPE_ATTRIBUTE_INSTRUMENT_MODEL\x10\x90\x8f@\x124\n.NISCOPE_ATTRIBUTE_INSTRUMENT_FIRMWARE_REVISION\x10\x8e\x8f@\x12.\n(NISCOPE_ATTRIBUTE_IO_RESOURCE_DESCRIPTOR\x10\xc0\x8d@\x12$\n\x1eNISCOPE_ATTRIBUTE_LOGICAL_NAME\x10\xc1\x8d@\x12$\n\x1eNISCOPE_ATTRIBUTE_DRIVER_SETUP\x10\x97\x8b@\x12(\n"NISCOPE_ATTRIBUTE_ACQUISITION_TYPE\x10\xb5\xa6L\x12#\n\x1dNISCOPE_ATTRIBUTE_SAMPLE_MODE\x10\xba\xa6L\x12\'\n!NISCOPE_ATTRIBUTE_CHANNEL_ENABLED\x10\xd5\xa5L\x12)\n#NISCOPE_ATTRIBUTE_PROBE_ATTENUATION\x10\xd4\xa5L\x12&\n NISCOPE_ATTRIBUTE_VERTICAL_RANGE\x10\xd1\xa5L\x12\'\n!NISCOPE_ATTRIBUTE_VERTICAL_OFFSET\x10\xd2\xa5L\x12\'\n!NISCOPE_ATTRIBUTE_WIDTH_CONDITION\x10\xc8\xa9L\x12+\n%NISCOPE_ATTRIBUTE_WIDTH_LOW_THRESHOLD\x10\xc5\xa9L\x12,\n&NISCOPE_ATTRIBUTE_WIDTH_HIGH_THRESHOLD\x10\xc6\xa9L\x12&\n NISCOPE_ATTRIBUTE_WIDTH_POLARITY\x10\xc7\xa9L\x12)\n#NISCOPE_ATTRIBUTE_VERTICAL_COUPLING\x10\xd3\xa5L\x12+\n%NISCOPE_ATTRIBUTE_MAX_INPUT_FREQUENCY\x10\xd6\xa5L\x12\'\n!NISCOPE_ATTRIBUTE_INPUT_IMPEDANCE\x10\xb7\xa6L\x12,\n&NISCOPE_ATTRIBUTE_HORZ_TIME_PER_RECORD\x10\xd7\xa5L\x12.\n(NISCOPE_ATTRIBUTE_ACQUISITION_START_TIME\x10\xbd\xa6L\x12(\n"NISCOPE_ATTRIBUTE_HORZ_MIN_NUM_PTS\x10\xd9\xa5L\x12*\n$NISCOPE_ATTRIBUTE_HORZ_RECORD_LENGTH\x10\xd8\xa5L\x120\n*NISCOPE_ATTRIBUTE_HORZ_RECORD_REF_POSITION\x10\xdb\xa5L\x12(\n"NISCOPE_ATTRIBUTE_HORZ_SAMPLE_RATE\x10\xda\xa5L\x12$\n\x1eNISCOPE_ATTRIBUTE_TRIGGER_TYPE\x10\xdc\xa5L\x12&\n NISCOPE_ATTRIBUTE_TRIGGER_SOURCE\x10\xdd\xa5L\x12%\n\x1fNISCOPE_ATTRIBUTE_TRIGGER_LEVEL\x10\xe1\xa5L\x12*\n$NISCOPE_ATTRIBUTE_TRIGGER_DELAY_TIME\x10\xdf\xa5L\x12\'\n!NISCOPE_ATTRIBUTE_TRIGGER_HOLDOFF\x10\xe0\xa5L\x12(\n"NISCOPE_ATTRIBUTE_TRIGGER_COUPLING\x10\xde\xa5L\x12%\n\x1fNISCOPE_ATTRIBUTE_TRIGGER_SLOPE\x10\xe2\xa5L\x12(\n"NISCOPE_ATTRIBUTE_TV_TRIGGER_EVENT\x10\x9d\xa7L\x12.\n(NISCOPE_ATTRIBUTE_TV_TRIGGER_LINE_NUMBER\x10\x9e\xa7L\x120\n*NISCOPE_ATTRIBUTE_TV_TRIGGER_SIGNAL_FORMAT\x10\x99\xa7L\x12+\n%NISCOPE_ATTRIBUTE_TV_TRIGGER_POLARITY\x10\x9c\xa7L\x12(\n"NISCOPE_ATTRIBUTE_HORZ_NUM_RECORDS\x10\xb1\x98F\x12*\n$NISCOPE_ATTRIBUTE_INPUT_CLOCK_SOURCE\x10\xb2\x98F\x12+\n%NISCOPE_ATTRIBUTE_OUTPUT_CLOCK_SOURCE\x10\xb3\x98F\x12-\n\'NISCOPE_ATTRIBUTE_HORZ_ENFORCE_REALTIME\x10\xb4\x98F\x12+\n%NISCOPE_ATTRIBUTE_BINARY_SAMPLE_WIDTH\x10\xb5\x98F\x12+\n%NISCOPE_ATTRIBUTE_CABLE_SENSE_VOLTAGE\x10\xb9\x99F\x12(\n"NISCOPE_ATTRIBUTE_CABLE_SENSE_MODE\x10\xba\x99F\x121\n+NISCOPE_ATTRIBUTE_CABLE_SENSE_SIGNAL_ENABLE\x10\xbb\x99F\x12*\n$NISCOPE_ATTRIBUTE_TRIGGER_HYSTERESIS\x10\xb6\x98F\x12/\n)NISCOPE_ATTRIBUTE_CLOCK_SYNC_PULSE_SOURCE\x10\xb7\x98F\x12%\n\x1fNISCOPE_ATTRIBUTE_MASTER_ENABLE\x10\xb8\x98F\x12\'\n!NISCOPE_ATTRIBUTE_MIN_SAMPLE_RATE\x10\xb9\x98F\x12+\n%NISCOPE_ATTRIBUTE_TRIGGER_WINDOW_MODE\x10\xbc\x98F\x120\n*NISCOPE_ATTRIBUTE_TRIGGER_WINDOW_LOW_LEVEL\x10\xbd\x98F\x121\n+NISCOPE_ATTRIBUTE_TRIGGER_WINDOW_HIGH_LEVEL\x10\xbe\x98F\x12,\n&NISCOPE_ATTRIBUTE_MEAS_REF_LEVEL_UNITS\x10\xc0\x98F\x12*\n$NISCOPE_ATTRIBUTE_MEAS_OTHER_CHANNEL\x10\xc2\x98F\x12/\n)NISCOPE_ATTRIBUTE_MEAS_HYSTERESIS_PERCENT\x10\xc3\x98F\x124\n.NISCOPE_ATTRIBUTE_MEAS_LAST_ACQ_HISTOGRAM_SIZE\x10\xc4\x98F\x123\n-NISCOPE_ATTRIBUTE_MEAS_VOLTAGE_HISTOGRAM_SIZE\x10\xc5\x98F\x128\n2NISCOPE_ATTRIBUTE_MEAS_VOLTAGE_HISTOGRAM_LOW_VOLTS\x10\xc6\x98F\x129\n3NISCOPE_ATTRIBUTE_MEAS_VOLTAGE_HISTOGRAM_HIGH_VOLTS\x10\xc7\x98F\x120\n*NISCOPE_ATTRIBUTE_MEAS_TIME_HISTOGRAM_SIZE\x10\xc8\x98F\x125\n/NISCOPE_ATTRIBUTE_MEAS_TIME_HISTOGRAM_LOW_VOLTS\x10\xc9\x98F\x126\n0NISCOPE_ATTRIBUTE_MEAS_TIME_HISTOGRAM_HIGH_VOLTS\x10\xca\x98F\x124\n.NISCOPE_ATTRIBUTE_MEAS_TIME_HISTOGRAM_LOW_TIME\x10\xcb\x98F\x125\n/NISCOPE_ATTRIBUTE_MEAS_TIME_HISTOGRAM_HIGH_TIME\x10\xcc\x98F\x12;\n5NISCOPE_ATTRIBUTE_MEAS_POLYNOMIAL_INTERPOLATION_ORDER\x10\xcd\x98F\x12:\n4NISCOPE_ATTRIBUTE_MEAS_INTERPOLATION_SAMPLING_FACTOR\x10\xce\x98F\x12/\n)NISCOPE_ATTRIBUTE_MEAS_FILTER_CUTOFF_FREQ\x10\xcf\x98F\x12/\n)NISCOPE_ATTRIBUTE_MEAS_FILTER_CENTER_FREQ\x10\xd0\x98F\x12*\n$NISCOPE_ATTRIBUTE_MEAS_FILTER_RIPPLE\x10\xd1\x98F\x12>\n8NISCOPE_ATTRIBUTE_MEAS_FILTER_TRANSIENT_WAVEFORM_PERCENT\x10\xd2\x98F\x12(\n"NISCOPE_ATTRIBUTE_MEAS_FILTER_TYPE\x10\xd3\x98F\x12)\n#NISCOPE_ATTRIBUTE_MEAS_FILTER_ORDER\x10\xd4\x98F\x12(\n"NISCOPE_ATTRIBUTE_MEAS_FILTER_TAPS\x10\xd5\x98F\x12/\n)NISCOPE_ATTRIBUTE_MEAS_CHAN_LOW_REF_LEVEL\x10\xd6\x98F\x12/\n)NISCOPE_ATTRIBUTE_MEAS_CHAN_MID_REF_LEVEL\x10\xd7\x98F\x120\n*NISCOPE_ATTRIBUTE_MEAS_CHAN_HIGH_REF_LEVEL\x10\xd8\x98F\x12)\n#NISCOPE_ATTRIBUTE_MEAS_FILTER_WIDTH\x10\xd9\x98F\x12.\n(NISCOPE_ATTRIBUTE_MEAS_FIR_FILTER_WINDOW\x10\xda\x98F\x12\'\n!NISCOPE_ATTRIBUTE_MEAS_ARRAY_GAIN\x10\xdb\x98F\x12)\n#NISCOPE_ATTRIBUTE_MEAS_ARRAY_OFFSET\x10\xdc\x98F\x12.\n(NISCOPE_ATTRIBUTE_MEAS_PERCENTAGE_METHOD\x10\xdd\x98F\x12&\n NISCOPE_ATTRIBUTE_ACQ_ARM_SOURCE\x10\xe5\x98F\x12(\n"NISCOPE_ATTRIBUTE_IS_PROBE_COMP_ON\x10\xf2\x98F\x12*\n$NISCOPE_ATTRIBUTE_USE_SPEC_INITIAL_X\x10\xf3\x98F\x126\n0NISCOPE_ATTRIBUTE_ALLOW_MORE_RECORDS_THAN_MEMORY\x10\xf4\x98F\x12+\n%NISCOPE_ATTRIBUTE_ONBOARD_MEMORY_SIZE\x10\xf5\x98F\x12(\n"NISCOPE_ATTRIBUTE_RIS_NUM_AVERAGES\x10\xf6\x98F\x12+\n%NISCOPE_ATTRIBUTE_RUNT_TIME_CONDITION\x10\xb4\x99F\x12+\n%NISCOPE_ATTRIBUTE_RUNT_TIME_LOW_LIMIT\x10\xb5\x99F\x12,\n&NISCOPE_ATTRIBUTE_RUNT_TIME_HIGH_LIMIT\x10\xb6\x99F\x12%\n\x1fNISCOPE_ATTRIBUTE_RUNT_POLARITY\x10\xff\xa7L\x12*\n$NISCOPE_ATTRIBUTE_RUNT_LOW_THRESHOLD\x10\xfe\xa7L\x12+\n%NISCOPE_ATTRIBUTE_RUNT_HIGH_THRESHOLD\x10\xfd\xa7L\x12"\n\x1cNISCOPE_ATTRIBUTE_RIS_METHOD\x10\xf7\x98F\x12.\n(NISCOPE_ATTRIBUTE_FETCH_INTERLEAVED_DATA\x10\xf8\x98F\x123\n-NISCOPE_ATTRIBUTE_MAX_REAL_TIME_SAMPLING_RATE\x10\xf9\x98F\x12$\n\x1eNISCOPE_ATTRIBUTE_MAX_RIS_RATE\x10\xfa\x98F\x12)\n#NISCOPE_ATTRIBUTE_TRIGGER_IMPEDANCE\x10\xfb\x98F\x12%\n\x1fNISCOPE_ATTRIBUTE_DEVICE_NUMBER\x10\xfc\x98F\x12)\n#NISCOPE_ATTRIBUTE_FETCH_RELATIVE_TO\x10\xfd\x98F\x12$\n\x1eNISCOPE_ATTRIBUTE_FETCH_OFFSET\x10\xfe\x98F\x12+\n%NISCOPE_ATTRIBUTE_FETCH_RECORD_NUMBER\x10\xff\x98F\x12)\n#NISCOPE_ATTRIBUTE_FETCH_NUM_RECORDS\x10\x80\x99F\x12.\n(NISCOPE_ATTRIBUTE_FETCH_MEAS_NUM_SAMPLES\x10\x81\x99F\x12#\n\x1dNISCOPE_ATTRIBUTE_POINTS_DONE\x10\x82\x99F\x12$\n\x1eNISCOPE_ATTRIBUTE_RECORDS_DONE\x10\x83\x99F\x12\x1f\n\x19NISCOPE_ATTRIBUTE_BACKLOG\x10\x84\x99F\x12%\n\x1fNISCOPE_ATTRIBUTE_POLL_INTERVAL\x10\x94\x99F\x12\'\n!NISCOPE_ATTRIBUTE_PLL_LOCK_STATUS\x10\xc7\xa2F\x12*\n$NISCOPE_ATTRIBUTE_DEVICE_TEMPERATURE\x10\x86\x99F\x12-\n\'NISCOPE_ATTRIBUTE_SAMP_CLK_TIMEBASE_SRC\x10\x87\x99F\x12.\n(NISCOPE_ATTRIBUTE_SAMP_CLK_TIMEBASE_RATE\x10\x88\x99F\x12-\n\'NISCOPE_ATTRIBUTE_SAMP_CLK_TIMEBASE_DIV\x10\x89\x99F\x12$\n\x1eNISCOPE_ATTRIBUTE_REF_CLK_RATE\x10\x8a\x99F\x12=\n7NISCOPE_ATTRIBUTE_EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL\x10\x8b\x99F\x12)\n#NISCOPE_ATTRIBUTE_ENABLE_DC_RESTORE\x10\x8d\x99F\x12$\n\x1eNISCOPE_ATTRIBUTE_ADV_TRIG_SRC\x10\x8e\x99F\x12(\n"NISCOPE_ATTRIBUTE_ARM_REF_TRIG_SRC\x10\x8f\x99F\x12+\n%NISCOPE_ATTRIBUTE_REF_TRIG_TDC_ENABLE\x10\x90\x99F\x12"\n\x1cNISCOPE_ATTRIBUTE_RESOLUTION\x10\x96\x99F\x124\n.NISCOPE_ATTRIBUTE_START_TO_REF_TRIGGER_HOLDOFF\x10\x97\x99F\x12%\n\x1fNISCOPE_ATTRIBUTE_SERIAL_NUMBER\x10\x98\x99F\x122\n,NISCOPE_ATTRIBUTE_OSCILLATOR_PHASE_DAC_VALUE\x10\x99\x99F\x120\n*NISCOPE_ATTRIBUTE_RIS_IN_AUTO_SETUP_ENABLE\x10\x9a\x99F\x126\n0NISCOPE_ATTRIBUTE_CHANNEL_TERMINAL_CONFIGURATION\x10\x9b\x99F\x12@\n:NISCOPE_ATTRIBUTE_EXPORTED_ADVANCE_TRIGGER_OUTPUT_TERMINAL\x10\x9d\x99F\x12=\n7NISCOPE_ATTRIBUTE_READY_FOR_START_EVENT_OUTPUT_TERMINAL\x10\x9e\x99F\x12;\n5NISCOPE_ATTRIBUTE_READY_FOR_REF_EVENT_OUTPUT_TERMINAL\x10\x9f\x99F\x12?\n9NISCOPE_ATTRIBUTE_READY_FOR_ADVANCE_EVENT_OUTPUT_TERMINAL\x10\xa0\x99F\x126\n0NISCOPE_ATTRIBUTE_FLEX_FIR_ANTIALIAS_FILTER_TYPE\x10\xbf\x9aF\x12#\n\x1dNISCOPE_ATTRIBUTE_DDC_ENABLED\x10\xdc\x9aF\x129\n3NISCOPE_ATTRIBUTE_DDC_FREQUENCY_TRANSLATION_ENABLED\x10\xde\x9aF\x12,\n&NISCOPE_ATTRIBUTE_DDC_CENTER_FREQUENCY\x10\xdf\x9aF\x120\n*NISCOPE_ATTRIBUTE_DDC_DATA_PROCESSING_MODE\x10\xe0\x9aF\x129\n3NISCOPE_ATTRIBUTE_DDC_FREQUENCY_TRANSLATION_PHASE_I\x10\xe1\x9aF\x129\n3NISCOPE_ATTRIBUTE_DDC_FREQUENCY_TRANSLATION_PHASE_Q\x10\xe2\x9aF\x12$\n\x1eNISCOPE_ATTRIBUTE_DIGITAL_GAIN\x10\xe3\x9aF\x12&\n NISCOPE_ATTRIBUTE_DIGITAL_OFFSET\x10\xe4\x9aF\x120\n*NISCOPE_ATTRIBUTE_OVERFLOW_ERROR_REPORTING\x10\xe5\x9aF\x12$\n\x1eNISCOPE_ATTRIBUTE_DDC_Q_SOURCE\x10\xe6\x9aF\x121\n+NISCOPE_ATTRIBUTE_FETCH_INTERLEAVED_IQ_DATA\x10\xe7\x9aF\x125\n/NISCOPE_ATTRIBUTE_EQUALIZATION_NUM_COEFFICIENTS\x10\xe8\x9aF\x123\n-NISCOPE_ATTRIBUTE_EQUALIZATION_FILTER_ENABLED\x10\xe9\x9aF\x125\n/NISCOPE_ATTRIBUTE_REF_TRIGGER_DETECTOR_LOCATION\x10\xea\x9aF\x126\n0NISCOPE_ATTRIBUTE_REF_TRIGGER_MINIMUM_QUIET_TIME\x10\xeb\x9aF\x128\n2NISCOPE_ATTRIBUTE_ENABLE_TIME_INTERLEAVED_SAMPLING\x10\xb0\x99F\x12(\n"NISCOPE_ATTRIBUTE_ENABLED_CHANNELS\x10\xbc\x99F\x120\n*NISCOPE_ATTRIBUTE_DATA_TRANSFER_BLOCK_SIZE\x10\xec\x9aF\x12(\n"NISCOPE_ATTRIBUTE_TRIGGER_MODIFIER\x10\xb6\xa6L\x12.\n(NISCOPE_ATTRIBUTE_TRIGGER_AUTO_TRIGGERED\x10\xc6\x9aF\x12>\n8NISCOPE_ATTRIBUTE_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL\x10\x91\x99F\x12<\n6NISCOPE_ATTRIBUTE_EXPORTED_REF_TRIGGER_OUTPUT_TERMINAL\x10\x92\x99F\x12;\n5NISCOPE_ATTRIBUTE_END_OF_RECORD_EVENT_OUTPUT_TERMINAL\x10\x93\x99F\x12@\n:NISCOPE_ATTRIBUTE_END_OF_ACQUISITION_EVENT_OUTPUT_TERMINAL\x10\x95\x99F\x12.\n(NISCOPE_ATTRIBUTE_5V_OUT_OUTPUT_TERMINAL\x10\xb1\x99F\x12/\n)NISCOPE_ATTRIBUTE_BANDPASS_FILTER_ENABLED\x10\xee\x9aF\x12&\n NISCOPE_ATTRIBUTE_DITHER_ENABLED\x10\xef\x9aF\x123\n-NISCOPE_ATTRIBUTE_FRACTIONAL_RESAMPLE_ENABLED\x10\xf0\x9aF\x12(\n"NISCOPE_ATTRIBUTE_GLITCH_CONDITION\x10\xe3\xa8L\x12$\n\x1eNISCOPE_ATTRIBUTE_GLITCH_WIDTH\x10\xe1\xa8L\x12\'\n!NISCOPE_ATTRIBUTE_GLITCH_POLARITY\x10\xe2\xa8L\x127\n1NISCOPE_ATTRIBUTE_DATA_TRANSFER_MAXIMUM_BANDWIDTH\x10\xf1\x9aF\x12;\n5NISCOPE_ATTRIBUTE_DATA_TRANSFER_PREFERRED_PACKET_SIZE\x10\xf2\x9aF\x12(\n"NISCOPE_ATTRIBUTE_SIGNAL_COND_GAIN\x10\xc7\x9aF\x12*\n$NISCOPE_ATTRIBUTE_SIGNAL_COND_OFFSET\x10\xc8\x9aF\x12#\n\x1dNISCOPE_ATTRIBUTE_P2P_ENABLED\x10\x82\x9bF\x12.\n(NISCOPE_ATTRIBUTE_P2P_CHANNELS_TO_STREAM\x10\x83\x9bF\x12)\n#NISCOPE_ATTRIBUTE_P2P_ENDPOINT_SIZE\x10\x86\x9bF\x125\n/NISCOPE_ATTRIBUTE_P2P_SAMPLES_AVAIL_IN_ENDPOINT\x10\xf8\x9aF\x12:\n4NISCOPE_ATTRIBUTE_P2P_MOST_SAMPLES_AVAIL_IN_ENDPOINT\x10\x85\x9bF\x12/\n)NISCOPE_ATTRIBUTE_P2P_SAMPLES_TRANSFERRED\x10\x84\x9bF\x12-\n\'NISCOPE_ATTRIBUTE_P2P_ENDPOINT_OVERFLOW\x10\x88\x9bF\x12/\n)NISCOPE_ATTRIBUTE_P2P_FIFO_ENDPOINT_COUNT\x10\x89\x9bF\x122\n,NISCOPE_ATTRIBUTE_P2P_ONBOARD_MEMORY_ENABLED\x10\x92\x9bF\x128\n2NISCOPE_ATTRIBUTE_P2P_MANUAL_CONFIGURATION_ENABLED\x10\x87\x9bF\x126\n0NISCOPE_ATTRIBUTE_P2P_DATA_TRANS_PERMISSION_ADDR\x10\xf9\x9aF\x12;\n5NISCOPE_ATTRIBUTE_P2P_DATA_TRANS_PERMISSION_ADDR_TYPE\x10\xfa\x9aF\x123\n-NISCOPE_ATTRIBUTE_P2P_DESTINATION_WINDOW_ADDR\x10\xfb\x9aF\x128\n2NISCOPE_ATTRIBUTE_P2P_DESTINATION_WINDOW_ADDR_TYPE\x10\xfc\x9aF\x123\n-NISCOPE_ATTRIBUTE_P2P_DESTINATION_WINDOW_SIZE\x10\xfd\x9aF\x122\n,NISCOPE_ATTRIBUTE_P2P_NOTIFY_PUSH_MESSAGE_ON\x10\xfe\x9aF\x124\n.NISCOPE_ATTRIBUTE_P2P_NOTIFY_MESSAGE_PUSH_ADDR\x10\xff\x9aF\x129\n3NISCOPE_ATTRIBUTE_P2P_NOTIFY_MESSAGE_PUSH_ADDR_TYPE\x10\x80\x9bF\x125\n/NISCOPE_ATTRIBUTE_P2P_NOTIFY_MESSAGE_PUSH_VALUE\x10\x81\x9bF\x12.\n(NISCOPE_ATTRIBUTE_SAMP_CLK_TIMEBASE_MULT\x10\x9f\x9bF\x12.\n(NISCOPE_ATTRIBUTE_P2P_STREAM_RELATIVE_TO\x10\xa5\x9bF\x12:\n4NISCOPE_ATTRIBUTE_P2P_SAMPLES_TRANSFERRED_PER_RECORD\x10\xac\x9bF\x12@\n:NISCOPE_ATTRIBUTE_END_OF_RECORD_TO_ADVANCE_TRIGGER_HOLDOFF\x10\x9e\x9bF\x124\n.NISCOPE_ATTRIBUTE_ABSOLUTE_SAMPLE_CLOCK_OFFSET\x10\xa6\x9bF\x12)\n#NISCOPE_ATTRIBUTE_FPGA_BITFILE_PATH\x10\xa7\x9bF\x12>\n8NISCOPE_ATTRIBUTE_INTERLEAVING_OFFSET_CORRECTION_ENABLED\x10\xa8\x9bF\x122\n,NISCOPE_ATTRIBUTE_HIGH_PASS_FILTER_FREQUENCY\x10\xa9\x9bF\x12>\n8NISCOPE_ATTRIBUTE_END_OF_ACQUISITION_EVENT_TERMINAL_NAME\x10\xbd\x99F\x129\n3NISCOPE_ATTRIBUTE_END_OF_RECORD_EVENT_TERMINAL_NAME\x10\xbe\x99F\x125\n/NISCOPE_ATTRIBUTE_ADVANCE_TRIGGER_TERMINAL_NAME\x10\xbf\x99F\x121\n+NISCOPE_ATTRIBUTE_REF_TRIGGER_TERMINAL_NAME\x10\xc0\x99F\x123\n-NISCOPE_ATTRIBUTE_START_TRIGGER_TERMINAL_NAME\x10\xc1\x99F\x12=\n7NISCOPE_ATTRIBUTE_READY_FOR_ADVANCE_EVENT_TERMINAL_NAME\x10\xc2\x99F\x129\n3NISCOPE_ATTRIBUTE_READY_FOR_REF_EVENT_TERMINAL_NAME\x10\xc3\x99F\x12;\n5NISCOPE_ATTRIBUTE_READY_FOR_START_EVENT_TERMINAL_NAME\x10\xc4\x99F*\xf4\x01\n\x0cWhichTrigger\x124\n0WHICH_TRIGGER_NISCOPE_VAL_SOFTWARE_TRIGGER_START\x10\x00\x12<\n8WHICH_TRIGGER_NISCOPE_VAL_SOFTWARE_TRIGGER_ARM_REFERENCE\x10\x01\x128\n4WHICH_TRIGGER_NISCOPE_VAL_SOFTWARE_TRIGGER_REFERENCE\x10\x02\x126\n2WHICH_TRIGGER_NISCOPE_VAL_SOFTWARE_TRIGGER_ADVANCE\x10\x03*\x85\x01\n\x10VerticalCoupling\x12$\n VERTICAL_COUPLING_NISCOPE_VAL_AC\x10\x00\x12$\n VERTICAL_COUPLING_NISCOPE_VAL_DC\x10\x01\x12%\n!VERTICAL_COUPLING_NISCOPE_VAL_GND\x10\x02*\xe8\x01\n\x0fTriggerCoupling\x12#\n\x1fTRIGGER_COUPLING_NISCOPE_VAL_AC\x10\x00\x12#\n\x1fTRIGGER_COUPLING_NISCOPE_VAL_DC\x10\x01\x12*\n&TRIGGER_COUPLING_NISCOPE_VAL_HF_REJECT\x10\x03\x12*\n&TRIGGER_COUPLING_NISCOPE_VAL_LF_REJECT\x10\x04\x123\n.TRIGGER_COUPLING_NISCOPE_VAL_AC_PLUS_HF_REJECT\x10\xe9\x07*\x8a\x01\n\x0cTriggerSlope\x12&\n"TRIGGER_SLOPE_NISCOPE_VAL_NEGATIVE\x10\x00\x12&\n"TRIGGER_SLOPE_NISCOPE_VAL_POSITIVE\x10\x01\x12*\n&TRIGGER_SLOPE_NISCOPE_VAL_SLOPE_EITHER\x10\x03*\x87\x01\n\rVideoPolarity\x12\x1e\n\x1aVIDEO_POLARITY_UNSPECIFIED\x10\x00\x12*\n&VIDEO_POLARITY_NISCOPE_VAL_TV_POSITIVE\x10\x01\x12*\n&VIDEO_POLARITY_NISCOPE_VAL_TV_NEGATIVE\x10\x02*\xcb\x02\n\x11VideoTriggerEvent\x12#\n\x1fVIDEO_TRIGGER_EVENT_UNSPECIFIED\x10\x00\x123\n/VIDEO_TRIGGER_EVENT_NISCOPE_VAL_TV_EVENT_FIELD1\x10\x01\x123\n/VIDEO_TRIGGER_EVENT_NISCOPE_VAL_TV_EVENT_FIELD2\x10\x02\x126\n2VIDEO_TRIGGER_EVENT_NISCOPE_VAL_TV_EVENT_ANY_FIELD\x10\x03\x125\n1VIDEO_TRIGGER_EVENT_NISCOPE_VAL_TV_EVENT_ANY_LINE\x10\x04\x128\n4VIDEO_TRIGGER_EVENT_NISCOPE_VAL_TV_EVENT_LINE_NUMBER\x10\x05*\x9c\x01\n\x0fGlitchCondition\x12 \n\x1cGLITCH_CONDITION_UNSPECIFIED\x10\x00\x124\n0GLITCH_CONDITION_NISCOPE_VAL_GLITCH_GREATER_THAN\x10\x02\x121\n-GLITCH_CONDITION_NISCOPE_VAL_GLITCH_LESS_THAN\x10\x01*\xc2\x01\n\x0eGlitchPolarity\x12\x1f\n\x1bGLITCH_POLARITY_UNSPECIFIED\x10\x00\x12/\n+GLITCH_POLARITY_NISCOPE_VAL_GLITCH_POSITIVE\x10\x01\x12/\n+GLITCH_POLARITY_NISCOPE_VAL_GLITCH_NEGATIVE\x10\x02\x12-\n)GLITCH_POLARITY_NISCOPE_VAL_GLITCH_EITHER\x10\x03*\x8e\x01\n\x0eWidthCondition\x12\x1f\n\x1bWIDTH_CONDITION_UNSPECIFIED\x10\x00\x12,\n(WIDTH_CONDITION_NISCOPE_VAL_WIDTH_WITHIN\x10\x01\x12-\n)WIDTH_CONDITION_NISCOPE_VAL_WIDTH_OUTSIDE\x10\x02*\xba\x01\n\rWidthPolarity\x12\x1e\n\x1aWIDTH_POLARITY_UNSPECIFIED\x10\x00\x12-\n)WIDTH_POLARITY_NISCOPE_VAL_WIDTH_POSITIVE\x10\x01\x12-\n)WIDTH_POLARITY_NISCOPE_VAL_WIDTH_NEGATIVE\x10\x02\x12+\n\'WIDTH_POLARITY_NISCOPE_VAL_WIDTH_EITHER\x10\x03*\xb2\x01\n\x0cRuntPolarity\x12\x1d\n\x19RUNT_POLARITY_UNSPECIFIED\x10\x00\x12+\n\'RUNT_POLARITY_NISCOPE_VAL_RUNT_POSITIVE\x10\x01\x12+\n\'RUNT_POLARITY_NISCOPE_VAL_RUNT_NEGATIVE\x10\x02\x12)\n%RUNT_POLARITY_NISCOPE_VAL_RUNT_EITHER\x10\x03*\x96\x07\n\x16ClockingTerminalValues\x12(\n$CLOCKING_TERMINAL_VALUES_UNSPECIFIED\x10\x00\x122\n.CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_NO_SOURCE\x10\x01\x123\n/CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_RTSI_CLOCK\x10\x02\x121\n-CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_EXTERNAL\x10\x03\x12.\n*CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_PFI_0\x10\x04\x12.\n*CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_PFI_1\x10\x05\x12.\n*CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_PFI_2\x10\x06\x12/\n+CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_CLK_IN\x10\x07\x120\n,CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_CLK_OUT\x10\x08\x12:\n6CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_INTERNAL10MHZ_OSC\x10\t\x120\n,CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_PXI_CLK\x10\n\x122\n.CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_PXI_CLK10\x10\x0b\x123\n/CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_PXI_CLK100\x10\x0c\x125\n1CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_PXIE_DSTAR_A\x10\r\x125\n1CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_AUX_0_CLK_IN\x10\x0e\x126\n2CLOCKING_TERMINAL_VALUES_NISCOPE_VAL_AUX_0_CLK_OUT\x10\x0f\x12F\nBCLOCKING_TERMINAL_VALUES_NISCOPE_VAL_ONBOARD_CONFIGURABLE_RATE_CLK\x10\x10*\xfa\x04\n\x11ExportableSignals\x12"\n\x1eEXPORTABLE_SIGNALS_UNSPECIFIED\x10\x00\x12.\n*EXPORTABLE_SIGNALS_NISCOPE_VAL_REF_TRIGGER\x10\x01\x120\n,EXPORTABLE_SIGNALS_NISCOPE_VAL_START_TRIGGER\x10\x02\x12;\n7EXPORTABLE_SIGNALS_NISCOPE_VAL_END_OF_ACQUISITION_EVENT\x10\x03\x126\n2EXPORTABLE_SIGNALS_NISCOPE_VAL_END_OF_RECORD_EVENT\x10\x04\x122\n.EXPORTABLE_SIGNALS_NISCOPE_VAL_ADVANCE_TRIGGER\x10\x05\x12:\n6EXPORTABLE_SIGNALS_NISCOPE_VAL_READY_FOR_ADVANCE_EVENT\x10\x06\x128\n4EXPORTABLE_SIGNALS_NISCOPE_VAL_READY_FOR_START_EVENT\x10\x07\x126\n2EXPORTABLE_SIGNALS_NISCOPE_VAL_READY_FOR_REF_EVENT\x10\n\x12)\n%EXPORTABLE_SIGNALS_NISCOPE_VAL_5V_OUT\x10\r\x12,\n(EXPORTABLE_SIGNALS_NISCOPE_VAL_REF_CLOCK\x10d\x12/\n+EXPORTABLE_SIGNALS_NISCOPE_VAL_SAMPLE_CLOCK\x10e*\xbc\x01\n\x11TriggerWindowMode\x123\n/TRIGGER_WINDOW_MODE_NISCOPE_VAL_ENTERING_WINDOW\x10\x00\x122\n.TRIGGER_WINDOW_MODE_NISCOPE_VAL_LEAVING_WINDOW\x10\x01\x12>\n:TRIGGER_WINDOW_MODE_NISCOPE_VAL_ENTERING_OR_LEAVING_WINDOW\x10\x02*\xb8\x01\n\x11AcquisitionStatus\x122\n.ACQUISITION_STATUS_NISCOPE_VAL_ACQ_IN_PROGRESS\x10\x00\x12/\n+ACQUISITION_STATUS_NISCOPE_VAL_ACQ_COMPLETE\x10\x01\x12>\n1ACQUISITION_STATUS_NISCOPE_VAL_ACQ_STATUS_UNKNOWN\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01*\xcf\x0f\n\x11ScalarMeasurement\x12,\n(SCALAR_MEASUREMENT_NISCOPE_VAL_RISE_TIME\x10\x00\x122\n-SCALAR_MEASUREMENT_NISCOPE_VAL_NO_MEASUREMENT\x10\xa0\x1f\x12,\n(SCALAR_MEASUREMENT_NISCOPE_VAL_FALL_TIME\x10\x01\x12,\n(SCALAR_MEASUREMENT_NISCOPE_VAL_FREQUENCY\x10\x02\x12)\n%SCALAR_MEASUREMENT_NISCOPE_VAL_PERIOD\x10\x03\x12.\n*SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_RMS\x10\x04\x127\n3SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_PEAK_TO_PEAK\x10\x05\x12.\n*SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_MAX\x10\x06\x12.\n*SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_MIN\x10\x07\x12/\n+SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HIGH\x10\x08\x12.\n*SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_LOW\x10\t\x122\n.SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_AVERAGE\x10\n\x12,\n(SCALAR_MEASUREMENT_NISCOPE_VAL_WIDTH_NEG\x10\x0b\x12,\n(SCALAR_MEASUREMENT_NISCOPE_VAL_WIDTH_POS\x10\x0c\x121\n-SCALAR_MEASUREMENT_NISCOPE_VAL_DUTY_CYCLE_NEG\x10\r\x121\n-SCALAR_MEASUREMENT_NISCOPE_VAL_DUTY_CYCLE_POS\x10\x0e\x12,\n(SCALAR_MEASUREMENT_NISCOPE_VAL_AMPLITUDE\x10\x0f\x124\n0SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_CYCLE_RMS\x10\x10\x128\n4SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_CYCLE_AVERAGE\x10\x11\x12,\n(SCALAR_MEASUREMENT_NISCOPE_VAL_OVERSHOOT\x10\x12\x12+\n\'SCALAR_MEASUREMENT_NISCOPE_VAL_PRESHOOT\x10\x13\x121\n,SCALAR_MEASUREMENT_NISCOPE_VAL_LOW_REF_VOLTS\x10\xe8\x07\x121\n,SCALAR_MEASUREMENT_NISCOPE_VAL_MID_REF_VOLTS\x10\xe9\x07\x122\n-SCALAR_MEASUREMENT_NISCOPE_VAL_HIGH_REF_VOLTS\x10\xea\x07\x12(\n#SCALAR_MEASUREMENT_NISCOPE_VAL_AREA\x10\xeb\x07\x12.\n)SCALAR_MEASUREMENT_NISCOPE_VAL_CYCLE_AREA\x10\xec\x07\x12,\n\'SCALAR_MEASUREMENT_NISCOPE_VAL_INTEGRAL\x10\xed\x07\x120\n+SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_BASE\x10\xee\x07\x12/\n*SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_TOP\x10\xef\x07\x121\n,SCALAR_MEASUREMENT_NISCOPE_VAL_FFT_FREQUENCY\x10\xf0\x07\x121\n,SCALAR_MEASUREMENT_NISCOPE_VAL_FFT_AMPLITUDE\x10\xf1\x07\x122\n-SCALAR_MEASUREMENT_NISCOPE_VAL_RISE_SLEW_RATE\x10\xf2\x07\x122\n-SCALAR_MEASUREMENT_NISCOPE_VAL_FALL_SLEW_RATE\x10\xf3\x07\x12/\n*SCALAR_MEASUREMENT_NISCOPE_VAL_AC_ESTIMATE\x10\xf4\x07\x12/\n*SCALAR_MEASUREMENT_NISCOPE_VAL_DC_ESTIMATE\x10\xf5\x07\x12.\n)SCALAR_MEASUREMENT_NISCOPE_VAL_TIME_DELAY\x10\xf6\x07\x122\n-SCALAR_MEASUREMENT_NISCOPE_VAL_AVERAGE_PERIOD\x10\xf7\x07\x125\n0SCALAR_MEASUREMENT_NISCOPE_VAL_AVERAGE_FREQUENCY\x10\xf8\x07\x127\n2SCALAR_MEASUREMENT_NISCOPE_VAL_VOLTAGE_BASE_TO_TOP\x10\xf9\x07\x12/\n*SCALAR_MEASUREMENT_NISCOPE_VAL_PHASE_DELAY\x10\xfa\x07*\xd4\x0b\n\x10ArrayMeasurement\x12!\n\x1dARRAY_MEASUREMENT_UNSPECIFIED\x10\x00\x121\n,ARRAY_MEASUREMENT_NISCOPE_VAL_NO_MEASUREMENT\x10\xa0\x1f\x125\n0ARRAY_MEASUREMENT_NISCOPE_VAL_LAST_ACQ_HISTOGRAM\x10\xa1\x1f\x125\n0ARRAY_MEASUREMENT_NISCOPE_VAL_FFT_PHASE_SPECTRUM\x10\xa2\x1f\x12=\n8ARRAY_MEASUREMENT_NISCOPE_VAL_FFT_AMP_SPECTRUM_VOLTS_RMS\x10\xa3\x1f\x12>\n9ARRAY_MEASUREMENT_NISCOPE_VAL_MULTI_ACQ_VOLTAGE_HISTOGRAM\x10\xa4\x1f\x12;\n6ARRAY_MEASUREMENT_NISCOPE_VAL_MULTI_ACQ_TIME_HISTOGRAM\x10\xa5\x1f\x121\n,ARRAY_MEASUREMENT_NISCOPE_VAL_ARRAY_INTEGRAL\x10\xa6\x1f\x12-\n(ARRAY_MEASUREMENT_NISCOPE_VAL_DERIVATIVE\x10\xa7\x1f\x12*\n%ARRAY_MEASUREMENT_NISCOPE_VAL_INVERSE\x10\xa8\x1f\x121\n,ARRAY_MEASUREMENT_NISCOPE_VAL_HANNING_WINDOW\x10\xa9\x1f\x122\n-ARRAY_MEASUREMENT_NISCOPE_VAL_FLAT_TOP_WINDOW\x10\xaa\x1f\x12;\n6ARRAY_MEASUREMENT_NISCOPE_VAL_POLYNOMIAL_INTERPOLATION\x10\xab\x1f\x124\n/ARRAY_MEASUREMENT_NISCOPE_VAL_MULTIPLY_CHANNELS\x10\xac\x1f\x12/\n*ARRAY_MEASUREMENT_NISCOPE_VAL_ADD_CHANNELS\x10\xad\x1f\x124\n/ARRAY_MEASUREMENT_NISCOPE_VAL_SUBTRACT_CHANNELS\x10\xae\x1f\x122\n-ARRAY_MEASUREMENT_NISCOPE_VAL_DIVIDE_CHANNELS\x10\xaf\x1f\x124\n/ARRAY_MEASUREMENT_NISCOPE_VAL_MULTI_ACQ_AVERAGE\x10\xb0\x1f\x125\n0ARRAY_MEASUREMENT_NISCOPE_VAL_BUTTERWORTH_FILTER\x10\xb1\x1f\x123\n.ARRAY_MEASUREMENT_NISCOPE_VAL_CHEBYSHEV_FILTER\x10\xb2\x1f\x126\n1ARRAY_MEASUREMENT_NISCOPE_VAL_FFT_AMP_SPECTRUM_DB\x10\xb3\x1f\x121\n,ARRAY_MEASUREMENT_NISCOPE_VAL_HAMMING_WINDOW\x10\xb4\x1f\x126\n1ARRAY_MEASUREMENT_NISCOPE_VAL_WINDOWED_FIR_FILTER\x10\xb5\x1f\x120\n+ARRAY_MEASUREMENT_NISCOPE_VAL_BESSEL_FILTER\x10\xb6\x1f\x122\n-ARRAY_MEASUREMENT_NISCOPE_VAL_TRIANGLE_WINDOW\x10\xb7\x1f\x122\n-ARRAY_MEASUREMENT_NISCOPE_VAL_BLACKMAN_WINDOW\x10\xb8\x1f\x12/\n*ARRAY_MEASUREMENT_NISCOPE_VAL_ARRAY_OFFSET\x10\xb9\x1f\x12-\n(ARRAY_MEASUREMENT_NISCOPE_VAL_ARRAY_GAIN\x10\xba\x1f*\xa1\x01\n\x10CalibrationTypes\x12.\n*CALIBRATION_TYPES_NISCOPE_VAL_CAL_EXTERNAL\x10\x00\x12*\n&CALIBRATION_TYPES_NISCOPE_VAL_CAL_SELF\x10\x01\x121\n-CALIBRATION_TYPES_NISCOPE_VAL_CAL_MANUFACTURE\x10\x02*\xb3\x1e\n\x14ClearableMeasurement\x12/\n+CLEARABLE_MEASUREMENT_NISCOPE_VAL_RISE_TIME\x10\x00\x127\n2CLEARABLE_MEASUREMENT_NISCOPE_VAL_ALL_MEASUREMENTS\x10\x90N\x12B\n=CLEARABLE_MEASUREMENT_NISCOPE_VAL_MULTI_ACQ_VOLTAGE_HISTOGRAM\x10\xa4\x1f\x12?\n:CLEARABLE_MEASUREMENT_NISCOPE_VAL_MULTI_ACQ_TIME_HISTOGRAM\x10\xa5\x1f\x128\n3CLEARABLE_MEASUREMENT_NISCOPE_VAL_MULTI_ACQ_AVERAGE\x10\xb0\x1f\x12/\n+CLEARABLE_MEASUREMENT_NISCOPE_VAL_FREQUENCY\x10\x02\x128\n3CLEARABLE_MEASUREMENT_NISCOPE_VAL_AVERAGE_FREQUENCY\x10\xf8\x07\x124\n/CLEARABLE_MEASUREMENT_NISCOPE_VAL_FFT_FREQUENCY\x10\xf0\x07\x12,\n(CLEARABLE_MEASUREMENT_NISCOPE_VAL_PERIOD\x10\x03\x125\n0CLEARABLE_MEASUREMENT_NISCOPE_VAL_AVERAGE_PERIOD\x10\xf7\x07\x12/\n+CLEARABLE_MEASUREMENT_NISCOPE_VAL_FALL_TIME\x10\x01\x125\n0CLEARABLE_MEASUREMENT_NISCOPE_VAL_RISE_SLEW_RATE\x10\xf2\x07\x125\n0CLEARABLE_MEASUREMENT_NISCOPE_VAL_FALL_SLEW_RATE\x10\xf3\x07\x12/\n+CLEARABLE_MEASUREMENT_NISCOPE_VAL_OVERSHOOT\x10\x12\x12.\n*CLEARABLE_MEASUREMENT_NISCOPE_VAL_PRESHOOT\x10\x13\x121\n-CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_RMS\x10\x04\x127\n3CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_CYCLE_RMS\x10\x10\x122\n-CLEARABLE_MEASUREMENT_NISCOPE_VAL_AC_ESTIMATE\x10\xf4\x07\x124\n/CLEARABLE_MEASUREMENT_NISCOPE_VAL_FFT_AMPLITUDE\x10\xf1\x07\x125\n1CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_AVERAGE\x10\n\x12;\n7CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_CYCLE_AVERAGE\x10\x11\x122\n-CLEARABLE_MEASUREMENT_NISCOPE_VAL_DC_ESTIMATE\x10\xf5\x07\x121\n-CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_MAX\x10\x06\x121\n-CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_MIN\x10\x07\x12:\n6CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_PEAK_TO_PEAK\x10\x05\x122\n.CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HIGH\x10\x08\x121\n-CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_LOW\x10\t\x12/\n+CLEARABLE_MEASUREMENT_NISCOPE_VAL_AMPLITUDE\x10\x0f\x122\n-CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_TOP\x10\xef\x07\x123\n.CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_BASE\x10\xee\x07\x12:\n5CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_BASE_TO_TOP\x10\xf9\x07\x12/\n+CLEARABLE_MEASUREMENT_NISCOPE_VAL_WIDTH_NEG\x10\x0b\x12/\n+CLEARABLE_MEASUREMENT_NISCOPE_VAL_WIDTH_POS\x10\x0c\x124\n0CLEARABLE_MEASUREMENT_NISCOPE_VAL_DUTY_CYCLE_NEG\x10\r\x124\n0CLEARABLE_MEASUREMENT_NISCOPE_VAL_DUTY_CYCLE_POS\x10\x0e\x12/\n*CLEARABLE_MEASUREMENT_NISCOPE_VAL_INTEGRAL\x10\xed\x07\x12+\n&CLEARABLE_MEASUREMENT_NISCOPE_VAL_AREA\x10\xeb\x07\x121\n,CLEARABLE_MEASUREMENT_NISCOPE_VAL_CYCLE_AREA\x10\xec\x07\x121\n,CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_DELAY\x10\xf6\x07\x122\n-CLEARABLE_MEASUREMENT_NISCOPE_VAL_PHASE_DELAY\x10\xfa\x07\x124\n/CLEARABLE_MEASUREMENT_NISCOPE_VAL_LOW_REF_VOLTS\x10\xe8\x07\x124\n/CLEARABLE_MEASUREMENT_NISCOPE_VAL_MID_REF_VOLTS\x10\xe9\x07\x125\n0CLEARABLE_MEASUREMENT_NISCOPE_VAL_HIGH_REF_VOLTS\x10\xea\x07\x12=\n8CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN\x10\xd0\x0f\x12>\n9CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_STDEV\x10\xd1\x0f\x12?\n:CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEDIAN\x10\xd3\x0f\x12=\n8CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_MODE\x10\xda\x0f\x12<\n7CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_MAX\x10\xd5\x0f\x12<\n7CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_MIN\x10\xd6\x0f\x12E\n@CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_PEAK_TO_PEAK\x10\xd2\x0f\x12H\nCCLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_STDEV\x10\xd7\x0f\x12J\nECLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_2_STDEV\x10\xd8\x0f\x12J\nECLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_MEAN_PLUS_3_STDEV\x10\xd9\x0f\x12=\n8CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_HITS\x10\xd4\x0f\x12A\n<CLEARABLE_MEASUREMENT_NISCOPE_VAL_VOLTAGE_HISTOGRAM_NEW_HITS\x10\xdb\x0f\x12:\n5CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_MEAN\x10\xb8\x17\x12;\n6CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_STDEV\x10\xb9\x17\x12<\n7CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_MEDIAN\x10\xbb\x17\x12:\n5CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_MODE\x10\xc2\x17\x129\n4CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_MAX\x10\xbd\x17\x129\n4CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_MIN\x10\xbe\x17\x12B\n=CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_PEAK_TO_PEAK\x10\xba\x17\x12E\n@CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_STDEV\x10\xbf\x17\x12G\nBCLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_2_STDEV\x10\xc0\x17\x12G\nBCLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_MEAN_PLUS_3_STDEV\x10\xc1\x17\x12:\n5CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_HITS\x10\xbc\x17\x12>\n9CLEARABLE_MEASUREMENT_NISCOPE_VAL_TIME_HISTOGRAM_NEW_HITS\x10\xc3\x17*q\n\x06Option\x122\n.OPTION_NISCOPE_VAL_SELF_CALIBRATE_ALL_CHANNELS\x10\x00\x123\n/OPTION_NISCOPE_VAL_RESTORE_EXTERNAL_CALIBRATION\x10\x01*\x80\t\n\x11VideoSignalFormat\x12#\n\x1fVIDEO_SIGNAL_FORMAT_UNSPECIFIED\x10\x00\x12(\n$VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_NTSC\x10\x01\x12\'\n#VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_PAL\x10\x02\x12)\n%VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_SECAM\x10\x03\x12*\n%VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_M_PAL\x10\xe9\x07\x12G\nBVIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_480I_59_94_FIELDS_PER_SECOND\x10\xf2\x07\x12D\n?VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_480I_60_FIELDS_PER_SECOND\x10\xf3\x07\x12G\nBVIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_480P_59_94_FRAMES_PER_SECOND\x10\xf7\x07\x12D\n?VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_480P_60_FRAMES_PER_SECOND\x10\xf8\x07\x12D\n?VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_576I_50_FIELDS_PER_SECOND\x10\xfc\x07\x12D\n?VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_576P_50_FRAMES_PER_SECOND\x10\x81\x08\x12D\n?VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_720P_50_FRAMES_PER_SECOND\x10\x87\x08\x12G\nBVIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_720P_59_94_FRAMES_PER_SECOND\x10\x88\x08\x12D\n?VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_720P_60_FRAMES_PER_SECOND\x10\x89\x08\x12E\n@VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_1080I_50_FIELDS_PER_SECOND\x10\x90\x08\x12H\nCVIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_1080I_59_94_FIELDS_PER_SECOND\x10\x91\x08\x12E\n@VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_1080I_60_FIELDS_PER_SECOND\x10\x92\x08\x12E\n@VIDEO_SIGNAL_FORMAT_NISCOPE_VAL_VIDEO_1080P_24_FRAMES_PER_SECOND\x10\x95\x08*\xad5\n\x1bNiScopeInt32AttributeValues\x12\x1d\n\x19NISCOPE_INT32_UNSPECIFIED\x10\x00\x12-\n)NISCOPE_INT32_ACQUISITION_TYPE_VAL_NORMAL\x10\x00\x12/\n*NISCOPE_INT32_ACQUISITION_TYPE_VAL_FLEXRES\x10\xe9\x07\x12+\n&NISCOPE_INT32_ACQUISITION_TYPE_VAL_DDC\x10\xea\x07\x120\n,NISCOPE_INT32_ADDRESS_TYPE_VAL_ADDR_PHYSICAL\x10\x00\x12/\n+NISCOPE_INT32_ADDRESS_TYPE_VAL_ADDR_VIRTUAL\x10\x01\x12/\n+NISCOPE_INT32_DATA_PROCESSING_MODE_VAL_REAL\x10\x00\x122\n.NISCOPE_INT32_DATA_PROCESSING_MODE_VAL_COMPLEX\x10\x01\x12,\n(NISCOPE_INT32_FIR_FILTER_WINDOW_VAL_NONE\x10\x00\x120\n+NISCOPE_INT32_FIR_FILTER_WINDOW_VAL_HANNING\x10\x99\x03\x121\n,NISCOPE_INT32_FIR_FILTER_WINDOW_VAL_FLAT_TOP\x10\x9a\x03\x120\n+NISCOPE_INT32_FIR_FILTER_WINDOW_VAL_HAMMING\x10\xa4\x03\x121\n,NISCOPE_INT32_FIR_FILTER_WINDOW_VAL_TRIANGLE\x10\xa7\x03\x121\n,NISCOPE_INT32_FIR_FILTER_WINDOW_VAL_BLACKMAN\x10\xa8\x03\x125\n0NISCOPE_INT32_FETCH_RELATIVE_TO_VAL_READ_POINTER\x10\x84\x03\x123\n.NISCOPE_INT32_FETCH_RELATIVE_TO_VAL_PRETRIGGER\x10\xdd\x03\x12,\n\'NISCOPE_INT32_FETCH_RELATIVE_TO_VAL_NOW\x10\xe1\x03\x12.\n)NISCOPE_INT32_FETCH_RELATIVE_TO_VAL_START\x10\xe2\x03\x120\n+NISCOPE_INT32_FETCH_RELATIVE_TO_VAL_TRIGGER\x10\xe3\x03\x12D\n@NISCOPE_INT32_FLEX_FIR_ANTIALIAS_FILTER_TYPE_VAL_48_TAP_STANDARD\x10\x00\x12C\n?NISCOPE_INT32_FLEX_FIR_ANTIALIAS_FILTER_TYPE_VAL_48_TAP_HANNING\x10\x01\x12C\n?NISCOPE_INT32_FLEX_FIR_ANTIALIAS_FILTER_TYPE_VAL_16_TAP_HANNING\x10\x02\x12B\n>NISCOPE_INT32_FLEX_FIR_ANTIALIAS_FILTER_TYPE_VAL_8_TAP_HANNING\x10\x03\x12:\n6NISCOPE_INT32_GLITCH_CONDITION_VAL_GLITCH_GREATER_THAN\x10\x02\x127\n3NISCOPE_INT32_GLITCH_CONDITION_VAL_GLITCH_LESS_THAN\x10\x01\x125\n1NISCOPE_INT32_GLITCH_POLARITY_VAL_GLITCH_POSITIVE\x10\x01\x125\n1NISCOPE_INT32_GLITCH_POLARITY_VAL_GLITCH_NEGATIVE\x10\x02\x123\n/NISCOPE_INT32_GLITCH_POLARITY_VAL_GLITCH_EITHER\x10\x03\x123\n/NISCOPE_INT32_MEAS_FILTER_TYPE_VAL_MEAS_LOWPASS\x10\x00\x124\n0NISCOPE_INT32_MEAS_FILTER_TYPE_VAL_MEAS_HIGHPASS\x10\x01\x124\n0NISCOPE_INT32_MEAS_FILTER_TYPE_VAL_MEAS_BANDPASS\x10\x02\x124\n0NISCOPE_INT32_MEAS_FILTER_TYPE_VAL_MEAS_BANDSTOP\x10\x03\x12:\n6NISCOPE_INT32_MEAS_PERCENTAGE_METHOD_VAL_MEAS_LOW_HIGH\x10\x00\x129\n5NISCOPE_INT32_MEAS_PERCENTAGE_METHOD_VAL_MEAS_MIN_MAX\x10\x01\x12:\n6NISCOPE_INT32_MEAS_PERCENTAGE_METHOD_VAL_MEAS_BASE_TOP\x10\x02\x127\n3NISCOPE_INT32_MEAS_REF_LEVEL_UNITS_VAL_MEAS_VOLTAGE\x10\x00\x12:\n6NISCOPE_INT32_MEAS_REF_LEVEL_UNITS_VAL_MEAS_PERCENTAGE\x10\x01\x124\n0NISCOPE_INT32_NOTIFICATION_TYPE_VAL_NOTIFY_NEVER\x10\x00\x123\n/NISCOPE_INT32_NOTIFICATION_TYPE_VAL_NOTIFY_DONE\x10\x01\x12D\n@NISCOPE_INT32_OVERFLOW_ERROR_REPORTING_VAL_ERROR_REPORTING_ERROR\x10\x00\x12F\nBNISCOPE_INT32_OVERFLOW_ERROR_REPORTING_VAL_ERROR_REPORTING_WARNING\x10\x01\x12G\nCNISCOPE_INT32_OVERFLOW_ERROR_REPORTING_VAL_ERROR_REPORTING_DISABLED\x10\x02\x12N\nJNISCOPE_INT32_P2_P_STREAM_RELATIVE_TO_VAL_STREAM_RELATIVE_TO_START_TRIGGER\x10\x00\x12R\nNNISCOPE_INT32_P2_P_STREAM_RELATIVE_TO_VAL_STREAM_RELATIVE_TO_REFERENCE_TRIGGER\x10\x01\x12M\nINISCOPE_INT32_P2_P_STREAM_RELATIVE_TO_VAL_STREAM_RELATIVE_TO_SYNC_TRIGGER\x10\x02\x127\n3NISCOPE_INT32_RIS_METHOD_VAL_RIS_EXACT_NUM_AVERAGES\x10\x01\x125\n1NISCOPE_INT32_RIS_METHOD_VAL_RIS_MIN_NUM_AVERAGES\x10\x02\x12/\n+NISCOPE_INT32_RIS_METHOD_VAL_RIS_INCOMPLETE\x10\x03\x126\n2NISCOPE_INT32_RIS_METHOD_VAL_RIS_LIMITED_BIN_WIDTH\x10\x05\x12L\nHNISCOPE_INT32_REF_TRIGGER_DETECTOR_LOCATION_VAL_ANALOG_DETECTION_CIRCUIT\x10\x00\x12>\n:NISCOPE_INT32_REF_TRIGGER_DETECTOR_LOCATION_VAL_DDC_OUTPUT\x10\x01\x121\n-NISCOPE_INT32_RUNT_POLARITY_VAL_RUNT_POSITIVE\x10\x01\x121\n-NISCOPE_INT32_RUNT_POLARITY_VAL_RUNT_NEGATIVE\x10\x02\x12/\n+NISCOPE_INT32_RUNT_POLARITY_VAL_RUNT_EITHER\x10\x03\x12B\n>NISCOPE_INT32_RUNT_TIME_CONDITION_VAL_RUNT_TIME_CONDITION_NONE\x10\x00\x12D\n@NISCOPE_INT32_RUNT_TIME_CONDITION_VAL_RUNT_TIME_CONDITION_WITHIN\x10\x01\x12E\nANISCOPE_INT32_RUNT_TIME_CONDITION_VAL_RUNT_TIME_CONDITION_OUTSIDE\x10\x02\x12+\n\'NISCOPE_INT32_SAMPLE_MODE_VAL_REAL_TIME\x10\x00\x121\n-NISCOPE_INT32_SAMPLE_MODE_VAL_EQUIVALENT_TIME\x10\x01\x129\n5NISCOPE_INT32_TERMINAL_CONFIGURATION_VAL_SINGLE_ENDED\x10\x00\x12D\n@NISCOPE_INT32_TERMINAL_CONFIGURATION_VAL_UNBALANCED_DIFFERENTIAL\x10\x01\x129\n5NISCOPE_INT32_TERMINAL_CONFIGURATION_VAL_DIFFERENTIAL\x10\x02\x12)\n%NISCOPE_INT32_TRIGGER_COUPLING_VAL_AC\x10\x00\x12)\n%NISCOPE_INT32_TRIGGER_COUPLING_VAL_DC\x10\x01\x120\n,NISCOPE_INT32_TRIGGER_COUPLING_VAL_HF_REJECT\x10\x03\x120\n,NISCOPE_INT32_TRIGGER_COUPLING_VAL_LF_REJECT\x10\x04\x129\n4NISCOPE_INT32_TRIGGER_COUPLING_VAL_AC_PLUS_HF_REJECT\x10\xe9\x07\x125\n1NISCOPE_INT32_TRIGGER_MODIFIER_VAL_NO_TRIGGER_MOD\x10\x01\x12+\n\'NISCOPE_INT32_TRIGGER_MODIFIER_VAL_AUTO\x10\x02\x121\n-NISCOPE_INT32_TRIGGER_MODIFIER_VAL_AUTO_LEVEL\x10\x03\x12,\n(NISCOPE_INT32_TRIGGER_SLOPE_VAL_NEGATIVE\x10\x00\x12,\n(NISCOPE_INT32_TRIGGER_SLOPE_VAL_POSITIVE\x10\x01\x120\n,NISCOPE_INT32_TRIGGER_SLOPE_VAL_SLOPE_EITHER\x10\x03\x12/\n+NISCOPE_INT32_TRIGGER_TYPE_VAL_EDGE_TRIGGER\x10\x01\x126\n1NISCOPE_INT32_TRIGGER_TYPE_VAL_HYSTERESIS_TRIGGER\x10\xe9\x07\x123\n.NISCOPE_INT32_TRIGGER_TYPE_VAL_DIGITAL_TRIGGER\x10\xea\x07\x122\n-NISCOPE_INT32_TRIGGER_TYPE_VAL_WINDOW_TRIGGER\x10\xeb\x07\x124\n/NISCOPE_INT32_TRIGGER_TYPE_VAL_SOFTWARE_TRIGGER\x10\xec\x07\x12-\n)NISCOPE_INT32_TRIGGER_TYPE_VAL_TV_TRIGGER\x10\x05\x121\n-NISCOPE_INT32_TRIGGER_TYPE_VAL_GLITCH_TRIGGER\x10\x04\x120\n,NISCOPE_INT32_TRIGGER_TYPE_VAL_WIDTH_TRIGGER\x10\x02\x12/\n+NISCOPE_INT32_TRIGGER_TYPE_VAL_RUNT_TRIGGER\x10\x03\x124\n0NISCOPE_INT32_TRIGGER_TYPE_VAL_IMMEDIATE_TRIGGER\x10\x06\x129\n5NISCOPE_INT32_TRIGGER_WINDOW_MODE_VAL_ENTERING_WINDOW\x10\x00\x128\n4NISCOPE_INT32_TRIGGER_WINDOW_MODE_VAL_LEAVING_WINDOW\x10\x01\x12D\n@NISCOPE_INT32_TRIGGER_WINDOW_MODE_VAL_ENTERING_OR_LEAVING_WINDOW\x10\x02\x12*\n&NISCOPE_INT32_VERTICAL_COUPLING_VAL_AC\x10\x00\x12*\n&NISCOPE_INT32_VERTICAL_COUPLING_VAL_DC\x10\x01\x12+\n\'NISCOPE_INT32_VERTICAL_COUPLING_VAL_GND\x10\x02\x120\n,NISCOPE_INT32_VIDEO_POLARITY_VAL_TV_POSITIVE\x10\x01\x120\n,NISCOPE_INT32_VIDEO_POLARITY_VAL_TV_NEGATIVE\x10\x02\x12.\n*NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_NTSC\x10\x01\x12-\n)NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_PAL\x10\x02\x12/\n+NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_SECAM\x10\x03\x120\n+NISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_M_PAL\x10\xe9\x07\x12M\nHNISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_480I_59_94_FIELDS_PER_SECOND\x10\xf2\x07\x12J\nENISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_480I_60_FIELDS_PER_SECOND\x10\xf3\x07\x12M\nHNISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_480P_59_94_FRAMES_PER_SECOND\x10\xf7\x07\x12J\nENISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_480P_60_FRAMES_PER_SECOND\x10\xf8\x07\x12J\nENISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_576I_50_FIELDS_PER_SECOND\x10\xfc\x07\x12J\nENISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_576P_50_FRAMES_PER_SECOND\x10\x81\x08\x12J\nENISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_720P_50_FRAMES_PER_SECOND\x10\x87\x08\x12M\nHNISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_720P_59_94_FRAMES_PER_SECOND\x10\x88\x08\x12J\nENISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_720P_60_FRAMES_PER_SECOND\x10\x89\x08\x12K\nFNISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_1080I_50_FIELDS_PER_SECOND\x10\x90\x08\x12N\nINISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_1080I_59_94_FIELDS_PER_SECOND\x10\x91\x08\x12K\nFNISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_1080I_60_FIELDS_PER_SECOND\x10\x92\x08\x12K\nFNISCOPE_INT32_VIDEO_SIGNAL_FORMAT_VAL_VIDEO_1080P_24_FRAMES_PER_SECOND\x10\x95\x08\x129\n5NISCOPE_INT32_VIDEO_TRIGGER_EVENT_VAL_TV_EVENT_FIELD1\x10\x01\x129\n5NISCOPE_INT32_VIDEO_TRIGGER_EVENT_VAL_TV_EVENT_FIELD2\x10\x02\x12<\n8NISCOPE_INT32_VIDEO_TRIGGER_EVENT_VAL_TV_EVENT_ANY_FIELD\x10\x03\x12;\n7NISCOPE_INT32_VIDEO_TRIGGER_EVENT_VAL_TV_EVENT_ANY_LINE\x10\x04\x12>\n:NISCOPE_INT32_VIDEO_TRIGGER_EVENT_VAL_TV_EVENT_LINE_NUMBER\x10\x05\x122\n.NISCOPE_INT32_WIDTH_CONDITION_VAL_WIDTH_WITHIN\x10\x01\x123\n/NISCOPE_INT32_WIDTH_CONDITION_VAL_WIDTH_OUTSIDE\x10\x02\x123\n/NISCOPE_INT32_WIDTH_POLARITY_VAL_WIDTH_POSITIVE\x10\x01\x123\n/NISCOPE_INT32_WIDTH_POLARITY_VAL_WIDTH_NEGATIVE\x10\x02\x121\n-NISCOPE_INT32_WIDTH_POLARITY_VAL_WIDTH_EITHER\x10\x03\x1a\x02\x10\x01*\xc9\x01\n\x1cNiScopeReal64AttributeValues\x12\x1e\n\x1aNISCOPE_REAL64_UNSPECIFIED\x10\x00\x12A\n=NISCOPE_REAL64_CABLE_SENSE_MODE_VAL_CABLE_SENSE_MODE_DISABLED\x10\x00\x12B\n>NISCOPE_REAL64_CABLE_SENSE_MODE_VAL_CABLE_SENSE_MODE_ON_DEMAND\x10\x01\x1a\x02\x10\x01*\xe3\x04\n"NiScopeReal64AttributeValuesMapped\x12%\n!NISCOPE_REAL64_MAPPED_UNSPECIFIED\x10\x00\x12.\n*NISCOPE_REAL64_INPUT_IMPEDANCE_VAL_50_OHMS\x10\x01\x12.\n*NISCOPE_REAL64_INPUT_IMPEDANCE_VAL_75_OHMS\x10\x02\x120\n,NISCOPE_REAL64_INPUT_IMPEDANCE_VAL_1_MEG_OHM\x10\x03\x12C\n?NISCOPE_REAL64_MAX_INPUT_FREQUENCY_VAL_BANDWIDTH_DEVICE_DEFAULT\x10\x04\x129\n5NISCOPE_REAL64_MAX_INPUT_FREQUENCY_VAL_BANDWIDTH_FULL\x10\x05\x12:\n6NISCOPE_REAL64_MAX_INPUT_FREQUENCY_VAL_20MHZ_BANDWIDTH\x10\x06\x12;\n7NISCOPE_REAL64_MAX_INPUT_FREQUENCY_VAL_100MHZ_BANDWIDTH\x10\x07\x12D\n@NISCOPE_REAL64_MAX_INPUT_FREQUENCY_VAL_20MHZ_MAX_INPUT_FREQUENCY\x10\x08\x12E\nANISCOPE_REAL64_MAX_INPUT_FREQUENCY_VAL_100MHZ_MAX_INPUT_FREQUENCY\x10\t*\x9e\x11\n"NiScopeStringAttributeValuesMapped\x12%\n!NISCOPE_STRING_MAPPED_UNSPECIFIED\x10\x00\x123\n/NISCOPE_STRING_SAMP_CLK_TIMEPACE_SRC_VAL_CLK_IN\x10\x01\x126\n2NISCOPE_STRING_SAMP_CLK_TIMEPACE_SRC_VAL_NO_SOURCE\x10\x02\x125\n1NISCOPE_STRING_SAMP_CLK_TIMEPACE_SRC_VAL_PXI_STAR\x10\x03\x129\n5NISCOPE_STRING_SAMP_CLK_TIMEPACE_SRC_VAL_PXIE_DSTAR_A\x10\x04\x129\n5NISCOPE_STRING_SAMP_CLK_TIMEPACE_SRC_VAL_AUX_0_CLK_IN\x10\x05\x12J\nFNISCOPE_STRING_SAMP_CLK_TIMEPACE_SRC_VAL_ONBOARD_CONFIGURABLE_RATE_CLK\x10\x06\x12/\n+NISCOPE_STRING_TRIGGER_SOURCE_VAL_IMMEDIATE\x10\x07\x12.\n*NISCOPE_STRING_TRIGGER_SOURCE_VAL_EXTERNAL\x10\x08\x122\n.NISCOPE_STRING_TRIGGER_SOURCE_VAL_SW_TRIG_FUNC\x10\t\x12*\n&NISCOPE_STRING_TRIGGER_SOURCE_VAL_TTL0\x10\n\x12*\n&NISCOPE_STRING_TRIGGER_SOURCE_VAL_TTL1\x10\x0b\x12*\n&NISCOPE_STRING_TRIGGER_SOURCE_VAL_TTL2\x10\x0c\x12*\n&NISCOPE_STRING_TRIGGER_SOURCE_VAL_TTL3\x10\r\x12*\n&NISCOPE_STRING_TRIGGER_SOURCE_VAL_TTL4\x10\x0e\x12*\n&NISCOPE_STRING_TRIGGER_SOURCE_VAL_TTL5\x10\x0f\x12*\n&NISCOPE_STRING_TRIGGER_SOURCE_VAL_TTL6\x10\x10\x12*\n&NISCOPE_STRING_TRIGGER_SOURCE_VAL_TTL7\x10\x11\x12*\n&NISCOPE_STRING_TRIGGER_SOURCE_VAL_ECL0\x10\x12\x12*\n&NISCOPE_STRING_TRIGGER_SOURCE_VAL_ECL1\x10\x13\x12.\n*NISCOPE_STRING_TRIGGER_SOURCE_VAL_PXI_STAR\x10\x14\x12,\n(NISCOPE_STRING_TRIGGER_SOURCE_VAL_RTSI_0\x10\x15\x12,\n(NISCOPE_STRING_TRIGGER_SOURCE_VAL_RTSI_1\x10\x16\x12,\n(NISCOPE_STRING_TRIGGER_SOURCE_VAL_RTSI_2\x10\x17\x12,\n(NISCOPE_STRING_TRIGGER_SOURCE_VAL_RTSI_3\x10\x18\x12,\n(NISCOPE_STRING_TRIGGER_SOURCE_VAL_RTSI_4\x10\x19\x12,\n(NISCOPE_STRING_TRIGGER_SOURCE_VAL_RTSI_5\x10\x1a\x12,\n(NISCOPE_STRING_TRIGGER_SOURCE_VAL_RTSI_6\x10\x1b\x12,\n(NISCOPE_STRING_TRIGGER_SOURCE_VAL_RTSI_7\x10\x1c\x12+\n\'NISCOPE_STRING_TRIGGER_SOURCE_VAL_PFI_0\x10\x1d\x12+\n\'NISCOPE_STRING_TRIGGER_SOURCE_VAL_PFI_1\x10\x1e\x12+\n\'NISCOPE_STRING_TRIGGER_SOURCE_VAL_PFI_2\x10\x1f\x12+\n\'NISCOPE_STRING_TRIGGER_SOURCE_VAL_PFI_3\x10 \x12+\n\'NISCOPE_STRING_TRIGGER_SOURCE_VAL_PFI_4\x10!\x12+\n\'NISCOPE_STRING_TRIGGER_SOURCE_VAL_PFI_5\x10"\x12+\n\'NISCOPE_STRING_TRIGGER_SOURCE_VAL_PFI_6\x10#\x12+\n\'NISCOPE_STRING_TRIGGER_SOURCE_VAL_PFI_7\x10$\x121\n-NISCOPE_STRING_TRIGGER_SOURCE_VAL_AUX_0_PFI_0\x10%\x121\n-NISCOPE_STRING_TRIGGER_SOURCE_VAL_AUX_0_PFI_1\x10&\x121\n-NISCOPE_STRING_TRIGGER_SOURCE_VAL_AUX_0_PFI_3\x10\'\x121\n-NISCOPE_STRING_TRIGGER_SOURCE_VAL_AUX_0_PFI_4\x10(\x121\n-NISCOPE_STRING_TRIGGER_SOURCE_VAL_AUX_0_PFI_5\x10)\x121\n-NISCOPE_STRING_TRIGGER_SOURCE_VAL_AUX_0_PFI_6\x10*\x121\n-NISCOPE_STRING_TRIGGER_SOURCE_VAL_AUX_0_PFI_7\x10+\x121\n-NISCOPE_STRING_TRIGGER_SOURCE_VAL_AUX_0_PFI_2\x10,2\xe0K\n\x07NiScope\x12=\n\x04Init\x12\x19.niscope_grpc.InitRequest\x1a\x1a.niscope_grpc.InitResponse\x12^\n\x0fInitWithOptions\x12$.niscope_grpc.InitWithOptionsRequest\x1a%.niscope_grpc.InitWithOptionsResponse\x12@\n\x05Close\x12\x1a.niscope_grpc.CloseRequest\x1a\x1b.niscope_grpc.CloseResponse\x12L\n\tAutoSetup\x12\x1e.niscope_grpc.AutoSetupRequest\x1a\x1f.niscope_grpc.AutoSetupResponse\x12d\n\x11ConfigureVertical\x12&.niscope_grpc.ConfigureVerticalRequest\x1a\'.niscope_grpc.ConfigureVerticalResponse\x12\x85\x01\n\x1cConfigureChanCharacteristics\x121.niscope_grpc.ConfigureChanCharacteristicsRequest\x1a2.niscope_grpc.ConfigureChanCharacteristicsResponse\x12|\n\x19ConfigureHorizontalTiming\x12..niscope_grpc.ConfigureHorizontalTimingRequest\x1a/.niscope_grpc.ConfigureHorizontalTimingResponse\x12[\n\x0eConfigureClock\x12#.niscope_grpc.ConfigureClockRequest\x1a$.niscope_grpc.ConfigureClockResponse\x12U\n\x0cExportSignal\x12!.niscope_grpc.ExportSignalRequest\x1a".niscope_grpc.ExportSignalResponse\x12\x8b\x01\n\x1eAdjustSampleClockRelativeDelay\x123.niscope_grpc.AdjustSampleClockRelativeDelayRequest\x1a4.niscope_grpc.AdjustSampleClockRelativeDelayResponse\x12m\n\x14ConfigureTriggerEdge\x12).niscope_grpc.ConfigureTriggerEdgeRequest\x1a*.niscope_grpc.ConfigureTriggerEdgeResponse\x12s\n\x16ConfigureTriggerGlitch\x12+.niscope_grpc.ConfigureTriggerGlitchRequest\x1a,.niscope_grpc.ConfigureTriggerGlitchResponse\x12\x7f\n\x1aConfigureTriggerHysteresis\x12/.niscope_grpc.ConfigureTriggerHysteresisRequest\x1a0.niscope_grpc.ConfigureTriggerHysteresisResponse\x12s\n\x16ConfigureTriggerWindow\x12+.niscope_grpc.ConfigureTriggerWindowRequest\x1a,.niscope_grpc.ConfigureTriggerWindowResponse\x12y\n\x18ConfigureTriggerSoftware\x12-.niscope_grpc.ConfigureTriggerSoftwareRequest\x1a..niscope_grpc.ConfigureTriggerSoftwareResponse\x12v\n\x17SendSoftwareTriggerEdge\x12,.niscope_grpc.SendSoftwareTriggerEdgeRequest\x1a-.niscope_grpc.SendSoftwareTriggerEdgeResponse\x12|\n\x19ConfigureTriggerImmediate\x12..niscope_grpc.ConfigureTriggerImmediateRequest\x1a/.niscope_grpc.ConfigureTriggerImmediateResponse\x12m\n\x14ConfigureTriggerRunt\x12).niscope_grpc.ConfigureTriggerRuntRequest\x1a*.niscope_grpc.ConfigureTriggerRuntResponse\x12v\n\x17ConfigureTriggerDigital\x12,.niscope_grpc.ConfigureTriggerDigitalRequest\x1a-.niscope_grpc.ConfigureTriggerDigitalResponse\x12p\n\x15ConfigureTriggerVideo\x12*.niscope_grpc.ConfigureTriggerVideoRequest\x1a+.niscope_grpc.ConfigureTriggerVideoResponse\x12p\n\x15ConfigureTriggerWidth\x12*.niscope_grpc.ConfigureTriggerWidthRequest\x1a+.niscope_grpc.ConfigureTriggerWidthResponse\x12\xa6\x01\n\'ConfigureEqualizationFilterCoefficients\x12<.niscope_grpc.ConfigureEqualizationFilterCoefficientsRequest\x1a=.niscope_grpc.ConfigureEqualizationFilterCoefficientsResponse\x12\x94\x01\n!GetEqualizationFilterCoefficients\x126.niscope_grpc.GetEqualizationFilterCoefficientsRequest\x1a7.niscope_grpc.GetEqualizationFilterCoefficientsResponse\x12m\n\x14GetFrequencyResponse\x12).niscope_grpc.GetFrequencyResponseRequest\x1a*.niscope_grpc.GetFrequencyResponseResponse\x12m\n\x14ConfigureAcquisition\x12).niscope_grpc.ConfigureAcquisitionRequest\x1a*.niscope_grpc.ConfigureAcquisitionResponse\x12j\n\x13InitiateAcquisition\x12(.niscope_grpc.InitiateAcquisitionRequest\x1a).niscope_grpc.InitiateAcquisitionResponse\x12@\n\x05Abort\x12\x1a.niscope_grpc.AbortRequest\x1a\x1b.niscope_grpc.AbortResponse\x12C\n\x06Commit\x12\x1b.niscope_grpc.CommitRequest\x1a\x1c.niscope_grpc.CommitResponse\x12=\n\x04Read\x12\x19.niscope_grpc.ReadRequest\x1a\x1a.niscope_grpc.ReadResponse\x12@\n\x05Fetch\x12\x1a.niscope_grpc.FetchRequest\x1a\x1b.niscope_grpc.FetchResponse\x12U\n\x0cFetchBinary8\x12!.niscope_grpc.FetchBinary8Request\x1a".niscope_grpc.FetchBinary8Response\x12X\n\rFetchBinary16\x12".niscope_grpc.FetchBinary16Request\x1a#.niscope_grpc.FetchBinary16Response\x12X\n\rFetchBinary32\x12".niscope_grpc.FetchBinary32Request\x1a#.niscope_grpc.FetchBinary32Response\x12U\n\x0cFetchComplex\x12!.niscope_grpc.FetchComplexRequest\x1a".niscope_grpc.FetchComplexResponse\x12m\n\x14FetchComplexBinary16\x12).niscope_grpc.FetchComplexBinary16Request\x1a*.niscope_grpc.FetchComplexBinary16Response\x12d\n\x11AcquisitionStatus\x12&.niscope_grpc.AcquisitionStatusRequest\x1a\'.niscope_grpc.AcquisitionStatusResponse\x12X\n\rActualNumWfms\x12".niscope_grpc.ActualNumWfmsRequest\x1a#.niscope_grpc.ActualNumWfmsResponse\x12d\n\x11ActualMeasWfmSize\x12&.niscope_grpc.ActualMeasWfmSizeRequest\x1a\'.niscope_grpc.ActualMeasWfmSizeResponse\x12g\n\x12ActualRecordLength\x12\'.niscope_grpc.ActualRecordLengthRequest\x1a(.niscope_grpc.ActualRecordLengthResponse\x12O\n\nSampleRate\x12\x1f.niscope_grpc.SampleRateRequest\x1a .niscope_grpc.SampleRateResponse\x12O\n\nSampleMode\x12\x1f.niscope_grpc.SampleModeRequest\x1a .niscope_grpc.SampleModeResponse\x12p\n\x15AddWaveformProcessing\x12*.niscope_grpc.AddWaveformProcessingRequest\x1a+.niscope_grpc.AddWaveformProcessingResponse\x12v\n\x17ClearWaveformProcessing\x12,.niscope_grpc.ClearWaveformProcessingRequest\x1a-.niscope_grpc.ClearWaveformProcessingResponse\x12\x88\x01\n\x1dClearWaveformMeasurementStats\x122.niscope_grpc.ClearWaveformMeasurementStatsRequest\x1a3.niscope_grpc.ClearWaveformMeasurementStatsResponse\x12^\n\x0fReadMeasurement\x12$.niscope_grpc.ReadMeasurementRequest\x1a%.niscope_grpc.ReadMeasurementResponse\x12a\n\x10FetchMeasurement\x12%.niscope_grpc.FetchMeasurementRequest\x1a&.niscope_grpc.FetchMeasurementResponse\x12p\n\x15FetchMeasurementStats\x12*.niscope_grpc.FetchMeasurementStatsRequest\x1a+.niscope_grpc.FetchMeasurementStatsResponse\x12p\n\x15FetchArrayMeasurement\x12*.niscope_grpc.FetchArrayMeasurementRequest\x1a+.niscope_grpc.FetchArrayMeasurementResponse\x12@\n\x05Reset\x12\x1a.niscope_grpc.ResetRequest\x1a\x1b.niscope_grpc.ResetResponse\x12I\n\x08SelfTest\x12\x1d.niscope_grpc.SelfTestRequest\x1a\x1e.niscope_grpc.SelfTestResponse\x12F\n\x07Disable\x12\x1c.niscope_grpc.DisableRequest\x1a\x1d.niscope_grpc.DisableResponse\x12R\n\x0bResetDevice\x12 .niscope_grpc.ResetDeviceRequest\x1a!.niscope_grpc.ResetDeviceResponse\x12a\n\x10CalSelfCalibrate\x12%.niscope_grpc.CalSelfCalibrateRequest\x1a&.niscope_grpc.CalSelfCalibrateResponse\x12X\n\rRevisionQuery\x12".niscope_grpc.RevisionQueryRequest\x1a#.niscope_grpc.RevisionQueryResponse\x12\x85\x01\n\x1cProbeCompensationSignalStart\x121.niscope_grpc.ProbeCompensationSignalStartRequest\x1a2.niscope_grpc.ProbeCompensationSignalStartResponse\x12\x82\x01\n\x1bProbeCompensationSignalStop\x120.niscope_grpc.ProbeCompensationSignalStopRequest\x1a1.niscope_grpc.ProbeCompensationSignalStopResponse\x12p\n\x15CableSenseSignalStart\x12*.niscope_grpc.CableSenseSignalStartRequest\x1a+.niscope_grpc.CableSenseSignalStartResponse\x12m\n\x14CableSenseSignalStop\x12).niscope_grpc.CableSenseSignalStopRequest\x1a*.niscope_grpc.CableSenseSignalStopResponse\x12[\n\x0eGetChannelName\x12#.niscope_grpc.GetChannelNameRequest\x1a$.niscope_grpc.GetChannelNameResponse\x12y\n\x18GetChannelNameFromString\x12-.niscope_grpc.GetChannelNameFromStringRequest\x1a..niscope_grpc.GetChannelNameFromStringResponse\x12U\n\x0cErrorHandler\x12!.niscope_grpc.ErrorHandlerRequest\x1a".niscope_grpc.ErrorHandlerResponse\x12I\n\x08GetError\x12\x1d.niscope_grpc.GetErrorRequest\x1a\x1e.niscope_grpc.GetErrorResponse\x12^\n\x0fGetErrorMessage\x12$.niscope_grpc.GetErrorMessageRequest\x1a%.niscope_grpc.GetErrorMessageResponse\x12j\n\x13GetAttributeViInt32\x12(.niscope_grpc.GetAttributeViInt32Request\x1a).niscope_grpc.GetAttributeViInt32Response\x12j\n\x13SetAttributeViInt32\x12(.niscope_grpc.SetAttributeViInt32Request\x1a).niscope_grpc.SetAttributeViInt32Response\x12p\n\x15CheckAttributeViInt32\x12*.niscope_grpc.CheckAttributeViInt32Request\x1a+.niscope_grpc.CheckAttributeViInt32Response\x12j\n\x13GetAttributeViInt64\x12(.niscope_grpc.GetAttributeViInt64Request\x1a).niscope_grpc.GetAttributeViInt64Response\x12j\n\x13SetAttributeViInt64\x12(.niscope_grpc.SetAttributeViInt64Request\x1a).niscope_grpc.SetAttributeViInt64Response\x12p\n\x15CheckAttributeViInt64\x12*.niscope_grpc.CheckAttributeViInt64Request\x1a+.niscope_grpc.CheckAttributeViInt64Response\x12m\n\x14GetAttributeViReal64\x12).niscope_grpc.GetAttributeViReal64Request\x1a*.niscope_grpc.GetAttributeViReal64Response\x12m\n\x14SetAttributeViReal64\x12).niscope_grpc.SetAttributeViReal64Request\x1a*.niscope_grpc.SetAttributeViReal64Response\x12s\n\x16CheckAttributeViReal64\x12+.niscope_grpc.CheckAttributeViReal64Request\x1a,.niscope_grpc.CheckAttributeViReal64Response\x12m\n\x14GetAttributeViString\x12).niscope_grpc.GetAttributeViStringRequest\x1a*.niscope_grpc.GetAttributeViStringResponse\x12m\n\x14SetAttributeViString\x12).niscope_grpc.SetAttributeViStringRequest\x1a*.niscope_grpc.SetAttributeViStringResponse\x12s\n\x16CheckAttributeViString\x12+.niscope_grpc.CheckAttributeViStringRequest\x1a,.niscope_grpc.CheckAttributeViStringResponse\x12p\n\x15GetAttributeViSession\x12*.niscope_grpc.GetAttributeViSessionRequest\x1a+.niscope_grpc.GetAttributeViSessionResponse\x12p\n\x15SetAttributeViSession\x12*.niscope_grpc.SetAttributeViSessionRequest\x1a+.niscope_grpc.SetAttributeViSessionResponse\x12v\n\x17CheckAttributeViSession\x12,.niscope_grpc.CheckAttributeViSessionRequest\x1a-.niscope_grpc.CheckAttributeViSessionResponse\x12p\n\x15GetAttributeViBoolean\x12*.niscope_grpc.GetAttributeViBooleanRequest\x1a+.niscope_grpc.GetAttributeViBooleanResponse\x12p\n\x15SetAttributeViBoolean\x12*.niscope_grpc.SetAttributeViBooleanRequest\x1a+.niscope_grpc.SetAttributeViBooleanResponse\x12v\n\x17CheckAttributeViBoolean\x12,.niscope_grpc.CheckAttributeViBooleanRequest\x1a-.niscope_grpc.CheckAttributeViBooleanResponse\x12\x97\x01\n"ImportAttributeConfigurationBuffer\x127.niscope_grpc.ImportAttributeConfigurationBufferRequest\x1a8.niscope_grpc.ImportAttributeConfigurationBufferResponse\x12\x97\x01\n"ExportAttributeConfigurationBuffer\x127.niscope_grpc.ExportAttributeConfigurationBufferRequest\x1a8.niscope_grpc.ExportAttributeConfigurationBufferResponse\x12\x91\x01\n ImportAttributeConfigurationFile\x125.niscope_grpc.ImportAttributeConfigurationFileRequest\x1a6.niscope_grpc.ImportAttributeConfigurationFileResponse\x12\x91\x01\n ExportAttributeConfigurationFile\x125.niscope_grpc.ExportAttributeConfigurationFileRequest\x1a6.niscope_grpc.ExportAttributeConfigurationFileResponse\x12s\n\x16GetScalingCoefficients\x12+.niscope_grpc.GetScalingCoefficientsRequest\x1a,.niscope_grpc.GetScalingCoefficientsResponse\x12\x85\x01\n\x1cGetNormalizationCoefficients\x121.niscope_grpc.GetNormalizationCoefficientsRequest\x1a2.niscope_grpc.GetNormalizationCoefficientsResponse\x12v\n\x17GetStreamEndpointHandle\x12,.niscope_grpc.GetStreamEndpointHandleRequest\x1a-.niscope_grpc.GetStreamEndpointHandleResponse\x12U\n\x0cCalFetchDate\x12!.niscope_grpc.CalFetchDateRequest\x1a".niscope_grpc.CalFetchDateResponse\x12j\n\x13CalFetchTemperature\x12(.niscope_grpc.CalFetchTemperatureRequest\x1a).niscope_grpc.CalFetchTemperatureResponseB?\n\x11com.ni.grpc.scopeB\x07NiScopeP\x01\xaa\x02\x1eNationalInstruments.Grpc.Scopeb\x06proto3')`

<!--NI_PYTHON_API repo=nimi-python path=generated/niscope/niscope/niscope_pb2_grpc.py -->
## PYTHON MODULE: generated/niscope/niscope/niscope_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

### `class NiScopeStub(object)`

Missing associated documentation comment in .proto file.

#### `def __init__(self, channel)`

Constructor.

        Args:
            channel: A grpc.Channel.
        

### `class NiScopeServicer(object)`

Missing associated documentation comment in .proto file.

#### `def Init(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def InitWithOptions(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Close(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def AutoSetup(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureVertical(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureChanCharacteristics(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureHorizontalTiming(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureClock(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ExportSignal(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def AdjustSampleClockRelativeDelay(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureTriggerEdge(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureTriggerGlitch(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureTriggerHysteresis(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureTriggerWindow(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureTriggerSoftware(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SendSoftwareTriggerEdge(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureTriggerImmediate(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureTriggerRunt(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureTriggerDigital(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureTriggerVideo(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureTriggerWidth(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureEqualizationFilterCoefficients(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetEqualizationFilterCoefficients(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetFrequencyResponse(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureAcquisition(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def InitiateAcquisition(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Abort(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Commit(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Read(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Fetch(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def FetchBinary8(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def FetchBinary16(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def FetchBinary32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def FetchComplex(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def FetchComplexBinary16(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def AcquisitionStatus(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ActualNumWfms(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ActualMeasWfmSize(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ActualRecordLength(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SampleRate(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SampleMode(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def AddWaveformProcessing(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ClearWaveformProcessing(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ClearWaveformMeasurementStats(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadMeasurement(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def FetchMeasurement(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def FetchMeasurementStats(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def FetchArrayMeasurement(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Reset(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SelfTest(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Disable(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ResetDevice(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CalSelfCalibrate(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def RevisionQuery(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ProbeCompensationSignalStart(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ProbeCompensationSignalStop(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CableSenseSignalStart(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CableSenseSignalStop(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetChannelName(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetChannelNameFromString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ErrorHandler(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetError(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetErrorMessage(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CheckAttributeViInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViInt64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViInt64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CheckAttributeViInt64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViReal64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViReal64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CheckAttributeViReal64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CheckAttributeViString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViSession(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViSession(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CheckAttributeViSession(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViBoolean(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViBoolean(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CheckAttributeViBoolean(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ImportAttributeConfigurationBuffer(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ExportAttributeConfigurationBuffer(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ImportAttributeConfigurationFile(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ExportAttributeConfigurationFile(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetScalingCoefficients(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetNormalizationCoefficients(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetStreamEndpointHandle(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CalFetchDate(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CalFetchTemperature(self, request, context)`

Missing associated documentation comment in .proto file.

### `def add_NiScopeServicer_to_server(servicer, server)`

### `class NiScope(object)`

Missing associated documentation comment in .proto file.

#### `def Init(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def InitWithOptions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Close(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def AutoSetup(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureVertical(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureChanCharacteristics(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureHorizontalTiming(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureClock(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ExportSignal(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def AdjustSampleClockRelativeDelay(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureTriggerEdge(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureTriggerGlitch(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureTriggerHysteresis(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureTriggerWindow(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureTriggerSoftware(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SendSoftwareTriggerEdge(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureTriggerImmediate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureTriggerRunt(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureTriggerDigital(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureTriggerVideo(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureTriggerWidth(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureEqualizationFilterCoefficients(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetEqualizationFilterCoefficients(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetFrequencyResponse(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureAcquisition(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def InitiateAcquisition(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Abort(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Commit(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Read(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Fetch(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def FetchBinary8(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def FetchBinary16(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def FetchBinary32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def FetchComplex(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def FetchComplexBinary16(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def AcquisitionStatus(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ActualNumWfms(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ActualMeasWfmSize(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ActualRecordLength(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SampleRate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SampleMode(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def AddWaveformProcessing(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ClearWaveformProcessing(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ClearWaveformMeasurementStats(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadMeasurement(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def FetchMeasurement(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def FetchMeasurementStats(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def FetchArrayMeasurement(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Reset(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SelfTest(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Disable(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ResetDevice(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CalSelfCalibrate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def RevisionQuery(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ProbeCompensationSignalStart(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ProbeCompensationSignalStop(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CableSenseSignalStart(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CableSenseSignalStop(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetChannelName(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetChannelNameFromString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ErrorHandler(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetError(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetErrorMessage(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CheckAttributeViInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViInt64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViInt64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CheckAttributeViInt64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViReal64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViReal64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CheckAttributeViReal64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CheckAttributeViString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViSession(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViSession(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CheckAttributeViSession(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViBoolean(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViBoolean(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CheckAttributeViBoolean(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ImportAttributeConfigurationBuffer(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ExportAttributeConfigurationBuffer(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ImportAttributeConfigurationFile(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ExportAttributeConfigurationFile(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetScalingCoefficients(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetNormalizationCoefficients(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetStreamEndpointHandle(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CalFetchDate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CalFetchTemperature(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

<!--NI_PYTHON_API repo=nimi-python path=generated/niscope/niscope/session.py -->
## PYTHON MODULE: generated/niscope/niscope/session.py

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

Base class for all NI-SCOPE sessions.

#### `def __init__(self, repeated_capability_list, all_channels_in_session, interpreter, freeze_it=False)`

#### `def __repr__(self)`

#### `def __setattr__(self, key, value)`

#### `def _actual_meas_wfm_size(self, array_meas_function)`

_actual_meas_wfm_size

        Returns the total available size of an array measurement acquisition.

        Args:
            array_meas_function (enums.ArrayMeasurement): The `array
                measurement <REPLACE_DRIVER_SPECIFIC_URL_2(array_measurements_refs)>`__
                to perform.


        Returns:
            meas_waveform_size (int): Returns the size (in number of samples) of the resulting analysis
                waveform.

        

#### `def _actual_num_wfms(self)`

_actual_num_wfms

        Helps you to declare appropriately sized waveforms. NI-SCOPE handles the
        channel list parsing for you.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._actual_num_wfms`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._actual_num_wfms`

        Returns:
            num_wfms (int): Returns the number of records times the number of channels; if you are
                operating in DDC mode (NI 5620/5621 only), this value is multiplied by
                two.

        

#### `def add_waveform_processing(self, meas_function)`

add_waveform_processing

        Adds one measurement to the list of processing steps that are completed
        before the measurement. The processing is added on a per channel basis,
        and the processing measurements are completed in the same order they are
        registered. All measurement library parameters—the properties starting
        with "meas_"—are cached at the time of registering the
        processing, and this set of parameters is used during the processing
        step. The processing measurements are streamed, so the result of the
        first processing step is used as the input for the next step. The
        processing is done before any other measurements.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].add_waveform_processing`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session.add_waveform_processing`

        Args:
            meas_function (enums.ArrayMeasurement): The `array
                measurement <REPLACE_DRIVER_SPECIFIC_URL_2(array_measurements_refs)>`__
                to add.

        

#### `def self_cal(self, option=enums.Option.SELF_CALIBRATE_ALL_CHANNELS)`

self_cal

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
        CalEnd is called with **action** set to
        NISCOPE_VAL_ACTION_STORE and no errors occur.

        Note:
        One or more of the referenced methods are not in the Python API for this driver.

        Note:
        One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].self_cal`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session.self_cal`

        Args:
            option (enums.Option): The calibration option. Use VI_NULL for a normal self-calibration
                operation or NISCOPE_VAL_CAL_RESTORE_EXTERNAL_CALIBRATION to
                restore the previous calibration.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        

#### `def clear_waveform_measurement_stats(self, clearable_measurement_function=enums.ClearableMeasurement.ALL_MEASUREMENTS)`

clear_waveform_measurement_stats

        Clears the waveform stats on the channel and measurement you specify. If
        you want to clear all of the measurements, use
        ClearableMeasurement.ALL_MEASUREMENTS in the **clearableMeasurementFunction**
        parameter.

        Every time a measurement is called, the statistics information is
        updated, including the min, max, mean, standard deviation, and number of
        updates. This information is fetched with
        _fetch_measurement_stats. The multi-acquisition array measurements
        are also cleared with this method.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].clear_waveform_measurement_stats`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session.clear_waveform_measurement_stats`

        Args:
            clearable_measurement_function (enums.ClearableMeasurement): The `scalar
                measurement <REPLACE_DRIVER_SPECIFIC_URL_2(scalar_measurements_refs)>`__
                or `array
                measurement <REPLACE_DRIVER_SPECIFIC_URL_2(array_measurements_refs)>`__
                to clear the stats for.

        

#### `def clear_waveform_processing(self)`

clear_waveform_processing

        Clears the list of processing steps assigned to the given channel. The
        processing is added using the add_waveform_processing method,
        where the processing steps are completed in the same order in which they
        are registered. The processing measurements are streamed, so the result
        of the first processing step is used as the input for the next step. The
        processing is also done before any other measurements.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].clear_waveform_processing`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session.clear_waveform_processing`
        

#### `def configure_chan_characteristics(self, input_impedance, max_input_frequency)`

configure_chan_characteristics

        Configures the properties that control the electrical characteristics of
        the channel—the input impedance and the bandwidth.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_chan_characteristics`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session.configure_chan_characteristics`

        Args:
            input_impedance (float): The input impedance for the channel; NI-SCOPE sets
                input_impedance to this value.

            max_input_frequency (float): The bandwidth for the channel; NI-SCOPE sets
                max_input_frequency to this value. Pass 0 for this
                value to use the hardware default bandwidth. Pass –1 for this value to
                achieve full bandwidth.

        

#### `def configure_equalization_filter_coefficients(self, coefficients)`

configure_equalization_filter_coefficients

        Configures the custom coefficients for the equalization FIR filter on
        the device. This filter is designed to compensate the input signal for
        artifacts introduced to the signal outside of the digitizer. Because
        this filter is a generic FIR filter, any coefficients are valid.
        Coefficient values should be between +1 and –1.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_equalization_filter_coefficients`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session.configure_equalization_filter_coefficients`

        Args:
            coefficients (list of float): The custom coefficients for the equalization FIR filter on the device.
                These coefficients should be between +1 and –1. You can obtain the
                number of coefficients from the
                `equalization_num_coefficients <cviequalization_num_coefficients.html>`__
                property. The
                `equalization_filter_enabled <cviequalization_filter_enabled.html>`__
                property must be set to TRUE to enable the filter.

        

#### `def configure_vertical(self, range, coupling, offset=0.0, probe_attenuation=1.0, enabled=True)`

configure_vertical

        Configures the most commonly configured properties of the digitizer
        vertical subsystem, such as the range, offset, coupling, probe
        attenuation, and the channel.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_vertical`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session.configure_vertical`

        Args:
            range (float): Specifies the vertical range Refer to vertical_range for
                more information.

            coupling (enums.VerticalCoupling): Specifies how to couple the input signal. Refer to
                vertical_coupling for more information.

            offset (float): Specifies the vertical offset. Refer to vertical_offset
                for more information.

            probe_attenuation (float): Specifies the probe attenuation. Refer to
                probe_attenuation for valid values.

            enabled (bool): Specifies whether the channel is enabled for acquisition. Refer to
                channel_enabled for more information.

        

#### `def fetch(self, num_samples=None, relative_to=enums.FetchRelativeTo.PRETRIGGER, offset=0, record_number=0, num_records=None, timeout=hightime.timedelta(seconds=5.0))`

fetch

        Returns the waveform from a previously initiated acquisition that the
        digitizer acquires for the specified channel. This method returns
        scaled voltage waveforms.

        This method may return multiple waveforms depending on the number of
        channels, the acquisition type, and the number of records you specify.

        Note: Some functionality, such as time stamping, is not supported in all digitizers.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].fetch`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session.fetch`

        Args:
            num_samples (int): The maximum number of samples to fetch for each waveform. If the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. If it fails to complete within the timeout period, the method raises.

            relative_to (enums.FetchRelativeTo): Position to start fetching within one record.

            offset (int): Offset in samples to start fetching data within each record. The offset can be positive or negative.

            record_number (int): Zero-based index of the first record to fetch.

            num_records (int): Number of records to fetch. Use -1 to fetch all configured records.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): The time to wait for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 seconds for this parameter implies infinite timeout.


        Returns:
            wfm_info (list of WaveformInfo): Returns a list of class instances with the following timing and scaling information about each waveform:

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

        

#### `def fetch_array_measurement(self, array_meas_function, meas_wfm_size=None, relative_to=enums.FetchRelativeTo.PRETRIGGER, offset=0, record_number=0, num_records=None, meas_num_samples=None, timeout=hightime.timedelta(seconds=5.0))`

fetch_array_measurement

        Obtains a waveform from the digitizer and returns the specified
        measurement array. This method may return multiple waveforms depending
        on the number of channels, the acquisition type, and the number of
        records you specify.

        Note:
        Some functionality, such as time stamping, is not supported in all
        digitizers.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].fetch_array_measurement`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session.fetch_array_measurement`

        Args:
            array_meas_function (enums.ArrayMeasurement): The array measurement to perform.

            meas_wfm_size (int): The maximum number of samples returned in the measurement waveform array
                for each waveform measurement. Default Value: None (returns all available samples).

            relative_to (enums.FetchRelativeTo): Position to start fetching within one record.

            offset (int): Offset in samples to start fetching data within each record. The offset can be positive or negative.

            record_number (int): Zero-based index of the first record to fetch.

            num_records (int): Number of records to fetch. Use `None` to fetch all configured records.

            meas_num_samples (int): Number of samples to fetch when performing a measurement. Use `None` to fetch the actual record length.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): The time to wait in seconds for data to be acquired; using 0 for this
                parameter tells NI-SCOPE to fetch whatever is currently available. Using
                -1 for this parameter implies infinite timeout.


        Returns:
            wfm_info (list of WaveformInfo): Returns a list of class instances with the following timing and scaling
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

        

#### `def fetch_measurement_stats(self, scalar_meas_function, relative_to=enums.FetchRelativeTo.PRETRIGGER, offset=0, record_number=0, num_records=None, timeout=hightime.timedelta(seconds=5.0))`

fetch_measurement_stats

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
        clear_waveform_measurement_stats.

        Many of the measurements use the low, mid, and high reference levels.
        You configure the low, mid, and high references with
        meas_chan_low_ref_level,
        meas_chan_mid_ref_level, and
        meas_chan_high_ref_level to set each channel
        differently.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].fetch_measurement_stats`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session.fetch_measurement_stats`

        Args:
            scalar_meas_function (enums.ScalarMeasurement): The scalar measurement to be performed on each fetched waveform.

            relative_to (enums.FetchRelativeTo): Position to start fetching within one record.

            offset (int): Offset in samples to start fetching data within each record. The offset can be positive or negative.

            record_number (int): Zero-based index of the first record to fetch.

            num_records (int): Number of records to fetch. Use `None` to fetch all configured records.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): The time to wait in seconds for data to be acquired; using 0 for this
                parameter tells NI-SCOPE to fetch whatever is currently available. Using
                -1 for this parameter implies infinite timeout.


        Returns:
            measurement_stats (list of MeasurementStats): Returns a list of class instances with the following measurement statistics
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

        

#### `def get_equalization_filter_coefficients(self)`

get_equalization_filter_coefficients

        Retrieves the custom coefficients for the equalization FIR filter on the device. This filter is designed to compensate the input signal for artifacts introduced to the signal outside of the digitizer. Because this filter is a generic FIR filter, any coefficients are valid. Coefficient values should be between +1 and –1.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].get_equalization_filter_coefficients`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session.get_equalization_filter_coefficients`
        

#### `def read(self, num_samples=None, relative_to=enums.FetchRelativeTo.PRETRIGGER, offset=0, record_number=0, num_records=None, timeout=hightime.timedelta(seconds=5.0))`

read

        Initiates an acquisition, waits for it to complete, and retrieves the
        data. The process is similar to calling _initiate_acquisition,
        acquisition_status, and fetch. The only difference is
        that with read, you enable all channels specified with
        **channelList** before the acquisition; in the other method, you enable
        the channels with configure_vertical.

        This method may return multiple waveforms depending on the number of
        channels, the acquisition type, and the number of records you specify.

        Note: Some functionality, such as time stamping, is not supported in all digitizers.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].read`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session.read`

        Args:
            num_samples (int): The maximum number of samples to fetch for each waveform. If the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. If it fails to complete within the timeout period, the method raises.

            relative_to (enums.FetchRelativeTo): Position to start fetching within one record.

            offset (int): Offset in samples to start fetching data within each record. The offset can be positive or negative.

            record_number (int): Zero-based index of the first record to fetch.

            num_records (int): Number of records to fetch. Use -1 to fetch all configured records.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): The time to wait for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 seconds for this parameter implies infinite timeout.


        Returns:
            wfm_info (list of WaveformInfo): Returns a list of class instances with the following timing and scaling information about each waveform:

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

        

#### `def _fetch(self, num_samples, timeout=hightime.timedelta(seconds=5.0))`

_fetch

        Returns the waveform from a previously initiated acquisition that the
        digitizer acquires for the specified channel. This method returns
        scaled voltage waveforms.

        This method may return multiple waveforms depending on the number of
        channels, the acquisition type, and the number of records you specify.

        Note:
        You can use read instead of this method. read
        starts an acquisition on all enabled channels, waits for the acquisition
        to complete, and returns the waveform for the specified channel.

        Some functionality, such as time stamping, is not supported in all
        digitizers. Refer to `Features Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._fetch`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._fetch`

        Args:
            num_samples (int): The maximum number of samples to fetch for each waveform. If the
                acquisition finishes with fewer points than requested, some devices
                return partial data if the acquisition finished, was aborted, or a
                timeout of 0 was used. If it fails to complete within the timeout
                period, the method returns an error.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): The time to wait in seconds for data to be acquired; using 0 for this
                parameter tells NI-SCOPE to fetch whatever is currently available. Using
                -1 for this parameter implies infinite timeout.


        Returns:
            waveform (array.array("d")): Returns an array whose length is the **numSamples** times number of
                waveforms. Call ActualNumwfms to determine the number of
                waveforms.

                NI-SCOPE returns this data sequentially, so all record 0 waveforms are
                first. For example, with a channel list of 0,1, you would have the
                following index values:

                index 0 = record 0, channel 0

                index *x* = record 0, channel 1

                index 2\ *x* = record 1, channel 0

                index 3\ *x* = record 1, channel 1

                Where *x* = the record length

                Note:
                One or more of the referenced methods are not in the Python API for this driver.

            wfm_info (list of WaveformInfo): Returns a list of class instances with the following timing and scaling
                information about each waveform:

                -  **relativeInitialX**—the time (in seconds) from the trigger to the
                   first sample in the fetched waveform
                -  **absoluteInitialX**—timestamp (in seconds) of the first fetched
                   sample. This timestamp is comparable between records and
                   acquisitions; devices that do not support this parameter use 0 for
                   this output.
                -  **xIncrement**—the time between points in the acquired waveform in
                   seconds
                -  **actualSamples**—the actual number of samples fetched and placed in
                   the waveform array
                -  **gain**—the gain factor of the given channel; useful for scaling
                   binary data with the following formula:

                voltage = binary data × gain factor + offset

                -  **offset**—the offset factor of the given channel; useful for scaling
                   binary data with the following formula:

                voltage = binary data × gain factor + offset

                Call _actual_num_wfms to determine the size of this array.

        

#### `def _fetch_into_numpy(self, num_samples, waveform, timeout=hightime.timedelta(seconds=5.0))`

_fetch_into_numpy

        Returns the waveform from a previously initiated acquisition that the
        digitizer acquires for the specified channel. This method returns
        scaled voltage waveforms.

        This method may return multiple waveforms depending on the number of
        channels, the acquisition type, and the number of records you specify.

        Note:
        You can use read instead of this method. read
        starts an acquisition on all enabled channels, waits for the acquisition
        to complete, and returns the waveform for the specified channel.

        Some functionality, such as time stamping, is not supported in all
        digitizers. Refer to `Features Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._fetch`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._fetch`

        Args:
            num_samples (int): The maximum number of samples to fetch for each waveform. If the
                acquisition finishes with fewer points than requested, some devices
                return partial data if the acquisition finished, was aborted, or a
                timeout of 0 was used. If it fails to complete within the timeout
                period, the method returns an error.

            waveform (numpy.array(dtype=numpy.float64)): Returns an array whose length is the **numSamples** times number of
                waveforms. Call ActualNumwfms to determine the number of
                waveforms.

                NI-SCOPE returns this data sequentially, so all record 0 waveforms are
                first. For example, with a channel list of 0,1, you would have the
                following index values:

                index 0 = record 0, channel 0

                index *x* = record 0, channel 1

                index 2\ *x* = record 1, channel 0

                index 3\ *x* = record 1, channel 1

                Where *x* = the record length

                Note:
                One or more of the referenced methods are not in the Python API for this driver.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): The time to wait in seconds for data to be acquired; using 0 for this
                parameter tells NI-SCOPE to fetch whatever is currently available. Using
                -1 for this parameter implies infinite timeout.


        Returns:
            wfm_info (numpy.array(dtype=numpy.WaveformInfo)): Returns a list of class instances with the following timing and scaling
                information about each waveform:

                -  **relativeInitialX**—the time (in seconds) from the trigger to the
                   first sample in the fetched waveform
                -  **absoluteInitialX**—timestamp (in seconds) of the first fetched
                   sample. This timestamp is comparable between records and
                   acquisitions; devices that do not support this parameter use 0 for
                   this output.
                -  **xIncrement**—the time between points in the acquired waveform in
                   seconds
                -  **actualSamples**—the actual number of samples fetched and placed in
                   the waveform array
                -  **gain**—the gain factor of the given channel; useful for scaling
                   binary data with the following formula:

                voltage = binary data × gain factor + offset

                -  **offset**—the offset factor of the given channel; useful for scaling
                   binary data with the following formula:

                voltage = binary data × gain factor + offset

                Call _actual_num_wfms to determine the size of this array.

        

#### `def _fetch_array_measurement(self, array_meas_function, measurement_waveform_size, timeout=hightime.timedelta(seconds=5.0))`

_fetch_array_measurement

        Obtains a waveform from the digitizer and returns the specified
        measurement array. This method may return multiple waveforms depending
        on the number of channels, the acquisition type, and the number of
        records you specify.

        Note:
        Some functionality, such as time stamping, is not supported in all
        digitizers. Refer to `Features Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._fetch_array_measurement`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._fetch_array_measurement`

        Args:
            array_meas_function (enums.ArrayMeasurement): The `array
                measurement <REPLACE_DRIVER_SPECIFIC_URL_2(array_measurements_refs)>`__
                to perform.

            measurement_waveform_size (int): The maximum number of samples returned in the measurement waveform array
                for each waveform measurement. Default Value: None (returns all available samples).

                Note:
                Use the property fetch_meas_num_samples to set the
                number of samples to fetch when performing a measurement. For more
                information about when to use this property, refer to the `NI
                KnowledgeBase <javascript:WWW(WWW_KB_MEAS)>`__.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): The time to wait in seconds for data to be acquired; using 0 for this
                parameter tells NI-SCOPE to fetch whatever is currently available. Using
                -1 for this parameter implies infinite timeout.


        Returns:
            meas_wfm (list of float): Returns an array whose length is the number of waveforms times
                **measurementWaveformSize**; call _actual_num_wfms to determine the number of
                waveforms; call _actual_meas_wfm_size to determine the size of each
                waveform.

                NI-SCOPE returns this data sequentially, so all record 0 waveforms are
                first. For example, with channel list of 0, 1, you would have the
                following index values:

                index 0 = record 0, channel 0

                index *x* = record 0, channel 1

                index 2\ *x* = record 1, channel 0

                index 3\ *x* = record 1, channel 1

                Where *x* = the record length

            wfm_info (list of WaveformInfo): Returns a list of class instances with the following timing and scaling
                information about each waveform:

                -  **relativeInitialX**—the time (in seconds) from the trigger to the
                   first sample in the fetched waveform
                -  **absoluteInitialX**—timestamp (in seconds) of the first fetched
                   sample. This timestamp is comparable between records and
                   acquisitions; devices that do not support this parameter use 0 for
                   this output.
                -  **xIncrement**—the time between points in the acquired waveform in
                   seconds
                -  **actualSamples**—the actual number of samples fetched and placed in
                   the waveform array
                -  **gain**—the gain factor of the given channel; useful for scaling
                   binary data with the following formula:

                voltage = binary data × gain factor + offset

                -  **offset**—the offset factor of the given channel; useful for scaling
                   binary data with the following formula:

                voltage = binary data × gain factor + offset

                Call _actual_num_wfms to determine the size of this array.

        

#### `def _fetch_binary16_into_numpy(self, num_samples, waveform, timeout=hightime.timedelta(seconds=5.0))`

_fetch_binary16_into_numpy

        Retrieves data from a previously initiated acquisition and returns
        binary 16-bit waveforms. This method may return multiple waveforms
        depending on the number of channels, the acquisition type, and the
        number of records you specify.

        Refer to `Using Fetch
        Methods <REPLACE_DRIVER_SPECIFIC_URL_1(using_fetch_functions)>`__ for
        more information on using this method.

        Note:
        Some functionality, such as time stamping, is not supported in all
        digitizers. Refer to `Features Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._fetch_binary16`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._fetch_binary16`

        Args:
            num_samples (int): The maximum number of samples to fetch for each waveform. If the
                acquisition finishes with fewer points than requested, some devices
                return partial data if the acquisition finished, was aborted, or a
                timeout of 0 was used. If it fails to complete within the timeout
                period, the method returns an error.

            waveform (numpy.array(dtype=numpy.int16)): Returns an array whose length is the **numSamples** times number of
                waveforms. Call ActualNumwfms to determine the number of
                waveforms.

                NI-SCOPE returns this data sequentially, so all record 0 waveforms are
                first. For example, with a channel list of 0,1, you would have the
                following index values:

                index 0 = record 0, channel 0

                index *x* = record 0, channel 1

                index 2\ *x* = record 1, channel 0

                index 3\ *x* = record 1, channel 1

                Where *x* = the record length

                Note:
                One or more of the referenced methods are not in the Python API for this driver.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): The time to wait in seconds for data to be acquired; using 0 for this
                parameter tells NI-SCOPE to fetch whatever is currently available. Using
                -1 for this parameter implies infinite timeout.


        Returns:
            wfm_info (numpy.array(dtype=numpy.WaveformInfo)): Returns a list of class instances with the following timing and scaling
                information about each waveform:

                -  **relativeInitialX**—the time (in seconds) from the trigger to the
                   first sample in the fetched waveform
                -  **absoluteInitialX**—timestamp (in seconds) of the first fetched
                   sample. This timestamp is comparable between records and
                   acquisitions; devices that do not support this parameter use 0 for
                   this output.
                -  **xIncrement**—the time between points in the acquired waveform in
                   seconds
                -  **actualSamples**—the actual number of samples fetched and placed in
                   the waveform array
                -  **gain**—the gain factor of the given channel; useful for scaling
                   binary data with the following formula:

                voltage = binary data × gain factor + offset

                -  **offset**—the offset factor of the given channel; useful for scaling
                   binary data with the following formula:

                voltage = binary data × gain factor + offset

                Call _actual_num_wfms to determine the size of this array.

        

#### `def _fetch_binary32_into_numpy(self, num_samples, waveform, timeout=hightime.timedelta(seconds=5.0))`

_fetch_binary32_into_numpy

        Retrieves data from a previously initiated acquisition and returns
        binary 32-bit waveforms. This method may return multiple waveforms
        depending on the number of channels, the acquisition type, and the
        number of records you specify.

        Refer to `Using Fetch
        Methods <REPLACE_DRIVER_SPECIFIC_URL_1(using_fetch_functions)>`__ for
        more information on using this method.

        Note:
        Some functionality, such as time stamping, is not supported in all
        digitizers. Refer to `Features Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._fetch_binary32`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._fetch_binary32`

        Args:
            num_samples (int): The maximum number of samples to fetch for each waveform. If the
                acquisition finishes with fewer points than requested, some devices
                return partial data if the acquisition finished, was aborted, or a
                timeout of 0 was used. If it fails to complete within the timeout
                period, the method returns an error.

            waveform (numpy.array(dtype=numpy.int32)): Returns an array whose length is the **numSamples** times number of
                waveforms. Call ActualNumwfms to determine the number of
                waveforms.

                NI-SCOPE returns this data sequentially, so all record 0 waveforms are
                first. For example, with a channel list of 0,1, you would have the
                following index values:

                index 0 = record 0, channel 0

                index *x* = record 0, channel 1

                index 2\ *x* = record 1, channel 0

                index 3\ *x* = record 1, channel 1

                Where *x* = the record length

                Note:
                One or more of the referenced methods are not in the Python API for this driver.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): The time to wait in seconds for data to be acquired; using 0 for this
                parameter tells NI-SCOPE to fetch whatever is currently available. Using
                -1 for this parameter implies infinite timeout.


        Returns:
            wfm_info (numpy.array(dtype=numpy.WaveformInfo)): Returns a list of class instances with the following timing and scaling
                information about each waveform:

                -  **relativeInitialX**—the time (in seconds) from the trigger to the
                   first sample in the fetched waveform
                -  **absoluteInitialX**—timestamp (in seconds) of the first fetched
                   sample. This timestamp is comparable between records and
                   acquisitions; devices that do not support this parameter use 0 for
                   this output.
                -  **xIncrement**—the time between points in the acquired waveform in
                   seconds
                -  **actualSamples**—the actual number of samples fetched and placed in
                   the waveform array
                -  **gain**—the gain factor of the given channel; useful for scaling
                   binary data with the following formula:

                voltage = binary data × gain factor + offset

                -  **offset**—the offset factor of the given channel; useful for scaling
                   binary data with the following formula:

                voltage = binary data × gain factor + offset

                Call _actual_num_wfms to determine the size of this array.

        

#### `def _fetch_binary8_into_numpy(self, num_samples, waveform, timeout=hightime.timedelta(seconds=5.0))`

_fetch_binary8_into_numpy

        Retrieves data from a previously initiated acquisition and returns
        binary 8-bit waveforms. This method may return multiple waveforms
        depending on the number of channels, the acquisition type, and the
        number of records you specify.

        Refer to `Using Fetch
        Methods <REPLACE_DRIVER_SPECIFIC_URL_1(using_fetch_functions)>`__ for
        more information on using this method.

        Note:
        Some functionality, such as time stamping, is not supported in all
        digitizers. Refer to `Features Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._fetch_binary8`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._fetch_binary8`

        Args:
            num_samples (int): The maximum number of samples to fetch for each waveform. If the
                acquisition finishes with fewer points than requested, some devices
                return partial data if the acquisition finished, was aborted, or a
                timeout of 0 was used. If it fails to complete within the timeout
                period, the method returns an error.

            waveform (numpy.array(dtype=numpy.int8)): Returns an array whose length is the **numSamples** times number of
                waveforms. Call ActualNumwfms to determine the number of
                waveforms.

                NI-SCOPE returns this data sequentially, so all record 0 waveforms are
                first. For example, with a channel list of 0,1, you would have the
                following index values:

                index 0 = record 0, channel 0

                index *x* = record 0, channel 1

                index 2\ *x* = record 1, channel 0

                index 3\ *x* = record 1, channel 1

                Where *x* = the record length

                Note:
                One or more of the referenced methods are not in the Python API for this driver.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): The time to wait in seconds for data to be acquired; using 0 for this
                parameter tells NI-SCOPE to fetch whatever is currently available. Using
                -1 for this parameter implies infinite timeout.


        Returns:
            wfm_info (numpy.array(dtype=numpy.WaveformInfo)): Returns a list of class instances with the following timing and scaling
                information about each waveform:

                -  **relativeInitialX**—the time (in seconds) from the trigger to the
                   first sample in the fetched waveform
                -  **absoluteInitialX**—timestamp (in seconds) of the first fetched
                   sample. This timestamp is comparable between records and
                   acquisitions; devices that do not support this parameter use 0 for
                   this output.
                -  **xIncrement**—the time between points in the acquired waveform in
                   seconds
                -  **actualSamples**—the actual number of samples fetched and placed in
                   the waveform array
                -  **gain**—the gain factor of the given channel; useful for scaling
                   binary data with the following formula:

                voltage = binary data × gain factor + offset

                -  **offset**—the offset factor of the given channel; useful for scaling
                   binary data with the following formula:

                voltage = binary data × gain factor + offset

                Call _actual_num_wfms to determine the size of this array.

        

#### `def fetch_into(self, waveform, relative_to=enums.FetchRelativeTo.PRETRIGGER, offset=0, record_number=0, num_records=None, timeout=hightime.timedelta(seconds=5.0))`

fetch

        Returns the waveform from a previously initiated acquisition that the
        digitizer acquires for the specified channel. This method returns
        scaled voltage waveforms.

        This method may return multiple waveforms depending on the number of
        channels, the acquisition type, and the number of records you specify.

        Note: Some functionality, such as time stamping, is not supported in all digitizers.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].fetch`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session.fetch`

        Args:
            waveform (array.array("d")): numpy array of the appropriate type and size that should be acquired as a 1D array. Size should be **num_samples** times number of waveforms. Call _actual_num_wfms to determine the number of waveforms.

                Types supported are

                - `numpy.float64`
                - `numpy.int8`
                - `numpy.in16`
                - `numpy.int32`

                Example:

                .. code-block:: python

                    waveform = numpy.ndarray(num_samples * session.actual_num_wfms(), dtype=numpy.float64)
                    wfm_info = session['0,1'].fetch_into(waveform, timeout=5.0)

            relative_to (enums.FetchRelativeTo): Position to start fetching within one record.

            offset (int): Offset in samples to start fetching data within each record.The offset can be positive or negative.

            record_number (int): Zero-based index of the first record to fetch.

            num_records (int): Number of records to fetch. Use -1 to fetch all configured records.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): The time to wait in seconds for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout.


        Returns:
            wfm_info (list of WaveformInfo): Returns a list of class instances with the following timing and scaling information about each waveform:

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

        

#### `def _fetch_measurement_stats(self, scalar_meas_function, timeout=hightime.timedelta(seconds=5.0))`

_fetch_measurement_stats

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
        clear_waveform_measurement_stats. Refer to `Using Fetch
        Methods <REPLACE_DRIVER_SPECIFIC_URL_1(using_fetch_functions)>`__ for
        more information on incorporating fetch methods in your application.

        Many of the measurements use the low, mid, and high reference levels.
        You configure the low, mid, and high references with
        meas_chan_low_ref_level,
        meas_chan_mid_ref_level, and
        meas_chan_high_ref_level to set each channel
        differently.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._fetch_measurement_stats`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._fetch_measurement_stats`

        Args:
            scalar_meas_function (enums.ScalarMeasurement): The `scalar
                measurement <REPLACE_DRIVER_SPECIFIC_URL_2(scalar_measurements_refs)>`__
                to be performed on each fetched waveform.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): The time to wait in seconds for data to be acquired; using 0 for this
                parameter tells NI-SCOPE to fetch whatever is currently available. Using
                -1 for this parameter implies infinite timeout.


        Returns:
            result (list of float): Returns the resulting measurement

            mean (list of float): Returns the mean scalar value, which is obtained by averaging each
                _fetch_measurement_stats call.

            stdev (list of float): Returns the standard deviation of the most recent **numInStats**
                measurements.

            min (list of float): Returns the smallest scalar value acquired (the minimum of the
                **numInStats** measurements).

            max (list of float): Returns the largest scalar value acquired (the maximum of the
                **numInStats** measurements).

            num_in_stats (list of int): Returns the number of times _fetch_measurement_stats has been
                called.

        

#### `def _get_attribute_vi_boolean(self, attribute_id)`

_get_attribute_vi_boolean

        Queries the value of a ViBoolean property. You can use this method to
        get the values of instrument-specific properties and inherent IVI
        properties. If the property represents an instrument state, this
        method performs instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_boolean`

        Args:
            attribute_id (int): The ID of a property.


        Returns:
            value (bool): Returns the current value of the property; pass the address of a
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
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_int32`

        Args:
            attribute_id (int): The ID of a property.


        Returns:
            value (int): Returns the current value of the property.

        

#### `def _get_attribute_vi_int64(self, attribute_id)`

_get_attribute_vi_int64

        Queries the value of a ViInt64 property. You can use this method to
        get the values of instrument-specific properties and inherent IVI
        properties. If the property represents an instrument state, this
        method performs instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_int64`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_int64`

        Args:
            attribute_id (int): The ID of a property.


        Returns:
            value (int): Returns the current value of the property.

        

#### `def _get_attribute_vi_real64(self, attribute_id)`

_get_attribute_vi_real64

        Queries the value of a ViReal64 property. You can use this method to
        get the values of instrument-specific properties and inherent IVI
        properties. If the property represents an instrument state, this
        method performs instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_real64`

        Args:
            attribute_id (int): The ID of a property.


        Returns:
            value (float): Returns the current value of the property; pass the address of a
                ViReal64 variable.

        

#### `def _get_attribute_vi_string(self, attribute_id)`

_get_attribute_vi_string

        Queries the value of a ViString property. You can use this method to
        get the values of instrument-specific properties and inherent IVI
        properties. If the property represents an instrument state, this
        method performs instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid.

        You must provide a ViChar array to serve as a buffer for the value. You
        pass the number of bytes in the buffer as the **bufSize**. If the
        current value of the property, including the terminating NUL byte, is
        larger than the size you indicate in the **bufSize**, the method
        copies (**bufSize** – 1) bytes into the buffer, places an ASCII NUL byte
        at the end of the buffer, and returns the **bufSize** you must pass to
        get the entire value. For example, if the value is 123456 and the
        **bufSize** is 4, the method places 123 into the buffer and returns 7.
        If you want to call this method just to get the required buffer size,
        you can pass 0 for the **bufSize** and VI_NULL for the **value**.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_string`

        Args:
            attribute_id (int): The ID of a property.


        Returns:
            value (str): The buffer in which the method returns the current value of the
                property; the buffer must be of type ViChar and have at least as many
                bytes as indicated in the **bufSize**.

        

#### `def _get_equalization_filter_coefficients(self, number_of_coefficients)`

_get_equalization_filter_coefficients

        Retrieves the custom coefficients for the equalization FIR filter on the
        device. This filter is designed to compensate the input signal for
        artifacts introduced to the signal outside of the digitizer. Because
        this filter is a generic FIR filter, any coefficients are valid.
        Coefficient values should be between +1 and –1.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_equalization_filter_coefficients`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._get_equalization_filter_coefficients`

        Args:
            number_of_coefficients (int): The number of coefficients being passed in the **coefficients** array.


        Returns:
            coefficients (list of float): The custom coefficients for the equalization FIR filter on the device.
                These coefficients should be between +1 and –1. You can obtain the
                number of coefficients from the
                `equalization_num_coefficients <cviequalization_num_coefficients.html>`__
                property.

        

#### `def lock(self)`

lock

        Obtains a multithread lock on the device session. Before doing so, the
        software waits until all other execution threads release their locks
        on the device session.

        Other threads may have obtained a lock on this session for the
        following reasons:

            -  The application called the lock method.
            -  A call to NI-SCOPE locked the session.
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
            lock (context manager): When used in a with statement, niscope.Session.lock acts as
            a context manager and unlock will be called when the with block is exited
        

#### `def _read(self, num_samples, timeout=hightime.timedelta(seconds=5.0))`

_read

        Initiates an acquisition, waits for it to complete, and retrieves the
        data. The process is similar to calling _initiate_acquisition,
        acquisition_status, and fetch. The only difference is
        that with read, you enable all channels specified with
        **channelList** before the acquisition; in the other method, you enable
        the channels with configure_vertical.

        This method may return multiple waveforms depending on the number of
        channels, the acquisition type, and the number of records you specify.

        Note:
        Some functionality is not supported in all digitizers. Refer to
        `Features Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._read`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._read`

        Args:
            num_samples (int): The maximum number of samples to fetch for each waveform. If the
                acquisition finishes with fewer points than requested, some devices
                return partial data if the acquisition finished, was aborted, or a
                timeout of 0 was used. If it fails to complete within the timeout
                period, the method returns an error.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): The time to wait in seconds for data to be acquired; using 0 for this
                parameter tells NI-SCOPE to fetch whatever is currently available. Using
                -1 for this parameter implies infinite timeout.


        Returns:
            waveform (array.array("d")): Returns an array whose length is the **numSamples** times number of
                waveforms. Call ActualNumwfms to determine the number of
                waveforms.

                NI-SCOPE returns this data sequentially, so all record 0 waveforms are
                first. For example, with a channel list of 0,1, you would have the
                following index values:

                index 0 = record 0, channel 0

                index *x* = record 0, channel 1

                index 2\ *x* = record 1, channel 0

                index 3\ *x* = record 1, channel 1

                Where *x* = the record length

                Note:
                One or more of the referenced methods are not in the Python API for this driver.

            wfm_info (list of WaveformInfo): Returns a list of class instances with the following timing and scaling
                information about each waveform:

                -  **relativeInitialX**—the time (in seconds) from the trigger to the
                   first sample in the fetched waveform
                -  **absoluteInitialX**—timestamp (in seconds) of the first fetched
                   sample. This timestamp is comparable between records and
                   acquisitions; devices that do not support this parameter use 0 for
                   this output.
                -  **xIncrement**—the time between points in the acquired waveform in
                   seconds
                -  **actualSamples**—the actual number of samples fetched and placed in
                   the waveform array
                -  **gain**—the gain factor of the given channel; useful for scaling
                   binary data with the following formula:

                voltage = binary data × gain factor + offset

                -  **offset**—the offset factor of the given channel; useful for scaling
                   binary data with the following formula:

                voltage = binary data × gain factor + offset

                Call _actual_num_wfms to determine the size of this array.

        

#### `def _set_attribute_vi_boolean(self, attribute_id, value)`

_set_attribute_vi_boolean

        Sets the value of a ViBoolean property. This is a low-level method
        that you can use to set the values of instrument-specific properties and
        inherent IVI properties. If the property represents an instrument
        state, this method performs instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid or
           is different than the value you specify.

        Note:
        NI-SCOPE contains high-level methods that set most of the instrument
        properties. Use the high-level driver methods as much as possible
        because they handle order dependencies and multithread locking for you.
        In addition, the high-level methods perform status checking only after
        setting all of the properties. In contrast, when you set multiple
        properties using the SetAttribute methods, the methods check the
        instrument status after each call. Also, when state caching is enabled,
        the high-level methods that configure multiple properties perform
        instrument I/O only for the properties whose value you change. Thus, you
        can safely call the high-level methods without the penalty of
        redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_boolean`

        Args:
            attribute_id (int): The ID of a property.

            value (bool): The value that you want to set the property to. Some values might not
                be valid depending on the current settings of the instrument session.

        

#### `def _set_attribute_vi_int32(self, attribute_id, value)`

_set_attribute_vi_int32

        Sets the value of a ViInt32 property. This is a low-level method that
        you can use to set the values of instrument-specific properties and
        inherent IVI properties. If the property represents an instrument
        state, this method performs instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid or
           is different than the value you specify.

        Note:
        NI-SCOPE contains high-level methods that set most of the instrument
        properties. Use the high-level methods as much as possible because
        they handle order dependencies and multithread locking for you. In
        addition, high-level methods perform status checking only after
        setting all of the properties. In contrast, when you set multiple
        properties using the Set Property methods, the methods check the
        instrument status after each call. Also, when state caching is enabled,
        the high-level methods that configure multiple properties perform
        instrument I/O only for the properties whose value you change. Thus, you
        can safely call the high-level methods without the penalty of
        redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_int32`

        Args:
            attribute_id (int): The ID of a property.

            value (int): The value that you want to set the property. Some values might not be
                valid depending on the current settings of the instrument session.

        

#### `def _set_attribute_vi_int64(self, attribute_id, value)`

_set_attribute_vi_int64

        Sets the value of a ViInt64 property. This is a low-level method that
        you can use to set the values of instrument-specific properties and
        inherent IVI properties. If the property represents an instrument
        state, this method performs instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid or
           is different than the value you specify.

        Note:
        NI-SCOPE contains high-level methods that set most of the instrument
        properties. Use the high-level methods as much as possible because
        they handle order dependencies and multithread locking for you. In
        addition, high-level methods perform status checking only after
        setting all of the properties. In contrast, when you set multiple
        properties using the Set Property methods, the methods check the
        instrument status after each call. Also, when state caching is enabled,
        the high-level methods that configure multiple properties perform
        instrument I/O only for the properties whose value you change. Thus, you
        can safely call the high-level methods without the penalty of
        redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_int64`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_int64`

        Args:
            attribute_id (int): The ID of a property.

            value (int): The value that you want to set the property. Some values might not be
                valid depending on the current settings of the instrument session.

        

#### `def _set_attribute_vi_real64(self, attribute_id, value)`

_set_attribute_vi_real64

        Sets the value of a ViReal64 property. This is a low-level method
        that you can use to set the values of instrument-specific properties and
        inherent IVI properties. If the property represents an instrument
        state, this method performs instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid or
           is different than the value you specify.

        Note:
        NI-SCOPE contains high-level methods that set most of the instrument
        properties. Use the high-level driver methods as much as possible
        because they handle order dependencies and multithread locking for you.
        In addition, the high-level methods perform status checking only after
        setting all of the properties. In contrast, when you set multiple
        properties using the Set Property methods, the methods check the
        instrument status after each call. Also, when state caching is enabled,
        the high-level methods that configure multiple properties perform
        instrument I/O only for the properties whose value you change. Thus, you
        can safely call the high-level methods without the penalty of
        redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_real64`

        Args:
            attribute_id (int): The ID of a property.

            value (float): The value that you want to set the property to. Some values might not
                be valid depending on the current settings of the instrument session.

        

#### `def _set_attribute_vi_string(self, attribute_id, value)`

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

        Note:
        NI-SCOPE contains high-level methods that set most of the instrument
        properties. Use the high-level driver methods as much as possible
        because they handle order dependencies and multithread locking for you.
        In addition, the high-level methods perform status checking only after
        setting all of the properties. In contrast, when you set multiple
        properties using the SetAttribute methods, the methods check the
        instrument status after each call. Also, when state caching is enabled,
        the high-level methods that configure multiple properties perform
        instrument I/O only for the properties whose value you change. Thus, you
        can safely call the high-level methods without the penalty of
        redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`niscope.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`niscope.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_string`

        Args:
            attribute_id (int): The ID of a property.

            value (str): The value that you want to set the property to. Some values might not
                be valid depending on the current settings of the instrument session.

        

#### `def unlock(self)`

unlock

        Releases a lock that you acquired on an device session using
        lock. Refer to lock for additional
        information on session locks.
        

#### `def _error_message(self, error_code)`

_error_message

        Takes the **Error_Code** returned by the instrument driver methods, interprets it, and returns it as a user-readable string.

        Note:
        When using grpc-device, this method will call GetErrorMessage server-side while providing the same interface.

        Args:
            error_code (int): The **error_code** returned from the instrument. The default is 0, indicating VI_SUCCESS.


        Returns:
            error_message (str): The error information formatted into a string.

        

### `class Session(_SessionBase)`

An NI-SCOPE session to an NI digitizer.

#### `def __init__(self, resource_name, id_query=False, reset_device=False, options={}, *, grpc_options=None)`

An NI-SCOPE session to an NI digitizer.

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

        Args:
            resource_name (str): Caution:
                Traditional NI-DAQ and NI-DAQmx device names are not case-sensitive.
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

            id_query (bool): Specify whether to perform an ID query.

                When you set this parameter to True, NI-SCOPE verifies that the
                device you initialize is a type that it supports.

                When you set this parameter to False, the method initializes the
                device without performing an ID query.

                **Defined Values**

                | True—Perform ID query
                | False—Skip ID query

                **Default Value**: True

            reset_device (bool): Specify whether to reset the device during the initialization process.

                Default Value: True

                **Defined Values**

                True (1)—Reset device

                False (0)—Do not reset device

                Note:
                For the NI 5112, repeatedly resetting the device may cause excessive
                wear on the electromechanical relays. Refer to `NI 5112
                Electromechanical Relays <REPLACE_DRIVER_SPECIFIC_URL_1(5112_relays)>`__
                for recommended programming practices.

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

            grpc_options (niscope.grpc_session_options.GrpcSessionOptions): MeasurementLink gRPC session options


        Returns:
            session (niscope.Session): A session object representing the device.

        

#### `def __enter__(self)`

#### `def __exit__(self, exc_type, exc_value, traceback)`

#### `def initiate(self)`

initiate

        Initiates a waveform acquisition.

        After calling this method, the digitizer leaves the Idle state and
        waits for a trigger. The digitizer acquires a waveform for each channel
        you enable with configure_vertical.

        Note:
        This method will return a Python context manager that will initiate on entering and abort on exit.
        

#### `def close(self)`

close

        When you are finished using an instrument driver session, you must call
        this method to perform the following actions:

        -  Closes the instrument I/O session.
        -  Destroys the IVI session and all of its properties.
        -  Deallocates any memory resources used by the IVI session.

        Note:
        This method is not needed when using the session context manager
        

#### `def abort(self)`

abort

        Aborts an acquisition and returns the digitizer to the Idle state. Call
        this method if the digitizer times out waiting for a trigger.
        

#### `def acquisition_status(self)`

acquisition_status

        Returns status information about the acquisition to the **status**
        output parameter.

        Returns:
            acquisition_status (enums.AcquisitionStatus): Returns whether the acquisition is complete, in progress, or unknown.

                **Defined Values**

                AcquisitionStatus.COMPLETE

                AcquisitionStatus.IN_PROGRESS

                AcquisitionStatus.STATUS_UNKNOWN

        

#### `def auto_setup(self)`

auto_setup

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
        

#### `def _cal_fetch_date(self, which_one)`

_cal_fetch_date

        TBD

        Args:
            which_one (enums.CalibrationTypes):


        Returns:
            year (int):

            month (int):

            day (int):

        

#### `def _cal_fetch_temperature(self, which_one)`

_cal_fetch_temperature

        TBD

        Args:
            which_one (int):


        Returns:
            temperature (float):

        

#### `def commit(self)`

commit

        Commits to hardware all the parameter settings associated with the task.
        Use this method if you want a parameter change to be immediately
        reflected in the hardware. This method is not supported for
        Traditional NI-DAQ (Legacy) devices.
        

#### `def configure_horizontal_timing(self, min_sample_rate, min_num_pts, ref_position, num_records, enforce_realtime)`

configure_horizontal_timing

        Configures the common properties of the horizontal subsystem for a
        multirecord acquisition in terms of minimum sample rate.

        Args:
            min_sample_rate (float): The sampling rate for the acquisition. Refer to
                min_sample_rate for more information.

            min_num_pts (int): The minimum number of points you need in the record for each channel;
                call ActualRecordLength to obtain the actual record length
                used.

                Valid Values: Greater than 1; limited by available memory

                Note:
                One or more of the referenced methods are not in the Python API for this driver.

            ref_position (float): The position of the Reference Event in the waveform record specified as
                a percentage.

            num_records (int): The number of records to acquire

            enforce_realtime (bool): Indicates whether the digitizer enforces real-time measurements or
                allows equivalent-time (RIS) measurements; not all digitizers support
                RIS—refer to `Features Supported by
                Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
                more information.

                Default value: True

                **Defined Values**

                True—Allow real-time acquisitions only

                False—Allow real-time and equivalent-time acquisitions

        

#### `def _configure_ref_levels(self, low=10.0, mid=50.0, high=90.0)`

_configure_ref_levels

        This method is included for compliance with the IviScope Class
        Specification.

        Configures the reference levels for all channels of the digitizer. The
        levels may be set on a per channel basis by setting
        meas_chan_high_ref_level,
        meas_chan_low_ref_level, and
        meas_chan_mid_ref_level

        This method configures the reference levels for waveform measurements.
        Call this method before calling FetchMeasurement to take a
        rise time, fall time, width negative, width positive, duty cycle
        negative, or duty cycle positive measurement.

        Note:
        One or more of the referenced methods are not in the Python API for this driver.

        Args:
            low (float): Pass the low reference you want the digitizer to use for waveform
                measurements.

                Units: Either a percentage or voltage based on
                meas_ref_level_units. A percentage is calculated with
                the voltage low and voltage high measurements representing 0% and 100%,
                respectively.

                Default Value: 10.0

            mid (float): Pass the mid reference you want the digitizer to use for waveform
                measurements.

                Units: Either a percentage or voltage based on
                meas_ref_level_units. A percentage is calculated with
                the voltage low and voltage high measurements representing 0% and 100%,
                respectively.

                Default Value: 50.0

            high (float): Pass the high reference you want the digitizer to use for waveform
                measurements.

                Units: Either a percentage or voltage based on
                meas_ref_level_units. A percentage is calculated with
                the voltage low and voltage high measurements representing 0% and 100%,
                respectively.

                Default Value: 90.0

        

#### `def configure_trigger_digital(self, trigger_source, slope=enums.TriggerSlope.POSITIVE, holdoff=hightime.timedelta(seconds=0.0), delay=hightime.timedelta(seconds=0.0))`

configure_trigger_digital

        Configures the common properties of a digital trigger.

        When you initiate an acquisition, the digitizer waits for the start
        trigger, which is configured through the acq_arm_source
        (Start Trigger Source) property. The default is immediate. Upon
        receiving the start trigger the digitizer begins sampling pretrigger
        points. After the digitizer finishes sampling pretrigger points, the
        digitizer waits for a reference (stop) trigger that you specify with a
        method such as this one. Upon receiving the reference trigger the
        digitizer finishes the acquisition after completing posttrigger
        sampling. With each Configure Trigger method, you specify
        configuration parameters such as the trigger source and the amount of
        trigger delay.

        Note:
        For multirecord acquisitions, all records after the first record are
        started by using the Advance Trigger Source. The default is immediate.

        You can adjust the amount of pre-trigger and post-trigger samples using
        the reference position parameter on the
        configure_horizontal_timing method. The default is half of the
        record length.

        Some features are not supported by all digitizers. Refer to `Features
        Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Digital triggering is not supported in RIS mode.

        Args:
            trigger_source (str): Specifies the trigger source. Refer to trigger_source
                for defined values.

            slope (enums.TriggerSlope): Specifies whether you want a rising edge or a falling edge to trigger
                the digitizer. Refer to trigger_slope for more
                information.

            holdoff (hightime.timedelta, datetime.timedelta, or float in seconds): The length of time the digitizer waits after detecting a trigger before
                enabling NI-SCOPE to detect another trigger. Refer to
                trigger_holdoff for more information.

            delay (hightime.timedelta, datetime.timedelta, or float in seconds): How long the digitizer waits after receiving the trigger to start
                acquiring data. Refer to trigger_delay_time for more
                information.

        

#### `def configure_trigger_edge(self, trigger_source, level, trigger_coupling, slope=enums.TriggerSlope.POSITIVE, holdoff=hightime.timedelta(seconds=0.0), delay=hightime.timedelta(seconds=0.0))`

configure_trigger_edge

        Configures common properties for analog edge triggering.

        When you initiate an acquisition, the digitizer waits for the start
        trigger, which is configured through the acq_arm_source
        (Start Trigger Source) property. The default is immediate. Upon
        receiving the start trigger the digitizer begins sampling pretrigger
        points. After the digitizer finishes sampling pretrigger points, the
        digitizer waits for a reference (stop) trigger that you specify with a
        method such as this one. Upon receiving the reference trigger the
        digitizer finishes the acquisition after completing posttrigger
        sampling. With each Configure Trigger method, you specify
        configuration parameters such as the trigger source and the amount of
        trigger delay.

        Note:
        Some features are not supported by all digitizers. Refer to `Features
        Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Args:
            trigger_source (str): Specifies the trigger source. Refer to trigger_source
                for defined values.

            level (float): The voltage threshold for the trigger. Refer to
                trigger_level for more information.

            trigger_coupling (enums.TriggerCoupling): Applies coupling and filtering options to the trigger signal. Refer to
                trigger_coupling for more information.

            slope (enums.TriggerSlope): Specifies whether you want a rising edge or a falling edge to trigger
                the digitizer. Refer to trigger_slope for more
                information.

            holdoff (hightime.timedelta, datetime.timedelta, or float in seconds): The length of time the digitizer waits after detecting a trigger before
                enabling NI-SCOPE to detect another trigger. Refer to
                trigger_holdoff for more information.

            delay (hightime.timedelta, datetime.timedelta, or float in seconds): How long the digitizer waits after receiving the trigger to start
                acquiring data. Refer to trigger_delay_time for more
                information.

        

#### `def configure_trigger_hysteresis(self, trigger_source, level, hysteresis, trigger_coupling, slope=enums.TriggerSlope.POSITIVE, holdoff=hightime.timedelta(seconds=0.0), delay=hightime.timedelta(seconds=0.0))`

configure_trigger_hysteresis

        Configures common properties for analog hysteresis triggering. This kind
        of trigger specifies an additional value, specified in the
        **hysteresis** parameter, that a signal must pass through before a
        trigger can occur. This additional value acts as a kind of buffer zone
        that keeps noise from triggering an acquisition.

        When you initiate an acquisition, the digitizer waits for the start
        trigger, which is configured through the
        acq_arm_source. The default is immediate. Upon
        receiving the start trigger the digitizer begins sampling pretrigger
        points. After the digitizer finishes sampling pretrigger points, the
        digitizer waits for a reference (stop) trigger that you specify with a
        method such as this one. Upon receiving the reference trigger the
        digitizer finishes the acquisition after completing posttrigger
        sampling. With each Configure Trigger method, you specify
        configuration parameters such as the trigger source and the amount of
        trigger delay.

        Note:
        Some features are not supported by all digitizers. Refer to `Features
        Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Args:
            trigger_source (str): Specifies the trigger source. Refer to trigger_source
                for defined values.

            level (float): The voltage threshold for the trigger. Refer to
                trigger_level for more information.

            hysteresis (float): The size of the hysteresis window on either side of the **level** in
                volts; the digitizer triggers when the trigger signal passes through the
                hysteresis value you specify with this parameter, has the slope you
                specify with **slope**, and passes through the **level**. Refer to
                trigger_hysteresis for defined values.

            trigger_coupling (enums.TriggerCoupling): Applies coupling and filtering options to the trigger signal. Refer to
                trigger_coupling for more information.

            slope (enums.TriggerSlope): Specifies whether you want a rising edge or a falling edge to trigger
                the digitizer. Refer to trigger_slope for more
                information.

            holdoff (hightime.timedelta, datetime.timedelta, or float in seconds): The length of time the digitizer waits after detecting a trigger before
                enabling NI-SCOPE to detect another trigger. Refer to
                trigger_holdoff for more information.

            delay (hightime.timedelta, datetime.timedelta, or float in seconds): How long the digitizer waits after receiving the trigger to start
                acquiring data. Refer to trigger_delay_time for more
                information.

        

#### `def configure_trigger_immediate(self)`

configure_trigger_immediate

        Configures common properties for immediate triggering. Immediate
        triggering means the digitizer triggers itself.

        When you initiate an acquisition, the digitizer waits for a trigger. You
        specify the type of trigger that the digitizer waits for with a
        Configure Trigger method, such as configure_trigger_immediate.
        

#### `def configure_trigger_software(self, holdoff=hightime.timedelta(seconds=0.0), delay=hightime.timedelta(seconds=0.0))`

configure_trigger_software

        Configures common properties for software triggering.

        When you initiate an acquisition, the digitizer waits for the start
        trigger, which is configured through the acq_arm_source
        (Start Trigger Source) property. The default is immediate. Upon
        receiving the start trigger the digitizer begins sampling pretrigger
        points. After the digitizer finishes sampling pretrigger points, the
        digitizer waits for a reference (stop) trigger that you specify with a
        method such as this one. Upon receiving the reference trigger the
        digitizer finishes the acquisition after completing posttrigger
        sampling. With each Configure Trigger method, you specify
        configuration parameters such as the trigger source and the amount of
        trigger delay.

        To trigger the acquisition, use send_software_trigger_edge.

        Note:
        Some features are not supported by all digitizers. Refer to `Features
        Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Args:
            holdoff (hightime.timedelta, datetime.timedelta, or float in seconds): The length of time the digitizer waits after detecting a trigger before
                enabling NI-SCOPE to detect another trigger. Refer to
                trigger_holdoff for more information.

            delay (hightime.timedelta, datetime.timedelta, or float in seconds): How long the digitizer waits after receiving the trigger to start
                acquiring data. Refer to trigger_delay_time for more
                information.

        

#### `def configure_trigger_video(self, trigger_source, signal_format, event, polarity, trigger_coupling, enable_dc_restore=False, line_number=1, holdoff=hightime.timedelta(seconds=0.0), delay=hightime.timedelta(seconds=0.0))`

configure_trigger_video

        Configures the common properties for video triggering, including the
        signal format, TV event, line number, polarity, and enable DC restore. A
        video trigger occurs when the digitizer finds a valid video signal sync.

        When you initiate an acquisition, the digitizer waits for the start
        trigger, which is configured through the acq_arm_source
        (Start Trigger Source) property. The default is immediate. Upon
        receiving the start trigger the digitizer begins sampling pretrigger
        points. After the digitizer finishes sampling pretrigger points, the
        digitizer waits for a reference (stop) trigger that you specify with a
        method such as this one. Upon receiving the reference trigger the
        digitizer finishes the acquisition after completing posttrigger
        sampling. With each Configure Trigger method, you specify
        configuration parameters such as the trigger source and the amount of
        trigger delay.

        Note:
        Some features are not supported by all digitizers. Refer to `Features
        Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Args:
            trigger_source (str): Specifies the trigger source. Refer to trigger_source
                for defined values.

            signal_format (enums.VideoSignalFormat): Specifies the type of video signal sync the digitizer should look for.
                Refer to tv_trigger_signal_format for more
                information.

            event (enums.VideoTriggerEvent): Specifies the TV event you want to trigger on. You can trigger on a
                specific or on the next coming line or field of the signal.

            polarity (enums.VideoPolarity): Specifies the polarity of the video signal sync.

            trigger_coupling (enums.TriggerCoupling): Applies coupling and filtering options to the trigger signal. Refer to
                trigger_coupling for more information.

            enable_dc_restore (bool): Offsets each video line so the clamping level (the portion of the video
                line between the end of the color burst and the beginning of the active
                image) is moved to zero volt. Refer to
                enable_dc_restore for defined values.

            line_number (int): Selects the line number to trigger on. The line number range covers an
                entire frame and is referenced as shown on `Vertical Blanking and
                Synchronization
                Signal <REPLACE_DRIVER_SPECIFIC_URL_1(gray_scale_image)>`__. Refer to
                tv_trigger_line_number for more information.

                Default value: 1

            holdoff (hightime.timedelta, datetime.timedelta, or float in seconds): The length of time the digitizer waits after detecting a trigger before
                enabling NI-SCOPE to detect another trigger. Refer to
                trigger_holdoff for more information.

            delay (hightime.timedelta, datetime.timedelta, or float in seconds): How long the digitizer waits after receiving the trigger to start
                acquiring data. Refer to trigger_delay_time for more
                information.

        

#### `def configure_trigger_window(self, trigger_source, low_level, high_level, window_mode, trigger_coupling, holdoff=hightime.timedelta(seconds=0.0), delay=hightime.timedelta(seconds=0.0))`

configure_trigger_window

        Configures common properties for analog window triggering. A window
        trigger occurs when a signal enters or leaves a window you specify with
        the **high level** or **low level** parameters.

        When you initiate an acquisition, the digitizer waits for the start
        trigger, which is configured through the acq_arm_source
        (Start Trigger Source) property. The default is immediate. Upon
        receiving the start trigger the digitizer begins sampling pretrigger
        points. After the digitizer finishes sampling pretrigger points, the
        digitizer waits for a reference (stop) trigger that you specify with a
        method such as this one. Upon receiving the reference trigger the
        digitizer finishes the acquisition after completing posttrigger
        sampling. With each Configure Trigger method, you specify
        configuration parameters such as the trigger source and the amount of
        trigger delay.

        To trigger the acquisition, use send_software_trigger_edge.

        Note: Some features are not supported by all digitizers.

        Args:
            trigger_source (str): Specifies the trigger source. Refer to trigger_source
                for defined values.

            low_level (float): Passes the voltage threshold you want the digitizer to use for low
                triggering.

            high_level (float): Passes the voltage threshold you want the digitizer to use for high
                triggering.

            window_mode (enums.TriggerWindowMode): Specifies whether you want the trigger to occur when the signal enters
                or leaves a window.

            trigger_coupling (enums.TriggerCoupling): Applies coupling and filtering options to the trigger signal. Refer to
                trigger_coupling for more information.

            holdoff (hightime.timedelta, datetime.timedelta, or float in seconds): The length of time the digitizer waits after detecting a trigger before
                enabling NI-SCOPE to detect another trigger. Refer to
                trigger_holdoff for more information.

            delay (hightime.timedelta, datetime.timedelta, or float in seconds): How long the digitizer waits after receiving the trigger to start
                acquiring data. Refer to trigger_delay_time for more
                information.

        

#### `def disable(self)`

disable

        Aborts any current operation, opens data channel relays, and releases
        RTSI and PFI lines.
        

#### `def export_attribute_configuration_buffer(self)`

export_attribute_configuration_buffer

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
        session are valid. If the configuration is invalid, NI‑SCOPE returns an
        error.

        **Related Topics:**

        `Properties and Property
        Methods <REPLACE_DRIVER_SPECIFIC_URL_1(attributes_and_attribute_functions)>`__

        `Setting Properties Before Reading
        Properties <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

        Args:
            file_path (str): Specifies the absolute path to the file to contain the exported
                property configuration. If you specify an empty or relative path, this
                method returns an error.
                **Default file extension:** .niscopeconfig

        

#### `def get_ext_cal_last_date_and_time(self)`

get_ext_cal_last_date_and_time

        Returns the date and time of the last external calibration performed.

        Returns:
            last_cal_datetime (hightime.timedelta, datetime.timedelta, or float in seconds): Indicates the **date** of the last calibration. A hightime.datetime object is returned, but only contains resolution to the day.

        

#### `def get_ext_cal_last_temp(self)`

get_ext_cal_last_temp

        Returns the onboard temperature, in degrees Celsius, of an oscilloscope at the time of the last successful external calibration.
        The temperature returned by this node is an onboard temperature read from a sensor on the surface of the oscilloscope. This temperature should not be confused with the environmental temperature of the oscilloscope surroundings. During operation, the onboard temperature is normally higher than the environmental temperature.
        Temperature-sensitive parameters are calibrated during self-calibration. Therefore, the self-calibration temperature is usually more important to read than the external calibration temperature.

        Returns:
            temperature (float): Returns the **temperature** in degrees Celsius during the last calibration.

        

#### `def get_self_cal_last_date_and_time(self)`

get_self_cal_last_date_and_time

        Returns the date and time of the last self calibration performed.

        Returns:
            last_cal_datetime (hightime.timedelta, datetime.timedelta, or float in seconds): Indicates the **date** of the last calibration. A hightime.datetime object is returned, but only contains resolution to the day.

        

#### `def get_self_cal_last_temp(self)`

get_self_cal_last_temp

        Returns the onboard temperature, in degrees Celsius, of an oscilloscope at the time of the last successful self calibration.
        The temperature returned by this node is an onboard temperature read from a sensor on the surface of the oscilloscope. This temperature should not be confused with the environmental temperature of the oscilloscope surroundings. During operation, the onboard temperature is normally higher than the environmental temperature.
        Temperature-sensitive parameters are calibrated during self-calibration. Therefore, the self-calibration temperature is usually more important to read than the external calibration temperature.

        Returns:
            temperature (float): Returns the **temperature** in degrees Celsius during the last calibration.

        

#### `def get_channel_names(self, indices)`

get_channel_names

        Returns a list of channel names for given channel indices.

        Args:
            indices (basic sequence types, str, or int): Index list for the channels in the session. Valid values are from zero to the total number of channels in the session minus one. The index string can be one of the following formats:

                -   A comma-separated list—for example, "0,2,3,1"
                -   A range using a hyphen—for example, "0-3"
                -   A range using a colon—for example, "0:3 "

                You can combine comma-separated lists and ranges that use a hyphen or colon. Both out-of-order and repeated indices are supported ("2,3,0", "1,2,2,3"). White space characters, including spaces, tabs, feeds, and carriage returns, are allowed between characters. Ranges can be incrementing or decrementing.


        Returns:
            names (list of str): The channel name(s) at the specified indices.

        

#### `def import_attribute_configuration_buffer(self, configuration)`

import_attribute_configuration_buffer

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

        Note:
        You cannot call this method while the session is in a running state,
        such as while acquiring a signal.

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

        **Related Topics:**

        `Properties and Property
        Methods <REPLACE_DRIVER_SPECIFIC_URL_1(attributes_and_attribute_functions)>`__

        `Setting Properties Before Reading
        Properties <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

        Note:
        You cannot call this method while the session is in a running state,
        such as while acquiring a signal.

        Args:
            file_path (str): Specifies the absolute path to the file containing the property
                configuration to import. If you specify an empty or relative path, this
                method returns an error.
                **Default File Extension:** .niscopeconfig

        

#### `def _init_with_options(self, resource_name, id_query=False, reset_device=False, option_string='')`

_init_with_options

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

        Args:
            resource_name (str): Caution:
                Traditional NI-DAQ and NI-DAQmx device names are not case-sensitive.
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

            id_query (bool): Specify whether to perform an ID query.

                When you set this parameter to True, NI-SCOPE verifies that the
                device you initialize is a type that it supports.

                When you set this parameter to False, the method initializes the
                device without performing an ID query.

                **Defined Values**

                | True—Perform ID query
                | False—Skip ID query

                **Default Value**: True

            reset_device (bool): Specify whether to reset the device during the initialization process.

                Default Value: True

                **Defined Values**

                True (1)—Reset device

                False (0)—Do not reset device

                Note:
                For the NI 5112, repeatedly resetting the device may cause excessive
                wear on the electromechanical relays. Refer to `NI 5112
                Electromechanical Relays <REPLACE_DRIVER_SPECIFIC_URL_1(5112_relays)>`__
                for recommended programming practices.

            option_string (dict): | Specifies initialization commands. The following table lists the
                  properties and the name you use in the **optionString** to identify
                  the property.

                Default Values: "Simulate=0,RangeCheck=1,QueryInstrStatus=1,Cache=1"

                You can use the option string to simulate a device. The DriverSetup flag
                specifies the model that is to be simulated and the type of the model.
                One example to simulate an NI PXI-5102 would be as follows:

                Option String: Simulate = 1, DriverSetup = Model:5102; BoardType:PXI

                Refer to the example niScope EX Simulated Acquisition for more
                information on simulation.

                You can also use the option string to attach an accessory such as the
                NI 5900 to your digitizer session to allow the seamless use of the
                accessory:

                Option String: DriverSetup = Accessory:Dev1

                Refer to the example niScope EX External Amplifier for more information.


        Returns:
            vi (int): Returns a session handle that you can use to identify the device in all
                subsequent NI-SCOPE method calls.

        

#### `def _initiate_acquisition(self)`

_initiate_acquisition

        Initiates a waveform acquisition.

        After calling this method, the digitizer leaves the Idle state and
        waits for a trigger. The digitizer acquires a waveform for each channel
        you enable with configure_vertical.
        

#### `def probe_compensation_signal_start(self)`

probe_compensation_signal_start

        Starts the 1 kHz square wave output on PFI 1 for probe compensation.
        

#### `def probe_compensation_signal_stop(self)`

probe_compensation_signal_stop

        Stops the 1 kHz square wave output on PFI 1 for probe compensation.
        

#### `def reset_device(self)`

reset_device

        Performs a hard reset of the device. Acquisition stops, all routes are
        released, RTSI and PFI lines are tristated, hardware is configured to
        its default state, and all session properties are reset to their default
        state.

        -  `Thermal Shutdown <digitizers.chm::/Thermal_Shutdown.html>`__
        

#### `def reset_with_defaults(self)`

reset_with_defaults

        Performs a software reset of the device, returning it to the default
        state and applying any initial default settings from the IVI
        Configuration Store.
        

#### `def send_software_trigger_edge(self, which_trigger)`

send_software_trigger_edge

        Sends the selected trigger to the digitizer. Call this method if you
        called configure_trigger_software when you want the Reference
        trigger to occur. You can also call this method to override a misused
        edge, digital, or hysteresis trigger. If you have configured
        acq_arm_source, arm_ref_trig_src, or
        adv_trig_src, call this method when you want to send
        the corresponding trigger to the digitizer.

        Args:
            which_trigger (enums.WhichTrigger): Specifies the type of trigger to send to the digitizer.

                **Defined Values**

                | WhichTrigger.START (0L)
                |  WhichTrigger.ARM_REFERENCE (1L)
                | WhichTrigger.REFERENCE (2L)
                | WhichTrigger.ADVANCE (3L)

        

#### `def _close(self)`

_close

        When you are finished using an instrument driver session, you must call
        this method to perform the following actions:

        -  Closes the instrument I/O session.
        -  Destroys the IVI session and all of its properties.
        -  Deallocates any memory resources used by the IVI session.
        

#### `def self_test(self)`

self_test

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
        

#### `def reset(self)`

reset

        Stops the acquisition, releases routes, and all session properties are
        reset to their `default
        states <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cviattribute_defaults)>`__.
        

#### `def _self_test(self)`

_self_test

        Runs the instrument self-test routine and returns the test result(s).

        Returns:
            self_test_result (int): This control contains the value returned from the instrument self-test.

                **Self-Test Code Description**

                0—Self-test passed

                1—Self-test failed

            self_test_message (str): Returns the self-test response string from the instrument. Refer to the
                device-specific help topics for an explanation of the string contents;
                you must pass a ViChar array at least IVI_MAX_MESSAGE_BUF_SIZE bytes
                in length.

        

<!--NI_PYTHON_API repo=nimi-python path=generated/niscope/niscope/unit_tests/_matchers.py -->
## PYTHON MODULE: generated/niscope/niscope/unit_tests/_matchers.py

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

<!--NI_PYTHON_API repo=nimi-python path=generated/niscope/niscope/unit_tests/_mock_helper.py -->
## PYTHON MODULE: generated/niscope/niscope/unit_tests/_mock_helper.py

### `class MockFunctionCallError(Exception)`

#### `def __init__(self, function, param=None)`

### `class SideEffectsHelper(object)`

#### `def __init__(self)`

#### `def __getitem__(self, func)`

#### `def __setitem__(self, func, val)`

#### `def niScope_Abort(self, vi)`

#### `def niScope_AcquisitionStatus(self, vi, acquisition_status)`

#### `def niScope_ActualMeasWfmSize(self, vi, array_meas_function, meas_waveform_size)`

#### `def niScope_ActualNumWfms(self, vi, channel_list, num_wfms)`

#### `def niScope_AddWaveformProcessing(self, vi, channel_list, meas_function)`

#### `def niScope_AutoSetup(self, vi)`

#### `def niScope_CalFetchDate(self, vi, which_one, year, month, day)`

#### `def niScope_CalFetchTemperature(self, vi, which_one, temperature)`

#### `def niScope_CalSelfCalibrate(self, vi, channel_list, option)`

#### `def niScope_ClearWaveformMeasurementStats(self, vi, channel_list, clearable_measurement_function)`

#### `def niScope_ClearWaveformProcessing(self, vi, channel_list)`

#### `def niScope_Commit(self, vi)`

#### `def niScope_ConfigureChanCharacteristics(self, vi, channel_list, input_impedance, max_input_frequency)`

#### `def niScope_ConfigureEqualizationFilterCoefficients(self, vi, channel_list, number_of_coefficients, coefficients)`

#### `def niScope_ConfigureHorizontalTiming(self, vi, min_sample_rate, min_num_pts, ref_position, num_records, enforce_realtime)`

#### `def niScope_ConfigureRefLevels(self, vi, low, mid, high)`

#### `def niScope_ConfigureTriggerDigital(self, vi, trigger_source, slope, holdoff, delay)`

#### `def niScope_ConfigureTriggerEdge(self, vi, trigger_source, level, slope, trigger_coupling, holdoff, delay)`

#### `def niScope_ConfigureTriggerHysteresis(self, vi, trigger_source, level, hysteresis, slope, trigger_coupling, holdoff, delay)`

#### `def niScope_ConfigureTriggerImmediate(self, vi)`

#### `def niScope_ConfigureTriggerSoftware(self, vi, holdoff, delay)`

#### `def niScope_ConfigureTriggerVideo(self, vi, trigger_source, enable_dc_restore, signal_format, event, line_number, polarity, trigger_coupling, holdoff, delay)`

#### `def niScope_ConfigureTriggerWindow(self, vi, trigger_source, low_level, high_level, window_mode, trigger_coupling, holdoff, delay)`

#### `def niScope_ConfigureVertical(self, vi, channel_list, range, offset, coupling, probe_attenuation, enabled)`

#### `def niScope_Disable(self, vi)`

#### `def niScope_ExportAttributeConfigurationBuffer(self, vi, size_in_bytes, configuration)`

#### `def niScope_ExportAttributeConfigurationFile(self, vi, file_path)`

#### `def niScope_Fetch(self, vi, channel_list, timeout, num_samples, waveform, wfm_info)`

#### `def niScope_FetchArrayMeasurement(self, vi, channel_list, timeout, array_meas_function, measurement_waveform_size, meas_wfm, wfm_info)`

#### `def niScope_FetchBinary16(self, vi, channel_list, timeout, num_samples, waveform, wfm_info)`

#### `def niScope_FetchBinary32(self, vi, channel_list, timeout, num_samples, waveform, wfm_info)`

#### `def niScope_FetchBinary8(self, vi, channel_list, timeout, num_samples, waveform, wfm_info)`

#### `def niScope_FetchMeasurementStats(self, vi, channel_list, timeout, scalar_meas_function, result, mean, stdev, min, max, num_in_stats)`

#### `def niScope_GetAttributeViBoolean(self, vi, channel_list, attribute_id, value)`

#### `def niScope_GetAttributeViInt32(self, vi, channel_list, attribute_id, value)`

#### `def niScope_GetAttributeViInt64(self, vi, channel_list, attribute_id, value)`

#### `def niScope_GetAttributeViReal64(self, vi, channel_list, attribute_id, value)`

#### `def niScope_GetAttributeViString(self, vi, channel_list, attribute_id, buf_size, value)`

#### `def niScope_GetChannelNameFromString(self, vi, indices, buffer_size, names)`

#### `def niScope_GetEqualizationFilterCoefficients(self, vi, channel, number_of_coefficients, coefficients)`

#### `def niScope_GetError(self, vi, error_code, buffer_size, description)`

#### `def niScope_ImportAttributeConfigurationBuffer(self, vi, size_in_bytes, configuration)`

#### `def niScope_ImportAttributeConfigurationFile(self, vi, file_path)`

#### `def niScope_InitWithOptions(self, resource_name, id_query, reset_device, option_string, vi)`

#### `def niScope_InitiateAcquisition(self, vi)`

#### `def niScope_LockSession(self, vi, caller_has_lock)`

#### `def niScope_ProbeCompensationSignalStart(self, vi)`

#### `def niScope_ProbeCompensationSignalStop(self, vi)`

#### `def niScope_Read(self, vi, channel_list, timeout, num_samples, waveform, wfm_info)`

#### `def niScope_ResetDevice(self, vi)`

#### `def niScope_ResetWithDefaults(self, vi)`

#### `def niScope_SendSoftwareTriggerEdge(self, vi, which_trigger)`

#### `def niScope_SetAttributeViBoolean(self, vi, channel_list, attribute_id, value)`

#### `def niScope_SetAttributeViInt32(self, vi, channel_list, attribute_id, value)`

#### `def niScope_SetAttributeViInt64(self, vi, channel_list, attribute_id, value)`

#### `def niScope_SetAttributeViReal64(self, vi, channel_list, attribute_id, value)`

#### `def niScope_SetAttributeViString(self, vi, channel_list, attribute_id, value)`

#### `def niScope_SetRuntimeEnvironment(self, environment, environment_version, reserved1, reserved2)`

#### `def niScope_UnlockSession(self, vi, caller_has_lock)`

#### `def niScope_close(self, vi)`

#### `def niScope_error_message(self, vi, error_code, error_message)`

#### `def niScope_reset(self, vi)`

#### `def niScope_self_test(self, vi, self_test_result, self_test_message)`

#### `def set_side_effects_and_return_values(self, mock_library)`

<!--NI_PYTHON_API repo=nimi-python path=generated/niscope/niscope/unit_tests/test_niscope.py -->
## PYTHON MODULE: generated/niscope/niscope/unit_tests/test_niscope.py

### `def test_populate_samples_info()`

### `def test_populate_channel_and_record_info()`

<!--NI_PYTHON_API repo=nimi-python path=generated/niscope/niscope/waveform_info.py -->
## PYTHON MODULE: generated/niscope/niscope/waveform_info.py

### `class struct_niScope_wfmInfo(ctypes.Structure)`

#### `def __init__(self, data=None, absolute_initial_x=0.0, relative_initial_x=0.0, x_increment=0.0, actual_samples=0, offset=0.0, gain=0.0, reserved1=0.0, reserved2=0.0)`

### `class WaveformInfo()`

#### `def __init__(self, data=None, absolute_initial_x=0.0, relative_initial_x=0.0, x_increment=0.0, offset=0.0, gain=0.0, reserved1=0.0, reserved2=0.0)`

#### `def __repr__(self)`

#### `def __str__(self)`

### `def _populate_samples_info(waveform_infos, sample_data, num_samples_per_waveform)`

Chunk up flat array of sample_data and copy each chunk into individual WaveformInfo instance

    Args:
        waveform_infos (Iterable of WaveformInfo): WaveformInfo class instances

        sample_data (Iterable of float): Waveform sample data

        num_samples_per_waveform (int): Number of samples belonging to each waveform
    

### `def _populate_channel_and_record_info(waveform_infos, channels, records)`

Populate the channel and record attributes of WaveformInfo instances

    Args:
        waveform_infos (Iterable of WaveformInfo): WaveformInfo class instances

        channels (Iterable of str): Channel names

        records (Iterable of int): Record numbers
    

<!--NI_PYTHON_API repo=nimi-python path=generated/niscope/setup.py -->
## PYTHON MODULE: generated/niscope/setup.py

### `def read_contents(file_to_read)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nise/nise/__init__.py -->
## PYTHON MODULE: generated/nise/nise/__init__.py

### `def get_diagnostic_information()`

Get diagnostic information about the system state that is suitable for printing or logging

    returns: dict

    note: Python bitness may be incorrect when running in a virtual environment
    

### `def print_diagnostic_information()`

Print diagnostic information in a format suitable for issue report

    note: Python bitness may be incorrect when running in a virtual environment
    

<!--NI_PYTHON_API repo=nimi-python path=generated/nise/nise/_converters.py -->
## PYTHON MODULE: generated/nise/nise/_converters.py

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
    

<!--NI_PYTHON_API repo=nimi-python path=generated/nise/nise/_library.py -->
## PYTHON MODULE: generated/nise/nise/_library.py

### `class Library(object)`

Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    

#### `def __init__(self, ctypes_library)`

#### `def _get_library_function(self, name)`

#### `def niSE_CloseSession(self, vi)`

#### `def niSE_Connect(self, vi, connect_spec, multiconnect_mode, wait_for_debounce)`

#### `def niSE_ConnectAndDisconnect(self, vi, connect_spec, disconnect_spec, multiconnect_mode, operation_order, wait_for_debounce)`

#### `def niSE_Disconnect(self, vi, disconnect_spec)`

#### `def niSE_DisconnectAll(self, vi)`

#### `def niSE_ExpandRouteSpec(self, vi, route_spec, expand_action, expanded_route_spec, expanded_route_spec_size)`

#### `def niSE_FindRoute(self, vi, channel1, channel2, route_spec, route_spec_size, path_capability)`

#### `def niSE_GetAllConnections(self, vi, route_spec, route_spec_size)`

#### `def niSE_GetError(self, vi, error_number, error_description, error_description_size)`

#### `def niSE_IsConnected(self, vi, route_spec, is_connected)`

#### `def niSE_IsDebounced(self, vi, is_debounced)`

#### `def niSE_OpenSession(self, virtual_device_name, option_string, vi)`

#### `def niSE_WaitForDebounce(self, vi, maximum_time_ms)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nise/nise/_library_interpreter.py -->
## PYTHON MODULE: generated/nise/nise/_library_interpreter.py

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
        

#### `def close_session(self)`

#### `def connect(self, connect_spec, multiconnect_mode, wait_for_debounce)`

#### `def connect_and_disconnect(self, connect_spec, disconnect_spec, multiconnect_mode, operation_order, wait_for_debounce)`

#### `def disconnect(self, disconnect_spec)`

#### `def disconnect_all(self)`

#### `def expand_route_spec(self, route_spec, expand_action, expanded_route_spec_size)`

#### `def find_route(self, channel1, channel2, route_spec_size)`

#### `def get_all_connections(self, route_spec_size)`

#### `def get_error(self, error_description_size)`

#### `def is_connected(self, route_spec)`

#### `def is_debounced(self)`

#### `def open_session(self, virtual_device_name, option_string)`

#### `def wait_for_debounce(self, maximum_time_ms)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nise/nise/_library_singleton.py -->
## PYTHON MODULE: generated/nise/nise/_library_singleton.py

### `def _get_library_name()`

### `def _get_library_type()`

### `def get()`

get

    Returns the library.Library singleton for nise.
    

<!--NI_PYTHON_API repo=nimi-python path=generated/nise/nise/enums.py -->
## PYTHON MODULE: generated/nise/nise/enums.py

### `class ExpandAction(Enum)`

### `class MulticonnectMode(Enum)`

### `class OperationOrder(Enum)`

### `class PathCapability(Enum)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nise/nise/errors.py -->
## PYTHON MODULE: generated/nise/nise/errors.py

### `def _is_success(code)`

### `def _is_error(code)`

### `def _is_warning(code)`

### `class Error(Exception)`

Base error class for NI Switch Executive

#### `def __init__(self, message)`

### `class DriverError(Error)`

An error originating from the NI Switch Executive driver

#### `def __init__(self, code, description)`

### `class DriverWarning(Warning)`

A warning originating from the NI Switch Executive driver

#### `def __init__(self, code, description)`

### `class UnsupportedConfigurationError(Error)`

An error due to using this module in an usupported platform.

#### `def __init__(self)`

### `class DriverNotInstalledError(Error)`

An error due to using this module without the driver runtime installed.

#### `def __init__(self)`

### `class DriverTooOldError(Error)`

An error due to using this module with an older version of the NI Switch Executive driver runtime.

#### `def __init__(self)`

### `class DriverTooNewError(Error)`

An error due to the NI Switch Executive driver runtime being too new for this module.

#### `def __init__(self)`

### `class InvalidRepeatedCapabilityError(Error)`

An error due to an invalid character in a repeated capability

#### `def __init__(self, invalid_character, invalid_string)`

### `def handle_error(library_interpreter, code, ignore_warnings, is_error_handling)`

handle_error

    Helper function for handling errors returned by nise.Library.
    It calls back into the LibraryInterpreter to get the corresponding error
    description and raises if necessary.
    

<!--NI_PYTHON_API repo=nimi-python path=generated/nise/nise/session.py -->
## PYTHON MODULE: generated/nise/nise/session.py

### `class _SessionBase(object)`

Base class for all NI Switch Executive sessions.

#### `def __init__(self, repeated_capability_list, all_channels_in_session, interpreter, freeze_it=False)`

#### `def __repr__(self)`

#### `def __setattr__(self, key, value)`

### `class Session(_SessionBase)`

An NI Switch Executive session

#### `def __init__(self, virtual_device_name, options={})`

An NI Switch Executive session

        Opens a session to a specified NI Switch Executive virtual device. Opens
        communications with all of the IVI switches associated with the
        specified NI Switch Executive virtual device. Returns a session handle
        that you use to identify the virtual device in all subsequent NI Switch
        Executive method calls. NI Switch Executive uses a reference counting
        scheme to manage open session handles to an NI Switch Executive virtual
        device. Each call to __init__ must be matched with a subsequent
        call to close. Successive calls to __init__ with
        the same virtual device name always returns the same session handle. NI
        Switch Executive disconnects its communication with the IVI switches
        after all session handles are closed to a given virtual device. The
        session handles may be used safely in multiple threads of an
        application. Sessions may only be opened to a given NI Switch Executive
        virtual device from a single process at a time.

        Args:
            virtual_device_name (str): The name of the NI Switch Executive virtual device.

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


        Returns:
            session (nise.Session): A session object representing the device.

        

#### `def __enter__(self)`

#### `def __exit__(self, exc_type, exc_value, traceback)`

#### `def close(self)`

close

        Reduces the reference count of open sessions by one. If the reference
        count goes to 0, the method deallocates any memory resources the
        driver uses and closes any open IVI switch sessions. After calling the
        close method, you should not use the NI Switch Executive
        virtual device again until you call __init__.

        Note:
        This method is not needed when using the session context manager
        

#### `def _close_session(self)`

_close_session

        Reduces the reference count of open sessions by one. If the reference
        count goes to 0, the method deallocates any memory resources the
        driver uses and closes any open IVI switch sessions. After calling the
        close method, you should not use the NI Switch Executive
        virtual device again until you call __init__.
        

#### `def connect(self, connect_spec, multiconnect_mode=enums.MulticonnectMode.DEFAULT, wait_for_debounce=True)`

connect

        Connects the routes specified by the connection specification. When
        connecting, it may allow for multiconnection based on the
        multiconnection mode. In the event of an error, the call to
        connect will attempt to undo any connections made so that the
        system will be left in the same state that it was in before the call was
        made. Some errors can be caught before manipulating hardware, although
        it is feasible that a hardware call could fail causing some connections
        to be momentarily closed and then reopened. If the wait for debounce
        parameter is set, the method will not return until the switch system
        has debounced.

        Args:
            connect_spec (str): String describing the connections to be made. The route specification
                strings are best summarized as a series of routes delimited by
                ampersands. The specified routes may be route names, route group names,
                or fully specified route paths delimited by square brackets. Some
                examples of route specification strings are: MyRoute MyRouteGroup
                MyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute & MyRouteGroup &
                [A->Switch1/r0->B] Refer to Route Specification Strings in the NI Switch
                Executive Help for more information.

            multiconnect_mode (enums.MulticonnectMode): This value sets the connection mode for the method. The mode might be
                one of the following: NISE_VAL_USE_DEFAULT_MODE (-1) - uses the mode
                selected as the default for the route in the NI Switch Executive virtual
                device configuration. If a mode has not been selected for the route in
                the NI Switch Executive virtual device, this parameter defaults to
                NISE_VAL_MULTICONNECT_ROUTES. MulticonnectMode.NO_MULTICONNECT (0) -
                routes specified in the connection specification must be disconnected
                before they can be reconnected. Calling Connect on a route that was
                connected using No Multiconnect mode results in an error condition.
                NISE_VAL_MULTICONNECT_ROUTES (1)- routes specified in the connection
                specification can be connected multiple times. The first call to Connect
                performs the physical hardware connection. Successive calls to Connect
                increase a connection reference count. Similarly, calls to Disconnect
                decrease the reference count. Once it reaches 0, the hardware is
                physically disconnected. Multiconnecting routes applies to entire routes
                and not to route segments.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            wait_for_debounce (bool): Waits (if true) for switches to debounce between its connect and
                disconnect operations. If false, it immediately begins the second
                operation after completing the first. The order of connect and
                disconnect operation is set by the Operation Order input.

        

#### `def connect_and_disconnect(self, connect_spec, disconnect_spec, multiconnect_mode=enums.MulticonnectMode.DEFAULT, operation_order=enums.OperationOrder.AFTER, wait_for_debounce=True)`

connect_and_disconnect

        Connects routes and disconnects routes in a similar fashion to
        connect and disconnect except that the operations happen in
        the context of a single method call. This method is useful for
        switching from one state to another state. connect_and_disconnect
        manipulates the hardware connections and disconnections only when the
        routes are different between the connection and disconnection
        specifications. If any routes are common between the connection and
        disconnection specifications, NI Switch Executive determines whether or
        not the relays need to be switched. This functionality has the distinct
        advantage of increased throughput for shared connections, because
        hardware does not have to be involved and potentially increases relay
        lifetime by decreasing the number of times that the relay has to be
        switched. In the event of an error, the call to
        connect_and_disconnect attempts to undo any connections made, but
        does not attempt to reconnect disconnections. Some errors can be caught
        before manipulating hardware, although it is feasible that a hardware
        call could fail causing some connections to be momentarily closed and
        then reopened.

        Args:
            connect_spec (str): String describing the connections to be made. The route specification
                strings are best summarized as a series of routes delimited by
                ampersands. The specified routes may be route names, route group names,
                or fully specified route paths delimited by square brackets. Some
                examples of route specification strings are: MyRoute MyRouteGroup
                MyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute & MyRouteGroup &
                [A->Switch1/r0->B] Refer to Route Specification Strings in the NI Switch
                Executive Help for more information.

            disconnect_spec (str): String describing the disconnections to be made. The route specification
                strings are best summarized as a series of routes delimited by
                ampersands. The specified routes may be route names, route group names,
                or fully specified route paths delimited by square brackets. Some
                examples of route specification strings are: MyRoute MyRouteGroup
                MyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute & MyRouteGroup &
                [A->Switch1/r0->B] Refer to Route Specification Strings in the NI Switch
                Executive Help for more information.

            multiconnect_mode (enums.MulticonnectMode): This value sets the connection mode for the method. The mode might be
                one of the following: NISE_VAL_USE_DEFAULT_MODE (-1) - uses the mode
                selected as the default for the route in the NI Switch Executive virtual
                device configuration. If a mode has not been selected for the route in
                the NI Switch Executive virtual device, this parameter defaults to
                NISE_VAL_MULTICONNECT_ROUTES. MulticonnectMode.NO_MULTICONNECT (0) -
                routes specified in the connection specification must be disconnected
                before they can be reconnected. Calling Connect on a route that was
                connected using No Multiconnect mode results in an error condition.
                NISE_VAL_MULTICONNECT_ROUTES (1) - routes specified in the connection
                specification can be connected multiple times. The first call to Connect
                performs the physical hardware connection. Successive calls to Connect
                increase a connection reference count. Similarly, calls to Disconnect
                decrease the reference count. Once it reaches 0, the hardware is
                physically disconnected. This behavior is slightly different with SPDT
                relays. For more information, refer to the Exclusions and SPDT Relays
                topic in the NI Switch Executive Help. Multiconnecting routes applies to
                entire routes and not to route segments.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            operation_order (enums.OperationOrder): Sets the order of the operation for the method. Defined values are
                Break Before Make and Break After Make. OperationOrder.BEFORE
                (1) - The method disconnects the routes specified in the disconnect
                specification before connecting the routes specified in the connect
                specification. This is the typical mode of operation.
                OperationOrder.AFTER (2) - The method connects the routes
                specified in the connection specification before connecting the routes
                specified in the disconnection specification. This mode of operation is
                normally used when you are switching current and want to ensure that a
                load is always connected to your source. The order of operation is to
                connect first or disconnect first.

            wait_for_debounce (bool): Waits (if true) for switches to debounce between its connect and
                disconnect operations. If false, it immediately begins the second
                operation after completing the first. The order of connect and
                disconnect operation is set by the Operation Order input.

        

#### `def disconnect(self, disconnect_spec)`

disconnect

        Disconnects the routes specified in the Disconnection Specification. If
        any of the specified routes were originally connected in a
        multiconnected mode, the call to disconnect reduces the reference
        count on the route by 1. If the reference count reaches 0, it is
        disconnected. If a specified route does not exist, it is an error
        condition. In the event of an error, the call to disconnect
        continues to try to disconnect everything specified by the route
        specification string but reports the error on completion.

        Args:
            disconnect_spec (str): String describing the disconnections to be made. The route specification
                strings are best summarized as a series of routes delimited by
                ampersands. The specified routes may be route names, route group names,
                or fully specified route paths delimited by square brackets. Some
                examples of route specification strings are: MyRoute MyRouteGroup
                MyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute & MyRouteGroup &
                [A->Switch1/r0->B] Refer to Route Specification Strings in the NI Switch
                Executive Help for more information.

        

#### `def disconnect_all(self)`

disconnect_all

        Disconnects all connections on every IVI switch device managed by the
        NISE session reference passed to this method. disconnect_all
        ignores all multiconnect modes. Calling disconnect_all resets all
        of the switch states for the system.
        

#### `def expand_route_spec(self, route_spec, expand_action=enums.ExpandAction.ROUTES, expanded_route_spec_size=[1024])`

expand_route_spec

        Expands a route spec string to yield more information about the routes
        and route groups within the spec. The route specification string
        returned from expand_route_spec can be passed to other Switch
        Executive API methods (such as connect, disconnect, and
        connect_and_disconnect) that use route specification strings.

        Args:
            route_spec (str): String describing the routes and route groups to expand. The route
                specification strings are best summarized as a series of routes
                delimited by ampersands. The specified routes may be route names, route
                group names, or fully specified route paths delimited by square
                brackets. Some examples of route specification strings are: MyRoute
                MyRouteGroup MyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute &
                MyRouteGroup & [A->Switch1/r0->B] Refer to Route Specification Strings
                in the NI Switch Executive Help for more information.

            expand_action (enums.ExpandAction): This value sets the expand action for the method. The action might be
                one of the following: ExpandAction.ROUTES (0) - expands the
                route spec to routes. Converts route groups to their constituent routes.
                ExpandAction.PATHS (1) - expands the route spec to paths.
                Converts routes and route groups to their constituent square bracket
                route spec strings. Example: [Dev1/c0->Dev1/r0->Dev1/c1]

            expanded_route_spec_size (list of int): The routeSpecSize is an ViInt32 that is passed by reference into the
                method. As an input, it is the size of the route spec string buffer
                being passed. If the route spec string is larger than the string buffer
                being passed, only the portion of the route spec string that can fit in
                the string buffer is copied into it. On return from the method,
                routeSpecSize holds the size required to hold the entire route spec
                string. Note that this size may be larger than the buffer size as the
                method always returns the size needed to hold the entire buffer. You
                may pass NULL for this parameter if you are not interested in the return
                value for routeSpecSize and routeSpec.


        Returns:
            expanded_route_spec (str): The expanded route spec. Route specification strings can be directly
                passed to connect, disconnect, or connect_and_disconnect
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

        

#### `def find_route(self, channel1, channel2, route_spec_size=[1024])`

find_route

        Finds an existing or potential route between channel 1 and channel 2.
        The returned route specification contains the route specification and
        the route capability determines whether or not the route existed, is
        possible, or is not possible for various reasons. The route
        specification string returned from find_route can be passed to
        other Switch Executive API methods (such as connect,
        disconnect, and connect_and_disconnect) that use route
        specification strings.

        Args:
            channel1 (str): Channel name of one of the endpoints of the route to find. The channel
                name must either be a channel alias name or a name in the
                device/ivichannel syntax. Examples: MyChannel Switch1/R0

            channel2 (str): Channel name of one of the endpoints of the route to find. The channel
                name must either be a channel alias name or a name in the
                device/ivichannel syntax. Examples: MyChannel Switch1/R0

            route_spec_size (list of int): The routeSpecSize is an ViInt32 that is passed by reference into the
                method. As an input, it is the size of the route string buffer being
                passed. If the route string is larger than the string buffer being
                passed, only the portion of the route string that can fit in the string
                buffer is copied into it. On return from the method, routeSpecSize
                holds the size required to hold the entire route string. Note that this
                size may be larger than the buffer size as the method always returns
                the size needed to hold the entire buffer. You may pass NULL for this
                parameter if you are not interested in the return value for
                routeSpecSize and routeSpec.


        Returns:
            route_spec (str): The fully specified route path complete with delimiting square
                brackets if the route exists or is possible. An example of a fully
                specified route string is: [A->Switch1/r0->B] Route specification
                strings can be directly passed to connect, disconnect, or
                connect_and_disconnect Refer to Route Specification Strings in the
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

            path_capability (enums.PathCapability): The return value which expresses the capability of finding a valid route
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

        

#### `def get_all_connections(self, route_spec_size=[1024])`

get_all_connections

        Returns the top-level connected routes and route groups. The route
        specification string returned from get_all_connections can be passed
        to other Switch Executive API methods (such as connect,
        disconnect, connect_and_disconnect, and expand_route_spec)
        that use route specification strings.

        Args:
            route_spec_size (list of int): The routeSpecSize is an ViInt32 that is passed by reference into the
                method. As an input, it is the size of the route spec string buffer
                being passed. If the route spec string is larger than the string buffer
                being passed, only the portion of the route spec string that can fit in
                the string buffer is copied into it. On return from the method,
                routeSpecSize holds the size required to hold the entire route spec
                string. Note that this size may be larger than the buffer size as the
                method always returns the size needed to hold the entire buffer. You
                may pass NULL for this parameter if you are not interested in the return
                value for routeSpecSize and routeSpec.


        Returns:
            route_spec (str): The route spec of all currently connected routes and route groups. Route
                specification strings can be directly passed to connect,
                disconnect, connect_and_disconnect, or expand_route_spec
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

        

#### `def is_connected(self, route_spec)`

is_connected

        Checks whether the specified routes and routes groups are connected. It
        returns true if connected.

        Args:
            route_spec (str): String describing the connections to check. The route specification
                strings are best summarized as a series of routes delimited by
                ampersands. The specified routes may be route names, route group names,
                or fully specified route paths delimited by square brackets. Some
                examples of route specification strings are: MyRoute MyRouteGroup
                MyRoute & MyRouteGroup [A->Switch1/r0->B] MyRoute & MyRouteGroup &
                [A->Switch1/r0->B] Refer to Route Specification Strings in the NI Switch
                Executive Help for more information.


        Returns:
            is_connected (bool): Returns TRUE if the routes and routes groups are connected or FALSE if
                they are not.

        

#### `def is_debounced(self)`

is_debounced

        Checks to see if the switching system is debounced or not. This method
        does not wait for debouncing to occur. It returns true if the system is
        fully debounced. This method is similar to the IviSwtch specific
        method.

        Returns:
            is_debounced (bool): Returns TRUE if the system is fully debounced or FALSE if it is still
                settling.

        

#### `def _open_session(self, virtual_device_name, option_string='')`

_open_session

        Opens a session to a specified NI Switch Executive virtual device. Opens
        communications with all of the IVI switches associated with the
        specified NI Switch Executive virtual device. Returns a session handle
        that you use to identify the virtual device in all subsequent NI Switch
        Executive method calls. NI Switch Executive uses a reference counting
        scheme to manage open session handles to an NI Switch Executive virtual
        device. Each call to __init__ must be matched with a subsequent
        call to close. Successive calls to __init__ with
        the same virtual device name always returns the same session handle. NI
        Switch Executive disconnects its communication with the IVI switches
        after all session handles are closed to a given virtual device. The
        session handles may be used safely in multiple threads of an
        application. Sessions may only be opened to a given NI Switch Executive
        virtual device from a single process at a time.

        Args:
            virtual_device_name (str): The name of the NI Switch Executive virtual device.

            option_string (dict): The option string can be used to pass information to each of the IVI
                devices on startup. It can be used to set things such as simulation,
                range checking, etc. Consult your driver documentation for more
                information about valid entries for the option string.


        Returns:
            vi (int): The session referencing this NI Switch Executive virtual device session.

        

#### `def wait_for_debounce(self, maximum_time_ms=hightime.timedelta(milliseconds=-1))`

wait_for_debounce

        Waits for all of the switches in the NI Switch Executive virtual device
        to debounce. This method does not return until either the switching
        system is completely debounced and settled or the maximum time has
        elapsed and the system is not yet debounced. In the event that the
        maximum time elapses, the method returns an error indicating that a
        timeout has occurred. To ensure that all of the switches have settled,
        NI recommends calling wait_for_debounce after a series of connection
        or disconnection operations and before taking any measurements of the
        signals connected to the switching system.

        Args:
            maximum_time_ms (hightime.timedelta, datetime.timedelta, or int in milliseconds): The amount of time to wait (in milliseconds) for the debounce to
                complete. A value of 0 checks for debouncing once and returns an error
                if the system is not debounced at that time. A value of -1 means to
                block for an infinite period of time until the system is debounced.

        

<!--NI_PYTHON_API repo=nimi-python path=generated/nise/nise/unit_tests/_matchers.py -->
## PYTHON MODULE: generated/nise/nise/unit_tests/_matchers.py

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

<!--NI_PYTHON_API repo=nimi-python path=generated/nise/nise/unit_tests/_mock_helper.py -->
## PYTHON MODULE: generated/nise/nise/unit_tests/_mock_helper.py

### `class MockFunctionCallError(Exception)`

#### `def __init__(self, function, param=None)`

### `class SideEffectsHelper(object)`

#### `def __init__(self)`

#### `def __getitem__(self, func)`

#### `def __setitem__(self, func, val)`

#### `def niSE_CloseSession(self, vi)`

#### `def niSE_Connect(self, vi, connect_spec, multiconnect_mode, wait_for_debounce)`

#### `def niSE_ConnectAndDisconnect(self, vi, connect_spec, disconnect_spec, multiconnect_mode, operation_order, wait_for_debounce)`

#### `def niSE_Disconnect(self, vi, disconnect_spec)`

#### `def niSE_DisconnectAll(self, vi)`

#### `def niSE_ExpandRouteSpec(self, vi, route_spec, expand_action, expanded_route_spec, expanded_route_spec_size)`

#### `def niSE_FindRoute(self, vi, channel1, channel2, route_spec, route_spec_size, path_capability)`

#### `def niSE_GetAllConnections(self, vi, route_spec, route_spec_size)`

#### `def niSE_GetError(self, vi, error_number, error_description, error_description_size)`

#### `def niSE_IsConnected(self, vi, route_spec, is_connected)`

#### `def niSE_IsDebounced(self, vi, is_debounced)`

#### `def niSE_OpenSession(self, virtual_device_name, option_string, vi)`

#### `def niSE_WaitForDebounce(self, vi, maximum_time_ms)`

#### `def set_side_effects_and_return_values(self, mock_library)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nise/setup.py -->
## PYTHON MODULE: generated/nise/setup.py

### `def read_contents(file_to_read)`

<!--NI_PYTHON_API repo=nimi-python path=generated/niswitch/niswitch/__init__.py -->
## PYTHON MODULE: generated/niswitch/niswitch/__init__.py

### `def get_diagnostic_information()`

Get diagnostic information about the system state that is suitable for printing or logging

    returns: dict

    note: Python bitness may be incorrect when running in a virtual environment
    

### `def print_diagnostic_information()`

Print diagnostic information in a format suitable for issue report

    note: Python bitness may be incorrect when running in a virtual environment
    

<!--NI_PYTHON_API repo=nimi-python path=generated/niswitch/niswitch/_attributes.py -->
## PYTHON MODULE: generated/niswitch/niswitch/_attributes.py

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

Class for attributes that use enums internally but are exposed in the niswitch Python module as something else, thus need conversion.

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

<!--NI_PYTHON_API repo=nimi-python path=generated/niswitch/niswitch/_converters.py -->
## PYTHON MODULE: generated/niswitch/niswitch/_converters.py

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
    

<!--NI_PYTHON_API repo=nimi-python path=generated/niswitch/niswitch/_grpc_stub_interpreter.py -->
## PYTHON MODULE: generated/niswitch/niswitch/_grpc_stub_interpreter.py

### `class GrpcStubInterpreter(object)`

Interpreter for interacting with a gRPC Stub class

#### `def __init__(self, grpc_options)`

#### `def set_session_handle(self, value=session_grpc_types.Session())`

#### `def get_session_handle(self)`

#### `def _invoke(self, func, request, metadata=None)`

#### `def abort(self)`

#### `def can_connect(self, channel1, channel2)`

#### `def commit(self)`

#### `def connect(self, channel1, channel2)`

#### `def connect_multiple(self, connection_list)`

#### `def disable(self)`

#### `def disconnect(self, channel1, channel2)`

#### `def disconnect_all(self)`

#### `def disconnect_multiple(self, disconnection_list)`

#### `def get_attribute_vi_boolean(self, channel_name, attribute_id)`

#### `def get_attribute_vi_int32(self, channel_name, attribute_id)`

#### `def get_attribute_vi_real64(self, channel_name, attribute_id)`

#### `def get_attribute_vi_string(self, channel_name, attribute_id)`

#### `def get_channel_name(self, index)`

#### `def get_error(self)`

#### `def get_path(self, channel1, channel2)`

#### `def get_relay_count(self, relay_name)`

#### `def get_relay_name(self, index)`

#### `def get_relay_position(self, relay_name)`

#### `def init_with_topology(self, resource_name, topology, simulate, reset_device)`

#### `def initiate_scan(self)`

#### `def lock(self)`

#### `def relay_control(self, relay_name, relay_action)`

#### `def reset_with_defaults(self)`

#### `def route_scan_advanced_output(self, scan_advanced_output_connector, scan_advanced_output_bus_line, invert)`

#### `def route_trigger_input(self, trigger_input_connector, trigger_input_bus_line, invert)`

#### `def send_software_trigger(self)`

#### `def set_attribute_vi_boolean(self, channel_name, attribute_id, attribute_value)`

#### `def set_attribute_vi_int32(self, channel_name, attribute_id, attribute_value)`

#### `def set_attribute_vi_real64(self, channel_name, attribute_id, attribute_value)`

#### `def set_attribute_vi_string(self, channel_name, attribute_id, attribute_value)`

#### `def set_path(self, path_list)`

#### `def set_runtime_environment(self, environment, environment_version, reserved1, reserved2)`

#### `def unlock(self)`

#### `def wait_for_debounce(self, maximum_time_ms)`

#### `def wait_for_scan_complete(self, maximum_time_ms)`

#### `def close(self)`

#### `def error_message(self, error_code)`

#### `def reset(self)`

#### `def self_test(self)`

<!--NI_PYTHON_API repo=nimi-python path=generated/niswitch/niswitch/_library.py -->
## PYTHON MODULE: generated/niswitch/niswitch/_library.py

### `class Library(object)`

Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    

#### `def __init__(self, ctypes_library)`

#### `def _get_library_function(self, name)`

#### `def niSwitch_AbortScan(self, vi)`

#### `def niSwitch_CanConnect(self, vi, channel1, channel2, path_capability)`

#### `def niSwitch_Commit(self, vi)`

#### `def niSwitch_Connect(self, vi, channel1, channel2)`

#### `def niSwitch_ConnectMultiple(self, vi, connection_list)`

#### `def niSwitch_Disable(self, vi)`

#### `def niSwitch_Disconnect(self, vi, channel1, channel2)`

#### `def niSwitch_DisconnectAll(self, vi)`

#### `def niSwitch_DisconnectMultiple(self, vi, disconnection_list)`

#### `def niSwitch_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niSwitch_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niSwitch_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niSwitch_GetAttributeViString(self, vi, channel_name, attribute_id, array_size, attribute_value)`

#### `def niSwitch_GetChannelName(self, vi, index, buffer_size, channel_name_buffer)`

#### `def niSwitch_GetError(self, vi, error_code, buffer_size, description)`

#### `def niSwitch_GetPath(self, vi, channel1, channel2, buffer_size, path)`

#### `def niSwitch_GetRelayCount(self, vi, relay_name, relay_count)`

#### `def niSwitch_GetRelayName(self, vi, index, relay_name_buffer_size, relay_name_buffer)`

#### `def niSwitch_GetRelayPosition(self, vi, relay_name, relay_position)`

#### `def niSwitch_InitWithTopology(self, resource_name, topology, simulate, reset_device, vi)`

#### `def niSwitch_InitiateScan(self, vi)`

#### `def niSwitch_LockSession(self, vi, caller_has_lock)`

#### `def niSwitch_RelayControl(self, vi, relay_name, relay_action)`

#### `def niSwitch_ResetWithDefaults(self, vi)`

#### `def niSwitch_RouteScanAdvancedOutput(self, vi, scan_advanced_output_connector, scan_advanced_output_bus_line, invert)`

#### `def niSwitch_RouteTriggerInput(self, vi, trigger_input_connector, trigger_input_bus_line, invert)`

#### `def niSwitch_SendSoftwareTrigger(self, vi)`

#### `def niSwitch_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niSwitch_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niSwitch_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niSwitch_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niSwitch_SetPath(self, vi, path_list)`

#### `def niSwitch_SetRuntimeEnvironment(self, environment, environment_version, reserved1, reserved2)`

#### `def niSwitch_UnlockSession(self, vi, caller_has_lock)`

#### `def niSwitch_WaitForDebounce(self, vi, maximum_time_ms)`

#### `def niSwitch_WaitForScanComplete(self, vi, maximum_time_ms)`

#### `def niSwitch_close(self, vi)`

#### `def niSwitch_error_message(self, vi, error_code, error_message)`

#### `def niSwitch_reset(self, vi)`

#### `def niSwitch_self_test(self, vi, self_test_result, self_test_message)`

<!--NI_PYTHON_API repo=nimi-python path=generated/niswitch/niswitch/_library_interpreter.py -->
## PYTHON MODULE: generated/niswitch/niswitch/_library_interpreter.py

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

#### `def can_connect(self, channel1, channel2)`

#### `def commit(self)`

#### `def connect(self, channel1, channel2)`

#### `def connect_multiple(self, connection_list)`

#### `def disable(self)`

#### `def disconnect(self, channel1, channel2)`

#### `def disconnect_all(self)`

#### `def disconnect_multiple(self, disconnection_list)`

#### `def get_attribute_vi_boolean(self, channel_name, attribute_id)`

#### `def get_attribute_vi_int32(self, channel_name, attribute_id)`

#### `def get_attribute_vi_real64(self, channel_name, attribute_id)`

#### `def get_attribute_vi_string(self, channel_name, attribute_id)`

#### `def get_channel_name(self, index)`

#### `def get_error(self)`

#### `def get_path(self, channel1, channel2)`

#### `def get_relay_count(self, relay_name)`

#### `def get_relay_name(self, index)`

#### `def get_relay_position(self, relay_name)`

#### `def init_with_topology(self, resource_name, topology, simulate, reset_device)`

#### `def initiate_scan(self)`

#### `def lock(self)`

#### `def relay_control(self, relay_name, relay_action)`

#### `def reset_with_defaults(self)`

#### `def route_scan_advanced_output(self, scan_advanced_output_connector, scan_advanced_output_bus_line, invert)`

#### `def route_trigger_input(self, trigger_input_connector, trigger_input_bus_line, invert)`

#### `def send_software_trigger(self)`

#### `def set_attribute_vi_boolean(self, channel_name, attribute_id, attribute_value)`

#### `def set_attribute_vi_int32(self, channel_name, attribute_id, attribute_value)`

#### `def set_attribute_vi_real64(self, channel_name, attribute_id, attribute_value)`

#### `def set_attribute_vi_string(self, channel_name, attribute_id, attribute_value)`

#### `def set_path(self, path_list)`

#### `def set_runtime_environment(self, environment, environment_version, reserved1, reserved2)`

#### `def unlock(self)`

#### `def wait_for_debounce(self, maximum_time_ms)`

#### `def wait_for_scan_complete(self, maximum_time_ms)`

#### `def close(self)`

#### `def error_message(self, error_code)`

#### `def reset(self)`

#### `def self_test(self)`

<!--NI_PYTHON_API repo=nimi-python path=generated/niswitch/niswitch/_library_singleton.py -->
## PYTHON MODULE: generated/niswitch/niswitch/_library_singleton.py

### `def _get_library_name()`

### `def _get_library_type()`

### `def get()`

get

    Returns the library.Library singleton for niswitch.
    

<!--NI_PYTHON_API repo=nimi-python path=generated/niswitch/niswitch/enums.py -->
## PYTHON MODULE: generated/niswitch/niswitch/enums.py

### `class HandshakingInitiation(Enum)`

### `class PathCapability(Enum)`

### `class RelayAction(Enum)`

### `class RelayPosition(Enum)`

### `class ScanAdvancedOutput(Enum)`

### `class ScanAdvancedPolarity(Enum)`

### `class ScanMode(Enum)`

### `class TriggerInput(Enum)`

### `class TriggerInputPolarity(Enum)`

<!--NI_PYTHON_API repo=nimi-python path=generated/niswitch/niswitch/errors.py -->
## PYTHON MODULE: generated/niswitch/niswitch/errors.py

### `def _is_success(code)`

### `def _is_error(code)`

### `def _is_warning(code)`

### `class Error(Exception)`

Base error class for NI-SWITCH

#### `def __init__(self, message)`

### `class DriverError(Error)`

An error originating from the NI-SWITCH driver

#### `def __init__(self, code, description)`

### `class DriverWarning(Warning)`

A warning originating from the NI-SWITCH driver

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

An error due to using this module with an older version of the NI-SWITCH driver runtime.

#### `def __init__(self)`

### `class DriverTooNewError(Error)`

An error due to the NI-SWITCH driver runtime being too new for this module.

#### `def __init__(self)`

### `class InvalidRepeatedCapabilityError(Error)`

An error due to an invalid character in a repeated capability

#### `def __init__(self, invalid_character, invalid_string)`

### `class SelfTestError(Error)`

An error due to a failed self-test

#### `def __init__(self, code, msg)`

### `def handle_error(library_interpreter, code, ignore_warnings, is_error_handling)`

handle_error

    Helper function for handling errors returned by niswitch.Library.
    It calls back into the LibraryInterpreter to get the corresponding error
    description and raises if necessary.
    

<!--NI_PYTHON_API repo=nimi-python path=generated/niswitch/niswitch/grpc_session_options.py -->
## PYTHON MODULE: generated/niswitch/niswitch/grpc_session_options.py

- `GRPC_SERVICE_INTERFACE_NAME = 'niswitch_grpc.NiSwitch'`

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
        

<!--NI_PYTHON_API repo=nimi-python path=generated/niswitch/niswitch/nidevice_pb2.py -->
## PYTHON MODULE: generated/niswitch/niswitch/nidevice_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0enidevice.proto\x12\rnidevice_grpc"2\n\x0fNIComplexNumber\x12\x0c\n\x04real\x18\x01 \x01(\x01\x12\x11\n\timaginary\x18\x02 \x01(\x01"5\n\x12NIComplexNumberF32\x12\x0c\n\x04real\x18\x01 \x01(\x02\x12\x11\n\timaginary\x18\x02 \x01(\x02"/\n\x0cNIComplexI16\x12\x0c\n\x04real\x18\x01 \x01(\x11\x12\x11\n\timaginary\x18\x02 \x01(\x11"r\n\x0fSmtSpectrumInfo\x12\x15\n\rspectrum_type\x18\x01 \x01(\r\x12\x11\n\tlinear_db\x18\x02 \x01(\r\x12\x0e\n\x06window\x18\x03 \x01(\r\x12\x13\n\x0bwindow_size\x18\x04 \x01(\x11\x12\x10\n\x08fft_size\x18\x05 \x01(\x11BB\n\x12com.ni.grpc.deviceB\x08NiDeviceP\x01\xaa\x02\x1fNationalInstruments.Grpc.Deviceb\x06proto3')`

<!--NI_PYTHON_API repo=nimi-python path=generated/niswitch/niswitch/nidevice_pb2_grpc.py -->
## PYTHON MODULE: generated/niswitch/niswitch/nidevice_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

<!--NI_PYTHON_API repo=nimi-python path=generated/niswitch/niswitch/niswitch_pb2.py -->
## PYTHON MODULE: generated/niswitch/niswitch/niswitch_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eniswitch.proto\x12\rniswitch_grpc\x1a\rsession.proto"\xb1\x01\n\x0bInitRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\x10\n\x08id_query\x18\x03 \x01(\x08\x12\x14\n\x0creset_device\x18\x04 \x01(\x08\x12M\n\x17initialization_behavior\x18\x05 \x01(\x0e2,.nidevice_grpc.SessionInitializationBehavior"~\n\x0cInitResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12"\n\x02vi\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x19\n\rerror_message\x18\x03 \x01(\tB\x02\x18\x01\x12\x1f\n\x17new_session_initialized\x18\x04 \x01(\x08"\xd3\x01\n\x16InitWithOptionsRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\x10\n\x08id_query\x18\x03 \x01(\x08\x12\x14\n\x0creset_device\x18\x04 \x01(\x08\x12\x15\n\roption_string\x18\x05 \x01(\t\x12M\n\x17initialization_behavior\x18\x06 \x01(\x0e2,.nidevice_grpc.SessionInitializationBehavior"\x89\x01\n\x17InitWithOptionsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12"\n\x02vi\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x19\n\rerror_message\x18\x03 \x01(\tB\x02\x18\x01\x12\x1f\n\x17new_session_initialized\x18\x04 \x01(\x08"\xcf\x01\n\x17InitWithTopologyRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\x10\n\x08topology\x18\x03 \x01(\t\x12\x10\n\x08simulate\x18\x04 \x01(\x08\x12\x14\n\x0creset_device\x18\x05 \x01(\x08\x12M\n\x17initialization_behavior\x18\x06 \x01(\x0e2,.nidevice_grpc.SessionInitializationBehavior"\x8a\x01\n\x18InitWithTopologyResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12"\n\x02vi\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x19\n\rerror_message\x18\x03 \x01(\tB\x02\x18\x01\x12\x1f\n\x17new_session_initialized\x18\x04 \x01(\x08"2\n\x0cCloseRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\x1f\n\rCloseResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"X\n\x0eConnectRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x10\n\x08channel1\x18\x02 \x01(\t\x12\x10\n\x08channel2\x18\x03 \x01(\t"!\n\x0fConnectResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"U\n\x16ConnectMultipleRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x17\n\x0fconnection_list\x18\x02 \x01(\t")\n\x17ConnectMultipleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"[\n\x11DisconnectRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x10\n\x08channel1\x18\x02 \x01(\t\x12\x10\n\x08channel2\x18\x03 \x01(\t"$\n\x12DisconnectResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"[\n\x19DisconnectMultipleRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12disconnection_list\x18\x02 \x01(\t",\n\x1aDisconnectMultipleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05":\n\x14DisconnectAllRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\'\n\x15DisconnectAllResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"X\n\x0eGetPathRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x10\n\x08channel1\x18\x02 \x01(\t\x12\x10\n\x08channel2\x18\x03 \x01(\t"/\n\x0fGetPathResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04path\x18\x02 \x01(\t"G\n\x0eSetPathRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tpath_list\x18\x02 \x01(\t"!\n\x0fSetPathResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"[\n\x11CanConnectRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x10\n\x08channel1\x18\x02 \x01(\t\x12\x10\n\x08channel2\x18\x03 \x01(\t"y\n\x12CanConnectResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x126\n\x0fpath_capability\x18\x02 \x01(\x0e2\x1d.niswitch_grpc.PathCapability\x12\x1b\n\x13path_capability_raw\x18\x03 \x01(\x11"8\n\x12IsDebouncedRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session";\n\x13IsDebouncedResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x14\n\x0cis_debounced\x18\x02 \x01(\x08"U\n\x16WaitForDebounceRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x17\n\x0fmaximum_time_ms\x18\x02 \x01(\x11")\n\x17WaitForDebounceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xad\x01\n\x0bScanRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tscan_list\x18\x02 \x01(\t\x12:\n\ninitiation\x18\x03 \x01(\x0e2$.niswitch_grpc.HandshakingInitiationH\x00\x12\x18\n\x0einitiation_raw\x18\x04 \x01(\x11H\x00B\x11\n\x0finitiation_enum"\x1e\n\x0cScanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"9\n\x13InitiateScanRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"&\n\x14InitiateScanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"6\n\x10AbortScanRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"#\n\x11AbortScanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"7\n\x11IsScanningRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"9\n\x12IsScanningResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0bis_scanning\x18\x02 \x01(\x08"Y\n\x1aWaitForScanCompleteRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x17\n\x0fmaximum_time_ms\x18\x02 \x01(\x11"-\n\x1bWaitForScanCompleteResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"@\n\x1aSendSoftwareTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"-\n\x1bSendSoftwareTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xaa\x01\n\x18ConfigureScanListRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tscan_list\x18\x02 \x01(\t\x12,\n\tscan_mode\x18\x03 \x01(\x0e2\x17.niswitch_grpc.ScanModeH\x00\x12\x17\n\rscan_mode_raw\x18\x04 \x01(\x11H\x00B\x10\n\x0escan_mode_enum"+\n\x19ConfigureScanListResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xc2\x02\n\x1bConfigureScanTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x12\n\nscan_delay\x18\x02 \x01(\x01\x124\n\rtrigger_input\x18\x03 \x01(\x0e2\x1b.niswitch_grpc.TriggerInputH\x00\x12\x1b\n\x11trigger_input_raw\x18\x04 \x01(\x11H\x00\x12A\n\x14scan_advanced_output\x18\x05 \x01(\x0e2!.niswitch_grpc.ScanAdvancedOutputH\x01\x12"\n\x18scan_advanced_output_raw\x18\x06 \x01(\x11H\x01B\x14\n\x12trigger_input_enumB\x1b\n\x19scan_advanced_output_enum".\n\x1cConfigureScanTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"W\n\x18SetContinuousScanRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x17\n\x0fcontinuous_scan\x18\x02 \x01(\x08"+\n\x19SetContinuousScanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xd9\x02\n\x18RouteTriggerInputRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12>\n\x17trigger_input_connector\x18\x02 \x01(\x0e2\x1b.niswitch_grpc.TriggerInputH\x00\x12%\n\x1btrigger_input_connector_raw\x18\x03 \x01(\x11H\x00\x12=\n\x16trigger_input_bus_line\x18\x04 \x01(\x0e2\x1b.niswitch_grpc.TriggerInputH\x01\x12$\n\x1atrigger_input_bus_line_raw\x18\x05 \x01(\x11H\x01\x12\x0e\n\x06invert\x18\x06 \x01(\x08B\x1e\n\x1ctrigger_input_connector_enumB\x1d\n\x1btrigger_input_bus_line_enum"+\n\x19RouteTriggerInputResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x95\x03\n\x1eRouteScanAdvancedOutputRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12K\n\x1escan_advanced_output_connector\x18\x02 \x01(\x0e2!.niswitch_grpc.ScanAdvancedOutputH\x00\x12,\n"scan_advanced_output_connector_raw\x18\x03 \x01(\x11H\x00\x12J\n\x1dscan_advanced_output_bus_line\x18\x04 \x01(\x0e2!.niswitch_grpc.ScanAdvancedOutputH\x01\x12+\n!scan_advanced_output_bus_line_raw\x18\x05 \x01(\x11H\x01\x12\x0e\n\x06invert\x18\x06 \x01(\x08B%\n#scan_advanced_output_connector_enumB$\n"scan_advanced_output_bus_line_enum"1\n\x1fRouteScanAdvancedOutputResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"7\n\x11ErrorQueryRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"O\n\x12ErrorQueryResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nerror_code\x18\x02 \x01(\x11\x12\x15\n\rerror_message\x18\x03 \x01(\t"5\n\x0fGetErrorRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"E\n\x10GetErrorResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04code\x18\x02 \x01(\x11\x12\x13\n\x0bdescription\x18\x03 \x01(\t"7\n\x11ClearErrorRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"$\n\x12ClearErrorResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"M\n\x13ErrorMessageRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x12\n\nerror_code\x18\x02 \x01(\x11"=\n\x14ErrorMessageResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rerror_message\x18\x02 \x01(\t"J\n\x15GetChannelNameRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\r\n\x05index\x18\x02 \x01(\x11"E\n\x16GetChannelNameResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1b\n\x13channel_name_buffer\x18\x02 \x01(\t"H\n\x13GetRelayNameRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\r\n\x05index\x18\x02 \x01(\x11"A\n\x14GetRelayNameResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x19\n\x11relay_name_buffer\x18\x02 \x01(\t"N\n\x14GetRelayCountRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x12\n\nrelay_name\x18\x02 \x01(\t"<\n\x15GetRelayCountResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0brelay_count\x18\x02 \x01(\x11"Q\n\x17GetRelayPositionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x12\n\nrelay_name\x18\x02 \x01(\t"|\n\x18GetRelayPositionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x124\n\x0erelay_position\x18\x02 \x01(\x0e2\x1c.niswitch_grpc.RelayPosition\x12\x1a\n\x12relay_position_raw\x18\x03 \x01(\x11"\xb2\x01\n\x13RelayControlRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x12\n\nrelay_name\x18\x02 \x01(\t\x122\n\x0crelay_action\x18\x03 \x01(\x0e2\x1a.niswitch_grpc.RelayActionH\x00\x12\x1a\n\x10relay_action_raw\x18\x04 \x01(\x11H\x00B\x13\n\x11relay_action_enum"&\n\x14RelayControlResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"B\n\x1cResetInterchangeCheckRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"/\n\x1dResetInterchangeCheckResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"E\n\x1fClearInterchangeWarningsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"2\n ClearInterchangeWarningsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"3\n\rCommitRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session" \n\x0eCommitResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05">\n\x18ResetWithDefaultsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"+\n\x19ResetWithDefaultsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"4\n\x0eDisableRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"!\n\x0fDisableResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"2\n\x0cResetRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\x1f\n\rResetResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"5\n\x0fSelfTestRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"W\n\x10SelfTestResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x18\n\x10self_test_result\x18\x02 \x01(\x11\x12\x19\n\x11self_test_message\x18\x03 \x01(\t":\n\x14RevisionQueryRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"f\n\x15RevisionQueryResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12"\n\x1ainstrument_driver_revision\x18\x02 \x01(\t\x12\x19\n\x11firmware_revision\x18\x03 \x01(\t"\x8e\x01\n\x1aGetAttributeViInt32Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x126\n\x0cattribute_id\x18\x03 \x01(\x0e2 .niswitch_grpc.NiSwitchAttribute"F\n\x1bGetAttributeViInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fattribute_value\x18\x02 \x01(\x11"\x8f\x01\n\x1bGetAttributeViReal64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x126\n\x0cattribute_id\x18\x03 \x01(\x0e2 .niswitch_grpc.NiSwitchAttribute"G\n\x1cGetAttributeViReal64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fattribute_value\x18\x02 \x01(\x01"\x8f\x01\n\x1bGetAttributeViStringRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x126\n\x0cattribute_id\x18\x03 \x01(\x0e2 .niswitch_grpc.NiSwitchAttribute"G\n\x1cGetAttributeViStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fattribute_value\x18\x02 \x01(\t"\x90\x01\n\x1cGetAttributeViSessionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x126\n\x0cattribute_id\x18\x03 \x01(\x0e2 .niswitch_grpc.NiSwitchAttribute"`\n\x1dGetAttributeViSessionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12/\n\x0fattribute_value\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session"\x90\x01\n\x1cGetAttributeViBooleanRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x126\n\x0cattribute_id\x18\x03 \x01(\x0e2 .niswitch_grpc.NiSwitchAttribute"H\n\x1dGetAttributeViBooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fattribute_value\x18\x02 \x01(\x08"\x8d\x02\n\x1aSetAttributeViInt32Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x126\n\x0cattribute_id\x18\x03 \x01(\x0e2 .niswitch_grpc.NiSwitchAttribute\x12\x1d\n\x13attribute_value_raw\x18\x04 \x01(\x11H\x00\x12F\n\x0fattribute_value\x18\x05 \x01(\x0e2+.niswitch_grpc.NiSwitchInt32AttributeValuesH\x00B\x16\n\x14attribute_value_enum"-\n\x1bSetAttributeViInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xac\x01\n\x1bSetAttributeViReal64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x126\n\x0cattribute_id\x18\x03 \x01(\x0e2 .niswitch_grpc.NiSwitchAttribute\x12\x1b\n\x13attribute_value_raw\x18\x04 \x01(\x01".\n\x1cSetAttributeViReal64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xac\x01\n\x1bSetAttributeViStringRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x126\n\x0cattribute_id\x18\x03 \x01(\x0e2 .niswitch_grpc.NiSwitchAttribute\x12\x1b\n\x13attribute_value_raw\x18\x04 \x01(\t".\n\x1cSetAttributeViStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xc1\x01\n\x1cSetAttributeViSessionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x126\n\x0cattribute_id\x18\x03 \x01(\x0e2 .niswitch_grpc.NiSwitchAttribute\x12/\n\x0fattribute_value\x18\x04 \x01(\x0b2\x16.nidevice_grpc.Session"/\n\x1dSetAttributeViSessionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa9\x01\n\x1cSetAttributeViBooleanRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x126\n\x0cattribute_id\x18\x03 \x01(\x0e2 .niswitch_grpc.NiSwitchAttribute\x12\x17\n\x0fattribute_value\x18\x04 \x01(\x08"/\n\x1dSetAttributeViBooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x8f\x02\n\x1cCheckAttributeViInt32Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x126\n\x0cattribute_id\x18\x03 \x01(\x0e2 .niswitch_grpc.NiSwitchAttribute\x12\x1d\n\x13attribute_value_raw\x18\x04 \x01(\x11H\x00\x12F\n\x0fattribute_value\x18\x05 \x01(\x0e2+.niswitch_grpc.NiSwitchInt32AttributeValuesH\x00B\x16\n\x14attribute_value_enum"/\n\x1dCheckAttributeViInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xae\x01\n\x1dCheckAttributeViReal64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x126\n\x0cattribute_id\x18\x03 \x01(\x0e2 .niswitch_grpc.NiSwitchAttribute\x12\x1b\n\x13attribute_value_raw\x18\x04 \x01(\x01"0\n\x1eCheckAttributeViReal64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xae\x01\n\x1dCheckAttributeViStringRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x126\n\x0cattribute_id\x18\x03 \x01(\x0e2 .niswitch_grpc.NiSwitchAttribute\x12\x1b\n\x13attribute_value_raw\x18\x04 \x01(\t"0\n\x1eCheckAttributeViStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xc3\x01\n\x1eCheckAttributeViSessionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x126\n\x0cattribute_id\x18\x03 \x01(\x0e2 .niswitch_grpc.NiSwitchAttribute\x12/\n\x0fattribute_value\x18\x04 \x01(\x0b2\x16.nidevice_grpc.Session"1\n\x1fCheckAttributeViSessionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xab\x01\n\x1eCheckAttributeViBooleanRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x126\n\x0cattribute_id\x18\x03 \x01(\x0e2 .niswitch_grpc.NiSwitchAttribute\x12\x17\n\x0fattribute_value\x18\x04 \x01(\x08"1\n\x1fCheckAttributeViBooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"D\n\x1eInvalidateAllAttributesRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"1\n\x1fInvalidateAllAttributesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05*\xb0\x17\n\x11NiSwitchAttribute\x12"\n\x1eNISWITCH_ATTRIBUTE_UNSPECIFIED\x10\x00\x12$\n\x1eNISWITCH_ATTRIBUTE_RANGE_CHECK\x10\x92\x8b@\x120\n*NISWITCH_ATTRIBUTE_QUERY_INSTRUMENT_STATUS\x10\x93\x8b@\x12\x1e\n\x18NISWITCH_ATTRIBUTE_CACHE\x10\x94\x8b@\x12!\n\x1bNISWITCH_ATTRIBUTE_SIMULATE\x10\x95\x8b@\x12)\n#NISWITCH_ATTRIBUTE_RECORD_COERCIONS\x10\x96\x8b@\x12*\n$NISWITCH_ATTRIBUTE_INTERCHANGE_CHECK\x10\xa5\x8b@\x12&\n NISWITCH_ATTRIBUTE_CHANNEL_COUNT\x10\xdb\x8c@\x12+\n%NISWITCH_ATTRIBUTE_GROUP_CAPABILITIES\x10\xa1\x8e@\x12/\n)NISWITCH_ATTRIBUTE_SPECIFIC_DRIVER_PREFIX\x10\xbe\x8d@\x124\n.NISWITCH_ATTRIBUTE_SUPPORTED_INSTRUMENT_MODELS\x10\xd7\x8d@\x120\n*NISWITCH_ATTRIBUTE_INSTRUMENT_MANUFACTURER\x10\x8f\x8f@\x12)\n#NISWITCH_ATTRIBUTE_INSTRUMENT_MODEL\x10\x90\x8f@\x125\n/NISWITCH_ATTRIBUTE_INSTRUMENT_FIRMWARE_REVISION\x10\x8e\x8f@\x121\n+NISWITCH_ATTRIBUTE_SPECIFIC_DRIVER_REVISION\x10\xb7\x8f@\x12/\n)NISWITCH_ATTRIBUTE_SPECIFIC_DRIVER_VENDOR\x10\x91\x8f@\x12A\n;NISWITCH_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION\x10\x93\x8f@\x12A\n;NISWITCH_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION\x10\x94\x8f@\x124\n.NISWITCH_ATTRIBUTE_SPECIFIC_DRIVER_DESCRIPTION\x10\x92\x8f@\x12%\n\x1fNISWITCH_ATTRIBUTE_DRIVER_SETUP\x10\x97\x8b@\x12%\n\x1fNISWITCH_ATTRIBUTE_LOGICAL_NAME\x10\xc1\x8d@\x12/\n)NISWITCH_ATTRIBUTE_IO_RESOURCE_DESCRIPTOR\x10\xc0\x8d@\x12*\n$NISWITCH_ATTRIBUTE_IS_SOURCE_CHANNEL\x10\xd1\xa5L\x121\n+NISWITCH_ATTRIBUTE_IS_CONFIGURATION_CHANNEL\x10\xd3\xa5L\x12%\n\x1fNISWITCH_ATTRIBUTE_IS_DEBOUNCED\x10\xd2\xa5L\x12&\n NISWITCH_ATTRIBUTE_SETTLING_TIME\x10\xd4\xa5L\x12"\n\x1cNISWITCH_ATTRIBUTE_BANDWIDTH\x10\xd5\xa5L\x12\'\n!NISWITCH_ATTRIBUTE_MAX_DC_VOLTAGE\x10\xd6\xa5L\x12\'\n!NISWITCH_ATTRIBUTE_MAX_AC_VOLTAGE\x10\xd7\xa5L\x121\n+NISWITCH_ATTRIBUTE_MAX_SWITCHING_AC_CURRENT\x10\xd9\xa5L\x121\n+NISWITCH_ATTRIBUTE_MAX_SWITCHING_DC_CURRENT\x10\xd8\xa5L\x12-\n\'NISWITCH_ATTRIBUTE_MAX_CARRY_AC_CURRENT\x10\xdb\xa5L\x12-\n\'NISWITCH_ATTRIBUTE_MAX_CARRY_DC_CURRENT\x10\xda\xa5L\x12/\n)NISWITCH_ATTRIBUTE_MAX_SWITCHING_AC_POWER\x10\xdd\xa5L\x12/\n)NISWITCH_ATTRIBUTE_MAX_SWITCHING_DC_POWER\x10\xdc\xa5L\x12+\n%NISWITCH_ATTRIBUTE_MAX_CARRY_AC_POWER\x10\xdf\xa5L\x12+\n%NISWITCH_ATTRIBUTE_MAX_CARRY_DC_POWER\x10\xde\xa5L\x121\n+NISWITCH_ATTRIBUTE_CHARACTERISTIC_IMPEDANCE\x10\xe0\xa5L\x12"\n\x1cNISWITCH_ATTRIBUTE_WIRE_MODE\x10\xe1\xa5L\x12$\n\x1eNISWITCH_ATTRIBUTE_NUM_OF_ROWS\x10\xe2\xa5L\x12\'\n!NISWITCH_ATTRIBUTE_NUM_OF_COLUMNS\x10\xe3\xa5L\x12"\n\x1cNISWITCH_ATTRIBUTE_SCAN_LIST\x10\xe4\xa5L\x12"\n\x1cNISWITCH_ATTRIBUTE_SCAN_MODE\x10\xe5\xa5L\x12&\n NISWITCH_ATTRIBUTE_TRIGGER_INPUT\x10\xe6\xa5L\x12-\n\'NISWITCH_ATTRIBUTE_SCAN_ADVANCED_OUTPUT\x10\xe7\xa5L\x12#\n\x1dNISWITCH_ATTRIBUTE_SCAN_DELAY\x10\xe9\xa5L\x12(\n"NISWITCH_ATTRIBUTE_CONTINUOUS_SCAN\x10\xea\xa5L\x12$\n\x1eNISWITCH_ATTRIBUTE_IS_SCANNING\x10\xe8\xa5L\x12,\n&NISWITCH_ATTRIBUTE_IS_WAITING_FOR_TRIG\x10\xb4\x98F\x12%\n\x1fNISWITCH_ATTRIBUTE_TRIGGER_MODE\x10\xb5\x98F\x121\n+NISWITCH_ATTRIBUTE_MASTER_SLAVE_TRIGGER_BUS\x10\xb6\x98F\x127\n1NISWITCH_ATTRIBUTE_MASTER_SLAVE_SCAN_ADVANCED_BUS\x10\xb7\x98F\x122\n,NISWITCH_ATTRIBUTE_CABLED_MODULE_TRIGGER_BUS\x10\xb8\x98F\x128\n2NISWITCH_ATTRIBUTE_CABLED_MODULE_SCAN_ADVANCED_BUS\x10\xb9\x98F\x12/\n)NISWITCH_ATTRIBUTE_TRIGGER_INPUT_POLARITY\x10\xba\x98F\x12/\n)NISWITCH_ATTRIBUTE_SCAN_ADVANCED_POLARITY\x10\xbb\x98F\x12)\n#NISWITCH_ATTRIBUTE_PARSED_SCAN_LIST\x10\xbc\x98F\x12/\n)NISWITCH_ATTRIBUTE_HANDSHAKING_INITIATION\x10\xbd\x98F\x12)\n#NISWITCH_ATTRIBUTE_NUMBER_OF_RELAYS\x10\xbe\x98F\x12&\n NISWITCH_ATTRIBUTE_SERIAL_NUMBER\x10\xbf\x98F\x12.\n(NISWITCH_ATTRIBUTE_DIGITAL_FILTER_ENABLE\x10\xc0\x98F\x12B\n<NISWITCH_ATTRIBUTE_POWER_DOWN_LATCHING_RELAYS_AFTER_DEBOUNCE\x10\xc1\x98F\x122\n,NISWITCH_ATTRIBUTE_ANALOG_BUS_SHARING_ENABLE\x10\xc2\x98F\x12$\n\x1eNISWITCH_ATTRIBUTE_TEMPERATURE\x10\xc3\x98F\x12*\n$NISWITCH_ATTRIBUTE_SERIAL_NUMBER_I32\x10\xb1\x98F*\x86\x01\n\x08ScanMode\x12\x1f\n\x1bSCAN_MODE_NISWITCH_VAL_NONE\x10\x00\x12,\n(SCAN_MODE_NISWITCH_VAL_BREAK_BEFORE_MAKE\x10\x01\x12+\n\'SCAN_MODE_NISWITCH_VAL_BREAK_AFTER_MAKE\x10\x02*\x98\x0f\n\x0cTriggerInput\x12\x1d\n\x19TRIGGER_INPUT_UNSPECIFIED\x10\x00\x12(\n$TRIGGER_INPUT_NISWITCH_VAL_IMMEDIATE\x10\x01\x12\'\n#TRIGGER_INPUT_NISWITCH_VAL_EXTERNAL\x10\x02\x12,\n(TRIGGER_INPUT_NISWITCH_VAL_SOFTWARE_TRIG\x10\x03\x12#\n\x1fTRIGGER_INPUT_NISWITCH_VAL_TTL0\x10o\x12#\n\x1fTRIGGER_INPUT_NISWITCH_VAL_TTL1\x10p\x12#\n\x1fTRIGGER_INPUT_NISWITCH_VAL_TTL2\x10q\x12#\n\x1fTRIGGER_INPUT_NISWITCH_VAL_TTL3\x10r\x12#\n\x1fTRIGGER_INPUT_NISWITCH_VAL_TTL4\x10s\x12#\n\x1fTRIGGER_INPUT_NISWITCH_VAL_TTL5\x10t\x12#\n\x1fTRIGGER_INPUT_NISWITCH_VAL_TTL6\x10u\x12#\n\x1fTRIGGER_INPUT_NISWITCH_VAL_TTL7\x10v\x12\'\n#TRIGGER_INPUT_NISWITCH_VAL_PXI_STAR\x10}\x12-\n(TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR\x10\xe8\x07\x12.\n)TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR\x10\xe9\x07\x125\n0TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE1\x10\xfd\x07\x125\n0TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE2\x10\xfe\x07\x125\n0TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE3\x10\xff\x07\x125\n0TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE4\x10\x80\x08\x125\n0TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE5\x10\x81\x08\x125\n0TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE6\x10\x82\x08\x125\n0TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE7\x10\x83\x08\x125\n0TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE8\x10\x84\x08\x125\n0TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE9\x10\x85\x08\x126\n1TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE10\x10\x86\x08\x126\n1TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE11\x10\x87\x08\x126\n1TRIGGER_INPUT_NISWITCH_VAL_REARCONNECTOR_MODULE12\x10\x88\x08\x126\n1TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE1\x10\x91\x08\x126\n1TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE2\x10\x92\x08\x126\n1TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE3\x10\x93\x08\x126\n1TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE4\x10\x94\x08\x126\n1TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE5\x10\x95\x08\x126\n1TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE6\x10\x96\x08\x126\n1TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE7\x10\x97\x08\x126\n1TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE8\x10\x98\x08\x126\n1TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE9\x10\x99\x08\x127\n2TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE10\x10\x9a\x08\x127\n2TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE11\x10\x9b\x08\x127\n2TRIGGER_INPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE12\x10\x9c\x08*\xdb\x02\n\x0ePathCapability\x12\x1f\n\x1bPATH_CAPABILITY_UNSPECIFIED\x10\x00\x12/\n+PATH_CAPABILITY_NISWITCH_VAL_PATH_AVAILABLE\x10\x01\x12,\n(PATH_CAPABILITY_NISWITCH_VAL_PATH_EXISTS\x10\x02\x121\n-PATH_CAPABILITY_NISWITCH_VAL_PATH_UNSUPPORTED\x10\x03\x12,\n(PATH_CAPABILITY_NISWITCH_VAL_RSRC_IN_USE\x10\x04\x120\n,PATH_CAPABILITY_NISWITCH_VAL_SOURCE_CONFLICT\x10\x05\x126\n2PATH_CAPABILITY_NISWITCH_VAL_CHANNEL_NOT_AVAILABLE\x10\x06*\x97\x01\n\x15HandshakingInitiation\x12D\n@HANDSHAKING_INITIATION_NISWITCH_VAL_MEASUREMENT_DEVICE_INITIATED\x10\x00\x128\n4HANDSHAKING_INITIATION_NISWITCH_VAL_SWITCH_INITIATED\x10\x01*}\n\rRelayPosition\x12\x1e\n\x1aRELAY_POSITION_UNSPECIFIED\x10\x00\x12$\n RELAY_POSITION_NISWITCH_VAL_OPEN\x10\n\x12&\n"RELAY_POSITION_NISWITCH_VAL_CLOSED\x10\x0b*\x80\x01\n\x0bRelayAction\x12\x1c\n\x18RELAY_ACTION_UNSPECIFIED\x10\x00\x12(\n$RELAY_ACTION_NISWITCH_VAL_OPEN_RELAY\x10\x14\x12)\n%RELAY_ACTION_NISWITCH_VAL_CLOSE_RELAY\x10\x15*\xcf\x10\n\x12ScanAdvancedOutput\x12*\n&SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_NONE\x10\x00\x12.\n*SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_EXTERNAL\x10\x02\x12*\n&SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_TTL0\x10o\x12*\n&SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_TTL1\x10p\x12*\n&SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_TTL2\x10q\x12*\n&SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_TTL3\x10r\x12*\n&SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_TTL4\x10s\x12*\n&SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_TTL5\x10t\x12*\n&SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_TTL6\x10u\x12*\n&SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_TTL7\x10v\x12.\n*SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_PXI_STAR\x10}\x124\n/SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR\x10\xe8\x07\x125\n0SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR\x10\xe9\x07\x12<\n7SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE1\x10\xfd\x07\x12<\n7SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE2\x10\xfe\x07\x12<\n7SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE3\x10\xff\x07\x12<\n7SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE4\x10\x80\x08\x12<\n7SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE5\x10\x81\x08\x12<\n7SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE6\x10\x82\x08\x12<\n7SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE7\x10\x83\x08\x12<\n7SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE8\x10\x84\x08\x12<\n7SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE9\x10\x85\x08\x12=\n8SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE10\x10\x86\x08\x12=\n8SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE11\x10\x87\x08\x12=\n8SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_REARCONNECTOR_MODULE12\x10\x88\x08\x12=\n8SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE1\x10\x91\x08\x12=\n8SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE2\x10\x92\x08\x12=\n8SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE3\x10\x93\x08\x12=\n8SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE4\x10\x94\x08\x12=\n8SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE5\x10\x95\x08\x12=\n8SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE6\x10\x96\x08\x12=\n8SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE7\x10\x97\x08\x12=\n8SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE8\x10\x98\x08\x12=\n8SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE9\x10\x99\x08\x12>\n9SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE10\x10\x9a\x08\x12>\n9SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE11\x10\x9b\x08\x12>\n9SCAN_ADVANCED_OUTPUT_NISWITCH_VAL_FRONTCONNECTOR_MODULE12\x10\x9c\x08*\xad(\n\x1cNiSwitchInt32AttributeValues\x12\x1e\n\x1aNISWITCH_INT32_UNSPECIFIED\x10\x00\x12J\nFNISWITCH_INT32_HANDSHAKING_INITIATION_VAL_MEASUREMENT_DEVICE_INITIATED\x10\x00\x12>\n:NISWITCH_INT32_HANDSHAKING_INITIATION_VAL_SWITCH_INITIATED\x10\x01\x120\n,NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_NONE\x10\x00\x124\n0NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_EXTERNAL\x10\x02\x120\n,NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_TTL0\x10o\x120\n,NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_TTL1\x10p\x120\n,NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_TTL2\x10q\x120\n,NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_TTL3\x10r\x120\n,NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_TTL4\x10s\x120\n,NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_TTL5\x10t\x120\n,NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_TTL6\x10u\x120\n,NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_TTL7\x10v\x124\n0NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_PXI_STAR\x10}\x12:\n5NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR\x10\xe8\x07\x12;\n6NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR\x10\xe9\x07\x12B\n=NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE1\x10\xfd\x07\x12B\n=NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE2\x10\xfe\x07\x12B\n=NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE3\x10\xff\x07\x12B\n=NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE4\x10\x80\x08\x12B\n=NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE5\x10\x81\x08\x12B\n=NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE6\x10\x82\x08\x12B\n=NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE7\x10\x83\x08\x12B\n=NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE8\x10\x84\x08\x12B\n=NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE9\x10\x85\x08\x12C\n>NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE10\x10\x86\x08\x12C\n>NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE11\x10\x87\x08\x12C\n>NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_REARCONNECTOR_MODULE12\x10\x88\x08\x12C\n>NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE1\x10\x91\x08\x12C\n>NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE2\x10\x92\x08\x12C\n>NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE3\x10\x93\x08\x12C\n>NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE4\x10\x94\x08\x12C\n>NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE5\x10\x95\x08\x12C\n>NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE6\x10\x96\x08\x12C\n>NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE7\x10\x97\x08\x12C\n>NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE8\x10\x98\x08\x12C\n>NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE9\x10\x99\x08\x12D\n?NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE10\x10\x9a\x08\x12D\n?NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE11\x10\x9b\x08\x12D\n?NISWITCH_INT32_SCAN_ADVANCED_OUTPUT_VAL_FRONTCONNECTOR_MODULE12\x10\x9c\x08\x129\n5NISWITCH_INT32_SCAN_ADVANCED_POLARITY_VAL_RISING_EDGE\x10\x00\x12:\n6NISWITCH_INT32_SCAN_ADVANCED_POLARITY_VAL_FALLING_EDGE\x10\x01\x12%\n!NISWITCH_INT32_SCAN_MODE_VAL_NONE\x10\x00\x122\n.NISWITCH_INT32_SCAN_MODE_VAL_BREAK_BEFORE_MAKE\x10\x01\x121\n-NISWITCH_INT32_SCAN_MODE_VAL_BREAK_AFTER_MAKE\x10\x02\x12.\n*NISWITCH_INT32_TRIGGER_INPUT_VAL_IMMEDIATE\x10\x01\x12-\n)NISWITCH_INT32_TRIGGER_INPUT_VAL_EXTERNAL\x10\x02\x122\n.NISWITCH_INT32_TRIGGER_INPUT_VAL_SOFTWARE_TRIG\x10\x03\x12)\n%NISWITCH_INT32_TRIGGER_INPUT_VAL_TTL0\x10o\x12)\n%NISWITCH_INT32_TRIGGER_INPUT_VAL_TTL1\x10p\x12)\n%NISWITCH_INT32_TRIGGER_INPUT_VAL_TTL2\x10q\x12)\n%NISWITCH_INT32_TRIGGER_INPUT_VAL_TTL3\x10r\x12)\n%NISWITCH_INT32_TRIGGER_INPUT_VAL_TTL4\x10s\x12)\n%NISWITCH_INT32_TRIGGER_INPUT_VAL_TTL5\x10t\x12)\n%NISWITCH_INT32_TRIGGER_INPUT_VAL_TTL6\x10u\x12)\n%NISWITCH_INT32_TRIGGER_INPUT_VAL_TTL7\x10v\x12-\n)NISWITCH_INT32_TRIGGER_INPUT_VAL_PXI_STAR\x10}\x123\n.NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR\x10\xe8\x07\x124\n/NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR\x10\xe9\x07\x12;\n6NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE1\x10\xfd\x07\x12;\n6NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE2\x10\xfe\x07\x12;\n6NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE3\x10\xff\x07\x12;\n6NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE4\x10\x80\x08\x12;\n6NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE5\x10\x81\x08\x12;\n6NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE6\x10\x82\x08\x12;\n6NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE7\x10\x83\x08\x12;\n6NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE8\x10\x84\x08\x12;\n6NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE9\x10\x85\x08\x12<\n7NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE10\x10\x86\x08\x12<\n7NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE11\x10\x87\x08\x12<\n7NISWITCH_INT32_TRIGGER_INPUT_VAL_REARCONNECTOR_MODULE12\x10\x88\x08\x12<\n7NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE1\x10\x91\x08\x12<\n7NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE2\x10\x92\x08\x12<\n7NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE3\x10\x93\x08\x12<\n7NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE4\x10\x94\x08\x12<\n7NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE5\x10\x95\x08\x12<\n7NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE6\x10\x96\x08\x12<\n7NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE7\x10\x97\x08\x12<\n7NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE8\x10\x98\x08\x12<\n7NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE9\x10\x99\x08\x12=\n8NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE10\x10\x9a\x08\x12=\n8NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE11\x10\x9b\x08\x12=\n8NISWITCH_INT32_TRIGGER_INPUT_VAL_FRONTCONNECTOR_MODULE12\x10\x9c\x08\x129\n5NISWITCH_INT32_TRIGGER_INPUT_POLARITY_VAL_RISING_EDGE\x10\x00\x12:\n6NISWITCH_INT32_TRIGGER_INPUT_POLARITY_VAL_FALLING_EDGE\x10\x01\x12\'\n#NISWITCH_INT32_WIRE_MODE_VAL_1_WIRE\x10\x01\x12\'\n#NISWITCH_INT32_WIRE_MODE_VAL_2_WIRE\x10\x02\x12\'\n#NISWITCH_INT32_WIRE_MODE_VAL_4_WIRE\x10\x04\x1a\x02\x10\x012\xac,\n\x08NiSwitch\x12?\n\x04Init\x12\x1a.niswitch_grpc.InitRequest\x1a\x1b.niswitch_grpc.InitResponse\x12`\n\x0fInitWithOptions\x12%.niswitch_grpc.InitWithOptionsRequest\x1a&.niswitch_grpc.InitWithOptionsResponse\x12c\n\x10InitWithTopology\x12&.niswitch_grpc.InitWithTopologyRequest\x1a\'.niswitch_grpc.InitWithTopologyResponse\x12B\n\x05Close\x12\x1b.niswitch_grpc.CloseRequest\x1a\x1c.niswitch_grpc.CloseResponse\x12H\n\x07Connect\x12\x1d.niswitch_grpc.ConnectRequest\x1a\x1e.niswitch_grpc.ConnectResponse\x12`\n\x0fConnectMultiple\x12%.niswitch_grpc.ConnectMultipleRequest\x1a&.niswitch_grpc.ConnectMultipleResponse\x12Q\n\nDisconnect\x12 .niswitch_grpc.DisconnectRequest\x1a!.niswitch_grpc.DisconnectResponse\x12i\n\x12DisconnectMultiple\x12(.niswitch_grpc.DisconnectMultipleRequest\x1a).niswitch_grpc.DisconnectMultipleResponse\x12Z\n\rDisconnectAll\x12#.niswitch_grpc.DisconnectAllRequest\x1a$.niswitch_grpc.DisconnectAllResponse\x12H\n\x07GetPath\x12\x1d.niswitch_grpc.GetPathRequest\x1a\x1e.niswitch_grpc.GetPathResponse\x12H\n\x07SetPath\x12\x1d.niswitch_grpc.SetPathRequest\x1a\x1e.niswitch_grpc.SetPathResponse\x12Q\n\nCanConnect\x12 .niswitch_grpc.CanConnectRequest\x1a!.niswitch_grpc.CanConnectResponse\x12T\n\x0bIsDebounced\x12!.niswitch_grpc.IsDebouncedRequest\x1a".niswitch_grpc.IsDebouncedResponse\x12`\n\x0fWaitForDebounce\x12%.niswitch_grpc.WaitForDebounceRequest\x1a&.niswitch_grpc.WaitForDebounceResponse\x12?\n\x04Scan\x12\x1a.niswitch_grpc.ScanRequest\x1a\x1b.niswitch_grpc.ScanResponse\x12W\n\x0cInitiateScan\x12".niswitch_grpc.InitiateScanRequest\x1a#.niswitch_grpc.InitiateScanResponse\x12N\n\tAbortScan\x12\x1f.niswitch_grpc.AbortScanRequest\x1a .niswitch_grpc.AbortScanResponse\x12Q\n\nIsScanning\x12 .niswitch_grpc.IsScanningRequest\x1a!.niswitch_grpc.IsScanningResponse\x12l\n\x13WaitForScanComplete\x12).niswitch_grpc.WaitForScanCompleteRequest\x1a*.niswitch_grpc.WaitForScanCompleteResponse\x12l\n\x13SendSoftwareTrigger\x12).niswitch_grpc.SendSoftwareTriggerRequest\x1a*.niswitch_grpc.SendSoftwareTriggerResponse\x12f\n\x11ConfigureScanList\x12\'.niswitch_grpc.ConfigureScanListRequest\x1a(.niswitch_grpc.ConfigureScanListResponse\x12o\n\x14ConfigureScanTrigger\x12*.niswitch_grpc.ConfigureScanTriggerRequest\x1a+.niswitch_grpc.ConfigureScanTriggerResponse\x12f\n\x11SetContinuousScan\x12\'.niswitch_grpc.SetContinuousScanRequest\x1a(.niswitch_grpc.SetContinuousScanResponse\x12f\n\x11RouteTriggerInput\x12\'.niswitch_grpc.RouteTriggerInputRequest\x1a(.niswitch_grpc.RouteTriggerInputResponse\x12x\n\x17RouteScanAdvancedOutput\x12-.niswitch_grpc.RouteScanAdvancedOutputRequest\x1a..niswitch_grpc.RouteScanAdvancedOutputResponse\x12Q\n\nErrorQuery\x12 .niswitch_grpc.ErrorQueryRequest\x1a!.niswitch_grpc.ErrorQueryResponse\x12K\n\x08GetError\x12\x1e.niswitch_grpc.GetErrorRequest\x1a\x1f.niswitch_grpc.GetErrorResponse\x12Q\n\nClearError\x12 .niswitch_grpc.ClearErrorRequest\x1a!.niswitch_grpc.ClearErrorResponse\x12W\n\x0cErrorMessage\x12".niswitch_grpc.ErrorMessageRequest\x1a#.niswitch_grpc.ErrorMessageResponse\x12]\n\x0eGetChannelName\x12$.niswitch_grpc.GetChannelNameRequest\x1a%.niswitch_grpc.GetChannelNameResponse\x12W\n\x0cGetRelayName\x12".niswitch_grpc.GetRelayNameRequest\x1a#.niswitch_grpc.GetRelayNameResponse\x12Z\n\rGetRelayCount\x12#.niswitch_grpc.GetRelayCountRequest\x1a$.niswitch_grpc.GetRelayCountResponse\x12c\n\x10GetRelayPosition\x12&.niswitch_grpc.GetRelayPositionRequest\x1a\'.niswitch_grpc.GetRelayPositionResponse\x12W\n\x0cRelayControl\x12".niswitch_grpc.RelayControlRequest\x1a#.niswitch_grpc.RelayControlResponse\x12r\n\x15ResetInterchangeCheck\x12+.niswitch_grpc.ResetInterchangeCheckRequest\x1a,.niswitch_grpc.ResetInterchangeCheckResponse\x12{\n\x18ClearInterchangeWarnings\x12..niswitch_grpc.ClearInterchangeWarningsRequest\x1a/.niswitch_grpc.ClearInterchangeWarningsResponse\x12E\n\x06Commit\x12\x1c.niswitch_grpc.CommitRequest\x1a\x1d.niswitch_grpc.CommitResponse\x12f\n\x11ResetWithDefaults\x12\'.niswitch_grpc.ResetWithDefaultsRequest\x1a(.niswitch_grpc.ResetWithDefaultsResponse\x12H\n\x07Disable\x12\x1d.niswitch_grpc.DisableRequest\x1a\x1e.niswitch_grpc.DisableResponse\x12B\n\x05Reset\x12\x1b.niswitch_grpc.ResetRequest\x1a\x1c.niswitch_grpc.ResetResponse\x12K\n\x08SelfTest\x12\x1e.niswitch_grpc.SelfTestRequest\x1a\x1f.niswitch_grpc.SelfTestResponse\x12Z\n\rRevisionQuery\x12#.niswitch_grpc.RevisionQueryRequest\x1a$.niswitch_grpc.RevisionQueryResponse\x12l\n\x13GetAttributeViInt32\x12).niswitch_grpc.GetAttributeViInt32Request\x1a*.niswitch_grpc.GetAttributeViInt32Response\x12o\n\x14GetAttributeViReal64\x12*.niswitch_grpc.GetAttributeViReal64Request\x1a+.niswitch_grpc.GetAttributeViReal64Response\x12o\n\x14GetAttributeViString\x12*.niswitch_grpc.GetAttributeViStringRequest\x1a+.niswitch_grpc.GetAttributeViStringResponse\x12r\n\x15GetAttributeViSession\x12+.niswitch_grpc.GetAttributeViSessionRequest\x1a,.niswitch_grpc.GetAttributeViSessionResponse\x12r\n\x15GetAttributeViBoolean\x12+.niswitch_grpc.GetAttributeViBooleanRequest\x1a,.niswitch_grpc.GetAttributeViBooleanResponse\x12l\n\x13SetAttributeViInt32\x12).niswitch_grpc.SetAttributeViInt32Request\x1a*.niswitch_grpc.SetAttributeViInt32Response\x12o\n\x14SetAttributeViReal64\x12*.niswitch_grpc.SetAttributeViReal64Request\x1a+.niswitch_grpc.SetAttributeViReal64Response\x12o\n\x14SetAttributeViString\x12*.niswitch_grpc.SetAttributeViStringRequest\x1a+.niswitch_grpc.SetAttributeViStringResponse\x12r\n\x15SetAttributeViSession\x12+.niswitch_grpc.SetAttributeViSessionRequest\x1a,.niswitch_grpc.SetAttributeViSessionResponse\x12r\n\x15SetAttributeViBoolean\x12+.niswitch_grpc.SetAttributeViBooleanRequest\x1a,.niswitch_grpc.SetAttributeViBooleanResponse\x12r\n\x15CheckAttributeViInt32\x12+.niswitch_grpc.CheckAttributeViInt32Request\x1a,.niswitch_grpc.CheckAttributeViInt32Response\x12u\n\x16CheckAttributeViReal64\x12,.niswitch_grpc.CheckAttributeViReal64Request\x1a-.niswitch_grpc.CheckAttributeViReal64Response\x12u\n\x16CheckAttributeViString\x12,.niswitch_grpc.CheckAttributeViStringRequest\x1a-.niswitch_grpc.CheckAttributeViStringResponse\x12x\n\x17CheckAttributeViSession\x12-.niswitch_grpc.CheckAttributeViSessionRequest\x1a..niswitch_grpc.CheckAttributeViSessionResponse\x12x\n\x17CheckAttributeViBoolean\x12-.niswitch_grpc.CheckAttributeViBooleanRequest\x1a..niswitch_grpc.CheckAttributeViBooleanResponse\x12x\n\x17InvalidateAllAttributes\x12-.niswitch_grpc.InvalidateAllAttributesRequest\x1a..niswitch_grpc.InvalidateAllAttributesResponseBD\n\x14com.ni.grpc.niswitchB\x08NiSwitchP\x01\xaa\x02\x1fNationalInstruments.Grpc.Switchb\x06proto3')`

<!--NI_PYTHON_API repo=nimi-python path=generated/niswitch/niswitch/niswitch_pb2_grpc.py -->
## PYTHON MODULE: generated/niswitch/niswitch/niswitch_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

### `class NiSwitchStub(object)`

Missing associated documentation comment in .proto file.

#### `def __init__(self, channel)`

Constructor.

        Args:
            channel: A grpc.Channel.
        

### `class NiSwitchServicer(object)`

Missing associated documentation comment in .proto file.

#### `def Init(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def InitWithOptions(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def InitWithTopology(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Close(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Connect(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConnectMultiple(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Disconnect(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DisconnectMultiple(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DisconnectAll(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetPath(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetPath(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CanConnect(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def IsDebounced(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WaitForDebounce(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Scan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def InitiateScan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def AbortScan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def IsScanning(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WaitForScanComplete(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SendSoftwareTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureScanList(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureScanTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetContinuousScan(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def RouteTriggerInput(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def RouteScanAdvancedOutput(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ErrorQuery(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetError(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ClearError(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ErrorMessage(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetChannelName(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetRelayName(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetRelayCount(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetRelayPosition(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def RelayControl(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ResetInterchangeCheck(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ClearInterchangeWarnings(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Commit(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ResetWithDefaults(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Disable(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Reset(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SelfTest(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def RevisionQuery(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViReal64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViSession(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViBoolean(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViReal64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViSession(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViBoolean(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CheckAttributeViInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CheckAttributeViReal64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CheckAttributeViString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CheckAttributeViSession(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CheckAttributeViBoolean(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def InvalidateAllAttributes(self, request, context)`

Missing associated documentation comment in .proto file.

### `def add_NiSwitchServicer_to_server(servicer, server)`

### `class NiSwitch(object)`

Missing associated documentation comment in .proto file.

#### `def Init(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def InitWithOptions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def InitWithTopology(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Close(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Connect(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConnectMultiple(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Disconnect(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DisconnectMultiple(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DisconnectAll(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetPath(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetPath(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CanConnect(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def IsDebounced(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WaitForDebounce(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Scan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def InitiateScan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def AbortScan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def IsScanning(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WaitForScanComplete(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SendSoftwareTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureScanList(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureScanTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetContinuousScan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def RouteTriggerInput(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def RouteScanAdvancedOutput(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ErrorQuery(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetError(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ClearError(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ErrorMessage(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetChannelName(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetRelayName(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetRelayCount(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetRelayPosition(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def RelayControl(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ResetInterchangeCheck(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ClearInterchangeWarnings(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Commit(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ResetWithDefaults(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Disable(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Reset(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SelfTest(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def RevisionQuery(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViReal64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViSession(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViBoolean(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViReal64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViSession(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViBoolean(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CheckAttributeViInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CheckAttributeViReal64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CheckAttributeViString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CheckAttributeViSession(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CheckAttributeViBoolean(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def InvalidateAllAttributes(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

<!--NI_PYTHON_API repo=nimi-python path=generated/niswitch/niswitch/session.py -->
## PYTHON MODULE: generated/niswitch/niswitch/session.py

### `class _Scan(object)`

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

Base class for all NI-SWITCH sessions.

#### `def __init__(self, repeated_capability_list, all_channels_in_session, interpreter, freeze_it=False)`

#### `def __repr__(self)`

#### `def __setattr__(self, key, value)`

#### `def _get_attribute_vi_boolean(self, attribute_id)`

_get_attribute_vi_boolean

        This method queries the value of a ViBoolean property. You can use
        this method to get the values of instrument specific properties and
        inherent IVI properties. If the property represents an instrument
        state, this method performs instrument I/O in the following cases: -
        State caching is disabled for the entire session or for the particular
        property. - State caching is enabled and the currently cached value is
        invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`niswitch.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`niswitch.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_boolean`

        Args:
            attribute_id (int): Pass the ID of a property. From the method panel window, you can use
                this control as follows. - Click on the control or press , , or , to
                display a dialog box containing a hierarchical list of the available
                properties. Properties whose value cannot be set are dim. Help text is
                shown for each property. Select a property by double-clicking on it
                or by selecting it and then pressing . A ring control at the top of the
                dialog box allows you to see all IVI properties or only the properties
                of the ViInt32 type. If you choose to see all IVI properties, the data
                types appear to the right of the property names in the list box. The
                data types that are not consistent with this method are dim. If you
                select a property data type that is dim, LabWindows/CVI transfers you
                to the method panel for the corresponding method that is consistent
                with the data type. - If you want to enter a variable name, press to
                change this ring control to a manual input box. - If the property in
                this ring control has constants as valid values, you can view the
                constants by moving to the Property Value control and pressing .


        Returns:
            attribute_value (bool): Returns the current value of the property. Pass the address of a
                ViBoolean variable. From the method panel window, you can use this
                control as follows. - If the property currently showing in the
                Property ID ring control has constants as valid values, you can view a
                list of the constants by pressing on this control. Select a value by
                double-clicking on it or by selecting it and then pressing .

        

#### `def _get_attribute_vi_int32(self, attribute_id)`

_get_attribute_vi_int32

        This method queries the value of a ViInt32 property. You can use this
        method to get the values of instrument specific properties and
        inherent IVI properties. If the property represents an instrument
        state, this method performs instrument I/O in the following cases: -
        State caching is disabled for the entire session or for the particular
        property. - State caching is enabled and the currently cached value is
        invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`niswitch.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`niswitch.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_int32`

        Args:
            attribute_id (int): Pass the ID of a property. From the method panel window, you can use
                this control as follows. - Click on the control or press , , or , to
                display a dialog box containing a hierarchical list of the available
                properties. Properties whose value cannot be set are dim. Help text is
                shown for each property. Select a property by double-clicking on it
                or by selecting it and then pressing . A ring control at the top of the
                dialog box allows you to see all IVI properties or only the properties
                of the ViInt32 type. If you choose to see all IVI properties, the data
                types appear to the right of the property names in the list box. The
                data types that are not consistent with this method are dim. If you
                select a property data type that is dim, LabWindows/CVI transfers you
                to the method panel for the corresponding method that is consistent
                with the data type. - If you want to enter a variable name, press to
                change this ring control to a manual input box. - If the property in
                this ring control has constants as valid values, you can view the
                constants by moving to the Property Value control and pressing .


        Returns:
            attribute_value (int): Returns the current value of the property. Pass the address of a
                ViInt32 variable. From the method panel window, you can use this
                control as follows. - If the property currently showing in the
                Property ID ring control has constants as valid values, you can view a
                list of the constants by pressing on this control. Select a value by
                double-clicking on it or by selecting it and then pressing .

        

#### `def _get_attribute_vi_real64(self, attribute_id)`

_get_attribute_vi_real64

        This method queries the value of a ViReal64 property. You can use
        this method to get the values of instrument specific properties and
        inherent IVI properties. If the property represents an instrument
        state, this method performs instrument I/O in the following cases: -
        State caching is disabled for the entire session or for the particular
        property. - State caching is enabled and the currently cached value is
        invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`niswitch.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`niswitch.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_real64`

        Args:
            attribute_id (int): Pass the ID of a property. From the method panel window, you can use
                this control as follows. - Click on the control or press , , or , to
                display a dialog box containing a hierarchical list of the available
                properties. Properties whose value cannot be set are dim. Help text is
                shown for each property. Select a property by double-clicking on it
                or by selecting it and then pressing . A ring control at the top of the
                dialog box allows you to see all IVI properties or only the properties
                of the ViInt32 type. If you choose to see all IVI properties, the data
                types appear to the right of the property names in the list box. The
                data types that are not consistent with this method are dim. If you
                select a property data type that is dim, LabWindows/CVI transfers you
                to the method panel for the corresponding method that is consistent
                with the data type. - If you want to enter a variable name, press to
                change this ring control to a manual input box. - If the property in
                this ring control has constants as valid values, you can view the
                constants by moving to the Property Value control and pressing .


        Returns:
            attribute_value (float): Returns the current value of the property. Pass the address of a
                ViReal64 variable. From the method panel window, you can use this
                control as follows. - If the property currently showing in the
                Property ID ring control has constants as valid values, you can view a
                list of the constants by pressing on this control. Select a value by
                double-clicking on it or by selecting it and then pressing .

        

#### `def _get_attribute_vi_string(self, attribute_id)`

_get_attribute_vi_string

        This method queries the value of a ViString property. You can use
        this method to get the values of instrument specific properties and
        inherent IVI properties. If the property represents an instrument
        state, this method performs instrument I/O in the following cases: -
        State caching is disabled for the entire session or for the particular
        property. - State caching is enabled and the currently cached value is
        invalid. You must provide a ViChar array to serve as a buffer for the
        value. You pass the number of bytes in the buffer as the Array Size
        parameter. If the current value of the property, including the
        terminating NULL byte, is larger than the size you indicate in the Array
        Size parameter, the method copies Array Size-1 bytes into the buffer,
        places an ASCII NULL byte at the end of the buffer, and returns the
        array size you must pass to get the entire value. For example, if the
        value is "123456" and the Array Size is 4, the method places "123"
        into the buffer and returns 7. If you want to call this method just to
        get the required array size, you can pass 0 for the Array Size and
        VI_NULL for the Property Value buffer. If you want the method to
        fill in the buffer regardless of the number of bytes in the value, pass
        a negative number for the Array Size parameter.

        Tip:
        This method can be called on specific channels within your :py:class:`niswitch.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`niswitch.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_string`

        Args:
            attribute_id (int): Pass the ID of a property. From the method panel window, you can use
                this control as follows. - Click on the control or press , , or , to
                display a dialog box containing a hierarchical list of the available
                properties. Properties whose value cannot be set are dim. Help text is
                shown for each property. Select a property by double-clicking on it
                or by selecting it and then pressing . A ring control at the top of the
                dialog box allows you to see all IVI properties or only the properties
                of the ViInt32 type. If you choose to see all IVI properties, the data
                types appear to the right of the property names in the list box. The
                data types that are not consistent with this method are dim. If you
                select a property data type that is dim, LabWindows/CVI transfers you
                to the method panel for the corresponding method that is consistent
                with the data type. - If you want to enter a variable name, press to
                change this ring control to a manual input box. - If the property in
                this ring control has constants as valid values, you can view the
                constants by moving to the Property Value control and pressing .


        Returns:
            attribute_value (str): The buffer in which the method returns the current value of the
                property. The buffer must be of type ViChar and have at least as many
                bytes as indicated in the Array Size parameter. If the current value of
                the property, including the terminating NUL byte, contains more bytes
                that you indicate in this parameter, the method copies Array Size-1
                bytes into the buffer, places an ASCII NUL byte at the end of the
                buffer, and returns the array size you must pass to get the entire
                value. For example, if the value is "123456" and the Array Size is 4,
                the method places "123" into the buffer and returns 7. If you specify
                0 for the Array Size parameter, you can pass VI_NULL for this
                parameter. From the method panel window, you can use this control as
                follows. - If the property currently showing in the Property ID ring
                control has constants as valid values, you can view a list of the
                constants by pressing on this control. Select a value by double-clicking
                on it or by selecting it and then pressing .

        

#### `def lock(self)`

lock

        Obtains a multithread lock on the device session. Before doing so, the
        software waits until all other execution threads release their locks
        on the device session.

        Other threads may have obtained a lock on this session for the
        following reasons:

            -  The application called the lock method.
            -  A call to NI-SWITCH locked the session.
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
            lock (context manager): When used in a with statement, niswitch.Session.lock acts as
            a context manager and unlock will be called when the with block is exited
        

#### `def _set_attribute_vi_boolean(self, attribute_id, attribute_value)`

_set_attribute_vi_boolean

        This method sets the value of a ViBoolean property. This is a
        low-level method that you can use to set the values of
        instrument-specific properties and inherent IVI properties. If the
        property represents an instrument state, this method performs
        instrument I/O in the following cases: - State caching is disabled for
        the entire session or for the particular property. - State caching is
        enabled and the currently cached value is invalid or is different than
        the value you specify. This instrument driver contains high-level
        methods that set most of the instrument properties. It is best to use
        the high-level driver methods as much as possible. They handle order
        dependencies and multithread locking for you. In addition, they perform
        status checking only after setting all of the properties. In contrast,
        when you set multiple properties using the SetAttribute methods, the
        methods check the instrument status after each call. Also, when state
        caching is enabled, the high-level methods that configure multiple
        properties perform instrument I/O only for the properties whose value
        you change. Thus, you can safely call the high-level methods without
        the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`niswitch.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`niswitch.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_boolean`

        Args:
            attribute_id (int): Pass the ID of a property. From the method panel window, you can use
                this control as follows. - Click on the control or press , , or , to
                display a dialog box containing a hierarchical list of the available
                properties. Properties whose value cannot be set are dim. Help text is
                shown for each property. Select a property by double-clicking on it
                or by selecting it and then pressing . Read-only properties appear dim
                in the list box. If you select a read-only property, an error message
                appears. A ring control at the top of the dialog box allows you to see
                all IVI properties or only the properties of the ViInt32 type. If you
                choose to see all IVI properties, the data types appear to the right of
                the property names in the list box. The data types that are not
                consistent with this method are dim. If you select a property data
                type that is dim, LabWindows/CVI transfers you to the method panel for
                the corresponding method that is consistent with the data type. - If
                you want to enter a variable name, press to change this ring control to
                a manual input box. - If the property in this ring control has
                constants as valid values, you can view the constants by moving to the
                Property Value control and pressing .

            attribute_value (bool): Pass the value to which you want to set the property. From the method
                panel window, you can use this control as follows. - If the property
                currently showing in the Property ID ring control has constants as
                valid values, you can view a list of the constants by pressing on this
                control. Select a value by double-clicking on it or by selecting it and
                then pressing . Note: Some of the values might not be valid depending on
                the current settings of the instrument session. Default Value: none

        

#### `def _set_attribute_vi_int32(self, attribute_id, attribute_value)`

_set_attribute_vi_int32

        This method sets the value of a ViInt32 property. This is a low-level
        method that you can use to set the values of instrument-specific
        properties and inherent IVI properties. If the property represents an
        instrument state, this method performs instrument I/O in the following
        cases: - State caching is disabled for the entire session or for the
        particular property. - State caching is enabled and the currently
        cached value is invalid or is different than the value you specify. This
        instrument driver contains high-level methods that set most of the
        instrument properties. It is best to use the high-level driver methods
        as much as possible. They handle order dependencies and multithread
        locking for you. In addition, they perform status checking only after
        setting all of the properties. In contrast, when you set multiple
        properties using the SetAttribute methods, the methods check the
        instrument status after each call. Also, when state caching is enabled,
        the high-level methods that configure multiple properties perform
        instrument I/O only for the properties whose value you change. Thus, you
        can safely call the high-level methods without the penalty of
        redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`niswitch.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`niswitch.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_int32`

        Args:
            attribute_id (int): Pass the ID of a property. From the method panel window, you can use
                this control as follows. - Click on the control or press , , or , to
                display a dialog box containing a hierarchical list of the available
                properties. Properties whose value cannot be set are dim. Help text is
                shown for each property. Select a property by double-clicking on it
                or by selecting it and then pressing . Read-only properties appear dim
                in the list box. If you select a read-only property, an error message
                appears. A ring control at the top of the dialog box allows you to see
                all IVI properties or only the properties of the ViInt32 type. If you
                choose to see all IVI properties, the data types appear to the right of
                the property names in the list box. The data types that are not
                consistent with this method are dim. If you select a property data
                type that is dim, LabWindows/CVI transfers you to the method panel for
                the corresponding method that is consistent with the data type. - If
                you want to enter a variable name, press to change this ring control to
                a manual input box. - If the property in this ring control has
                constants as valid values, you can view the constants by moving to the
                Property Value control and pressing .

            attribute_value (int): Pass the value to which you want to set the property. From the method
                panel window, you can use this control as follows. - If the property
                currently showing in the Property ID ring control has constants as
                valid values, you can view a list of the constants by pressing on this
                control. Select a value by double-clicking on it or by selecting it and
                then pressing . Note: Some of the values might not be valid depending on
                the current settings of the instrument session. Default Value: none

        

#### `def _set_attribute_vi_real64(self, attribute_id, attribute_value)`

_set_attribute_vi_real64

        This method sets the value of a ViReal64 property. This is a
        low-level method that you can use to set the values of
        instrument-specific properties and inherent IVI properties. If the
        property represents an instrument state, this method performs
        instrument I/O in the following cases: - State caching is disabled for
        the entire session or for the particular property. - State caching is
        enabled and the currently cached value is invalid or is different than
        the value you specify. This instrument driver contains high-level
        methods that set most of the instrument properties. It is best to use
        the high-level driver methods as much as possible. They handle order
        dependencies and multithread locking for you. In addition, they perform
        status checking only after setting all of the properties. In contrast,
        when you set multiple properties using the SetAttribute methods, the
        methods check the instrument status after each call. Also, when state
        caching is enabled, the high-level methods that configure multiple
        properties perform instrument I/O only for the properties whose value
        you change. Thus, you can safely call the high-level methods without
        the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`niswitch.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`niswitch.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_real64`

        Args:
            attribute_id (int): Pass the ID of a property. From the method panel window, you can use
                this control as follows. - Click on the control or press , , or , to
                display a dialog box containing a hierarchical list of the available
                properties. Properties whose value cannot be set are dim. Help text is
                shown for each property. Select a property by double-clicking on it
                or by selecting it and then pressing . Read-only properties appear dim
                in the list box. If you select a read-only property, an error message
                appears. A ring control at the top of the dialog box allows you to see
                all IVI properties or only the properties of the ViInt32 type. If you
                choose to see all IVI properties, the data types appear to the right of
                the property names in the list box. The data types that are not
                consistent with this method are dim. If you select a property data
                type that is dim, LabWindows/CVI transfers you to the method panel for
                the corresponding method that is consistent with the data type. - If
                you want to enter a variable name, press to change this ring control to
                a manual input box. - If the property in this ring control has
                constants as valid values, you can view the constants by moving to the
                Property Value control and pressing .

            attribute_value (float): Pass the value to which you want to set the property. From the method
                panel window, you can use this control as follows. - If the property
                currently showing in the Property ID ring control has constants as
                valid values, you can view a list of the constants by pressing on this
                control. Select a value by double-clicking on it or by selecting it and
                then pressing . Note: Some of the values might not be valid depending on
                the current settings of the instrument session. Default Value: none

        

#### `def _set_attribute_vi_string(self, attribute_id, attribute_value)`

_set_attribute_vi_string

        This method sets the value of a ViString property. This is a
        low-level method that you can use to set the values of
        instrument-specific properties and inherent IVI properties. If the
        property represents an instrument state, this method performs
        instrument I/O in the following cases: - State caching is disabled for
        the entire session or for the particular property. - State caching is
        enabled and the currently cached value is invalid or is different than
        the value you specify. This instrument driver contains high-level
        methods that set most of the instrument properties. It is best to use
        the high-level driver methods as much as possible. They handle order
        dependencies and multithread locking for you. In addition, they perform
        status checking only after setting all of the properties. In contrast,
        when you set multiple properties using the SetAttribute methods, the
        methods check the instrument status after each call. Also, when state
        caching is enabled, the high-level methods that configure multiple
        properties perform instrument I/O only for the properties whose value
        you change. Thus, you can safely call the high-level methods without
        the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`niswitch.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`niswitch.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_string`

        Args:
            attribute_id (int): Pass the ID of a property. From the method panel window, you can use
                this control as follows. - Click on the control or press , , or , to
                display a dialog box containing a hierarchical list of the available
                properties. Properties whose value cannot be set are dim. Help text is
                shown for each property. Select a property by double-clicking on it
                or by selecting it and then pressing . Read-only properties appear dim
                in the list box. If you select a read-only property, an error message
                appears. A ring control at the top of the dialog box allows you to see
                all IVI properties or only the properties of the ViInt32 type. If you
                choose to see all IVI properties, the data types appear to the right of
                the property names in the list box. The data types that are not
                consistent with this method are dim. If you select a property data
                type that is dim, LabWindows/CVI transfers you to the method panel for
                the corresponding method that is consistent with the data type. - If
                you want to enter a variable name, press to change this ring control to
                a manual input box. - If the property in this ring control has
                constants as valid values, you can view the constants by moving to the
                Property Value control and pressing .

            attribute_value (str): Pass the value to which you want to set the property. From the method
                panel window, you can use this control as follows. - If the property
                currently showing in the Property ID ring control has constants as
                valid values, you can view a list of the constants by pressing on this
                control. Select a value by double-clicking on it or by selecting it and
                then pressing . Note: Some of the values might not be valid depending on
                the current settings of the instrument session. Default Value: none

        

#### `def unlock(self)`

unlock

        Releases a lock that you acquired on an device session using
        lock. Refer to lock for additional
        information on session locks.
        

#### `def _error_message(self, error_code)`

_error_message

        Converts an error code returned by NI-SWITCH into a user-readable
        string. Generally this information is supplied in error out of any
        NI-SWITCH VI. Use _error_message for a static lookup of an
        error code description.

        Args:
            error_code (int): Status code returned by any NI-SWITCH method. Default Value: 0
                (VI_SUCCESS)


        Returns:
            error_message (str): The error information formatted into a string. You must pass a ViChar
                array with at least 256 bytes.

        

### `class Session(_SessionBase)`

An NI-SWITCH session to an NI switch module.

#### `def __init__(self, resource_name, topology='Configured Topology', simulate=False, reset_device=False, *, grpc_options=None)`

An NI-SWITCH session to an NI switch module.

        Returns a session handle used to identify the switch in all subsequent
        instrument driver calls and sets the topology of the switch.
        __init__ creates a new IVI instrument driver session
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

        Args:
            resource_name (str): Resource name of the switch module to initialize. Default value: None
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

            topology (str): Pass the topology name you want to use for the switch you specify with
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

            simulate (bool): Enables simulation of the switch module specified in the resource name
                parameter. Valid Values: True - simulate False - Don't simulate
                (Default Value)

            reset_device (bool): Specifies whether to reset the switch module during the initialization
                process. Valid Values: True - Reset Device (Default Value) False
                - Currently unsupported. The device will not reset.

            grpc_options (niswitch.grpc_session_options.GrpcSessionOptions): MeasurementLink gRPC session options


        Returns:
            session (niswitch.Session): A session object representing the device.

        

#### `def __enter__(self)`

#### `def __exit__(self, exc_type, exc_value, traceback)`

#### `def initiate(self)`

initiate

        Commits the configured scan list and trigger settings to hardware and
        initiates the scan. If niSwitch Commit was called earlier, niSwitch
        Initiate Scan only initiates the scan and returns immediately. Once the
        scanning operation begins, you cannot perform any other operation other
        than GetAttribute, AbortScan, or SendSoftwareTrigger. All other
        methods return NISWITCH_ERROR_SCAN_IN_PROGRESS. To stop the
        scanning operation, To stop the scanning operation, call
        abort.

        Note:
        This method will return a Python context manager that will initiate on entering and abort on exit.
        

#### `def close(self)`

close

        Terminates the NI-SWITCH session and all of its properties and
        deallocates any memory resources the driver uses. Notes: (1) You must
        unlock the session before calling _close. (2) After calling
        _close, you cannot use the instrument driver again until you
        call init or InitWithOptions.

        Note:
        One or more of the referenced methods are not in the Python API for this driver.

        Note:
        This method is not needed when using the session context manager
        

#### `def abort(self)`

abort

        Aborts the scan in progress. Initiate a scan with
        initiate. If the switch module is not scanning,
        NISWITCH_ERROR_NO_SCAN_IN_PROGRESS error is returned.
        

#### `def can_connect(self, channel1, channel2)`

can_connect

        Verifies that a path between channel 1 and channel 2 can be created. If
        a path is possible in the switch module, the availability of that path
        is returned given the existing connections. If the path is possible but
        in use, a NISWITCH_WARN_IMPLICIT_CONNECTION_EXISTS warning is
        returned.

        Args:
            channel1 (str): Input one of the channel names of the desired path. Pass the other
                channel name as the channel 2 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: ""

            channel2 (str): Input one of the channel names of the desired path. Pass the other
                channel name as the channel 1 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: ""


        Returns:
            path_capability (enums.PathCapability): Indicates whether a path is valid. Possible values include:

                - PathCapability.PATH_AVAILABLE 1
                - PathCapability.PATH_EXISTS 2
                - PathCapability.PATH_UNSUPPORTED 3
                - PathCapability.RESOURCE_IN_USE 4
                - PathCapability.SOURCE_CONFLICT 5
                - PathCapability.CHANNEL_NOT_AVAILABLE 6

                Notes: (1)
                PathCapability.PATH_AVAILABLE indicates that the driver can create the
                path at this time. (2) PathCapability.PATH_EXISTS indicates that the
                path already exists. (3) PathCapability.PATH_UNSUPPORTED indicates that
                the instrument is not capable of creating a path between the channels
                you specify. (4) PathCapability.RESOURCE_IN_USE indicates that although
                the path is valid, the driver cannot create the path at this moment
                because the switch device is currently using one or more of the required
                channels to create another path. You must destroy the other path before
                creating this one. (5) PathCapability.SOURCE_CONFLICT indicates that
                the instrument cannot create a path because both channels are connected
                to a different source channel. (6)
                PathCapability.CHANNEL_NOT_AVAILABLE indicates that the driver cannot
                create a path between the two channels because one of the channels is a
                configuration channel and thus unavailable for external connections.

        

#### `def commit(self)`

commit

        Downloads the configured scan list and trigger settings to hardware.
        Calling commit optional as it is implicitly called during
        initiate. Use commit to arm triggers in a given
        order or to control when expensive hardware operations are performed.
        

#### `def connect(self, channel1, channel2)`

connect

        Creates a path between channel 1 and channel 2. The driver calculates
        and uses the shortest path between the two channels. Refer to Immediate
        Operations for information about Channel Usage types. If a path is not
        available, the method returns one of the following errors: -
        NISWITCH_ERROR_EXPLICIT_CONNECTION_EXISTS, if the two channels are
        already explicitly connected by calling either the connect or
        set_path method. -
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

        Args:
            channel1 (str): Input one of the channel names of the desired path. Pass the other
                channel name as the channel 2 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: None

            channel2 (str): Input one of the channel names of the desired path. Pass the other
                channel name as the channel 1 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: None

        

#### `def connect_multiple(self, connection_list)`

connect_multiple

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

        Args:
            connection_list (str): Connection List specifies a list of connections between channels to
                make. NI-SWITCH validates the connection list, and aborts execution of
                the list if errors are returned. Refer to Connection and Disconnection
                List Syntax for valid connection list syntax and examples. Refer to
                Devices Overview for valid channel names for the switch module. Example
                of a valid connection list: c0 -> r1, [c2 -> r2 -> c3] In this example,
                r2 is a configuration channel. Default value: None

        

#### `def disable(self)`

disable

        Places the switch module in a quiescent state where it has minimal or no
        impact on the system to which it is connected. All channels are
        disconnected and any scan in progress is aborted.
        

#### `def disconnect(self, channel1, channel2)`

disconnect

        This method destroys the path between two channels that you create
        with the connect or set_path method. If a path is
        not connected or not available, the method returns the
        IVISWTCH_ERROR_NO_SUCH_PATH error.

        Args:
            channel1 (str): Input one of the channel names of the path to break. Pass the other
                channel name as the channel 2 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: None

            channel2 (str): Input one of the channel names of the path to break. Pass the other
                channel name as the channel 1 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: None

        

#### `def disconnect_all(self)`

disconnect_all

        Breaks all existing paths. If the switch module cannot break all paths,
        NISWITCH_WARN_PATH_REMAINS warning is returned.
        

#### `def disconnect_multiple(self, disconnection_list)`

disconnect_multiple

        Breaks the connections between channels specified in Disconnection List.
        If no connections exist between channels, NI-SWITCH returns an error. In
        the event of an error, the VI stops at the point in the list where the
        error occurred.

        Args:
            disconnection_list (str): Disconnection List specifies a list of connections between channels to
                break. NI-SWITCH validates the disconnection list, and aborts execution
                of the list if errors are returned. Refer to Connection and
                Disconnection List Syntax for valid disconnection list syntax and
                examples. Refer to Devices Overview for valid channel names for the
                switch module. Example of a valid disconnection list: c0 -> r1, [c2 ->
                r2 -> c3] In this example, r2 is a configuration channel. Default value:
                None

        

#### `def get_channel_name(self, index)`

get_channel_name

        Returns the channel string that is in the channel table at the specified
        index. Use get_channel_name in a For Loop to get a complete list
        of valid channel names for the switch module. Use the Channel Count
        property to determine the number of channels.

        Args:
            index (int): A 1-based index into the channel table. Default value: 1 Maximum value:
                Value of Channel Count property.


        Returns:
            channel_name_buffer (str): Returns the channel name that is in the channel table at the index you
                specify.

        

#### `def get_path(self, channel1, channel2)`

get_path

        Returns a string that identifies the explicit path created with
        connect. Pass this string to set_path to establish
        the exact same path in future connections. In some cases, multiple paths
        are available between two channels. When you call connect, the
        driver selects an available path. With connect, there is no
        guarantee that the driver selected path will always be the same path
        through the switch module. get_path only returns those paths
        explicitly created by niSwitch Connect Channels or set_path.
        For example, if you connect channels CH1 and CH3,and then channels CH2
        and CH3, an explicit path between channels CH1 and CH2 does not exist an
        error is returned

        Args:
            channel1 (str): Input one of the channel names of the desired path. Pass the other
                channel name as the channel 2 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: ""

            channel2 (str): Input one of the channel names of the desired path. Pass the other
                channel name as the channel 1 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: ""


        Returns:
            path (str): A string composed of comma-separated paths between channel 1 and channel
                2. The first and last names in the path are the endpoints of the path.
                All other channels in the path are configuration channels. Examples of
                returned paths: ch0->com0, com0->ab0

        

#### `def get_relay_count(self, relay_name)`

get_relay_count

        Returns the number of times the relay has changed from Closed to Open.
        Relay count is useful for tracking relay lifetime and usage. Call
        wait_for_debounce before get_relay_count to ensure an
        accurate count. Refer to the Relay Count topic in the NI Switches Help
        to determine if the switch module supports relay counting.

        Args:
            relay_name (str): Name of the relay. Default value: None Examples of valid relay names:
                ch0, ab0, 1wire, hlselect Refer to Devices Overview for a list of valid
                relay names for the switch module.


        Returns:
            relay_count (int): The number of relay cycles.

        

#### `def get_relay_name(self, index)`

get_relay_name

        Returns the relay name string that is in the relay list at the specified
        index. Use get_relay_name in a For Loop to get a complete list
        of valid relay names for the switch module. Use the Number of Relays
        property to determine the number of relays.

        Args:
            index (int): A 1-based index into the channel table. Default value: 1 Maximum value:
                Value of Channel Count property.


        Returns:
            relay_name_buffer (str): Returns the relay name for the index you specify.

        

#### `def get_relay_position(self, relay_name)`

get_relay_position

        Returns the relay position for the relay specified in the Relay Name
        parameter.

        Args:
            relay_name (str): Name of the relay. Default value: None Examples of valid relay names:
                ch0, ab0, 1wire, hlselect Refer to Devices Overview for a list of valid
                relay names for the switch module.


        Returns:
            relay_position (enums.RelayPosition): Indicates whether the relay is open or closed. RelayPosition.OPEN 10
                RelayPosition.CLOSED 11

        

#### `def _init_with_topology(self, resource_name, topology='Configured Topology', simulate=False, reset_device=False)`

_init_with_topology

        Returns a session handle used to identify the switch in all subsequent
        instrument driver calls and sets the topology of the switch.
        __init__ creates a new IVI instrument driver session
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

        Args:
            resource_name (str): Resource name of the switch module to initialize. Default value: None
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

            topology (str): Pass the topology name you want to use for the switch you specify with
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

            simulate (bool): Enables simulation of the switch module specified in the resource name
                parameter. Valid Values: True - simulate False - Don't simulate
                (Default Value)

            reset_device (bool): Specifies whether to reset the switch module during the initialization
                process. Valid Values: True - Reset Device (Default Value) False
                - Currently unsupported. The device will not reset.


        Returns:
            vi (int): A particular NI-SWITCH session established with
                __init__, InitWithOptions, or init
                and used for all subsequent NI-SWITCH calls.

                Note:
                One or more of the referenced methods are not in the Python API for this driver.

        

#### `def _initiate_scan(self)`

_initiate_scan

        Commits the configured scan list and trigger settings to hardware and
        initiates the scan. If niSwitch Commit was called earlier, niSwitch
        Initiate Scan only initiates the scan and returns immediately. Once the
        scanning operation begins, you cannot perform any other operation other
        than GetAttribute, AbortScan, or SendSoftwareTrigger. All other
        methods return NISWITCH_ERROR_SCAN_IN_PROGRESS. To stop the
        scanning operation, To stop the scanning operation, call
        abort.
        

#### `def relay_control(self, relay_name, relay_action)`

relay_control

        Controls individual relays of the switch. When controlling individual
        relays, the protection offered by setting the usage of source channels
        and configuration channels, and by enabling or disabling analog bus
        sharing on the NI SwitchBlock, does not apply. Refer to the device book
        for your switch in the NI Switches Help to determine if the switch
        supports individual relay control.

        Args:
            relay_name (str): Name of the relay. Default value: None Examples of valid relay names:
                ch0, ab0, 1wire, hlselect Refer to Devices Overview for a list of valid
                relay names for the switch module.

            relay_action (enums.RelayAction): Specifies whether to open or close a given relay. Default value: Relay
                Close Defined values: RelayAction.OPEN
                RelayAction.CLOSE (Default Value)

        

#### `def reset_with_defaults(self)`

reset_with_defaults

        Resets the switch module and applies initial user specified settings
        from the logical name used to initialize the session. If the session was
        created without a logical name, this method is equivalent to
        reset.
        

#### `def route_scan_advanced_output(self, scan_advanced_output_connector, scan_advanced_output_bus_line, invert=False)`

route_scan_advanced_output

        Routes the scan advanced output trigger from a trigger bus line (TTLx)
        to the front or rear connector.

        Args:
            scan_advanced_output_connector (enums.ScanAdvancedOutput): The scan advanced trigger destination. Valid locations are the
                ScanAdvancedOutput.FRONTCONNECTOR and ScanAdvancedOutput.REARCONNECTOR. Default
                value: ScanAdvancedOutput.FRONTCONNECTOR

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            scan_advanced_output_bus_line (enums.ScanAdvancedOutput): The trigger line to route the scan advanced output trigger from the
                front or rear connector. Select ScanAdvancedOutput.NONE to break an existing
                route. Default value: None Valid Values: ScanAdvancedOutput.NONE
                ScanAdvancedOutput.TTL0 ScanAdvancedOutput.TTL1 ScanAdvancedOutput.TTL2
                ScanAdvancedOutput.TTL3 ScanAdvancedOutput.TTL4 ScanAdvancedOutput.TTL5
                ScanAdvancedOutput.TTL6 ScanAdvancedOutput.TTL7

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            invert (bool): If True, inverts the input trigger signal from falling to rising or
                vice versa. Default value: False

        

#### `def route_trigger_input(self, trigger_input_connector, trigger_input_bus_line, invert=False)`

route_trigger_input

        Routes the input trigger from the front or rear connector to a trigger
        bus line (TTLx). To disconnect the route, call this method again and
        specify None for trigger bus line parameter.

        Args:
            trigger_input_connector (enums.TriggerInput): The location of the input trigger source on the switch module. Valid
                locations are the TriggerInput.FRONTCONNECTOR and
                TriggerInput.REARCONNECTOR. Default value:
                TriggerInput.FRONTCONNECTOR

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            trigger_input_bus_line (enums.TriggerInput): The trigger line to route the input trigger. Select NISWITCH_VAL_NONE
                to break an existing route. Default value: None Valid Values:
                NISWITCH_VAL_NONE TriggerInput.TTL0 TriggerInput.TTL1
                TriggerInput.TTL2 TriggerInput.TTL3 TriggerInput.TTL4
                TriggerInput.TTL5 TriggerInput.TTL6 TriggerInput.TTL7

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            invert (bool): If True, inverts the input trigger signal from falling to rising or
                vice versa. Default value: False

        

#### `def send_software_trigger(self)`

send_software_trigger

        Sends a software trigger to the switch module specified in the NI-SWITCH
        session. When the trigger input is set to TriggerInput.SOFTWARE_TRIG
        through either the ConfigureScanTrigger or the
        trigger_input property, the scan does not proceed from
        a semi-colon (wait for trigger) until send_software_trigger is
        called.

        Note:
        One or more of the referenced methods are not in the Python API for this driver.
        

#### `def set_path(self, path_list)`

set_path

        Connects two channels by specifying an explicit path in the path list
        parameter. set_path is particularly useful where path
        repeatability is important, such as in calibrated signal paths. If this
        is not necessary, use connect.

        Args:
            path_list (str): A string composed of comma-separated paths between channel 1 and channel
                2. The first and last names in the path are the endpoints of the path.
                Every other channel in the path are configuration channels. Example of a
                valid path list string: ch0->com0, com0->ab0. In this example, com0 is a
                configuration channel. Default value: None Obtain the path list for a
                previously created path with get_path.

        

#### `def wait_for_debounce(self, maximum_time_ms=hightime.timedelta(milliseconds=5000))`

wait_for_debounce

        Pauses until all created paths have settled. If the time you specify
        with the Maximum Time (ms) parameter elapsed before the switch paths
        have settled, this method returns the
        NISWITCH_ERROR_MAX_TIME_EXCEEDED error.

        Args:
            maximum_time_ms (hightime.timedelta, datetime.timedelta, or int in milliseconds): Specifies the maximum length of time to wait for all relays in the
                switch module to activate or deactivate. If the specified time elapses
                before all relays active or deactivate, a timeout error is returned.
                Default Value:5000 ms

        

#### `def wait_for_scan_complete(self, maximum_time_ms=hightime.timedelta(milliseconds=5000))`

wait_for_scan_complete

        Pauses until the switch module stops scanning or the maximum time has
        elapsed and returns a timeout error. If the time you specify with the
        Maximum Time (ms) parameter elapsed before the scanning operation has
        finished, this method returns the NISWITCH_ERROR_MAX_TIME_EXCEEDED
        error.

        Args:
            maximum_time_ms (hightime.timedelta, datetime.timedelta, or int in milliseconds): Specifies the maximum length of time to wait for the switch module to
                stop scanning. If the specified time elapses before the scan ends,
                NISWITCH_ERROR_MAX_TIME_EXCEEDED error is returned. Default
                Value:5000 ms

        

#### `def _close(self)`

_close

        Terminates the NI-SWITCH session and all of its properties and
        deallocates any memory resources the driver uses. Notes: (1) You must
        unlock the session before calling _close. (2) After calling
        _close, you cannot use the instrument driver again until you
        call init or InitWithOptions.

        Note:
        One or more of the referenced methods are not in the Python API for this driver.
        

#### `def self_test(self)`

self_test

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
        

#### `def reset(self)`

reset

        Disconnects all created paths and returns the switch module to the state
        at initialization. Configuration channel and source channel settings
        remain unchanged.
        

#### `def _self_test(self)`

_self_test

        Verifies that the driver can communicate with the switch module.

        Returns:
            self_test_result (int): Value returned from the switch device self-test. Passed 0 Failed 1

            self_test_message (str): Self-test response string from the switch device. You must pass a ViChar
                array with at least 256 bytes.

        

<!--NI_PYTHON_API repo=nimi-python path=generated/niswitch/niswitch/unit_tests/_matchers.py -->
## PYTHON MODULE: generated/niswitch/niswitch/unit_tests/_matchers.py

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

<!--NI_PYTHON_API repo=nimi-python path=generated/niswitch/niswitch/unit_tests/_mock_helper.py -->
## PYTHON MODULE: generated/niswitch/niswitch/unit_tests/_mock_helper.py

### `class MockFunctionCallError(Exception)`

#### `def __init__(self, function, param=None)`

### `class SideEffectsHelper(object)`

#### `def __init__(self)`

#### `def __getitem__(self, func)`

#### `def __setitem__(self, func, val)`

#### `def niSwitch_AbortScan(self, vi)`

#### `def niSwitch_CanConnect(self, vi, channel1, channel2, path_capability)`

#### `def niSwitch_Commit(self, vi)`

#### `def niSwitch_Connect(self, vi, channel1, channel2)`

#### `def niSwitch_ConnectMultiple(self, vi, connection_list)`

#### `def niSwitch_Disable(self, vi)`

#### `def niSwitch_Disconnect(self, vi, channel1, channel2)`

#### `def niSwitch_DisconnectAll(self, vi)`

#### `def niSwitch_DisconnectMultiple(self, vi, disconnection_list)`

#### `def niSwitch_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niSwitch_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niSwitch_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niSwitch_GetAttributeViString(self, vi, channel_name, attribute_id, array_size, attribute_value)`

#### `def niSwitch_GetChannelName(self, vi, index, buffer_size, channel_name_buffer)`

#### `def niSwitch_GetError(self, vi, error_code, buffer_size, description)`

#### `def niSwitch_GetPath(self, vi, channel1, channel2, buffer_size, path)`

#### `def niSwitch_GetRelayCount(self, vi, relay_name, relay_count)`

#### `def niSwitch_GetRelayName(self, vi, index, relay_name_buffer_size, relay_name_buffer)`

#### `def niSwitch_GetRelayPosition(self, vi, relay_name, relay_position)`

#### `def niSwitch_InitWithTopology(self, resource_name, topology, simulate, reset_device, vi)`

#### `def niSwitch_InitiateScan(self, vi)`

#### `def niSwitch_LockSession(self, vi, caller_has_lock)`

#### `def niSwitch_RelayControl(self, vi, relay_name, relay_action)`

#### `def niSwitch_ResetWithDefaults(self, vi)`

#### `def niSwitch_RouteScanAdvancedOutput(self, vi, scan_advanced_output_connector, scan_advanced_output_bus_line, invert)`

#### `def niSwitch_RouteTriggerInput(self, vi, trigger_input_connector, trigger_input_bus_line, invert)`

#### `def niSwitch_SendSoftwareTrigger(self, vi)`

#### `def niSwitch_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niSwitch_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niSwitch_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niSwitch_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niSwitch_SetPath(self, vi, path_list)`

#### `def niSwitch_SetRuntimeEnvironment(self, environment, environment_version, reserved1, reserved2)`

#### `def niSwitch_UnlockSession(self, vi, caller_has_lock)`

#### `def niSwitch_WaitForDebounce(self, vi, maximum_time_ms)`

#### `def niSwitch_WaitForScanComplete(self, vi, maximum_time_ms)`

#### `def niSwitch_close(self, vi)`

#### `def niSwitch_error_message(self, vi, error_code, error_message)`

#### `def niSwitch_reset(self, vi)`

#### `def niSwitch_self_test(self, vi, self_test_result, self_test_message)`

#### `def set_side_effects_and_return_values(self, mock_library)`

<!--NI_PYTHON_API repo=nimi-python path=generated/niswitch/setup.py -->
## PYTHON MODULE: generated/niswitch/setup.py

### `def read_contents(file_to_read)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nitclk/nitclk/__init__.py -->
## PYTHON MODULE: generated/nitclk/nitclk/__init__.py

### `def get_diagnostic_information()`

Get diagnostic information about the system state that is suitable for printing or logging

    returns: dict

    note: Python bitness may be incorrect when running in a virtual environment
    

### `def print_diagnostic_information()`

Print diagnostic information in a format suitable for issue report

    note: Python bitness may be incorrect when running in a virtual environment
    

<!--NI_PYTHON_API repo=nimi-python path=generated/nitclk/nitclk/_attributes.py -->
## PYTHON MODULE: generated/nitclk/nitclk/_attributes.py

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

Class for attributes that use enums internally but are exposed in the nitclk Python module as something else, thus need conversion.

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

<!--NI_PYTHON_API repo=nimi-python path=generated/nitclk/nitclk/_converters.py -->
## PYTHON MODULE: generated/nitclk/nitclk/_converters.py

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
    

### `def convert_to_nitclk_session_number(item)`

Convert from supported objects to NI-TClk Session Num

    Supported objects are:
    - class with .tclk object of type nitclk.SessionReference
    - nitclk.SessionReference
    

### `def convert_to_nitclk_session_number_list(item_list)`

Converts a list of items to nitclk session nums

<!--NI_PYTHON_API repo=nimi-python path=generated/nitclk/nitclk/_library.py -->
## PYTHON MODULE: generated/nitclk/nitclk/_library.py

### `class Library(object)`

Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    

#### `def __init__(self, ctypes_library)`

#### `def _get_library_function(self, name)`

#### `def niTClk_ConfigureForHomogeneousTriggers(self, session_count, sessions)`

#### `def niTClk_FinishSyncPulseSenderSynchronize(self, session_count, sessions, min_time)`

#### `def niTClk_GetAttributeViReal64(self, session, channel_name, attribute_id, value)`

#### `def niTClk_GetAttributeViSession(self, session, channel_name, attribute_id, value)`

#### `def niTClk_GetAttributeViString(self, session, channel_name, attribute_id, buf_size, value)`

#### `def niTClk_GetExtendedErrorInfo(self, error_string, error_string_size)`

#### `def niTClk_Initiate(self, session_count, sessions)`

#### `def niTClk_IsDone(self, session_count, sessions, done)`

#### `def niTClk_SetAttributeViReal64(self, session, channel_name, attribute_id, value)`

#### `def niTClk_SetAttributeViSession(self, session, channel_name, attribute_id, value)`

#### `def niTClk_SetAttributeViString(self, session, channel_name, attribute_id, value)`

#### `def niTClk_SetupForSyncPulseSenderSynchronize(self, session_count, sessions, min_time)`

#### `def niTClk_Synchronize(self, session_count, sessions, min_tclk_period)`

#### `def niTClk_SynchronizeToSyncPulseSender(self, session_count, sessions, min_time)`

#### `def niTClk_WaitUntilDone(self, session_count, sessions, timeout)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nitclk/nitclk/_library_interpreter.py -->
## PYTHON MODULE: generated/nitclk/nitclk/_library_interpreter.py

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
        

#### `def configure_for_homogeneous_triggers(self, sessions)`

#### `def finish_sync_pulse_sender_synchronize(self, sessions, min_time)`

#### `def get_attribute_vi_real64(self, channel_name, attribute_id)`

#### `def get_attribute_vi_session(self, channel_name, attribute_id)`

#### `def get_attribute_vi_string(self, channel_name, attribute_id)`

#### `def get_extended_error_info(self)`

#### `def initiate(self, sessions)`

#### `def is_done(self, sessions)`

#### `def set_attribute_vi_real64(self, channel_name, attribute_id, value)`

#### `def set_attribute_vi_session(self, channel_name, attribute_id, value)`

#### `def set_attribute_vi_string(self, channel_name, attribute_id, value)`

#### `def setup_for_sync_pulse_sender_synchronize(self, sessions, min_time)`

#### `def synchronize(self, sessions, min_tclk_period)`

#### `def synchronize_to_sync_pulse_sender(self, sessions, min_time)`

#### `def wait_until_done(self, sessions, timeout)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nitclk/nitclk/_library_singleton.py -->
## PYTHON MODULE: generated/nitclk/nitclk/_library_singleton.py

### `def _get_library_name()`

### `def _get_library_type()`

### `def get()`

get

    Returns the library.Library singleton for nitclk.
    

<!--NI_PYTHON_API repo=nimi-python path=generated/nitclk/nitclk/errors.py -->
## PYTHON MODULE: generated/nitclk/nitclk/errors.py

### `def _is_success(code)`

### `def _is_error(code)`

### `def _is_warning(code)`

### `class Error(Exception)`

Base error class for NI-TClk

#### `def __init__(self, message)`

### `class DriverError(Error)`

An error originating from the NI-TClk driver

#### `def __init__(self, code, description)`

### `class DriverWarning(Warning)`

A warning originating from the NI-TClk driver

#### `def __init__(self, code, description)`

### `class UnsupportedConfigurationError(Error)`

An error due to using this module in an usupported platform.

#### `def __init__(self)`

### `class DriverNotInstalledError(Error)`

An error due to using this module without the driver runtime installed.

#### `def __init__(self)`

### `class DriverTooOldError(Error)`

An error due to using this module with an older version of the NI-TClk driver runtime.

#### `def __init__(self)`

### `class DriverTooNewError(Error)`

An error due to the NI-TClk driver runtime being too new for this module.

#### `def __init__(self)`

### `def handle_error(library_interpreter, code, ignore_warnings, is_error_handling)`

handle_error

    Helper function for handling errors returned by nitclk.Library.
    It calls back into the LibraryInterpreter to get the corresponding error
    description and raises if necessary.
    

<!--NI_PYTHON_API repo=nimi-python path=generated/nitclk/nitclk/session.py -->
## PYTHON MODULE: generated/nitclk/nitclk/session.py

### `class SessionReference(object)`

Properties container for NI-TClk attributes.

    Note: Constructing this class is an advanced use case and should not be needed in most circumstances.
    

#### `def __init__(self, session_number, encoding='windows-1251')`

#### `def __repr__(self)`

#### `def __setattr__(self, key, value)`

#### `def _get_tclk_session_reference(self)`

#### `def _get_attribute_vi_real64(self, attribute_id)`

_get_attribute_vi_real64

        Gets the value of an NI-TClk ViReal64 property.

        Tip:
        This method can be called on specific channels within your :py:class:`nitclk.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nitclk.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_real64`

        Args:
            attribute_id (int): The ID of the property that you want to get Supported Property
                sample_clock_delay


        Returns:
            value (float): The value that you are getting

        

#### `def _get_attribute_vi_session(self, attribute_id)`

_get_attribute_vi_session

        Gets the value of an NI-TClk ViSession property.

        Tip:
        This method can be called on specific channels within your :py:class:`nitclk.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_session`

        To call the method on all channels, you can call it directly on the :py:class:`nitclk.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_session`

        Args:
            attribute_id (int): The ID of the property that you want to set Supported Properties
                start_trigger_master_session
                ref_trigger_master_session
                pause_trigger_master_session


        Returns:
            value (int): The value that you are getting

        

#### `def _get_attribute_vi_string(self, attribute_id)`

_get_attribute_vi_string

        This method queries the value of an NI-TClk ViString property. You
        must provide a ViChar array to serve as a buffer for the value. You pass
        the number of bytes in the buffer as bufSize. If the current value of
        the property, including the terminating NULL byte, is larger than the
        size you indicate in bufSize, the method copies bufSize minus 1 bytes
        into the buffer, places an ASCII NULL byte at the end of the buffer, and
        returns the array size that you must pass to get the entire value. For
        example, if the value is "123456" and bufSize is 4, the method places
        "123" into the buffer and returns 7. If you want to call
        _get_attribute_vi_string just to get the required array size, pass 0
        for bufSize and VI_NULL for the value.

        Tip:
        This method can be called on specific channels within your :py:class:`nitclk.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nitclk.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_string`

        Args:
            attribute_id (int): The ID of the property that you want to get Supported Properties
                sync_pulse_source
                sync_pulse_clock_source
                exported_sync_pulse_output_terminal


        Returns:
            value (str): The value that you are getting

        

#### `def _set_attribute_vi_real64(self, attribute_id, value)`

_set_attribute_vi_real64

        Sets the value of an NI-TClk VIReal64 property.
        _set_attribute_vi_real64 is a low-level method that you can use to
        set the values NI-TClk properties. NI-TClk contains high-level methods
        that set most of the properties. It is best to use the high-level
        methods as much as possible.

        Tip:
        This method can be called on specific channels within your :py:class:`nitclk.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nitclk.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_real64`

        Args:
            attribute_id (int): The ID of the property that you want to set Supported Property
                sample_clock_delay

            value (float): The value for the property

        

#### `def _set_attribute_vi_session(self, attribute_id, value)`

_set_attribute_vi_session

        Sets the value of an NI-TClk ViSession property.
        _set_attribute_vi_session is a low-level method that you can use
        to set the values NI-TClk properties. NI-TClk contains high-level
        methods that set most of the properties. It is best to use the
        high-level methods as much as possible.

        Tip:
        This method can be called on specific channels within your :py:class:`nitclk.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_session`

        To call the method on all channels, you can call it directly on the :py:class:`nitclk.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_session`

        Args:
            attribute_id (int): The ID of the property that you want to set Supported Properties
                start_trigger_master_session
                ref_trigger_master_session
                pause_trigger_master_session

            value (int): The value for the property

        

#### `def _set_attribute_vi_string(self, attribute_id, value)`

_set_attribute_vi_string

        Sets the value of an NI-TClk VIString property.
        _set_attribute_vi_string is a low-level method that you can use to
        set the values of NI-TClk properties. NI-TClk contain high-level
        methods that set most of the properties. It is best to use the
        high-level methods as much as possible.

        Tip:
        This method can be called on specific channels within your :py:class:`nitclk.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nitclk.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_string`

        Args:
            attribute_id (int): Pass the ID of the property that you want to set Supported Properties
                sync_pulse_source
                sync_pulse_clock_source
                exported_sync_pulse_output_terminal

            value (str): Pass the value for the property

        

### `class _Session(object)`

Private class

    This class allows reusing function templates that are used in all other drivers. If
    we don't do this, we would need new template(s) that the only difference is in the
    indentation.
    

#### `def __init__(self)`

#### `def configure_for_homogeneous_triggers(self, sessions)`

configure_for_homogeneous_triggers

        Configures the properties commonly required for the TClk synchronization
        of device sessions with homogeneous triggers in a single PXI chassis or
        a single PC. Use configure_for_homogeneous_triggers to configure
        the properties for the reference clocks, start triggers, reference
        triggers, script triggers, and pause triggers. If
        configure_for_homogeneous_triggers cannot perform all the steps
        appropriate for the given sessions, it returns an error. If an error is
        returned, use the instrument driver methods and properties for signal
        routing, along with the following NI-TClk properties:
        start_trigger_master_session
        ref_trigger_master_session
        pause_trigger_master_session
        configure_for_homogeneous_triggers affects the following clocks and
        triggers: - Reference clocks - Start triggers - Reference triggers -
        Script triggers - Pause triggers Reference Clocks
        configure_for_homogeneous_triggers configures the reference clocks
        if they are needed. Specifically, if the internal sample clocks or
        internal sample clock timebases are used, and the reference clock source
        is not configured--or is set to None (no trigger
        configured)--configure_for_homogeneous_triggers configures the
        following: PXI--The reference clock source on all devices is set to be
        the 10 MHz PXI backplane clock (PXI_CLK10). PCI--One of the devices
        exports its 10 MHz onboard reference clock to RTSI 7. The reference
        clock source on all devices is set to be RTSI 7. Note: If the reference
        clock source is set to a value other than None,
        configure_for_homogeneous_triggers cannot configure the reference
        clock source. Start Triggers If the start trigger is set to None (no
        trigger configured) for all sessions, the sessions are configured to
        share the start trigger. The start trigger is shared by: - Implicitly
        exporting the start trigger from one session - Configuring the other
        sessions for digital edge start triggers with sources corresponding to
        the exported start trigger - Setting
        start_trigger_master_session to the session that is
        exporting the trigger for all sessions If the start triggers are None
        for all except one session, configure_for_homogeneous_triggers
        configures the sessions to share the start trigger from the one excepted
        session. The start trigger is shared by: - Implicitly exporting start
        trigger from the session with the start trigger that is not None -
        Configuring the other sessions for digital-edge start triggers with
        sources corresponding to the exported start trigger - Setting
        start_trigger_master_session to the session that is
        exporting the trigger for all sessions If start triggers are configured
        for all sessions, configure_for_homogeneous_triggers does not
        affect the start triggers. Start triggers are considered to be
        configured for all sessions if either of the following conditions is
        true: - No session has a start trigger that is None - One session has a
        start trigger that is None, and all other sessions have start triggers
        other than None. The one session with the None trigger must have
        start_trigger_master_session set to itself, indicating
        that the session itself is the start trigger master Reference Triggers
        configure_for_homogeneous_triggers configures sessions that support
        reference triggers to share the reference triggers if the reference
        triggers are None (no trigger configured) for all except one session.
        The reference triggers are shared by: - Implicitly exporting the
        reference trigger from the session whose reference trigger is not None -
        Configuring the other sessions that support the reference trigger for
        digital-edge reference triggers with sources corresponding to the
        exported reference trigger - Setting
        ref_trigger_master_session to the session that is
        exporting the trigger for all sessions that support reference trigger If
        the reference triggers are configured for all sessions that support
        reference triggers, configure_for_homogeneous_triggers does not
        affect the reference triggers. Reference triggers are considered to be
        configured for all sessions if either one or the other of the following
        conditions is true: - No session has a reference trigger that is None -
        One session has a reference trigger that is None, and all other sessions
        have reference triggers other than None. The one session with the None
        trigger must have ref_trigger_master_session set to
        itself, indicating that the session itself is the reference trigger
        master Reference Trigger Holdoffs Acquisition sessions may be configured
        with the reference trigger. For acquisition sessions, when the reference
        trigger is shared, configure_for_homogeneous_triggers configures
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
        configure_for_homogeneous_triggers configures generation sessions
        that support pause triggers to share them, if the pause triggers are
        None (no trigger configured) for all except one session. The pause
        triggers are shared by: - Implicitly exporting the pause trigger from
        the session whose script trigger is not None - Configuring the other
        sessions that support the pause trigger for digital-edge pause triggers
        with sources corresponding to the exported pause trigger - Setting
        pause_trigger_master_session to the session that is
        exporting the trigger for all sessions that support script triggers If
        the pause triggers are configured for all generation sessions that
        support pause triggers, configure_for_homogeneous_triggers does not
        affect pause triggers. Pause triggers are considered to be configured
        for all sessions if either one or the other of the following conditions
        is true: - No session has a pause trigger that is None - One session has
        a pause trigger that is None and all other sessions have pause triggers
        other than None. The one session with the None trigger must have
        pause_trigger_master_session set to itself, indicating
        that the session itself is the pause trigger master Note: TClk
        synchronization is not supported for pause triggers on acquisition
        sessions.

        Args:
            sessions (list of instrument-specific sessions or nitclk.SessionReference instances): sessions is an array of sessions that are being synchronized.

        

#### `def finish_sync_pulse_sender_synchronize(self, sessions, min_time=hightime.timedelta(seconds=0.0))`

finish_sync_pulse_sender_synchronize

        Finishes synchronizing the Sync Pulse Sender.

        Args:
            sessions (list of instrument-specific sessions or nitclk.SessionReference instances): sessions is an array of sessions that are being synchronized.

            min_time (hightime.timedelta, datetime.timedelta, or float in seconds): Minimal period of TClk, expressed in seconds. Supported values are
                between 0.0 s and 0.050 s (50 ms). Minimal period for a single
                chassis/PC is 200 ns. If the specified value is less than 200 ns,
                NI-TClk automatically coerces minTime to 200 ns. For multichassis
                synchronization, adjust this value to account for propagation delays
                through the various devices and cables.

        

#### `def initiate(self, sessions)`

initiate

        Initiates the acquisition or generation sessions specified, taking into
        consideration any special requirements needed for synchronization. For
        example, the session exporting the TClk-synchronized start trigger is
        not initiated until after initiate initiates all the sessions
        that import the TClk-synchronized start trigger.

        Args:
            sessions (list of instrument-specific sessions or nitclk.SessionReference instances): sessions is an array of sessions that are being synchronized.

        

#### `def is_done(self, sessions)`

is_done

        Monitors the progress of the acquisitions and/or generations
        corresponding to sessions.

        Args:
            sessions (list of instrument-specific sessions or nitclk.SessionReference instances): sessions is an array of sessions that are being synchronized.


        Returns:
            done (bool): Indicates that the operation is done. The operation is done when each
                session has completed without any errors or when any one of the sessions
                reports an error.

        

#### `def setup_for_sync_pulse_sender_synchronize(self, sessions, min_time=hightime.timedelta(seconds=0.0))`

setup_for_sync_pulse_sender_synchronize

        Configures the TClks on all the devices and prepares the Sync Pulse Sender for synchronization

        Args:
            sessions (list of instrument-specific sessions or nitclk.SessionReference instances): sessions is an array of sessions that are being synchronized.

            min_time (hightime.timedelta, datetime.timedelta, or float in seconds): Minimal period of TClk, expressed in seconds. Supported values are
                between 0.0 s and 0.050 s (50 ms). Minimal period for a single
                chassis/PC is 200 ns. If the specified value is less than 200 ns,
                NI-TClk automatically coerces minTime to 200 ns. For multichassis
                synchronization, adjust this value to account for propagation delays
                through the various devices and cables.

        

#### `def synchronize(self, sessions, min_tclk_period=hightime.timedelta(seconds=0.0))`

synchronize

        Synchronizes the TClk signals on the given sessions. After
        synchronize executes, TClk signals from all sessions are
        synchronized. Note: Before using this NI-TClk method, verify that your
        system is configured as specified in the PXI Trigger Lines and RTSI
        Lines topic of the NI-TClk Synchronization Help. You can locate this
        help file at Start>>Programs>>National Instruments>>NI-TClk.

        Args:
            sessions (list of instrument-specific sessions or nitclk.SessionReference instances): sessions is an array of sessions that are being synchronized.

            min_tclk_period (hightime.timedelta, datetime.timedelta, or float in seconds): Minimal period of TClk, expressed in seconds. Supported values are
                between 0.0 s and 0.050 s (50 ms). Minimal period for a single
                chassis/PC is 200 ns. If the specified value is less than 200 ns,
                NI-TClk automatically coerces minTime to 200 ns. For multichassis
                synchronization, adjust this value to account for propagation delays
                through the various devices and cables.

        

#### `def synchronize_to_sync_pulse_sender(self, sessions, min_time=hightime.timedelta(seconds=0.0))`

synchronize_to_sync_pulse_sender

        Synchronizes the other devices to the Sync Pulse Sender.

        Args:
            sessions (list of instrument-specific sessions or nitclk.SessionReference instances): sessions is an array of sessions that are being synchronized.

            min_time (hightime.timedelta, datetime.timedelta, or float in seconds): Minimal period of TClk, expressed in seconds. Supported values are
                between 0.0 s and 0.050 s (50 ms). Minimal period for a single
                chassis/PC is 200 ns. If the specified value is less than 200 ns,
                NI-TClk automatically coerces minTime to 200 ns. For multichassis
                synchronization, adjust this value to account for propagation delays
                through the various devices and cables.

        

#### `def wait_until_done(self, sessions, timeout=hightime.timedelta(seconds=0.0))`

wait_until_done

        Call this method to pause execution of your program until the
        acquisitions and/or generations corresponding to sessions are done or
        until the method returns a timeout error. wait_until_done is a
        blocking method that periodically checks the operation status. It
        returns control to the calling program if the operation completes
        successfully or an error occurs (including a timeout error). This
        method is most useful for finite data operations that you expect to
        complete within a certain time.

        Args:
            sessions (list of instrument-specific sessions or nitclk.SessionReference instances): sessions is an array of sessions that are being synchronized.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): The amount of time in seconds that wait_until_done waits for the
                sessions to complete. If timeout is exceeded, wait_until_done
                returns an error.

        

### `def configure_for_homogeneous_triggers(sessions)`

configure_for_homogeneous_triggers

    Configures the properties commonly required for the TClk synchronization
    of device sessions with homogeneous triggers in a single PXI chassis or
    a single PC. Use configure_for_homogeneous_triggers to configure
    the properties for the reference clocks, start triggers, reference
    triggers, script triggers, and pause triggers. If
    configure_for_homogeneous_triggers cannot perform all the steps
    appropriate for the given sessions, it returns an error. If an error is
    returned, use the instrument driver methods and properties for signal
    routing, along with the following NI-TClk properties:
    start_trigger_master_session
    ref_trigger_master_session
    pause_trigger_master_session
    configure_for_homogeneous_triggers affects the following clocks and
    triggers: - Reference clocks - Start triggers - Reference triggers -
    Script triggers - Pause triggers Reference Clocks
    configure_for_homogeneous_triggers configures the reference clocks
    if they are needed. Specifically, if the internal sample clocks or
    internal sample clock timebases are used, and the reference clock source
    is not configured--or is set to None (no trigger
    configured)--configure_for_homogeneous_triggers configures the
    following: PXI--The reference clock source on all devices is set to be
    the 10 MHz PXI backplane clock (PXI_CLK10). PCI--One of the devices
    exports its 10 MHz onboard reference clock to RTSI 7. The reference
    clock source on all devices is set to be RTSI 7. Note: If the reference
    clock source is set to a value other than None,
    configure_for_homogeneous_triggers cannot configure the reference
    clock source. Start Triggers If the start trigger is set to None (no
    trigger configured) for all sessions, the sessions are configured to
    share the start trigger. The start trigger is shared by: - Implicitly
    exporting the start trigger from one session - Configuring the other
    sessions for digital edge start triggers with sources corresponding to
    the exported start trigger - Setting
    start_trigger_master_session to the session that is
    exporting the trigger for all sessions If the start triggers are None
    for all except one session, configure_for_homogeneous_triggers
    configures the sessions to share the start trigger from the one excepted
    session. The start trigger is shared by: - Implicitly exporting start
    trigger from the session with the start trigger that is not None -
    Configuring the other sessions for digital-edge start triggers with
    sources corresponding to the exported start trigger - Setting
    start_trigger_master_session to the session that is
    exporting the trigger for all sessions If start triggers are configured
    for all sessions, configure_for_homogeneous_triggers does not
    affect the start triggers. Start triggers are considered to be
    configured for all sessions if either of the following conditions is
    true: - No session has a start trigger that is None - One session has a
    start trigger that is None, and all other sessions have start triggers
    other than None. The one session with the None trigger must have
    start_trigger_master_session set to itself, indicating
    that the session itself is the start trigger master Reference Triggers
    configure_for_homogeneous_triggers configures sessions that support
    reference triggers to share the reference triggers if the reference
    triggers are None (no trigger configured) for all except one session.
    The reference triggers are shared by: - Implicitly exporting the
    reference trigger from the session whose reference trigger is not None -
    Configuring the other sessions that support the reference trigger for
    digital-edge reference triggers with sources corresponding to the
    exported reference trigger - Setting
    ref_trigger_master_session to the session that is
    exporting the trigger for all sessions that support reference trigger If
    the reference triggers are configured for all sessions that support
    reference triggers, configure_for_homogeneous_triggers does not
    affect the reference triggers. Reference triggers are considered to be
    configured for all sessions if either one or the other of the following
    conditions is true: - No session has a reference trigger that is None -
    One session has a reference trigger that is None, and all other sessions
    have reference triggers other than None. The one session with the None
    trigger must have ref_trigger_master_session set to
    itself, indicating that the session itself is the reference trigger
    master Reference Trigger Holdoffs Acquisition sessions may be configured
    with the reference trigger. For acquisition sessions, when the reference
    trigger is shared, configure_for_homogeneous_triggers configures
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
    configure_for_homogeneous_triggers configures generation sessions
    that support pause triggers to share them, if the pause triggers are
    None (no trigger configured) for all except one session. The pause
    triggers are shared by: - Implicitly exporting the pause trigger from
    the session whose script trigger is not None - Configuring the other
    sessions that support the pause trigger for digital-edge pause triggers
    with sources corresponding to the exported pause trigger - Setting
    pause_trigger_master_session to the session that is
    exporting the trigger for all sessions that support script triggers If
    the pause triggers are configured for all generation sessions that
    support pause triggers, configure_for_homogeneous_triggers does not
    affect pause triggers. Pause triggers are considered to be configured
    for all sessions if either one or the other of the following conditions
    is true: - No session has a pause trigger that is None - One session has
    a pause trigger that is None and all other sessions have pause triggers
    other than None. The one session with the None trigger must have
    pause_trigger_master_session set to itself, indicating
    that the session itself is the pause trigger master Note: TClk
    synchronization is not supported for pause triggers on acquisition
    sessions.

    Args:
        sessions (list of instrument-specific sessions or nitclk.SessionReference instances): sessions is an array of sessions that are being synchronized.

    

### `def finish_sync_pulse_sender_synchronize(sessions, min_time)`

finish_sync_pulse_sender_synchronize

    Finishes synchronizing the Sync Pulse Sender.

    Args:
        sessions (list of instrument-specific sessions or nitclk.SessionReference instances): sessions is an array of sessions that are being synchronized.

        min_time (hightime.timedelta, datetime.timedelta, or float in seconds): Minimal period of TClk, expressed in seconds. Supported values are
            between 0.0 s and 0.050 s (50 ms). Minimal period for a single
            chassis/PC is 200 ns. If the specified value is less than 200 ns,
            NI-TClk automatically coerces minTime to 200 ns. For multichassis
            synchronization, adjust this value to account for propagation delays
            through the various devices and cables.

    

### `def initiate(sessions)`

initiate

    Initiates the acquisition or generation sessions specified, taking into
    consideration any special requirements needed for synchronization. For
    example, the session exporting the TClk-synchronized start trigger is
    not initiated until after initiate initiates all the sessions
    that import the TClk-synchronized start trigger.

    Args:
        sessions (list of instrument-specific sessions or nitclk.SessionReference instances): sessions is an array of sessions that are being synchronized.

    

### `def is_done(sessions)`

is_done

    Monitors the progress of the acquisitions and/or generations
    corresponding to sessions.

    Args:
        sessions (list of instrument-specific sessions or nitclk.SessionReference instances): sessions is an array of sessions that are being synchronized.


    Returns:
        done (bool): Indicates that the operation is done. The operation is done when each
            session has completed without any errors or when any one of the sessions
            reports an error.

    

### `def setup_for_sync_pulse_sender_synchronize(sessions, min_time)`

setup_for_sync_pulse_sender_synchronize

    Configures the TClks on all the devices and prepares the Sync Pulse Sender for synchronization

    Args:
        sessions (list of instrument-specific sessions or nitclk.SessionReference instances): sessions is an array of sessions that are being synchronized.

        min_time (hightime.timedelta, datetime.timedelta, or float in seconds): Minimal period of TClk, expressed in seconds. Supported values are
            between 0.0 s and 0.050 s (50 ms). Minimal period for a single
            chassis/PC is 200 ns. If the specified value is less than 200 ns,
            NI-TClk automatically coerces minTime to 200 ns. For multichassis
            synchronization, adjust this value to account for propagation delays
            through the various devices and cables.

    

### `def synchronize(sessions, min_tclk_period)`

synchronize

    Synchronizes the TClk signals on the given sessions. After
    synchronize executes, TClk signals from all sessions are
    synchronized. Note: Before using this NI-TClk method, verify that your
    system is configured as specified in the PXI Trigger Lines and RTSI
    Lines topic of the NI-TClk Synchronization Help. You can locate this
    help file at Start>>Programs>>National Instruments>>NI-TClk.

    Args:
        sessions (list of instrument-specific sessions or nitclk.SessionReference instances): sessions is an array of sessions that are being synchronized.

        min_tclk_period (hightime.timedelta, datetime.timedelta, or float in seconds): Minimal period of TClk, expressed in seconds. Supported values are
            between 0.0 s and 0.050 s (50 ms). Minimal period for a single
            chassis/PC is 200 ns. If the specified value is less than 200 ns,
            NI-TClk automatically coerces minTime to 200 ns. For multichassis
            synchronization, adjust this value to account for propagation delays
            through the various devices and cables.

    

### `def synchronize_to_sync_pulse_sender(sessions, min_time)`

synchronize_to_sync_pulse_sender

    Synchronizes the other devices to the Sync Pulse Sender.

    Args:
        sessions (list of instrument-specific sessions or nitclk.SessionReference instances): sessions is an array of sessions that are being synchronized.

        min_time (hightime.timedelta, datetime.timedelta, or float in seconds): Minimal period of TClk, expressed in seconds. Supported values are
            between 0.0 s and 0.050 s (50 ms). Minimal period for a single
            chassis/PC is 200 ns. If the specified value is less than 200 ns,
            NI-TClk automatically coerces minTime to 200 ns. For multichassis
            synchronization, adjust this value to account for propagation delays
            through the various devices and cables.

    

### `def wait_until_done(sessions, timeout)`

wait_until_done

    Call this method to pause execution of your program until the
    acquisitions and/or generations corresponding to sessions are done or
    until the method returns a timeout error. wait_until_done is a
    blocking method that periodically checks the operation status. It
    returns control to the calling program if the operation completes
    successfully or an error occurs (including a timeout error). This
    method is most useful for finite data operations that you expect to
    complete within a certain time.

    Args:
        sessions (list of instrument-specific sessions or nitclk.SessionReference instances): sessions is an array of sessions that are being synchronized.

        timeout (hightime.timedelta, datetime.timedelta, or float in seconds): The amount of time in seconds that wait_until_done waits for the
            sessions to complete. If timeout is exceeded, wait_until_done
            returns an error.

    

<!--NI_PYTHON_API repo=nimi-python path=generated/nitclk/nitclk/unit_tests/_matchers.py -->
## PYTHON MODULE: generated/nitclk/nitclk/unit_tests/_matchers.py

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

<!--NI_PYTHON_API repo=nimi-python path=generated/nitclk/nitclk/unit_tests/_mock_helper.py -->
## PYTHON MODULE: generated/nitclk/nitclk/unit_tests/_mock_helper.py

### `class MockFunctionCallError(Exception)`

#### `def __init__(self, function, param=None)`

### `class SideEffectsHelper(object)`

#### `def __init__(self)`

#### `def __getitem__(self, func)`

#### `def __setitem__(self, func, val)`

#### `def niTClk_ConfigureForHomogeneousTriggers(self, session_count, sessions)`

#### `def niTClk_FinishSyncPulseSenderSynchronize(self, session_count, sessions, min_time)`

#### `def niTClk_GetAttributeViReal64(self, session, channel_name, attribute_id, value)`

#### `def niTClk_GetAttributeViSession(self, session, channel_name, attribute_id, value)`

#### `def niTClk_GetAttributeViString(self, session, channel_name, attribute_id, buf_size, value)`

#### `def niTClk_GetExtendedErrorInfo(self, error_string, error_string_size)`

#### `def niTClk_Initiate(self, session_count, sessions)`

#### `def niTClk_IsDone(self, session_count, sessions, done)`

#### `def niTClk_SetAttributeViReal64(self, session, channel_name, attribute_id, value)`

#### `def niTClk_SetAttributeViSession(self, session, channel_name, attribute_id, value)`

#### `def niTClk_SetAttributeViString(self, session, channel_name, attribute_id, value)`

#### `def niTClk_SetupForSyncPulseSenderSynchronize(self, session_count, sessions, min_time)`

#### `def niTClk_Synchronize(self, session_count, sessions, min_tclk_period)`

#### `def niTClk_SynchronizeToSyncPulseSender(self, session_count, sessions, min_time)`

#### `def niTClk_WaitUntilDone(self, session_count, sessions, timeout)`

#### `def set_side_effects_and_return_values(self, mock_library)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nitclk/nitclk/unit_tests/test_nitclk.py -->
## PYTHON MODULE: generated/nitclk/nitclk/unit_tests/test_nitclk.py

- `SESSION_NUM_FOR_TEST = 42`

### `class NitclkSupportingDriverSession()`

Session objects for drivers that support NI-TClk are expected to have a property of type nitclk.SessionReference called tclk

    This is why we're creating this fake driver class and adding the tclk property.
    

#### `def __init__(self, session_number)`

### `class TestNitclkApi()`

#### `def setup_method(self, method)`

#### `def teardown_method(self, method)`

#### `def test_initialize_one_session(self)`

#### `def test_initialize_multiple_sessions(self)`

#### `def test_configure_for_homogeneous_triggers(self)`

#### `def test_finish_sync_pulse_sender_synchronize(self)`

#### `def test_is_done(self)`

#### `def test_setup_for_sync_pulse_sender_synchronize(self)`

#### `def test_synchronize(self)`

#### `def test_synchronize_timedelta(self)`

#### `def test_synchronize_to_sync_pulse_sender(self)`

#### `def test_wait_until_done(self)`

#### `def test_api_error(self)`

#### `def test_api_get_error_description_fails(self)`

#### `def test_session_reference_error(self)`

#### `def test_session_reference_get_error_description_fails(self)`

#### `def test_set_vi_real64(self)`

#### `def test_get_vi_real64(self)`

#### `def test_set_timedelta_as_vi_real64(self)`

#### `def test_set_timedelta_as_timedelta(self)`

#### `def test_get_timedelta(self)`

#### `def test_set_vi_string(self)`

#### `def test_get_vi_string(self)`

#### `def test_set_vi_session_with_int(self)`

#### `def test_set_vi_session_with_session_reference(self)`

#### `def test_set_vi_session_with_session(self)`

#### `def test_get_tclk_session_reference(self)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nitclk/setup.py -->
## PYTHON MODULE: generated/nitclk/setup.py

### `def read_contents(file_to_read)`

<!--NI_PYTHON_API repo=nimi-python path=src/nidcpower/custom_types/lcr_load_compensation_spot.py -->
## PYTHON MODULE: src/nidcpower/custom_types/lcr_load_compensation_spot.py

### `class struct_NILCRLoadCompensationSpot(ctypes.Structure)`

#### `def __init__(self, data)`

### `class LCRLoadCompensationSpot()`

Specifies a DUT specification for a given frequency to use in LCR load compensation.

#### `def __init__(self, frequency, reference_value_type, reference_value)`

LCRLoadCompensationSpot

        Creates and returns an instance of LCRLoadCompensationSpot.

        Args:
            frequency (float): The spot frequency, in Hz.

            reference_value_type (enums.LCRReferenceValueType): A known specification value of your
                DUT to use as the basis for load compensation.

            reference_value (complex or float): A value that describes the reference_value_type
                specification. Use as indicated by the reference_value_type option you choose.
        

#### `def _create_copy(self, target_class)`

#### `def __repr__(self)`

#### `def __str__(self)`

<!--NI_PYTHON_API repo=nimi-python path=src/nidcpower/custom_types/lcr_measurement.py -->
## PYTHON MODULE: src/nidcpower/custom_types/lcr_measurement.py

### `class struct_NILCRMeasurement(ctypes.Structure)`

### `class LCRMeasurement()`

Specifies an LCR measurement.

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
    

#### `def __init__(self, data)`

LCRMeasurement

        Creates and returns an instance of LCRMeasurement.

        Args:
            data (struct_NILCRMeasurement): The LCR measurement ctypes instance returned by the driver.
        

#### `def __str__(self)`

<!--NI_PYTHON_API repo=nimi-python path=src/nidcpower/disabled_examples/nidcpower_advanced_sequence.py -->
## PYTHON MODULE: src/nidcpower/disabled_examples/nidcpower_advanced_sequence.py

### `def create_sweep(begin_value, end_value, number_of_steps)`

### `def example(resource_name, channels, options, steps, voltage_start, voltage_final, current_start, current_final)`

### `def _main(argsv)`

### `def main()`

### `def test_example()`

### `def test_main()`

<!--NI_PYTHON_API repo=nimi-python path=src/nidcpower/examples/nidcpower_advanced_sequence.py -->
## PYTHON MODULE: src/nidcpower/examples/nidcpower_advanced_sequence.py

### `def example(resource_name, options, voltage_max, current_max, points_per_output_function, source_delay)`

### `def _main(argsv)`

### `def main()`

### `def test_main()`

### `def test_example()`

<!--NI_PYTHON_API repo=nimi-python path=src/nidcpower/examples/nidcpower_constant_resistance_and_constant_power.py -->
## PYTHON MODULE: src/nidcpower/examples/nidcpower_constant_resistance_and_constant_power.py

### `def example(resource_name, options, output_function, constant_resistance_level, constant_resistance_level_range, constant_resistance_current_limit, constant_power_level, constant_power_level_range, constant_power_current_limit, source_delay)`

### `def _main(argsv)`

### `def main()`

### `def test_example()`

### `def test_main()`

<!--NI_PYTHON_API repo=nimi-python path=src/nidcpower/examples/nidcpower_lcr_source_ac_voltage.py -->
## PYTHON MODULE: src/nidcpower/examples/nidcpower_lcr_source_ac_voltage.py

### `def example(resource_name, options, lcr_frequency, lcr_impedance_range, cable_length, lcr_voltage_rms, lcr_dc_bias_source, lcr_dc_bias_voltage_level, lcr_measurement_time, lcr_custom_measurement_time, lcr_source_delay_mode, source_delay)`

### `def _main(argsv)`

### `def main()`

### `def test_example()`

### `def test_main()`

<!--NI_PYTHON_API repo=nimi-python path=src/nidcpower/examples/nidcpower_measure_record.py -->
## PYTHON MODULE: src/nidcpower/examples/nidcpower_measure_record.py

### `def example(resource_name, options, voltage, length)`

### `def _main(argsv)`

### `def main()`

### `def test_example()`

### `def test_main()`

<!--NI_PYTHON_API repo=nimi-python path=src/nidcpower/examples/nidcpower_sink_dc_current_into_electronic_load.py -->
## PYTHON MODULE: src/nidcpower/examples/nidcpower_sink_dc_current_into_electronic_load.py

### `def example(resource_name, options, current_level, current_level_range, voltage_limit_range, source_delay, output_shorted, conduction_voltage_mode, conduction_voltage_on_threshold, conduction_voltage_off_threshold, current_level_rising_slew_rate, current_level_falling_slew_rate)`

### `def _main(argsv)`

### `def main()`

### `def test_example()`

### `def test_main()`

<!--NI_PYTHON_API repo=nimi-python path=src/nidcpower/examples/nidcpower_source_delay_measure.py -->
## PYTHON MODULE: src/nidcpower/examples/nidcpower_source_delay_measure.py

### `def print_fetched_measurements(measurements)`

### `def example(resource_name, options, voltage1, voltage2, delay)`

### `def _main(argsv)`

### `def main()`

### `def test_main()`

### `def test_example()`

<!--NI_PYTHON_API repo=nimi-python path=src/nidcpower/system_tests/conftest.py -->
## PYTHON MODULE: src/nidcpower/system_tests/conftest.py

### `def pytest_collection_modifyitems(items)`

Ignores initializer deprecation warnings for all nidcpower system tests.

<!--NI_PYTHON_API repo=nimi-python path=src/nidcpower/system_tests/test_system_nidcpower.py -->
## PYTHON MODULE: src/nidcpower/system_tests/test_system_nidcpower.py

### `def pytest_generate_tests(metafunc)`

Parametrizes the "session" fixture by examining the the markers set for a test.

    By default, the session fixture is parametrized so each test runs once with an Independent
    Channels session. To also run a test with a legacy Synchronized Channels session, decorate the
    test with the custom marker @pytest.mark.include_legacy_session. To run a test with only a
    legacy session, decorate the test with @pytest.mark.legacy_session_only.
    

### `class SystemTests()`

#### `def session(self, request, session_creation_kwargs)`

Creates an NI-DCPower Session.

        Markers can be used to override the default initializer arguments. For example,
        @pytest.mark.resource_name('4162/0') will override the default resource name.

        Available markers include:
            @pytest.mark.resource_name
            @pytest.mark.channels
            @pytest.mark.reset
            @pytest.mark.options
            @pytest.mark.independent_channels

        By default, all dependent tests will run once with an Independent Channels session. Dependent
        tests can override this behavior by using custom markers. Refer to the documentation in
        pytest_generate_tests for more information.
        

#### `def test_self_test(self, session)`

#### `def test_self_cal(self, session)`

#### `def test_get_channel_name(self, session)`

#### `def test_get_channel_names(self, session)`

#### `def test_get_channel_names_multiple_instruments(self, session)`

#### `def test_get_attribute_string(self, session)`

#### `def test_error_message(self, session_creation_kwargs)`

#### `def test_get_error(self, session)`

#### `def test_get_self_cal_last_date_and_time(self, session)`

#### `def test_get_self_cal_last_temp(self, session)`

#### `def test_read_current_temperature(self, session)`

#### `def test_reset_device(self, session)`

#### `def test_reset_with_default(self, session)`

#### `def test_reset(self, session)`

#### `def test_disable(self, session)`

#### `def test_measure(self, session)`

#### `def test_query_output_state(self, session)`

#### `def test_config_aperture_time(self, session)`

#### `def test_fetch_multiple(self, session)`

#### `def test_measure_multiple(self, session)`

#### `def test_fetch_multiple_channels(self, session_creation_kwargs, resource_name, channels, independent_channels, measurement_channels, expected_measured_channel)`

#### `def test_measure_multiple_channels(self, session_creation_kwargs, resource_name, channels, independent_channels, measurement_channels, expected_measured_channels)`

#### `def test_measure_multiple_channel_ordering(self, session)`

#### `def test_measure_multiple_channel_ordering_non_independent_channels(self, session)`

#### `def test_measure_multiple_error_invalid_channels(self, session_creation_kwargs, resource_name, measurement_channels)`

#### `def test_query_max_current_limit(self, session)`

#### `def test_query_max_voltage_level(self, session)`

#### `def test_query_min_current_limit(self, session)`

#### `def test_set_sequence_with_source_delays(self, session)`

#### `def test_set_sequence_with_too_many_source_delays(self, session)`

#### `def test_set_sequence_with_too_few_source_delays(self, session)`

#### `def test_wait_for_event_default_timeout(self, session)`

#### `def test_wait_for_event_with_timeout(self, session)`

#### `def test_commit(self, session)`

#### `def test_import_export_buffer(self, session)`

#### `def test_import_export_file(self, session)`

#### `def test_create_and_delete_advanced_sequence(self, session)`

#### `def test_create_advanced_sequence_commit_step(self, session)`

#### `def test_create_and_delete_advanced_sequence_bad_name(self, session)`

#### `def test_create_and_delete_advanced_sequence_bad_type(self, session)`

#### `def test_send_software_edge_trigger_error(self, session)`

#### `def test_get_ext_cal_last_date_and_time(self, session)`

#### `def test_get_ext_cal_last_temp(self, session)`

#### `def test_get_ext_cal_recommended_interval(self, session)`

#### `def test_set_get_vi_int_64_attribute(self, session)`

#### `def test_channels_argument_format(self, session_creation_kwargs, channels, expected_channel_count)`

#### `def test_default_channels_argument(self, session_creation_kwargs)`

#### `def test_init_issues_deprecation_warnings(self, session_creation_kwargs, resource_name, channels, independent_channels)`

Tests for deprecation warnings for legacy initialization options.

        A deprecation warning should occur any time independent_channels is False or a channels
        argument is supplied.
        

#### `def test_init_backwards_compatibility_with_initialize_with_channels(self, session_creation_kwargs, resource_name, channels)`

Tests that legacy sessions open without exception for valid arguments.

#### `def test_init_with_independent_channels(self, session_creation_kwargs, resource_name, channels)`

Tests that independent channels sessions open without exception for valid arguments.

#### `def test_init_raises_value_error_for_multi_instrument_resource_name_and_channels_argument(self, session_creation_kwargs)`

Combining channels with multiple instruments is invalid.

        Tests that a value error is thrown when a multi-instrument resource name is provided with
        a channels argument. How to combine the two arguments is undefined.
        

#### `def test_init_raises_driver_errors_for_invalid_arguments(self, session_creation_kwargs, resource_name, channels)`

Tests for driver errors that should occur for invalid initialization arguments.

#### `def test_init_raises_driver_errors_for_invalid_arguments_legacy_session(self, session_creation_kwargs, resource_name, channels)`

Tests invalid initializer arguments for legacy initialize with channels sessions.

        Multi-instrument resource names are valid for simulated initialize with channels sessions. So,
        we attempt to initialize a true session and assert an unsupported device exception is raised.
        

#### `def test_repeated_capabilities_on_method_when_all_channels_are_specified(self, session)`

Sessions should not error when specifying all channels by number.

#### `def test_error_channel_name_not_allowed_in_legacy_session(self, session)`

#### `def test_error_channel_name_not_allowed(self, session)`

#### `def test_repeated_capabilities_with_initiate_multi_instrument_session(self, session, channels)`

#### `def test_repeated_capabilities_with_initiate_single_instrument_session(self, session, channels)`

#### `def test_repeated_capabilities_with_initiate_legacy_session(self, session, channels)`

Initiate should work on legacy sessions when all channels are specified.

#### `def test_repeated_capabilities_with_initiate_and_get_channel_names(self, session, indices)`

#### `def test_invalid_channels_repeated_capabilities(self, session, channels)`

#### `def test_instruments_repeated_capability(self, session, device_name)`

#### `def test_create_and_delete_advanced_sequence_repeated_capabilities(self, session, channels)`

#### `def test_create_advanced_sequence_commit_step_repeated_capabilities(self, session, channels)`

#### `def test_repeated_capabilities_parameterless_methods(self, session, channels, method)`

Double parametrize markers of this method results in nested parameterization of the test.

#### `def test_send_software_edge_trigger_repeated_capabilities(self, session, channels)`

#### `def test_wait_for_event_repeated_capabilities(self, session, channels)`

#### `def test_fetch_multiple_lcr(self, session)`

#### `def test_measure_multiple_lcr(self, session)`

#### `def test_fetch_multiple_lcr_channels(self, session_creation_kwargs, resource_name, channels, independent_channels, measurement_channels, expected_measured_channel)`

#### `def test_measure_multiple_lcr_channels(self, session_creation_kwargs, resource_name, channels, independent_channels, measurement_channels, expected_measured_channels)`

#### `def test_perform_lcr_open_compensation(self, session, additional_frequencies)`

#### `def test_perform_lcr_short_compensation(self, session, additional_frequencies)`

#### `def test_perform_lcr_load_compensation(self, session)`

#### `def test_perform_lcr_open_short_custom_cable_compensation(self, session, compensation_function)`

#### `def test_lcr_custom_cable_compensation_data(self, session)`

#### `def test_get_lcr_compensation_last_date_and_time(self, session, compensation_type)`

#### `def test_multi_threading_lock_unlock(self, session)`

#### `def test_multi_threading_ivi_synchronized_wrapper_releases_lock(self, session)`

### `class TestLibrary(SystemTests)`

#### `def session_creation_kwargs(self)`

#### `def test_lcr_compensation_data(self, session)`

### `class TestGrpc(SystemTests)`

#### `def grpc_channel(self)`

#### `def session_creation_kwargs(self, grpc_channel)`

#### `def test_get_lcr_compensation_data(self, session)`

#### `def test_configure_lcr_compensation(self, session)`

<!--NI_PYTHON_API repo=nimi-python path=src/nidcpower/unit_tests/test_nidcpower.py -->
## PYTHON MODULE: src/nidcpower/unit_tests/test_nidcpower.py

### `def test_lcr_measurement(ctype_members, channel, expected_python_members, expected_python_str)`

### `def test_lcr_load_compensation_spot(python_init_params, expected_repr, expected_str, expected_ctype_members)`

### `def test_lcr_load_compensation_spot_byte_packing_alignment()`

<!--NI_PYTHON_API repo=nimi-python path=src/nidigital/custom_types/history_ram_cycle_information.py -->
## PYTHON MODULE: src/nidigital/custom_types/history_ram_cycle_information.py

### `class HistoryRAMCycleInformation()`

#### `def __init__(self, pattern_name, time_set_name, vector_number, cycle_number, scan_cycle_number, expected_pin_states, actual_pin_states, per_pin_pass_fail)`

#### `def __repr__(self)`

#### `def __str__(self)`

#### `def _digital_states_representation(states)`

#### `def _digital_states_string(states)`

<!--NI_PYTHON_API repo=nimi-python path=src/nidigital/examples/burst_with_start_trigger/nidigital_burst_with_start_trigger.py -->
## PYTHON MODULE: src/nidigital/examples/burst_with_start_trigger/nidigital_burst_with_start_trigger.py

### `def example(resource_name, options, trigger_source=None, trigger_edge=None)`

### `def _main(argsv)`

### `def main()`

### `def test_main()`

### `def test_example()`

<!--NI_PYTHON_API repo=nimi-python path=src/nidigital/examples/configure_time_set_and_voltage_levels/nidigital_configure_time_set_and_voltage_levels.py -->
## PYTHON MODULE: src/nidigital/examples/configure_time_set_and_voltage_levels/nidigital_configure_time_set_and_voltage_levels.py

### `class VoltageLevelsAndTerminationConfig()`

#### `def __init__(self, vil, vih, vol, voh, vterm, termination_mode, iol, ioh, vcom)`

### `class TimeSetConfig()`

#### `def __init__(self, time_set_name, period, drive_format, drive_on, drive_data, drive_return, drive_off, strobe_edge)`

### `def convert_drive_format(drive_format)`

### `def example(resource_name, options, channels, voltage_config, time_set_config)`

### `def _main(argsv)`

### `def main()`

### `def test_main()`

### `def test_example()`

<!--NI_PYTHON_API repo=nimi-python path=src/nidigital/examples/ppmu_source_and_measure/nidigital_ppmu_source_and_measure.py -->
## PYTHON MODULE: src/nidigital/examples/ppmu_source_and_measure/nidigital_ppmu_source_and_measure.py

### `def example(resource_name, options, channels, measure, aperture_time, source=None, settling_time=None, current_level_range=None, current_level=None, voltage_limit_high=None, voltage_limit_low=None, current_limit_range=None, voltage_level=None)`

### `def _main(argsv)`

### `def main()`

### `def test_main()`

### `def test_example()`

<!--NI_PYTHON_API repo=nimi-python path=src/nidigital/system_tests/test_system_nidigital.py -->
## PYTHON MODULE: src/nidigital/system_tests/test_system_nidigital.py

### `class SystemTests()`

#### `def multi_instrument_session(self, session_creation_kwargs)`

#### `def single_instrument_session(self, session_creation_kwargs)`

#### `def test_close(self, session_creation_kwargs)`

#### `def test_reset(self, multi_instrument_session)`

#### `def test_reset_device(self, multi_instrument_session)`

#### `def test_self_test(self, multi_instrument_session)`

#### `def test_get_error(self, multi_instrument_session)`

#### `def test_self_calibrate(self, multi_instrument_session)`

#### `def test_channels_rep_cap(self, multi_instrument_session)`

#### `def test_sites_rep_cap(self, multi_instrument_session)`

#### `def test_pins_rep_cap(self, multi_instrument_session)`

#### `def test_chained_sites_pins_rep_cap(self, multi_instrument_session)`

#### `def test_instruments_rep_cap(self, multi_instrument_session)`

#### `def test_pattern_opcode_events_rep_cap(self, multi_instrument_session)`

#### `def test_conditional_jump_triggers_rep_cap(self, multi_instrument_session)`

#### `def test_rio_events_rep_cap(self, single_instrument_session)`

#### `def test_rio_triggers_rep_cap(self, single_instrument_session)`

#### `def test_property_boolean(self, multi_instrument_session)`

#### `def test_property_int32(self, multi_instrument_session)`

#### `def test_property_int64(self, multi_instrument_session)`

#### `def test_property_real64(self, multi_instrument_session)`

#### `def test_property_string(self, multi_instrument_session)`

#### `def test_get_channel_names(self, multi_instrument_session)`

#### `def test_tdr_all_channels(self, multi_instrument_session)`

#### `def test_tdr_some_channels(self, multi_instrument_session)`

#### `def test_burst_pattern_burst_only(self, multi_instrument_session)`

#### `def test_burst_pattern_pass_fail(self, multi_instrument_session)`

#### `def test_source_waveform_parallel_broadcast(self, multi_instrument_session)`

Test methods for using source waveform with parallel sourcing and broadcast data mapping.

        - create_source_waveform_parallel
        - write_source_waveform_broadcast
        

#### `def configure_session(self, session, test_name)`

#### `def get_test_file_path(self, test_name, file_name)`

#### `def source_waveform_type(self, request)`

#### `def test_source_waveform_parallel_site_unique(self, multi_instrument_session, source_waveform_type)`

Test methods for using source waveform with parallel sourcing and site-unique data mapping.

        - create_source_waveform_parallel
        - write_source_waveform_site_unique
        

#### `def source_waveform_wrong_type(self, request)`

#### `def test_source_waveform_parallel_site_unique_wrong_type(self, multi_instrument_session, source_waveform_wrong_type)`

Test methods for passing wrong types write_source_waveform_site_unique .

        - create_source_waveform_parallel
        - write_source_waveform_site_unique
        

#### `def test_fetch_capture_waveform_parallel(self, multi_instrument_session)`

Test methods for using capture waveform with parallel acquisition.

        - create_capture_waveform_parallel
        - fetch_capture_waveform
        

#### `def test_get_pin_results_pin_information(self, multi_instrument_session)`

#### `def test_history_ram_cycle_information_representation(self)`

#### `def test_history_ram_cycle_information_string(self)`

#### `def test_fetch_history_ram_cycle_information_without_site(self, multi_instrument_session)`

#### `def test_fetch_history_ram_cycle_information_position_negative(self, multi_instrument_session)`

#### `def configure_for_history_ram_test(self, session)`

#### `def test_fetch_history_ram_cycle_information_position_out_of_bound(self, multi_instrument_session)`

#### `def test_fetch_history_ram_cycle_information_position_last(self, multi_instrument_session)`

#### `def test_fetch_history_ram_cycle_information_is_finite_invalid(self, multi_instrument_session)`

#### `def test_fetch_history_ram_cycle_information_samples_to_read_too_much(self, multi_instrument_session)`

#### `def test_fetch_history_ram_cycle_information_samples_to_read_negative(self, multi_instrument_session)`

#### `def test_fetch_history_ram_cycle_information_samples_to_read_zero(self, multi_instrument_session)`

#### `def test_fetch_history_ram_cycle_information_samples_to_read_all(self, multi_instrument_session)`

#### `def test_fetch_history_ram_cycle_information_no_failures(self, multi_instrument_session)`

#### `def test_get_pattern_pin_names(self, multi_instrument_session)`

#### `def test_get_site_pass_fail(self, multi_instrument_session)`

#### `def test_get_fail_count(self, multi_instrument_session)`

#### `def test_ppmu_measure(self, multi_instrument_session)`

#### `def test_ppmu_source(self, multi_instrument_session)`

#### `def test_read_static(self, multi_instrument_session)`

#### `def test_write_static(self, multi_instrument_session)`

#### `def test_read_sequencer_flag(self, multi_instrument_session)`

#### `def test_write_sequencer_flag(self, multi_instrument_session)`

#### `def test_read_sequencer_register(self, multi_instrument_session)`

#### `def test_write_sequencer_register(self, multi_instrument_session)`

#### `def test_configure_voltage_levels(self, multi_instrument_session)`

#### `def test_configure_active_load_levels(self, multi_instrument_session)`

#### `def test_clock_generator_abort(self, multi_instrument_session)`

#### `def test_clock_generator_generate_clock(self, multi_instrument_session)`

#### `def test_frequency_counter_measure_frequency(self, multi_instrument_session)`

#### `def test_create_get_delete_time_sets(self, multi_instrument_session)`

Test basic time set methods.

        - create_time_set
        - delete_all_time_sets
        

#### `def test_configure_get_time_set_period(self, multi_instrument_session)`

Test time set period methods.

        - configure_time_set_period
        - get_time_set_period
        

#### `def test_configure_get_time_set_drive_format(self, multi_instrument_session)`

Test time set drive format methods.

        - configure_time_set_drive_format
        - get_time_set_drive_format
        

#### `def test_configure_get_time_set_edge(self, multi_instrument_session)`

Test time set individual edge methods.

        - configure_time_set_edge
        - get_time_set_edge
        

#### `def test_configure_time_set_drive_edges(self, multi_instrument_session)`

#### `def test_configure_time_set_compare_edges_strobe(self, multi_instrument_session)`

#### `def test_configure_get_time_set_edge_multiplier(self, multi_instrument_session)`

Test time set edge multiplier methods.

        - configure_time_set_edge_multiplier
        - get_time_set_edge_multiplier
        

#### `def test_configure_time_set_drive_edges2x(self, multi_instrument_session)`

#### `def test_configure_time_set_compare_edges_strobe2x(self, multi_instrument_session)`

#### `def test_enable_disable_sites_single(self, multi_instrument_session)`

Test methods for single site enable configuration.

        - enable_sites
        - disable_sites
        - is_site_enabled
        

#### `def test_enable_disable_sites_multiple(self, multi_instrument_session)`

Test methods for multiple site enable configuration.

        - enable_sites
        - disable_sites
        - is_site_enabled
        

#### `def test_load_get_unload_patterns(self, multi_instrument_session)`

Test basic pattern methods.

        - load_pattern
        - unload_all_patterns
        

#### `def test_configure_pattern_burst_sites(self, multi_instrument_session)`

#### `def test_commit(self, multi_instrument_session)`

#### `def test_initiate_context_manager_and_wait_until_done(self, multi_instrument_session)`

Test initiate's context manager and pattern completion methods.

        - with initiate
        - wait_until_done
        - is_done
        

#### `def test_abort(self, multi_instrument_session)`

#### `def test_abort_keep_alive(self, multi_instrument_session)`

#### `def test_create_source_waveform_serial(self, multi_instrument_session)`

#### `def test_create_source_waveform_from_file_tdms(self, multi_instrument_session)`

#### `def test_write_source_waveform_data_from_file_tdms(self, multi_instrument_session)`

#### `def test_create_capture_waveform_serial(self, multi_instrument_session)`

#### `def test_create_capture_waveform_from_file_digicapture(self, multi_instrument_session)`

#### `def test_send_software_edge_trigger(self, multi_instrument_session)`

#### `def test_specifications_levels_and_timing_single(self, multi_instrument_session)`

Test methods for loading, applying and unloading specifications, levels, and timing files.

        - apply_levels_and_timing
        - load_specifications_levels_and_timing
        - unload_specifications
        

#### `def test_specifications_levels_and_timing_multiple(self, multi_instrument_session)`

Test methods for loading, applying and unloading multiple specifications, levels, and timing files.

        - apply_levels_and_timing
        - load_specifications_levels_and_timing
        - unload_specifications
        

#### `def test_specifications_levels_and_timing_load_sequentially(self, multi_instrument_session)`

Test methods for separately loading, applying and unloading multiple specifications, levels, and timing files.

        - apply_levels_and_timing
        - load_specifications_levels_and_timing
        - unload_specifications
        

#### `def test_apply_levels_and_timing_initial_states(self, multi_instrument_session)`

#### `def test_multi_threading_lock_unlock(self, multi_instrument_session)`

#### `def test_multi_threading_ivi_synchronized_wrapper_releases_lock(self, multi_instrument_session)`

### `class TestLibrary(SystemTests)`

#### `def session_creation_kwargs(self)`

#### `def test_enable_match_fail_combination(self, multi_instrument_session)`

### `class TestGrpc(SystemTests)`

#### `def grpc_channel(self)`

#### `def session_creation_kwargs(self, grpc_channel)`

<!--NI_PYTHON_API repo=nimi-python path=src/nidigital/unit_tests/test_nidigital.py -->
## PYTHON MODULE: src/nidigital/unit_tests/test_nidigital.py

### `class TestSession()`

#### `def setup_method(self, method)`

#### `def teardown_method(self, method)`

#### `def test_fetch_history_ram_cycle_information_position_out_of_bound(self)`

#### `def test_fetch_history_ram_cycle_information_position_last(self)`

#### `def test_fetch_history_ram_cycle_information_samples_to_read_too_much(self)`

#### `def niDigital_FetchHistoryRAMCycleInformation_looping(self, vi, site, sample_index, pattern_index, time_set_index, vector_number, cycle_number, num_dut_cycles)`

#### `def niDigital_GetTimeSetName_looping(self, vi, time_set_index, name_buffer_size, name)`

#### `def niDigital_FetchHistoryRAMScanCycleNumber_looping(self, vi, site, sample_index, scan_cycle_number)`

#### `def niDigital_FetchHistoryRAMCyclePinData_looping(self, vi, site, pin_list, sample_index, dut_cycle_index, pin_data_buffer_size, expected_pin_states, actual_pin_states, per_pin_pass_fail, actual_num_pin_data)`

#### `def test_fetch_history_ram_cycle_information_samples_to_read_all(self)`

#### `def niDigital_FetchHistoryRAMCyclePinData_check_pins_looping(self, vi, site, pin_list, sample_index, dut_cycle_index, pin_data_buffer_size, expected_pin_states, actual_pin_states, per_pin_pass_fail, actual_num_pin_data)`

#### `def test_fetch_history_ram_cycle_information_pin_list(self)`

#### `def niDigital_GetHistoryRAMSampleCount_check_site_looping(self, vi, site, sample_count)`

#### `def test_fetch_history_ram_cycle_information_site_n(self)`

#### `def test_pin_state_enum_print(self)`

#### `def test_write_static_pin_state_enum_print(self)`

<!--NI_PYTHON_API repo=nimi-python path=src/nidmm/examples/nidmm_fetch_waveform.py -->
## PYTHON MODULE: src/nidmm/examples/nidmm_fetch_waveform.py

### `def example(resource_name, options, function, range, points, rate)`

### `def _main(argsv)`

### `def main()`

### `def test_example()`

### `def test_main()`

<!--NI_PYTHON_API repo=nimi-python path=src/nidmm/examples/nidmm_measurement.py -->
## PYTHON MODULE: src/nidmm/examples/nidmm_measurement.py

### `def example(resource_name, option_string, function, range, digits)`

### `def _main(argsv)`

### `def main()`

### `def test_example()`

### `def test_main()`

<!--NI_PYTHON_API repo=nimi-python path=src/nidmm/examples/nidmm_multi_point_measurement.py -->
## PYTHON MODULE: src/nidmm/examples/nidmm_multi_point_measurement.py

### `def example(resource_name, options, function, range, digits, samples, triggers)`

### `def _main(argsv)`

### `def main()`

### `def test_example()`

### `def test_main()`

<!--NI_PYTHON_API repo=nimi-python path=src/nidmm/system_tests/test_system_nidmm.py -->
## PYTHON MODULE: src/nidmm/system_tests/test_system_nidmm.py

### `class SystemTests()`

#### `def session(self, session_creation_kwargs)`

#### `def test_take_simple_measurement_works(self, session)`

#### `def test_acquisition(self, session)`

#### `def test_multi_point_acquisition(self, session)`

#### `def test_vi_string_attribute(self, session)`

#### `def test_vi_int32_attribute(self, session)`

#### `def test_vi_real64_attribute(self, session)`

#### `def test_enum_attribute(self, session)`

#### `def test_writeonly_attribute(self, session)`

#### `def test_method_configure_trigger(self, session)`

#### `def test_method_self_test(self, session)`

#### `def test_method_get_dev_temp(self, session)`

#### `def test_method_reset_with_defaults(self, session)`

#### `def test_method_get_self_cal_supported(self, session)`

#### `def test_method_read_status(self, session)`

#### `def test_fetch_error_while_not_initiated(self, session)`

#### `def test_multi_point_acquisition_with_measurement_absolute(self, session)`

#### `def test_disable(self, session)`

#### `def test_fetch_multiple(self, session)`

#### `def test_get_auto_range_value(self, session)`

#### `def test_get_cal_date_time(self, session)`

#### `def test_get_last_cal_temperature(self, session)`

#### `def test_trigger_max_time_exceeded_errror(self, session)`

#### `def test_self_cal(self, session)`

#### `def test_configure_rtd(self, session)`

#### `def test_configure_thermistor(self, session)`

#### `def test_configure_thermocouple(self, session)`

#### `def test_configure_waveform_acquisition(self, session)`

#### `def test_fetch_waveform(self, session)`

#### `def test_fetch_waveform_error(self, session)`

#### `def test_perform_cable_compensation(self, session)`

#### `def test_read_waveform(self, session)`

#### `def test_send_software_trigger(self, session)`

#### `def test_reset_method(self, session)`

#### `def test_import_export_buffer(self, session)`

#### `def test_import_export_file(self, session)`

#### `def test_error_message(self, session_creation_kwargs)`

#### `def test_get_ext_cal_recommended_interval(self, session)`

#### `def test_locks_are_reentrant(self, session)`

#### `def test_multi_threading_lock_unlock(self, session)`

#### `def test_multi_threading_ivi_synchronized_wrapper_releases_lock(self, session)`

### `class TestLibrary(SystemTests)`

#### `def session_creation_kwargs(self)`

#### `def test_fetch_waveform_into(self, session)`

### `class TestGrpc(SystemTests)`

#### `def grpc_channel(self)`

#### `def session_creation_kwargs(self, grpc_channel)`

#### `def test_new_session_already_exists(self, grpc_channel)`

#### `def test_attach_to_non_existent_session(self, grpc_channel)`

<!--NI_PYTHON_API repo=nimi-python path=src/nifake/custom_types/custom_struct.py -->
## PYTHON MODULE: src/nifake/custom_types/custom_struct.py

### `class struct_CustomStruct(ctypes.Structure)`

#### `def __init__(self, data=None, struct_int=0, struct_double=0.0)`

#### `def __repr__(self)`

#### `def __str__(self)`

### `class CustomStruct()`

#### `def __init__(self, data=None, struct_int=0, struct_double=0.0)`

#### `def _create_copy(self, target_class)`

#### `def __repr__(self)`

#### `def __str__(self)`

<!--NI_PYTHON_API repo=nimi-python path=src/nifake/custom_types/custom_struct_nested_typedef.py -->
## PYTHON MODULE: src/nifake/custom_types/custom_struct_nested_typedef.py

### `class struct_CustomStructNestedTypedef(ctypes.Structure)`

#### `def __init__(self, data=None)`

### `class CustomStructNestedTypedef()`

#### `def __init__(self, data=None, struct_custom_struct=custom_struct.CustomStruct(), struct_custom_struct_typedef=custom_struct_typedef.CustomStructTypedef())`

#### `def _create_copy(self, target_class)`

#### `def __repr__(self)`

#### `def __str__(self)`

<!--NI_PYTHON_API repo=nimi-python path=src/nifake/custom_types/custom_struct_typedef.py -->
## PYTHON MODULE: src/nifake/custom_types/custom_struct_typedef.py

### `class struct_CustomStructTypedef(ctypes.Structure)`

#### `def __init__(self, data=None)`

### `class CustomStructTypedef()`

#### `def __init__(self, data=None, struct_int=0, struct_double=0.0)`

#### `def _create_copy(self, target_class)`

#### `def __repr__(self)`

#### `def __str__(self)`

<!--NI_PYTHON_API repo=nimi-python path=src/nifake/unit_tests/test_converters.py -->
## PYTHON MODULE: src/nifake/unit_tests/test_converters.py

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

<!--NI_PYTHON_API repo=nimi-python path=src/nifake/unit_tests/test_grpc.py -->
## PYTHON MODULE: src/nifake/unit_tests/test_grpc.py

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

<!--NI_PYTHON_API repo=nimi-python path=src/nifake/unit_tests/test_library_interpreter.py -->
## PYTHON MODULE: src/nifake/unit_tests/test_library_interpreter.py

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

<!--NI_PYTHON_API repo=nimi-python path=src/nifake/unit_tests/test_library_singleton.py -->
## PYTHON MODULE: src/nifake/unit_tests/test_library_singleton.py

### `def test_driver_runtime_not_installed_raises_driver_not_installed_error()`

<!--NI_PYTHON_API repo=nimi-python path=src/nifake/unit_tests/test_session.py -->
## PYTHON MODULE: src/nifake/unit_tests/test_session.py

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

<!--NI_PYTHON_API repo=nimi-python path=src/nifgen/examples/nifgen_arb_waveform.py -->
## PYTHON MODULE: src/nifgen/examples/nifgen_arb_waveform.py

### `def create_waveform_data(number_of_samples)`

### `def example(resource_name, options, samples, gain, offset, gen_time)`

### `def _main(argsv)`

### `def main()`

### `def test_example()`

### `def test_main()`

<!--NI_PYTHON_API repo=nimi-python path=src/nifgen/examples/nifgen_script.py -->
## PYTHON MODULE: src/nifgen/examples/nifgen_script.py

- `NUMBER_OF_SAMPLES = 2096`

- `SINE_WAVE = [math.sin(math.pi * 2 * x / NUMBER_OF_SAMPLES) for x in range(NUMBER_OF_SAMPLES)]`

- `RAMP_UP = [x / NUMBER_OF_SAMPLES for x in range(NUMBER_OF_SAMPLES)]`

- `RAMP_DOWN = [-1.0 * x for x in RAMP_UP]`

- `SQUARE_WAVE = [1.0 if x < NUMBER_OF_SAMPLES / 2 else -1.0 for x in range(NUMBER_OF_SAMPLES)]`

- `SAWTOOTH_WAVE = RAMP_UP[::2] + [-1 + x for x in RAMP_UP][::2]`

- `SCRIPT_ALL = '\nscript scriptmulti\n  repeat until scriptTrigger0\n    generate rampup\n    generate sine\n    generate rampdown\n  end repeat\n  repeat until scriptTrigger0\n    generate rampdown\n    generate square\n    generate rampup\n  end repeat\n  repeat until scriptTrigger0\n    generate rampup\n    generate rampdown\n  end repeat\n  repeat until scriptTrigger0\n    generate sine\n  end repeat\n  repeat until scriptTrigger0\n    generate sawtooth\n  end repeat\n  repeat until scriptTrigger0\n    generate rampdown\n    generate rampup\n  end repeat\nend script\n\nscript scriptsine\n  repeat until scriptTrigger0\n    generate sine\n  end repeat\nend script\n\nscript scriptrampup\n  repeat until scriptTrigger0\n    generate rampup\n  end repeat\nend script\n\nscript scriptrampdown\n  repeat until scriptTrigger0\n    generate rampdown\n  end repeat\nend script\n\nscript scriptsquare\n  repeat until scriptTrigger0\n    generate square\n  end repeat\nend script\n\nscript scriptsawtooth\n  repeat until scriptTrigger0\n    generate sawtooth\n  end repeat\nend script\n'`

### `def example(resource_name, options, shape, channel)`

### `def _main(argsv)`

### `def test_example()`

### `def test_main()`

### `def main()`

<!--NI_PYTHON_API repo=nimi-python path=src/nifgen/examples/nifgen_standard_function.py -->
## PYTHON MODULE: src/nifgen/examples/nifgen_standard_function.py

### `def example(resource_name, options, waveform, frequency, amplitude, offset, phase, gen_time)`

### `def _main(argsv)`

### `def main()`

### `def test_example()`

### `def test_main()`

<!--NI_PYTHON_API repo=nimi-python path=src/nifgen/examples/nifgen_trigger.py -->
## PYTHON MODULE: src/nifgen/examples/nifgen_trigger.py

### `def example(resource_name1, resource_name2, options, waveform, gen_time)`

### `def _main(argsv)`

### `def main()`

### `def test_example()`

### `def test_main()`

<!--NI_PYTHON_API repo=nimi-python path=src/nifgen/system_tests/test_system_nifgen.py -->
## PYTHON MODULE: src/nifgen/system_tests/test_system_nifgen.py

### `def get_test_file_path(file_name)`

### `class SystemTests()`

#### `def session(self, session_creation_kwargs)`

#### `def test_self_test(self, session)`

#### `def test_get_attribute_string(self, session)`

#### `def test_error_message(self, session_creation_kwargs)`

#### `def test_get_error(self, session)`

#### `def test_method_get_self_cal_supported(self, session)`

#### `def test_get_self_cal_last_date_and_time(self, session)`

#### `def test_self_cal(self, session)`

#### `def test_channels_rep_cap(self)`

#### `def test_markers_rep_cap(self, session)`

#### `def test_data_markers_rep_cap(self, session)`

#### `def test_script_triggers_rep_cap(self, session)`

#### `def test_standard_waveform(self, session)`

#### `def test_frequency_list(self, session)`

#### `def test_clear_freq_list(self, session)`

#### `def test_create_waveform_from_list(self, session)`

#### `def test_configure_arb_waveform(self, session)`

#### `def test_disable(self, session)`

#### `def test_get_ext_cal_last_date_and_time(self, session)`

#### `def test_get_ext_cal_last_temp(self, session)`

#### `def test_get_ext_cal_recommended_interval(self, session)`

#### `def test_get_hardware_state(self, session)`

#### `def test_get_self_cal_last_temp(self, session)`

#### `def test_query_arb_wfm_capabilities(self, session)`

#### `def test_query_freq_list_capabilities(self, session)`

#### `def test_read_current_temperature(self, session)`

#### `def test_allocate_waveform(self, session)`

#### `def test_clear_waveform_memory(self, session)`

#### `def test_query_arb_seq_capabilities(self, session)`

#### `def test_create_arb_sequence(self, session)`

#### `def test_create_advanced_arb_sequence(self, session)`

#### `def test_arb_script(self, session)`

#### `def test_reset(self, session)`

#### `def test_reset_device(self, session)`

#### `def test_reset_with_default(self, session)`

#### `def test_write_waveform_from_list(self, session)`

#### `def test_write_named_waveform_from_list(self, session)`

#### `def test_write_waveform_wrong_type(self, session)`

#### `def test_set_waveform_next_write_position(self, session)`

#### `def test_write_waveform_from_filei64(self, session)`

#### `def test_named_waveform_operations(self, session)`

#### `def test_handle_waveform_operations(self, session)`

#### `def test_write_waveform_from_file_f64(self, session)`

#### `def test_wait_until_done(self, session)`

#### `def test_user_standard_waveform(self, session)`

#### `def test_send_software_edge_trigger_start_deprecated(self, session)`

#### `def test_send_software_edge_trigger_script_deprecated(self, session)`

#### `def test_send_software_edge_trigger_start(self, session)`

#### `def test_send_software_edge_trigger_script(self, session)`

#### `def test_channel_format_types(self, session_creation_kwargs)`

#### `def test_import_export_buffer(self, session)`

#### `def test_import_export_file(self, session)`

#### `def test_get_channel_name(self, session)`

#### `def test_create_waveform_wrong_type(self, session)`

#### `def test_create_advanced_arb_sequence_wrong_size(self, session)`

#### `def test_multi_threading_lock_unlock(self, session)`

#### `def test_multi_threading_ivi_synchronized_wrapper_releases_lock(self, session)`

### `class TestLibrary(SystemTests)`

#### `def session_creation_kwargs(self)`

#### `def test_create_waveform_from_numpy_array_float64(self, session)`

#### `def test_create_waveform_numpy_array_int16(self, session)`

#### `def test_write_waveform_from_numpy_array_float64(self, session)`

#### `def test_write_waveform_numpy_array_int16(self, session)`

#### `def test_write_named_waveform_from_numpy_array_float64(self, session)`

#### `def test_write_named_waveform_numpy_array_int16(self, session)`

### `class TestGrpc(SystemTests)`

#### `def grpc_channel(self)`

#### `def session_creation_kwargs(self, grpc_channel)`

<!--NI_PYTHON_API repo=nimi-python path=src/nimodinst/examples/nimodinst_all_devices.py -->
## PYTHON MODULE: src/nimodinst/examples/nimodinst_all_devices.py

### `def example()`

### `def _main()`

### `def test_example()`

<!--NI_PYTHON_API repo=nimi-python path=src/nimodinst/system_tests/test_system_nimodinst.py -->
## PYTHON MODULE: src/nimodinst/system_tests/test_system_nimodinst.py

### `def test_bad_device_family()`

### `def test_no_device_family()`

### `def test_device_family_string_with_dashes()`

### `def test_device_family_string_without_dashes()`

### `def test_int_attribute_error_on_non_existant_device()`

### `def test_string_attribute_error_on_non_existant_device()`

### `def test_device_name_attribute()`

### `def test_device_model_attribute()`

### `def test_serial_number_attribute()`

### `def test_bus_number_attribute()`

### `def test_chassis_number_attribute()`

### `def test_max_pciexpress_link_width_attribute()`

### `def test_pciexpress_link_width_attribute()`

### `def test_slot_number_attribute()`

### `def test_socket_number_attribute()`

<!--NI_PYTHON_API repo=nimi-python path=src/nimodinst/unit_tests/test_modinst.py -->
## PYTHON MODULE: src/nimodinst/unit_tests/test_modinst.py

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

<!--NI_PYTHON_API repo=nimi-python path=src/nirfsg/examples/nirfsg_arb_waveform.py -->
## PYTHON MODULE: src/nirfsg/examples/nirfsg_arb_waveform.py

### `def example(resource_name, options, frequency, power_level, number_of_samples)`

### `def _main(argsv)`

### `def main()`

### `def test_example()`

### `def test_main()`

<!--NI_PYTHON_API repo=nimi-python path=src/nirfsg/examples/nirfsg_cw.py -->
## PYTHON MODULE: src/nirfsg/examples/nirfsg_cw.py

### `def example(resource_name, options, frequency, power_level)`

### `def _main(argsv)`

### `def main()`

### `def test_example()`

### `def test_main()`

<!--NI_PYTHON_API repo=nimi-python path=src/nirfsg/examples/nirfsg_script.py -->
## PYTHON MODULE: src/nirfsg/examples/nirfsg_script.py

- `SAMPLE_SCRIPT = '\nscript continuousWaveform\n    repeat forever\n        generate wfm\n    end repeat\nend script\n'`

### `def example(resource_name, options, frequency, power_level, number_of_samples)`

### `def _main(argsv)`

### `def main()`

### `def test_example()`

### `def test_main()`

<!--NI_PYTHON_API repo=nimi-python path=src/nirfsg/system_tests/test_system_nirfsg.py -->
## PYTHON MODULE: src/nirfsg/system_tests/test_system_nirfsg.py

### `def get_test_file_path(file_name)`

### `class SystemTests()`

#### `def rfsg_device_session(self, session_creation_kwargs)`

#### `def simulated_5831_device_session(self, session_creation_kwargs)`

#### `def test_get_float_attribute(self, rfsg_device_session)`

#### `def test_set_float_attribute(self, rfsg_device_session)`

#### `def test_get_string_attribute(self, rfsg_device_session)`

#### `def test_get_list_of_strings_attribute(self, rfsg_device_session)`

#### `def test_set_string_attribute(self, rfsg_device_session)`

#### `def test_get_timedelta_attribute(self, rfsg_device_session)`

#### `def test_get_int32_attribute(self, rfsg_device_session)`

#### `def test_set_int32_enum_attribute(self, rfsg_device_session)`

#### `def test_set_invalid_attribute_raises(self, rfsg_device_session)`

#### `def test_multi_threading_lock_unlock(self, rfsg_device_session)`

#### `def test_multi_threading_ivi_synchronized_wrapper_releases_lock(self, rfsg_device_session)`

#### `def test_error_message(self, session_creation_kwargs)`

#### `def test_get_error(self, rfsg_device_session)`

#### `def test_reset(self, rfsg_device_session)`

#### `def test_reset_with_options(self, rfsg_device_session)`

#### `def test_self_test(self, rfsg_device_session)`

#### `def test_self_cal(self, rfsg_device_session)`

#### `def test_self_cal_range(self, rfsg_device_session)`

#### `def test_clear_self_calibrate_range(self, rfsg_device_session)`

#### `def test_get_ext_cal_last_date_and_time(self, rfsg_device_session)`

#### `def test_get_self_cal_last_date_and_time(self, rfsg_device_session)`

#### `def test_get_terminal_name(self, rfsg_device_session)`

#### `def test_query_arb_waveform_capabilities(self, rfsg_device_session)`

#### `def test_markers_rep_cap(self, rfsg_device_session)`

#### `def test_script_triggers_rep_cap(self, rfsg_device_session)`

#### `def test_waveforms_rep_cap(self, rfsg_device_session)`

#### `def test_ports_rep_cap(self, simulated_5831_device_session)`

#### `def test_los_rep_cap(self, simulated_5831_device_session)`

#### `def test_configure_rf(self, rfsg_device_session)`

#### `def test_write_arb_waveform_numpy_complex128(self, rfsg_device_session)`

#### `def test_write_arb_waveform_numpy_complex64(self, rfsg_device_session)`

#### `def test_write_arb_waveform_numpy_interleaved_int16(self, rfsg_device_session)`

#### `def test_write_arb_waveform_with_wrong_datatype(self, rfsg_device_session)`

#### `def test_clear_arb_waveform(self, rfsg_device_session)`

#### `def test_clear_all_arb_waveforms(self, rfsg_device_session)`

#### `def test_allocate_arb_waveform(self, rfsg_device_session)`

#### `def test_set_arb_waveform_next_write_position(self, rfsg_device_session)`

#### `def test_set_get_burst_start_stop_locations(self, rfsg_device_session)`

#### `def test_set_get_marker_event_locations(self, rfsg_device_session)`

#### `def test_write_script(self, rfsg_device_session)`

#### `def test_check_if_script_exists(self, rfsg_device_session)`

#### `def test_write_script_with_bad_script(self, rfsg_device_session)`

#### `def test_get_script(self, rfsg_device_session)`

#### `def test_delete_script(self, rfsg_device_session)`

#### `def test_configure_software_trigger(self, rfsg_device_session)`

#### `def test_configure_digital_edge_trigger(self, rfsg_device_session)`

#### `def test_disable_trigger(self, rfsg_device_session)`

#### `def test_export_started_event_with_invalid_terminal(self, rfsg_device_session)`

#### `def test_save_load_configuration(self, rfsg_device_session)`

#### `def test_cw_generation(self, rfsg_device_session)`

#### `def test_cw_generation_with_status(self, rfsg_device_session)`

#### `def test_abort(self, rfsg_device_session)`

#### `def test_abort_with_status(self, rfsg_device_session)`

#### `def test_multiple_arb_waveform_generation(self, rfsg_device_session)`

#### `def test_multiple_arb_waveform_generation_with_status(self, rfsg_device_session)`

#### `def test_multiple_script_generation(self, rfsg_device_session)`

#### `def test_multiple_script_generation_with_status(self, rfsg_device_session)`

#### `def test_send_software_edge_trigger(self, rfsg_device_session)`

#### `def test_create_deembedding_sparameter_table_s2p_file(self, rfsg_device_session)`

#### `def test_set_get_deembedding_sparameters(self, rfsg_device_session)`

#### `def test_create_deembedding_sparameter_table_array_error_cases(self, rfsg_device_session)`

#### `def test_read_and_download_waveform_from_file_tdms(self, rfsg_device_session)`

#### `def test_wait_until_settled(self, rfsg_device_session)`

#### `def test_get_all_script_names(self, rfsg_device_session)`

### `class TestLibrary(SystemTests)`

#### `def session_creation_kwargs(self)`

#### `def test_get_all_named_waveform_names(self, rfsg_device_session)`

### `class TestGrpc(SystemTests)`

#### `def grpc_channel(self)`

#### `def session_creation_kwargs(self, grpc_channel)`

<!--NI_PYTHON_API repo=nimi-python path=src/niscope/custom_types/measurement_stats.py -->
## PYTHON MODULE: src/niscope/custom_types/measurement_stats.py

### `class MeasurementStats()`

#### `def __init__(self, result=0.0, mean=0.0, stdev=0.0, min_val=0.0, max_val=0.0, num_in_stats=0)`

#### `def __repr__(self)`

#### `def __str__(self)`

<!--NI_PYTHON_API repo=nimi-python path=src/niscope/custom_types/waveform_info.py -->
## PYTHON MODULE: src/niscope/custom_types/waveform_info.py

### `class struct_niScope_wfmInfo(ctypes.Structure)`

#### `def __init__(self, data=None, absolute_initial_x=0.0, relative_initial_x=0.0, x_increment=0.0, actual_samples=0, offset=0.0, gain=0.0, reserved1=0.0, reserved2=0.0)`

### `class WaveformInfo()`

#### `def __init__(self, data=None, absolute_initial_x=0.0, relative_initial_x=0.0, x_increment=0.0, offset=0.0, gain=0.0, reserved1=0.0, reserved2=0.0)`

#### `def __repr__(self)`

#### `def __str__(self)`

### `def _populate_samples_info(waveform_infos, sample_data, num_samples_per_waveform)`

Chunk up flat array of sample_data and copy each chunk into individual WaveformInfo instance

    Args:
        waveform_infos (Iterable of WaveformInfo): WaveformInfo class instances

        sample_data (Iterable of float): Waveform sample data

        num_samples_per_waveform (int): Number of samples belonging to each waveform
    

### `def _populate_channel_and_record_info(waveform_infos, channels, records)`

Populate the channel and record attributes of WaveformInfo instances

    Args:
        waveform_infos (Iterable of WaveformInfo): WaveformInfo class instances

        channels (Iterable of str): Channel names

        records (Iterable of int): Record numbers
    

<!--NI_PYTHON_API repo=nimi-python path=src/niscope/examples/niscope_fetch.py -->
## PYTHON MODULE: src/niscope/examples/niscope_fetch.py

### `def example(resource_name, channels, options, length, voltage)`

### `def _main(argsv)`

### `def main()`

### `def test_example()`

### `def test_main()`

<!--NI_PYTHON_API repo=nimi-python path=src/niscope/examples/niscope_fetch_forever.py -->
## PYTHON MODULE: src/niscope/examples/niscope_fetch_forever.py

### `def example(resource_name, options, total_acquisition_time_in_seconds, voltage, sample_rate_in_hz, samples_per_fetch)`

### `def _main(argsv)`

### `def main()`

### `def test_example()`

### `def test_main()`

<!--NI_PYTHON_API repo=nimi-python path=src/niscope/examples/niscope_fetch_into.py -->
## PYTHON MODULE: src/niscope/examples/niscope_fetch_into.py

### `def example(resource_name, channels, options, length, voltage)`

### `def _main(argsv)`

### `def main()`

### `def test_example()`

### `def test_main()`

<!--NI_PYTHON_API repo=nimi-python path=src/niscope/examples/niscope_read.py -->
## PYTHON MODULE: src/niscope/examples/niscope_read.py

### `def example(resource_name, channels, options, length, voltage)`

### `def _main(argsv)`

### `def main()`

### `def test_example()`

### `def test_main()`

<!--NI_PYTHON_API repo=nimi-python path=src/niscope/system_tests/test_system_niscope.py -->
## PYTHON MODULE: src/niscope/system_tests/test_system_niscope.py

### `def check_fetched_data(data, test_channels_expanded, test_record_length, test_num_records_to_fetch, test_starting_record_number=0)`

### `class SystemTests()`

#### `def single_instrument_session(self, session_creation_kwargs)`

#### `def single_instrument_session_5171(self, session_creation_kwargs)`

#### `def multi_instrument_session(self, session_creation_kwargs)`

#### `def multi_instrument_session_5171(self, session_creation_kwargs)`

#### `def session_5124(self, session_creation_kwargs)`

#### `def session_5142(self, session_creation_kwargs)`

#### `def test_vi_boolean_attribute(self, multi_instrument_session)`

#### `def test_vi_string_attribute(self, multi_instrument_session)`

#### `def test_get_channel_names_with_single_instrument_session(self, single_instrument_session_5171)`

#### `def test_get_channel_names_with_multi_instrument_session(self, multi_instrument_session_5171)`

#### `def test_read(self, multi_instrument_session, test_channels, test_channels_expanded)`

#### `def test_fetch(self, multi_instrument_session, test_channels, test_channels_expanded)`

#### `def test_fetch_defaults(self, multi_instrument_session)`

#### `def measurement_wfm_length(self, request)`

#### `def test_fetch_array_measurement(self, multi_instrument_session, measurement_wfm_length, test_channels, test_channels_expanded)`

#### `def test_fetch_array_measurement_defaults(self, multi_instrument_session)`

#### `def test_fetch_measurement_stats(self, multi_instrument_session, test_channels, test_channels_expanded)`

#### `def test_fetch_measurement_stats_defaults(self, multi_instrument_session)`

#### `def test_clear_waveform_measurement_stats(self, multi_instrument_session)`

#### `def test_waveform_processing(self, multi_instrument_session)`

#### `def test_measurement_stats_str(self, multi_instrument_session)`

#### `def test_self_test(self, multi_instrument_session)`

#### `def test_reset(self, multi_instrument_session)`

#### `def test_reset_device(self, multi_instrument_session)`

#### `def test_error_message(self, session_creation_kwargs)`

#### `def test_get_error(self, multi_instrument_session)`

#### `def test_acquisition_status(self, multi_instrument_session)`

#### `def test_self_cal(self, multi_instrument_session)`

#### `def test_get_self_cal_last_date_time(self, single_instrument_session)`

#### `def test_get_ext_cal_last_date_time(self, single_instrument_session)`

#### `def test_get_self_cal_last_temperature(self, single_instrument_session)`

#### `def test_get_ext_cal_last_temperature(self, single_instrument_session)`

#### `def test_probe_compensation_signal(self, multi_instrument_session)`

#### `def test_configure_horizontal_timing(self, multi_instrument_session)`

#### `def test_configure_chan_characteristics(self, multi_instrument_session)`

#### `def test_filter_coefficients(self, session_5142)`

#### `def test_send_software_trigger_edge(self, multi_instrument_session)`

#### `def test_disable(self, multi_instrument_session)`

#### `def test_configure_trigger_digital(self, multi_instrument_session)`

#### `def test_configure_trigger_edge(self, multi_instrument_session)`

#### `def test_configure_trigger_hysteresis(self, multi_instrument_session)`

#### `def test_import_export_buffer(self, multi_instrument_session)`

#### `def test_import_export_file(self, multi_instrument_session)`

#### `def test_configure_trigger_software(self, multi_instrument_session)`

#### `def test_configure_trigger_video(self, session_5124)`

#### `def test_configure_trigger_window(self, multi_instrument_session)`

#### `def test_multi_threading_lock_unlock(self, multi_instrument_session)`

#### `def test_multi_threading_ivi_synchronized_wrapper_releases_lock(self, multi_instrument_session)`

### `class TestLibrary(SystemTests)`

#### `def session_creation_kwargs(self)`

#### `def test_fetch_into(self, multi_instrument_session, fetch_waveform_type, type_min_value, test_channels, test_channels_expanded)`

#### `def test_configure_ref_levels(self, single_instrument_session)`

#### `def test_reset_with_defaults(self, single_instrument_session)`

### `class TestGrpc(SystemTests)`

#### `def grpc_channel(self)`

#### `def session_creation_kwargs(self, grpc_channel)`

#### `def test_configure_ref_levels(self, single_instrument_session)`

#### `def test_reset_with_defaults(self, single_instrument_session)`

<!--NI_PYTHON_API repo=nimi-python path=src/niscope/unit_tests/test_niscope.py -->
## PYTHON MODULE: src/niscope/unit_tests/test_niscope.py

### `def test_populate_samples_info()`

### `def test_populate_channel_and_record_info()`

<!--NI_PYTHON_API repo=nimi-python path=src/nise/examples/nise_basic_example.py -->
## PYTHON MODULE: src/nise/examples/nise_basic_example.py

### `def example(virtual_device_name, connection)`

### `def _main(argsv)`

### `def main()`

### `def test_example()`

### `def test_main()`

<!--NI_PYTHON_API repo=nimi-python path=src/nise/system_tests/test_system_nise.py -->
## PYTHON MODULE: src/nise/system_tests/test_system_nise.py

### `def session()`

### `def test_connect_single_disconnect_single_is_connected(session)`

### `def test_connect_and_disconnect(session)`

### `def test_connect_single_disconnect_all(session)`

### `def test_get_all_connections(session)`

### `def test_find_route(session)`

### `def test_find_route_different_length(session)`

### `def test_expand_route_spec(session)`

### `def test_is_debounced_wait_for_debounce(session)`

### `def test_error(session)`

<!--NI_PYTHON_API repo=nimi-python path=src/niswitch/examples/niswitch_connect_channels.py -->
## PYTHON MODULE: src/niswitch/examples/niswitch_connect_channels.py

### `def example(resource_name, channel1, channel2, topology, simulate)`

### `def _main(argsv)`

### `def test_example()`

### `def test_main()`

### `def main()`

<!--NI_PYTHON_API repo=nimi-python path=src/niswitch/examples/niswitch_get_device_info.py -->
## PYTHON MODULE: src/niswitch/examples/niswitch_get_device_info.py

### `def example(resource_name, topology, simulate, device, channel, relay)`

### `def _main(argsv)`

### `def test_example()`

### `def test_main()`

### `def main()`

<!--NI_PYTHON_API repo=nimi-python path=src/niswitch/examples/niswitch_relay_control.py -->
## PYTHON MODULE: src/niswitch/examples/niswitch_relay_control.py

### `def example(resource_name, topology, simulate, relay, action)`

### `def _main(argsv)`

### `def test_example()`

### `def test_main()`

### `def main()`

<!--NI_PYTHON_API repo=nimi-python path=src/niswitch/system_tests/test_system_niswitch.py -->
## PYTHON MODULE: src/niswitch/system_tests/test_system_niswitch.py

### `class SystemTests()`

#### `def session(self, session_creation_kwargs)`

#### `def session_2532(self, session_creation_kwargs)`

#### `def test_relayclose(self, session)`

#### `def test_channel_connection(self, session)`

#### `def test_continuous_software_scanning(self, session_2532)`

#### `def test_vi_string_attribute(self, session)`

#### `def test_vi_int32_attribute(self, session)`

#### `def test_vi_real64_attribute(self, session)`

#### `def test_enum_attribute(self, session_2532)`

#### `def test_write_only_attribute(self, session)`

#### `def test_method_reset(self, session)`

#### `def test_method_set_path(self, session)`

#### `def test_method_can_connect(self, session)`

#### `def test_method_reset_with_defaults(self, session)`

#### `def test_functions_get_relay_name(self, session)`

#### `def test_functions_get_channel_name(self, session)`

#### `def test_functions_self_test(self, session)`

#### `def test_locks_are_reentrant(self, session)`

#### `def test_functions_get_path(self, session)`

#### `def test_functions_connect_disconnect_multiple(self, session)`

#### `def test_functions_disable(self, session)`

#### `def test_error_message(self, session_creation_kwargs)`

#### `def test_multi_threading_lock_unlock(self, session)`

#### `def test_multi_threading_ivi_synchronized_wrapper_releases_lock(self, session)`

### `class TestLibrary(SystemTests)`

#### `def session_creation_kwargs(self)`

### `class TestGrpc(SystemTests)`

#### `def grpc_channel(self)`

#### `def session_creation_kwargs(self, grpc_channel)`

<!--NI_PYTHON_API repo=nimi-python path=src/nitclk/examples/nitclk_niscope_synchronize_with_trigger.py -->
## PYTHON MODULE: src/nitclk/examples/nitclk_niscope_synchronize_with_trigger.py

### `def example(resource_name1, resource_name2, options)`

### `def _main(argsv)`

### `def main()`

### `def test_example()`

### `def test_main()`

<!--NI_PYTHON_API repo=nimi-python path=src/nitclk/system_tests/test_system_nitclk.py -->
## PYTHON MODULE: src/nitclk/system_tests/test_system_nitclk.py

### `def single_niscope_session()`

### `def multiple_niscope_sessions()`

### `def test_nitclk_integration(single_niscope_session)`

### `def test_nitclk_vi_string(single_niscope_session)`

### `def test_nitclk_session_reference(single_niscope_session)`

### `def test_nitclk_vi_real64(single_niscope_session)`

### `def test_nitclk_error_handling()`

### `def test_nitclk_configure_for_homogeneous_triggers(multiple_niscope_sessions)`

### `def test_nitclk_sync_pulse_sender_synchronize(multiple_niscope_sessions)`

### `def test_nitclk_synchronize(multiple_niscope_sessions)`

### `def test_nitclk_initiate(multiple_niscope_sessions)`

### `def test_nitclk_is_done(multiple_niscope_sessions)`

### `def test_nitclk_wait_until_done(multiple_niscope_sessions)`

<!--NI_PYTHON_API repo=nimi-python path=src/nitclk/unit_tests/test_nitclk.py -->
## PYTHON MODULE: src/nitclk/unit_tests/test_nitclk.py

- `SESSION_NUM_FOR_TEST = 42`

### `class NitclkSupportingDriverSession()`

Session objects for drivers that support NI-TClk are expected to have a property of type nitclk.SessionReference called tclk

    This is why we're creating this fake driver class and adding the tclk property.
    

#### `def __init__(self, session_number)`

### `class TestNitclkApi()`

#### `def setup_method(self, method)`

#### `def teardown_method(self, method)`

#### `def test_initialize_one_session(self)`

#### `def test_initialize_multiple_sessions(self)`

#### `def test_configure_for_homogeneous_triggers(self)`

#### `def test_finish_sync_pulse_sender_synchronize(self)`

#### `def test_is_done(self)`

#### `def test_setup_for_sync_pulse_sender_synchronize(self)`

#### `def test_synchronize(self)`

#### `def test_synchronize_timedelta(self)`

#### `def test_synchronize_to_sync_pulse_sender(self)`

#### `def test_wait_until_done(self)`

#### `def test_api_error(self)`

#### `def test_api_get_error_description_fails(self)`

#### `def test_session_reference_error(self)`

#### `def test_session_reference_get_error_description_fails(self)`

#### `def test_set_vi_real64(self)`

#### `def test_get_vi_real64(self)`

#### `def test_set_timedelta_as_vi_real64(self)`

#### `def test_set_timedelta_as_timedelta(self)`

#### `def test_get_timedelta(self)`

#### `def test_set_vi_string(self)`

#### `def test_get_vi_string(self)`

#### `def test_set_vi_session_with_int(self)`

#### `def test_set_vi_session_with_session_reference(self)`

#### `def test_set_vi_session_with_session(self)`

#### `def test_get_tclk_session_reference(self)`

<!--NI_PYTHON_API repo=nimi-python path=src/shared/system_test_utilities.py -->
## PYTHON MODULE: src/shared/system_test_utilities.py

### `class GrpcServerProcess()`

#### `def __init__(self, config_file_path)`

#### `def __enter__(self)`

#### `def __exit__(self, exc_type, exc_val, exc_tb)`

#### `def _get_grpc_server_exe(self)`

#### `def _discard_output(self, stdout)`

### `def impl_test_multi_threading_lock_unlock(session)`

### `def impl_test_multi_threading_ivi_synchronized_wrapper_releases_lock(ivi_method_to_call)`

<!--NI_PYTHON_API repo=nimi-python path=tools/build_release.py -->
## PYTHON MODULE: tools/build_release.py

### `class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawDescriptionHelpFormatter)`

We want the description to use the raw formatting but have the parameters be formatted as before

    from stackoverflow:
    https://stackoverflow.com/questions/18462610/argumentparser-epilog-and-description-formatting-in-conjunction-with-argumentdef
    

### `def main()`

<!--NI_PYTHON_API repo=nimi-python path=tools/configure_logging.py -->
## PYTHON MODULE: tools/configure_logging.py

### `def configure_logging(lvl=logging.WARNING, logfile=None)`

<!--NI_PYTHON_API repo=nimi-python path=tools/ensure_codegen_up_to_date.py -->
## PYTHON MODULE: tools/ensure_codegen_up_to_date.py

### MODULE DOCSTRING


ensure_codegen_up_to_date
-------------------------
Ensure changes to code generation are committed to repository


### `def _configure_git_credentials()`

Configures git user name and email with dummy name and email

### `def _clean_codegen_files()`

Before code generation clean the existing codegen files

### `def _create_codegen_files()`

create codegen files

### `def _check_no_dirty_files()`

Checks if there are any modified files, outputting a warning if only line endings are different

<!--NI_PYTHON_API repo=nimi-python path=tools/install_local_wheel.py -->
## PYTHON MODULE: tools/install_local_wheel.py

### `def main()`

<!--NI_PYTHON_API repo=nimi-python path=tools/simple_mako.py -->
## PYTHON MODULE: tools/simple_mako.py

### `def generate_template(template_name, template_params, dest_file)`

### `def main()`

<!--NI_PYTHON_API repo=nimi-python path=tools/update_version_file.py -->
## PYTHON MODULE: tools/update_version_file.py

### `def main()`

<!--NI_PYTHON_API repo=nimi-python path=tools/updateReleaseInfo.py -->
## PYTHON MODULE: tools/updateReleaseInfo.py

### `def bump_version(version, bump_type)`

### `def main()`
