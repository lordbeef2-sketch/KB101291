# NI PYTHON API DIGEST: nisemi-python

<!--NI_PYTHON_API_SNAPSHOT repo=ni/nisemi-python commit=0da9300d33d2348311fd9ccd785b207c926ab824 -->

<!--NI_PYTHON_API repo=nisemi-python path=examples/dut_communication_using_semi_device_control.py -->
## PYTHON MODULE: examples/dut_communication_using_semi_device_control.py

### MODULE DOCSTRING

Overview:.
 
Demonstrates how to use the Semi Device Control APIs to 
establish communication sequence with the DUT.

Requirement: Python full development system.
Instructions:
1. Run this python code.
2. View the read register value being printed in the terminal for each iteration


<!--NI_PYTHON_API repo=nisemi-python path=examples/dut_communication_using_semi_device_control_nidigital.py -->
## PYTHON MODULE: examples/dut_communication_using_semi_device_control_nidigital.py

### MODULE DOCSTRING

Overview:.

Demonstrates how to use the NI Digital Instance through
Semi Device Control APIs to establish communication sequence with the DUT.

Requirement: Python full development system.

Instructions:.
1. Run this python code.
2. View the read register value being printed in the terminal for each iteration.


<!--NI_PYTHON_API repo=nisemi-python path=examples/dut_communication_using_semi_device_control_scripts.py -->
## PYTHON MODULE: examples/dut_communication_using_semi_device_control_scripts.py

### MODULE DOCSTRING

Overview:.

Demonstrates how to use the Semi Device Control APIs to establish
communication sequence with the DUT using scripts.

Requirement: Python full development system.
Instructions:
1. Run this python code.
2. View the read register value being printed in the terminal for each iteration.


<!--NI_PYTHON_API repo=nisemi-python path=examples/dut_i3c_communication_using_semi_device_control.py -->
## PYTHON MODULE: examples/dut_i3c_communication_using_semi_device_control.py

### MODULE DOCSTRING

Overview:.

Demonstrates how to use the Semi Device Control APIs to establish
communication sequence with the DUT using I3C protocol.

Requirement: Python full development system.
Instructions:
1. Run this python code.
2. View the read register value being printed in the terminal for each iteration.


<!--NI_PYTHON_API repo=nisemi-python path=examples/generate_device_elements_using_semi_device_control.py -->
## PYTHON MODULE: examples/generate_device_elements_using_semi_device_control.py

### MODULE DOCSTRING

Overview:.

Demonstrates how to use the "generate_device_elements" API to generate
the class file that contains all the device elements.

Requirement: Python full development system.
Instructions:
1. Run this python code.
2. Use the python file generated to easily access the register and field names.


<!--NI_PYTHON_API repo=nisemi-python path=examples/nisdc_device_elements.py -->
## PYTHON MODULE: examples/nisdc_device_elements.py

### MODULE DOCSTRING

This file contains registers and field info.

### `class Register()`

This class contains all register info.

### `class Field()`

This class contains field info.

<!--NI_PYTHON_API repo=nisemi-python path=nisdc/__init__.py -->
## PYTHON MODULE: nisdc/__init__.py

### MODULE DOCSTRING

"This file is for init.

<!--NI_PYTHON_API repo=nisemi-python path=nisdc/nisemidevicecontrol.py -->
## PYTHON MODULE: nisdc/nisemidevicecontrol.py

### MODULE DOCSTRING

This file is used for Semi Device Control API.

### `def generate_class_string(element_type, device_element_list)`

This method generates the class string to be written to the auto generated file.

### `class GrpcSessionOptions()`

#### `def __init__(self, session_name, resource_name, grpc_channel)`

### `class SemiconductorDeviceControl()`

This class is used for Instrument Studio export configuration.

#### `def __init__(self, isconfigpath=None)`

Create and return device control session using Instrument Studio export configuration.

        IS export configuration contains the register map and hardware configuration
        for Device Control.

        Args:
            isconfigpath : the isconfig path. if not specified, the device control session will not be created.
        

#### `def attach_to_existing_session(self)`

Returns the instantiated device control session if any
        

#### `def start(self)`

Description:.

        Starts the Instrument/Hardware sessions configured for the device control
        through the IS export configuration.
        

#### `def stop(self)`

Stops the Instrument/Hardware sessions configured for the device control.

#### `def destroy(self)`

Destroys the device control session.

        Deallocates the reserved reference and data in memory.
        

#### `def write_register_by_name_device(self, register_uid, register_data)`

Writes the data to the device using the register unique name.

        Register UID: Unique name for the register in the format.

        <IP block/Device name>-<Register group>-<Register name>.

        Args:
            register_uid: string register uid
            register_data: int register data

        

