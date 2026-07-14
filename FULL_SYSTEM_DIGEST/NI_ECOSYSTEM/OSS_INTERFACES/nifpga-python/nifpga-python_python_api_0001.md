# NI PYTHON API DIGEST: nifpga-python

<!--NI_PYTHON_API_SNAPSHOT repo=ni/nifpga-python commit=6a878b3c124af06e77f9d95cf7c5f8b4a57054d9 -->

<!--NI_PYTHON_API repo=nifpga-python path=nifpga/bitfile.py -->
## PYTHON MODULE: nifpga/bitfile.py

### `class Bitfile(object)`

 Class that represents the contents of the .lvbitx file.

    Bitfile is a class that parses and contains the data from the XML based
    .lvbitx file.  This class can be used to lookup registers and FIFOs and
    is mostly intended to be used by Session.
    

#### `def __init__(self, filepath, parse_contents=False)`

#### `def filepath(self)`

 Returns the filepath used to create this bitfile. 

#### `def signature(self)`

 Returns the signature of the bitfile. 

#### `def build_spec_version(self)`

 Returns the build spec version from the bitfile Documentation, or
        None if not present or empty.
        

#### `def build_spec_description(self)`

 Returns the build spec description from the bitfile Documentation,
        or None if not present or empty.
        

#### `def registers(self)`

 Returns a dictionary of Registers (Controls and Indicators) that
        the bitfile contained.  The dictionary is indexed by the name of the
        register.
        

#### `def fifos(self)`

 Returns a dictionary of FIFOs that the bitfile contained.
        The dictionary is indexed by the name of the FIFO.
        

#### `def base_address_on_device(self)`

 Returns the base address on the device.  This is the offset on the
        device that Registers are located at.  So a Registers offset is
        base_address_on_device + register_offset
        

### `class UnsupportedTypeError(RuntimeError)`

### `def _parse_type(type_xml)`

 Parses the XML given and creates the appropriate type class for it.

    Type XML comes in 2 flavors and we need to handle both.
    We will sometimes (for FIFOs) get a non-recursive "SubType" that just
    provides the type and does not name it.  We will never see Clusters or
    Arrays as the "SubType".
    For registers and sometimes FIFOs, we will always get a recursive type
    containing names for all members.
    

### `class _BaseType(object)`

#### `def __init__(self, name)`

#### `def name(self)`

### `class _String(_BaseType)`

 Handles ignoring string types on the FPGA.  Strings are not supported
    on the FPGA, but sometimes show up in error clusters. 

#### `def __init__(self, name)`

#### `def datatype(self)`

#### `def size_in_bits(self)`

#### `def is_c_api_type(self)`

#### `def unpack_data(self, data)`

#### `def pack_data(self, data_to_pack, packed_data)`

### `class _Numeric(_BaseType)`

 Handles packing and unpacking Numerics such as U8, I8, EnumU8, etc

#### `def __init__(self, name, type_name)`

#### `def _unpack_numeric_unsigned(self, bits_from_fpga)`

#### `def _unpack_numeric_signed(self, bits_from_fpga)`

#### `def datatype(self)`

#### `def size_in_bits(self)`

#### `def is_c_api_type(self)`

#### `def unpack_data(self, data)`

#### `def pack_data(self, data_to_pack, packed_data)`

### `class _Float(_BaseType)`

 Handles packing and unpacking floating point values from the FPGA. 

#### `def __init__(self, name, type_name)`

#### `def datatype(self)`

#### `def size_in_bits(self)`

#### `def is_c_api_type(self)`

#### `def unpack_data(self, data)`

#### `def pack_data(self, data_to_pack, packed_data)`

### `class _Bool(_BaseType)`

 Handles packing and unpacking bools. 

#### `def __init__(self, name)`

#### `def datatype(self)`

#### `def size_in_bits(self)`

#### `def is_c_api_type(self)`

#### `def unpack_data(self, data)`

#### `def pack_data(self, data_to_pack, packed_data)`

### `class ClusterMustContainUniqueNames(RuntimeError)`

 For the FPGA Interface Python API, we have chosen to represent clusters
    as dictionaries.  This has a relatively straight forward conversion, but
    requires that all members of the cluster have a unique label.

### `class _Cluster(_BaseType)`

 Handles packing and unpacking clusters. 

#### `def __init__(self, name, type_xml)`

#### `def datatype(self)`

#### `def size_in_bits(self)`

#### `def is_c_api_type(self)`

#### `def _unpack_data_recursive(self, data, result, child_iter)`

 Clusters are stored in the correct order in the blob, but since we
        parse the blob from least significant to most, we are parsing the clusters
        out backwards. So parse out the data backwards going down the stack and
        add it to the dict going back up the stack. This way we insert into the
        OrderedDict in the correct order

#### `def unpack_data(self, data)`

#### `def pack_data(self, data_to_pack, packed_data)`

### `class _Array(_BaseType)`

 Handles packing and unpacking arrays. 

#### `def __init__(self, name, type_xml)`

#### `def datatype(self)`

#### `def size(self)`

#### `def size_in_bits(self)`

#### `def is_c_api_type(self)`

#### `def unpack_data(self, data)`

#### `def pack_data(self, data_to_pack, packed_data)`

### `class _FXP(_BaseType)`

 Handles packing and unpacking FXP values from the FPGA. 

#### `def __init__(self, name, type_xml)`

#### `def datatype(self)`

#### `def size_in_bits(self)`

#### `def is_c_api_type(self)`

#### `def _calculate_delta(self)`

 Determines the fixed point delta value, the value of the register
        is only allowed to be an integer multiple of the delta. For example if
        delta is 1, then it is impossible to represent a fraction.
        The value persisted in the bitfile for delta is not always correct,
        therefore we must calculate it manually.
        

#### `def _calculate_minimum(self)`

 Determines the minimum possible value that can be represented with
        the given fixed point register. The value persisted in the bitfile for
        the minimum value is not always accurate, therefore we must calculate
        it manually.
        

