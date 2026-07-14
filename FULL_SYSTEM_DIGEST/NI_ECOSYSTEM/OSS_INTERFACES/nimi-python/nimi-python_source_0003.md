# NI OSS SOURCE SNAPSHOT: nimi-python

<!--NI_OSS_SNAPSHOT repo=ni/nimi-python commit=6511f8025f072f7f7021953888b916bbdc31aa2a -->

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nidigital/class.rst sha256=ac197ebed520085908976dbc900667f8cbb92b77588891cfe5d57d107a182387 bytes=263872 -->
## FILE: docs/nidigital/class.rst

- repository: `ni/nimi-python`
- source_path: `docs/nidigital/class.rst`
- sha256: `ac197ebed520085908976dbc900667f8cbb92b77588891cfe5d57d107a182387`
- bytes: 263872

````rst
.. py:module:: nidigital

Session
=======

.. py:class:: Session(self, resource_name, id_query=False, reset_device=False, options={}, *, grpc_options=None)

    

    Creates and returns a new session to the specified digital pattern instrument to use in all subsequent method calls. To place the instrument in a known startup state when creating a new session, set the reset parameter to True, which is equivalent to calling the :py:meth:`nidigital.Session.reset` method immediately after initializing the session.

    



    :param resource_name:
        

        The specified resource name shown in Measurement & Automation Explorer (MAX) for a digital pattern instrument, for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name. **resourceName** can also be a logical IVI name. This parameter accepts a comma-delimited list of strings in the form PXI1Slot2,PXI1Slot3, where ``PXI1Slot2`` is one instrument resource name and ``PXI1Slot3`` is another. When including more than one digital pattern instrument in the comma-delimited list of strings, list the instruments in the same order they appear in the pin map.

        +--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | |Note| | Note   You only can specify multiple instruments of the same model. For example, you can list two PXIe-6570s but not a PXIe-6570 and PXIe-6571. The instruments must be in the same chassis. |
        +--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. |Note| image:: note.gif

        

        .. note:: 


    :type resource_name: str

    :param id_query:
        

        A Boolean that verifies that the digital pattern instrument you initialize is supported by NI-Digital. NI-Digital automatically performs this query, so setting this parameter is not necessary.

        


    :type id_query: bool

    :param reset_device:
        

        A Boolean that specifies whether to reset a digital pattern instrument to a known state when the session is initialized. Setting the **resetDevice** value to True is equivalent to calling the :py:meth:`nidigital.Session.reset` method immediately after initializing the session.

        


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

        


    :type grpc_options: nidigital.GrpcSessionOptions


Methods
=======

abort
-----

    .. py:currentmodule:: nidigital.Session

    .. py:method:: abort()

            Stops bursting the pattern.

            



abort_keep_alive
----------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: abort_keep_alive()

            Stops the keep alive pattern if it is currently running. If a pattern burst is in progress, the method aborts the pattern burst. If you start a new pattern burst while a keep alive pattern is running, the keep alive pattern runs to the last keep alive vector, and the new pattern burst starts on the next cycle.

            



apply_levels_and_timing
-----------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: apply_levels_and_timing(levels_sheet, timing_sheet, initial_state_high_pins=None, initial_state_low_pins=None, initial_state_tristate_pins=None)

            Applies digital levels and timing values defined in previously loaded levels and timing sheets. When applying a levels sheet, only the levels specified in the sheet are affected. Any levels not specified in the sheet remain unchanged. When applying a timing sheet, all existing time sets are deleted before the new time sets are loaded.

            


            .. tip:: This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container sites to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.sites[ ... ].apply_levels_and_timing`

                To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.apply_levels_and_timing`


            :param levels_sheet:


                Name of the levels sheet to apply. Use the name of the sheet or pass the absolute file path you use in the :py:meth:`nidigital.Session.load_specifications_levels_and_timing` method. The name of the levels sheet is the file name without the directory and file extension.

                


            :type levels_sheet: str
            :param timing_sheet:


                Name of the timing sheet to apply. Use the name of the sheet or pass the absolute file path that you use in the :py:meth:`nidigital.Session.load_specifications_levels_and_timing` method. The name of the timing sheet is the file name without the directory and file extension.

                


            :type timing_sheet: str
            :param initial_state_high_pins:


                Comma-delimited list of pins, pin groups, or channels to initialize to a high state.

                


            :type initial_state_high_pins: basic sequence types or str
            :param initial_state_low_pins:


                Comma-delimited list of pins, pin groups, or channels to initialize to a low state.

                


            :type initial_state_low_pins: basic sequence types or str
            :param initial_state_tristate_pins:


                Comma-delimited list of pins, pin groups, or channels to initialize to a non-drive state (X)

                


            :type initial_state_tristate_pins: basic sequence types or str

apply_tdr_offsets
-----------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: apply_tdr_offsets(offsets)

            Applies the correction for propagation delay offsets to a digital pattern instrument. Use this method to apply TDR offsets that are stored from a past measurement or are measured by means other than the :py:meth:`nidigital.Session.tdr` method. Also use this method to apply correction for offsets if the **applyOffsets** input of the :py:meth:`nidigital.Session.tdr` method was set to False at the time of measurement.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].apply_tdr_offsets`

                To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.apply_tdr_offsets`


            :param offsets:


                TDR offsets to apply, in seconds. Specify an offset for each pin or channel in the repeated capabilities. If the repeated capabilities contain pin names, you must specify offsets for each site in the channel map per pin.

                


            :type offsets: basic sequence of hightime.timedelta, datetime.timedelta, or float in seconds

burst_pattern
-------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: burst_pattern(start_label, select_digital_function=True, wait_until_done=True, timeout=hightime.timedelta(seconds=10.0))

            Uses the start_label you specify to burst the pattern on the sites you specify. If you
            specify wait_until_done as True, waits for the burst to complete, and returns comparison results for each site.

            Digital pins retain their state at the end of a pattern burst until the first vector of the pattern burst, a call to
            :py:meth:`nidigital.Session.write_static`, or a call to :py:meth:`nidigital.Session.apply_levels_and_timing`.

            


            .. tip:: This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container sites to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.sites[ ... ].burst_pattern`

                To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.burst_pattern`


            :param start_label:


                Pattern name or exported pattern label from which to start bursting the pattern.

                


            :type start_label: str
            :param select_digital_function:


                A Boolean that specifies whether to select the digital method for the pins in the pattern prior to bursting.

                


            :type select_digital_function: bool
            :param wait_until_done:


                A Boolean that indicates whether to wait until the bursting is complete.

                


            :type wait_until_done: bool
            :param timeout:


                Maximum time (in seconds) allowed for this method to complete. If this method does not complete within this time interval, this method returns an error.

                


            :type timeout: hightime.timedelta, datetime.timedelta, or float in seconds

            :rtype: { int: bool, int: bool, ... }
            :return:


                    Dictionary where each key is a site number and value is pass/fail,
                    if wait_until_done is specified as True. Else, None.

                    



clock_generator_abort
---------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: clock_generator_abort()

            Stops clock generation on the specified channel(s) or pin(s) and pin group(s).

            


            .. tip:: This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].clock_generator_abort`

                To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.clock_generator_abort`


clock_generator_generate_clock
------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: clock_generator_generate_clock(frequency, select_digital_function=True)

            Configures clock generator frequency and initiates clock generation on the specified channel(s) or pin(s) and pin group(s).

            


            .. tip:: This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].clock_generator_generate_clock`

                To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.clock_generator_generate_clock`


            :param frequency:


                The frequency of the clock generation, in Hz.

                


            :type frequency: float
            :param select_digital_function:


                A Boolean that specifies whether to select the digital method for the pins specified prior to starting clock generation.

                


            :type select_digital_function: bool

close
-----

    .. py:currentmodule:: nidigital.Session

    .. py:method:: close()

            Closes the specified instrument session to a digital pattern instrument, aborts pattern execution, and unloads pattern memory. The channels on a digital pattern instrument remain in their current state.

            

            .. note:: This method is not needed when using the session context manager



commit
------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: commit()

            Applies all previously configured pin levels, termination modes, clocks, triggers, and pattern timing to a digital pattern instrument. If you do not call the :py:meth:`nidigital.Session.commit` method, then the initiate method or the :py:meth:`nidigital.Session.burst_pattern` method will implicitly call this method for you. Calling this method moves the session from the Uncommitted state to the Committed state.

            



configure_active_load_levels
----------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_active_load_levels(iol, ioh, vcom)

            Configures I\ :sub:`OL`, I\ :sub:`OH`, and V\ :sub:`COM` levels for the active load on the pins you specify. The DUT sources or sinks current based on the level values. To enable active load, set the termination mode to :py:data:`~nidigital.TerminationMode.ACTIVE_LOAD`. To disable active load, set the termination mode of the instrument to :py:data:`~nidigital.TerminationMode.HIGH_Z` or :py:data:`~nidigital.TerminationMode.VTERM`.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].configure_active_load_levels`

                To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.configure_active_load_levels`


            :param iol:


                Maximum current that the DUT sinks while outputting a voltage below V\ :sub:`COM`.

                


            :type iol: float
            :param ioh:


                Maximum current that the DUT sources while outputting a voltage above V\ :sub:`COM`.

                


            :type ioh: float
            :param vcom:


                Commutating voltage level at which the active load circuit switches between sourcing current and sinking current.

                


            :type vcom: float

configure_pattern_burst_sites
-----------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_pattern_burst_sites()

            Configures which sites burst the pattern on the next call to the initiate method. The pattern burst sites can also be modified through the repeated capabilities for the :py:meth:`nidigital.Session.burst_pattern` method. If a site has been disabled through the :py:meth:`nidigital.Session.disable_sites` method, the site does not burst a pattern even if included in the pattern burst sites.

            


            .. tip:: This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container sites to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.sites[ ... ].configure_pattern_burst_sites`

                To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.configure_pattern_burst_sites`


configure_time_set_compare_edges_strobe
---------------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_time_set_compare_edges_strobe(time_set_name, strobe_edge)

            Configures the strobe edge time for the specified pins. Use this method to modify time set values after applying a timing sheet with the :py:meth:`nidigital.Session.apply_levels_and_timing` method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to :py:meth:`nidigital.Session.apply_levels_and_timing`; it only affects the values of the current timing context.

            


            .. tip:: This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container pins to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.pins[ ... ].configure_time_set_compare_edges_strobe`

                To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.configure_time_set_compare_edges_strobe`


            :param time_set_name:


                The specified time set name.

                


            :type time_set_name: str
            :param strobe_edge:


                Time when the comparison happens within a vector period.

                


            :type strobe_edge: hightime.timedelta, datetime.timedelta, or float in seconds

configure_time_set_compare_edges_strobe2x
-----------------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_time_set_compare_edges_strobe2x(time_set_name, strobe_edge, strobe2_edge)

            Configures the compare strobes for the specified pins in the time set, including the 2x strobe. Use this method to modify time set values after applying a timing sheet with the :py:meth:`nidigital.Session.apply_levels_and_timing` method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to :py:meth:`nidigital.Session.apply_levels_and_timing`; it only affects the values of the current timing context.

            


            .. tip:: This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container pins to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.pins[ ... ].configure_time_set_compare_edges_strobe2x`

                To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.configure_time_set_compare_edges_strobe2x`


            :param time_set_name:


                The specified time set name.

                


            :type time_set_name: str
            :param strobe_edge:


                Time when the comparison happens within a vector period.

                


            :type strobe_edge: hightime.timedelta, datetime.timedelta, or float in seconds
            :param strobe2_edge:


                Time when the comparison happens for the second DUT cycle within a vector period.

                


            :type strobe2_edge: hightime.timedelta, datetime.timedelta, or float in seconds

configure_time_set_drive_edges
------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_time_set_drive_edges(time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge)

            Configures the drive format and drive edge placement for the specified pins. Use this method to modify time set values after applying a timing sheet with the :py:meth:`nidigital.Session.apply_levels_and_timing` method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to :py:meth:`nidigital.Session.apply_levels_and_timing`; it only affects the values of the current timing context.

            


            .. tip:: This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container pins to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.pins[ ... ].configure_time_set_drive_edges`

                To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.configure_time_set_drive_edges`


            :param time_set_name:


                The specified time set name.

                


            :type time_set_name: str
            :param format:


                Drive format of the time set.

                -   :py:data:`~nidigital.DriveFormat.NR`: Non-return.
                -   :py:data:`~nidigital.DriveFormat.RL`: Return to low.
                -   :py:data:`~nidigital.DriveFormat.RH`: Return to high.
                -   :py:data:`~nidigital.DriveFormat.SBC`: Surround by complement.

                


            :type format: :py:data:`nidigital.DriveFormat`
            :param drive_on_edge:


                Delay, in seconds, from the beginning of the vector period for turning on the pin driver.This option applies only when the prior vector left the pin in a non-drive pin state (L, H, X, V, M, E). For the SBC format, this option specifies the delay from the beginning of the vector period at which the complement of the pattern value is driven.

                


            :type drive_on_edge: hightime.timedelta, datetime.timedelta, or float in seconds
            :param drive_data_edge:


                Delay, in seconds, from the beginning of the vector period until the pattern data is driven to the pattern value.The ending state from the previous vector persists until this point.

                


            :type drive_data_edge: hightime.timedelta, datetime.timedelta, or float in seconds
            :param drive_return_edge:


                Delay, in seconds, from the beginning of the vector period until the pin changes from the pattern data to the return value, as specified in the format.

                


            :type drive_return_edge: hightime.timedelta, datetime.timedelta, or float in seconds
            :param drive_off_edge:


                Delay, in seconds, from the beginning of the vector period to turn off the pin driver when the next vector period uses a non-drive symbol (L, H, X, V, M, E).

                


            :type drive_off_edge: hightime.timedelta, datetime.timedelta, or float in seconds

configure_time_set_drive_edges2x
--------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_time_set_drive_edges2x(time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge, drive_data2_edge, drive_return2_edge)

            Configures the drive edges of the pins in the time set, including 2x edges. Use this method to modify time set values after applying a timing sheet with the :py:meth:`nidigital.Session.apply_levels_and_timing` method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to :py:meth:`nidigital.Session.apply_levels_and_timing`; it only affects the values of the current timing context.

            


            .. tip:: This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container pins to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.pins[ ... ].configure_time_set_drive_edges2x`

                To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.configure_time_set_drive_edges2x`


            :param time_set_name:


                The specified time set name.

                


            :type time_set_name: str
            :param format:


                Drive format of the time set.

                -   :py:data:`~nidigital.DriveFormat.NR`: Non-return.
                -   :py:data:`~nidigital.DriveFormat.RL`: Return to low.
                -   :py:data:`~nidigital.DriveFormat.RH`: Return to high.
                -   :py:data:`~nidigital.DriveFormat.SBC`: Surround by complement.

                


            :type format: :py:data:`nidigital.DriveFormat`
            :param drive_on_edge:


                Delay, in seconds, from the beginning of the vector period for turning on the pin driver.This option applies only when the prior vector left the pin in a non-drive pin state (L, H, X, V, M, E). For the SBC format, this option specifies the delay from the beginning of the vector period at which the complement of the pattern value is driven.

                


            :type drive_on_edge: hightime.timedelta, datetime.timedelta, or float in seconds
            :param drive_data_edge:


                Delay, in seconds, from the beginning of the vector period until the pattern data is driven to the pattern value.The ending state from the previous vector persists until this point.

                


            :type drive_data_edge: hightime.timedelta, datetime.timedelta, or float in seconds
            :param drive_return_edge:


                Delay, in seconds, from the beginning of the vector period until the pin changes from the pattern data to the return value, as specified in the format.

                


            :type drive_return_edge: hightime.timedelta, datetime.timedelta, or float in seconds
            :param drive_off_edge:


                Delay, in seconds, from the beginning of the vector period to turn off the pin driver when the next vector period uses a non-drive symbol (L, H, X, V, M, E).

                


            :type drive_off_edge: hightime.timedelta, datetime.timedelta, or float in seconds
            :param drive_data2_edge:


                Delay, in seconds, from the beginning of the vector period until the pattern data in the second DUT cycle is driven to the pattern value.

                


            :type drive_data2_edge: hightime.timedelta, datetime.timedelta, or float in seconds
            :param drive_return2_edge:


                Delay, in seconds, from the beginning of the vector period until the pin changes from the pattern data in the second DUT cycle to the return value, as specified in the format.

                


            :type drive_return2_edge: hightime.timedelta, datetime.timedelta, or float in seconds

configure_time_set_drive_format
-------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_time_set_drive_format(time_set_name, drive_format)

            Configures the drive format for the pins specified in the **pinList**. Use this method to modify time set values after applying a timing sheet with the :py:meth:`nidigital.Session.apply_levels_and_timing` method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to :py:meth:`nidigital.Session.apply_levels_and_timing`; it only affects the values of the current timing context.

            


            .. tip:: This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container pins to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.pins[ ... ].configure_time_set_drive_format`

                To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.configure_time_set_drive_format`


            :param time_set_name:


                The specified time set name.

                


            :type time_set_name: str
            :param drive_format:


                Drive format of the time set.

                -   :py:data:`~nidigital.DriveFormat.NR`: Non-return.
                -   :py:data:`~nidigital.DriveFormat.RL`: Return to low.
                -   :py:data:`~nidigital.DriveFormat.RH`: Return to high.
                -   :py:data:`~nidigital.DriveFormat.SBC`: Surround by complement.

                


            :type drive_format: :py:data:`nidigital.DriveFormat`

configure_time_set_edge
-----------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_time_set_edge(time_set_name, edge, time)

            Configures the edge placement for the pins specified in the pin list. Use this method to modify time set values after applying a timing sheet with the :py:meth:`nidigital.Session.apply_levels_and_timing` method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to :py:meth:`nidigital.Session.apply_levels_and_timing`; it only affects the values of the current timing context.

            


            .. tip:: This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container pins to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.pins[ ... ].configure_time_set_edge`

                To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.configure_time_set_edge`


            :param time_set_name:


                The specified time set name.

                


            :type time_set_name: str
            :param edge:


                Name of the edge.

                -   :py:data:`~nidigital.TimeSetEdgeType.DRIVE_ON`
                -   :py:data:`~nidigital.TimeSetEdgeType.DRIVE_DATA`
                -   :py:data:`~nidigital.TimeSetEdgeType.DRIVE_RETURN`
                -   :py:data:`~nidigital.TimeSetEdgeType.DRIVE_OFF`
                -   :py:data:`~nidigital.TimeSetEdgeType.COMPARE_STROBE`
                -   :py:data:`~nidigital.TimeSetEdgeType.DRIVE_DATA2`
                -   :py:data:`~nidigital.TimeSetEdgeType.DRIVE_RETURN2`
                -   :py:data:`~nidigital.TimeSetEdgeType.COMPARE_STROBE2`

                


            :type edge: :py:data:`nidigital.TimeSetEdgeType`
            :param time:


                The time from the beginning of the vector period in which to place the edge.

                


            :type time: hightime.timedelta, datetime.timedelta, or float in seconds

configure_time_set_edge_multiplier
----------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_time_set_edge_multiplier(time_set_name, edge_multiplier)

            Configures the edge multiplier of the pins in the time set. Use this method to modify time set values after applying a timing sheet with the :py:meth:`nidigital.Session.apply_levels_and_timing` method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to :py:meth:`nidigital.Session.apply_levels_and_timing`; it only affects the values of the current timing context.

            


            .. tip:: This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container pins to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.pins[ ... ].configure_time_set_edge_multiplier`

                To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.configure_time_set_edge_multiplier`


            :param time_set_name:


                The specified time set name.

                


            :type time_set_name: str
            :param edge_multiplier:


                The specified edge multiplier for the pins in the pin list.

                


            :type edge_multiplier: int

configure_time_set_period
-------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_time_set_period(time_set_name, period)

            Configures the period of a time set. Use this method to modify time set values after applying a timing sheet with the :py:meth:`nidigital.Session.apply_levels_and_timing` method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to :py:meth:`nidigital.Session.apply_levels_and_timing`; it only affects the values of the current timing context.

            



            :param time_set_name:


                The specified time set name.

                


            :type time_set_name: str
            :param period:


                Period for this time set, in seconds.

                


            :type period: hightime.timedelta, datetime.timedelta, or float in seconds

configure_voltage_levels
------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: configure_voltage_levels(vil, vih, vol, voh, vterm)

            Configures voltage levels for the pins you specify.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].configure_voltage_levels`

                To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.configure_voltage_levels`


            :param vil:


                Voltage that the instrument will apply to the input of the DUT when the pin driver drives a logic low (0).

                


            :type vil: float
            :param vih:


                Voltage that the instrument will apply to the input of the DUT when the test instrument drives a logic high (1).

                


            :type vih: float
            :param vol:


                Output voltage below which the comparator on the pin driver interprets a logic low (L).

                


            :type vol: float
            :param voh:


                Output voltage above which the comparator on the pin driver interprets a logic high (H).

                


            :type voh: float
            :param vterm:


                Termination voltage the instrument applies during non-drive cycles when the termination mode is set to V\ :sub:`term`. The instrument applies the termination voltage through a 50 ohm parallel termination resistance.

                


            :type vterm: float

create_capture_waveform_from_file_digicapture
---------------------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: create_capture_waveform_from_file_digicapture(waveform_name, waveform_file_path)

            Creates a capture waveform with the configuration information from a Digicapture file generated by the Digital Pattern Editor.

            



            :param waveform_name:


                Waveform name you want to use. You must specify waveform_name if the file contains multiple waveforms. Use the waveform_name with the capture_start opcode in your pattern.

                


            :type waveform_name: str
            :param waveform_file_path:


                Absolute file path to the capture waveform file (.digicapture) you want to load.

                


            :type waveform_file_path: str

create_capture_waveform_parallel
--------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: create_capture_waveform_parallel(waveform_name)

            Sets the capture waveform settings for parallel acquisition. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.

            


            .. tip:: This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container pins to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.pins[ ... ].create_capture_waveform_parallel`

                To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.create_capture_waveform_parallel`


            :param waveform_name:


                Waveform name you want to use. Use the waveform_name with the capture_start opcode in your pattern.

                


            :type waveform_name: str

create_capture_waveform_serial
------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: create_capture_waveform_serial(waveform_name, sample_width, bit_order)

            Sets the capture waveform settings for serial acquisition. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.

            


            .. tip:: This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container pins to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.pins[ ... ].create_capture_waveform_serial`

                To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.create_capture_waveform_serial`


            :param waveform_name:


                Waveform name you want to use. Use the waveform_name with the capture_start opcode in your pattern.

                


            :type waveform_name: str
            :param sample_width:


                Width in bits of each serial sample. Valid values are between 1 and 32.

                


            :type sample_width: int
            :param bit_order:


                Order in which to shift the bits.

                -   :py:data:`~nidigital.BitOrder.MSB`: Specifies the bit order by most significant bit first.
                -   :py:data:`~nidigital.BitOrder.LSB`: Specifies the bit order by least significant bit first.

                


            :type bit_order: :py:data:`nidigital.BitOrder`

create_source_waveform_from_file_tdms
-------------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: create_source_waveform_from_file_tdms(waveform_name, waveform_file_path, write_waveform_data=True)

            Creates a source waveform with configuration information from a TDMS file generated by the Digital Pattern Editor. It also optionally writes waveform data from the file.

            



            :param waveform_name:


                The waveform name you want to use from the file. You must specify waveform_name if the file contains multiple waveforms. Use the waveform_name with the source_start opcode in your pattern.

                


            :type waveform_name: str
            :param waveform_file_path:


                Absolute file path to the load source waveform file (.tdms).

                


            :type waveform_file_path: str
            :param write_waveform_data:


                A Boolean that writes waveform data to source memory if True and the waveform data is in the file.

                


            :type write_waveform_data: bool

create_source_waveform_parallel
-------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: create_source_waveform_parallel(waveform_name, data_mapping)

            Sets the source waveform settings required for parallel sourcing. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.

            


            .. tip:: This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container pins to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.pins[ ... ].create_source_waveform_parallel`

                To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.create_source_waveform_parallel`


            :param waveform_name:


                The name to assign to the waveform. Use the waveform_name  with source_start opcode in your pattern.

                


            :type waveform_name: str
            :param data_mapping:


                Parameter that specifies how to map data on multiple sites.

                -   :py:data:`~nidigital.SourceDataMapping.BROADCAST`: Broadcasts the waveform you specify to all sites.
                -   :py:data:`~nidigital.SourceDataMapping.SITE_UNIQUE`: Sources unique waveform data to each site.

                


            :type data_mapping: :py:data:`nidigital.SourceDataMapping`

create_source_waveform_serial
-----------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: create_source_waveform_serial(waveform_name, data_mapping, sample_width, bit_order)

            Sets the source waveform settings required for serial sourcing. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.

            


            .. tip:: This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container pins to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.pins[ ... ].create_source_waveform_serial`

                To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.create_source_waveform_serial`


            :param waveform_name:


                The name to assign to the waveform. Use the waveform_name  with source_start opcode in your pattern.

                


            :type waveform_name: str
            :param data_mapping:


                Parameter that specifies how to map data on multiple sites.

                -   :py:data:`~nidigital.SourceDataMapping.BROADCAST`: Broadcasts the waveform you specify to all sites.
                -   :py:data:`~nidigital.SourceDataMapping.SITE_UNIQUE`: Sources unique waveform data to each site.

                


            :type data_mapping: :py:data:`nidigital.SourceDataMapping`
            :param sample_width:


                Width in bits of each serial sample. Valid values are between 1 and 32.

                


            :type sample_width: int
            :param bit_order:


                Order in which to shift the bits.

                -   :py:data:`~nidigital.BitOrder.MSB`: Specifies the bit order by most significant bit first.
                -   :py:data:`~nidigital.BitOrder.LSB`: Specifies the bit order by least significant bit first.

                


            :type bit_order: :py:data:`nidigital.BitOrder`

create_time_set
---------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: create_time_set(name)

            Creates a time set with the name that you specify. Use this method when you want to create time sets programmatically rather than with a timing sheet.

            



            :param name:


                The specified name of the new time set.

                


            :type name: str

delete_all_time_sets
--------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: delete_all_time_sets()

            Deletes all time sets from instrument memory.

            



disable_sites
-------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: disable_sites()

            Disables specified sites. Disabled sites are not included in pattern bursts initiated by the initiate method or the :py:meth:`nidigital.Session.burst_pattern` method, even if the site is specified in the list of pattern burst sites in :py:meth:`nidigital.Session.configure_pattern_burst_sites` method or in the repeated capabilities for the :py:meth:`nidigital.Session.burst_pattern` method. Additionally, if you specify a list of pin or pin group names in repeated capabilities in any NI-Digital method, digital pattern instrument channels mapped to disabled sites are not affected by the method. The methods that return per-pin data, such as the :py:meth:`nidigital.Session.ppmu_measure` method, do not return data for channels mapped to disabled sites. The digital pattern instrument channels mapped to the sites specified are left in their current state. NI TestStand Semiconductor Module requires all sites to always be enabled, and manages the set of active sites without disabling the sites in the digital instrument session. Do not use this method with the Semiconductor Module.

            


            .. tip:: This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container sites to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.sites[ ... ].disable_sites`

                To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.disable_sites`


enable_match_fail_combination
-----------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: enable_match_fail_combination()

            Configures digital pattern instruments and the PXIe-6674T timing and synchronization instrument to combine pattern comparison results and control subsequent pattern execution across digital pattern instruments based on those results. You must initialize the PXIe-6674T using NI-Sync and call this method from a multi-instrument session.

            



enable_sites
------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: enable_sites()

            Enables the sites you specify. All sites are enabled by default.

            


            .. tip:: This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container sites to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.sites[ ... ].enable_sites`

                To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.enable_sites`


fetch_capture_waveform
----------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: fetch_capture_waveform(waveform_name, samples_to_read, timeout=hightime.timedelta(seconds=10.0))

            Returns dictionary where each key is a site number and value is a collection of digital states representing capture waveform data

            


            .. tip:: This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container sites to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.sites[ ... ].fetch_capture_waveform`

                To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.fetch_capture_waveform`


            :param waveform_name:


                Waveform name you create with the create capture waveform method. Use the waveform_name parameter with capture_start opcode in your pattern.

                


            :type waveform_name: str
            :param samples_to_read:


                Number of samples to fetch.

                


            :type samples_to_read: int
            :param timeout:


                Maximum time (in seconds) allowed for this method to complete. If this method does not complete within this time interval, this method returns an error.

                


            :type timeout: hightime.timedelta, datetime.timedelta, or float in seconds

            :rtype: { int: memoryview of array.array of unsigned int, int: memoryview of array.array of unsigned int, ... }
            :return:


                    Dictionary where each key is a site number and value is a collection of digital states representing capture waveform data

                    



fetch_history_ram_cycle_information
-----------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: fetch_history_ram_cycle_information(position, samples_to_read)

            Returns the pattern information acquired for the specified cycles.

            If the pattern is using the edge multiplier feature, cycle numbers represent tester cycles, each of which may
            consist of multiple DUT cycles. When using pins with mixed edge multipliers, pins may return
            :py:data:`~nidigital.PinState.PIN_STATE_NOT_ACQUIRED` for DUT cycles where those pins do not have edges defined.

            Site number on which to retrieve pattern information must be specified via sites repeated capability.
            The method returns an error if more than one site is specified.

            Pins for which to retrieve pattern information must be specified via pins repeated capability.
            If pins are not specified, pin list from the pattern containing the start label is used. Call
            :py:meth:`nidigital.Session.get_pattern_pin_names` with the start label to retrieve the pins associated with the pattern burst:

            .. code:: python

             session.sites[0].pins['PinA', 'PinB'].fetch_history_ram_cycle_information(0, -1)

            

            .. note:: Before bursting a pattern, you must configure the History RAM trigger and specify which cycles to acquire.

                :py:attr:`nidigital.Session.history_ram_trigger_type` should be used to specify the trigger condition on which History RAM
                starts acquiring pattern information.

                If History RAM trigger is configured as :py:data:`~nidigital.HistoryRAMTriggerType.CYCLE_NUMBER`,
                :py:attr:`nidigital.Session.cycle_number_history_ram_trigger_cycle_number` should be used to specify the cycle number on which
                History RAM starts acquiring pattern information.

                If History RAM trigger is configured as :py:data:`~nidigital.HistoryRAMTriggerType.PATTERN_LABEL`,
                :py:attr:`nidigital.Session.pattern_label_history_ram_trigger_label` should be used to specify the pattern label from which to
                start acquiring pattern information.
                :py:attr:`nidigital.Session.pattern_label_history_ram_trigger_vector_offset` should be used to specify the number of vectors
                following the specified pattern label from which to start acquiring pattern information.
                :py:attr:`nidigital.Session.pattern_label_history_ram_trigger_cycle_offset` should be used to specify the number of cycles
                following the specified pattern label and vector offset from which to start acquiring pattern information.

                For all History RAM trigger conditions, :py:attr:`nidigital.Session.history_ram_pretrigger_samples` should be used to specify
                the number of samples to acquire before the trigger conditions are met. If you configure History RAM to only
                acquire failed cycles, you must set :py:attr:`nidigital.Session.history_ram_pretrigger_samples` to 0.

                :py:attr:`nidigital.Session.history_ram_cycles_to_acquire` should be used to specify which cycles History RAM acquires after
                the trigger conditions are met.


            .. tip:: This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container pins to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.pins[ ... ].fetch_history_ram_cycle_information`

                To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.fetch_history_ram_cycle_information`


            :param position:


                Sample index from which to start fetching pattern information.

                


            :type position: int
            :param samples_to_read:


                Number of samples to fetch. A value of -1 specifies to fetch all available samples.

                


            :type samples_to_read: int

            :rtype: list of HistoryRAMCycleInformation
            :return:


                    Returns a list of class instances with
                    the following information about each pattern cycle:

                    -  **pattern_name** (str)  Name of the pattern for the acquired cycle.
                    -  **time_set_name** (str) Time set for the acquired cycle.
                    -  **vector_number** (int) Vector number within the pattern for the acquired cycle. Vector numbers start
                       at 0 from the beginning of the pattern.
                    -  **cycle_number** (int) Cycle number acquired by this History RAM sample. Cycle numbers start at 0
                       from the beginning of the pattern burst.
                    -  **scan_cycle_number** (int) Scan cycle number acquired by this History RAM sample. Scan cycle numbers
                       start at 0 from the first cycle of the scan vector. Scan cycle numbers are -1 for cycles that do not
                       have a scan opcode.
                    -  **expected_pin_states** (list of list of enums.PinState) Pin states as expected by the loaded
                       pattern in the order specified in the pin list. Pins without defined edges in the specified DUT cycle
                       will have a value of :py:data:`~nidigital.PinState.PIN_STATE_NOT_ACQUIRED`.
                       Length of the outer list will be equal to the value of edge multiplier for the given vector.
                       Length of the inner list will be equal to the number of pins requested.
                    -  **actual_pin_states** (list of list of enums.PinState) Pin states acquired by History RAM in the
                       order specified in the pin list. Pins without defined edges in the specified DUT cycle will have a
                       value of :py:data:`~nidigital.PinState.PIN_STATE_NOT_ACQUIRED`.
                       Length of the outer list will be equal to the value of edge multiplier for the given vector.
                       Length of the inner list will be equal to the number of pins requested.
                    -  **per_pin_pass_fail** (list of list of bool) Pass fail information for pins in the order specified in
                       the pin list. Pins without defined edges in the specified DUT cycle will have a value of pass (True).
                       Length of the outer list will be equal to the value of edge multiplier for the given vector.
                       Length of the inner list will be equal to the number of pins requested.

                    



frequency_counter_measure_frequency
-----------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: frequency_counter_measure_frequency()

            Measures the frequency on the specified channel(s) over the specified measurement time. All channels in the repeated capabilities should have the same measurement time.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].frequency_counter_measure_frequency`

                To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.frequency_counter_measure_frequency`


            :rtype: list of float
            :return:


                    The returned frequency counter measurement, in Hz.This method returns -1 if the measurement is invalid for the channel.

                    



get_channel_names
-----------------

    .. py:currentmodule:: nidigital.Session

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

                    



get_fail_count
--------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_fail_count()

            Returns the comparison fail count for pins in the repeated capabilities.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].get_fail_count`

                To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.get_fail_count`


            :rtype: list of int
            :return:


                    Number of failures in an array. If a site is disabled or not enabled for burst, the method does not return data for that site. You can also use the :py:meth:`nidigital.Session.get_pin_results_pin_information` method to obtain a sorted list of returned sites and channels.

                    



get_history_ram_sample_count
----------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_history_ram_sample_count()

            Returns the number of samples History RAM acquired on the last pattern burst.

            

            .. note:: Before bursting a pattern, you must configure the History RAM trigger and specify which cycles to acquire.

                :py:attr:`nidigital.Session.history_ram_trigger_type` should be used to specify the trigger condition on which History RAM
                starts acquiring pattern information.

                If History RAM trigger is configured as :py:data:`~nidigital.HistoryRAMTriggerType.CYCLE_NUMBER`,
                :py:attr:`nidigital.Session.cycle_number_history_ram_trigger_cycle_number` should be used to specify the cycle number on which
                History RAM starts acquiring pattern information.

                If History RAM trigger is configured as :py:data:`~nidigital.HistoryRAMTriggerType.PATTERN_LABEL`,
                :py:attr:`nidigital.Session.pattern_label_history_ram_trigger_label` should be used to specify the pattern label from which to
                start acquiring pattern information.
                :py:attr:`nidigital.Session.pattern_label_history_ram_trigger_vector_offset` should be used to specify the number of vectors
                following the specified pattern label from which to start acquiring pattern information.
                :py:attr:`nidigital.Session.pattern_label_history_ram_trigger_cycle_offset` should be used to specify the number of cycles
                following the specified pattern label and vector offset from which to start acquiring pattern information.

                For all History RAM trigger conditions, :py:attr:`nidigital.Session.history_ram_pretrigger_samples` should be used to specify
                the number of samples to acquire before the trigger conditions are met. If you configure History RAM to only
                acquire failed cycles, you must set :py:attr:`nidigital.Session.history_ram_pretrigger_samples` to 0.

                :py:attr:`nidigital.Session.history_ram_cycles_to_acquire` should be used to specify which cycles History RAM acquires after
                the trigger conditions are met.


            .. tip:: This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container sites to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.sites[ ... ].get_history_ram_sample_count`

                To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.get_history_ram_sample_count`


            :rtype: int
            :return:


                    The returned number of samples that History RAM acquired.

                    



get_pattern_pin_names
---------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_pattern_pin_names(start_label)

            Returns the pattern pin list.

            



            :param start_label:


                Pattern name or exported pattern label from which to get the pin names that the pattern references.

                


            :type start_label: str

            :rtype: list of str
            :return:


                    List of pins referenced by the pattern with the **startLabel**.

                    



get_pin_results_pin_information
-------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_pin_results_pin_information()

            Returns the pin names, site numbers, and channel names that correspond to per-pin data read from the digital pattern instrument. The method returns pin information in the same order as values read using the :py:meth:`nidigital.Session.read_static` method, :py:meth:`nidigital.Session.ppmu_measure` method, and :py:meth:`nidigital.Session.get_fail_count` method. Use this method to match values the previously listed methods return with pins, sites, and instrument channels.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].get_pin_results_pin_information`

                To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.get_pin_results_pin_information`


            :rtype: list of PinInfo
            :return:


                    List of named tuples with fields:

                    - **pin_name** (str)
                    - **site_number** (int)
                    - **channel_name** (str)

                    



get_site_pass_fail
------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_site_pass_fail()

            Returns dictionary where each key is a site number and value is pass/fail

            


            .. tip:: This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container sites to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.sites[ ... ].get_site_pass_fail`

                To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.get_site_pass_fail`


            :rtype: { int: bool, int: bool, ... }
            :return:


                    Dictionary where each key is a site number and value is pass/fail

                    



get_time_set_drive_format
-------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_time_set_drive_format(time_set_name)

            Returns the drive format of a pin in the specified time set.

            


            .. tip:: This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container pins to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.pins[ ... ].get_time_set_drive_format`

                To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.get_time_set_drive_format`


            :param time_set_name:


                The specified time set name.

                


            :type time_set_name: str

            :rtype: :py:data:`nidigital.DriveFormat`
            :return:


                    Returned drive format of the time set for the specified pin.

                    



get_time_set_edge
-----------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_time_set_edge(time_set_name, edge)

            Returns the edge time of a pin in the specified time set.

            


            .. tip:: This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container pins to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.pins[ ... ].get_time_set_edge`

                To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.get_time_set_edge`


            :param time_set_name:


                The specified time set name.

                


            :type time_set_name: str
            :param edge:


                Name of the edge.

                -   :py:data:`~nidigital.TimeSetEdgeType.DRIVE_ON`
                -   :py:data:`~nidigital.TimeSetEdgeType.DRIVE_DATA`
                -   :py:data:`~nidigital.TimeSetEdgeType.DRIVE_RETURN`
                -   :py:data:`~nidigital.TimeSetEdgeType.DRIVE_OFF`
                -   :py:data:`~nidigital.TimeSetEdgeType.COMPARE_STROBE`
                -   :py:data:`~nidigital.TimeSetEdgeType.DRIVE_DATA2`
                -   :py:data:`~nidigital.TimeSetEdgeType.DRIVE_RETURN2`
                -   :py:data:`~nidigital.TimeSetEdgeType.COMPARE_STROBE2`

                


            :type edge: :py:data:`nidigital.TimeSetEdgeType`

            :rtype: hightime.timedelta
            :return:


                    Time from the beginning of the vector period in which to place the edge.

                    



get_time_set_edge_multiplier
----------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_time_set_edge_multiplier(time_set_name)

            Returns the edge multiplier of the specified time set.

            


            .. tip:: This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container pins to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.pins[ ... ].get_time_set_edge_multiplier`

                To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.get_time_set_edge_multiplier`


            :param time_set_name:


                The specified time set name.

                


            :type time_set_name: str

            :rtype: int
            :return:


                    Returned edge multiplier of the time set for the specified pin.

                    



get_time_set_period
-------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: get_time_set_period(time_set_name)

            Returns the period of the specified time set.

            



            :param time_set_name:


                The specified time set name.

                


            :type time_set_name: str

            :rtype: hightime.timedelta
            :return:


                    Returned period, in seconds, that the edge is configured to.

                    



initiate
--------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: initiate()

            Starts bursting the pattern configured by :py:attr:`nidigital.Session.start_label`, causing the NI-Digital session to be committed. To stop the pattern burst, call :py:meth:`nidigital.Session.abort`. If keep alive pattern is bursting when :py:meth:`nidigital.Session.abort` is called or upon exiting the context manager, keep alive pattern will not be stopped. To stop the keep alive pattern, call :py:meth:`nidigital.Session.abort_keep_alive`.

            

            .. note:: This method will return a Python context manager that will initiate on entering and abort on exit.



is_done
-------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: is_done()

            Checks the hardware to determine if the pattern burst has completed or if any errors have occurred.

            



            :rtype: bool
            :return:


                    A Boolean that indicates whether the pattern burst completed.

                    



is_site_enabled
---------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: is_site_enabled()

            Checks if a specified site is enabled.

            

            .. note:: The method returns an error if more than one site is specified.


            .. tip:: This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container sites to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.sites[ ... ].is_site_enabled`

                To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.is_site_enabled`


            :rtype: bool
            :return:


                    Boolean value that returns whether the site is enabled or disabled.

                    



load_pattern
------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: load_pattern(file_path)

            Loads the specified pattern file.

            



            :param file_path:


                Absolute file path of the binary .digipat pattern file to load. Specify the pattern to burst using :py:attr:`nidigital.Session.start_label` or the start_label parameter of the :py:meth:`nidigital.Session.burst_pattern` method.

                


            :type file_path: str

load_pin_map
------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: load_pin_map(file_path)

            Loads a pin map file. You can load only a single pin and channel map file during an NI-Digital Pattern Driver session. To switch pin maps, create a new session or call the :py:meth:`nidigital.Session.reset` method.

            



            :param file_path:


                Absolute file path to a pin map file created with the Digital Pattern Editor or the NI TestStand Semiconductor Module.

                


            :type file_path: str

load_specifications_levels_and_timing
-------------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: load_specifications_levels_and_timing(specifications_file_paths=None, levels_file_paths=None, timing_file_paths=None)

            Loads settings in specifications, levels, and timing sheets. These settings are not
            applied to the digital pattern instrument until :py:meth:`nidigital.Session.apply_levels_and_timing` is called.

            If the levels and timing sheets contains formulas, they are evaluated at load time.
            If the formulas refer to variables, the specifications sheets that define those
            variables must be loaded either first, or at the same time as the levels and timing sheets.

            



            :param specifications_file_paths:


                Absolute file path of one or more specifications files.

                


            :type specifications_file_paths: str or basic sequence of str
            :param levels_file_paths:


                Absolute file path of one or more levels sheet files.

                


            :type levels_file_paths: str or basic sequence of str
            :param timing_file_paths:


                Absolute file path of one or more timing sheet files.

                


            :type timing_file_paths: str or basic sequence of str

lock
----

    .. py:currentmodule:: nidigital.Session

.. py:method:: lock()

    Obtains a multithread lock on the device session. Before doing so, the
    software waits until all other execution threads release their locks
    on the device session.

    Other threads may have obtained a lock on this session for the
    following reasons:

        -  The application called the :py:meth:`nidigital.Session.lock` method.
        -  A call to NI-Digital Pattern Driver locked the session.
        -  After a call to the :py:meth:`nidigital.Session.lock` method returns
           successfully, no other threads can access the device session until
           you call the :py:meth:`nidigital.Session.unlock` method or exit out of the with block when using
           lock context manager.
        -  Use the :py:meth:`nidigital.Session.lock` method and the
           :py:meth:`nidigital.Session.unlock` method around a sequence of calls to
           instrument driver methods if you require that the device retain its
           settings through the end of the sequence.

    You can safely make nested calls to the :py:meth:`nidigital.Session.lock` method
    within the same thread. To completely unlock the session, you must
    balance each call to the :py:meth:`nidigital.Session.lock` method with a call to
    the :py:meth:`nidigital.Session.unlock` method.

    One method for ensuring there are the same number of unlock method calls as there is lock calls
    is to use lock as a context manager

        .. code:: python

            with nidigital.Session('dev1') as session:
                with session.lock():
                    # Calls to session within a single lock context

        The first `with` block ensures the session is closed regardless of any exceptions raised

        The second `with` block ensures that unlock is called regardless of any exceptions raised

    :rtype: context manager
    :return:
        When used in a `with` statement, :py:meth:`nidigital.Session.lock` acts as
        a context manager and unlock will be called when the `with` block is exited

ppmu_measure
------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: ppmu_measure(measurement_type)

            Instructs the PPMU to measure voltage or current. This method can be called to take a voltage measurement even if the pin method is not set to PPMU.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].ppmu_measure`

                To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.ppmu_measure`


            :param measurement_type:


                Parameter that specifies whether the PPMU measures voltage or current from the DUT.

                -   :py:data:`~nidigital.PPMUMeasurementType.CURRENT`: The PPMU measures current from the DUT.
                -   :py:data:`~nidigital.PPMUMeasurementType.VOLTAGE`: The PPMU measures voltage from the DUT.

                


            :type measurement_type: :py:data:`nidigital.PPMUMeasurementType`

            :rtype: list of float
            :return:


                    The returned array of measurements in the order you specify in the repeated capabilities. If a site is disabled, the method does not return data for that site. You can also use the :py:meth:`nidigital.Session.get_pin_results_pin_information` method to obtain a sorted list of returned sites and channels.

                    



ppmu_source
-----------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: ppmu_source()

            Starts sourcing voltage or current from the PPMU. This method automatically selects the PPMU method. Changes to PPMU source settings do not take effect until you call this method. If you modify source settings after you call this method, you must call this method again for changes in the configuration to take effect.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].ppmu_source`

                To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.ppmu_source`


read_sequencer_flag
-------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: read_sequencer_flag(flag)

            Reads the state of a pattern sequencer flag. Use pattern sequencer flags to coordinate execution between the pattern sequencer and a runtime test program.

            



            :param flag:


                The pattern sequencer flag you want to read.

                -   :py:data:`~nidigital.SequencerFlag.FLAG0` ("seqflag0"): Reads pattern sequencer flag 0.
                -   :py:data:`~nidigital.SequencerFlag.FLAG1` ("seqflag1"): Reads pattern sequencer flag 1.
                -   :py:data:`~nidigital.SequencerFlag.FLAG2` ("seqflag2"): Reads pattern sequencer flag 2.
                -   :py:data:`~nidigital.SequencerFlag.FLAG3` ("seqflag3"): Reads pattern sequencer flag 3.

                


            :type flag: :py:data:`nidigital.SequencerFlag`

            :rtype: bool
            :return:


                    A Boolean that indicates the state of the pattern sequencer flag you specify.

                    



read_sequencer_register
-----------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: read_sequencer_register(reg)

            Reads the value of a pattern sequencer register. Use pattern sequencer registers to pass numeric values between the pattern sequencer and a runtime test program. For example, you can use this method to read a register modified by the write_reg opcode during a pattern burst.

            



            :param reg:


                The sequencer register to read from.

                -   :py:data:`~nidigital.SequencerRegister.REGISTER0` ("reg0"): Reads sequencer register 0.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER1` ("reg1"): Reads sequencer register 1.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER2` ("reg2"): Reads sequencer register 2.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER3` ("reg3"): Reads sequencer register 3.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER4` ("reg4"): Reads sequencer register 4.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER5` ("reg5"): Reads sequencer register 5.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER6` ("reg6"): Reads sequencer register 6.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER7` ("reg7"): Reads sequencer register 7.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER8` ("reg8"): Reads sequencer register 8.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER9` ("reg9"): Reads sequencer register 9.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER10` ("reg10"): Reads sequencer register 10.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER11` ("reg11"): Reads sequencer register 11.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER12` ("reg12"): Reads sequencer register 12.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER13` ("reg13"): Reads sequencer register 13.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER14` ("reg14"): Reads sequencer register 14.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER15` ("reg15"): Reads sequencer register 15.

                


            :type reg: :py:data:`nidigital.SequencerRegister`

            :rtype: int
            :return:


                    Value read from the sequencer register.

                    



read_static
-----------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: read_static()

            Reads the current state of comparators for pins you specify in the repeated capabilities. If there are uncommitted changes to levels or the termination mode, this method commits the changes to the pins.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].read_static`

                To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.read_static`


            :rtype: list of :py:data:`nidigital.PinState`
            :return:


                    The returned array of pin states read from the channels in the repeated capabilities. Data is returned in the order you specify in the repeated capabilities. If a site is disabled, the method does not return data for that site. You can also use the :py:meth:`nidigital.Session.get_pin_results_pin_information` method to obtain a sorted list of returned sites and channels.

                    -   :py:data:`~nidigital.PinState.L`: The comparators read a logic low pin state.
                    -   :py:data:`~nidigital.PinState.H`: The comparators read a logic high pin state.
                    -   :py:data:`~nidigital.PinState.M`: The comparators read a midband pin state.
                    -   :py:data:`~nidigital.PinState.V`: The comparators read a value that is above VOH and below VOL, which can occur when you set VOL higher than VOH.

                    



reset
-----

    .. py:currentmodule:: nidigital.Session

    .. py:method:: reset()

            Returns a digital pattern instrument to a known state. This method performs the following actions:

            - Aborts pattern execution.
            - Clears pin maps, time sets, source and capture waveforms, and patterns.
            - Resets all properties to default values, including the :py:attr:`nidigital.Session.selected_function` property that is set to :py:data:`~nidigital.SelectedFunction.DISCONNECT`, causing the I/O switches to open.
            - Stops exporting all external signals and events.

            



reset_device
------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: reset_device()

            Returns a digital pattern instrument to a known state. This method performs the following actions:

            - Aborts pattern execution.
            - Clears pin maps, time sets, source and capture waveforms, and patterns.
            - Resets all properties to default values, including the :py:attr:`nidigital.Session.selected_function` property that is set to :py:data:`~nidigital.SelectedFunction.DISCONNECT`, causing the I/O switches to open.
            - Stops export of all external signals and events.
            - Clears over-temperature and over-power conditions.

            



self_calibrate
--------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: self_calibrate()

            Performs self-calibration on a digital pattern instrument.

            



self_test
---------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: self_test()

            Returns self test results from a digital pattern instrument. This test requires several minutes to execute.

            Raises `SelfTestError` on self test failure. Properties on exception object:

            - code - failure code from driver
            - message - status message from driver

            +----------------+-------------------+
            | Self-Test Code | Description       |
            +================+===================+
            | 0              | Self test passed. |
            +----------------+-------------------+
            | 1              | Self test failed. |
            +----------------+-------------------+



send_software_edge_trigger
--------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: send_software_edge_trigger(trigger, trigger_identifier)

            Forces a particular edge-based trigger to occur regardless of how the specified trigger is configured. You can use this method as a software override.

            



            :param trigger:


                Trigger specifies the trigger you want to override.

                +--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
                | Defined Values                                         |                                                                                                                                 |
                +========================================================+=================================================================================================================================+
                | :py:data:`~nidigital.SoftwareTrigger.START`            | Overrides the Start trigger. You must specify an empty string in the trigger_identifier parameter.                              |
                +--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nidigital.SoftwareTrigger.CONDITIONAL_JUMP` | Specifies to route a conditional jump trigger. You must specify a conditional jump trigger in the trigger_identifier parameter. |
                +--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type trigger: :py:data:`nidigital.SoftwareTrigger`
            :param trigger_identifier:


                Trigger Identifier specifies the instance of the trigger you want to override.
                If trigger is specified as :py:data:`~nidigital.NIDIGITAL_VAL_START_TRIGGER`, this parameter must be an empty string. If trigger is
                specified as :py:data:`~nidigital.NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER`, allowed values are conditionalJumpTrigger0,
                conditionalJumpTrigger1, conditionalJumpTrigger2, and conditionalJumpTrigger3.

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type trigger_identifier: str

tdr
---

    .. py:currentmodule:: nidigital.Session

    .. py:method:: tdr(apply_offsets=True)

            Measures propagation delays through cables, connectors, and load boards using Time-Domain Reflectometry (TDR). Ensure that the channels and pins you select are connected to an open circuit.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].tdr`

                To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.tdr`


            :param apply_offsets:


                A Boolean that specifies whether to apply the measured TDR offsets. If you need to adjust the measured offsets prior to applying, set this input to False, and call the :py:meth:`nidigital.Session.apply_tdr_offsets` method to specify the adjusted TDR offsets values.

                


            :type apply_offsets: bool

            :rtype: list of hightime.timedelta
            :return:


                    Measured TDR offsets specified in seconds.

                    



unload_all_patterns
-------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: unload_all_patterns(unload_keep_alive_pattern=False)

            Unloads all patterns, source waveforms, and capture waveforms from a digital pattern instrument.

            



            :param unload_keep_alive_pattern:


                A Boolean that specifies whether to keep or unload the keep alive pattern.

                


            :type unload_keep_alive_pattern: bool

unload_specifications
---------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: unload_specifications(file_paths)

            Unloads the given specifications sheets present in the previously loaded
            specifications files that you select.

            You must call :py:meth:`nidigital.Session.load_specifications_levels_and_timing` to reload the files with updated
            specifications values. You must then call :py:meth:`nidigital.Session.apply_levels_and_timing` in order to apply
            the levels and timing values that reference the updated specifications values.

            



            :param file_paths:


                Absolute file path of one or more loaded specifications files.

                


            :type file_paths: str or basic sequence of str

unlock
------

    .. py:currentmodule:: nidigital.Session

.. py:method:: unlock()

    Releases a lock that you acquired on an device session using
    :py:meth:`nidigital.Session.lock`. Refer to :py:meth:`nidigital.Session.unlock` for additional
    information on session locks.

wait_until_done
---------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: wait_until_done(timeout=hightime.timedelta(seconds=10.0))

            Waits until the pattern burst has completed or the timeout has expired.

            



            :param timeout:


                Maximum time (in seconds) allowed for this method to complete. If this method does not complete within this time interval, this method returns an error.

                


            :type timeout: hightime.timedelta, datetime.timedelta, or float in seconds

write_sequencer_flag
--------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: write_sequencer_flag(flag, value)

            Writes the state of a pattern sequencer flag. Use pattern sequencer flags to coordinate execution between the pattern sequencer and a runtime test program.

            



            :param flag:


                The pattern sequencer flag to write.

                -   :py:data:`~nidigital.SequencerFlag.FLAG0` ("seqflag0"): Writes pattern sequencer flag 0.
                -   :py:data:`~nidigital.SequencerFlag.FLAG1` ("seqflag1"): Writes pattern sequencer flag 1.
                -   :py:data:`~nidigital.SequencerFlag.FLAG2` ("seqflag2"): Writes pattern sequencer flag 2.
                -   :py:data:`~nidigital.SequencerFlag.FLAG3` ("seqflag3"): Writes pattern sequencer flag 3.

                


            :type flag: :py:data:`nidigital.SequencerFlag`
            :param value:


                A Boolean that assigns a state to the pattern sequencer flag you specify.

                


            :type value: bool

write_sequencer_register
------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: write_sequencer_register(reg, value)

            Writes a value to a pattern sequencer register. Use pattern sequencer registers to pass numeric values between the pattern sequencer and a runtime test program.

            



            :param reg:


                The sequencer register you want to write to.

                -   :py:data:`~nidigital.SequencerRegister.REGISTER0` ("reg0"): Writes sequencer register 0.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER1` ("reg1"): Writes sequencer register 1.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER2` ("reg2"): Writes sequencer register 2.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER3` ("reg3"): Writes sequencer register 3.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER4` ("reg4"): Writes sequencer register 4.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER5` ("reg5"): Writes sequencer register 5.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER6` ("reg6"): Writes sequencer register 6.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER7` ("reg7"): Writes sequencer register 7.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER8` ("reg8"): Writes sequencer register 8.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER9` ("reg9"): Writes sequencer register 9.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER10` ("reg10"): Writes sequencer register 10.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER11` ("reg11"): Writes sequencer register 11.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER12` ("reg12"): Writes sequencer register 12.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER13` ("reg13"): Writes sequencer register 13.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER14` ("reg14"): Writes sequencer register 14.
                -   :py:data:`~nidigital.SequencerRegister.REGISTER15` ("reg15"): Writes sequencer register 15.

                


            :type reg: :py:data:`nidigital.SequencerRegister`
            :param value:


                The value you want to write to the register.

                


            :type value: int

write_source_waveform_broadcast
-------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: write_source_waveform_broadcast(waveform_name, waveform_data)

            Writes the same waveform data to all sites. Use this write method if you set the data_mapping parameter of the create source waveform method to :py:data:`~nidigital.SourceDataMapping.BROADCAST`.

            



            :param waveform_name:


                The name to assign to the waveform. Use the waveform_name  with source_start opcode in your pattern.

                


            :type waveform_name: str
            :param waveform_data:


                1D array of samples to use as source data to apply to all sites.

                


            :type waveform_data: list of int

write_source_waveform_data_from_file_tdms
-----------------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: write_source_waveform_data_from_file_tdms(waveform_name, waveform_file_path)

            Writes a source waveform based on the waveform data and configuration information the file contains.

            



            :param waveform_name:


                The name to assign to the waveform. Use the waveform_name  with source_start opcode in your pattern.

                


            :type waveform_name: str
            :param waveform_file_path:


                Absolute file path to the load source waveform file (.tdms).

                


            :type waveform_file_path: str

write_source_waveform_site_unique
---------------------------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: write_source_waveform_site_unique(waveform_name, waveform_data)

            Writes one waveform per site. Use this write method if you set the parameter of the create source waveform method to Site Unique.

            



            :param waveform_name:


                The name to assign to the waveform. Use the waveform_name with source_start opcode in your pattern.

                


            :type waveform_name: str
            :param waveform_data:


                Dictionary where each key is a site number and value is a collection of samples to use as source data

                


            :type waveform_data: { int: basic sequence of unsigned int, int: basic sequence of unsigned int, ... }

write_static
------------

    .. py:currentmodule:: nidigital.Session

    .. py:method:: write_static(state)

            Writes a static state to the specified pins. The selected pins remain in the specified state until the next pattern burst or call to this method. If there are uncommitted changes to levels or the termination mode, this method commits the changes to the pins. This method does not change the selected pin method. If you write a static state to a pin that does not have the Digital method selected, the new static state is stored by the instrument, and affects the state of the pin the next time you change the selected method to Digital.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].write_static`

                To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

                Example: :py:meth:`my_session.write_static`


            :param state:


                Parameter that specifies one of the following digital states to assign to the pin.

                -   :py:data:`~nidigital.WriteStaticPinState.ZERO`: Specifies to drive low.
                -   :py:data:`~nidigital.WriteStaticPinState.ONE`: Specifies to drive high.
                -   :py:data:`~nidigital.WriteStaticPinState.X`: Specifies to not drive.

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type state: :py:data:`nidigital.WriteStaticPinState`


Properties
==========

active_load_ioh
---------------

    .. py:attribute:: active_load_ioh

        Specifies the current that the DUT sources to the active load while outputting a voltage above VCOM.




        .. tip:: This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].active_load_ioh`

            To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.active_load_ioh`

        The following table lists the characteristics of this property.

            +-----------------------+----------------+
            | Characteristic        | Value          |
            +=======================+================+
            | Datatype              | float          |
            +-----------------------+----------------+
            | Permissions           | read-write     |
            +-----------------------+----------------+
            | Repeated Capabilities | channels, pins |
            +-----------------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_ACTIVE_LOAD_IOH**

active_load_iol
---------------

    .. py:attribute:: active_load_iol

        Specifies the current that the DUT sinks from the active load while outputting a voltage below VCOM.




        .. tip:: This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].active_load_iol`

            To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.active_load_iol`

        The following table lists the characteristics of this property.

            +-----------------------+----------------+
            | Characteristic        | Value          |
            +=======================+================+
            | Datatype              | float          |
            +-----------------------+----------------+
            | Permissions           | read-write     |
            +-----------------------+----------------+
            | Repeated Capabilities | channels, pins |
            +-----------------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_ACTIVE_LOAD_IOL**

active_load_vcom
----------------

    .. py:attribute:: active_load_vcom

        Specifies the voltage level at which the active load circuit switches between sourcing current and sinking current.




        .. tip:: This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].active_load_vcom`

            To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.active_load_vcom`

        The following table lists the characteristics of this property.

            +-----------------------+----------------+
            | Characteristic        | Value          |
            +=======================+================+
            | Datatype              | float          |
            +-----------------------+----------------+
            | Permissions           | read-write     |
            +-----------------------+----------------+
            | Repeated Capabilities | channels, pins |
            +-----------------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_ACTIVE_LOAD_VCOM**

cache
-----

    .. py:attribute:: cache

        Specifies whether to cache the value of properties. When caching is enabled, the instrument driver keeps track of the current instrument settings and avoids sending redundant commands to the instrument. This significantly increases execution speed. Caching is always enabled in the driver, regardless of the value of this property.

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

                - C Attribute: **NIDIGITAL_ATTR_CACHE**

channel_count
-------------

    .. py:attribute:: channel_count

        Returns the number of channels that the specific digital pattern instrument driver supports.

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

                - C Attribute: **NIDIGITAL_ATTR_CHANNEL_COUNT**

clock_generator_frequency
-------------------------

    .. py:attribute:: clock_generator_frequency

        Specifies the frequency for the clock generator.




        .. tip:: This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].clock_generator_frequency`

            To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.clock_generator_frequency`

        The following table lists the characteristics of this property.

            +-----------------------+----------------+
            | Characteristic        | Value          |
            +=======================+================+
            | Datatype              | float          |
            +-----------------------+----------------+
            | Permissions           | read-write     |
            +-----------------------+----------------+
            | Repeated Capabilities | channels, pins |
            +-----------------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_CLOCK_GENERATOR_FREQUENCY**

clock_generator_is_running
--------------------------

    .. py:attribute:: clock_generator_is_running

        Indicates whether the clock generator is running.




        .. tip:: This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].clock_generator_is_running`

            To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.clock_generator_is_running`

        The following table lists the characteristics of this property.

            +-----------------------+----------------+
            | Characteristic        | Value          |
            +=======================+================+
            | Datatype              | bool           |
            +-----------------------+----------------+
            | Permissions           | read only      |
            +-----------------------+----------------+
            | Repeated Capabilities | channels, pins |
            +-----------------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_CLOCK_GENERATOR_IS_RUNNING**

conditional_jump_trigger_terminal_name
--------------------------------------

    .. py:attribute:: conditional_jump_trigger_terminal_name

        Specifies the terminal name from which the exported conditional jump trigger signal may be routed to other instruments through the PXI trigger bus. You can use this signal to trigger other instruments when the conditional jump trigger instance asserts on the digital pattern instrument.




        .. tip:: This property can be set/get on specific conditional_jump_triggers within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container conditional_jump_triggers to specify a subset.

            Example: :py:attr:`my_session.conditional_jump_triggers[ ... ].conditional_jump_trigger_terminal_name`

            To set/get on all conditional_jump_triggers, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.conditional_jump_trigger_terminal_name`

        The following table lists the characteristics of this property.

            +-----------------------+---------------------------+
            | Characteristic        | Value                     |
            +=======================+===========================+
            | Datatype              | str                       |
            +-----------------------+---------------------------+
            | Permissions           | read only                 |
            +-----------------------+---------------------------+
            | Repeated Capabilities | conditional_jump_triggers |
            +-----------------------+---------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_CONDITIONAL_JUMP_TRIGGER_TERMINAL_NAME**

conditional_jump_trigger_type
-----------------------------

    .. py:attribute:: conditional_jump_trigger_type

        Disables the conditional jump trigger or configures it for either hardware triggering or software triggering.  The default value is :py:data:`~nidigital.TriggerType.NONE`.

        +------------------------------------------------+------------------------------------------------------------------+
        | Valid Values:                                  |                                                                  |
        +================================================+==================================================================+
        | :py:data:`~nidigital.TriggerType.NONE`         | Disables the conditional jump trigger.                           |
        +------------------------------------------------+------------------------------------------------------------------+
        | :py:data:`~nidigital.TriggerType.DIGITAL_EDGE` | Configures the conditional jump trigger for hardware triggering. |
        +------------------------------------------------+------------------------------------------------------------------+
        | :py:data:`~nidigital.TriggerType.SOFTWARE`     | Configures the conditional jump trigger for software triggering. |
        +------------------------------------------------+------------------------------------------------------------------+


        .. tip:: This property can be set/get on specific conditional_jump_triggers within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container conditional_jump_triggers to specify a subset.

            Example: :py:attr:`my_session.conditional_jump_triggers[ ... ].conditional_jump_trigger_type`

            To set/get on all conditional_jump_triggers, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.conditional_jump_trigger_type`

        The following table lists the characteristics of this property.

            +-----------------------+---------------------------+
            | Characteristic        | Value                     |
            +=======================+===========================+
            | Datatype              | enums.TriggerType         |
            +-----------------------+---------------------------+
            | Permissions           | read-write                |
            +-----------------------+---------------------------+
            | Repeated Capabilities | conditional_jump_triggers |
            +-----------------------+---------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_CONDITIONAL_JUMP_TRIGGER_TYPE**

cycle_number_history_ram_trigger_cycle_number
---------------------------------------------

    .. py:attribute:: cycle_number_history_ram_trigger_cycle_number

        Specifies the cycle number on which History RAM starts acquiring pattern information when configured for a cycle number trigger.

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

                - C Attribute: **NIDIGITAL_ATTR_CYCLE_NUMBER_HISTORY_RAM_TRIGGER_CYCLE_NUMBER**

digital_edge_conditional_jump_trigger_edge
------------------------------------------

    .. py:attribute:: digital_edge_conditional_jump_trigger_edge

        Configures the active edge of the incoming trigger signal for the conditional jump trigger instance. The default value is :py:data:`~nidigital.DigitalEdge.RISING`.

        +-------------------------------------------+---------------------------------------------------------------+
        | Valid Values:                             |                                                               |
        +===========================================+===============================================================+
        | :py:data:`~nidigital.DigitalEdge.RISING`  | Specifies the signal transition from low level to high level. |
        +-------------------------------------------+---------------------------------------------------------------+
        | :py:data:`~nidigital.DigitalEdge.FALLING` | Specifies the signal transition from high level to low level. |
        +-------------------------------------------+---------------------------------------------------------------+


        .. tip:: This property can be set/get on specific conditional_jump_triggers within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container conditional_jump_triggers to specify a subset.

            Example: :py:attr:`my_session.conditional_jump_triggers[ ... ].digital_edge_conditional_jump_trigger_edge`

            To set/get on all conditional_jump_triggers, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.digital_edge_conditional_jump_trigger_edge`

        The following table lists the characteristics of this property.

            +-----------------------+---------------------------+
            | Characteristic        | Value                     |
            +=======================+===========================+
            | Datatype              | enums.DigitalEdge         |
            +-----------------------+---------------------------+
            | Permissions           | read-write                |
            +-----------------------+---------------------------+
            | Repeated Capabilities | conditional_jump_triggers |
            +-----------------------+---------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_DIGITAL_EDGE_CONDITIONAL_JUMP_TRIGGER_EDGE**

digital_edge_conditional_jump_trigger_source
--------------------------------------------

    .. py:attribute:: digital_edge_conditional_jump_trigger_source

        Configures the digital trigger source terminal for a conditional jump trigger instance. The PXIe-6570/6571 supports triggering through the PXI trigger bus. You can specify source terminals in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The source terminal can also be a terminal from another device, in which case the NI-Digital Pattern Driver automatically finds a route (if one is available) from that terminal to the input terminal (going through a physical PXI backplane trigger line). For example, you can set the source terminal on Dev1 to be /Dev2/ConditionalJumpTrigger0. The default value is VI_NULL.

        +----------------------------------------------+
        | Valid Values:                                |
        +==============================================+
        | String identifier to any valid terminal name |
        +----------------------------------------------+


        .. tip:: This property can be set/get on specific conditional_jump_triggers within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container conditional_jump_triggers to specify a subset.

            Example: :py:attr:`my_session.conditional_jump_triggers[ ... ].digital_edge_conditional_jump_trigger_source`

            To set/get on all conditional_jump_triggers, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.digital_edge_conditional_jump_trigger_source`

        The following table lists the characteristics of this property.

            +-----------------------+---------------------------+
            | Characteristic        | Value                     |
            +=======================+===========================+
            | Datatype              | str                       |
            +-----------------------+---------------------------+
            | Permissions           | read-write                |
            +-----------------------+---------------------------+
            | Repeated Capabilities | conditional_jump_triggers |
            +-----------------------+---------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_DIGITAL_EDGE_CONDITIONAL_JUMP_TRIGGER_SOURCE**

digital_edge_rio_trigger_edge
-----------------------------

    .. py:attribute:: digital_edge_rio_trigger_edge

        Configures the active edge of the incoming trigger signal for the RIO trigger instance. The default value is :py:data:`~nidigital.DigitalEdge.RISING`.

        +-------------------------------------------+---------------------------------------------------------------+
        | Valid Values:                             |                                                               |
        +===========================================+===============================================================+
        | :py:data:`~nidigital.DigitalEdge.RISING`  | Specifies the signal transition from low level to high level. |
        +-------------------------------------------+---------------------------------------------------------------+
        | :py:data:`~nidigital.DigitalEdge.FALLING` | Specifies the signal transition from high level to low level. |
        +-------------------------------------------+---------------------------------------------------------------+


        .. tip:: This property can be set/get on specific rio_triggers within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container rio_triggers to specify a subset.

            Example: :py:attr:`my_session.rio_triggers[ ... ].digital_edge_rio_trigger_edge`

            To set/get on all rio_triggers, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.digital_edge_rio_trigger_edge`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------+
            | Characteristic        | Value             |
            +=======================+===================+
            | Datatype              | enums.DigitalEdge |
            +-----------------------+-------------------+
            | Permissions           | read-write        |
            +-----------------------+-------------------+
            | Repeated Capabilities | rio_triggers      |
            +-----------------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_DIGITAL_EDGE_RIO_TRIGGER_EDGE**

digital_edge_rio_trigger_source
-------------------------------

    .. py:attribute:: digital_edge_rio_trigger_source

        Configures the digital trigger source terminal for a RIO trigger instance. The PXIe-6570/6571 supports triggering through the PXI trigger bus. You can specify source terminals in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The source terminal can also be a terminal from another device, in which case the NI-Digital Pattern Driver automatically finds a route (if one is available) from that terminal to the input terminal (going through a physical PXI backplane trigger line). For example, you can set the source terminal on Dev1 to be /Dev2/RIOTrigger0. The default value is VI_NULL.

        +----------------------------------------------+
        | Valid Values:                                |
        +==============================================+
        | String identifier to any valid terminal name |
        +----------------------------------------------+


        .. tip:: This property can be set/get on specific rio_triggers within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container rio_triggers to specify a subset.

            Example: :py:attr:`my_session.rio_triggers[ ... ].digital_edge_rio_trigger_source`

            To set/get on all rio_triggers, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.digital_edge_rio_trigger_source`

        The following table lists the characteristics of this property.

            +-----------------------+--------------+
            | Characteristic        | Value        |
            +=======================+==============+
            | Datatype              | str          |
            +-----------------------+--------------+
            | Permissions           | read-write   |
            +-----------------------+--------------+
            | Repeated Capabilities | rio_triggers |
            +-----------------------+--------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_DIGITAL_EDGE_RIO_TRIGGER_SOURCE**

digital_edge_start_trigger_edge
-------------------------------

    .. py:attribute:: digital_edge_start_trigger_edge

        Specifies the active edge for the Start trigger. This property is used when the :py:attr:`nidigital.Session.start_trigger_type` property is set to Digital Edge.

        +-------------------------------------------+-------------------------------------------------------------------------------+
        | Defined Values:                           |                                                                               |
        +===========================================+===============================================================================+
        | :py:data:`~nidigital.DigitalEdge.RISING`  | Asserts the trigger when the signal transitions from low level to high level. |
        +-------------------------------------------+-------------------------------------------------------------------------------+
        | :py:data:`~nidigital.DigitalEdge.FALLING` | Asserts the trigger when the signal transitions from high level to low level. |
        +-------------------------------------------+-------------------------------------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+-------------------+
            | Characteristic        | Value             |
            +=======================+===================+
            | Datatype              | enums.DigitalEdge |
            +-----------------------+-------------------+
            | Permissions           | read-write        |
            +-----------------------+-------------------+
            | Repeated Capabilities | None              |
            +-----------------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE**

digital_edge_start_trigger_source
---------------------------------

    .. py:attribute:: digital_edge_start_trigger_source

        Specifies the source terminal for the Start trigger. This property is used when the :py:attr:`nidigital.Session.start_trigger_type` property is set to Digital Edge. You can specify source terminals in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The source terminal can also be a terminal from another device, in which case the NI-Digital Pattern Driver automatically finds a route (if one is available) from that terminal to the input terminal (going through a physical PXI backplane trigger line). For example, you can set the source terminal on Dev1 to be /Dev2/StartTrigger.

        +-----------------+--------------------+
        | Defined Values: |                    |
        +=================+====================+
        | PXI_Trig0       | PXI trigger line 0 |
        +-----------------+--------------------+
        | PXI_Trig1       | PXI trigger line 1 |
        +-----------------+--------------------+
        | PXI_Trig2       | PXI trigger line 2 |
        +-----------------+--------------------+
        | PXI_Trig3       | PXI trigger line 3 |
        +-----------------+--------------------+
        | PXI_Trig4       | PXI trigger line 4 |
        +-----------------+--------------------+
        | PXI_Trig5       | PXI trigger line 5 |
        +-----------------+--------------------+
        | PXI_Trig6       | PXI trigger line 6 |
        +-----------------+--------------------+
        | PXI_Trig7       | PXI trigger line 7 |
        +-----------------+--------------------+

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

                - C Attribute: **NIDIGITAL_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE**

driver_setup
------------

    .. py:attribute:: driver_setup

        This property returns initial values for NI-Digital Pattern Driver properties as a string.

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

                - C Attribute: **NIDIGITAL_ATTR_DRIVER_SETUP**

exported_conditional_jump_trigger_output_terminal
-------------------------------------------------

    .. py:attribute:: exported_conditional_jump_trigger_output_terminal

        Specifies the terminal to output the exported signal of the specified instance of the conditional jump trigger. The default value is VI_NULL.

        +---------------+-------------------------+
        | Valid Values: |                         |
        +===============+=========================+
        | VI_NULL ("")  | Returns an empty string |
        +---------------+-------------------------+
        | PXI_Trig0     | PXI trigger line 0      |
        +---------------+-------------------------+
        | PXI_Trig1     | PXI trigger line 1      |
        +---------------+-------------------------+
        | PXI_Trig2     | PXI trigger line 2      |
        +---------------+-------------------------+
        | PXI_Trig3     | PXI trigger line 3      |
        +---------------+-------------------------+
        | PXI_Trig4     | PXI trigger line 4      |
        +---------------+-------------------------+
        | PXI_Trig5     | PXI trigger line 5      |
        +---------------+-------------------------+
        | PXI_Trig6     | PXI trigger line 6      |
        +---------------+-------------------------+
        | PXI_Trig7     | PXI trigger line 7      |
        +---------------+-------------------------+


        .. tip:: This property can be set/get on specific conditional_jump_triggers within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container conditional_jump_triggers to specify a subset.

            Example: :py:attr:`my_session.conditional_jump_triggers[ ... ].exported_conditional_jump_trigger_output_terminal`

            To set/get on all conditional_jump_triggers, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.exported_conditional_jump_trigger_output_terminal`

        The following table lists the characteristics of this property.

            +-----------------------+---------------------------+
            | Characteristic        | Value                     |
            +=======================+===========================+
            | Datatype              | str                       |
            +-----------------------+---------------------------+
            | Permissions           | read-write                |
            +-----------------------+---------------------------+
            | Repeated Capabilities | conditional_jump_triggers |
            +-----------------------+---------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_EXPORTED_CONDITIONAL_JUMP_TRIGGER_OUTPUT_TERMINAL**

exported_pattern_opcode_event_output_terminal
---------------------------------------------

    .. py:attribute:: exported_pattern_opcode_event_output_terminal

        Specifies the destination terminal for exporting the Pattern Opcode Event. Terminals can be specified in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.

        +-----------------+--------------------+
        | Defined Values: |                    |
        +=================+====================+
        | PXI_Trig0       | PXI trigger line 0 |
        +-----------------+--------------------+
        | PXI_Trig1       | PXI trigger line 1 |
        +-----------------+--------------------+
        | PXI_Trig2       | PXI trigger line 2 |
        +-----------------+--------------------+
        | PXI_Trig3       | PXI trigger line 3 |
        +-----------------+--------------------+
        | PXI_Trig4       | PXI trigger line 4 |
        +-----------------+--------------------+
        | PXI_Trig5       | PXI trigger line 5 |
        +-----------------+--------------------+
        | PXI_Trig6       | PXI trigger line 6 |
        +-----------------+--------------------+
        | PXI_Trig7       | PXI trigger line 7 |
        +-----------------+--------------------+


        .. tip:: This property can be set/get on specific pattern_opcode_events within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container pattern_opcode_events to specify a subset.

            Example: :py:attr:`my_session.pattern_opcode_events[ ... ].exported_pattern_opcode_event_output_terminal`

            To set/get on all pattern_opcode_events, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.exported_pattern_opcode_event_output_terminal`

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------+
            | Characteristic        | Value                 |
            +=======================+=======================+
            | Datatype              | str                   |
            +-----------------------+-----------------------+
            | Permissions           | read-write            |
            +-----------------------+-----------------------+
            | Repeated Capabilities | pattern_opcode_events |
            +-----------------------+-----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_EXPORTED_PATTERN_OPCODE_EVENT_OUTPUT_TERMINAL**

exported_rio_event_output_terminal
----------------------------------

    .. py:attribute:: exported_rio_event_output_terminal

        Specifies the destination terminal for exporting the RIO Event. Terminals can be specified in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.

        +-----------------+--------------------+
        | Defined Values: |                    |
        +=================+====================+
        | PXI_Trig0       | PXI trigger line 0 |
        +-----------------+--------------------+
        | PXI_Trig1       | PXI trigger line 1 |
        +-----------------+--------------------+
        | PXI_Trig2       | PXI trigger line 2 |
        +-----------------+--------------------+
        | PXI_Trig3       | PXI trigger line 3 |
        +-----------------+--------------------+
        | PXI_Trig4       | PXI trigger line 4 |
        +-----------------+--------------------+
        | PXI_Trig5       | PXI trigger line 5 |
        +-----------------+--------------------+
        | PXI_Trig6       | PXI trigger line 6 |
        +-----------------+--------------------+
        | PXI_Trig7       | PXI trigger line 7 |
        +-----------------+--------------------+


        .. tip:: This property can be set/get on specific rio_events within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container rio_events to specify a subset.

            Example: :py:attr:`my_session.rio_events[ ... ].exported_rio_event_output_terminal`

            To set/get on all rio_events, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.exported_rio_event_output_terminal`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | rio_events |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_EXPORTED_RIO_EVENT_OUTPUT_TERMINAL**

exported_start_trigger_output_terminal
--------------------------------------

    .. py:attribute:: exported_start_trigger_output_terminal

        Specifies the destination terminal for exporting the Start trigger. Terminals can be specified in one of two ways. If the digital pattern instrument is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.

        +----------------------+-----------------------------+
        | Defined Values:      |                             |
        +======================+=============================+
        | Do not export signal | The signal is not exported. |
        +----------------------+-----------------------------+
        | PXI_Trig0            | PXI trigger line 0          |
        +----------------------+-----------------------------+
        | PXI_Trig1            | PXI trigger line 1          |
        +----------------------+-----------------------------+
        | PXI_Trig2            | PXI trigger line 2          |
        +----------------------+-----------------------------+
        | PXI_Trig3            | PXI trigger line 3          |
        +----------------------+-----------------------------+
        | PXI_Trig4            | PXI trigger line 4          |
        +----------------------+-----------------------------+
        | PXI_Trig5            | PXI trigger line 5          |
        +----------------------+-----------------------------+
        | PXI_Trig6            | PXI trigger line 6          |
        +----------------------+-----------------------------+
        | PXI_Trig7            | PXI trigger line 7          |
        +----------------------+-----------------------------+

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

                - C Attribute: **NIDIGITAL_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL**

frequency_counter_hysteresis_enabled
------------------------------------

    .. py:attribute:: frequency_counter_hysteresis_enabled

        Specifies whether hysteresis is enabled for the frequency counters of the digital pattern instrument.

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

                - C Attribute: **NIDIGITAL_ATTR_FREQUENCY_COUNTER_HYSTERESIS_ENABLED**

frequency_counter_measurement_mode
----------------------------------

    .. py:attribute:: frequency_counter_measurement_mode

        Determines how the frequency counters of the digital pattern instrument make measurements.

        +---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Valid Values:                                           |                                                                                                                                                                                                                                                                                                                                                                                                  |
        +=========================================================+==================================================================================================================================================================================================================================================================================================================================================================================================+
        | :py:data:`~nidigital.FrequencyMeasurementMode.BANKED`   | Each discrete frequency counter is mapped to specific channels and makes frequency measurements from only those channels. Use banked mode when you need access to the full measure frequency range of the instrument. **Note:** If you request frequency measurements from multiple channels within the same bank, the measurements are made in series for the channels in that bank.            |
        +---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nidigital.FrequencyMeasurementMode.PARALLEL` | All discrete frequency counters make frequency measurements from all channels in parallel with one another. Use parallel mode to increase the speed of frequency measurements if you do not need access to the full measure frequency range of the instrument; in parallel mode, you can also add :py:attr:`nidigital.Session.frequency_counter_hysteresis_enabled` to reduce measurement noise. |
        +---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+--------------------------------+
            | Characteristic        | Value                          |
            +=======================+================================+
            | Datatype              | enums.FrequencyMeasurementMode |
            +-----------------------+--------------------------------+
            | Permissions           | read-write                     |
            +-----------------------+--------------------------------+
            | Repeated Capabilities | None                           |
            +-----------------------+--------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_FREQUENCY_COUNTER_MEASUREMENT_MODE**

frequency_counter_measurement_time
----------------------------------

    .. py:attribute:: frequency_counter_measurement_time

        Specifies the measurement time for the frequency counter.




        .. tip:: This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].frequency_counter_measurement_time`

            To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.frequency_counter_measurement_time`

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------------------+
            | Characteristic        | Value                                  |
            +=======================+========================================+
            | Datatype              | float in seconds or datetime.timedelta |
            +-----------------------+----------------------------------------+
            | Permissions           | read-write                             |
            +-----------------------+----------------------------------------+
            | Repeated Capabilities | channels, pins                         |
            +-----------------------+----------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_FREQUENCY_COUNTER_MEASUREMENT_TIME**

group_capabilities
------------------

    .. py:attribute:: group_capabilities

        Returns a string that contains a comma-separated list of class-extension groups that the driver implements.

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

                - C Attribute: **NIDIGITAL_ATTR_GROUP_CAPABILITIES**

halt_on_keep_alive_opcode
-------------------------

    .. py:attribute:: halt_on_keep_alive_opcode

        Specifies whether keep_alive opcodes should behave like halt opcodes.

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

                - C Attribute: **NIDIGITAL_ATTR_HALT_ON_KEEP_ALIVE_OPCODE**

history_ram_buffer_size_per_site
--------------------------------

    .. py:attribute:: history_ram_buffer_size_per_site

        Specifies the size, in samples, of the host memory buffer. The default value is 32000.

        +---------------+
        | Valid Values: |
        +===============+
        | 0-INT64_MAX   |
        +---------------+

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

                - C Attribute: **NIDIGITAL_ATTR_HISTORY_RAM_BUFFER_SIZE_PER_SITE**

history_ram_cycles_to_acquire
-----------------------------

    .. py:attribute:: history_ram_cycles_to_acquire

        Configures which cycles History RAM acquires after the trigger conditions are met. If you configure History RAM to only acquire failed cycles, you must set the pretrigger samples for History RAM to 0.

        +--------------------------------------------------------+-----------------------------------------------------------------------------------+
        | Defined Values:                                        |                                                                                   |
        +========================================================+===================================================================================+
        | :py:data:`~nidigital.HistoryRAMCyclesToAcquire.FAILED` | Only acquires cycles that fail a compare after the triggering conditions are met. |
        +--------------------------------------------------------+-----------------------------------------------------------------------------------+
        | :py:data:`~nidigital.HistoryRAMCyclesToAcquire.ALL`    | Acquires all cycles after the triggering conditions are met.                      |
        +--------------------------------------------------------+-----------------------------------------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+---------------------------------+
            | Characteristic        | Value                           |
            +=======================+=================================+
            | Datatype              | enums.HistoryRAMCyclesToAcquire |
            +-----------------------+---------------------------------+
            | Permissions           | read-write                      |
            +-----------------------+---------------------------------+
            | Repeated Capabilities | None                            |
            +-----------------------+---------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_HISTORY_RAM_CYCLES_TO_ACQUIRE**

history_ram_max_samples_to_acquire_per_site
-------------------------------------------

    .. py:attribute:: history_ram_max_samples_to_acquire_per_site

        Specifies the maximum number of History RAM samples to acquire per site. If the property is set to -1, it will acquire until the History RAM buffer is full.

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

                - C Attribute: **NIDIGITAL_ATTR_HISTORY_RAM_MAX_SAMPLES_TO_ACQUIRE_PER_SITE**

history_ram_number_of_samples_is_finite
---------------------------------------

    .. py:attribute:: history_ram_number_of_samples_is_finite

        Specifies whether the instrument acquires a finite number of History Ram samples or acquires continuously. The maximum number of samples that will be acquired when this property is set to True is determined by the instrument History RAM depth specification and the History RAM Max Samples to Acquire Per Site property. The default value is True.

        +---------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Valid Values: |                                                                                                                                                      |
        +===============+======================================================================================================================================================+
        | True          | Specifies that History RAM results will not stream into the host buffer until a History RAM fetch API is called.                                     |
        +---------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
        | False         | Specifies that History RAM results will automatically start streaming into a host buffer after a pattern is burst and the History RAM has triggered. |
        +---------------+------------------------------------------------------------------------------------------------------------------------------------------------------+

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

                - C Attribute: **NIDIGITAL_ATTR_HISTORY_RAM_NUMBER_OF_SAMPLES_IS_FINITE**

history_ram_pretrigger_samples
------------------------------

    .. py:attribute:: history_ram_pretrigger_samples

        Specifies the number of samples to acquire before the trigger conditions are met. If you configure History RAM to only acquire failed cycles, you must set the pretrigger samples for History RAM to 0.

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

                - C Attribute: **NIDIGITAL_ATTR_HISTORY_RAM_PRETRIGGER_SAMPLES**

history_ram_trigger_type
------------------------

    .. py:attribute:: history_ram_trigger_type

        Specifies the type of trigger condition on which History RAM starts acquiring pattern information.

        +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
        | Defined Values:                                           |                                                                                                                                     |
        +===========================================================+=====================================================================================================================================+
        | :py:data:`~nidigital.HistoryRAMTriggerType.FIRST_FAILURE` | Starts acquiring pattern information in History RAM on the first failed cycle in a pattern burst.                                   |
        +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nidigital.HistoryRAMTriggerType.CYCLE_NUMBER`  | Starts acquiring pattern information in History RAM starting from a specified cycle number.                                         |
        +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nidigital.HistoryRAMTriggerType.PATTERN_LABEL` | Starts acquiring pattern information in History RAM starting from a specified pattern label, augmented by vector and cycle offsets. |
        +-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------------+
            | Characteristic        | Value                       |
            +=======================+=============================+
            | Datatype              | enums.HistoryRAMTriggerType |
            +-----------------------+-----------------------------+
            | Permissions           | read-write                  |
            +-----------------------+-----------------------------+
            | Repeated Capabilities | None                        |
            +-----------------------+-----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_HISTORY_RAM_TRIGGER_TYPE**

instrument_firmware_revision
----------------------------

    .. py:attribute:: instrument_firmware_revision

        Returns a string that contains the firmware revision information for the digital pattern instrument.




        .. tip:: This property can be set/get on specific instruments within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container instruments to specify a subset.

            Example: :py:attr:`my_session.instruments[ ... ].instrument_firmware_revision`

            To set/get on all instruments, you can call the property directly on the :py:class:`nidigital.Session`.

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

                - C Attribute: **NIDIGITAL_ATTR_INSTRUMENT_FIRMWARE_REVISION**

instrument_manufacturer
-----------------------

    .. py:attribute:: instrument_manufacturer

        Returns a string ("National Instruments") that contains the name of the manufacturer of the digital pattern instrument.

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

                - C Attribute: **NIDIGITAL_ATTR_INSTRUMENT_MANUFACTURER**

instrument_model
----------------

    .. py:attribute:: instrument_model

        Returns a string that contains the model number or name of the digital pattern instrument.

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

                - C Attribute: **NIDIGITAL_ATTR_INSTRUMENT_MODEL**

interchange_check
-----------------

    .. py:attribute:: interchange_check

        This property is not supported.

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

                - C Attribute: **NIDIGITAL_ATTR_INTERCHANGE_CHECK**

io_resource_descriptor
----------------------

    .. py:attribute:: io_resource_descriptor

        Returns a string that contains the resource descriptor that the NI-Digital Pattern Driver uses to identify the digital pattern instrument.

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

                - C Attribute: **NIDIGITAL_ATTR_IO_RESOURCE_DESCRIPTOR**

is_keep_alive_active
--------------------

    .. py:attribute:: is_keep_alive_active

        Returns True if the digital pattern instrument is driving the keep alive pattern.

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

                - C Attribute: **NIDIGITAL_ATTR_IS_KEEP_ALIVE_ACTIVE**

logical_name
------------

    .. py:attribute:: logical_name

        Returns a string containing the logical name that you specified when opening the current IVI session. This property is not supported.

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

                - C Attribute: **NIDIGITAL_ATTR_LOGICAL_NAME**

mask_compare
------------

    .. py:attribute:: mask_compare

        Specifies whether the pattern comparisons are masked or not. When set to True for a specified pin, failures on that pin will be masked.




        .. tip:: This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].mask_compare`

            To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.mask_compare`

        The following table lists the characteristics of this property.

            +-----------------------+----------------+
            | Characteristic        | Value          |
            +=======================+================+
            | Datatype              | bool           |
            +-----------------------+----------------+
            | Permissions           | read-write     |
            +-----------------------+----------------+
            | Repeated Capabilities | channels, pins |
            +-----------------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_MASK_COMPARE**

pattern_label_history_ram_trigger_cycle_offset
----------------------------------------------

    .. py:attribute:: pattern_label_history_ram_trigger_cycle_offset

        Specifies the number of cycles that follow the specified pattern label and vector offset, after which History RAM will start acquiring pattern information when configured for a pattern label trigger.

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

                - C Attribute: **NIDIGITAL_ATTR_PATTERN_LABEL_HISTORY_RAM_TRIGGER_CYCLE_OFFSET**

pattern_label_history_ram_trigger_label
---------------------------------------

    .. py:attribute:: pattern_label_history_ram_trigger_label

        Specifies the pattern label, augmented by the vector and cycle offset, to determine the point where History RAM will start acquiring pattern information when configured for a pattern label trigger.

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

                - C Attribute: **NIDIGITAL_ATTR_PATTERN_LABEL_HISTORY_RAM_TRIGGER_LABEL**

pattern_label_history_ram_trigger_vector_offset
-----------------------------------------------

    .. py:attribute:: pattern_label_history_ram_trigger_vector_offset

        Specifies the number of vectors that follow the specified pattern label, after which History RAM will start acquiring pattern information when configured for a pattern label trigger.

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

                - C Attribute: **NIDIGITAL_ATTR_PATTERN_LABEL_HISTORY_RAM_TRIGGER_VECTOR_OFFSET**

pattern_opcode_event_terminal_name
----------------------------------

    .. py:attribute:: pattern_opcode_event_terminal_name

        Specifies the terminal name for the output trigger signal of the specified instance of a Pattern Opcode Event. You can use this terminal name as an input signal source for another trigger.




        .. tip:: This property can be set/get on specific pattern_opcode_events within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container pattern_opcode_events to specify a subset.

            Example: :py:attr:`my_session.pattern_opcode_events[ ... ].pattern_opcode_event_terminal_name`

            To set/get on all pattern_opcode_events, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.pattern_opcode_event_terminal_name`

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------+
            | Characteristic        | Value                 |
            +=======================+=======================+
            | Datatype              | str                   |
            +-----------------------+-----------------------+
            | Permissions           | read only             |
            +-----------------------+-----------------------+
            | Repeated Capabilities | pattern_opcode_events |
            +-----------------------+-----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PATTERN_OPCODE_EVENT_TERMINAL_NAME**

ppmu_allow_extended_voltage_range
---------------------------------

    .. py:attribute:: ppmu_allow_extended_voltage_range

        Enables the instrument to operate in additional voltage ranges where instrument specifications may differ from standard ranges. When set to True, this property enables extended voltage range operation. Review specification deviations for application suitability before using this property. NI recommends setting this property to False when not using the extended voltage range to avoid unintentional use of this range. The extended voltage range is supported only for PPMU, with the output method set to DC Voltage. A voltage glitch may occur when you change the PPMU output voltage from a standard range to the extended voltage range, or vice-versa, while the PPMU is sourcing. NI recommends temporarily changing the :py:attr:`nidigital.Session.selected_function` property to Off before sourcing a voltage level that requires a range change.




        .. tip:: This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].ppmu_allow_extended_voltage_range`

            To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.ppmu_allow_extended_voltage_range`

        The following table lists the characteristics of this property.

            +-----------------------+----------------+
            | Characteristic        | Value          |
            +=======================+================+
            | Datatype              | bool           |
            +-----------------------+----------------+
            | Permissions           | read-write     |
            +-----------------------+----------------+
            | Repeated Capabilities | channels, pins |
            +-----------------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PPMU_ALLOW_EXTENDED_VOLTAGE_RANGE**

ppmu_aperture_time
------------------

    .. py:attribute:: ppmu_aperture_time

        Specifies the measurement aperture time for the PPMU. The :py:attr:`nidigital.Session.ppmu_aperture_time_units` property sets the units of the PPMU aperture time.




        .. tip:: This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].ppmu_aperture_time`

            To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.ppmu_aperture_time`

        The following table lists the characteristics of this property.

            +-----------------------+----------------+
            | Characteristic        | Value          |
            +=======================+================+
            | Datatype              | float          |
            +-----------------------+----------------+
            | Permissions           | read-write     |
            +-----------------------+----------------+
            | Repeated Capabilities | channels, pins |
            +-----------------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PPMU_APERTURE_TIME**

ppmu_aperture_time_units
------------------------

    .. py:attribute:: ppmu_aperture_time_units

        Specifies the units of the measurement aperture time for the PPMU.

        +-----------------------------------------------------+-----------------------------------------+
        | Defined Values:                                     |                                         |
        +=====================================================+=========================================+
        | :py:data:`~nidigital.PPMUApertureTimeUnits.SECONDS` | Specifies the aperture time in seconds. |
        +-----------------------------------------------------+-----------------------------------------+


        .. tip:: This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].ppmu_aperture_time_units`

            To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.ppmu_aperture_time_units`

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------------+
            | Characteristic        | Value                       |
            +=======================+=============================+
            | Datatype              | enums.PPMUApertureTimeUnits |
            +-----------------------+-----------------------------+
            | Permissions           | read-write                  |
            +-----------------------+-----------------------------+
            | Repeated Capabilities | channels, pins              |
            +-----------------------+-----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PPMU_APERTURE_TIME_UNITS**

ppmu_current_level
------------------

    .. py:attribute:: ppmu_current_level

        Specifies the current level, in amps, that the PPMU forces to the DUT. This property is applicable only when you set the :py:attr:`nidigital.Session.ppmu_output_function` property to DC Current. Specify valid values for the current level using the :py:meth:`nidigital.Session.PPMU_ConfigureCurrentLevelRange` method.



        .. note:: One or more of the referenced methods are not in the Python API for this driver.


        .. tip:: This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].ppmu_current_level`

            To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.ppmu_current_level`

        The following table lists the characteristics of this property.

            +-----------------------+----------------+
            | Characteristic        | Value          |
            +=======================+================+
            | Datatype              | float          |
            +-----------------------+----------------+
            | Permissions           | read-write     |
            +-----------------------+----------------+
            | Repeated Capabilities | channels, pins |
            +-----------------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PPMU_CURRENT_LEVEL**

ppmu_current_level_range
------------------------

    .. py:attribute:: ppmu_current_level_range

        Specifies the range of valid values for the current level, in amps, that the PPMU forces to the DUT. This property is applicable only when you set the :py:attr:`nidigital.Session.ppmu_output_function` property to DC Current.




        .. tip:: This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].ppmu_current_level_range`

            To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.ppmu_current_level_range`

        The following table lists the characteristics of this property.

            +-----------------------+----------------+
            | Characteristic        | Value          |
            +=======================+================+
            | Datatype              | float          |
            +-----------------------+----------------+
            | Permissions           | read-write     |
            +-----------------------+----------------+
            | Repeated Capabilities | channels, pins |
            +-----------------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PPMU_CURRENT_LEVEL_RANGE**

ppmu_current_limit
------------------

    .. py:attribute:: ppmu_current_limit

        Specifies the current limit, in amps, that the output cannot exceed while the PPMU forces voltage to the DUT. This property is applicable only when you set the :py:attr:`nidigital.Session.ppmu_output_function` property to DC Voltage. The PXIe-6570/6571 does not support the :py:attr:`nidigital.Session.ppmu_current_limit` property and only allows configuration of the :py:attr:`nidigital.Session.ppmu_current_limit_range` property.




        .. tip:: This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].ppmu_current_limit`

            To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.ppmu_current_limit`

        The following table lists the characteristics of this property.

            +-----------------------+----------------+
            | Characteristic        | Value          |
            +=======================+================+
            | Datatype              | float          |
            +-----------------------+----------------+
            | Permissions           | read-write     |
            +-----------------------+----------------+
            | Repeated Capabilities | channels, pins |
            +-----------------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT**

ppmu_current_limit_behavior
---------------------------

    .. py:attribute:: ppmu_current_limit_behavior

        Specifies how the output should behave when the current limit is reached.

        +---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
        | Defined Values:                                         |                                                                                                                                         |
        +=========================================================+=========================================================================================================================================+
        | :py:data:`~nidigital.PPMUCurrentLimitBehavior.REGULATE` | Controls output current so that it does not exceed the current limit. Power continues to generate even if the current limit is reached. |
        +---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+


        .. tip:: This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].ppmu_current_limit_behavior`

            To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.ppmu_current_limit_behavior`

        The following table lists the characteristics of this property.

            +-----------------------+--------------------------------+
            | Characteristic        | Value                          |
            +=======================+================================+
            | Datatype              | enums.PPMUCurrentLimitBehavior |
            +-----------------------+--------------------------------+
            | Permissions           | read-write                     |
            +-----------------------+--------------------------------+
            | Repeated Capabilities | channels, pins                 |
            +-----------------------+--------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT_BEHAVIOR**

ppmu_current_limit_range
------------------------

    .. py:attribute:: ppmu_current_limit_range

        Specifies the valid range, in amps, to which the current limit can be set while the PPMU forces voltage to the DUT. This property is applicable only when you set the :py:attr:`nidigital.Session.ppmu_output_function` property to DC Voltage.




        .. tip:: This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].ppmu_current_limit_range`

            To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.ppmu_current_limit_range`

        The following table lists the characteristics of this property.

            +-----------------------+----------------+
            | Characteristic        | Value          |
            +=======================+================+
            | Datatype              | float          |
            +-----------------------+----------------+
            | Permissions           | read-write     |
            +-----------------------+----------------+
            | Repeated Capabilities | channels, pins |
            +-----------------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT_RANGE**

ppmu_current_limit_supported
----------------------------

    .. py:attribute:: ppmu_current_limit_supported

        Returns whether the device supports configuration of a current limit when you set the :py:attr:`nidigital.Session.ppmu_output_function` property to DC Voltage.




        .. tip:: This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].ppmu_current_limit_supported`

            To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.ppmu_current_limit_supported`

        The following table lists the characteristics of this property.

            +-----------------------+----------------+
            | Characteristic        | Value          |
            +=======================+================+
            | Datatype              | bool           |
            +-----------------------+----------------+
            | Permissions           | read only      |
            +-----------------------+----------------+
            | Repeated Capabilities | channels, pins |
            +-----------------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PPMU_CURRENT_LIMIT_SUPPORTED**

ppmu_output_function
--------------------

    .. py:attribute:: ppmu_output_function

        Specifies whether the PPMU forces voltage or current to the DUT.

        +--------------------------------------------------+--------------------------------------------+
        | Defined Values:                                  |                                            |
        +==================================================+============================================+
        | :py:data:`~nidigital.PPMUOutputFunction.VOLTAGE` | Specifies the output method to DC Voltage. |
        +--------------------------------------------------+--------------------------------------------+
        | :py:data:`~nidigital.PPMUOutputFunction.CURRENT` | Specifies the output method to DC Current. |
        +--------------------------------------------------+--------------------------------------------+


        .. tip:: This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].ppmu_output_function`

            To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.ppmu_output_function`

        The following table lists the characteristics of this property.

            +-----------------------+--------------------------+
            | Characteristic        | Value                    |
            +=======================+==========================+
            | Datatype              | enums.PPMUOutputFunction |
            +-----------------------+--------------------------+
            | Permissions           | read-write               |
            +-----------------------+--------------------------+
            | Repeated Capabilities | channels, pins           |
            +-----------------------+--------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PPMU_OUTPUT_FUNCTION**

ppmu_voltage_level
------------------

    .. py:attribute:: ppmu_voltage_level

        Specifies the voltage level, in volts, that the PPMU forces to the DUT. This property is applicable only when you set the :py:attr:`nidigital.Session.ppmu_output_function` property to DC Voltage.




        .. tip:: This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].ppmu_voltage_level`

            To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.ppmu_voltage_level`

        The following table lists the characteristics of this property.

            +-----------------------+----------------+
            | Characteristic        | Value          |
            +=======================+================+
            | Datatype              | float          |
            +-----------------------+----------------+
            | Permissions           | read-write     |
            +-----------------------+----------------+
            | Repeated Capabilities | channels, pins |
            +-----------------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PPMU_VOLTAGE_LEVEL**

ppmu_voltage_limit_high
-----------------------

    .. py:attribute:: ppmu_voltage_limit_high

        Specifies the maximum voltage limit, or high clamp voltage (V :sub:`CH` ), in volts, at the pin when the PPMU forces current to the DUT. This property is applicable only when you set the :py:attr:`nidigital.Session.ppmu_output_function` property to DC Current.




        .. tip:: This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].ppmu_voltage_limit_high`

            To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.ppmu_voltage_limit_high`

        The following table lists the characteristics of this property.

            +-----------------------+----------------+
            | Characteristic        | Value          |
            +=======================+================+
            | Datatype              | float          |
            +-----------------------+----------------+
            | Permissions           | read-write     |
            +-----------------------+----------------+
            | Repeated Capabilities | channels, pins |
            +-----------------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PPMU_VOLTAGE_LIMIT_HIGH**

ppmu_voltage_limit_low
----------------------

    .. py:attribute:: ppmu_voltage_limit_low

        Specifies the minimum voltage limit, or low clamp voltage (V :sub:`CL` ), in volts, at the pin when the PPMU forces current to the DUT. This property is applicable only when you set the :py:attr:`nidigital.Session.ppmu_output_function` property to DC Current.




        .. tip:: This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].ppmu_voltage_limit_low`

            To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.ppmu_voltage_limit_low`

        The following table lists the characteristics of this property.

            +-----------------------+----------------+
            | Characteristic        | Value          |
            +=======================+================+
            | Datatype              | float          |
            +-----------------------+----------------+
            | Permissions           | read-write     |
            +-----------------------+----------------+
            | Repeated Capabilities | channels, pins |
            +-----------------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_PPMU_VOLTAGE_LIMIT_LOW**

query_instrument_status
-----------------------

    .. py:attribute:: query_instrument_status

        Specifies whether the NI-Digital Pattern Driver queries the digital pattern instrument status after each operation. The instrument status is always queried, regardless of the property setting.

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

                - C Attribute: **NIDIGITAL_ATTR_QUERY_INSTRUMENT_STATUS**

range_check
-----------

    .. py:attribute:: range_check

        Checks the range and validates parameter and property values you pass to NI-Digital Pattern Driver methods. Ranges are always checked, regardless of the property setting.

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

                - C Attribute: **NIDIGITAL_ATTR_RANGE_CHECK**

record_coercions
----------------

    .. py:attribute:: record_coercions

        Specifies whether the IVI engine keeps a list of the value coercions it makes for integer and real type properties. Enabling record value coercions is not supported.

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

                - C Attribute: **NIDIGITAL_ATTR_RECORD_COERCIONS**

rio_event_terminal_name
-----------------------

    .. py:attribute:: rio_event_terminal_name

        Specifies the terminal name for the output signal of the specified instance of a RIO Event. You can use this terminal name as an input signal source for another trigger.




        .. tip:: This property can be set/get on specific rio_events within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container rio_events to specify a subset.

            Example: :py:attr:`my_session.rio_events[ ... ].rio_event_terminal_name`

            To set/get on all rio_events, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.rio_event_terminal_name`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read only  |
            +-----------------------+------------+
            | Repeated Capabilities | rio_events |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_RIO_EVENT_TERMINAL_NAME**

rio_trigger_terminal_name
-------------------------

    .. py:attribute:: rio_trigger_terminal_name

        Specifies the terminal name from which the exported RIO trigger signal may be routed to other instruments through the PXI trigger bus. You can use this signal to trigger other instruments when the RIO trigger instance asserts on the digital pattern instrument.




        .. tip:: This property can be set/get on specific rio_triggers within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container rio_triggers to specify a subset.

            Example: :py:attr:`my_session.rio_triggers[ ... ].rio_trigger_terminal_name`

            To set/get on all rio_triggers, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.rio_trigger_terminal_name`

        The following table lists the characteristics of this property.

            +-----------------------+--------------+
            | Characteristic        | Value        |
            +=======================+==============+
            | Datatype              | str          |
            +-----------------------+--------------+
            | Permissions           | read only    |
            +-----------------------+--------------+
            | Repeated Capabilities | rio_triggers |
            +-----------------------+--------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_RIO_TRIGGER_TERMINAL_NAME**

rio_trigger_type
----------------

    .. py:attribute:: rio_trigger_type

        Disables the rio trigger or configures it for hardware triggering.  The default value is :py:data:`~nidigital.TriggerType.NONE`.

        +------------------------------------------------+------------------------------------------------------------------+
        | Valid Values:                                  |                                                                  |
        +================================================+==================================================================+
        | :py:data:`~nidigital.TriggerType.NONE`         | Disables the conditional jump trigger.                           |
        +------------------------------------------------+------------------------------------------------------------------+
        | :py:data:`~nidigital.TriggerType.DIGITAL_EDGE` | Configures the conditional jump trigger for hardware triggering. |
        +------------------------------------------------+------------------------------------------------------------------+


        .. tip:: This property can be set/get on specific rio_triggers within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container rio_triggers to specify a subset.

            Example: :py:attr:`my_session.rio_triggers[ ... ].rio_trigger_type`

            To set/get on all rio_triggers, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.rio_trigger_type`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------+
            | Characteristic        | Value             |
            +=======================+===================+
            | Datatype              | enums.TriggerType |
            +-----------------------+-------------------+
            | Permissions           | read-write        |
            +-----------------------+-------------------+
            | Repeated Capabilities | rio_triggers      |
            +-----------------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_RIO_TRIGGER_TYPE**

selected_function
-----------------

    .. py:attribute:: selected_function

        .. caution:: In the Disconnect state, some I/O protection and sensing circuitry remains exposed. Do not subject the instrument to voltage beyond its operating range.

        Specifies whether digital pattern instrument channels are controlled by the pattern sequencer or PPMU, disconnected, or off.

        +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Defined Values:                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
        +===================================================+==================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
        | :py:data:`~nidigital.SelectedFunction.DIGITAL`    | The pin is connected to the driver, comparator, and active load methods. The PPMU is not sourcing, but can make voltage measurements. The state of the digital pin driver when you change the :py:attr:`nidigital.Session.selected_function` to Digital is determined by the most recent call to the :py:meth:`nidigital.Session.write_static` method or the last vector of the most recently executed pattern burst, whichever happened last. Use the :py:meth:`nidigital.Session.write_static` method to control the state of the digital pin driver through software. Use the :py:meth:`nidigital.Session.burst_pattern` method to control the state of the digital pin driver through a pattern. Set the **selectDigitalFunction** parameter of the :py:meth:`nidigital.Session.burst_pattern` method to True to automatically switch the :py:attr:`nidigital.Session.selected_function` of the pins in the pattern burst to :py:data:`~nidigital.SelectedFunction.DIGITAL`. |
        +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nidigital.SelectedFunction.PPMU`       | The pin is connected to the PPMU. The driver, comparator, and active load are off while this method is selected. Call the :py:meth:`nidigital.Session.ppmu_source` method to source a voltage or current. The :py:meth:`nidigital.Session.ppmu_source` method automatically switches the :py:attr:`nidigital.Session.selected_function` to the PPMU state and starts sourcing from the PPMU. Changing the :py:attr:`nidigital.Session.selected_function` to :py:data:`~nidigital.SelectedFunction.DISCONNECT`, :py:data:`~nidigital.SelectedFunction.OFF`, or :py:data:`~nidigital.SelectedFunction.DIGITAL` causes the PPMU to stop sourcing. If you set the :py:attr:`nidigital.Session.selected_function` property to PPMU, the PPMU is initially not sourcing.                                                                                                                                                                                                               |
        +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nidigital.SelectedFunction.OFF`        | The pin is electrically connected, and the PPMU and digital pin driver are off while this method is selected.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
        +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nidigital.SelectedFunction.DISCONNECT` | The pin is electrically disconnected from instrument methods. Selecting this method causes the PPMU to stop sourcing prior to disconnecting the pin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
        +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: You can make PPMU voltage measurements using the :py:meth:`nidigital.Session.ppmu_measure` method from within any :py:attr:`nidigital.Session.selected_function`.


        .. tip:: This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].selected_function`

            To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.selected_function`

        The following table lists the characteristics of this property.

            +-----------------------+------------------------+
            | Characteristic        | Value                  |
            +=======================+========================+
            | Datatype              | enums.SelectedFunction |
            +-----------------------+------------------------+
            | Permissions           | read-write             |
            +-----------------------+------------------------+
            | Repeated Capabilities | channels, pins         |
            +-----------------------+------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_SELECTED_FUNCTION**

sequencer_flag_terminal_name
----------------------------

    .. py:attribute:: sequencer_flag_terminal_name

        Specifies the terminal name for the output trigger signal of the Sequencer Flags trigger. You can use this terminal name as an input signal source for another trigger.

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

                - C Attribute: **NIDIGITAL_ATTR_SEQUENCER_FLAG_TERMINAL_NAME**

serial_number
-------------

    .. py:attribute:: serial_number

        Returns the serial number of the device.




        .. tip:: This property can be set/get on specific instruments within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container instruments to specify a subset.

            Example: :py:attr:`my_session.instruments[ ... ].serial_number`

            To set/get on all instruments, you can call the property directly on the :py:class:`nidigital.Session`.

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

                - C Attribute: **NIDIGITAL_ATTR_SERIAL_NUMBER**

simulate
--------

    .. py:attribute:: simulate

        Simulates I/O operations. After you open a session, you cannot change the simulation state. Use the :py:meth:`nidigital.Session.__init__` method to enable simulation.

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

                - C Attribute: **NIDIGITAL_ATTR_SIMULATE**

specific_driver_class_spec_major_version
----------------------------------------

    .. py:attribute:: specific_driver_class_spec_major_version

        Returns the major version number of the class specification with which NI-Digital is compliant. This property is not supported.

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

                - C Attribute: **NIDIGITAL_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION**

specific_driver_class_spec_minor_version
----------------------------------------

    .. py:attribute:: specific_driver_class_spec_minor_version

        Returns the minor version number of the class specification with which NI-Digital is compliant. This property is not supported.

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

                - C Attribute: **NIDIGITAL_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION**

specific_driver_description
---------------------------

    .. py:attribute:: specific_driver_description

        Returns a string that contains a brief description of the NI-Digital Pattern driver.

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

                - C Attribute: **NIDIGITAL_ATTR_SPECIFIC_DRIVER_DESCRIPTION**

specific_driver_prefix
----------------------

    .. py:attribute:: specific_driver_prefix

        Returns a string that contains the prefix for the NI-Digital Pattern driver.

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

                - C Attribute: **NIDIGITAL_ATTR_SPECIFIC_DRIVER_PREFIX**

specific_driver_revision
------------------------

    .. py:attribute:: specific_driver_revision

        Returns a string that contains additional version information about the NI-Digital Pattern Driver. For example, the driver can return Driver: NI-Digital 16.0 as the value of this property.

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

                - C Attribute: **NIDIGITAL_ATTR_SPECIFIC_DRIVER_REVISION**

specific_driver_vendor
----------------------

    .. py:attribute:: specific_driver_vendor

        Returns a string ("National Instruments") that contains the name of the vendor that supplies the NI-Digital Pattern Driver.

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

                - C Attribute: **NIDIGITAL_ATTR_SPECIFIC_DRIVER_VENDOR**

start_label
-----------

    .. py:attribute:: start_label

        Specifies the pattern name or exported pattern label from which to start bursting the pattern.

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

                - C Attribute: **NIDIGITAL_ATTR_START_LABEL**

start_trigger_terminal_name
---------------------------

    .. py:attribute:: start_trigger_terminal_name

        Specifies the terminal name for the output trigger signal of the Start trigger. You can use this terminal name as an input signal source for another trigger.

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

                - C Attribute: **NIDIGITAL_ATTR_START_TRIGGER_TERMINAL_NAME**

start_trigger_type
------------------

    .. py:attribute:: start_trigger_type

        Specifies the Start trigger type. The digital pattern instrument waits for this trigger after you call the :py:meth:`nidigital.Session.init` method or the :py:meth:`nidigital.Session.burst_pattern` method, and does not burst a pattern until this trigger is received.

        +------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Defined Values:                                |                                                                                                                                                                                                                                                                                                                                     |
        +================================================+=====================================================================================================================================================================================================================================================================================================================================+
        | :py:data:`~nidigital.TriggerType.NONE`         | Disables the Start trigger. Pattern bursting starts immediately after you call the :py:meth:`nidigital.Session.init` method or the :py:meth:`nidigital.Session.burst_pattern` method.                                                                                                                                               |
        +------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nidigital.TriggerType.DIGITAL_EDGE` | Pattern bursting does not start until the digital pattern instrument detects a digital edge.                                                                                                                                                                                                                                        |
        +------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nidigital.TriggerType.SOFTWARE`     | Pattern bursting does not start until the digital pattern instrument receives a software Start trigger. Create a software Start trigger by calling the :py:meth:`nidigital.Session.send_software_edge_trigger` method and selecting start trigger in the **trigger** parameter.Related information: SendSoftwareEdgeTrigger method. |
        +------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: One or more of the referenced methods are not in the Python API for this driver.

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

                - C Attribute: **NIDIGITAL_ATTR_START_TRIGGER_TYPE**

supported_instrument_models
---------------------------

    .. py:attribute:: supported_instrument_models

        Returns a comma delimited string that contains the supported digital pattern instrument models for the specific driver.

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

                - C Attribute: **NIDIGITAL_ATTR_SUPPORTED_INSTRUMENT_MODELS**

tdr_endpoint_termination
------------------------

    .. py:attribute:: tdr_endpoint_termination

        Specifies whether TDR Channels are connected to an open circuit or a short to ground.

        The following table lists the characteristics of this property.

            +-----------------------+------------------------------+
            | Characteristic        | Value                        |
            +=======================+==============================+
            | Datatype              | enums.TDREndpointTermination |
            +-----------------------+------------------------------+
            | Permissions           | read-write                   |
            +-----------------------+------------------------------+
            | Repeated Capabilities | None                         |
            +-----------------------+------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_TDR_ENDPOINT_TERMINATION**

tdr_offset
----------

    .. py:attribute:: tdr_offset

        Specifies the TDR Offset.




        .. tip:: This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].tdr_offset`

            To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.tdr_offset`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------------------------------+
            | Characteristic        | Value                                                       |
            +=======================+=============================================================+
            | Datatype              | hightime.timedelta, datetime.timedelta, or float in seconds |
            +-----------------------+-------------------------------------------------------------+
            | Permissions           | read-write                                                  |
            +-----------------------+-------------------------------------------------------------+
            | Repeated Capabilities | channels, pins                                              |
            +-----------------------+-------------------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_TDR_OFFSET**

termination_mode
----------------

    .. py:attribute:: termination_mode

        Specifies the behavior of the pin during non-drive cycles.

        +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Defined Values:                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
        +===================================================+======================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
        | :py:data:`~nidigital.TerminationMode.ACTIVE_LOAD` | Specifies that, for non-drive pin states (L, H, X, V, M, E), the active load is connected and the instrument sources or sinks a defined amount of current to load the DUT. The amount of current sourced by the instrument and therefore sunk by the DUT is specified by IOL. The amount of current sunk by the instrument and therefore sourced by the DUT is specified by IOH. The voltage at which the instrument changes between sourcing and sinking is specified by VCOM.                                                                                                                                                                                                                                                                                                                                                                                      |
        +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nidigital.TerminationMode.VTERM`       | Specifies that, for non-drive pin states (L, H, X, V, M, E), the pin driver terminates the pin to the configured VTERM voltage through a 50 Ω impedance. VTERM is adjustable to allow for the pin to terminate at a set level. This is useful for instruments that might operate incorrectly if an instrument pin is unterminated and is allowed to float to any voltage level within the instrument voltage range. To address this issue, enable VTERM by configuring the VTERM pin level to the desired voltage and selecting the VTERM termination mode. Setting VTERM to 0 V and selecting the VTERM termination mode has the effect of connecting a 50 Ω termination to ground, which provides an effective 50 Ω impedance for the pin. This can be useful for improving signal integrity of certain DUTs by reducing reflections while the DUT drives the pin. |
        +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nidigital.TerminationMode.HIGH_Z`      | Specifies that, for non-drive pin states (L, H, X, V, M, E), the pin driver is put in a high-impedance state and the active load is disabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
        +---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


        .. tip:: This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].termination_mode`

            To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.termination_mode`

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------+
            | Characteristic        | Value                 |
            +=======================+=======================+
            | Datatype              | enums.TerminationMode |
            +-----------------------+-----------------------+
            | Permissions           | read-write            |
            +-----------------------+-----------------------+
            | Repeated Capabilities | channels, pins        |
            +-----------------------+-----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_TERMINATION_MODE**

timing_absolute_delay
---------------------

    .. py:attribute:: timing_absolute_delay

        Specifies a timing delay, measured in seconds, and applies the delay to the digital pattern instrument in addition to TDR and calibration adjustments. If the :py:attr:`nidigital.Session.timing_absolute_delay_enabled` property is set to True, this value is the intermodule skew measured by NI-TClk. You can modify this value to override the timing delay and align the I/O timing of this instrument with another instrument that shares the same reference clock. If the :py:attr:`nidigital.Session.timing_absolute_delay_enabled` property is False, this property will return 0.0. Changing the :py:attr:`nidigital.Session.timing_absolute_delay_enabled` property from False to True will set the :py:attr:`nidigital.Session.timing_absolute_delay` value back to your previously set value.




        .. tip:: This property can be set/get on specific instruments within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container instruments to specify a subset.

            Example: :py:attr:`my_session.instruments[ ... ].timing_absolute_delay`

            To set/get on all instruments, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.timing_absolute_delay`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------------------------------------------+
            | Characteristic        | Value                                                       |
            +=======================+=============================================================+
            | Datatype              | hightime.timedelta, datetime.timedelta, or float in seconds |
            +-----------------------+-------------------------------------------------------------+
            | Permissions           | read-write                                                  |
            +-----------------------+-------------------------------------------------------------+
            | Repeated Capabilities | instruments                                                 |
            +-----------------------+-------------------------------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_TIMING_ABSOLUTE_DELAY**

timing_absolute_delay_enabled
-----------------------------

    .. py:attribute:: timing_absolute_delay_enabled

        Specifies whether the :py:attr:`nidigital.Session.timing_absolute_delay` property should be applied to adjust the digital pattern instrument timing reference relative to other instruments in the system. Do not use this feature with digital pattern instruments in a Semiconductor Test System (STS). Timing absolute delay conflicts with the adjustment performed during STS timing calibration. When set to True, the digital pattern instrument automatically adjusts the timing absolute delay to correct the instrument timing reference relative to other instruments in the system for better timing alignment among synchronized instruments.

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

                - C Attribute: **NIDIGITAL_ATTR_TIMING_ABSOLUTE_DELAY_ENABLED**

vih
---

    .. py:attribute:: vih

        Specifies the voltage that the digital pattern instrument will apply to the input of the DUT when the test instrument drives a logic high (1).




        .. tip:: This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].vih`

            To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.vih`

        The following table lists the characteristics of this property.

            +-----------------------+----------------+
            | Characteristic        | Value          |
            +=======================+================+
            | Datatype              | float          |
            +-----------------------+----------------+
            | Permissions           | read-write     |
            +-----------------------+----------------+
            | Repeated Capabilities | channels, pins |
            +-----------------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_VIH**

vil
---

    .. py:attribute:: vil

        Specifies the voltage that the digital pattern instrument will apply to the input of the DUT when the test instrument drives a logic low (0).




        .. tip:: This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].vil`

            To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.vil`

        The following table lists the characteristics of this property.

            +-----------------------+----------------+
            | Characteristic        | Value          |
            +=======================+================+
            | Datatype              | float          |
            +-----------------------+----------------+
            | Permissions           | read-write     |
            +-----------------------+----------------+
            | Repeated Capabilities | channels, pins |
            +-----------------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_VIL**

voh
---

    .. py:attribute:: voh

        Specifies the output voltage from the DUT above which the comparator on the digital pattern test instrument interprets a logic high (H).




        .. tip:: This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].voh`

            To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.voh`

        The following table lists the characteristics of this property.

            +-----------------------+----------------+
            | Characteristic        | Value          |
            +=======================+================+
            | Datatype              | float          |
            +-----------------------+----------------+
            | Permissions           | read-write     |
            +-----------------------+----------------+
            | Repeated Capabilities | channels, pins |
            +-----------------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_VOH**

vol
---

    .. py:attribute:: vol

        Specifies the output voltage from the DUT below which the comparator on the digital pattern test instrument interprets a logic low (L).




        .. tip:: This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].vol`

            To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.vol`

        The following table lists the characteristics of this property.

            +-----------------------+----------------+
            | Characteristic        | Value          |
            +=======================+================+
            | Datatype              | float          |
            +-----------------------+----------------+
            | Permissions           | read-write     |
            +-----------------------+----------------+
            | Repeated Capabilities | channels, pins |
            +-----------------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_VOL**

vterm
-----

    .. py:attribute:: vterm

        Specifies the termination voltage the digital pattern instrument applies during non-drive cycles when the termination mode is set to V :sub:`term`. The instrument applies the termination voltage through a 50 Ω parallel termination resistance.




        .. tip:: This property can be set/get on specific channels or pins within your :py:class:`nidigital.Session` instance.
            Use Python index notation on the repeated capabilities container channels or pins to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].vterm`

            To set/get on all channels or pins, you can call the property directly on the :py:class:`nidigital.Session`.

            Example: :py:attr:`my_session.vterm`

        The following table lists the characteristics of this property.

            +-----------------------+----------------+
            | Characteristic        | Value          |
            +=======================+================+
            | Datatype              | float          |
            +-----------------------+----------------+
            | Permissions           | read-write     |
            +-----------------------+----------------+
            | Repeated Capabilities | channels, pins |
            +-----------------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIDIGITAL_ATTR_VTERM**


NI-TClk Support
===============

    .. py:attribute:: tclk

        This is used to get and set NI-TClk attributes on the session.

        .. seealso:: See :py:class:`nitclk.SessionReference` for a complete list of attributes.


.. contents:: Session
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nidigital/conf.py sha256=36ca15ca7807bb78a3c643b2f0c8cc12b426adf0d5d939db76739ed92587d1c1 bytes=6679 -->
## FILE: docs/nidigital/conf.py

- repository: `ni/nimi-python`
- source_path: `docs/nidigital/conf.py`
- sha256: `36ca15ca7807bb78a3c643b2f0c8cc12b426adf0d5d939db76739ed92587d1c1`
- bytes: 6679

````python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# NI-Digital Pattern Driver Python API documentation build configuration file, created by
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
project = 'NI-Digital Pattern Driver Python API'
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
    (master_doc, 'NIDigitalPatternDriverPythonAPI.tex', 'NI-Digital Pattern Driver Python API Documentation',
     'NI', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'nidigitalpatterndriverpythonapi', 'NI-Digital Pattern Driver Python API Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'NIDigitalPatternDriverPythonAPI', 'NI-Digital Pattern Driver Python API Documentation',
     author, 'NIDigitalPatternDriverPythonAPI', 'One line description of project.',
     'Miscellaneous'),
]

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'nidcpower': ('https://nidcpower.readthedocs.io/en/latest/', None),
    'nidmm': ('https://nidmm.readthedocs.io/en/latest/', None),
    'nifgen': ('https://nifgen.readthedocs.io/en/latest/', None),
    'nimodinst': ('https://nimodinst.readthedocs.io/en/latest/', None),
    'nirfsg': ('https://nirfsg.readthedocs.io/en/latest/', None),
    'niscope': ('https://niscope.readthedocs.io/en/latest/', None),
    'nise': ('https://nise.readthedocs.io/en/latest/', None),
    'niswitch': ('https://niswitch.readthedocs.io/en/latest/', None),
    'nitclk': ('https://nitclk.readthedocs.io/en/latest/', None),
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nidigital/enums.rst sha256=4dda5fbc17dbf7b66a677b2ad1f7ba6b700c08cc573c324067a4c75993a917ae bytes=10450 -->
## FILE: docs/nidigital/enums.rst

- repository: `ni/nimi-python`
- source_path: `docs/nidigital/enums.rst`
- sha256: `4dda5fbc17dbf7b66a677b2ad1f7ba6b700c08cc573c324067a4c75993a917ae`
- bytes: 10450

````rst
Enums
=====

Enums used in NI-Digital Pattern Driver

.. py:currentmodule:: nidigital


BitOrder
--------

.. py:class:: BitOrder

    .. py:attribute:: BitOrder.MSB



        The most significant bit is first. The first bit is in the 2^n place, where n is the number of bits.

        



    .. py:attribute:: BitOrder.LSB



        The least significant bit is first. The first bit is in the 2^0 place.

        



DigitalEdge
-----------

.. py:class:: DigitalEdge

    .. py:attribute:: DigitalEdge.RISING



        Asserts the trigger when the signal transitions from low level to high level.

        



    .. py:attribute:: DigitalEdge.FALLING



        Asserts the trigger when the signal transitions from high level to low level.

        



DriveFormat
-----------

.. py:class:: DriveFormat

    .. py:attribute:: DriveFormat.NR



        Drive format remains at logic level after each bit.

        



    .. py:attribute:: DriveFormat.RL



        Drive format returns to a logic level low after each bit.

        



    .. py:attribute:: DriveFormat.RH



        Drive format returns to a logic level high after each bit.

        



    .. py:attribute:: DriveFormat.SBC



        Drive format returns to the complement logic level of the bit after each bit.

        



FrequencyMeasurementMode
------------------------

.. py:class:: FrequencyMeasurementMode

    .. py:attribute:: FrequencyMeasurementMode.BANKED



        Frequency measurements are made serially for groups of channels associated with a single frequency counter for each group.

        Maximum frequency measured: 200 MHz.

        



    .. py:attribute:: FrequencyMeasurementMode.PARALLEL



        Frequency measurements are made by multiple frequency counters in parallel.

        Maximum frequency measured: 100 MHz.

        



HistoryRAMCyclesToAcquire
-------------------------

.. py:class:: HistoryRAMCyclesToAcquire

    .. py:attribute:: HistoryRAMCyclesToAcquire.FAILED



        Acquires failed cycles.

        



    .. py:attribute:: HistoryRAMCyclesToAcquire.ALL



        Acquires all cycles.

        



HistoryRAMTriggerType
---------------------

.. py:class:: HistoryRAMTriggerType

    .. py:attribute:: HistoryRAMTriggerType.FIRST_FAILURE



        First Failure History RAM trigger

        



    .. py:attribute:: HistoryRAMTriggerType.CYCLE_NUMBER



        Cycle Number History RAM trigger.

        



    .. py:attribute:: HistoryRAMTriggerType.PATTERN_LABEL



        Pattern Label History RAM trigger

        



PPMUApertureTimeUnits
---------------------

.. py:class:: PPMUApertureTimeUnits

    .. py:attribute:: PPMUApertureTimeUnits.SECONDS



        Unit in seconds.

        



PPMUCurrentLimitBehavior
------------------------

.. py:class:: PPMUCurrentLimitBehavior

    .. py:attribute:: PPMUCurrentLimitBehavior.REGULATE



        Controls output current so that it does not exceed the current limit. Power continues to generate even if the current limit is reached.

        



PPMUMeasurementType
-------------------

.. py:class:: PPMUMeasurementType

    .. py:attribute:: PPMUMeasurementType.CURRENT



        The PPMU measures current.

        



    .. py:attribute:: PPMUMeasurementType.VOLTAGE



        The PPMU measures voltage.

        



PPMUOutputFunction
------------------

.. py:class:: PPMUOutputFunction

    .. py:attribute:: PPMUOutputFunction.VOLTAGE



        The PPMU forces voltage to the DUT.

        



    .. py:attribute:: PPMUOutputFunction.CURRENT



        The PPMU forces current to the DUT.

        



PinState
--------

.. py:class:: PinState

    .. py:attribute:: PinState.ZERO



        A digital state of 0.

        



    .. py:attribute:: PinState.ONE



        A digital state of 1.

        



    .. py:attribute:: PinState.L



        A digital state of L (low).

        



    .. py:attribute:: PinState.H



        A digital state of H (high).

        



    .. py:attribute:: PinState.X



        A digital state of X (non-drive state).

        



    .. py:attribute:: PinState.M



        A digital state of M (midband).

        



    .. py:attribute:: PinState.V



        A digital state of V (compare high or low, not midband; store results from capture functionality if configured).

        



    .. py:attribute:: PinState.D



        A digital state of D (drive data from source functionality if configured).

        



    .. py:attribute:: PinState.E



        A digital state of E (compare data from source functionality if configured).

        



    .. py:attribute:: PinState.NOT_A_PIN_STATE



        Not a pin state is used for non-existent DUT cycles.

        



    .. py:attribute:: PinState.PIN_STATE_NOT_ACQUIRED



        Pin state could not be acquired because none of the pins mapped to the instrument in a multi-instrument session had any failures.

        



SelectedFunction
----------------

.. py:class:: SelectedFunction

    .. py:attribute:: SelectedFunction.DIGITAL



        The pattern sequencer controls the specified pin(s). If a pattern is currently bursting, the pin immediately switches to bursting the pattern. This option disconnects the PPMU.

        



    .. py:attribute:: SelectedFunction.PPMU



        The PPMU controls the specified pin(s) and connects the PPMU. The pin driver is in a non-drive state, and the active load is disabled. The PPMU does not start sourcing or measuring until Source or Measure(PpmuMeasurementType) is called.

        



    .. py:attribute:: SelectedFunction.OFF



        Puts the digital driver in a non-drive state, disables the active load, disconnects the PPMU, and closes the I/O switch connecting the instrument channel.

        



    .. py:attribute:: SelectedFunction.DISCONNECT



        The I/O switch connecting the instrument channel is open to the I/O connector. If the PPMU is sourcing, it is stopped prior to opening the I/O switch.

        



    .. py:attribute:: SelectedFunction.RIO



        Yields control of the specified pin(s) to LabVIEW FPGA.

        



SequencerFlag
-------------

.. py:class:: SequencerFlag

    .. py:attribute:: SequencerFlag.FLAG0



    .. py:attribute:: SequencerFlag.FLAG1



    .. py:attribute:: SequencerFlag.FLAG2



    .. py:attribute:: SequencerFlag.FLAG3



SequencerRegister
-----------------

.. py:class:: SequencerRegister

    .. py:attribute:: SequencerRegister.REGISTER0



    .. py:attribute:: SequencerRegister.REGISTER1



    .. py:attribute:: SequencerRegister.REGISTER2



    .. py:attribute:: SequencerRegister.REGISTER3



    .. py:attribute:: SequencerRegister.REGISTER4



    .. py:attribute:: SequencerRegister.REGISTER5



    .. py:attribute:: SequencerRegister.REGISTER6



    .. py:attribute:: SequencerRegister.REGISTER7



    .. py:attribute:: SequencerRegister.REGISTER8



    .. py:attribute:: SequencerRegister.REGISTER9



    .. py:attribute:: SequencerRegister.REGISTER10



    .. py:attribute:: SequencerRegister.REGISTER11



    .. py:attribute:: SequencerRegister.REGISTER12



    .. py:attribute:: SequencerRegister.REGISTER13



    .. py:attribute:: SequencerRegister.REGISTER14



    .. py:attribute:: SequencerRegister.REGISTER15



SoftwareTrigger
---------------

.. py:class:: SoftwareTrigger

    .. py:attribute:: SoftwareTrigger.START



        Overrides the start trigger.

        



    .. py:attribute:: SoftwareTrigger.CONDITIONAL_JUMP



        Specifies to route a conditional jump trigger.

        



SourceDataMapping
-----------------

.. py:class:: SourceDataMapping

    .. py:attribute:: SourceDataMapping.BROADCAST



        Broadcasts the waveform you specify to all sites.

        



    .. py:attribute:: SourceDataMapping.SITE_UNIQUE



        Sources unique waveform data to each site.

        



TDREndpointTermination
----------------------

.. py:class:: TDREndpointTermination

    .. py:attribute:: TDREndpointTermination.OPEN



        TDR channels are connected to an open circuit.

        



    .. py:attribute:: TDREndpointTermination.SHORT_TO_GROUND



        TDR channels are connected to a short to ground.

        



TerminationMode
---------------

.. py:class:: TerminationMode

    .. py:attribute:: TerminationMode.ACTIVE_LOAD



        The active load provides a constant current to a commutating voltage (Vcom).

        



    .. py:attribute:: TerminationMode.VTERM



        The pin driver drives Vterm.

        



    .. py:attribute:: TerminationMode.HIGH_Z



        The pin driver is in a non-drive state (in a high-impedance state) and the active load is disabled.

        



TimeSetEdgeType
---------------

.. py:class:: TimeSetEdgeType

    .. py:attribute:: TimeSetEdgeType.DRIVE_ON



        Specifies the drive on edge of the time set.

        



    .. py:attribute:: TimeSetEdgeType.DRIVE_DATA



        Specifies the drive data edge of the time set.

        



    .. py:attribute:: TimeSetEdgeType.DRIVE_RETURN



        Specifies the drive return edge of the time set.

        



    .. py:attribute:: TimeSetEdgeType.DRIVE_OFF



        Specifies the drive off edge of the time set.

        



    .. py:attribute:: TimeSetEdgeType.COMPARE_STROBE



        Specifies the compare strobe of the time set.

        



    .. py:attribute:: TimeSetEdgeType.DRIVE_DATA2



        Specifies the drive data 2 edge of the time set.

        



    .. py:attribute:: TimeSetEdgeType.DRIVE_RETURN2



        Specifies the drive return 2 edge of the time set.

        



    .. py:attribute:: TimeSetEdgeType.COMPARE_STROBE2



        Specifies the compare strobe 2 of the time set.

        



TriggerType
-----------

.. py:class:: TriggerType

    .. py:attribute:: TriggerType.NONE



        Disables the start trigger.

        



    .. py:attribute:: TriggerType.DIGITAL_EDGE



        Digital edge trigger.

        



    .. py:attribute:: TriggerType.SOFTWARE



        Software start trigger.

        



WriteStaticPinState
-------------------

.. py:class:: WriteStaticPinState

    .. py:attribute:: WriteStaticPinState.ZERO



        Specifies to drive low.

        



    .. py:attribute:: WriteStaticPinState.ONE



        Specifies to drive high.

        



    .. py:attribute:: WriteStaticPinState.X



        Specifies to not drive.

        
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nidigital/errors.rst sha256=0312ef54ee74ca71fbcbe9eedbda15293d6296c12b8d6ca69090943c14750f1f bytes=2015 -->
## FILE: docs/nidigital/errors.rst

- repository: `ni/nimi-python`
- source_path: `docs/nidigital/errors.rst`
- sha256: `0312ef54ee74ca71fbcbe9eedbda15293d6296c12b8d6ca69090943c14750f1f`
- bytes: 2015

````rst
Exceptions and Warnings
=======================

Error
-----

    .. py:currentmodule:: nidigital.errors

    .. exception:: Error

        Base exception type that all NI-Digital Pattern Driver exceptions derive from


DriverError
-----------

    .. py:currentmodule:: nidigital.errors

    .. exception:: DriverError

        An error originating from the NI-Digital Pattern Driver driver


UnsupportedConfigurationError
-----------------------------

    .. py:currentmodule:: nidigital.errors

    .. exception:: UnsupportedConfigurationError

        An error due to using this module in an usupported platform.

DriverNotInstalledError
-----------------------

    .. py:currentmodule:: nidigital.errors

    .. exception:: DriverNotInstalledError

        An error due to using this module without the driver runtime installed.

DriverTooOldError
-----------------

    .. py:currentmodule:: nidigital.errors

    .. exception:: DriverTooOldError

        An error due to using this module with an older version of the NI-Digital Pattern Driver driver runtime.

DriverTooNewError
-----------------

    .. py:currentmodule:: nidigital.errors

    .. exception:: DriverTooNewError

        An error due to the NI-Digital Pattern Driver driver runtime being too new for this module.

InvalidRepeatedCapabilityError
------------------------------

    .. py:currentmodule:: nidigital.errors

    .. exception:: InvalidRepeatedCapabilityError

        An error due to an invalid character in a repeated capability


SelfTestError
-------------

    .. py:currentmodule:: nidigital.errors

    .. exception:: SelfTestError

        An error due to a failed self-test


RpcError
--------

    .. py:currentmodule:: nidigital.errors

    .. exception:: RpcError

        An error specific to sessions to the NI gRPC Device Server


DriverWarning
-------------

    .. py:currentmodule:: nidigital.errors

    .. exception:: DriverWarning

        A warning originating from the NI-Digital Pattern Driver driver
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nidigital/examples.rst sha256=777e4d0e960ccd13bb7cb48dd7098261cbe95da39993c181df448aa4ed86e197 bytes=1553 -->
## FILE: docs/nidigital/examples.rst

- repository: `ni/nimi-python`
- source_path: `docs/nidigital/examples.rst`
- sha256: `777e4d0e960ccd13bb7cb48dd7098261cbe95da39993c181df448aa4ed86e197`
- bytes: 1553

````rst
Examples
========

`You can download all nidigital examples for latest version here <https://github.com/ni/nimi-python/releases/download/1.4.9/nidigital_examples.zip>`_

nidigital_burst_with_start_trigger.py
-------------------------------------

.. literalinclude:: ../../src/nidigital/examples/burst_with_start_trigger/nidigital_burst_with_start_trigger.py
   :language: python
   :linenos:
   :encoding: utf8
   :caption: `(nidigital_burst_with_start_trigger.py) <https://github.com/ni/nimi-python/blob/master/src/nidigital/examples/burst_with_start_trigger/nidigital_burst_with_start_trigger.py>`_

nidigital_configure_time_set_and_voltage_levels.py
--------------------------------------------------

.. literalinclude:: ../../src/nidigital/examples/configure_time_set_and_voltage_levels/nidigital_configure_time_set_and_voltage_levels.py
   :language: python
   :linenos:
   :encoding: utf8
   :caption: `(nidigital_configure_time_set_and_voltage_levels.py) <https://github.com/ni/nimi-python/blob/master/src/nidigital/examples/configure_time_set_and_voltage_levels/nidigital_configure_time_set_and_voltage_levels.py>`_

nidigital_ppmu_source_and_measure.py
------------------------------------

.. literalinclude:: ../../src/nidigital/examples/ppmu_source_and_measure/nidigital_ppmu_source_and_measure.py
   :language: python
   :linenos:
   :encoding: utf8
   :caption: `(nidigital_ppmu_source_and_measure.py) <https://github.com/ni/nimi-python/blob/master/src/nidigital/examples/ppmu_source_and_measure/nidigital_ppmu_source_and_measure.py>`_
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nidigital/grpc_session_options.rst sha256=96992e95720342d990dc089f232d7c5f90d532eac9b8fd8503a3fc8f11d0e3ca bytes=2911 -->
## FILE: docs/nidigital/grpc_session_options.rst

- repository: `ni/nimi-python`
- source_path: `docs/nidigital/grpc_session_options.rst`
- sha256: `96992e95720342d990dc089f232d7c5f90d532eac9b8fd8503a3fc8f11d0e3ca`
- bytes: 2911

````rst
gRPC Support
============

Support for using NI-Digital Pattern Driver over gRPC

.. py:currentmodule:: nidigital



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

        

    :type initialization_behavior: :py:data:`nidigital.SessionInitializationBehavior`
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nidigital/index.rst sha256=409b61042e5d2951cbe7915db45d555c17fd1adeb0a6c0251c52e4f4d7ee0347 bytes=728 -->
## FILE: docs/nidigital/index.rst

- repository: `ni/nimi-python`
- source_path: `docs/nidigital/index.rst`
- sha256: `409b61042e5d2951cbe7915db45d555c17fd1adeb0a6c0251c52e4f4d7ee0347`
- bytes: 728

````rst

NI-Digital Pattern Driver Python API Documentation
==================================================

.. include:: about_nidigital.inc

.. include:: ../_static/contributing.inc

.. include:: ../_static/support.inc

.. toctree::
   :maxdepth: 3
   :caption: Documentation

   nidigital

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

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nidigital/installation.inc sha256=7ce1e21a1d9017b5d29a9292a701451e0edb8bbdc52147d17b65bcb1befded7b bytes=465 -->
## FILE: docs/nidigital/installation.inc

- repository: `ni/nimi-python`
- source_path: `docs/nidigital/installation.inc`
- sha256: `7ce1e21a1d9017b5d29a9292a701451e0edb8bbdc52147d17b65bcb1befded7b`
- bytes: 465

````text

.. _nidigital_installation-section:

Installation
------------

As a prerequisite to using the **nidigital** module, you must install the NI-Digital Pattern Driver runtime on your system. Visit `ni.com/downloads <http://www.ni.com/downloads/>`_ to download the driver runtime for your devices.

The nimi-python modules (i.e. for **NI-Digital Pattern Driver**) can be installed with `pip <http://pypi.python.org/pypi/pip>`_::

  $ python -m pip install nidigital
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nidigital/nidigital.rst sha256=04c1192f414a6a3c7a42a9d54960a686b68f21b8b33fc303def95cf3684a0811 bytes=133 -->
## FILE: docs/nidigital/nidigital.rst

- repository: `ni/nimi-python`
- source_path: `docs/nidigital/nidigital.rst`
- sha256: `04c1192f414a6a3c7a42a9d54960a686b68f21b8b33fc303def95cf3684a0811`
- bytes: 133

````rst
nidigital module
================

.. include:: installation.inc

.. include:: ../_static/nidigital_usage.inc

.. include:: toc.inc
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nidigital/rep_caps.rst sha256=e0ec99bc7309a322ac1772a0f51cf37032c7cb5aecdeadc022b863503bb590bc bytes=6337 -->
## FILE: docs/nidigital/rep_caps.rst

- repository: `ni/nimi-python`
- source_path: `docs/nidigital/rep_caps.rst`
- sha256: `e0ec99bc7309a322ac1772a0f51cf37032c7cb5aecdeadc022b863503bb590bc`
- bytes: 6337

````rst
.. py:module:: nidigital
    :noindex:

.. py:currentmodule:: nidigital.Session

.. role:: c(code)
    :language: c

.. role:: python(code)
    :language: python

Repeated Capabilities
=====================

    Repeated capabilities attributes are used to set the `channel_string` parameter to the
    underlying driver function call. This can be the actual function based on the :py:class:`Session`
    method being called, or it can be the appropriate Get/Set Attribute function, such as :c:`niDigital_SetAttributeViInt32()`.

    Repeated capabilities attributes use the indexing operator :python:`[]` to indicate the repeated capabilities.
    The parameter can be a string, list, tuple, or slice (range). Each element of those can be a string or
    an integer. If it is a string, you can indicate a range using the same format as the driver: :python:`'0-2'` or
    :python:`'0:2'`

    Some repeated capabilities use a prefix before the number and this is optional

channels
--------

    .. py:attribute:: nidigital.Session.channels[]

        .. code:: python

            session.channels['0-2'].channel_enabled = True

        passes a string of :python:`'0, 1, 2'` to the set attribute function.


pins
----

    .. py:attribute:: nidigital.Session.pins[]

        .. code:: python

            session.pins['0-2'].channel_enabled = True

        passes a string of :python:`'0, 1, 2'` to the set attribute function.


instruments
-----------

    .. py:attribute:: nidigital.Session.instruments[]

        .. code:: python

            session.instruments['0-2'].channel_enabled = True

        passes a string of :python:`'0, 1, 2'` to the set attribute function.


pattern_opcode_events
---------------------

    .. py:attribute:: nidigital.Session.pattern_opcode_events[]

        If no prefix is added to the items in the parameter, the correct prefix will be added when
        the driver function call is made.

        .. code:: python

            session.pattern_opcode_events['0-2'].channel_enabled = True

        passes a string of :python:`'patternOpcodeEvent0, patternOpcodeEvent1, patternOpcodeEvent2'` to the set attribute function.

        If an invalid repeated capability is passed to the driver, the driver will return an error.

        You can also explicitly use the prefix as part of the parameter, but it must be the correct prefix
        for the specific repeated capability.

        .. code:: python

            session.pattern_opcode_events['patternOpcodeEvent0-patternOpcodeEvent2'].channel_enabled = True

        passes a string of :python:`'patternOpcodeEvent0, patternOpcodeEvent1, patternOpcodeEvent2'` to the set attribute function.


conditional_jump_triggers
-------------------------

    .. py:attribute:: nidigital.Session.conditional_jump_triggers[]

        If no prefix is added to the items in the parameter, the correct prefix will be added when
        the driver function call is made.

        .. code:: python

            session.conditional_jump_triggers['0-2'].channel_enabled = True

        passes a string of :python:`'conditionalJumpTrigger0, conditionalJumpTrigger1, conditionalJumpTrigger2'` to the set attribute function.

        If an invalid repeated capability is passed to the driver, the driver will return an error.

        You can also explicitly use the prefix as part of the parameter, but it must be the correct prefix
        for the specific repeated capability.

        .. code:: python

            session.conditional_jump_triggers['conditionalJumpTrigger0-conditionalJumpTrigger2'].channel_enabled = True

        passes a string of :python:`'conditionalJumpTrigger0, conditionalJumpTrigger1, conditionalJumpTrigger2'` to the set attribute function.


sites
-----

    .. py:attribute:: nidigital.Session.sites[]

        If no prefix is added to the items in the parameter, the correct prefix will be added when
        the driver function call is made.

        .. code:: python

            session.sites['0-2'].channel_enabled = True

        passes a string of :python:`'site0, site1, site2'` to the set attribute function.

        If an invalid repeated capability is passed to the driver, the driver will return an error.

        You can also explicitly use the prefix as part of the parameter, but it must be the correct prefix
        for the specific repeated capability.

        .. code:: python

            session.sites['site0-site2'].channel_enabled = True

        passes a string of :python:`'site0, site1, site2'` to the set attribute function.


rio_events
----------

    .. py:attribute:: nidigital.Session.rio_events[]

        If no prefix is added to the items in the parameter, the correct prefix will be added when
        the driver function call is made.

        .. code:: python

            session.rio_events['0-2'].channel_enabled = True

        passes a string of :python:`'RIOEvent0, RIOEvent1, RIOEvent2'` to the set attribute function.

        If an invalid repeated capability is passed to the driver, the driver will return an error.

        You can also explicitly use the prefix as part of the parameter, but it must be the correct prefix
        for the specific repeated capability.

        .. code:: python

            session.rio_events['RIOEvent0-RIOEvent2'].channel_enabled = True

        passes a string of :python:`'RIOEvent0, RIOEvent1, RIOEvent2'` to the set attribute function.


rio_triggers
------------

    .. py:attribute:: nidigital.Session.rio_triggers[]

        If no prefix is added to the items in the parameter, the correct prefix will be added when
        the driver function call is made.

        .. code:: python

            session.rio_triggers['0-2'].channel_enabled = True

        passes a string of :python:`'RIOTrigger0, RIOTrigger1, RIOTrigger2'` to the set attribute function.

        If an invalid repeated capability is passed to the driver, the driver will return an error.

        You can also explicitly use the prefix as part of the parameter, but it must be the correct prefix
        for the specific repeated capability.

        .. code:: python

            session.rio_triggers['RIOTrigger0-RIOTrigger2'].channel_enabled = True

        passes a string of :python:`'RIOTrigger0, RIOTrigger1, RIOTrigger2'` to the set attribute function.
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nidigital/status.inc sha256=0061287add0ee880e18dcfcefae65ad1d33538e5bc87ff9beebdce500e03383e bytes=2244 -->
## FILE: docs/nidigital/status.inc

- repository: `ni/nimi-python`
- source_path: `docs/nidigital/status.inc`
- sha256: `0061287add0ee880e18dcfcefae65ad1d33538e5bc87ff9beebdce500e03383e`
- bytes: 2244

````text

NI-Digital Pattern Driver Python API Status
-------------------------------------------

+---------------------------------------+--------------------------+
| NI-Digital Pattern Driver (nidigital) |                          |
+=======================================+==========================+
| Driver Version Tested Against         | 2025 Q4                  |
+---------------------------------------+--------------------------+
| PyPI Version                          | |nidigitalLatestVersion| |
+---------------------------------------+--------------------------+
| Supported Python Version              | |nidigitalPythonVersion| |
+---------------------------------------+--------------------------+
| Documentation                         | |nidigitalDocs|          |
+---------------------------------------+--------------------------+
| Open Issues                           | |nidigitalOpenIssues|    |
+---------------------------------------+--------------------------+
| Open Pull Requests                    | |nidigitalOpenPRs|       |
+---------------------------------------+--------------------------+


.. |nidigitalLatestVersion| image:: http://img.shields.io/pypi/v/nidigital.svg
    :alt: Latest NI-Digital Pattern Driver Version
    :target: http://pypi.python.org/pypi/nidigital


.. |nidigitalPythonVersion| image:: http://img.shields.io/pypi/pyversions/nidigital.svg
    :alt: NI-Digital Pattern Driver supported Python versions
    :target: http://pypi.python.org/pypi/nidigital


.. |nidigitalDocs| image:: https://readthedocs.org/projects/nidigital/badge/?version=latest
    :alt: NI-Digital Pattern Driver Python API Documentation Status
    :target: https://nidigital.readthedocs.io/en/latest


.. |nidigitalOpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python/nidigital.svg
    :alt: Open Issues + Pull Requests for NI-Digital Pattern Driver
    :target: https://github.com/ni/nimi-python/issues?q=is%3Aopen+is%3Aissue+label%3Anidigital


.. |nidigitalOpenPRs| image:: https://img.shields.io/github/issues-pr/ni/nimi-python/nidigital.svg
    :alt: Pull Requests for NI-Digital Pattern Driver
    :target: https://github.com/ni/nimi-python/pulls?q=is%3Aopen+is%3Aissue+label%3Anidigital
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nidigital/toc.inc sha256=4958d5597b4005305d15cdc9a09014d5afa552d460451b042172b99069952975 bytes=121 -->
## FILE: docs/nidigital/toc.inc

- repository: `ni/nimi-python`
- source_path: `docs/nidigital/toc.inc`
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

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nidmm/.readthedocs.yaml sha256=d1504c920d8909002eaab2daf4dfae62d5d914e8197497d9e1f76783a03f5882 bytes=1873 -->
## FILE: docs/nidmm/.readthedocs.yaml

- repository: `ni/nimi-python`
- source_path: `docs/nidmm/.readthedocs.yaml`
- sha256: `d1504c920d8909002eaab2daf4dfae62d5d914e8197497d9e1f76783a03f5882`
- bytes: 1873

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
      # Cancel building pull requests when there aren't changes in any of these paths: docs/_static/ docs/nidmm/.
      #
      # If there are no changes (git diff exits with 0) we force the command to return with 183.
      # This is a special exit code on Read the Docs that will cancel the build immediately.
      - |
        if [ "$READTHEDOCS_VERSION_TYPE" = "external" ] && git diff --quiet origin/master -- docs/_static/ docs/nidmm/;
        then
          exit 183;
        fi

# Have Read the Docs build documentation with Sphinx
sphinx:
  builder: html
  configuration: docs/nidmm/conf.py

# If using Sphinx, optionally build your docs in additional formats such as PDF
formats:
  - epub
  - pdf

# Declare the Python requirements required to build your docs
python:
  install:
  - requirements: docs/requirements.txt
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nidmm/about_nidmm.inc sha256=317c6bc8e097c6d94f897f7f607ba2d43be89e91f89e7c0b6dcab369c5dd5c21 bytes=480 -->
## FILE: docs/nidmm/about_nidmm.inc

- repository: `ni/nimi-python`
- source_path: `docs/nidmm/about_nidmm.inc`
- sha256: `317c6bc8e097c6d94f897f7f607ba2d43be89e91f89e7c0b6dcab369c5dd5c21`
- bytes: 480

````text
.. _about-section:

About
=====

The **nidmm** module provides a Python API for NI-DMM. The code is maintained in the Open Source repository for `nimi-python <https://github.com/ni/nimi-python>`_.

Support Policy
--------------
**nidmm** supports all the Operating Systems supported by NI-DMM.

It follows `Python Software Foundation <https://devguide.python.org/#status-of-python-branches>`_ support policy for different versions of CPython.

NI created and supports **nidmm**.
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nidmm/class.rst sha256=c122924aadceab03b6442e584a3a3a3a9e3e05e6edd9a5cfa60da6ea11aebb5c bytes=145699 -->
## FILE: docs/nidmm/class.rst

- repository: `ni/nimi-python`
- source_path: `docs/nidmm/class.rst`
- sha256: `c122924aadceab03b6442e584a3a3a3a9e3e05e6edd9a5cfa60da6ea11aebb5c`
- bytes: 145699

````rst
.. py:module:: nidmm

Session
=======

.. py:class:: Session(self, resource_name, id_query=False, reset_device=False, options={}, *, grpc_options=None)

    

    This method completes the following tasks:

    -  Creates a new IVI instrument driver session and, optionally, sets the
       initial state of the following session properties:
       :py:attr:`nidmm.Session.RANGE_CHECK`, :py:attr:`nidmm.Session.QUERY_INSTR_STATUS`,
       :py:attr:`nidmm.Session.CACHE`, :py:attr:`nidmm.Session.simulate`,
       :py:attr:`nidmm.Session.RECORD_COERCIONS`.
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

    

    .. note:: One or more of the referenced properties are not in the Python API for this driver.



    :param resource_name:
        

        .. caution:: All IVI names for the **Resource_Name**, such as logical names or
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

        


    :type resource_name: str

    :param id_query:
        

        Verifies that the device you initialize is one that the driver supports.
        NI-DMM automatically performs this query, so setting this parameter is
        not necessary.
        Defined Values:

        +----------------+---+------------------+
        | True (default) | 1 | Perform ID Query |
        +----------------+---+------------------+
        | False          | 0 | Skip ID Query    |
        +----------------+---+------------------+


    :type id_query: bool

    :param reset_device:
        

        Specifies whether to reset the instrument during the initialization
        procedure.
        Defined Values:

        +----------------+---+--------------+
        | True (default) | 1 | Reset Device |
        +----------------+---+--------------+
        | False          | 0 | Don't Reset  |
        +----------------+---+--------------+


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

        


    :type grpc_options: nidmm.GrpcSessionOptions


Methods
=======

abort
-----

    .. py:currentmodule:: nidmm.Session

    .. py:method:: abort()

            Aborts a previously initiated measurement and returns the DMM to the
            Idle state.

            



close
-----

    .. py:currentmodule:: nidmm.Session

    .. py:method:: close()

            Closes the specified session and deallocates resources that it reserved.

            

            .. note:: This method is not needed when using the session context manager



configure_measurement_absolute
------------------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: configure_measurement_absolute(measurement_function, range, resolution_absolute)

            Configures the common properties of the measurement. These properties
            include :py:attr:`nidmm.Session.method`, :py:attr:`nidmm.Session.range`, and
            :py:attr:`nidmm.Session.resolution_absolute`.

            



            :param measurement_function:


                Specifies the **measurement_function** used to acquire the measurement.
                The driver sets :py:attr:`nidmm.Session.method` to this value.

                


            :type measurement_function: :py:data:`nidmm.Function`
            :param range:


                Specifies the **range** for the method specified in the
                **Measurement_Function** parameter. When frequency is specified in the
                **Measurement_Function** parameter, you must supply the minimum
                frequency expected in the **range** parameter. For example, you must
                type in 100 Hz if you are measuring 101 Hz or higher.
                For all other methods, you must supply a **range** that exceeds the
                value that you are measuring. For example, you must type in 10 V if you
                are measuring 9 V. **range** values are coerced up to the closest input
                **range**. Refer to the `Devices
                Overview <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__ for a list of valid
                ranges. The driver sets :py:attr:`nidmm.Session.range` to this value. The default is
                0.02 V.

                +---------------------------------------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_ON`   | -1.0 | NI-DMM performs an Auto Range before acquiring the measurement.                                                                                                                                                  |
                +---------------------------------------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_OFF`  | -2.0 | NI-DMM sets the Range to the current :py:attr:`nidmm.Session.auto_range_value` and uses this range for all subsequent measurements until the measurement configuration is changed.                               |
                +---------------------------------------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_ONCE` | -3.0 | NI-DMM performs an Auto Range before acquiring the measurement. The :py:attr:`nidmm.Session.auto_range_value` is stored and used for all subsequent measurements until the measurement configuration is changed. |
                +---------------------------------------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

                .. note:: The NI 4050, NI 4060, and NI 4065 only support Auto Range when the
                    trigger and sample trigger are set to IMMEDIATE.

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type range: float
            :param resolution_absolute:


                Specifies the absolute resolution for the measurement. NI-DMM sets
                :py:attr:`nidmm.Session.resolution_absolute` to this value. The PXIe-4080/4081/4082
                uses the resolution you specify. The NI 4065 and NI 4070/4071/4072
                ignore this parameter when the **Range** parameter is set to
                :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_ON` (-1.0) or :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_ONCE`
                (-3.0). The default is 0.001 V.

                

                .. note:: NI-DMM ignores this parameter for capacitance and inductance
                    measurements on the NI 4072. To achieve better resolution for such
                    measurements, use the :py:attr:`nidmm.Session.lc_number_meas_to_average`
                    property.

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type resolution_absolute: float

configure_measurement_digits
----------------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: configure_measurement_digits(measurement_function, range, resolution_digits)

            Configures the common properties of the measurement. These properties
            include :py:attr:`nidmm.Session.method`, :py:attr:`nidmm.Session.range`, and
            :py:attr:`nidmm.Session.resolution_digits`.

            



            :param measurement_function:


                Specifies the **measurement_function** used to acquire the measurement.
                The driver sets :py:attr:`nidmm.Session.method` to this value.

                


            :type measurement_function: :py:data:`nidmm.Function`
            :param range:


                Specifies the range for the method specified in the
                **Measurement_Function** parameter. When frequency is specified in the
                **Measurement_Function** parameter, you must supply the minimum
                frequency expected in the **range** parameter. For example, you must
                type in 100 Hz if you are measuring 101 Hz or higher.
                For all other methods, you must supply a range that exceeds the value
                that you are measuring. For example, you must type in 10 V if you are
                measuring 9 V. range values are coerced up to the closest input range.
                Refer to the `Devices
                Overview <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__ for a list of valid
                ranges. The driver sets :py:attr:`nidmm.Session.range` to this value. The default is
                0.02 V.

                +---------------------------------------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_ON`   | -1.0 | NI-DMM performs an Auto Range before acquiring the measurement.                                                                                                                                                  |
                +---------------------------------------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_OFF`  | -2.0 | NI-DMM sets the Range to the current :py:attr:`nidmm.Session.auto_range_value` and uses this range for all subsequent measurements until the measurement configuration is changed.                               |
                +---------------------------------------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_ONCE` | -3.0 | NI-DMM performs an Auto Range before acquiring the measurement. The :py:attr:`nidmm.Session.auto_range_value` is stored and used for all subsequent measurements until the measurement configuration is changed. |
                +---------------------------------------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

                .. note:: The NI 4050, NI 4060, and NI 4065 only support Auto Range when the
                    trigger and sample trigger are set to IMMEDIATE.

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type range: float
            :param resolution_digits:


                Specifies the resolution of the measurement in digits. The driver sets
                the `Devices Overview <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__ for a
                list of valid ranges. The driver sets :py:attr:`nidmm.Session.resolution_digits`
                property to this value. The PXIe-4080/4081/4082 uses the resolution you
                specify. The NI 4065 and NI 4070/4071/4072 ignore this parameter when
                the **Range** parameter is set to :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_ON` (-1.0) or
                :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_ONCE` (-3.0). The default is 5½.

                

                .. note:: NI-DMM ignores this parameter for capacitance and inductance
                    measurements on the NI 4072. To achieve better resolution for such
                    measurements, use the :py:attr:`nidmm.Session.lc_number_meas_to_average`
                    property.

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type resolution_digits: float

configure_multi_point
---------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: configure_multi_point(trigger_count, sample_count, sample_trigger=nidmm.SampleTrigger.IMMEDIATE, sample_interval=hightime.timedelta(seconds=-1))

            Configures the properties for multipoint measurements. These properties
            include :py:attr:`nidmm.Session.trigger_count`, :py:attr:`nidmm.Session.sample_count`,
            :py:attr:`nidmm.Session.sample_trigger`, and :py:attr:`nidmm.Session.sample_interval`.

            For continuous acquisitions, set :py:attr:`nidmm.Session.trigger_count` or
            :py:attr:`nidmm.Session.sample_count` to zero. For more information, refer to
            `Multiple Point
            Acquisitions <REPLACE_DRIVER_SPECIFIC_URL_1(multi_point)>`__,
            `Triggering <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__, and `Using
            Switches <REPLACE_DRIVER_SPECIFIC_URL_1(switch_selection)>`__.

            



            :param trigger_count:


                Sets the number of triggers you want the DMM to receive before returning
                to the Idle state. The driver sets :py:attr:`nidmm.Session.trigger_count` to this
                value. The default value is 1.

                


            :type trigger_count: int
            :param sample_count:


                Sets the number of measurements the DMM makes in each measurement
                sequence initiated by a trigger. The driver sets
                :py:attr:`nidmm.Session.sample_count` to this value. The default value is 1.

                


            :type sample_count: int
            :param sample_trigger:


                Specifies the **sample_trigger** source you want to use. The driver
                sets :py:attr:`nidmm.Session.sample_trigger` to this value. The default is
                Immediate.

                

                .. note:: To determine which values are supported by each device, refer to the
                    `LabWindows/CVI Trigger
                    Routing <REPLACE_DRIVER_SPECIFIC_URL_1(cvitrigger_routing)>`__ section.


            :type sample_trigger: :py:data:`nidmm.SampleTrigger`
            :param sample_interval:


                Sets the amount of time in seconds the DMM waits between measurement
                cycles. The driver sets :py:attr:`nidmm.Session.sample_interval` to this value.
                Specify a sample interval to add settling time between measurement
                cycles or to decrease the measurement rate. **sample_interval** only
                applies when the **Sample_Trigger** is set to INTERVAL.

                On the NI 4060, the **sample_interval** value is used as the settling
                time. When sample interval is set to 0, the DMM does not settle between
                measurement cycles. The NI 4065 and NI 4070/4071/4072 use the value
                specified in **sample_interval** as additional delay. The default value
                (-1) ensures that the DMM settles for a recommended time. This is the
                same as using an Immediate trigger.

                

                .. note:: This property is not used on the NI 4080/4081/4082 and the NI 4050.


            :type sample_interval: hightime.timedelta, datetime.timedelta, or float in seconds

configure_rtd_custom
--------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: configure_rtd_custom(rtd_a, rtd_b, rtd_c)

            Configures the A, B, and C parameters for a custom RTD.

            



            :param rtd_a:


                Specifies the Callendar-Van Dusen A coefficient for RTD scaling when RTD
                Type parameter is set to Custom in the :py:meth:`nidmm.Session.configure_rtd_type` method.
                The default is 3.9083e-3 (Pt3851)

                


            :type rtd_a: float
            :param rtd_b:


                Specifies the Callendar-Van Dusen B coefficient for RTD scaling when RTD
                Type parameter is set to Custom in the :py:meth:`nidmm.Session.configure_rtd_type` method.
                The default is -5.775e-7 (Pt3851).

                


            :type rtd_b: float
            :param rtd_c:


                Specifies the Callendar-Van Dusen C coefficient for RTD scaling when RTD
                Type parameter is set to Custom in the :py:meth:`nidmm.Session.configure_rtd_type` method.
                The default is -4.183e-12 (Pt3851).

                


            :type rtd_c: float

configure_rtd_type
------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: configure_rtd_type(rtd_type, rtd_resistance)

            Configures the RTD Type and RTD Resistance parameters for an RTD.

            



            :param rtd_type:


                Specifies the type of RTD used to measure the temperature resistance.
                NI-DMM uses this value to set the RTD Type property. The default is
                :py:data:`~nidmm.RTDType.PT3851`.

                +----------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | Enum                             | Standards                                     | Material | TCR (α) | Typical R\ :sub:`0` (Ω) | Notes                                                                         |                               |
                +==================================+===============================================+==========+=========+=========================+===============================================================================+===============================+
                | Callendar-Van Dusen Coefficient  |                                               |          |         |                         |                                                                               |                               |
                +----------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | :py:data:`~nidmm.RTDType.PT3851` | IEC-751 DIN 43760 BS 1904 ASTM-E1137 EN-60751 | Platinum | .003851 | 100 Ω 1000 Ω            | A = 3.9083 × 10\ :sup:`–3` B = –5.775×10:sup:`–7` C = –4.183×10:sup:`–12`     | Most common RTDs              |
                +----------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | :py:data:`~nidmm.RTDType.PT3750` | Low-cost vendor compliant RTD\*               | Platinum | .003750 | 1000 Ω                  | A = 3.81 × 10\ :sup:`–3` B = –6.02×10:sup:`–7` C = –6.0×10:sup:`–12`          | Low-cost RTD                  |
                +----------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | :py:data:`~nidmm.RTDType.PT3916` | JISC 1604                                     | Platinum | .003916 | 100 Ω                   | A = 3.9739 × 10\ :sup:`–3` B = –5.870×10:sup:`–7` C = –4.4 ×10\ :sup:`–12`    | Used in primarily in Japan    |
                +----------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | :py:data:`~nidmm.RTDType.PT3920` | US Industrial Standard D-100 American         | Platinum | .003920 | 100 Ω                   | A = 3.9787 × 10\ :sup:`–3` B = –5.8686×10:sup:`–7` C = –4.167 ×10\ :sup:`–12` | Low-cost RTD                  |
                +----------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | :py:data:`~nidmm.RTDType.PT3911` | US Industrial Standard American               | Platinum | .003911 | 100 Ω                   | A = 3.9692 × 10\ :sup:`–3` B = –5.8495×10:sup:`–7` C = –4.233 ×10\ :sup:`–12` | Low-cost RTD                  |
                +----------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | :py:data:`~nidmm.RTDType.PT3928` | ITS-90                                        | Platinum | .003928 | 100 Ω                   | A = 3.9888 × 10\ :sup:`–3` B = –5.915×10:sup:`–7` C = –3.85 ×10\ :sup:`–12`   | The definition of temperature |
                +----------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
                | \*No standard. Check the TCR.    |                                               |          |         |                         |                                                                               |                               |
                +----------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+


            :type rtd_type: :py:data:`nidmm.RTDType`
            :param rtd_resistance:


                Specifies the RTD resistance in ohms at 0 °C. NI-DMM uses this value to
                set the RTD Resistance property. The default is 100 (Ω).

                


            :type rtd_resistance: float

configure_thermistor_custom
---------------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: configure_thermistor_custom(thermistor_a, thermistor_b, thermistor_c)

            Configures the A, B, and C parameters for a custom thermistor.

            



            :param thermistor_a:


                Specifies the Steinhart-Hart A coefficient for thermistor scaling when
                Thermistor Type is set to Custom in the :py:meth:`nidmm.Session.ConfigureThermistorType`
                method. The default is 1.0295e-3 (44006).

                

                .. note:: One or more of the referenced methods are not in the Python API for this driver.


            :type thermistor_a: float
            :param thermistor_b:


                Specifies the Steinhart-Hart B coefficient for thermistor scaling when
                Thermistor Type is set to Custom in the :py:meth:`nidmm.Session.ConfigureThermistorType`
                method. The default is 2.391e-4 (44006).

                

                .. note:: One or more of the referenced methods are not in the Python API for this driver.


            :type thermistor_b: float
            :param thermistor_c:


                Specifies the Steinhart-Hart C coefficient for thermistor scaling when
                Thermistor Type is set to Custom in the :py:meth:`nidmm.Session.ConfigureThermistorType`
                method. The default is 1.568e-7 (44006).

                

                .. note:: One or more of the referenced methods are not in the Python API for this driver.


            :type thermistor_c: float

configure_thermocouple
----------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: configure_thermocouple(thermocouple_type, reference_junction_type=nidmm.ThermocoupleReferenceJunctionType.FIXED)

            Configures the thermocouple type and reference junction type for a
            chosen thermocouple.

            



            :param thermocouple_type:


                Specifies the type of thermocouple used to measure the temperature.
                NI-DMM uses this value to set the Thermocouple Type property. The
                default is :py:data:`~nidmm.ThermocoupleType.J`.

                +--------------------------------------+---------------------+
                | :py:data:`~nidmm.ThermocoupleType.B` | Thermocouple type B |
                +--------------------------------------+---------------------+
                | :py:data:`~nidmm.ThermocoupleType.E` | Thermocouple type E |
                +--------------------------------------+---------------------+
                | :py:data:`~nidmm.ThermocoupleType.J` | Thermocouple type J |
                +--------------------------------------+---------------------+
                | :py:data:`~nidmm.ThermocoupleType.K` | Thermocouple type K |
                +--------------------------------------+---------------------+
                | :py:data:`~nidmm.ThermocoupleType.N` | Thermocouple type N |
                +--------------------------------------+---------------------+
                | :py:data:`~nidmm.ThermocoupleType.R` | Thermocouple type R |
                +--------------------------------------+---------------------+
                | :py:data:`~nidmm.ThermocoupleType.S` | Thermocouple type S |
                +--------------------------------------+---------------------+
                | :py:data:`~nidmm.ThermocoupleType.T` | Thermocouple type T |
                +--------------------------------------+---------------------+


            :type thermocouple_type: :py:data:`nidmm.ThermocoupleType`
            :param reference_junction_type:


                Specifies the type of reference junction to be used in the reference
                junction compensation of a thermocouple measurement. NI-DMM uses this
                value to set the Reference Junction Type property. The only supported
                value is :py:data:`~nidmm.ThermocoupleReferenceJunctionType.FIXED`.

                


            :type reference_junction_type: :py:data:`nidmm.ThermocoupleReferenceJunctionType`

configure_trigger
-----------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: configure_trigger(trigger_source, trigger_delay=hightime.timedelta(seconds=-1))

            Configures the DMM **Trigger_Source** and **Trigger_Delay**. Refer to
            `Triggering <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__ and `Using
            Switches <REPLACE_DRIVER_SPECIFIC_URL_1(switch_selection)>`__ for more
            information.

            



            :param trigger_source:


                Specifies the **trigger_source** that initiates the acquisition. The
                driver sets :py:attr:`nidmm.Session.trigger_source` to this value. Software
                configures the DMM to wait until :py:meth:`nidmm.Session.send_software_trigger` is called
                before triggering the DMM.

                

                .. note:: To determine which values are supported by each device, refer to the
                    `LabWindows/CVI Trigger
                    Routing <REPLACE_DRIVER_SPECIFIC_URL_1(cvitrigger_routing)>`__ section.


            :type trigger_source: :py:data:`nidmm.TriggerSource`
            :param trigger_delay:


                Specifies the time that the DMM waits after it has received a trigger
                before taking a measurement. The driver sets the
                :py:attr:`nidmm.Session.trigger_delay` property to this value. By default,
                **trigger_delay** is :py:data:`~nidmm.NIDMM_VAL_AUTO_DELAY` (-1), which means the DMM
                waits an appropriate settling time before taking the measurement. On the
                NI 4060, if you set **trigger_delay** to 0, the DMM does not settle
                before taking the measurement. The NI 4065 and NI 4070/4071/4072 use the
                value specified in **trigger_delay** as additional settling time.

                

                .. note:: When using the NI 4050, **Trigger_Delay** must be set to
                    :py:data:`~nidmm.NIDMM_VAL_AUTO_DELAY` (-1).

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type trigger_delay: hightime.timedelta, datetime.timedelta, or float in seconds

configure_waveform_acquisition
------------------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: configure_waveform_acquisition(measurement_function, range, rate, waveform_points)

            Configures the DMM for waveform acquisitions. This feature is supported
            on the NI 4080/4081/4082 and the NI 4070/4071/4072.

            



            :param measurement_function:


                Specifies the **measurement_function** used in a waveform acquisition.
                The driver sets :py:attr:`nidmm.Session.method` to this value.

                +-----------------------------------------------------+------+------------------+
                | :py:data:`~nidmm.Method.WAVEFORM_VOLTAGE` (default) | 1003 | Voltage Waveform |
                +-----------------------------------------------------+------+------------------+
                | :py:data:`~nidmm.Method.WAVEFORM_CURRENT`           | 1004 | Current Waveform |
                +-----------------------------------------------------+------+------------------+


            :type measurement_function: :py:data:`nidmm.Function`
            :param range:


                Specifies the expected maximum amplitude of the input signal and sets
                the **range** for the **Measurement_Function**. NI-DMM sets
                :py:attr:`nidmm.Session.range` to this value. **range** values are coerced up to the
                closest input **range**. The default is 10.0.

                For valid ranges refer to the topics in
                `Devices <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__.

                Auto-ranging is not supported during waveform acquisitions.

                


            :type range: float
            :param rate:


                Specifies the **rate** of the acquisition in samples per second. NI-DMM
                sets :py:attr:`nidmm.Session.waveform_rate` to this value.

                The valid **Range** is 10.0–1,800,000 S/s. **rate** values are coerced
                to the closest integer divisor of 1,800,000. The default value is
                1,800,000.

                


            :type rate: float
            :param waveform_points:


                Specifies the number of points to acquire before the waveform
                acquisition completes. NI-DMM sets :py:attr:`nidmm.Session.waveform_points` to this
                value.

                To calculate the maximum and minimum number of waveform points that you
                can acquire in one acquisition, refer to the `Waveform Acquisition
                Measurement Cycle <REPLACE_DRIVER_SPECIFIC_URL_1(waveform_cycle)>`__.

                The default value is 500.

                


            :type waveform_points: int

disable
-------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: disable()

            Places the instrument in a quiescent state where it has minimal or no
            impact on the system to which it is connected. If a measurement is in
            progress when this method is called, the measurement is aborted.

            



export_attribute_configuration_buffer
-------------------------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: export_attribute_configuration_buffer()

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

            

            .. note:: Not supported on the PCMCIA‑4050 or the PXI/PCI‑4060.



            :rtype: bytes
            :return:


                    Specifies the byte array buffer to be populated with the exported
                    property configuration.

                    



export_attribute_configuration_file
-----------------------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: export_attribute_configuration_file(file_path)

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

            

            .. note:: Not supported on the PCMCIA‑4050 or the PXI/PCI‑4060.



            :param file_path:


                Specifies the absolute path to the file to contain the exported
                property configuration. If you specify an empty or relative path, this
                method returns an error.
                **Default file extension:**\  .nidmmconfig

                


            :type file_path: str

fetch
-----

    .. py:currentmodule:: nidmm.Session

    .. py:method:: fetch(maximum_time=hightime.timedelta(milliseconds=-1))

            Returns the value from a previously initiated measurement. You must call
            :py:meth:`nidmm.Session._initiate` before calling this method. Value is in base units.

            



            :param maximum_time:


                Specifies the **maximum_time** allowed for this method to complete in
                milliseconds. If the method does not complete within this time
                interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                :py:data:`~nidmm.NIDMM_VAL_TIME_LIMIT_AUTO` (-1). The DMM calculates the timeout
                automatically.

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type maximum_time: hightime.timedelta, datetime.timedelta, or int in milliseconds

            :rtype: float
            :return:


                    The measured value returned from the DMM.

                    



fetch_multi_point
-----------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: fetch_multi_point(array_size, maximum_time=hightime.timedelta(milliseconds=-1))

            Returns an array of values from a previously initiated multipoint
            measurement. The number of measurements the DMM makes is determined by
            the values you specify for the **Trigger_Count** and **Sample_Count**
            parameters of :py:meth:`nidmm.Session.configure_multi_point`. You must first call
            :py:meth:`nidmm.Session._initiate` to initiate a measurement before calling this method. Values are in base units.

            



            :param array_size:


                Specifies the number of measurements to acquire. The maximum number of
                measurements for a finite acquisition is the (**Trigger Count** x
                **Sample Count**) parameters in :py:meth:`nidmm.Session.configure_multi_point`.

                For continuous acquisitions, up to 100,000 points can be returned at
                once. The number of measurements can be a subset. The valid range is any
                positive ViInt32. The default value is 1.

                


            :type array_size: int
            :param maximum_time:


                Specifies the **maximum_time** allowed for this method to complete in
                milliseconds. If the method does not complete within this time
                interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                :py:data:`~nidmm.NIDMM_VAL_TIME_LIMIT_AUTO` (-1). The DMM calculates the timeout
                automatically.

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type maximum_time: hightime.timedelta, datetime.timedelta, or int in milliseconds

            :rtype: array.array("d")
            :return:


                    An array of measurement values.

                    

                    .. note:: The size of the **Reading_Array** must be at least the size that you
                        specify for the **Array_Size** parameter.



fetch_waveform
--------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: fetch_waveform(array_size, maximum_time=hightime.timedelta(milliseconds=-1))

            For the NI 4080/4081/4082 and the NI 4070/4071/4072, returns an array of
            values from a previously initiated waveform acquisition. You must call
            :py:meth:`nidmm.Session._initiate` before calling this method.

            



            :param array_size:


                Specifies the number of waveform points to return. You specify the total
                number of points that the DMM acquires in the **Waveform Points**
                parameter of :py:meth:`nidmm.Session.configure_waveform_acquisition`. The default value is
                1.

                


            :type array_size: int
            :param maximum_time:


                Specifies the **maximum_time** allowed for this method to complete in
                milliseconds. If the method does not complete within this time
                interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                :py:data:`~nidmm.NIDMM_VAL_TIME_LIMIT_AUTO` (-1). The DMM calculates the timeout
                automatically.

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type maximum_time: hightime.timedelta, datetime.timedelta, or int in milliseconds

            :rtype: array.array("d")
            :return:


                    **Waveform Array** is an array of measurement values stored in waveform
                    data type.

                    



fetch_waveform_into
-------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: fetch_waveform_into(array_size, maximum_time=hightime.timedelta(milliseconds=-1))

            For the NI 4080/4081/4082 and the NI 4070/4071/4072, returns an array of
            values from a previously initiated waveform acquisition. You must call
            :py:meth:`nidmm.Session._initiate` before calling this method.

            



            :param waveform_array:


                **Waveform Array** is an array of measurement values stored in waveform
                data type.

                


            :type waveform_array: numpy.array(dtype=numpy.float64)
            :param maximum_time:


                Specifies the **maximum_time** allowed for this method to complete in
                milliseconds. If the method does not complete within this time
                interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                :py:data:`~nidmm.NIDMM_VAL_TIME_LIMIT_AUTO` (-1). The DMM calculates the timeout
                automatically.

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type maximum_time: hightime.timedelta, datetime.timedelta, or int in milliseconds

get_cal_date_and_time
---------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: get_cal_date_and_time(cal_type)

            Returns the date and time of the last calibration performed.

            

            .. note:: The NI 4050 and NI 4060 are not supported.



            :param cal_type:


                Specifies the type of calibration performed (external or self-calibration).

                +-----------------------------------------------------+---+----------------------+
                | :py:data:`~nidmm.NIDMM_VAL_INTERNAL_AREA` (default) | 0 | Self-Calibration     |
                +-----------------------------------------------------+---+----------------------+
                | :py:data:`~nidmm.NIDMM_VAL_EXTERNAL_AREA`           | 1 | External Calibration |
                +-----------------------------------------------------+---+----------------------+

                .. note:: The NI 4065 does not support self-calibration.

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type cal_type: int

            :rtype: hightime.datetime
            :return:


                    Indicates date and time of the last calibration.

                    



get_dev_temp
------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: get_dev_temp(options="")

            Returns the current **Temperature** of the device.

            

            .. note:: The NI 4050 and NI 4060 are not supported.



            :param options:


                Reserved.

                


            :type options: str

            :rtype: float
            :return:


                    Returns the current **temperature** of the device.

                    



get_ext_cal_recommended_interval
--------------------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: get_ext_cal_recommended_interval()

            Returns the recommended interval between external recalibration in
            **Months**.

            

            .. note:: The NI 4050 and NI 4060 are not supported.



            :rtype: hightime.timedelta
            :return:


                    Returns the recommended number of **months** between external
                    calibrations.

                    



get_last_cal_temp
-----------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: get_last_cal_temp(cal_type)

            Returns the **Temperature** during the last calibration procedure.

            

            .. note:: The NI 4050 and NI 4060 are not supported.



            :param cal_type:


                Specifies the type of calibration performed (external or
                self-calibration).

                +-----------------------------------------------------+---+----------------------+
                | :py:data:`~nidmm.NIDMM_VAL_INTERNAL_AREA` (default) | 0 | Self-Calibration     |
                +-----------------------------------------------------+---+----------------------+
                | :py:data:`~nidmm.NIDMM_VAL_EXTERNAL_AREA`           | 1 | External Calibration |
                +-----------------------------------------------------+---+----------------------+

                .. note:: The NI 4065 does not support self-calibration.

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type cal_type: int

            :rtype: float
            :return:


                    Returns the **temperature** during the last calibration.

                    



get_self_cal_supported
----------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: get_self_cal_supported()

            Returns a Boolean value that expresses whether or not the DMM that you
            are using can perform self-calibration.

            



            :rtype: bool
            :return:


                    Returns whether Self Cal is supported for the device specified by the
                    given session.

                    +-------+---+-------------------------------------------------------------+
                    | True  | 1 | The DMM that you are using can perform self-calibration.    |
                    +-------+---+-------------------------------------------------------------+
                    | False | 0 | The DMM that you are using cannot perform self-calibration. |
                    +-------+---+-------------------------------------------------------------+



import_attribute_configuration_buffer
-------------------------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: import_attribute_configuration_buffer(configuration)

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

            

            .. note:: Not supported on the PCMCIA‑4050 or the PXI/PCI‑4060.



            :param configuration:


                Specifies the byte array buffer that contains the property
                configuration to import.

                


            :type configuration: bytes

import_attribute_configuration_file
-----------------------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: import_attribute_configuration_file(file_path)

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

            

            .. note:: Not supported on the PCMCIA‑4050 or the PXI/PCI‑4060.



            :param file_path:


                Specifies the absolute path to the file containing the property
                configuration to import. If you specify an empty or relative path, this
                method returns an error.
                **Default File Extension:**\  .nidmmconfig

                


            :type file_path: str

initiate
--------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: initiate()

            Initiates an acquisition. After you call this method, the DMM leaves
            the Idle state and enters the Wait-for-Trigger state. If trigger is set
            to Immediate mode, the DMM begins acquiring measurement data. Use
            :py:meth:`nidmm.Session.fetch`, :py:meth:`nidmm.Session.fetch_multi_point`, or :py:meth:`nidmm.Session.fetch_waveform` to
            retrieve the measurement data.

            

            .. note:: This method will return a Python context manager that will initiate on entering and abort on exit.



lock
----

    .. py:currentmodule:: nidmm.Session

.. py:method:: lock()

    Obtains a multithread lock on the device session. Before doing so, the
    software waits until all other execution threads release their locks
    on the device session.

    Other threads may have obtained a lock on this session for the
    following reasons:

        -  The application called the :py:meth:`nidmm.Session.lock` method.
        -  A call to NI-DMM locked the session.
        -  After a call to the :py:meth:`nidmm.Session.lock` method returns
           successfully, no other threads can access the device session until
           you call the :py:meth:`nidmm.Session.unlock` method or exit out of the with block when using
           lock context manager.
        -  Use the :py:meth:`nidmm.Session.lock` method and the
           :py:meth:`nidmm.Session.unlock` method around a sequence of calls to
           instrument driver methods if you require that the device retain its
           settings through the end of the sequence.

    You can safely make nested calls to the :py:meth:`nidmm.Session.lock` method
    within the same thread. To completely unlock the session, you must
    balance each call to the :py:meth:`nidmm.Session.lock` method with a call to
    the :py:meth:`nidmm.Session.unlock` method.

    One method for ensuring there are the same number of unlock method calls as there is lock calls
    is to use lock as a context manager

        .. code:: python

            with nidmm.Session('dev1') as session:
                with session.lock():
                    # Calls to session within a single lock context

        The first `with` block ensures the session is closed regardless of any exceptions raised

        The second `with` block ensures that unlock is called regardless of any exceptions raised

    :rtype: context manager
    :return:
        When used in a `with` statement, :py:meth:`nidmm.Session.lock` acts as
        a context manager and unlock will be called when the `with` block is exited

perform_open_cable_comp
-----------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: perform_open_cable_comp()

            For the NI 4082 and NI 4072 only, performs the open cable compensation
            measurements for the current capacitance/inductance range, and returns
            open cable compensation **Conductance** and **Susceptance** values. You
            can use the return values of this method as inputs to
            :py:meth:`nidmm.Session.ConfigureOpenCableCompValues`.

            This method returns an error if the value of the :py:attr:`nidmm.Session.method`
            property is not set to :py:data:`~nidmm.Method.CAPACITANCE` (1005) or
            :py:data:`~nidmm.Method.INDUCTANCE` (1006).

            

            .. note:: One or more of the referenced methods are not in the Python API for this driver.



            :rtype: tuple (conductance, susceptance)

                WHERE

                conductance (float): 


                    **conductance** is the measured value of open cable compensation
                    **conductance**.

                    


                susceptance (float): 


                    **susceptance** is the measured value of open cable compensation
                    **susceptance**.

                    



perform_short_cable_comp
------------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: perform_short_cable_comp()

            Performs the short cable compensation measurements for the current
            capacitance/inductance range, and returns short cable compensation
            **Resistance** and **Reactance** values. You can use the return values
            of this method as inputs to :py:meth:`nidmm.Session.ConfigureShortCableCompValues`.

            This method returns an error if the value of the :py:attr:`nidmm.Session.method`
            property is not set to :py:data:`~nidmm.Method.CAPACITANCE` (1005) or
            :py:data:`~nidmm.Method.INDUCTANCE` (1006).

            

            .. note:: One or more of the referenced methods are not in the Python API for this driver.



            :rtype: tuple (resistance, reactance)

                WHERE

                resistance (float): 


                    **resistance** is the measured value of short cable compensation
                    **resistance**.

                    


                reactance (float): 


                    **reactance** is the measured value of short cable compensation
                    **reactance**.

                    



read
----

    .. py:currentmodule:: nidmm.Session

    .. py:method:: read(maximum_time=hightime.timedelta(milliseconds=-1))

            Acquires a single measurement and returns the measured value in base units.

            



            :param maximum_time:


                Specifies the **maximum_time** allowed for this method to complete in
                milliseconds. If the method does not complete within this time
                interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                :py:data:`~nidmm.NIDMM_VAL_TIME_LIMIT_AUTO` (-1). The DMM calculates the timeout
                automatically.

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type maximum_time: hightime.timedelta, datetime.timedelta, or int in milliseconds

            :rtype: float
            :return:


                    The measured value returned from the DMM.

                    



read_multi_point
----------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: read_multi_point(array_size, maximum_time=hightime.timedelta(milliseconds=-1))

            Acquires multiple measurements and returns an array of measured values.
            The number of measurements the DMM makes is determined by the values you
            specify for the **Trigger_Count** and **Sample_Count** parameters in
            :py:meth:`nidmm.Session.configure_multi_point`.

            



            :param array_size:


                Specifies the number of measurements to acquire. The maximum number of
                measurements for a finite acquisition is the (**Trigger Count** x
                **Sample Count**) parameters in :py:meth:`nidmm.Session.configure_multi_point`.

                For continuous acquisitions, up to 100,000 points can be returned at
                once. The number of measurements can be a subset. The valid range is any
                positive ViInt32. The default value is 1.

                


            :type array_size: int
            :param maximum_time:


                Specifies the **maximum_time** allowed for this method to complete in
                milliseconds. If the method does not complete within this time
                interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                :py:data:`~nidmm.NIDMM_VAL_TIME_LIMIT_AUTO` (-1). The DMM calculates the timeout
                automatically.

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type maximum_time: hightime.timedelta, datetime.timedelta, or int in milliseconds

            :rtype: array.array("d")
            :return:


                    An array of measurement values.

                    

                    .. note:: The size of the **Reading_Array** must be at least the size that you
                        specify for the **Array_Size** parameter.



read_status
-----------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: read_status()

            Returns measurement backlog and acquisition status. Use this method to
            determine how many measurements are available before calling
            :py:meth:`nidmm.Session.fetch`, :py:meth:`nidmm.Session.fetch_multi_point`, or :py:meth:`nidmm.Session.fetch_waveform`.

            

            .. note:: The NI 4050 is not supported.



            :rtype: tuple (acquisition_backlog, acquisition_status)

                WHERE

                acquisition_backlog (int): 


                    The number of measurements available to be read. If the backlog
                    continues to increase, data is eventually overwritten, resulting in an
                    error.

                    

                    .. note:: On the NI 4060, the **Backlog** does not increase when autoranging. On
                        the NI 4065, the **Backlog** does not increase when Range is set to AUTO
                        RANGE ON (-1), or before the first point is fetched when Range is set to
                        AUTO RANGE ONCE (-3). These behaviors are due to the autorange model of
                        the devices.


                acquisition_status (:py:data:`nidmm.AcquisitionStatus`): 


                    Indicates status of the acquisition. The following table shows the
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



read_waveform
-------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: read_waveform(array_size, maximum_time=hightime.timedelta(milliseconds=-1))

            For the NI 4080/4081/4082 and the NI 4070/4071/4072, acquires a waveform
            and returns data as an array of values or as a waveform data type. The
            number of elements in the **Waveform_Array** is determined by the
            values you specify for the **Waveform_Points** parameter in
            :py:meth:`nidmm.Session.configure_waveform_acquisition`.

            



            :param array_size:


                Specifies the number of waveform points to return. You specify the total
                number of points that the DMM acquires in the **Waveform Points**
                parameter of :py:meth:`nidmm.Session.configure_waveform_acquisition`. The default value is
                1.

                


            :type array_size: int
            :param maximum_time:


                Specifies the **maximum_time** allowed for this method to complete in
                milliseconds. If the method does not complete within this time
                interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
                error code. This may happen if an external trigger has not been
                received, or if the specified timeout is not long enough for the
                acquisition to complete.

                The valid range is 0–86400000. The default value is
                :py:data:`~nidmm.NIDMM_VAL_TIME_LIMIT_AUTO` (-1). The DMM calculates the timeout
                automatically.

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type maximum_time: hightime.timedelta, datetime.timedelta, or int in milliseconds

            :rtype: array.array("d")
            :return:


                    An array of measurement values.

                    

                    .. note:: The size of the **Waveform_Array** must be at least the size that you
                        specify for the **Array_Size** parameter.



reset
-----

    .. py:currentmodule:: nidmm.Session

    .. py:method:: reset()

            Resets the instrument to a known state and sends initialization commands
            to the instrument. The initialization commands set instrument settings
            to the state necessary for the operation of the instrument driver.

            



reset_with_defaults
-------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: reset_with_defaults()

            Resets the instrument to a known state and sends initialization commands
            to the DMM. The initialization commands set the DMM settings to the
            state necessary for the operation of NI-DMM. All user-defined default
            values associated with a logical name are applied after setting the DMM.

            



self_cal
--------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: self_cal()

            For the NI 4080/4081/4082 and the NI 4070/4071/4072, executes the
            self-calibration routine to maintain measurement accuracy.

            

            .. note:: This method calls :py:meth:`nidmm.Session.reset`, and any configurations previous to
                the call will be lost. All properties will be set to their default
                values after the call returns.



self_test
---------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: self_test()

            Performs a self-test on the DMM to ensure that the DMM is functioning
            properly. Self-test does not calibrate the DMM. Zero
            indicates success.

            On the NI 4080/4082 and NI 4070/4072, the error code 1013 indicates that
            you should check the fuse and replace it, if necessary.

            Raises `SelfTestError` on self test failure. Properties on exception object:

            - code - failure code from driver
            - message - status message from driver

            

            .. note:: Self-test does not check the fuse on the NI 4065, NI 4071, and NI 4081. Hence, even if the fuse is blown on the device, self-test does not return error code 1013.

            .. note:: This method calls :py:meth:`nidmm.Session.reset`, and any configurations previous to the call will be lost. All properties will be set to their default values after the call returns.



send_software_trigger
---------------------

    .. py:currentmodule:: nidmm.Session

    .. py:method:: send_software_trigger()

            Sends a command to trigger the DMM. Call this method if you have
            configured either the :py:attr:`nidmm.Session.trigger_source` or
            :py:attr:`nidmm.Session.sample_trigger` properties. If the
            :py:attr:`nidmm.Session.trigger_source` and/or :py:attr:`nidmm.Session.sample_trigger`
            properties are set to :py:data:`~nidmm.NIDMM_VAL_EXTERNAL` or :py:data:`~nidmm.NIDMM_VAL_TTL`\ *n*, you
            can use this method to override the trigger source that you configured
            and trigger the device. The NI 4050 and NI 4060 are not supported.

            

            .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.



unlock
------

    .. py:currentmodule:: nidmm.Session

.. py:method:: unlock()

    Releases a lock that you acquired on an device session using
    :py:meth:`nidmm.Session.lock`. Refer to :py:meth:`nidmm.Session.unlock` for additional
    information on session locks.


Properties
==========

ac_max_freq
-----------

    .. py:attribute:: ac_max_freq

        Specifies the maximum frequency component of the input signal for AC  measurements. This property is used only for error checking and verifies  that the value of this parameter is less than the maximum frequency  of the device. This property affects the DMM only when you set the   :py:attr:`nidmm.Session.method` property to AC measurements.
        The valid range is 1 Hz-300 kHz for the NI 4070/4071/4072, 10 Hz-100 kHz  for the NI 4065, and 20 Hz-25 kHz for the NI 4050 and NI 4060.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Max Frequency**
                - C Attribute: **NIDMM_ATTR_AC_MAX_FREQ**

ac_min_freq
-----------

    .. py:attribute:: ac_min_freq

        Specifies the minimum frequency component of the input signal for AC  measurements. This property affects the DMM only when you set the  :py:attr:`nidmm.Session.method` property to AC measurements.
        The valid range is 1 Hz-300 kHz for the NI 4070/4071/4072, 10 Hz-100 kHz  for the NI 4065, and 20 Hz-25 kHz for the NI 4050 and NI 4060.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Min Frequency**
                - C Attribute: **NIDMM_ATTR_AC_MIN_FREQ**

adc_calibration
---------------

    .. py:attribute:: adc_calibration

        For the NI 4070/4071/4072 only, specifies the ADC calibration mode.

        The following table lists the characteristics of this property.

            +----------------+----------------------+
            | Characteristic | Value                |
            +================+======================+
            | Datatype       | enums.ADCCalibration |
            +----------------+----------------------+
            | Permissions    | read-write           |
            +----------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:ADC Calibration**
                - C Attribute: **NIDMM_ATTR_ADC_CALIBRATION**

aperture_time
-------------

    .. py:attribute:: aperture_time

        Specifies the measurement aperture time for the current configuration.  Aperture time is specified in units set by :py:attr:`nidmm.Session.aperture_time_units`. To  override the default aperture, set this property to the desired  aperture time after calling :py:meth:`nidmm.Session.ConfigureMeasurement`. To return to the  default, set this property to :py:data:`~nidmm.NIDMM_VAL_APERTURE_TIME_AUTO` (-1).
        On the NI 4070/4071/4072, the minimum aperture time is 8.89 usec,  and the maximum aperture time is 149 sec. Any number of powerline cycles (PLCs)  within the minimum and maximum ranges is allowed on the NI 4070/4071/4072.
        On the NI 4065 the minimum aperture time is 333 µs, and the maximum aperture time  is 78.2 s. If setting the number of averages directly, the total measurement time is  aperture time X the number of averages, which must be less than 72.8 s. The aperture  times allowed are 333 µs, 667 µs, or multiples of 1.11 ms-for example 1.11 ms, 2.22 ms,  3.33 ms, and so on. If you set an aperture time other than 333 µs, 667 µs, or multiples  of 1.11 ms, the value will be coerced up to the next supported aperture time.
        On the NI 4060, when the powerline frequency is 60 Hz, the PLCs allowed are  1 PLC, 6 PLC, 12 PLC, and 120 PLC. When the powerline frequency is 50 Hz, the  PLCs allowed are 1 PLC, 5 PLC, 10 PLC, and 100 PLC.



        .. note:: One or more of the referenced methods are not in the Python API for this driver.

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Advanced:Aperture Time**
                - C Attribute: **NIDMM_ATTR_APERTURE_TIME**

aperture_time_units
-------------------

    .. py:attribute:: aperture_time_units

        Specifies the units of aperture time for the current configuration.
        The NI 4060 does not support an aperture time set in seconds.

        The following table lists the characteristics of this property.

            +----------------+-------------------------+
            | Characteristic | Value                   |
            +================+=========================+
            | Datatype       | enums.ApertureTimeUnits |
            +----------------+-------------------------+
            | Permissions    | read-write              |
            +----------------+-------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Advanced:Aperture Time Units**
                - C Attribute: **NIDMM_ATTR_APERTURE_TIME_UNITS**

auto_range_value
----------------

    .. py:attribute:: auto_range_value

        Specifies the value of the range. If auto ranging, shows the actual value of  the active range. The value of this property is set during a read operation.

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

                - LabVIEW Property: **Configuration:Auto Range Value**
                - C Attribute: **NIDMM_ATTR_AUTO_RANGE_VALUE**

auto_zero
---------

    .. py:attribute:: auto_zero

        Specifies the AutoZero mode.
        The NI 4050 is not supported.

        The following table lists the characteristics of this property.

            +----------------+----------------+
            | Characteristic | Value          |
            +================+================+
            | Datatype       | enums.AutoZero |
            +----------------+----------------+
            | Permissions    | read-write     |
            +----------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Auto Zero**
                - C Attribute: **NIDMM_ATTR_AUTO_ZERO**

buffer_size
-----------

    .. py:attribute:: buffer_size

        Size in samples of the internal data buffer. Maximum is 134,217,727 (OX7FFFFFF) samples. When  set to :py:data:`~nidmm.NIDMM_VAL_BUFFER_SIZE_AUTO` (-1), NI-DMM chooses the buffer size.



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Multi Point Acquisition:Advanced:Buffer Size**
                - C Attribute: **NIDMM_ATTR_BUFFER_SIZE**

cable_comp_type
---------------

    .. py:attribute:: cable_comp_type

        For the NI 4072 only,  the type of cable compensation that is applied to the current capacitance  or inductance measurement for the current range.
        Changing the method or the range through this property or through :py:meth:`nidmm.Session.configure_measurement_digits`  resets the value of this property to the default value.

        The following table lists the characteristics of this property.

            +----------------+-----------------------------+
            | Characteristic | Value                       |
            +================+=============================+
            | Datatype       | enums.CableCompensationType |
            +----------------+-----------------------------+
            | Permissions    | read-write                  |
            +----------------+-----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Capacitance and Inductance:Cable Compensation Type**
                - C Attribute: **NIDMM_ATTR_CABLE_COMP_TYPE**

channel_count
-------------

    .. py:attribute:: channel_count

        Indicates the number of channels that the specific instrument driver  supports. For each property for which the IVI_VAL_MULTI_CHANNEL flag  property is set, the IVI engine maintains a separate cache value for each  channel.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Capabilities:Channel Count**
                - C Attribute: **NIDMM_ATTR_CHANNEL_COUNT**

current_source
--------------

    .. py:attribute:: current_source

        Specifies the current source provided during diode measurements.
        The NI 4050 and NI 4060 are not supported.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Current Source**
                - C Attribute: **NIDMM_ATTR_CURRENT_SOURCE**

dc_bias
-------

    .. py:attribute:: dc_bias

        For the NI 4072 only, controls the available DC bias for capacitance measurements.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Capacitance and Inductance:Advanced:DC Bias**
                - C Attribute: **NIDMM_ATTR_DC_BIAS**

dc_noise_rejection
------------------

    .. py:attribute:: dc_noise_rejection

        Specifies the DC noise rejection mode.
        The NI 4050 and NI 4060 are not supported.

        The following table lists the characteristics of this property.

            +----------------+------------------------+
            | Characteristic | Value                  |
            +================+========================+
            | Datatype       | enums.DCNoiseRejection |
            +----------------+------------------------+
            | Permissions    | read-write             |
            +----------------+------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:DC Noise Rejection**
                - C Attribute: **NIDMM_ATTR_DC_NOISE_REJECTION**

driver_setup
------------

    .. py:attribute:: driver_setup

        This property indicates the Driver Setup string that the user specified when  initializing the driver.
        Some cases exist where the end-user must specify instrument driver options  at initialization time.  An example of this is specifying a particular  instrument model from among a family of instruments that the driver supports.   This is useful when using simulation.  The end-user can specify  driver-specific options through the DriverSetup keyword in the optionsString  parameter to the niDMM Init With Options.vi.
        If the user does not specify a Driver Setup string, this property returns  an empty string.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:User Options:Driver Setup**
                - C Attribute: **NIDMM_ATTR_DRIVER_SETUP**

freq_voltage_auto_range
-----------------------

    .. py:attribute:: freq_voltage_auto_range

        For the NI 4070/4071/4072 only, specifies the value of the frequency voltage range.  If Auto Ranging, shows the actual value of the active frequency voltage range.  If not Auto Ranging, the value of this property is the same as that of  :py:attr:`nidmm.Session.freq_voltage_range`.

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

                - LabVIEW Property: **Configuration:Measurement Options:Frequency Voltage Auto Range Value**
                - C Attribute: **NIDMM_ATTR_FREQ_VOLTAGE_AUTO_RANGE**

freq_voltage_range
------------------

    .. py:attribute:: freq_voltage_range

        Specifies the maximum amplitude of the input signal for frequency  measurements.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Frequency Voltage Range**
                - C Attribute: **NIDMM_ATTR_FREQ_VOLTAGE_RANGE**

function
--------

    .. py:attribute:: function

        Specifies the measurement method.
        Refer to the :py:attr:`nidmm.Session.method` topic in  the NI Digital Multimeters Help for device-specific information.
        If you are setting this property directly, you must also set the :py:attr:`nidmm.Session.operation_mode` property,  which controls whether the DMM takes standard single or multipoint measurements, or acquires a waveform.  If you are programming properties directly, you must set the :py:attr:`nidmm.Session.operation_mode` property before  setting other configuration properties. If the :py:attr:`nidmm.Session.operation_mode` property is set to :py:data:`~nidmm.OperationMode.WAVEFORM`,  the only valid method types are :py:data:`~nidmm.Method.WAVEFORM_VOLTAGE` and :py:data:`~nidmm.Method.WAVEFORM_CURRENT`. Set the  :py:attr:`nidmm.Session.operation_mode` property to :py:data:`~nidmm.OperationMode.IVIDMM` to set all other method values.

        The following table lists the characteristics of this property.

            +----------------+----------------+
            | Characteristic | Value          |
            +================+================+
            | Datatype       | enums.Function |
            +----------------+----------------+
            | Permissions    | read-write     |
            +----------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Function**
                - C Attribute: **NIDMM_ATTR_FUNCTION**

input_resistance
----------------

    .. py:attribute:: input_resistance

        Specifies the input resistance of the instrument.
        The NI 4050 and NI 4060 are not supported.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Input Resistance**
                - C Attribute: **NIDMM_ATTR_INPUT_RESISTANCE**

instrument_firmware_revision
----------------------------

    .. py:attribute:: instrument_firmware_revision

        A string containing the instrument firmware revision number.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Instrument Firmware Revision**
                - C Attribute: **NIDMM_ATTR_INSTRUMENT_FIRMWARE_REVISION**

instrument_manufacturer
-----------------------

    .. py:attribute:: instrument_manufacturer

        A string containing the manufacturer of the instrument.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Instrument Manufacturer**
                - C Attribute: **NIDMM_ATTR_INSTRUMENT_MANUFACTURER**

instrument_model
----------------

    .. py:attribute:: instrument_model

        A string containing the instrument model.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Instrument Model**
                - C Attribute: **NIDMM_ATTR_INSTRUMENT_MODEL**

instrument_product_id
---------------------

    .. py:attribute:: instrument_product_id

        The PCI product ID.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Instrument Product ID**
                - C Attribute: **NIDMM_ATTR_INSTRUMENT_PRODUCT_ID**

io_resource_descriptor
----------------------

    .. py:attribute:: io_resource_descriptor

        A string containing the resource descriptor of the instrument.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Advanced Session Information:I/O Resource Descriptor**
                - C Attribute: **NIDMM_ATTR_IO_RESOURCE_DESCRIPTOR**

lc_calculation_model
--------------------

    .. py:attribute:: lc_calculation_model

        For the NI 4072 only, specifies the type of algorithm that the measurement processing uses for  capacitance and inductance measurements.

        The following table lists the characteristics of this property.

            +----------------+--------------------------+
            | Characteristic | Value                    |
            +================+==========================+
            | Datatype       | enums.LCCalculationModel |
            +----------------+--------------------------+
            | Permissions    | read-write               |
            +----------------+--------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Capacitance and Inductance:Advanced:Calculation Model**
                - C Attribute: **NIDMM_ATTR_LC_CALCULATION_MODEL**

lc_number_meas_to_average
-------------------------

    .. py:attribute:: lc_number_meas_to_average

        For the NI 4072 only, specifies the number of LC measurements that are averaged to produce one reading.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Capacitance and Inductance:Number of LC Measurements To Average**
                - C Attribute: **NIDMM_ATTR_LC_NUMBER_MEAS_TO_AVERAGE**

logical_name
------------

    .. py:attribute:: logical_name

        A string containing the logical name of the instrument.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Advanced Session Information:Logical Name**
                - C Attribute: **NIDMM_ATTR_LOGICAL_NAME**

meas_complete_dest
------------------

    .. py:attribute:: meas_complete_dest

        Specifies the destination of the measurement complete (MC) signal.
        The NI 4050 is not supported.
        To determine which values are supported by each device, refer to the LabWindows/CVI Trigger Routing section in  the NI Digital Multimeters Help.

        The following table lists the characteristics of this property.

            +----------------+-------------------------------+
            | Characteristic | Value                         |
            +================+===============================+
            | Datatype       | enums.MeasurementCompleteDest |
            +----------------+-------------------------------+
            | Permissions    | read-write                    |
            +----------------+-------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Trigger:Measurement Complete Dest**
                - C Attribute: **NIDMM_ATTR_MEAS_COMPLETE_DEST**

number_of_averages
------------------

    .. py:attribute:: number_of_averages

        Specifies the number of averages to perform in a measurement. For the NI 4070/4071/4072,  applies only when the aperture time is not set to AUTO and Auto Zero is ON.  The default is 1.
        The NI 4050 and NI 4060 are not supported.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Advanced:Number Of Averages**
                - C Attribute: **NIDMM_ATTR_NUMBER_OF_AVERAGES**

offset_comp_ohms
----------------

    .. py:attribute:: offset_comp_ohms

        For the NI 4070/4071/4072 only, enables or disables offset compensated ohms.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Offset Compensated Ohms**
                - C Attribute: **NIDMM_ATTR_OFFSET_COMP_OHMS**

open_cable_comp_conductance
---------------------------

    .. py:attribute:: open_cable_comp_conductance

        For the NI 4072 only, specifies the active part (conductance) of the open cable compensation.  The valid range is any real number greater than 0. The default value (-1.0)  indicates that compensation has not taken place.
        Changing the method or the range through this property or through :py:meth:`nidmm.Session.configure_measurement_digits`  resets the value of this property to the default value.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Capacitance and Inductance:Open Cable Compensation Values:Conductance**
                - C Attribute: **NIDMM_ATTR_OPEN_CABLE_COMP_CONDUCTANCE**

open_cable_comp_susceptance
---------------------------

    .. py:attribute:: open_cable_comp_susceptance

        For the NI 4072 only, specifies the reactive part (susceptance) of the open cable compensation.  The valid range is any real number greater than 0. The default value (-1.0)  indicates that compensation has not taken place.
        Changing the method or the range through this property or through :py:meth:`nidmm.Session.configure_measurement_digits`  resets the value of this property to the default value.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Capacitance and Inductance:Open Cable Compensation Values:Susceptance**
                - C Attribute: **NIDMM_ATTR_OPEN_CABLE_COMP_SUSCEPTANCE**

operation_mode
--------------

    .. py:attribute:: operation_mode

        Specifies how the NI 4065 and NI 4070/4071/4072 acquire data. When you call  :py:meth:`nidmm.Session.configure_measurement_digits`, NI-DMM sets this property to :py:data:`~nidmm.OperationMode.IVIDMM`.  When you call :py:meth:`nidmm.Session.configure_waveform_acquisition`, NI-DMM sets this property to :py:data:`~nidmm.OperationMode.WAVEFORM`.  If you are programming properties directly, you must set this property before  setting other configuration properties.

        The following table lists the characteristics of this property.

            +----------------+---------------------+
            | Characteristic | Value               |
            +================+=====================+
            | Datatype       | enums.OperationMode |
            +----------------+---------------------+
            | Permissions    | read-write          |
            +----------------+---------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Advanced:Operation Mode**
                - C Attribute: **NIDMM_ATTR_OPERATION_MODE**

powerline_freq
--------------

    .. py:attribute:: powerline_freq

        Specifies the powerline frequency. The NI 4050 and NI 4060 use this value to select an aperture time to reject  powerline noise by selecting the appropriate internal sample clock and filter. The NI 4065 and  NI 4070/4071/4072 use this value to select a timebase for setting the :py:attr:`nidmm.Session.aperture_time`  property in powerline cycles (PLCs).
        After configuring powerline frequency, set the :py:attr:`nidmm.Session.aperture_time_units` property to PLCs.  When setting the :py:attr:`nidmm.Session.aperture_time` property, select the number of PLCs for the powerline frequency.  For example, if powerline frequency = 50 Hz (or 20ms) and aperture time in PLCs = 5, then aperture time in  Seconds = 20ms * 5 PLCs = 100 ms. Similarly, if powerline frequency = 60 Hz (or 16.667 ms) and aperture time  in PLCs = 6, then aperture time in Seconds = 16.667 ms * 6 PLCs = 100 ms.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Powerline Frequency**
                - C Attribute: **NIDMM_ATTR_POWERLINE_FREQ**

range
-----

    .. py:attribute:: range

        Specifies the measurement range. Use positive values to represent the  absolute value of the maximum expected measurement. The value is in units  appropriate for the current value of the :py:attr:`nidmm.Session.method` property. For  example, if :py:attr:`nidmm.Session.method` is set to :py:data:`~nidmm.NIDMM_VAL_VOLTS`, the units are  volts.
        The NI 4050 and NI 4060 only support Auto Range when the trigger and  sample trigger is set to IMMEDIATE.
        :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_ON` -1.0
        NI-DMM performs an Auto Range before acquiring the measurement.
        :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_OFF` -2.0
        NI-DMM sets the Range to the current :py:attr:`nidmm.Session.auto_range_value` and uses this range  for all subsequent measurements until the measurement configuration is changed.
        :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_ONCE` -3.0
        NI-DMM performs an Auto Range before acquiring the next measurement. The :py:attr:`nidmm.Session.auto_range_value`  is stored and used for all subsequent measurements until the measurement configuration is changed.



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Range**
                - C Attribute: **NIDMM_ATTR_RANGE**

resolution_absolute
-------------------

    .. py:attribute:: resolution_absolute

        Specifies the measurement resolution in absolute units. Setting this  property to higher values increases the measurement accuracy. Setting this  property to lower values increases the measurement speed.
        NI-DMM ignores this property for capacitance and inductance measurements on the NI 4072.  To achieve better resolution for such measurements, use the :py:attr:`nidmm.Session.lc_number_meas_to_average` property.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Absolute Resolution**
                - C Attribute: **NIDMM_ATTR_RESOLUTION_ABSOLUTE**

resolution_digits
-----------------

    .. py:attribute:: resolution_digits

        Specifies the measurement resolution in digits. Setting this  property to higher values increases the measurement accuracy. Setting this  property to lower values increases the measurement speed.
        NI-DMM ignores this property for capacitance and inductance measurements on the NI 4072.  To achieve better resolution for such measurements, use the :py:attr:`nidmm.Session.lc_number_meas_to_average` property.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Digits Resolution**
                - C Attribute: **NIDMM_ATTR_RESOLUTION_DIGITS**

sample_count
------------

    .. py:attribute:: sample_count

        Specifies the number of measurements the DMM takes each time it receives a  trigger in a multiple point acquisition.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Multi Point Acquisition:Sample Count**
                - C Attribute: **NIDMM_ATTR_SAMPLE_COUNT**

sample_interval
---------------

    .. py:attribute:: sample_interval

        Specifies the amount of time in seconds the DMM waits between measurement cycles.  This property only applies when the :py:attr:`nidmm.Session.sample_trigger` property is set to INTERVAL.
        On the NI 4060, the value for this property is used as the settling time.  When this property is set to 0, the NI 4060 does not settle between  measurement cycles. The onboard timing resolution is 1 µs on the NI 4060.
        The NI 4065 and NI 4070/4071/4072 use the value specified in this property as additional  delay. On the NI 4065 and NI 4070/4071/4072, the onboard timing resolution is 34.72 ns and  the valid range is 0-149 s.
        Only positive values are valid when setting the sample interval.
        The NI 4050 is not supported.

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

                - LabVIEW Property: **Multi Point Acquisition:Sample Interval**
                - C Attribute: **NIDMM_ATTR_SAMPLE_INTERVAL**

sample_trigger
--------------

    .. py:attribute:: sample_trigger

        Specifies the sample trigger source.
        To determine which values are supported by each device, refer to the LabWindows/CVI Trigger Routing section in  the NI Digital Multimeters Help.

        The following table lists the characteristics of this property.

            +----------------+---------------------+
            | Characteristic | Value               |
            +================+=====================+
            | Datatype       | enums.SampleTrigger |
            +----------------+---------------------+
            | Permissions    | read-write          |
            +----------------+---------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Multi Point Acquisition:Sample Trigger**
                - C Attribute: **NIDMM_ATTR_SAMPLE_TRIGGER**

serial_number
-------------

    .. py:attribute:: serial_number

        A string containing the serial number of the instrument. This property corresponds  to the serial number label that is attached to most products.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Instrument Serial Number**
                - C Attribute: **NIDMM_ATTR_SERIAL_NUMBER**

settle_time
-----------

    .. py:attribute:: settle_time

        Specifies the settling time in seconds. To override the default settling time,  set this property. To return to the default, set this property to  :py:data:`~nidmm.NIDMM_VAL_SETTLE_TIME_AUTO` (-1).
        The NI 4050 and NI 4060 are not supported.



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

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

                - LabVIEW Property: **Configuration:Advanced:Settle Time**
                - C Attribute: **NIDMM_ATTR_SETTLE_TIME**

short_cable_comp_reactance
--------------------------

    .. py:attribute:: short_cable_comp_reactance

        For the NI 4072 only, represents the reactive part (reactance) of the short cable compensation.  The valid range is any real number greater than 0. The default value (-1)  indicates that compensation has not taken place.
        Changing the method or the range through this property or through :py:meth:`nidmm.Session.configure_measurement_digits`  resets the value of this property to the default value.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Capacitance and Inductance:Short Cable Compensation Values:Reactance**
                - C Attribute: **NIDMM_ATTR_SHORT_CABLE_COMP_REACTANCE**

short_cable_comp_resistance
---------------------------

    .. py:attribute:: short_cable_comp_resistance

        For the NI 4072 only, represents the active part (resistance) of the short cable compensation.  The valid range is any real number greater than 0. The default value (-1)  indicates that compensation has not taken place.
        Changing the method or the range through this property or through :py:meth:`nidmm.Session.configure_measurement_digits`  resets the value of this property to the default value.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Capacitance and Inductance:Short Cable Compensation Values:Resistance**
                - C Attribute: **NIDMM_ATTR_SHORT_CABLE_COMP_RESISTANCE**

simulate
--------

    .. py:attribute:: simulate

        Specifies whether or not to simulate instrument driver I/O operations. If  simulation is enabled, instrument driver methods perform range checking and  call IVI Get and Set methods, but they do not perform  instrument I/O. For output parameters that represent instrument data, the  instrument driver methods return calculated values.
        The default value is False (0). Use the :py:meth:`nidmm.Session.__init__` method to  override this setting.
        Simulate can only be set within the InitWithOptions method.  The property value cannot be changed outside of the method.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:User Options:Simulate**
                - C Attribute: **NIDMM_ATTR_SIMULATE**

specific_driver_description
---------------------------

    .. py:attribute:: specific_driver_description

        A string containing a description of the specific driver.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Specific Driver Identification:Specific Driver Description**
                - C Attribute: **NIDMM_ATTR_SPECIFIC_DRIVER_DESCRIPTION**

specific_driver_major_version
-----------------------------

    .. py:attribute:: specific_driver_major_version

        Returns the major version number of this instrument driver.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Version Info:Specific Driver Major Version**
                - C Attribute: **NIDMM_ATTR_SPECIFIC_DRIVER_MAJOR_VERSION**

specific_driver_minor_version
-----------------------------

    .. py:attribute:: specific_driver_minor_version

        The minor version number of this instrument driver.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Version Info:Specific Driver Minor Version**
                - C Attribute: **NIDMM_ATTR_SPECIFIC_DRIVER_MINOR_VERSION**

specific_driver_revision
------------------------

    .. py:attribute:: specific_driver_revision

        A string that contains additional version information about this specific  instrument driver.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Version Info:Specific Driver Revision**
                - C Attribute: **NIDMM_ATTR_SPECIFIC_DRIVER_REVISION**

specific_driver_vendor
----------------------

    .. py:attribute:: specific_driver_vendor

        A string containing the vendor of the specific driver.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Specific Driver Identification:Specific Driver Vendor**
                - C Attribute: **NIDMM_ATTR_SPECIFIC_DRIVER_VENDOR**

supported_instrument_models
---------------------------

    .. py:attribute:: supported_instrument_models

        A string containing the instrument models supported by the specific driver.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Specific Driver Capabilities:Supported Instrument Models**
                - C Attribute: **NIDMM_ATTR_SUPPORTED_INSTRUMENT_MODELS**

temp_rtd_a
----------

    .. py:attribute:: temp_rtd_a

        Specifies the Callendar-Van Dusen A coefficient for RTD scaling when the RTD Type property   is set to Custom. The default value is 3.9083e-3 (Pt3851).

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD A**
                - C Attribute: **NIDMM_ATTR_TEMP_RTD_A**

temp_rtd_b
----------

    .. py:attribute:: temp_rtd_b

        Specifies the Callendar-Van Dusen B coefficient for RTD scaling when the RTD Type property  is set to Custom. The default value is -5.775e-7(Pt3851).

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD B**
                - C Attribute: **NIDMM_ATTR_TEMP_RTD_B**

temp_rtd_c
----------

    .. py:attribute:: temp_rtd_c

        Specifies the Callendar-Van Dusen C coefficient for RTD scaling when the RTD Type property  is set to Custom. The default value is -4.183e-12(Pt3851).

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD C**
                - C Attribute: **NIDMM_ATTR_TEMP_RTD_C**

temp_rtd_res
------------

    .. py:attribute:: temp_rtd_res

        Specifies the RTD resistance at 0 degrees Celsius. This applies to all supported RTDs,  including custom RTDs. The default value is 100 (?).

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD Resistance**
                - C Attribute: **NIDMM_ATTR_TEMP_RTD_RES**

temp_rtd_type
-------------

    .. py:attribute:: temp_rtd_type

        Specifies the type of RTD used to measure temperature. The default value is :py:data:`~nidmm.RTDType.PT3851`.
        Refer to the :py:attr:`nidmm.Session.temp_rtd_type` topic in the NI Digital Multimeters Help for additional information about defined values.

        The following table lists the characteristics of this property.

            +----------------+---------------+
            | Characteristic | Value         |
            +================+===============+
            | Datatype       | enums.RTDType |
            +----------------+---------------+
            | Permissions    | read-write    |
            +----------------+---------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD Type**
                - C Attribute: **NIDMM_ATTR_TEMP_RTD_TYPE**

temp_tc_fixed_ref_junc
----------------------

    .. py:attribute:: temp_tc_fixed_ref_junc

        Specifies the reference junction temperature when a fixed reference junction is used to take  a thermocouple measurement. The default value is 25.0 (°C).

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Temperature:Thermocouple:Fixed Reference Junction**
                - C Attribute: **NIDMM_ATTR_TEMP_TC_FIXED_REF_JUNC**

temp_tc_ref_junc_type
---------------------

    .. py:attribute:: temp_tc_ref_junc_type

        Specifies the type of reference junction to be used in the reference junction compensation  of a thermocouple. The only supported value, :py:data:`~nidmm.ThermocoupleReferenceJunctionType.FIXED`, is fixed.

        The following table lists the characteristics of this property.

            +----------------+-----------------------------------------+
            | Characteristic | Value                                   |
            +================+=========================================+
            | Datatype       | enums.ThermocoupleReferenceJunctionType |
            +----------------+-----------------------------------------+
            | Permissions    | read-write                              |
            +----------------+-----------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Temperature:Thermocouple:Reference Junction Type**
                - C Attribute: **NIDMM_ATTR_TEMP_TC_REF_JUNC_TYPE**

temp_tc_type
------------

    .. py:attribute:: temp_tc_type

        Specifies the type of thermocouple used to measure the temperature. The default value is :py:data:`~nidmm.ThermocoupleType.J`.

        The following table lists the characteristics of this property.

            +----------------+------------------------+
            | Characteristic | Value                  |
            +================+========================+
            | Datatype       | enums.ThermocoupleType |
            +----------------+------------------------+
            | Permissions    | read-write             |
            +----------------+------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Temperature:Thermocouple:Thermocouple Type**
                - C Attribute: **NIDMM_ATTR_TEMP_TC_TYPE**

temp_thermistor_a
-----------------

    .. py:attribute:: temp_thermistor_a

        Specifies the Steinhart-Hart A coefficient for thermistor scaling when the Thermistor Type  property is set to Custom. The default value is 0.0010295 (44006).

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Temperature:Thermistor:Thermistor A**
                - C Attribute: **NIDMM_ATTR_TEMP_THERMISTOR_A**

temp_thermistor_b
-----------------

    .. py:attribute:: temp_thermistor_b

        Specifies the Steinhart-Hart B coefficient for thermistor scaling when the Thermistor Type  proerty is set to Custom. The default value is 0.0002391 (44006).

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Temperature:Thermistor:Thermistor B**
                - C Attribute: **NIDMM_ATTR_TEMP_THERMISTOR_B**

temp_thermistor_c
-----------------

    .. py:attribute:: temp_thermistor_c

        Specifies the Steinhart-Hart C coefficient for thermistor scaling when the Thermistor Type  property is set to Custom. The default value is 1.568e-7 (44006).

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Temperature:Thermistor:Thermistor C**
                - C Attribute: **NIDMM_ATTR_TEMP_THERMISTOR_C**

temp_thermistor_type
--------------------

    .. py:attribute:: temp_thermistor_type

        Specifies the type of thermistor used to measure the temperature. The default value is  :py:data:`~nidmm.ThermistorType.THERMISTOR_44006`.
        Refer to the :py:attr:`nidmm.Session.temp_thermistor_type` topic in the NI Digital Multimeters Help for additional information about defined values.

        The following table lists the characteristics of this property.

            +----------------+----------------------+
            | Characteristic | Value                |
            +================+======================+
            | Datatype       | enums.ThermistorType |
            +----------------+----------------------+
            | Permissions    | read-write           |
            +----------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Temperature:Thermistor:Thermistor Type**
                - C Attribute: **NIDMM_ATTR_TEMP_THERMISTOR_TYPE**

temp_transducer_type
--------------------

    .. py:attribute:: temp_transducer_type

        Specifies the type of device used to measure the temperature. The default value is :py:data:`~nidmm.NIDMM_VAL_4_THERMOCOUPLE`.



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +----------------+----------------------+
            | Characteristic | Value                |
            +================+======================+
            | Datatype       | enums.TransducerType |
            +----------------+----------------------+
            | Permissions    | read-write           |
            +----------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Configuration:Measurement Options:Temperature:Transducer Type**
                - C Attribute: **NIDMM_ATTR_TEMP_TRANSDUCER_TYPE**

trigger_count
-------------

    .. py:attribute:: trigger_count

        Specifies the number of triggers the DMM receives before returning to the  Idle state.
        This property can be set to any positive ViInt32 value for the NI 4065 and NI 4070/4071/4072.
        The NI 4050 and NI 4060 support this property being set to 1.
        Refer to the Multiple Point Acquisitions section of the NI Digital Multimeters Help for more information.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Multi Point Acquisition:Trigger Count**
                - C Attribute: **NIDMM_ATTR_TRIGGER_COUNT**

trigger_delay
-------------

    .. py:attribute:: trigger_delay

        Specifies the time (in seconds) that the DMM waits after it has received a trigger before taking a measurement.  The default value is AUTO DELAY (-1), which means that the DMM waits an appropriate settling time before taking  the measurement. (-1) signifies that AUTO DELAY is on, and (-2) signifies that AUTO DELAY is off.
        The NI 4065 and NI 4070/4071/4072 use the value specified in this property as additional settling time.  For the The NI 4065 and NI 4070/4071/4072, the valid range for Trigger Delay is AUTO DELAY (-1) or 0.0-149.0  seconds and the onboard timing resolution is 34.72 ns.
        On the NI 4060, if this property is set to 0, the DMM does not settle before taking the measurement.  On the NI 4060, the valid range for AUTO DELAY (-1) is 0.0-12.0 seconds and the onboard timing resolution  is 100 ms.
        When using the NI 4050, this property must be set to AUTO DELAY (-1).
        Use positive values to set the trigger delay in seconds.
        Valid Range: :py:data:`~nidmm.NIDMM_VAL_AUTO_DELAY` (-1.0), 0.0-12.0 seconds (NI 4060 only)
        Default Value: :py:data:`~nidmm.NIDMM_VAL_AUTO_DELAY`



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

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

                - LabVIEW Property: **Trigger:Trigger Delay**
                - C Attribute: **NIDMM_ATTR_TRIGGER_DELAY**

trigger_source
--------------

    .. py:attribute:: trigger_source

        Specifies the trigger source. When :py:meth:`nidmm.Session._initiate` is called, the DMM waits  for the trigger specified with this property. After it receives the trigger,  the DMM waits the length of time specified with the :py:attr:`nidmm.Session.trigger_delay`  property. The DMM then takes a measurement.
        This property is not supported on the NI 4050.
        To determine which values are supported by each device, refer to the LabWindows/CVI Trigger Routing section in  the NI Digital Multimeters Help.

        The following table lists the characteristics of this property.

            +----------------+---------------------+
            | Characteristic | Value               |
            +================+=====================+
            | Datatype       | enums.TriggerSource |
            +----------------+---------------------+
            | Permissions    | read-write          |
            +----------------+---------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Trigger:Trigger Source**
                - C Attribute: **NIDMM_ATTR_TRIGGER_SOURCE**

waveform_coupling
-----------------

    .. py:attribute:: waveform_coupling

        For the NI 4070/4071/4072 only, specifies the coupling during a waveform acquisition.

        The following table lists the characteristics of this property.

            +----------------+------------------------+
            | Characteristic | Value                  |
            +================+========================+
            | Datatype       | enums.WaveformCoupling |
            +----------------+------------------------+
            | Permissions    | read-write             |
            +----------------+------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Waveform Acquisition:Waveform Coupling**
                - C Attribute: **NIDMM_ATTR_WAVEFORM_COUPLING**

waveform_points
---------------

    .. py:attribute:: waveform_points

        For the NI 4070/4071/4072 only, specifies the number of points to acquire in a waveform acquisition.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Waveform Acquisition:Waveform Points**
                - C Attribute: **NIDMM_ATTR_WAVEFORM_POINTS**

waveform_rate
-------------

    .. py:attribute:: waveform_rate

        For the NI 4070/4071/4072 only, specifies the rate of the waveform acquisition in Samples per second (S/s).  The valid Range is 10.0-1,800,000 S/s. Values are coerced to the  closest integer divisor of 1,800,000. The default value is 1,800,000.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Waveform Acquisition:Waveform Rate**
                - C Attribute: **NIDMM_ATTR_WAVEFORM_RATE**


.. contents:: Session
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nidmm/conf.py sha256=3c4c4d8db885f1cdae0dedabfdee51b63603a436223294610d8653b665292aec bytes=6524 -->
## FILE: docs/nidmm/conf.py

- repository: `ni/nimi-python`
- source_path: `docs/nidmm/conf.py`
- sha256: `3c4c4d8db885f1cdae0dedabfdee51b63603a436223294610d8653b665292aec`
- bytes: 6524

````python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# NI-DMM Python API documentation build configuration file, created by
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
project = 'NI-DMM Python API'
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
    (master_doc, 'NIDMMPythonAPI.tex', 'NI-DMM Python API Documentation',
     'NI', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'nidmmpythonapi', 'NI-DMM Python API Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'NIDMMPythonAPI', 'NI-DMM Python API Documentation',
     author, 'NIDMMPythonAPI', 'One line description of project.',
     'Miscellaneous'),
]

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'nidcpower': ('https://nidcpower.readthedocs.io/en/latest/', None),
    'nidigital': ('https://nidigital.readthedocs.io/en/latest/', None),
    'nifgen': ('https://nifgen.readthedocs.io/en/latest/', None),
    'nimodinst': ('https://nimodinst.readthedocs.io/en/latest/', None),
    'nirfsg': ('https://nirfsg.readthedocs.io/en/latest/', None),
    'niscope': ('https://niscope.readthedocs.io/en/latest/', None),
    'nise': ('https://nise.readthedocs.io/en/latest/', None),
    'niswitch': ('https://niswitch.readthedocs.io/en/latest/', None),
    'nitclk': ('https://nitclk.readthedocs.io/en/latest/', None),
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nidmm/enums.rst sha256=aeff18522d232eb8a192243d577c3e03012433434d1ea0af1bf5fb15cf381979 bytes=12287 -->
## FILE: docs/nidmm/enums.rst

- repository: `ni/nimi-python`
- source_path: `docs/nidmm/enums.rst`
- sha256: `aeff18522d232eb8a192243d577c3e03012433434d1ea0af1bf5fb15cf381979`
- bytes: 12287

````rst
Enums
=====

Enums used in NI-DMM

.. py:currentmodule:: nidmm


ADCCalibration
--------------

.. py:class:: ADCCalibration

    .. py:attribute:: ADCCalibration.AUTO



        The DMM enables or disables ADC calibration for you.

        



    .. py:attribute:: ADCCalibration.OFF



        The DMM does not compensate for changes to the gain.

        



    .. py:attribute:: ADCCalibration.ON



        The DMM measures an internal reference to calculate the correct gain for the  measurement.

        



AcquisitionStatus
-----------------

.. py:class:: AcquisitionStatus

    .. py:attribute:: AcquisitionStatus.RUNNING



        Running

        



    .. py:attribute:: AcquisitionStatus.FINISHED_WITH_BACKLOG



        Finished with **Backlog**

        



    .. py:attribute:: AcquisitionStatus.FINISHED_WITH_NO_BACKLOG



        Finished with no **Backlog**

        



    .. py:attribute:: AcquisitionStatus.PAUSED



        Paused

        



    .. py:attribute:: AcquisitionStatus.NO_ACQUISITION_IN_PROGRESS



        No acquisition in progress

        



ApertureTimeUnits
-----------------

.. py:class:: ApertureTimeUnits

    .. py:attribute:: ApertureTimeUnits.SECONDS



        Seconds

        



    .. py:attribute:: ApertureTimeUnits.POWER_LINE_CYCLES



        Powerline Cycles

        



AutoZero
--------

.. py:class:: AutoZero

    .. py:attribute:: AutoZero.AUTO



        The drivers chooses the AutoZero setting based on the configured method  and resolution.

        



    .. py:attribute:: AutoZero.OFF



        Disables AutoZero.

        



    .. py:attribute:: AutoZero.ON



        The DMM internally disconnects the input signal following each measurement  and takes a zero reading. It then subtracts the zero reading from the  preceding reading.

        



    .. py:attribute:: AutoZero.ONCE



        The DMM internally disconnects the input signal for the first measurement  and takes a zero reading. It then subtracts the zero reading from the first  reading and the following readings.

        



CableCompensationType
---------------------

.. py:class:: CableCompensationType

    .. py:attribute:: CableCompensationType.NONE



        No Cable Compensation

        



    .. py:attribute:: CableCompensationType.OPEN



        Open Cable Compensation

        



    .. py:attribute:: CableCompensationType.SHORT



        Short Cable Compensation

        



    .. py:attribute:: CableCompensationType.OPEN_AND_SHORT



        Open and Short Cable Compensation

        



DCNoiseRejection
----------------

.. py:class:: DCNoiseRejection

    .. py:attribute:: DCNoiseRejection.AUTO



        The driver chooses the DC noise rejection setting based on the configured  method and resolution.

        



    .. py:attribute:: DCNoiseRejection.NORMAL



        NI-DMM weighs all samples equally.

        



    .. py:attribute:: DCNoiseRejection.SECOND_ORDER



        NI-DMM weighs the samples taken in the middle of the aperture time more than  samples taken at the beginning and the end of the measurement using a  triangular weighing method.

        



    .. py:attribute:: DCNoiseRejection.HIGH_ORDER



        NI-DMM weighs the samples taken in the middle of the aperture time more than  samples taken at the beginning and the end of the measurement using a  bell-curve weighing method.

        



Function
--------

.. py:class:: Function

    .. py:attribute:: Function.DC_VOLTS



        DC Voltage

        



    .. py:attribute:: Function.AC_VOLTS



        AC Voltage

        



    .. py:attribute:: Function.DC_CURRENT



        DC Current

        



    .. py:attribute:: Function.AC_CURRENT



        AC Current

        



    .. py:attribute:: Function.TWO_WIRE_RES



        2-Wire Resistance

        



    .. py:attribute:: Function.FOUR_WIRE_RES



        4-Wire Resistance

        



    .. py:attribute:: Function.FREQ



        Frequency

        



    .. py:attribute:: Function.PERIOD



        Period

        



    .. py:attribute:: Function.TEMPERATURE



        NI 4065, NI 4070/4071/4072, and NI 4080/4081/4182 supported.

        



    .. py:attribute:: Function.AC_VOLTS_DC_COUPLED



        AC Voltage with DC Coupling

        



    .. py:attribute:: Function.DIODE



        Diode

        



    .. py:attribute:: Function.WAVEFORM_VOLTAGE



        Waveform voltage

        



    .. py:attribute:: Function.WAVEFORM_CURRENT



        Waveform current

        



    .. py:attribute:: Function.CAPACITANCE



        Capacitance

        



    .. py:attribute:: Function.INDUCTANCE



        Inductance

        



LCCalculationModel
------------------

.. py:class:: LCCalculationModel

    .. py:attribute:: LCCalculationModel.AUTO



        NI-DMM chooses the algorithm based on method and range

        



    .. py:attribute:: LCCalculationModel.SERIES



        NI-DMM uses the series impedance model to calculate capacitance and inductance

        



    .. py:attribute:: LCCalculationModel.PARALLEL



        NI-DMM uses the parallel admittance model to calculate capacitance and inductance

        



MeasurementCompleteDest
-----------------------

.. py:class:: MeasurementCompleteDest

    .. py:attribute:: MeasurementCompleteDest.NONE



        No Trigger

        



    .. py:attribute:: MeasurementCompleteDest.EXTERNAL



        AUX I/O Connector

        



    .. py:attribute:: MeasurementCompleteDest.PXI_TRIG0



        PXI Trigger Line 0

        



    .. py:attribute:: MeasurementCompleteDest.PXI_TRIG1



        PXI Trigger Line 1

        



    .. py:attribute:: MeasurementCompleteDest.PXI_TRIG2



        PXI Trigger Line 2

        



    .. py:attribute:: MeasurementCompleteDest.PXI_TRIG3



        PXI Trigger Line 3

        



    .. py:attribute:: MeasurementCompleteDest.PXI_TRIG4



        PXI Trigger Line 4

        



    .. py:attribute:: MeasurementCompleteDest.PXI_TRIG5



        PXI Trigger Line 5

        



    .. py:attribute:: MeasurementCompleteDest.PXI_TRIG6



        PXI Trigger Line 6

        



    .. py:attribute:: MeasurementCompleteDest.PXI_TRIG7



        PXI Trigger Line 7

        



    .. py:attribute:: MeasurementCompleteDest.LBR_TRIG0



        Internal Trigger Line of a PXI/SCXI Combination Chassis

        



OperationMode
-------------

.. py:class:: OperationMode

    .. py:attribute:: OperationMode.IVIDMM



        IviDmm Mode

        



    .. py:attribute:: OperationMode.WAVEFORM



        Waveform acquisition mode

        



RTDType
-------

.. py:class:: RTDType

    .. py:attribute:: RTDType.CUSTOM



        Performs Callendar-Van Dusen RTD scaling with the user-specified A, B,
        and C coefficients.

        



    .. py:attribute:: RTDType.PT3750



        Performs scaling for a Pt 3750 RTD.

        



    .. py:attribute:: RTDType.PT3851



        Performs scaling for a Pt 3851 RTD.

        



    .. py:attribute:: RTDType.PT3911



        Performs scaling for a Pt 3911 RTD.

        



    .. py:attribute:: RTDType.PT3916



        Performs scaling for a Pt 3916 RTD.

        



    .. py:attribute:: RTDType.PT3920



        Performs scaling for a Pt 3920 RTD.

        



    .. py:attribute:: RTDType.PT3928



        Performs scaling for a Pt 3928 RTD.

        



SampleTrigger
-------------

.. py:class:: SampleTrigger

    .. py:attribute:: SampleTrigger.IMMEDIATE



        No Trigger

        



    .. py:attribute:: SampleTrigger.EXTERNAL



        AUX I/O Connector Trigger Line 0

        



    .. py:attribute:: SampleTrigger.SOFTWARE_TRIG



        Software Trigger

        



    .. py:attribute:: SampleTrigger.INTERVAL



        Interval Trigger

        



    .. py:attribute:: SampleTrigger.PXI_TRIG0



        PXI Trigger Line 0

        



    .. py:attribute:: SampleTrigger.PXI_TRIG1



        PXI Trigger Line 1

        



    .. py:attribute:: SampleTrigger.PXI_TRIG2



        PXI Trigger Line 2

        



    .. py:attribute:: SampleTrigger.PXI_TRIG3



        PXI Trigger Line 3

        



    .. py:attribute:: SampleTrigger.PXI_TRIG4



        PXI Trigger Line 4

        



    .. py:attribute:: SampleTrigger.PXI_TRIG5



        PXI Trigger Line 5

        



    .. py:attribute:: SampleTrigger.PXI_TRIG6



        PXI Trigger Line 6

        



    .. py:attribute:: SampleTrigger.PXI_TRIG7



        PXI Trigger Line 7

        



    .. py:attribute:: SampleTrigger.PXI_STAR



        PXI Star Trigger Line

        



    .. py:attribute:: SampleTrigger.AUX_TRIG1



        AUX I/0 Connector Trigger Line 1

        



    .. py:attribute:: SampleTrigger.LBR_TRIG1



        Internal Trigger Line of a PXI/SCXI Combination Chassis

        



ThermistorType
--------------

.. py:class:: ThermistorType

    .. py:attribute:: ThermistorType.CUSTOM



        Custom

        



    .. py:attribute:: ThermistorType.THERMISTOR_44004



        44004

        



    .. py:attribute:: ThermistorType.THERMISTOR_44006



        44006

        



    .. py:attribute:: ThermistorType.THERMISTOR_44007



        44007

        



ThermocoupleReferenceJunctionType
---------------------------------

.. py:class:: ThermocoupleReferenceJunctionType

    .. py:attribute:: ThermocoupleReferenceJunctionType.FIXED



        Thermocouple reference juction is fixed at the user-specified
        temperature.

        



ThermocoupleType
----------------

.. py:class:: ThermocoupleType

    .. py:attribute:: ThermocoupleType.B



        Thermocouple type B

        



    .. py:attribute:: ThermocoupleType.E



        Thermocouple type E

        



    .. py:attribute:: ThermocoupleType.J



        Thermocouple type J

        



    .. py:attribute:: ThermocoupleType.K



        Thermocouple type K

        



    .. py:attribute:: ThermocoupleType.N



        Thermocouple type N

        



    .. py:attribute:: ThermocoupleType.R



        Thermocouple type R

        



    .. py:attribute:: ThermocoupleType.S



        Thermocouple type S

        



    .. py:attribute:: ThermocoupleType.T



        Thermocouple type T

        



TransducerType
--------------

.. py:class:: TransducerType

    .. py:attribute:: TransducerType.THERMOCOUPLE



        Thermocouple

        



    .. py:attribute:: TransducerType.THERMISTOR



        Thermistor

        



    .. py:attribute:: TransducerType.TWO_WIRE_RTD



        2-wire RTD

        



    .. py:attribute:: TransducerType.FOUR_WIRE_RTD



        4-wire RTD

        



TriggerSource
-------------

.. py:class:: TriggerSource

    .. py:attribute:: TriggerSource.IMMEDIATE



        No Trigger

        



    .. py:attribute:: TriggerSource.EXTERNAL



        AUX I/O Connector Trigger Line 0

        



    .. py:attribute:: TriggerSource.SOFTWARE_TRIG



        Software Trigger

        



    .. py:attribute:: TriggerSource.PXI_TRIG0



        PXI Trigger Line 0

        



    .. py:attribute:: TriggerSource.PXI_TRIG1



        PXI Trigger Line 1

        



    .. py:attribute:: TriggerSource.PXI_TRIG2



        PXI Trigger Line 2

        



    .. py:attribute:: TriggerSource.PXI_TRIG3



        PXI Trigger Line 3

        



    .. py:attribute:: TriggerSource.PXI_TRIG4



        PXI Trigger Line 4

        



    .. py:attribute:: TriggerSource.PXI_TRIG5



        PXI Trigger Line 5

        



    .. py:attribute:: TriggerSource.PXI_TRIG6



        PXI Trigger Line 6

        



    .. py:attribute:: TriggerSource.PXI_TRIG7



        PXI Trigger Line 7

        



    .. py:attribute:: TriggerSource.PXI_STAR



        PXI Star Trigger Line

        



    .. py:attribute:: TriggerSource.AUX_TRIG1



        AUX I/O Connector Trigger Line 1

        



    .. py:attribute:: TriggerSource.LBR_TRIG1



        Internal Trigger Line of a PXI/SCXI Combination Chassis

        



WaveformCoupling
----------------

.. py:class:: WaveformCoupling

    .. py:attribute:: WaveformCoupling.AC



        AC Coupled

        



    .. py:attribute:: WaveformCoupling.DC



        DC Coupled

        
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nidmm/errors.rst sha256=b8fe203c5b1b3cb0daa645288d7ddd11fe412186be383dcd2217af584034c7f7 bytes=1880 -->
## FILE: docs/nidmm/errors.rst

- repository: `ni/nimi-python`
- source_path: `docs/nidmm/errors.rst`
- sha256: `b8fe203c5b1b3cb0daa645288d7ddd11fe412186be383dcd2217af584034c7f7`
- bytes: 1880

````rst
Exceptions and Warnings
=======================

Error
-----

    .. py:currentmodule:: nidmm.errors

    .. exception:: Error

        Base exception type that all NI-DMM exceptions derive from


DriverError
-----------

    .. py:currentmodule:: nidmm.errors

    .. exception:: DriverError

        An error originating from the NI-DMM driver


UnsupportedConfigurationError
-----------------------------

    .. py:currentmodule:: nidmm.errors

    .. exception:: UnsupportedConfigurationError

        An error due to using this module in an usupported platform.

DriverNotInstalledError
-----------------------

    .. py:currentmodule:: nidmm.errors

    .. exception:: DriverNotInstalledError

        An error due to using this module without the driver runtime installed.

DriverTooOldError
-----------------

    .. py:currentmodule:: nidmm.errors

    .. exception:: DriverTooOldError

        An error due to using this module with an older version of the NI-DMM driver runtime.

DriverTooNewError
-----------------

    .. py:currentmodule:: nidmm.errors

    .. exception:: DriverTooNewError

        An error due to the NI-DMM driver runtime being too new for this module.

InvalidRepeatedCapabilityError
------------------------------

    .. py:currentmodule:: nidmm.errors

    .. exception:: InvalidRepeatedCapabilityError

        An error due to an invalid character in a repeated capability


SelfTestError
-------------

    .. py:currentmodule:: nidmm.errors

    .. exception:: SelfTestError

        An error due to a failed self-test


RpcError
--------

    .. py:currentmodule:: nidmm.errors

    .. exception:: RpcError

        An error specific to sessions to the NI gRPC Device Server


DriverWarning
-------------

    .. py:currentmodule:: nidmm.errors

    .. exception:: DriverWarning

        A warning originating from the NI-DMM driver
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nidmm/examples.rst sha256=47bd65bae74790e29b415b70fed58c9356aad121f06cf959040bcee6c8670959 bytes=1107 -->
## FILE: docs/nidmm/examples.rst

- repository: `ni/nimi-python`
- source_path: `docs/nidmm/examples.rst`
- sha256: `47bd65bae74790e29b415b70fed58c9356aad121f06cf959040bcee6c8670959`
- bytes: 1107

````rst
Examples
========

`You can download all nidmm examples for latest version here <https://github.com/ni/nimi-python/releases/download/1.4.9/nidmm_examples.zip>`_

nidmm_fetch_waveform.py
-----------------------

.. literalinclude:: ../../src/nidmm/examples/nidmm_fetch_waveform.py
   :language: python
   :linenos:
   :encoding: utf8
   :caption: `(nidmm_fetch_waveform.py) <https://github.com/ni/nimi-python/blob/master/src/nidmm/examples/nidmm_fetch_waveform.py>`_

nidmm_measurement.py
--------------------

.. literalinclude:: ../../src/nidmm/examples/nidmm_measurement.py
   :language: python
   :linenos:
   :encoding: utf8
   :caption: `(nidmm_measurement.py) <https://github.com/ni/nimi-python/blob/master/src/nidmm/examples/nidmm_measurement.py>`_

nidmm_multi_point_measurement.py
--------------------------------

.. literalinclude:: ../../src/nidmm/examples/nidmm_multi_point_measurement.py
   :language: python
   :linenos:
   :encoding: utf8
   :caption: `(nidmm_multi_point_measurement.py) <https://github.com/ni/nimi-python/blob/master/src/nidmm/examples/nidmm_multi_point_measurement.py>`_
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nidmm/grpc_session_options.rst sha256=2afe97fe5c58b2eef43bdf0ec97ec6817fa848189e6989a0c6634022e86030e4 bytes=2884 -->
## FILE: docs/nidmm/grpc_session_options.rst

- repository: `ni/nimi-python`
- source_path: `docs/nidmm/grpc_session_options.rst`
- sha256: `2afe97fe5c58b2eef43bdf0ec97ec6817fa848189e6989a0c6634022e86030e4`
- bytes: 2884

````rst
gRPC Support
============

Support for using NI-DMM over gRPC

.. py:currentmodule:: nidmm



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

        

    :type initialization_behavior: :py:data:`nidmm.SessionInitializationBehavior`
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nidmm/index.rst sha256=6600b7771066548af2bd175a22d4634e4cfcf54f06f42a78a625615070922aeb bytes=682 -->
## FILE: docs/nidmm/index.rst

- repository: `ni/nimi-python`
- source_path: `docs/nidmm/index.rst`
- sha256: `6600b7771066548af2bd175a22d4634e4cfcf54f06f42a78a625615070922aeb`
- bytes: 682

````rst

NI-DMM Python API Documentation
===============================

.. include:: about_nidmm.inc

.. include:: ../_static/contributing.inc

.. include:: ../_static/support.inc

.. toctree::
   :maxdepth: 3
   :caption: Documentation

   nidmm

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

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nidmm/installation.inc sha256=4df17b92d4ed0910aef3786977ad0141511470c2850ddeacd6da1e47bef002e0 bytes=415 -->
## FILE: docs/nidmm/installation.inc

- repository: `ni/nimi-python`
- source_path: `docs/nidmm/installation.inc`
- sha256: `4df17b92d4ed0910aef3786977ad0141511470c2850ddeacd6da1e47bef002e0`
- bytes: 415

````text

.. _nidmm_installation-section:

Installation
------------

As a prerequisite to using the **nidmm** module, you must install the NI-DMM runtime on your system. Visit `ni.com/downloads <http://www.ni.com/downloads/>`_ to download the driver runtime for your devices.

The nimi-python modules (i.e. for **NI-DMM**) can be installed with `pip <http://pypi.python.org/pypi/pip>`_::

  $ python -m pip install nidmm
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nidmm/nidmm.rst sha256=c3f0b633500a0c26fdb1389c9ce67f123e2ce718d77c3aabd10363a498542b4d bytes=121 -->
## FILE: docs/nidmm/nidmm.rst

- repository: `ni/nimi-python`
- source_path: `docs/nidmm/nidmm.rst`
- sha256: `c3f0b633500a0c26fdb1389c9ce67f123e2ce718d77c3aabd10363a498542b4d`
- bytes: 121

````rst
nidmm module
============

.. include:: installation.inc

.. include:: ../_static/nidmm_usage.inc

.. include:: toc.inc
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nidmm/status.inc sha256=771d648009aa7835dfc6fc5ef78c6fd48e30364e900fe07f833094602bbec140 bytes=1871 -->
## FILE: docs/nidmm/status.inc

- repository: `ni/nimi-python`
- source_path: `docs/nidmm/status.inc`
- sha256: `771d648009aa7835dfc6fc5ef78c6fd48e30364e900fe07f833094602bbec140`
- bytes: 1871

````text

NI-DMM Python API Status
------------------------

+-------------------------------+----------------------+
| NI-DMM (nidmm)                |                      |
+===============================+======================+
| Driver Version Tested Against | 2025 Q4              |
+-------------------------------+----------------------+
| PyPI Version                  | |nidmmLatestVersion| |
+-------------------------------+----------------------+
| Supported Python Version      | |nidmmPythonVersion| |
+-------------------------------+----------------------+
| Documentation                 | |nidmmDocs|          |
+-------------------------------+----------------------+
| Open Issues                   | |nidmmOpenIssues|    |
+-------------------------------+----------------------+
| Open Pull Requests            | |nidmmOpenPRs|       |
+-------------------------------+----------------------+


.. |nidmmLatestVersion| image:: http://img.shields.io/pypi/v/nidmm.svg
    :alt: Latest NI-DMM Version
    :target: http://pypi.python.org/pypi/nidmm


.. |nidmmPythonVersion| image:: http://img.shields.io/pypi/pyversions/nidmm.svg
    :alt: NI-DMM supported Python versions
    :target: http://pypi.python.org/pypi/nidmm


.. |nidmmDocs| image:: https://readthedocs.org/projects/nidmm/badge/?version=latest
    :alt: NI-DMM Python API Documentation Status
    :target: https://nidmm.readthedocs.io/en/latest


.. |nidmmOpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python/nidmm.svg
    :alt: Open Issues + Pull Requests for NI-DMM
    :target: https://github.com/ni/nimi-python/issues?q=is%3Aopen+is%3Aissue+label%3Anidmm


.. |nidmmOpenPRs| image:: https://img.shields.io/github/issues-pr/ni/nimi-python/nidmm.svg
    :alt: Pull Requests for NI-DMM
    :target: https://github.com/ni/nimi-python/pulls?q=is%3Aopen+is%3Aissue+label%3Anidmm
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nidmm/toc.inc sha256=a7156341742a8e0bb0b41bdad4a3f12d1f3ed5a38ba09d2ca8b7ac5f36afe060 bytes=109 -->
## FILE: docs/nidmm/toc.inc

- repository: `ni/nimi-python`
- source_path: `docs/nidmm/toc.inc`
- sha256: `a7156341742a8e0bb0b41bdad4a3f12d1f3ed5a38ba09d2ca8b7ac5f36afe060`
- bytes: 109

````text
API Reference
--------------

.. toctree::

   class
   enums
   errors
   examples
   grpc_session_options
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nifgen/.readthedocs.yaml sha256=5ecd370b6acaa8a1693a011c0e4cf5fac5a6c4155baf267d6a5964596606161c bytes=1876 -->
## FILE: docs/nifgen/.readthedocs.yaml

- repository: `ni/nimi-python`
- source_path: `docs/nifgen/.readthedocs.yaml`
- sha256: `5ecd370b6acaa8a1693a011c0e4cf5fac5a6c4155baf267d6a5964596606161c`
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
      # Cancel building pull requests when there aren't changes in any of these paths: docs/_static/ docs/nifgen/.
      #
      # If there are no changes (git diff exits with 0) we force the command to return with 183.
      # This is a special exit code on Read the Docs that will cancel the build immediately.
      - |
        if [ "$READTHEDOCS_VERSION_TYPE" = "external" ] && git diff --quiet origin/master -- docs/_static/ docs/nifgen/;
        then
          exit 183;
        fi

# Have Read the Docs build documentation with Sphinx
sphinx:
  builder: html
  configuration: docs/nifgen/conf.py

# If using Sphinx, optionally build your docs in additional formats such as PDF
formats:
  - epub
  - pdf

# Declare the Python requirements required to build your docs
python:
  install:
  - requirements: docs/requirements.txt
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nifgen/about_nifgen.inc sha256=9ae1c6a4774b9b43cb5a64b33f307ee73c7a84922a92a415da5a6967e8fc93c1 bytes=485 -->
## FILE: docs/nifgen/about_nifgen.inc

- repository: `ni/nimi-python`
- source_path: `docs/nifgen/about_nifgen.inc`
- sha256: `9ae1c6a4774b9b43cb5a64b33f307ee73c7a84922a92a415da5a6967e8fc93c1`
- bytes: 485

````text
.. _about-section:

About
=====

The **nifgen** module provides a Python API for NI-FGEN. The code is maintained in the Open Source repository for `nimi-python <https://github.com/ni/nimi-python>`_.

Support Policy
--------------
**nifgen** supports all the Operating Systems supported by NI-FGEN.

It follows `Python Software Foundation <https://devguide.python.org/#status-of-python-branches>`_ support policy for different versions of CPython.

NI created and supports **nifgen**.
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nifgen/class.rst sha256=7e2d40f0770e351a00c2891faaeab83202ad31014cc8d2cd9aad46049db99a28 bytes=256177 -->
## FILE: docs/nifgen/class.rst

- repository: `ni/nimi-python`
- source_path: `docs/nifgen/class.rst`
- sha256: `7e2d40f0770e351a00c2891faaeab83202ad31014cc8d2cd9aad46049db99a28`
- bytes: 256177

````rst
.. py:module:: nifgen

Session
=======

.. py:class:: Session(self, resource_name, channel_name=None, reset_device=False, options={}, *, grpc_options=None)

    

    Creates and returns a new NI-FGEN session to the specified channel of a
    waveform generator that is used in all subsequent NI-FGEN method
    calls.

    



    :param resource_name:
        

        .. caution:: Traditional NI-DAQ and NI-DAQmx device names are not case-sensitive.
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


    :type resource_name: str

    :param channel_name:
        

        Specifies the channel that this VI uses.

        **Default Value**: "0"

        


    :type channel_name: str, list, range, tuple

    :param reset_device:
        

        Specifies whether you want to reset the device during the initialization
        procedure. True specifies that the device is reset and performs the
        same method as the :py:meth:`nifgen.Session.Reset` method.

        ****Defined Values****

        **Default Value**: False

        +-------+---------------------+
        | True  | Reset device        |
        +-------+---------------------+
        | False | Do not reset device |
        +-------+---------------------+


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

        


    :type grpc_options: nifgen.GrpcSessionOptions


Methods
=======

abort
-----

    .. py:currentmodule:: nifgen.Session

    .. py:method:: abort()

            Aborts any previously initiated signal generation. Call the
            :py:meth:`nifgen.Session.initiate` method to cause the signal generator to
            produce a signal again.

            



allocate_named_waveform
-----------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: allocate_named_waveform(waveform_name, waveform_size)

            Specifies the size of a named waveform up front so that it can be
            allocated in onboard memory before loading the associated data. Data can
            then be loaded in smaller blocks with the niFgen Write (Binary16)
            Waveform methods.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].allocate_named_waveform`

                To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

                Example: :py:meth:`my_session.allocate_named_waveform`


            :param waveform_name:


                Specifies the name to associate with the allocated waveform.

                


            :type waveform_name: str
            :param waveform_size:


                Specifies the size of the waveform to allocate in samples.

                **Default Value**: "4096"

                


            :type waveform_size: int

allocate_waveform
-----------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: allocate_waveform(waveform_size)

            Specifies the size of a waveform so that it can be allocated in onboard
            memory before loading the associated data. Data can then be loaded in
            smaller blocks with the Write Binary 16 Waveform methods.

            

            .. note:: The signal generator must not be in the Generating state when you call
                this method.


            .. tip:: This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].allocate_waveform`

                To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

                Example: :py:meth:`my_session.allocate_waveform`


            :param waveform_size:


                Specifies, in samples, the size of the waveform to allocate.

                


            :type waveform_size: int

            :rtype: int
            :return:


                    The handle that identifies the new waveform. This handle is used later
                    when referring to this waveform.

                    



clear_arb_memory
----------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: clear_arb_memory()

            Removes all previously created arbitrary waveforms, sequences, and
            scripts from the signal generator memory and invalidates all waveform
            handles, sequence handles, and waveform names.

            

            .. note:: The signal generator must not be in the Generating state when you
                call this method.



clear_arb_sequence
------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: clear_arb_sequence(sequence_handle)

            Removes a previously created arbitrary sequence from the signal
            generator memory and invalidates the sequence handle.

            

            .. note:: The signal generator must not be in the Generating state when you
                call this method.



            :param sequence_handle:


                Specifies the handle of the arbitrary sequence that you want the signal
                generator to remove. You can create an arbitrary sequence using the
                :py:meth:`nifgen.Session.create_arb_sequence` or :py:meth:`nifgen.Session.create_advanced_arb_sequence` method.
                These methods return a handle that you use to identify the sequence.

                | **Defined Value**:
                | :py:data:`~nifgen.NIFGEN_VAL_ALL_SEQUENCES`—Remove all sequences from the signal
                  generator

                **Default Value**: None

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type sequence_handle: int

clear_freq_list
---------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: clear_freq_list(frequency_list_handle)

            Removes a previously created frequency list from the signal generator
            memory and invalidates the frequency list handle.

            

            .. note:: The signal generator must not be in the Generating state when you
                call this method.



            :param frequency_list_handle:


                Specifies the handle of the frequency list you want the signal generator
                to remove. You create multiple frequency lists using
                :py:meth:`nifgen.Session.create_freq_list`. :py:meth:`nifgen.Session.create_freq_list` returns a handle that you
                use to identify each list. Specify a value of -1 to clear all frequency
                lists.

                **Defined Value**

                :py:data:`~nifgen.NIFGEN_VAL_ALL_FLISTS`—Remove all frequency lists from the signal
                generator.

                **Default Value**: None

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type frequency_list_handle: int

clear_user_standard_waveform
----------------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: clear_user_standard_waveform()

            Clears the user-defined waveform created by the
            :py:meth:`nifgen.Session.define_user_standard_waveform` method.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].clear_user_standard_waveform`

                To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

                Example: :py:meth:`my_session.clear_user_standard_waveform`


close
-----

    .. py:currentmodule:: nifgen.Session

    .. py:method:: close()

            Performs the following operations:

            -  Closes the instrument I/O session.
            -  Destroys the NI-FGEN session and all of its properties.
            -  Deallocates any memory resources NI-FGEN uses.

            Not all signal routes established by calling the :py:meth:`nifgen.Session.ExportSignal`
            and :py:meth:`nifgen.Session.RouteSignalOut` methods are released when the NI-FGEN
            session is closed. The following table shows what happens to a signal
            route on your device when you call the :py:meth:`nifgen.Session._close` method.

            +--------------------+-------------------+------------------+
            | Routes To          | NI 5401/5411/5431 | Other Devices    |
            +====================+===================+==================+
            | Front Panel        | Remain connected  | Remain connected |
            +--------------------+-------------------+------------------+
            | RTSI/PXI Backplane | Remain connected  | Disconnected     |
            +--------------------+-------------------+------------------+

            .. note:: After calling :py:meth:`nifgen.Session._close`, you cannot use NI-FGEN again until you
                call the :py:meth:`nifgen.Session.init` or :py:meth:`nifgen.Session.InitWithOptions` methods.

            .. note:: This method is not needed when using the session context manager



commit
------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: commit()

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
            -  A subsequent :py:meth:`nifgen.Session.initiate` method can run faster
               because the device is already configured.

            



configure_arb_sequence
----------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: configure_arb_sequence(sequence_handle, gain, offset)

            Configures the signal generator properties that affect arbitrary
            sequence generation. Sets the :py:attr:`nifgen.Session.arb_sequence_handle`,
            :py:attr:`nifgen.Session.arb_gain`, and :py:attr:`nifgen.Session.arb_offset` properties.

            

            .. note:: The signal generator must not be in the Generating state when you call
                this method.


            .. tip:: This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].configure_arb_sequence`

                To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

                Example: :py:meth:`my_session.configure_arb_sequence`


            :param sequence_handle:


                Specifies the handle of the arbitrary sequence that you want the signal
                generator to produce. NI-FGEN sets the
                :py:attr:`nifgen.Session.arb_sequence_handle` property to this value. You can
                create an arbitrary sequence using the :py:meth:`nifgen.Session.create_arb_sequence` or
                :py:meth:`nifgen.Session.create_advanced_arb_sequence` method. These methods return a
                handle that you use to identify the sequence.

                **Default Value**: None

                


            :type sequence_handle: int
            :param gain:


                Specifies the factor by which the signal generator scales the arbitrary
                waveforms in the sequence. When you create an arbitrary waveform, you
                must first normalize the data points to a range of –1.00 to +1.00. You
                can use this parameter to scale the waveform to other ranges. The gain
                is applied before the offset is added.

                For example, to configure the output signal to range from –2.00 to
                +2.00 V, set **gain** to 2.00.

                **Units**: unitless

                **Default Value**: None

                


            :type gain: float
            :param offset:


                Specifies the value the signal generator adds to the arbitrary waveform
                data. When you create arbitrary waveforms, you must first normalize the
                data points to a range of –1.00 to +1.00 V. You can use this parameter
                to shift the range of the arbitrary waveform. NI-FGEN sets the
                :py:attr:`nifgen.Session.arb_offset` property to this value.

                For example, to configure the output signal to range from 0.00 to 2.00 V
                instead of –1.00 to 1.00 V, set the offset to 1.00.

                **Units**: volts

                **Default Value**: None

                


            :type offset: float

configure_arb_waveform
----------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: configure_arb_waveform(waveform_handle, gain, offset)

            Configures the properties of the signal generator that affect arbitrary
            waveform generation. Sets the :py:attr:`nifgen.Session.arb_waveform_handle`,
            :py:attr:`nifgen.Session.arb_gain`, and :py:attr:`nifgen.Session.arb_offset` properties.

            

            .. note:: The signal generator must not be in the Generating state when you call
                this method.


            .. tip:: This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].configure_arb_waveform`

                To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

                Example: :py:meth:`my_session.configure_arb_waveform`


            :param waveform_handle:


                Specifies the handle of the arbitrary waveform you want the signal
                generator to produce. NI-FGEN sets the
                :py:attr:`nifgen.Session.arb_waveform_handle` property to this value. You can
                create an arbitrary waveform using one of the following niFgen Create
                Waveform methods:

                -  :py:meth:`nifgen.Session.create_waveform`
                -  :py:meth:`nifgen.Session.create_waveform`
                -  :py:meth:`nifgen.Session.create_waveform_from_file_i16`
                -  :py:meth:`nifgen.Session.create_waveform_from_file_f64`

                These methods return a handle that you use to identify the waveform.

                **Default Value**: None

                


            :type waveform_handle: int
            :param gain:


                Specifies the factor by which the signal generator scales the arbitrary
                waveforms in the sequence. When you create an arbitrary waveform, you
                must first normalize the data points to a range of –1.00 to +1.00. You
                can use this parameter to scale the waveform to other ranges. The gain
                is applied before the offset is added.

                For example, to configure the output signal to range from –2.00 to
                +2.00 V, set **gain** to 2.00.

                **Units**: unitless

                **Default Value**: None

                


            :type gain: float
            :param offset:


                Specifies the value the signal generator adds to the arbitrary waveform
                data. When you create arbitrary waveforms, you must first normalize the
                data points to a range of –1.00 to +1.00 V. You can use this parameter
                to shift the range of the arbitrary waveform. NI-FGEN sets the
                :py:attr:`nifgen.Session.arb_offset` property to this value.

                For example, to configure the output signal to range from 0.00 to 2.00 V
                instead of –1.00 to 1.00 V, set the offset to 1.00.

                **Units**: volts

                **Default Value**: None

                


            :type offset: float

configure_freq_list
-------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: configure_freq_list(frequency_list_handle, amplitude, dc_offset=0.0, start_phase=0.0)

            Configures the properties of the signal generator that affect frequency
            list generation (the :py:attr:`nifgen.Session.freq_list_handle`,
            :py:attr:`nifgen.Session.func_amplitude`, :py:attr:`nifgen.Session.func_dc_offset`, and
            :py:attr:`nifgen.Session.func_start_phase` properties).

            

            .. note:: The signal generator must not be in the Generating state when you call
                this method.


            .. tip:: This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].configure_freq_list`

                To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

                Example: :py:meth:`my_session.configure_freq_list`


            :param frequency_list_handle:


                Specifies the handle of the frequency list that you want the signal
                generator to produce. NI-FGEN sets the :py:attr:`nifgen.Session.freq_list_handle`
                property to this value. You can create a frequency list using the
                :py:meth:`nifgen.Session.create_freq_list` method, which returns a handle that you use to
                identify the list.
                **Default Value**: None

                


            :type frequency_list_handle: int
            :param amplitude:


                Specifies the amplitude of the standard waveform that you want the
                signal generator to produce. This value is the amplitude at the output
                terminal. NI-FGEN sets the :py:attr:`nifgen.Session.func_amplitude` property to
                this value.

                For example, to produce a waveform ranging from –5.00 V to +5.00 V, set
                the amplitude to 10.00 V.

                **Units**: peak-to-peak voltage

                **Default Value**: None

                

                .. note:: This parameter does not affect signal generator behavior when you set
                    the **waveform** parameter of the :py:meth:`nifgen.Session.configure_standard_waveform`
                    method to :py:data:`~nifgen.Waveform.DC`.


            :type amplitude: float
            :param dc_offset:


                Specifies the DC offset of the standard waveform that you want the
                signal generator to produce. The value is the offset from ground to the
                center of the waveform you specify with the **waveform** parameter,
                observed at the output terminal. For example, to configure a waveform
                with an amplitude of 10.00 V to range from 0.00 V to +10.00 V, set the
                **dcOffset** to 5.00 V. NI-FGEN sets the :py:attr:`nifgen.Session.func_dc_offset`
                property to this value.

                **Units**: volts

                **Default Value**: None

                


            :type dc_offset: float
            :param start_phase:


                Specifies the horizontal offset of the standard waveform you want the
                signal generator to produce. Specify this property in degrees of one
                waveform cycle. NI-FGEN sets the :py:attr:`nifgen.Session.func_start_phase`
                property to this value. A start phase of 180 degrees means output
                generation begins halfway through the waveform. A start phase of 360
                degrees offsets the output by an entire waveform cycle, which is
                identical to a start phase of 0 degrees.

                **Units**: degrees of one cycle

                **Default Value**: None degrees

                

                .. note:: This parameter does not affect signal generator behavior when you set
                    the **waveform** parameter to :py:data:`~nifgen.Waveform.DC`.


            :type start_phase: float

configure_standard_waveform
---------------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: configure_standard_waveform(waveform, amplitude, frequency, dc_offset=0.0, start_phase=0.0)

            Configures the following properties of the signal generator that affect
            standard waveform generation:

            -  :py:attr:`nifgen.Session.func_waveform`
            -  :py:attr:`nifgen.Session.func_amplitude`
            -  :py:attr:`nifgen.Session.func_dc_offset`
            -  :py:attr:`nifgen.Session.func_frequency`
            -  :py:attr:`nifgen.Session.func_start_phase`

            

            .. note:: You must call the :py:meth:`nifgen.Session.ConfigureOutputMode` method with the
                **outputMode** parameter set to :py:data:`~nifgen.OutputMode.FUNC` before calling
                this method.

            .. note:: One or more of the referenced methods are not in the Python API for this driver.


            .. tip:: This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].configure_standard_waveform`

                To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

                Example: :py:meth:`my_session.configure_standard_waveform`


            :param waveform:


                Specifies the standard waveform that you want the signal generator to
                produce. NI-FGEN sets the :py:attr:`nifgen.Session.func_waveform` property to this
                value.

                ****Defined Values****

                **Default Value**: :py:data:`~nifgen.Waveform.SINE`

                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.Waveform.SINE`      | Specifies that the signal generator produces a sinusoid waveform.                                                                                        |
                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.Waveform.SQUARE`    | Specifies that the signal generator produces a square waveform.                                                                                          |
                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.Waveform.TRIANGLE`  | Specifies that the signal generator produces a triangle waveform.                                                                                        |
                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.Waveform.RAMP_UP`   | Specifies that the signal generator produces a positive ramp waveform.                                                                                   |
                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.Waveform.RAMP_DOWN` | Specifies that the signal generator produces a negative ramp waveform.                                                                                   |
                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.Waveform.DC`        | Specifies that the signal generator produces a constant voltage.                                                                                         |
                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.Waveform.NOISE`     | Specifies that the signal generator produces white noise.                                                                                                |
                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.Waveform.USER`      | Specifies that the signal generator produces a user-defined waveform as defined with the :py:meth:`nifgen.Session.define_user_standard_waveform` method. |
                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+


            :type waveform: :py:data:`nifgen.Waveform`
            :param amplitude:


                Specifies the amplitude of the standard waveform that you want the
                signal generator to produce. This value is the amplitude at the output
                terminal. NI-FGEN sets the :py:attr:`nifgen.Session.func_amplitude` property to
                this value.

                For example, to produce a waveform ranging from –5.00 V to +5.00 V, set
                the amplitude to 10.00 V.

                **Units**: peak-to-peak voltage

                **Default Value**: None

                

                .. note:: This parameter does not affect signal generator behavior when you set
                    the **waveform** parameter of the :py:meth:`nifgen.Session.configure_standard_waveform`
                    method to :py:data:`~nifgen.Waveform.DC`.


            :type amplitude: float
            :param frequency:


                | Specifies the frequency of the standard waveform that you want the
                  signal generator to produce. NI-FGEN sets the
                  :py:attr:`nifgen.Session.func_frequency` property to this value.

                **Units**: hertz

                **Default Value**: None

                

                .. note:: This parameter does not affect signal generator behavior when you set
                    the **waveform** parameter of the :py:meth:`nifgen.Session.configure_standard_waveform`
                    method to :py:data:`~nifgen.Waveform.DC`.


            :type frequency: float
            :param dc_offset:


                Specifies the DC offset of the standard waveform that you want the
                signal generator to produce. The value is the offset from ground to the
                center of the waveform you specify with the **waveform** parameter,
                observed at the output terminal. For example, to configure a waveform
                with an amplitude of 10.00 V to range from 0.00 V to +10.00 V, set the
                **dcOffset** to 5.00 V. NI-FGEN sets the :py:attr:`nifgen.Session.func_dc_offset`
                property to this value.

                **Units**: volts

                **Default Value**: None

                


            :type dc_offset: float
            :param start_phase:


                Specifies the horizontal offset of the standard waveform that you want
                the signal generator to produce. Specify this parameter in degrees of
                one waveform cycle. NI-FGEN sets the :py:attr:`nifgen.Session.func_start_phase`
                property to this value. A start phase of 180 degrees means output
                generation begins halfway through the waveform. A start phase of 360
                degrees offsets the output by an entire waveform cycle, which is
                identical to a start phase of 0 degrees.

                **Units**: degrees of one cycle

                **Default Value**: 0.00

                

                .. note:: This parameter does not affect signal generator behavior when you set
                    the **waveform** parameter to :py:data:`~nifgen.Waveform.DC`.


            :type start_phase: float

create_advanced_arb_sequence
----------------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: create_advanced_arb_sequence(waveform_handles_array, loop_counts_array, sample_counts_array=None, marker_location_array=None)

            Creates an arbitrary sequence from an array of waveform handles and an
            array of corresponding loop counts. This method returns a handle that
            identifies the sequence. You pass this handle to the
            :py:meth:`nifgen.Session.configure_arb_sequence` method to specify what arbitrary sequence
            you want the signal generator to produce.

            The :py:meth:`nifgen.Session.create_advanced_arb_sequence` method extends on the
            :py:meth:`nifgen.Session.create_arb_sequence` method by adding the ability to set the
            number of samples in each sequence step and to set marker locations.

            An arbitrary sequence consists of multiple waveforms. For each waveform,
            you specify the number of times the signal generator produces the
            waveform before proceeding to the next waveform. The number of times to
            repeat a specific waveform is called the loop count.

            

            .. note:: The signal generator must not be in the Generating state when you call
                this method.
                You must call the :py:meth:`nifgen.Session.ConfigureOutputMode` method to set the
                **outputMode** parameter to :py:data:`~nifgen.OutputMode.SEQ` before calling this
                method.



            :param waveform_handles_array:


                Specifies the array of waveform handles from which you want to create a
                new arbitrary sequence. The array must have at least as many elements as
                the value that you specify in **sequenceLength**. Each
                **waveformHandlesArray** element has a corresponding **loopCountsArray**
                element that indicates how many times that waveform is repeated. You
                obtain waveform handles when you create arbitrary waveforms with the
                :py:meth:`nifgen.Session.allocate_waveform` method or one of the following niFgen
                CreateWaveform methods:

                -  :py:meth:`nifgen.Session.create_waveform`
                -  :py:meth:`nifgen.Session.create_waveform`
                -  :py:meth:`nifgen.Session.create_waveform_from_file_i16`
                -  :py:meth:`nifgen.Session.create_waveform_from_file_f64`

                **Default Value**: None

                


            :type waveform_handles_array: list of int
            :param loop_counts_array:


                Specifies the array of loop counts you want to use to create a new
                arbitrary sequence. The array must have at least as many elements as the
                value that you specify in the **sequenceLength** parameter. Each
                **loopCountsArray** element corresponds to a **waveformHandlesArray**
                element and indicates how many times to repeat that waveform. Each
                element of the **loopCountsArray** must be less than or equal to the
                maximum number of loop counts that the signal generator allows. You can
                obtain the maximum loop count from **maximumLoopCount** in the
                :py:meth:`nifgen.Session.query_arb_seq_capabilities` method.

                **Default Value**: None

                


            :type loop_counts_array: list of int
            :param sample_counts_array:


                Specifies the array of sample counts that you want to use to create a
                new arbitrary sequence. The array must have at least as many elements as
                the value you specify in the **sequenceLength** parameter. Each
                **sampleCountsArray** element corresponds to a **waveformHandlesArray**
                element and indicates the subset, in samples, of the given waveform to
                generate. Each element of the **sampleCountsArray** must be larger than
                the minimum waveform size, a multiple of the waveform quantum and no
                larger than the number of samples in the corresponding waveform. You can
                obtain these values by calling the :py:meth:`nifgen.Session.query_arb_wfm_capabilities`
                method.

                **Default Value**: None

                


            :type sample_counts_array: list of int
            :param marker_location_array:


                Specifies the array of marker locations to where you want a marker to be
                generated in the sequence. The array must have at least as many elements
                as the value you specify in the **sequenceLength** parameter. Each
                **markerLocationArray** element corresponds to a
                **waveformHandlesArray** element and indicates where in the waveform a
                marker is to generate. The marker location must be less than the size of
                the waveform the marker is in. The markers are coerced to the nearest
                marker quantum and the coerced values are returned in the
                **coercedMarkersArray** parameter.

                If you do not want a marker generated for a particular sequence stage,
                set this parameter to :py:data:`~nifgen.NIFGEN_VAL_NO_MARKER`.

                **Defined Value**: :py:data:`~nifgen.NIFGEN_VAL_NO_MARKER`

                **Default Value**: None

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type marker_location_array: list of int

            :rtype: tuple (coerced_markers_array, sequence_handle)

                WHERE

                coerced_markers_array (list of int): 


                    Returns an array of all given markers that are coerced (rounded) to the
                    nearest marker quantum. Not all devices coerce markers.

                    **Default Value**: None

                    


                sequence_handle (int): 


                    Returns the handle that identifies the new arbitrary sequence. You can
                    pass this handle to :py:meth:`nifgen.Session.configure_arb_sequence` to generate the
                    arbitrary sequence.

                    



create_arb_sequence
-------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: create_arb_sequence(waveform_handles_array, loop_counts_array)

            Creates an arbitrary sequence from an array of waveform handles and an
            array of corresponding loop counts. This method returns a handle that
            identifies the sequence. You pass this handle to the
            :py:meth:`nifgen.Session.configure_arb_sequence` method to specify what arbitrary sequence
            you want the signal generator to produce.

            An arbitrary sequence consists of multiple waveforms. For each waveform,
            you can specify the number of times that the signal generator produces
            the waveform before proceeding to the next waveform. The number of times
            to repeat a specific waveform is called the loop count.

            

            .. note:: You must call the :py:meth:`nifgen.Session.ConfigureOutputMode` method to set the
                **outputMode** parameter to :py:data:`~nifgen.OutputMode.SEQ` before calling this
                method.



            :param waveform_handles_array:


                Specifies the array of waveform handles from which you want to create a
                new arbitrary sequence. The array must have at least as many elements as
                the value that you specify in **sequenceLength**. Each
                **waveformHandlesArray** element has a corresponding **loopCountsArray**
                element that indicates how many times that waveform is repeated. You
                obtain waveform handles when you create arbitrary waveforms with the
                :py:meth:`nifgen.Session.allocate_waveform` method or one of the following niFgen
                CreateWaveform methods:

                -  :py:meth:`nifgen.Session.create_waveform`
                -  :py:meth:`nifgen.Session.create_waveform`
                -  :py:meth:`nifgen.Session.create_waveform_from_file_i16`
                -  :py:meth:`nifgen.Session.create_waveform_from_file_f64`

                **Default Value**: None

                


            :type waveform_handles_array: list of int
            :param loop_counts_array:


                Specifies the array of loop counts you want to use to create a new
                arbitrary sequence. The array must have at least as many elements as the
                value that you specify in the **sequenceLength** parameter. Each
                **loopCountsArray** element corresponds to a **waveformHandlesArray**
                element and indicates how many times to repeat that waveform. Each
                element of the **loopCountsArray** must be less than or equal to the
                maximum number of loop counts that the signal generator allows. You can
                obtain the maximum loop count from **maximumLoopCount** in the
                :py:meth:`nifgen.Session.query_arb_seq_capabilities` method.

                **Default Value**: None

                


            :type loop_counts_array: list of int

            :rtype: int
            :return:


                    Returns the handle that identifies the new arbitrary sequence. You can
                    pass this handle to :py:meth:`nifgen.Session.configure_arb_sequence` to generate the
                    arbitrary sequence.

                    



create_freq_list
----------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: create_freq_list(waveform, frequency_array, duration_array)

            Creates a frequency list from an array of frequencies
            (**frequencyArray**) and an array of durations (**durationArray**). The
            two arrays should have the same number of elements, and this value must
            also be the size of the **frequencyListLength**. The method returns a
            handle that identifies the frequency list (the **frequencyListHandle**).
            You can pass this handle to :py:meth:`nifgen.Session.configure_freq_list` to specify what
            frequency list you want the signal generator to produce.

            A frequency list consists of a list of frequencies and durations. The
            signal generator generates each frequency for the given amount of time
            and then proceeds to the next frequency. When the end of the list is
            reached, the signal generator starts over at the beginning of the list.

            

            .. note:: The signal generator must not be in the Generating state when you call
                this method.



            :param waveform:


                Specifies the standard waveform that you want the signal generator to
                produce. NI-FGEN sets the :py:attr:`nifgen.Session.func_waveform` property to this
                value.

                ****Defined Values****

                **Default Value**: :py:data:`~nifgen.Waveform.SINE`

                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.Waveform.SINE`      | Specifies that the signal generator produces a sinusoid waveform.                                                                                        |
                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.Waveform.SQUARE`    | Specifies that the signal generator produces a square waveform.                                                                                          |
                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.Waveform.TRIANGLE`  | Specifies that the signal generator produces a triangle waveform.                                                                                        |
                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.Waveform.RAMP_UP`   | Specifies that the signal generator produces a positive ramp waveform.                                                                                   |
                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.Waveform.RAMP_DOWN` | Specifies that the signal generator produces a negative ramp waveform.                                                                                   |
                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.Waveform.DC`        | Specifies that the signal generator produces a constant voltage.                                                                                         |
                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.Waveform.NOISE`     | Specifies that the signal generator produces white noise.                                                                                                |
                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.Waveform.USER`      | Specifies that the signal generator produces a user-defined waveform as defined with the :py:meth:`nifgen.Session.define_user_standard_waveform` method. |
                +---------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+


            :type waveform: :py:data:`nifgen.Waveform`
            :param frequency_array:


                Specifies the array of frequencies to form the frequency list. The array
                must have at least as many elements as the value you specify in
                **frequencyListLength**. Each **frequencyArray** element has a
                corresponding **durationArray** element that indicates how long that
                frequency is repeated.

                **Units**: hertz

                **Default Value**: None

                


            :type frequency_array: list of float
            :param duration_array:


                Specifies the array of durations to form the frequency list. The array
                must have at least as many elements as the value that you specify in
                **frequencyListLength**. Each **durationArray** element has a
                corresponding **frequencyArray** element and indicates how long in
                seconds to generate the corresponding frequency.

                **Units**: seconds

                **Default Value**: None

                


            :type duration_array: list of float

            :rtype: int
            :return:


                    Returns the handle that identifies the new frequency list. You can pass
                    this handle to :py:meth:`nifgen.Session.configure_freq_list` to generate the arbitrary
                    sequence.

                    



create_waveform_from_file_f64
-----------------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: create_waveform_from_file_f64(file_name, byte_order)

            This method takes the floating point double (F64) data from the
            specified file and creates an onboard waveform for use in Arbitrary
            Waveform or Arbitrary Sequence output mode. The **waveformHandle**
            returned by this method can later be used for setting the active
            waveform, changing the data in the waveform, building sequences of
            waveforms, or deleting the waveform when it is no longer needed.

            

            .. note:: The F64 data must be between –1.0 and +1.0 V. Use the
                :py:attr:`nifgen.Session.digital_gain` property to generate different voltage
                outputs.


            .. tip:: This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].create_waveform_from_file_f64`

                To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

                Example: :py:meth:`my_session.create_waveform_from_file_f64`


            :param file_name:


                The full path and name of the file where the waveform data resides.

                


            :type file_name: str
            :param byte_order:


                Specifies the byte order of the data in the file.

                ****Defined Values****

                |
                | ****Default Value**:** :py:data:`~nifgen.ByteOrder.LITTLE`

                +-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.ByteOrder.LITTLE` | Little Endian Data—The least significant bit is stored at the lowest address, followed by the other bits, in order of increasing significance. |
                +-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.ByteOrder.BIG`    | Big Endian Data—The most significant bit is stored at the lowest address, followed by the other bits, in order of decreasing significance.     |
                +-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+

                .. note:: Data written by most applications in Windows (including
                    LabWindows™/CVI™) is in Little Endian format. Data written to a file
                    from LabVIEW is in Big Endian format by default on all platforms. Big
                    Endian and Little Endian refer to the way data is stored in memory,
                    which can differ on different processors.


            :type byte_order: :py:data:`nifgen.ByteOrder`

            :rtype: int
            :return:


                    The handle that identifies the new waveform. This handle is used later
                    when referring to this waveform.

                    



create_waveform_from_file_i16
-----------------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: create_waveform_from_file_i16(file_name, byte_order)

            Takes the binary 16-bit signed integer (I16) data from the specified
            file and creates an onboard waveform for use in Arbitrary Waveform or
            Arbitrary Sequence output mode. The **waveformHandle** returned by this
            method can later be used for setting the active waveform, changing the
            data in the waveform, building sequences of waveforms, or deleting the
            waveform when it is no longer needed.

            

            .. note:: The I16 data (values between –32768 and +32767) is assumed to
                represent –1 to +1 V. Use the :py:attr:`nifgen.Session.digital_gain` property to
                generate different voltage outputs.


            .. tip:: This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].create_waveform_from_file_i16`

                To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

                Example: :py:meth:`my_session.create_waveform_from_file_i16`


            :param file_name:


                The full path and name of the file where the waveform data resides.

                


            :type file_name: str
            :param byte_order:


                Specifies the byte order of the data in the file.

                ****Defined Values****

                |
                | ****Default Value**:** :py:data:`~nifgen.ByteOrder.LITTLE`

                +-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.ByteOrder.LITTLE` | Little Endian Data—The least significant bit is stored at the lowest address, followed by the other bits, in order of increasing significance. |
                +-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
                | :py:data:`~nifgen.ByteOrder.BIG`    | Big Endian Data—The most significant bit is stored at the lowest address, followed by the other bits, in order of decreasing significance.     |
                +-------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+

                .. note:: Data written by most applications in Windows (including
                    LabWindows™/CVI™) is in Little Endian format. Data written to a file
                    from LabVIEW is in Big Endian format by default on all platforms. Big
                    Endian and Little Endian refer to the way data is stored in memory,
                    which can differ on different processors.


            :type byte_order: :py:data:`nifgen.ByteOrder`

            :rtype: int
            :return:


                    The handle that identifies the new waveform. This handle is used later
                    when referring to this waveform.

                    



create_waveform_numpy
---------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: create_waveform_numpy(waveform_data_array)

            Creates an onboard waveform for use in Arbitrary Waveform output mode or Arbitrary Sequence output mode.

            

            .. note:: You must set :py:attr:`nifgen.Session.output_mode` to :py:data:`~nifgen.OutputMode.ARB` or :py:data:`~nifgen.OutputMode.SEQ` before calling this method.


            .. tip:: This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].create_waveform`

                To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

                Example: :py:meth:`my_session.create_waveform`


            :param waveform_data_array:


                Array of data for the new arbitrary waveform. This may be an iterable of float or int16, or for best performance a numpy.ndarray of dtype int16 or float64.

                


            :type waveform_data_array: iterable of float or int16

            :rtype: int
            :return:


                    The handle that identifies the new waveform. This handle is used in other methods when referring to this waveform.

                    



define_user_standard_waveform
-----------------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: define_user_standard_waveform(waveform_data_array)

            Defines a user waveform for use in either Standard Method or Frequency
            List output mode.

            To select the waveform, set the **waveform** parameter to
            :py:data:`~nifgen.Waveform.USER` with either the :py:meth:`nifgen.Session.configure_standard_waveform`
            or the :py:meth:`nifgen.Session.create_freq_list` method.

            The waveform data must be scaled between –1.0 and 1.0. Use the
            **amplitude** parameter in the :py:meth:`nifgen.Session.configure_standard_waveform`
            method to generate different output voltages.

            

            .. note:: You must call the :py:meth:`nifgen.Session.ConfigureOutputMode` method to set the
                **outputMode** parameter to :py:data:`~nifgen.OutputMode.FUNC` or
                :py:data:`~nifgen.OutputMode.FREQ_LIST` before calling this method.


            .. tip:: This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].define_user_standard_waveform`

                To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

                Example: :py:meth:`my_session.define_user_standard_waveform`


            :param waveform_data_array:


                Specifies the array of data you want to use for the new arbitrary
                waveform. The array must have at least as many elements as the value
                that you specify in **waveformSize**.

                You must normalize the data points in the array to be between –1.00 and
                +1.00.

                **Default Value**: None

                


            :type waveform_data_array: list of float

delete_script
-------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: delete_script(script_name)

            Deletes the specified script from onboard memory.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].delete_script`

                To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

                Example: :py:meth:`my_session.delete_script`


            :param script_name:


                Specifies the name of the script you want to delete. The script name
                appears in the text of the script following the script keyword.

                


            :type script_name: str

delete_waveform
---------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: delete_waveform(waveform_name_or_handle)

            Removes a previously created arbitrary waveform from the signal generator memory.

            

            .. note:: The signal generator must not be in the Generating state when you call this method.


            .. tip:: This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].delete_waveform`

                To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

                Example: :py:meth:`my_session.delete_waveform`


            :param waveform_name_or_handle:


                The name (str) or handle (int) of an arbitrary waveform previously allocated with :py:meth:`nifgen.Session.allocate_named_waveform`, :py:meth:`nifgen.Session.allocate_waveform` or :py:meth:`nifgen.Session.create_waveform`.

                


            :type waveform_name_or_handle: str or int

disable
-------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: disable()

            Places the instrument in a quiescent state where it has minimal or no
            impact on the system to which it is connected. The analog output and all
            exported signals are disabled.

            



export_attribute_configuration_buffer
-------------------------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: export_attribute_configuration_buffer()

            Exports the property configuration of the session to a configuration
            buffer.

            You can export and import session property configurations only between
            devices with identical model numbers, channel counts, and onboard memory
            sizes.

            This method verifies that the properties you have configured for the
            session are valid. If the configuration is invalid, NI‑FGEN returns an
            error.

            



            :rtype: bytes
            :return:


                    Specifies the byte array buffer to be populated with the exported
                    property configuration.

                    



export_attribute_configuration_file
-----------------------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: export_attribute_configuration_file(file_path)

            Exports the property configuration of the session to the specified
            file.

            You can export and import session property configurations only between
            devices with identical model numbers, channel counts, and onboard memory
            sizes.

            This method verifies that the properties you have configured for the
            session are valid. If the configuration is invalid, NI‑FGEN returns an
            error.

            



            :param file_path:


                Specifies the absolute path to the file to contain the exported
                property configuration. If you specify an empty or relative path, this
                method returns an error.
                **Default file extension:** .nifgenconfig

                


            :type file_path: str

get_channel_name
----------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: get_channel_name(index)

            Returns the channel string that is in the channel table at an index you
            specify.

            

            .. note:: This method is included for compliance with the IviFgen Class
                Specification.



            :param index:


                A 1-based index into the channel table.

                


            :type index: int

            :rtype: str
            :return:


                    Returns the channel string that is in the channel table at the index you
                    specify. Do not modify the contents of the channel string.

                    



get_ext_cal_last_date_and_time
------------------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: get_ext_cal_last_date_and_time()

            Returns the date and time of the last successful external calibration. The time returned is 24-hour (military) local time; for example, if the device was calibrated at 2:30 PM, this method returns 14 for the **hour** parameter and 30 for the **minute** parameter.

            



            :rtype: hightime.datetime
            :return:


                    Indicates date and time of the last calibration.

                    



get_ext_cal_last_temp
---------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: get_ext_cal_last_temp()

            Returns the temperature at the last successful external calibration. The
            temperature is returned in degrees Celsius.

            



            :rtype: float
            :return:


                    Specifies the temperature at the last successful calibration in degrees
                    Celsius.

                    



get_ext_cal_recommended_interval
--------------------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: get_ext_cal_recommended_interval()

            Returns the recommended interval between external calibrations in
            months.

            



            :rtype: hightime.timedelta
            :return:


                    Specifies the recommended interval between external calibrations in
                    months.

                    



get_hardware_state
------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: get_hardware_state()

            Returns the current hardware state of the device and, if the device is
            in the hardware error state, the current hardware error.

            

            .. note:: Hardware states do not necessarily correspond to NI-FGEN states.



            :rtype: :py:data:`nifgen.HardwareState`
            :return:


                    Returns the hardware state of the signal generator.

                    **Defined Values**

                    +------------------------------------------------------------+--------------------------------------------+
                    | :py:data:`~nifgen.HardwareState.IDLE`                      | The device is in the Idle state.           |
                    +------------------------------------------------------------+--------------------------------------------+
                    | :py:data:`~nifgen.HardwareState.WAITING_FOR_START_TRIGGER` | The device is waiting for Start Trigger.   |
                    +------------------------------------------------------------+--------------------------------------------+
                    | :py:data:`~nifgen.HardwareState.RUNNING`                   | The device is in the Running state.        |
                    +------------------------------------------------------------+--------------------------------------------+
                    | :py:data:`~nifgen.HardwareState.DONE`                      | The generation has completed successfully. |
                    +------------------------------------------------------------+--------------------------------------------+
                    | :py:data:`~nifgen.HardwareState.HARDWARE_ERROR`            | There is a hardware error.                 |
                    +------------------------------------------------------------+--------------------------------------------+



get_self_cal_last_date_and_time
-------------------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: get_self_cal_last_date_and_time()

            Returns the date and time of the last successful self-calibration.

            



            :rtype: hightime.datetime
            :return:


                    Returns the date and time the device was last calibrated.

                    



get_self_cal_last_temp
----------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: get_self_cal_last_temp()

            Returns the temperature at the last successful self-calibration. The
            temperature is returned in degrees Celsius.

            



            :rtype: float
            :return:


                    Specifies the temperature at the last successful calibration in degrees
                    Celsius.

                    



get_self_cal_supported
----------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: get_self_cal_supported()

            Returns whether the device supports self–calibration.

            



            :rtype: bool
            :return:


                    Returns whether the device supports self-calibration.

                    ****Defined Values****

                    +-------+------------------------------------+
                    | True  | Self–calibration is supported.     |
                    +-------+------------------------------------+
                    | False | Self–calibration is not supported. |
                    +-------+------------------------------------+



import_attribute_configuration_buffer
-------------------------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: import_attribute_configuration_buffer(configuration)

            Imports a property configuration to the session from the specified
            configuration buffer.

            You can export and import session property configurations only between
            devices with identical model numbers, channel counts, and onboard memory
            sizes.

            

            .. note:: You cannot call this method while the session is in a running state,
                such as while generating a signal.



            :param configuration:


                Specifies the byte array buffer that contains the property
                configuration to import.

                


            :type configuration: bytes

import_attribute_configuration_file
-----------------------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: import_attribute_configuration_file(file_path)

            Imports a property configuration to the session from the specified
            file.

            You can export and import session property configurations only between
            devices with identical model numbers, channel counts, and onboard memory
            sizes.

            

            .. note:: You cannot call this method while the session is in a running state,
                such as while generating a signal.



            :param file_path:


                Specifies the absolute path to the file containing the property
                configuration to import. If you specify an empty or relative path, this
                method returns an error.
                **Default File Extension:** .nifgenconfig

                


            :type file_path: str

initiate
--------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: initiate()

            Initiates signal generation. If you want to abort signal generation,
            call the :py:meth:`nifgen.Session.abort` method. After the signal generation
            is aborted, you can call the :py:meth:`nifgen.Session.initiate` method to
            cause the signal generator to produce a signal again.

            

            .. note:: This method will return a Python context manager that will initiate on entering and abort on exit.



is_done
-------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: is_done()

            Determines whether the current generation is complete. This method
            sets the **done** parameter to True if the session is in the Idle or
            Committed states.

            

            .. note:: NI-FGEN only reports the **done** parameter as True after the
                current generation is complete in Single trigger mode.



            :rtype: bool
            :return:


                    Returns information about the completion of waveform generation.

                    **Defined Values**

                    +-------+-----------------------------+
                    | True  | Generation is complete.     |
                    +-------+-----------------------------+
                    | False | Generation is not complete. |
                    +-------+-----------------------------+



lock
----

    .. py:currentmodule:: nifgen.Session

.. py:method:: lock()

    Obtains a multithread lock on the device session. Before doing so, the
    software waits until all other execution threads release their locks
    on the device session.

    Other threads may have obtained a lock on this session for the
    following reasons:

        -  The application called the :py:meth:`nifgen.Session.lock` method.
        -  A call to NI-FGEN locked the session.
        -  After a call to the :py:meth:`nifgen.Session.lock` method returns
           successfully, no other threads can access the device session until
           you call the :py:meth:`nifgen.Session.unlock` method or exit out of the with block when using
           lock context manager.
        -  Use the :py:meth:`nifgen.Session.lock` method and the
           :py:meth:`nifgen.Session.unlock` method around a sequence of calls to
           instrument driver methods if you require that the device retain its
           settings through the end of the sequence.

    You can safely make nested calls to the :py:meth:`nifgen.Session.lock` method
    within the same thread. To completely unlock the session, you must
    balance each call to the :py:meth:`nifgen.Session.lock` method with a call to
    the :py:meth:`nifgen.Session.unlock` method.

    One method for ensuring there are the same number of unlock method calls as there is lock calls
    is to use lock as a context manager

        .. code:: python

            with nifgen.Session('dev1') as session:
                with session.lock():
                    # Calls to session within a single lock context

        The first `with` block ensures the session is closed regardless of any exceptions raised

        The second `with` block ensures that unlock is called regardless of any exceptions raised

    :rtype: context manager
    :return:
        When used in a `with` statement, :py:meth:`nifgen.Session.lock` acts as
        a context manager and unlock will be called when the `with` block is exited

query_arb_seq_capabilities
--------------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: query_arb_seq_capabilities()

            Returns the properties of the signal generator that are related to
            creating arbitrary sequences (the :py:attr:`nifgen.Session.max_num_sequences`,
            :py:attr:`nifgen.Session.min_sequence_length`,
            :py:attr:`nifgen.Session.max_sequence_length`, and :py:attr:`nifgen.Session.max_loop_count`
            properties).

            



            :rtype: tuple (maximum_number_of_sequences, minimum_sequence_length, maximum_sequence_length, maximum_loop_count)

                WHERE

                maximum_number_of_sequences (int): 


                    Returns the maximum number of arbitrary waveform sequences that the
                    signal generator allows. NI-FGEN obtains this value from the
                    :py:attr:`nifgen.Session.max_num_sequences` property.

                    


                minimum_sequence_length (int): 


                    Returns the minimum number of arbitrary waveforms the signal generator
                    allows in a sequence. NI-FGEN obtains this value from the
                    :py:attr:`nifgen.Session.min_sequence_length` property.

                    


                maximum_sequence_length (int): 


                    Returns the maximum number of arbitrary waveforms the signal generator
                    allows in a sequence. NI-FGEN obtains this value from the
                    :py:attr:`nifgen.Session.max_sequence_length` property.

                    


                maximum_loop_count (int): 


                    Returns the maximum number of times the signal generator can repeat an
                    arbitrary waveform in a sequence. NI-FGEN obtains this value from the
                    :py:attr:`nifgen.Session.max_loop_count` property.

                    



query_arb_wfm_capabilities
--------------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: query_arb_wfm_capabilities()

            Returns the properties of the signal generator that are related to
            creating arbitrary waveforms. These properties are the maximum number of
            waveforms, waveform quantum, minimum waveform size, and maximum waveform
            size.

            

            .. note:: If you do not want to obtain the waveform quantum, pass a value of
                VI_NULL for this parameter.



            :rtype: tuple (maximum_number_of_waveforms, waveform_quantum, minimum_waveform_size, maximum_waveform_size)

                WHERE

                maximum_number_of_waveforms (int): 


                    Returns the maximum number of arbitrary waveforms that the signal
                    generator allows. NI-FGEN obtains this value from the
                    :py:attr:`nifgen.Session.max_num_waveforms` property.

                    


                waveform_quantum (int): 


                    The size (number of points) of each waveform must be a multiple of a
                    constant quantum value. This parameter obtains the quantum value that
                    the signal generator uses. NI-FGEN returns this value from the
                    :py:attr:`nifgen.Session.waveform_quantum` property.

                    For example, when this property returns a value of 8, all waveform
                    sizes must be a multiple of 8.

                    


                minimum_waveform_size (int): 


                    Returns the minimum number of points that the signal generator allows in
                    a waveform. NI-FGEN obtains this value from the
                    :py:attr:`nifgen.Session.min_waveform_size` property.

                    


                maximum_waveform_size (int): 


                    Returns the maximum number of points that the signal generator allows in
                    a waveform. NI-FGEN obtains this value from the
                    :py:attr:`nifgen.Session.max_waveform_size` property.

                    



query_freq_list_capabilities
----------------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: query_freq_list_capabilities()

            Returns the properties of the signal generator that are related to
            creating frequency lists. These properties are
            :py:attr:`nifgen.Session.max_num_freq_lists`,
            :py:attr:`nifgen.Session.min_freq_list_length`,
            :py:attr:`nifgen.Session.max_freq_list_length`,
            :py:attr:`nifgen.Session.min_freq_list_duration`,
            :py:attr:`nifgen.Session.max_freq_list_duration`, and
            :py:attr:`nifgen.Session.freq_list_duration_quantum`.

            



            :rtype: tuple (maximum_number_of_freq_lists, minimum_frequency_list_length, maximum_frequency_list_length, minimum_frequency_list_duration, maximum_frequency_list_duration, frequency_list_duration_quantum)

                WHERE

                maximum_number_of_freq_lists (int): 


                    Returns the maximum number of frequency lists that the signal generator
                    allows. NI-FGEN obtains this value from the
                    :py:attr:`nifgen.Session.max_num_freq_lists` property.

                    


                minimum_frequency_list_length (int): 


                    Returns the minimum number of steps that the signal generator allows in
                    a frequency list. NI-FGEN obtains this value from the
                    :py:attr:`nifgen.Session.min_freq_list_length` property.

                    


                maximum_frequency_list_length (int): 


                    Returns the maximum number of steps that the signal generator allows in
                    a frequency list. NI-FGEN obtains this value from the
                    :py:attr:`nifgen.Session.max_freq_list_length` property.

                    


                minimum_frequency_list_duration (float): 


                    Returns the minimum duration that the signal generator allows in a step
                    of a frequency list. NI-FGEN obtains this value from the
                    :py:attr:`nifgen.Session.min_freq_list_duration` property.

                    


                maximum_frequency_list_duration (float): 


                    Returns the maximum duration that the signal generator allows in a step
                    of a frequency list. NI-FGEN obtains this value from the
                    :py:attr:`nifgen.Session.max_freq_list_duration` property.

                    


                frequency_list_duration_quantum (float): 


                    Returns the quantum of which all durations must be a multiple in a
                    frequency list. NI-FGEN obtains this value from the
                    :py:attr:`nifgen.Session.freq_list_duration_quantum` property.

                    



read_current_temperature
------------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: read_current_temperature()

            Reads the current onboard temperature of the device. The temperature is
            returned in degrees Celsius.

            



            :rtype: float
            :return:


                    Returns the current temperature read from onboard temperature sensors,
                    in degrees Celsius.

                    



reset
-----

    .. py:currentmodule:: nifgen.Session

    .. py:method:: reset()

            Resets the instrument to a known state. This method aborts the
            generation, clears all routes, and resets session properties to the
            default values. This method does not, however, commit the session
            properties or configure the device hardware to its default state.

            

            .. note:: For the NI 5401/5404/5411/5431, this method exhibits the same
                behavior as the :py:meth:`nifgen.Session.reset_device` method.



reset_device
------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: reset_device()

            Performs a hard reset on the device. Generation is stopped, all routes
            are released, external bidirectional terminals are tristated, FPGAs are
            reset, hardware is configured to its default state, and all session
            properties are reset to their default states.

            



reset_with_defaults
-------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: reset_with_defaults()

            Resets the instrument and reapplies initial user–specified settings from
            the logical name that was used to initialize the session. If the session
            was created without a logical name, this method is equivalent to the
            :py:meth:`nifgen.Session.reset` method.

            



self_cal
--------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: self_cal()

            Performs a full internal self-calibration on the device. If the
            calibration is successful, new calibration data and constants are stored
            in the onboard EEPROM.

            



self_test
---------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: self_test()

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

            .. note:: When used on some signal generators, the device is reset after the
                :py:meth:`nifgen.Session.self_test` method runs. If you use the :py:meth:`nifgen.Session.self_test`
                method, your device may not be in its previously configured state
                after the method runs.



send_software_edge_trigger
--------------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: send_software_edge_trigger(trigger, trigger_id)

            Sends a command to trigger the signal generator. This VI can act as an
            override for an external edge trigger.

            

            .. note:: This VI does not override external digital edge triggers of the
                NI 5401/5411/5431.



            :param trigger:


                Trigger specifies the type of software trigger to send

                +-----------------------------------+
                | Defined Values                    |
                +===================================+
                | :py:data:`~nifgen.Trigger.START`  |
                +-----------------------------------+
                | :py:data:`~nifgen.Trigger.SCRIPT` |
                +-----------------------------------+

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type trigger: :py:data:`nifgen.Trigger`
            :param trigger_id:


                Trigger ID specifies the Script Trigger to use for triggering.

                


            :type trigger_id: str

set_next_write_position
-----------------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: set_next_write_position(waveform_name_or_handle, relative_to, offset)

            Sets the position in the waveform at which the next waveform data is
            written. This method allows you to write to arbitrary locations within
            the waveform. These settings apply only to the next write to the
            waveform specified by the waveformHandle parameter. Subsequent writes to
            that waveform begin where the last write left off, unless this method
            is called again. The waveformHandle passed in must have been created by
            a call to the :py:meth:`nifgen.Session.allocate_waveform` method or one of the following
            :py:meth:`nifgen.Session.create_waveform` method.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].set_next_write_position`

                To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

                Example: :py:meth:`my_session.set_next_write_position`


            :param waveform_name_or_handle:


                The name (str) or handle (int) of an arbitrary waveform previously allocated with :py:meth:`nifgen.Session.allocate_named_waveform`, :py:meth:`nifgen.Session.allocate_waveform` or :py:meth:`nifgen.Session.create_waveform`.

                


            :type waveform_name_or_handle: str or int
            :param relative_to:


                Specifies the reference position in the waveform. This position and
                **offset** together determine where to start loading data into the
                waveform.

                ****Defined Values****

                +-------------------------------------------+-------------------------------------------------------------------------+
                | :py:data:`~nifgen.RelativeTo.START` (0)   | Use the start of the waveform as the reference position.                |
                +-------------------------------------------+-------------------------------------------------------------------------+
                | :py:data:`~nifgen.RelativeTo.CURRENT` (1) | Use the current position within the waveform as the reference position. |
                +-------------------------------------------+-------------------------------------------------------------------------+


            :type relative_to: :py:data:`nifgen.RelativeTo`
            :param offset:


                Specifies the offset from **relativeTo** at which to start loading the
                data into the waveform.

                


            :type offset: int

unlock
------

    .. py:currentmodule:: nifgen.Session

.. py:method:: unlock()

    Releases a lock that you acquired on an device session using
    :py:meth:`nifgen.Session.lock`. Refer to :py:meth:`nifgen.Session.unlock` for additional
    information on session locks.

wait_until_done
---------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: wait_until_done(max_time=hightime.timedelta(seconds=10.0))

            Waits until the device is done generating or until the maximum time has
            expired.

            



            :param max_time:


                Specifies the timeout value in milliseconds.

                


            :type max_time: hightime.timedelta, datetime.timedelta, or int in milliseconds

write_script
------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: write_script(script)

            Writes a string containing one or more scripts that govern the
            generation of waveforms.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].write_script`

                To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

                Example: :py:meth:`my_session.write_script`


            :param script:


                Contains the text of the script you want to use for your generation
                operation. Refer to `scripting
                Instructions <REPLACE_DRIVER_SPECIFIC_URL_2(niscripted.chm',%20'scripting_instructions)>`__
                for more information about writing scripts.

                


            :type script: str

write_waveform
--------------

    .. py:currentmodule:: nifgen.Session

    .. py:method:: write_waveform(waveform_name_or_handle, data)

            Writes data to the waveform in onboard memory.

            By default, subsequent calls to this method
            continue writing data from the position of the last sample written. You
            can set the write position and offset by calling the :py:meth:`nifgen.Session.set_next_write_position`
            :py:meth:`nifgen.Session.set_next_write_position` method.

            


            .. tip:: This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
                Use Python index notation on the repeated capabilities container channels to specify a subset,
                and then call this method on the result.

                Example: :py:meth:`my_session.channels[ ... ].write_waveform`

                To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

                Example: :py:meth:`my_session.write_waveform`


            :param waveform_name_or_handle:


                The name (str) or handle (int) of an arbitrary waveform previously allocated with :py:meth:`nifgen.Session.allocate_named_waveform`, :py:meth:`nifgen.Session.allocate_waveform` or :py:meth:`nifgen.Session.create_waveform`.

                


            :type waveform_name_or_handle: str or int
            :param data:


                Array of data to load into the waveform. This may be an iterable of float, or for best performance a numpy.ndarray of dtype int16 or float64.

                


            :type data: list of float


Properties
==========

absolute_delay
--------------

    .. py:attribute:: absolute_delay

        Specifies the sub-Sample Clock delay, in seconds, to apply to the
        waveform. Use this property to reduce the trigger jitter when
        synchronizing multiple devices with NI-TClk. This property can also help
        maintain synchronization repeatability by writing the absolute delay
        value of a previous measurement to the current session.
        To set this property, the waveform generator must be in the Idle
        (Configuration) state.
        **Units**: seconds (s)
        **Valid Values**: Plus or minus half of one Sample Clock period
        **Default Value**: 0.0
        **Supported Waveform Generators**: PXIe-5413/5423/5433



        .. note:: If this property is set, NI-TClk cannot perform any sub-Sample Clock
            adjustment.

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

                - LabVIEW Property: **Output:Absolute Delay**
                - C Attribute: **NIFGEN_ATTR_ABSOLUTE_DELAY**

all_marker_events_latched_status
--------------------------------

    .. py:attribute:: all_marker_events_latched_status

        Returns a bit field of the latched status of all Marker Events.  Write 0 to this property to clear the latched status of all Marker Events.

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

                - LabVIEW Property: **Events:Marker:Advanced:All Marker Events Latched Status**
                - C Attribute: **NIFGEN_ATTR_ALL_MARKER_EVENTS_LATCHED_STATUS**

all_marker_events_live_status
-----------------------------

    .. py:attribute:: all_marker_events_live_status

        Returns a bit field of the live status of all Marker Events.

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

                - LabVIEW Property: **Events:Marker:Advanced:All Marker Events Live Status**
                - C Attribute: **NIFGEN_ATTR_ALL_MARKER_EVENTS_LIVE_STATUS**

analog_data_mask
----------------

    .. py:attribute:: analog_data_mask

        Specifies the mask to apply to the analog output. The masked data is replaced with the data in :py:attr:`nifgen.Session.analog_static_value`.

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

                - LabVIEW Property: **Output:Data Mask:Analog Data Mask**
                - C Attribute: **NIFGEN_ATTR_ANALOG_DATA_MASK**

analog_filter_enabled
---------------------

    .. py:attribute:: analog_filter_enabled

        Controls whether the signal generator applies to an analog filter to the output signal. This property is valid in arbitrary waveform, arbitrary sequence, and script modes. This property can also be used in standard method and frequency list modes for user-defined waveforms.

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

                - LabVIEW Property: **Output:Filters:Analog Filter Enabled**
                - C Attribute: **NIFGEN_ATTR_ANALOG_FILTER_ENABLED**

analog_path
-----------

    .. py:attribute:: analog_path

        Specifies the analog signal path that should be used. The main path allows you to configure gain, offset, analog filter status, output impedance, and output enable. The main path has two amplifier options, high- and low-gain.
        The direct path presents a much smaller gain range, and you cannot adjust offset or the filter status. The direct path also provides a smaller output range but also lower distortion. NI-FGEN normally chooses the amplifier based on the user-specified gain.

        The following table lists the characteristics of this property.

            +-----------------------+------------------+
            | Characteristic        | Value            |
            +=======================+==================+
            | Datatype              | enums.AnalogPath |
            +-----------------------+------------------+
            | Permissions           | read-write       |
            +-----------------------+------------------+
            | Repeated Capabilities | None             |
            +-----------------------+------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Output:Analog Path**
                - C Attribute: **NIFGEN_ATTR_ANALOG_PATH**

analog_static_value
-------------------

    .. py:attribute:: analog_static_value

        Specifies the static value that replaces data masked by :py:attr:`nifgen.Session.analog_data_mask`.

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

                - LabVIEW Property: **Output:Data Mask:Analog Static Value**
                - C Attribute: **NIFGEN_ATTR_ANALOG_STATIC_VALUE**

arb_gain
--------

    .. py:attribute:: arb_gain

        Specifies the factor by which the signal generator scales the arbitrary waveform data. When you create arbitrary waveforms, you must first normalize the data points to the range -1.0 to +1.0. Use this property to scale the arbitrary waveform to other ranges.
        For example, when you set this property to 2.0, the output signal ranges from -2.0 V to +2.0 V.
        Use this property when :py:attr:`nifgen.Session.output_mode` is set to :py:data:`~nifgen.OutputMode.ARB` or :py:data:`~nifgen.OutputMode.SEQ`.




        .. tip:: This property can be set/get on specific channels within your :py:class:`nifgen.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].arb_gain`

            To set/get on all channels, you can call the property directly on the :py:class:`nifgen.Session`.

            Example: :py:attr:`my_session.arb_gain`

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

                - LabVIEW Property: **Arbitrary Waveform:Gain**
                - C Attribute: **NIFGEN_ATTR_ARB_GAIN**

arb_marker_position
-------------------

    .. py:attribute:: arb_marker_position

        Specifies the position for a marker to be asserted in the arbitrary waveform. This property defaults to -1 when no marker position is specified. Use this property when :py:attr:`nifgen.Session.output_mode` is set to :py:data:`~nifgen.OutputMode.ARB`.
        Use :py:meth:`nifgen.Session.ExportSignal` to export the marker signal.



        .. note:: One or more of the referenced methods are not in the Python API for this driver.

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

                - LabVIEW Property: **Arbitrary Waveform:Arbitrary Waveform Mode:Marker Position**
                - C Attribute: **NIFGEN_ATTR_ARB_MARKER_POSITION**

arb_offset
----------

    .. py:attribute:: arb_offset

        Specifies the value that the signal generator adds to the arbitrary waveform data. When you create arbitrary waveforms, you must first normalize the data points to the range -1.0 to +1.0. Use this property to shift the arbitrary waveform range.
        For example, when you set this property to 1.0, the output signal ranges from 2.0 V to 0.0 V.
        Use this property when :py:attr:`nifgen.Session.output_mode` is set to :py:data:`~nifgen.OutputMode.ARB` or :py:data:`~nifgen.OutputMode.SEQ`.
        Units: Volts




        .. tip:: This property can be set/get on specific channels within your :py:class:`nifgen.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].arb_offset`

            To set/get on all channels, you can call the property directly on the :py:class:`nifgen.Session`.

            Example: :py:attr:`my_session.arb_offset`

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

                - LabVIEW Property: **Arbitrary Waveform:Offset**
                - C Attribute: **NIFGEN_ATTR_ARB_OFFSET**

arb_repeat_count
----------------

    .. py:attribute:: arb_repeat_count

        Specifies number of times to repeat the arbitrary waveform when the triggerMode parameter of :py:meth:`nifgen.Session.ConfigureTriggerMode` is set to :py:data:`~nifgen.TriggerMode.SINGLE` or :py:data:`~nifgen.TriggerMode.STEPPED`. This property is ignored if the triggerMode parameter is set to :py:data:`~nifgen.TriggerMode.CONTINUOUS` or :py:data:`~nifgen.TriggerMode.BURST`. Use this property when :py:attr:`nifgen.Session.output_mode` is set to :py:data:`~nifgen.OutputMode.ARB`.
        When used during streaming, this property specifies the number of times to repeat the streaming waveform (the onboard memory allocated for streaming).  For more information about streaming, refer to the Streaming topic.

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

                - LabVIEW Property: **Arbitrary Waveform:Arbitrary Waveform Mode:Repeat Count**
                - C Attribute: **NIFGEN_ATTR_ARB_REPEAT_COUNT**

arb_sample_rate
---------------

    .. py:attribute:: arb_sample_rate

        Specifies the rate at which the signal generator outputs the points in arbitrary waveforms.  Use this property when :py:attr:`nifgen.Session.output_mode` is set  to :py:data:`~nifgen.OutputMode.ARB` or :py:data:`~nifgen.OutputMode.SEQ`.
        Units: Samples/s

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

                - LabVIEW Property: **Clocks:Sample Clock:Rate**
                - C Attribute: **NIFGEN_ATTR_ARB_SAMPLE_RATE**

arb_sequence_handle
-------------------

    .. py:attribute:: arb_sequence_handle

        This channel-based property identifies which sequence the signal generator produces. You can create multiple sequences using :py:meth:`nifgen.Session.create_arb_sequence`. :py:meth:`nifgen.Session.create_arb_sequence` returns a handle that you can use to identify the particular sequence. To configure the signal generator to produce a particular sequence, set this property to the sequence handle.
        Use this property only when :py:attr:`nifgen.Session.output_mode` is set to :py:data:`~nifgen.OutputMode.SEQ`.




        .. tip:: This property can be set/get on specific channels within your :py:class:`nifgen.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].arb_sequence_handle`

            To set/get on all channels, you can call the property directly on the :py:class:`nifgen.Session`.

            Example: :py:attr:`my_session.arb_sequence_handle`

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

                - LabVIEW Property: **Arbitrary Waveform:Arbitrary Sequence Mode:Arbitrary Sequence Handle**
                - C Attribute: **NIFGEN_ATTR_ARB_SEQUENCE_HANDLE**

arb_waveform_handle
-------------------

    .. py:attribute:: arb_waveform_handle

        Selects which arbitrary waveform the signal generator produces. You can create multiple arbitrary waveforms using one of the following niFgen Create Waveform methods:
        :py:meth:`nifgen.Session.create_waveform`
        :py:meth:`nifgen.Session.create_waveform`
        :py:meth:`nifgen.Session.create_waveform_from_file_i16`
        :py:meth:`nifgen.Session.create_waveform_from_file_f64`
        These methods return a handle that you can use to identify the particular waveform. To configure the signal generator to produce a particular waveform, set this property to the waveform handle.
        Use this property only when :py:attr:`nifgen.Session.output_mode` is set to :py:data:`~nifgen.OutputMode.ARB`.




        .. tip:: This property can be set/get on specific channels within your :py:class:`nifgen.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].arb_waveform_handle`

            To set/get on all channels, you can call the property directly on the :py:class:`nifgen.Session`.

            Example: :py:attr:`my_session.arb_waveform_handle`

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

                - LabVIEW Property: **Arbitrary Waveform:Arbitrary Waveform Mode:Arbitrary Waveform Handle**
                - C Attribute: **NIFGEN_ATTR_ARB_WAVEFORM_HANDLE**

aux_power_enabled
-----------------

    .. py:attribute:: aux_power_enabled

        Controls the specified auxiliary power pin. Setting this property to TRUE energizes the auxiliary power when the session is committed. When this property is FALSE, the power pin of the connector outputs no power.

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

                - LabVIEW Property: **Output:Advanced:AUX Power Enabled**
                - C Attribute: **NIFGEN_ATTR_AUX_POWER_ENABLED**

bus_type
--------

    .. py:attribute:: bus_type

        The bus type of the signal generator.

        The following table lists the characteristics of this property.

            +-----------------------+---------------+
            | Characteristic        | Value         |
            +=======================+===============+
            | Datatype              | enums.BusType |
            +-----------------------+---------------+
            | Permissions           | read only     |
            +-----------------------+---------------+
            | Repeated Capabilities | None          |
            +-----------------------+---------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Instrument:Bus Type**
                - C Attribute: **NIFGEN_ATTR_BUS_TYPE**

channel_delay
-------------

    .. py:attribute:: channel_delay

        Specifies, in seconds, the delay to apply to the analog output of the channel specified by the channel string. You can use the channel delay to configure the timing relationship between channels on a multichannel device. Values for this property can be zero or positive. A value of zero indicates that the channels are aligned. A positive value delays the analog output by the specified number of seconds.




        .. tip:: This property can be set/get on specific channels within your :py:class:`nifgen.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].channel_delay`

            To set/get on all channels, you can call the property directly on the :py:class:`nifgen.Session`.

            Example: :py:attr:`my_session.channel_delay`

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

                - LabVIEW Property: **Output:Channel Delay**
                - C Attribute: **NIFGEN_ATTR_CHANNEL_DELAY**

clock_mode
----------

    .. py:attribute:: clock_mode

        Controls which clock mode is used for the signal generator.
        For signal generators that support it, this property allows switching the sample  clock to High-Resolution mode. When in Divide-Down  mode, the sample rate can only be set to certain frequences, based on  dividing down the update clock. However, in High-Resolution mode, the  sample rate may be set to any value.

        The following table lists the characteristics of this property.

            +-----------------------+-----------------+
            | Characteristic        | Value           |
            +=======================+=================+
            | Datatype              | enums.ClockMode |
            +-----------------------+-----------------+
            | Permissions           | read-write      |
            +-----------------------+-----------------+
            | Repeated Capabilities | None            |
            +-----------------------+-----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocks:Sample Clock:Mode**
                - C Attribute: **NIFGEN_ATTR_CLOCK_MODE**

common_mode_offset
------------------

    .. py:attribute:: common_mode_offset

        Specifies, in volts, the value the signal generator adds to or subtracts from the arbitrary waveform data. This property applies only when you set the :py:attr:`nifgen.Session.terminal_configuration` property to :py:data:`~nifgen.TerminalConfiguration.DIFFERENTIAL`. Common mode offset is applied to the signals generated at each differential output terminal.




        .. tip:: This property can be set/get on specific channels within your :py:class:`nifgen.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].common_mode_offset`

            To set/get on all channels, you can call the property directly on the :py:class:`nifgen.Session`.

            Example: :py:attr:`my_session.common_mode_offset`

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

                - LabVIEW Property: **Output:Common Mode Offset**
                - C Attribute: **NIFGEN_ATTR_COMMON_MODE_OFFSET**

data_marker_events_count
------------------------

    .. py:attribute:: data_marker_events_count

        Returns the number of Data Marker Events supported by the device.

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

                - LabVIEW Property: **Instrument:Data Marker Events Count**
                - C Attribute: **NIFGEN_ATTR_DATA_MARKER_EVENTS_COUNT**

data_marker_event_data_bit_number
---------------------------------

    .. py:attribute:: data_marker_event_data_bit_number

        Specifies the bit number to assign to the Data Marker Event.




        .. tip:: This property can be set/get on specific data_markers within your :py:class:`nifgen.Session` instance.
            Use Python index notation on the repeated capabilities container data_markers to specify a subset.

            Example: :py:attr:`my_session.data_markers[ ... ].data_marker_event_data_bit_number`

            To set/get on all data_markers, you can call the property directly on the :py:class:`nifgen.Session`.

            Example: :py:attr:`my_session.data_marker_event_data_bit_number`

        The following table lists the characteristics of this property.

            +-----------------------+--------------+
            | Characteristic        | Value        |
            +=======================+==============+
            | Datatype              | int          |
            +-----------------------+--------------+
            | Permissions           | read-write   |
            +-----------------------+--------------+
            | Repeated Capabilities | data_markers |
            +-----------------------+--------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Data Marker:Data Bit Number**
                - C Attribute: **NIFGEN_ATTR_DATA_MARKER_EVENT_DATA_BIT_NUMBER**

data_marker_event_level_polarity
--------------------------------

    .. py:attribute:: data_marker_event_level_polarity

        Specifies the output polarity of the Data marker event.




        .. tip:: This property can be set/get on specific data_markers within your :py:class:`nifgen.Session` instance.
            Use Python index notation on the repeated capabilities container data_markers to specify a subset.

            Example: :py:attr:`my_session.data_markers[ ... ].data_marker_event_level_polarity`

            To set/get on all data_markers, you can call the property directly on the :py:class:`nifgen.Session`.

            Example: :py:attr:`my_session.data_marker_event_level_polarity`

        The following table lists the characteristics of this property.

            +-----------------------+------------------------------------+
            | Characteristic        | Value                              |
            +=======================+====================================+
            | Datatype              | enums.DataMarkerEventLevelPolarity |
            +-----------------------+------------------------------------+
            | Permissions           | read-write                         |
            +-----------------------+------------------------------------+
            | Repeated Capabilities | data_markers                       |
            +-----------------------+------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Data Marker:Level:Active Level**
                - C Attribute: **NIFGEN_ATTR_DATA_MARKER_EVENT_LEVEL_POLARITY**

data_marker_event_output_terminal
---------------------------------

    .. py:attribute:: data_marker_event_output_terminal

        Specifies the destination terminal for the Data Marker Event.




        .. tip:: This property can be set/get on specific data_markers within your :py:class:`nifgen.Session` instance.
            Use Python index notation on the repeated capabilities container data_markers to specify a subset.

            Example: :py:attr:`my_session.data_markers[ ... ].data_marker_event_output_terminal`

            To set/get on all data_markers, you can call the property directly on the :py:class:`nifgen.Session`.

            Example: :py:attr:`my_session.data_marker_event_output_terminal`

        The following table lists the characteristics of this property.

            +-----------------------+--------------+
            | Characteristic        | Value        |
            +=======================+==============+
            | Datatype              | str          |
            +-----------------------+--------------+
            | Permissions           | read-write   |
            +-----------------------+--------------+
            | Repeated Capabilities | data_markers |
            +-----------------------+--------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Data Marker:Output Terminal**
                - C Attribute: **NIFGEN_ATTR_DATA_MARKER_EVENT_OUTPUT_TERMINAL**

data_transfer_block_size
------------------------

    .. py:attribute:: data_transfer_block_size

        The number of samples at a time to download to onboard memory. Useful when the total data to be transferred to onboard memory is large.

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

                - LabVIEW Property: **Arbitrary Waveform:Data Transfer:Data Transfer Block Size**
                - C Attribute: **NIFGEN_ATTR_DATA_TRANSFER_BLOCK_SIZE**

data_transfer_maximum_bandwidth
-------------------------------

    .. py:attribute:: data_transfer_maximum_bandwidth

        Specifies the maximum amount of bus bandwidth (in bytes per second) to use for data transfers. The signal generator limits data transfer speeds on the PCIe bus to the value you specify for this property. Set this property to optimize bus bandwidth usage for multi-device streaming applications by preventing the signal generator from consuming all of the available bandwidth on a PCI express link when waveforms are being written to the onboard memory of the device.

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

                - LabVIEW Property: **Arbitrary Waveform:Data Transfer:Maximum Bandwidth**
                - C Attribute: **NIFGEN_ATTR_DATA_TRANSFER_MAXIMUM_BANDWIDTH**

data_transfer_maximum_in_flight_reads
-------------------------------------

    .. py:attribute:: data_transfer_maximum_in_flight_reads

        Specifies the maximum number of concurrent PCI Express read requests the signal generator can issue.
        When transferring data from computer memory to device onboard memory across the PCI Express bus, the signal generator can issue multiple memory reads at the same time. In general, the larger the number of read requests, the more efficiently the device uses the bus because the multiple read requests keep the data flowing, even in a PCI Express topology that has high latency due to PCI Express switches in the data path. Most NI devices can issue a large number of read requests (typically 8 or 16). By default, this property is set to the highest value the signal generator supports.
        If other devices in your system cannot tolerate long data latencies, it may be helpful to decrease the number of in-flight read requests the NI signal generator issues. This helps to reduce the amount of data the signal generator reads at one time.

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

                - LabVIEW Property: **Arbitrary Waveform:Data Transfer:Advanced:Maximum In-Flight Read Requests**
                - C Attribute: **NIFGEN_ATTR_DATA_TRANSFER_MAXIMUM_IN_FLIGHT_READS**

data_transfer_preferred_packet_size
-----------------------------------

    .. py:attribute:: data_transfer_preferred_packet_size

        Specifies the preferred size of the data field in a PCI Express read request packet. In general, the larger the packet size, the more efficiently the device uses the bus. By default, NI signal generators use the largest packet size allowed by the system. However, due to different system implementations, some systems may perform better with smaller packet sizes.
        Recommended values for this property are powers of two between 64 and 512.
        In some cases, the signal generator generates packets smaller than  the preferred size you set with this property.
        You cannot change this property while the device is generating a waveform. If you want to change the device configuration, call the :py:meth:`nifgen.Session.abort` method or wait for the generation to complete.



        .. note:: :

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

                - LabVIEW Property: **Arbitrary Waveform:Data Transfer:Advanced:Preferred Packet Size**
                - C Attribute: **NIFGEN_ATTR_DATA_TRANSFER_PREFERRED_PACKET_SIZE**

digital_data_mask
-----------------

    .. py:attribute:: digital_data_mask

        Specifies the mask to apply to the output on the digital connector. The masked data is replaced with the data in :py:attr:`nifgen.Session.digital_static_value`.

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

                - LabVIEW Property: **Output:Data Mask:Digital Data Mask**
                - C Attribute: **NIFGEN_ATTR_DIGITAL_DATA_MASK**

digital_edge_script_trigger_edge
--------------------------------

    .. py:attribute:: digital_edge_script_trigger_edge

        Specifies the active edge for the Script trigger. This property is used when :py:attr:`nifgen.Session.script_trigger_type` is set to Digital Edge.




        .. tip:: This property can be set/get on specific script_triggers within your :py:class:`nifgen.Session` instance.
            Use Python index notation on the repeated capabilities container script_triggers to specify a subset.

            Example: :py:attr:`my_session.script_triggers[ ... ].digital_edge_script_trigger_edge`

            To set/get on all script_triggers, you can call the property directly on the :py:class:`nifgen.Session`.

            Example: :py:attr:`my_session.digital_edge_script_trigger_edge`

        The following table lists the characteristics of this property.

            +-----------------------+------------------------------------+
            | Characteristic        | Value                              |
            +=======================+====================================+
            | Datatype              | enums.ScriptTriggerDigitalEdgeEdge |
            +-----------------------+------------------------------------+
            | Permissions           | read-write                         |
            +-----------------------+------------------------------------+
            | Repeated Capabilities | script_triggers                    |
            +-----------------------+------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Script:Digital Edge:Edge**
                - C Attribute: **NIFGEN_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_EDGE**

digital_edge_script_trigger_source
----------------------------------

    .. py:attribute:: digital_edge_script_trigger_source

        Specifies the source terminal for the Script trigger. This property is used when :py:attr:`nifgen.Session.script_trigger_type` is set to Digital Edge.




        .. tip:: This property can be set/get on specific script_triggers within your :py:class:`nifgen.Session` instance.
            Use Python index notation on the repeated capabilities container script_triggers to specify a subset.

            Example: :py:attr:`my_session.script_triggers[ ... ].digital_edge_script_trigger_source`

            To set/get on all script_triggers, you can call the property directly on the :py:class:`nifgen.Session`.

            Example: :py:attr:`my_session.digital_edge_script_trigger_source`

        The following table lists the characteristics of this property.

            +-----------------------+-----------------+
            | Characteristic        | Value           |
            +=======================+=================+
            | Datatype              | str             |
            +-----------------------+-----------------+
            | Permissions           | read-write      |
            +-----------------------+-----------------+
            | Repeated Capabilities | script_triggers |
            +-----------------------+-----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Script:Digital Edge:Source**
                - C Attribute: **NIFGEN_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_SOURCE**

digital_edge_start_trigger_edge
-------------------------------

    .. py:attribute:: digital_edge_start_trigger_edge

        Specifies the active edge for the Start trigger. This property is used only when :py:attr:`nifgen.Session.start_trigger_type` is set to Digital Edge.

        The following table lists the characteristics of this property.

            +-----------------------+-----------------------------------+
            | Characteristic        | Value                             |
            +=======================+===================================+
            | Datatype              | enums.StartTriggerDigitalEdgeEdge |
            +-----------------------+-----------------------------------+
            | Permissions           | read-write                        |
            +-----------------------+-----------------------------------+
            | Repeated Capabilities | None                              |
            +-----------------------+-----------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Start:Digital Edge:Edge**
                - C Attribute: **NIFGEN_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE**

digital_edge_start_trigger_source
---------------------------------

    .. py:attribute:: digital_edge_start_trigger_source

        Specifies the source terminal for the Start trigger. This property is used only when :py:attr:`nifgen.Session.start_trigger_type` is set to Digital Edge.

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

                - LabVIEW Property: **Triggers:Start:Digital Edge:Source**
                - C Attribute: **NIFGEN_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE**

digital_filter_enabled
----------------------

    .. py:attribute:: digital_filter_enabled

        Controls whether the signal generator applies a digital filter to the output signal. This property is valid in arbitrary waveform, arbitrary sequence, and script modes. This property can also be used in standard method and frequency list modes for user-defined waveforms.

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

                - LabVIEW Property: **Output:Filters:Digital Filter Enabled**
                - C Attribute: **NIFGEN_ATTR_DIGITAL_FILTER_ENABLED**

digital_filter_interpolation_factor
-----------------------------------

    .. py:attribute:: digital_filter_interpolation_factor

        This property only affects the device when :py:attr:`nifgen.Session.digital_filter_enabled` is set to True. If you do not set this property directly, NI-FGEN automatically selects the maximum interpolation factor allowed for the current sample rate. Valid values are 2, 4, and 8.

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

                - LabVIEW Property: **Output:Filters:Digital Filter Interpolation Factor**
                - C Attribute: **NIFGEN_ATTR_DIGITAL_FILTER_INTERPOLATION_FACTOR**

digital_gain
------------

    .. py:attribute:: digital_gain

        Specifies a factor by which the signal generator digitally multiplies generated data before converting it to an analog signal in the DAC. For a digital gain greater than 1.0, the product of digital gain times the generated data must be inside the range plus or minus 1.0 (assuming floating point data).  If the product exceeds these limits, the signal generator clips the output signal, and an error results.
        Some signal generators support both digital gain and an analog gain (analog gain is specified with the :py:attr:`nifgen.Session.func_amplitude` property or the :py:attr:`nifgen.Session.arb_gain` property). Digital gain can be changed during generation without the glitches that may occur when changing analog gains, due to relay switching. However, the DAC output resolution is a method of analog gain, so only analog gain makes full use of the resolution of the DAC.

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

                - LabVIEW Property: **Output:Digital Gain**
                - C Attribute: **NIFGEN_ATTR_DIGITAL_GAIN**

digital_pattern_enabled
-----------------------

    .. py:attribute:: digital_pattern_enabled

        Controls whether the signal generator generates a digital pattern of the output signal.

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

                - LabVIEW Property: **Output:Advanced:Digital Pattern Enabled**
                - C Attribute: **NIFGEN_ATTR_DIGITAL_PATTERN_ENABLED**

digital_static_value
--------------------

    .. py:attribute:: digital_static_value

        Specifies the static value that replaces data masked by :py:attr:`nifgen.Session.digital_data_mask`.

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

                - LabVIEW Property: **Output:Data Mask:Digital Static Value**
                - C Attribute: **NIFGEN_ATTR_DIGITAL_STATIC_VALUE**

done_event_output_terminal
--------------------------

    .. py:attribute:: done_event_output_terminal

        Specifies the destination terminal for the Done Event.

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

                - LabVIEW Property: **Events:Done:Output Terminal**
                - C Attribute: **NIFGEN_ATTR_DONE_EVENT_OUTPUT_TERMINAL**

done_event_pulse_width
----------------------

    .. py:attribute:: done_event_pulse_width

        Specifies the pulse width for the Done Event.

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

                - LabVIEW Property: **Events:Done:Pulse:Width Value**
                - C Attribute: **NIFGEN_ATTR_DONE_EVENT_PULSE_WIDTH**

done_event_pulse_width_units
----------------------------

    .. py:attribute:: done_event_pulse_width_units

        Specifies the pulse width units for the Done Event.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------+
            | Characteristic        | Value                      |
            +=======================+============================+
            | Datatype              | enums.EventPulseWidthUnits |
            +-----------------------+----------------------------+
            | Permissions           | read-write                 |
            +-----------------------+----------------------------+
            | Repeated Capabilities | None                       |
            +-----------------------+----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Done:Pulse:Width Units**
                - C Attribute: **NIFGEN_ATTR_DONE_EVENT_PULSE_WIDTH_UNITS**

driver_setup
------------

    .. py:attribute:: driver_setup

        Specifies the driver setup portion of the option string that was passed into the :py:meth:`nifgen.Session.InitWithOptions` method.



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

                - C Attribute: **NIFGEN_ATTR_DRIVER_SETUP**

exported_onboard_reference_clock_output_terminal
------------------------------------------------

    .. py:attribute:: exported_onboard_reference_clock_output_terminal

        Specifies the terminal to which to export the Onboard Reference Clock.

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

                - LabVIEW Property: **Clocks:Reference Clock:Onboard Reference Clock:Export Output Terminal**
                - C Attribute: **NIFGEN_ATTR_EXPORTED_ONBOARD_REFERENCE_CLOCK_OUTPUT_TERMINAL**

exported_reference_clock_output_terminal
----------------------------------------

    .. py:attribute:: exported_reference_clock_output_terminal

        Specifies the terminal to which to export the Reference Clock.

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

                - LabVIEW Property: **Clocks:Reference Clock:Export Output Terminal**
                - C Attribute: **NIFGEN_ATTR_EXPORTED_REFERENCE_CLOCK_OUTPUT_TERMINAL**

exported_sample_clock_divisor
-----------------------------

    .. py:attribute:: exported_sample_clock_divisor

        Specifies the factor by which to divide the Sample clock, also known as the Update clock, before it is exported.  To export the Sample clock, use the :py:meth:`nifgen.Session.ExportSignal` method or the  :py:attr:`nifgen.Session.exported_sample_clock_output_terminal` property.



        .. note:: One or more of the referenced methods are not in the Python API for this driver.

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

                - LabVIEW Property: **Clocks:Sample Clock:Exported Sample Clock Divisor**
                - C Attribute: **NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_DIVISOR**

exported_sample_clock_output_terminal
-------------------------------------

    .. py:attribute:: exported_sample_clock_output_terminal

        Specifies the terminal to which to export the Sample Clock.

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

                - LabVIEW Property: **Clocks:Sample Clock:Export Output Terminal**
                - C Attribute: **NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL**

exported_sample_clock_timebase_divisor
--------------------------------------

    .. py:attribute:: exported_sample_clock_timebase_divisor

        Specifies the factor by which to divide the sample clock timebase (board clock) before it is exported.  To export the Sample clock timebase, use the :py:meth:`nifgen.Session.ExportSignal` method or the  :py:attr:`nifgen.Session.exported_sample_clock_timebase_output_terminal` property.



        .. note:: One or more of the referenced methods are not in the Python API for this driver.

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

                - LabVIEW Property: **Clocks:Sample Clock Timebase:Exported Sample Clock Timebase Divisor**
                - C Attribute: **NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_TIMEBASE_DIVISOR**

exported_sample_clock_timebase_output_terminal
----------------------------------------------

    .. py:attribute:: exported_sample_clock_timebase_output_terminal

        Specifies the terminal to which to export the Sample clock timebase. If you specify a divisor with the :py:attr:`nifgen.Session.exported_sample_clock_timebase_divisor` property,   the Sample clock exported with the :py:attr:`nifgen.Session.exported_sample_clock_timebase_output_terminal`  property is the value of the Sample clock timebase after it is divided-down.  For a list of the terminals available on your device, refer to the Device Routes tab in MAX.
        To change the device configuration, call :py:meth:`nifgen.Session.abort` or wait for the generation to complete.



        .. note:: The signal generator must not be in the Generating state when you change this property.

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

                - LabVIEW Property: **Clocks:Sample Clock Timebase:Export Output Terminal**
                - C Attribute: **NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_TIMEBASE_OUTPUT_TERMINAL**

exported_script_trigger_output_terminal
---------------------------------------

    .. py:attribute:: exported_script_trigger_output_terminal

        Specifies the output terminal for the exported Script trigger.
        Setting this property to an empty string means that when you commit the session, the signal is removed from that terminal and, if possible, the terminal is tristated.




        .. tip:: This property can be set/get on specific script_triggers within your :py:class:`nifgen.Session` instance.
            Use Python index notation on the repeated capabilities container script_triggers to specify a subset.

            Example: :py:attr:`my_session.script_triggers[ ... ].exported_script_trigger_output_terminal`

            To set/get on all script_triggers, you can call the property directly on the :py:class:`nifgen.Session`.

            Example: :py:attr:`my_session.exported_script_trigger_output_terminal`

        The following table lists the characteristics of this property.

            +-----------------------+-----------------+
            | Characteristic        | Value           |
            +=======================+=================+
            | Datatype              | str             |
            +-----------------------+-----------------+
            | Permissions           | read-write      |
            +-----------------------+-----------------+
            | Repeated Capabilities | script_triggers |
            +-----------------------+-----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Script:Output Terminal**
                - C Attribute: **NIFGEN_ATTR_EXPORTED_SCRIPT_TRIGGER_OUTPUT_TERMINAL**

exported_start_trigger_output_terminal
--------------------------------------

    .. py:attribute:: exported_start_trigger_output_terminal

        Specifies the destination terminal for exporting the Start trigger.

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

                - LabVIEW Property: **Triggers:Start:Output Terminal**
                - C Attribute: **NIFGEN_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL**

external_clock_delay_binary_value
---------------------------------

    .. py:attribute:: external_clock_delay_binary_value

        Binary value of the external clock delay.

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

                - LabVIEW Property: **Clocks:Advanced:External Clock Delay Binary Value**
                - C Attribute: **NIFGEN_ATTR_EXTERNAL_CLOCK_DELAY_BINARY_VALUE**

external_sample_clock_multiplier
--------------------------------

    .. py:attribute:: external_sample_clock_multiplier

        Specifies a multiplication factor to use to obtain a desired sample rate from an external Sample clock.  The resulting sample rate is equal to this factor multiplied by the external Sample clock rate.  You can use this property to generate samples at a rate higher than your external clock rate.  When using this property, you do not need to explicitly set the external clock rate.

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

                - LabVIEW Property: **Clocks:Advanced:External Sample Clock Multiplier**
                - C Attribute: **NIFGEN_ATTR_EXTERNAL_SAMPLE_CLOCK_MULTIPLIER**

file_transfer_block_size
------------------------

    .. py:attribute:: file_transfer_block_size

        The number of samples at a time to read from the file and download to onboard memory. Used in conjunction with the Create From File and Write From File methods.

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

                - LabVIEW Property: **Arbitrary Waveform:Data Transfer:File Transfer Block Size**
                - C Attribute: **NIFGEN_ATTR_FILE_TRANSFER_BLOCK_SIZE**

filter_correction_frequency
---------------------------

    .. py:attribute:: filter_correction_frequency

        Controls the filter correction frequency of the analog filter. This property corrects for the ripples in the analog filter frequency response at the frequency specified. For standard waveform output, the filter correction frequency should be set to be the same as the frequency of the standard waveform. To have no filter correction, set this property to 0 Hz.

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

                - LabVIEW Property: **Instrument:5401/5411/5431:Filter Correction Frequency**
                - C Attribute: **NIFGEN_ATTR_FILTER_CORRECTION_FREQUENCY**

flatness_correction_enabled
---------------------------

    .. py:attribute:: flatness_correction_enabled

        When True, the signal generator applies a flatness correction factor to the generated sine wave in order to ensure the same output power level at all frequencies.
        This property should be set to False when performing Flatness Calibration.

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

                - LabVIEW Property: **Output:Filters:Flatness Correction Enabled**
                - C Attribute: **NIFGEN_ATTR_FLATNESS_CORRECTION_ENABLED**

fpga_bitfile_path
-----------------

    .. py:attribute:: fpga_bitfile_path

        Gets the absolute file path to the bitfile loaded on the FPGA.

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

                - LabVIEW Property: **Instrument:FPGA Bitfile Path**
                - C Attribute: **NIFGEN_ATTR_FPGA_BITFILE_PATH**

freq_list_duration_quantum
--------------------------

    .. py:attribute:: freq_list_duration_quantum

        Returns the quantum of which all durations must be a multiple in a  frequency list.

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

                - LabVIEW Property: **Standard Function:Frequency List Mode:Frequency List Duration Quantum**
                - C Attribute: **NIFGEN_ATTR_FREQ_LIST_DURATION_QUANTUM**

freq_list_handle
----------------

    .. py:attribute:: freq_list_handle

        Sets which frequency list the signal generator  produces. Create a frequency list using :py:meth:`nifgen.Session.create_freq_list`.  :py:meth:`nifgen.Session.create_freq_list` returns a handle that you can  use to identify the list.

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

                - LabVIEW Property: **Standard Function:Frequency List Mode:Frequency List Handle**
                - C Attribute: **NIFGEN_ATTR_FREQ_LIST_HANDLE**

func_amplitude
--------------

    .. py:attribute:: func_amplitude

        Controls the amplitude of the standard waveform that the  signal generator produces. This value is the amplitude at the  output terminal.
        For example, to produce a waveform ranging from -5.00 V to +5.00 V, set  the amplitude to 10.00 V.
        set the Waveform parameter to :py:data:`~nifgen.Waveform.DC`.
        Units: Vpk-pk



        .. note:: This parameter does not affect signal generator behavior when you


        .. tip:: This property can be set/get on specific channels within your :py:class:`nifgen.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].func_amplitude`

            To set/get on all channels, you can call the property directly on the :py:class:`nifgen.Session`.

            Example: :py:attr:`my_session.func_amplitude`

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

                - LabVIEW Property: **Standard Function:Amplitude**
                - C Attribute: **NIFGEN_ATTR_FUNC_AMPLITUDE**

func_buffer_size
----------------

    .. py:attribute:: func_buffer_size

        This property contains the number of samples used in the standard method waveform  buffer. This property is only valid on devices that implement standard method mode  in software, and is read-only for all other devices.
        implementation of Standard Method Mode on your device.



        .. note:: Refer to the Standard Method Mode topic for more information on the

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

                - LabVIEW Property: **Standard Function:Standard Function Mode:Buffer Size**
                - C Attribute: **NIFGEN_ATTR_FUNC_BUFFER_SIZE**

func_dc_offset
--------------

    .. py:attribute:: func_dc_offset

        Controls the DC offset of the standard waveform that the  signal generator produces.  This value is the offset at the output  terminal. The value is the offset from ground to the center of the  waveform that you specify with the Waveform parameter.
        For example, to configure a waveform with an amplitude of 10.00 V to  range from 0.00 V to +10.00 V, set DC Offset to 5.00 V.
        Units: volts




        .. tip:: This property can be set/get on specific channels within your :py:class:`nifgen.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].func_dc_offset`

            To set/get on all channels, you can call the property directly on the :py:class:`nifgen.Session`.

            Example: :py:attr:`my_session.func_dc_offset`

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

                - LabVIEW Property: **Standard Function:DC Offset**
                - C Attribute: **NIFGEN_ATTR_FUNC_DC_OFFSET**

func_duty_cycle_high
--------------------

    .. py:attribute:: func_duty_cycle_high

        Controls the duty cycle of the square wave the signal generator  produces. Specify this property as a percentage of  the time the square wave is high in a cycle.
        set the Waveform parameter to :py:data:`~nifgen.Waveform.SQUARE`.
        Units: Percentage of time the waveform is high



        .. note:: This parameter only affects signal generator behavior when you


        .. tip:: This property can be set/get on specific channels within your :py:class:`nifgen.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].func_duty_cycle_high`

            To set/get on all channels, you can call the property directly on the :py:class:`nifgen.Session`.

            Example: :py:attr:`my_session.func_duty_cycle_high`

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

                - LabVIEW Property: **Standard Function:Duty Cycle High**
                - C Attribute: **NIFGEN_ATTR_FUNC_DUTY_CYCLE_HIGH**

func_frequency
--------------

    .. py:attribute:: func_frequency

        Controls the frequency of the standard waveform that the  signal generator produces.
        Units: hertz
        (1) This parameter does not affect signal generator behavior when you  set the Waveform parameter of the :py:meth:`nifgen.Session.configure_standard_waveform` method  to :py:data:`~nifgen.Waveform.DC`.
        (2) For :py:data:`~nifgen.Waveform.SINE`, the range is between 0 MHz and 16 MHz, but the  range is between 0 MHz and 1 MHz for all other waveforms.



        .. note:: :


        .. tip:: This property can be set/get on specific channels within your :py:class:`nifgen.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].func_frequency`

            To set/get on all channels, you can call the property directly on the :py:class:`nifgen.Session`.

            Example: :py:attr:`my_session.func_frequency`

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

                - LabVIEW Property: **Standard Function:Standard Function Mode:Frequency**
                - C Attribute: **NIFGEN_ATTR_FUNC_FREQUENCY**

func_max_buffer_size
--------------------

    .. py:attribute:: func_max_buffer_size

        This property sets the maximum number of samples that can be used in the standard  method waveform buffer. Increasing this value may increase the quality of  the waveform. This property is only valid on devices that implement standard  method mode in software, and is read-only for all other devices.
        implementation of Standard Method Mode on your device.



        .. note:: Refer to the Standard Method Mode topic for more information on the

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

                - LabVIEW Property: **Standard Function:Standard Function Mode:Maximum Buffer Size**
                - C Attribute: **NIFGEN_ATTR_FUNC_MAX_BUFFER_SIZE**

func_start_phase
----------------

    .. py:attribute:: func_start_phase

        Controls horizontal offset of the standard waveform the  signal generator produces. Specify this property in degrees of  one waveform cycle.
        A start phase of 180 degrees means output generation begins halfway  through the waveform. A start phase of 360 degrees offsets the output by  an entire waveform cycle, which is identical to a start phase of 0  degrees.
        set the Waveform parameter to :py:data:`~nifgen.Waveform.DC`.
        Units: Degrees of one cycle



        .. note:: This parameter does not affect signal generator behavior when you


        .. tip:: This property can be set/get on specific channels within your :py:class:`nifgen.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].func_start_phase`

            To set/get on all channels, you can call the property directly on the :py:class:`nifgen.Session`.

            Example: :py:attr:`my_session.func_start_phase`

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

                - LabVIEW Property: **Standard Function:Start Phase**
                - C Attribute: **NIFGEN_ATTR_FUNC_START_PHASE**

func_waveform
-------------

    .. py:attribute:: func_waveform

        This channel-based property specifies which standard waveform the signal generator produces.
        Use this property only when :py:attr:`nifgen.Session.output_mode` is set to  :py:data:`~nifgen.OutputMode.FUNC`.
        :py:data:`~nifgen.Waveform.SINE`      - Sinusoid waveform
        :py:data:`~nifgen.Waveform.SQUARE`    - Square waveform
        :py:data:`~nifgen.Waveform.TRIANGLE`  - Triangle waveform
        :py:data:`~nifgen.Waveform.RAMP_UP`   - Positive ramp waveform
        :py:data:`~nifgen.Waveform.RAMP_DOWN` - Negative ramp waveform
        :py:data:`~nifgen.Waveform.DC`        - Constant voltage
        :py:data:`~nifgen.Waveform.NOISE`     - White noise
        :py:data:`~nifgen.Waveform.USER`      - User-defined waveform as defined with
        :py:meth:`nifgen.Session.define_user_standard_waveform`




        .. tip:: This property can be set/get on specific channels within your :py:class:`nifgen.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].func_waveform`

            To set/get on all channels, you can call the property directly on the :py:class:`nifgen.Session`.

            Example: :py:attr:`my_session.func_waveform`

        The following table lists the characteristics of this property.

            +-----------------------+----------------+
            | Characteristic        | Value          |
            +=======================+================+
            | Datatype              | enums.Waveform |
            +-----------------------+----------------+
            | Permissions           | read-write     |
            +-----------------------+----------------+
            | Repeated Capabilities | channels       |
            +-----------------------+----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Standard Function:Waveform**
                - C Attribute: **NIFGEN_ATTR_FUNC_WAVEFORM**

idle_behavior
-------------

    .. py:attribute:: idle_behavior

        Specifies the behavior of the output during the Idle state.  The output can be configured to hold the last generated voltage before entering the Idle state or jump to the Idle Value.

        The following table lists the characteristics of this property.

            +-----------------------+--------------------+
            | Characteristic        | Value              |
            +=======================+====================+
            | Datatype              | enums.IdleBehavior |
            +-----------------------+--------------------+
            | Permissions           | read-write         |
            +-----------------------+--------------------+
            | Repeated Capabilities | None               |
            +-----------------------+--------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Output:Advanced:Idle Behavior**
                - C Attribute: **NIFGEN_ATTR_IDLE_BEHAVIOR**

idle_value
----------

    .. py:attribute:: idle_value

        Specifies the value to generate in the Idle state.  The Idle Behavior must be configured to jump to this value.

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

                - LabVIEW Property: **Output:Advanced:Idle Value**
                - C Attribute: **NIFGEN_ATTR_IDLE_VALUE**

instrument_firmware_revision
----------------------------

    .. py:attribute:: instrument_firmware_revision

        A string that contains the firmware revision information  for the device that you are currently using.

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

                - LabVIEW Property: **Instrument:Inherent IVI Attributes:Instrument Identification:Firmware Revision**
                - C Attribute: **NIFGEN_ATTR_INSTRUMENT_FIRMWARE_REVISION**

instrument_manufacturer
-----------------------

    .. py:attribute:: instrument_manufacturer

        A string that contains the name of the device manufacturer you are currently  using.

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

                - LabVIEW Property: **Instrument:Inherent IVI Attributes:Instrument Identification:Manufacturer**
                - C Attribute: **NIFGEN_ATTR_INSTRUMENT_MANUFACTURER**

instrument_model
----------------

    .. py:attribute:: instrument_model

        A string that contains the model number or name of the device that you  are currently using.

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

                - LabVIEW Property: **Instrument:Inherent IVI Attributes:Instrument Identification:Model**
                - C Attribute: **NIFGEN_ATTR_INSTRUMENT_MODEL**

io_resource_descriptor
----------------------

    .. py:attribute:: io_resource_descriptor

        Indicates the resource descriptor that NI-FGEN uses to identify the physical device.
        If you initialize NI-FGEN with a logical name, this  property contains the resource descriptor that corresponds  to the entry in the IVI Configuration Utility.
        If you initialize NI-FGEN with the resource  descriptor, this property contains that value.

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

                - LabVIEW Property: **Instrument:Inherent IVI Attributes:Advanced Session Information:Resource Descriptor**
                - C Attribute: **NIFGEN_ATTR_IO_RESOURCE_DESCRIPTOR**

load_impedance
--------------

    .. py:attribute:: load_impedance

        This channel-based property specifies the load impedance connected to the analog output of the channel. If you set this property to :py:data:`~nifgen.NIFGEN_VAL_MATCHED_LOAD_IMPEDANCE` (-1.0), NI-FGEN assumes that the load impedance matches the output impedance. NI-FGEN compensates to give the desired peak-to-peak voltage amplitude or arbitrary gain (relative to 1 V).



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

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

                - LabVIEW Property: **Output:Load Impedance**
                - C Attribute: **NIFGEN_ATTR_LOAD_IMPEDANCE**

logical_name
------------

    .. py:attribute:: logical_name

        A string containing the logical name that you specified when opening the  current IVI session.
        You may pass a logical name to :py:meth:`nifgen.Session.init` or  :py:meth:`nifgen.Session.InitWithOptions`.  The IVI Configuration Utility must contain an entry for the logical name.   The logical name entry refers to a virtual instrument section in the  IVI Configuration file. The virtual instrument section specifies a physical  device and initial user options.



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

                - LabVIEW Property: **Instrument:Inherent IVI Attributes:Advanced Session Information:Logical Name**
                - C Attribute: **NIFGEN_ATTR_LOGICAL_NAME**

marker_events_count
-------------------

    .. py:attribute:: marker_events_count

        Returns the number of markers supported by the device. Use this property when :py:attr:`nifgen.Session.output_mode` is set to :py:data:`~nifgen.OutputMode.SCRIPT`.

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

                - LabVIEW Property: **Instrument:Marker Events Count**
                - C Attribute: **NIFGEN_ATTR_MARKER_EVENTS_COUNT**

marker_event_output_terminal
----------------------------

    .. py:attribute:: marker_event_output_terminal

        Specifies the destination terminal for the Marker Event.




        .. tip:: This property can be set/get on specific markers within your :py:class:`nifgen.Session` instance.
            Use Python index notation on the repeated capabilities container markers to specify a subset.

            Example: :py:attr:`my_session.markers[ ... ].marker_event_output_terminal`

            To set/get on all markers, you can call the property directly on the :py:class:`nifgen.Session`.

            Example: :py:attr:`my_session.marker_event_output_terminal`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | str        |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | markers    |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Marker:Output Terminal**
                - C Attribute: **NIFGEN_ATTR_MARKER_EVENT_OUTPUT_TERMINAL**

marker_event_pulse_width
------------------------

    .. py:attribute:: marker_event_pulse_width

        Specifies the pulse width for the Marker Event.




        .. tip:: This property can be set/get on specific markers within your :py:class:`nifgen.Session` instance.
            Use Python index notation on the repeated capabilities container markers to specify a subset.

            Example: :py:attr:`my_session.markers[ ... ].marker_event_pulse_width`

            To set/get on all markers, you can call the property directly on the :py:class:`nifgen.Session`.

            Example: :py:attr:`my_session.marker_event_pulse_width`

        The following table lists the characteristics of this property.

            +-----------------------+------------+
            | Characteristic        | Value      |
            +=======================+============+
            | Datatype              | float      |
            +-----------------------+------------+
            | Permissions           | read-write |
            +-----------------------+------------+
            | Repeated Capabilities | markers    |
            +-----------------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Marker:Pulse:Width Value**
                - C Attribute: **NIFGEN_ATTR_MARKER_EVENT_PULSE_WIDTH**

marker_event_pulse_width_units
------------------------------

    .. py:attribute:: marker_event_pulse_width_units

        Specifies the pulse width units for the Marker Event.




        .. tip:: This property can be set/get on specific markers within your :py:class:`nifgen.Session` instance.
            Use Python index notation on the repeated capabilities container markers to specify a subset.

            Example: :py:attr:`my_session.markers[ ... ].marker_event_pulse_width_units`

            To set/get on all markers, you can call the property directly on the :py:class:`nifgen.Session`.

            Example: :py:attr:`my_session.marker_event_pulse_width_units`

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------+
            | Characteristic        | Value                      |
            +=======================+============================+
            | Datatype              | enums.EventPulseWidthUnits |
            +-----------------------+----------------------------+
            | Permissions           | read-write                 |
            +-----------------------+----------------------------+
            | Repeated Capabilities | markers                    |
            +-----------------------+----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Marker:Pulse:Width Units**
                - C Attribute: **NIFGEN_ATTR_MARKER_EVENT_PULSE_WIDTH_UNITS**

max_freq_list_duration
----------------------

    .. py:attribute:: max_freq_list_duration

        Returns the maximum duration of any one step in the frequency  list.

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

                - LabVIEW Property: **Standard Function:Frequency List Mode:Maximum Frequency List Duration**
                - C Attribute: **NIFGEN_ATTR_MAX_FREQ_LIST_DURATION**

max_freq_list_length
--------------------

    .. py:attribute:: max_freq_list_length

        Returns the maximum number of steps that can be in a frequency  list.

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

                - LabVIEW Property: **Standard Function:Frequency List Mode:Maximum Frequency List Length**
                - C Attribute: **NIFGEN_ATTR_MAX_FREQ_LIST_LENGTH**

max_loop_count
--------------

    .. py:attribute:: max_loop_count

        Returns the maximum number of times that the signal generator can repeat a waveform in a sequence. Typically, this value is constant for the signal generator.

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

                - LabVIEW Property: **Arbitrary Waveform:Arbitrary Sequence Mode:Max Loop Count**
                - C Attribute: **NIFGEN_ATTR_MAX_LOOP_COUNT**

max_num_freq_lists
------------------

    .. py:attribute:: max_num_freq_lists

        Returns the maximum number of frequency lists the signal generator allows.

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

                - LabVIEW Property: **Standard Function:Frequency List Mode:Maximum Number Of Frequency Lists**
                - C Attribute: **NIFGEN_ATTR_MAX_NUM_FREQ_LISTS**

max_num_sequences
-----------------

    .. py:attribute:: max_num_sequences

        Returns the maximum number of arbitrary sequences that the signal generator allows. Typically, this value is constant for the signal generator.

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

                - LabVIEW Property: **Arbitrary Waveform:Arbitrary Sequence Mode:Max Number of Sequences**
                - C Attribute: **NIFGEN_ATTR_MAX_NUM_SEQUENCES**

max_num_waveforms
-----------------

    .. py:attribute:: max_num_waveforms

        Returns the maximum number of arbitrary waveforms that the signal generator allows. Typically, this value is constant for the signal generator.

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

                - LabVIEW Property: **Arbitrary Waveform:Capabilities:Max Number of Waveforms**
                - C Attribute: **NIFGEN_ATTR_MAX_NUM_WAVEFORMS**

max_sequence_length
-------------------

    .. py:attribute:: max_sequence_length

        Returns the maximum number of arbitrary waveforms that the signal generator allows in a sequence. Typically, this value is constant for the signal generator.

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

                - LabVIEW Property: **Arbitrary Waveform:Arbitrary Sequence Mode:Max Sequence Length**
                - C Attribute: **NIFGEN_ATTR_MAX_SEQUENCE_LENGTH**

max_waveform_size
-----------------

    .. py:attribute:: max_waveform_size

        Returns the size, in samples, of the largest waveform that can be created. This property reflects the space currently available, taking into account previously allocated waveforms and instructions.

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

                - LabVIEW Property: **Arbitrary Waveform:Capabilities:Max Waveform Size**
                - C Attribute: **NIFGEN_ATTR_MAX_WAVEFORM_SIZE**

memory_size
-----------

    .. py:attribute:: memory_size

        The total amount of memory, in bytes, on the signal generator.

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

                - LabVIEW Property: **Instrument:Memory Size**
                - C Attribute: **NIFGEN_ATTR_MEMORY_SIZE**

min_freq_list_duration
----------------------

    .. py:attribute:: min_freq_list_duration

        Returns the minimum number of steps that can be in a frequency  list.

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

                - LabVIEW Property: **Standard Function:Frequency List Mode:Minimum Frequency List Duration**
                - C Attribute: **NIFGEN_ATTR_MIN_FREQ_LIST_DURATION**

min_freq_list_length
--------------------

    .. py:attribute:: min_freq_list_length

        Returns the minimum number of frequency lists that the signal generator allows.

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

                - LabVIEW Property: **Standard Function:Frequency List Mode:Minimum Frequency List Length**
                - C Attribute: **NIFGEN_ATTR_MIN_FREQ_LIST_LENGTH**

min_sequence_length
-------------------

    .. py:attribute:: min_sequence_length

        Returns the minimum number of arbitrary waveforms that the signal generator allows in a sequence. Typically, this value is constant for the signal generator.

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

                - LabVIEW Property: **Arbitrary Waveform:Arbitrary Sequence Mode:Min Sequence Length**
                - C Attribute: **NIFGEN_ATTR_MIN_SEQUENCE_LENGTH**

min_waveform_size
-----------------

    .. py:attribute:: min_waveform_size

        Returns the minimum number of points that the signal generator allows in an arbitrary waveform. Typically, this value is constant for the signal generator.

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

                - LabVIEW Property: **Arbitrary Waveform:Capabilities:Min Waveform Size**
                - C Attribute: **NIFGEN_ATTR_MIN_WAVEFORM_SIZE**

module_revision
---------------

    .. py:attribute:: module_revision

        A string that contains the module revision  for the device that you are currently using.

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

                - LabVIEW Property: **Instrument:Inherent IVI Attributes:Instrument Identification:Module Revision**
                - C Attribute: **NIFGEN_ATTR_MODULE_REVISION**

channel_count
-------------

    .. py:attribute:: channel_count

        Indicates the number of channels that the specific instrument  driver supports.
        For each property for which IVI_VAL_MULTI_CHANNEL is set, the IVI Engine maintains a separate cache value for each channel.

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

                - LabVIEW Property: **Instrument:Inherent IVI Attributes:Driver Capabilities:Channel Count**
                - C Attribute: **NIFGEN_ATTR_NUM_CHANNELS**

output_enabled
--------------

    .. py:attribute:: output_enabled

        This channel-based property specifies whether the signal that the signal generator produces appears at the output connector.




        .. tip:: This property can be set/get on specific channels within your :py:class:`nifgen.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].output_enabled`

            To set/get on all channels, you can call the property directly on the :py:class:`nifgen.Session`.

            Example: :py:attr:`my_session.output_enabled`

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

                - LabVIEW Property: **Output:Output Enabled**
                - C Attribute: **NIFGEN_ATTR_OUTPUT_ENABLED**

output_impedance
----------------

    .. py:attribute:: output_impedance

        This channel-based property specifies the signal generator output impedance at the output connector. NI signal sources modules have an output impedance of 50 ohms and an optional 75 ohms on select modules. If the load impedance matches the output impedance, then the voltage at the signal output connector is at the needed level. The voltage at the signal output connector varies with load output impedance, up to doubling the voltage for a high-impedance load.




        .. tip:: This property can be set/get on specific channels within your :py:class:`nifgen.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].output_impedance`

            To set/get on all channels, you can call the property directly on the :py:class:`nifgen.Session`.

            Example: :py:attr:`my_session.output_impedance`

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

                - LabVIEW Property: **Output:Output Impedance**
                - C Attribute: **NIFGEN_ATTR_OUTPUT_IMPEDANCE**

output_mode
-----------

    .. py:attribute:: output_mode

        Sets which output mode the signal generator will use. The value you specify determines which methods and properties you use to configure the waveform the signal generator produces.



        .. note:: The signal generator must not be in the Generating state when you change this property. To change the device configuration, call :py:meth:`nifgen.Session.abort` or wait for the generation to complete.

        The following table lists the characteristics of this property.

            +-----------------------+------------------+
            | Characteristic        | Value            |
            +=======================+==================+
            | Datatype              | enums.OutputMode |
            +-----------------------+------------------+
            | Permissions           | read-write       |
            +-----------------------+------------------+
            | Repeated Capabilities | None             |
            +-----------------------+------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Output:Output Mode**
                - C Attribute: **NIFGEN_ATTR_OUTPUT_MODE**

ready_for_start_event_output_terminal
-------------------------------------

    .. py:attribute:: ready_for_start_event_output_terminal

        Specifies the destination terminal for the Ready for Start Event.

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

                - LabVIEW Property: **Events:Ready For Start:Output Terminal**
                - C Attribute: **NIFGEN_ATTR_READY_FOR_START_EVENT_OUTPUT_TERMINAL**

reference_clock_source
----------------------

    .. py:attribute:: reference_clock_source

        Specifies the reference clock source used by the signal generator.
        The signal generator derives the frequencies and sample rates that it uses  to generate waveforms from the source you specify.  For example, when you set this property to ClkIn, the signal  generator uses the signal it receives at the CLK IN front  panel connector as the Reference clock.
        To change the device configuration, call :py:meth:`nifgen.Session.abort` or wait for the generation to complete.



        .. note:: The signal generator must not be in the Generating state when you change this property.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------+
            | Characteristic        | Value                      |
            +=======================+============================+
            | Datatype              | enums.ReferenceClockSource |
            +-----------------------+----------------------------+
            | Permissions           | read-write                 |
            +-----------------------+----------------------------+
            | Repeated Capabilities | None                       |
            +-----------------------+----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocks:Reference Clock:Source**
                - C Attribute: **NIFGEN_ATTR_REFERENCE_CLOCK_SOURCE**

ref_clock_frequency
-------------------

    .. py:attribute:: ref_clock_frequency

        Sets the frequency of the signal generator reference  clock. The signal generator uses the reference clock to derive  frequencies and sample rates when generating output.

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

                - LabVIEW Property: **Clocks:Reference Clock:Frequency**
                - C Attribute: **NIFGEN_ATTR_REF_CLOCK_FREQUENCY**

sample_clock_source
-------------------

    .. py:attribute:: sample_clock_source

        Specifies the Sample clock source. If you specify a divisor with the :py:attr:`nifgen.Session.exported_sample_clock_divisor`  property, the Sample clock exported with the :py:attr:`nifgen.Session.exported_sample_clock_output_terminal` property is the  value of the Sample clock after it is divided-down. For a list of the terminals available on your device, refer  to the Device Routes tab in MAX.
        To change the device configuration, call :py:meth:`nifgen.Session.abort` or wait for the generation to complete.



        .. note:: The signal generator must not be in the Generating state when you change this property.

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------+
            | Characteristic        | Value                   |
            +=======================+=========================+
            | Datatype              | enums.SampleClockSource |
            +-----------------------+-------------------------+
            | Permissions           | read-write              |
            +-----------------------+-------------------------+
            | Repeated Capabilities | None                    |
            +-----------------------+-------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocks:Sample Clock:Source**
                - C Attribute: **NIFGEN_ATTR_SAMPLE_CLOCK_SOURCE**

sample_clock_timebase_rate
--------------------------

    .. py:attribute:: sample_clock_timebase_rate

        Specifies the Sample clock timebase rate. This property applies only to external Sample clock timebases.
        To change the device configuration, call :py:meth:`nifgen.Session.abort` or wait for the generation to complete.



        .. note:: The signal generator must not be in the Generating state when you change this property.

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

                - LabVIEW Property: **Clocks:Sample Clock Timebase:Rate**
                - C Attribute: **NIFGEN_ATTR_SAMPLE_CLOCK_TIMEBASE_RATE**

sample_clock_timebase_source
----------------------------

    .. py:attribute:: sample_clock_timebase_source

        Specifies the Sample Clock Timebase source.
        To change the device configuration, call the :py:meth:`nifgen.Session.abort` method or wait for the generation to complete.



        .. note:: The signal generator must not be in the Generating state when you change this property.

        The following table lists the characteristics of this property.

            +-----------------------+---------------------------------+
            | Characteristic        | Value                           |
            +=======================+=================================+
            | Datatype              | enums.SampleClockTimebaseSource |
            +-----------------------+---------------------------------+
            | Permissions           | read-write                      |
            +-----------------------+---------------------------------+
            | Repeated Capabilities | None                            |
            +-----------------------+---------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocks:Sample Clock Timebase:Source**
                - C Attribute: **NIFGEN_ATTR_SAMPLE_CLOCK_TIMEBASE_SOURCE**

script_to_generate
------------------

    .. py:attribute:: script_to_generate

        Specifies which script the generator produces. To configure the generator to run a particular script, set this property to the name of the script. Use :py:meth:`nifgen.Session.write_script` to create multiple scripts. Use this property when :py:attr:`nifgen.Session.output_mode` is set to :py:data:`~nifgen.OutputMode.SCRIPT`.



        .. note:: The signal generator must not be in the Generating state when you change this property. To change the device configuration, call :py:meth:`nifgen.Session.abort` or wait for the generation to complete.

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

                - LabVIEW Property: **Arbitrary Waveform:Script Mode:Script to Generate**
                - C Attribute: **NIFGEN_ATTR_SCRIPT_TO_GENERATE**

script_triggers_count
---------------------

    .. py:attribute:: script_triggers_count

        Specifies the number of Script triggers supported by the device. Use this property when :py:attr:`nifgen.Session.output_mode` is set to :py:data:`~nifgen.OutputMode.SCRIPT`.

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

                - LabVIEW Property: **Instrument:Script Triggers Count**
                - C Attribute: **NIFGEN_ATTR_SCRIPT_TRIGGERS_COUNT**

script_trigger_type
-------------------

    .. py:attribute:: script_trigger_type

        Specifies the Script trigger type. Depending upon the value of this property, additional properties may need to be configured to fully configure the trigger.




        .. tip:: This property can be set/get on specific script_triggers within your :py:class:`nifgen.Session` instance.
            Use Python index notation on the repeated capabilities container script_triggers to specify a subset.

            Example: :py:attr:`my_session.script_triggers[ ... ].script_trigger_type`

            To set/get on all script_triggers, you can call the property directly on the :py:class:`nifgen.Session`.

            Example: :py:attr:`my_session.script_trigger_type`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------------+
            | Characteristic        | Value                   |
            +=======================+=========================+
            | Datatype              | enums.ScriptTriggerType |
            +-----------------------+-------------------------+
            | Permissions           | read-write              |
            +-----------------------+-------------------------+
            | Repeated Capabilities | script_triggers         |
            +-----------------------+-------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Script:Trigger Type**
                - C Attribute: **NIFGEN_ATTR_SCRIPT_TRIGGER_TYPE**

serial_number
-------------

    .. py:attribute:: serial_number

        The signal generator's serial number.

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

                - LabVIEW Property: **Instrument:Serial Number**
                - C Attribute: **NIFGEN_ATTR_SERIAL_NUMBER**

simulate
--------

    .. py:attribute:: simulate

        Specifies whether to simulate NI-FGEN I/O  operations. If simulation is enabled, NI-FGEN  methods perform range checking and call Ivi_GetAttribute and  Ivi_SetAttribute, but they do not perform device I/O.   For output parameters that represent device data, NI-FGEN  methods return calculated values.
        Default Value: False
        Use :py:meth:`nifgen.Session.InitWithOptions` to override default value.



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

                - LabVIEW Property: **Instrument:Inherent IVI Attributes:User Options:Simulate**
                - C Attribute: **NIFGEN_ATTR_SIMULATE**

specific_driver_description
---------------------------

    .. py:attribute:: specific_driver_description

        Returns a brief description of NI-FGEN.

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

                - LabVIEW Property: **Instrument:Inherent IVI Attributes:Driver Identification:Description**
                - C Attribute: **NIFGEN_ATTR_SPECIFIC_DRIVER_DESCRIPTION**

major_version
-------------

    .. py:attribute:: major_version

        Returns the major version number of NI-FGEN.

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

                - LabVIEW Property: **Instrument:Obsolete:Major Version**
                - C Attribute: **NIFGEN_ATTR_SPECIFIC_DRIVER_MAJOR_VERSION**

minor_version
-------------

    .. py:attribute:: minor_version

        Returns the minor version number of NI-FGEN.

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

                - LabVIEW Property: **Instrument:Obsolete:Minor Version**
                - C Attribute: **NIFGEN_ATTR_SPECIFIC_DRIVER_MINOR_VERSION**

specific_driver_revision
------------------------

    .. py:attribute:: specific_driver_revision

        A string that contains additional version information about  NI-FGEN.

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

                - LabVIEW Property: **Instrument:Inherent IVI Attributes:Driver Identification:Revision**
                - C Attribute: **NIFGEN_ATTR_SPECIFIC_DRIVER_REVISION**

specific_driver_vendor
----------------------

    .. py:attribute:: specific_driver_vendor

        A string that contains the name of the vendor that supplies NI-FGEN.

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

                - LabVIEW Property: **Instrument:Inherent IVI Attributes:Driver Identification:Driver Vendor**
                - C Attribute: **NIFGEN_ATTR_SPECIFIC_DRIVER_VENDOR**

started_event_output_terminal
-----------------------------

    .. py:attribute:: started_event_output_terminal

        Specifies the destination terminal for the Started Event.

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

                - LabVIEW Property: **Events:Started:Output Terminal**
                - C Attribute: **NIFGEN_ATTR_STARTED_EVENT_OUTPUT_TERMINAL**

started_event_pulse_width
-------------------------

    .. py:attribute:: started_event_pulse_width

        Specifies the pulse width for the Started Event.

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

                - LabVIEW Property: **Events:Started:Pulse:Width Value**
                - C Attribute: **NIFGEN_ATTR_STARTED_EVENT_PULSE_WIDTH**

started_event_pulse_width_units
-------------------------------

    .. py:attribute:: started_event_pulse_width_units

        Specifies the pulse width units for the Started Event.

        The following table lists the characteristics of this property.

            +-----------------------+----------------------------+
            | Characteristic        | Value                      |
            +=======================+============================+
            | Datatype              | enums.EventPulseWidthUnits |
            +-----------------------+----------------------------+
            | Permissions           | read-write                 |
            +-----------------------+----------------------------+
            | Repeated Capabilities | None                       |
            +-----------------------+----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Events:Started:Pulse:Width Units**
                - C Attribute: **NIFGEN_ATTR_STARTED_EVENT_PULSE_WIDTH_UNITS**

start_trigger_type
------------------

    .. py:attribute:: start_trigger_type

        Specifies whether you want the Start trigger to be a Digital Edge, or Software trigger. You can also choose None as the value for this property.

        The following table lists the characteristics of this property.

            +-----------------------+------------------------+
            | Characteristic        | Value                  |
            +=======================+========================+
            | Datatype              | enums.StartTriggerType |
            +-----------------------+------------------------+
            | Permissions           | read-write             |
            +-----------------------+------------------------+
            | Repeated Capabilities | None                   |
            +-----------------------+------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Start:Trigger Type**
                - C Attribute: **NIFGEN_ATTR_START_TRIGGER_TYPE**

streaming_space_available_in_waveform
-------------------------------------

    .. py:attribute:: streaming_space_available_in_waveform

        Indicates the space available (in samples) in the streaming waveform for writing new data. During generation, this available space may be in multiple locations with, for example, part of the available space at the end of the streaming waveform and the rest at the beginning. In this situation, writing a block of waveform data the size of the  total space available in the streaming waveform causes NI-FGEN to return an error, as  NI-FGEN will not wrap the data from the end of the waveform to the beginning and cannot write data past the end of the waveform buffer.
        To avoid writing data past the end of the waveform, write new data to the waveform in a fixed size that is an integer divisor of the total size of the streaming waveform.
        Used in conjunction with the :py:attr:`nifgen.Session.streaming_waveform_handle` or :py:attr:`nifgen.Session.streaming_waveform_name` properties.

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

                - LabVIEW Property: **Arbitrary Waveform:Data Transfer:Streaming:Space Available in Streaming Waveform**
                - C Attribute: **NIFGEN_ATTR_STREAMING_SPACE_AVAILABLE_IN_WAVEFORM**

streaming_waveform_handle
-------------------------

    .. py:attribute:: streaming_waveform_handle

        Specifies the waveform handle of the waveform used to continuously stream data during generation. This property defaults to -1 when no streaming waveform is specified.
        Used in conjunction with :py:attr:`nifgen.Session.streaming_space_available_in_waveform`.

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

                - LabVIEW Property: **Arbitrary Waveform:Data Transfer:Streaming:Streaming Waveform Handle**
                - C Attribute: **NIFGEN_ATTR_STREAMING_WAVEFORM_HANDLE**

streaming_waveform_name
-----------------------

    .. py:attribute:: streaming_waveform_name

        Specifies the name of the waveform used to continuously stream data during generation. This property defaults to // when no streaming waveform is specified.
        Use in conjunction with :py:attr:`nifgen.Session.streaming_space_available_in_waveform`.

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

                - LabVIEW Property: **Arbitrary Waveform:Data Transfer:Streaming:Streaming Waveform Name**
                - C Attribute: **NIFGEN_ATTR_STREAMING_WAVEFORM_NAME**

streaming_write_timeout
-----------------------

    .. py:attribute:: streaming_write_timeout

        Specifies the maximum amount of time allowed to complete a streaming write operation.

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

                - LabVIEW Property: **Arbitrary Waveform:Data Transfer:Streaming:Streaming Write Timeout**
                - C Attribute: **NIFGEN_ATTR_STREAMING_WRITE_TIMEOUT**

supported_instrument_models
---------------------------

    .. py:attribute:: supported_instrument_models

        Returns a model code of the device. For NI-FGEN versions that support more than one device, this  property contains a comma-separated list of supported device  models.

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

                - LabVIEW Property: **Instrument:Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models**
                - C Attribute: **NIFGEN_ATTR_SUPPORTED_INSTRUMENT_MODELS**

terminal_configuration
----------------------

    .. py:attribute:: terminal_configuration

        Specifies whether gain and offset values will be analyzed based on single-ended or differential operation.




        .. tip:: This property can be set/get on specific channels within your :py:class:`nifgen.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].terminal_configuration`

            To set/get on all channels, you can call the property directly on the :py:class:`nifgen.Session`.

            Example: :py:attr:`my_session.terminal_configuration`

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

                - LabVIEW Property: **Output:Terminal Configuration**
                - C Attribute: **NIFGEN_ATTR_TERMINAL_CONFIGURATION**

trigger_mode
------------

    .. py:attribute:: trigger_mode

        Controls the trigger mode.




        .. tip:: This property can be set/get on specific channels within your :py:class:`nifgen.Session` instance.
            Use Python index notation on the repeated capabilities container channels to specify a subset.

            Example: :py:attr:`my_session.channels[ ... ].trigger_mode`

            To set/get on all channels, you can call the property directly on the :py:class:`nifgen.Session`.

            Example: :py:attr:`my_session.trigger_mode`

        The following table lists the characteristics of this property.

            +-----------------------+-------------------+
            | Characteristic        | Value             |
            +=======================+===================+
            | Datatype              | enums.TriggerMode |
            +-----------------------+-------------------+
            | Permissions           | read-write        |
            +-----------------------+-------------------+
            | Repeated Capabilities | channels          |
            +-----------------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggers:Trigger Mode**
                - C Attribute: **NIFGEN_ATTR_TRIGGER_MODE**

wait_behavior
-------------

    .. py:attribute:: wait_behavior

        Specifies the behavior of the output while waiting for a script trigger or during a wait instruction.  The output can be configured to hold the last generated voltage before waiting or jump to the Wait Value.

        The following table lists the characteristics of this property.

            +-----------------------+--------------------+
            | Characteristic        | Value              |
            +=======================+====================+
            | Datatype              | enums.WaitBehavior |
            +-----------------------+--------------------+
            | Permissions           | read-write         |
            +-----------------------+--------------------+
            | Repeated Capabilities | None               |
            +-----------------------+--------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Output:Advanced:Wait Behavior**
                - C Attribute: **NIFGEN_ATTR_WAIT_BEHAVIOR**

wait_value
----------

    .. py:attribute:: wait_value

        Specifies the value to generate while waiting.  The Wait Behavior must be configured to jump to this value.

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

                - LabVIEW Property: **Output:Advanced:Wait Value**
                - C Attribute: **NIFGEN_ATTR_WAIT_VALUE**

waveform_quantum
----------------

    .. py:attribute:: waveform_quantum

        The size of each arbitrary waveform must be a multiple of a quantum value. This property returns the quantum value that the signal generator allows.
        For example, when this property returns a value of 8, all waveform sizes must be a multiple of 8. Typically, this value is constant for the signal generator.

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

                - LabVIEW Property: **Arbitrary Waveform:Capabilities:Waveform Quantum**
                - C Attribute: **NIFGEN_ATTR_WAVEFORM_QUANTUM**


NI-TClk Support
===============

    .. py:attribute:: tclk

        This is used to get and set NI-TClk attributes on the session.

        .. seealso:: See :py:class:`nitclk.SessionReference` for a complete list of attributes.


.. contents:: Session
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nifgen/conf.py sha256=153b37b8980efb82baae260ba6eb3886eb4fe73492905c548fd4643616ea246a bytes=6531 -->
## FILE: docs/nifgen/conf.py

- repository: `ni/nimi-python`
- source_path: `docs/nifgen/conf.py`
- sha256: `153b37b8980efb82baae260ba6eb3886eb4fe73492905c548fd4643616ea246a`
- bytes: 6531

````python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# NI-FGEN Python API documentation build configuration file, created by
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
project = 'NI-FGEN Python API'
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
    (master_doc, 'NIFGENPythonAPI.tex', 'NI-FGEN Python API Documentation',
     'NI', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'nifgenpythonapi', 'NI-FGEN Python API Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'NIFGENPythonAPI', 'NI-FGEN Python API Documentation',
     author, 'NIFGENPythonAPI', 'One line description of project.',
     'Miscellaneous'),
]

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'nidcpower': ('https://nidcpower.readthedocs.io/en/latest/', None),
    'nidigital': ('https://nidigital.readthedocs.io/en/latest/', None),
    'nidmm': ('https://nidmm.readthedocs.io/en/latest/', None),
    'nimodinst': ('https://nimodinst.readthedocs.io/en/latest/', None),
    'nirfsg': ('https://nirfsg.readthedocs.io/en/latest/', None),
    'niscope': ('https://niscope.readthedocs.io/en/latest/', None),
    'nise': ('https://nise.readthedocs.io/en/latest/', None),
    'niswitch': ('https://niswitch.readthedocs.io/en/latest/', None),
    'nitclk': ('https://nitclk.readthedocs.io/en/latest/', None),
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nifgen/enums.rst sha256=2007ceae12bacacb830f731e561c6f5a79bada2279522d4c7713afbbc3b377a3 bytes=13834 -->
## FILE: docs/nifgen/enums.rst

- repository: `ni/nimi-python`
- source_path: `docs/nifgen/enums.rst`
- sha256: `2007ceae12bacacb830f731e561c6f5a79bada2279522d4c7713afbbc3b377a3`
- bytes: 13834

````rst
Enums
=====

Enums used in NI-FGEN

.. py:currentmodule:: nifgen


AnalogPath
----------

.. py:class:: AnalogPath

    .. py:attribute:: AnalogPath.MAIN



        Specifies use of the main path.  NI-FGEN chooses the amplifier based on the user-specified gain.

        



    .. py:attribute:: AnalogPath.DIRECT



        Specifies use of the direct path.

        



    .. py:attribute:: AnalogPath.FIXED_LOW_GAIN



        Specifies use of the low-gain amplifier in the main path, no matter  what value the user specifies for gain. This setting limits the output  range.

        



    .. py:attribute:: AnalogPath.FIXED_HIGH_GAIN



        Specifies use of the high-gain amplifier in the main path.

        



BusType
-------

.. py:class:: BusType

    .. py:attribute:: BusType.INVALID



        Indicates an invalid bus type.

        



    .. py:attribute:: BusType.AT



        Indicates the signal generator is the AT bus type.

        



    .. py:attribute:: BusType.PCI



        Indicates the signal generator is the PCI bus type.

        



    .. py:attribute:: BusType.PXI



        Indicates the signal generator is the PXI bus type.

        



    .. py:attribute:: BusType.VXI



        Indicates the signal generator is the VXI bus type.

        



    .. py:attribute:: BusType.PCMCIA



        Indicates the signal generator is the PCI-CMA bus type.

        



    .. py:attribute:: BusType.PXIE



        Indicates the signal generator is the PXI Express bus type.

        



ByteOrder
---------

.. py:class:: ByteOrder

    .. py:attribute:: ByteOrder.LITTLE



    .. py:attribute:: ByteOrder.BIG



ClockMode
---------

.. py:class:: ClockMode

    .. py:attribute:: ClockMode.HIGH_RESOLUTION



        High resolution sampling—Sample rate is generated by a high–resolution clock source.

        



    .. py:attribute:: ClockMode.DIVIDE_DOWN



        Divide down sampling—Sample rates are generated by dividing the source frequency.

        



    .. py:attribute:: ClockMode.AUTOMATIC



        Automatic Selection—NI-FGEN selects between the divide–down and high–resolution clocking modes.

        



DataMarkerEventLevelPolarity
----------------------------

.. py:class:: DataMarkerEventLevelPolarity

    .. py:attribute:: DataMarkerEventLevelPolarity.HIGH



        When the operation is ready to start, the Ready for Start  event level is high.

        



    .. py:attribute:: DataMarkerEventLevelPolarity.LOW



        When the operation is ready to start, the Ready for Start  event level is low.

        



EventPulseWidthUnits
--------------------

.. py:class:: EventPulseWidthUnits

    .. py:attribute:: EventPulseWidthUnits.SAMPLE_CLOCK_PERIODS



        Specifies the pulse width in Sample clock periods.

        



    .. py:attribute:: EventPulseWidthUnits.SECONDS



        Specifies the pulse width in seconds.

        



HardwareState
-------------

.. py:class:: HardwareState

    .. py:attribute:: HardwareState.IDLE



    .. py:attribute:: HardwareState.WAITING_FOR_START_TRIGGER



    .. py:attribute:: HardwareState.RUNNING



    .. py:attribute:: HardwareState.DONE



    .. py:attribute:: HardwareState.HARDWARE_ERROR



IdleBehavior
------------

.. py:class:: IdleBehavior

    .. py:attribute:: IdleBehavior.HOLD_LAST



        While in an Idle or Wait state, the output signal remains  at the last voltage generated prior to entering the state.

        



    .. py:attribute:: IdleBehavior.JUMP_TO



        While in an Idle or Wait state, the output signal remains  at the value configured in the Idle or Wait value property.

        



OutputMode
----------

.. py:class:: OutputMode

    .. py:attribute:: OutputMode.FUNC



        Standard Method mode—  Generates standard method waveforms  such as sine, square, triangle, and so on.

        



    .. py:attribute:: OutputMode.ARB



        Arbitrary waveform mode—Generates  waveforms from user-created/provided  waveform arrays of numeric data.

        



    .. py:attribute:: OutputMode.SEQ



        Arbitrary sequence mode —  Generates downloaded waveforms  in an order your specify.

        



    .. py:attribute:: OutputMode.FREQ_LIST



        Frequency List mode—Generates a  standard method using a list of  frequencies you define.

        



    .. py:attribute:: OutputMode.SCRIPT



        **Script mode—**\ Allows you to use scripting to link and loop multiple
        waveforms in complex combinations.

        



ReferenceClockSource
--------------------

.. py:class:: ReferenceClockSource

    .. py:attribute:: ReferenceClockSource.CLOCK_IN



        Specifies that the CLK IN input signal from the front panel connector is
        used as the Reference Clock source.

        



    .. py:attribute:: ReferenceClockSource.NONE



        Specifies that a Reference Clock is not used.

        



    .. py:attribute:: ReferenceClockSource.ONBOARD_REFERENCE_CLOCK



        Specifies that the onboard Reference Clock is used as the Reference
        Clock source.

        



    .. py:attribute:: ReferenceClockSource.PXI_CLOCK



        Specifies that the PXI Clock is used as the Reference Clock source.

        



    .. py:attribute:: ReferenceClockSource.RTSI_7



        Specifies that the RTSI line 7 is used as the Reference Clock source.

        



RelativeTo
----------

.. py:class:: RelativeTo

    .. py:attribute:: RelativeTo.START



    .. py:attribute:: RelativeTo.CURRENT



SampleClockSource
-----------------

.. py:class:: SampleClockSource

    .. py:attribute:: SampleClockSource.CLOCK_IN



        Specifies that the signal at the CLK IN front panel connector is used as
        the Sample Clock source.

        



    .. py:attribute:: SampleClockSource.DDC_CLOCK_IN



        Specifies that the Sample Clock from the DDC connector is used as the Sample
        Clock source.

        



    .. py:attribute:: SampleClockSource.ONBOARD_CLOCK



        Specifies that the onboard clock is used as the Sample Clock source.

        



    .. py:attribute:: SampleClockSource.PXI_STAR_LINE



        Specifies that the PXI\_STAR trigger line is used as the Sample Clock
        source.

        



    .. py:attribute:: SampleClockSource.PXI_TRIGGER_LINE_0_RTSI_0



        Specifies that the PXI or RTSI line 0 is used as the Sample Clock
        source.

        



    .. py:attribute:: SampleClockSource.PXI_TRIGGER_LINE_1_RTSI_1



        Specifies that the PXI or RTSI line 1 is used as the Sample Clock
        source.

        



    .. py:attribute:: SampleClockSource.PXI_TRIGGER_LINE_2_RTSI_2



        Specifies that the PXI or RTSI line 2 is used as the Sample Clock
        source.

        



    .. py:attribute:: SampleClockSource.PXI_TRIGGER_LINE_3_RTSI_3



        Specifies that the PXI or RTSI line 3 is used as the Sample Clock
        source.

        



    .. py:attribute:: SampleClockSource.PXI_TRIGGER_LINE_4_RTSI_4



        Specifies that the PXI or RTSI line 4 is used as the Sample Clock
        source.

        



    .. py:attribute:: SampleClockSource.PXI_TRIGGER_LINE_5_RTSI_5



        Specifies that the PXI or RTSI line 5 is used as the Sample Clock
        source.

        



    .. py:attribute:: SampleClockSource.PXI_TRIGGER_LINE_6_RTSI_6



        Specifies that the PXI or RTSI line 6 is used as the Sample Clock
        source.

        



    .. py:attribute:: SampleClockSource.PXI_TRIGGER_LINE_7_RTSI_7



        Specifies that the PXI or RTSI line 7 is used as the Sample Clock
        source.

        



SampleClockTimebaseSource
-------------------------

.. py:class:: SampleClockTimebaseSource

    .. py:attribute:: SampleClockTimebaseSource.CLOCK_IN



        Specifies that the external signal on the CLK IN front panel connector
        is used as the source.

        



    .. py:attribute:: SampleClockTimebaseSource.ONBOARD_CLOCK



        Specifies that the onboard Sample Clock timebase is used as the source.

        



ScriptTriggerDigitalEdgeEdge
----------------------------

.. py:class:: ScriptTriggerDigitalEdgeEdge

    .. py:attribute:: ScriptTriggerDigitalEdgeEdge.RISING



        Rising Edge

        



    .. py:attribute:: ScriptTriggerDigitalEdgeEdge.FALLING



        Falling Edge

        



ScriptTriggerType
-----------------

.. py:class:: ScriptTriggerType

    .. py:attribute:: ScriptTriggerType.TRIG_NONE



        No trigger is configured. Signal generation starts immediately.

        



    .. py:attribute:: ScriptTriggerType.DIGITAL_EDGE



        Trigger is asserted when a digital edge is detected.

        



    .. py:attribute:: ScriptTriggerType.DIGITAL_LEVEL



        Trigger is asserted when a digital level is detected.

        



    .. py:attribute:: ScriptTriggerType.SOFTWARE_EDGE



        Trigger is asserted when a software edge is detected.

        



StartTriggerDigitalEdgeEdge
---------------------------

.. py:class:: StartTriggerDigitalEdgeEdge

    .. py:attribute:: StartTriggerDigitalEdgeEdge.RISING



        Rising Edge

        



    .. py:attribute:: StartTriggerDigitalEdgeEdge.FALLING



        Falling Edge

        



StartTriggerType
----------------

.. py:class:: StartTriggerType

    .. py:attribute:: StartTriggerType.TRIG_NONE



        None

        



    .. py:attribute:: StartTriggerType.DIGITAL_EDGE



        Digital Edge

        



    .. py:attribute:: StartTriggerType.SOFTWARE_EDGE



        Software Edge

        



    .. py:attribute:: StartTriggerType.P2P_ENDPOINT_FULLNESS



        P2P Endpoint Fullness

        



TerminalConfiguration
---------------------

.. py:class:: TerminalConfiguration

    .. py:attribute:: TerminalConfiguration.SINGLE_ENDED



        Single-ended operation

        



    .. py:attribute:: TerminalConfiguration.DIFFERENTIAL



        Differential operation

        



Trigger
-------

.. py:class:: Trigger

    .. py:attribute:: Trigger.START



    .. py:attribute:: Trigger.SCRIPT



TriggerMode
-----------

.. py:class:: TriggerMode

    .. py:attribute:: TriggerMode.SINGLE



        Single Trigger Mode - The waveform you describe in the sequence list is  generated only once by going through the entire staging list. Only one  trigger is required to start the waveform generation. You can use Single  trigger mode with the output mode in any mode. After a trigger is  received, the waveform generation starts from the first stage and  continues through to the last stage. Then, the last stage generates  repeatedly until you stop the waveform generation.

        



    .. py:attribute:: TriggerMode.CONTINUOUS



        Continuous Trigger Mode - The waveform you describe in the staging list generates infinitely by repeatedly cycling through the staging list.  After a trigger is received, the waveform generation starts from the  first stage and continues through to the last stage. After the last stage  completes, the waveform generation loops back to the start of the  first stage and continues until it is stopped. Only one trigger is  required to start the waveform generation.

        



    .. py:attribute:: TriggerMode.STEPPED



        Stepped Trigger Mode - After a start trigger is received, the waveform  described by the first stage generates. Then, the device waits for the  next trigger signal. On the next trigger, the waveform described by the  second stage generates, and so on. After the staging list completes,  the waveform generation returns to the first stage and continues in a  cyclic fashion. After any stage has generated completely, the first  eight samples of the next stage are repeated continuously until the next  trigger is received.
        trigger mode.

        

        .. note:: In Frequency List mode, Stepped trigger mode is the same as Burst



    .. py:attribute:: TriggerMode.BURST



        Burst Trigger Mode - After a start trigger is received, the waveform  described by the first stage generates until another trigger is  received. At the next trigger, the buffer of the previous stage completes, and then the waveform described by the second stage generates. After the staging list completes, the waveform generation  returns to the first stage and continues in a cyclic fashion. In  Frequency List mode, the duration instruction is ignored, and the trigger  switches the frequency to the next frequency in the list.
        trigger mode.

        

        .. note:: In Frequency List mode, Stepped trigger mode is the same as Burst



WaitBehavior
------------

.. py:class:: WaitBehavior

    .. py:attribute:: WaitBehavior.HOLD_LAST



        While in an Idle or Wait state, the output signal remains  at the last voltage generated prior to entering the state.

        



    .. py:attribute:: WaitBehavior.JUMP_TO



        While in an Idle or Wait state, the output signal remains  at the value configured in the Idle or Wait value property.

        



Waveform
--------

.. py:class:: Waveform

    .. py:attribute:: Waveform.SINE



        Sinusoid waveform

        



    .. py:attribute:: Waveform.SQUARE



        Square waveform

        



    .. py:attribute:: Waveform.TRIANGLE



        Triange waveform

        



    .. py:attribute:: Waveform.RAMP_UP



        Positive ramp waveform

        



    .. py:attribute:: Waveform.RAMP_DOWN



        Negative ramp waveform

        



    .. py:attribute:: Waveform.DC



        Constant voltage

        



    .. py:attribute:: Waveform.NOISE



        White noise

        



    .. py:attribute:: Waveform.USER



        User-defined waveform as defined by the :py:meth:`nifgen.Session.define_user_standard_waveform` method.

        
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nifgen/errors.rst sha256=156ba0b7f578acb965320a849c68947de545df4a5dddb2778e1341a4445ab971 bytes=1895 -->
## FILE: docs/nifgen/errors.rst

- repository: `ni/nimi-python`
- source_path: `docs/nifgen/errors.rst`
- sha256: `156ba0b7f578acb965320a849c68947de545df4a5dddb2778e1341a4445ab971`
- bytes: 1895

````rst
Exceptions and Warnings
=======================

Error
-----

    .. py:currentmodule:: nifgen.errors

    .. exception:: Error

        Base exception type that all NI-FGEN exceptions derive from


DriverError
-----------

    .. py:currentmodule:: nifgen.errors

    .. exception:: DriverError

        An error originating from the NI-FGEN driver


UnsupportedConfigurationError
-----------------------------

    .. py:currentmodule:: nifgen.errors

    .. exception:: UnsupportedConfigurationError

        An error due to using this module in an usupported platform.

DriverNotInstalledError
-----------------------

    .. py:currentmodule:: nifgen.errors

    .. exception:: DriverNotInstalledError

        An error due to using this module without the driver runtime installed.

DriverTooOldError
-----------------

    .. py:currentmodule:: nifgen.errors

    .. exception:: DriverTooOldError

        An error due to using this module with an older version of the NI-FGEN driver runtime.

DriverTooNewError
-----------------

    .. py:currentmodule:: nifgen.errors

    .. exception:: DriverTooNewError

        An error due to the NI-FGEN driver runtime being too new for this module.

InvalidRepeatedCapabilityError
------------------------------

    .. py:currentmodule:: nifgen.errors

    .. exception:: InvalidRepeatedCapabilityError

        An error due to an invalid character in a repeated capability


SelfTestError
-------------

    .. py:currentmodule:: nifgen.errors

    .. exception:: SelfTestError

        An error due to a failed self-test


RpcError
--------

    .. py:currentmodule:: nifgen.errors

    .. exception:: RpcError

        An error specific to sessions to the NI gRPC Device Server


DriverWarning
-------------

    .. py:currentmodule:: nifgen.errors

    .. exception:: DriverWarning

        A warning originating from the NI-FGEN driver
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nifgen/examples.rst sha256=45acf0fcd02013d73447454529ff51831b6628ecf9d346b0987f6c3a08a42a58 bytes=1342 -->
## FILE: docs/nifgen/examples.rst

- repository: `ni/nimi-python`
- source_path: `docs/nifgen/examples.rst`
- sha256: `45acf0fcd02013d73447454529ff51831b6628ecf9d346b0987f6c3a08a42a58`
- bytes: 1342

````rst
Examples
========

`You can download all nifgen examples for latest version here <https://github.com/ni/nimi-python/releases/download/1.4.9/nifgen_examples.zip>`_

nifgen_arb_waveform.py
----------------------

.. literalinclude:: ../../src/nifgen/examples/nifgen_arb_waveform.py
   :language: python
   :linenos:
   :encoding: utf8
   :caption: `(nifgen_arb_waveform.py) <https://github.com/ni/nimi-python/blob/master/src/nifgen/examples/nifgen_arb_waveform.py>`_

nifgen_script.py
----------------

.. literalinclude:: ../../src/nifgen/examples/nifgen_script.py
   :language: python
   :linenos:
   :encoding: utf8
   :caption: `(nifgen_script.py) <https://github.com/ni/nimi-python/blob/master/src/nifgen/examples/nifgen_script.py>`_

nifgen_standard_function.py
---------------------------

.. literalinclude:: ../../src/nifgen/examples/nifgen_standard_function.py
   :language: python
   :linenos:
   :encoding: utf8
   :caption: `(nifgen_standard_function.py) <https://github.com/ni/nimi-python/blob/master/src/nifgen/examples/nifgen_standard_function.py>`_

nifgen_trigger.py
-----------------

.. literalinclude:: ../../src/nifgen/examples/nifgen_trigger.py
   :language: python
   :linenos:
   :encoding: utf8
   :caption: `(nifgen_trigger.py) <https://github.com/ni/nimi-python/blob/master/src/nifgen/examples/nifgen_trigger.py>`_
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nifgen/grpc_session_options.rst sha256=c481cd18cf799fa17cda5650316d865dd62e0e326746a9422f5d24fe152b8609 bytes=2887 -->
## FILE: docs/nifgen/grpc_session_options.rst

- repository: `ni/nimi-python`
- source_path: `docs/nifgen/grpc_session_options.rst`
- sha256: `c481cd18cf799fa17cda5650316d865dd62e0e326746a9422f5d24fe152b8609`
- bytes: 2887

````rst
gRPC Support
============

Support for using NI-FGEN over gRPC

.. py:currentmodule:: nifgen



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

        

    :type initialization_behavior: :py:data:`nifgen.SessionInitializationBehavior`
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nifgen/index.rst sha256=ac1249b312897db1fd7520989010a7297744ff80e67524a5b4175a70ca00022b bytes=686 -->
## FILE: docs/nifgen/index.rst

- repository: `ni/nimi-python`
- source_path: `docs/nifgen/index.rst`
- sha256: `ac1249b312897db1fd7520989010a7297744ff80e67524a5b4175a70ca00022b`
- bytes: 686

````rst

NI-FGEN Python API Documentation
================================

.. include:: about_nifgen.inc

.. include:: ../_static/contributing.inc

.. include:: ../_static/support.inc

.. toctree::
   :maxdepth: 3
   :caption: Documentation

   nifgen

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

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nifgen/installation.inc sha256=246473674a3a3a79d26c3635114674544d5d5e492063bd885592a25577cc0f05 bytes=420 -->
## FILE: docs/nifgen/installation.inc

- repository: `ni/nimi-python`
- source_path: `docs/nifgen/installation.inc`
- sha256: `246473674a3a3a79d26c3635114674544d5d5e492063bd885592a25577cc0f05`
- bytes: 420

````text

.. _nifgen_installation-section:

Installation
------------

As a prerequisite to using the **nifgen** module, you must install the NI-FGEN runtime on your system. Visit `ni.com/downloads <http://www.ni.com/downloads/>`_ to download the driver runtime for your devices.

The nimi-python modules (i.e. for **NI-FGEN**) can be installed with `pip <http://pypi.python.org/pypi/pip>`_::

  $ python -m pip install nifgen
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nifgen/nifgen.rst sha256=cc462bbc5ec837e3812dde5c6b667167e5eefb7e83ed5be3cf23c1d97c5ae76e bytes=124 -->
## FILE: docs/nifgen/nifgen.rst

- repository: `ni/nimi-python`
- source_path: `docs/nifgen/nifgen.rst`
- sha256: `cc462bbc5ec837e3812dde5c6b667167e5eefb7e83ed5be3cf23c1d97c5ae76e`
- bytes: 124

````rst
nifgen module
=============

.. include:: installation.inc

.. include:: ../_static/nifgen_usage.inc

.. include:: toc.inc
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nifgen/rep_caps.rst sha256=96baa0dc816184db111da0ab9a586801f2b6787940225d86ee1329daf3c4dbc4 bytes=3869 -->
## FILE: docs/nifgen/rep_caps.rst

- repository: `ni/nimi-python`
- source_path: `docs/nifgen/rep_caps.rst`
- sha256: `96baa0dc816184db111da0ab9a586801f2b6787940225d86ee1329daf3c4dbc4`
- bytes: 3869

````rst
.. py:module:: nifgen
    :noindex:

.. py:currentmodule:: nifgen.Session

.. role:: c(code)
    :language: c

.. role:: python(code)
    :language: python

Repeated Capabilities
=====================

    Repeated capabilities attributes are used to set the `channel_string` parameter to the
    underlying driver function call. This can be the actual function based on the :py:class:`Session`
    method being called, or it can be the appropriate Get/Set Attribute function, such as :c:`niFgen_SetAttributeViInt32()`.

    Repeated capabilities attributes use the indexing operator :python:`[]` to indicate the repeated capabilities.
    The parameter can be a string, list, tuple, or slice (range). Each element of those can be a string or
    an integer. If it is a string, you can indicate a range using the same format as the driver: :python:`'0-2'` or
    :python:`'0:2'`

    Some repeated capabilities use a prefix before the number and this is optional

channels
--------

    .. py:attribute:: nifgen.Session.channels[]

        .. code:: python

            session.channels['0-2'].channel_enabled = True

        passes a string of :python:`'0, 1, 2'` to the set attribute function.


script_triggers
---------------

    .. py:attribute:: nifgen.Session.script_triggers[]

        If no prefix is added to the items in the parameter, the correct prefix will be added when
        the driver function call is made.

        .. code:: python

            session.script_triggers['0-2'].channel_enabled = True

        passes a string of :python:`'ScriptTrigger0, ScriptTrigger1, ScriptTrigger2'` to the set attribute function.

        If an invalid repeated capability is passed to the driver, the driver will return an error.

        You can also explicitly use the prefix as part of the parameter, but it must be the correct prefix
        for the specific repeated capability.

        .. code:: python

            session.script_triggers['ScriptTrigger0-ScriptTrigger2'].channel_enabled = True

        passes a string of :python:`'ScriptTrigger0, ScriptTrigger1, ScriptTrigger2'` to the set attribute function.


markers
-------

    .. py:attribute:: nifgen.Session.markers[]

        If no prefix is added to the items in the parameter, the correct prefix will be added when
        the driver function call is made.

        .. code:: python

            session.markers['0-2'].channel_enabled = True

        passes a string of :python:`'Marker0, Marker1, Marker2'` to the set attribute function.

        If an invalid repeated capability is passed to the driver, the driver will return an error.

        You can also explicitly use the prefix as part of the parameter, but it must be the correct prefix
        for the specific repeated capability.

        .. code:: python

            session.markers['Marker0-Marker2'].channel_enabled = True

        passes a string of :python:`'Marker0, Marker1, Marker2'` to the set attribute function.


data_markers
------------

    .. py:attribute:: nifgen.Session.data_markers[]

        If no prefix is added to the items in the parameter, the correct prefix will be added when
        the driver function call is made.

        .. code:: python

            session.data_markers['0-2'].channel_enabled = True

        passes a string of :python:`'DataMarker0, DataMarker1, DataMarker2'` to the set attribute function.

        If an invalid repeated capability is passed to the driver, the driver will return an error.

        You can also explicitly use the prefix as part of the parameter, but it must be the correct prefix
        for the specific repeated capability.

        .. code:: python

            session.data_markers['DataMarker0-DataMarker2'].channel_enabled = True

        passes a string of :python:`'DataMarker0, DataMarker1, DataMarker2'` to the set attribute function.
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nifgen/status.inc sha256=9c250327fc5e05f38d8d5d11211b0fa17079079909187f7f32fab11cc73c513e bytes=1908 -->
## FILE: docs/nifgen/status.inc

- repository: `ni/nimi-python`
- source_path: `docs/nifgen/status.inc`
- sha256: `9c250327fc5e05f38d8d5d11211b0fa17079079909187f7f32fab11cc73c513e`
- bytes: 1908

````text

NI-FGEN Python API Status
-------------------------

+-------------------------------+-----------------------+
| NI-FGEN (nifgen)              |                       |
+===============================+=======================+
| Driver Version Tested Against | 2025 Q4               |
+-------------------------------+-----------------------+
| PyPI Version                  | |nifgenLatestVersion| |
+-------------------------------+-----------------------+
| Supported Python Version      | |nifgenPythonVersion| |
+-------------------------------+-----------------------+
| Documentation                 | |nifgenDocs|          |
+-------------------------------+-----------------------+
| Open Issues                   | |nifgenOpenIssues|    |
+-------------------------------+-----------------------+
| Open Pull Requests            | |nifgenOpenPRs|       |
+-------------------------------+-----------------------+


.. |nifgenLatestVersion| image:: http://img.shields.io/pypi/v/nifgen.svg
    :alt: Latest NI-FGEN Version
    :target: http://pypi.python.org/pypi/nifgen


.. |nifgenPythonVersion| image:: http://img.shields.io/pypi/pyversions/nifgen.svg
    :alt: NI-FGEN supported Python versions
    :target: http://pypi.python.org/pypi/nifgen


.. |nifgenDocs| image:: https://readthedocs.org/projects/nifgen/badge/?version=latest
    :alt: NI-FGEN Python API Documentation Status
    :target: https://nifgen.readthedocs.io/en/latest


.. |nifgenOpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python/nifgen.svg
    :alt: Open Issues + Pull Requests for NI-FGEN
    :target: https://github.com/ni/nimi-python/issues?q=is%3Aopen+is%3Aissue+label%3Anifgen


.. |nifgenOpenPRs| image:: https://img.shields.io/github/issues-pr/ni/nimi-python/nifgen.svg
    :alt: Pull Requests for NI-FGEN
    :target: https://github.com/ni/nimi-python/pulls?q=is%3Aopen+is%3Aissue+label%3Anifgen
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nifgen/toc.inc sha256=4958d5597b4005305d15cdc9a09014d5afa552d460451b042172b99069952975 bytes=121 -->
## FILE: docs/nifgen/toc.inc

- repository: `ni/nimi-python`
- source_path: `docs/nifgen/toc.inc`
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

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nimodinst/.readthedocs.yaml sha256=96b2094099a24d31c93e43db023318733b2131a1b609baa3e74bac4c6526a48c bytes=1885 -->
## FILE: docs/nimodinst/.readthedocs.yaml

- repository: `ni/nimi-python`
- source_path: `docs/nimodinst/.readthedocs.yaml`
- sha256: `96b2094099a24d31c93e43db023318733b2131a1b609baa3e74bac4c6526a48c`
- bytes: 1885

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
      # Cancel building pull requests when there aren't changes in any of these paths: docs/_static/ docs/nimodinst/.
      #
      # If there are no changes (git diff exits with 0) we force the command to return with 183.
      # This is a special exit code on Read the Docs that will cancel the build immediately.
      - |
        if [ "$READTHEDOCS_VERSION_TYPE" = "external" ] && git diff --quiet origin/master -- docs/_static/ docs/nimodinst/;
        then
          exit 183;
        fi

# Have Read the Docs build documentation with Sphinx
sphinx:
  builder: html
  configuration: docs/nimodinst/conf.py

# If using Sphinx, optionally build your docs in additional formats such as PDF
formats:
  - epub
  - pdf

# Declare the Python requirements required to build your docs
python:
  install:
  - requirements: docs/requirements.txt
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nimodinst/about_nimodinst.inc sha256=943af69789df6a2fad4c2b8a2cd192411fe89c854091d34b43020086b83752d7 bytes=500 -->
## FILE: docs/nimodinst/about_nimodinst.inc

- repository: `ni/nimi-python`
- source_path: `docs/nimodinst/about_nimodinst.inc`
- sha256: `943af69789df6a2fad4c2b8a2cd192411fe89c854091d34b43020086b83752d7`
- bytes: 500

````text
.. _about-section:

About
=====

The **nimodinst** module provides a Python API for NI-ModInst. The code is maintained in the Open Source repository for `nimi-python <https://github.com/ni/nimi-python>`_.

Support Policy
--------------
**nimodinst** supports all the Operating Systems supported by NI-ModInst.

It follows `Python Software Foundation <https://devguide.python.org/#status-of-python-branches>`_ support policy for different versions of CPython.

NI created and supports **nimodinst**.
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nimodinst/class.rst sha256=4ef5f15d8262a8d043b3841dae175249b9f33c007dca00baa0094ff5df150346 bytes=8361 -->
## FILE: docs/nimodinst/class.rst

- repository: `ni/nimi-python`
- source_path: `docs/nimodinst/class.rst`
- sha256: `4ef5f15d8262a8d043b3841dae175249b9f33c007dca00baa0094ff5df150346`
- bytes: 8361

````rst
.. py:module:: nimodinst

Session
=======

.. py:class:: Session(self, driver)

    

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
    :py:meth:`nimodinst.Session._close_installed_devices_session` and create a new handle using
    this method.

    



    :param driver:
        

        A string specifying the driver whose supported devices you want to find.
        This string is not case-sensitive. Some examples are: NI-SCOPE niScope
        NI-FGEN niFgen NI-HSDIO niHSDIO NI-DMM niDMM NI-SWITCH niSwitch Note If
        you use the empty string for this parameter, NI-ModInst creates a list
        of all Modular Instruments devices installed in the system.

        


    :type driver: str


Methods
=======

close
-----

    .. py:currentmodule:: nimodinst.Session

    .. py:method:: close()

            Cleans up the NI-ModInst session created by a call to
            :py:meth:`nimodinst.Session._open_installed_devices_session`. Call this method when you are
            finished using the session handle and do not use this handle again.

            

            .. note:: This method is not needed when using the session context manager




Properties
==========

bus_number
----------

    .. py:attribute:: bus_number

        The bus on which the device has been enumerated.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIMODINST_ATTR_BUS_NUMBER**

chassis_number
--------------

    .. py:attribute:: chassis_number

        The number of the chassis in which the device is installed. This property can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIMODINST_ATTR_CHASSIS_NUMBER**

device_model
------------

    .. py:attribute:: device_model

        The model of the device (for example, NI PXI-5122)

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIMODINST_ATTR_DEVICE_MODEL**

device_name
-----------

    .. py:attribute:: device_name

        The name of the device, which can be used to open an instrument driver session for that device

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIMODINST_ATTR_DEVICE_NAME**

max_pciexpress_link_width
-------------------------

    .. py:attribute:: max_pciexpress_link_width

        **MAX_PCIEXPRESS_LINK_WIDTH**

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIMODINST_ATTR_MAX_PCIEXPRESS_LINK_WIDTH**

pciexpress_link_width
---------------------

    .. py:attribute:: pciexpress_link_width

        **PCIEXPRESS_LINK_WIDTH**

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIMODINST_ATTR_PCIEXPRESS_LINK_WIDTH**

serial_number
-------------

    .. py:attribute:: serial_number

        The serial number of the device

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIMODINST_ATTR_SERIAL_NUMBER**

slot_number
-----------

    .. py:attribute:: slot_number

        The slot (for example, in a PXI chassis) in which the device is installed. This property can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIMODINST_ATTR_SLOT_NUMBER**

socket_number
-------------

    .. py:attribute:: socket_number

        The socket number on which the device has been enumerated

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NIMODINST_ATTR_SOCKET_NUMBER**


.. contents:: Session
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nimodinst/conf.py sha256=0dc9cade9649ca7ee29178222c5b1c6b82fcc30db3a6cd06b09f7ecd11312b35 bytes=6552 -->
## FILE: docs/nimodinst/conf.py

- repository: `ni/nimi-python`
- source_path: `docs/nimodinst/conf.py`
- sha256: `0dc9cade9649ca7ee29178222c5b1c6b82fcc30db3a6cd06b09f7ecd11312b35`
- bytes: 6552

````python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# NI-ModInst Python API documentation build configuration file, created by
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
project = 'NI-ModInst Python API'
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
    (master_doc, 'NIModInstPythonAPI.tex', 'NI-ModInst Python API Documentation',
     'NI', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'nimodinstpythonapi', 'NI-ModInst Python API Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'NIModInstPythonAPI', 'NI-ModInst Python API Documentation',
     author, 'NIModInstPythonAPI', 'One line description of project.',
     'Miscellaneous'),
]

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'nidcpower': ('https://nidcpower.readthedocs.io/en/latest/', None),
    'nidigital': ('https://nidigital.readthedocs.io/en/latest/', None),
    'nidmm': ('https://nidmm.readthedocs.io/en/latest/', None),
    'nifgen': ('https://nifgen.readthedocs.io/en/latest/', None),
    'nirfsg': ('https://nirfsg.readthedocs.io/en/latest/', None),
    'niscope': ('https://niscope.readthedocs.io/en/latest/', None),
    'nise': ('https://nise.readthedocs.io/en/latest/', None),
    'niswitch': ('https://niswitch.readthedocs.io/en/latest/', None),
    'nitclk': ('https://nitclk.readthedocs.io/en/latest/', None),
}
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nimodinst/errors.rst sha256=68d31103377ea0f4cfc35ef738d6ba104cb25d336f8a850c6040ede7cd2396bb bytes=1397 -->
## FILE: docs/nimodinst/errors.rst

- repository: `ni/nimi-python`
- source_path: `docs/nimodinst/errors.rst`
- sha256: `68d31103377ea0f4cfc35ef738d6ba104cb25d336f8a850c6040ede7cd2396bb`
- bytes: 1397

````rst
Exceptions and Warnings
=======================

Error
-----

    .. py:currentmodule:: nimodinst.errors

    .. exception:: Error

        Base exception type that all NI-ModInst exceptions derive from


DriverError
-----------

    .. py:currentmodule:: nimodinst.errors

    .. exception:: DriverError

        An error originating from the NI-ModInst driver


UnsupportedConfigurationError
-----------------------------

    .. py:currentmodule:: nimodinst.errors

    .. exception:: UnsupportedConfigurationError

        An error due to using this module in an usupported platform.

DriverNotInstalledError
-----------------------

    .. py:currentmodule:: nimodinst.errors

    .. exception:: DriverNotInstalledError

        An error due to using this module without the driver runtime installed.

DriverTooOldError
-----------------

    .. py:currentmodule:: nimodinst.errors

    .. exception:: DriverTooOldError

        An error due to using this module with an older version of the NI-ModInst driver runtime.

DriverTooNewError
-----------------

    .. py:currentmodule:: nimodinst.errors

    .. exception:: DriverTooNewError

        An error due to the NI-ModInst driver runtime being too new for this module.

DriverWarning
-------------

    .. py:currentmodule:: nimodinst.errors

    .. exception:: DriverWarning

        A warning originating from the NI-ModInst driver
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nimodinst/examples.rst sha256=460bee1b93863bdf78763f856ec99f5d486834afa0e622ec14eafb187f4b7114 bytes=488 -->
## FILE: docs/nimodinst/examples.rst

- repository: `ni/nimi-python`
- source_path: `docs/nimodinst/examples.rst`
- sha256: `460bee1b93863bdf78763f856ec99f5d486834afa0e622ec14eafb187f4b7114`
- bytes: 488

````rst
Examples
========

`You can download all nimodinst examples for latest version here <https://github.com/ni/nimi-python/releases/download/1.4.9/nimodinst_examples.zip>`_

nimodinst_all_devices.py
------------------------

.. literalinclude:: ../../src/nimodinst/examples/nimodinst_all_devices.py
   :language: python
   :linenos:
   :encoding: utf8
   :caption: `(nimodinst_all_devices.py) <https://github.com/ni/nimi-python/blob/master/src/nimodinst/examples/nimodinst_all_devices.py>`_
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nimodinst/index.rst sha256=2522d3dea9da4666a243a009aa4ee967b7d42033eb3298dab19fe93caf387177 bytes=698 -->
## FILE: docs/nimodinst/index.rst

- repository: `ni/nimi-python`
- source_path: `docs/nimodinst/index.rst`
- sha256: `2522d3dea9da4666a243a009aa4ee967b7d42033eb3298dab19fe93caf387177`
- bytes: 698

````rst

NI-ModInst Python API Documentation
===================================

.. include:: about_nimodinst.inc

.. include:: ../_static/contributing.inc

.. include:: ../_static/support.inc

.. toctree::
   :maxdepth: 3
   :caption: Documentation

   nimodinst

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

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nimodinst/installation.inc sha256=b9080a864522ddb9a46523c21deff4cca136d750de873d0cbe06a5818347f3e3 bytes=435 -->
## FILE: docs/nimodinst/installation.inc

- repository: `ni/nimi-python`
- source_path: `docs/nimodinst/installation.inc`
- sha256: `b9080a864522ddb9a46523c21deff4cca136d750de873d0cbe06a5818347f3e3`
- bytes: 435

````text

.. _nimodinst_installation-section:

Installation
------------

As a prerequisite to using the **nimodinst** module, you must install the NI-ModInst runtime on your system. Visit `ni.com/downloads <http://www.ni.com/downloads/>`_ to download the driver runtime for your devices.

The nimi-python modules (i.e. for **NI-ModInst**) can be installed with `pip <http://pypi.python.org/pypi/pip>`_::

  $ python -m pip install nimodinst
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nimodinst/nimodinst.rst sha256=3b19ff99d76b757066d8dd3abae3b871f0e211c270692b5fc411e84d77d1f0c8 bytes=133 -->
## FILE: docs/nimodinst/nimodinst.rst

- repository: `ni/nimi-python`
- source_path: `docs/nimodinst/nimodinst.rst`
- sha256: `3b19ff99d76b757066d8dd3abae3b871f0e211c270692b5fc411e84d77d1f0c8`
- bytes: 133

````rst
nimodinst module
================

.. include:: installation.inc

.. include:: ../_static/nimodinst_usage.inc

.. include:: toc.inc
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nimodinst/status.inc sha256=0be4e60465dddadf5271bfc3be162d64f28649affa784ad44182259775b873ba bytes=2019 -->
## FILE: docs/nimodinst/status.inc

- repository: `ni/nimi-python`
- source_path: `docs/nimodinst/status.inc`
- sha256: `0be4e60465dddadf5271bfc3be162d64f28649affa784ad44182259775b873ba`
- bytes: 2019

````text

NI-ModInst Python API Status
----------------------------

+-------------------------------+--------------------------+
| NI-ModInst (nimodinst)        |                          |
+===============================+==========================+
| Driver Version Tested Against | 2025 Q4                  |
+-------------------------------+--------------------------+
| PyPI Version                  | |nimodinstLatestVersion| |
+-------------------------------+--------------------------+
| Supported Python Version      | |nimodinstPythonVersion| |
+-------------------------------+--------------------------+
| Documentation                 | |nimodinstDocs|          |
+-------------------------------+--------------------------+
| Open Issues                   | |nimodinstOpenIssues|    |
+-------------------------------+--------------------------+
| Open Pull Requests            | |nimodinstOpenPRs|       |
+-------------------------------+--------------------------+


.. |nimodinstLatestVersion| image:: http://img.shields.io/pypi/v/nimodinst.svg
    :alt: Latest NI-ModInst Version
    :target: http://pypi.python.org/pypi/nimodinst


.. |nimodinstPythonVersion| image:: http://img.shields.io/pypi/pyversions/nimodinst.svg
    :alt: NI-ModInst supported Python versions
    :target: http://pypi.python.org/pypi/nimodinst


.. |nimodinstDocs| image:: https://readthedocs.org/projects/nimodinst/badge/?version=latest
    :alt: NI-ModInst Python API Documentation Status
    :target: https://nimodinst.readthedocs.io/en/latest


.. |nimodinstOpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python/nimodinst.svg
    :alt: Open Issues + Pull Requests for NI-ModInst
    :target: https://github.com/ni/nimi-python/issues?q=is%3Aopen+is%3Aissue+label%3Animodinst


.. |nimodinstOpenPRs| image:: https://img.shields.io/github/issues-pr/ni/nimi-python/nimodinst.svg
    :alt: Pull Requests for NI-ModInst
    :target: https://github.com/ni/nimi-python/pulls?q=is%3Aopen+is%3Aissue+label%3Animodinst
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nimodinst/toc.inc sha256=a423b560d349bdc16bbc762ed9737d740a20c7f36ca493b6c40282bcfd93d8ea bytes=76 -->
## FILE: docs/nimodinst/toc.inc

- repository: `ni/nimi-python`
- source_path: `docs/nimodinst/toc.inc`
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

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nirfsg/.readthedocs.yaml sha256=b2f40205e32e25afbd845da2eeb68f76898b5896c30ef004309c25f48b76c518 bytes=1876 -->
## FILE: docs/nirfsg/.readthedocs.yaml

- repository: `ni/nimi-python`
- source_path: `docs/nirfsg/.readthedocs.yaml`
- sha256: `b2f40205e32e25afbd845da2eeb68f76898b5896c30ef004309c25f48b76c518`
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
      # Cancel building pull requests when there aren't changes in any of these paths: docs/_static/ docs/nirfsg/.
      #
      # If there are no changes (git diff exits with 0) we force the command to return with 183.
      # This is a special exit code on Read the Docs that will cancel the build immediately.
      - |
        if [ "$READTHEDOCS_VERSION_TYPE" = "external" ] && git diff --quiet origin/master -- docs/_static/ docs/nirfsg/;
        then
          exit 183;
        fi

# Have Read the Docs build documentation with Sphinx
sphinx:
  builder: html
  configuration: docs/nirfsg/conf.py

# If using Sphinx, optionally build your docs in additional formats such as PDF
formats:
  - epub
  - pdf

# Declare the Python requirements required to build your docs
python:
  install:
  - requirements: docs/requirements.txt
````

<!--NI_OSS_SOURCE repo=nimi-python path=docs/nirfsg/about_nirfsg.inc sha256=917453400cadde28042669a2af0e08ec7cdf66dac2b376a88a988a9566bb1c11 bytes=485 -->
## FILE: docs/nirfsg/about_nirfsg.inc

- repository: `ni/nimi-python`
- source_path: `docs/nirfsg/about_nirfsg.inc`
- sha256: `917453400cadde28042669a2af0e08ec7cdf66dac2b376a88a988a9566bb1c11`
- bytes: 485

````text
.. _about-section:

About
=====

The **nirfsg** module provides a Python API for NI-RFSG. The code is maintained in the Open Source repository for `nimi-python <https://github.com/ni/nimi-python>`_.

Support Policy
--------------
**nirfsg** supports all the Operating Systems supported by NI-RFSG.

It follows `Python Software Foundation <https://devguide.python.org/#status-of-python-branches>`_ support policy for different versions of CPython.

NI created and supports **nirfsg**.
````