#### `def write_multi_register_by_name_device(self, register_uid_list, register_data_list)`

Writes data to multiple registers on the device using the register unique name.

        Register UID: Unique name for the register in the format.

        <IP block/Device name>-<Register group>-<Register name>.

        For each Register UID element,the corresponding element from the data array will be applied.

        Args:
            register_uid_list: {list of string}
            register_data_list: {list of int}
        

#### `def write_register_by_address_device(self, ip_block_name, register_address, register_data)`

Writes the data to the device using the register address and IP block name.

        Register address: Address of the register from register map.

        IP block name: Name of the IP block or Device from register map.

        Args:
            ip_block_name: {string} ip black name
            register_address: {int} register address
            register_data: {int} register data
        

#### `def write_multi_register_by_address_device(self, ip_block_name_list, register_address_list, register_data_list)`

Write data to multiple registers on the device, using the register address.

        And IP block name.

        Register address: Address of the register from register map.

        IP block name: Name of the IP block or Device from register map.

        For each Register address & IP block element, the corresponding element
        from the data array will be applied.

        Args:
            ip_block_name_list: list of string
            register_address_list: list of int
            register_data_list: list of int
        

#### `def write_custom_register_by_address_device(self, register_address, address_size, register_data, register_size, interface_name, protocol_name)`

Writes the data using the register address and register size.

           To the device with the given interface and protocol.

        Register address: Address of the register.

        Address size: Size of the address.

        Size: Size of the register.

        Interface name: Name of the interface to use.

        Protocol name: Name of the protocol to use.

        Args:
            register_address: {int}
            address_size: {int}
            register_data: {int}
            register_size: {int}
            interface_name: {string}
            protocol_name: {string}
        

#### `def read_register_by_name_device(self, register_uid)`

Reads the data from the device using the register unique name.

        Register UID: Unique name for the register in the format.

        <IP block/Device name>-<Register group>-<Register name>.

        Args:
            register_uid : {string}

        Returns:
            register_data : {int}
        

#### `def read_multi_register_by_name_device(self, register_uid_list)`

Reads data from multiple registers on the device using the register unique name.

        Register UID: Unique name for the register in the format.

        <IP block/Device name>-<Register group>-<Register name>.

        For each Register UID element, the corresponding element from the data
        array will be applied.

        Args:
            register_uid_list : {list of string}

        Returns:
            register_data_list : {list of int}
        

#### `def read_register_by_address_device(self, ip_block_name, register_address)`

Reads the data from the device using the register address and IP block name.

        Register address: Address of the register from register map.

        IP block name: Name of the IP block or Device from register map.

        Args:
            ip_block_name : {string}
            register_address : {int}

        Returns:
            register_data : {int}
        

#### `def read_multi_register_by_address_device(self, ip_block_name_list, register_address_list)`

Reads data from multiple registers on the device.

        Using the register address and IP block name.

        Register address: Address of the register from register map.

        IP block name: Name of the IP block or Device from register map.

        For each Register address & IP block element, the corresponding.

        Element from the data array will be applied.

        Args:
            ip_block_name_list : {list of string}
            register_address_list : {list of int}

        Returns:
            register_data_list : {list of int}
        

#### `def read_custom_register_by_address_device(self, register_address, address_size, register_size, interface_name, protocol_name)`

Reads the data using the register address and register size from the device.

        With the given interface and protocol.

        Register address: Address of the register.

        Address size: Size of the address.

        Size: Size of the register.

        Interface name: Name of the interface to use.

        Protocol name: Name of the protocol to use.

        Arguments:
            register_address: {int}
            address_size: {int}
            register_size: {int}
            interface_name: {string}
            protocol_name: {string}

        Returns:
            register_data: {int}
        

#### `def get_register_addresses(self)`