#### `def _calculate_maximum(self)`

 Determines the minimum possible value that can be represented with
        the given fixed point register.The value persisted in the bitfile for
        the maximum value is not always accurate, therefore we must calculate
        it manually.
        

#### `def _calculate_size_in_bits(self)`

 Fixed point values are transfered to the driver as an array of U32
        The length is between 1 and 3 determined by the word length (includes
        the signed bit) plus the include_overflow_status_enable bit.
        

#### `def unpack_data(self, data)`

 This method converts value from hardware and returns the respective
        decimal value or a tuple with the overflow status and the decimal
        value.
        

#### `def _get_overflow_value(self, data)`

 Mask out all the data within the word length, leaving the overflow
        bit. If the result after masking the the word portion of the fixed
        point is nonzero that indicates the data read has overflowed. 

#### `def _remove_overflow_bit(self, data)`

 This helper method masks out all bits not inside the word length,
        ultimately returning a value of data without the overflow bit. 

#### `def _integer_twos_comp(self, data)`

 Checks the signed bit and determines if the value is negative, If
        so take the twos complement of the input.

#### `def pack_data(self, data_to_pack, packed_data)`

#### `def _validate_and_parse_user_input(self, user_input)`

#### `def _convert_value_to_fxp(self, data)`

#### `def warn_coerced_data(self)`

### `class Register(object)`

#### `def __init__(self, reg_xml)`


        A control or indicator from the front panel of the top level FPGA VI

        reg_xml: the <Register> XML element, e.g. one of these:
            <Register>
                <Name>Output Array Bool 17</Name>
                <Indicator>true</Indicator>
                <Datatype>
                    <Array>
                        <Name>Output Array Bool 17</Name>
                        <Size>17</Size>
                        <Type>
                            <Boolean>
                            </Boolean>
                        </Type>
                    </Array>
                </Datatype>
                <Offset>98364</Offset>
                <Internal>false</Internal>
                <AccessMayTimeout>false</AccessMayTimeout>
            </Register>

            Or

            <Register>
                <Name>Input U64</Name>
                <Indicator>false</Indicator>
                <Datatype>
                    <U64>
                    </U64>
                </Datatype>
                <Offset>98464</Offset>
                <Internal>false</Internal>
                <AccessMayTimeout>false</AccessMayTimeout>
            </Register>
        

#### `def __len__(self)`

 Returns the number of elements in this register. 

#### `def name(self)`

 Returns the name of the Register. 

#### `def datatype(self)`

 Returns a string containing the datatype of the Register. 

#### `def type(self)`

#### `def is_array(self)`

 Returns whether or not this Register is an array 

#### `def is_indicator(self)`

 Returns whether or not this Register is an Indicator 

#### `def offset(self)`

 Returns the offset of this register from the base address. 

#### `def access_may_timeout(self)`

 Returns Whether or not this register access could timeout.
        This could happen if the register is in an external clock domain.
        

#### `def is_internal(self)`

 Returns whether or not this register is for internal use. 

#### `def __str__(self)`

### `def _is_not_power_of_2(value)`

### `class Fifo(object)`

#### `def __init__(self, channel_xml)`

#### `def datatype(self)`

 Returns the datatype string of the FIFO. 

#### `def number(self)`

 Returns the FIFO number.
        This number is the unique identifier for the FIFO in this bitfile.
        

#### `def name(self)`

 Returns the name of the FIFO. 

#### `def type(self)`

#### `def transfer_size_bytes(self)`

 The size of one FIFO element in bytes. 

#### `def is_fxp(self)`

#### `def is_composite(self)`

<!--NI_PYTHON_API repo=nifpga-python path=nifpga/nifpga.py -->
## PYTHON MODULE: nifpga/nifpga.py

### MODULE DOCSTRING


NiFpga, a thin wrapper around the FPGA Interface C API

Copyright (c) 2015 National Instruments


### `class DataType(Enum)`

 DataType is an enumerator, with the intention of abstracting the
    association between datatypes and ctypes within the Python API.
    

#### `def __str__(self)`

#### `def _return_ctype(self)`

 Returns the associated ctype of a given datatype. 

#### `def isSigned(self)`

### `class FifoPropertyType(Enum)`

 Types of FIFO Properties, intended to abstract away the C Type. 

#### `def __str__(self)`

#### `def _return_ctype(self)`

 Returns the associated ctype of a given property type. 

### `class FifoProperty(Enum)`

#### `def __str__(self)`

### `class FlowControl(Enum)`

 When flow control is disabled, the FIFO no longer acts like a FIFO.
    The FIFO will overwrite data in this mode. The FPGA fully controls when
    data transfers. This can be useful when regenerating a waveform or when
    you only care about the most recent data.
    For Host to Target FIFOs, this only disables flow control when the entire FIFO
    has been written once.
    For Target to Host FIFOs, flow control is disabled on start and the FPGA can
    begin writing then.
    

### `class DmaBufferType(Enum)`

 Allocated by RIO means the driver take the other properties and create
    a buffer that meets their requirements.
    

### `class FpgaViState(Enum)`

 The FPGA VI has either been downloaded and not run, or the VI was aborted
    or reset. 

- `OPEN_ATTRIBUTE_NO_RUN = 1`

- `OPEN_ATTRIBUTE_BITFILE_PATH_IS_UTF8 = 2`

- `RUN_ATTRIBUTE_WAIT_UNTIL_DONE = 1`

- `CLOSE_ATTRIBUTE_NO_RESET_IF_LAST_SESSION = 1`

- `INFINITE_TIMEOUT = 4294967295`

### `class _NiFpga(StatusCheckedLibrary)`


    _NiFpga, a thin wrapper around the FPGA Interface C API

    Defines FPGA Interface C API types, and provides the _NiFpga class
    which loads C API symbols and allows them to be called, e.g.
    nifpga.Open(<args>) or nifpga["ReadU32](<args>). If any NiFpga function
    return status is non-zero, the appropriate exception derived from either
    WarningStatus or ErrorStatus is raised.

    While _NiFpga can be used directly, Session provides a higher-level and
    more convenient API that is better-suited for most users.
    

#### `def __init__(self)`

<!--NI_PYTHON_API repo=nifpga-python path=nifpga/session.py -->
## PYTHON MODULE: nifpga/session.py

### MODULE DOCSTRING


Session, a convenient wrapper around the low-level _NiFpga class.

Copyright (c) 2017 National Instruments


### `class Session(object)`


    Session, a convenient wrapper around the low-level _NiFpga class.

    The Session class uses regular python types, provides convenient default
    arguments to C API functions, and makes controls, indicators, and FIFOs
    available by name. If any NiFpga function return status is non-zero, the
    appropriate exception derived from either WarningStatus or ErrorStatus is
    raised.
    Example usage of FPGA configuration functions::

        with Session(bitfile="myBitfilePath.lvbitx", resource="RIO0") as session:
            session.run()
            session.download()
            session.abort()
            session.reset()

    Note:
        It is always recommended that you use a Session with a context manager
        (with). Opening a Session without a context manager could cause you to
        leak the session if :meth:`Session.close` is not called.

    Controls and indicators are accessed directly via a _Register object
    obtained from the session::

        my_control = session.registers["MyControl"]
        my_control.write(data=4)
        data = my_control.read()

    FIFOs are accessed directly via a _FIFO object obtained from the session::

        myHostToFpgaFifo = session.fifos["MyHostToFpgaFifo"]
        myHostToFpgaFifo.stop()
        actual_depth = myHostToFpgaFifo.configure(requested_depth=4096)
        myHostToFpgaFifo.start()
        empty_elements_remaining = myHostToFpgaFifo.write(data=[1, 2, 3, 4],
                                                          timeout_ms=2)

        myFpgaToHostFifo = session.fifos["MyHostToFpgaFifo"]
        read_values = myFpgaToHostFifo.read(number_of_elements=4,
                                            timeout_ms=0)
        print(read_values.data)
    

#### `def __init__(self, bitfile, resource, no_run=False, reset_if_last_session_on_exit=False, **kwargs)`

Creates a session to the specified resource with the specified
        bitfile.

        Args:
            bitfile (str)(Bitfile): A bitfile.Bitfile() instance or a string
                                    filepath to a bitfile.
            resource (str): e.g. "RIO0", "PXI1Slot2", or "rio://hostname/RIO0"
                            or an already open session
            no_run (bool): If true, don't run the bitfile, just open the
                session.
            reset_if_last_session_on_exit (bool): Passed into Close on
                exit. Unused if not using this session as a context guard.
            **kwargs: Additional arguments that edit the session.
        

#### `def __enter__(self)`

#### `def __exit__(self, exception_type, exception_val, trace)`

#### `def close(self, reset_if_last_session=False)`

 Closes the FPGA Session.

        Args:
            reset_if_last_session (bool): If True, resets the FPGA on the
                last close. If true, does not reset the FPGA on the last
                session close.
        

#### `def run(self, wait_until_done=False)`

 Runs the FPGA VI on the target.

        Args:
            wait_until_done (bool): If true, this functions blocks until the
                                    FPGA VI stops running
        

#### `def abort(self)`

 Aborts the FPGA VI. 

#### `def download(self)`

 Re-downloads the FPGA bitstream to the target. 

#### `def reset(self)`

 Resets the FPGA VI. 

#### `def fpga_vi_state(self)`

 Returns the current state of the FPGA VI. 

#### `def _irq_ordinals_to_bitmask(self, ordinals)`

#### `def wait_on_irqs(self, irqs, timeout_ms)`

 Stops the calling thread until the FPGA asserts any IRQ in the irqs
        parameter or until the function call times out.

        Args:
            irqs: A list of irq ordinals 0-31, e.g. [0, 6, 31].
            timeout_ms: The timeout to wait in milliseconds.

        Returns:
            session_wait_on_irqs (namedtuple)::

                session_wait_on_irqs.irqs_asserted (list): is a list of the
                    asserted IRQs.
                session_wait_on_irqs.timed_out (bool): Outputs whether or not
                    the time out expired before all irqs were asserted.

        

#### `def acknowledge_irqs(self, irqs)`

 Acknowledges an IRQ or set of IRQs.

        Args:
            irqs (list): A list of irq ordinals 0-31, e.g. [0, 6, 31].
        

#### `def _get_unique_register_or_fifo(self, name)`

#### `def registers(self)`

 This property returns a dictionary containing all registers that
        are associated with the bitfile opened with the session. A register can
        be accessed by its unique name.
        

#### `def _internal_registers(self)`

 This property contains internal registers

#### `def fifos(self)`

 This property returns a dictionary containing all FIFOs that are
        associated with the bitfile opened with the session. A FIFO can be
        accessed by its unique name.
        

#### `def _create_register(self, bitfile_register, base_address_on_device)`

#### `def _create_fifo(self, bitfile_fifo)`

### `class _Register(object)`

 _Register is a private class that is a wrapper of logic that is
    associated with controls and indicators.

    All Registers will exists in a sessions session.registers property. This
    means that all possible registers for a given session are created during
    session initialization; a user should never need to create a new instance
    of this class.

    

#### `def __init__(self, session, nifpga, bitfile_register, base_address_on_device, read_func=None, write_func=None)`

#### `def __len__(self)`

 A single register will always have one and only one element.

        Returns:
            (int): Always a constant 1.
        

#### `def write(self, data)`

 Writes the specified data to the control or indicator

        Args:
            data (DataType.value): The data to be written into the register
        

#### `def read(self)`

 Reads a single element from the control or indicator

        Returns:
            data (DataType.value): The data inside the register.
        

#### `def name(self)`

 Property of a register that returns the name of the control or
        indicator. 

#### `def datatype(self)`

 Property of a register that returns the datatype of the control or
        indicator. 

### `class _ArrayRegister(_Register)`


    _ArryRegister is a private class that inherits from _Register with
    additional interfaces unique to the logic of array controls and indicators.
    

#### `def __init__(self, session, nifpga, bitfile_register, base_address_on_device)`

#### `def __len__(self)`

 Returns the length of the array.

        Returns:
            (int): The number of elements in the array.
        

#### `def write(self, data)`

 Writes the specified array of data to the control or indicator

            Args:
                data (list): The data "array" to be written into the registers
                wrapped into a python list.
        

#### `def read(self)`

 Reads the entire array from the control or indicator.

        Returns:
            (list): The data in the register in a python list.
        

### `class _DataConvertingRegister(_Register)`


    _DataConvertingRegister does all the work of converting the LabVIEW Cluster
    and fixed point types into something more native to python. As a
    user you will read and write to this register just as you would any other
    register. Given the nature of fixed point there are a few caveats.

    Just like the other registers, we do not support users creating their
    instances of _FxpRegister, but after opening a session to a valid bitfile
    the session.registers property will contain all registers fixed point
    included.

    Fixed point registers should be easily used from python with a few caveats:
        1. Trying to write a value that does not conform to boundaries of the
        defined register, will be coerced just as it would in labVIEW. Input
        a value that needs to be coerced will result in a warning to the user.
        A value is to be coerced if it is not a multiple of the delta value, or
        if it exceeds the minimum or maximum values.
    

#### `def __init__(self, session, nifpga, bitfile_register, base_address_on_device)`

#### `def read(self)`

 Reads the value from the control or indicator

        Returns:
            data (value_type): The data inside the register.
        

#### `def _combine_array_of_u32_into_one_value(self, data)`

 This method is a helper to convert the array read from hardware
        and return a single value removing any excessive bits. Whenever
        the array is longer than 1 element, the data is left justified, we need
        to shift the combined data to the right before doing the conversion.
        For example, if the register had a word length of 54, the 54 MSB would
        be the fixed point bits. The 10 LSB of the combinedData must be shifted
        off in order to not mess up further calculations.

        

#### `def write(self, user_input)`

 Writes the user's the users input into the register as a fixed
        point number. Any inputs outside the bounds of this fixed point
        register will be coerced and the user will be warned. The user input's
        supported include any python Number.

            Args:
                Number: user numerical input to be converted to fixed point.
                (bool, Number): Tuple with the members : Boolean for overflow,
                                user numerical input to be converted to fixed
                                point.
        

#### `def _convert_to_u32_array(self, data)`

### `class _FIFO(object)`

 _FIFO is a private class that is a wrapper for the logic that
    associated with a FIFO.

    All FIFOs will exists in a sessions session.fifos property. This means that
    all possible FIFOs for a given session are created during session
    initialization; a user should never need to create a new instance of this
    class.
    

#### `def __init__(self, session, nifpga, bitfile_fifo, datatype=None)`

#### `def configure(self, requested_depth)`

 Specifies the depth of the host memory part of the DMA FIFO.

        Args:
            requested_depth (int): The depth of the host memory part of the DMA
                                   FIFO in number of elements.

        Returns:
            actual_depth (int): The actual number of elements in the host
            memory part of the DMA FIFO, which may be more than the
            requested number.
        

#### `def start(self)`

 Starts the FIFO. 

#### `def stop(self)`

 Stops the FIFO. 

#### `def unreserve(self)`

 Unreserves the FIFO.

        FIFOs are reserved by the first process that uses them.  This call will
        unreserve them from the calling process so a different process may use
        the FIFO.
        

#### `def write(self, data, timeout_ms=0)`

 Writes the specified data to the FIFO.

        NOTE:
            If the FIFO has not been started before calling
            :meth:`_FIFO.write()`, then it will automatically start and
            continue to work as expected.

        Args:
            data (list): Data to be written to the FIFO.
            timeout_ms (int): The timeout to wait in milliseconds.

        Returns:
            elements_remaining (int): The number of elements remaining in the
            host memory part of the DMA FIFO.
        

#### `def read(self, number_of_elements, timeout_ms=0)`

 Read the specified number of elements from the FIFO.

        NOTE:
            If the FIFO has not been started before calling
            :meth:`_FIFO.read()`, then it will automatically start and continue
            to work as expected.

        Args:
            number_of_elements (int): The number of elements to read from the
                                      FIFO.
            timeout_ms (int): The timeout to wait in milliseconds.

        Returns:
            ReadValues (namedtuple)::

                ReadValues.data (list): containing the data from
                    the FIFO.
                ReadValues.elements_remaining (int): The amount of elements
                    remaining in the FIFO.
        

#### `def _acquire_write(self, number_of_elements, timeout_ms=0)`

 Write the specified number of elements from the FIFO.

        Args:
            number_of_elements (int): The number of elements to read from the
                                      FIFO.
            timeout_ms (int): The timeout to wait in milliseconds.

        Returns:
            AcquireWriteValues(namedtuple)::

                AcquireWriteValues.data (ctypes.pointer): Contains the data
                    from the FIFO.
                AcquireWriteValues.elements_acquired (int): The number of
                    elements that were actually acquired.
                AcquireWriteValues.elements_remaining (int): The amount of
                    elements remaining in the FIFO.
        

#### `def _acquire_read(self, number_of_elements, timeout_ms=0)`

 Read the specified number of elements from the FIFO.

        Args:
            number_of_elements (int): The number of elements to read from the
                                      FIFO.
            timeout_ms (int): The timeout to wait in milliseconds.

        Returns:
            AcquireReadValues(namedtuple): has the following members::

                AcquireReadValues.data (ctypes.pointer): Contains the data
                    from the FIFO.
                AcquireReadValues.elements_acquired (int): The number of
                    elements that were actually acquired.
                AcquireReadValues.elements_remaining (int): The amount of
                    elements remaining in the FIFO.
        

#### `def _release_elements(self, number_of_elements)`

 Releases the FIFOs elements. 

#### `def acquire_read_region(self, number_of_elements, timeout_ms=0)`

 Acquire regions of the FIFO's buffer directly.

        This function can be useful if you are going to access large sections of
        FIFO buffer at one time and don't want a copy of it in memory.

        Args:
            number_of_elements (int): The number of elements to read from the
                                      FIFO.
            timeout_ms (int): The timeout to wait in milliseconds.

        Returns:
            AcquireRegionValues(namedtuple): has the following members::

                AcquireRegionValues.region (_FIFODataRegion): A region that can
                    be used with a content manager to access elements in the FIFO.
                AcquireRegionValues.elements_acquired (int): The number of
                    elements that were actually acquired.
                AcquireRegionValues.elements_remaining (int): The amount of
                    elements remaining in the FIFO.
        

#### `def acquire_write_region(self, number_of_elements, timeout_ms=0)`

 Acquire regions of the FIFO's buffer directly.

        This function can be useful if you are going to access large sections of
        FIFO buffer at one time and don't want a copy of it in memory.

        Args:
            number_of_elements (int): The number of elements to read from the
                                      FIFO.
            timeout_ms (int): The timeout to wait in milliseconds.

        Returns:
            AcquireRegionValues(namedtuple): has the following members::

                AcquireRegionValues.region (_FIFODataRegion): A region that can
                    be used with a content manager to access elements in the FIFO.
                AcquireRegionValues.elements_acquired (int): The number of
                    elements that were actually acquired.
                AcquireRegionValues.elements_remaining (int): The amount of
                    elements remaining in the FIFO.
        

#### `def release_region(self, accessor)`

 Releases a region.

        Args:
            accessor (_FIFODataAccessor): the accessor from the acquired region
        

#### `def get_peer_to_peer_endpoint(self)`

 Gets an endpoint reference to a peer-to-peer FIFO. 

#### `def commit_configuration(self)`

 Resolves and Commits property changes made to the FIFO. 

#### `def name(self)`

 Property of a Fifo that contains its name. 

#### `def datatype(self)`

 Property of a Fifo that contains its datatype. 

#### `def _get_fifo_property(self, prop)`

#### `def _set_fifo_property(self, prop, value)`

#### `def buffer_allocation_granularity(self)`

 The allocation granularity of the host memory part of a DMA FIFO.

        By default this will usually be a page size, which is optimal for most
        devices.  This property can be used to customize it.
        

#### `def buffer_allocation_granularity(self, value)`

#### `def buffer_size(self)`

 The size in elements of the Host Memory part of a DMA FIFO. 

#### `def buffer_size(self, value)`

#### `def _mirror_size(self)`

 The amount of elements in the Host Memory part of the DMA FIFO that
        mirror elements at the beginning.

        The Host Memory part of a DMA FIFO is a circular buffer.  This means that
        when we hit the end of the buffer we have to deal with the logic of wrapping
        around the buffer.  Mirrored elements are elements at the beginning of
        the buffer that are mapped twice in memory to the end of the buffer.
        Settings this value can allow us to avoid wrap arounds.

        This is mostly useful when using our Zero Copy API.  Its not yet
        supported in Python though, so this property is private.
        

#### `def _mirror_size(self, value)`

#### `def _dma_buffer_type(self)`

#### `def _dma_buffer_type(self, value)`

#### `def _dma_buffer(self)`

#### `def _dma_buffer(self, value)`

#### `def flow_control(self)`

 Controls whether the FPGA will wait for the host when using FIFOs.

        If flow control is disabled, the FPGA will have free reign to read or
        write elements before the host is ready.  This means the FIFO no longer
        acts in a First In First Out manner.

        For Host To Target FIFOs, this feature is useful when you want to put
        something like a waveform in a FIFO and let the FPGA continue reading
        that waveform over and over without any involvement from the host.

        For Target To Host FIFOs, this feature is useful when you only care
        about the latest data and don't care about old data.
        

#### `def flow_control(self, value)`

#### `def elements_currently_acquired(self)`

#### `def preferred_numa_node(self)`

#### `def preferred_numa_node(self, value)`

### `class _FxpFIFO(_FIFO)`


    FXP FIFOs are packed up to 64bits
    

#### `def __init__(self, session, nifpga, bitfile_fifo)`

#### `def datatype(self)`

#### `def write(self, data, timeout_ms=0)`

 Writes the specified data to the FIFO.

        NOTE:
            If the FIFO has not been started before calling
            :meth:`_FIFO.write()`, then it will automatically start and
            continue to work as expected.

        Args:
            data (list): Data to be written to the FIFO.
            timeout_ms (int): The timeout to wait in milliseconds.

        Returns:
            elements_remaining (int): The number of elements remaining in the
            host memory part of the DMA FIFO.
        

#### `def read(self, number_of_elements, timeout_ms=0)`

 Read the specified number of elements from the FIFO.

        NOTE:
            If the FIFO has not been started before calling
            :meth:`_FIFO.read()`, then it will automatically start and continue
            to work as expected.

        Args:
            number_of_elements (int): The number of elements to read from the
                                      FIFO.
            timeout_ms (int): The timeout to wait in milliseconds.

        Returns:
            ReadValues (namedtuple)::

                ReadValues.data (list): containing the data from
                    the FIFO.
                ReadValues.elements_remaining (int): The amount of elements
                    remaining in the FIFO.
        

### `def _combine_array_of_u8_into_one_value(data, element_index, transfer_size_bytes, size_in_bits)`

 This method is a helper to convert the array read from hardware
    and return a single element removing any excessive bits.

    First we combine the data into a single number while swapping the
    endianness.

    Whenever the array is longer than 1 word, the data is left justified, we
    need to shift the combined data to the right before doing the
    conversion.
    For example, if the element had a size in bits of 54, the 54 MSB would
    be the data bits. The 10 LSB of the combinedData must be shifted
    off in order to not mess up further calculations.
    

### `def _convert_to_u8_array(u8_array, element_index, data, transfer_size_bytes, size_in_bits)`

 Converts the data into the format expected by the FPGA FIFO and inserts it
    into the given u8_array at the provided element_index.
    

### `class _DataConvertingFifo(_FIFO)`


    Converts FIFOs that transfer data that is packed in the FPGA representation
    into Python types.  In this case, it converts a FIFO of clusters into lists
    of OrderedDicts and back.
    

#### `def __init__(self, session, nifpga, bitfile_fifo)`

#### `def datatype(self)`

#### `def write(self, data, timeout_ms=0)`

#### `def read(self, number_of_elements, timeout_ms=0)`

### `class _FIFODataAccessor(object)`


        Accesses FIFO Data element by element.
    

#### `def __init__(self, buffer, type, bytes_per_element, number_of_elements)`

#### `def __iter__(self)`

#### `def __getitem__(self, index)`

#### `def __setitem__(self, index, value)`

#### `def __len__(self)`

#### `def __eq__(self, other)`

#### `def __str__(self)`

#### `def __repr__(self)`

### `class _FIFODataRegion(object)`

#### `def __init__(self, accessor, region, fifo)`

#### `def __enter__(self)`

#### `def __exit__(self, exception_type, exception_val, trace)`

#### `def accessor(self)`

#### `def release(self)`

<!--NI_PYTHON_API repo=nifpga-python path=nifpga/status.py -->
## PYTHON MODULE: nifpga/status.py

### MODULE DOCSTRING


An set of status exception classes to be used when an NiFpga
function returns either a warning or error status.

Use check_status() to raise an appropriate exception if necessary.

Error and Warning exception class names are auto-generated from the
strings in 'codeToString' in this file.
For example, handle a fatal error like this:

    >>> @check_status('frob', ['foo', 'bar', 'baz'])
    ... def frob(foo, bar, baz):
    ...     return -61141
    ...
    >>> try:
    ...     frob(0, 1, 2)
    ... except FpgaBusyError as e:
    ...     print(e)  # doctest: +NORMALIZE_WHITESPACE
    Error: FpgaBusy (-61141) when calling 'frob' with arguments:
        foo: 0x0
        bar: 0x1
        baz: 0x2

Or handle a warning like this:

    >>> @check_status('frob', ['foo', 'bar', 'baz'])
    ... def frob(foo, bar, baz):
    ...     return 61003
    ...
    >>> with warnings.catch_warnings(record=True) as w:
    ...     frob(0, 1, 2)
    ...     print(w[0].message)  # doctest: +NORMALIZE_WHITESPACE
    Warning: FpgaAlreadyRunning (61003) when calling 'frob' with arguments:
        foo: 0x0
        bar: 0x1
        baz: 0x2

Copyright (c) 2017 National Instruments


### `def _raise_or_warn_if_nonzero_status(status, function_name, argument_names, *args)`


    Helper for the 'check_status' decorator.

    Raises the proper ErrorStatus subclass or warns the proper WarnStatus
    subclass if status is not 0 (success).

    function_name: the name of the function, e.g. "NiFpga_ConfigureFifo"
        Used to make the exception message more useful.
    argument_names: list of names of the arguments to the function
        e.g. ["session", "fifo"]
    args: the arguments that were passed to the function

    'argument_names' and 'args' are used to make the exception message
    more useful, and to find the arguments after catching an exception if
    the function fails (e.g. 'e.get_args()["session"]').
    

### `def check_status(function_name, argument_names)`


    Decorator (that takes arguments) to call a function and raise
    an appropriate subclass of Status if the
    returned status is not zero.
    Also validates that the number of parameters passed to the
    function is correct.

    function_name: the name of the function, e.g. "NiFpga_ConfigureFifo"
        Used to make the exception message more useful.
    argument_names: list of names of the arguments to the function
        e.g. ["session", "fifo"]
        Used to make the exception message more useful, and to find the
        arguments after catching an exception if the function fails
        (e.g. 'e.get_args()["session"]').
    

### `class Status(BaseException)`

#### `def __init__(self, code, code_string, function_name, argument_names, function_args)`

 Base exception class for when an NiFpga function returns a non-zero
        status.

        Args:
            code (int): e.g. -52000
            code_string (str) : e.g. 'MemoryFull'
            function_name (string): the function that returned the error or
                warning status. e.g. 'NiFpga_ConfigureFifo'
            argument_names (list): a list of the names of the arguments to the
                function. e.g. ["session", "fifo", "requested depth"]
            function_args (tuple) : a tuple of the arguments passed to the
                function. The order of argument_names should correspond to the
                order of function_args. e.g. '(session, fifo, depth)'
        

#### `def get_code(self)`

#### `def get_code_string(self)`

#### `def get_function_name(self)`

 Returns a string for the functions name, 

#### `def get_args(self)`


        Returns a dictionary of argument names to argument values of
        the function that caused the exception to be raised.

        Returns:
        arg_dict (dictionary): Converts ctypes args to their actual values
        instead of the  ctypes instance. e.g.

        .. code-block:: python

            {
            "session":0x10000L,
            "fifo" : 0x0,
            ...}



        

#### `def _stringify_arg(self, arg)`


        Converts a function argument to a readable string for debugging.

        Stringify ctypes values, instead of the ctypes instance itself.
        Adds single quotes around strings (so it's obvious they are strings).
        Stringify numbers as hex to make it easier to decode
        bit packed sessions, attributes, etc.
        

#### `def __str__(self)`


        Returns the function name, status code, and arguments used.
        Example:

        .. code-block:: python

            Error: FifoTimeout (-50400) when calling 'Dummy Function Name' with
            arguments:
                session: 0xbeef
                fifo: 0xf1f0L
                data: 0xda7aL
                number of elements: 0x100L
                timeout ms: 0x200L
                elements remaining: 0x300L
                a bogus string argument: 'I am a string'
        

### `class WarningStatus(Status, RuntimeWarning)`


    Base warning class for when an NiFpga function returns a warning (> 0)
    status.

    Useful if trying to catch warning and error status exceptions separately
    

#### `def __init__(self, code, code_string, function_name, argument_names, function_args)`

### `class ErrorStatus(Status, RuntimeError)`


    Base Error class for when an NiFpga function returns an error (< 0)
    status.

    Useful if trying to catch warning and error status exceptions separately
    

#### `def __init__(self, code, code_string, function_name, argument_names, function_args)`

### `class UnknownWarning(WarningStatus)`

#### `def __init__(self, code, function_name, argument_names, function_args)`

### `class UnknownError(ErrorStatus)`

#### `def __init__(self, code, function_name, argument_names, function_args)`

<!--NI_PYTHON_API repo=nifpga-python path=nifpga/statuscheckedlibrary.py -->
## PYTHON MODULE: nifpga/statuscheckedlibrary.py

### `class FunctionInfo(object)`

#### `def __init__(self, function, name, argument_names)`


        A struct describing a function to be used in StatusCheckedFunctions.
        Args:
            function (str): the callable function itself
            name (str): A name used to call 'function'
                e.g. "ReadFifoU32".
                See 'StatusCheckedFunctions' to see this parameter's usage
                and how functions are called with this name.
            argument_names (list): a list of the strings of the arguments to
            'function'
                e.g. ["session",
                        "fifo",
                        "data",
                        "number of elements",
                        "timeout ms",
                        "elements remaining"]
                Used for printing helpful messages if the function fails,
                and to get arguments after catching an exception if
                the function fails (e.g. 'e.get_args()["session"]').
        

#### `def __str__(self)`

### `class StatusCheckedFunctions(object)`

#### `def __init__(self, function_infos)`


        A class to wrap functions that return an Status error code. Each
        function is wrapped with a closure that raises an appropriate derived
        class of Status if the returned error code is non-zero.

        Args:
            function_infos (list): A list of FunctionInfo objects

        The name from each FunctionInfo can be used to call its associated
        function, e.g.::

            def my_raw_func(code)
                return code

            checked_functions =                     StatusCheckedFunctions(
                        function_infos=[                            FunctionInfo(
                                function=my_raw_func,
                                name="MyFunc",
                                argument_names="code to return")
                        ])

            # This raises FifoTimeoutError with a useful error message
            # mentioning all arguments, such as 'code to return'.
            checked_functions.MyFunc(-50400)

            # Returns with no exceptions thrown
            checked_functions.MyFunc(0)

            # You can also call functions using the bracket operator.
            # This raises FifoTimeoutWarning.
            checked_functions["MyFunc"](50400)
        

#### `def __getitem__(self, key)`


        Override bracket operator to call wrapped functions.

        For convenience when function names are dynamically built, e.g.,
        makes this work:
            datatype = "U64"
            <this object>['ReadArray%s' % datatype](session, ...)
        

### `class NamedArgtype(object)`

#### `def __init__(self, name, argtype)`


        A struct of a name and ctypes argtype for a function argument
        to be used in a LibraryFunctionInfo.
        name: e.g. "session"
            Used for printing helpful messages if the function fails,
            and to get arguments after catching an exception if
            the function fails (e.g. 'e.get_args()["session"]').
        argtype: e.g. "ctypes.c_uint32", the ctypes type of the argument
        

### `class LibraryFunctionInfo(object)`

#### `def __init__(self, pretty_name, name_in_library, named_argtypes)`


        A struct describing a library entry point function to be used
        in StatusCheckedLibrary.
        pretty_name: e.g. "Run"
            A "pretty" name by which a StatusCheckedLibrary object will
            call the function.
        name_in_library: e.g. "NiFpgaDll_Run"
            The name of the actual DLL entry point used to call the function.
        named_argtypes: e.g. [NamedArgtype("session", _SessionType),
                                NamedArgtype("fifo", ctypes.c_uint32)]
            A list of NamedArgtype structs used to call the function.
        

### `class LibraryNotFoundError(RuntimeError)`

### `class StatusCheckedLibrary(StatusCheckedFunctions)`

#### `def __init__(self, library_name, library_function_infos)`


        Raises exceptions from entry points that return NiFpga_Status codes.

        library_name: e.g. "NiFpga" (libNiFpga.so, NiFpga.dll)
        library_function_infos: a list of library_function_info objects

        Automatically wraps each entry point named in library_function_infos
        with a closure that raises an appropriate derived class of
        Status if the returned error code is non-zero.

        The pretty_name from the LibraryFunctionInfo's passed to the
        constructor can be used to call functions in the library, e.g.:
            cool_library =                 StatusCheckedLibrary(
                    library_name="CoolLibrary",  # CoolLibrary.dll, libCoolLibrary.so
                    library_function_infos=[                        LibraryFunctionInfo(
                            pretty_name="AwesomeFunction",
                            name_in_library="CoolLibraryEntrypoint_AwesomeFunction",
                            named_argtypes=[NamedArgtype("session", ctypes.c_uint32)])
                    ])

            # Both lines below call "CoolLibraryEntrypoint_AwesomeFunction()"
            # from CoolLibrary.dll (or libCoolLibrary.so) with '7' as a uint32_t
            # argument.
            cool_library.AwesomeFunction(7)
            cool_library["AwesomeFunction"](7)
        

<!--NI_PYTHON_API repo=nifpga-python path=nifpga/tests/test_bitfile.py -->
## PYTHON MODULE: nifpga/tests/test_bitfile.py

- `BITFILE_ALL_REGISTERS = 'nifpga/tests/allregistertypes.lvbitx'`

### `class BitfileTest(unittest.TestCase)`

#### `def test_parse_from_path(self)`

#### `def test_parse_from_contents(self)`

#### `def test_parse_bitfile_with_fxp_fifo(self)`

#### `def test_parse_bitfile_with_fxp_register_array(self)`

#### `def test_build_spec_version(self)`

#### `def test_build_spec_description(self)`

#### `def test_build_spec_version_none_when_empty(self)`

<!--NI_PYTHON_API repo=nifpga-python path=nifpga/tests/test_Cluster.py -->
## PYTHON MODULE: nifpga/tests/test_Cluster.py

### `class ClusterTests(unittest.TestCase)`

#### `def setUp(self)`

#### `def test_cluster_zero_data(self)`

#### `def test_cluster_values_set_to_1(self)`

#### `def test_cluster_random_data(self)`

#### `def test_unsupported_type(self)`

#### `def test_error_when_multiple_members(self)`

<!--NI_PYTHON_API repo=nifpga-python path=nifpga/tests/test_FXP.py -->
## PYTHON MODULE: nifpga/tests/test_FXP.py

### `class MockFxp(_FXP)`

#### `def __init__(self, signed, enableOverflowStatus, word_length, integer_word_length)`

#### `def set_register_attributes(self)`

### `class FXPRegisterAsserts(object)`

#### `def __init__(self, test)`

#### `def assert_fxp_value_converted_to_decimal(self, register, read_value, expected_value)`

#### `def assert_user_input_converted_to_fxp(self, register, user_input, expected_value)`

### `def _calculate_minimum_fxp_value(register)`

### `def _calculate_maximum_fxp_value(register)`

### `class FXPRegisterSharedTests(unittest.TestCase)`

#### `def setUp(self)`

#### `def test_converting_fxp_to_decimal_value(self)`

#### `def test_converting_user_data_into_binary(self)`

#### `def test_user_input_less_than_minimum(self)`

#### `def test_user_input_greater_than_maximum(self)`

### `class FXPRegister16bitWord16bitInteger(FXPRegisterSharedTests)`

#### `def setUp(self)`

### `class FXPRegister16bitWord16bitIntegerSigned(FXPRegisterSharedTests)`

#### `def setUp(self)`

### `class FXPRegister15bitWord15bitIntegerOverflow(FXPRegisterSharedTests)`

#### `def setUp(self)`

#### `def test_converting_user_data_without_overflow_use_false(self)`

### `class FXPRegister15bitWord15bitIntegerSignedOverflow(FXPRegisterSharedTests)`

#### `def setUp(self)`

#### `def test_overflow_bit_is_not_calculated_in_twos_compliment(self)`

### `class FXPRegister16bitWord0bitInteger(FXPRegisterSharedTests)`

#### `def setUp(self)`

### `class FXPRegister15bitWord0bitIntegerOverflow(FXPRegisterSharedTests)`

#### `def setUp(self)`

### `class FXPRegister15bitWord0bitIntegerSignedOverflow(FXPRegisterSharedTests)`

#### `def setUp(self)`

### `class FXPRegister32bitWord16bitIntegerOverflow(FXPRegisterSharedTests)`

#### `def setUp(self)`

### `class FXPRegister16bitWord100bitInteger(FXPRegisterSharedTests)`

#### `def setUp(self)`

### `class FXPRegister16bitWordNegative100bitInteger(FXPRegisterSharedTests)`

#### `def setUp(self)`

### `class FXPRegister64bitWord64bitIntegerOverflow(FXPRegisterSharedTests)`

#### `def setUp(self)`

<!--NI_PYTHON_API repo=nifpga-python path=nifpga/tests/test_nifpga.py -->
## PYTHON MODULE: nifpga/tests/test_nifpga.py

### `def raise_an_exception()`


    A helper for NiFpgaStatusExceptionTest
    

### `class NiFpgaStatusExceptionTest(unittest.TestCase)`

#### `def test_autogenerated_status_warning_and_error_classes_exist(self)`

#### `def test_can_get_arguments_from_exception(self)`

#### `def test_status_exceptions_can_be_pickled_across_processes(self)`

### `def return_a_checked_status(code)`


    A helper for CheckStatusTest
    

### `def assert_warns(warning)`

### `class CheckStatusTest(unittest.TestCase)`

#### `def test_success(self)`

#### `def test_get_known_error(self)`

#### `def test_get_known_warning(self)`

#### `def test_get_unknown_error(self)`

#### `def test_get_unknown_warning(self)`

### `class StatusCheckedLibraryTestCRunTime(unittest.TestCase)`


    Since we can't load NiFpga on a dev machine unless we have all its
    dependencies installed (i.e. a bunch of NI software we don't want on
    a dev machine), we'll cheat and use the C runtime library and
    atoi. atoi doesn't really return a NiFpga_Status, but we can pretend.
    

#### `def setUp(self)`

#### `def test_success(self)`

#### `def test_get_unknown_error(self)`

#### `def test_get_unknown_warning(self)`

### `class StatusCheckedLibraryTestFunctionDoesntExist(unittest.TestCase)`


    New versions of NiFpga will have new functions.  We want the API to support
    old versions of NiFpga without erroring because it can't find certain symbols.
    So StatusCheckedLibrary will return VersionMismatchError for symbols it can't
    find.
    

#### `def setUp(self)`

#### `def test_correct_error(self)`

### `class StatusCheckedLibraryTestMockedLibrary(unittest.TestCase)`


    Since we can't load NiFpga on a dev machine unless we have all its
    dependencies installed (i.e. a bunch of NI software we don't want on
    a dev machine), we'll monkey patch and use mocked libraries.
    

#### `def shortDescription(self)`

#### `def setUp(self, mock_cdll, mock_find_library)`


        Setup up self._library so that self._library.AwesomeFunction(int, str)
        can be called, and the return value can be changed by setting
        self._mock_awesome_function.return_value.
        

#### `def test_good_error_message_from_memory_full_error(self)`

 Tests a good error message from a library call that fails.
        1. Correctly converts -52000 to NiFpgaMemoryFullError
        2. An integer arg gets printed as hex (easier to debug than decimal)
        3. A string arg gets printed with quotes surrounding it (so it's obviously a string)
        

#### `def test_success_when_library_function_is_success(self)`

 Tests that a 0 status return value does not raise any errors. 

#### `def test_good_error_message_if_wrong_number_of_arguments(self)`

 Tests that calling a function with wrong number of arguments is error 

### `class NiFpgaTest(unittest.TestCase)`

#### `def test_that_we_at_least_get_to_try_loading_library(self)`

<!--NI_PYTHON_API repo=nifpga-python path=setup.py -->
## PYTHON MODULE: setup.py

### `def get_version()`

### `def get_long_description()`