Gets the list of unique ID and Register addresses.

        Returns:
            register_uid_list: {list of string}
            register_address_list: {list of int
        

#### `def write_field_by_name_device(self, field_uid, field_data)`

Writes the data to the device using the field unique name.

        Field UID: Unique name for the field in the format.

        <IP block/Device name>-<Register group>-<Field name>.

        Args:
            field_uid: {string}
            field_data :{int}
        

#### `def write_multi_field_by_name_device(self, field_uid_list, field_data_list)`

Writes data to multiple fields on the device using the field unique name.

        Field UID: Unique name for the field in the format.

        <IP block/Device name>-<Register group>-<Field name>.

        For each Field UID element, the corresponding element from the data.

        Array will be applied.

        Args:
            field_uid_list: {list of string}
            field_data_list: {list of int}
        

#### `def write_field_by_value_definition_device(self, field_uid, value_definition)`

Write the data to the device using the field unique name.

        And field value definition.

        Field UID: Unique name for the field in the format.

        <IP block/Device name>-<Register group>-<Field name>.

        Value Definition: This is defined in the register map for each field.

        Each value of the field can contain a definition string.

        That represents the value.

        Args:
            field_uid: {string}
            value_definition: {string}
        

#### `def read_field_by_name_device(self, field_uid)`

Reads the data from the device using the field unique name.

        Field UID: Unique name for the field in the format.

        <IP block/Device name>-<Register group>-<Field name>.

        Args:
            field_uid: {string}

        Returns:
            field_data: {int}
        

#### `def read_multi_field_by_name_device(self, field_uid_list)`

Reads data from multiple fields on the device using the field unique name.

        Field UID: Unique name for the field in the format.

        <IP block/Device name>-<Register group>-<Field name>.

        For each Field UID element, the corresponding element from the data
        array will be applied.

        Arguments:
            field_uid_list: {list of string}

        Returns:
            field_data_list: {list of int}
        

#### `def get_field_definition_details(self, field_uid)`

Gets the field display values, field values and field size for given unique ID.

        Arguments:
            field_uid: {string}

        Returns:
            field_display_values {list of string}
            field_values {list of int}
            field_size {int}
        

#### `def write_register_by_name_cache(self, register_uid, register_data)`

Writes the data to the cache using the register unique name.

        Register UID: Unique name for the register in the format.

        <IP block/Device name>-<Register group>-<Register name>.

        Args:
            register_uid: {string}
            register_data: {int}
        

#### `def write_multi_register_by_name_cache(self, register_uid_list, register_data_list)`

Writes data to multiple registers on the cache using the register unique name.

        Register UID: Unique name for the register in the format.

        <IP block/Device name>-<Register group>-<Register name>.

        For each Register UID element, the corresponding element from the data.

        Array will be applied.

        Arguments:
            register_uid_list: {list of string}
            register_data_list: {list of int}
        

#### `def write_register_by_address_cache(self, ip_block_name, register_address, register_data)`

Writes the data to the cache using the register address and IP block name.

        Register address: Address of the register from register map.

        IP block name: Name of the IP block or Device from register map.

        Arguments:
            ip_block_name: {string}
            register_address: {int}
            register_data: {int}
        

#### `def write_multi_register_by_address_cache(self, ip_block_name_list, register_address_list, register_data_list)`

Writes data to multiple registers on the cache.

        Using the register, address and IP block name.

        Register address: Address of the register from register map.

        IP block name: Name of the IP block or Device from register map.

        For each Register address & IP block element, the corresponding.

        Element from the data array will be applied.

        Arguments:
            ip_block_name_list: {list of string}
            register_address_list: {list of int}
            register_data_list: {list of int}
        

#### `def read_register_by_name_cache(self, register_uid)`

Reads the data from the cache using the register unique name.

        Register UID: Unique name for the register in the format.

        <IP block/Device name>-<Register group>-<Register name>.

        Args:
            register_uid: {string}

        Returns:
            register_data :{int}
        

#### `def read_multi_register_by_name_cache(self, register_uid_list)`

Reads data from multiple registers on the cache using the register unique name.

        Register UID: Unique name for the register in the format.

        <IP block/Device name>-<Register group>-<Register name>.

        For each Register UID element, the corresponding element from the data.
        array will be applied.

        Arguments:
            register_uid_list: {list of string}

        Returns:
            register_data_list: {list of int}
        

#### `def read_register_by_address_cache(self, ip_block_name, register_address)`

Reads the data from the cache using the register address and IP block name.

        Register address: Address of the register from register map.

        IP block name: Name of the IP block or Device from register map.

        Args:
            ip_block_name: {string}
            register_address: {int}

        Returns:
            register_data :{int}
        

#### `def read_multi_register_by_address_cache(self, ip_block_name_list, register_address_list)`

Reads data from multiple registers on the cache.

        Using the register address and IP block name.

        Register address: Address of the register from register map.

        IP block name: Name of the IP block or Device from register map.

        For each Register address & IP block element, the corresponding.

        Element from the data array will be applied.

        Args:
            ip_block_name_list: {list of string}
            register_address_list: {list of int}

        Returns:
            register_data_list: {list of int}
        

#### `def write_field_by_name_cache(self, field_uid, field_data)`

Writes the data to the cache using the field unique name.

        Field UID: Unique name for the field in the format.

        <IP block/Device name>-<Register group>-<Field name>.

        Args:
            field_uid: {string}
            field_data: {int}
        

#### `def write_multi_field_by_name_cache(self, field_uid_list, field_data_list)`

Writes data to multiple fields on the cache using the fields unique name.

        Field UID: Unique name for the field in the format.

        <IP block/Device name>-<Register group>-<Field name>.

        For each Field UID element, the corresponding element from the data.

        Array will be applied.

        Args:
            field_uid_list: {list of string}
            field_data_list: {list of int}
        

#### `def write_field_by_value_definition_cache(self, field_uid, value_definition)`

Writes the data to the cache using the field unique name.

        And field value definition.

        Field UID: Unique name for the field in the format.

        <IP block/Device name>-<Register group>-<Field name>.

        Value Definition: This is defined in the register map for each field.

        Each value of the field can contain a definition string.

        That represents the value.

        Args:
            field_uid: {string}
            value_definition: {string}
        

#### `def read_field_by_name_cache(self, field_uid)`

Read the data from the cache using the field unique name.

        Field UID: Unique name for the field in the format.

        <IP block/Device name>-<Register group>-<Field name>.

        Args:
            field_uid: {string}

        Returns:
            field_data: {int}
        

#### `def read_multi_field_by_name_cache(self, field_uid_list)`

Reads data from multiple fields on the cache using the field unique name.

        Field UID: Unique name for the field in the format.

        <IP block/Device name>-<Register group>-<Field name>.

        For each Field UID element, the corresponding element from the data.

        Array will be applied.

        Args:
            field_uid_list: {list of string}

        Returns:
            field_data_list: {list of int}
        

#### `def write_from_cache_to_device(self)`

Writes all the cache register data to the device, in the order.

        It is stored in the cache memory. The cache will be auto cleared.

        After this operation.
        

#### `def clear_cache(self)`

Clears all the cache register data from the device control session.

#### `def read_pin_state(self, pin_name)`

Reads the pin state (High / Low / Terminate) using the Pin name.

        Defined in the register map.

        Pin State corresponding int values.2-Terminate, 1=High, 0-Low.

        Args:
            pin_name: {string}

        Return:
            pin_state: {int}
        

#### `def write_pin_state(self, pin_name, pin_state)`

Puts the pin to High / Low / Terminate state using the Pin name.

        defined in the register map.

        Args:
            pin_name: {string}
            pin_state: {int}

            Pin State corresponding int values.

            2-Terminate, 1=High, 0-Low.
        

#### `def execute_script(self, file_name, wait_until_complete=True)`

Executes the script using the Script Name provided as a input.

        If a script is already running on the semi device control session.

        This API will throw error indicating that another script is running already.

        Using waitUntilScriptCompletion bool control, developer can configure.

        This API to run the script as a blocking call or run asynchronously.

        Args:
            file_name: {string}
            wait_until_complete: {bool}

        Returns:
            Array of string, each  string is the result of the command.

            Executed from the script in JSON format {list of string}
        

#### `def execute_script_command(self, script_string, wait_until_complete=True)`

Executes the Script String provided as the input to the API.

        If the Script String is invalid, error will be thrown, and execution will be skipped.
        If waitUntilComplete? is True, then the API will wait until the script is executed.
        Else the API will run the script asynchronously and stop.

        Args:
            script_string :{string}
            wait_until_complete: {bool}

        Returns:
            Array of string, each  string is the result of the command.

            Executed from the script in JSON format {list of string}.
        

#### `def abort_script(self)`

Abort Script will abort the current running script on the semi device control session.

#### `def get_logs(self)`

Get log details.

        Returns:
            logs {2d array of strings}
        

#### `def reset_to_default_state(self)`

Reset the device software register values and dio states to default.

#### `def get_script_names(self)`

Gets the list of script file names available in the source folder location.

        Return:
            script_names {list of strings}
        

#### `def get_protocol_dynamic_setting(self, interface_name, protocol_name, setting_name)`

Gets the dynamic protocol setting value of the protocol setting.

        Args:
            interface_name: {string}
            protocol_name: {string}
            setting_name: {string}

        Return:
            setting_value {string}
        

#### `def set_protocol_dynamic_setting(self, interface_name, protocol_name, setting_name, setting_value)`

Updates the dynamic protocol settings of the protocol.

        Args:
            interface_name: {string}
            protocol_name: {string}
            setting_name: {string}
            setting_value: {string}
        

#### `def get_interface_dynamic_setting(self, interface_name, setting_name)`

Gets the dynamic interface setting value of the interface setting.

        Args:
            interface_name: {string}
            setting_name: {string}

        Return:
            setting_value: {string}
        

#### `def set_interface_dynamic_setting(self, interface_name, setting_name, setting_value)`

Updates the dynamic interface setting value of the interface setting.

        Args:
            interface_name: {string}
            setting_name: {string}
            setting_value: {string}
        

#### `def get_instrument_session(self, interface_name)`

Gets the session ID of the instrument.

        Return:
            int {session ID}
        

#### `def get_session_options(self, interface_name)`

Gets the grpc options for the instrument session.
           Creates service server channel using the grpc options.

            Return:
                grpc_session_options {Object contains the session_name {string} and device_server_channel {grpc.Channel}}
        

#### `def get_interface_details(self)`

Gets the list of interface name and interface type.

        Return:
            interface_name_list {list of string}
            interface_type_list {list of string}
        

#### `def get_script_string(self, script_name)`

API provides the Script String and IsScriptFileValid status from Device Control session.

        For the given the Script Name input.

        Args:
            script_name: {string}

        Return:
            Tuple { bool - IsScriptValid, string - ScriptContent}
        

#### `def generate_device_elements(self, directory='')`

This API generates a class file in the specified directory.

        That contains the register and field elements from the register map
        configured in the sdcconfig file.
        If the directory provided is empty, the file will be created in the working directory.

        Args:
            directory: {string}

        Return:
            string - The path where the file is created
        

<!--NI_PYTHON_API repo=nisemi-python path=nisdc_i3c/__init__.py -->
## PYTHON MODULE: nisdc_i3c/__init__.py

### MODULE DOCSTRING

This is __init__.py file.

<!--NI_PYTHON_API repo=nisemi-python path=nisdc_i3c/nisdc_i3c.py -->
## PYTHON MODULE: nisdc_i3c/nisdc_i3c.py

### MODULE DOCSTRING

This file is used for Semi Device Control I3C API.

### `class SemiDeviceControlI3CSession()`

"This class is used to create I3C session.

#### `def __init__(self, semidevicecontrol_session, interface_name, protocol_name)`

Creates and returns a I3C session using the Semi Device Control session.

        Args:
            semidevicecontrol_session: {Semi Device Control session object}
            interface_name: {string}
            protocol_name: {string}
        

#### `def execute_dynamic_addressing_ccc(self, ccc_type, command_id, dynamic_address=-1)`

Executes the CCC used for dynamic addressing based on the given inputs.
        
        If for a given Command ID the dynamic address is not applicable then it will not be applied
        and if the Command ID doesn’t match with the CCC Type
        and CCC Operation an exception will be thrown.
        
        CCC Type corresponding int values.1=Direct,0-Broadcast.

        Args:
            ccc_type: { int }
            command_id: {int}
            dynamic_address: {int}
        

#### `def execute_dynamic_addressing_ccc_with_read(self, ccc_type, command_id, dynamic_address=-1)`

Executes the CCC used for dynamic addressing based on the given inputs.
        
        And returns the data read back from the DUT.
        This API is only applicable for the ENTDAA in the current spec.
        If for a given Command ID the dynamic address is not applicable then it will not be applied
        and if the Command ID doesn’t match with the CCC Type
        and CCC Operation an exception will be thrown.
        
        CCC Type corresponding int values. 1=Direct, 0-Broadcast.

        Args:
            ccc_type: { int }
            command_id: {int}
            dynamic_address: {int}

        Return:
            read_data {list of int}
        

#### `def execute_sdr_ccc_write(self, ccc_type, command_id, defining_byte=-1, write_data=None)`

Executes the write CCC commands used in SDR mode based on the given inputs.
        
        If for a given Command ID the defining byte
        and data are not applicable then they will be ignored.
        If the Command ID doesn’t match with the CCC Type
        and CCC Operation an exception will be thrown.
        
        CCC Type corresponding int values. 1=Direct, 0-Broadcast.

        Arguments:
            ccc_type: { int }
            command_id: {int}
            defining_byte: {int}
            write_data: {list of int}
        

#### `def execute_sdr_ccc_read(self, ccc_type, command_id, defining_byte=-1, read_byte_length=-1)`

Executes the read CCC commands used in SDR mode based on the given inputs.
        
        And returns the read data.
        If for a given Command ID the Defining Byte is not applicable then they will be ignored.
        The  read Data Length will only be considered if the value is not provided in the csv file
        else it will take the value from the csv file.
        and if the Command ID doesn’t match with the CCC Type
        and CCC Operation an exception will be thrown.
        
        CCC Type corresponding int values. 1=Direct, 0-Broadcast.

        Arguments:
            ccc_type: { int }
            command_id: {int}
            defining_byte: {int}
            read_byte_length: {int}

        Returns:
            read_data {list of int}
        
