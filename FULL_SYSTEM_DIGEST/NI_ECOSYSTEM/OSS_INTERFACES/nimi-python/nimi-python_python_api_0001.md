# NI PYTHON API DIGEST: nimi-python

<!--NI_PYTHON_API_SNAPSHOT repo=ni/nimi-python commit=6511f8025f072f7f7021953888b916bbdc31aa2a -->

<!--NI_PYTHON_API repo=nimi-python path=build/__init__.py -->
## PYTHON MODULE: build/__init__.py

### `def add_to_path(p)`

<!--NI_PYTHON_API repo=nimi-python path=build/generate_template.py -->
## PYTHON MODULE: build/generate_template.py

### `def generate_template(template_name, template_params, dest_file, in_zip_file=False)`

<!--NI_PYTHON_API repo=nimi-python path=build/helper/codegen_helper.py -->
## PYTHON MODULE: build/helper/codegen_helper.py

### `def get_params_snippet(function, parameter_usage_options)`

get_params_snippet

    Get a parameter list snippet based on parameter_usage_options.
    

### `def _get_interpreter_output_param_return_type(output_parameter, config)`

### `def _get_library_interpreter_output_param_return_snippet(output_parameter, parameters, config)`

Returns the snippet for returning a single output parameter from a LibraryInterpreter method, i.e. "reading_ctype.value"

### `def _get_grpc_interpreter_output_param_return_snippet(output_parameter, parameters, config)`

### `def _get_session_output_param_return_snippet(output_parameter, parameters, config)`

Returns the snippet for returning a single output parameter from a Session method

### `def get_library_interpreter_method_return_snippet(parameters, config, use_numpy_array=False)`

Returns a string suitable to use as the return argument of a LibraryInterpreter method, i.e. "return reading_ctype.value"

### `def get_grpc_interpreter_method_return_snippet(parameters, config)`

Returns a string suitable to use as the return argument of a _gprc.LibraryInterpreter method

### `def get_session_method_return_snippet(parameters, config, use_numpy_array=False)`

Returns a string suitable to use as the return argument of a Session method

### `def get_enum_type_check_snippet(parameter, indent)`

Returns python snippet to check that the type of a parameter is what is expected

### `def _get_buffer_parameters_for_size_parameter(parameter, parameters)`

Return all parameters that use this parameter for size. Empty list if none

### `class IviDanceStep(Enum)`

### `def get_ctype_variable_declaration_snippet(parameter, parameters, ivi_dance_step, config, use_numpy_array=False)`

Returns array of python snippets that declares and initializes a ctypes variable for the parameter that can be passed to the Library.

    Logic for creating the appropriate snippet is split up in two helper functions. One for scalars and one for buffers.
    

### `def _get_ctype_variable_definition_snippet_for_string(parameter, parameters, ivi_dance_step, module_name)`

These are the different cases for initializing the ctype variables for strings

    C010. Input repeated capability:                                           ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))
    C020. Input string:                                                        ctypes.create_string_buffer(parameter_name.encode(self._encoding))
    C030. Input string enum:                                                   ctypes.create_string_buffer(parameter_name.value.encode(self._encoding))
    C050. Output buffer with mechanism ivi-dance, QUERY_SIZE:                  None
    C060. Output buffer with mechanism ivi-dance, GET_DATA:                    (visatype.ViChar * buffer_size_ctype.value)()
    C070. Output buffer with mechanism fixed-size:                             visatype.ViChar * 256
    C080. Output buffer with mechanism python-code:                            visatype.ViChar * <python_code>
    C090. Output buffer with mechanism ivi-dance-with-a-twist, QUERY_SIZE:     None
    C100. Output buffer with mechanism ivi-dance-with-a-twist, GET_DATA:       (visatype.ViChar * buffer_size_ctype.value)()
    

### `def _get_ctype_variable_definition_snippet_for_scalar(parameter, parameters, ivi_dance_step, module_name, config)`

These are the different cases for initializing the ctype variable for scalars:

        S110. Input session handle:                                                visatype.ViSession(self._vi)
        S120. Input is size of buffer with mechanism is python-code:               visatype.ViInt32(<custom python code>)
        S130. Input enum:                                                          visatype.ViInt32(parameter_name.value)
        S150. Input scalar:                                                        visatype.ViInt32(parameter_name)
        S160. Input is size of 1-dimensional input buffer:                         visatype.ViInt32(0 if list is None else len(list))
        S161. Input is total number of elements in multidimensional input buffer:  visatype.ViInt32(0 if array is None else array.size)
        S170. Input is size of output buffer with mechanism ivi-dance, QUERY_SIZE: visatype.ViInt32()
        S180. Input is size of output buffer with mechanism ivi-dance, GET_DATA:   visatype.ViInt32(error_code)
        S190. Input is size of output buffer with mechanism ivi-dance-with-a-twist, QUERY_SIZE: visatype.ViInt32()
        S200. Input is size of output buffer with mechanism ivi-dance-with-a-twist, GET_DATA:   visatype.ViInt32(error_code)
        S210. Input is size of output buffer with mechanism passed-in:             visatype.ViInt32(buffer_size)
        S220. Output scalar or enum:                                               visatype.ViInt32()

    Return Value (list): each item in the list will be one line needed for the declaration of that parameter
    

### `def _get_ctype_variable_definition_snippet_for_buffers(parameter, parameters, ivi_dance_step, use_numpy_array, custom_type, module_name)`

These are the different cases for initializing the ctype variable for buffers:

        B510. Input/output numpy array:                                            _get_ctypes_pointer_for_buffer(value=waveform)
        B540. Input buffer (custom type):                                          _get_ctypes_pointer_for_buffer(value=[custom_struct(l) for l in list], library_type=custom_struct)
        B550. Input buffer of simple types:                                        _get_ctypes_pointer_for_buffer(value=array.array('d', list), library_type=visatype.ViReal64)
        B560. Output buffer with mechanism python-code:                            _get_ctypes_pointer_for_buffer(value=array.array('d'), library_type=ViInt32)
        B570. Output buffer with mechanism fixed-size:                             _get_ctypes_pointer_for_buffer(library_type=ViInt32, size=256)
        B580. Output buffer with mechanism ivi-dance, QUERY_SIZE:                  None
        B590. Output buffer with mechanism ivi-dance, GET_DATA:                    _get_ctypes_pointer_for_buffer(value=array.array('d', [0]) * buffer_size_ctype.value, library_type=ViInt32)
        B600. Output buffer with mechanism passed-in:                              _get_ctypes_pointer_for_buffer(value-array.array('d', [0]) * buffer_size, library_type=ViInt32)
        B610. Output buffer with mechanism ivi-dance-with-a-twist, QUERY_SIZE:     None
        B620. Output buffer with mechanism ivi-dance-with-a-twist, GET_DATA:       _get_ctypes_pointer_for_buffer(value=array.array('d', [0]) * buffer_size_ctype.value, library_type=ViInt32)

    Return Value (list): each item in the list will be one line needed for the declaration of that parameter

    All versions that have array.array have an alternate format for lists
    

### `def get_parameter_size_check_snippets(parameters)`

Returns python snippets to check that parameter sizes are correct.

### `def _get_parameter_size_check_snippets(parameter, parameters)`

### `def get_dictionary_snippet(d, indent=4)`

Returns a formatted dictionary

### `def get_enum_value_snippet(value)`

Returns value formatted into string, surrounding it with single quotes if it is of str type

<!--NI_PYTHON_API repo=nimi-python path=build/helper/documentation_helper.py -->
## PYTHON MODULE: build/helper/documentation_helper.py

### `def get_indented_docstring_snippet(d, indent=4)`

Returns a docstring with the correct amount of indentation.

    First line is not indented.

    Can't use similar construct as get_dictionary_snippet
    ('
' + (' ' * indent)).join(d_lines) because empty lines would get
    the spaces, which violates pep8 and causes the flake8 step to fail

    Args:
        docstring (str): multiline string to format
        indent (int): How much to indent lines 2+

    Returns:
        str: formatted string
    

### `def get_rst_header_snippet(t, header_level='=')`

Get rst formatted heading

### `def get_rst_picture_reference(tag, url, title, link, indent=0)`

Get rst formatted snippet that represents a picture

### `def _get_rst_table_snippet(node, d, config, indent=0, make_link=True)`

Returns an rst table snippet if table_header and/or table_body are in the dictionary

### `def get_rst_admonition_snippet(node, admonition, d, config, indent=0)`

Returns a rst formatted admonition if the given admonition ('note', 'caution') exists in the dictionary

### `def add_attribute_rep_cap_tip(attr, config)`

Add the appropriate docstring formatted repeated capability tip for an attribute

### `def get_documentation_for_node_rst(node, config, indent=0)`

Returns any documentation information formatted for rst

    Documentation will be in the following order (if existing)
    - 'caution' admonition
    - 'description'
    - table made of 'table_header' and 'table_body'
    - 'note' admonition

    Args:
        node (dict) - Node possibly containing documentation
        config (dict) - build configuration
        indent (int) - how much each line should be indented

    Returns:
        str - formatted documentation, empty string if none
    

### `def get_docstring_admonition_snippet(node, admonition, d, config, indent=0, extra_newline='\n')`

Returns a docstring formatted admonition if the given admonition ('note', 'caution') exists in the dictionary

    Args:
        admonition (str) - admonition to check and format. I.e. 'note', 'tip', etc.
        d (dict) - documentation note dictionary
        config (dict) - build configuration
        indent (int) - how much each line should be indented
        extra_newline (str) - empty string or newline - needed to keep docstring formatting correct

    Returns:
        str - empty string if no admonition, else formatted string with one or more admonitions
    

### `def get_documentation_for_node_docstring(node, config, indent=0)`

Returns any documentation information formatted for docstring

    Documentation will be in the following order (if existing)
    - 'caution' admonition
    - 'description'
    - table made of 'table_header' and 'table_body'
    - 'note' admonition
    - 'tip' admonition

    Args:
        node (dict) - Node possibly containing documentation
        config (dict) - build configuration
        indent (int) - how much each line should be indented

    Returns:
        str - formatted documentation, empty string if none
    

### `def find_enum_by_value(enums, value, start_enum=None)`

Returns the enum that contains the given value if there is one

    There should only be one so return that individual parameter and not a list
    

### `def _replace_enum_python_name(e_match)`

callback function for enum value regex sub command

    Args:
        m (match object): Match object from the attribute substitution command

    Returns:
        str: python name of the enum value, possibly set to sphinx python domain data item link
    

### `def find_attribute_by_name(attributes, name)`

Returns the attribute with the given name if there is one

    There should only be one so return that individual parameter and not a list
    

### `def _replace_attribute_python_name(a_match)`

callback function for attribute regex sub command

    Args:
        m (match object): Match object from the attribute substitution command

    Returns:
        str: python name of the attribute, possibly set to sphinx python domain data item link
    

### `def _replace_func_python_name(f_match)`

callback function for function regex sub command

    Args:
        f_match (match object): Match object from the function substitution command

    Returns:
        str: rst link to function using python name, possibly set to sphinx python domain meth item link
    

### `def _replace_urls(u_match)`

callback function for regex when url link needed

    Args:
        u_match (match object): Match object from the function substitution command

    Returns:
        str: replacement url
    

### `def _fix_references(node, doc, cfg, make_link=False)`

Replace ATTR and function mentions in documentation

    Args:
        doc (str): documentation string to be updated
        config (dict): config dictionary from metadata
        make_link (bool): Default False
            True - references are replaced with a rst style link
            False - references are replaced with just the python name

    Returns:
        str: documentation with references replaces based on make_link
    

### `def format_type_for_rst_documentation(param, numpy, config)`

### `def get_function_rst(function, method_template, numpy, config, indent=0, method_or_function='method')`

Gets formatted documentation for given function or method that can be used in rst documentation

    Args:
        function (dict): function dictionary
        config (dict): configuration dictoionary (from metadata)
        method_template (dict): entry from function['methos_temlates'] that corresponds to specific entry we are processon
        numpy (boolean): Is the entry we are processing a numpy based method
        indent (int): default 0 - initial indentation

    Returns:
        str: rst formatted documentation
    

### `def _format_type_for_docstring(param, numpy, config)`

### `def get_function_docstring(function, numpy, config, indent=0)`

Gets formatted documentation for given function that can be used as a docstring

    Args:
        function (dict): function dictionary
        config (dict): configuration dictionary (from metadata)
        numpy (boolean): Is the entry we are processing a numpy based method
        indent (int): default 0 - initial indentation

    Returns:
        str: docstring formatted documentation
    

### `def as_rest_table(data, header=True)`

Create rst formatted table

    >>> data = [('what', 'how', 'who'),
    ...         ('lorem', 'that is a long value', 3.1415),
    ...         ('ipsum', 89798, 0.2)]
    >>> print(as_rest_table(data))
    +-------+----------------------+--------+
    | what  | how                  | who    |
    +=======+======================+========+
    | lorem | that is a long value | 3.1415 |
    +-------+----------------------+--------+
    | ipsum |                89798 |    0.2 |
    +-------+----------------------+--------+
    >>> print(as_rest_table(data, header=False))
    +-------+----------------------+--------+
    | what  | how                  | who    |
    +-------+----------------------+--------+
    | lorem | that is a long value | 3.1415 |
    +-------+----------------------+--------+
    | ipsum |                89798 |    0.2 |
    +-------+----------------------+--------+
    

### `def _square_up_table(nd)`

_square_up_table

    The function we use to generate rst tables requires the table be a rectangle. I.e. all
    rows must have the same number of cells. This will check 'table_header' and 'table_body'
    to get the longest row and then make sure they are all that length
    

### `def square_up_tables(config)`

Go through all documentation and make sure tables rows have consistent lengths

### `def _need_func_note(nd, config)`

Determine if we need the extra note about function names not matching anything in Python

### `def _need_attr_note(nd, config)`

Determine if we need the extra note about attribute names not matching anything in Python

### `def _need_enum_note(nd, config, start_enum=None)`

Determine if we need the extra note about enum names not matching anything in Python

### `def _check_documentation(nd, config, start_enum=None)`

_check_documentation

    Look through all the different documentation pieces for this node documentation object for
    any references to functions, attributes or enums that will not exist in the Python API for
    whatever reason. If we find something, we will add a note admonition stating that.

    Args:
        nd (dict) - documentation dictionary - expected to follow standard layout we have been using
        config (dict) - configuration information'
        start_enum (book) - possible context - used for finding enums based on the value
    

### `def add_notes_re_links(config)`

_add_notes_re_links

    Go through all documentation looking for names that won't exist in the Python API and
    adding a note about it.
    

### `def get_attribute_repeated_caps(attr)`

Creates a comma-separated string representing the attribute's repeated capabilities. Returns 'None' if there are no repeated capabilities

### `def get_attribute_repeated_caps_with_conjunction(attr)`

Creates a comma-separated string, with terminating 'and', representing the attribute's repeated capabilities. Returns 'None' if there are no repeated capabilities

### `def module_supports_repeated_caps(config)`

<!--NI_PYTHON_API repo=nimi-python path=build/helper/documentation_snippets.py -->
## PYTHON MODULE: build/helper/documentation_snippets.py

### `def close_function_def_for_doc(functions, config)`

### `def initiate_function_def_for_doc(functions, config)`

<!--NI_PYTHON_API repo=nimi-python path=build/helper/helper.py -->
## PYTHON MODULE: build/helper/helper.py

### `def shoutcase_to_camelcase(shout_string)`

Converts a C-style SHOUT_CASE string to camelCase

### `def camelcase_to_snakecase(camelcase_string)`

Converts a camelCase string to lower_case_snake_case

### `def function_to_method_name(f)`

Returns an appropriate session method name for a given function

### `def sorted_attrs(a)`

### `def get_python_type_for_api_type(api_type, config)`

Returns the type to use in the Python API from the original visa or custom type used in the C API

    Do not use this with enums.
    

### `def get_numpy_type_for_api_type(api_type, config)`

Returns the numpy type to use in the Python API from the original visa or custom type used in the C API

    Do not use this with enums.
    

### `def get_array_type_for_api_type(api_type)`

Returns the array type to use in the Python API from the original visa or custom type used in the C API

    Do not use this with enums.
    

### `def get_development_status(config)`

Get the PyPI Development Status, based on module version

    module_version must be PEP 440 conformant
    See https://packaging.pypa.io/en/latest/version/ and https://www.python.org/dev/peps/pep-0440/
    Arbitrary rules:
    version < 0.5 - alpha
    version >= 0.5 && version < 1.0 - beta
    version >= 1.0
       .devN or .aN - Alpha
       .bN, cN, rcN - Beta
       <nothing> or postN - Stable
    

### `def enum_uses_converter(enum)`

Returns True if enum uses converter, False otherwise.

    An enum uses converter if it has both 'enum_to_converted_value_function_name' and
    'converted_value_to_enum_function_name' defined which are not None. If one of them is defined
    and not None but not the other, an AssertionError would be thrown.
    

<!--NI_PYTHON_API repo=nimi-python path=build/helper/metadata_add_all.py -->
## PYTHON MODULE: build/helper/metadata_add_all.py

### `def _add_name(n, name)`

Adds a name' key/value pair to the function metadata

### `def _add_codegen_method(n)`

Add 'codegen_method' as public if it isn't already there

### `def _add_enum(n)`

Add 'enum' as None if it isn't already there

### `def _add_grpc_enum(n)`

Add 'grpc_enum' if it isn't already there

### `def _add_python_method_name(function, name)`

Adds 'python_name' to the function metadata if not already there

### `def _add_interpreter_method_name(function, name)`

Adds 'interpreter_name' to the function metadata if not already there

### `def _add_python_parameter_name(parameter)`

Adds a python_name key/value pair to the parameter metadata

### `def _add_grpc_parameter_name(parameter)`

Adds a grpc_name key/value pair to the parameter metadata

### `def _add_python_type(item, config)`

Adds the type to use in the Python API and the documentation to the item metadata, if not already there

### `def _add_ctypes_variable_name(parameter)`

Adds a ctypes_variable_name key/value pair to the parameter metadata for a corresponding ctypes variable

### `def _add_ctypes_type(parameter, config)`

Adds a ctypes_type key/value pair to the parameter metadata for calling into the library

### `def _add_complex_array_representation(parameter)`

Adds a complex_array_representation parameter to the metadata for complex numbers

### `def _add_array_dimensions(parameter)`

Adds a array_dimensions parameter to the metadata for multi dimensional arrays

### `def _add_numpy_info(parameter, parameters, config)`

Adds the following numpy-related information:

             numpy: Default to False unless already set. True for buffers that allow being passed as a numpy.ndarray.
        numpy_type: The name of the element type to use in the numpy.ndarray.
    

### `def _add_is_error_handling(f)`

Adds is_error_handling information to the function metadata if it isn't already defined. Defaults to False.

### `def _add_buffer_info(parameter, config)`

Adds buffer information to the parameter metadata

    These are the pieces of information that will be added to metadata:
        'is_string' - Used for any string type - see below for complete list
        'use_list'  - Used for an array of custom types. We are not putting custom types into array.array or numpy.array
        'use_array' - Used for arrays of simple types
        'is_buffer' - True when either 'use_list' or 'use_array' is True
        'size'      - set to default value of {'mechanism': 'fixed', 'value': 1} if it doesn't already exist
    

### `def _add_ctypes_method_call_snippet(parameter)`

Code snippet for calling a ctypes method for this parameter.

### `def _add_interpreter_method_call_snippet(parameter, config)`

Code snippet for calling a method of Library for this parameter.

### `def _add_grpc_request_snippet(parameter, config)`

### `def _add_default_value_name(parameter)`

Declaration with default value, if set

### `def _add_default_value_name_for_docs(parameter, module_name)`

Declaration with default value, if set

### `def _add_method_templates(f)`

Adds a list of 'method_template_filenames' value to function metadata if not found. This are the mako templates that will be used to render the method.

### `def _add_has_repeated_capability(f)`

Adds a boolean 'has_repeated_capability' to the function metadata by inferring it from its parameter names, if not previously populated.

### `def _add_render_in_session_base(f)`

Adds a boolean 'render_in_session_base' to the function metadata if not previously populated.

    This tells the code generator to render those methods in _SessionBase class and not Session.
    By default, we want all functions that have repeated capability input and all error handling related functions in _SessionBase but there are exceptions to this rule.
    

### `def _add_is_repeated_capability(parameter)`

Adds a boolean 'is_repeated_capability' to the parameter metadata by inferring it from its name, if not previously populated.

### `def _add_use_session_lock(f)`

Set 'use_session_lock' to True unless it already exists

    Only nimodinst doesn't have session locking and the modinst session.py.mako doesn't even look at this
    

### `def _add_is_session_handle(parameter)`

Adds a boolean 'is_session_handle' to the parameter metadata by inferring it from its type, if not previously populated.

### `def _fix_type(parameter)`

Replace any spaces in the parameter type with an underscore.

### `def _fix_custom_type(parameter, config)`

Add "struct_" prefix to custom type if necessary to match its ctypes_type.

### `def _add_use_in_python_api(p, parameters)`

Add 'use_in_python_api' if not there with value of True

### `def _setup_init_function(functions, config)`

Copy the selected init function to a known name and update information about it for documentation purposes

### `def add_all_function_metadata(functions, config)`

Merges and Adds all codegen-specific metada to the function metadata list

### `def _add_python_name(a, attributes)`

Adds 'python_name' - lower case + leading '_' if first character is a digit

### `def _add_default_attribute_class(a, attributes)`

Set 'attribute_class' if not set.

    By default, the 'attribute_class' is only based on the 'type'.
    It can be set in attributes_addon if we want to convert to/from a different datatype, such as hightime.timedelta
    

### `def add_all_attribute_metadata(attributes, config)`

Merges and Adds all codegen-specific metada to the function metadata list

### `def _add_enum_codegen_method(enums, config)`

Adds 'codegen_method' if not explicitly specified that will determine whether and how the enum is code-generated.

    If an enum does not explicitly specify its 'codegen_method' in metadata, it will be assigned the
    least restrictive codegen_method based on the codegen_method of all the functions and attributes
    that use it. The default codegen_method is 'no' (if no function nor attribute uses it).

    If an enum explicitly specifies its 'codegen_method' in metadata, it will be checked against the
    least restrictive codegen_method based on the codegen_method of all the functions and attributes
    that use it (if its explicit 'codegen_method' is more restrictive than the calculated least
    restrictive codegen_method and it does not use converter, a ValueError would be thrown).

    The restrictiveness of the codegen_method is as follows (most restrictive -> least restrictive):
    'no' -> 'private' -> 'public' / 'python-only' (will be converted to 'public' if not explicitly specified)
    

### `def _get_functions_that_use_enums(enums, config)`

Generate a dict that maps each enum to a list of functions that use it in their parameters

### `def _get_attributes_that_use_enums(enums, config)`

Generate a dict that maps each enum to a list of attributes that use it

### `def _get_least_restrictive_codegen_method(codegen_methods)`

Get the least restrictive codegen_method among the input codegen_methods.

    If the codegen_methods parameter is empty, return 'no'.
    The restrictiveness of the codegen_method is as follows (most restrictive -> least restrictive):
    'no' -> 'private' -> 'public' / 'python-only' (will be converted to 'public')
    

### `def _add_enum_value_python_name(enum_info, config)`

Add 'python_name' for all values, removing any common prefixes and suffixes

### `def fixup_enum_names(config)`

Fix enum types for private enums

    Now that we have all the metadata calculated, we need to fix any enum types in attributes and functions
    where the underlying enum is private. At the time the 'python_type' was set, we hadn't yet calculated
    whether the enum would be private or not. We couldn't because we needed to process all the functions and
    attributes first.
    

### `def add_all_enum_metadata(enums, config)`

Merges and Adds all codegen-specific metada to the function metadata list

### `def add_all_config_metadata(config)`

add_all_config_metadata

    Ensure all defaults added to config
    

### `def add_all_metadata(functions, attributes, enums, config, persist_output=True)`

merge and add all additional metadata_dir

    Updates all parameters
        functions, attributes, enums - addon data merged, additional metadata
        config - functions, attributes, enums added
    

<!--NI_PYTHON_API repo=nimi-python path=build/helper/metadata_filters.py -->
## PYTHON MODULE: build/helper/metadata_filters.py

### `def filter_parameters(parameters, parameter_usage_options)`

filter_parameters

    Filters and reorders the parameters passed in based on parameter_usage_options.
    

### `def filter_ivi_dance_parameters(parameters)`

Returns the ivi-dance parameters of a session method if there are any. These are the parameters whose size is determined at runtime using the ivi-dance.

    asserts all parameters that use ivi-dance reference the same parameter
    Args:
        parameters: parameters to be checked

    Return:
        None if no ivi-dance parameter found
        Parameters dict if one is found
    

### `def filter_ivi_dance_twist_parameters(parameters)`

Returns the ivi-dance parameters of a session method if there are any. These are the parameters whose size is determined at runtime using the ivi-dance.

    asserts all parameters that use ivi-dance reference the same parameter
    Args:
        parameters: parameters to be checked

    Return:
        None if no ivi-dance parameter found
        Parameters dict if one is found
    

### `def filter_len_parameters(parameters)`

Returns the len parameters of a session method if there are any. These are the parameters whose size is determined at runtime using the value of a different parameter.

    Note: Multiple len parameters may reference different size parameters.
    Args:
        parameters: parameters to be checked

    Return:
        Empty list if no len parameter found
        List of parameter dicts if any are found
    

### `def filter_codegen_functions(functions)`

Returns function metadata only for those functions to be included in codegen

### `def filter_library_functions(functions)`

Returns function metadata only for those functions to included the library layer (library.py and mock_helper.py)

### `def filter_public_functions(functions)`

Returns function metadata only for those functions that are public

### `def filter_codegen_attributes(attributes)`

Returns attribute metadata only for those attributes to be included in codegen

### `def filter_codegen_attributes_public_only(attributes)`

Returns attribute metadata only for those attributes to be included in codegen

### `def filter_codegen_enums(enums)`

Returns enum metadata only for those enums to be included in codegen

### `def are_complex_parameters_used(functions)`

Returns bool based on whether any complex parameters are used in the functions metadata.

<!--NI_PYTHON_API repo=nimi-python path=build/helper/metadata_find.py -->
## PYTHON MODULE: build/helper/metadata_find.py

### `def find_parameter(name, parameters)`

### `def find_session_handle_parameter(parameters)`

Returns the ViSession parameter.

    Usually it's the one marked as is_session_handle. For Init functions, it's the output parameter.
    

### `def find_size_parameter(parameter_list, parameters, key='value')`

Returns the parameter that is used to specify the size other parameters. Applies to 'ivi-dance', 'ivi-dance-with-a-twist' and 'passed-in'.

    Most behaviors will use 'value', but 'ivi-dance-with-a-twist' uses 'value' and 'value_twist'
    

### `def find_len_size_parameter_names(parameters)`

Returns names of size parameters referenced by len-sized parameters.

    A function may have multiple len-sized parameters, each with a different size parameter.
    

### `def find_custom_type(p, config)`

<!--NI_PYTHON_API repo=nimi-python path=build/helper/metadata_merge_dicts.py -->
## PYTHON MODULE: build/helper/metadata_merge_dicts.py

### `def merge_helper(metadata, metadata_type, config, use_re)`

### `def merge_dicts(into, outof, use_re, dict_name)`

merge_dicts

    Recursively merges the contents of dictionary 'outof' into dictionary 'into'.
    'into' may contain lists as values.
    'outof' may contain regular expressions as keys, in which case values are
    merged with all key matches in into.
    

<!--NI_PYTHON_API repo=nimi-python path=build/helper/parameter_usage_options.py -->
## PYTHON MODULE: build/helper/parameter_usage_options.py

### `class AutoNumber(Enum)`

#### `def __new__(cls)`

### `class ParameterUsageOptions(AutoNumber)`

Different usage options for parameter lists.

<!--NI_PYTHON_API repo=nimi-python path=build/unit_tests/test_codegen_helper.py -->
## PYTHON MODULE: build/unit_tests/test_codegen_helper.py

### `def test_get_library_interpreter_method_return_snippet_vi()`

### `def test_get_library_interpreter_method_return_snippet_int()`

### `def test_get_library_interpreter_method_return_snippet_string()`

### `def test_get_library_interpreter_method_return_snippet_custom_type()`

### `def test_get_library_interpreter_method_return_snippet_enum()`

### `def test_get_library_interpreter_method_return_snippet_into()`

### `def test_get_grpc_interpreter_method_return_snippet_vi()`

### `def test_get_grpc_interpreter_method_return_snippet_int()`

### `def test_get_grpc_interpreter_method_return_snippet_string()`

### `def test_get_grpc_interpreter_method_return_snippet_custom_type()`

### `def test_get_grpc_interpreter_method_return_snippet_enum()`

### `def test_get_grpc_interpreter_method_return_snippet_bytes()`

### `def test_get_session_method_return_snippet()`

### `def test_get_session_method_return_snippet_non_numpy()`

### `def test_get_session_method_return_snippet_numpy()`

### `def test_get_enum_type_check_snippet()`

### `def test_get_buffer_parameters_for_size_parameter_none()`

### `def test_get_buffer_parameters_for_size_parameter()`

### `def test_get_ctype_variable_declaration_snippet_case_c010()`

### `def test_get_ctype_variable_declaration_snippet_case_c020()`

### `def test_get_ctype_variable_declaration_snippet_case_c030()`

### `def test_get_ctype_variable_declaration_snippet_case_c050()`

### `def test_get_ctype_variable_declaration_snippet_case_c060()`

### `def test_get_ctype_variable_declaration_snippet_case_c070()`

### `def test_get_ctype_variable_declaration_snippet_case_c080()`

### `def test_get_ctype_variable_declaration_snippet_case_c090()`

### `def test_get_ctype_variable_declaration_snippet_case_c100()`

### `def test_get_ctype_variable_declaration_snippet_case_s110()`

### `def test_get_ctype_variable_declaration_snippet_case_s120()`

### `def test_get_ctype_variable_declaration_snippet_case_s130()`

### `def test_get_ctype_variable_declaration_snippet_case_s150()`

### `def test_get_ctype_variable_declaration_snippet_case_s160()`

### `def test_get_ctype_variable_declaration_snippet_case_s161()`

### `def test_get_ctype_variable_declaration_snippet_case_s170()`

### `def test_get_ctype_variable_declaration_snippet_case_s180()`

### `def test_get_ctype_variable_declaration_snippet_case_s2190()`

### `def test_get_ctype_variable_declaration_snippet_case_s200()`

### `def test_get_ctype_variable_declaration_snippet_case_s210()`

### `def test_get_ctype_variable_declaration_snippet_case_s220()`

### `def test_get_ctype_variable_declaration_snippet_case_b510()`

### `def test_get_ctype_variable_declaration_snippet_case_b540()`

### `def test_get_ctype_variable_declaration_snippet_case_b550_array()`

### `def test_get_ctype_variable_declaration_snippet_case_b550_list()`

### `def test_get_ctype_variable_declaration_snippet_case_b560()`

### `def test_get_ctype_variable_declaration_snippet_case_b570()`

### `def test_get_ctype_variable_declaration_snippet_case_b580_array()`

### `def test_get_ctype_variable_declaration_snippet_case_b590_array()`

### `def test_get_ctype_variable_declaration_snippet_case_b580_list()`

### `def test_get_ctype_variable_declaration_snippet_case_b590_list()`

### `def test_get_ctype_variable_declaration_snippet_case_b600()`

### `def test_get_ctype_variable_declaration_snippet_case_b610_array()`

### `def test_get_ctype_variable_declaration_snippet_case_b620_array()`

### `def test_get_ctype_variable_declaration_snippet_case_b610_list()`

### `def test_get_ctype_variable_declaration_snippet_case_b620_list()`

### `def test_get_ctype_variable_declaration_snippet_bad_ivi_dance_step()`

### `def test_get_enum_value_snippet()`

<!--NI_PYTHON_API repo=nimi-python path=build/unit_tests/test_documentation_helper.py -->
## PYTHON MODULE: build/unit_tests/test_documentation_helper.py

### `def _remove_trailing_whitespace(s)`

Removes trailing whitespace and empty lines in multi-line strings.

### `def assert_rst_strings_are_equal(expected, actual)`

Asserts rst formatted strings (multiline) are equal. Ignores trailing whitespace and empty lines.

### `def test_get_function_rst_default()`

### `def test_get_function_rst_numpy()`

### `def test_get_attribute_repeated_caps()`

### `def test_get_attribute_repeated_caps_with_conjunction()`

### `def test_module_supports_repeated_caps()`

### `def test_get_function_docstring_default()`

### `def test_get_function_docstring_numpy()`

### `def test_get_rst_header_snippet()`

### `def test_get_documentation_for_node_docstring()`

### `def test_get_rst_picture_reference()`

### `def test_square_up_tables()`

### `def test_add_notes_re_links()`

<!--NI_PYTHON_API repo=nimi-python path=build/unit_tests/test_documentation_snippets.py -->
## PYTHON MODULE: build/unit_tests/test_documentation_snippets.py

### `def test_close_function_def_for_doc_note_not_list()`

Testing for lack of syntax error - not actual documentation

### `def test_close_function_def_for_doc_note_list()`

Testing for lack of syntax error - not actual documentation

### `def test_close_function_def_for_doc_no_note()`

Testing for lack of syntax error - not actual documentation

### `def test_initiate_function_def_for_doc_note_not_list()`

Testing for lack of syntax error - not actual documentation

### `def test_initiate_function_def_for_doc_note_list()`

Testing for lack of syntax error - not actual documentation

### `def test_initiate_function_def_for_doc_no_note()`

Testing for lack of syntax error - not actual documentation

<!--NI_PYTHON_API repo=nimi-python path=build/unit_tests/test_helper.py -->
## PYTHON MODULE: build/unit_tests/test_helper.py

### `def test_get_development_status()`

### `def test_enum_uses_converter()`

<!--NI_PYTHON_API repo=nimi-python path=build/unit_tests/test_metadata_add_all.py -->
## PYTHON MODULE: build/unit_tests/test_metadata_add_all.py

### `def _compare_values(actual, expected, k)`

### `def _compare_lists(actual, expected)`

### `def _compare_dicts(actual, expected)`

### `def _do_the_test_add_functions_metadata(functions, expected)`

### `def test_add_functions_metadata_simple()`

### `def _do_the_test_add_attributes_metadata(attributes, expected)`

### `def test_add_attributes_metadata_simple()`

### `def _do_the_test_add_enums_metadata(enums, expected)`

### `def test_add_enums_metadata_simple()`

### `def _do_the_test_add_all_metadata(functions, attributes, enums, config, expected)`

### `def test_add_all_metadata_defaults()`

### `def test_add_all_metadata()`

### `def _setup_inputs_for_enum_codegen_method_tests()`

### `def test_add_enum_codegen_method()`

### `def test_add_enum_codegen_method_error()`

### `def test_get_functions_that_use_enums()`

### `def test_get_attributes_that_use_enums()`

### `def test_get_least_restrictive_codegen_method()`

<!--NI_PYTHON_API repo=nimi-python path=build/unit_tests/test_metadata_filters.py -->
## PYTHON MODULE: build/unit_tests/test_metadata_filters.py

### `def _parameter(name, direction='in', mechanism='passed-in', size_value=None)`

### `def test_filter_parameters_mixed_usage_ivi_dance_and_len()`

### `def test_filter_parameters_multiple_len_sizes()`

<!--NI_PYTHON_API repo=nimi-python path=build/unit_tests/test_metadata_find.py -->
## PYTHON MODULE: build/unit_tests/test_metadata_find.py

### `def _parameter(name, mechanism='passed-in', size_value=None)`

### `def test_find_len_size_parameter_names_multiple_sizes()`

### `def test_find_len_size_parameter_names_empty_when_no_len_parameters()`

<!--NI_PYTHON_API repo=nimi-python path=build/unit_tests/test_metadata_merge_dicts.py -->
## PYTHON MODULE: build/unit_tests/test_metadata_merge_dicts.py

### `def _do_the_test_merge_dicts(a, b, expected, use_re)`

### `def test_merge_dict_second_is_empty()`

### `def test_merge_dict_key_exists()`

### `def test_merge_dict_recurse()`

### `def test_merge_dict_replace_in_list()`

### `def test_merge_dict_replace_in_dict_and_list()`

### `def test_merge_dict_with_regex()`

### `def test_merge_dict_with_regex_off()`

### `def test_merge_dict_top_level_key_missing()`

<!--NI_PYTHON_API repo=nimi-python path=build/utilities.py -->
## PYTHON MODULE: build/utilities.py

### `def add_to_path(p)`

### `def path_import(absolute_path)`

implementation taken from https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly

### `def configure_logging(lvl=logging.WARNING, logfile=None)`

### `def load_build(m)`

<!--NI_PYTHON_API repo=nimi-python path=docs/nidcpower/conf.py -->
## PYTHON MODULE: docs/nidcpower/conf.py

### `def setup(app)`

<!--NI_PYTHON_API repo=nimi-python path=docs/nidigital/conf.py -->
## PYTHON MODULE: docs/nidigital/conf.py

### `def setup(app)`

<!--NI_PYTHON_API repo=nimi-python path=docs/nidmm/conf.py -->
## PYTHON MODULE: docs/nidmm/conf.py

### `def setup(app)`

<!--NI_PYTHON_API repo=nimi-python path=docs/nifgen/conf.py -->
## PYTHON MODULE: docs/nifgen/conf.py

### `def setup(app)`

<!--NI_PYTHON_API repo=nimi-python path=docs/nimodinst/conf.py -->
## PYTHON MODULE: docs/nimodinst/conf.py

### `def setup(app)`

<!--NI_PYTHON_API repo=nimi-python path=docs/nirfsg/conf.py -->
## PYTHON MODULE: docs/nirfsg/conf.py

### `def setup(app)`

<!--NI_PYTHON_API repo=nimi-python path=docs/niscope/conf.py -->
## PYTHON MODULE: docs/niscope/conf.py

### `def setup(app)`

<!--NI_PYTHON_API repo=nimi-python path=docs/nise/conf.py -->
## PYTHON MODULE: docs/nise/conf.py

### `def setup(app)`

<!--NI_PYTHON_API repo=nimi-python path=docs/niswitch/conf.py -->
## PYTHON MODULE: docs/niswitch/conf.py

### `def setup(app)`

<!--NI_PYTHON_API repo=nimi-python path=docs/nitclk/conf.py -->
## PYTHON MODULE: docs/nitclk/conf.py

### `def setup(app)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nidcpower/nidcpower/__init__.py -->
## PYTHON MODULE: generated/nidcpower/nidcpower/__init__.py

### `def get_diagnostic_information()`

Get diagnostic information about the system state that is suitable for printing or logging

    returns: dict

    note: Python bitness may be incorrect when running in a virtual environment
    

### `def print_diagnostic_information()`

Print diagnostic information in a format suitable for issue report

    note: Python bitness may be incorrect when running in a virtual environment
    

<!--NI_PYTHON_API repo=nimi-python path=generated/nidcpower/nidcpower/_attributes.py -->
## PYTHON MODULE: generated/nidcpower/nidcpower/_attributes.py

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

Class for attributes that use enums internally but are exposed in the nidcpower Python module as something else, thus need conversion.

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

<!--NI_PYTHON_API repo=nimi-python path=generated/nidcpower/nidcpower/_converters.py -->
## PYTHON MODULE: generated/nidcpower/nidcpower/_converters.py

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
    

### `def convert_from_isolation_state_enum(value)`

### `def convert_to_isolation_state_enum(value)`

### `def convert_from_lcr_impedance_auto_range_enum(value)`

### `def convert_to_lcr_impedance_auto_range_enum(value)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nidcpower/nidcpower/_grpc_stub_interpreter.py -->
## PYTHON MODULE: generated/nidcpower/nidcpower/_grpc_stub_interpreter.py

### `class GrpcStubInterpreter(object)`

Interpreter for interacting with a gRPC Stub class

#### `def __init__(self, grpc_options)`

#### `def set_session_handle(self, value=session_grpc_types.Session())`

#### `def get_session_handle(self)`

#### `def _invoke(self, func, request, metadata=None)`

#### `def abort(self, channel_name)`

#### `def self_cal(self, channel_name)`

#### `def clear_latched_output_cutoff_state(self, channel_name, output_cutoff_reason)`

#### `def commit(self, channel_name)`

#### `def configure_aperture_time(self, channel_name, aperture_time, units)`

#### `def configure_lcr_compensation(self, channel_name, compensation_data)`

#### `def configure_lcr_custom_cable_compensation(self, channel_name, custom_cable_compensation_data)`

#### `def create_advanced_sequence_commit_step(self, channel_name, set_as_active_step)`

#### `def create_advanced_sequence_step(self, channel_name, set_as_active_step)`

#### `def create_advanced_sequence_with_channels(self, channel_name, sequence_name, attribute_ids, set_as_active_sequence)`

#### `def delete_advanced_sequence(self, channel_name, sequence_name)`

#### `def disable(self)`

#### `def export_attribute_configuration_buffer(self)`

#### `def export_attribute_configuration_file(self, file_path)`

#### `def fancy_initialize(self, resource_name, channels, reset, option_string, independent_channels)`

#### `def fetch_multiple(self, channel_name, timeout, count)`

#### `def fetch_multiple_lcr(self, channel_name, timeout, count)`

#### `def get_attribute_vi_boolean(self, channel_name, attribute_id)`

#### `def get_attribute_vi_int32(self, channel_name, attribute_id)`

#### `def get_attribute_vi_int64(self, channel_name, attribute_id)`

#### `def get_attribute_vi_real64(self, channel_name, attribute_id)`

#### `def get_attribute_vi_string(self, channel_name, attribute_id)`

#### `def get_channel_name(self, index)`

#### `def get_channel_names(self, indices)`

#### `def get_error(self)`

#### `def get_ext_cal_last_date_and_time(self)`

#### `def get_ext_cal_last_temp(self)`

#### `def get_ext_cal_recommended_interval(self)`

#### `def get_lcr_compensation_data(self, channel_name)`

#### `def get_lcr_compensation_last_date_and_time(self, channel_name, compensation_type)`

#### `def get_lcr_custom_cable_compensation_data(self, channel_name)`

#### `def get_self_cal_last_date_and_time(self)`

#### `def get_self_cal_last_temp(self)`

#### `def import_attribute_configuration_buffer(self, configuration)`

#### `def import_attribute_configuration_file(self, file_path)`

#### `def initialize_with_channels(self, resource_name, channels, reset, option_string)`

#### `def initialize_with_independent_channels(self, resource_name, reset, option_string)`

#### `def initiate_with_channels(self, channel_name)`

#### `def lock(self)`

#### `def measure(self, channel_name, measurement_type)`

#### `def measure_multiple(self, channel_name)`

#### `def measure_multiple_lcr(self, channel_name)`

#### `def parse_channel_count(self, channels_string)`

#### `def perform_lcr_load_compensation(self, channel_name, compensation_spots)`

#### `def perform_lcr_open_compensation(self, channel_name, additional_frequencies)`

#### `def perform_lcr_open_custom_cable_compensation(self, channel_name)`

#### `def perform_lcr_short_compensation(self, channel_name, additional_frequencies)`

#### `def perform_lcr_short_custom_cable_compensation(self, channel_name)`

#### `def query_in_compliance(self, channel_name)`

#### `def query_latched_output_cutoff_state(self, channel_name, output_cutoff_reason)`

#### `def query_max_current_limit(self, channel_name, voltage_level)`

#### `def query_max_voltage_level(self, channel_name, current_limit)`

#### `def query_min_current_limit(self, channel_name, voltage_level)`

#### `def query_output_state(self, channel_name, output_state)`

#### `def read_current_temperature(self)`

#### `def reset_device(self)`

#### `def reset(self, channel_name)`

#### `def reset_with_defaults(self)`

#### `def send_software_edge_trigger(self, channel_name, trigger)`

#### `def set_attribute_vi_boolean(self, channel_name, attribute_id, attribute_value)`

#### `def set_attribute_vi_int32(self, channel_name, attribute_id, attribute_value)`

#### `def set_attribute_vi_int64(self, channel_name, attribute_id, attribute_value)`

#### `def set_attribute_vi_real64(self, channel_name, attribute_id, attribute_value)`

#### `def set_attribute_vi_string(self, channel_name, attribute_id, attribute_value)`

#### `def set_runtime_environment(self, environment, environment_version, reserved1, reserved2)`

#### `def set_sequence(self, channel_name, values, source_delays)`

#### `def unlock(self)`

#### `def wait_for_event(self, channel_name, event_id, timeout)`

#### `def close(self)`

#### `def error_message(self, error_code)`

#### `def self_test(self)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nidcpower/nidcpower/_library.py -->
## PYTHON MODULE: generated/nidcpower/nidcpower/_library.py

### `class Library(object)`

Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    

#### `def __init__(self, ctypes_library)`

#### `def _get_library_function(self, name)`

#### `def niDCPower_AbortWithChannels(self, vi, channel_name)`

#### `def niDCPower_CalSelfCalibrate(self, vi, channel_name)`

#### `def niDCPower_ClearLatchedOutputCutoffState(self, vi, channel_name, output_cutoff_reason)`

#### `def niDCPower_CommitWithChannels(self, vi, channel_name)`

#### `def niDCPower_ConfigureApertureTime(self, vi, channel_name, aperture_time, units)`

#### `def niDCPower_ConfigureLCRCompensation(self, vi, channel_name, compensation_data_size, compensation_data)`

#### `def niDCPower_ConfigureLCRCustomCableCompensation(self, vi, channel_name, custom_cable_compensation_data_size, custom_cable_compensation_data)`

#### `def niDCPower_CreateAdvancedSequenceCommitStepWithChannels(self, vi, channel_name, set_as_active_step)`

#### `def niDCPower_CreateAdvancedSequenceStepWithChannels(self, vi, channel_name, set_as_active_step)`

#### `def niDCPower_CreateAdvancedSequenceWithChannels(self, vi, channel_name, sequence_name, attribute_id_count, attribute_ids, set_as_active_sequence)`

#### `def niDCPower_DeleteAdvancedSequenceWithChannels(self, vi, channel_name, sequence_name)`

#### `def niDCPower_Disable(self, vi)`

#### `def niDCPower_ExportAttributeConfigurationBuffer(self, vi, size, configuration)`

#### `def niDCPower_ExportAttributeConfigurationFile(self, vi, file_path)`

#### `def niDCPower_FancyInitialize(self, resource_name, channels, reset, option_string, vi, independent_channels)`

#### `def niDCPower_FetchMultiple(self, vi, channel_name, timeout, count, voltage_measurements, current_measurements, in_compliance, actual_count)`

#### `def niDCPower_FetchMultipleLCR(self, vi, channel_name, timeout, count, measurements, actual_count)`

#### `def niDCPower_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niDCPower_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niDCPower_GetAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niDCPower_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niDCPower_GetAttributeViString(self, vi, channel_name, attribute_id, buffer_size, attribute_value)`

#### `def niDCPower_GetChannelName(self, vi, index, buffer_size, channel_name)`

#### `def niDCPower_GetChannelNameFromString(self, vi, indices, buffer_size, names)`

#### `def niDCPower_GetError(self, vi, code, buffer_size, description)`

#### `def niDCPower_GetExtCalLastDateAndTime(self, vi, year, month, day, hour, minute)`

#### `def niDCPower_GetExtCalLastTemp(self, vi, temperature)`

#### `def niDCPower_GetExtCalRecommendedInterval(self, vi, months)`

#### `def niDCPower_GetLCRCompensationData(self, vi, channel_name, compensation_data_size, compensation_data)`

#### `def niDCPower_GetLCRCompensationLastDateAndTime(self, vi, channel_name, compensation_type, year, month, day, hour, minute)`

#### `def niDCPower_GetLCRCustomCableCompensationData(self, vi, channel_name, custom_cable_compensation_data_size, custom_cable_compensation_data)`

#### `def niDCPower_GetSelfCalLastDateAndTime(self, vi, year, month, day, hour, minute)`

#### `def niDCPower_GetSelfCalLastTemp(self, vi, temperature)`

#### `def niDCPower_ImportAttributeConfigurationBuffer(self, vi, size, configuration)`

#### `def niDCPower_ImportAttributeConfigurationFile(self, vi, file_path)`

#### `def niDCPower_InitializeWithChannels(self, resource_name, channels, reset, option_string, vi)`

#### `def niDCPower_InitializeWithIndependentChannels(self, resource_name, reset, option_string, vi)`

#### `def niDCPower_InitiateWithChannels(self, vi, channel_name)`

#### `def niDCPower_LockSession(self, vi, caller_has_lock)`

#### `def niDCPower_Measure(self, vi, channel_name, measurement_type, measurement)`

#### `def niDCPower_MeasureMultiple(self, vi, channel_name, voltage_measurements, current_measurements)`

#### `def niDCPower_MeasureMultipleLCR(self, vi, channel_name, measurements)`

#### `def niDCPower_ParseChannelCount(self, vi, channels_string, number_of_channels)`

#### `def niDCPower_PerformLCRLoadCompensation(self, vi, channel_name, num_compensation_spots, compensation_spots)`

#### `def niDCPower_PerformLCROpenCompensation(self, vi, channel_name, num_frequencies, additional_frequencies)`

#### `def niDCPower_PerformLCROpenCustomCableCompensation(self, vi, channel_name)`

#### `def niDCPower_PerformLCRShortCompensation(self, vi, channel_name, num_frequencies, additional_frequencies)`

#### `def niDCPower_PerformLCRShortCustomCableCompensation(self, vi, channel_name)`

#### `def niDCPower_QueryInCompliance(self, vi, channel_name, in_compliance)`

#### `def niDCPower_QueryLatchedOutputCutoffState(self, vi, channel_name, output_cutoff_reason, output_cutoff_state)`

#### `def niDCPower_QueryMaxCurrentLimit(self, vi, channel_name, voltage_level, max_current_limit)`

#### `def niDCPower_QueryMaxVoltageLevel(self, vi, channel_name, current_limit, max_voltage_level)`

#### `def niDCPower_QueryMinCurrentLimit(self, vi, channel_name, voltage_level, min_current_limit)`

#### `def niDCPower_QueryOutputState(self, vi, channel_name, output_state, in_state)`

#### `def niDCPower_ReadCurrentTemperature(self, vi, temperature)`

#### `def niDCPower_ResetDevice(self, vi)`

#### `def niDCPower_ResetWithChannels(self, vi, channel_name)`

#### `def niDCPower_ResetWithDefaults(self, vi)`

#### `def niDCPower_SendSoftwareEdgeTriggerWithChannels(self, vi, channel_name, trigger)`

#### `def niDCPower_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niDCPower_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niDCPower_SetAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niDCPower_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niDCPower_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niDCPower_SetRuntimeEnvironment(self, environment, environment_version, reserved1, reserved2)`

#### `def niDCPower_SetSequence(self, vi, channel_name, values, source_delays, size)`

#### `def niDCPower_UnlockSession(self, vi, caller_has_lock)`

#### `def niDCPower_WaitForEventWithChannels(self, vi, channel_name, event_id, timeout)`

#### `def niDCPower_close(self, vi)`

#### `def niDCPower_error_message(self, vi, error_code, error_message)`

#### `def niDCPower_self_test(self, vi, self_test_result, self_test_message)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nidcpower/nidcpower/_library_interpreter.py -->
## PYTHON MODULE: generated/nidcpower/nidcpower/_library_interpreter.py

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
        

#### `def abort(self, channel_name)`

#### `def self_cal(self, channel_name)`

#### `def clear_latched_output_cutoff_state(self, channel_name, output_cutoff_reason)`

#### `def commit(self, channel_name)`

#### `def configure_aperture_time(self, channel_name, aperture_time, units)`

#### `def configure_lcr_compensation(self, channel_name, compensation_data)`

#### `def configure_lcr_custom_cable_compensation(self, channel_name, custom_cable_compensation_data)`

#### `def create_advanced_sequence_commit_step(self, channel_name, set_as_active_step)`

#### `def create_advanced_sequence_step(self, channel_name, set_as_active_step)`

#### `def create_advanced_sequence_with_channels(self, channel_name, sequence_name, attribute_ids, set_as_active_sequence)`

#### `def delete_advanced_sequence(self, channel_name, sequence_name)`

#### `def disable(self)`

#### `def export_attribute_configuration_buffer(self)`

#### `def export_attribute_configuration_file(self, file_path)`

#### `def fancy_initialize(self, resource_name, channels, reset, option_string, independent_channels)`

#### `def fetch_multiple(self, channel_name, timeout, count)`

#### `def fetch_multiple_lcr(self, channel_name, timeout, count)`

#### `def get_attribute_vi_boolean(self, channel_name, attribute_id)`

#### `def get_attribute_vi_int32(self, channel_name, attribute_id)`

#### `def get_attribute_vi_int64(self, channel_name, attribute_id)`

#### `def get_attribute_vi_real64(self, channel_name, attribute_id)`

#### `def get_attribute_vi_string(self, channel_name, attribute_id)`

#### `def get_channel_name(self, index)`

#### `def get_channel_names(self, indices)`

#### `def get_error(self)`

#### `def get_ext_cal_last_date_and_time(self)`

#### `def get_ext_cal_last_temp(self)`

#### `def get_ext_cal_recommended_interval(self)`

#### `def get_lcr_compensation_data(self, channel_name)`

#### `def get_lcr_compensation_last_date_and_time(self, channel_name, compensation_type)`

#### `def get_lcr_custom_cable_compensation_data(self, channel_name)`

#### `def get_self_cal_last_date_and_time(self)`

#### `def get_self_cal_last_temp(self)`

#### `def import_attribute_configuration_buffer(self, configuration)`

#### `def import_attribute_configuration_file(self, file_path)`

#### `def initialize_with_channels(self, resource_name, channels, reset, option_string)`

#### `def initialize_with_independent_channels(self, resource_name, reset, option_string)`

#### `def initiate_with_channels(self, channel_name)`

#### `def lock(self)`

#### `def measure(self, channel_name, measurement_type)`

#### `def measure_multiple(self, channel_name)`

#### `def measure_multiple_lcr(self, channel_name)`

#### `def parse_channel_count(self, channels_string)`

#### `def perform_lcr_load_compensation(self, channel_name, compensation_spots)`

#### `def perform_lcr_open_compensation(self, channel_name, additional_frequencies)`

#### `def perform_lcr_open_custom_cable_compensation(self, channel_name)`

#### `def perform_lcr_short_compensation(self, channel_name, additional_frequencies)`

#### `def perform_lcr_short_custom_cable_compensation(self, channel_name)`

#### `def query_in_compliance(self, channel_name)`

#### `def query_latched_output_cutoff_state(self, channel_name, output_cutoff_reason)`

#### `def query_max_current_limit(self, channel_name, voltage_level)`

#### `def query_max_voltage_level(self, channel_name, current_limit)`

#### `def query_min_current_limit(self, channel_name, voltage_level)`

#### `def query_output_state(self, channel_name, output_state)`

#### `def read_current_temperature(self)`

#### `def reset_device(self)`

#### `def reset(self, channel_name)`

#### `def reset_with_defaults(self)`

#### `def send_software_edge_trigger(self, channel_name, trigger)`

#### `def set_attribute_vi_boolean(self, channel_name, attribute_id, attribute_value)`

#### `def set_attribute_vi_int32(self, channel_name, attribute_id, attribute_value)`

#### `def set_attribute_vi_int64(self, channel_name, attribute_id, attribute_value)`

#### `def set_attribute_vi_real64(self, channel_name, attribute_id, attribute_value)`

#### `def set_attribute_vi_string(self, channel_name, attribute_id, attribute_value)`

#### `def set_runtime_environment(self, environment, environment_version, reserved1, reserved2)`

#### `def set_sequence(self, channel_name, values, source_delays)`

#### `def unlock(self)`

#### `def wait_for_event(self, channel_name, event_id, timeout)`

#### `def close(self)`

#### `def error_message(self, error_code)`

#### `def self_test(self)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nidcpower/nidcpower/_library_singleton.py -->
## PYTHON MODULE: generated/nidcpower/nidcpower/_library_singleton.py

### `def _get_library_name()`

### `def _get_library_type()`

### `def get()`

get

    Returns the library.Library singleton for nidcpower.
    

<!--NI_PYTHON_API repo=nimi-python path=generated/nidcpower/nidcpower/enums.py -->
## PYTHON MODULE: generated/nidcpower/nidcpower/enums.py

### `class ApertureTimeAutoMode(Enum)`

### `class ApertureTimeUnits(Enum)`

### `class AutoZero(Enum)`

### `class AutorangeApertureTimeMode(Enum)`

### `class AutorangeBehavior(Enum)`

### `class AutorangeThresholdMode(Enum)`

### `class CableLength(Enum)`

### `class ComplianceLimitSymmetry(Enum)`

### `class ConductionVoltageMode(Enum)`

### `class CurrentLimitBehavior(Enum)`

### `class DCNoiseRejection(Enum)`

### `class Event(Enum)`

### `class EventOutputBehavior(Enum)`

### `class EventToggleInitialState(Enum)`

### `class InstrumentMode(Enum)`

### `class _IsolationState(Enum)`

### `class LCRCompensationType(Enum)`

### `class LCRDCBiasSource(Enum)`

### `class LCRDCBiasTransientResponse(Enum)`

### `class _LCRImpedanceAutoRange(Enum)`

### `class LCRImpedanceRangeSource(Enum)`

### `class LCRMeasurementTime(Enum)`

### `class LCROpenShortLoadCompensationDataSource(Enum)`

### `class LCRReferenceValueType(Enum)`

### `class LCRSourceDelayMode(Enum)`

### `class LCRStimulusFunction(Enum)`

### `class MeasureWhen(Enum)`

### `class MeasurementTypes(Enum)`

### `class OutputCapacitance(Enum)`

### `class OutputCutoffReason(Enum)`

### `class OutputFunction(Enum)`

### `class OutputStates(Enum)`

### `class Polarity(Enum)`

### `class PowerAllocationMode(Enum)`

### `class PowerSource(Enum)`

### `class PowerSourceInUse(Enum)`

### `class SelfCalibrationPersistence(Enum)`

### `class SendSoftwareEdgeTriggerType(Enum)`

### `class Sense(Enum)`

### `class SourceMode(Enum)`

### `class TransientResponse(Enum)`

### `class TriggerType(Enum)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nidcpower/nidcpower/errors.py -->
## PYTHON MODULE: generated/nidcpower/nidcpower/errors.py

### `def _is_success(code)`

### `def _is_error(code)`

### `def _is_warning(code)`

### `class Error(Exception)`

Base error class for NI-DCPower

#### `def __init__(self, message)`

### `class DriverError(Error)`

An error originating from the NI-DCPower driver

#### `def __init__(self, code, description)`

### `class DriverWarning(Warning)`

A warning originating from the NI-DCPower driver

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

An error due to using this module with an older version of the NI-DCPower driver runtime.

#### `def __init__(self)`

### `class DriverTooNewError(Error)`

An error due to the NI-DCPower driver runtime being too new for this module.

#### `def __init__(self)`

### `class InvalidRepeatedCapabilityError(Error)`

An error due to an invalid character in a repeated capability

#### `def __init__(self, invalid_character, invalid_string)`

### `class SelfTestError(Error)`

An error due to a failed self-test

#### `def __init__(self, code, msg)`

### `def handle_error(library_interpreter, code, ignore_warnings, is_error_handling)`

handle_error

    Helper function for handling errors returned by nidcpower.Library.
    It calls back into the LibraryInterpreter to get the corresponding error
    description and raises if necessary.
    

<!--NI_PYTHON_API repo=nimi-python path=generated/nidcpower/nidcpower/grpc_session_options.py -->
## PYTHON MODULE: generated/nidcpower/nidcpower/grpc_session_options.py

- `GRPC_SERVICE_INTERFACE_NAME = 'nidcpower_grpc.NiDCPower'`

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
        

<!--NI_PYTHON_API repo=nimi-python path=generated/nidcpower/nidcpower/lcr_load_compensation_spot.py -->
## PYTHON MODULE: generated/nidcpower/nidcpower/lcr_load_compensation_spot.py

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

<!--NI_PYTHON_API repo=nimi-python path=generated/nidcpower/nidcpower/lcr_measurement.py -->
## PYTHON MODULE: generated/nidcpower/nidcpower/lcr_measurement.py

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

<!--NI_PYTHON_API repo=nimi-python path=generated/nidcpower/nidcpower/nidcpower_pb2.py -->
## PYTHON MODULE: generated/nidcpower/nidcpower/nidcpower_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fnidcpower.proto\x12\x0enidcpower_grpc\x1a\x0enidevice.proto\x1a\rsession.proto"\x92\x04\n\x10NILCRMeasurement\x12\x0b\n\x03vdc\x18\x01 \x01(\x01\x12\x0b\n\x03idc\x18\x02 \x01(\x01\x12\x1a\n\x12stimulus_frequency\x18\x03 \x01(\x01\x122\n\nac_voltage\x18\x04 \x01(\x0b2\x1e.nidevice_grpc.NIComplexNumber\x122\n\nac_current\x18\x05 \x01(\x0b2\x1e.nidevice_grpc.NIComplexNumber\x12)\n\x01z\x18\x06 \x01(\x0b2\x1e.nidevice_grpc.NIComplexNumber\x12\x13\n\x0bz_magnitude\x18\x07 \x01(\x01\x12\x0f\n\x07z_phase\x18\x08 \x01(\x01\x12)\n\x01y\x18\t \x01(\x0b2\x1e.nidevice_grpc.NIComplexNumber\x12\x13\n\x0by_magnitude\x18\n \x01(\x01\x12\x0f\n\x07y_phase\x18\x0b \x01(\x01\x12\n\n\x02ls\x18\x0c \x01(\x01\x12\n\n\x02cs\x18\r \x01(\x01\x12\n\n\x02rs\x18\x0e \x01(\x01\x12\n\n\x02lp\x18\x0f \x01(\x01\x12\n\n\x02cp\x18\x10 \x01(\x01\x12\n\n\x02rp\x18\x11 \x01(\x01\x12\t\n\x01d\x18\x12 \x01(\x01\x12\t\n\x01q\x18\x13 \x01(\x01\x12\x18\n\x10measurement_mode\x18\x14 \x01(\r\x12\x18\n\x10dc_in_compliance\x18\x15 \x01(\x08\x12\x18\n\x10ac_in_compliance\x18\x16 \x01(\x08\x12\x12\n\nunbalanced\x18\x17 \x01(\x08"\x82\x01\n\x19NILCRLoadCompensationSpot\x12\x11\n\tfrequency\x18\x01 \x01(\x01\x12\x1c\n\x14reference_value_type\x18\x02 \x01(\x11\x12\x19\n\x11reference_value_a\x18\x03 \x01(\x01\x12\x19\n\x11reference_value_b\x18\x04 \x01(\x01"\xd3\x01\n\x1dInitializeWithChannelsRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\x10\n\x08channels\x18\x03 \x01(\t\x12\r\n\x05reset\x18\x04 \x01(\x08\x12\x15\n\roption_string\x18\x05 \x01(\t\x12M\n\x17initialization_behavior\x18\x06 \x01(\x0e2,.nidevice_grpc.SessionInitializationBehavior"\x90\x01\n\x1eInitializeWithChannelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12"\n\x02vi\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x19\n\rerror_message\x18\x03 \x01(\tB\x02\x18\x01\x12\x1f\n\x17new_session_initialized\x18\x04 \x01(\x08"2\n\x0cCloseRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\x1f\n\rCloseResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa2\x01\n\x1aConfigureSourceModeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x121\n\x0bsource_mode\x18\x02 \x01(\x0e2\x1a.nidcpower_grpc.SourceModeH\x00\x12\x19\n\x0fsource_mode_raw\x18\x03 \x01(\x11H\x00B\x12\n\x10source_mode_enum"-\n\x1bConfigureSourceModeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb7\x01\n\x1eConfigureOutputFunctionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x122\n\x08function\x18\x03 \x01(\x0e2\x1e.nidcpower_grpc.OutputFunctionH\x00\x12\x16\n\x0cfunction_raw\x18\x04 \x01(\x11H\x00B\x0f\n\rfunction_enum"1\n\x1fConfigureOutputFunctionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"j\n\x1dConfigureOutputEnabledRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x0f\n\x07enabled\x18\x03 \x01(\x08"0\n\x1eConfigureOutputEnabledResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"u\n\x12SetSequenceRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x0e\n\x06values\x18\x03 \x03(\x01\x12\x15\n\rsource_delays\x18\x04 \x03(\x01"%\n\x13SetSequenceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"g\n\x1cConfigureVoltageLevelRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\r\n\x05level\x18\x03 \x01(\x01"/\n\x1dConfigureVoltageLevelResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xca\x01\n\x1cConfigureCurrentLimitRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x128\n\x08behavior\x18\x03 \x01(\x0e2$.nidcpower_grpc.CurrentLimitBehaviorH\x00\x12\x16\n\x0cbehavior_raw\x18\x04 \x01(\x11H\x00\x12\r\n\x05limit\x18\x05 \x01(\x01B\x0f\n\rbehavior_enum"/\n\x1dConfigureCurrentLimitResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"l\n!ConfigureVoltageLevelRangeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\r\n\x05range\x18\x03 \x01(\x01"4\n"ConfigureVoltageLevelRangeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"l\n!ConfigureCurrentLimitRangeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\r\n\x05range\x18\x03 \x01(\x01"4\n"ConfigureCurrentLimitRangeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"p\n ConfigureOutputResistanceRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x12\n\nresistance\x18\x03 \x01(\x01"3\n!ConfigureOutputResistanceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"g\n\x1cConfigureCurrentLevelRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\r\n\x05level\x18\x03 \x01(\x01"/\n\x1dConfigureCurrentLevelResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"l\n!ConfigureCurrentLevelRangeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\r\n\x05range\x18\x03 \x01(\x01"4\n"ConfigureCurrentLevelRangeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"g\n\x1cConfigureVoltageLimitRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\r\n\x05limit\x18\x03 \x01(\x01"/\n\x1dConfigureVoltageLimitResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"l\n!ConfigureVoltageLimitRangeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\r\n\x05range\x18\x03 \x01(\x01"4\n"ConfigureVoltageLimitRangeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"l\n!ConfigurePulseVoltageLevelRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\r\n\x05level\x18\x03 \x01(\x01"4\n"ConfigurePulseVoltageLevelResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"l\n!ConfigurePulseCurrentLimitRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\r\n\x05limit\x18\x03 \x01(\x01"4\n"ConfigurePulseCurrentLimitResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"p\n%ConfigurePulseBiasVoltageLevelRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\r\n\x05level\x18\x03 \x01(\x01"8\n&ConfigurePulseBiasVoltageLevelResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"p\n%ConfigurePulseBiasCurrentLimitRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\r\n\x05limit\x18\x03 \x01(\x01"8\n&ConfigurePulseBiasCurrentLimitResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"q\n&ConfigurePulseVoltageLevelRangeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\r\n\x05range\x18\x03 \x01(\x01"9\n\'ConfigurePulseVoltageLevelRangeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"q\n&ConfigurePulseCurrentLimitRangeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\r\n\x05range\x18\x03 \x01(\x01"9\n\'ConfigurePulseCurrentLimitRangeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"l\n!ConfigurePulseCurrentLevelRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\r\n\x05level\x18\x03 \x01(\x01"4\n"ConfigurePulseCurrentLevelResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"l\n!ConfigurePulseVoltageLimitRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\r\n\x05limit\x18\x03 \x01(\x01"4\n"ConfigurePulseVoltageLimitResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"p\n%ConfigurePulseBiasCurrentLevelRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\r\n\x05level\x18\x03 \x01(\x01"8\n&ConfigurePulseBiasCurrentLevelResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"p\n%ConfigurePulseBiasVoltageLimitRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\r\n\x05limit\x18\x03 \x01(\x01"8\n&ConfigurePulseBiasVoltageLimitResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"q\n&ConfigurePulseCurrentLevelRangeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\r\n\x05range\x18\x03 \x01(\x01"9\n\'ConfigurePulseCurrentLevelRangeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"q\n&ConfigurePulseVoltageLimitRangeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\r\n\x05range\x18\x03 \x01(\x01"9\n\'ConfigurePulseVoltageLimitRangeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x91\x01\n\x1dCreateAdvancedSequenceRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rsequence_name\x18\x02 \x01(\t\x12\x15\n\rattribute_ids\x18\x03 \x03(\x11\x12\x1e\n\x16set_as_active_sequence\x18\x04 \x01(\x08"0\n\x1eCreateAdvancedSequenceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"c\n!CreateAdvancedSequenceStepRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12set_as_active_step\x18\x02 \x01(\x08"4\n"CreateAdvancedSequenceStepResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"Z\n\x1dDeleteAdvancedSequenceRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rsequence_name\x18\x02 \x01(\t"0\n\x1eDeleteAdvancedSequenceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xc6\x01\n\x1cConfigureApertureTimeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x15\n\raperture_time\x18\x03 \x01(\x01\x122\n\x05units\x18\x04 \x01(\x0e2!.nidcpower_grpc.ApertureTimeUnitsH\x00\x12\x13\n\tunits_raw\x18\x05 \x01(\x11H\x00B\x0c\n\nunits_enum"/\n\x1dConfigureApertureTimeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xae\x01\n\x18ConfigureAutoZeroRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12-\n\tauto_zero\x18\x03 \x01(\x0e2\x18.nidcpower_grpc.AutoZeroH\x00\x12\x17\n\rauto_zero_raw\x18\x04 \x01(\x11H\x00B\x10\n\x0eauto_zero_enum"+\n\x19ConfigureAutoZeroResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xcc\x01\n"ConfigurePowerLineFrequencyRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12C\n\x13powerline_frequency\x18\x02 \x01(\x0e2$.nidcpower_grpc.PowerLineFrequenciesH\x00\x12!\n\x17powerline_frequency_raw\x18\x03 \x01(\x01H\x00B\x1a\n\x18powerline_frequency_enum"5\n#ConfigurePowerLineFrequencyResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x9c\x01\n\x15ConfigureSenseRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12&\n\x05sense\x18\x03 \x01(\x0e2\x15.nidcpower_grpc.SenseH\x00\x12\x13\n\tsense_raw\x18\x04 \x01(\x11H\x00B\x0c\n\nsense_enum"(\n\x16ConfigureSenseResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xc1\x01\n\x0eMeasureRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12<\n\x10measurement_type\x18\x03 \x01(\x0e2 .nidcpower_grpc.MeasurementTypesH\x00\x12\x1e\n\x14measurement_type_raw\x18\x04 \x01(\x11H\x00B\x17\n\x15measurement_type_enum"6\n\x0fMeasureResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0bmeasurement\x18\x02 \x01(\x01"R\n\x16MeasureMultipleRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t"e\n\x17MeasureMultipleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1c\n\x14voltage_measurements\x18\x02 \x03(\x01\x12\x1c\n\x14current_measurements\x18\x03 \x03(\x01"p\n\x14FetchMultipleRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12\r\n\x05count\x18\x04 \x01(\x11"\x90\x01\n\x15FetchMultipleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1c\n\x14voltage_measurements\x18\x02 \x03(\x01\x12\x1c\n\x14current_measurements\x18\x03 \x03(\x01\x12\x15\n\rin_compliance\x18\x04 \x03(\x08\x12\x14\n\x0cactual_count\x18\x05 \x01(\x11"U\n\x19MeasureMultipleLCRRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t"d\n\x1aMeasureMultipleLCRResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x126\n\x0cmeasurements\x18\x02 \x03(\x0b2 .nidcpower_grpc.NILCRMeasurement"s\n\x17FetchMultipleLCRRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x0f\n\x07timeout\x18\x03 \x01(\x01\x12\r\n\x05count\x18\x04 \x01(\x11"x\n\x18FetchMultipleLCRResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x126\n\x0cmeasurements\x18\x02 \x03(\x0b2 .nidcpower_grpc.NILCRMeasurement\x12\x14\n\x0cactual_count\x18\x03 \x01(\x11"T\n\x18QueryInComplianceRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t"B\n\x19QueryInComplianceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rin_compliance\x18\x02 \x01(\x08"\xba\x01\n\x17QueryOutputStateRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x124\n\x0coutput_state\x18\x03 \x01(\x0e2\x1c.nidcpower_grpc.OutputStatesH\x00\x12\x1a\n\x10output_state_raw\x18\x04 \x01(\x11H\x00B\x13\n\x11output_state_enum"<\n\x18QueryOutputStateResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x10\n\x08in_state\x18\x02 \x01(\x08"\xe5\x01\n$QueryLatchedOutputCutoffStateRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12B\n\x14output_cutoff_reason\x18\x03 \x01(\x0e2".nidcpower_grpc.OutputCutoffReasonH\x00\x12"\n\x18output_cutoff_reason_raw\x18\x04 \x01(\x11H\x00B\x1b\n\x19output_cutoff_reason_enum"T\n%QueryLatchedOutputCutoffStateResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1b\n\x13output_cutoff_state\x18\x02 \x01(\x08"\xe5\x01\n$ClearLatchedOutputCutoffStateRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12B\n\x14output_cutoff_reason\x18\x03 \x01(\x0e2".nidcpower_grpc.OutputCutoffReasonH\x00\x12"\n\x18output_cutoff_reason_raw\x18\x04 \x01(\x11H\x00B\x1b\n\x19output_cutoff_reason_enum"7\n%ClearLatchedOutputCutoffStateResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"3\n\rCommitRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session" \n\x0eCommitResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"5\n\x0fInitiateRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session""\n\x10InitiateResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"2\n\x0cAbortRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\x1f\n\rAbortResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"n\n\x1bQueryMaxCurrentLimitRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x15\n\rvoltage_level\x18\x03 \x01(\x01"I\n\x1cQueryMaxCurrentLimitResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x19\n\x11max_current_limit\x18\x02 \x01(\x01"n\n\x1bQueryMaxVoltageLevelRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x15\n\rcurrent_limit\x18\x03 \x01(\x01"I\n\x1cQueryMaxVoltageLevelResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x19\n\x11max_voltage_level\x18\x02 \x01(\x01"n\n\x1bQueryMinCurrentLimitRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x15\n\rvoltage_level\x18\x03 \x01(\x01"I\n\x1cQueryMinCurrentLimitResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x19\n\x11min_current_limit\x18\x02 \x01(\x01"S\n\x17CalSelfCalibrateRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t"*\n\x18CalSelfCalibrateResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"I\n#GetExtCalRecommendedIntervalRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"F\n$GetExtCalRecommendedIntervalResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0e\n\x06months\x18\x02 \x01(\x11"E\n\x1fGetExtCalLastDateAndTimeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"z\n GetExtCalLastDateAndTimeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04year\x18\x02 \x01(\x11\x12\r\n\x05month\x18\x03 \x01(\x11\x12\x0b\n\x03day\x18\x04 \x01(\x11\x12\x0c\n\x04hour\x18\x05 \x01(\x11\x12\x0e\n\x06minute\x18\x06 \x01(\x11"C\n\x1dReadCurrentTemperatureRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"E\n\x1eReadCurrentTemperatureResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0btemperature\x18\x02 \x01(\x01">\n\x18GetExtCalLastTempRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"@\n\x19GetExtCalLastTempResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0btemperature\x18\x02 \x01(\x01"F\n GetSelfCalLastDateAndTimeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"{\n!GetSelfCalLastDateAndTimeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04year\x18\x02 \x01(\x11\x12\r\n\x05month\x18\x03 \x01(\x11\x12\x0b\n\x03day\x18\x04 \x01(\x11\x12\x0c\n\x04hour\x18\x05 \x01(\x11\x12\x0e\n\x06minute\x18\x06 \x01(\x11"?\n\x19GetSelfCalLastTempRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"A\n\x1aGetSelfCalLastTempResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0btemperature\x18\x02 \x01(\x01"\xe1\x01\n(GetLCRCompensationLastDateAndTimeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12@\n\x11compensation_type\x18\x03 \x01(\x0e2#.nidcpower_grpc.LCRCompensationTypeH\x00\x12\x1f\n\x15compensation_type_raw\x18\x04 \x01(\x11H\x00B\x18\n\x16compensation_type_enum"\x83\x01\n)GetLCRCompensationLastDateAndTimeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04year\x18\x02 \x01(\x11\x12\r\n\x05month\x18\x03 \x01(\x11\x12\x0b\n\x03day\x18\x04 \x01(\x11\x12\x0c\n\x04hour\x18\x05 \x01(\x11\x12\x0e\n\x06minute\x18\x06 \x01(\x11"\xb3\x01\n\'ConfigureDigitalEdgeStartTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x16\n\x0einput_terminal\x18\x02 \x01(\t\x12+\n\x04edge\x18\x03 \x01(\x0e2\x1b.nidcpower_grpc.DigitalEdgeH\x00\x12\x12\n\x08edge_raw\x18\x04 \x01(\x11H\x00B\x0b\n\tedge_enum":\n(ConfigureDigitalEdgeStartTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"N\n(ConfigureSoftwareEdgeStartTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session";\n)ConfigureSoftwareEdgeStartTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"@\n\x1aDisableStartTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"-\n\x1bDisableStartTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xbd\x01\n1ConfigureDigitalEdgeSequenceAdvanceTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x16\n\x0einput_terminal\x18\x02 \x01(\t\x12+\n\x04edge\x18\x03 \x01(\x0e2\x1b.nidcpower_grpc.DigitalEdgeH\x00\x12\x12\n\x08edge_raw\x18\x04 \x01(\x11H\x00B\x0b\n\tedge_enum"D\n2ConfigureDigitalEdgeSequenceAdvanceTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"X\n2ConfigureSoftwareEdgeSequenceAdvanceTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"E\n3ConfigureSoftwareEdgeSequenceAdvanceTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"J\n$DisableSequenceAdvanceTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"7\n%DisableSequenceAdvanceTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb4\x01\n(ConfigureDigitalEdgeSourceTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x16\n\x0einput_terminal\x18\x02 \x01(\t\x12+\n\x04edge\x18\x03 \x01(\x0e2\x1b.nidcpower_grpc.DigitalEdgeH\x00\x12\x12\n\x08edge_raw\x18\x04 \x01(\x11H\x00B\x0b\n\tedge_enum";\n)ConfigureDigitalEdgeSourceTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"O\n)ConfigureSoftwareEdgeSourceTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"<\n*ConfigureSoftwareEdgeSourceTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"A\n\x1bDisableSourceTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session".\n\x1cDisableSourceTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb5\x01\n)ConfigureDigitalEdgeMeasureTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x16\n\x0einput_terminal\x18\x02 \x01(\t\x12+\n\x04edge\x18\x03 \x01(\x0e2\x1b.nidcpower_grpc.DigitalEdgeH\x00\x12\x12\n\x08edge_raw\x18\x04 \x01(\x11H\x00B\x0b\n\tedge_enum"<\n*ConfigureDigitalEdgeMeasureTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"P\n*ConfigureSoftwareEdgeMeasureTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"=\n+ConfigureSoftwareEdgeMeasureTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb3\x01\n\'ConfigureDigitalEdgePulseTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x16\n\x0einput_terminal\x18\x02 \x01(\t\x12+\n\x04edge\x18\x03 \x01(\x0e2\x1b.nidcpower_grpc.DigitalEdgeH\x00\x12\x12\n\x08edge_raw\x18\x04 \x01(\x11H\x00B\x0b\n\tedge_enum":\n(ConfigureDigitalEdgePulseTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"N\n(ConfigureSoftwareEdgePulseTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session";\n)ConfigureSoftwareEdgePulseTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"@\n\x1aDisablePulseTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"-\n\x1bDisablePulseTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xc2\x01\n\x13ExportSignalRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12.\n\x06signal\x18\x02 \x01(\x0e2\x1c.nidcpower_grpc.ExportSignalH\x00\x12\x14\n\nsignal_raw\x18\x03 \x01(\x11H\x00\x12\x19\n\x11signal_identifier\x18\x04 \x01(\t\x12\x17\n\x0foutput_terminal\x18\x05 \x01(\tB\r\n\x0bsignal_enum"&\n\x14ExportSignalResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xab\x01\n\x1eSendSoftwareEdgeTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12>\n\x07trigger\x18\x02 \x01(\x0e2+.nidcpower_grpc.SendSoftwareEdgeTriggerTypeH\x00\x12\x15\n\x0btrigger_raw\x18\x03 \x01(\x11H\x00B\x0e\n\x0ctrigger_enum"1\n\x1fSendSoftwareEdgeTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x9e\x01\n\x13WaitForEventRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12)\n\x08event_id\x18\x02 \x01(\x0e2\x15.nidcpower_grpc.EventH\x00\x12\x16\n\x0cevent_id_raw\x18\x03 \x01(\x11H\x00\x12\x0f\n\x07timeout\x18\x04 \x01(\x01B\x0f\n\revent_id_enum"&\n\x14WaitForEventResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"4\n\x0eDisableRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"!\n\x0fDisableResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"2\n\x0cResetRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\x1f\n\rResetResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"8\n\x12ResetDeviceRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"%\n\x13ResetDeviceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"5\n\x0fSelfTestRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"W\n\x10SelfTestResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x18\n\x10self_test_result\x18\x02 \x01(\x11\x12\x19\n\x11self_test_message\x18\x03 \x01(\t":\n\x14RevisionQueryRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"f\n\x15RevisionQueryResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12"\n\x1ainstrument_driver_revision\x18\x02 \x01(\t\x12\x19\n\x11firmware_revision\x18\x03 \x01(\t">\n\x18ResetWithDefaultsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"+\n\x19ResetWithDefaultsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"J\n\x15GetChannelNameRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\r\n\x05index\x18\x02 \x01(\x11">\n\x16GetChannelNameResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t"T\n\x1fGetChannelNameFromStringRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\r\n\x05index\x18\x02 \x01(\t"H\n GetChannelNameFromStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t"B\n\x1cGetNextCoercionRecordRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"H\n\x1dGetNextCoercionRecordResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fcoercion_record\x18\x02 \x01(\t"E\n\x1fClearInterchangeWarningsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"2\n ClearInterchangeWarningsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"B\n\x1cResetInterchangeCheckRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"/\n\x1dResetInterchangeCheckResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"F\n GetNextInterchangeWarningRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"P\n!GetNextInterchangeWarningResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1b\n\x13interchange_warning\x18\x02 \x01(\t"5\n\x0fGetErrorRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"E\n\x10GetErrorResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04code\x18\x02 \x01(\x11\x12\x13\n\x0bdescription\x18\x03 \x01(\t"7\n\x11ClearErrorRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"$\n\x12ClearErrorResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"M\n\x13ErrorMessageRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x12\n\nerror_code\x18\x02 \x01(\x11"=\n\x14ErrorMessageResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rerror_message\x18\x02 \x01(\t"\x91\x02\n\x1aSetAttributeViInt32Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x128\n\x0cattribute_id\x18\x03 \x01(\x0e2".nidcpower_grpc.NiDCPowerAttribute\x12H\n\x0fattribute_value\x18\x04 \x01(\x0e2-.nidcpower_grpc.NiDCPowerInt32AttributeValuesH\x00\x12\x1d\n\x13attribute_value_raw\x18\x05 \x01(\x11H\x00B\x16\n\x14attribute_value_enum"-\n\x1bSetAttributeViInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xad\x01\n\x1aSetAttributeViInt64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x128\n\x0cattribute_id\x18\x03 \x01(\x0e2".nidcpower_grpc.NiDCPowerAttribute\x12\x1b\n\x13attribute_value_raw\x18\x04 \x01(\x03"-\n\x1bSetAttributeViInt64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x93\x02\n\x1bSetAttributeViReal64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x128\n\x0cattribute_id\x18\x03 \x01(\x0e2".nidcpower_grpc.NiDCPowerAttribute\x12I\n\x0fattribute_value\x18\x04 \x01(\x0e2..nidcpower_grpc.NiDCPowerReal64AttributeValuesH\x00\x12\x1d\n\x13attribute_value_raw\x18\x05 \x01(\x01H\x00B\x16\n\x14attribute_value_enum".\n\x1cSetAttributeViReal64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xae\x01\n\x1bSetAttributeViStringRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x128\n\x0cattribute_id\x18\x03 \x01(\x0e2".nidcpower_grpc.NiDCPowerAttribute\x12\x1b\n\x13attribute_value_raw\x18\x04 \x01(\t".\n\x1cSetAttributeViStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xc3\x01\n\x1cSetAttributeViSessionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x128\n\x0cattribute_id\x18\x03 \x01(\x0e2".nidcpower_grpc.NiDCPowerAttribute\x12/\n\x0fattribute_value\x18\x04 \x01(\x0b2\x16.nidevice_grpc.Session"/\n\x1dSetAttributeViSessionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xab\x01\n\x1cSetAttributeViBooleanRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x128\n\x0cattribute_id\x18\x03 \x01(\x0e2".nidcpower_grpc.NiDCPowerAttribute\x12\x17\n\x0fattribute_value\x18\x04 \x01(\x08"/\n\x1dSetAttributeViBooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x90\x01\n\x1aGetAttributeViInt32Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x128\n\x0cattribute_id\x18\x03 \x01(\x0e2".nidcpower_grpc.NiDCPowerAttribute"F\n\x1bGetAttributeViInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fattribute_value\x18\x02 \x01(\x11"\x90\x01\n\x1aGetAttributeViInt64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x128\n\x0cattribute_id\x18\x03 \x01(\x0e2".nidcpower_grpc.NiDCPowerAttribute"F\n\x1bGetAttributeViInt64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fattribute_value\x18\x02 \x01(\x03"\x91\x01\n\x1bGetAttributeViReal64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x128\n\x0cattribute_id\x18\x03 \x01(\x0e2".nidcpower_grpc.NiDCPowerAttribute"G\n\x1cGetAttributeViReal64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fattribute_value\x18\x02 \x01(\x01"\x91\x01\n\x1bGetAttributeViStringRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x128\n\x0cattribute_id\x18\x03 \x01(\x0e2".nidcpower_grpc.NiDCPowerAttribute"G\n\x1cGetAttributeViStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fattribute_value\x18\x02 \x01(\t"\x92\x01\n\x1cGetAttributeViSessionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x128\n\x0cattribute_id\x18\x03 \x01(\x0e2".nidcpower_grpc.NiDCPowerAttribute"`\n\x1dGetAttributeViSessionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12/\n\x0fattribute_value\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session"\x92\x01\n\x1cGetAttributeViBooleanRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x128\n\x0cattribute_id\x18\x03 \x01(\x0e2".nidcpower_grpc.NiDCPowerAttribute"H\n\x1dGetAttributeViBooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fattribute_value\x18\x02 \x01(\x08"`\n\'ImportAttributeConfigurationFileRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tfile_path\x18\x02 \x01(\t":\n(ImportAttributeConfigurationFileResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"`\n\'ExportAttributeConfigurationFileRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tfile_path\x18\x02 \x01(\t":\n(ExportAttributeConfigurationFileResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"f\n)ImportAttributeConfigurationBufferRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rconfiguration\x18\x02 \x01(\x0c"<\n*ImportAttributeConfigurationBufferResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"O\n)ExportAttributeConfigurationBufferRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"S\n*ExportAttributeConfigurationBufferResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rconfiguration\x18\x02 \x01(\x0c"}\n!PerformLCROpenCompensationRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x1e\n\x16additional_frequencies\x18\x03 \x03(\x01"4\n"PerformLCROpenCompensationResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"~\n"PerformLCRShortCompensationRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x1e\n\x16additional_frequencies\x18\x03 \x03(\x01"5\n#PerformLCRShortCompensationResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa4\x01\n!PerformLCRLoadCompensationRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12E\n\x12compensation_spots\x18\x03 \x03(\x0b2).nidcpower_grpc.NILCRLoadCompensationSpot"4\n"PerformLCRLoadCompensationResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"v\n\x1fConfigureLCRCompensationRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x19\n\x11compensation_data\x18\x03 \x01(\x0c"2\n ConfigureLCRCompensationResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"h\n,PerformLCROpenCustomCableCompensationRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t"?\n-PerformLCROpenCustomCableCompensationResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"i\n-PerformLCRShortCustomCableCompensationRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t"@\n.PerformLCRShortCustomCableCompensationResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"Y\n\x1dGetLCRCompensationDataRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t"K\n\x1eGetLCRCompensationDataResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x19\n\x11compensation_data\x18\x02 \x01(\x0c"\xcc\x01\n(InitializeWithIndependentChannelsRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\r\n\x05reset\x18\x03 \x01(\x08\x12\x15\n\roption_string\x18\x04 \x01(\t\x12M\n\x17initialization_behavior\x18\x05 \x01(\x0e2,.nidevice_grpc.SessionInitializationBehavior"\x9b\x01\n)InitializeWithIndependentChannelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12"\n\x02vi\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x19\n\rerror_message\x18\x03 \x01(\tB\x02\x18\x01\x12\x1f\n\x17new_session_initialized\x18\x04 \x01(\x08"\xc4\x01\n&ConfigureSourceModeWithChannelsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x121\n\x0bsource_mode\x18\x03 \x01(\x0e2\x1a.nidcpower_grpc.SourceModeH\x00\x12\x19\n\x0fsource_mode_raw\x18\x04 \x01(\x11H\x00B\x12\n\x10source_mode_enum"9\n\'ConfigureSourceModeWithChannelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb3\x01\n)CreateAdvancedSequenceWithChannelsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x15\n\rsequence_name\x18\x03 \x01(\t\x12\x15\n\rattribute_ids\x18\x04 \x03(\x11\x12\x1e\n\x16set_as_active_sequence\x18\x05 \x01(\x08"<\n*CreateAdvancedSequenceWithChannelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x85\x01\n-CreateAdvancedSequenceStepWithChannelsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x1a\n\x12set_as_active_step\x18\x03 \x01(\x08"@\n.CreateAdvancedSequenceStepWithChannelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x8b\x01\n3CreateAdvancedSequenceCommitStepWithChannelsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x1a\n\x12set_as_active_step\x18\x03 \x01(\x08"F\n4CreateAdvancedSequenceCommitStepWithChannelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"|\n)DeleteAdvancedSequenceWithChannelsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x15\n\rsequence_name\x18\x03 \x01(\t"<\n*DeleteAdvancedSequenceWithChannelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"U\n\x19CommitWithChannelsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t",\n\x1aCommitWithChannelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"W\n\x1bInitiateWithChannelsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t".\n\x1cInitiateWithChannelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"T\n\x18AbortWithChannelsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t"+\n\x19AbortWithChannelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xd5\x01\n3ConfigureDigitalEdgeStartTriggerWithChannelsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x16\n\x0einput_terminal\x18\x03 \x01(\t\x12+\n\x04edge\x18\x04 \x01(\x0e2\x1b.nidcpower_grpc.DigitalEdgeH\x00\x12\x12\n\x08edge_raw\x18\x05 \x01(\x11H\x00B\x0b\n\tedge_enum"F\n4ConfigureDigitalEdgeStartTriggerWithChannelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"p\n4ConfigureSoftwareEdgeStartTriggerWithChannelsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t"G\n5ConfigureSoftwareEdgeStartTriggerWithChannelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"b\n&DisableStartTriggerWithChannelsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t"9\n\'DisableStartTriggerWithChannelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xdf\x01\n=ConfigureDigitalEdgeSequenceAdvanceTriggerWithChannelsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x16\n\x0einput_terminal\x18\x03 \x01(\t\x12+\n\x04edge\x18\x04 \x01(\x0e2\x1b.nidcpower_grpc.DigitalEdgeH\x00\x12\x12\n\x08edge_raw\x18\x05 \x01(\x11H\x00B\x0b\n\tedge_enum"P\n>ConfigureDigitalEdgeSequenceAdvanceTriggerWithChannelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"z\n>ConfigureSoftwareEdgeSequenceAdvanceTriggerWithChannelsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t"Q\n?ConfigureSoftwareEdgeSequenceAdvanceTriggerWithChannelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"l\n0DisableSequenceAdvanceTriggerWithChannelsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t"C\n1DisableSequenceAdvanceTriggerWithChannelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xd6\x01\n4ConfigureDigitalEdgeSourceTriggerWithChannelsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x16\n\x0einput_terminal\x18\x03 \x01(\t\x12+\n\x04edge\x18\x04 \x01(\x0e2\x1b.nidcpower_grpc.DigitalEdgeH\x00\x12\x12\n\x08edge_raw\x18\x05 \x01(\x11H\x00B\x0b\n\tedge_enum"G\n5ConfigureDigitalEdgeSourceTriggerWithChannelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"q\n5ConfigureSoftwareEdgeSourceTriggerWithChannelsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t"H\n6ConfigureSoftwareEdgeSourceTriggerWithChannelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"c\n\'DisableSourceTriggerWithChannelsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t":\n(DisableSourceTriggerWithChannelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xd7\x01\n5ConfigureDigitalEdgeMeasureTriggerWithChannelsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x16\n\x0einput_terminal\x18\x03 \x01(\t\x12+\n\x04edge\x18\x04 \x01(\x0e2\x1b.nidcpower_grpc.DigitalEdgeH\x00\x12\x12\n\x08edge_raw\x18\x05 \x01(\x11H\x00B\x0b\n\tedge_enum"H\n6ConfigureDigitalEdgeMeasureTriggerWithChannelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"r\n6ConfigureSoftwareEdgeMeasureTriggerWithChannelsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t"I\n7ConfigureSoftwareEdgeMeasureTriggerWithChannelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xd5\x01\n3ConfigureDigitalEdgePulseTriggerWithChannelsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x16\n\x0einput_terminal\x18\x03 \x01(\t\x12+\n\x04edge\x18\x04 \x01(\x0e2\x1b.nidcpower_grpc.DigitalEdgeH\x00\x12\x12\n\x08edge_raw\x18\x05 \x01(\x11H\x00B\x0b\n\tedge_enum"F\n4ConfigureDigitalEdgePulseTriggerWithChannelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"p\n4ConfigureSoftwareEdgePulseTriggerWithChannelsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t"G\n5ConfigureSoftwareEdgePulseTriggerWithChannelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"b\n&DisablePulseTriggerWithChannelsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t"9\n\'DisablePulseTriggerWithChannelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xd8\x01\n6ConfigureDigitalEdgeShutdownTriggerWithChannelsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x16\n\x0einput_terminal\x18\x03 \x01(\t\x12+\n\x04edge\x18\x04 \x01(\x0e2\x1b.nidcpower_grpc.DigitalEdgeH\x00\x12\x12\n\x08edge_raw\x18\x05 \x01(\x11H\x00B\x0b\n\tedge_enum"I\n7ConfigureDigitalEdgeShutdownTriggerWithChannelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"s\n7ConfigureSoftwareEdgeShutdownTriggerWithChannelsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t"J\n8ConfigureSoftwareEdgeShutdownTriggerWithChannelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"e\n)DisableShutdownTriggerWithChannelsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t"<\n*DisableShutdownTriggerWithChannelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xe4\x01\n\x1fExportSignalWithChannelsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12.\n\x06signal\x18\x03 \x01(\x0e2\x1c.nidcpower_grpc.ExportSignalH\x00\x12\x14\n\nsignal_raw\x18\x04 \x01(\x11H\x00\x12\x19\n\x11signal_identifier\x18\x05 \x01(\t\x12\x17\n\x0foutput_terminal\x18\x06 \x01(\tB\r\n\x0bsignal_enum"2\n ExportSignalWithChannelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xcd\x01\n*SendSoftwareEdgeTriggerWithChannelsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12>\n\x07trigger\x18\x03 \x01(\x0e2+.nidcpower_grpc.SendSoftwareEdgeTriggerTypeH\x00\x12\x15\n\x0btrigger_raw\x18\x04 \x01(\x11H\x00B\x0e\n\x0ctrigger_enum"=\n+SendSoftwareEdgeTriggerWithChannelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xc0\x01\n\x1fWaitForEventWithChannelsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12)\n\x08event_id\x18\x03 \x01(\x0e2\x15.nidcpower_grpc.EventH\x00\x12\x16\n\x0cevent_id_raw\x18\x04 \x01(\x11H\x00\x12\x0f\n\x07timeout\x18\x05 \x01(\x01B\x0f\n\revent_id_enum"2\n WaitForEventWithChannelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"T\n\x18ResetWithChannelsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t"+\n\x19ResetWithChannelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"D\n\x1eInvalidateAllAttributesRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"1\n\x1fInvalidateAllAttributesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"o\n\x13ConfigureOvpRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12\x0f\n\x07enabled\x18\x03 \x01(\x08\x12\r\n\x05limit\x18\x04 \x01(\x01"&\n\x14ConfigureOvpResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"7\n\x11ErrorQueryRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"O\n\x12ErrorQueryResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nerror_code\x18\x02 \x01(\x11\x12\x15\n\rerror_message\x18\x03 \x01(\t"d\n(GetLCRCustomCableCompensationDataRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t"c\n)GetLCRCustomCableCompensationDataResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12&\n\x1ecustom_cable_compensation_data\x18\x02 \x01(\x0c"\x8e\x01\n*ConfigureLCRCustomCableCompensationRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12&\n\x1ecustom_cable_compensation_data\x18\x03 \x01(\x0c"=\n+ConfigureLCRCustomCableCompensationResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05*\xc2e\n\x12NiDCPowerAttribute\x12#\n\x1fNIDCPOWER_ATTRIBUTE_UNSPECIFIED\x10\x00\x12%\n\x1fNIDCPOWER_ATTRIBUTE_RANGE_CHECK\x10\x92\x8b@\x121\n+NIDCPOWER_ATTRIBUTE_QUERY_INSTRUMENT_STATUS\x10\x93\x8b@\x12\x1f\n\x19NIDCPOWER_ATTRIBUTE_CACHE\x10\x94\x8b@\x12"\n\x1cNIDCPOWER_ATTRIBUTE_SIMULATE\x10\x95\x8b@\x12*\n$NIDCPOWER_ATTRIBUTE_RECORD_COERCIONS\x10\x96\x8b@\x12+\n%NIDCPOWER_ATTRIBUTE_INTERCHANGE_CHECK\x10\xa5\x8b@\x12\'\n!NIDCPOWER_ATTRIBUTE_CHANNEL_COUNT\x10\xdb\x8c@\x120\n*NIDCPOWER_ATTRIBUTE_SPECIFIC_DRIVER_PREFIX\x10\xbe\x8d@\x125\n/NIDCPOWER_ATTRIBUTE_SUPPORTED_INSTRUMENT_MODELS\x10\xd7\x8d@\x12,\n&NIDCPOWER_ATTRIBUTE_GROUP_CAPABILITIES\x10\xa1\x8e@\x121\n+NIDCPOWER_ATTRIBUTE_INSTRUMENT_MANUFACTURER\x10\x8f\x8f@\x12*\n$NIDCPOWER_ATTRIBUTE_INSTRUMENT_MODEL\x10\x90\x8f@\x126\n0NIDCPOWER_ATTRIBUTE_INSTRUMENT_FIRMWARE_REVISION\x10\x8e\x8f@\x122\n,NIDCPOWER_ATTRIBUTE_SPECIFIC_DRIVER_REVISION\x10\xb7\x8f@\x120\n*NIDCPOWER_ATTRIBUTE_SPECIFIC_DRIVER_VENDOR\x10\x91\x8f@\x125\n/NIDCPOWER_ATTRIBUTE_SPECIFIC_DRIVER_DESCRIPTION\x10\x92\x8f@\x12B\n<NIDCPOWER_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION\x10\x93\x8f@\x12B\n<NIDCPOWER_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION\x10\x94\x8f@\x12\'\n!NIDCPOWER_ATTRIBUTE_SERIAL_NUMBER\x10\xc8\x99F\x12&\n NIDCPOWER_ATTRIBUTE_LOGICAL_NAME\x10\xc1\x8d@\x120\n*NIDCPOWER_ATTRIBUTE_IO_RESOURCE_DESCRIPTOR\x10\xc0\x8d@\x12&\n NIDCPOWER_ATTRIBUTE_DRIVER_SETUP\x10\x97\x8b@\x12%\n\x1fNIDCPOWER_ATTRIBUTE_SOURCE_MODE\x10\xe6\x98F\x12)\n#NIDCPOWER_ATTRIBUTE_OUTPUT_FUNCTION\x10\xb8\x98F\x12(\n"NIDCPOWER_ATTRIBUTE_OUTPUT_ENABLED\x10\xd6\xa5L\x12*\n$NIDCPOWER_ATTRIBUTE_OUTPUT_CONNECTED\x10\xec\x98F\x12+\n%NIDCPOWER_ATTRIBUTE_OUTPUT_RESISTANCE\x10\xed\x98F\x12,\n&NIDCPOWER_ATTRIBUTE_TRANSIENT_RESPONSE\x10\xee\x98F\x120\n*NIDCPOWER_ATTRIBUTE_VOLTAGE_GAIN_BANDWIDTH\x10\xf3\x98F\x128\n2NIDCPOWER_ATTRIBUTE_VOLTAGE_COMPENSATION_FREQUENCY\x10\xf4\x98F\x121\n+NIDCPOWER_ATTRIBUTE_VOLTAGE_POLE_ZERO_RATIO\x10\xf5\x98F\x120\n*NIDCPOWER_ATTRIBUTE_CURRENT_GAIN_BANDWIDTH\x10\xf6\x98F\x128\n2NIDCPOWER_ATTRIBUTE_CURRENT_COMPENSATION_FREQUENCY\x10\xf7\x98F\x121\n+NIDCPOWER_ATTRIBUTE_CURRENT_POLE_ZERO_RATIO\x10\xf8\x98F\x12<\n6NIDCPOWER_ATTRIBUTE_CONSTANT_RESISTANCE_GAIN_BANDWIDTH\x10\xa0\x9bF\x12D\n>NIDCPOWER_ATTRIBUTE_CONSTANT_RESISTANCE_COMPENSATION_FREQUENCY\x10\x9e\x9bF\x12=\n7NIDCPOWER_ATTRIBUTE_CONSTANT_RESISTANCE_POLE_ZERO_RATIO\x10\xa3\x9bF\x127\n1NIDCPOWER_ATTRIBUTE_CONSTANT_POWER_GAIN_BANDWIDTH\x10\x9a\x9bF\x12?\n9NIDCPOWER_ATTRIBUTE_CONSTANT_POWER_COMPENSATION_FREQUENCY\x10\x98\x9bF\x128\n2NIDCPOWER_ATTRIBUTE_CONSTANT_POWER_POLE_ZERO_RATIO\x10\x9d\x9bF\x12\'\n!NIDCPOWER_ATTRIBUTE_VOLTAGE_LEVEL\x10\xd1\xa5L\x12\'\n!NIDCPOWER_ATTRIBUTE_CURRENT_LIMIT\x10\xd5\xa5L\x12-\n\'NIDCPOWER_ATTRIBUTE_VOLTAGE_LEVEL_RANGE\x10\xb5\x98F\x12-\n\'NIDCPOWER_ATTRIBUTE_CURRENT_LIMIT_RANGE\x10\xb4\x98F\x120\n*NIDCPOWER_ATTRIBUTE_CURRENT_LIMIT_BEHAVIOR\x10\xd4\xa5L\x121\n+NIDCPOWER_ATTRIBUTE_VOLTAGE_LEVEL_AUTORANGE\x10\xbf\x98F\x121\n+NIDCPOWER_ATTRIBUTE_CURRENT_LIMIT_AUTORANGE\x10\xc0\x98F\x12,\n&NIDCPOWER_ATTRIBUTE_CURRENT_LIMIT_HIGH\x10\xeb\x99F\x12+\n%NIDCPOWER_ATTRIBUTE_CURRENT_LIMIT_LOW\x10\xec\x99F\x12\'\n!NIDCPOWER_ATTRIBUTE_CURRENT_LEVEL\x10\xb9\x98F\x12\'\n!NIDCPOWER_ATTRIBUTE_VOLTAGE_LIMIT\x10\xba\x98F\x12-\n\'NIDCPOWER_ATTRIBUTE_CURRENT_LEVEL_RANGE\x10\xbb\x98F\x12-\n\'NIDCPOWER_ATTRIBUTE_VOLTAGE_LIMIT_RANGE\x10\xbc\x98F\x121\n+NIDCPOWER_ATTRIBUTE_CURRENT_LEVEL_AUTORANGE\x10\xc1\x98F\x121\n+NIDCPOWER_ATTRIBUTE_VOLTAGE_LIMIT_AUTORANGE\x10\xc2\x98F\x12,\n&NIDCPOWER_ATTRIBUTE_VOLTAGE_LIMIT_HIGH\x10\xe9\x99F\x12+\n%NIDCPOWER_ATTRIBUTE_VOLTAGE_LIMIT_LOW\x10\xea\x99F\x128\n2NIDCPOWER_ATTRIBUTE_CURRENT_LEVEL_RISING_SLEW_RATE\x10\x87\x9bF\x129\n3NIDCPOWER_ATTRIBUTE_CURRENT_LEVEL_FALLING_SLEW_RATE\x10\x88\x9bF\x12-\n\'NIDCPOWER_ATTRIBUTE_PULSE_VOLTAGE_LEVEL\x10\x80\x99F\x12-\n\'NIDCPOWER_ATTRIBUTE_PULSE_CURRENT_LIMIT\x10\x81\x99F\x122\n,NIDCPOWER_ATTRIBUTE_PULSE_BIAS_VOLTAGE_LEVEL\x10\x82\x99F\x122\n,NIDCPOWER_ATTRIBUTE_PULSE_BIAS_CURRENT_LIMIT\x10\x83\x99F\x123\n-NIDCPOWER_ATTRIBUTE_PULSE_VOLTAGE_LEVEL_RANGE\x10\x84\x99F\x123\n-NIDCPOWER_ATTRIBUTE_PULSE_CURRENT_LIMIT_RANGE\x10\x85\x99F\x122\n,NIDCPOWER_ATTRIBUTE_PULSE_CURRENT_LIMIT_HIGH\x10\xf1\x99F\x121\n+NIDCPOWER_ATTRIBUTE_PULSE_CURRENT_LIMIT_LOW\x10\xf2\x99F\x127\n1NIDCPOWER_ATTRIBUTE_PULSE_BIAS_CURRENT_LIMIT_HIGH\x10\xf3\x99F\x126\n0NIDCPOWER_ATTRIBUTE_PULSE_BIAS_CURRENT_LIMIT_LOW\x10\xf4\x99F\x12-\n\'NIDCPOWER_ATTRIBUTE_PULSE_CURRENT_LEVEL\x10\x86\x99F\x12-\n\'NIDCPOWER_ATTRIBUTE_PULSE_VOLTAGE_LIMIT\x10\x87\x99F\x122\n,NIDCPOWER_ATTRIBUTE_PULSE_BIAS_CURRENT_LEVEL\x10\x88\x99F\x122\n,NIDCPOWER_ATTRIBUTE_PULSE_BIAS_VOLTAGE_LIMIT\x10\x89\x99F\x123\n-NIDCPOWER_ATTRIBUTE_PULSE_CURRENT_LEVEL_RANGE\x10\x8a\x99F\x123\n-NIDCPOWER_ATTRIBUTE_PULSE_VOLTAGE_LIMIT_RANGE\x10\x8b\x99F\x122\n,NIDCPOWER_ATTRIBUTE_PULSE_VOLTAGE_LIMIT_HIGH\x10\xed\x99F\x121\n+NIDCPOWER_ATTRIBUTE_PULSE_VOLTAGE_LIMIT_LOW\x10\xee\x99F\x127\n1NIDCPOWER_ATTRIBUTE_PULSE_BIAS_VOLTAGE_LIMIT_HIGH\x10\xef\x99F\x126\n0NIDCPOWER_ATTRIBUTE_PULSE_BIAS_VOLTAGE_LIMIT_LOW\x10\xf0\x99F\x123\n-NIDCPOWER_ATTRIBUTE_CONSTANT_RESISTANCE_LEVEL\x10\xa1\x9bF\x129\n3NIDCPOWER_ATTRIBUTE_CONSTANT_RESISTANCE_LEVEL_RANGE\x10\xa2\x9bF\x12;\n5NIDCPOWER_ATTRIBUTE_CONSTANT_RESISTANCE_CURRENT_LIMIT\x10\x9f\x9bF\x12.\n(NIDCPOWER_ATTRIBUTE_CONSTANT_POWER_LEVEL\x10\x9b\x9bF\x124\n.NIDCPOWER_ATTRIBUTE_CONSTANT_POWER_LEVEL_RANGE\x10\x9c\x9bF\x126\n0NIDCPOWER_ATTRIBUTE_CONSTANT_POWER_CURRENT_LIMIT\x10\x99\x9bF\x12&\n NIDCPOWER_ATTRIBUTE_SOURCE_DELAY\x10\xe3\x98F\x12-\n\'NIDCPOWER_ATTRIBUTE_OVERRANGING_ENABLED\x10\xb7\x98F\x12,\n&NIDCPOWER_ATTRIBUTE_OUTPUT_CAPACITANCE\x10\xbe\x98F\x12-\n\'NIDCPOWER_ATTRIBUTE_SEQUENCE_LOOP_COUNT\x10\xc9\x98F\x127\n1NIDCPOWER_ATTRIBUTE_SEQUENCE_LOOP_COUNT_IS_FINITE\x10\xfe\x98F\x123\n-NIDCPOWER_ATTRIBUTE_COMPLIANCE_LIMIT_SYMMETRY\x10\xe8\x99F\x122\n,NIDCPOWER_ATTRIBUTE_SEQUENCE_STEP_DELTA_TIME\x10\xf6\x99F\x12:\n4NIDCPOWER_ATTRIBUTE_SEQUENCE_STEP_DELTA_TIME_ENABLED\x10\xf7\x99F\x121\n+NIDCPOWER_ATTRIBUTE_ACTUAL_POWER_ALLOCATION\x10\xfd\x99F\x124\n.NIDCPOWER_ATTRIBUTE_REQUESTED_POWER_ALLOCATION\x10\xfe\x99F\x12/\n)NIDCPOWER_ATTRIBUTE_POWER_ALLOCATION_MODE\x10\xff\x99F\x12)\n#NIDCPOWER_ATTRIBUTE_MERGED_CHANNELS\x10\xa9\x9aF\x121\n+NIDCPOWER_ATTRIBUTE_CONDUCTION_VOLTAGE_MODE\x10\x8e\x9bF\x129\n3NIDCPOWER_ATTRIBUTE_CONDUCTION_VOLTAGE_ON_THRESHOLD\x10\x8f\x9bF\x12:\n4NIDCPOWER_ATTRIBUTE_CONDUCTION_VOLTAGE_OFF_THRESHOLD\x10\x90\x9bF\x12(\n"NIDCPOWER_ATTRIBUTE_OUTPUT_SHORTED\x10\xa4\x9bF\x12*\n$NIDCPOWER_ATTRIBUTE_PULSE_BIAS_DELAY\x10\x8c\x99F\x12\'\n!NIDCPOWER_ATTRIBUTE_PULSE_ON_TIME\x10\x8d\x99F\x12(\n"NIDCPOWER_ATTRIBUTE_PULSE_OFF_TIME\x10\x8e\x99F\x12%\n\x1fNIDCPOWER_ATTRIBUTE_OVP_ENABLED\x10\xd2\xa5L\x12#\n\x1dNIDCPOWER_ATTRIBUTE_OVP_LIMIT\x10\xd3\xa5L\x12\x1f\n\x19NIDCPOWER_ATTRIBUTE_SENSE\x10\xbd\x98F\x12#\n\x1dNIDCPOWER_ATTRIBUTE_AUTO_ZERO\x10\xe7\x98F\x12\'\n!NIDCPOWER_ATTRIBUTE_APERTURE_TIME\x10\xea\x98F\x12-\n\'NIDCPOWER_ATTRIBUTE_APERTURE_TIME_UNITS\x10\xeb\x98F\x12.\n(NIDCPOWER_ATTRIBUTE_POWER_LINE_FREQUENCY\x10\xc4\x98F\x12,\n&NIDCPOWER_ATTRIBUTE_SAMPLES_TO_AVERAGE\x10\xb3\x98F\x12\'\n!NIDCPOWER_ATTRIBUTE_FETCH_BACKLOG\x10\xe8\x98F\x121\n+NIDCPOWER_ATTRIBUTE_APERTURE_TIME_AUTO_MODE\x10\xea\x9aF\x12#\n\x1dNIDCPOWER_ATTRIBUTE_AUTORANGE\x10\xa4\x9aF\x12&\n NIDCPOWER_ATTRIBUTE_MEASURE_WHEN\x10\xe9\x98F\x12:\n4NIDCPOWER_ATTRIBUTE_RESET_AVERAGE_BEFORE_MEASUREMENT\x10\xb6\x98F\x12/\n)NIDCPOWER_ATTRIBUTE_MEASURE_RECORD_LENGTH\x10\xef\x98F\x129\n3NIDCPOWER_ATTRIBUTE_MEASURE_RECORD_LENGTH_IS_FINITE\x10\xf0\x98F\x123\n-NIDCPOWER_ATTRIBUTE_MEASURE_RECORD_DELTA_TIME\x10\xf1\x98F\x12,\n&NIDCPOWER_ATTRIBUTE_DC_NOISE_REJECTION\x10\xf2\x98F\x126\n0NIDCPOWER_ATTRIBUTE_SELF_CALIBRATION_PERSISTENCE\x10\xf9\x98F\x12-\n\'NIDCPOWER_ATTRIBUTE_MEASURE_BUFFER_SIZE\x10\xfd\x98F\x12,\n&NIDCPOWER_ATTRIBUTE_AUTORANGE_BEHAVIOR\x10\xa5\x9aF\x126\n0NIDCPOWER_ATTRIBUTE_AUTORANGE_APERTURE_TIME_MODE\x10\xa6\x9aF\x129\n3NIDCPOWER_ATTRIBUTE_AUTORANGE_MINIMUM_APERTURE_TIME\x10\xa7\x9aF\x12?\n9NIDCPOWER_ATTRIBUTE_AUTORANGE_MINIMUM_APERTURE_TIME_UNITS\x10\xa8\x9aF\x129\n3NIDCPOWER_ATTRIBUTE_AUTORANGE_MINIMUM_CURRENT_RANGE\x10\xaf\x9aF\x129\n3NIDCPOWER_ATTRIBUTE_AUTORANGE_MINIMUM_VOLTAGE_RANGE\x10\xb0\x9aF\x122\n,NIDCPOWER_ATTRIBUTE_AUTORANGE_THRESHOLD_MODE\x10\xb1\x9aF\x12D\n>NIDCPOWER_ATTRIBUTE_AUTORANGE_MAXIMUM_DELAY_AFTER_RANGE_CHANGE\x10\xf2\x9aF\x12,\n&NIDCPOWER_ATTRIBUTE_START_TRIGGER_TYPE\x10\xc5\x98F\x129\n3NIDCPOWER_ATTRIBUTE_DIGITAL_EDGE_START_TRIGGER_EDGE\x10\xc6\x98F\x12C\n=NIDCPOWER_ATTRIBUTE_DIGITAL_EDGE_START_TRIGGER_INPUT_TERMINAL\x10\xc7\x98F\x12@\n:NIDCPOWER_ATTRIBUTE_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL\x10\xc8\x98F\x12-\n\'NIDCPOWER_ATTRIBUTE_SOURCE_TRIGGER_TYPE\x10\xce\x98F\x12:\n4NIDCPOWER_ATTRIBUTE_DIGITAL_EDGE_SOURCE_TRIGGER_EDGE\x10\xcf\x98F\x12D\n>NIDCPOWER_ATTRIBUTE_DIGITAL_EDGE_SOURCE_TRIGGER_INPUT_TERMINAL\x10\xd0\x98F\x12A\n;NIDCPOWER_ATTRIBUTE_EXPORTED_SOURCE_TRIGGER_OUTPUT_TERMINAL\x10\xd1\x98F\x12.\n(NIDCPOWER_ATTRIBUTE_MEASURE_TRIGGER_TYPE\x10\xd2\x98F\x12;\n5NIDCPOWER_ATTRIBUTE_DIGITAL_EDGE_MEASURE_TRIGGER_EDGE\x10\xd3\x98F\x12E\n?NIDCPOWER_ATTRIBUTE_DIGITAL_EDGE_MEASURE_TRIGGER_INPUT_TERMINAL\x10\xd4\x98F\x12B\n<NIDCPOWER_ATTRIBUTE_EXPORTED_MEASURE_TRIGGER_OUTPUT_TERMINAL\x10\xd5\x98F\x127\n1NIDCPOWER_ATTRIBUTE_SEQUENCE_ADVANCE_TRIGGER_TYPE\x10\xca\x98F\x12D\n>NIDCPOWER_ATTRIBUTE_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_EDGE\x10\xcb\x98F\x12N\nHNIDCPOWER_ATTRIBUTE_DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_INPUT_TERMINAL\x10\xcc\x98F\x12K\nENIDCPOWER_ATTRIBUTE_EXPORTED_SEQUENCE_ADVANCE_TRIGGER_OUTPUT_TERMINAL\x10\xcd\x98F\x12?\n9NIDCPOWER_ATTRIBUTE_SOURCE_COMPLETE_EVENT_OUTPUT_TERMINAL\x10\xdb\x98F\x12>\n8NIDCPOWER_ATTRIBUTE_SOURCE_COMPLETE_EVENT_PULSE_POLARITY\x10\xd9\x98F\x12;\n5NIDCPOWER_ATTRIBUTE_SOURCE_COMPLETE_EVENT_PULSE_WIDTH\x10\xda\x98F\x12@\n:NIDCPOWER_ATTRIBUTE_MEASURE_COMPLETE_EVENT_OUTPUT_TERMINAL\x10\xdf\x98F\x126\n0NIDCPOWER_ATTRIBUTE_MEASURE_COMPLETE_EVENT_DELAY\x10\xde\x98F\x12?\n9NIDCPOWER_ATTRIBUTE_MEASURE_COMPLETE_EVENT_PULSE_POLARITY\x10\xdc\x98F\x12<\n6NIDCPOWER_ATTRIBUTE_MEASURE_COMPLETE_EVENT_PULSE_WIDTH\x10\xdd\x98F\x12K\nENIDCPOWER_ATTRIBUTE_SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_TERMINAL\x10\xd8\x98F\x12J\nDNIDCPOWER_ATTRIBUTE_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_POLARITY\x10\xd6\x98F\x12G\nANIDCPOWER_ATTRIBUTE_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_WIDTH\x10\xd7\x98F\x12D\n>NIDCPOWER_ATTRIBUTE_SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_TERMINAL\x10\xe2\x98F\x12C\n=NIDCPOWER_ATTRIBUTE_SEQUENCE_ENGINE_DONE_EVENT_PULSE_POLARITY\x10\xe0\x98F\x12@\n:NIDCPOWER_ATTRIBUTE_SEQUENCE_ENGINE_DONE_EVENT_PULSE_WIDTH\x10\xe1\x98F\x122\n,NIDCPOWER_ATTRIBUTE_ACTIVE_ADVANCED_SEQUENCE\x10\xfa\x98F\x127\n1NIDCPOWER_ATTRIBUTE_ACTIVE_ADVANCED_SEQUENCE_STEP\x10\xfb\x98F\x12,\n&NIDCPOWER_ATTRIBUTE_PULSE_TRIGGER_TYPE\x10\x8f\x99F\x129\n3NIDCPOWER_ATTRIBUTE_DIGITAL_EDGE_PULSE_TRIGGER_EDGE\x10\x90\x99F\x12C\n=NIDCPOWER_ATTRIBUTE_DIGITAL_EDGE_PULSE_TRIGGER_INPUT_TERMINAL\x10\x91\x99F\x12@\n:NIDCPOWER_ATTRIBUTE_EXPORTED_PULSE_TRIGGER_OUTPUT_TERMINAL\x10\x92\x99F\x12>\n8NIDCPOWER_ATTRIBUTE_PULSE_COMPLETE_EVENT_OUTPUT_TERMINAL\x10\x93\x99F\x12=\n7NIDCPOWER_ATTRIBUTE_PULSE_COMPLETE_EVENT_PULSE_POLARITY\x10\x94\x99F\x12:\n4NIDCPOWER_ATTRIBUTE_PULSE_COMPLETE_EVENT_PULSE_WIDTH\x10\x95\x99F\x12G\nANIDCPOWER_ATTRIBUTE_READY_FOR_PULSE_TRIGGER_EVENT_OUTPUT_TERMINAL\x10\x96\x99F\x12F\n@NIDCPOWER_ATTRIBUTE_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_POLARITY\x10\x97\x99F\x12C\n=NIDCPOWER_ATTRIBUTE_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_WIDTH\x10\x98\x99F\x12/\n)NIDCPOWER_ATTRIBUTE_SHUTDOWN_TRIGGER_TYPE\x10\xc3\x9aF\x12<\n6NIDCPOWER_ATTRIBUTE_DIGITAL_EDGE_SHUTDOWN_TRIGGER_EDGE\x10\xc4\x9aF\x12F\n@NIDCPOWER_ATTRIBUTE_DIGITAL_EDGE_SHUTDOWN_TRIGGER_INPUT_TERMINAL\x10\xc5\x9aF\x12.\n(NIDCPOWER_ATTRIBUTE_INTERLOCK_INPUT_OPEN\x10\x99\x99F\x12&\n NIDCPOWER_ATTRIBUTE_POWER_SOURCE\x10\xb0\x98F\x12-\n\'NIDCPOWER_ATTRIBUTE_POWER_SOURCE_IN_USE\x10\xb1\x98F\x12:\n4NIDCPOWER_ATTRIBUTE_AUXILIARY_POWER_SOURCE_AVAILABLE\x10\xb2\x98F\x12)\n#NIDCPOWER_ATTRIBUTE_ISOLATION_STATE\x10\xde\x9aF\x12)\n#NIDCPOWER_ATTRIBUTE_INSTRUMENT_MODE\x10\x80\x9aF\x12/\n)NIDCPOWER_ATTRIBUTE_LCR_STIMULUS_FUNCTION\x10\x81\x9aF\x12\'\n!NIDCPOWER_ATTRIBUTE_LCR_FREQUENCY\x10\x82\x9aF\x12/\n)NIDCPOWER_ATTRIBUTE_LCR_VOLTAGE_AMPLITUDE\x10\x83\x9aF\x12/\n)NIDCPOWER_ATTRIBUTE_LCR_CURRENT_AMPLITUDE\x10\x84\x9aF\x12,\n&NIDCPOWER_ATTRIBUTE_LCR_DC_BIAS_SOURCE\x10\x85\x9aF\x123\n-NIDCPOWER_ATTRIBUTE_LCR_DC_BIAS_VOLTAGE_LEVEL\x10\x86\x9aF\x123\n-NIDCPOWER_ATTRIBUTE_LCR_DC_BIAS_CURRENT_LEVEL\x10\x87\x9aF\x122\n,NIDCPOWER_ATTRIBUTE_LCR_IMPEDANCE_AUTO_RANGE\x10\x88\x9aF\x12-\n\'NIDCPOWER_ATTRIBUTE_LCR_IMPEDANCE_RANGE\x10\x89\x9aF\x12.\n(NIDCPOWER_ATTRIBUTE_LCR_MEASUREMENT_TIME\x10\x8a\x9aF\x127\n1NIDCPOWER_ATTRIBUTE_LCR_OPEN_COMPENSATION_ENABLED\x10\x8c\x9aF\x128\n2NIDCPOWER_ATTRIBUTE_LCR_SHORT_COMPENSATION_ENABLED\x10\x8d\x9aF\x127\n1NIDCPOWER_ATTRIBUTE_LCR_LOAD_COMPENSATION_ENABLED\x10\x8e\x9aF\x12F\n@NIDCPOWER_ATTRIBUTE_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE\x10\x8f\x9aF\x125\n/NIDCPOWER_ATTRIBUTE_LCR_CUSTOM_MEASUREMENT_TIME\x10\xb2\x9aF\x12.\n(NIDCPOWER_ATTRIBUTE_LCR_OPEN_CONDUCTANCE\x10\xb5\x9aF\x12.\n(NIDCPOWER_ATTRIBUTE_LCR_OPEN_SUSCEPTANCE\x10\xb6\x9aF\x12.\n(NIDCPOWER_ATTRIBUTE_LCR_SHORT_RESISTANCE\x10\xb7\x9aF\x12-\n\'NIDCPOWER_ATTRIBUTE_LCR_SHORT_REACTANCE\x10\xb8\x9aF\x12+\n%NIDCPOWER_ATTRIBUTE_LCR_VOLTAGE_RANGE\x10\xb9\x9aF\x123\n-NIDCPOWER_ATTRIBUTE_LCR_DC_BIAS_VOLTAGE_RANGE\x10\xba\x9aF\x12+\n%NIDCPOWER_ATTRIBUTE_LCR_CURRENT_RANGE\x10\xbb\x9aF\x123\n-NIDCPOWER_ATTRIBUTE_LCR_DC_BIAS_CURRENT_RANGE\x10\xc2\x9aF\x126\n0NIDCPOWER_ATTRIBUTE_LCR_MEASURED_LOAD_RESISTANCE\x10\xbc\x9aF\x125\n/NIDCPOWER_ATTRIBUTE_LCR_MEASURED_LOAD_REACTANCE\x10\xbd\x9aF\x124\n.NIDCPOWER_ATTRIBUTE_LCR_ACTUAL_LOAD_RESISTANCE\x10\xbe\x9aF\x123\n-NIDCPOWER_ATTRIBUTE_LCR_ACTUAL_LOAD_REACTANCE\x10\xbf\x9aF\x12&\n NIDCPOWER_ATTRIBUTE_CABLE_LENGTH\x10\xc6\x9aF\x125\n/NIDCPOWER_ATTRIBUTE_LCR_AUTOMATIC_LEVEL_CONTROL\x10\xd2\x9aF\x12=\n7NIDCPOWER_ATTRIBUTE_LCR_DC_BIAS_AUTOMATIC_LEVEL_CONTROL\x10\xd3\x9aF\x12E\n?NIDCPOWER_ATTRIBUTE_LCR_SHORT_CUSTOM_CABLE_COMPENSATION_ENABLED\x10\xdb\x9aF\x12>\n8NIDCPOWER_ATTRIBUTE_LCR_AC_ELECTRICAL_CABLE_LENGTH_DELAY\x10\xe5\x9aF\x12/\n)NIDCPOWER_ATTRIBUTE_LCR_SOURCE_DELAY_MODE\x10\xeb\x9aF\x12-\n\'NIDCPOWER_ATTRIBUTE_LCR_LOAD_RESISTANCE\x10\xee\x9aF\x12-\n\'NIDCPOWER_ATTRIBUTE_LCR_LOAD_INDUCTANCE\x10\xef\x9aF\x12.\n(NIDCPOWER_ATTRIBUTE_LCR_LOAD_CAPACITANCE\x10\xf0\x9aF\x124\n.NIDCPOWER_ATTRIBUTE_LCR_IMPEDANCE_RANGE_SOURCE\x10\xf1\x9aF\x128\n2NIDCPOWER_ATTRIBUTE_LCR_DC_BIAS_TRANSIENT_RESPONSE\x10\x8b\x9bF\x12/\n)NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_ENABLED\x10\x9b\x9aF\x12A\n;NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_HIGH\x10\x9c\x9aF\x12B\n<NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_HIGH\x10\x9d\x9aF\x12@\n:NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_LOW\x10\x9e\x9aF\x12@\n:NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_LOW\x10\x9f\x9aF\x12A\n;NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_CURRENT_OVERRANGE_ENABLED\x10\xa0\x9aF\x12@\n:NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_LOW\x10\xd4\x9aF\x12A\n;NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_LOW\x10\xd5\x9aF\x12A\n;NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_HIGH\x10\xd6\x9aF\x12A\n;NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_HIGH\x10\xd7\x9aF\x12-\n\'NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_DELAY\x10\xdc\x9aF\x12B\n<NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_VOLTAGE_MEASURE_LIMIT_HIGH\x10\x95\x9bF\x12A\n;NIDCPOWER_ATTRIBUTE_OUTPUT_CUTOFF_VOLTAGE_MEASURE_LIMIT_LOW\x10\x96\x9bF\x12/\n)NIDCPOWER_ATTRIBUTE_LCR_AC_DITHER_ENABLED\x10\x8c\x9bF\x122\n,NIDCPOWER_ATTRIBUTE_LCR_SOURCE_APERTURE_TIME\x10\x8d\x9bF\x12.\n(NIDCPOWER_ATTRIBUTE_OCP_ERROR_PERCENTAGE\x10\xf8\x99F\x12,\n&NIDCPOWER_ATTRIBUTE_SUPPORT_OUTPUT_DMA\x10\xff\x98F\x127\n1NIDCPOWER_ATTRIBUTE_INSTRUMENT_API_SESSION_HANDLE\x10\x9e\x99F\x12=\n7NIDCPOWER_ATTRIBUTE_ACTUAL_VOLTAGE_RANGE_FOR_LAST_FETCH\x10\xb3\x9aF\x12=\n7NIDCPOWER_ATTRIBUTE_ACTUAL_CURRENT_RANGE_FOR_LAST_FETCH\x10\xb4\x9aF\x12T\nNNIDCPOWER_ATTRIBUTE_WAS_SESSION_OPENED_BY_INITIALIZE_WITH_INDEPENDENT_CHANNELS\x10\x9f\x99F*\x88\x01\n\x14CurrentLimitBehavior\x129\n5CURRENT_LIMIT_BEHAVIOR_NIDCPOWER_VAL_CURRENT_REGULATE\x10\x00\x125\n1CURRENT_LIMIT_BEHAVIOR_NIDCPOWER_VAL_CURRENT_TRIP\x10\x01*\xd1\x02\n\x0cOutputStates\x127\n3OUTPUT_STATES_NIDCPOWER_VAL_OUTPUT_CONSTANT_VOLTAGE\x10\x00\x127\n3OUTPUT_STATES_NIDCPOWER_VAL_OUTPUT_CONSTANT_CURRENT\x10\x01\x123\n/OUTPUT_STATES_NIDCPOWER_VAL_OUTPUT_OVER_VOLTAGE\x10\x02\x123\n/OUTPUT_STATES_NIDCPOWER_VAL_OUTPUT_OVER_CURRENT\x10\x03\x122\n.OUTPUT_STATES_NIDCPOWER_VAL_OUTPUT_UNREGULATED\x10\x04\x121\n,OUTPUT_STATES_NIDCPOWER_VAL_OUTPUT_INHIBITED\x10\x8b\t*|\n\x10MeasurementTypes\x123\n/MEASUREMENT_TYPES_NIDCPOWER_VAL_MEASURE_CURRENT\x10\x00\x123\n/MEASUREMENT_TYPES_NIDCPOWER_VAL_MEASURE_VOLTAGE\x10\x01*\xde\x02\n\x0eOutputFunction\x12\x1f\n\x1bOUTPUT_FUNCTION_UNSPECIFIED\x10\x00\x12-\n(OUTPUT_FUNCTION_NIDCPOWER_VAL_DC_VOLTAGE\x10\xee\x07\x12-\n(OUTPUT_FUNCTION_NIDCPOWER_VAL_DC_CURRENT\x10\xef\x07\x120\n+OUTPUT_FUNCTION_NIDCPOWER_VAL_PULSE_VOLTAGE\x10\x99\x08\x120\n+OUTPUT_FUNCTION_NIDCPOWER_VAL_PULSE_CURRENT\x10\x9a\x08\x126\n1OUTPUT_FUNCTION_NIDCPOWER_VAL_CONSTANT_RESISTANCE\x10\x89\t\x121\n,OUTPUT_FUNCTION_NIDCPOWER_VAL_CONSTANT_POWER\x10\x8a\t*_\n\x05Sense\x12\x15\n\x11SENSE_UNSPECIFIED\x10\x00\x12\x1e\n\x19SENSE_NIDCPOWER_VAL_LOCAL\x10\xf0\x07\x12\x1f\n\x1aSENSE_NIDCPOWER_VAL_REMOTE\x10\xf1\x07*|\n\x0bDigitalEdge\x12\x1c\n\x18DIGITAL_EDGE_UNSPECIFIED\x10\x00\x12&\n!DIGITAL_EDGE_NIDCPOWER_VAL_RISING\x10\xf8\x07\x12\'\n"DIGITAL_EDGE_NIDCPOWER_VAL_FALLING\x10\xf9\x07*\x7f\n\nSourceMode\x12\x1b\n\x17SOURCE_MODE_UNSPECIFIED\x10\x00\x12+\n&SOURCE_MODE_NIDCPOWER_VAL_SINGLE_POINT\x10\xfc\x07\x12\'\n"SOURCE_MODE_NIDCPOWER_VAL_SEQUENCE\x10\xfd\x07*n\n\x08AutoZero\x12\x1f\n\x1bAUTO_ZERO_NIDCPOWER_VAL_OFF\x10\x00\x12!\n\x1cAUTO_ZERO_NIDCPOWER_VAL_ONCE\x10\x80\x08\x12\x1e\n\x1aAUTO_ZERO_NIDCPOWER_VAL_ON\x10\x01*\xa4\x01\n\x14PowerLineFrequencies\x12&\n"POWER_LINE_FREQUENCIES_UNSPECIFIED\x10\x00\x121\n-POWER_LINE_FREQUENCIES_NIDCPOWER_VAL_50_HERTZ\x102\x121\n-POWER_LINE_FREQUENCIES_NIDCPOWER_VAL_60_HERTZ\x10<*\xa2\x01\n\x11ApertureTimeUnits\x12#\n\x1fAPERTURE_TIME_UNITS_UNSPECIFIED\x10\x00\x12.\n)APERTURE_TIME_UNITS_NIDCPOWER_VAL_SECONDS\x10\x84\x08\x128\n3APERTURE_TIME_UNITS_NIDCPOWER_VAL_POWER_LINE_CYCLES\x10\x85\x08*\xc7\x05\n\x0cExportSignal\x12\x1d\n\x19EXPORT_SIGNAL_UNSPECIFIED\x10\x00\x126\n1EXPORT_SIGNAL_NIDCPOWER_VAL_SOURCE_COMPLETE_EVENT\x10\x86\x08\x127\n2EXPORT_SIGNAL_NIDCPOWER_VAL_MEASURE_COMPLETE_EVENT\x10\x87\x08\x12B\n=EXPORT_SIGNAL_NIDCPOWER_VAL_SEQUENCE_ITERATION_COMPLETE_EVENT\x10\x88\x08\x12;\n6EXPORT_SIGNAL_NIDCPOWER_VAL_SEQUENCE_ENGINE_DONE_EVENT\x10\x89\x08\x125\n0EXPORT_SIGNAL_NIDCPOWER_VAL_PULSE_COMPLETE_EVENT\x10\x9b\x08\x12>\n9EXPORT_SIGNAL_NIDCPOWER_VAL_READY_FOR_PULSE_TRIGGER_EVENT\x10\x9c\x08\x12.\n)EXPORT_SIGNAL_NIDCPOWER_VAL_START_TRIGGER\x10\x8a\x08\x12/\n*EXPORT_SIGNAL_NIDCPOWER_VAL_SOURCE_TRIGGER\x10\x8b\x08\x120\n+EXPORT_SIGNAL_NIDCPOWER_VAL_MEASURE_TRIGGER\x10\x8c\x08\x129\n4EXPORT_SIGNAL_NIDCPOWER_VAL_SEQUENCE_ADVANCE_TRIGGER\x10\x8d\x08\x12.\n)EXPORT_SIGNAL_NIDCPOWER_VAL_PULSE_TRIGGER\x10\x9d\x08\x121\n,EXPORT_SIGNAL_NIDCPOWER_VAL_SHUTDOWN_TRIGGER\x10\xde\x08*\x81\n\n\x12OutputCutoffReason\x12$\n OUTPUT_CUTOFF_REASON_UNSPECIFIED\x10\x00\x12H\n;OUTPUT_CUTOFF_REASON_NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_ALL\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12O\nKOUTPUT_CUTOFF_REASON_NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_OUTPUT_HIGH\x10\x01\x12N\nJOUTPUT_CUTOFF_REASON_NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_OUTPUT_LOW\x10\x02\x12P\nLOUTPUT_CUTOFF_REASON_NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_MEASURE_HIGH\x10\x04\x12O\nKOUTPUT_CUTOFF_REASON_NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_MEASURE_LOW\x10\x08\x12O\nKOUTPUT_CUTOFF_REASON_NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_CHANGE_HIGH\x10\x10\x12N\nJOUTPUT_CUTOFF_REASON_NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_CHANGE_LOW\x10 \x12O\nKOUTPUT_CUTOFF_REASON_NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_CHANGE_HIGH\x10@\x12O\nJOUTPUT_CUTOFF_REASON_NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_CHANGE_LOW\x10\x80\x01\x12N\nIOUTPUT_CUTOFF_REASON_NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_SATURATED\x10\x80\x02\x12N\nIOUTPUT_CUTOFF_REASON_NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_SATURATED\x10\x80\x04\x12Q\nLOUTPUT_CUTOFF_REASON_NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_MEASURE_HIGH\x10\x80\x08\x12P\nKOUTPUT_CUTOFF_REASON_NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_MEASURE_LOW\x10\x80\x10\x12W\nROUTPUT_CUTOFF_REASON_NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_SELF_TEST_MEASUREMENT_HIGH\x10\x80 \x12V\nQOUTPUT_CUTOFF_REASON_NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_SELF_TEST_MEASUREMENT_LOW\x10\x80@*\x84\x03\n\x13LCRCompensationType\x12%\n!LCR_COMPENSATION_TYPE_UNSPECIFIED\x10\x00\x12:\n5LCR_COMPENSATION_TYPE_NIDCPOWER_VAL_OPEN_COMPENSATION\x10\xea\x08\x12;\n6LCR_COMPENSATION_TYPE_NIDCPOWER_VAL_SHORT_COMPENSATION\x10\xeb\x08\x12:\n5LCR_COMPENSATION_TYPE_NIDCPOWER_VAL_LOAD_COMPENSATION\x10\xec\x08\x12G\nBLCR_COMPENSATION_TYPE_NIDCPOWER_VAL_OPEN_CUSTOM_CABLE_COMPENSATION\x10\xed\x08\x12H\nCLCR_COMPENSATION_TYPE_NIDCPOWER_VAL_SHORT_CUSTOM_CABLE_COMPENSATION\x10\xee\x08*\xb3\x02\n\x05Event\x12\x15\n\x11EVENT_UNSPECIFIED\x10\x00\x12(\n#EVENT_NIDCPOWER_VAL_SOURCE_COMPLETE\x10\x86\x08\x12)\n$EVENT_NIDCPOWER_VAL_MEASURE_COMPLETE\x10\x87\x08\x124\n/EVENT_NIDCPOWER_VAL_SEQUENCE_ITERATION_COMPLETE\x10\x88\x08\x12-\n(EVENT_NIDCPOWER_VAL_SEQUENCE_ENGINE_DONE\x10\x89\x08\x12\'\n"EVENT_NIDCPOWER_VAL_PULSE_COMPLETE\x10\x9b\x08\x120\n+EVENT_NIDCPOWER_VAL_READY_FOR_PULSE_TRIGGER\x10\x9c\x08*\xbb\x03\n\x1bSendSoftwareEdgeTriggerType\x12/\n+SEND_SOFTWARE_EDGE_TRIGGER_TYPE_UNSPECIFIED\x10\x00\x128\n3SEND_SOFTWARE_EDGE_TRIGGER_TYPE_NIDCPOWER_VAL_START\x10\x8a\x08\x129\n4SEND_SOFTWARE_EDGE_TRIGGER_TYPE_NIDCPOWER_VAL_SOURCE\x10\x8b\x08\x12:\n5SEND_SOFTWARE_EDGE_TRIGGER_TYPE_NIDCPOWER_VAL_MEASURE\x10\x8c\x08\x12C\n>SEND_SOFTWARE_EDGE_TRIGGER_TYPE_NIDCPOWER_VAL_SEQUENCE_ADVANCE\x10\x8d\x08\x128\n3SEND_SOFTWARE_EDGE_TRIGGER_TYPE_NIDCPOWER_VAL_PULSE\x10\x9d\x08\x12;\n6SEND_SOFTWARE_EDGE_TRIGGER_TYPE_NIDCPOWER_VAL_SHUTDOWN\x10\xde\x08*\x8e1\n\x1dNiDCPowerInt32AttributeValues\x12\x1f\n\x1bNIDCPOWER_INT32_UNSPECIFIED\x10\x00\x12L\nGNIDCPOWER_INT32_APERTURE_TIME_AUTO_MODE_VAL_APERTURE_TIME_AUTO_MODE_OFF\x10\xef\x08\x12N\nINIDCPOWER_INT32_APERTURE_TIME_AUTO_MODE_VAL_APERTURE_TIME_AUTO_MODE_SHORT\x10\xf0\x08\x12O\nJNIDCPOWER_INT32_APERTURE_TIME_AUTO_MODE_VAL_APERTURE_TIME_AUTO_MODE_NORMAL\x10\xf1\x08\x12M\nHNIDCPOWER_INT32_APERTURE_TIME_AUTO_MODE_VAL_APERTURE_TIME_AUTO_MODE_LONG\x10\xf2\x08\x124\n/NIDCPOWER_INT32_APERTURE_TIME_UNITS_VAL_SECONDS\x10\x84\x08\x12>\n9NIDCPOWER_INT32_APERTURE_TIME_UNITS_VAL_POWER_LINE_CYCLES\x10\x85\x08\x12%\n!NIDCPOWER_INT32_AUTO_ZERO_VAL_OFF\x10\x00\x12\'\n"NIDCPOWER_INT32_AUTO_ZERO_VAL_ONCE\x10\x80\x08\x12$\n NIDCPOWER_INT32_AUTO_ZERO_VAL_ON\x10\x01\x12H\nCNIDCPOWER_INT32_AUTORANGE_APERTURE_TIME_MODE_VAL_APERTURE_TIME_AUTO\x10\xd6\x08\x12J\nENIDCPOWER_INT32_AUTORANGE_APERTURE_TIME_MODE_VAL_APERTURE_TIME_CUSTOM\x10\xd7\x08\x12G\nBNIDCPOWER_INT32_AUTORANGE_BEHAVIOR_VAL_RANGE_UP_TO_LIMIT_THEN_DOWN\x10\xd3\x08\x124\n/NIDCPOWER_INT32_AUTORANGE_BEHAVIOR_VAL_RANGE_UP\x10\xd4\x08\x12=\n8NIDCPOWER_INT32_AUTORANGE_BEHAVIOR_VAL_RANGE_UP_AND_DOWN\x10\xd5\x08\x12G\nBNIDCPOWER_INT32_AUTORANGE_THRESHOLD_MODE_VAL_THRESHOLD_MODE_NORMAL\x10\xd8\x08\x12J\nENIDCPOWER_INT32_AUTORANGE_THRESHOLD_MODE_VAL_THRESHOLD_MODE_FAST_STEP\x10\xd9\x08\x12P\nKNIDCPOWER_INT32_AUTORANGE_THRESHOLD_MODE_VAL_THRESHOLD_MODE_HIGH_HYSTERESIS\x10\xda\x08\x12R\nMNIDCPOWER_INT32_AUTORANGE_THRESHOLD_MODE_VAL_THRESHOLD_MODE_MEDIUM_HYSTERESIS\x10\xdb\x08\x12E\n@NIDCPOWER_INT32_AUTORANGE_THRESHOLD_MODE_VAL_THRESHOLD_MODE_HOLD\x10\xdc\x08\x12,\n\'NIDCPOWER_INT32_CABLE_LENGTH_VAL_ZERO_M\x10\xe1\x08\x126\n1NIDCPOWER_INT32_CABLE_LENGTH_VAL_NI_STANDARD_0_5M\x10\x81\t\x124\n/NIDCPOWER_INT32_CABLE_LENGTH_VAL_NI_STANDARD_1M\x10\xe2\x08\x124\n/NIDCPOWER_INT32_CABLE_LENGTH_VAL_NI_STANDARD_2M\x10\xe3\x08\x124\n/NIDCPOWER_INT32_CABLE_LENGTH_VAL_NI_STANDARD_4M\x10\xe4\x08\x12=\n8NIDCPOWER_INT32_CABLE_LENGTH_VAL_NI_STANDARD_TRIAXIAL_1M\x10\xf3\x08\x12=\n8NIDCPOWER_INT32_CABLE_LENGTH_VAL_NI_STANDARD_TRIAXIAL_2M\x10\xf4\x08\x12=\n8NIDCPOWER_INT32_CABLE_LENGTH_VAL_NI_STANDARD_TRIAXIAL_4M\x10\xf5\x08\x12<\n7NIDCPOWER_INT32_CABLE_LENGTH_VAL_CUSTOM_ONBOARD_STORAGE\x10\xe5\x08\x12:\n5NIDCPOWER_INT32_CABLE_LENGTH_VAL_CUSTOM_AS_CONFIGURED\x10\xe6\x08\x12;\n7NIDCPOWER_INT32_COMPLIANCE_LIMIT_SYMMETRY_VAL_SYMMETRIC\x10\x00\x12<\n8NIDCPOWER_INT32_COMPLIANCE_LIMIT_SYMMETRY_VAL_ASYMMETRIC\x10\x01\x12R\nMNIDCPOWER_INT32_CONDUCTION_VOLTAGE_MODE_VAL_CONDUCTION_VOLTAGE_MODE_AUTOMATIC\x10\x83\t\x12P\nKNIDCPOWER_INT32_CONDUCTION_VOLTAGE_MODE_VAL_CONDUCTION_VOLTAGE_MODE_ENABLED\x10\x84\t\x12Q\nLNIDCPOWER_INT32_CONDUCTION_VOLTAGE_MODE_VAL_CONDUCTION_VOLTAGE_MODE_DISABLED\x10\x85\t\x12?\n;NIDCPOWER_INT32_CURRENT_LIMIT_BEHAVIOR_VAL_CURRENT_REGULATE\x10\x00\x12;\n7NIDCPOWER_INT32_CURRENT_LIMIT_BEHAVIOR_VAL_CURRENT_TRIP\x10\x01\x12K\nFNIDCPOWER_INT32_DC_NOISE_REJECTION_VAL_DC_NOISE_REJECTION_SECOND_ORDER\x10\x93\x08\x12E\n@NIDCPOWER_INT32_DC_NOISE_REJECTION_VAL_DC_NOISE_REJECTION_NORMAL\x10\x94\x08\x12,\n\'NIDCPOWER_INT32_DIGITAL_EDGE_VAL_RISING\x10\xf8\x07\x12-\n(NIDCPOWER_INT32_DIGITAL_EDGE_VAL_FALLING\x10\xf9\x07\x12/\n*NIDCPOWER_INT32_INSTRUMENT_MODE_VAL_SMU_PS\x10\xa5\x08\x12,\n\'NIDCPOWER_INT32_INSTRUMENT_MODE_VAL_LCR\x10\xa6\x08\x12/\n*NIDCPOWER_INT32_INSTRUMENT_MODE_VAL_E_LOAD\x10\x82\t\x121\n,NIDCPOWER_INT32_ISOLATION_STATE_VAL_ISOLATED\x10\xe8\x08\x125\n0NIDCPOWER_INT32_ISOLATION_STATE_VAL_NON_ISOLATED\x10\xe9\x08\x127\n3NIDCPOWER_INT32_LCR_AUTOMATIC_LEVEL_CONTROL_VAL_OFF\x10\x00\x126\n2NIDCPOWER_INT32_LCR_AUTOMATIC_LEVEL_CONTROL_VAL_ON\x10\x01\x126\n1NIDCPOWER_INT32_LCRDC_BIAS_SOURCE_VAL_DC_BIAS_OFF\x10\xa9\x08\x12:\n5NIDCPOWER_INT32_LCRDC_BIAS_SOURCE_VAL_DC_BIAS_VOLTAGE\x10\xaa\x08\x12:\n5NIDCPOWER_INT32_LCRDC_BIAS_SOURCE_VAL_DC_BIAS_CURRENT\x10\xab\x08\x12\\\nWNIDCPOWER_INT32_LCRDC_BIAS_TRANSIENT_RESPONSE_VAL_LCR_DC_BIAS_TRANSIENT_RESPONSE_NORMAL\x10\xff\x08\x12\\\nWNIDCPOWER_INT32_LCRDC_BIAS_TRANSIENT_RESPONSE_VAL_LCR_DC_BIAS_TRANSIENT_RESPONSE_CUSTOM\x10\x80\t\x12@\n;NIDCPOWER_INT32_LCR_IMPEDANCE_AUTO_RANGE_VAL_AUTO_RANGE_OFF\x10\xac\x08\x12?\n:NIDCPOWER_INT32_LCR_IMPEDANCE_AUTO_RANGE_VAL_AUTO_RANGE_ON\x10\xae\x08\x12G\nBNIDCPOWER_INT32_LCR_IMPEDANCE_RANGE_SOURCE_VAL_LCR_IMPEDANCE_RANGE\x10\xf6\x08\x12J\nENIDCPOWER_INT32_LCR_IMPEDANCE_RANGE_SOURCE_VAL_LCR_LOAD_CONFIGURATION\x10\xf7\x08\x12D\n?NIDCPOWER_INT32_LCR_MEASUREMENT_TIME_VAL_MEASUREMENT_TIME_SHORT\x10\xaf\x08\x12E\n@NIDCPOWER_INT32_LCR_MEASUREMENT_TIME_VAL_MEASUREMENT_TIME_MEDIUM\x10\xb0\x08\x12C\n>NIDCPOWER_INT32_LCR_MEASUREMENT_TIME_VAL_MEASUREMENT_TIME_LONG\x10\xb1\x08\x12E\n@NIDCPOWER_INT32_LCR_MEASUREMENT_TIME_VAL_MEASUREMENT_TIME_CUSTOM\x10\xdd\x08\x12U\nPNIDCPOWER_INT32_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE_VAL_ONBOARD_STORAGE\x10\xb2\x08\x12P\nKNIDCPOWER_INT32_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE_VAL_AS_DEFINED\x10\xb3\x08\x12S\nNNIDCPOWER_INT32_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE_VAL_AS_CONFIGURED\x10\xfa\x08\x12N\nINIDCPOWER_INT32_LCR_SOURCE_DELAY_MODE_VAL_LCR_SOURCE_DELAY_MODE_AUTOMATIC\x10\xf8\x08\x12K\nFNIDCPOWER_INT32_LCR_SOURCE_DELAY_MODE_VAL_LCR_SOURCE_DELAY_MODE_MANUAL\x10\xf9\x08\x129\n4NIDCPOWER_INT32_LCR_STIMULUS_FUNCTION_VAL_AC_VOLTAGE\x10\xa7\x08\x129\n4NIDCPOWER_INT32_LCR_STIMULUS_FUNCTION_VAL_AC_CURRENT\x10\xa8\x08\x12I\nDNIDCPOWER_INT32_MEASURE_WHEN_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE\x10\x81\x08\x12/\n*NIDCPOWER_INT32_MEASURE_WHEN_VAL_ON_DEMAND\x10\x82\x08\x128\n3NIDCPOWER_INT32_MEASURE_WHEN_VAL_ON_MEASURE_TRIGGER\x10\x83\x08\x12/\n*NIDCPOWER_INT32_OUTPUT_CAPACITANCE_VAL_LOW\x10\xf2\x07\x120\n+NIDCPOWER_INT32_OUTPUT_CAPACITANCE_VAL_HIGH\x10\xf3\x07\x123\n.NIDCPOWER_INT32_OUTPUT_FUNCTION_VAL_DC_VOLTAGE\x10\xee\x07\x123\n.NIDCPOWER_INT32_OUTPUT_FUNCTION_VAL_DC_CURRENT\x10\xef\x07\x126\n1NIDCPOWER_INT32_OUTPUT_FUNCTION_VAL_PULSE_VOLTAGE\x10\x99\x08\x126\n1NIDCPOWER_INT32_OUTPUT_FUNCTION_VAL_PULSE_CURRENT\x10\x9a\x08\x12<\n7NIDCPOWER_INT32_OUTPUT_FUNCTION_VAL_CONSTANT_RESISTANCE\x10\x89\t\x127\n2NIDCPOWER_INT32_OUTPUT_FUNCTION_VAL_CONSTANT_POWER\x10\x8a\t\x12-\n(NIDCPOWER_INT32_POLARITY_VAL_ACTIVE_HIGH\x10\xfa\x07\x12,\n\'NIDCPOWER_INT32_POLARITY_VAL_ACTIVE_LOW\x10\xfb\x07\x127\n2NIDCPOWER_INT32_POWER_ALLOCATION_MODE_VAL_DISABLED\x10\xa2\x08\x128\n3NIDCPOWER_INT32_POWER_ALLOCATION_MODE_VAL_AUTOMATIC\x10\xa3\x08\x125\n0NIDCPOWER_INT32_POWER_ALLOCATION_MODE_VAL_MANUAL\x10\xa4\x08\x12.\n)NIDCPOWER_INT32_POWER_SOURCE_VAL_INTERNAL\x10\xeb\x07\x12/\n*NIDCPOWER_INT32_POWER_SOURCE_VAL_AUXILIARY\x10\xec\x07\x12/\n*NIDCPOWER_INT32_POWER_SOURCE_VAL_AUTOMATIC\x10\xed\x07\x125\n0NIDCPOWER_INT32_POWER_SOURCE_IN_USE_VAL_INTERNAL\x10\xeb\x07\x126\n1NIDCPOWER_INT32_POWER_SOURCE_IN_USE_VAL_AUXILIARY\x10\xec\x07\x12D\n?NIDCPOWER_INT32_SELF_CALIBRATION_PERSISTENCE_VAL_KEEP_IN_MEMORY\x10\x95\x08\x12E\n@NIDCPOWER_INT32_SELF_CALIBRATION_PERSISTENCE_VAL_WRITE_TO_EEPROM\x10\x96\x08\x12$\n\x1fNIDCPOWER_INT32_SENSE_VAL_LOCAL\x10\xf0\x07\x12%\n NIDCPOWER_INT32_SENSE_VAL_REMOTE\x10\xf1\x07\x121\n,NIDCPOWER_INT32_SOURCE_MODE_VAL_SINGLE_POINT\x10\xfc\x07\x12-\n(NIDCPOWER_INT32_SOURCE_MODE_VAL_SEQUENCE\x10\xfd\x07\x122\n-NIDCPOWER_INT32_TRANSIENT_RESPONSE_VAL_NORMAL\x10\x8e\x08\x120\n+NIDCPOWER_INT32_TRANSIENT_RESPONSE_VAL_FAST\x10\x8f\x08\x120\n+NIDCPOWER_INT32_TRANSIENT_RESPONSE_VAL_SLOW\x10\x91\x08\x122\n-NIDCPOWER_INT32_TRANSIENT_RESPONSE_VAL_CUSTOM\x10\x92\x08\x12*\n%NIDCPOWER_INT32_TRIGGER_TYPE_VAL_NONE\x10\xf4\x07\x122\n-NIDCPOWER_INT32_TRIGGER_TYPE_VAL_DIGITAL_EDGE\x10\xf6\x07\x123\n.NIDCPOWER_INT32_TRIGGER_TYPE_VAL_SOFTWARE_EDGE\x10\xf7\x07\x1a\x02\x10\x01*\xb6\x01\n\x1eNiDCPowerReal64AttributeValues\x12 \n\x1cNIDCPOWER_REAL64_UNSPECIFIED\x10\x00\x128\n4NIDCPOWER_REAL64_POWER_LINE_FREQUENCIES_VAL_50_HERTZ\x102\x128\n4NIDCPOWER_REAL64_POWER_LINE_FREQUENCIES_VAL_60_HERTZ\x10<2\x97\x97\x01\n\tNiDCPower\x12w\n\x16InitializeWithChannels\x12-.nidcpower_grpc.InitializeWithChannelsRequest\x1a..nidcpower_grpc.InitializeWithChannelsResponse\x12D\n\x05Close\x12\x1c.nidcpower_grpc.CloseRequest\x1a\x1d.nidcpower_grpc.CloseResponse\x12n\n\x13ConfigureSourceMode\x12*.nidcpower_grpc.ConfigureSourceModeRequest\x1a+.nidcpower_grpc.ConfigureSourceModeResponse\x12z\n\x17ConfigureOutputFunction\x12..nidcpower_grpc.ConfigureOutputFunctionRequest\x1a/.nidcpower_grpc.ConfigureOutputFunctionResponse\x12w\n\x16ConfigureOutputEnabled\x12-.nidcpower_grpc.ConfigureOutputEnabledRequest\x1a..nidcpower_grpc.ConfigureOutputEnabledResponse\x12V\n\x0bSetSequence\x12".nidcpower_grpc.SetSequenceRequest\x1a#.nidcpower_grpc.SetSequenceResponse\x12t\n\x15ConfigureVoltageLevel\x12,.nidcpower_grpc.ConfigureVoltageLevelRequest\x1a-.nidcpower_grpc.ConfigureVoltageLevelResponse\x12t\n\x15ConfigureCurrentLimit\x12,.nidcpower_grpc.ConfigureCurrentLimitRequest\x1a-.nidcpower_grpc.ConfigureCurrentLimitResponse\x12\x83\x01\n\x1aConfigureVoltageLevelRange\x121.nidcpower_grpc.ConfigureVoltageLevelRangeRequest\x1a2.nidcpower_grpc.ConfigureVoltageLevelRangeResponse\x12\x83\x01\n\x1aConfigureCurrentLimitRange\x121.nidcpower_grpc.ConfigureCurrentLimitRangeRequest\x1a2.nidcpower_grpc.ConfigureCurrentLimitRangeResponse\x12\x80\x01\n\x19ConfigureOutputResistance\x120.nidcpower_grpc.ConfigureOutputResistanceRequest\x1a1.nidcpower_grpc.ConfigureOutputResistanceResponse\x12t\n\x15ConfigureCurrentLevel\x12,.nidcpower_grpc.ConfigureCurrentLevelRequest\x1a-.nidcpower_grpc.ConfigureCurrentLevelResponse\x12\x83\x01\n\x1aConfigureCurrentLevelRange\x121.nidcpower_grpc.ConfigureCurrentLevelRangeRequest\x1a2.nidcpower_grpc.ConfigureCurrentLevelRangeResponse\x12t\n\x15ConfigureVoltageLimit\x12,.nidcpower_grpc.ConfigureVoltageLimitRequest\x1a-.nidcpower_grpc.ConfigureVoltageLimitResponse\x12\x83\x01\n\x1aConfigureVoltageLimitRange\x121.nidcpower_grpc.ConfigureVoltageLimitRangeRequest\x1a2.nidcpower_grpc.ConfigureVoltageLimitRangeResponse\x12\x83\x01\n\x1aConfigurePulseVoltageLevel\x121.nidcpower_grpc.ConfigurePulseVoltageLevelRequest\x1a2.nidcpower_grpc.ConfigurePulseVoltageLevelResponse\x12\x83\x01\n\x1aConfigurePulseCurrentLimit\x121.nidcpower_grpc.ConfigurePulseCurrentLimitRequest\x1a2.nidcpower_grpc.ConfigurePulseCurrentLimitResponse\x12\x8f\x01\n\x1eConfigurePulseBiasVoltageLevel\x125.nidcpower_grpc.ConfigurePulseBiasVoltageLevelRequest\x1a6.nidcpower_grpc.ConfigurePulseBiasVoltageLevelResponse\x12\x8f\x01\n\x1eConfigurePulseBiasCurrentLimit\x125.nidcpower_grpc.ConfigurePulseBiasCurrentLimitRequest\x1a6.nidcpower_grpc.ConfigurePulseBiasCurrentLimitResponse\x12\x92\x01\n\x1fConfigurePulseVoltageLevelRange\x126.nidcpower_grpc.ConfigurePulseVoltageLevelRangeRequest\x1a7.nidcpower_grpc.ConfigurePulseVoltageLevelRangeResponse\x12\x92\x01\n\x1fConfigurePulseCurrentLimitRange\x126.nidcpower_grpc.ConfigurePulseCurrentLimitRangeRequest\x1a7.nidcpower_grpc.ConfigurePulseCurrentLimitRangeResponse\x12\x83\x01\n\x1aConfigurePulseCurrentLevel\x121.nidcpower_grpc.ConfigurePulseCurrentLevelRequest\x1a2.nidcpower_grpc.ConfigurePulseCurrentLevelResponse\x12\x83\x01\n\x1aConfigurePulseVoltageLimit\x121.nidcpower_grpc.ConfigurePulseVoltageLimitRequest\x1a2.nidcpower_grpc.ConfigurePulseVoltageLimitResponse\x12\x8f\x01\n\x1eConfigurePulseBiasCurrentLevel\x125.nidcpower_grpc.ConfigurePulseBiasCurrentLevelRequest\x1a6.nidcpower_grpc.ConfigurePulseBiasCurrentLevelResponse\x12\x8f\x01\n\x1eConfigurePulseBiasVoltageLimit\x125.nidcpower_grpc.ConfigurePulseBiasVoltageLimitRequest\x1a6.nidcpower_grpc.ConfigurePulseBiasVoltageLimitResponse\x12\x92\x01\n\x1fConfigurePulseCurrentLevelRange\x126.nidcpower_grpc.ConfigurePulseCurrentLevelRangeRequest\x1a7.nidcpower_grpc.ConfigurePulseCurrentLevelRangeResponse\x12\x92\x01\n\x1fConfigurePulseVoltageLimitRange\x126.nidcpower_grpc.ConfigurePulseVoltageLimitRangeRequest\x1a7.nidcpower_grpc.ConfigurePulseVoltageLimitRangeResponse\x12w\n\x16CreateAdvancedSequence\x12-.nidcpower_grpc.CreateAdvancedSequenceRequest\x1a..nidcpower_grpc.CreateAdvancedSequenceResponse\x12\x83\x01\n\x1aCreateAdvancedSequenceStep\x121.nidcpower_grpc.CreateAdvancedSequenceStepRequest\x1a2.nidcpower_grpc.CreateAdvancedSequenceStepResponse\x12w\n\x16DeleteAdvancedSequence\x12-.nidcpower_grpc.DeleteAdvancedSequenceRequest\x1a..nidcpower_grpc.DeleteAdvancedSequenceResponse\x12t\n\x15ConfigureApertureTime\x12,.nidcpower_grpc.ConfigureApertureTimeRequest\x1a-.nidcpower_grpc.ConfigureApertureTimeResponse\x12h\n\x11ConfigureAutoZero\x12(.nidcpower_grpc.ConfigureAutoZeroRequest\x1a).nidcpower_grpc.ConfigureAutoZeroResponse\x12\x86\x01\n\x1bConfigurePowerLineFrequency\x122.nidcpower_grpc.ConfigurePowerLineFrequencyRequest\x1a3.nidcpower_grpc.ConfigurePowerLineFrequencyResponse\x12_\n\x0eConfigureSense\x12%.nidcpower_grpc.ConfigureSenseRequest\x1a&.nidcpower_grpc.ConfigureSenseResponse\x12J\n\x07Measure\x12\x1e.nidcpower_grpc.MeasureRequest\x1a\x1f.nidcpower_grpc.MeasureResponse\x12b\n\x0fMeasureMultiple\x12&.nidcpower_grpc.MeasureMultipleRequest\x1a\'.nidcpower_grpc.MeasureMultipleResponse\x12\\\n\rFetchMultiple\x12$.nidcpower_grpc.FetchMultipleRequest\x1a%.nidcpower_grpc.FetchMultipleResponse\x12k\n\x12MeasureMultipleLCR\x12).nidcpower_grpc.MeasureMultipleLCRRequest\x1a*.nidcpower_grpc.MeasureMultipleLCRResponse\x12e\n\x10FetchMultipleLCR\x12\'.nidcpower_grpc.FetchMultipleLCRRequest\x1a(.nidcpower_grpc.FetchMultipleLCRResponse\x12h\n\x11QueryInCompliance\x12(.nidcpower_grpc.QueryInComplianceRequest\x1a).nidcpower_grpc.QueryInComplianceResponse\x12e\n\x10QueryOutputState\x12\'.nidcpower_grpc.QueryOutputStateRequest\x1a(.nidcpower_grpc.QueryOutputStateResponse\x12\x8c\x01\n\x1dQueryLatchedOutputCutoffState\x124.nidcpower_grpc.QueryLatchedOutputCutoffStateRequest\x1a5.nidcpower_grpc.QueryLatchedOutputCutoffStateResponse\x12\x8c\x01\n\x1dClearLatchedOutputCutoffState\x124.nidcpower_grpc.ClearLatchedOutputCutoffStateRequest\x1a5.nidcpower_grpc.ClearLatchedOutputCutoffStateResponse\x12G\n\x06Commit\x12\x1d.nidcpower_grpc.CommitRequest\x1a\x1e.nidcpower_grpc.CommitResponse\x12M\n\x08Initiate\x12\x1f.nidcpower_grpc.InitiateRequest\x1a .nidcpower_grpc.InitiateResponse\x12D\n\x05Abort\x12\x1c.nidcpower_grpc.AbortRequest\x1a\x1d.nidcpower_grpc.AbortResponse\x12q\n\x14QueryMaxCurrentLimit\x12+.nidcpower_grpc.QueryMaxCurrentLimitRequest\x1a,.nidcpower_grpc.QueryMaxCurrentLimitResponse\x12q\n\x14QueryMaxVoltageLevel\x12+.nidcpower_grpc.QueryMaxVoltageLevelRequest\x1a,.nidcpower_grpc.QueryMaxVoltageLevelResponse\x12q\n\x14QueryMinCurrentLimit\x12+.nidcpower_grpc.QueryMinCurrentLimitRequest\x1a,.nidcpower_grpc.QueryMinCurrentLimitResponse\x12e\n\x10CalSelfCalibrate\x12\'.nidcpower_grpc.CalSelfCalibrateRequest\x1a(.nidcpower_grpc.CalSelfCalibrateResponse\x12\x89\x01\n\x1cGetExtCalRecommendedInterval\x123.nidcpower_grpc.GetExtCalRecommendedIntervalRequest\x1a4.nidcpower_grpc.GetExtCalRecommendedIntervalResponse\x12}\n\x18GetExtCalLastDateAndTime\x12/.nidcpower_grpc.GetExtCalLastDateAndTimeRequest\x1a0.nidcpower_grpc.GetExtCalLastDateAndTimeResponse\x12w\n\x16ReadCurrentTemperature\x12-.nidcpower_grpc.ReadCurrentTemperatureRequest\x1a..nidcpower_grpc.ReadCurrentTemperatureResponse\x12h\n\x11GetExtCalLastTemp\x12(.nidcpower_grpc.GetExtCalLastTempRequest\x1a).nidcpower_grpc.GetExtCalLastTempResponse\x12\x80\x01\n\x19GetSelfCalLastDateAndTime\x120.nidcpower_grpc.GetSelfCalLastDateAndTimeRequest\x1a1.nidcpower_grpc.GetSelfCalLastDateAndTimeResponse\x12k\n\x12GetSelfCalLastTemp\x12).nidcpower_grpc.GetSelfCalLastTempRequest\x1a*.nidcpower_grpc.GetSelfCalLastTempResponse\x12\x98\x01\n!GetLCRCompensationLastDateAndTime\x128.nidcpower_grpc.GetLCRCompensationLastDateAndTimeRequest\x1a9.nidcpower_grpc.GetLCRCompensationLastDateAndTimeResponse\x12\x95\x01\n ConfigureDigitalEdgeStartTrigger\x127.nidcpower_grpc.ConfigureDigitalEdgeStartTriggerRequest\x1a8.nidcpower_grpc.ConfigureDigitalEdgeStartTriggerResponse\x12\x98\x01\n!ConfigureSoftwareEdgeStartTrigger\x128.nidcpower_grpc.ConfigureSoftwareEdgeStartTriggerRequest\x1a9.nidcpower_grpc.ConfigureSoftwareEdgeStartTriggerResponse\x12n\n\x13DisableStartTrigger\x12*.nidcpower_grpc.DisableStartTriggerRequest\x1a+.nidcpower_grpc.DisableStartTriggerResponse\x12\xb3\x01\n*ConfigureDigitalEdgeSequenceAdvanceTrigger\x12A.nidcpower_grpc.ConfigureDigitalEdgeSequenceAdvanceTriggerRequest\x1aB.nidcpower_grpc.ConfigureDigitalEdgeSequenceAdvanceTriggerResponse\x12\xb6\x01\n+ConfigureSoftwareEdgeSequenceAdvanceTrigger\x12B.nidcpower_grpc.ConfigureSoftwareEdgeSequenceAdvanceTriggerRequest\x1aC.nidcpower_grpc.ConfigureSoftwareEdgeSequenceAdvanceTriggerResponse\x12\x8c\x01\n\x1dDisableSequenceAdvanceTrigger\x124.nidcpower_grpc.DisableSequenceAdvanceTriggerRequest\x1a5.nidcpower_grpc.DisableSequenceAdvanceTriggerResponse\x12\x98\x01\n!ConfigureDigitalEdgeSourceTrigger\x128.nidcpower_grpc.ConfigureDigitalEdgeSourceTriggerRequest\x1a9.nidcpower_grpc.ConfigureDigitalEdgeSourceTriggerResponse\x12\x9b\x01\n"ConfigureSoftwareEdgeSourceTrigger\x129.nidcpower_grpc.ConfigureSoftwareEdgeSourceTriggerRequest\x1a:.nidcpower_grpc.ConfigureSoftwareEdgeSourceTriggerResponse\x12q\n\x14DisableSourceTrigger\x12+.nidcpower_grpc.DisableSourceTriggerRequest\x1a,.nidcpower_grpc.DisableSourceTriggerResponse\x12\x9b\x01\n"ConfigureDigitalEdgeMeasureTrigger\x129.nidcpower_grpc.ConfigureDigitalEdgeMeasureTriggerRequest\x1a:.nidcpower_grpc.ConfigureDigitalEdgeMeasureTriggerResponse\x12\x9e\x01\n#ConfigureSoftwareEdgeMeasureTrigger\x12:.nidcpower_grpc.ConfigureSoftwareEdgeMeasureTriggerRequest\x1a;.nidcpower_grpc.ConfigureSoftwareEdgeMeasureTriggerResponse\x12\x95\x01\n ConfigureDigitalEdgePulseTrigger\x127.nidcpower_grpc.ConfigureDigitalEdgePulseTriggerRequest\x1a8.nidcpower_grpc.ConfigureDigitalEdgePulseTriggerResponse\x12\x98\x01\n!ConfigureSoftwareEdgePulseTrigger\x128.nidcpower_grpc.ConfigureSoftwareEdgePulseTriggerRequest\x1a9.nidcpower_grpc.ConfigureSoftwareEdgePulseTriggerResponse\x12n\n\x13DisablePulseTrigger\x12*.nidcpower_grpc.DisablePulseTriggerRequest\x1a+.nidcpower_grpc.DisablePulseTriggerResponse\x12Y\n\x0cExportSignal\x12#.nidcpower_grpc.ExportSignalRequest\x1a$.nidcpower_grpc.ExportSignalResponse\x12z\n\x17SendSoftwareEdgeTrigger\x12..nidcpower_grpc.SendSoftwareEdgeTriggerRequest\x1a/.nidcpower_grpc.SendSoftwareEdgeTriggerResponse\x12Y\n\x0cWaitForEvent\x12#.nidcpower_grpc.WaitForEventRequest\x1a$.nidcpower_grpc.WaitForEventResponse\x12J\n\x07Disable\x12\x1e.nidcpower_grpc.DisableRequest\x1a\x1f.nidcpower_grpc.DisableResponse\x12D\n\x05Reset\x12\x1c.nidcpower_grpc.ResetRequest\x1a\x1d.nidcpower_grpc.ResetResponse\x12V\n\x0bResetDevice\x12".nidcpower_grpc.ResetDeviceRequest\x1a#.nidcpower_grpc.ResetDeviceResponse\x12M\n\x08SelfTest\x12\x1f.nidcpower_grpc.SelfTestRequest\x1a .nidcpower_grpc.SelfTestResponse\x12\\\n\rRevisionQuery\x12$.nidcpower_grpc.RevisionQueryRequest\x1a%.nidcpower_grpc.RevisionQueryResponse\x12h\n\x11ResetWithDefaults\x12(.nidcpower_grpc.ResetWithDefaultsRequest\x1a).nidcpower_grpc.ResetWithDefaultsResponse\x12_\n\x0eGetChannelName\x12%.nidcpower_grpc.GetChannelNameRequest\x1a&.nidcpower_grpc.GetChannelNameResponse\x12}\n\x18GetChannelNameFromString\x12/.nidcpower_grpc.GetChannelNameFromStringRequest\x1a0.nidcpower_grpc.GetChannelNameFromStringResponse\x12t\n\x15GetNextCoercionRecord\x12,.nidcpower_grpc.GetNextCoercionRecordRequest\x1a-.nidcpower_grpc.GetNextCoercionRecordResponse\x12}\n\x18ClearInterchangeWarnings\x12/.nidcpower_grpc.ClearInterchangeWarningsRequest\x1a0.nidcpower_grpc.ClearInterchangeWarningsResponse\x12t\n\x15ResetInterchangeCheck\x12,.nidcpower_grpc.ResetInterchangeCheckRequest\x1a-.nidcpower_grpc.ResetInterchangeCheckResponse\x12\x80\x01\n\x19GetNextInterchangeWarning\x120.nidcpower_grpc.GetNextInterchangeWarningRequest\x1a1.nidcpower_grpc.GetNextInterchangeWarningResponse\x12M\n\x08GetError\x12\x1f.nidcpower_grpc.GetErrorRequest\x1a .nidcpower_grpc.GetErrorResponse\x12S\n\nClearError\x12!.nidcpower_grpc.ClearErrorRequest\x1a".nidcpower_grpc.ClearErrorResponse\x12Y\n\x0cErrorMessage\x12#.nidcpower_grpc.ErrorMessageRequest\x1a$.nidcpower_grpc.ErrorMessageResponse\x12n\n\x13SetAttributeViInt32\x12*.nidcpower_grpc.SetAttributeViInt32Request\x1a+.nidcpower_grpc.SetAttributeViInt32Response\x12n\n\x13SetAttributeViInt64\x12*.nidcpower_grpc.SetAttributeViInt64Request\x1a+.nidcpower_grpc.SetAttributeViInt64Response\x12q\n\x14SetAttributeViReal64\x12+.nidcpower_grpc.SetAttributeViReal64Request\x1a,.nidcpower_grpc.SetAttributeViReal64Response\x12q\n\x14SetAttributeViString\x12+.nidcpower_grpc.SetAttributeViStringRequest\x1a,.nidcpower_grpc.SetAttributeViStringResponse\x12t\n\x15SetAttributeViSession\x12,.nidcpower_grpc.SetAttributeViSessionRequest\x1a-.nidcpower_grpc.SetAttributeViSessionResponse\x12t\n\x15SetAttributeViBoolean\x12,.nidcpower_grpc.SetAttributeViBooleanRequest\x1a-.nidcpower_grpc.SetAttributeViBooleanResponse\x12n\n\x13GetAttributeViInt32\x12*.nidcpower_grpc.GetAttributeViInt32Request\x1a+.nidcpower_grpc.GetAttributeViInt32Response\x12n\n\x13GetAttributeViInt64\x12*.nidcpower_grpc.GetAttributeViInt64Request\x1a+.nidcpower_grpc.GetAttributeViInt64Response\x12q\n\x14GetAttributeViReal64\x12+.nidcpower_grpc.GetAttributeViReal64Request\x1a,.nidcpower_grpc.GetAttributeViReal64Response\x12q\n\x14GetAttributeViString\x12+.nidcpower_grpc.GetAttributeViStringRequest\x1a,.nidcpower_grpc.GetAttributeViStringResponse\x12t\n\x15GetAttributeViSession\x12,.nidcpower_grpc.GetAttributeViSessionRequest\x1a-.nidcpower_grpc.GetAttributeViSessionResponse\x12t\n\x15GetAttributeViBoolean\x12,.nidcpower_grpc.GetAttributeViBooleanRequest\x1a-.nidcpower_grpc.GetAttributeViBooleanResponse\x12\x95\x01\n ImportAttributeConfigurationFile\x127.nidcpower_grpc.ImportAttributeConfigurationFileRequest\x1a8.nidcpower_grpc.ImportAttributeConfigurationFileResponse\x12\x95\x01\n ExportAttributeConfigurationFile\x127.nidcpower_grpc.ExportAttributeConfigurationFileRequest\x1a8.nidcpower_grpc.ExportAttributeConfigurationFileResponse\x12\x9b\x01\n"ImportAttributeConfigurationBuffer\x129.nidcpower_grpc.ImportAttributeConfigurationBufferRequest\x1a:.nidcpower_grpc.ImportAttributeConfigurationBufferResponse\x12\x9b\x01\n"ExportAttributeConfigurationBuffer\x129.nidcpower_grpc.ExportAttributeConfigurationBufferRequest\x1a:.nidcpower_grpc.ExportAttributeConfigurationBufferResponse\x12\x83\x01\n\x1aPerformLCROpenCompensation\x121.nidcpower_grpc.PerformLCROpenCompensationRequest\x1a2.nidcpower_grpc.PerformLCROpenCompensationResponse\x12\x86\x01\n\x1bPerformLCRShortCompensation\x122.nidcpower_grpc.PerformLCRShortCompensationRequest\x1a3.nidcpower_grpc.PerformLCRShortCompensationResponse\x12\x83\x01\n\x1aPerformLCRLoadCompensation\x121.nidcpower_grpc.PerformLCRLoadCompensationRequest\x1a2.nidcpower_grpc.PerformLCRLoadCompensationResponse\x12}\n\x18ConfigureLCRCompensation\x12/.nidcpower_grpc.ConfigureLCRCompensationRequest\x1a0.nidcpower_grpc.ConfigureLCRCompensationResponse\x12\xa4\x01\n%PerformLCROpenCustomCableCompensation\x12<.nidcpower_grpc.PerformLCROpenCustomCableCompensationRequest\x1a=.nidcpower_grpc.PerformLCROpenCustomCableCompensationResponse\x12\xa7\x01\n&PerformLCRShortCustomCableCompensation\x12=.nidcpower_grpc.PerformLCRShortCustomCableCompensationRequest\x1a>.nidcpower_grpc.PerformLCRShortCustomCableCompensationResponse\x12w\n\x16GetLCRCompensationData\x12-.nidcpower_grpc.GetLCRCompensationDataRequest\x1a..nidcpower_grpc.GetLCRCompensationDataResponse\x12\x98\x01\n!InitializeWithIndependentChannels\x128.nidcpower_grpc.InitializeWithIndependentChannelsRequest\x1a9.nidcpower_grpc.InitializeWithIndependentChannelsResponse\x12\x92\x01\n\x1fConfigureSourceModeWithChannels\x126.nidcpower_grpc.ConfigureSourceModeWithChannelsRequest\x1a7.nidcpower_grpc.ConfigureSourceModeWithChannelsResponse\x12\x9b\x01\n"CreateAdvancedSequenceWithChannels\x129.nidcpower_grpc.CreateAdvancedSequenceWithChannelsRequest\x1a:.nidcpower_grpc.CreateAdvancedSequenceWithChannelsResponse\x12\xa7\x01\n&CreateAdvancedSequenceStepWithChannels\x12=.nidcpower_grpc.CreateAdvancedSequenceStepWithChannelsRequest\x1a>.nidcpower_grpc.CreateAdvancedSequenceStepWithChannelsResponse\x12\xb9\x01\n,CreateAdvancedSequenceCommitStepWithChannels\x12C.nidcpower_grpc.CreateAdvancedSequenceCommitStepWithChannelsRequest\x1aD.nidcpower_grpc.CreateAdvancedSequenceCommitStepWithChannelsResponse\x12\x9b\x01\n"DeleteAdvancedSequenceWithChannels\x129.nidcpower_grpc.DeleteAdvancedSequenceWithChannelsRequest\x1a:.nidcpower_grpc.DeleteAdvancedSequenceWithChannelsResponse\x12k\n\x12CommitWithChannels\x12).nidcpower_grpc.CommitWithChannelsRequest\x1a*.nidcpower_grpc.CommitWithChannelsResponse\x12q\n\x14InitiateWithChannels\x12+.nidcpower_grpc.InitiateWithChannelsRequest\x1a,.nidcpower_grpc.InitiateWithChannelsResponse\x12h\n\x11AbortWithChannels\x12(.nidcpower_grpc.AbortWithChannelsRequest\x1a).nidcpower_grpc.AbortWithChannelsResponse\x12\xb9\x01\n,ConfigureDigitalEdgeStartTriggerWithChannels\x12C.nidcpower_grpc.ConfigureDigitalEdgeStartTriggerWithChannelsRequest\x1aD.nidcpower_grpc.ConfigureDigitalEdgeStartTriggerWithChannelsResponse\x12\xbc\x01\n-ConfigureSoftwareEdgeStartTriggerWithChannels\x12D.nidcpower_grpc.ConfigureSoftwareEdgeStartTriggerWithChannelsRequest\x1aE.nidcpower_grpc.ConfigureSoftwareEdgeStartTriggerWithChannelsResponse\x12\x92\x01\n\x1fDisableStartTriggerWithChannels\x126.nidcpower_grpc.DisableStartTriggerWithChannelsRequest\x1a7.nidcpower_grpc.DisableStartTriggerWithChannelsResponse\x12\xd7\x01\n6ConfigureDigitalEdgeSequenceAdvanceTriggerWithChannels\x12M.nidcpower_grpc.ConfigureDigitalEdgeSequenceAdvanceTriggerWithChannelsRequest\x1aN.nidcpower_grpc.ConfigureDigitalEdgeSequenceAdvanceTriggerWithChannelsResponse\x12\xda\x01\n7ConfigureSoftwareEdgeSequenceAdvanceTriggerWithChannels\x12N.nidcpower_grpc.ConfigureSoftwareEdgeSequenceAdvanceTriggerWithChannelsRequest\x1aO.nidcpower_grpc.ConfigureSoftwareEdgeSequenceAdvanceTriggerWithChannelsResponse\x12\xb0\x01\n)DisableSequenceAdvanceTriggerWithChannels\x12@.nidcpower_grpc.DisableSequenceAdvanceTriggerWithChannelsRequest\x1aA.nidcpower_grpc.DisableSequenceAdvanceTriggerWithChannelsResponse\x12\xbc\x01\n-ConfigureDigitalEdgeSourceTriggerWithChannels\x12D.nidcpower_grpc.ConfigureDigitalEdgeSourceTriggerWithChannelsRequest\x1aE.nidcpower_grpc.ConfigureDigitalEdgeSourceTriggerWithChannelsResponse\x12\xbf\x01\n.ConfigureSoftwareEdgeSourceTriggerWithChannels\x12E.nidcpower_grpc.ConfigureSoftwareEdgeSourceTriggerWithChannelsRequest\x1aF.nidcpower_grpc.ConfigureSoftwareEdgeSourceTriggerWithChannelsResponse\x12\x95\x01\n DisableSourceTriggerWithChannels\x127.nidcpower_grpc.DisableSourceTriggerWithChannelsRequest\x1a8.nidcpower_grpc.DisableSourceTriggerWithChannelsResponse\x12\xbf\x01\n.ConfigureDigitalEdgeMeasureTriggerWithChannels\x12E.nidcpower_grpc.ConfigureDigitalEdgeMeasureTriggerWithChannelsRequest\x1aF.nidcpower_grpc.ConfigureDigitalEdgeMeasureTriggerWithChannelsResponse\x12\xc2\x01\n/ConfigureSoftwareEdgeMeasureTriggerWithChannels\x12F.nidcpower_grpc.ConfigureSoftwareEdgeMeasureTriggerWithChannelsRequest\x1aG.nidcpower_grpc.ConfigureSoftwareEdgeMeasureTriggerWithChannelsResponse\x12\xb9\x01\n,ConfigureDigitalEdgePulseTriggerWithChannels\x12C.nidcpower_grpc.ConfigureDigitalEdgePulseTriggerWithChannelsRequest\x1aD.nidcpower_grpc.ConfigureDigitalEdgePulseTriggerWithChannelsResponse\x12\xbc\x01\n-ConfigureSoftwareEdgePulseTriggerWithChannels\x12D.nidcpower_grpc.ConfigureSoftwareEdgePulseTriggerWithChannelsRequest\x1aE.nidcpower_grpc.ConfigureSoftwareEdgePulseTriggerWithChannelsResponse\x12\x92\x01\n\x1fDisablePulseTriggerWithChannels\x126.nidcpower_grpc.DisablePulseTriggerWithChannelsRequest\x1a7.nidcpower_grpc.DisablePulseTriggerWithChannelsResponse\x12\xc2\x01\n/ConfigureDigitalEdgeShutdownTriggerWithChannels\x12F.nidcpower_grpc.ConfigureDigitalEdgeShutdownTriggerWithChannelsRequest\x1aG.nidcpower_grpc.ConfigureDigitalEdgeShutdownTriggerWithChannelsResponse\x12\xc5\x01\n0ConfigureSoftwareEdgeShutdownTriggerWithChannels\x12G.nidcpower_grpc.ConfigureSoftwareEdgeShutdownTriggerWithChannelsRequest\x1aH.nidcpower_grpc.ConfigureSoftwareEdgeShutdownTriggerWithChannelsResponse\x12\x9b\x01\n"DisableShutdownTriggerWithChannels\x129.nidcpower_grpc.DisableShutdownTriggerWithChannelsRequest\x1a:.nidcpower_grpc.DisableShutdownTriggerWithChannelsResponse\x12}\n\x18ExportSignalWithChannels\x12/.nidcpower_grpc.ExportSignalWithChannelsRequest\x1a0.nidcpower_grpc.ExportSignalWithChannelsResponse\x12\x9e\x01\n#SendSoftwareEdgeTriggerWithChannels\x12:.nidcpower_grpc.SendSoftwareEdgeTriggerWithChannelsRequest\x1a;.nidcpower_grpc.SendSoftwareEdgeTriggerWithChannelsResponse\x12}\n\x18WaitForEventWithChannels\x12/.nidcpower_grpc.WaitForEventWithChannelsRequest\x1a0.nidcpower_grpc.WaitForEventWithChannelsResponse\x12h\n\x11ResetWithChannels\x12(.nidcpower_grpc.ResetWithChannelsRequest\x1a).nidcpower_grpc.ResetWithChannelsResponse\x12z\n\x17InvalidateAllAttributes\x12..nidcpower_grpc.InvalidateAllAttributesRequest\x1a/.nidcpower_grpc.InvalidateAllAttributesResponse\x12Y\n\x0cConfigureOvp\x12#.nidcpower_grpc.ConfigureOvpRequest\x1a$.nidcpower_grpc.ConfigureOvpResponse\x12S\n\nErrorQuery\x12!.nidcpower_grpc.ErrorQueryRequest\x1a".nidcpower_grpc.ErrorQueryResponse\x12\x98\x01\n!GetLCRCustomCableCompensationData\x128.nidcpower_grpc.GetLCRCustomCableCompensationDataRequest\x1a9.nidcpower_grpc.GetLCRCustomCableCompensationDataResponse\x12\x9e\x01\n#ConfigureLCRCustomCableCompensation\x12:.nidcpower_grpc.ConfigureLCRCustomCableCompensationRequest\x1a;.nidcpower_grpc.ConfigureLCRCustomCableCompensationResponseBE\n\x13com.ni.grpc.dcpowerB\tNiDCPowerP\x01\xaa\x02 NationalInstruments.Grpc.DCPowerb\x06proto3')`

<!--NI_PYTHON_API repo=nimi-python path=generated/nidcpower/nidcpower/nidcpower_pb2_grpc.py -->
## PYTHON MODULE: generated/nidcpower/nidcpower/nidcpower_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

### `class NiDCPowerStub(object)`

Missing associated documentation comment in .proto file.

#### `def __init__(self, channel)`

Constructor.

        Args:
            channel: A grpc.Channel.
        

### `class NiDCPowerServicer(object)`

Missing associated documentation comment in .proto file.

#### `def InitializeWithChannels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Close(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureSourceMode(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureOutputFunction(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureOutputEnabled(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetSequence(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureVoltageLevel(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureCurrentLimit(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureVoltageLevelRange(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureCurrentLimitRange(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureOutputResistance(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureCurrentLevel(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureCurrentLevelRange(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureVoltageLimit(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureVoltageLimitRange(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigurePulseVoltageLevel(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigurePulseCurrentLimit(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigurePulseBiasVoltageLevel(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigurePulseBiasCurrentLimit(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigurePulseVoltageLevelRange(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigurePulseCurrentLimitRange(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigurePulseCurrentLevel(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigurePulseVoltageLimit(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigurePulseBiasCurrentLevel(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigurePulseBiasVoltageLimit(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigurePulseCurrentLevelRange(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigurePulseVoltageLimitRange(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAdvancedSequence(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAdvancedSequenceStep(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DeleteAdvancedSequence(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureApertureTime(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureAutoZero(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigurePowerLineFrequency(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureSense(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Measure(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def MeasureMultiple(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def FetchMultiple(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def MeasureMultipleLCR(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def FetchMultipleLCR(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def QueryInCompliance(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def QueryOutputState(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def QueryLatchedOutputCutoffState(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ClearLatchedOutputCutoffState(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Commit(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Initiate(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Abort(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def QueryMaxCurrentLimit(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def QueryMaxVoltageLevel(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def QueryMinCurrentLimit(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CalSelfCalibrate(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetExtCalRecommendedInterval(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetExtCalLastDateAndTime(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadCurrentTemperature(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetExtCalLastTemp(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetSelfCalLastDateAndTime(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetSelfCalLastTemp(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetLCRCompensationLastDateAndTime(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureDigitalEdgeStartTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureSoftwareEdgeStartTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DisableStartTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureDigitalEdgeSequenceAdvanceTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureSoftwareEdgeSequenceAdvanceTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DisableSequenceAdvanceTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureDigitalEdgeSourceTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureSoftwareEdgeSourceTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DisableSourceTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureDigitalEdgeMeasureTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureSoftwareEdgeMeasureTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureDigitalEdgePulseTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureSoftwareEdgePulseTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DisablePulseTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ExportSignal(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SendSoftwareEdgeTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WaitForEvent(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Disable(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Reset(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ResetDevice(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SelfTest(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def RevisionQuery(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ResetWithDefaults(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetChannelName(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetChannelNameFromString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetNextCoercionRecord(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ClearInterchangeWarnings(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ResetInterchangeCheck(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetNextInterchangeWarning(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetError(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ClearError(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ErrorMessage(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViInt64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViReal64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViSession(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViBoolean(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViInt64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViReal64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViSession(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViBoolean(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ImportAttributeConfigurationFile(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ExportAttributeConfigurationFile(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ImportAttributeConfigurationBuffer(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ExportAttributeConfigurationBuffer(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def PerformLCROpenCompensation(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def PerformLCRShortCompensation(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def PerformLCRLoadCompensation(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureLCRCompensation(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def PerformLCROpenCustomCableCompensation(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def PerformLCRShortCustomCableCompensation(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetLCRCompensationData(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def InitializeWithIndependentChannels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureSourceModeWithChannels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAdvancedSequenceWithChannels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAdvancedSequenceStepWithChannels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateAdvancedSequenceCommitStepWithChannels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DeleteAdvancedSequenceWithChannels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CommitWithChannels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def InitiateWithChannels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def AbortWithChannels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureDigitalEdgeStartTriggerWithChannels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureSoftwareEdgeStartTriggerWithChannels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DisableStartTriggerWithChannels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureDigitalEdgeSequenceAdvanceTriggerWithChannels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureSoftwareEdgeSequenceAdvanceTriggerWithChannels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DisableSequenceAdvanceTriggerWithChannels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureDigitalEdgeSourceTriggerWithChannels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureSoftwareEdgeSourceTriggerWithChannels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DisableSourceTriggerWithChannels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureDigitalEdgeMeasureTriggerWithChannels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureSoftwareEdgeMeasureTriggerWithChannels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureDigitalEdgePulseTriggerWithChannels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureSoftwareEdgePulseTriggerWithChannels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DisablePulseTriggerWithChannels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureDigitalEdgeShutdownTriggerWithChannels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureSoftwareEdgeShutdownTriggerWithChannels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DisableShutdownTriggerWithChannels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ExportSignalWithChannels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SendSoftwareEdgeTriggerWithChannels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WaitForEventWithChannels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ResetWithChannels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def InvalidateAllAttributes(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureOvp(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ErrorQuery(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetLCRCustomCableCompensationData(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureLCRCustomCableCompensation(self, request, context)`

Missing associated documentation comment in .proto file.

### `def add_NiDCPowerServicer_to_server(servicer, server)`

### `class NiDCPower(object)`

Missing associated documentation comment in .proto file.

#### `def InitializeWithChannels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Close(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureSourceMode(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureOutputFunction(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureOutputEnabled(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetSequence(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureVoltageLevel(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureCurrentLimit(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureVoltageLevelRange(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureCurrentLimitRange(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureOutputResistance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureCurrentLevel(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureCurrentLevelRange(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureVoltageLimit(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureVoltageLimitRange(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigurePulseVoltageLevel(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigurePulseCurrentLimit(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigurePulseBiasVoltageLevel(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigurePulseBiasCurrentLimit(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigurePulseVoltageLevelRange(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigurePulseCurrentLimitRange(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigurePulseCurrentLevel(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigurePulseVoltageLimit(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigurePulseBiasCurrentLevel(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigurePulseBiasVoltageLimit(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigurePulseCurrentLevelRange(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigurePulseVoltageLimitRange(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAdvancedSequence(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAdvancedSequenceStep(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DeleteAdvancedSequence(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureApertureTime(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureAutoZero(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigurePowerLineFrequency(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureSense(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Measure(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def MeasureMultiple(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def FetchMultiple(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def MeasureMultipleLCR(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def FetchMultipleLCR(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def QueryInCompliance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def QueryOutputState(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def QueryLatchedOutputCutoffState(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ClearLatchedOutputCutoffState(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Commit(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Initiate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Abort(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def QueryMaxCurrentLimit(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def QueryMaxVoltageLevel(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def QueryMinCurrentLimit(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CalSelfCalibrate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetExtCalRecommendedInterval(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetExtCalLastDateAndTime(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadCurrentTemperature(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetExtCalLastTemp(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetSelfCalLastDateAndTime(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetSelfCalLastTemp(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetLCRCompensationLastDateAndTime(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureDigitalEdgeStartTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureSoftwareEdgeStartTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DisableStartTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureDigitalEdgeSequenceAdvanceTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureSoftwareEdgeSequenceAdvanceTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DisableSequenceAdvanceTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureDigitalEdgeSourceTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureSoftwareEdgeSourceTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DisableSourceTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureDigitalEdgeMeasureTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureSoftwareEdgeMeasureTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureDigitalEdgePulseTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureSoftwareEdgePulseTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DisablePulseTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ExportSignal(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SendSoftwareEdgeTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WaitForEvent(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Disable(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Reset(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ResetDevice(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SelfTest(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def RevisionQuery(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ResetWithDefaults(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetChannelName(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetChannelNameFromString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetNextCoercionRecord(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ClearInterchangeWarnings(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ResetInterchangeCheck(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetNextInterchangeWarning(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetError(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ClearError(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ErrorMessage(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViInt64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViReal64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViSession(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViBoolean(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViInt64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViReal64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViSession(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViBoolean(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ImportAttributeConfigurationFile(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ExportAttributeConfigurationFile(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ImportAttributeConfigurationBuffer(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ExportAttributeConfigurationBuffer(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def PerformLCROpenCompensation(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def PerformLCRShortCompensation(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def PerformLCRLoadCompensation(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureLCRCompensation(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def PerformLCROpenCustomCableCompensation(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def PerformLCRShortCustomCableCompensation(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetLCRCompensationData(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def InitializeWithIndependentChannels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureSourceModeWithChannels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAdvancedSequenceWithChannels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAdvancedSequenceStepWithChannels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateAdvancedSequenceCommitStepWithChannels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DeleteAdvancedSequenceWithChannels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CommitWithChannels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def InitiateWithChannels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def AbortWithChannels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureDigitalEdgeStartTriggerWithChannels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureSoftwareEdgeStartTriggerWithChannels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DisableStartTriggerWithChannels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureDigitalEdgeSequenceAdvanceTriggerWithChannels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureSoftwareEdgeSequenceAdvanceTriggerWithChannels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DisableSequenceAdvanceTriggerWithChannels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureDigitalEdgeSourceTriggerWithChannels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureSoftwareEdgeSourceTriggerWithChannels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DisableSourceTriggerWithChannels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureDigitalEdgeMeasureTriggerWithChannels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureSoftwareEdgeMeasureTriggerWithChannels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureDigitalEdgePulseTriggerWithChannels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureSoftwareEdgePulseTriggerWithChannels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DisablePulseTriggerWithChannels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureDigitalEdgeShutdownTriggerWithChannels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureSoftwareEdgeShutdownTriggerWithChannels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DisableShutdownTriggerWithChannels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ExportSignalWithChannels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SendSoftwareEdgeTriggerWithChannels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WaitForEventWithChannels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ResetWithChannels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def InvalidateAllAttributes(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureOvp(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ErrorQuery(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetLCRCustomCableCompensationData(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureLCRCustomCableCompensation(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nidcpower/nidcpower/nidevice_pb2.py -->
## PYTHON MODULE: generated/nidcpower/nidcpower/nidevice_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0enidevice.proto\x12\rnidevice_grpc"2\n\x0fNIComplexNumber\x12\x0c\n\x04real\x18\x01 \x01(\x01\x12\x11\n\timaginary\x18\x02 \x01(\x01"5\n\x12NIComplexNumberF32\x12\x0c\n\x04real\x18\x01 \x01(\x02\x12\x11\n\timaginary\x18\x02 \x01(\x02"/\n\x0cNIComplexI16\x12\x0c\n\x04real\x18\x01 \x01(\x11\x12\x11\n\timaginary\x18\x02 \x01(\x11"r\n\x0fSmtSpectrumInfo\x12\x15\n\rspectrum_type\x18\x01 \x01(\r\x12\x11\n\tlinear_db\x18\x02 \x01(\r\x12\x0e\n\x06window\x18\x03 \x01(\r\x12\x13\n\x0bwindow_size\x18\x04 \x01(\x11\x12\x10\n\x08fft_size\x18\x05 \x01(\x11BB\n\x12com.ni.grpc.deviceB\x08NiDeviceP\x01\xaa\x02\x1fNationalInstruments.Grpc.Deviceb\x06proto3')`

<!--NI_PYTHON_API repo=nimi-python path=generated/nidcpower/nidcpower/nidevice_pb2_grpc.py -->
## PYTHON MODULE: generated/nidcpower/nidcpower/nidevice_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

<!--NI_PYTHON_API repo=nimi-python path=generated/nidcpower/nidcpower/session.py -->
## PYTHON MODULE: generated/nidcpower/nidcpower/session.py

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

Base class for all NI-DCPower sessions.

#### `def __init__(self, repeated_capability_list, all_channels_in_session, interpreter, freeze_it=False)`

#### `def __repr__(self)`

#### `def __setattr__(self, key, value)`

#### `def initiate(self)`

initiate

        Starts generation or acquisition, causing the specified channel(s) to
        leave the Uncommitted state or Committed state and enter the Running
        state. To return to the Uncommitted state call the abort
        method. Refer to the `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in
        the *NI DC Power Supplies and SMUs Help* for information about the
        specific NI-DCPower software states.

        **Related Topics:**

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        Note:
        This method will return a Python context manager that will initiate on entering and abort on exit.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].initiate`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.initiate`
        

#### `def abort(self)`

abort

        Transitions the specified channel(s) from the Running state to the
        Uncommitted state. If a sequence is running, it is stopped. Any
        configuration methods called after this method are not applied until
        the initiate method is called. If power output is enabled
        when you call the abort method, the channels remain
        in their current state and continue providing power.

        Use the ConfigureOutputEnabled method to disable power
        output on a per channel basis. Use the reset method to
        disable output on all channels.

        Refer to the `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in
        the *NI DC Power Supplies and SMUs Help* for information about the
        specific NI-DCPower software states.

        **Related Topics:**

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        Note:
        NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

        Note:
        One or more of the referenced methods are not in the Python API for this driver.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].abort`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.abort`
        

#### `def self_cal(self)`

self_cal

        Performs a self-calibration upon the specified channel(s).

        This method disables the output, performs several internal
        calculations, and updates calibration values. The updated calibration
        values are written to the device hardware if the
        self_calibration_persistence property is set to
        SelfCalibrationPersistence.WRITE_TO_EEPROM. Refer to the
        self_calibration_persistence property topic for more
        information about the settings for this property.

        When calling self_cal with the PXIe-4162/4163,
        specify all channels of your PXIe-4162/4163 with the channelName input.
        You cannot self-calibrate a subset of PXIe-4162/4163 channels.

        Refer to the
        `Self-Calibration <REPLACE_DRIVER_SPECIFIC_URL_1(selfcal)>`__ topic for
        more information about this method.

        **Related Topics:**

        `Self-Calibration <REPLACE_DRIVER_SPECIFIC_URL_1(selfcal)>`__

        Note:
        NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].self_cal`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.self_cal`
        

#### `def clear_latched_output_cutoff_state(self, output_cutoff_reason)`

clear_latched_output_cutoff_state

        Clears the state of an output cutoff that was engaged.
        To clear the state for all output cutoff reasons, use OutputCutoffReason.ALL.

        Note:
        NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].clear_latched_output_cutoff_state`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.clear_latched_output_cutoff_state`

        Args:
            output_cutoff_reason (enums.OutputCutoffReason): Specifies the reasons for which to clear the output cutoff state.

                +-----------------------------------------+-----------------------------------------------------------------------------------------------------------------+
                | OutputCutoffReason.ALL                  | Clears all output cutoff conditions                                                                             |
                +-----------------------------------------+-----------------------------------------------------------------------------------------------------------------+
                | OutputCutoffReason.VOLTAGE_OUTPUT_HIGH  | Clears cutoffs caused when the output exceeded the high cutoff limit for voltage output                         |
                +-----------------------------------------+-----------------------------------------------------------------------------------------------------------------+
                | OutputCutoffReason.VOLTAGE_OUTPUT_LOW   | Clears cutoffs caused when the output fell below the low cutoff limit for voltage output                        |
                +-----------------------------------------+-----------------------------------------------------------------------------------------------------------------+
                | OutputCutoffReason.VOLTAGE_MEASURE_HIGH | Clears cutoffs caused when the measured voltage exceeded the high cutoff limit for voltage output               |
                +-----------------------------------------+-----------------------------------------------------------------------------------------------------------------+
                | OutputCutoffReason.VOLTAGE_MEASURE_LOW  | Clears cutoffs caused when the measured voltage fell below the low cutoff limit for voltage output              |
                +-----------------------------------------+-----------------------------------------------------------------------------------------------------------------+
                | OutputCutoffReason.CURRENT_MEASURE_HIGH | Clears cutoffs caused when the measured current exceeded the high cutoff limit for current output               |
                +-----------------------------------------+-----------------------------------------------------------------------------------------------------------------+
                | OutputCutoffReason.CURRENT_MEASURE_LOW  | Clears cutoffs caused when the measured current fell below the low cutoff limit for current output              |
                +-----------------------------------------+-----------------------------------------------------------------------------------------------------------------+
                | OutputCutoffReason.VOLTAGE_CHANGE_HIGH  | Clears cutoffs caused when the voltage slew rate increased beyond the positive change cutoff for voltage output |
                +-----------------------------------------+-----------------------------------------------------------------------------------------------------------------+
                | OutputCutoffReason.VOLTAGE_CHANGE_LOW   | Clears cutoffs caused when the voltage slew rate decreased beyond the negative change cutoff for voltage output |
                +-----------------------------------------+-----------------------------------------------------------------------------------------------------------------+
                | OutputCutoffReason.CURRENT_CHANGE_HIGH  | Clears cutoffs caused when the current slew rate increased beyond the positive change cutoff for current output |
                +-----------------------------------------+-----------------------------------------------------------------------------------------------------------------+
                | OutputCutoffReason.CURRENT_CHANGE_LOW   | Clears cutoffs caused when the voltage slew rate decreased beyond the negative change cutoff for current output |
                +-----------------------------------------+-----------------------------------------------------------------------------------------------------------------+
                | OutputCutoffReason.CURRENT_SATURATED    | Clears cutoffs caused when the measured current saturates the current range                                     |
                +-----------------------------------------+-----------------------------------------------------------------------------------------------------------------+

        

#### `def commit(self)`

commit

        Applies previously configured settings to the specified channel(s). Calling this
        method moves the NI-DCPower session from the Uncommitted state into
        the Committed state. After calling this method, modifying any
        property reverts the NI-DCPower session to the Uncommitted state. Use
        the initiate method to transition to the Running state.
        Refer to the `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in
        the *NI DC Power Supplies and SMUs Help* for details about the specific
        NI-DCPower software states.

        **Related Topics:**

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].commit`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.commit`
        

#### `def configure_aperture_time(self, aperture_time, units=enums.ApertureTimeUnits.SECONDS)`

configure_aperture_time

        Configures the aperture time on the specified channel(s).

        The supported values depend on the **units**. Refer to the *Aperture
        Time* topic for your device in the *NI DC Power Supplies and SMUs Help*
        for more information. In general, devices support discrete
        **apertureTime** values, and if you configure **apertureTime** to some
        unsupported value, NI-DCPower coerces it up to the next supported value.

        Refer to the *Measurement Configuration and Timing* or *DC Noise
        Rejection* topic for your device in the *NI DC Power Supplies and SMUs
        Help* for more information about how to configure your measurements.

        **Related Topics:**

        `Aperture Time <REPLACE_DRIVER_SPECIFIC_URL_1(aperture)>`__

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_aperture_time`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.configure_aperture_time`

        Args:
            aperture_time (float): Specifies the aperture time. Refer to the *Aperture Time* topic for your
                device in the *NI DC Power Supplies and SMUs Help* for more information.

            units (enums.ApertureTimeUnits): Specifies the units for **apertureTime**.
                **Defined Values**:

                +-------------------------------------+------------------------------+
                | ApertureTimeUnits.SECONDS           | Specifies seconds.           |
                +-------------------------------------+------------------------------+
                | ApertureTimeUnits.POWER_LINE_CYCLES | Specifies Power Line Cycles. |
                +-------------------------------------+------------------------------+

        

#### `def configure_lcr_compensation(self, compensation_data)`

configure_lcr_compensation

        Applies previously generated open, short, load, as well as open and short custom cable compensation data to LCR measurements.

        This method applies open, short and load compensation data when you have set the lcr_open_short_load_compensation_data_source property to LCROpenShortLoadCompensationDataSource.AS_CONFIGURED, and it also applies custom cable compensation data when you have set the cable_length property to CableLength.CUSTOM_AS_CONFIGURED.

        Call this method after you have obtained LCR compensation data.

        If the lcr_short_custom_cable_compensation_enabled property is set to True, you must generate data with both perform_lcr_open_custom_cable_compensation and perform_lcr_short_custom_cable_compensation; if False, you must only use perform_lcr_open_custom_cable_compensation, and NI-DCPower uses default short data.

        Call get_lcr_compensation_data and pass the **compensation data** to this method.

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_lcr_compensation`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.configure_lcr_compensation`

        Args:
            compensation_data (bytes): The open, short and load compensation data to apply.

        

#### `def configure_lcr_custom_cable_compensation(self, custom_cable_compensation_data)`

configure_lcr_custom_cable_compensation

        This method is deprecated. Use configure_lcr_compensation
        instead.

        Applies previously generated open and short custom cable compensation data to LCR measurements.

        This method applies custom cable compensation data when you have set cable_length property to CableLength.CUSTOM_AS_CONFIGURED.

        Call this method after you have obtained custom cable compensation data.

        If lcr_short_custom_cable_compensation_enabled property is set to True, you must generate data with both perform_lcr_open_custom_cable_compensation and perform_lcr_short_custom_cable_compensation;
        if False, you must only use perform_lcr_open_custom_cable_compensation, and NI-DCPower uses default short data.

        Call get_lcr_custom_cable_compensation_data and pass the **custom cable compensation data** to this method.

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_lcr_custom_cable_compensation`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.configure_lcr_custom_cable_compensation`

        Args:
            custom_cable_compensation_data (bytes): The open and short custom cable compensation data to apply.

        

#### `def create_advanced_sequence_commit_step(self, set_as_active_step=True)`

create_advanced_sequence_commit_step

        Creates a Commit step in the Active advanced sequence. A Commit step
        configures channels to a user-defined known state before starting the advanced sequence.
        When a Commit step exists in the Active advanced sequence, you cannot
        set the output method to Pulse Voltage or Pulse Current in either
        the Commit step (-1) or step 0. When you create an advanced sequence
        step, each property you passed to the create_advanced_sequence
        method is reset to its default value for that step unless otherwise specified.

        **Support for this Method**

        You must set the source mode to Sequence to use this method.

        Using the set_sequence method with Advanced Sequence
        methods is unsupported.

        **Related Topics**:

        `Advanced Sequence
        Mode <REPLACE_DRIVER_SPECIFIC_URL_1(advancedsequencemode)>`__

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        create_advanced_sequence

        Note:
        NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].create_advanced_sequence_commit_step`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.create_advanced_sequence_commit_step`

        Args:
            set_as_active_step (bool): Specifies whether the step created with this method is active in the Active advanced sequence.

        

#### `def create_advanced_sequence_step(self, set_as_active_step=True)`

create_advanced_sequence_step

        Creates a new advanced sequence step in the advanced sequence specified
        by the Active advanced sequence. When you create an advanced sequence
        step, each property you passed to the create_advanced_sequence
        method is reset to its default value for that step unless otherwise
        specified.

        **Support for this Method**

        You must set the source mode to Sequence to use this method.

        Using the set_sequence method with Advanced Sequence
        methods is unsupported.

        **Related Topics**:

        `Advanced Sequence
        Mode <REPLACE_DRIVER_SPECIFIC_URL_1(advancedsequencemode)>`__

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        create_advanced_sequence

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].create_advanced_sequence_step`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.create_advanced_sequence_step`

        Args:
            set_as_active_step (bool): Specifies whether the step created with this method is active in the Active advanced sequence.

        

#### `def _create_advanced_sequence_with_channels(self, sequence_name, attribute_ids, set_as_active_sequence)`

_create_advanced_sequence_with_channels

        Creates an empty advanced sequence. Call the
        create_advanced_sequence_step method to add steps to the
        active advanced sequence.

        You can create multiple advanced sequences for a channel.

        **Support for this method**

        You must set the source mode to Sequence to use this method.

        Using the set_sequence method with Advanced Sequence
        methods is unsupported.

        Use this method in the Uncommitted or Committed programming states.
        Refer to the `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in
        the *NI DC Power Supplies and SMUs Help* for more information about
        NI-DCPower programming states.

        **Related Topics**:

        `Advanced Sequence
        Mode <REPLACE_DRIVER_SPECIFIC_URL_1(advancedsequencemode)>`__

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        create_advanced_sequence_step

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._create_advanced_sequence_with_channels`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._create_advanced_sequence_with_channels`

        Args:
            sequence_name (str): Specifies the name of the sequence to create.

            attribute_ids (list of int): Specifies the properties you reconfigure per step in the advanced
                sequence. For more information about which properties can be configured
                in an advanced sequence for each NI-DCPower device that supports advanced
                sequencing, search ni.com for Supported Properties by Device.

            set_as_active_sequence (bool): Specifies that this current sequence is active.

        

#### `def delete_advanced_sequence(self, sequence_name)`

delete_advanced_sequence

        Deletes a previously created advanced sequence and all the advanced
        sequence steps in the advanced sequence.

        **Support for this Method**

        You must set the source mode to Sequence to use this method.

        Using the set_sequence method with Advanced Sequence
        methods is unsupported.

        **Related Topics**:

        `Advanced Sequence
        Mode <REPLACE_DRIVER_SPECIFIC_URL_1(advancedsequencemode)>`__

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].delete_advanced_sequence`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.delete_advanced_sequence`

        Args:
            sequence_name (str): specifies the name of the sequence to delete.

        

#### `def create_advanced_sequence(self, sequence_name, property_names, set_as_active_sequence=True)`

create_advanced_sequence

        Creates an empty advanced sequence. Call the
        create_advanced_sequence_step method to add steps to the
        active advanced sequence.

        You can create multiple advanced sequences in a session.

        **Support for this method**

        You must set the source mode to Sequence to use this method.

        Using the set_sequence method with Advanced Sequence
        methods is unsupported.

        Use this method in the Uncommitted or Committed programming states.
        Refer to the `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in
        the *NI DC Power Supplies and SMUs Help* for more information about
        NI-DCPower programming states.

        **Related Topics**:

        `Advanced Sequence
        Mode <REPLACE_DRIVER_SPECIFIC_URL_1(advancedsequencemode)>`__

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        create_advanced_sequence_step

        Note:
        This method is not supported on all devices. Refer to `Supported
        Methods by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].create_advanced_sequence`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.create_advanced_sequence`

        Args:
            sequence_name (str): Specifies the name of the sequence to create.

            property_names (list of str): Specifies the names of the properties you reconfigure per step in the advanced sequence. For more information about properties that can be configured in an advanced sequence for each NI-DCPower device that supports advanced sequencing, search ni.com for Supported Properties by Device.

            set_as_active_sequence (bool): Specifies that this current sequence is active.

        

#### `def fetch_multiple(self, count, timeout=hightime.timedelta(seconds=1.0))`

fetch_multiple

        Returns a list of named tuples (Measurement) that were
        previously taken and are stored in the NI-DCPower buffer. This method
        should not be used when the measure_when property is
        set to MeasureWhen.ON_DEMAND. You must first call
        initiate before calling this method.

        Fields in Measurement:

        - **voltage** (float)
        - **current** (float)
        - **in_compliance** (bool)
        - **channel** (str)

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].fetch_multiple`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.fetch_multiple`

        Args:
            count (int): Specifies the number of measurements to fetch.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): Specifies the maximum time allowed for this method to complete. If the method does not complete within this time interval, NI-DCPower returns an error.
                Default value: 1.0 second

                Note: When setting the timeout interval, ensure you take into account any triggers so that the timeout interval is long enough for your application.


        Returns:
            measurements (list of Measurement): List of named tuples with fields:

                - **voltage** (float)
                - **current** (float)
                - **in_compliance** (bool)
                - **channel** (str)

        

#### `def fetch_multiple_lcr(self, count, timeout=hightime.timedelta(seconds=1.0))`

fetch_multiple_lcr

        Returns a list of previously measured LCRMeasurement instances on the specified channel that have been taken and stored in a buffer.

        To use this method:

        -  Set measure_when property to MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE or MeasureWhen.ON_MEASURE_TRIGGER
        -  Put the channel in the Running state (call initiate)

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].fetch_multiple_lcr`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.fetch_multiple_lcr`

        Args:
            count (int): Specifies the number of measurements to fetch.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): Specifies the maximum time allowed for this method to complete, in seconds.
                If the method does not complete within this time interval, NI-DCPower returns an error.
                Default value: 1.0 second

                Note:
                When setting the timeout interval, ensure you take into account any triggers so that the timeout interval is long enough for your application.


        Returns:
            measurements (list of LCRMeasurement): A list of LCRMeasurement instances.

                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | channel               |                      | The channel name associated with this LCR measurement.                                                                                                                                                |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | vdc                   | float                | The measured DC voltage, in volts.                                                                                                                                                                    |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | idc                   | float                | The measured DC current, in amps.                                                                                                                                                                     |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | stimulus_frequency    | float                | The frequency of the LCR test signal, in Hz.                                                                                                                                                          |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ac_voltage            | complex              | The measured AC voltage, in volts RMS.                                                                                                                                                                |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ac_current            | complex              | The measured AC current, in amps RMS.                                                                                                                                                                 |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | z                     | complex              | The complex impedance.                                                                                                                                                                                |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | z_magnitude_and_phase | tuple of float       | The magnitude, in ohms, and phase angle, in degrees, of the complex impedance.                                                                                                                        |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | y                     | complex              | The complex admittance.                                                                                                                                                                               |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | y_magnitude_and_phase | tuple of float       | The magnitude, in siemens, and phase angle, in degrees, of the complex admittance.                                                                                                                    |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | series_lcr            | LCR                  | The inductance, in henrys, the capacitance, in farads, and the resistance, in ohms, as measured using a series circuit model.                                                                         |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | parallel_lcr          | LCR                  | The inductance, in henrys, the capacitance, in farads, and the resistance, in ohms, as measured using a parallel circuit model.                                                                       |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | d                     | float                | The dissipation factor of the circuit. The dimensionless dissipation factor is directly proportional to how quickly an oscillating system loses energy. D is the reciprocal of Q, the quality factor. |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | q                     | float                | The quality factor of the circuit. The dimensionless quality factor is inversely proportional to the degree of damping in a system. Q is the reciprocal of D, the dissipation factor.                 |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | measurement_mode      | enums.InstrumentMode | The measurement mode: **SMU** - The channel(s) are operating as a power supply/SMU. **LCR** - The channel(s) are operating as an LCR meter.                                                           |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | dc_in_compliance      | bool                 | Indicates whether the output was in DC compliance at the time the measurement was taken.                                                                                                              |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ac_in_compliance      | bool                 | Indicates whether the output was in AC compliance at the time the measurement was taken.                                                                                                              |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | unbalanced            | bool                 | Indicates whether the output was unbalanced at the time the measurement was taken.                                                                                                                    |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        

#### `def measure_multiple(self)`

measure_multiple

        Returns a list of named tuples (Measurement) containing the measured voltage
        and current values on the specified channel(s). Each call to this method
        blocks other method calls until the measurements are returned from the device.
        The order of the measurements returned in the array corresponds to the order
        on the specified channel(s).

        Fields in Measurement:

        - **voltage** (float)
        - **current** (float)
        - **in_compliance** (bool) - Always None
        - **channel** (str)

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].measure_multiple`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.measure_multiple`

        Returns:
            measurements (list of Measurement): List of named tuples with fields:

                - **voltage** (float)
                - **current** (float)
                - **in_compliance** (bool) - Always None
                - **channel** (str)

        

#### `def measure_multiple_lcr(self)`

measure_multiple_lcr

        Measures and returns a list of LCRMeasurement instances on the specified channel(s).

        To use this method:

        -  Set instrument_mode property to InstrumentMode.LCR
        -  Set measure_when property to MeasureWhen.ON_DEMAND
        -  Put the channel(s) in the Running state (call initiate)

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].measure_multiple_lcr`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.measure_multiple_lcr`

        Returns:
            measurements (list of LCRMeasurement): A list of LCRMeasurement instances.

                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | channel               |                      | The channel name associated with this LCR measurement.                                                                                                                                                |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | vdc                   | float                | The measured DC voltage, in volts.                                                                                                                                                                    |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | idc                   | float                | The measured DC current, in amps.                                                                                                                                                                     |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | stimulus_frequency    | float                | The frequency of the LCR test signal, in Hz.                                                                                                                                                          |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ac_voltage            | complex              | The measured AC voltage, in volts RMS.                                                                                                                                                                |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ac_current            | complex              | The measured AC current, in amps RMS.                                                                                                                                                                 |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | z                     | complex              | The complex impedance.                                                                                                                                                                                |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | z_magnitude_and_phase | tuple of float       | The magnitude, in ohms, and phase angle, in degrees, of the complex impedance.                                                                                                                        |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | y                     | complex              | The complex admittance.                                                                                                                                                                               |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | y_magnitude_and_phase | tuple of float       | The magnitude, in siemens, and phase angle, in degrees, of the complex admittance.                                                                                                                    |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | series_lcr            | LCR                  | The inductance, in henrys, the capacitance, in farads, and the resistance, in ohms, as measured using a series circuit model.                                                                         |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | parallel_lcr          | LCR                  | The inductance, in henrys, the capacitance, in farads, and the resistance, in ohms, as measured using a parallel circuit model.                                                                       |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | d                     | float                | The dissipation factor of the circuit. The dimensionless dissipation factor is directly proportional to how quickly an oscillating system loses energy. D is the reciprocal of Q, the quality factor. |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | q                     | float                | The quality factor of the circuit. The dimensionless quality factor is inversely proportional to the degree of damping in a system. Q is the reciprocal of D, the dissipation factor.                 |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | measurement_mode      | enums.InstrumentMode | The measurement mode: **SMU** - The channel(s) are operating as a power supply/SMU. **LCR** - The channel(s) are operating as an LCR meter.                                                           |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | dc_in_compliance      | bool                 | Indicates whether the output was in DC compliance at the time the measurement was taken.                                                                                                              |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ac_in_compliance      | bool                 | Indicates whether the output was in AC compliance at the time the measurement was taken.                                                                                                              |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | unbalanced            | bool                 | Indicates whether the output was unbalanced at the time the measurement was taken.                                                                                                                    |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        

#### `def _fetch_multiple(self, timeout, count)`

_fetch_multiple

        Returns an array of voltage measurements, an array of current
        measurements, and an array of compliance measurements that were
        previously taken and are stored in the NI-DCPower buffer. This method
        should not be used when the measure_when property is
        set to MeasureWhen.ON_DEMAND. You must first call
        initiate before calling this method.

        Refer to the `Acquiring
        Measurements <REPLACE_DRIVER_SPECIFIC_URL_1(acquiringmeasurements)>`__
        and `Compliance <REPLACE_DRIVER_SPECIFIC_URL_1(compliance)>`__ topics in
        the *NI DC Power Supplies and SMUs Help* for more information about
        configuring this method.

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._fetch_multiple`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._fetch_multiple`

        Args:
            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): Specifies the maximum time allowed for this method to complete, in
                seconds. If the method does not complete within this time interval,
                NI-DCPower returns an error.

                Note:
                When setting the timeout interval, ensure you take into account any
                triggers so that the timeout interval is long enough for your
                application.

            count (int): Specifies the number of measurements to fetch.


        Returns:
            voltage_measurements (array.array("d")): Returns an array of voltage measurements. Ensure that sufficient space
                has been allocated for the returned array.

            current_measurements (array.array("d")): Returns an array of current measurements. Ensure that sufficient space
                has been allocated for the returned array.

            in_compliance (list of bool): Returns an array of Boolean values indicating whether the output was in
                compliance at the time the measurement was taken. Ensure that sufficient
                space has been allocated for the returned array.

        

#### `def _fetch_multiple_lcr(self, count, timeout=hightime.timedelta(seconds=1.0))`

_fetch_multiple_lcr

        Returns a list of previously measured LCRMeasurement instances on the specified channel that have been taken and stored in a buffer.

        To use this method:

        -  Set measure_when property to MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE or MeasureWhen.ON_MEASURE_TRIGGER
        -  Put the channel in the Running state (call initiate)

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._fetch_multiple_lcr`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._fetch_multiple_lcr`

        Args:
            count (int): Specifies the number of measurements to fetch.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): Specifies the maximum time allowed for this method to complete, in seconds.
                If the method does not complete within this time interval, NI-DCPower returns an error.

                Note:
                When setting the timeout interval, ensure you take into account any triggers so that the timeout interval is long enough for your application.


        Returns:
            measurements (list of LCRMeasurement): A list of LCRMeasurement instances.

                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | vdc                   | float                | The measured DC voltage, in volts.                                                                                                                                                                    |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | idc                   | float                | The measured DC current, in amps.                                                                                                                                                                     |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | stimulus_frequency    | float                | The frequency of the LCR test signal, in Hz.                                                                                                                                                          |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ac_voltage            | complex              | The measured AC voltage, in volts RMS.                                                                                                                                                                |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ac_current            | complex              | The measured AC current, in amps RMS.                                                                                                                                                                 |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | z                     | complex              | The complex impedance.                                                                                                                                                                                |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | z_magnitude_and_phase | tuple of float       | The magnitude, in ohms, and phase angle, in degrees, of the complex impedance.                                                                                                                        |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | y                     | complex              | The complex admittance.                                                                                                                                                                               |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | y_magnitude_and_phase | tuple of float       | The magnitude, in siemens, and phase angle, in degrees, of the complex admittance.                                                                                                                    |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | series_lcr            | LCR                  | The inductance, in henrys, the capacitance, in farads, and the resistance, in ohms, as measured using a series circuit model.                                                                         |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | parallel_lcr          | LCR                  | The inductance, in henrys, the capacitance, in farads, and the resistance, in ohms, as measured using a parallel circuit model.                                                                       |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | d                     | float                | The dissipation factor of the circuit. The dimensionless dissipation factor is directly proportional to how quickly an oscillating system loses energy. D is the reciprocal of Q, the quality factor. |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | q                     | float                | The quality factor of the circuit. The dimensionless quality factor is inversely proportional to the degree of damping in a system. Q is the reciprocal of D, the dissipation factor.                 |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | measurement_mode      | enums.InstrumentMode | The measurement mode: **SMU** - The channel(s) are operating as a power supply/SMU. **LCR** - The channel(s) are operating as an LCR meter.                                                           |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | dc_in_compliance      | bool                 | Indicates whether the output was in DC compliance at the time the measurement was taken.                                                                                                              |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ac_in_compliance      | bool                 | Indicates whether the output was in AC compliance at the time the measurement was taken.                                                                                                              |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | unbalanced            | bool                 | Indicates whether the output was unbalanced at the time the measurement was taken.                                                                                                                    |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        

#### `def _get_attribute_vi_boolean(self, attribute_id)`

_get_attribute_vi_boolean

        | Queries the value of a ViBoolean property.
        | You can use this method to get the values of device-specific
          properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_boolean`

        Args:
            attribute_id (int): Specifies the ID of a property. From the method panel window, you
                can use this control as follows.

                -  In the method panel window, click on the control or press **Enter**
                   or the spacebar to display a dialog box containing hierarchical list
                   of the available properties. Help text is shown for each property.
                   Select a property by double-clicking on it or by selecting it and
                   then pressing **Enter**.
                -  A ring control at the top of the dialog box allows you to see all IVI
                   properties or only the properties of type ViBoolean. If you choose to
                   see all IVI properties, the data types appear to the right of the
                   property names in the list box. Properties with data types other
                   than ViBoolean are dim. If you select a property data type that is
                   dim, LabWindows/CVI transfers you to the method panel for the
                   corresponding method that is consistent with the data type.
                -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
                   change this ring control to a manual input box. If the property in
                   this ring control has named constants as valid values, you can view
                   the constants by moving to the value control and pressing **Enter**.


        Returns:
            attribute_value (bool): Returns the current value of the property. Passes the address of a
                ViBoolean variable.
                If the property currently showing in the property ring control has
                constants as valid values, you can view a list of the constants by
                pressing **Enter** on this control. Select a value by double-clicking on
                it or by selecting it and then pressing **Enter**.

        

#### `def _get_attribute_vi_int32(self, attribute_id)`

_get_attribute_vi_int32

        | Queries the value of a ViInt32 property.
        | You can use this method to get the values of device-specific
          properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_int32`

        Args:
            attribute_id (int): Specifies the ID of a property. From the method panel window, you
                can use this control as follows.

                -  In the method panel window, click on the control or press **Enter**
                   or the spacebar to display a dialog box containing hierarchical list
                   of the available properties. Help text is shown for each property.
                   Select a property by double-clicking on it or by selecting it and
                   then pressing **Enter**.
                -  A ring control at the top of the dialog box allows you to see all IVI
                   properties or only the properties of type ViInt32. If you choose to
                   see all IVI properties, the data types appear to the right of the
                   property names in the list box. Properties with data types other
                   than ViInt32 are dim. If you select a property data type that is
                   dim, LabWindows/CVI transfers you to the method panel for the
                   corresponding method that is consistent with the data type.
                -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
                   change this ring control to a manual input box. If the property in
                   this ring control has named constants as valid values, you can view
                   the constants by moving to the value control and pressing **Enter**.


        Returns:
            attribute_value (int): Returns the current value of the property. Passes the address of a
                ViInt32 variable.
                If the property currently showing in the property ring control has
                constants as valid values, you can view a list of the constants by
                pressing **Enter** on this control. Select a value by double-clicking on
                it or by selecting it and then pressing **Enter**.

        

#### `def _get_attribute_vi_int64(self, attribute_id)`

_get_attribute_vi_int64

        | Queries the value of a ViInt64 property.
        | You can use this method to get the values of device-specific
          properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_int64`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_int64`

        Args:
            attribute_id (int): Specifies the ID of a property. From the method panel window, you
                can use this control as follows.

                -  In the method panel window, click on the control or press **Enter**
                   or the spacebar to display a dialog box containing hierarchical list
                   of the available properties. Help text is shown for each property.
                   Select a property by double-clicking on it or by selecting it and
                   then pressing **Enter**.
                -  A ring control at the top of the dialog box allows you to see all IVI
                   properties or only the properties of type ViReal64. If you choose to
                   see all IVI properties, the data types appear to the right of the
                   property names in the list box. Properties with data types other
                   than ViReal64 are dim. If you select a property data type that is
                   dim, LabWindows/CVI transfers you to the method panel for the
                   corresponding method that is consistent with the data type.
                -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
                   change this ring control to a manual input box. If the property in
                   this ring control has named constants as valid values, you can view
                   the constants by moving to the value control and pressing **Enter**.


        Returns:
            attribute_value (int): Returns the current value of the property. Passes the address of a
                ViReal64 variable.
                If the property currently showing in the property ring control has
                constants as valid values, you can view a list of the constants by
                pressing **Enter** on this control. Select a value by double-clicking on
                it or by selecting it and then pressing **Enter**.

        

#### `def _get_attribute_vi_real64(self, attribute_id)`

_get_attribute_vi_real64

        | Queries the value of a ViReal64 property.
        | You can use this method to get the values of device-specific
          properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_real64`

        Args:
            attribute_id (int): Specifies the ID of a property. From the method panel window, you
                can use this control as follows.

                -  In the method panel window, click on the control or press **Enter**
                   or the spacebar to display a dialog box containing hierarchical list
                   of the available properties. Help text is shown for each property.
                   Select a property by double-clicking on it or by selecting it and
                   then pressing **Enter**.
                -  A ring control at the top of the dialog box allows you to see all IVI
                   properties or only the properties of type ViReal64. If you choose to
                   see all IVI properties, the data types appear to the right of the
                   property names in the list box. Properties with data types other
                   than ViReal64 are dim. If you select a property data type that is
                   dim, LabWindows/CVI transfers you to the method panel for the
                   corresponding method that is consistent with the data type.
                -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
                   change this ring control to a manual input box. If the property in
                   this ring control has named constants as valid values, you can view
                   the constants by moving to the value control and pressing **Enter**.


        Returns:
            attribute_value (float): Returns the current value of the property. Passes the address of a
                ViReal64 variable.
                If the property currently showing in the property ring control has
                constants as valid values, you can view a list of the constants by
                pressing **Enter** on this control. Select a value by double-clicking on
                it or by selecting it and then pressing **Enter**.

        

#### `def _get_attribute_vi_string(self, attribute_id)`

_get_attribute_vi_string

        | Queries the value of a ViString property.
        | You can use this method to get the values of device-specific
          properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_string`

        Args:
            attribute_id (int): Specifies the ID of a property. From the method panel window, you
                can use this control as follows.

                -  In the method panel window, click on the control or press or the
                   spacebar to display a dialog box containing hierarchical list of the
                   available properties. Help text is shown for each property. Select
                   a property by double-clicking on it or by selecting it and then
                   pressing .
                -  A ring control at the top of the dialog box allows you to see all IVI
                   properties or only the properties of type ViString. If you choose to
                   see all IVI properties, the data types appear to the right of the
                   property names in the list box. Properties with data types other
                   than ViString are dimmed. If you select a property data type that
                   is dimmed, LabWindows/CVI transfers you to the method panel for the
                   corresponding method that is consistent with the data type.
                -  If you want to enter a variable name, press to change this ring
                   control to a manual input control. If the property in this ring
                   control has named constants as valid values, you can view the
                   constants by moving to the value control and pressing .


        Returns:
            attribute_value (str): The buffer in which the method returns the current value of the
                property. The buffer must be of type ViChar and have at least as many
                bytes as indicated in **bufSize**.
                If the current value of the property, including the terminating NUL
                byte, contains more bytes that you indicate in this property, the
                method copies (buffer size -1) bytes into the buffer, places an ASCII
                NUL byte at the end of the buffer, and returns the buffer size you must
                pass to get the entire value. For example, if the value is 123456 and
                the buffer size is 4, the method places 123 into the buffer and
                returns 7.
                If you specify 0 for **bufSize**, you can pass VI_NULL for this
                property.
                If the property currently showing in the property ring control has
                constants as valid values, you can view a list of the constants by
                pressing on this control. Select a value by double-clicking on it or by
                selecting it and then pressing .

        

#### `def _get_channel_names(self, indices)`

_get_channel_names

        Returns a list of channel names for the given channel indices.

        Args:
            indices (basic sequence types, str, or int): Index list for the channels in the session. Valid values are from zero to the total number of channels in the session minus one. The index string can be one of the following formats:

                -   A comma-separated list—for example, "0,2,3,1"
                -   A range using a hyphen—for example, "0-3"
                -   A range using a colon—for example, "0:3 "

                You can combine comma-separated lists and ranges that use a hyphen or colon. Both out-of-order and repeated indices are supported ("2,3,0", "1,2,2,3"). White space characters, including spaces, tabs, feeds, and carriage returns, are allowed between characters. Ranges can be incrementing or decrementing.


        Returns:
            names (list of str): The channel name(s) at the specified indices.

        

#### `def get_lcr_compensation_data(self)`

get_lcr_compensation_data

        Collects previously generated open, short, load, and custom cable compensation data so you can then apply it to LCR measurements with configure_lcr_compensation.

        Call this method after you have obtained the compensation data of all types (open, short, load, open custom cable compensation, and short custom cable compensation) you want to apply to your measurements. Pass the **compensation data** to configure_lcr_compensation

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].get_lcr_compensation_data`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.get_lcr_compensation_data`

        Returns:
            compensation_data (bytes): The open, short, load, and custom cable compensation data to retrieve.

        

#### `def _get_lcr_compensation_last_date_and_time(self, compensation_type)`

_get_lcr_compensation_last_date_and_time

        Returns the date and time the specified type of compensation data for LCR measurements was most recently generated.
        The time returned is 24-hour (military) local time; for example, if the selected type of compensation data was generated at 2:30 PM, this method returns 14 for **hours** and 30 for **minutes**.

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_lcr_compensation_last_date_and_time`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._get_lcr_compensation_last_date_and_time`

        Args:
            compensation_type (enums.LCRCompensationType): Specifies the type of compensation for LCR measurements.


        Returns:
            year (int): Returns the year of the relevant operation.

            month (int): Returns the month of the relevant operation.

            day (int): Returns the day of the relevant operation.

            hour (int): Returns the hour (in 24-hour time) of the relevant operation.

            minute (int): Returns the minute of the relevant operation.

        

#### `def get_lcr_custom_cable_compensation_data(self)`

get_lcr_custom_cable_compensation_data

        This method is deprecated. Use get_lcr_compensation_data
        instead.

        Collects previously generated open and short custom cable compensation data so you can then apply it to LCR measurements with configure_lcr_custom_cable_compensation.

        Call this method after you have obtained open and short custom cable compensation data. Pass the **custom cable compensation data** to configure_lcr_custom_cable_compensation

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].get_lcr_custom_cable_compensation_data`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.get_lcr_custom_cable_compensation_data`

        Returns:
            custom_cable_compensation_data (bytes): The open and short custom cable compensation data to retrieve.

        

#### `def get_lcr_compensation_last_date_and_time(self, compensation_type)`

get_lcr_compensation_last_date_and_time

        Returns the date and time the specified type of compensation data for LCR measurements was most recently generated.

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].get_lcr_compensation_last_date_and_time`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.get_lcr_compensation_last_date_and_time`

        Args:
            compensation_type (enums.LCRCompensationType): Specifies the type of compensation for LCR measurements.


        Returns:
            last_comp_datetime (hightime.datetime): Returns the date and time the specified type of compensation data for LCR measurements was most recently generated.

        

#### `def _initiate_with_channels(self)`

_initiate_with_channels

        Starts generation or acquisition, causing the specified channel(s) to
        leave the Uncommitted state or Committed state and enter the Running
        state. To return to the Uncommitted state call the abort
        method. Refer to the `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in
        the *NI DC Power Supplies and SMUs Help* for information about the
        specific NI-DCPower software states.

        **Related Topics:**

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._initiate_with_channels`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._initiate_with_channels`
        

#### `def lock(self)`

lock

        Obtains a multithread lock on the device session. Before doing so, the
        software waits until all other execution threads release their locks
        on the device session.

        Other threads may have obtained a lock on this session for the
        following reasons:

            -  The application called the lock method.
            -  A call to NI-DCPower locked the session.
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
            lock (context manager): When used in a with statement, nidcpower.Session.lock acts as
            a context manager and unlock will be called when the with block is exited
        

#### `def measure(self, measurement_type)`

measure

        Returns the measured value of either the voltage or current on the
        specified channel. Each call to this method blocks other
        method calls until the hardware returns the **measurement**. To
        measure multiple channels, use the measure_multiple
        method.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].measure`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.measure`

        Args:
            measurement_type (enums.MeasurementTypes): Specifies whether a voltage or current value is measured.
                **Defined Values**:

                +--------------------------+------------------------------+
                | MeasurementTypes.VOLTAGE | The device measures voltage. |
                +--------------------------+------------------------------+
                | MeasurementTypes.CURRENT | The device measures current. |
                +--------------------------+------------------------------+


        Returns:
            measurement (float): Returns the value of the measurement, either in volts for voltage or
                amps for current.

        

#### `def _measure_multiple(self)`

_measure_multiple

        Returns arrays of the measured voltage and current values on the
        specified channel(s). Each call to this method blocks other
        method calls until the measurements are returned from the device. The
        order of the measurements returned in the array corresponds to the order
        on the specified channel(s).

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._measure_multiple`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._measure_multiple`

        Returns:
            voltage_measurements (array.array("d")): Returns an array of voltage measurements. The measurements in the array
                are returned in the same order as the channels specified in
                **channelName**. Ensure that sufficient space has been allocated for the
                returned array.

            current_measurements (array.array("d")): Returns an array of current measurements. The measurements in the array
                are returned in the same order as the channels specified in
                **channelName**. Ensure that sufficient space has been allocated for the
                returned array.

        

#### `def _measure_multiple_lcr(self)`

_measure_multiple_lcr

        Measures and returns a list of LCRMeasurement instances on the specified channel(s).

        To use this method:

        -  Set instrument_mode property to InstrumentMode.LCR
        -  Set measure_when property to MeasureWhen.ON_DEMAND
        -  Put the channel(s) in the Running state (call initiate)

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._measure_multiple_lcr`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._measure_multiple_lcr`

        Returns:
            measurements (list of LCRMeasurement): A list of LCRMeasurement instances.

                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | vdc                   | float                | The measured DC voltage, in volts.                                                                                                                                                                    |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | idc                   | float                | The measured DC current, in amps.                                                                                                                                                                     |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | stimulus_frequency    | float                | The frequency of the LCR test signal, in Hz.                                                                                                                                                          |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ac_voltage            | complex              | The measured AC voltage, in volts RMS.                                                                                                                                                                |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ac_current            | complex              | The measured AC current, in amps RMS.                                                                                                                                                                 |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | z                     | complex              | The complex impedance.                                                                                                                                                                                |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | z_magnitude_and_phase | tuple of float       | The magnitude, in ohms, and phase angle, in degrees, of the complex impedance.                                                                                                                        |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | y                     | complex              | The complex admittance.                                                                                                                                                                               |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | y_magnitude_and_phase | tuple of float       | The magnitude, in siemens, and phase angle, in degrees, of the complex admittance.                                                                                                                    |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | series_lcr            | LCR                  | The inductance, in henrys, the capacitance, in farads, and the resistance, in ohms, as measured using a series circuit model.                                                                         |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | parallel_lcr          | LCR                  | The inductance, in henrys, the capacitance, in farads, and the resistance, in ohms, as measured using a parallel circuit model.                                                                       |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | d                     | float                | The dissipation factor of the circuit. The dimensionless dissipation factor is directly proportional to how quickly an oscillating system loses energy. D is the reciprocal of Q, the quality factor. |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | q                     | float                | The quality factor of the circuit. The dimensionless quality factor is inversely proportional to the degree of damping in a system. Q is the reciprocal of D, the dissipation factor.                 |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | measurement_mode      | enums.InstrumentMode | The measurement mode: **SMU** - The channel(s) are operating as a power supply/SMU. **LCR** - The channel(s) are operating as an LCR meter.                                                           |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | dc_in_compliance      | bool                 | Indicates whether the output was in DC compliance at the time the measurement was taken.                                                                                                              |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | ac_in_compliance      | bool                 | Indicates whether the output was in AC compliance at the time the measurement was taken.                                                                                                              |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | unbalanced            | bool                 | Indicates whether the output was unbalanced at the time the measurement was taken.                                                                                                                    |
                +-----------------------+----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        

#### `def _parse_channel_count(self)`

_parse_channel_count

        Returns the number of channels.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._parse_channel_count`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._parse_channel_count`

        Returns:
            number_of_channels (int):

        

#### `def perform_lcr_load_compensation(self, compensation_spots)`

perform_lcr_load_compensation

        Generates load compensation data for LCR measurements for the test spots you specify.

        You must physically configure your LCR circuit with an appropriate reference load to use this method to generate valid load compensation data.

        When you call this method:

        -  The load compensation data is written to the onboard storage of the instrument. Onboard storage can contain only the most recent set of data.
        -  Most NI-DCPower properties in the session are reset to their default values. Rewrite the values of any properties you want to maintain.

        To apply the load compensation data you generate with this method to your LCR measurements, set the lcr_load_compensation_enabled property to True.

        Load compensation data are generated only for those specific frequencies you define with this method; load compensation is not interpolated from the specific frequencies you define and applied to other frequencies.

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].perform_lcr_load_compensation`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.perform_lcr_load_compensation`

        Args:
            compensation_spots (list of LCRLoadCompensationSpot): Defines the frequencies and DUT specifications to use for LCR load compensation.

                You can specify <=1000 spot frequencies.

                +----------------------+----------------------------------------------------------------------------------------------------------------------------------------+
                | frequency            | The spot frequency, in Hz.                                                                                                             |
                +----------------------+----------------------------------------------------------------------------------------------------------------------------------------+
                | reference_value_type | A known specification value of your DUT to use as the basis for load compensation.                                                     |
                +----------------------+----------------------------------------------------------------------------------------------------------------------------------------+
                | reference_value      | A value that describes the **reference_value_type** specification. Use as indicated by the **reference_value_type** option you choose. |
                +----------------------+----------------------------------------------------------------------------------------------------------------------------------------+

        

#### `def perform_lcr_open_compensation(self, additional_frequencies=None)`

perform_lcr_open_compensation

        Generates open compensation data for LCR measurements based on a default set of test frequencies and, optionally, additional frequencies you can specify.

        You must physically configure an open LCR circuit to use this method to generate valid open compensation data.

        When you call this method:

        -  The open compensation data is written to the onboard storage of the instrument. Onboard storage can contain only the most recent set of data.
        -  Most NI-DCPower properties in the session are reset to their default values. Rewrite the values of any properties you want to maintain.

        To apply the open compensation data you generate with this method to your LCR measurements, set the lcr_open_compensation_enabled property to True.

        Corrections for frequencies other than the default frequencies or any additional frequencies you specify are interpolated.

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Note:
        Default Open Compensation Frequencies:
        By default, NI-DCPower uses the following frequencies for LCR open compensation:

        -  10 logarithmic steps at 1 kHz frequency decade
        -  10 logarithmic steps at 10 kHz frequency decade
        -  100 logarithmic steps at 100 kHz frequency decade
        -  100 logarithmic steps at 1 MHz frequency decade

        The actual frequencies used depend on the bandwidth of your instrument.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].perform_lcr_open_compensation`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.perform_lcr_open_compensation`

        Args:
            additional_frequencies (list of float): Defines a further set of frequencies, in addition to the default frequencies, to perform the compensation for. You can specify <=200 additional frequencies.

        

#### `def perform_lcr_open_custom_cable_compensation(self)`

perform_lcr_open_custom_cable_compensation

        Generates open custom cable compensation data for LCR measurements.

        To use this method, you must physically configure an open LCR circuit to generate valid open custom cable compensation data.

        When you call this method:

        -  The open compensation data is written to the onboard storage of the instrument. Onboard storage can contain only the most recent set of data.
        -  Most NI-DCPower properties in the session are reset to their default values. Rewrite the values of any properties you want to maintain.

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].perform_lcr_open_custom_cable_compensation`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.perform_lcr_open_custom_cable_compensation`
        

#### `def perform_lcr_short_compensation(self, additional_frequencies=None)`

perform_lcr_short_compensation

        Generates short compensation data for LCR measurements based on a default set of test frequencies and, optionally, additional frequencies you can specify.

        You must physically configure your LCR circuit with a short to use this method to generate valid short compensation data.

        When you call this method:

        -  The short compensation data is written to the onboard storage of the instrument. Onboard storage can contain only the most recent set of data.
        - Most NI-DCPower properties in the session are reset to their default values. Rewrite the values of any properties you want to maintain.

        To apply the short compensation data you generate with this method to your LCR measurements, set the lcr_short_compensation_enabled property to True.

        Corrections for frequencies other than the default frequencies or any additional frequencies you specify are interpolated.

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Note:
        Default Short Compensation Frequencies:
        By default, NI-DCPower uses the following frequencies for LCR short compensation:

        -  10 logarithmic steps at 1 kHz frequency decade
        -  10 logarithmic steps at 10 kHz frequency decade
        -  100 logarithmic steps at 100 kHz frequency decade
        -  100 logarithmic steps at 1 MHz frequency decade

        The actual frequencies used depend on the bandwidth of your instrument.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].perform_lcr_short_compensation`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.perform_lcr_short_compensation`

        Args:
            additional_frequencies (list of float): Defines a further set of frequencies, in addition to the default frequencies, to perform the compensation for. You can specify <=200 additional frequencies.

        

#### `def perform_lcr_short_custom_cable_compensation(self)`

perform_lcr_short_custom_cable_compensation

        Generates short custom cable compensation data for LCR measurements.

        To use this method:

        -  You must physically configure your LCR circuit with a short to generate valid short custom cable compensation data.
        -  Set lcr_short_custom_cable_compensation_enabled property to True

        When you call this method:

        -  The short compensation data is written to the onboard storage of the instrument. Onboard storage can contain only the most recent set of data.
        -  Most NI-DCPower properties in the session are reset to their default values. Rewrite the values of any properties you want to maintain.

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].perform_lcr_short_custom_cable_compensation`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.perform_lcr_short_custom_cable_compensation`
        

#### `def query_in_compliance(self)`

query_in_compliance

        Queries the specified channel to determine if it is operating at the compliance limit.

        The compliance limit is the current limit when the output_function property is set to OutputFunction.DC_VOLTAGE, OutputFunction.PULSE_VOLTAGE, OutputFunction.CONSTANT_RESISTANCE or OutputFunction.CONSTANT_POWER. If the output is operating at the compliance limit, the output reaches the current limit before the desired voltage, resistance or power level.

        The compliance limit is the voltage limit when the output_function property is set to OutputFunction.DC_CURRENT or OutputFunction.PULSE_CURRENT. If the output is operating at the compliance limit, the output reaches the voltage limit before the desired current level.

        Refer to the output_function property for more information about the applicable properties to configure for each output method.

        Note:
        NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].query_in_compliance`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.query_in_compliance`

        Returns:
            in_compliance (bool): Returns whether the device channel is in compliance.

        

#### `def query_latched_output_cutoff_state(self, output_cutoff_reason)`

query_latched_output_cutoff_state

        Discovers if an output cutoff limit was exceeded for the specified reason. When an output cutoff is engaged, the output of the channel(s) is disconnected.
        If a limit was exceeded, the state is latched until you clear it with the clear_latched_output_cutoff_state method or the reset method.

        outputCutoffReason specifies the conditions for which an output is disconnected.

        Note:
        NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].query_latched_output_cutoff_state`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.query_latched_output_cutoff_state`

        Args:
            output_cutoff_reason (enums.OutputCutoffReason): Specifies which output cutoff conditions to query.

                +-----------------------------------------+--------------------------------------------------------------------------------------+
                | OutputCutoffReason.ALL                  | Any output cutoff condition was met                                                  |
                +-----------------------------------------+--------------------------------------------------------------------------------------+
                | OutputCutoffReason.VOLTAGE_OUTPUT_HIGH  | The output exceeded the high cutoff limit for voltage output                         |
                +-----------------------------------------+--------------------------------------------------------------------------------------+
                | OutputCutoffReason.VOLTAGE_OUTPUT_LOW   | The output fell below the low cutoff limit for voltage output                        |
                +-----------------------------------------+--------------------------------------------------------------------------------------+
                | OutputCutoffReason.VOLTAGE_MEASURE_HIGH | The measured voltage exceeded the high cutoff limit for voltage output               |
                +-----------------------------------------+--------------------------------------------------------------------------------------+
                | OutputCutoffReason.VOLTAGE_MEASURE_LOW  | The measured voltage fell below the low cutoff limit for voltage output              |
                +-----------------------------------------+--------------------------------------------------------------------------------------+
                | OutputCutoffReason.CURRENT_MEASURE_HIGH | The measured current exceeded the high cutoff limit for current output               |
                +-----------------------------------------+--------------------------------------------------------------------------------------+
                | OutputCutoffReason.CURRENT_MEASURE_LOW  | The measured current fell below the low cutoff limit for current output              |
                +-----------------------------------------+--------------------------------------------------------------------------------------+
                | OutputCutoffReason.VOLTAGE_CHANGE_HIGH  | The voltage slew rate increased beyond the positive change cutoff for voltage output |
                +-----------------------------------------+--------------------------------------------------------------------------------------+
                | OutputCutoffReason.VOLTAGE_CHANGE_LOW   | The voltage slew rate decreased beyond the negative change cutoff for voltage output |
                +-----------------------------------------+--------------------------------------------------------------------------------------+
                | OutputCutoffReason.CURRENT_CHANGE_HIGH  | The current slew rate increased beyond the positive change cutoff for current output |
                +-----------------------------------------+--------------------------------------------------------------------------------------+
                | OutputCutoffReason.CURRENT_CHANGE_LOW   | The current slew rate decreased beyond the negative change cutoff for current output |
                +-----------------------------------------+--------------------------------------------------------------------------------------+
                | OutputCutoffReason.CURRENT_SATURATED    | The measured current saturates the current range                                     |
                +-----------------------------------------+--------------------------------------------------------------------------------------+


        Returns:
            output_cutoff_state (bool): Specifies whether an output cutoff has engaged.

                +-------+------------------------------------------------------------------------------+
                | True  | An output cutoff has engaged for the conditions in **output cutoff reason**. |
                +-------+------------------------------------------------------------------------------+
                | False | No output cutoff has engaged.                                                |
                +-------+------------------------------------------------------------------------------+

        

#### `def query_max_current_limit(self, voltage_level)`

query_max_current_limit

        Queries the maximum current limit on a channel if the channel is set to the specified **voltageLevel**.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].query_max_current_limit`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.query_max_current_limit`

        Args:
            voltage_level (float): Specifies the voltage level to use when calculating the
                **maxCurrentLimit**.


        Returns:
            max_current_limit (float): Returns the maximum current limit that can be set with the specified
                **voltageLevel**.

        

#### `def query_max_voltage_level(self, current_limit)`

query_max_voltage_level

        Queries the maximum voltage level on a channel if the channel is set to the specified **currentLimit**.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].query_max_voltage_level`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.query_max_voltage_level`

        Args:
            current_limit (float): Specifies the current limit to use when calculating the
                **maxVoltageLevel**.


        Returns:
            max_voltage_level (float): Returns the maximum voltage level that can be set on a channel
                with the specified **currentLimit**.

        

#### `def query_min_current_limit(self, voltage_level)`

query_min_current_limit

        Queries the minimum current limit on a channel if the channel is set to the specified **voltageLevel**.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].query_min_current_limit`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.query_min_current_limit`

        Args:
            voltage_level (float): Specifies the voltage level to use when calculating the
                **minCurrentLimit**.


        Returns:
            min_current_limit (float): Returns the minimum current limit that can be set on a channel
                with the specified **voltageLevel**.

        

#### `def query_output_state(self, output_state)`

query_output_state

        Queries the specified channel to determine if the channel
        is currently in the state specified by **outputState**.

        **Related Topics:**

        `Compliance <REPLACE_DRIVER_SPECIFIC_URL_1(compliance)>`__

        Note:
        NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].query_output_state`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.query_output_state`

        Args:
            output_state (enums.OutputStates): Specifies the output state of the channel that is being queried.
                **Defined Values**:

                +-------------------------------+--------------------------------------------------------------------+
                | OutputStates.CONSTANT_VOLTAGE | The channel maintains a constant voltage by adjusting the current. |
                +-------------------------------+--------------------------------------------------------------------+
                | OutputStates.CONSTANT_CURRENT | The channel maintains a constant current by adjusting the voltage. |
                +-------------------------------+--------------------------------------------------------------------+
                | OutputStates.INHIBITED        | The channel is in the inhibited state.                             |
                +-------------------------------+--------------------------------------------------------------------+


        Returns:
            in_state (bool): Returns whether the device channel is in the specified output
                state.

        

#### `def reset(self)`

reset

        Resets the specified channel(s) to a known state. This method disables power
        generation, resets session properties to their default values, commits
        the session properties, and leaves the session in the Uncommitted state.
        Refer to the `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic for
        more information about NI-DCPower software states.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].reset`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.reset`
        

#### `def send_software_edge_trigger(self, trigger)`

send_software_edge_trigger

        Asserts the specified trigger. This method can override an external
        edge trigger.

        **Related Topics:**

        `Triggers <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].send_software_edge_trigger`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.send_software_edge_trigger`

        Args:
            trigger (enums.SendSoftwareEdgeTriggerType): Specifies which trigger to assert.
                **Defined Values:**

                +----------------------------------------------+---------------------------------------+
                | SendSoftwareEdgeTriggerType.START            | Asserts the Start trigger.            |
                +----------------------------------------------+---------------------------------------+
                | SendSoftwareEdgeTriggerType.SOURCE           | Asserts the Source trigger.           |
                +----------------------------------------------+---------------------------------------+
                | SendSoftwareEdgeTriggerType.MEASURE          | Asserts the Measure trigger.          |
                +----------------------------------------------+---------------------------------------+
                | SendSoftwareEdgeTriggerType.SEQUENCE_ADVANCE | Asserts the Sequence Advance trigger. |
                +----------------------------------------------+---------------------------------------+
                | SendSoftwareEdgeTriggerType.PULSE            | Asserts the Pulse trigger.            |
                +----------------------------------------------+---------------------------------------+
                | SendSoftwareEdgeTriggerType.SHUTDOWN         | Asserts the Shutdown trigger.         |
                +----------------------------------------------+---------------------------------------+

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        

#### `def _set_attribute_vi_boolean(self, attribute_id, attribute_value)`

_set_attribute_vi_boolean

        | Sets the value of a ViBoolean property.
        | This is a low-level method that you can use to set the values of
          device-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_boolean`

        Args:
            attribute_id (int): Specifies the ID of a property. From the method panel window, you
                can use this control as follows.

                -  In the method panel window, click on the control or press **Enter**
                   or the spacebar to display a dialog box containing hierarchical list
                   of the available properties. Properties whose value cannot be set are
                   dim. Help text is shown for each property. Select a property by
                   double-clicking on it or by selecting it and then pressing **Enter**.
                -  Read-only properties appear dim in the list box. If you select a
                   read-only property, an error message appears. A ring control at the
                   top of the dialog box allows you to see all IVI properties or only
                   the properties of type ViBoolean. If you choose to see all IVI
                   properties, the data types appear to the right of the property names
                   in the list box. Properties with data types other than ViBoolean are
                   dim. If you select a property data type that is dim, LabWindows/CVI
                   transfers you to the method panel for the corresponding method
                   that is consistent with the data type.
                -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
                   change this ring control to a manual input box. If the property in
                   this ring control has named constants as valid values, you can view
                   the constants by moving to the value control and pressing **Enter**.

            attribute_value (bool): Specifies the value to which you want to set the property. If the
                property currently showing in the property ring control has constants
                as valid values, you can view a list of the constants by pressing
                **Enter** on this control. Select a value by double-clicking on it or by
                selecting it and then pressing **Enter**.

                Note:
                Some of the values might not be valid depending upon the current
                settings of the device session.

        

#### `def _set_attribute_vi_int32(self, attribute_id, attribute_value)`

_set_attribute_vi_int32

        | Sets the value of a ViInt32 property.
        | This is a low-level method that you can use to set the values of
          device-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_int32`

        Args:
            attribute_id (int): Specifies the ID of a property. From the method panel window, you
                can use this control as follows.

                -  In the method panel window, click on the control or press **Enter**
                   or the spacebar to display a dialog box containing hierarchical list
                   of the available properties. Properties whose value cannot be set are
                   dim. Help text is shown for each property. Select a property by
                   double-clicking on it or by selecting it and then pressing **Enter**.
                -  Read-only properties appear dim in the list box. If you select a
                   read-only property, an error message appears. A ring control at the
                   top of the dialog box allows you to see all IVI properties or only
                   the properties of type ViInt32. If you choose to see all IVI
                   properties, the data types appear to the right of the property names
                   in the list box. Properties with data types other than ViInt32 are
                   dim. If you select a property data type that is dim, LabWindows/CVI
                   transfers you to the method panel for the corresponding method
                   that is consistent with the data type.
                -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
                   change this ring control to a manual input box. If the property in
                   this ring control has named constants as valid values, you can view
                   the constants by moving to the value control and pressing **Enter**.

            attribute_value (int): Specifies the value to which you want to set the property. If the
                property currently showing in the property ring control has constants
                as valid values, you can view a list of the constants by pressing
                **Enter** on this control. Select a value by double-clicking on it or by
                selecting it and then pressing **Enter**.

                Note:
                Some of the values might not be valid depending upon the current
                settings of the device session.

        

#### `def _set_attribute_vi_int64(self, attribute_id, attribute_value)`

_set_attribute_vi_int64

        | Sets the value of a ViInt64 property.
        | This is a low-level method that you can use to set the values of
          device-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_int64`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_int64`

        Args:
            attribute_id (int): Specifies the ID of a property. From the method panel window, you
                can use this control as follows.

                -  In the method panel window, click on the control or press **Enter**
                   or the spacebar to display a dialog box containing hierarchical list
                   of the available properties. Properties whose value cannot be set are
                   dim. Help text is shown for each property. Select a property by
                   double-clicking on it or by selecting it and then pressing **Enter**.
                -  Read-only properties appear dim in the list box. If you select a
                   read-only property, an error message appears. A ring control at the
                   top of the dialog box allows you to see all IVI properties or only
                   the properties of type ViReal64. If you choose to see all IVI
                   properties, the data types appear to the right of the property names
                   in the list box. Properties with data types other than ViReal64 are
                   dim. If you select a property data type that is dim, LabWindows/CVI
                   transfers you to the method panel for the corresponding method
                   that is consistent with the data type.
                -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
                   change this ring control to a manual input box. If the property in
                   this ring control has named constants as valid values, you can view
                   the constants by moving to the value control and pressing **Enter**.

            attribute_value (int): Specifies the value to which you want to set the property. If the
                property currently showing in the property ring control has constants
                as valid values, you can view a list of the constants by pressing
                **Enter** on this control. Select a value by double-clicking on it or by
                selecting it and then pressing **Enter**.

                Note:
                Some of the values might not be valid depending upon the current
                settings of the device session.

        

#### `def _set_attribute_vi_real64(self, attribute_id, attribute_value)`

_set_attribute_vi_real64

        | Sets the value of a ViReal64 property.
        | This is a low-level method that you can use to set the values of
          device-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_real64`

        Args:
            attribute_id (int): Specifies the ID of a property. From the method panel window, you
                can use this control as follows.

                -  In the method panel window, click on the control or press **Enter**
                   or the spacebar to display a dialog box containing hierarchical list
                   of the available properties. Properties whose value cannot be set are
                   dim. Help text is shown for each property. Select a property by
                   double-clicking on it or by selecting it and then pressing **Enter**.
                -  Read-only properties appear dim in the list box. If you select a
                   read-only property, an error message appears. A ring control at the
                   top of the dialog box allows you to see all IVI properties or only
                   the properties of type ViReal64. If you choose to see all IVI
                   properties, the data types appear to the right of the property names
                   in the list box. Properties with data types other than ViReal64 are
                   dim. If you select a property data type that is dim, LabWindows/CVI
                   transfers you to the method panel for the corresponding method
                   that is consistent with the data type.
                -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
                   change this ring control to a manual input box. If the property in
                   this ring control has named constants as valid values, you can view
                   the constants by moving to the value control and pressing **Enter**.

            attribute_value (float): Specifies the value to which you want to set the property. If the
                property currently showing in the property ring control has constants
                as valid values, you can view a list of the constants by pressing
                **Enter** on this control. Select a value by double-clicking on it or by
                selecting it and then pressing **Enter**.

                Note:
                Some of the values might not be valid depending upon the current
                settings of the device session.

        

#### `def _set_attribute_vi_string(self, attribute_id, attribute_value)`

_set_attribute_vi_string

        | Sets the value of a ViString property.
        | This is a low-level method that you can use to set the values of
          device-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_string`

        Args:
            attribute_id (int): Specifies the ID of a property. From the method panel window, you
                can use this control as follows.

                -  In the method panel window, click on the control or press **Enter**
                   or the spacebar to display a dialog box containing hierarchical list
                   of the available properties. Properties whose value cannot be set are
                   dim. Help text is shown for each property. Select a property by
                   double-clicking on it or by selecting it and then pressing **Enter**.
                -  Read-only properties appear dim in the list box. If you select a
                   read-only property, an error message appears. A ring control at the
                   top of the dialog box allows you to see all IVI properties or only
                   the properties of type ViString. If you choose to see all IVI
                   properties, the data types appear to the right of the property names
                   in the list box. Properties with data types other than ViString are
                   dim. If you select a property data type that is dim, LabWindows/CVI
                   transfers you to the method panel for the corresponding method
                   that is consistent with the data type.
                -  If you want to enter a variable name, press **Ctrl**\ +\ **T** to
                   change this ring control to a manual input box. If the property in
                   this ring control has named constants as valid values, you can view
                   the constants by moving to the value control and pressing **Enter**.

            attribute_value (str): Specifies the value to which you want to set the property. If the
                property currently showing in the property ring control has constants
                as valid values, you can view a list of the constants by pressing
                **Enter** on this control. Select a value by double-clicking on it or by
                selecting it and then pressing **Enter**.

                Note:
                Some of the values might not be valid depending upon the current
                settings of the device session.

        

#### `def set_sequence(self, values, source_delays)`

set_sequence

        Configures a series of voltage, current, resistance or power outputs and corresponding source delays. The source mode must be set to SourceMode.SEQUENCE for this method to take effect.

        Refer to the Configuring the Source Unit topic in the *NI DC Power Supplies and SMUs Help* for more information about how to configure your device.

        Use this method in the Uncommitted or Committed programming states.
        Refer to the Programming States topic in the *NI DC Power Supplies and SMUs Help* for more information about NI-DCPower programming states.

        Using this method with Advanced Sequence methods for the same channel in the same session is not supported.

        Note:
        NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].set_sequence`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.set_sequence`

        Args:
            values (list of float): Specifies the series of voltage, current, resistance or power levels, depending on the configured output_function.
                **Valid values**: The valid values for this parameter are defined by the voltage level range, current level range, constant resistance level range or constant power level range.

            source_delays (list of float): Specifies the source delay that follows the configuration of each value
                in the sequence.
                **Valid Values**:
                The valid values are between 0 and 167 seconds.

        

#### `def unlock(self)`

unlock

        Releases a lock that you acquired on an device session using
        lock. Refer to lock for additional
        information on session locks.
        

#### `def wait_for_event(self, event_id, timeout=hightime.timedelta(seconds=10.0))`

wait_for_event

        Waits until the specified channel(s) have generated the specified event.

        The session monitors whether each type of event has occurred at least
        once since the last time this method or the initiate
        method were called. If an event has only been generated once and you
        call this method successively, the method times out. Individual
        events must be generated between separate calls of this method.

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Tip:
        This method can be called on specific channels within your :py:class:`nidcpower.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].wait_for_event`

        To call the method on all channels, you can call it directly on the :py:class:`nidcpower.Session`.

        Example: :py:meth:`my_session.wait_for_event`

        Args:
            event_id (enums.Event): Specifies which event to wait for.
                **Defined Values:**

                +-----------------------------------+--------------------------------------------------+
                | Event.SOURCE_COMPLETE             | Waits for the Source Complete event.             |
                +-----------------------------------+--------------------------------------------------+
                | Event.MEASURE_COMPLETE            | Waits for the Measure Complete event.            |
                +-----------------------------------+--------------------------------------------------+
                | Event.SEQUENCE_ITERATION_COMPLETE | Waits for the Sequence Iteration Complete event. |
                +-----------------------------------+--------------------------------------------------+
                | Event.SEQUENCE_ENGINE_DONE        | Waits for the Sequence Engine Done event.        |
                +-----------------------------------+--------------------------------------------------+
                | Event.PULSE_COMPLETE              | Waits for the Pulse Complete event.              |
                +-----------------------------------+--------------------------------------------------+
                | Event.READY_FOR_PULSE_TRIGGER     | Waits for the Ready for Pulse Trigger event.     |
                +-----------------------------------+--------------------------------------------------+

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): Specifies the maximum time allowed for this method to complete, in
                seconds. If the method does not complete within this time interval,
                NI-DCPower returns an error.

                Note:
                When setting the timeout interval, ensure you take into account any
                triggers so that the timeout interval is long enough for your
                application.

        

#### `def _error_message(self, error_code)`

_error_message

        Converts a status code returned by an instrument driver method into a
        user-readable string.

        Args:
            error_code (int): Specifies the **status** parameter that is returned from any of the
                NI-DCPower methods.


        Returns:
            error_message (str): Returns the user-readable message string that corresponds to the status
                code you specify.
                You must pass a ViChar array with at least 256 bytes.

        

### `class Session(_SessionBase)`

An NI-DCPower session to an NI programmable power supply or source measure unit.

#### `def __init__(self, resource_name, channels=None, reset=False, options={}, independent_channels=True, *, grpc_options=None)`

An NI-DCPower session to an NI programmable power supply or source measure unit.

        Creates and returns a new NI-DCPower session to the instrument(s) and channel(s) specified
        in **resource name** to be used in all subsequent NI-DCPower method calls. With this method,
        you can optionally set the initial state of the following session properties:

        -  simulate
        -  driver_setup

        After calling this method, the specified channel or channels will be in the Uncommitted
        state.

        To place channel(s) in a known start-up state when creating a new session, set **reset** to
        True. This action is equivalent to using the reset method immediately after initializing the
        session.

        To open a session and leave the channel(s) in an existing configuration without passing
        through a transitional output state, set **reset** to False. Next, configure the channel(s)
        as in the previous session, change the desired settings, and then call the initiate method
        to write both settings.

        **Details of Independent Channel Operation**

        With this method and channel-based NI-DCPower methods and properties, you can use any
        channels in the session independently. For example, you can initiate a subset of channels in
        the session with initiate, and the other channels in the session remain in the Uncommitted
        state.

        When you initialize with independent channels, each channel steps through the NI-DCPower
        programming state model independently of all other channels, and you can specify a subset of
        channels for most operations.

        **Note** You can make concurrent calls to a session from multiple threads, but the session
        executes the calls one at a time. If you specify multiple channels for a method or property,
        the session may perform the operation on multiple channels in parallel, though this is not
        guaranteed, and some operations may execute sequentially.

        Args:
            resource_name (str, list, tuple): Specifies the **resource name** as seen in Measurement
                & Automation Explorer (MAX) or lsni, for example "PXI1Slot3" where "PXI1Slot3" is an
                instrument's **resource name**. If independent_channels is False, **resource name**
                can also be a logical IVI name.

                If independent_channels is True, **resource name** can be names of the instrument(s)
                and the channel(s) to initialize. Specify the instrument(s) and channel(s) using the
                form "PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or
                PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3", where "PXI1Slot3" and "PXI1Slot4" are
                instrument resource names followed by channels. If you exclude a channels string
                after an instrument resource name, all channels of the instrument(s) are included in
                the session.

            channels (str, list, range, tuple): For new applications, use the default value of None
                and specify the channels in **resource name**.

                Specifies which channel(s) to include in a new session. Specify multiple
                channels by using a channel list or a channel range. A channel list is a comma (,)
                separated sequence of channel names (for example, 0,2 specifies channels 0 and 2).
                A channel range is a lower bound channel followed by a hyphen (-) or colon (:)
                followed by an upper bound channel (for example, 0-2 specifies channels 0, 1,
                and 2).

                If independent_channels is False, this argument specifies which channels to include
                in a legacy synchronized channels session. If you do not specify any channels, by
                default all channels on the device are included in the session.

                If independent_channels is True, this argument combines with **resource name** to
                specify which channels to include in an independent channels session. Initializing
                an independent channels session with a channels argument is deprecated.

            reset (bool): Specifies whether to reset channel(s) during the initialization procedure.

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

            independent_channels (bool): Specifies whether to initialize the session with
                independent channels. Set this argument to False on legacy applications or if you
                are unable to upgrade your NI-DCPower driver runtime to 20.6 or higher.

            grpc_options (nidcpower.grpc_session_options.GrpcSessionOptions): MeasurementLink gRPC session options


        Returns:
            session (nidcpower.Session): A session object representing the device.

        

#### `def __enter__(self)`

#### `def __exit__(self, exc_type, exc_value, traceback)`

#### `def close(self)`

close

        Closes the session specified in **vi** and deallocates the resources
        that NI-DCPower reserves. If power output is enabled when you call this
        method, the channels remain in their existing state and
        continue providing power. Use the ConfigureOutputEnabled
        method to disable power output on a per channel basis. Use the
        reset method to disable power output on all channel(s).

        **Related Topics:**

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        Note:
        NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

        Note:
        One or more of the referenced methods are not in the Python API for this driver.

        Note:
        This method is not needed when using the session context manager
        

#### `def disable(self)`

disable

        This method performs the same actions as the reset
        method, except that this method also immediately sets the
        output_enabled property to False.

        This method opens the output relay on devices that have an output
        relay.

        Note:
        NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.
        

#### `def export_attribute_configuration_buffer(self)`

export_attribute_configuration_buffer

        Exports the property configuration of the session to the specified
        configuration buffer.

        You can export and import session property configurations only between
        devices with identical model numbers and the same number of configured
        channels.

        This method verifies that the properties you have configured for the
        session are valid. If the configuration is invalid, NI‑DCPower returns
        an error.

        **Support for this Method**

        Calling this method in `Sequence Source
        Mode <REPLACE_DRIVER_SPECIFIC_URL_1(sequencing)>`__ is unsupported.

        **Channel Mapping Behavior for Multichannel Sessions**

        When importing and exporting session property configurations between
        NI‑DCPower sessions that were initialized with different channels, the
        configurations of the exporting channels are mapped to the importing
        channels in the order you specify in the **channelName** input to the
        __init__ method.

        For example, if your entry for **channelName** is 0,1 for the exporting
        session and 1,2 for the importing session:

        -  The configuration exported from channel 0 is imported into channel 1.
        -  The configuration exported from channel 1 is imported into channel 2.

        **Related Topics:**

        `Using Properties and
        Properties <REPLACE_DRIVER_SPECIFIC_URL_1(using_properties_and_attributes)>`__

        `Setting Properties and Properties Before Reading
        Them <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

        Note:
        This method will return an error if the total number of channels
        initialized for the exporting session is not equal to the total number
        of channels initialized for the importing session.

        Returns:
            configuration (bytes): Specifies the byte array buffer to be populated with the exported
                property configuration.

        

#### `def export_attribute_configuration_file(self, file_path)`

export_attribute_configuration_file

        Exports the property configuration of the session to the specified
        file.

        You can export and import session property configurations only between
        devices with identical model numbers and the same number of configured
        channels.

        This method verifies that the properties you have configured for the
        session are valid. If the configuration is invalid, NI‑DCPower returns
        an error.

        **Support for this Method**

        Calling this method in `Sequence Source
        Mode <REPLACE_DRIVER_SPECIFIC_URL_1(sequencing)>`__ is unsupported.

        **Channel Mapping Behavior for Multichannel Sessions**

        When importing and exporting session property configurations between
        NI‑DCPower sessions that were initialized with different channels, the
        configurations of the exporting channels are mapped to the importing
        channels in the order you specify in the **channelName** input to the
        __init__ method.

        For example, if your entry for **channelName** is 0,1 for the exporting
        session and 1,2 for the importing session:

        -  The configuration exported from channel 0 is imported into channel 1.
        -  The configuration exported from channel 1 is imported into channel 2.

        **Related Topics:**

        `Using Properties and
        Properties <REPLACE_DRIVER_SPECIFIC_URL_1(using_properties_and_attributes)>`__

        `Setting Properties and Properties Before Reading
        Them <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

        Note:
        This method will return an error if the total number of channels
        initialized for the exporting session is not equal to the total number
        of channels initialized for the importing session.

        Args:
            file_path (str): Specifies the absolute path to the file to contain the exported
                property configuration. If you specify an empty or relative path, this
                method returns an error.
                **Default file extension:** .nidcpowerconfig

        

#### `def _fancy_initialize(self, resource_name, channels=None, reset=False, option_string='', independent_channels=True)`

_fancy_initialize

        Creates and returns a new NI-DCPower session to the instrument(s) and channel(s) specified
        in **resource name** to be used in all subsequent NI-DCPower method calls. With this method,
        you can optionally set the initial state of the following session properties:

        -  simulate
        -  driver_setup

        After calling this method, the specified channel or channels will be in the Uncommitted
        state.

        To place channel(s) in a known start-up state when creating a new session, set **reset** to
        True. This action is equivalent to using the reset method immediately after initializing the
        session.

        To open a session and leave the channel(s) in an existing configuration without passing
        through a transitional output state, set **reset** to False. Next, configure the channel(s)
        as in the previous session, change the desired settings, and then call the initiate method
        to write both settings.

        **Details of Independent Channel Operation**

        With this method and channel-based NI-DCPower methods and properties, you can use any
        channels in the session independently. For example, you can initiate a subset of channels in
        the session with initiate, and the other channels in the session remain in the Uncommitted
        state.

        When you initialize with independent channels, each channel steps through the NI-DCPower
        programming state model independently of all other channels, and you can specify a subset of
        channels for most operations.

        **Note** You can make concurrent calls to a session from multiple threads, but the session
        executes the calls one at a time. If you specify multiple channels for a method or property,
        the session may perform the operation on multiple channels in parallel, though this is not
        guaranteed, and some operations may execute sequentially.

        Args:
            resource_name (str, list, tuple): Specifies the **resource name** as seen in Measurement
                & Automation Explorer (MAX) or lsni, for example "PXI1Slot3" where "PXI1Slot3" is an
                instrument's **resource name**. If independent_channels is False, **resource name**
                can also be a logical IVI name.

                If independent_channels is True, **resource name** can be names of the instrument(s)
                and the channel(s) to initialize. Specify the instrument(s) and channel(s) using the
                form "PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3 or
                PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3", where "PXI1Slot3" and "PXI1Slot4" are
                instrument resource names followed by channels. If you exclude a channels string
                after an instrument resource name, all channels of the instrument(s) are included in
                the session.

            channels (str, list, range, tuple): For new applications, use the default value of None
                and specify the channels in **resource name**.

                Specifies which channel(s) to include in a new session. Specify multiple
                channels by using a channel list or a channel range. A channel list is a comma (,)
                separated sequence of channel names (for example, 0,2 specifies channels 0 and 2).
                A channel range is a lower bound channel followed by a hyphen (-) or colon (:)
                followed by an upper bound channel (for example, 0-2 specifies channels 0, 1,
                and 2).

                If independent_channels is False, this argument specifies which channels to include
                in a legacy synchronized channels session. If you do not specify any channels, by
                default all channels on the device are included in the session.

                If independent_channels is True, this argument combines with **resource name** to
                specify which channels to include in an independent channels session. Initializing
                an independent channels session with a channels argument is deprecated.

            reset (bool): Specifies whether to reset channel(s) during the initialization procedure.

            option_string (dict): Specifies the initial value of certain properties for the session.
                The syntax for **optionString** is a list of properties with an assigned value where
                1 is True and 0 is False. For example:

                Simulate=0, DriverSetup=Model:<model number>; BoardType:<bus connector>

                To simulate a multi-instrument session when independent_channels is True, set
                Simulate to 1 and list multiple instruments for DriverSetup. For example:

                Simulate=1, DriverSetup=ResourceName:<instrument name>; Model:<model number>;
                BoardType:<bus connector> & ResourceName:<resource name>; Model:<model number>;
                BoardType:<bus connector>

                You do not have to specify a value for all the properties. If you do not specify a
                value for a property, the default value is used.

            independent_channels (bool): Specifies whether to initialize the session with
                independent channels. Set this argument to False on legacy applications or if you
                are unable to upgrade your NI-DCPower driver runtime to 20.6 or higher.


        Returns:
            vi (int): Returns a session handle that you use to identify the device in all
                subsequent NI-DCPower method calls.

        

#### `def get_channel_name(self, index)`

get_channel_name

        Retrieves the output **channelName** that corresponds to the requested
        **index**. Use the channel_count property to
        determine the upper bound of valid values for **index**.

        Args:
            index (int): Specifies which channel name to return. The index values begin at
                1.


        Returns:
            channel_name (str): Returns the channel name that corresponds to **index**.

        

#### `def _get_ext_cal_last_date_and_time(self)`

_get_ext_cal_last_date_and_time

        Returns the date and time of the last successful calibration. The time
        returned is 24-hour (military) local time; for example, if the device
        was calibrated at 2:30 PM, this method returns 14 for **hours** and 30
        for **minutes**.

        Returns:
            year (int): Returns the **year** the device was last calibrated.

            month (int): Returns the **month** in which the device was last calibrated.

            day (int): Returns the **day** on which the device was last calibrated.

            hour (int): Returns the **hour** (in 24-hour time) in which the device was last
                calibrated.

            minute (int): Returns the **minute** in which the device was last calibrated.

        

#### `def get_ext_cal_last_temp(self)`

get_ext_cal_last_temp

        Returns the onboard **temperature** of the device, in degrees Celsius,
        during the last successful external calibration.

        Returns:
            temperature (float): Returns the onboard **temperature** of the device, in degrees Celsius,
                during the last successful external calibration.

        

#### `def get_ext_cal_recommended_interval(self)`

get_ext_cal_recommended_interval

        Returns the recommended maximum interval, in **months**, between
        external calibrations.

        Returns:
            months (hightime.timedelta): Specifies the recommended maximum interval, in **months**, between
                external calibrations.

        

#### `def get_ext_cal_last_date_and_time(self)`

get_ext_cal_last_date_and_time

        Returns the date and time of the last successful calibration.

        Returns:
            last_cal_datetime (hightime.datetime): Indicates date and time of the last calibration.

        

#### `def get_self_cal_last_date_and_time(self)`

get_self_cal_last_date_and_time

        Returns the date and time of the oldest successful self-calibration from among the channels in the session.

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Returns:
            last_cal_datetime (hightime.datetime): Returns the date and time the device was last calibrated.

        

#### `def _get_self_cal_last_date_and_time(self)`

_get_self_cal_last_date_and_time

        Returns the date and time of the oldest successful self-calibration from
        among the channels in the session.

        The time returned is 24-hour (military) local time; for example, if you
        have a session using channels 1 and 2, and a self-calibration was
        performed on channel 1 at 2:30 PM, and a self-calibration was performed
        on channel 2 at 3:00 PM on the same day, this method returns 14 for
        **hours** and 30 for **minutes**.

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Returns:
            year (int): Returns the **year** the device was last calibrated.

            month (int): Returns the **month** in which the device was last calibrated.

            day (int): Returns the **day** on which the device was last calibrated.

            hour (int): Returns the **hour** (in 24-hour time) in which the device was last
                calibrated.

            minute (int): Returns the **minute** in which the device was last calibrated.

        

#### `def get_self_cal_last_temp(self)`

get_self_cal_last_temp

        Returns the onboard temperature of the device, in degrees Celsius,
        during the oldest successful self-calibration from among the channels in
        the session.

        For example, if you have a session using channels 1 and 2, and you
        perform a self-calibration on channel 1 with a device temperature of 25
        degrees Celsius at 2:00, and a self-calibration was performed on channel
        2 at 27 degrees Celsius at 3:00 on the same day, this method returns
        25 for the **temperature** parameter.

        Note:
        This method is not supported on all devices. For more information about supported devices, search ni.com for Supported Methods by Device.

        Returns:
            temperature (float): Returns the onboard **temperature** of the device, in degrees Celsius,
                during the oldest successful calibration.

        

#### `def import_attribute_configuration_buffer(self, configuration)`

import_attribute_configuration_buffer

        Imports a property configuration to the session from the specified
        configuration buffer.

        You can export and import session property configurations only between
        devices with identical model numbers and the same number of configured
        channels.

        **Support for this Method**

        Calling this method in `Sequence Source
        Mode <REPLACE_DRIVER_SPECIFIC_URL_1(sequencing)>`__ is unsupported.

        **Channel Mapping Behavior for Multichannel Sessions**

        When importing and exporting session property configurations between
        NI‑DCPower sessions that were initialized with different channels, the
        configurations of the exporting channels are mapped to the importing
        channels in the order you specify in the **channelName** input to the
        __init__ method.

        For example, if your entry for **channelName** is 0,1 for the exporting
        session and 1,2 for the importing session:

        -  The configuration exported from channel 0 is imported into channel 1.
        -  The configuration exported from channel 1 is imported into channel 2.

        **Related Topics:**

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        `Using Properties and
        Properties <REPLACE_DRIVER_SPECIFIC_URL_1(using_properties_and_attributes)>`__

        `Setting Properties and Properties Before Reading
        Them <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

        Note:
        This method will return an error if the total number of channels
        initialized for the exporting session is not equal to the total number
        of channels initialized for the importing session.

        Args:
            configuration (bytes): Specifies the byte array buffer that contains the property
                configuration to import.

        

#### `def import_attribute_configuration_file(self, file_path)`

import_attribute_configuration_file

        Imports a property configuration to the session from the specified
        file.

        You can export and import session property configurations only between
        devices with identical model numbers and the same number of configured
        channels.

        **Support for this Method**

        Calling this method in `Sequence Source
        Mode <REPLACE_DRIVER_SPECIFIC_URL_1(sequencing)>`__ is unsupported.

        **Channel Mapping Behavior for Multichannel Sessions**

        When importing and exporting session property configurations between
        NI‑DCPower sessions that were initialized with different channels, the
        configurations of the exporting channels are mapped to the importing
        channels in the order you specify in the **channelName** input to the
        __init__ method.

        For example, if your entry for **channelName** is 0,1 for the exporting
        session and 1,2 for the importing session:

        -  The configuration exported from channel 0 is imported into channel 1.
        -  The configuration exported from channel 1 is imported into channel 2.

        **Related Topics:**

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        `Using Properties and
        Properties <REPLACE_DRIVER_SPECIFIC_URL_1(using_properties_and_attributes)>`__

        `Setting Properties and Properties Before Reading
        Them <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

        Note:
        This method will return an error if the total number of channels
        initialized for the exporting session is not equal to the total number
        of channels initialized for the importing session.

        Args:
            file_path (str): Specifies the absolute path to the file containing the property
                configuration to import. If you specify an empty or relative path, this
                method returns an error.
                **Default File Extension:** .nidcpowerconfig

        

#### `def _initialize_with_channels(self, resource_name, channels, reset, option_string)`

_initialize_with_channels

        Creates and returns a new NI-DCPower session to the instrument
        specified in **resource name** to be used in all subsequent NI-DCPower
        method calls. With this method, you can optionally set the initial
        state of the following session properties:

        -  simulate
        -  driver_setup

        After calling this method, the session will be in the Uncommitted
        state. Refer to the `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic for
        details about specific software states.

        To place the device in a known start-up state when creating a new
        session, set **reset** to True. This action is equivalent to using
        the reset method immediately after initializing the
        session.

        To open a session and leave the device in its existing configuration
        without passing through a transitional output state, set **reset** to
        False. Then configure the device as in the previous session,
        changing only the desired settings, and then call the
        initiate method.

        **Related Topics:**

        `Programming States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        Args:
            resource_name (str): Specifies the **resourceName** assigned by Measurement & Automation
                Explorer (MAX), for example "PXI1Slot3" where "PXI1Slot3" is an
                instrument's **resourceName**. **resourceName** can also be a logical
                IVI name.

            channels (str): Specifies which channel(s) to include in a new session. Specify
                multiple channels by using a channel list or a channel range. A channel
                list is a comma (,) separated sequence of channel names (for example,
                0,2 specifies channels 0 and 2). A channel range is a lower bound
                channel followed by a hyphen (-) or colon (:) followed by an upper bound
                channel (for example, 0-2 specifies channels 0, 1, and 2). In the
                Running state, multiple channel configurations are performed
                sequentially based on the order specified in this parameter. If you do
                not specify any channels, by default all channels on the device are
                included in the session.

            reset (bool): Specifies whether to reset the device during the initialization
                procedure.

            option_string (str): Specifies the initial value of certain properties for the session.
                The syntax for **optionString** is a list of properties with an assigned
                value where 1 is True and 0 is False. For example:

                "Simulate=0"

                You do not have to specify a value for all the properties. If you do not
                specify a value for a property, the default value is used.

                For more information about simulating a device, refer to `Simulating an
                Instrument <REPLACE_DRIVER_SPECIFIC_URL_1(simulate)>`__.


        Returns:
            vi (int): Returns a session handle that you use to identify the device in all
                subsequent NI-DCPower method calls.

        

#### `def _initialize_with_independent_channels(self, resource_name, reset, option_string)`

_initialize_with_independent_channels

        Creates a new NI-DCPower session to the specified instrument(s) and channel(s) and returns a
        session handle to be used in all subsequent NI-DCPower method calls.

        After calling this method, the specified channel or channels will be in the Uncommitted
        state.

        With this method and channel-based NI-DCPower methods and properties, you can use any
        channels in the session independently. For example, you can initiate a subset of channels in
        the session with initiate, and the other channels in the session
        remain in the Uncommitted state.

        **Details of Independent Channel Operation**

        When you initialize with independent channels, each channel steps through the NI-DCPower
        programming state model independently of all other channels, and you can specify a subset
        of channels for most operations.

        **Note** You can make concurrent calls to a session from multiple threads, but the session
        executes the calls one at a time. If you specify multiple channels for a method or
        property, the session may perform the operation on multiple channels in parallel, though
        this is not guaranteed, and some operations may execute sequentially.

        **Related Topics:**

        `Programming States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        Args:
            resource_name (str): Specifies the NI-DCPower resources to use in the session.
                NI-DCPower resources can be names of the instrument(s) assigned by Measurement &
                Automation Explorer (MAX) and the channel(s) to initialize. Specify the
                instrument(s) and channel(s) using the form PXI1Slot3/0,PXI1Slot3/2-3,PXI1Slot4/2-3
                or PXI1Slot3/0,PXI1Slot3/2:3,PXI1Slot4/2:3, where PXI1Slot3 and PXI1Slot4 are
                instrument resource names and 0, 2, and 3 are channels.

                If you pass "" for this control, all channels of the instrument(s) are included in
                the session.

            reset (bool): Specifies whether to reset channel(s) during the initialization procedure.
                The default is False.

                To place channel(s) in a known startup state when creating a new session, set
                **reset** to True. This action is equivalent to using the reset
                method immediately after initializing the session.

                To open a session and leave the channel(s) in an existing configuration without
                passing through a transitional output state, set **reset** to False. Next, configure
                the channel(s) as in the previous session, change the desired settings, and then
                call the initiate method to write both settings.

            option_string (str): Specifies the initial value of certain properties for the session.
                The syntax for **optionString** is a list of properties with an assigned value where
                1 is True and 0 is False. For example:

                Simulate=0, DriverSetup=Model:<model number>; BoardType:<bus connector>

                To simulate a multi-instrument session, set Simulate to 1 and list multiple
                instruments for DriverSetup. For example:

                Simulate=1, DriverSetup=ResourceName:<instrument name>; Model:<model number>;
                BoardType:<bus connector> & ResourceName:<resource name>; Model:<model number>;
                BoardType:<bus connector>

                You do not have to specify a value for all the properties. If you do not specify a
                value for a property, the default value is used.

                For more information about simulating a device, refer to `Simulating an
                Instrument <REPLACE_DRIVER_SPECIFIC_URL_1(simulate)>`__.


        Returns:
            vi (int): Returns a session handle that you use to identify the session in all
                subsequent NI-DCPower method calls.

        

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

        

#### `def read_current_temperature(self)`

read_current_temperature

        Returns the current onboard **temperature**, in degrees Celsius, of the
        device.

        Returns:
            temperature (float): Returns the onboard **temperature**, in degrees Celsius, of the device.

        

#### `def reset_device(self)`

reset_device

        Resets the device to a known state. The method disables power
        generation, resets session properties to their default values, clears
        errors such as overtemperature and unexpected loss of auxiliary power,
        commits the session properties, and leaves the session in the
        Uncommitted state. This method also performs a hard reset on the
        device and driver software. This method has the same functionality as
        using reset in Measurement & Automation Explorer. Refer to the
        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic for
        more information about NI-DCPower software states.

        This will also open the output relay on devices that have an output
        relay.

        Note:
        NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.
        

#### `def reset_with_defaults(self)`

reset_with_defaults

        Resets the device to a known state. This method disables power
        generation, resets session properties to their default values, commits
        the session properties, and leaves the session in the
        `Running <javascript:LaunchHelp('NI_DC_Power_Supplies_Help.chm::/programmingStates.html#running')>`__
        state. In addition to exhibiting the behavior of the reset
        method, this method can assign user-defined default values for
        configurable properties from the IVI configuration.
        

#### `def _close(self)`

_close

        Closes the session specified in **vi** and deallocates the resources
        that NI-DCPower reserves. If power output is enabled when you call this
        method, the channels remain in their existing state and
        continue providing power. Use the ConfigureOutputEnabled
        method to disable power output on a per channel basis. Use the
        reset method to disable power output on all channel(s).

        **Related Topics:**

        `Programming
        States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

        Note:
        NI-DCPower uses the terms "source" and "output". However, while sinking with electronic loads and SMUs these correspond to "sinking" and "input", respectively.

        Note:
        One or more of the referenced methods are not in the Python API for this driver.
        

#### `def self_test(self)`

self_test

        Performs the device self-test routine and returns the test result(s).
        Calling this method implicitly calls the reset method.

        When calling self_test with the PXIe-4162/4163, specify all
        channels of your PXIe-4162/4163 with the channels input of
        __init__. You cannot self test a subset of
        PXIe-4162/4163 channels.

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
        

#### `def _self_test(self)`

_self_test

        Performs the device self-test routine and returns the test result(s).
        Calling this method implicitly calls the reset method.

        When calling self_test with the PXIe-4162/4163, specify all
        channels of your PXIe-4162/4163 with the channels input of
        __init__. You cannot self test a subset of
        PXIe-4162/4163 channels.

        Returns:
            self_test_result (int): Returns the value result from the device self-test.

                +----------------+-------------------+
                | Self-Test Code | Description       |
                +================+===================+
                | 0              | Self test passed. |
                +----------------+-------------------+
                | 1              | Self test failed. |
                +----------------+-------------------+

            self_test_message (str): Returns the self-test result message. The size of this array must be at
                least 256 bytes.

        

<!--NI_PYTHON_API repo=nimi-python path=generated/nidcpower/nidcpower/unit_tests/_matchers.py -->
## PYTHON MODULE: generated/nidcpower/nidcpower/unit_tests/_matchers.py

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

<!--NI_PYTHON_API repo=nimi-python path=generated/nidcpower/nidcpower/unit_tests/_mock_helper.py -->
## PYTHON MODULE: generated/nidcpower/nidcpower/unit_tests/_mock_helper.py

### `class MockFunctionCallError(Exception)`

#### `def __init__(self, function, param=None)`

### `class SideEffectsHelper(object)`

#### `def __init__(self)`

#### `def __getitem__(self, func)`

#### `def __setitem__(self, func, val)`

#### `def niDCPower_AbortWithChannels(self, vi, channel_name)`

#### `def niDCPower_CalSelfCalibrate(self, vi, channel_name)`

#### `def niDCPower_ClearLatchedOutputCutoffState(self, vi, channel_name, output_cutoff_reason)`

#### `def niDCPower_CommitWithChannels(self, vi, channel_name)`

#### `def niDCPower_ConfigureApertureTime(self, vi, channel_name, aperture_time, units)`

#### `def niDCPower_ConfigureLCRCompensation(self, vi, channel_name, compensation_data_size, compensation_data)`

#### `def niDCPower_ConfigureLCRCustomCableCompensation(self, vi, channel_name, custom_cable_compensation_data_size, custom_cable_compensation_data)`

#### `def niDCPower_CreateAdvancedSequenceCommitStepWithChannels(self, vi, channel_name, set_as_active_step)`

#### `def niDCPower_CreateAdvancedSequenceStepWithChannels(self, vi, channel_name, set_as_active_step)`

#### `def niDCPower_CreateAdvancedSequenceWithChannels(self, vi, channel_name, sequence_name, attribute_id_count, attribute_ids, set_as_active_sequence)`

#### `def niDCPower_DeleteAdvancedSequenceWithChannels(self, vi, channel_name, sequence_name)`

#### `def niDCPower_Disable(self, vi)`

#### `def niDCPower_ExportAttributeConfigurationBuffer(self, vi, size, configuration)`

#### `def niDCPower_ExportAttributeConfigurationFile(self, vi, file_path)`

#### `def niDCPower_FancyInitialize(self, resource_name, channels, reset, option_string, vi, independent_channels)`

#### `def niDCPower_FetchMultiple(self, vi, channel_name, timeout, count, voltage_measurements, current_measurements, in_compliance, actual_count)`

#### `def niDCPower_FetchMultipleLCR(self, vi, channel_name, timeout, count, measurements, actual_count)`

#### `def niDCPower_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niDCPower_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niDCPower_GetAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niDCPower_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niDCPower_GetAttributeViString(self, vi, channel_name, attribute_id, buffer_size, attribute_value)`

#### `def niDCPower_GetChannelName(self, vi, index, buffer_size, channel_name)`

#### `def niDCPower_GetChannelNameFromString(self, vi, indices, buffer_size, names)`

#### `def niDCPower_GetError(self, vi, code, buffer_size, description)`

#### `def niDCPower_GetExtCalLastDateAndTime(self, vi, year, month, day, hour, minute)`

#### `def niDCPower_GetExtCalLastTemp(self, vi, temperature)`

#### `def niDCPower_GetExtCalRecommendedInterval(self, vi, months)`

#### `def niDCPower_GetLCRCompensationData(self, vi, channel_name, compensation_data_size, compensation_data)`

#### `def niDCPower_GetLCRCompensationLastDateAndTime(self, vi, channel_name, compensation_type, year, month, day, hour, minute)`

#### `def niDCPower_GetLCRCustomCableCompensationData(self, vi, channel_name, custom_cable_compensation_data_size, custom_cable_compensation_data)`

#### `def niDCPower_GetSelfCalLastDateAndTime(self, vi, year, month, day, hour, minute)`

#### `def niDCPower_GetSelfCalLastTemp(self, vi, temperature)`

#### `def niDCPower_ImportAttributeConfigurationBuffer(self, vi, size, configuration)`

#### `def niDCPower_ImportAttributeConfigurationFile(self, vi, file_path)`

#### `def niDCPower_InitializeWithChannels(self, resource_name, channels, reset, option_string, vi)`

#### `def niDCPower_InitializeWithIndependentChannels(self, resource_name, reset, option_string, vi)`

#### `def niDCPower_InitiateWithChannels(self, vi, channel_name)`

#### `def niDCPower_LockSession(self, vi, caller_has_lock)`

#### `def niDCPower_Measure(self, vi, channel_name, measurement_type, measurement)`

#### `def niDCPower_MeasureMultiple(self, vi, channel_name, voltage_measurements, current_measurements)`

#### `def niDCPower_MeasureMultipleLCR(self, vi, channel_name, measurements)`

#### `def niDCPower_ParseChannelCount(self, vi, channels_string, number_of_channels)`

#### `def niDCPower_PerformLCRLoadCompensation(self, vi, channel_name, num_compensation_spots, compensation_spots)`

#### `def niDCPower_PerformLCROpenCompensation(self, vi, channel_name, num_frequencies, additional_frequencies)`

#### `def niDCPower_PerformLCROpenCustomCableCompensation(self, vi, channel_name)`

#### `def niDCPower_PerformLCRShortCompensation(self, vi, channel_name, num_frequencies, additional_frequencies)`

#### `def niDCPower_PerformLCRShortCustomCableCompensation(self, vi, channel_name)`

#### `def niDCPower_QueryInCompliance(self, vi, channel_name, in_compliance)`

#### `def niDCPower_QueryLatchedOutputCutoffState(self, vi, channel_name, output_cutoff_reason, output_cutoff_state)`

#### `def niDCPower_QueryMaxCurrentLimit(self, vi, channel_name, voltage_level, max_current_limit)`

#### `def niDCPower_QueryMaxVoltageLevel(self, vi, channel_name, current_limit, max_voltage_level)`

#### `def niDCPower_QueryMinCurrentLimit(self, vi, channel_name, voltage_level, min_current_limit)`

#### `def niDCPower_QueryOutputState(self, vi, channel_name, output_state, in_state)`

#### `def niDCPower_ReadCurrentTemperature(self, vi, temperature)`

#### `def niDCPower_ResetDevice(self, vi)`

#### `def niDCPower_ResetWithChannels(self, vi, channel_name)`

#### `def niDCPower_ResetWithDefaults(self, vi)`

#### `def niDCPower_SendSoftwareEdgeTriggerWithChannels(self, vi, channel_name, trigger)`

#### `def niDCPower_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niDCPower_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niDCPower_SetAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niDCPower_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niDCPower_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value)`

#### `def niDCPower_SetRuntimeEnvironment(self, environment, environment_version, reserved1, reserved2)`

#### `def niDCPower_SetSequence(self, vi, channel_name, values, source_delays, size)`

#### `def niDCPower_UnlockSession(self, vi, caller_has_lock)`

#### `def niDCPower_WaitForEventWithChannels(self, vi, channel_name, event_id, timeout)`

#### `def niDCPower_close(self, vi)`

#### `def niDCPower_error_message(self, vi, error_code, error_message)`

#### `def niDCPower_self_test(self, vi, self_test_result, self_test_message)`

#### `def set_side_effects_and_return_values(self, mock_library)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nidcpower/nidcpower/unit_tests/test_nidcpower.py -->
## PYTHON MODULE: generated/nidcpower/nidcpower/unit_tests/test_nidcpower.py

### `def test_lcr_measurement(ctype_members, channel, expected_python_members, expected_python_str)`

### `def test_lcr_load_compensation_spot(python_init_params, expected_repr, expected_str, expected_ctype_members)`

### `def test_lcr_load_compensation_spot_byte_packing_alignment()`

<!--NI_PYTHON_API repo=nimi-python path=generated/nidcpower/setup.py -->
## PYTHON MODULE: generated/nidcpower/setup.py

### `def read_contents(file_to_read)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nidigital/nidigital/__init__.py -->
## PYTHON MODULE: generated/nidigital/nidigital/__init__.py

### `def get_diagnostic_information()`

Get diagnostic information about the system state that is suitable for printing or logging

    returns: dict

    note: Python bitness may be incorrect when running in a virtual environment
    

### `def print_diagnostic_information()`

Print diagnostic information in a format suitable for issue report

    note: Python bitness may be incorrect when running in a virtual environment
    

<!--NI_PYTHON_API repo=nimi-python path=generated/nidigital/nidigital/_attributes.py -->
## PYTHON MODULE: generated/nidigital/nidigital/_attributes.py

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

Class for attributes that use enums internally but are exposed in the nidigital Python module as something else, thus need conversion.

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

<!--NI_PYTHON_API repo=nimi-python path=generated/nidigital/nidigital/_converters.py -->
## PYTHON MODULE: generated/nidigital/nidigital/_converters.py

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
    

<!--NI_PYTHON_API repo=nimi-python path=generated/nidigital/nidigital/_grpc_stub_interpreter.py -->
## PYTHON MODULE: generated/nidigital/nidigital/_grpc_stub_interpreter.py

### `class GrpcStubInterpreter(object)`

Interpreter for interacting with a gRPC Stub class

#### `def __init__(self, grpc_options)`

#### `def set_session_handle(self, value=session_grpc_types.Session())`

#### `def get_session_handle(self)`

#### `def _invoke(self, func, request, metadata=None)`

#### `def abort(self)`

#### `def abort_keep_alive(self)`

#### `def apply_levels_and_timing(self, site_list, levels_sheet, timing_sheet, initial_state_high_pins, initial_state_low_pins, initial_state_tristate_pins)`

#### `def apply_tdr_offsets(self, channel_list, offsets)`

#### `def burst_pattern(self, site_list, start_label, select_digital_function, wait_until_done, timeout)`

#### `def clock_generator_abort(self, channel_list)`

#### `def clock_generator_generate_clock(self, channel_list, frequency, select_digital_function)`

#### `def commit(self)`

#### `def configure_active_load_levels(self, channel_list, iol, ioh, vcom)`

#### `def configure_pattern_burst_sites(self, site_list)`

#### `def configure_time_set_compare_edges_strobe(self, pin_list, time_set_name, strobe_edge)`

#### `def configure_time_set_compare_edges_strobe2x(self, pin_list, time_set_name, strobe_edge, strobe2_edge)`

#### `def configure_time_set_drive_edges(self, pin_list, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge)`

#### `def configure_time_set_drive_edges2x(self, pin_list, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge, drive_data2_edge, drive_return2_edge)`

#### `def configure_time_set_drive_format(self, pin_list, time_set_name, drive_format)`

#### `def configure_time_set_edge(self, pin_list, time_set_name, edge, time)`

#### `def configure_time_set_edge_multiplier(self, pin_list, time_set_name, edge_multiplier)`

#### `def configure_time_set_period(self, time_set_name, period)`

#### `def configure_voltage_levels(self, channel_list, vil, vih, vol, voh, vterm)`

#### `def create_capture_waveform_from_file_digicapture(self, waveform_name, waveform_file_path)`

#### `def create_capture_waveform_parallel(self, pin_list, waveform_name)`

#### `def create_capture_waveform_serial(self, pin_list, waveform_name, sample_width, bit_order)`

#### `def create_source_waveform_from_file_tdms(self, waveform_name, waveform_file_path, write_waveform_data)`

#### `def create_source_waveform_parallel(self, pin_list, waveform_name, data_mapping)`

#### `def create_source_waveform_serial(self, pin_list, waveform_name, data_mapping, sample_width, bit_order)`

#### `def create_time_set(self, name)`

#### `def delete_all_time_sets(self)`

#### `def disable_sites(self, site_list)`

#### `def enable_sites(self, site_list)`

#### `def fetch_capture_waveform(self, site_list, waveform_name, samples_to_read, timeout)`

#### `def fetch_history_ram_cycle_information(self, site, sample_index)`

#### `def fetch_history_ram_cycle_pin_data(self, site, pin_list, sample_index, dut_cycle_index)`

#### `def fetch_history_ram_scan_cycle_number(self, site, sample_index)`

#### `def frequency_counter_measure_frequency(self, channel_list)`

#### `def get_attribute_vi_boolean(self, channel_name, attribute)`

#### `def get_attribute_vi_int32(self, channel_name, attribute)`

#### `def get_attribute_vi_int64(self, channel_name, attribute)`

#### `def get_attribute_vi_real64(self, channel_name, attribute)`

#### `def get_attribute_vi_string(self, channel_name, attribute)`

#### `def get_channel_names(self, indices)`

#### `def get_error(self)`

#### `def get_fail_count(self, channel_list)`

#### `def get_history_ram_sample_count(self, site)`

#### `def get_pattern_name(self, pattern_index)`

#### `def get_pattern_pin_names(self, start_label)`

#### `def get_pin_name(self, pin_index)`

#### `def get_pin_results_pin_information(self, channel_list)`

#### `def get_site_pass_fail(self, site_list)`

#### `def get_site_results_site_numbers(self, site_list, site_result_type)`

#### `def get_time_set_drive_format(self, pin, time_set_name)`

#### `def get_time_set_edge(self, pin, time_set_name, edge)`

#### `def get_time_set_edge_multiplier(self, pin, time_set_name)`

#### `def get_time_set_name(self, time_set_index)`

#### `def get_time_set_period(self, time_set_name)`

#### `def init_with_options(self, resource_name, id_query, reset_device, option_string)`

#### `def initiate(self)`

#### `def is_done(self)`

#### `def is_site_enabled(self, site)`

#### `def load_levels(self, file_path)`

#### `def load_pattern(self, file_path)`

#### `def load_pin_map(self, file_path)`

#### `def load_specifications(self, file_path)`

#### `def load_timing(self, file_path)`

#### `def lock(self)`

#### `def ppmu_measure(self, channel_list, measurement_type)`

#### `def ppmu_source(self, channel_list)`

#### `def read_sequencer_flag(self, flag)`

#### `def read_sequencer_register(self, reg)`

#### `def read_static(self, channel_list)`

#### `def reset_device(self)`

#### `def self_calibrate(self)`

#### `def send_software_edge_trigger(self, trigger, trigger_identifier)`

#### `def set_attribute_vi_boolean(self, channel_name, attribute, value)`

#### `def set_attribute_vi_int32(self, channel_name, attribute, value)`

#### `def set_attribute_vi_int64(self, channel_name, attribute, value)`

#### `def set_attribute_vi_real64(self, channel_name, attribute, value)`

#### `def set_attribute_vi_string(self, channel_name, attribute, value)`

#### `def set_runtime_environment(self, environment, environment_version, reserved1, reserved2)`

#### `def tdr(self, channel_list, apply_offsets)`

#### `def unload_all_patterns(self, unload_keep_alive_pattern)`

#### `def unload_specifications(self, file_path)`

#### `def unlock(self)`

#### `def wait_until_done(self, timeout)`

#### `def write_sequencer_flag(self, flag, value)`

#### `def write_sequencer_register(self, reg, value)`

#### `def write_source_waveform_broadcast(self, waveform_name, waveform_data)`

#### `def write_source_waveform_data_from_file_tdms(self, waveform_name, waveform_file_path)`

#### `def write_source_waveform_site_unique_u32(self, site_list, waveform_name, num_waveforms, samples_per_waveform, waveform_data)`

#### `def write_static(self, channel_list, state)`

#### `def close(self)`

#### `def error_message(self, error_code)`

#### `def reset(self)`

#### `def self_test(self)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nidigital/nidigital/_library.py -->
## PYTHON MODULE: generated/nidigital/nidigital/_library.py

### `class Library(object)`

Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    

#### `def __init__(self, ctypes_library)`

#### `def _get_library_function(self, name)`

#### `def niDigital_Abort(self, vi)`

#### `def niDigital_AbortKeepAlive(self, vi)`

#### `def niDigital_ApplyLevelsAndTiming(self, vi, site_list, levels_sheet, timing_sheet, initial_state_high_pins, initial_state_low_pins, initial_state_tristate_pins)`

#### `def niDigital_ApplyTDROffsets(self, vi, channel_list, num_offsets, offsets)`

#### `def niDigital_BurstPattern(self, vi, site_list, start_label, select_digital_function, wait_until_done, timeout)`

#### `def niDigital_ClockGenerator_Abort(self, vi, channel_list)`

#### `def niDigital_ClockGenerator_GenerateClock(self, vi, channel_list, frequency, select_digital_function)`

#### `def niDigital_Commit(self, vi)`

#### `def niDigital_ConfigureActiveLoadLevels(self, vi, channel_list, iol, ioh, vcom)`

#### `def niDigital_ConfigurePatternBurstSites(self, vi, site_list)`

#### `def niDigital_ConfigureTimeSetCompareEdgesStrobe(self, vi, pin_list, time_set_name, strobe_edge)`

#### `def niDigital_ConfigureTimeSetCompareEdgesStrobe2x(self, vi, pin_list, time_set_name, strobe_edge, strobe2_edge)`

#### `def niDigital_ConfigureTimeSetDriveEdges(self, vi, pin_list, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge)`

#### `def niDigital_ConfigureTimeSetDriveEdges2x(self, vi, pin_list, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge, drive_data2_edge, drive_return2_edge)`

#### `def niDigital_ConfigureTimeSetDriveFormat(self, vi, pin_list, time_set_name, drive_format)`

#### `def niDigital_ConfigureTimeSetEdge(self, vi, pin_list, time_set_name, edge, time)`

#### `def niDigital_ConfigureTimeSetEdgeMultiplier(self, vi, pin_list, time_set_name, edge_multiplier)`

#### `def niDigital_ConfigureTimeSetPeriod(self, vi, time_set_name, period)`

#### `def niDigital_ConfigureVoltageLevels(self, vi, channel_list, vil, vih, vol, voh, vterm)`

#### `def niDigital_CreateCaptureWaveformFromFileDigicapture(self, vi, waveform_name, waveform_file_path)`

#### `def niDigital_CreateCaptureWaveformParallel(self, vi, pin_list, waveform_name)`

#### `def niDigital_CreateCaptureWaveformSerial(self, vi, pin_list, waveform_name, sample_width, bit_order)`

#### `def niDigital_CreateSourceWaveformFromFileTDMS(self, vi, waveform_name, waveform_file_path, write_waveform_data)`

#### `def niDigital_CreateSourceWaveformParallel(self, vi, pin_list, waveform_name, data_mapping)`

#### `def niDigital_CreateSourceWaveformSerial(self, vi, pin_list, waveform_name, data_mapping, sample_width, bit_order)`

#### `def niDigital_CreateTimeSet(self, vi, name)`

#### `def niDigital_DeleteAllTimeSets(self, vi)`

#### `def niDigital_DisableSites(self, vi, site_list)`

#### `def niDigital_EnableMatchFailCombination(self, session_count, sessions, sync_session)`

#### `def niDigital_EnableSites(self, vi, site_list)`

#### `def niDigital_FetchCaptureWaveformU32(self, vi, site_list, waveform_name, samples_to_read, timeout, data_buffer_size, data, actual_num_waveforms, actual_samples_per_waveform)`

#### `def niDigital_FetchHistoryRAMCycleInformation(self, vi, site, sample_index, pattern_index, time_set_index, vector_number, cycle_number, num_dut_cycles)`

#### `def niDigital_FetchHistoryRAMCyclePinData(self, vi, site, pin_list, sample_index, dut_cycle_index, pin_data_buffer_size, expected_pin_states, actual_pin_states, per_pin_pass_fail, actual_num_pin_data)`

#### `def niDigital_FetchHistoryRAMScanCycleNumber(self, vi, site, sample_index, scan_cycle_number)`

#### `def niDigital_FrequencyCounter_MeasureFrequency(self, vi, channel_list, frequencies_buffer_size, frequencies, actual_num_frequencies)`

#### `def niDigital_GetAttributeViBoolean(self, vi, channel_name, attribute, value)`

#### `def niDigital_GetAttributeViInt32(self, vi, channel_name, attribute, value)`

#### `def niDigital_GetAttributeViInt64(self, vi, channel_name, attribute, value)`

#### `def niDigital_GetAttributeViReal64(self, vi, channel_name, attribute, value)`

#### `def niDigital_GetAttributeViString(self, vi, channel_name, attribute, buffer_size, value)`

#### `def niDigital_GetChannelNameFromString(self, vi, indices, name_buffer_size, names)`

#### `def niDigital_GetError(self, vi, error_code, error_description_buffer_size, error_description)`

#### `def niDigital_GetFailCount(self, vi, channel_list, buffer_size, failure_count, actual_num_read)`

#### `def niDigital_GetHistoryRAMSampleCount(self, vi, site, sample_count)`

#### `def niDigital_GetPatternName(self, vi, pattern_index, name_buffer_size, name)`

#### `def niDigital_GetPatternPinList(self, vi, start_label, pin_list_buffer_size, pin_list)`

#### `def niDigital_GetPinName(self, vi, pin_index, name_buffer_size, name)`

#### `def niDigital_GetPinResultsPinInformation(self, vi, channel_list, buffer_size, pin_indexes, site_numbers, channel_indexes, actual_num_values)`

#### `def niDigital_GetSitePassFail(self, vi, site_list, pass_fail_buffer_size, pass_fail, actual_num_sites)`

#### `def niDigital_GetSiteResultsSiteNumbers(self, vi, site_list, site_result_type, site_numbers_buffer_size, site_numbers, actual_num_site_numbers)`

#### `def niDigital_GetTimeSetDriveFormat(self, vi, pin, time_set_name, format)`

#### `def niDigital_GetTimeSetEdge(self, vi, pin, time_set_name, edge, time)`

#### `def niDigital_GetTimeSetEdgeMultiplier(self, vi, pin, time_set_name, edge_multiplier)`

#### `def niDigital_GetTimeSetName(self, vi, time_set_index, name_buffer_size, name)`

#### `def niDigital_GetTimeSetPeriod(self, vi, time_set_name, period)`

#### `def niDigital_InitWithOptions(self, resource_name, id_query, reset_device, option_string, new_vi)`

#### `def niDigital_Initiate(self, vi)`

#### `def niDigital_IsDone(self, vi, done)`

#### `def niDigital_IsSiteEnabled(self, vi, site, enable)`

#### `def niDigital_LoadLevels(self, vi, file_path)`

#### `def niDigital_LoadPattern(self, vi, file_path)`

#### `def niDigital_LoadPinMap(self, vi, file_path)`

#### `def niDigital_LoadSpecifications(self, vi, file_path)`

#### `def niDigital_LoadTiming(self, vi, file_path)`

#### `def niDigital_LockSession(self, vi, caller_has_lock)`

#### `def niDigital_PPMU_Measure(self, vi, channel_list, measurement_type, buffer_size, measurements, actual_num_read)`

#### `def niDigital_PPMU_Source(self, vi, channel_list)`

#### `def niDigital_ReadSequencerFlag(self, vi, flag, value)`

#### `def niDigital_ReadSequencerRegister(self, vi, reg, value)`

#### `def niDigital_ReadStatic(self, vi, channel_list, buffer_size, data, actual_num_read)`

#### `def niDigital_ResetDevice(self, vi)`

#### `def niDigital_SelfCalibrate(self, vi)`

#### `def niDigital_SendSoftwareEdgeTrigger(self, vi, trigger, trigger_identifier)`

#### `def niDigital_SetAttributeViBoolean(self, vi, channel_name, attribute, value)`

#### `def niDigital_SetAttributeViInt32(self, vi, channel_name, attribute, value)`

#### `def niDigital_SetAttributeViInt64(self, vi, channel_name, attribute, value)`

#### `def niDigital_SetAttributeViReal64(self, vi, channel_name, attribute, value)`

#### `def niDigital_SetAttributeViString(self, vi, channel_name, attribute, value)`

#### `def niDigital_SetRuntimeEnvironment(self, environment, environment_version, reserved1, reserved2)`

#### `def niDigital_TDR(self, vi, channel_list, apply_offsets, offsets_buffer_size, offsets, actual_num_offsets)`

#### `def niDigital_UnloadAllPatterns(self, vi, unload_keep_alive_pattern)`

#### `def niDigital_UnloadSpecifications(self, vi, file_path)`

#### `def niDigital_UnlockSession(self, vi, caller_has_lock)`

#### `def niDigital_WaitUntilDone(self, vi, timeout)`

#### `def niDigital_WriteSequencerFlag(self, vi, flag, value)`

#### `def niDigital_WriteSequencerRegister(self, vi, reg, value)`

#### `def niDigital_WriteSourceWaveformBroadcastU32(self, vi, waveform_name, waveform_size, waveform_data)`

#### `def niDigital_WriteSourceWaveformDataFromFileTDMS(self, vi, waveform_name, waveform_file_path)`

#### `def niDigital_WriteSourceWaveformSiteUniqueU32(self, vi, site_list, waveform_name, num_waveforms, samples_per_waveform, waveform_data)`

#### `def niDigital_WriteStatic(self, vi, channel_list, state)`

#### `def niDigital_close(self, vi)`

#### `def niDigital_error_message(self, vi, error_code, error_message)`

#### `def niDigital_reset(self, vi)`

#### `def niDigital_self_test(self, vi, test_result, test_message)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nidigital/nidigital/_library_interpreter.py -->
## PYTHON MODULE: generated/nidigital/nidigital/_library_interpreter.py

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

#### `def abort_keep_alive(self)`

#### `def apply_levels_and_timing(self, site_list, levels_sheet, timing_sheet, initial_state_high_pins, initial_state_low_pins, initial_state_tristate_pins)`

#### `def apply_tdr_offsets(self, channel_list, offsets)`

#### `def burst_pattern(self, site_list, start_label, select_digital_function, wait_until_done, timeout)`

#### `def clock_generator_abort(self, channel_list)`

#### `def clock_generator_generate_clock(self, channel_list, frequency, select_digital_function)`

#### `def commit(self)`

#### `def configure_active_load_levels(self, channel_list, iol, ioh, vcom)`

#### `def configure_pattern_burst_sites(self, site_list)`

#### `def configure_time_set_compare_edges_strobe(self, pin_list, time_set_name, strobe_edge)`

#### `def configure_time_set_compare_edges_strobe2x(self, pin_list, time_set_name, strobe_edge, strobe2_edge)`

#### `def configure_time_set_drive_edges(self, pin_list, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge)`

#### `def configure_time_set_drive_edges2x(self, pin_list, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge, drive_data2_edge, drive_return2_edge)`

#### `def configure_time_set_drive_format(self, pin_list, time_set_name, drive_format)`

#### `def configure_time_set_edge(self, pin_list, time_set_name, edge, time)`

#### `def configure_time_set_edge_multiplier(self, pin_list, time_set_name, edge_multiplier)`

#### `def configure_time_set_period(self, time_set_name, period)`

#### `def configure_voltage_levels(self, channel_list, vil, vih, vol, voh, vterm)`

#### `def create_capture_waveform_from_file_digicapture(self, waveform_name, waveform_file_path)`

#### `def create_capture_waveform_parallel(self, pin_list, waveform_name)`

#### `def create_capture_waveform_serial(self, pin_list, waveform_name, sample_width, bit_order)`

#### `def create_source_waveform_from_file_tdms(self, waveform_name, waveform_file_path, write_waveform_data)`

#### `def create_source_waveform_parallel(self, pin_list, waveform_name, data_mapping)`

#### `def create_source_waveform_serial(self, pin_list, waveform_name, data_mapping, sample_width, bit_order)`

#### `def create_time_set(self, name)`

#### `def delete_all_time_sets(self)`

#### `def disable_sites(self, site_list)`

#### `def enable_match_fail_combination(self, sessions, sync_session)`

#### `def enable_sites(self, site_list)`

#### `def fetch_capture_waveform(self, site_list, waveform_name, samples_to_read, timeout)`

#### `def fetch_history_ram_cycle_information(self, site, sample_index)`

#### `def fetch_history_ram_cycle_pin_data(self, site, pin_list, sample_index, dut_cycle_index)`

#### `def fetch_history_ram_scan_cycle_number(self, site, sample_index)`

#### `def frequency_counter_measure_frequency(self, channel_list)`

#### `def get_attribute_vi_boolean(self, channel_name, attribute)`

#### `def get_attribute_vi_int32(self, channel_name, attribute)`

#### `def get_attribute_vi_int64(self, channel_name, attribute)`

#### `def get_attribute_vi_real64(self, channel_name, attribute)`

#### `def get_attribute_vi_string(self, channel_name, attribute)`

#### `def get_channel_names(self, indices)`

#### `def get_error(self)`

#### `def get_fail_count(self, channel_list)`

#### `def get_history_ram_sample_count(self, site)`

#### `def get_pattern_name(self, pattern_index)`

#### `def get_pattern_pin_names(self, start_label)`

#### `def get_pin_name(self, pin_index)`

#### `def get_pin_results_pin_information(self, channel_list)`

#### `def get_site_pass_fail(self, site_list)`

#### `def get_site_results_site_numbers(self, site_list, site_result_type)`

#### `def get_time_set_drive_format(self, pin, time_set_name)`

#### `def get_time_set_edge(self, pin, time_set_name, edge)`

#### `def get_time_set_edge_multiplier(self, pin, time_set_name)`

#### `def get_time_set_name(self, time_set_index)`

#### `def get_time_set_period(self, time_set_name)`

#### `def init_with_options(self, resource_name, id_query, reset_device, option_string)`

#### `def initiate(self)`

#### `def is_done(self)`

#### `def is_site_enabled(self, site)`

#### `def load_levels(self, file_path)`

#### `def load_pattern(self, file_path)`

#### `def load_pin_map(self, file_path)`

#### `def load_specifications(self, file_path)`

#### `def load_timing(self, file_path)`

#### `def lock(self)`

#### `def ppmu_measure(self, channel_list, measurement_type)`

#### `def ppmu_source(self, channel_list)`

#### `def read_sequencer_flag(self, flag)`

#### `def read_sequencer_register(self, reg)`

#### `def read_static(self, channel_list)`

#### `def reset_device(self)`

#### `def self_calibrate(self)`

#### `def send_software_edge_trigger(self, trigger, trigger_identifier)`

#### `def set_attribute_vi_boolean(self, channel_name, attribute, value)`

#### `def set_attribute_vi_int32(self, channel_name, attribute, value)`

#### `def set_attribute_vi_int64(self, channel_name, attribute, value)`

#### `def set_attribute_vi_real64(self, channel_name, attribute, value)`

#### `def set_attribute_vi_string(self, channel_name, attribute, value)`

#### `def set_runtime_environment(self, environment, environment_version, reserved1, reserved2)`

#### `def tdr(self, channel_list, apply_offsets)`

#### `def unload_all_patterns(self, unload_keep_alive_pattern)`

#### `def unload_specifications(self, file_path)`

#### `def unlock(self)`

#### `def wait_until_done(self, timeout)`

#### `def write_sequencer_flag(self, flag, value)`

#### `def write_sequencer_register(self, reg, value)`

#### `def write_source_waveform_broadcast(self, waveform_name, waveform_data)`

#### `def write_source_waveform_data_from_file_tdms(self, waveform_name, waveform_file_path)`

#### `def write_source_waveform_site_unique_u32(self, site_list, waveform_name, num_waveforms, samples_per_waveform, waveform_data)`

#### `def write_static(self, channel_list, state)`

#### `def close(self)`

#### `def error_message(self, error_code)`

#### `def reset(self)`

#### `def self_test(self)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nidigital/nidigital/_library_singleton.py -->
## PYTHON MODULE: generated/nidigital/nidigital/_library_singleton.py

### `def _get_library_name()`

### `def _get_library_type()`

### `def get()`

get

    Returns the library.Library singleton for nidigital.
    

<!--NI_PYTHON_API repo=nimi-python path=generated/nidigital/nidigital/enums.py -->
## PYTHON MODULE: generated/nidigital/nidigital/enums.py

### `class BitOrder(Enum)`

### `class DigitalEdge(Enum)`

### `class DriveFormat(Enum)`

### `class FrequencyMeasurementMode(Enum)`

### `class HistoryRAMCyclesToAcquire(Enum)`

### `class HistoryRAMTriggerType(Enum)`

### `class PPMUApertureTimeUnits(Enum)`

### `class PPMUCurrentLimitBehavior(Enum)`

### `class PPMUMeasurementType(Enum)`

### `class PPMUOutputFunction(Enum)`

### `class PinState(Enum)`

#### `def __str__(self)`

### `class SelectedFunction(Enum)`

### `class SequencerFlag(Enum)`

### `class SequencerRegister(Enum)`

### `class _SiteResultType(Enum)`

### `class SoftwareTrigger(Enum)`

### `class SourceDataMapping(Enum)`

### `class TDREndpointTermination(Enum)`

### `class TerminationMode(Enum)`

### `class TimeSetEdgeType(Enum)`

### `class TriggerType(Enum)`

### `class WriteStaticPinState(Enum)`

#### `def __str__(self)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nidigital/nidigital/errors.py -->
## PYTHON MODULE: generated/nidigital/nidigital/errors.py

### `def _is_success(code)`

### `def _is_error(code)`

### `def _is_warning(code)`

### `class Error(Exception)`

Base error class for NI-Digital Pattern Driver

#### `def __init__(self, message)`

### `class DriverError(Error)`

An error originating from the NI-Digital Pattern Driver driver

#### `def __init__(self, code, description)`

### `class DriverWarning(Warning)`

A warning originating from the NI-Digital Pattern Driver driver

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

An error due to using this module with an older version of the NI-Digital Pattern Driver driver runtime.

#### `def __init__(self)`

### `class DriverTooNewError(Error)`

An error due to the NI-Digital Pattern Driver driver runtime being too new for this module.

#### `def __init__(self)`

### `class InvalidRepeatedCapabilityError(Error)`

An error due to an invalid character in a repeated capability

#### `def __init__(self, invalid_character, invalid_string)`

### `class SelfTestError(Error)`

An error due to a failed self-test

#### `def __init__(self, code, msg)`

### `def handle_error(library_interpreter, code, ignore_warnings, is_error_handling)`

handle_error

    Helper function for handling errors returned by nidigital.Library.
    It calls back into the LibraryInterpreter to get the corresponding error
    description and raises if necessary.
    

<!--NI_PYTHON_API repo=nimi-python path=generated/nidigital/nidigital/grpc_session_options.py -->
## PYTHON MODULE: generated/nidigital/nidigital/grpc_session_options.py

- `GRPC_SERVICE_INTERFACE_NAME = 'nidigitalpattern_grpc.NiDigital'`

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
        

<!--NI_PYTHON_API repo=nimi-python path=generated/nidigital/nidigital/history_ram_cycle_information.py -->
## PYTHON MODULE: generated/nidigital/nidigital/history_ram_cycle_information.py

### `class HistoryRAMCycleInformation()`

#### `def __init__(self, pattern_name, time_set_name, vector_number, cycle_number, scan_cycle_number, expected_pin_states, actual_pin_states, per_pin_pass_fail)`

#### `def __repr__(self)`

#### `def __str__(self)`

#### `def _digital_states_representation(states)`

#### `def _digital_states_string(states)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nidigital/nidigital/nidevice_pb2.py -->
## PYTHON MODULE: generated/nidigital/nidigital/nidevice_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0enidevice.proto\x12\rnidevice_grpc"2\n\x0fNIComplexNumber\x12\x0c\n\x04real\x18\x01 \x01(\x01\x12\x11\n\timaginary\x18\x02 \x01(\x01"5\n\x12NIComplexNumberF32\x12\x0c\n\x04real\x18\x01 \x01(\x02\x12\x11\n\timaginary\x18\x02 \x01(\x02"/\n\x0cNIComplexI16\x12\x0c\n\x04real\x18\x01 \x01(\x11\x12\x11\n\timaginary\x18\x02 \x01(\x11"r\n\x0fSmtSpectrumInfo\x12\x15\n\rspectrum_type\x18\x01 \x01(\r\x12\x11\n\tlinear_db\x18\x02 \x01(\r\x12\x0e\n\x06window\x18\x03 \x01(\r\x12\x13\n\x0bwindow_size\x18\x04 \x01(\x11\x12\x10\n\x08fft_size\x18\x05 \x01(\x11BB\n\x12com.ni.grpc.deviceB\x08NiDeviceP\x01\xaa\x02\x1fNationalInstruments.Grpc.Deviceb\x06proto3')`

<!--NI_PYTHON_API repo=nimi-python path=generated/nidigital/nidigital/nidevice_pb2_grpc.py -->
## PYTHON MODULE: generated/nidigital/nidigital/nidevice_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

<!--NI_PYTHON_API repo=nimi-python path=generated/nidigital/nidigital/nidigitalpattern_pb2.py -->
## PYTHON MODULE: generated/nidigital/nidigital/nidigitalpattern_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16nidigitalpattern.proto\x12\x15nidigitalpattern_grpc\x1a\rsession.proto"\xb1\x01\n\x0bInitRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\x10\n\x08id_query\x18\x03 \x01(\x08\x12\x14\n\x0creset_device\x18\x04 \x01(\x08\x12M\n\x17initialization_behavior\x18\x05 \x01(\x0e2,.nidevice_grpc.SessionInitializationBehavior"~\n\x0cInitResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12"\n\x02vi\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x19\n\rerror_message\x18\x03 \x01(\tB\x02\x18\x01\x12\x1f\n\x17new_session_initialized\x18\x04 \x01(\x08"\xd3\x01\n\x16InitWithOptionsRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\x10\n\x08id_query\x18\x03 \x01(\x08\x12\x14\n\x0creset_device\x18\x04 \x01(\x08\x12\x15\n\roption_string\x18\x05 \x01(\t\x12M\n\x17initialization_behavior\x18\x06 \x01(\x0e2,.nidevice_grpc.SessionInitializationBehavior"\x89\x01\n\x17InitWithOptionsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12"\n\x02vi\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x19\n\rerror_message\x18\x03 \x01(\tB\x02\x18\x01\x12\x1f\n\x17new_session_initialized\x18\x04 \x01(\x08"2\n\x0cCloseRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\x1f\n\rCloseResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"2\n\x0cResetRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\x1f\n\rResetResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"8\n\x12ResetDeviceRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"%\n\x13ResetDeviceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"5\n\x0fSelfTestRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"M\n\x10SelfTestResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0btest_result\x18\x02 \x01(\x11\x12\x14\n\x0ctest_message\x18\x03 \x01(\t"5\n\x0fGetErrorRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"Q\n\x10GetErrorResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nerror_code\x18\x02 \x01(\x11\x12\x19\n\x11error_description\x18\x03 \x01(\t"7\n\x11ClearErrorRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"$\n\x12ClearErrorResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"M\n\x13ErrorMessageRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x12\n\nerror_code\x18\x02 \x01(\x11"=\n\x14ErrorMessageResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rerror_message\x18\x02 \x01(\t":\n\x14SelfCalibrateRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\'\n\x15SelfCalibrateResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x94\x01\n\x1aGetAttributeViInt32Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12<\n\tattribute\x18\x03 \x01(\x0e2).nidigitalpattern_grpc.NiDigitalAttribute"<\n\x1bGetAttributeViInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x11"\x94\x01\n\x1aGetAttributeViInt64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12<\n\tattribute\x18\x03 \x01(\x0e2).nidigitalpattern_grpc.NiDigitalAttribute"<\n\x1bGetAttributeViInt64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x03"\x95\x01\n\x1bGetAttributeViReal64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12<\n\tattribute\x18\x03 \x01(\x0e2).nidigitalpattern_grpc.NiDigitalAttribute"=\n\x1cGetAttributeViReal64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x01"\x95\x01\n\x1bGetAttributeViStringRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12<\n\tattribute\x18\x03 \x01(\x0e2).nidigitalpattern_grpc.NiDigitalAttribute"=\n\x1cGetAttributeViStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t"\x96\x01\n\x1cGetAttributeViSessionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12<\n\tattribute\x18\x03 \x01(\x0e2).nidigitalpattern_grpc.NiDigitalAttribute"V\n\x1dGetAttributeViSessionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12%\n\x05value\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session"\x96\x01\n\x1cGetAttributeViBooleanRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12<\n\tattribute\x18\x03 \x01(\x0e2).nidigitalpattern_grpc.NiDigitalAttribute">\n\x1dGetAttributeViBooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x08"\xfe\x01\n\x1aSetAttributeViInt32Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12<\n\tattribute\x18\x03 \x01(\x0e2).nidigitalpattern_grpc.NiDigitalAttribute\x12E\n\x05value\x18\x04 \x01(\x0e24.nidigitalpattern_grpc.NiDigitalInt32AttributeValuesH\x00\x12\x13\n\tvalue_raw\x18\x05 \x01(\x11H\x00B\x0c\n\nvalue_enum"-\n\x1bSetAttributeViInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa7\x01\n\x1aSetAttributeViInt64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12<\n\tattribute\x18\x03 \x01(\x0e2).nidigitalpattern_grpc.NiDigitalAttribute\x12\x11\n\tvalue_raw\x18\x04 \x01(\x03"-\n\x1bSetAttributeViInt64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa8\x01\n\x1bSetAttributeViReal64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12<\n\tattribute\x18\x03 \x01(\x0e2).nidigitalpattern_grpc.NiDigitalAttribute\x12\x11\n\tvalue_raw\x18\x04 \x01(\x01".\n\x1cSetAttributeViReal64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa8\x01\n\x1bSetAttributeViStringRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12<\n\tattribute\x18\x03 \x01(\x0e2).nidigitalpattern_grpc.NiDigitalAttribute\x12\x11\n\tvalue_raw\x18\x04 \x01(\t".\n\x1cSetAttributeViStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xbd\x01\n\x1cSetAttributeViSessionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12<\n\tattribute\x18\x03 \x01(\x0e2).nidigitalpattern_grpc.NiDigitalAttribute\x12%\n\x05value\x18\x04 \x01(\x0b2\x16.nidevice_grpc.Session"/\n\x1dSetAttributeViSessionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa5\x01\n\x1cSetAttributeViBooleanRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12<\n\tattribute\x18\x03 \x01(\x0e2).nidigitalpattern_grpc.NiDigitalAttribute\x12\r\n\x05value\x18\x04 \x01(\x08"/\n\x1dSetAttributeViBooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x92\x01\n\x15ResetAttributeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x12?\n\x0cattribute_id\x18\x03 \x01(\x0e2).nidigitalpattern_grpc.NiDigitalAttribute"(\n\x16ResetAttributeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"J\n\x11LoadPinMapRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tfile_path\x18\x02 \x01(\t"$\n\x12LoadPinMapResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"K\n\x12EnableSitesRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tsite_list\x18\x02 \x01(\t"%\n\x13EnableSitesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"L\n\x13DisableSitesRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tsite_list\x18\x02 \x01(\t"&\n\x14DisableSitesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"H\n\x14IsSiteEnabledRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0c\n\x04site\x18\x02 \x01(\t"7\n\x15IsSiteEnabledResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0e\n\x06enable\x18\x02 \x01(\x08"h\n\x13CreatePinMapRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cdut_pin_list\x18\x02 \x01(\t\x12\x17\n\x0fsystem_pin_list\x18\x03 \x01(\t"&\n\x14CreatePinMapResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"e\n\x15CreatePinGroupRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x16\n\x0epin_group_name\x18\x02 \x01(\t\x12\x10\n\x08pin_list\x18\x03 \x01(\t"(\n\x16CreatePinGroupResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"P\n\x17CreateChannelMapRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tnum_sites\x18\x02 \x01(\x11"*\n\x18CreateChannelMapResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"h\n\x16MapPinToChannelRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0b\n\x03pin\x18\x02 \x01(\t\x12\x0c\n\x04site\x18\x03 \x01(\x11\x12\x0f\n\x07channel\x18\x04 \x01(\t")\n\x17MapPinToChannelResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05":\n\x14EndChannelMapRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\'\n\x15EndChannelMapResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"J\n\x11GetPinNameRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tpin_index\x18\x02 \x01(\x11"2\n\x12GetPinNameResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t"J\n\x15GetChannelNameRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\r\n\x05index\x18\x02 \x01(\x11"6\n\x16GetChannelNameResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t"\xb7\x01\n\x15SelectFunctionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12;\n\x08function\x18\x03 \x01(\x0e2\'.nidigitalpattern_grpc.SelectedFunctionH\x00\x12\x16\n\x0cfunction_raw\x18\x04 \x01(\x11H\x00B\x0f\n\rfunction_enum"(\n\x16SelectFunctionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"M\n\x11ReadStaticRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t"~\n\x12ReadStaticResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12-\n\x04data\x18\x02 \x03(\x0e2\x1f.nidigitalpattern_grpc.PinState\x12\x10\n\x08data_raw\x18\x03 \x01(\x0c\x12\x17\n\x0factual_num_read\x18\x04 \x01(\x11"\xae\x01\n\x12WriteStaticRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12;\n\x05state\x18\x03 \x01(\x0e2*.nidigitalpattern_grpc.WriteStaticPinStateH\x00\x12\x13\n\tstate_raw\x18\x04 \x01(\rH\x00B\x0c\n\nstate_enum"%\n\x13WriteStaticResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x92\x01\n"ClockGeneratorGenerateClockRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12\x11\n\tfrequency\x18\x03 \x01(\x01\x12\x1f\n\x17select_digital_function\x18\x04 \x01(\x08"5\n#ClockGeneratorGenerateClockResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"Y\n\x1dClockGeneratorInitiateRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t"0\n\x1eClockGeneratorInitiateResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"V\n\x1aClockGeneratorAbortRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t"-\n\x1bClockGeneratorAbortResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"R\n\x19LoadSpecificationsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tfile_path\x18\x02 \x01(\t",\n\x1aLoadSpecificationsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"T\n\x1bUnloadSpecificationsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tfile_path\x18\x02 \x01(\t".\n\x1cUnloadSpecificationsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"J\n\x11LoadLevelsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tfile_path\x18\x02 \x01(\t"$\n\x12LoadLevelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"J\n\x11LoadTimingRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tfile_path\x18\x02 \x01(\t"$\n\x12LoadTimingResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xe6\x01\n\x1bApplyLevelsAndTimingRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tsite_list\x18\x02 \x01(\t\x12\x14\n\x0clevels_sheet\x18\x03 \x01(\t\x12\x14\n\x0ctiming_sheet\x18\x04 \x01(\t\x12\x1f\n\x17initial_state_high_pins\x18\x05 \x01(\t\x12\x1e\n\x16initial_state_low_pins\x18\x06 \x01(\t\x12#\n\x1binitial_state_tristate_pins\x18\x07 \x01(\t".\n\x1cApplyLevelsAndTimingResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x9c\x01\n\x1dConfigureVoltageLevelsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12\x0b\n\x03vil\x18\x03 \x01(\x01\x12\x0b\n\x03vih\x18\x04 \x01(\x01\x12\x0b\n\x03vol\x18\x05 \x01(\x01\x12\x0b\n\x03voh\x18\x06 \x01(\x01\x12\r\n\x05vterm\x18\x07 \x01(\x01"0\n\x1eConfigureVoltageLevelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x84\x01\n ConfigureActiveLoadLevelsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12\x0b\n\x03iol\x18\x03 \x01(\x01\x12\x0b\n\x03ioh\x18\x04 \x01(\x01\x12\x0c\n\x04vcom\x18\x05 \x01(\x01"3\n!ConfigureActiveLoadLevelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb4\x01\n\x1fConfigureTerminationModeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x126\n\x04mode\x18\x03 \x01(\x0e2&.nidigitalpattern_grpc.TerminationModeH\x00\x12\x12\n\x08mode_raw\x18\x04 \x01(\x11H\x00B\x0b\n\tmode_enum"2\n ConfigureTerminationModeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"H\n\x14CreateTimeSetRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0c\n\x04name\x18\x02 \x01(\t"\'\n\x15CreateTimeSetResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"j\n\x1dConfigureTimeSetPeriodRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rtime_set_name\x18\x02 \x01(\t\x12\x0e\n\x06period\x18\x03 \x01(\x01"0\n\x1eConfigureTimeSetPeriodResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xae\x02\n!ConfigureTimeSetDriveEdgesRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x10\n\x08pin_list\x18\x02 \x01(\t\x12\x15\n\rtime_set_name\x18\x03 \x01(\t\x124\n\x06format\x18\x04 \x01(\x0e2".nidigitalpattern_grpc.DriveFormatH\x00\x12\x14\n\nformat_raw\x18\x05 \x01(\x11H\x00\x12\x15\n\rdrive_on_edge\x18\x06 \x01(\x01\x12\x17\n\x0fdrive_data_edge\x18\x07 \x01(\x01\x12\x19\n\x11drive_return_edge\x18\x08 \x01(\x01\x12\x16\n\x0edrive_off_edge\x18\t \x01(\x01B\r\n\x0bformat_enum"4\n"ConfigureTimeSetDriveEdgesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x8d\x01\n)ConfigureTimeSetCompareEdgesStrobeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x10\n\x08pin_list\x18\x02 \x01(\t\x12\x15\n\rtime_set_name\x18\x03 \x01(\t\x12\x13\n\x0bstrobe_edge\x18\x04 \x01(\x01"<\n*ConfigureTimeSetCompareEdgesStrobeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xde\x01\n"ConfigureTimeSetDriveFormatRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x10\n\x08pin_list\x18\x02 \x01(\t\x12\x15\n\rtime_set_name\x18\x03 \x01(\t\x12:\n\x0cdrive_format\x18\x04 \x01(\x0e2".nidigitalpattern_grpc.DriveFormatH\x00\x12\x1a\n\x10drive_format_raw\x18\x05 \x01(\x11H\x00B\x13\n\x11drive_format_enum"5\n#ConfigureTimeSetDriveFormatResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05">\n\x18DeleteAllTimeSetsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"+\n\x19DeleteAllTimeSetsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x8d\x01\n%ConfigureTimeSetEdgeMultiplierRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x10\n\x08pin_list\x18\x02 \x01(\t\x12\x15\n\rtime_set_name\x18\x03 \x01(\t\x12\x17\n\x0fedge_multiplier\x18\x04 \x01(\x11"8\n&ConfigureTimeSetEdgeMultiplierResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xe6\x02\n#ConfigureTimeSetDriveEdges2xRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x10\n\x08pin_list\x18\x02 \x01(\t\x12\x15\n\rtime_set_name\x18\x03 \x01(\t\x124\n\x06format\x18\x04 \x01(\x0e2".nidigitalpattern_grpc.DriveFormatH\x00\x12\x14\n\nformat_raw\x18\x05 \x01(\x11H\x00\x12\x15\n\rdrive_on_edge\x18\x06 \x01(\x01\x12\x17\n\x0fdrive_data_edge\x18\x07 \x01(\x01\x12\x19\n\x11drive_return_edge\x18\x08 \x01(\x01\x12\x16\n\x0edrive_off_edge\x18\t \x01(\x01\x12\x18\n\x10drive_data2_edge\x18\n \x01(\x01\x12\x1a\n\x12drive_return2_edge\x18\x0b \x01(\x01B\r\n\x0bformat_enum"6\n$ConfigureTimeSetDriveEdges2xResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa5\x01\n+ConfigureTimeSetCompareEdgesStrobe2xRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x10\n\x08pin_list\x18\x02 \x01(\t\x12\x15\n\rtime_set_name\x18\x03 \x01(\t\x12\x13\n\x0bstrobe_edge\x18\x04 \x01(\x01\x12\x14\n\x0cstrobe2_edge\x18\x05 \x01(\x01">\n,ConfigureTimeSetCompareEdgesStrobe2xResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xd1\x01\n\x1bConfigureTimeSetEdgeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x10\n\x08pin_list\x18\x02 \x01(\t\x12\x15\n\rtime_set_name\x18\x03 \x01(\t\x126\n\x04edge\x18\x04 \x01(\x0e2&.nidigitalpattern_grpc.TimeSetEdgeTypeH\x00\x12\x12\n\x08edge_raw\x18\x05 \x01(\x11H\x00\x12\x0c\n\x04time\x18\x06 \x01(\x01B\x0b\n\tedge_enum".\n\x1cConfigureTimeSetEdgeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"T\n\x17GetTimeSetPeriodRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rtime_set_name\x18\x02 \x01(\t":\n\x18GetTimeSetPeriodResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0e\n\x06period\x18\x02 \x01(\x01"\xb8\x01\n\x15GetTimeSetEdgeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0b\n\x03pin\x18\x02 \x01(\t\x12\x15\n\rtime_set_name\x18\x03 \x01(\t\x126\n\x04edge\x18\x04 \x01(\x0e2&.nidigitalpattern_grpc.TimeSetEdgeTypeH\x00\x12\x12\n\x08edge_raw\x18\x05 \x01(\x11H\x00B\x0b\n\tedge_enum"6\n\x16GetTimeSetEdgeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04time\x18\x02 \x01(\x01"i\n\x1fGetTimeSetEdgeMultiplierRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0b\n\x03pin\x18\x02 \x01(\t\x12\x15\n\rtime_set_name\x18\x03 \x01(\t"K\n GetTimeSetEdgeMultiplierResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fedge_multiplier\x18\x02 \x01(\x11"f\n\x1cGetTimeSetDriveFormatRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0b\n\x03pin\x18\x02 \x01(\t\x12\x15\n\rtime_set_name\x18\x03 \x01(\t"w\n\x1dGetTimeSetDriveFormatResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x122\n\x06format\x18\x02 \x01(\x0e2".nidigitalpattern_grpc.DriveFormat\x12\x12\n\nformat_raw\x18\x03 \x01(\x11"S\n\x15GetTimeSetNameRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x16\n\x0etime_set_index\x18\x02 \x01(\x11"6\n\x16GetTimeSetNameResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t"]\n\nTDRRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12\x15\n\rapply_offsets\x18\x03 \x01(\x08"J\n\x0bTDRResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07offsets\x18\x02 \x03(\x01\x12\x1a\n\x12actual_num_offsets\x18\x03 \x01(\x11"c\n\x16ApplyTDROffsetsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12\x0f\n\x07offsets\x18\x03 \x03(\x01")\n\x17ApplyTDROffsetsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xdb\x01\n"PPMUConfigureOutputFunctionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12D\n\x0foutput_function\x18\x03 \x01(\x0e2).nidigitalpattern_grpc.PpmuOutputFunctionH\x00\x12\x1d\n\x13output_function_raw\x18\x04 \x01(\x11H\x00B\x16\n\x14output_function_enum"5\n#PPMUConfigureOutputFunctionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xd5\x01\n PPMUConfigureApertureTimeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12\x15\n\raperture_time\x18\x03 \x01(\x01\x12=\n\x05units\x18\x04 \x01(\x0e2,.nidigitalpattern_grpc.PpmuApertureTimeUnitsH\x00\x12\x13\n\tunits_raw\x18\x05 \x01(\x11H\x00B\x0c\n\nunits_enum"3\n!PPMUConfigureApertureTimeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"s\n PPMUConfigureVoltageLevelRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12\x15\n\rvoltage_level\x18\x03 \x01(\x01"3\n!PPMUConfigureVoltageLevelResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xd9\x01\n PPMUConfigureCurrentLimitRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12C\n\x08behavior\x18\x03 \x01(\x0e2/.nidigitalpattern_grpc.PpmuCurrentLimitBehaviorH\x00\x12\x16\n\x0cbehavior_raw\x18\x04 \x01(\x11H\x00\x12\r\n\x05limit\x18\x05 \x01(\x01B\x0f\n\rbehavior_enum"3\n!PPMUConfigureCurrentLimitResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"p\n%PPMUConfigureCurrentLimitRangeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12\r\n\x05range\x18\x03 \x01(\x01"8\n&PPMUConfigureCurrentLimitRangeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"s\n PPMUConfigureCurrentLevelRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12\x15\n\rcurrent_level\x18\x03 \x01(\x01"3\n!PPMUConfigureCurrentLevelResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"p\n%PPMUConfigureCurrentLevelRangeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12\r\n\x05range\x18\x03 \x01(\x01"8\n&PPMUConfigureCurrentLevelRangeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x97\x01\n!PPMUConfigureVoltageLimitsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12\x1b\n\x13lower_voltage_limit\x18\x03 \x01(\x01\x12\x1b\n\x13upper_voltage_limit\x18\x04 \x01(\x01"4\n"PPMUConfigureVoltageLimitsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"M\n\x11PPMUSourceRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t"$\n\x12PPMUSourceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xcf\x01\n\x12PPMUMeasureRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12F\n\x10measurement_type\x18\x03 \x01(\x0e2*.nidigitalpattern_grpc.PpmuMeasurementTypeH\x00\x12\x1e\n\x14measurement_type_raw\x18\x04 \x01(\x11H\x00B\x17\n\x15measurement_type_enum"T\n\x13PPMUMeasureResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x14\n\x0cmeasurements\x18\x02 \x03(\x01\x12\x17\n\x0factual_num_read\x18\x03 \x01(\x11"K\n\x12LoadPatternRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tfile_path\x18\x02 \x01(\t"%\n\x13LoadPatternResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"a\n\x18UnloadAllPatternsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12!\n\x19unload_keep_alive_pattern\x18\x02 \x01(\x08"+\n\x19UnloadAllPatternsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"O\n\x1aConfigureStartLabelRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\r\n\x05label\x18\x02 \x01(\t"-\n\x1bConfigureStartLabelResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"Z\n!ConfigurePatternBurstSitesRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tsite_list\x18\x02 \x01(\t"4\n"ConfigurePatternBurstSitesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"V\n\x1bGetPatternPinIndexesRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x13\n\x0bstart_label\x18\x02 \x01(\t"\\\n\x1cGetPatternPinIndexesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0bpin_indexes\x18\x02 \x03(\x11\x12\x17\n\x0factual_num_pins\x18\x03 \x01(\x11"S\n\x18GetPatternPinListRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x13\n\x0bstart_label\x18\x02 \x01(\t"=\n\x19GetPatternPinListResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x10\n\x08pin_list\x18\x02 \x01(\t"R\n\x15GetPatternNameRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rpattern_index\x18\x02 \x01(\x11"6\n\x16GetPatternNameResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t"\xac\x01\n\x13BurstPatternRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tsite_list\x18\x02 \x01(\t\x12\x13\n\x0bstart_label\x18\x03 \x01(\t\x12\x1f\n\x17select_digital_function\x18\x04 \x01(\x08\x12\x17\n\x0fwait_until_done\x18\x05 \x01(\x08\x12\x0f\n\x07timeout\x18\x06 \x01(\x01"&\n\x14BurstPatternResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xd5\x01\n\x1fBurstPatternSynchronizedRequest\x12\x15\n\rsession_count\x18\x01 \x01(\r\x12(\n\x08sessions\x18\x02 \x03(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tsite_list\x18\x03 \x01(\t\x12\x13\n\x0bstart_label\x18\x04 \x01(\t\x12\x1f\n\x17select_digital_function\x18\x05 \x01(\x08\x12\x17\n\x0fwait_until_done\x18\x06 \x01(\x08\x12\x0f\n\x07timeout\x18\x07 \x01(\x01"2\n BurstPatternSynchronizedResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"3\n\rCommitRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session" \n\x0eCommitResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"5\n\x0fInitiateRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session""\n\x10InitiateResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"3\n\rIsDoneRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session".\n\x0eIsDoneResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04done\x18\x02 \x01(\x08"K\n\x14WaitUntilDoneRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07timeout\x18\x02 \x01(\x01"\'\n\x15WaitUntilDoneResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"2\n\x0cAbortRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\x1f\n\rAbortResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05";\n\x15AbortKeepAliveRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"(\n\x16AbortKeepAliveResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xab\x01\n-ConfigurePatternLabelHistoryRAMTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\r\n\x05label\x18\x02 \x01(\t\x12\x15\n\rvector_offset\x18\x03 \x01(\x03\x12\x14\n\x0ccycle_offset\x18\x04 \x01(\x03\x12\x1a\n\x12pretrigger_samples\x18\x05 \x01(\x11"@\n.ConfigurePatternLabelHistoryRAMTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x84\x01\n,ConfigureCycleNumberHistoryRAMTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0ccycle_number\x18\x02 \x01(\x03\x12\x1a\n\x12pretrigger_samples\x18\x03 \x01(\x11"?\n-ConfigureCycleNumberHistoryRAMTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"o\n-ConfigureFirstFailureHistoryRAMTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12pretrigger_samples\x18\x02 \x01(\x11"@\n.ConfigureFirstFailureHistoryRAMTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xd9\x01\n)ConfigureHistoryRAMCyclesToAcquireRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12M\n\x11cycles_to_acquire\x18\x02 \x01(\x0e20.nidigitalpattern_grpc.HistoryRamCyclesToAcquireH\x00\x12\x1f\n\x15cycles_to_acquire_raw\x18\x03 \x01(\x11H\x00B\x18\n\x16cycles_to_acquire_enum"<\n*ConfigureHistoryRAMCyclesToAcquireResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"S\n\x1fGetHistoryRAMSampleCountRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0c\n\x04site\x18\x02 \x01(\t"H\n GetHistoryRAMSampleCountResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x14\n\x0csample_count\x18\x02 \x01(\x03"p\n&FetchHistoryRAMCycleInformationRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0c\n\x04site\x18\x02 \x01(\t\x12\x14\n\x0csample_index\x18\x03 \x01(\x03"\xad\x01\n\'FetchHistoryRAMCycleInformationResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rpattern_index\x18\x02 \x01(\x11\x12\x16\n\x0etime_set_index\x18\x03 \x01(\x11\x12\x15\n\rvector_number\x18\x04 \x01(\x03\x12\x14\n\x0ccycle_number\x18\x05 \x01(\x03\x12\x16\n\x0enum_dut_cycles\x18\x06 \x01(\x11"\x97\x01\n"FetchHistoryRAMCyclePinDataRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0c\n\x04site\x18\x02 \x01(\t\x12\x10\n\x08pin_list\x18\x03 \x01(\t\x12\x14\n\x0csample_index\x18\x04 \x01(\x03\x12\x17\n\x0fdut_cycle_index\x18\x05 \x01(\x11"\xa7\x02\n#FetchHistoryRAMCyclePinDataResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12<\n\x13expected_pin_states\x18\x02 \x03(\x0e2\x1f.nidigitalpattern_grpc.PinState\x12\x1f\n\x17expected_pin_states_raw\x18\x03 \x01(\x0c\x12:\n\x11actual_pin_states\x18\x04 \x03(\x0e2\x1f.nidigitalpattern_grpc.PinState\x12\x1d\n\x15actual_pin_states_raw\x18\x05 \x01(\x0c\x12\x19\n\x11per_pin_pass_fail\x18\x06 \x03(\x08\x12\x1b\n\x13actual_num_pin_data\x18\x07 \x01(\x11"o\n%FetchHistoryRAMScanCycleNumberRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0c\n\x04site\x18\x02 \x01(\t\x12\x14\n\x0csample_index\x18\x03 \x01(\x03"S\n&FetchHistoryRAMScanCycleNumberResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x19\n\x11scan_cycle_number\x18\x02 \x01(\x03"\xe5\x01\n#CreateSourceWaveformParallelRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x10\n\x08pin_list\x18\x02 \x01(\t\x12\x15\n\rwaveform_name\x18\x03 \x01(\t\x12@\n\x0cdata_mapping\x18\x04 \x01(\x0e2(.nidigitalpattern_grpc.SourceDataMappingH\x00\x12\x1a\n\x10data_mapping_raw\x18\x05 \x01(\x11H\x00B\x13\n\x11data_mapping_enum"6\n$CreateSourceWaveformParallelResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xda\x02\n!CreateSourceWaveformSerialRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x10\n\x08pin_list\x18\x02 \x01(\t\x12\x15\n\rwaveform_name\x18\x03 \x01(\t\x12@\n\x0cdata_mapping\x18\x04 \x01(\x0e2(.nidigitalpattern_grpc.SourceDataMappingH\x00\x12\x1a\n\x10data_mapping_raw\x18\x05 \x01(\x11H\x00\x12\x14\n\x0csample_width\x18\x06 \x01(\r\x124\n\tbit_order\x18\x07 \x01(\x0e2\x1f.nidigitalpattern_grpc.BitOrderH\x01\x12\x17\n\rbit_order_raw\x18\x08 \x01(\x11H\x01B\x13\n\x11data_mapping_enumB\x10\n\x0ebit_order_enum"4\n"CreateSourceWaveformSerialResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x9d\x01\n\'CreateSourceWaveformFromFileTDMSRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rwaveform_name\x18\x02 \x01(\t\x12\x1a\n\x12waveform_file_path\x18\x03 \x01(\t\x12\x1b\n\x13write_waveform_data\x18\x04 \x01(\x08":\n(CreateSourceWaveformFromFileTDMSResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"z\n&WriteSourceWaveformBroadcastU32Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rwaveform_name\x18\x02 \x01(\t\x12\x15\n\rwaveform_data\x18\x03 \x03(\r"9\n\'WriteSourceWaveformBroadcastU32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xc3\x01\n\'WriteSourceWaveformSiteUniqueU32Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tsite_list\x18\x02 \x01(\t\x12\x15\n\rwaveform_name\x18\x03 \x01(\t\x12\x15\n\rnum_waveforms\x18\x04 \x01(\x11\x12\x1c\n\x14samples_per_waveform\x18\x05 \x01(\x11\x12\x15\n\rwaveform_data\x18\x06 \x03(\r":\n(WriteSourceWaveformSiteUniqueU32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x83\x01\n*WriteSourceWaveformDataFromFileTDMSRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rwaveform_name\x18\x02 \x01(\t\x12\x1a\n\x12waveform_file_path\x18\x03 \x01(\t"=\n+WriteSourceWaveformDataFromFileTDMSResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"s\n$CreateCaptureWaveformParallelRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x10\n\x08pin_list\x18\x02 \x01(\t\x12\x15\n\rwaveform_name\x18\x03 \x01(\t"7\n%CreateCaptureWaveformParallelResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xe8\x01\n"CreateCaptureWaveformSerialRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x10\n\x08pin_list\x18\x02 \x01(\t\x12\x15\n\rwaveform_name\x18\x03 \x01(\t\x12\x14\n\x0csample_width\x18\x04 \x01(\r\x124\n\tbit_order\x18\x05 \x01(\x0e2\x1f.nidigitalpattern_grpc.BitOrderH\x00\x12\x17\n\rbit_order_raw\x18\x06 \x01(\x11H\x00B\x10\n\x0ebit_order_enum"5\n#CreateCaptureWaveformSerialResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x88\x01\n/CreateCaptureWaveformFromFileDigicaptureRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rwaveform_name\x18\x02 \x01(\t\x12\x1a\n\x12waveform_file_path\x18\x03 \x01(\t"B\n0CreateCaptureWaveformFromFileDigicaptureResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x98\x01\n\x1eFetchCaptureWaveformU32Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tsite_list\x18\x02 \x01(\t\x12\x15\n\rwaveform_name\x18\x03 \x01(\t\x12\x17\n\x0fsamples_to_read\x18\x04 \x01(\x11\x12\x0f\n\x07timeout\x18\x05 \x01(\x01"\x82\x01\n\x1fFetchCaptureWaveformU32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04data\x18\x02 \x03(\r\x12\x1c\n\x14actual_num_waveforms\x18\x03 \x01(\x11\x12#\n\x1bactual_samples_per_waveform\x18\x04 \x01(\x11"\xc9\x01\n\x13ExportSignalRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x125\n\x06signal\x18\x02 \x01(\x0e2#.nidigitalpattern_grpc.ExportSignalH\x00\x12\x14\n\nsignal_raw\x18\x03 \x01(\x11H\x00\x12\x19\n\x11signal_identifier\x18\x04 \x01(\t\x12\x17\n\x0foutput_terminal\x18\x05 \x01(\tB\r\n\x0bsignal_enum"&\n\x14ExportSignalResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb2\x01\n\'ConfigureDigitalEdgeStartTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0e\n\x06source\x18\x02 \x01(\t\x122\n\x04edge\x18\x03 \x01(\x0e2".nidigitalpattern_grpc.DigitalEdgeH\x00\x12\x12\n\x08edge_raw\x18\x04 \x01(\x11H\x00B\x0b\n\tedge_enum":\n(ConfigureDigitalEdgeStartTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"N\n(ConfigureSoftwareEdgeStartTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session";\n)ConfigureSoftwareEdgeStartTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"@\n\x1aDisableStartTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"-\n\x1bDisableStartTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xd8\x01\n1ConfigureDigitalEdgeConditionalJumpTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12trigger_identifier\x18\x02 \x01(\t\x12\x0e\n\x06source\x18\x03 \x01(\t\x122\n\x04edge\x18\x04 \x01(\x0e2".nidigitalpattern_grpc.DigitalEdgeH\x00\x12\x12\n\x08edge_raw\x18\x05 \x01(\x11H\x00B\x0b\n\tedge_enum"D\n2ConfigureDigitalEdgeConditionalJumpTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"t\n2ConfigureSoftwareEdgeConditionalJumpTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12trigger_identifier\x18\x02 \x01(\t"E\n3ConfigureSoftwareEdgeConditionalJumpTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"f\n$DisableConditionalJumpTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1a\n\x12trigger_identifier\x18\x02 \x01(\t"7\n%DisableConditionalJumpTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xc2\x01\n\x1eSendSoftwareEdgeTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x129\n\x07trigger\x18\x02 \x01(\x0e2&.nidigitalpattern_grpc.SoftwareTriggerH\x00\x12\x15\n\x0btrigger_raw\x18\x03 \x01(\x11H\x00\x12\x1a\n\x12trigger_identifier\x18\x04 \x01(\tB\x0e\n\x0ctrigger_enum"1\n\x1fSendSoftwareEdgeTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\\\n\x19WriteSequencerFlagRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0c\n\x04flag\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x08",\n\x1aWriteSequencerFlagResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x85\x01\n%WriteSequencerFlagSynchronizedRequest\x12\x15\n\rsession_count\x18\x01 \x01(\r\x12(\n\x08sessions\x18\x02 \x03(\x0b2\x16.nidevice_grpc.Session\x12\x0c\n\x04flag\x18\x03 \x01(\t\x12\r\n\x05value\x18\x04 \x01(\x08"8\n&WriteSequencerFlagSynchronizedResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"L\n\x18ReadSequencerFlagRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0c\n\x04flag\x18\x02 \x01(\t":\n\x19ReadSequencerFlagResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x08"_\n\x1dWriteSequencerRegisterRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0b\n\x03reg\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\x11"0\n\x1eWriteSequencerRegisterResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"O\n\x1cReadSequencerRegisterRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0b\n\x03reg\x18\x02 \x01(\t">\n\x1dReadSequencerRegisterResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x11"\x92\x01\n!EnableMatchFailCombinationRequest\x12\x15\n\rsession_count\x18\x01 \x01(\r\x12(\n\x08sessions\x18\x02 \x03(\x0b2\x16.nidevice_grpc.Session\x12,\n\x0csync_session\x18\x03 \x01(\x0b2\x16.nidevice_grpc.Session"4\n"EnableMatchFailCombinationResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"O\n\x16GetSitePassFailRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tsite_list\x18\x02 \x01(\t"V\n\x17GetSitePassFailResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x11\n\tpass_fail\x18\x02 \x03(\x08\x12\x18\n\x10actual_num_sites\x18\x03 \x01(\x11"O\n\x13GetFailCountRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t"V\n\x14GetFailCountResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rfailure_count\x18\x02 \x03(\x03\x12\x17\n\x0factual_num_read\x18\x03 \x01(\x11"^\n"GetPinResultsPinInformationRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t"\x94\x01\n#GetPinResultsPinInformationResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0bpin_indexes\x18\x02 \x03(\x11\x12\x14\n\x0csite_numbers\x18\x03 \x03(\x11\x12\x17\n\x0fchannel_indexes\x18\x04 \x03(\x11\x12\x19\n\x11actual_num_values\x18\x05 \x01(\x11"\xd5\x01\n GetSiteResultsSiteNumbersRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tsite_list\x18\x02 \x01(\t\x12A\n\x10site_result_type\x18\x03 \x01(\x0e2%.nidigitalpattern_grpc.SiteResultTypeH\x00\x12\x1e\n\x14site_result_type_raw\x18\x04 \x01(\x11H\x00B\x17\n\x15site_result_type_enum"j\n!GetSiteResultsSiteNumbersResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x14\n\x0csite_numbers\x18\x02 \x03(\x11\x12\x1f\n\x17actual_num_site_numbers\x18\x03 \x01(\x11"\x85\x01\n/FrequencyCounterConfigureMeasurementTimeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t\x12\x18\n\x10measurement_time\x18\x03 \x01(\x01"B\n0FrequencyCounterConfigureMeasurementTimeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xdb\x01\n/FrequencyCounterConfigureMeasurementModeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12K\n\x10measurement_mode\x18\x02 \x01(\x0e2/.nidigitalpattern_grpc.FrequencyMeasurementModeH\x00\x12\x1e\n\x14measurement_mode_raw\x18\x03 \x01(\x11H\x00B\x17\n\x15measurement_mode_enum"B\n0FrequencyCounterConfigureMeasurementModeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"c\n\'FrequencyCounterMeasureFrequencyRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_list\x18\x02 \x01(\t"o\n(FrequencyCounterMeasureFrequencyResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0bfrequencies\x18\x02 \x03(\x01\x12\x1e\n\x16actual_num_frequencies\x18\x03 \x01(\x11"V\n\x1fGetChannelNameFromStringRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07indices\x18\x02 \x01(\t"A\n GetChannelNameFromStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05names\x18\x02 \x01(\t*\x8c$\n\x12NiDigitalAttribute\x12#\n\x1fNIDIGITAL_ATTRIBUTE_UNSPECIFIED\x10\x00\x12%\n\x1fNIDIGITAL_ATTRIBUTE_RANGE_CHECK\x10\x92\x8b@\x121\n+NIDIGITAL_ATTRIBUTE_QUERY_INSTRUMENT_STATUS\x10\x93\x8b@\x12\x1f\n\x19NIDIGITAL_ATTRIBUTE_CACHE\x10\x94\x8b@\x12"\n\x1cNIDIGITAL_ATTRIBUTE_SIMULATE\x10\x95\x8b@\x12*\n$NIDIGITAL_ATTRIBUTE_RECORD_COERCIONS\x10\x96\x8b@\x12&\n NIDIGITAL_ATTRIBUTE_DRIVER_SETUP\x10\x97\x8b@\x12+\n%NIDIGITAL_ATTRIBUTE_INTERCHANGE_CHECK\x10\xa5\x8b@\x12\'\n!NIDIGITAL_ATTRIBUTE_CHANNEL_COUNT\x10\xdb\x8c@\x120\n*NIDIGITAL_ATTRIBUTE_SPECIFIC_DRIVER_PREFIX\x10\xbe\x8d@\x120\n*NIDIGITAL_ATTRIBUTE_IO_RESOURCE_DESCRIPTOR\x10\xc0\x8d@\x12&\n NIDIGITAL_ATTRIBUTE_LOGICAL_NAME\x10\xc1\x8d@\x125\n/NIDIGITAL_ATTRIBUTE_SUPPORTED_INSTRUMENT_MODELS\x10\xd7\x8d@\x12,\n&NIDIGITAL_ATTRIBUTE_GROUP_CAPABILITIES\x10\xa1\x8e@\x126\n0NIDIGITAL_ATTRIBUTE_INSTRUMENT_FIRMWARE_REVISION\x10\x8e\x8f@\x121\n+NIDIGITAL_ATTRIBUTE_INSTRUMENT_MANUFACTURER\x10\x8f\x8f@\x120\n*NIDIGITAL_ATTRIBUTE_SPECIFIC_DRIVER_VENDOR\x10\x91\x8f@\x125\n/NIDIGITAL_ATTRIBUTE_SPECIFIC_DRIVER_DESCRIPTION\x10\x92\x8f@\x12B\n<NIDIGITAL_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION\x10\x93\x8f@\x12B\n<NIDIGITAL_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION\x10\x94\x8f@\x122\n,NIDIGITAL_ATTRIBUTE_SPECIFIC_DRIVER_REVISION\x10\xb7\x8f@\x12*\n$NIDIGITAL_ATTRIBUTE_INSTRUMENT_MODEL\x10\x90\x8f@\x12\'\n!NIDIGITAL_ATTRIBUTE_SERIAL_NUMBER\x10\xb1\x98F\x12+\n%NIDIGITAL_ATTRIBUTE_SELECTED_FUNCTION\x10\xb4\x98F\x12*\n$NIDIGITAL_ATTRIBUTE_TERMINATION_MODE\x10\xb6\x98F\x12\x1d\n\x17NIDIGITAL_ATTRIBUTE_VIL\x10\xb7\x98F\x12\x1d\n\x17NIDIGITAL_ATTRIBUTE_VIH\x10\xb8\x98F\x12\x1d\n\x17NIDIGITAL_ATTRIBUTE_VOL\x10\xb9\x98F\x12\x1d\n\x17NIDIGITAL_ATTRIBUTE_VOH\x10\xba\x98F\x12\x1f\n\x19NIDIGITAL_ATTRIBUTE_VTERM\x10\xbb\x98F\x12)\n#NIDIGITAL_ATTRIBUTE_ACTIVE_LOAD_IOL\x10\xbc\x98F\x12)\n#NIDIGITAL_ATTRIBUTE_ACTIVE_LOAD_IOH\x10\xbd\x98F\x12*\n$NIDIGITAL_ATTRIBUTE_ACTIVE_LOAD_VCOM\x10\xbe\x98F\x12.\n(NIDIGITAL_ATTRIBUTE_PPMU_OUTPUT_FUNCTION\x10\xbf\x98F\x12,\n&NIDIGITAL_ATTRIBUTE_PPMU_VOLTAGE_LEVEL\x10\xc0\x98F\x122\n,NIDIGITAL_ATTRIBUTE_PPMU_CURRENT_LIMIT_RANGE\x10\xc1\x98F\x12,\n&NIDIGITAL_ATTRIBUTE_PPMU_CURRENT_LEVEL\x10\xc3\x98F\x122\n,NIDIGITAL_ATTRIBUTE_PPMU_CURRENT_LEVEL_RANGE\x10\xc4\x98F\x120\n*NIDIGITAL_ATTRIBUTE_PPMU_VOLTAGE_LIMIT_LOW\x10\xc5\x98F\x121\n+NIDIGITAL_ATTRIBUTE_PPMU_VOLTAGE_LIMIT_HIGH\x10\xc6\x98F\x12%\n\x1fNIDIGITAL_ATTRIBUTE_START_LABEL\x10\xc7\x98F\x12,\n&NIDIGITAL_ATTRIBUTE_START_TRIGGER_TYPE\x10\xcd\x98F\x12;\n5NIDIGITAL_ATTRIBUTE_DIGITAL_EDGE_START_TRIGGER_SOURCE\x10\xce\x98F\x129\n3NIDIGITAL_ATTRIBUTE_DIGITAL_EDGE_START_TRIGGER_EDGE\x10\xcf\x98F\x12@\n:NIDIGITAL_ATTRIBUTE_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL\x10\xd0\x98F\x125\n/NIDIGITAL_ATTRIBUTE_START_TRIGGER_TERMINAL_NAME\x10\xd7\x98F\x12,\n&NIDIGITAL_ATTRIBUTE_PPMU_APERTURE_TIME\x10\xd5\x98F\x122\n,NIDIGITAL_ATTRIBUTE_PPMU_APERTURE_TIME_UNITS\x10\xd6\x98F\x12G\nANIDIGITAL_ATTRIBUTE_EXPORTED_PATTERN_OPCODE_EVENT_OUTPUT_TERMINAL\x10\xd9\x98F\x12<\n6NIDIGITAL_ATTRIBUTE_PATTERN_OPCODE_EVENT_TERMINAL_NAME\x10\xda\x98F\x122\n,NIDIGITAL_ATTRIBUTE_HISTORY_RAM_TRIGGER_TYPE\x10\xdb\x98F\x12G\nANIDIGITAL_ATTRIBUTE_CYCLE_NUMBER_HISTORY_RAM_TRIGGER_CYCLE_NUMBER\x10\xdc\x98F\x12H\nBNIDIGITAL_ATTRIBUTE_PATTERN_LABEL_HISTORY_RAM_TRIGGER_CYCLE_OFFSET\x10\xdd\x98F\x12A\n;NIDIGITAL_ATTRIBUTE_PATTERN_LABEL_HISTORY_RAM_TRIGGER_LABEL\x10\xde\x98F\x127\n1NIDIGITAL_ATTRIBUTE_HISTORY_RAM_CYCLES_TO_ACQUIRE\x10\xdf\x98F\x128\n2NIDIGITAL_ATTRIBUTE_HISTORY_RAM_PRETRIGGER_SAMPLES\x10\xe0\x98F\x122\n,NIDIGITAL_ATTRIBUTE_TDR_ENDPOINT_TERMINATION\x10\x81\x99F\x12*\n$NIDIGITAL_ATTRIBUTE_RIO_TRIGGER_TYPE\x10\x86\x99F\x129\n3NIDIGITAL_ATTRIBUTE_DIGITAL_EDGE_RIO_TRIGGER_SOURCE\x10\x87\x99F\x127\n1NIDIGITAL_ATTRIBUTE_DIGITAL_EDGE_RIO_TRIGGER_EDGE\x10\x88\x99F\x123\n-NIDIGITAL_ATTRIBUTE_RIO_TRIGGER_TERMINAL_NAME\x10\x89\x99F\x12<\n6NIDIGITAL_ATTRIBUTE_EXPORTED_RIO_EVENT_OUTPUT_TERMINAL\x10\x8a\x99F\x121\n+NIDIGITAL_ATTRIBUTE_RIO_EVENT_TERMINAL_NAME\x10\x8b\x99F\x12$\n\x1eNIDIGITAL_ATTRIBUTE_TDR_OFFSET\x10\xe3\x98F\x12I\nCNIDIGITAL_ATTRIBUTE_PATTERN_LABEL_HISTORY_RAM_TRIGGER_VECTOR_OFFSET\x10\xe4\x98F\x12,\n&NIDIGITAL_ATTRIBUTE_PPMU_CURRENT_LIMIT\x10\xe6\x98F\x126\n0NIDIGITAL_ATTRIBUTE_PPMU_CURRENT_LIMIT_SUPPORTED\x10\xe7\x98F\x126\n0NIDIGITAL_ATTRIBUTE_SEQUENCER_FLAG_TERMINAL_NAME\x10\xeb\x98F\x12&\n NIDIGITAL_ATTRIBUTE_MASK_COMPARE\x10\xec\x98F\x123\n-NIDIGITAL_ATTRIBUTE_HALT_ON_KEEP_ALIVE_OPCODE\x10\xee\x98F\x12.\n(NIDIGITAL_ATTRIBUTE_IS_KEEP_ALIVE_ACTIVE\x10\xef\x98F\x125\n/NIDIGITAL_ATTRIBUTE_PPMU_CURRENT_LIMIT_BEHAVIOR\x10\xf0\x98F\x12<\n6NIDIGITAL_ATTRIBUTE_FREQUENCY_COUNTER_MEASUREMENT_TIME\x10\xf5\x98F\x12<\n6NIDIGITAL_ATTRIBUTE_FREQUENCY_COUNTER_MEASUREMENT_MODE\x10\x84\x99F\x12>\n8NIDIGITAL_ATTRIBUTE_FREQUENCY_COUNTER_HYSTERESIS_ENABLED\x10\x85\x99F\x127\n1NIDIGITAL_ATTRIBUTE_TIMING_ABSOLUTE_DELAY_ENABLED\x10\xf7\x98F\x12/\n)NIDIGITAL_ATTRIBUTE_TIMING_ABSOLUTE_DELAY\x10\xf8\x98F\x123\n-NIDIGITAL_ATTRIBUTE_CLOCK_GENERATOR_FREQUENCY\x10\xf9\x98F\x124\n.NIDIGITAL_ATTRIBUTE_CLOCK_GENERATOR_IS_RUNNING\x10\xfa\x98F\x12;\n5NIDIGITAL_ATTRIBUTE_PPMU_ALLOW_EXTENDED_VOLTAGE_RANGE\x10\xfc\x98F\x12E\n?NIDIGITAL_ATTRIBUTE_HISTORY_RAM_MAX_SAMPLES_TO_ACQUIRE_PER_SITE\x10\xfd\x98F\x12A\n;NIDIGITAL_ATTRIBUTE_HISTORY_RAM_NUMBER_OF_SAMPLES_IS_FINITE\x10\xfe\x98F\x12:\n4NIDIGITAL_ATTRIBUTE_HISTORY_RAM_BUFFER_SIZE_PER_SITE\x10\xff\x98F\x127\n1NIDIGITAL_ATTRIBUTE_CONDITIONAL_JUMP_TRIGGER_TYPE\x10\xd1\x98F\x12F\n@NIDIGITAL_ATTRIBUTE_DIGITAL_EDGE_CONDITIONAL_JUMP_TRIGGER_SOURCE\x10\xd2\x98F\x12D\n>NIDIGITAL_ATTRIBUTE_DIGITAL_EDGE_CONDITIONAL_JUMP_TRIGGER_EDGE\x10\xd3\x98F\x12K\nENIDIGITAL_ATTRIBUTE_EXPORTED_CONDITIONAL_JUMP_TRIGGER_OUTPUT_TERMINAL\x10\xd4\x98F\x12@\n:NIDIGITAL_ATTRIBUTE_CONDITIONAL_JUMP_TRIGGER_TERMINAL_NAME\x10\xd8\x98F*v\n\x15PpmuApertureTimeUnits\x12(\n$PPMU_APERTURE_TIME_UNITS_UNSPECIFIED\x10\x00\x123\n.PPMU_APERTURE_TIME_UNITS_NIDIGITAL_VAL_SECONDS\x10\xb4\x10*u\n\x08BitOrder\x12\x19\n\x15BIT_ORDER_UNSPECIFIED\x10\x00\x12&\n!BIT_ORDER_NIDIGITAL_VAL_MSB_FIRST\x10\xc4\x13\x12&\n!BIT_ORDER_NIDIGITAL_VAL_LSB_FIRST\x10\xc5\x13*\x86\x01\n\x0bDigitalEdge\x12\x1c\n\x18DIGITAL_EDGE_UNSPECIFIED\x10\x00\x12+\n&DIGITAL_EDGE_NIDIGITAL_VAL_RISING_EDGE\x10\x88\x0e\x12,\n\'DIGITAL_EDGE_NIDIGITAL_VAL_FALLING_EDGE\x10\x89\x0e*\x84\x03\n\x08PinState\x12\x1d\n\x19PIN_STATE_NIDIGITAL_VAL_0\x10\x00\x12\x1d\n\x19PIN_STATE_NIDIGITAL_VAL_1\x10\x01\x12\x1d\n\x19PIN_STATE_NIDIGITAL_VAL_L\x10\x03\x12\x1d\n\x19PIN_STATE_NIDIGITAL_VAL_H\x10\x04\x12\x1d\n\x19PIN_STATE_NIDIGITAL_VAL_X\x10\x05\x12\x1d\n\x19PIN_STATE_NIDIGITAL_VAL_M\x10\x06\x12\x1d\n\x19PIN_STATE_NIDIGITAL_VAL_V\x10\x07\x12\x1d\n\x19PIN_STATE_NIDIGITAL_VAL_D\x10\x08\x12\x1d\n\x19PIN_STATE_NIDIGITAL_VAL_E\x10\t\x12,\n\'PIN_STATE_NIDIGITAL_VAL_NOT_A_PIN_STATE\x10\xfe\x01\x123\n.PIN_STATE_NIDIGITAL_VAL_PIN_STATE_NOT_ACQUIRED\x10\xff\x01*\xbc\x01\n\x0bDriveFormat\x12\x1c\n\x18DRIVE_FORMAT_UNSPECIFIED\x10\x00\x12"\n\x1dDRIVE_FORMAT_NIDIGITAL_VAL_NR\x10\xdc\x0b\x12"\n\x1dDRIVE_FORMAT_NIDIGITAL_VAL_RL\x10\xdd\x0b\x12"\n\x1dDRIVE_FORMAT_NIDIGITAL_VAL_RH\x10\xde\x0b\x12#\n\x1eDRIVE_FORMAT_NIDIGITAL_VAL_SBC\x10\xdf\x0b*\xc7\x01\n\x19HistoryRamCyclesToAcquire\x12-\n)HISTORY_RAM_CYCLES_TO_ACQUIRE_UNSPECIFIED\x10\x00\x12>\n9HISTORY_RAM_CYCLES_TO_ACQUIRE_NIDIGITAL_VAL_FAILED_CYCLES\x10\xff\x11\x12;\n6HISTORY_RAM_CYCLES_TO_ACQUIRE_NIDIGITAL_VAL_ALL_CYCLES\x10\x80\x12*\x88\x01\n\x18PpmuCurrentLimitBehavior\x12+\n\'PPMU_CURRENT_LIMIT_BEHAVIOR_UNSPECIFIED\x10\x00\x12?\n:PPMU_CURRENT_LIMIT_BEHAVIOR_NIDIGITAL_VAL_CURRENT_REGULATE\x10\x9c\x18*\xb0\x01\n\x13PpmuMeasurementType\x12%\n!PPMU_MEASUREMENT_TYPE_UNSPECIFIED\x10\x00\x128\n3PPMU_MEASUREMENT_TYPE_NIDIGITAL_VAL_MEASURE_CURRENT\x10\xe0\x12\x128\n3PPMU_MEASUREMENT_TYPE_NIDIGITAL_VAL_MEASURE_VOLTAGE\x10\xe1\x12*\xa2\x01\n\x12PpmuOutputFunction\x12$\n PPMU_OUTPUT_FUNCTION_UNSPECIFIED\x10\x00\x122\n-PPMU_OUTPUT_FUNCTION_NIDIGITAL_VAL_DC_VOLTAGE\x10\x94\n\x122\n-PPMU_OUTPUT_FUNCTION_NIDIGITAL_VAL_DC_CURRENT\x10\x95\n*\x93\x02\n\x10SelectedFunction\x12!\n\x1dSELECTED_FUNCTION_UNSPECIFIED\x10\x00\x12,\n\'SELECTED_FUNCTION_NIDIGITAL_VAL_DIGITAL\x10\xcc\x08\x12)\n$SELECTED_FUNCTION_NIDIGITAL_VAL_PPMU\x10\xcd\x08\x12(\n#SELECTED_FUNCTION_NIDIGITAL_VAL_OFF\x10\xce\x08\x12/\n*SELECTED_FUNCTION_NIDIGITAL_VAL_DISCONNECT\x10\xcf\x08\x12(\n#SELECTED_FUNCTION_NIDIGITAL_VAL_RIO\x10\xd0\x08*\xa7\x02\n\x0cExportSignal\x12\x1d\n\x19EXPORT_SIGNAL_UNSPECIFIED\x10\x00\x12.\n)EXPORT_SIGNAL_NIDIGITAL_VAL_START_TRIGGER\x10\xd0\x0f\x129\n4EXPORT_SIGNAL_NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER\x10\xd1\x0f\x125\n0EXPORT_SIGNAL_NIDIGITAL_VAL_PATTERN_OPCODE_EVENT\x10\xd2\x0f\x12*\n%EXPORT_SIGNAL_NIDIGITAL_VAL_REF_CLOCK\x10\xd3\x0f\x12*\n%EXPORT_SIGNAL_NIDIGITAL_VAL_RIO_EVENT\x10\xd4\x0f*\x97\x01\n\x0eSiteResultType\x12 \n\x1cSITE_RESULT_TYPE_UNSPECIFIED\x10\x00\x12-\n(SITE_RESULT_TYPE_NIDIGITAL_VAL_PASS_FAIL\x10\xe4\x19\x124\n/SITE_RESULT_TYPE_NIDIGITAL_VAL_CAPTURE_WAVEFORM\x10\xe5\x19*\xa4\x01\n\x0fSoftwareTrigger\x12 \n\x1cSOFTWARE_TRIGGER_UNSPECIFIED\x10\x00\x121\n,SOFTWARE_TRIGGER_NIDIGITAL_VAL_START_TRIGGER\x10\xd0\x0f\x12<\n7SOFTWARE_TRIGGER_NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER\x10\xd1\x0f*\x9e\x01\n\x11SourceDataMapping\x12#\n\x1fSOURCE_DATA_MAPPING_UNSPECIFIED\x10\x00\x120\n+SOURCE_DATA_MAPPING_NIDIGITAL_VAL_BROADCAST\x10\xa8\x14\x122\n-SOURCE_DATA_MAPPING_NIDIGITAL_VAL_SITE_UNIQUE\x10\xa9\x14*\xbb\x01\n\x0fTerminationMode\x12 \n\x1cTERMINATION_MODE_UNSPECIFIED\x10\x00\x12/\n*TERMINATION_MODE_NIDIGITAL_VAL_ACTIVE_LOAD\x10\xb0\t\x12)\n$TERMINATION_MODE_NIDIGITAL_VAL_VTERM\x10\xb1\t\x12*\n%TERMINATION_MODE_NIDIGITAL_VAL_HIGH_Z\x10\xb2\t*\xd1\x03\n\x0fTimeSetEdgeType\x12"\n\x1eTIME_SET_EDGE_TYPE_UNSPECIFIED\x10\x00\x12.\n)TIME_SET_EDGE_TYPE_NIDIGITAL_VAL_DRIVE_ON\x10\xf0\x15\x120\n+TIME_SET_EDGE_TYPE_NIDIGITAL_VAL_DRIVE_DATA\x10\xf1\x15\x122\n-TIME_SET_EDGE_TYPE_NIDIGITAL_VAL_DRIVE_RETURN\x10\xf2\x15\x12/\n*TIME_SET_EDGE_TYPE_NIDIGITAL_VAL_DRIVE_OFF\x10\xf3\x15\x124\n/TIME_SET_EDGE_TYPE_NIDIGITAL_VAL_COMPARE_STROBE\x10\xf4\x15\x121\n,TIME_SET_EDGE_TYPE_NIDIGITAL_VAL_DRIVE_DATA2\x10\xf5\x15\x123\n.TIME_SET_EDGE_TYPE_NIDIGITAL_VAL_DRIVE_RETURN2\x10\xf6\x15\x125\n0TIME_SET_EDGE_TYPE_NIDIGITAL_VAL_COMPARE_STROBE2\x10\xf7\x15*\xb4\x01\n\x18FrequencyMeasurementMode\x12*\n&FREQUENCY_MEASUREMENT_MODE_UNSPECIFIED\x10\x00\x124\n/FREQUENCY_MEASUREMENT_MODE_NIDIGITAL_VAL_BANKED\x10\xf4\x1c\x126\n1FREQUENCY_MEASUREMENT_MODE_NIDIGITAL_VAL_PARALLEL\x10\xf5\x1c*\x99\x01\n\x13WriteStaticPinState\x12*\n&WRITE_STATIC_PIN_STATE_NIDIGITAL_VAL_0\x10\x00\x12*\n&WRITE_STATIC_PIN_STATE_NIDIGITAL_VAL_1\x10\x01\x12*\n&WRITE_STATIC_PIN_STATE_NIDIGITAL_VAL_X\x10\x05*\xf3\x0c\n\x1dNiDigitalInt32AttributeValues\x12\x1f\n\x1bNIDIGITAL_INT32_UNSPECIFIED\x10\x00\x121\n,NIDIGITAL_INT32_DIGITAL_EDGE_VAL_RISING_EDGE\x10\x88\x0e\x122\n-NIDIGITAL_INT32_DIGITAL_EDGE_VAL_FALLING_EDGE\x10\x89\x0e\x12:\n5NIDIGITAL_INT32_FREQUENCY_MEASUREMENT_MODE_VAL_BANKED\x10\xf4\x1c\x12<\n7NIDIGITAL_INT32_FREQUENCY_MEASUREMENT_MODE_VAL_PARALLEL\x10\xf5\x1c\x12D\n?NIDIGITAL_INT32_HISTORY_RAM_CYCLES_TO_ACQUIRE_VAL_FAILED_CYCLES\x10\xff\x11\x12A\n<NIDIGITAL_INT32_HISTORY_RAM_CYCLES_TO_ACQUIRE_VAL_ALL_CYCLES\x10\x80\x12\x12`\nSNIDIGITAL_INT32_HISTORY_RAM_MAX_SAMPLES_TO_ACQUIRE_PER_SITE_VAL_ACQUIRE_ALL_SAMPLES\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12?\n:NIDIGITAL_INT32_HISTORY_RAM_TRIGGER_TYPE_VAL_FIRST_FAILURE\x10\x98\x11\x12>\n9NIDIGITAL_INT32_HISTORY_RAM_TRIGGER_TYPE_VAL_CYCLE_NUMBER\x10\x99\x11\x12?\n:NIDIGITAL_INT32_HISTORY_RAM_TRIGGER_TYPE_VAL_PATTERN_LABEL\x10\x9a\x11\x129\n4NIDIGITAL_INT32_PPMU_APERTURE_TIME_UNITS_VAL_SECONDS\x10\xb4\x10\x12E\n@NIDIGITAL_INT32_PPMU_CURRENT_LIMIT_BEHAVIOR_VAL_CURRENT_REGULATE\x10\x9c\x18\x128\n3NIDIGITAL_INT32_PPMU_OUTPUT_FUNCTION_VAL_DC_VOLTAGE\x10\x94\n\x128\n3NIDIGITAL_INT32_PPMU_OUTPUT_FUNCTION_VAL_DC_CURRENT\x10\x95\n\x122\n-NIDIGITAL_INT32_SELECTED_FUNCTION_VAL_DIGITAL\x10\xcc\x08\x12/\n*NIDIGITAL_INT32_SELECTED_FUNCTION_VAL_PPMU\x10\xcd\x08\x12.\n)NIDIGITAL_INT32_SELECTED_FUNCTION_VAL_OFF\x10\xce\x08\x125\n0NIDIGITAL_INT32_SELECTED_FUNCTION_VAL_DISCONNECT\x10\xcf\x08\x12.\n)NIDIGITAL_INT32_SELECTED_FUNCTION_VAL_RIO\x10\xd0\x08\x12=\n8NIDIGITAL_INT32_TDR_ENDPOINT_TERMINATION_VAL_TDR_TO_OPEN\x10\x90\x1c\x12H\nCNIDIGITAL_INT32_TDR_ENDPOINT_TERMINATION_VAL_TDR_TO_SHORT_TO_GROUND\x10\x91\x1c\x125\n0NIDIGITAL_INT32_TERMINATION_MODE_VAL_ACTIVE_LOAD\x10\xb0\t\x12/\n*NIDIGITAL_INT32_TERMINATION_MODE_VAL_VTERM\x10\xb1\t\x120\n+NIDIGITAL_INT32_TERMINATION_MODE_VAL_HIGH_Z\x10\xb2\t\x12*\n%NIDIGITAL_INT32_TRIGGER_TYPE_VAL_NONE\x10\xa4\r\x122\n-NIDIGITAL_INT32_TRIGGER_TYPE_VAL_DIGITAL_EDGE\x10\xa5\r\x12.\n)NIDIGITAL_INT32_TRIGGER_TYPE_VAL_SOFTWARE\x10\xa6\r2\xd0\x85\x01\n\tNiDigital\x12O\n\x04Init\x12".nidigitalpattern_grpc.InitRequest\x1a#.nidigitalpattern_grpc.InitResponse\x12p\n\x0fInitWithOptions\x12-.nidigitalpattern_grpc.InitWithOptionsRequest\x1a..nidigitalpattern_grpc.InitWithOptionsResponse\x12R\n\x05Close\x12#.nidigitalpattern_grpc.CloseRequest\x1a$.nidigitalpattern_grpc.CloseResponse\x12R\n\x05Reset\x12#.nidigitalpattern_grpc.ResetRequest\x1a$.nidigitalpattern_grpc.ResetResponse\x12d\n\x0bResetDevice\x12).nidigitalpattern_grpc.ResetDeviceRequest\x1a*.nidigitalpattern_grpc.ResetDeviceResponse\x12[\n\x08SelfTest\x12&.nidigitalpattern_grpc.SelfTestRequest\x1a\'.nidigitalpattern_grpc.SelfTestResponse\x12[\n\x08GetError\x12&.nidigitalpattern_grpc.GetErrorRequest\x1a\'.nidigitalpattern_grpc.GetErrorResponse\x12a\n\nClearError\x12(.nidigitalpattern_grpc.ClearErrorRequest\x1a).nidigitalpattern_grpc.ClearErrorResponse\x12g\n\x0cErrorMessage\x12*.nidigitalpattern_grpc.ErrorMessageRequest\x1a+.nidigitalpattern_grpc.ErrorMessageResponse\x12j\n\rSelfCalibrate\x12+.nidigitalpattern_grpc.SelfCalibrateRequest\x1a,.nidigitalpattern_grpc.SelfCalibrateResponse\x12|\n\x13GetAttributeViInt32\x121.nidigitalpattern_grpc.GetAttributeViInt32Request\x1a2.nidigitalpattern_grpc.GetAttributeViInt32Response\x12|\n\x13GetAttributeViInt64\x121.nidigitalpattern_grpc.GetAttributeViInt64Request\x1a2.nidigitalpattern_grpc.GetAttributeViInt64Response\x12\x7f\n\x14GetAttributeViReal64\x122.nidigitalpattern_grpc.GetAttributeViReal64Request\x1a3.nidigitalpattern_grpc.GetAttributeViReal64Response\x12\x7f\n\x14GetAttributeViString\x122.nidigitalpattern_grpc.GetAttributeViStringRequest\x1a3.nidigitalpattern_grpc.GetAttributeViStringResponse\x12\x82\x01\n\x15GetAttributeViSession\x123.nidigitalpattern_grpc.GetAttributeViSessionRequest\x1a4.nidigitalpattern_grpc.GetAttributeViSessionResponse\x12\x82\x01\n\x15GetAttributeViBoolean\x123.nidigitalpattern_grpc.GetAttributeViBooleanRequest\x1a4.nidigitalpattern_grpc.GetAttributeViBooleanResponse\x12|\n\x13SetAttributeViInt32\x121.nidigitalpattern_grpc.SetAttributeViInt32Request\x1a2.nidigitalpattern_grpc.SetAttributeViInt32Response\x12|\n\x13SetAttributeViInt64\x121.nidigitalpattern_grpc.SetAttributeViInt64Request\x1a2.nidigitalpattern_grpc.SetAttributeViInt64Response\x12\x7f\n\x14SetAttributeViReal64\x122.nidigitalpattern_grpc.SetAttributeViReal64Request\x1a3.nidigitalpattern_grpc.SetAttributeViReal64Response\x12\x7f\n\x14SetAttributeViString\x122.nidigitalpattern_grpc.SetAttributeViStringRequest\x1a3.nidigitalpattern_grpc.SetAttributeViStringResponse\x12\x82\x01\n\x15SetAttributeViSession\x123.nidigitalpattern_grpc.SetAttributeViSessionRequest\x1a4.nidigitalpattern_grpc.SetAttributeViSessionResponse\x12\x82\x01\n\x15SetAttributeViBoolean\x123.nidigitalpattern_grpc.SetAttributeViBooleanRequest\x1a4.nidigitalpattern_grpc.SetAttributeViBooleanResponse\x12m\n\x0eResetAttribute\x12,.nidigitalpattern_grpc.ResetAttributeRequest\x1a-.nidigitalpattern_grpc.ResetAttributeResponse\x12a\n\nLoadPinMap\x12(.nidigitalpattern_grpc.LoadPinMapRequest\x1a).nidigitalpattern_grpc.LoadPinMapResponse\x12d\n\x0bEnableSites\x12).nidigitalpattern_grpc.EnableSitesRequest\x1a*.nidigitalpattern_grpc.EnableSitesResponse\x12g\n\x0cDisableSites\x12*.nidigitalpattern_grpc.DisableSitesRequest\x1a+.nidigitalpattern_grpc.DisableSitesResponse\x12j\n\rIsSiteEnabled\x12+.nidigitalpattern_grpc.IsSiteEnabledRequest\x1a,.nidigitalpattern_grpc.IsSiteEnabledResponse\x12g\n\x0cCreatePinMap\x12*.nidigitalpattern_grpc.CreatePinMapRequest\x1a+.nidigitalpattern_grpc.CreatePinMapResponse\x12m\n\x0eCreatePinGroup\x12,.nidigitalpattern_grpc.CreatePinGroupRequest\x1a-.nidigitalpattern_grpc.CreatePinGroupResponse\x12s\n\x10CreateChannelMap\x12..nidigitalpattern_grpc.CreateChannelMapRequest\x1a/.nidigitalpattern_grpc.CreateChannelMapResponse\x12p\n\x0fMapPinToChannel\x12-.nidigitalpattern_grpc.MapPinToChannelRequest\x1a..nidigitalpattern_grpc.MapPinToChannelResponse\x12j\n\rEndChannelMap\x12+.nidigitalpattern_grpc.EndChannelMapRequest\x1a,.nidigitalpattern_grpc.EndChannelMapResponse\x12a\n\nGetPinName\x12(.nidigitalpattern_grpc.GetPinNameRequest\x1a).nidigitalpattern_grpc.GetPinNameResponse\x12m\n\x0eGetChannelName\x12,.nidigitalpattern_grpc.GetChannelNameRequest\x1a-.nidigitalpattern_grpc.GetChannelNameResponse\x12m\n\x0eSelectFunction\x12,.nidigitalpattern_grpc.SelectFunctionRequest\x1a-.nidigitalpattern_grpc.SelectFunctionResponse\x12a\n\nReadStatic\x12(.nidigitalpattern_grpc.ReadStaticRequest\x1a).nidigitalpattern_grpc.ReadStaticResponse\x12d\n\x0bWriteStatic\x12).nidigitalpattern_grpc.WriteStaticRequest\x1a*.nidigitalpattern_grpc.WriteStaticResponse\x12\x94\x01\n\x1bClockGeneratorGenerateClock\x129.nidigitalpattern_grpc.ClockGeneratorGenerateClockRequest\x1a:.nidigitalpattern_grpc.ClockGeneratorGenerateClockResponse\x12\x85\x01\n\x16ClockGeneratorInitiate\x124.nidigitalpattern_grpc.ClockGeneratorInitiateRequest\x1a5.nidigitalpattern_grpc.ClockGeneratorInitiateResponse\x12|\n\x13ClockGeneratorAbort\x121.nidigitalpattern_grpc.ClockGeneratorAbortRequest\x1a2.nidigitalpattern_grpc.ClockGeneratorAbortResponse\x12y\n\x12LoadSpecifications\x120.nidigitalpattern_grpc.LoadSpecificationsRequest\x1a1.nidigitalpattern_grpc.LoadSpecificationsResponse\x12\x7f\n\x14UnloadSpecifications\x122.nidigitalpattern_grpc.UnloadSpecificationsRequest\x1a3.nidigitalpattern_grpc.UnloadSpecificationsResponse\x12a\n\nLoadLevels\x12(.nidigitalpattern_grpc.LoadLevelsRequest\x1a).nidigitalpattern_grpc.LoadLevelsResponse\x12a\n\nLoadTiming\x12(.nidigitalpattern_grpc.LoadTimingRequest\x1a).nidigitalpattern_grpc.LoadTimingResponse\x12\x7f\n\x14ApplyLevelsAndTiming\x122.nidigitalpattern_grpc.ApplyLevelsAndTimingRequest\x1a3.nidigitalpattern_grpc.ApplyLevelsAndTimingResponse\x12\x85\x01\n\x16ConfigureVoltageLevels\x124.nidigitalpattern_grpc.ConfigureVoltageLevelsRequest\x1a5.nidigitalpattern_grpc.ConfigureVoltageLevelsResponse\x12\x8e\x01\n\x19ConfigureActiveLoadLevels\x127.nidigitalpattern_grpc.ConfigureActiveLoadLevelsRequest\x1a8.nidigitalpattern_grpc.ConfigureActiveLoadLevelsResponse\x12\x8b\x01\n\x18ConfigureTerminationMode\x126.nidigitalpattern_grpc.ConfigureTerminationModeRequest\x1a7.nidigitalpattern_grpc.ConfigureTerminationModeResponse\x12j\n\rCreateTimeSet\x12+.nidigitalpattern_grpc.CreateTimeSetRequest\x1a,.nidigitalpattern_grpc.CreateTimeSetResponse\x12\x85\x01\n\x16ConfigureTimeSetPeriod\x124.nidigitalpattern_grpc.ConfigureTimeSetPeriodRequest\x1a5.nidigitalpattern_grpc.ConfigureTimeSetPeriodResponse\x12\x91\x01\n\x1aConfigureTimeSetDriveEdges\x128.nidigitalpattern_grpc.ConfigureTimeSetDriveEdgesRequest\x1a9.nidigitalpattern_grpc.ConfigureTimeSetDriveEdgesResponse\x12\xa9\x01\n"ConfigureTimeSetCompareEdgesStrobe\x12@.nidigitalpattern_grpc.ConfigureTimeSetCompareEdgesStrobeRequest\x1aA.nidigitalpattern_grpc.ConfigureTimeSetCompareEdgesStrobeResponse\x12\x94\x01\n\x1bConfigureTimeSetDriveFormat\x129.nidigitalpattern_grpc.ConfigureTimeSetDriveFormatRequest\x1a:.nidigitalpattern_grpc.ConfigureTimeSetDriveFormatResponse\x12v\n\x11DeleteAllTimeSets\x12/.nidigitalpattern_grpc.DeleteAllTimeSetsRequest\x1a0.nidigitalpattern_grpc.DeleteAllTimeSetsResponse\x12\x9d\x01\n\x1eConfigureTimeSetEdgeMultiplier\x12<.nidigitalpattern_grpc.ConfigureTimeSetEdgeMultiplierRequest\x1a=.nidigitalpattern_grpc.ConfigureTimeSetEdgeMultiplierResponse\x12\x97\x01\n\x1cConfigureTimeSetDriveEdges2x\x12:.nidigitalpattern_grpc.ConfigureTimeSetDriveEdges2xRequest\x1a;.nidigitalpattern_grpc.ConfigureTimeSetDriveEdges2xResponse\x12\xaf\x01\n$ConfigureTimeSetCompareEdgesStrobe2x\x12B.nidigitalpattern_grpc.ConfigureTimeSetCompareEdgesStrobe2xRequest\x1aC.nidigitalpattern_grpc.ConfigureTimeSetCompareEdgesStrobe2xResponse\x12\x7f\n\x14ConfigureTimeSetEdge\x122.nidigitalpattern_grpc.ConfigureTimeSetEdgeRequest\x1a3.nidigitalpattern_grpc.ConfigureTimeSetEdgeResponse\x12s\n\x10GetTimeSetPeriod\x12..nidigitalpattern_grpc.GetTimeSetPeriodRequest\x1a/.nidigitalpattern_grpc.GetTimeSetPeriodResponse\x12m\n\x0eGetTimeSetEdge\x12,.nidigitalpattern_grpc.GetTimeSetEdgeRequest\x1a-.nidigitalpattern_grpc.GetTimeSetEdgeResponse\x12\x8b\x01\n\x18GetTimeSetEdgeMultiplier\x126.nidigitalpattern_grpc.GetTimeSetEdgeMultiplierRequest\x1a7.nidigitalpattern_grpc.GetTimeSetEdgeMultiplierResponse\x12\x82\x01\n\x15GetTimeSetDriveFormat\x123.nidigitalpattern_grpc.GetTimeSetDriveFormatRequest\x1a4.nidigitalpattern_grpc.GetTimeSetDriveFormatResponse\x12m\n\x0eGetTimeSetName\x12,.nidigitalpattern_grpc.GetTimeSetNameRequest\x1a-.nidigitalpattern_grpc.GetTimeSetNameResponse\x12L\n\x03TDR\x12!.nidigitalpattern_grpc.TDRRequest\x1a".nidigitalpattern_grpc.TDRResponse\x12p\n\x0fApplyTDROffsets\x12-.nidigitalpattern_grpc.ApplyTDROffsetsRequest\x1a..nidigitalpattern_grpc.ApplyTDROffsetsResponse\x12\x94\x01\n\x1bPPMUConfigureOutputFunction\x129.nidigitalpattern_grpc.PPMUConfigureOutputFunctionRequest\x1a:.nidigitalpattern_grpc.PPMUConfigureOutputFunctionResponse\x12\x8e\x01\n\x19PPMUConfigureApertureTime\x127.nidigitalpattern_grpc.PPMUConfigureApertureTimeRequest\x1a8.nidigitalpattern_grpc.PPMUConfigureApertureTimeResponse\x12\x8e\x01\n\x19PPMUConfigureVoltageLevel\x127.nidigitalpattern_grpc.PPMUConfigureVoltageLevelRequest\x1a8.nidigitalpattern_grpc.PPMUConfigureVoltageLevelResponse\x12\x8e\x01\n\x19PPMUConfigureCurrentLimit\x127.nidigitalpattern_grpc.PPMUConfigureCurrentLimitRequest\x1a8.nidigitalpattern_grpc.PPMUConfigureCurrentLimitResponse\x12\x9d\x01\n\x1ePPMUConfigureCurrentLimitRange\x12<.nidigitalpattern_grpc.PPMUConfigureCurrentLimitRangeRequest\x1a=.nidigitalpattern_grpc.PPMUConfigureCurrentLimitRangeResponse\x12\x8e\x01\n\x19PPMUConfigureCurrentLevel\x127.nidigitalpattern_grpc.PPMUConfigureCurrentLevelRequest\x1a8.nidigitalpattern_grpc.PPMUConfigureCurrentLevelResponse\x12\x9d\x01\n\x1ePPMUConfigureCurrentLevelRange\x12<.nidigitalpattern_grpc.PPMUConfigureCurrentLevelRangeRequest\x1a=.nidigitalpattern_grpc.PPMUConfigureCurrentLevelRangeResponse\x12\x91\x01\n\x1aPPMUConfigureVoltageLimits\x128.nidigitalpattern_grpc.PPMUConfigureVoltageLimitsRequest\x1a9.nidigitalpattern_grpc.PPMUConfigureVoltageLimitsResponse\x12a\n\nPPMUSource\x12(.nidigitalpattern_grpc.PPMUSourceRequest\x1a).nidigitalpattern_grpc.PPMUSourceResponse\x12d\n\x0bPPMUMeasure\x12).nidigitalpattern_grpc.PPMUMeasureRequest\x1a*.nidigitalpattern_grpc.PPMUMeasureResponse\x12d\n\x0bLoadPattern\x12).nidigitalpattern_grpc.LoadPatternRequest\x1a*.nidigitalpattern_grpc.LoadPatternResponse\x12v\n\x11UnloadAllPatterns\x12/.nidigitalpattern_grpc.UnloadAllPatternsRequest\x1a0.nidigitalpattern_grpc.UnloadAllPatternsResponse\x12|\n\x13ConfigureStartLabel\x121.nidigitalpattern_grpc.ConfigureStartLabelRequest\x1a2.nidigitalpattern_grpc.ConfigureStartLabelResponse\x12\x91\x01\n\x1aConfigurePatternBurstSites\x128.nidigitalpattern_grpc.ConfigurePatternBurstSitesRequest\x1a9.nidigitalpattern_grpc.ConfigurePatternBurstSitesResponse\x12\x7f\n\x14GetPatternPinIndexes\x122.nidigitalpattern_grpc.GetPatternPinIndexesRequest\x1a3.nidigitalpattern_grpc.GetPatternPinIndexesResponse\x12v\n\x11GetPatternPinList\x12/.nidigitalpattern_grpc.GetPatternPinListRequest\x1a0.nidigitalpattern_grpc.GetPatternPinListResponse\x12m\n\x0eGetPatternName\x12,.nidigitalpattern_grpc.GetPatternNameRequest\x1a-.nidigitalpattern_grpc.GetPatternNameResponse\x12g\n\x0cBurstPattern\x12*.nidigitalpattern_grpc.BurstPatternRequest\x1a+.nidigitalpattern_grpc.BurstPatternResponse\x12\x8b\x01\n\x18BurstPatternSynchronized\x126.nidigitalpattern_grpc.BurstPatternSynchronizedRequest\x1a7.nidigitalpattern_grpc.BurstPatternSynchronizedResponse\x12U\n\x06Commit\x12$.nidigitalpattern_grpc.CommitRequest\x1a%.nidigitalpattern_grpc.CommitResponse\x12[\n\x08Initiate\x12&.nidigitalpattern_grpc.InitiateRequest\x1a\'.nidigitalpattern_grpc.InitiateResponse\x12U\n\x06IsDone\x12$.nidigitalpattern_grpc.IsDoneRequest\x1a%.nidigitalpattern_grpc.IsDoneResponse\x12j\n\rWaitUntilDone\x12+.nidigitalpattern_grpc.WaitUntilDoneRequest\x1a,.nidigitalpattern_grpc.WaitUntilDoneResponse\x12R\n\x05Abort\x12#.nidigitalpattern_grpc.AbortRequest\x1a$.nidigitalpattern_grpc.AbortResponse\x12m\n\x0eAbortKeepAlive\x12,.nidigitalpattern_grpc.AbortKeepAliveRequest\x1a-.nidigitalpattern_grpc.AbortKeepAliveResponse\x12\xb5\x01\n&ConfigurePatternLabelHistoryRAMTrigger\x12D.nidigitalpattern_grpc.ConfigurePatternLabelHistoryRAMTriggerRequest\x1aE.nidigitalpattern_grpc.ConfigurePatternLabelHistoryRAMTriggerResponse\x12\xb2\x01\n%ConfigureCycleNumberHistoryRAMTrigger\x12C.nidigitalpattern_grpc.ConfigureCycleNumberHistoryRAMTriggerRequest\x1aD.nidigitalpattern_grpc.ConfigureCycleNumberHistoryRAMTriggerResponse\x12\xb5\x01\n&ConfigureFirstFailureHistoryRAMTrigger\x12D.nidigitalpattern_grpc.ConfigureFirstFailureHistoryRAMTriggerRequest\x1aE.nidigitalpattern_grpc.ConfigureFirstFailureHistoryRAMTriggerResponse\x12\xa9\x01\n"ConfigureHistoryRAMCyclesToAcquire\x12@.nidigitalpattern_grpc.ConfigureHistoryRAMCyclesToAcquireRequest\x1aA.nidigitalpattern_grpc.ConfigureHistoryRAMCyclesToAcquireResponse\x12\x8b\x01\n\x18GetHistoryRAMSampleCount\x126.nidigitalpattern_grpc.GetHistoryRAMSampleCountRequest\x1a7.nidigitalpattern_grpc.GetHistoryRAMSampleCountResponse\x12\xa0\x01\n\x1fFetchHistoryRAMCycleInformation\x12=.nidigitalpattern_grpc.FetchHistoryRAMCycleInformationRequest\x1a>.nidigitalpattern_grpc.FetchHistoryRAMCycleInformationResponse\x12\x94\x01\n\x1bFetchHistoryRAMCyclePinData\x129.nidigitalpattern_grpc.FetchHistoryRAMCyclePinDataRequest\x1a:.nidigitalpattern_grpc.FetchHistoryRAMCyclePinDataResponse\x12\x9d\x01\n\x1eFetchHistoryRAMScanCycleNumber\x12<.nidigitalpattern_grpc.FetchHistoryRAMScanCycleNumberRequest\x1a=.nidigitalpattern_grpc.FetchHistoryRAMScanCycleNumberResponse\x12\x97\x01\n\x1cCreateSourceWaveformParallel\x12:.nidigitalpattern_grpc.CreateSourceWaveformParallelRequest\x1a;.nidigitalpattern_grpc.CreateSourceWaveformParallelResponse\x12\x91\x01\n\x1aCreateSourceWaveformSerial\x128.nidigitalpattern_grpc.CreateSourceWaveformSerialRequest\x1a9.nidigitalpattern_grpc.CreateSourceWaveformSerialResponse\x12\xa3\x01\n CreateSourceWaveformFromFileTDMS\x12>.nidigitalpattern_grpc.CreateSourceWaveformFromFileTDMSRequest\x1a?.nidigitalpattern_grpc.CreateSourceWaveformFromFileTDMSResponse\x12\xa0\x01\n\x1fWriteSourceWaveformBroadcastU32\x12=.nidigitalpattern_grpc.WriteSourceWaveformBroadcastU32Request\x1a>.nidigitalpattern_grpc.WriteSourceWaveformBroadcastU32Response\x12\xa3\x01\n WriteSourceWaveformSiteUniqueU32\x12>.nidigitalpattern_grpc.WriteSourceWaveformSiteUniqueU32Request\x1a?.nidigitalpattern_grpc.WriteSourceWaveformSiteUniqueU32Response\x12\xac\x01\n#WriteSourceWaveformDataFromFileTDMS\x12A.nidigitalpattern_grpc.WriteSourceWaveformDataFromFileTDMSRequest\x1aB.nidigitalpattern_grpc.WriteSourceWaveformDataFromFileTDMSResponse\x12\x9a\x01\n\x1dCreateCaptureWaveformParallel\x12;.nidigitalpattern_grpc.CreateCaptureWaveformParallelRequest\x1a<.nidigitalpattern_grpc.CreateCaptureWaveformParallelResponse\x12\x94\x01\n\x1bCreateCaptureWaveformSerial\x129.nidigitalpattern_grpc.CreateCaptureWaveformSerialRequest\x1a:.nidigitalpattern_grpc.CreateCaptureWaveformSerialResponse\x12\xbb\x01\n(CreateCaptureWaveformFromFileDigicapture\x12F.nidigitalpattern_grpc.CreateCaptureWaveformFromFileDigicaptureRequest\x1aG.nidigitalpattern_grpc.CreateCaptureWaveformFromFileDigicaptureResponse\x12\x88\x01\n\x17FetchCaptureWaveformU32\x125.nidigitalpattern_grpc.FetchCaptureWaveformU32Request\x1a6.nidigitalpattern_grpc.FetchCaptureWaveformU32Response\x12g\n\x0cExportSignal\x12*.nidigitalpattern_grpc.ExportSignalRequest\x1a+.nidigitalpattern_grpc.ExportSignalResponse\x12\xa3\x01\n ConfigureDigitalEdgeStartTrigger\x12>.nidigitalpattern_grpc.ConfigureDigitalEdgeStartTriggerRequest\x1a?.nidigitalpattern_grpc.ConfigureDigitalEdgeStartTriggerResponse\x12\xa6\x01\n!ConfigureSoftwareEdgeStartTrigger\x12?.nidigitalpattern_grpc.ConfigureSoftwareEdgeStartTriggerRequest\x1a@.nidigitalpattern_grpc.ConfigureSoftwareEdgeStartTriggerResponse\x12|\n\x13DisableStartTrigger\x121.nidigitalpattern_grpc.DisableStartTriggerRequest\x1a2.nidigitalpattern_grpc.DisableStartTriggerResponse\x12\xc1\x01\n*ConfigureDigitalEdgeConditionalJumpTrigger\x12H.nidigitalpattern_grpc.ConfigureDigitalEdgeConditionalJumpTriggerRequest\x1aI.nidigitalpattern_grpc.ConfigureDigitalEdgeConditionalJumpTriggerResponse\x12\xc4\x01\n+ConfigureSoftwareEdgeConditionalJumpTrigger\x12I.nidigitalpattern_grpc.ConfigureSoftwareEdgeConditionalJumpTriggerRequest\x1aJ.nidigitalpattern_grpc.ConfigureSoftwareEdgeConditionalJumpTriggerResponse\x12\x9a\x01\n\x1dDisableConditionalJumpTrigger\x12;.nidigitalpattern_grpc.DisableConditionalJumpTriggerRequest\x1a<.nidigitalpattern_grpc.DisableConditionalJumpTriggerResponse\x12\x88\x01\n\x17SendSoftwareEdgeTrigger\x125.nidigitalpattern_grpc.SendSoftwareEdgeTriggerRequest\x1a6.nidigitalpattern_grpc.SendSoftwareEdgeTriggerResponse\x12y\n\x12WriteSequencerFlag\x120.nidigitalpattern_grpc.WriteSequencerFlagRequest\x1a1.nidigitalpattern_grpc.WriteSequencerFlagResponse\x12\x9d\x01\n\x1eWriteSequencerFlagSynchronized\x12<.nidigitalpattern_grpc.WriteSequencerFlagSynchronizedRequest\x1a=.nidigitalpattern_grpc.WriteSequencerFlagSynchronizedResponse\x12v\n\x11ReadSequencerFlag\x12/.nidigitalpattern_grpc.ReadSequencerFlagRequest\x1a0.nidigitalpattern_grpc.ReadSequencerFlagResponse\x12\x85\x01\n\x16WriteSequencerRegister\x124.nidigitalpattern_grpc.WriteSequencerRegisterRequest\x1a5.nidigitalpattern_grpc.WriteSequencerRegisterResponse\x12\x82\x01\n\x15ReadSequencerRegister\x123.nidigitalpattern_grpc.ReadSequencerRegisterRequest\x1a4.nidigitalpattern_grpc.ReadSequencerRegisterResponse\x12\x91\x01\n\x1aEnableMatchFailCombination\x128.nidigitalpattern_grpc.EnableMatchFailCombinationRequest\x1a9.nidigitalpattern_grpc.EnableMatchFailCombinationResponse\x12p\n\x0fGetSitePassFail\x12-.nidigitalpattern_grpc.GetSitePassFailRequest\x1a..nidigitalpattern_grpc.GetSitePassFailResponse\x12g\n\x0cGetFailCount\x12*.nidigitalpattern_grpc.GetFailCountRequest\x1a+.nidigitalpattern_grpc.GetFailCountResponse\x12\x94\x01\n\x1bGetPinResultsPinInformation\x129.nidigitalpattern_grpc.GetPinResultsPinInformationRequest\x1a:.nidigitalpattern_grpc.GetPinResultsPinInformationResponse\x12\x8e\x01\n\x19GetSiteResultsSiteNumbers\x127.nidigitalpattern_grpc.GetSiteResultsSiteNumbersRequest\x1a8.nidigitalpattern_grpc.GetSiteResultsSiteNumbersResponse\x12\xbb\x01\n(FrequencyCounterConfigureMeasurementTime\x12F.nidigitalpattern_grpc.FrequencyCounterConfigureMeasurementTimeRequest\x1aG.nidigitalpattern_grpc.FrequencyCounterConfigureMeasurementTimeResponse\x12\xbb\x01\n(FrequencyCounterConfigureMeasurementMode\x12F.nidigitalpattern_grpc.FrequencyCounterConfigureMeasurementModeRequest\x1aG.nidigitalpattern_grpc.FrequencyCounterConfigureMeasurementModeResponse\x12\xa3\x01\n FrequencyCounterMeasureFrequency\x12>.nidigitalpattern_grpc.FrequencyCounterMeasureFrequencyRequest\x1a?.nidigitalpattern_grpc.FrequencyCounterMeasureFrequencyResponse\x12\x8b\x01\n\x18GetChannelNameFromString\x126.nidigitalpattern_grpc.GetChannelNameFromStringRequest\x1a7.nidigitalpattern_grpc.GetChannelNameFromStringResponseBG\n\x15com.ni.grpc.nidigitalB\tNiDigitalP\x01\xaa\x02 NationalInstruments.Grpc.Digitalb\x06proto3')`

<!--NI_PYTHON_API repo=nimi-python path=generated/nidigital/nidigital/nidigitalpattern_pb2_grpc.py -->
## PYTHON MODULE: generated/nidigital/nidigital/nidigitalpattern_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

### `class NiDigitalStub(object)`

Missing associated documentation comment in .proto file.

#### `def __init__(self, channel)`

Constructor.

        Args:
            channel: A grpc.Channel.
        

### `class NiDigitalServicer(object)`

Missing associated documentation comment in .proto file.

#### `def Init(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def InitWithOptions(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Close(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Reset(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ResetDevice(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SelfTest(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetError(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ClearError(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ErrorMessage(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SelfCalibrate(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViInt64(self, request, context)`

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

#### `def SetAttributeViInt64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViReal64(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViString(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViSession(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViBoolean(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ResetAttribute(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def LoadPinMap(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def EnableSites(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DisableSites(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def IsSiteEnabled(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreatePinMap(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreatePinGroup(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateChannelMap(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def MapPinToChannel(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def EndChannelMap(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetPinName(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetChannelName(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SelectFunction(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadStatic(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteStatic(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ClockGeneratorGenerateClock(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ClockGeneratorInitiate(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ClockGeneratorAbort(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def LoadSpecifications(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def UnloadSpecifications(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def LoadLevels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def LoadTiming(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ApplyLevelsAndTiming(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureVoltageLevels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureActiveLoadLevels(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureTerminationMode(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateTimeSet(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureTimeSetPeriod(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureTimeSetDriveEdges(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureTimeSetCompareEdgesStrobe(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureTimeSetDriveFormat(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DeleteAllTimeSets(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureTimeSetEdgeMultiplier(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureTimeSetDriveEdges2x(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureTimeSetCompareEdgesStrobe2x(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureTimeSetEdge(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetTimeSetPeriod(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetTimeSetEdge(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetTimeSetEdgeMultiplier(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetTimeSetDriveFormat(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetTimeSetName(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def TDR(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ApplyTDROffsets(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def PPMUConfigureOutputFunction(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def PPMUConfigureApertureTime(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def PPMUConfigureVoltageLevel(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def PPMUConfigureCurrentLimit(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def PPMUConfigureCurrentLimitRange(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def PPMUConfigureCurrentLevel(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def PPMUConfigureCurrentLevelRange(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def PPMUConfigureVoltageLimits(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def PPMUSource(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def PPMUMeasure(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def LoadPattern(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def UnloadAllPatterns(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureStartLabel(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigurePatternBurstSites(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetPatternPinIndexes(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetPatternPinList(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetPatternName(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BurstPattern(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def BurstPatternSynchronized(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Commit(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Initiate(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def IsDone(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WaitUntilDone(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Abort(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def AbortKeepAlive(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigurePatternLabelHistoryRAMTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureCycleNumberHistoryRAMTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureFirstFailureHistoryRAMTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureHistoryRAMCyclesToAcquire(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetHistoryRAMSampleCount(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def FetchHistoryRAMCycleInformation(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def FetchHistoryRAMCyclePinData(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def FetchHistoryRAMScanCycleNumber(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateSourceWaveformParallel(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateSourceWaveformSerial(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateSourceWaveformFromFileTDMS(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteSourceWaveformBroadcastU32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteSourceWaveformSiteUniqueU32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteSourceWaveformDataFromFileTDMS(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateCaptureWaveformParallel(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateCaptureWaveformSerial(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CreateCaptureWaveformFromFileDigicapture(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def FetchCaptureWaveformU32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ExportSignal(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureDigitalEdgeStartTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureSoftwareEdgeStartTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DisableStartTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureDigitalEdgeConditionalJumpTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureSoftwareEdgeConditionalJumpTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def DisableConditionalJumpTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SendSoftwareEdgeTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteSequencerFlag(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteSequencerFlagSynchronized(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadSequencerFlag(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def WriteSequencerRegister(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadSequencerRegister(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def EnableMatchFailCombination(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetSitePassFail(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetFailCount(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetPinResultsPinInformation(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetSiteResultsSiteNumbers(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def FrequencyCounterConfigureMeasurementTime(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def FrequencyCounterConfigureMeasurementMode(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def FrequencyCounterMeasureFrequency(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetChannelNameFromString(self, request, context)`

Missing associated documentation comment in .proto file.

### `def add_NiDigitalServicer_to_server(servicer, server)`

### `class NiDigital(object)`

Missing associated documentation comment in .proto file.

#### `def Init(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def InitWithOptions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Close(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Reset(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ResetDevice(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SelfTest(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetError(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ClearError(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ErrorMessage(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SelfCalibrate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViInt64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViReal64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViSession(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViBoolean(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViInt64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViReal64(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViSession(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViBoolean(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ResetAttribute(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def LoadPinMap(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def EnableSites(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DisableSites(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def IsSiteEnabled(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreatePinMap(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreatePinGroup(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateChannelMap(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def MapPinToChannel(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def EndChannelMap(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetPinName(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetChannelName(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SelectFunction(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadStatic(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteStatic(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ClockGeneratorGenerateClock(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ClockGeneratorInitiate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ClockGeneratorAbort(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def LoadSpecifications(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def UnloadSpecifications(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def LoadLevels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def LoadTiming(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ApplyLevelsAndTiming(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureVoltageLevels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureActiveLoadLevels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureTerminationMode(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateTimeSet(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureTimeSetPeriod(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureTimeSetDriveEdges(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureTimeSetCompareEdgesStrobe(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureTimeSetDriveFormat(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DeleteAllTimeSets(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureTimeSetEdgeMultiplier(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureTimeSetDriveEdges2x(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureTimeSetCompareEdgesStrobe2x(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureTimeSetEdge(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTimeSetPeriod(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTimeSetEdge(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTimeSetEdgeMultiplier(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTimeSetDriveFormat(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetTimeSetName(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def TDR(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ApplyTDROffsets(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def PPMUConfigureOutputFunction(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def PPMUConfigureApertureTime(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def PPMUConfigureVoltageLevel(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def PPMUConfigureCurrentLimit(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def PPMUConfigureCurrentLimitRange(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def PPMUConfigureCurrentLevel(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def PPMUConfigureCurrentLevelRange(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def PPMUConfigureVoltageLimits(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def PPMUSource(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def PPMUMeasure(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def LoadPattern(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def UnloadAllPatterns(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureStartLabel(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigurePatternBurstSites(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetPatternPinIndexes(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetPatternPinList(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetPatternName(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BurstPattern(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def BurstPatternSynchronized(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Commit(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Initiate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def IsDone(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WaitUntilDone(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Abort(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def AbortKeepAlive(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigurePatternLabelHistoryRAMTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureCycleNumberHistoryRAMTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureFirstFailureHistoryRAMTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureHistoryRAMCyclesToAcquire(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetHistoryRAMSampleCount(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def FetchHistoryRAMCycleInformation(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def FetchHistoryRAMCyclePinData(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def FetchHistoryRAMScanCycleNumber(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateSourceWaveformParallel(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateSourceWaveformSerial(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateSourceWaveformFromFileTDMS(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteSourceWaveformBroadcastU32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteSourceWaveformSiteUniqueU32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteSourceWaveformDataFromFileTDMS(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateCaptureWaveformParallel(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateCaptureWaveformSerial(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CreateCaptureWaveformFromFileDigicapture(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def FetchCaptureWaveformU32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ExportSignal(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureDigitalEdgeStartTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureSoftwareEdgeStartTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DisableStartTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureDigitalEdgeConditionalJumpTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureSoftwareEdgeConditionalJumpTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def DisableConditionalJumpTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SendSoftwareEdgeTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteSequencerFlag(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteSequencerFlagSynchronized(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadSequencerFlag(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def WriteSequencerRegister(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadSequencerRegister(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def EnableMatchFailCombination(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetSitePassFail(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetFailCount(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetPinResultsPinInformation(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetSiteResultsSiteNumbers(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def FrequencyCounterConfigureMeasurementTime(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def FrequencyCounterConfigureMeasurementMode(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def FrequencyCounterMeasureFrequency(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetChannelNameFromString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nidigital/nidigital/session.py -->
## PYTHON MODULE: generated/nidigital/nidigital/session.py

### `class _Burst(object)`

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

Base class for all NI-Digital Pattern Driver sessions.

#### `def __init__(self, repeated_capability_list, all_channels_in_session, interpreter, freeze_it=False)`

#### `def __repr__(self)`

#### `def __setattr__(self, key, value)`

#### `def apply_levels_and_timing(self, levels_sheet, timing_sheet, initial_state_high_pins=None, initial_state_low_pins=None, initial_state_tristate_pins=None)`

apply_levels_and_timing

        Applies digital levels and timing values defined in previously loaded levels and timing sheets. When applying a levels sheet, only the levels specified in the sheet are affected. Any levels not specified in the sheet remain unchanged. When applying a timing sheet, all existing time sets are deleted before the new time sets are loaded.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ].apply_levels_and_timing`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.apply_levels_and_timing`

        Args:
            levels_sheet (str): Name of the levels sheet to apply. Use the name of the sheet or pass the absolute file path you use in the load_specifications_levels_and_timing method. The name of the levels sheet is the file name without the directory and file extension.

            timing_sheet (str): Name of the timing sheet to apply. Use the name of the sheet or pass the absolute file path that you use in the load_specifications_levels_and_timing method. The name of the timing sheet is the file name without the directory and file extension.

            initial_state_high_pins (basic sequence types or str): Comma-delimited list of pins, pin groups, or channels to initialize to a high state.

            initial_state_low_pins (basic sequence types or str): Comma-delimited list of pins, pin groups, or channels to initialize to a low state.

            initial_state_tristate_pins (basic sequence types or str): Comma-delimited list of pins, pin groups, or channels to initialize to a non-drive state (X)

        

#### `def apply_tdr_offsets(self, offsets)`

apply_tdr_offsets

        Applies the correction for propagation delay offsets to a digital pattern instrument. Use this method to apply TDR offsets that are stored from a past measurement or are measured by means other than the tdr method. Also use this method to apply correction for offsets if the **applyOffsets** input of the tdr method was set to False at the time of measurement.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].apply_tdr_offsets`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.apply_tdr_offsets`

        Args:
            offsets (basic sequence of hightime.timedelta, datetime.timedelta, or float in seconds): TDR offsets to apply, in seconds. Specify an offset for each pin or channel in the repeated capabilities. If the repeated capabilities contain pin names, you must specify offsets for each site in the channel map per pin.

        

#### `def _burst_pattern(self, start_label, select_digital_function=True, wait_until_done=True, timeout=hightime.timedelta(seconds=10.0))`

_burst_pattern

        Uses the **startLabel** you specify to burst the pattern on the sites you specify and provides the option to wait for the burst to complete. Digital pins retain their state at the end of a pattern burst until the first vector of a subsequent pattern burst, a call to write_static, or a call to apply_levels_and_timing.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ]._burst_pattern`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._burst_pattern`

        Args:
            start_label (str): Pattern name or exported pattern label from which to start bursting the pattern.

            select_digital_function (bool): A Boolean that specifies whether to select the digital method for the pins in the pattern prior to bursting.

            wait_until_done (bool): A Boolean that indicates whether to wait until the bursting is complete.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): Maximum time (in seconds) allowed for this method to complete. If this method does not complete within this time interval, this method returns an error.

        

#### `def clock_generator_abort(self)`

clock_generator_abort

        Stops clock generation on the specified channel(s) or pin(s) and pin group(s).

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].clock_generator_abort`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.clock_generator_abort`
        

#### `def clock_generator_generate_clock(self, frequency, select_digital_function=True)`

clock_generator_generate_clock

        Configures clock generator frequency and initiates clock generation on the specified channel(s) or pin(s) and pin group(s).

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].clock_generator_generate_clock`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.clock_generator_generate_clock`

        Args:
            frequency (float): The frequency of the clock generation, in Hz.

            select_digital_function (bool): A Boolean that specifies whether to select the digital method for the pins specified prior to starting clock generation.

        

#### `def configure_active_load_levels(self, iol, ioh, vcom)`

configure_active_load_levels

        Configures I\ :sub:`OL`, I\ :sub:`OH`, and V\ :sub:`COM` levels for the active load on the pins you specify. The DUT sources or sinks current based on the level values. To enable active load, set the termination mode to TerminationMode.ACTIVE_LOAD. To disable active load, set the termination mode of the instrument to TerminationMode.HIGH_Z or TerminationMode.VTERM.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_active_load_levels`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.configure_active_load_levels`

        Args:
            iol (float): Maximum current that the DUT sinks while outputting a voltage below V\ :sub:`COM`.

            ioh (float): Maximum current that the DUT sources while outputting a voltage above V\ :sub:`COM`.

            vcom (float): Commutating voltage level at which the active load circuit switches between sourcing current and sinking current.

        

#### `def configure_pattern_burst_sites(self)`

configure_pattern_burst_sites

        Configures which sites burst the pattern on the next call to the initiate method. The pattern burst sites can also be modified through the repeated capabilities for the burst_pattern method. If a site has been disabled through the disable_sites method, the site does not burst a pattern even if included in the pattern burst sites.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ].configure_pattern_burst_sites`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.configure_pattern_burst_sites`
        

#### `def configure_time_set_compare_edges_strobe(self, time_set_name, strobe_edge)`

configure_time_set_compare_edges_strobe

        Configures the strobe edge time for the specified pins. Use this method to modify time set values after applying a timing sheet with the apply_levels_and_timing method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to apply_levels_and_timing; it only affects the values of the current timing context.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].configure_time_set_compare_edges_strobe`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.configure_time_set_compare_edges_strobe`

        Args:
            time_set_name (str): The specified time set name.

            strobe_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Time when the comparison happens within a vector period.

        

#### `def configure_time_set_compare_edges_strobe2x(self, time_set_name, strobe_edge, strobe2_edge)`

configure_time_set_compare_edges_strobe2x

        Configures the compare strobes for the specified pins in the time set, including the 2x strobe. Use this method to modify time set values after applying a timing sheet with the apply_levels_and_timing method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to apply_levels_and_timing; it only affects the values of the current timing context.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].configure_time_set_compare_edges_strobe2x`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.configure_time_set_compare_edges_strobe2x`

        Args:
            time_set_name (str): The specified time set name.

            strobe_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Time when the comparison happens within a vector period.

            strobe2_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Time when the comparison happens for the second DUT cycle within a vector period.

        

#### `def configure_time_set_drive_edges(self, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge)`

configure_time_set_drive_edges

        Configures the drive format and drive edge placement for the specified pins. Use this method to modify time set values after applying a timing sheet with the apply_levels_and_timing method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to apply_levels_and_timing; it only affects the values of the current timing context.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].configure_time_set_drive_edges`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.configure_time_set_drive_edges`

        Args:
            time_set_name (str): The specified time set name.

            format (enums.DriveFormat): Drive format of the time set.

                -   DriveFormat.NR: Non-return.
                -   DriveFormat.RL: Return to low.
                -   DriveFormat.RH: Return to high.
                -   DriveFormat.SBC: Surround by complement.

            drive_on_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Delay, in seconds, from the beginning of the vector period for turning on the pin driver.This option applies only when the prior vector left the pin in a non-drive pin state (L, H, X, V, M, E). For the SBC format, this option specifies the delay from the beginning of the vector period at which the complement of the pattern value is driven.

            drive_data_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Delay, in seconds, from the beginning of the vector period until the pattern data is driven to the pattern value.The ending state from the previous vector persists until this point.

            drive_return_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Delay, in seconds, from the beginning of the vector period until the pin changes from the pattern data to the return value, as specified in the format.

            drive_off_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Delay, in seconds, from the beginning of the vector period to turn off the pin driver when the next vector period uses a non-drive symbol (L, H, X, V, M, E).

        

#### `def configure_time_set_drive_edges2x(self, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge, drive_data2_edge, drive_return2_edge)`

configure_time_set_drive_edges2x

        Configures the drive edges of the pins in the time set, including 2x edges. Use this method to modify time set values after applying a timing sheet with the apply_levels_and_timing method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to apply_levels_and_timing; it only affects the values of the current timing context.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].configure_time_set_drive_edges2x`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.configure_time_set_drive_edges2x`

        Args:
            time_set_name (str): The specified time set name.

            format (enums.DriveFormat): Drive format of the time set.

                -   DriveFormat.NR: Non-return.
                -   DriveFormat.RL: Return to low.
                -   DriveFormat.RH: Return to high.
                -   DriveFormat.SBC: Surround by complement.

            drive_on_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Delay, in seconds, from the beginning of the vector period for turning on the pin driver.This option applies only when the prior vector left the pin in a non-drive pin state (L, H, X, V, M, E). For the SBC format, this option specifies the delay from the beginning of the vector period at which the complement of the pattern value is driven.

            drive_data_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Delay, in seconds, from the beginning of the vector period until the pattern data is driven to the pattern value.The ending state from the previous vector persists until this point.

            drive_return_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Delay, in seconds, from the beginning of the vector period until the pin changes from the pattern data to the return value, as specified in the format.

            drive_off_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Delay, in seconds, from the beginning of the vector period to turn off the pin driver when the next vector period uses a non-drive symbol (L, H, X, V, M, E).

            drive_data2_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Delay, in seconds, from the beginning of the vector period until the pattern data in the second DUT cycle is driven to the pattern value.

            drive_return2_edge (hightime.timedelta, datetime.timedelta, or float in seconds): Delay, in seconds, from the beginning of the vector period until the pin changes from the pattern data in the second DUT cycle to the return value, as specified in the format.

        

#### `def configure_time_set_drive_format(self, time_set_name, drive_format)`

configure_time_set_drive_format

        Configures the drive format for the pins specified in the **pinList**. Use this method to modify time set values after applying a timing sheet with the apply_levels_and_timing method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to apply_levels_and_timing; it only affects the values of the current timing context.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].configure_time_set_drive_format`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.configure_time_set_drive_format`

        Args:
            time_set_name (str): The specified time set name.

            drive_format (enums.DriveFormat): Drive format of the time set.

                -   DriveFormat.NR: Non-return.
                -   DriveFormat.RL: Return to low.
                -   DriveFormat.RH: Return to high.
                -   DriveFormat.SBC: Surround by complement.

        

#### `def configure_time_set_edge(self, time_set_name, edge, time)`

configure_time_set_edge

        Configures the edge placement for the pins specified in the pin list. Use this method to modify time set values after applying a timing sheet with the apply_levels_and_timing method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to apply_levels_and_timing; it only affects the values of the current timing context.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].configure_time_set_edge`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.configure_time_set_edge`

        Args:
            time_set_name (str): The specified time set name.

            edge (enums.TimeSetEdgeType): Name of the edge.

                -   TimeSetEdgeType.DRIVE_ON
                -   TimeSetEdgeType.DRIVE_DATA
                -   TimeSetEdgeType.DRIVE_RETURN
                -   TimeSetEdgeType.DRIVE_OFF
                -   TimeSetEdgeType.COMPARE_STROBE
                -   TimeSetEdgeType.DRIVE_DATA2
                -   TimeSetEdgeType.DRIVE_RETURN2
                -   TimeSetEdgeType.COMPARE_STROBE2

            time (hightime.timedelta, datetime.timedelta, or float in seconds): The time from the beginning of the vector period in which to place the edge.

        

#### `def configure_time_set_edge_multiplier(self, time_set_name, edge_multiplier)`

configure_time_set_edge_multiplier

        Configures the edge multiplier of the pins in the time set. Use this method to modify time set values after applying a timing sheet with the apply_levels_and_timing method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to apply_levels_and_timing; it only affects the values of the current timing context.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].configure_time_set_edge_multiplier`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.configure_time_set_edge_multiplier`

        Args:
            time_set_name (str): The specified time set name.

            edge_multiplier (int): The specified edge multiplier for the pins in the pin list.

        

#### `def configure_voltage_levels(self, vil, vih, vol, voh, vterm)`

configure_voltage_levels

        Configures voltage levels for the pins you specify.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_voltage_levels`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.configure_voltage_levels`

        Args:
            vil (float): Voltage that the instrument will apply to the input of the DUT when the pin driver drives a logic low (0).

            vih (float): Voltage that the instrument will apply to the input of the DUT when the test instrument drives a logic high (1).

            vol (float): Output voltage below which the comparator on the pin driver interprets a logic low (L).

            voh (float): Output voltage above which the comparator on the pin driver interprets a logic high (H).

            vterm (float): Termination voltage the instrument applies during non-drive cycles when the termination mode is set to V\ :sub:`term`. The instrument applies the termination voltage through a 50 ohm parallel termination resistance.

        

#### `def create_capture_waveform_parallel(self, waveform_name)`

create_capture_waveform_parallel

        Sets the capture waveform settings for parallel acquisition. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].create_capture_waveform_parallel`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.create_capture_waveform_parallel`

        Args:
            waveform_name (str): Waveform name you want to use. Use the waveform_name with the capture_start opcode in your pattern.

        

#### `def create_capture_waveform_serial(self, waveform_name, sample_width, bit_order)`

create_capture_waveform_serial

        Sets the capture waveform settings for serial acquisition. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].create_capture_waveform_serial`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.create_capture_waveform_serial`

        Args:
            waveform_name (str): Waveform name you want to use. Use the waveform_name with the capture_start opcode in your pattern.

            sample_width (int): Width in bits of each serial sample. Valid values are between 1 and 32.

            bit_order (enums.BitOrder): Order in which to shift the bits.

                -   BitOrder.MSB: Specifies the bit order by most significant bit first.
                -   BitOrder.LSB: Specifies the bit order by least significant bit first.

        

#### `def create_source_waveform_parallel(self, waveform_name, data_mapping)`

create_source_waveform_parallel

        Sets the source waveform settings required for parallel sourcing. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].create_source_waveform_parallel`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.create_source_waveform_parallel`

        Args:
            waveform_name (str): The name to assign to the waveform. Use the waveform_name  with source_start opcode in your pattern.

            data_mapping (enums.SourceDataMapping): Parameter that specifies how to map data on multiple sites.

                -   SourceDataMapping.BROADCAST: Broadcasts the waveform you specify to all sites.
                -   SourceDataMapping.SITE_UNIQUE: Sources unique waveform data to each site.

        

#### `def create_source_waveform_serial(self, waveform_name, data_mapping, sample_width, bit_order)`

create_source_waveform_serial

        Sets the source waveform settings required for serial sourcing. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].create_source_waveform_serial`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.create_source_waveform_serial`

        Args:
            waveform_name (str): The name to assign to the waveform. Use the waveform_name  with source_start opcode in your pattern.

            data_mapping (enums.SourceDataMapping): Parameter that specifies how to map data on multiple sites.

                -   SourceDataMapping.BROADCAST: Broadcasts the waveform you specify to all sites.
                -   SourceDataMapping.SITE_UNIQUE: Sources unique waveform data to each site.

            sample_width (int): Width in bits of each serial sample. Valid values are between 1 and 32.

            bit_order (enums.BitOrder): Order in which to shift the bits.

                -   BitOrder.MSB: Specifies the bit order by most significant bit first.
                -   BitOrder.LSB: Specifies the bit order by least significant bit first.

        

#### `def disable_sites(self)`

disable_sites

        Disables specified sites. Disabled sites are not included in pattern bursts initiated by the initiate method or the burst_pattern method, even if the site is specified in the list of pattern burst sites in configure_pattern_burst_sites method or in the repeated capabilities for the burst_pattern method. Additionally, if you specify a list of pin or pin group names in repeated capabilities in any NI-Digital method, digital pattern instrument channels mapped to disabled sites are not affected by the method. The methods that return per-pin data, such as the ppmu_measure method, do not return data for channels mapped to disabled sites. The digital pattern instrument channels mapped to the sites specified are left in their current state. NI TestStand Semiconductor Module requires all sites to always be enabled, and manages the set of active sites without disabling the sites in the digital instrument session. Do not use this method with the Semiconductor Module.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ].disable_sites`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.disable_sites`
        

#### `def enable_sites(self)`

enable_sites

        Enables the sites you specify. All sites are enabled by default.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ].enable_sites`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.enable_sites`
        

#### `def burst_pattern(self, start_label, select_digital_function=True, wait_until_done=True, timeout=hightime.timedelta(seconds=10.0))`

burst_pattern

        Uses the start_label you specify to burst the pattern on the sites you specify. If you
        specify wait_until_done as True, waits for the burst to complete, and returns comparison results for each site.

        Digital pins retain their state at the end of a pattern burst until the first vector of the pattern burst, a call to
        write_static, or a call to apply_levels_and_timing.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ].burst_pattern`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.burst_pattern`

        Args:
            start_label (str): Pattern name or exported pattern label from which to start bursting the pattern.

            select_digital_function (bool): A Boolean that specifies whether to select the digital method for the pins in the pattern prior to bursting.

            wait_until_done (bool): A Boolean that indicates whether to wait until the bursting is complete.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): Maximum time (in seconds) allowed for this method to complete. If this method does not complete within this time interval, this method returns an error.


        Returns:
            pass_fail ({ int: bool, int: bool, ... }): Dictionary where each key is a site number and value is pass/fail,
                if wait_until_done is specified as True. Else, None.

        

#### `def fetch_capture_waveform(self, waveform_name, samples_to_read, timeout=hightime.timedelta(seconds=10.0))`

fetch_capture_waveform

        Returns dictionary where each key is a site number and value is a collection of digital states representing capture waveform data

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ].fetch_capture_waveform`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.fetch_capture_waveform`

        Args:
            waveform_name (str): Waveform name you create with the create capture waveform method. Use the waveform_name parameter with capture_start opcode in your pattern.

            samples_to_read (int): Number of samples to fetch.

            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): Maximum time (in seconds) allowed for this method to complete. If this method does not complete within this time interval, this method returns an error.


        Returns:
            waveform ({ int: memoryview of array.array of unsigned int, int: memoryview of array.array of unsigned int, ... }): Dictionary where each key is a site number and value is a collection of digital states representing capture waveform data

        

#### `def fetch_history_ram_cycle_information(self, position, samples_to_read)`

fetch_history_ram_cycle_information

        Returns the pattern information acquired for the specified cycles.

        If the pattern is using the edge multiplier feature, cycle numbers represent tester cycles, each of which may
        consist of multiple DUT cycles. When using pins with mixed edge multipliers, pins may return
        PinState.PIN_STATE_NOT_ACQUIRED for DUT cycles where those pins do not have edges defined.

        Site number on which to retrieve pattern information must be specified via sites repeated capability.
        The method returns an error if more than one site is specified.

        Pins for which to retrieve pattern information must be specified via pins repeated capability.
        If pins are not specified, pin list from the pattern containing the start label is used. Call
        get_pattern_pin_names with the start label to retrieve the pins associated with the pattern burst:

        .. code:: python

         session.sites[0].pins['PinA', 'PinB'].fetch_history_ram_cycle_information(0, -1)

        Note:
        Before bursting a pattern, you must configure the History RAM trigger and specify which cycles to acquire.

        history_ram_trigger_type should be used to specify the trigger condition on which History RAM
        starts acquiring pattern information.

        If History RAM trigger is configured as HistoryRAMTriggerType.CYCLE_NUMBER,
        cycle_number_history_ram_trigger_cycle_number should be used to specify the cycle number on which
        History RAM starts acquiring pattern information.

        If History RAM trigger is configured as HistoryRAMTriggerType.PATTERN_LABEL,
        pattern_label_history_ram_trigger_label should be used to specify the pattern label from which to
        start acquiring pattern information.
        pattern_label_history_ram_trigger_vector_offset should be used to specify the number of vectors
        following the specified pattern label from which to start acquiring pattern information.
        pattern_label_history_ram_trigger_cycle_offset should be used to specify the number of cycles
        following the specified pattern label and vector offset from which to start acquiring pattern information.

        For all History RAM trigger conditions, history_ram_pretrigger_samples should be used to specify
        the number of samples to acquire before the trigger conditions are met. If you configure History RAM to only
        acquire failed cycles, you must set history_ram_pretrigger_samples to 0.

        history_ram_cycles_to_acquire should be used to specify which cycles History RAM acquires after
        the trigger conditions are met.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].fetch_history_ram_cycle_information`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.fetch_history_ram_cycle_information`

        Args:
            position (int): Sample index from which to start fetching pattern information.

            samples_to_read (int): Number of samples to fetch. A value of -1 specifies to fetch all available samples.


        Returns:
            history_ram_cycle_information (list of HistoryRAMCycleInformation): Returns a list of class instances with
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
                   will have a value of PinState.PIN_STATE_NOT_ACQUIRED.
                   Length of the outer list will be equal to the value of edge multiplier for the given vector.
                   Length of the inner list will be equal to the number of pins requested.
                -  **actual_pin_states** (list of list of enums.PinState) Pin states acquired by History RAM in the
                   order specified in the pin list. Pins without defined edges in the specified DUT cycle will have a
                   value of PinState.PIN_STATE_NOT_ACQUIRED.
                   Length of the outer list will be equal to the value of edge multiplier for the given vector.
                   Length of the inner list will be equal to the number of pins requested.
                -  **per_pin_pass_fail** (list of list of bool) Pass fail information for pins in the order specified in
                   the pin list. Pins without defined edges in the specified DUT cycle will have a value of pass (True).
                   Length of the outer list will be equal to the value of edge multiplier for the given vector.
                   Length of the inner list will be equal to the number of pins requested.

        

#### `def get_pin_results_pin_information(self)`

get_pin_results_pin_information

        Returns the pin names, site numbers, and channel names that correspond to per-pin data read from the digital pattern instrument. The method returns pin information in the same order as values read using the read_static method, ppmu_measure method, and get_fail_count method. Use this method to match values the previously listed methods return with pins, sites, and instrument channels.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].get_pin_results_pin_information`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.get_pin_results_pin_information`

        Returns:
            pin_info (list of PinInfo): List of named tuples with fields:

                - **pin_name** (str)
                - **site_number** (int)
                - **channel_name** (str)

        

#### `def get_site_pass_fail(self)`

get_site_pass_fail

        Returns dictionary where each key is a site number and value is pass/fail

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ].get_site_pass_fail`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.get_site_pass_fail`

        Returns:
            pass_fail ({ int: bool, int: bool, ... }): Dictionary where each key is a site number and value is pass/fail

        

#### `def _fetch_history_ram_cycle_information(self, sample_index)`

_fetch_history_ram_cycle_information

        Gets the per-cycle pattern information acquired for the specified cycle.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ]._fetch_history_ram_cycle_information`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._fetch_history_ram_cycle_information`

        Args:
            sample_index (int): The index of the History RAM sample to fetch. Each History RAM sample contains information about a single cycle in the pattern burst.


        Returns:
            pattern_index (int): The returned index of the pattern for the acquired cycle. Use _get_pattern_name to get the name of the pattern from its index.

            time_set_index (int): The returned time set for the acquired cycle. Use _get_time_set_name to get the name of the time set from its index.

            vector_number (int): The returned vector number within the pattern for the acquired cycle. Vector numbers start at 0 from the beginning of the pattern.

            cycle_number (int): Returns the cycle number acquired by this History RAM sample. Cycle numbers start at 0 from the beginning of the pattern burst.

            num_dut_cycles (int): The returned number of DUT cycles contained in the cycle acquired by this History RAM sample. This is only needed if the pattern uses the edge multiplier feature.

        

#### `def _fetch_history_ram_cycle_pin_data(self, pin_list, sample_index, dut_cycle_index)`

_fetch_history_ram_cycle_pin_data

        Gets the per-pin pattern data acquired for the specified cycle.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ]._fetch_history_ram_cycle_pin_data`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._fetch_history_ram_cycle_pin_data`

        Args:
            pin_list (str): The specified pins for which to retrieve History RAM data. If empty, the pin list from the pattern containing the start label is used. Call get_pattern_pin_names or GetPatternPinIndexeswith the start label to retrieve the pins associated with the pattern burst.

                Note:
                One or more of the referenced methods are not in the Python API for this driver.

            sample_index (int): The index of the History RAM sample to fetch. Each History RAM sample contains information about a single cycle in the pattern burst.

            dut_cycle_index (int): The specified index of the DUT cycle. If the pattern does not use the edge multiplier feature, pass 0 for this parameter. For History RAM samples that contain multiple DUT cycles, indicated by the **numDutCycles** value returned by _fetch_history_ram_cycle_information, call this method multiple times to retrieve pin states for each DUT cycle. The DUT cycle index should start at 0.


        Returns:
            expected_pin_states (list of enums.PinState): The returned pin state as expected by the loaded pattern in the order specified in **pinList**. Pins without defined edges in the specified DUT cycle will return PinState.NOT_A_PIN_STATE

            actual_pin_states (list of enums.PinState): The returned pin state acquired by History RAM in the order specified in **pinList**. Pins without defined edges in the specified DUT cycle will return PinState.NOT_A_PIN_STATE

            per_pin_pass_fail (list of bool): The returned pass fail information for pins in the order specified in **pinList**. Pins without defined edges in the specified DUT cycle will return pass (True).

        

#### `def _fetch_history_ram_scan_cycle_number(self, sample_index)`

_fetch_history_ram_scan_cycle_number

        Fetches the History RAM Scan Cycle Number for the sample index. If the sample is not from a scan vector, the scan cycle number will be returned as -1.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ]._fetch_history_ram_scan_cycle_number`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._fetch_history_ram_scan_cycle_number`

        Args:
            sample_index (int): The index of the History RAM sample to fetch. Each History RAM sample contains information about a single cycle in the pattern burst.


        Returns:
            scan_cycle_number (int): Returns the scan cycle number acquired by this History RAM sample. Scan cycle numbers start at 0 from the first cycle of the scan vector. Scan cycle numbers are -1 for cycles that do not have a scan opcode.

        

#### `def frequency_counter_measure_frequency(self)`

frequency_counter_measure_frequency

        Measures the frequency on the specified channel(s) over the specified measurement time. All channels in the repeated capabilities should have the same measurement time.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].frequency_counter_measure_frequency`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.frequency_counter_measure_frequency`

        Returns:
            frequencies (list of float): The returned frequency counter measurement, in Hz.This method returns -1 if the measurement is invalid for the channel.

        

#### `def _get_attribute_vi_boolean(self, attribute)`

_get_attribute_vi_boolean

        Queries the value of a ViBoolean property. Use this method to get the values of digital pattern instrument-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_boolean`

        Args:
            attribute (int): The ID of a property.


        Returns:
            value (bool): The returned current value of the property; pass the address of a ViBoolean variable.

        

#### `def _get_attribute_vi_int32(self, attribute)`

_get_attribute_vi_int32

        Queries the value of a ViInt32 property. Use this method to get the values of digital pattern instrument-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_int32`

        Args:
            attribute (int): The ID of a property.


        Returns:
            value (int): The returned current value of the property; pass the address of a ViInt32 variable.

        

#### `def _get_attribute_vi_int64(self, attribute)`

_get_attribute_vi_int64

        Queries the value of a ViInt64 property. Use this method to get the values of digital pattern instrument-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_int64`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_int64`

        Args:
            attribute (int): The ID of a property.


        Returns:
            value (int): The returned current value of the property; pass the address of a ViInt64 variable.

        

#### `def _get_attribute_vi_real64(self, attribute)`

_get_attribute_vi_real64

        This method queries the value of a ViReal64 property. Use this method to get the values of digital pattern instrument-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_real64`

        Args:
            attribute (int): The ID of a property.


        Returns:
            value (float): The returned current value of the property; pass the address of a ViReal64 variable.

        

#### `def _get_attribute_vi_string(self, attribute)`

_get_attribute_vi_string

        Queries the value of a ViString property. Use this method to get the values of digital pattern instrument-specific properties and inherent IVI properties. You must provide a ViChar array to serve as a buffer for the value. You pass the number of bytes in the buffer as the **bufferSize**. If the current value of the property, including the terminating NULL byte, is larger than the size you indicate in the **bufferSize**, the method copies (bufferSize - 1) bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the **bufferSize** you must pass to get the entire value. For example, if the value is "123456" and the **bufferSize** is 4, the method places "123" into the buffer and returns 7. If you want to call this method just to get the required buffer size, you can pass 0 for the **bufferSize** and VI_NULL for the value.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_string`

        Args:
            attribute (int): The ID of a property.


        Returns:
            value (str): The buffer in which the method returns the current value of the property; the buffer must be of type ViChar and have at least as many bytes as indicated in the **bufferSize**.

        

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

        

#### `def get_fail_count(self)`

get_fail_count

        Returns the comparison fail count for pins in the repeated capabilities.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].get_fail_count`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.get_fail_count`

        Returns:
            failure_count (list of int): Number of failures in an array. If a site is disabled or not enabled for burst, the method does not return data for that site. You can also use the get_pin_results_pin_information method to obtain a sorted list of returned sites and channels.

        

#### `def get_history_ram_sample_count(self)`

get_history_ram_sample_count

        Returns the number of samples History RAM acquired on the last pattern burst.

        Note:
        Before bursting a pattern, you must configure the History RAM trigger and specify which cycles to acquire.

        history_ram_trigger_type should be used to specify the trigger condition on which History RAM
        starts acquiring pattern information.

        If History RAM trigger is configured as HistoryRAMTriggerType.CYCLE_NUMBER,
        cycle_number_history_ram_trigger_cycle_number should be used to specify the cycle number on which
        History RAM starts acquiring pattern information.

        If History RAM trigger is configured as HistoryRAMTriggerType.PATTERN_LABEL,
        pattern_label_history_ram_trigger_label should be used to specify the pattern label from which to
        start acquiring pattern information.
        pattern_label_history_ram_trigger_vector_offset should be used to specify the number of vectors
        following the specified pattern label from which to start acquiring pattern information.
        pattern_label_history_ram_trigger_cycle_offset should be used to specify the number of cycles
        following the specified pattern label and vector offset from which to start acquiring pattern information.

        For all History RAM trigger conditions, history_ram_pretrigger_samples should be used to specify
        the number of samples to acquire before the trigger conditions are met. If you configure History RAM to only
        acquire failed cycles, you must set history_ram_pretrigger_samples to 0.

        history_ram_cycles_to_acquire should be used to specify which cycles History RAM acquires after
        the trigger conditions are met.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ].get_history_ram_sample_count`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.get_history_ram_sample_count`

        Returns:
            sample_count (int): The returned number of samples that History RAM acquired.

        

#### `def _get_pattern_name(self, pattern_index)`

_get_pattern_name

        TBD

        Args:
            pattern_index (int):


        Returns:
            name (str):

        

#### `def _get_pin_name(self, pin_index)`

_get_pin_name

        Returns the name of the pin at the index you specify. You must provide a ViChar array to serve as a buffer for the value. You pass the number of bytes in the buffer as the **nameBufferSize**. If the current value of the property, including the terminating NULL byte, is larger than the size you indicate in the buffer size, the method copies (buffer size - 1) bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the method places "123" into the buffer and returns 7. If you want to call this method just to get the required buffer size, you can pass 0 for **nameBufferSize** and VI_NULL for the name.

        Args:
            pin_index (int): Index of pin to query. Pin indexes begin at 0.


        Returns:
            name (str): Returns the pin name at the specified **pinIndex**.

        

#### `def _get_pin_results_pin_information(self)`

_get_pin_results_pin_information

        Returns the pin names, site numbers, and channel names that correspond to per-pin data read from the digital pattern instrument. The method returns pin information in the same order as values read using the read_static method, ppmu_measure method, and get_fail_count method. Use this method to match values the previously listed methods return with pins, sites, and instrument channels.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_pin_results_pin_information`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._get_pin_results_pin_information`

        Returns:
            pin_indexes (list of int): The returned index of the pins corresponding to data read from the digital pattern instrument using the specified repeated capabilities. If you do not want to use this parameter, pass VI_NULL.
                Call _get_pin_name to get the name of the pin associated with an index.

            site_numbers (list of int): The returned site numbers that correspond to data read from the digital pattern instrument using the specified repeated capabilities. If you do not want to use this parameter, pass VI_NULL.

            channel_indexes (list of int): The returned index of channels corresponding to data read from the digital pattern instrument using the specified repeated capabilities. If you do not want to use this parameter, pass VI_NULL.
                Call GetChannelName to get the name of the channel associated with an index. Channel indexes are one-based.

                Note:
                One or more of the referenced methods are not in the Python API for this driver.

        

#### `def _get_site_pass_fail(self)`

_get_site_pass_fail

        Returns the pass or fail results for each site.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ]._get_site_pass_fail`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._get_site_pass_fail`

        Returns:
            pass_fail (list of bool): The returned array of pass (True) and fail results for the sites you specify in the repeated capabilities. If sites span multiple digital pattern instruments, you must use an AND operator for the partial results for those sites returned by each instrument. If a site is disabled or not enabled for burst, the method does not return data for that site. Use the SortSiteResultsViBoolean method to order and combine the data to match the repeated capabilities. You can also use the _get_site_results_site_numbers method to determine the order of the sites returned from this method call so that you can match the pass array with site numbers.

                Note:
                One or more of the referenced methods are not in the Python API for this driver.

        

#### `def _get_site_results_site_numbers(self, site_result_type)`

_get_site_results_site_numbers

        Returns the site numbers that correspond to per-site data read from the digital pattern instrument. The method returns site numbers in the same order as values read using the _get_site_pass_fail and fetch_capture_waveform_u32 methods. Use this method to match values the previously listed methods return with site numbers.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ]._get_site_results_site_numbers`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._get_site_results_site_numbers`

        Args:
            site_result_type (enums.SiteResultType): The type of data specified in the results array.

                -   _SiteResultType.PASS_FAIL: Get site numbers for pass/fail data.
                -   _SiteResultType.CAPTURE_WAVEFORM: Get site numbers for capture waveforms.


        Returns:
            site_numbers (list of int): The returned array of site numbers that correspond to the values specified by **siteResultType**.

        

#### `def get_time_set_drive_format(self, time_set_name)`

get_time_set_drive_format

        Returns the drive format of a pin in the specified time set.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].get_time_set_drive_format`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.get_time_set_drive_format`

        Args:
            time_set_name (str): The specified time set name.


        Returns:
            format (enums.DriveFormat): Returned drive format of the time set for the specified pin.

        

#### `def get_time_set_edge(self, time_set_name, edge)`

get_time_set_edge

        Returns the edge time of a pin in the specified time set.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].get_time_set_edge`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.get_time_set_edge`

        Args:
            time_set_name (str): The specified time set name.

            edge (enums.TimeSetEdgeType): Name of the edge.

                -   TimeSetEdgeType.DRIVE_ON
                -   TimeSetEdgeType.DRIVE_DATA
                -   TimeSetEdgeType.DRIVE_RETURN
                -   TimeSetEdgeType.DRIVE_OFF
                -   TimeSetEdgeType.COMPARE_STROBE
                -   TimeSetEdgeType.DRIVE_DATA2
                -   TimeSetEdgeType.DRIVE_RETURN2
                -   TimeSetEdgeType.COMPARE_STROBE2


        Returns:
            time (hightime.timedelta): Time from the beginning of the vector period in which to place the edge.

        

#### `def get_time_set_edge_multiplier(self, time_set_name)`

get_time_set_edge_multiplier

        Returns the edge multiplier of the specified time set.

        Tip:
        This method can be called on specific pins within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container pins to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.pins[ ... ].get_time_set_edge_multiplier`

        To call the method on all pins, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.get_time_set_edge_multiplier`

        Args:
            time_set_name (str): The specified time set name.


        Returns:
            edge_multiplier (int): Returned edge multiplier of the time set for the specified pin.

        

#### `def _get_time_set_name(self, time_set_index)`

_get_time_set_name

        TBD

        Args:
            time_set_index (int):


        Returns:
            name (str):

        

#### `def is_site_enabled(self)`

is_site_enabled

        Checks if a specified site is enabled.

        Note: The method returns an error if more than one site is specified.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ].is_site_enabled`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.is_site_enabled`

        Returns:
            enable (bool): Boolean value that returns whether the site is enabled or disabled.

        

#### `def lock(self)`

lock

        Obtains a multithread lock on the device session. Before doing so, the
        software waits until all other execution threads release their locks
        on the device session.

        Other threads may have obtained a lock on this session for the
        following reasons:

            -  The application called the lock method.
            -  A call to NI-Digital Pattern Driver locked the session.
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
            lock (context manager): When used in a with statement, nidigital.Session.lock acts as
            a context manager and unlock will be called when the with block is exited
        

#### `def ppmu_measure(self, measurement_type)`

ppmu_measure

        Instructs the PPMU to measure voltage or current. This method can be called to take a voltage measurement even if the pin method is not set to PPMU.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].ppmu_measure`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.ppmu_measure`

        Args:
            measurement_type (enums.PPMUMeasurementType): Parameter that specifies whether the PPMU measures voltage or current from the DUT.

                -   PPMUMeasurementType.CURRENT: The PPMU measures current from the DUT.
                -   PPMUMeasurementType.VOLTAGE: The PPMU measures voltage from the DUT.


        Returns:
            measurements (list of float): The returned array of measurements in the order you specify in the repeated capabilities. If a site is disabled, the method does not return data for that site. You can also use the get_pin_results_pin_information method to obtain a sorted list of returned sites and channels.

        

#### `def ppmu_source(self)`

ppmu_source

        Starts sourcing voltage or current from the PPMU. This method automatically selects the PPMU method. Changes to PPMU source settings do not take effect until you call this method. If you modify source settings after you call this method, you must call this method again for changes in the configuration to take effect.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].ppmu_source`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.ppmu_source`
        

#### `def read_static(self)`

read_static

        Reads the current state of comparators for pins you specify in the repeated capabilities. If there are uncommitted changes to levels or the termination mode, this method commits the changes to the pins.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].read_static`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.read_static`

        Returns:
            data (list of enums.PinState): The returned array of pin states read from the channels in the repeated capabilities. Data is returned in the order you specify in the repeated capabilities. If a site is disabled, the method does not return data for that site. You can also use the get_pin_results_pin_information method to obtain a sorted list of returned sites and channels.

                -   PinState.L: The comparators read a logic low pin state.
                -   PinState.H: The comparators read a logic high pin state.
                -   PinState.M: The comparators read a midband pin state.
                -   PinState.V: The comparators read a value that is above VOH and below VOL, which can occur when you set VOL higher than VOH.

        

#### `def _set_attribute_vi_boolean(self, attribute, value)`

_set_attribute_vi_boolean

        Sets the value of a ViBoolean property. Use this method to set the values of digital pattern instrument-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_boolean`

        Args:
            attribute (int): The ID of a property.

            value (bool): The value to which you want to set the property; some of the values might not be valid depending on the current settings of the instrument session.

        

#### `def _set_attribute_vi_int32(self, attribute, value)`

_set_attribute_vi_int32

        Sets the value of a ViInt32 property. Use this method to set the values of digital pattern instrument-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_int32`

        Args:
            attribute (int): The ID of a property.

            value (int): The value to which you want to set the property; some of the values might not be valid depending on the current settings of the instrument session.

        

#### `def _set_attribute_vi_int64(self, attribute, value)`

_set_attribute_vi_int64

        Sets the value of a ViInt64 property. Use this method to set the values of digital pattern instrument-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_int64`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_int64`

        Args:
            attribute (int): The ID of a property.

            value (int): The value to which you want to set the property; some of the values might not be valid depending on the current settings of the instrument session.

        

#### `def _set_attribute_vi_real64(self, attribute, value)`

_set_attribute_vi_real64

        Sets the value of a ViIntReal64 property. Use this method to set the values of digital pattern instrument-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_real64`

        Args:
            attribute (int): The ID of a property.

            value (float): The value to which you want to set the property; some of the values might not be valid depending on the current settings of the instrument session.

        

#### `def _set_attribute_vi_string(self, attribute, value)`

_set_attribute_vi_string

        Sets the value of a ViString property. Use this method to set the values of digital pattern instrument-specific properties and inherent IVI properties.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_string`

        Args:
            attribute (int): The ID of a property.

            value (str): The value to which you want to set the property; some of the values might not be valid depending on the current settings of the instrument session.

        

#### `def tdr(self, apply_offsets=True)`

tdr

        Measures propagation delays through cables, connectors, and load boards using Time-Domain Reflectometry (TDR). Ensure that the channels and pins you select are connected to an open circuit.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].tdr`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.tdr`

        Args:
            apply_offsets (bool): A Boolean that specifies whether to apply the measured TDR offsets. If you need to adjust the measured offsets prior to applying, set this input to False, and call the apply_tdr_offsets method to specify the adjusted TDR offsets values.


        Returns:
            offsets (list of hightime.timedelta): Measured TDR offsets specified in seconds.

        

#### `def unlock(self)`

unlock

        Releases a lock that you acquired on an device session using
        lock. Refer to lock for additional
        information on session locks.
        

#### `def _write_source_waveform_site_unique_u32(self, waveform_name, num_waveforms, samples_per_waveform, waveform_data)`

_write_source_waveform_site_unique_u32

        Writes one waveform per site. Use this write method if you set the parameter of the create source waveform method to Site Unique.

        Tip:
        This method can be called on specific sites within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container sites to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.sites[ ... ]._write_source_waveform_site_unique_u32`

        To call the method on all sites, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session._write_source_waveform_site_unique_u32`

        Args:
            waveform_name (str): The name to assign to the waveform. Use the waveform_name  with source_start opcode in your pattern.

            num_waveforms (int): Number of waveforms.

            samples_per_waveform (int): Number of samples per waveform.

            waveform_data (array.array("L")): An array of samples to use as source data. Data for each site must be appended sequentially in the array (non-interleaved).

        

#### `def write_static(self, state)`

write_static

        Writes a static state to the specified pins. The selected pins remain in the specified state until the next pattern burst or call to this method. If there are uncommitted changes to levels or the termination mode, this method commits the changes to the pins. This method does not change the selected pin method. If you write a static state to a pin that does not have the Digital method selected, the new static state is stored by the instrument, and affects the state of the pin the next time you change the selected method to Digital.

        Tip:
        This method can be called on specific channels within your :py:class:`nidigital.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].write_static`

        To call the method on all channels, you can call it directly on the :py:class:`nidigital.Session`.

        Example: :py:meth:`my_session.write_static`

        Args:
            state (enums.WriteStaticPinState): Parameter that specifies one of the following digital states to assign to the pin.

                -   WriteStaticPinState.ZERO: Specifies to drive low.
                -   WriteStaticPinState.ONE: Specifies to drive high.
                -   WriteStaticPinState.X: Specifies to not drive.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        

#### `def _error_message(self, error_code)`

_error_message

        Takes the error code returned by the digital pattern instrument driver methods, interprets it, and returns it as a user readable string.

        Args:
            error_code (int): The specified error code.


        Returns:
            error_message (str): The error information formatted as a string. The array must contain at least 256 characters.

        

### `class Session(_SessionBase)`

An NI-Digital Pattern Driver session

#### `def __init__(self, resource_name, id_query=False, reset_device=False, options={}, *, grpc_options=None)`

An NI-Digital Pattern Driver session

        Creates and returns a new session to the specified digital pattern instrument to use in all subsequent method calls. To place the instrument in a known startup state when creating a new session, set the reset parameter to True, which is equivalent to calling the reset method immediately after initializing the session.

        Args:
            resource_name (str): The specified resource name shown in Measurement & Automation Explorer (MAX) for a digital pattern instrument, for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name. **resourceName** can also be a logical IVI name. This parameter accepts a comma-delimited list of strings in the form PXI1Slot2,PXI1Slot3, where ``PXI1Slot2`` is one instrument resource name and ``PXI1Slot3`` is another. When including more than one digital pattern instrument in the comma-delimited list of strings, list the instruments in the same order they appear in the pin map.

                +--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | |Note| | Note   You only can specify multiple instruments of the same model. For example, you can list two PXIe-6570s but not a PXIe-6570 and PXIe-6571. The instruments must be in the same chassis. |
                +--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

                .. |Note| image:: note.gif

                Note:

            id_query (bool): A Boolean that verifies that the digital pattern instrument you initialize is supported by NI-Digital. NI-Digital automatically performs this query, so setting this parameter is not necessary.

            reset_device (bool): A Boolean that specifies whether to reset a digital pattern instrument to a known state when the session is initialized. Setting the **resetDevice** value to True is equivalent to calling the reset method immediately after initializing the session.

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

            grpc_options (nidigital.grpc_session_options.GrpcSessionOptions): MeasurementLink gRPC session options


        Returns:
            new_vi (int): The returned instrument session.

        

#### `def __enter__(self)`

#### `def __exit__(self, exc_type, exc_value, traceback)`

#### `def initiate(self)`

initiate

        Starts bursting the pattern configured by start_label, causing the NI-Digital session to be committed. To stop the pattern burst, call abort. If keep alive pattern is bursting when abort is called or upon exiting the context manager, keep alive pattern will not be stopped. To stop the keep alive pattern, call abort_keep_alive.

        Note:
        This method will return a Python context manager that will initiate on entering and abort on exit.
        

#### `def close(self)`

close

        Closes the specified instrument session to a digital pattern instrument, aborts pattern execution, and unloads pattern memory. The channels on a digital pattern instrument remain in their current state.

        Note:
        This method is not needed when using the session context manager
        

#### `def abort(self)`

abort

        Stops bursting the pattern.
        

#### `def abort_keep_alive(self)`

abort_keep_alive

        Stops the keep alive pattern if it is currently running. If a pattern burst is in progress, the method aborts the pattern burst. If you start a new pattern burst while a keep alive pattern is running, the keep alive pattern runs to the last keep alive vector, and the new pattern burst starts on the next cycle.
        

#### `def commit(self)`

commit

        Applies all previously configured pin levels, termination modes, clocks, triggers, and pattern timing to a digital pattern instrument. If you do not call the commit method, then the initiate method or the burst_pattern method will implicitly call this method for you. Calling this method moves the session from the Uncommitted state to the Committed state.
        

#### `def configure_time_set_period(self, time_set_name, period)`

configure_time_set_period

        Configures the period of a time set. Use this method to modify time set values after applying a timing sheet with the apply_levels_and_timing method, or to create time sets programmatically without the use of timing sheets. This method does not modify the timing sheet file or the timing sheet contents that will be used in future calls to apply_levels_and_timing; it only affects the values of the current timing context.

        Args:
            time_set_name (str): The specified time set name.

            period (hightime.timedelta, datetime.timedelta, or float in seconds): Period for this time set, in seconds.

        

#### `def create_capture_waveform_from_file_digicapture(self, waveform_name, waveform_file_path)`

create_capture_waveform_from_file_digicapture

        Creates a capture waveform with the configuration information from a Digicapture file generated by the Digital Pattern Editor.

        Args:
            waveform_name (str): Waveform name you want to use. You must specify waveform_name if the file contains multiple waveforms. Use the waveform_name with the capture_start opcode in your pattern.

            waveform_file_path (str): Absolute file path to the capture waveform file (.digicapture) you want to load.

        

#### `def create_source_waveform_from_file_tdms(self, waveform_name, waveform_file_path, write_waveform_data=True)`

create_source_waveform_from_file_tdms

        Creates a source waveform with configuration information from a TDMS file generated by the Digital Pattern Editor. It also optionally writes waveform data from the file.

        Args:
            waveform_name (str): The waveform name you want to use from the file. You must specify waveform_name if the file contains multiple waveforms. Use the waveform_name with the source_start opcode in your pattern.

            waveform_file_path (str): Absolute file path to the load source waveform file (.tdms).

            write_waveform_data (bool): A Boolean that writes waveform data to source memory if True and the waveform data is in the file.

        

#### `def create_time_set(self, name)`

create_time_set

        Creates a time set with the name that you specify. Use this method when you want to create time sets programmatically rather than with a timing sheet.

        Args:
            name (str): The specified name of the new time set.

        

#### `def delete_all_time_sets(self)`

delete_all_time_sets

        Deletes all time sets from instrument memory.
        

#### `def enable_match_fail_combination(self, sync_session)`

enable_match_fail_combination

        Configures digital pattern instruments and the PXIe-6674T timing and synchronization instrument to combine pattern comparison results and control subsequent pattern execution across digital pattern instruments based on those results. You must initialize the PXIe-6674T using NI-Sync and call this method from a multi-instrument session.
        

#### `def load_specifications_levels_and_timing(self, specifications_file_paths=None, levels_file_paths=None, timing_file_paths=None)`

load_specifications_levels_and_timing

        Loads settings in specifications, levels, and timing sheets. These settings are not
        applied to the digital pattern instrument until apply_levels_and_timing is called.

        If the levels and timing sheets contains formulas, they are evaluated at load time.
        If the formulas refer to variables, the specifications sheets that define those
        variables must be loaded either first, or at the same time as the levels and timing sheets.

        Args:
            specifications_file_paths (str or basic sequence of str): Absolute file path of one or more specifications files.

            levels_file_paths (str or basic sequence of str): Absolute file path of one or more levels sheet files.

            timing_file_paths (str or basic sequence of str): Absolute file path of one or more timing sheet files.

        

#### `def _call_method_with_iterable(self, method, files)`

#### `def self_test(self)`

self_test

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
        

#### `def unload_specifications(self, file_paths)`

unload_specifications

        Unloads the given specifications sheets present in the previously loaded
        specifications files that you select.

        You must call load_specifications_levels_and_timing to reload the files with updated
        specifications values. You must then call apply_levels_and_timing in order to apply
        the levels and timing values that reference the updated specifications values.

        Args:
            file_paths (str or basic sequence of str): Absolute file path of one or more loaded specifications files.

        

#### `def write_source_waveform_site_unique(self, waveform_name, waveform_data)`

write_source_waveform_site_unique

        Writes one waveform per site. Use this write method if you set the parameter of the create source waveform method to Site Unique.

        Args:
            waveform_name (str): The name to assign to the waveform. Use the waveform_name with source_start opcode in your pattern.

            waveform_data ({ int: basic sequence of unsigned int, int: basic sequence of unsigned int, ... }): Dictionary where each key is a site number and value is a collection of samples to use as source data

        

#### `def get_pattern_pin_names(self, start_label)`

get_pattern_pin_names

        Returns the pattern pin list.

        Args:
            start_label (str): Pattern name or exported pattern label from which to get the pin names that the pattern references.


        Returns:
            pin_list (list of str): List of pins referenced by the pattern with the **startLabel**.

        

#### `def get_time_set_period(self, time_set_name)`

get_time_set_period

        Returns the period of the specified time set.

        Args:
            time_set_name (str): The specified time set name.


        Returns:
            period (hightime.timedelta): Returned period, in seconds, that the edge is configured to.

        

#### `def _init_with_options(self, resource_name, id_query=False, reset_device=False, option_string='')`

_init_with_options

        Creates and returns a new session to the specified digital pattern instrument to use in all subsequent method calls. To place the instrument in a known startup state when creating a new session, set the reset parameter to True, which is equivalent to calling the reset method immediately after initializing the session.

        Args:
            resource_name (str): The specified resource name shown in Measurement & Automation Explorer (MAX) for a digital pattern instrument, for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name. **resourceName** can also be a logical IVI name. This parameter accepts a comma-delimited list of strings in the form PXI1Slot2,PXI1Slot3, where ``PXI1Slot2`` is one instrument resource name and ``PXI1Slot3`` is another. When including more than one digital pattern instrument in the comma-delimited list of strings, list the instruments in the same order they appear in the pin map.

                +--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
                | |Note| | Note   You only can specify multiple instruments of the same model. For example, you can list two PXIe-6570s but not a PXIe-6570 and PXIe-6571. The instruments must be in the same chassis. |
                +--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

                .. |Note| image:: note.gif

                Note:

            id_query (bool): A Boolean that verifies that the digital pattern instrument you initialize is supported by NI-Digital. NI-Digital automatically performs this query, so setting this parameter is not necessary.

            reset_device (bool): A Boolean that specifies whether to reset a digital pattern instrument to a known state when the session is initialized. Setting the **resetDevice** value to True is equivalent to calling the reset method immediately after initializing the session.

            option_string (dict): The initial values of certain properties for the NI-Digital Pattern Driver session. The string can be empty. You can use the DriverSetup flag to simulate a digital pattern instrument. When simulating a digital pattern instrument, you must specify the model you want to simulate. For example, Simulate = 1, DriverSetup = Model:6570.


        Returns:
            new_vi (int): The returned instrument session.

        

#### `def _initiate(self)`

_initiate

        Starts bursting the pattern configured by start_label, causing the NI-Digital session to be committed. To stop the pattern burst, call abort. If keep alive pattern is bursting when abort is called or upon exiting the context manager, keep alive pattern will not be stopped. To stop the keep alive pattern, call abort_keep_alive.
        

#### `def is_done(self)`

is_done

        Checks the hardware to determine if the pattern burst has completed or if any errors have occurred.

        Returns:
            done (bool): A Boolean that indicates whether the pattern burst completed.

        

#### `def _load_levels(self, file_path)`

_load_levels

        Loads a levels sheet from a specified file.

        Args:
            file_path (str): Absolute file path to the specified levels sheet file.

        

#### `def load_pattern(self, file_path)`

load_pattern

        Loads the specified pattern file.

        Args:
            file_path (str): Absolute file path of the binary .digipat pattern file to load. Specify the pattern to burst using start_label or the start_label parameter of the burst_pattern method.

        

#### `def load_pin_map(self, file_path)`

load_pin_map

        Loads a pin map file. You can load only a single pin and channel map file during an NI-Digital Pattern Driver session. To switch pin maps, create a new session or call the reset method.

        Args:
            file_path (str): Absolute file path to a pin map file created with the Digital Pattern Editor or the NI TestStand Semiconductor Module.

        

#### `def _load_specifications(self, file_path)`

_load_specifications

        Loads a specifications sheet from a specified file.

        Args:
            file_path (str): Absolute file path to a specifications file.

        

#### `def _load_timing(self, file_path)`

_load_timing

        Loads a timing sheet from a specified file.

        Args:
            file_path (str): Absolute file path to the specified timing sheet file.

        

#### `def read_sequencer_flag(self, flag)`

read_sequencer_flag

        Reads the state of a pattern sequencer flag. Use pattern sequencer flags to coordinate execution between the pattern sequencer and a runtime test program.

        Args:
            flag (enums.SequencerFlag): The pattern sequencer flag you want to read.

                -   SequencerFlag.FLAG0 ("seqflag0"): Reads pattern sequencer flag 0.
                -   SequencerFlag.FLAG1 ("seqflag1"): Reads pattern sequencer flag 1.
                -   SequencerFlag.FLAG2 ("seqflag2"): Reads pattern sequencer flag 2.
                -   SequencerFlag.FLAG3 ("seqflag3"): Reads pattern sequencer flag 3.


        Returns:
            value (bool): A Boolean that indicates the state of the pattern sequencer flag you specify.

        

#### `def read_sequencer_register(self, reg)`

read_sequencer_register

        Reads the value of a pattern sequencer register. Use pattern sequencer registers to pass numeric values between the pattern sequencer and a runtime test program. For example, you can use this method to read a register modified by the write_reg opcode during a pattern burst.

        Args:
            reg (enums.SequencerRegister): The sequencer register to read from.

                -   SequencerRegister.REGISTER0 ("reg0"): Reads sequencer register 0.
                -   SequencerRegister.REGISTER1 ("reg1"): Reads sequencer register 1.
                -   SequencerRegister.REGISTER2 ("reg2"): Reads sequencer register 2.
                -   SequencerRegister.REGISTER3 ("reg3"): Reads sequencer register 3.
                -   SequencerRegister.REGISTER4 ("reg4"): Reads sequencer register 4.
                -   SequencerRegister.REGISTER5 ("reg5"): Reads sequencer register 5.
                -   SequencerRegister.REGISTER6 ("reg6"): Reads sequencer register 6.
                -   SequencerRegister.REGISTER7 ("reg7"): Reads sequencer register 7.
                -   SequencerRegister.REGISTER8 ("reg8"): Reads sequencer register 8.
                -   SequencerRegister.REGISTER9 ("reg9"): Reads sequencer register 9.
                -   SequencerRegister.REGISTER10 ("reg10"): Reads sequencer register 10.
                -   SequencerRegister.REGISTER11 ("reg11"): Reads sequencer register 11.
                -   SequencerRegister.REGISTER12 ("reg12"): Reads sequencer register 12.
                -   SequencerRegister.REGISTER13 ("reg13"): Reads sequencer register 13.
                -   SequencerRegister.REGISTER14 ("reg14"): Reads sequencer register 14.
                -   SequencerRegister.REGISTER15 ("reg15"): Reads sequencer register 15.


        Returns:
            value (int): Value read from the sequencer register.

        

#### `def reset_device(self)`

reset_device

        Returns a digital pattern instrument to a known state. This method performs the following actions:

        - Aborts pattern execution.
        - Clears pin maps, time sets, source and capture waveforms, and patterns.
        - Resets all properties to default values, including the selected_function property that is set to SelectedFunction.DISCONNECT, causing the I/O switches to open.
        - Stops export of all external signals and events.
        - Clears over-temperature and over-power conditions.
        

#### `def self_calibrate(self)`

self_calibrate

        Performs self-calibration on a digital pattern instrument.
        

#### `def send_software_edge_trigger(self, trigger, trigger_identifier)`

send_software_edge_trigger

        Forces a particular edge-based trigger to occur regardless of how the specified trigger is configured. You can use this method as a software override.

        Args:
            trigger (enums.SoftwareTrigger): Trigger specifies the trigger you want to override.

                +----------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
                | Defined Values                   |                                                                                                                                 |
                +==================================+=================================================================================================================================+
                | SoftwareTrigger.START            | Overrides the Start trigger. You must specify an empty string in the trigger_identifier parameter.                              |
                +----------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
                | SoftwareTrigger.CONDITIONAL_JUMP | Specifies to route a conditional jump trigger. You must specify a conditional jump trigger in the trigger_identifier parameter. |
                +----------------------------------+---------------------------------------------------------------------------------------------------------------------------------+

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            trigger_identifier (str): Trigger Identifier specifies the instance of the trigger you want to override.
                If trigger is specified as NIDIGITAL_VAL_START_TRIGGER, this parameter must be an empty string. If trigger is
                specified as NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER, allowed values are conditionalJumpTrigger0,
                conditionalJumpTrigger1, conditionalJumpTrigger2, and conditionalJumpTrigger3.

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        

#### `def unload_all_patterns(self, unload_keep_alive_pattern=False)`

unload_all_patterns

        Unloads all patterns, source waveforms, and capture waveforms from a digital pattern instrument.

        Args:
            unload_keep_alive_pattern (bool): A Boolean that specifies whether to keep or unload the keep alive pattern.

        

#### `def _unload_specifications(self, file_path)`

_unload_specifications

        Unloads the given specifications sheet present in the previously loaded specifications file that you select. You must call the _load_specifications method to reload the file with updated specifications values. You must then call the apply_levels_and_timing method in order to apply the levels and timing values that reference the updated specifications values.

        Args:
            file_path (str): Absolute file path to a loaded specifications file.

        

#### `def wait_until_done(self, timeout=hightime.timedelta(seconds=10.0))`

wait_until_done

        Waits until the pattern burst has completed or the timeout has expired.

        Args:
            timeout (hightime.timedelta, datetime.timedelta, or float in seconds): Maximum time (in seconds) allowed for this method to complete. If this method does not complete within this time interval, this method returns an error.

        

#### `def write_sequencer_flag(self, flag, value)`

write_sequencer_flag

        Writes the state of a pattern sequencer flag. Use pattern sequencer flags to coordinate execution between the pattern sequencer and a runtime test program.

        Args:
            flag (enums.SequencerFlag): The pattern sequencer flag to write.

                -   SequencerFlag.FLAG0 ("seqflag0"): Writes pattern sequencer flag 0.
                -   SequencerFlag.FLAG1 ("seqflag1"): Writes pattern sequencer flag 1.
                -   SequencerFlag.FLAG2 ("seqflag2"): Writes pattern sequencer flag 2.
                -   SequencerFlag.FLAG3 ("seqflag3"): Writes pattern sequencer flag 3.

            value (bool): A Boolean that assigns a state to the pattern sequencer flag you specify.

        

#### `def write_sequencer_register(self, reg, value)`

write_sequencer_register

        Writes a value to a pattern sequencer register. Use pattern sequencer registers to pass numeric values between the pattern sequencer and a runtime test program.

        Args:
            reg (enums.SequencerRegister): The sequencer register you want to write to.

                -   SequencerRegister.REGISTER0 ("reg0"): Writes sequencer register 0.
                -   SequencerRegister.REGISTER1 ("reg1"): Writes sequencer register 1.
                -   SequencerRegister.REGISTER2 ("reg2"): Writes sequencer register 2.
                -   SequencerRegister.REGISTER3 ("reg3"): Writes sequencer register 3.
                -   SequencerRegister.REGISTER4 ("reg4"): Writes sequencer register 4.
                -   SequencerRegister.REGISTER5 ("reg5"): Writes sequencer register 5.
                -   SequencerRegister.REGISTER6 ("reg6"): Writes sequencer register 6.
                -   SequencerRegister.REGISTER7 ("reg7"): Writes sequencer register 7.
                -   SequencerRegister.REGISTER8 ("reg8"): Writes sequencer register 8.
                -   SequencerRegister.REGISTER9 ("reg9"): Writes sequencer register 9.
                -   SequencerRegister.REGISTER10 ("reg10"): Writes sequencer register 10.
                -   SequencerRegister.REGISTER11 ("reg11"): Writes sequencer register 11.
                -   SequencerRegister.REGISTER12 ("reg12"): Writes sequencer register 12.
                -   SequencerRegister.REGISTER13 ("reg13"): Writes sequencer register 13.
                -   SequencerRegister.REGISTER14 ("reg14"): Writes sequencer register 14.
                -   SequencerRegister.REGISTER15 ("reg15"): Writes sequencer register 15.

            value (int): The value you want to write to the register.

        

#### `def write_source_waveform_broadcast(self, waveform_name, waveform_data)`

write_source_waveform_broadcast

        Writes the same waveform data to all sites. Use this write method if you set the data_mapping parameter of the create source waveform method to SourceDataMapping.BROADCAST.

        Args:
            waveform_name (str): The name to assign to the waveform. Use the waveform_name  with source_start opcode in your pattern.

            waveform_data (list of int): 1D array of samples to use as source data to apply to all sites.

        

#### `def write_source_waveform_data_from_file_tdms(self, waveform_name, waveform_file_path)`

write_source_waveform_data_from_file_tdms

        Writes a source waveform based on the waveform data and configuration information the file contains.

        Args:
            waveform_name (str): The name to assign to the waveform. Use the waveform_name  with source_start opcode in your pattern.

            waveform_file_path (str): Absolute file path to the load source waveform file (.tdms).

        

#### `def _close(self)`

_close

        Closes the specified instrument session to a digital pattern instrument, aborts pattern execution, and unloads pattern memory. The channels on a digital pattern instrument remain in their current state.
        

#### `def reset(self)`

reset

        Returns a digital pattern instrument to a known state. This method performs the following actions:

        - Aborts pattern execution.
        - Clears pin maps, time sets, source and capture waveforms, and patterns.
        - Resets all properties to default values, including the selected_function property that is set to SelectedFunction.DISCONNECT, causing the I/O switches to open.
        - Stops exporting all external signals and events.
        

#### `def _self_test(self)`

_self_test

        Returns self test results from a digital pattern instrument. This test requires several minutes to execute.

        Returns:
            test_result (int): A parameter that indicates if the self test passed (0) or failed (!=0).

            test_message (str): The returned self test status message. The array must contain at least 256 characters.

        

<!--NI_PYTHON_API repo=nimi-python path=generated/nidigital/nidigital/unit_tests/_matchers.py -->
## PYTHON MODULE: generated/nidigital/nidigital/unit_tests/_matchers.py

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

<!--NI_PYTHON_API repo=nimi-python path=generated/nidigital/nidigital/unit_tests/_mock_helper.py -->
## PYTHON MODULE: generated/nidigital/nidigital/unit_tests/_mock_helper.py

### `class MockFunctionCallError(Exception)`

#### `def __init__(self, function, param=None)`

### `class SideEffectsHelper(object)`

#### `def __init__(self)`

#### `def __getitem__(self, func)`

#### `def __setitem__(self, func, val)`

#### `def niDigital_Abort(self, vi)`

#### `def niDigital_AbortKeepAlive(self, vi)`

#### `def niDigital_ApplyLevelsAndTiming(self, vi, site_list, levels_sheet, timing_sheet, initial_state_high_pins, initial_state_low_pins, initial_state_tristate_pins)`

#### `def niDigital_ApplyTDROffsets(self, vi, channel_list, num_offsets, offsets)`

#### `def niDigital_BurstPattern(self, vi, site_list, start_label, select_digital_function, wait_until_done, timeout)`

#### `def niDigital_ClockGenerator_Abort(self, vi, channel_list)`

#### `def niDigital_ClockGenerator_GenerateClock(self, vi, channel_list, frequency, select_digital_function)`

#### `def niDigital_Commit(self, vi)`

#### `def niDigital_ConfigureActiveLoadLevels(self, vi, channel_list, iol, ioh, vcom)`

#### `def niDigital_ConfigurePatternBurstSites(self, vi, site_list)`

#### `def niDigital_ConfigureTimeSetCompareEdgesStrobe(self, vi, pin_list, time_set_name, strobe_edge)`

#### `def niDigital_ConfigureTimeSetCompareEdgesStrobe2x(self, vi, pin_list, time_set_name, strobe_edge, strobe2_edge)`

#### `def niDigital_ConfigureTimeSetDriveEdges(self, vi, pin_list, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge)`

#### `def niDigital_ConfigureTimeSetDriveEdges2x(self, vi, pin_list, time_set_name, format, drive_on_edge, drive_data_edge, drive_return_edge, drive_off_edge, drive_data2_edge, drive_return2_edge)`

#### `def niDigital_ConfigureTimeSetDriveFormat(self, vi, pin_list, time_set_name, drive_format)`

#### `def niDigital_ConfigureTimeSetEdge(self, vi, pin_list, time_set_name, edge, time)`

#### `def niDigital_ConfigureTimeSetEdgeMultiplier(self, vi, pin_list, time_set_name, edge_multiplier)`

#### `def niDigital_ConfigureTimeSetPeriod(self, vi, time_set_name, period)`

#### `def niDigital_ConfigureVoltageLevels(self, vi, channel_list, vil, vih, vol, voh, vterm)`

#### `def niDigital_CreateCaptureWaveformFromFileDigicapture(self, vi, waveform_name, waveform_file_path)`

#### `def niDigital_CreateCaptureWaveformParallel(self, vi, pin_list, waveform_name)`

#### `def niDigital_CreateCaptureWaveformSerial(self, vi, pin_list, waveform_name, sample_width, bit_order)`

#### `def niDigital_CreateSourceWaveformFromFileTDMS(self, vi, waveform_name, waveform_file_path, write_waveform_data)`

#### `def niDigital_CreateSourceWaveformParallel(self, vi, pin_list, waveform_name, data_mapping)`

#### `def niDigital_CreateSourceWaveformSerial(self, vi, pin_list, waveform_name, data_mapping, sample_width, bit_order)`

#### `def niDigital_CreateTimeSet(self, vi, name)`

#### `def niDigital_DeleteAllTimeSets(self, vi)`

#### `def niDigital_DisableSites(self, vi, site_list)`

#### `def niDigital_EnableMatchFailCombination(self, session_count, sessions, sync_session)`

#### `def niDigital_EnableSites(self, vi, site_list)`

#### `def niDigital_FetchCaptureWaveformU32(self, vi, site_list, waveform_name, samples_to_read, timeout, data_buffer_size, data, actual_num_waveforms, actual_samples_per_waveform)`

#### `def niDigital_FetchHistoryRAMCycleInformation(self, vi, site, sample_index, pattern_index, time_set_index, vector_number, cycle_number, num_dut_cycles)`

#### `def niDigital_FetchHistoryRAMCyclePinData(self, vi, site, pin_list, sample_index, dut_cycle_index, pin_data_buffer_size, expected_pin_states, actual_pin_states, per_pin_pass_fail, actual_num_pin_data)`

#### `def niDigital_FetchHistoryRAMScanCycleNumber(self, vi, site, sample_index, scan_cycle_number)`

#### `def niDigital_FrequencyCounter_MeasureFrequency(self, vi, channel_list, frequencies_buffer_size, frequencies, actual_num_frequencies)`

#### `def niDigital_GetAttributeViBoolean(self, vi, channel_name, attribute, value)`

#### `def niDigital_GetAttributeViInt32(self, vi, channel_name, attribute, value)`

#### `def niDigital_GetAttributeViInt64(self, vi, channel_name, attribute, value)`

#### `def niDigital_GetAttributeViReal64(self, vi, channel_name, attribute, value)`

#### `def niDigital_GetAttributeViString(self, vi, channel_name, attribute, buffer_size, value)`

#### `def niDigital_GetChannelNameFromString(self, vi, indices, name_buffer_size, names)`

#### `def niDigital_GetError(self, vi, error_code, error_description_buffer_size, error_description)`

#### `def niDigital_GetFailCount(self, vi, channel_list, buffer_size, failure_count, actual_num_read)`

#### `def niDigital_GetHistoryRAMSampleCount(self, vi, site, sample_count)`

#### `def niDigital_GetPatternName(self, vi, pattern_index, name_buffer_size, name)`

#### `def niDigital_GetPatternPinList(self, vi, start_label, pin_list_buffer_size, pin_list)`

#### `def niDigital_GetPinName(self, vi, pin_index, name_buffer_size, name)`

#### `def niDigital_GetPinResultsPinInformation(self, vi, channel_list, buffer_size, pin_indexes, site_numbers, channel_indexes, actual_num_values)`

#### `def niDigital_GetSitePassFail(self, vi, site_list, pass_fail_buffer_size, pass_fail, actual_num_sites)`

#### `def niDigital_GetSiteResultsSiteNumbers(self, vi, site_list, site_result_type, site_numbers_buffer_size, site_numbers, actual_num_site_numbers)`

#### `def niDigital_GetTimeSetDriveFormat(self, vi, pin, time_set_name, format)`

#### `def niDigital_GetTimeSetEdge(self, vi, pin, time_set_name, edge, time)`

#### `def niDigital_GetTimeSetEdgeMultiplier(self, vi, pin, time_set_name, edge_multiplier)`

#### `def niDigital_GetTimeSetName(self, vi, time_set_index, name_buffer_size, name)`

#### `def niDigital_GetTimeSetPeriod(self, vi, time_set_name, period)`

#### `def niDigital_InitWithOptions(self, resource_name, id_query, reset_device, option_string, new_vi)`

#### `def niDigital_Initiate(self, vi)`

#### `def niDigital_IsDone(self, vi, done)`

#### `def niDigital_IsSiteEnabled(self, vi, site, enable)`

#### `def niDigital_LoadLevels(self, vi, file_path)`

#### `def niDigital_LoadPattern(self, vi, file_path)`

#### `def niDigital_LoadPinMap(self, vi, file_path)`

#### `def niDigital_LoadSpecifications(self, vi, file_path)`

#### `def niDigital_LoadTiming(self, vi, file_path)`

#### `def niDigital_LockSession(self, vi, caller_has_lock)`

#### `def niDigital_PPMU_Measure(self, vi, channel_list, measurement_type, buffer_size, measurements, actual_num_read)`

#### `def niDigital_PPMU_Source(self, vi, channel_list)`

#### `def niDigital_ReadSequencerFlag(self, vi, flag, value)`

#### `def niDigital_ReadSequencerRegister(self, vi, reg, value)`

#### `def niDigital_ReadStatic(self, vi, channel_list, buffer_size, data, actual_num_read)`

#### `def niDigital_ResetDevice(self, vi)`

#### `def niDigital_SelfCalibrate(self, vi)`

#### `def niDigital_SendSoftwareEdgeTrigger(self, vi, trigger, trigger_identifier)`

#### `def niDigital_SetAttributeViBoolean(self, vi, channel_name, attribute, value)`

#### `def niDigital_SetAttributeViInt32(self, vi, channel_name, attribute, value)`

#### `def niDigital_SetAttributeViInt64(self, vi, channel_name, attribute, value)`

#### `def niDigital_SetAttributeViReal64(self, vi, channel_name, attribute, value)`

#### `def niDigital_SetAttributeViString(self, vi, channel_name, attribute, value)`

#### `def niDigital_SetRuntimeEnvironment(self, environment, environment_version, reserved1, reserved2)`

#### `def niDigital_TDR(self, vi, channel_list, apply_offsets, offsets_buffer_size, offsets, actual_num_offsets)`

#### `def niDigital_UnloadAllPatterns(self, vi, unload_keep_alive_pattern)`

#### `def niDigital_UnloadSpecifications(self, vi, file_path)`

#### `def niDigital_UnlockSession(self, vi, caller_has_lock)`

#### `def niDigital_WaitUntilDone(self, vi, timeout)`

#### `def niDigital_WriteSequencerFlag(self, vi, flag, value)`

#### `def niDigital_WriteSequencerRegister(self, vi, reg, value)`

#### `def niDigital_WriteSourceWaveformBroadcastU32(self, vi, waveform_name, waveform_size, waveform_data)`

#### `def niDigital_WriteSourceWaveformDataFromFileTDMS(self, vi, waveform_name, waveform_file_path)`

#### `def niDigital_WriteSourceWaveformSiteUniqueU32(self, vi, site_list, waveform_name, num_waveforms, samples_per_waveform, waveform_data)`

#### `def niDigital_WriteStatic(self, vi, channel_list, state)`

#### `def niDigital_close(self, vi)`

#### `def niDigital_error_message(self, vi, error_code, error_message)`

#### `def niDigital_reset(self, vi)`

#### `def niDigital_self_test(self, vi, test_result, test_message)`

#### `def set_side_effects_and_return_values(self, mock_library)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nidigital/nidigital/unit_tests/test_nidigital.py -->
## PYTHON MODULE: generated/nidigital/nidigital/unit_tests/test_nidigital.py

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

<!--NI_PYTHON_API repo=nimi-python path=generated/nidigital/setup.py -->
## PYTHON MODULE: generated/nidigital/setup.py

### `def read_contents(file_to_read)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nidmm/nidmm/__init__.py -->
## PYTHON MODULE: generated/nidmm/nidmm/__init__.py

### `def get_diagnostic_information()`

Get diagnostic information about the system state that is suitable for printing or logging

    returns: dict

    note: Python bitness may be incorrect when running in a virtual environment
    

### `def print_diagnostic_information()`

Print diagnostic information in a format suitable for issue report

    note: Python bitness may be incorrect when running in a virtual environment
    

<!--NI_PYTHON_API repo=nimi-python path=generated/nidmm/nidmm/_attributes.py -->
## PYTHON MODULE: generated/nidmm/nidmm/_attributes.py

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

Class for attributes that use enums internally but are exposed in the nidmm Python module as something else, thus need conversion.

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

<!--NI_PYTHON_API repo=nimi-python path=generated/nidmm/nidmm/_converters.py -->
## PYTHON MODULE: generated/nidmm/nidmm/_converters.py

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
    

<!--NI_PYTHON_API repo=nimi-python path=generated/nidmm/nidmm/_grpc_stub_interpreter.py -->
## PYTHON MODULE: generated/nidmm/nidmm/_grpc_stub_interpreter.py

### `class GrpcStubInterpreter(object)`

Interpreter for interacting with a gRPC Stub class

#### `def __init__(self, grpc_options)`

#### `def set_session_handle(self, value=session_grpc_types.Session())`

#### `def get_session_handle(self)`

#### `def _invoke(self, func, request, metadata=None)`

#### `def abort(self)`

#### `def configure_measurement_absolute(self, measurement_function, range, resolution_absolute)`

#### `def configure_measurement_digits(self, measurement_function, range, resolution_digits)`

#### `def configure_multi_point(self, trigger_count, sample_count, sample_trigger, sample_interval)`

#### `def configure_rtd_custom(self, rtd_a, rtd_b, rtd_c)`

#### `def configure_rtd_type(self, rtd_type, rtd_resistance)`

#### `def configure_thermistor_custom(self, thermistor_a, thermistor_b, thermistor_c)`

#### `def configure_thermocouple(self, thermocouple_type, reference_junction_type)`

#### `def configure_trigger(self, trigger_source, trigger_delay)`

#### `def configure_waveform_acquisition(self, measurement_function, range, rate, waveform_points)`

#### `def disable(self)`

#### `def export_attribute_configuration_buffer(self)`

#### `def export_attribute_configuration_file(self, file_path)`

#### `def fetch(self, maximum_time)`

#### `def fetch_multi_point(self, maximum_time, array_size)`

#### `def fetch_waveform(self, maximum_time, array_size)`

#### `def fetch_waveform_into(self, maximum_time, array_size)`

#### `def get_attribute_vi_boolean(self, channel_name, attribute_id)`

#### `def get_attribute_vi_int32(self, channel_name, attribute_id)`

#### `def get_attribute_vi_real64(self, channel_name, attribute_id)`

#### `def get_attribute_vi_string(self, channel_name, attribute_id)`

#### `def get_cal_date_and_time(self, cal_type)`

#### `def get_dev_temp(self, options)`

#### `def get_error(self)`

#### `def get_ext_cal_recommended_interval(self)`

#### `def get_last_cal_temp(self, cal_type)`

#### `def get_self_cal_supported(self)`

#### `def import_attribute_configuration_buffer(self, configuration)`

#### `def import_attribute_configuration_file(self, file_path)`

#### `def init_with_options(self, resource_name, id_query, reset_device, option_string)`

#### `def initiate(self)`

#### `def lock(self)`

#### `def perform_open_cable_comp(self)`

#### `def perform_short_cable_comp(self)`

#### `def read(self, maximum_time)`

#### `def read_multi_point(self, maximum_time, array_size)`

#### `def read_status(self)`

#### `def read_waveform(self, maximum_time, array_size)`

#### `def reset_with_defaults(self)`

#### `def self_cal(self)`

#### `def send_software_trigger(self)`

#### `def set_attribute_vi_boolean(self, channel_name, attribute_id, attribute_value)`

#### `def set_attribute_vi_int32(self, channel_name, attribute_id, attribute_value)`

#### `def set_attribute_vi_real64(self, channel_name, attribute_id, attribute_value)`

#### `def set_attribute_vi_string(self, channel_name, attribute_id, attribute_value)`

#### `def set_runtime_environment(self, environment, environment_version, reserved1, reserved2)`

#### `def unlock(self)`

#### `def close(self)`

#### `def error_message(self, error_code)`

#### `def reset(self)`

#### `def self_test(self)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nidmm/nidmm/_library.py -->
## PYTHON MODULE: generated/nidmm/nidmm/_library.py

### `class Library(object)`

Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    

#### `def __init__(self, ctypes_library)`

#### `def _get_library_function(self, name)`

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

<!--NI_PYTHON_API repo=nimi-python path=generated/nidmm/nidmm/_library_interpreter.py -->
## PYTHON MODULE: generated/nidmm/nidmm/_library_interpreter.py

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

#### `def configure_measurement_absolute(self, measurement_function, range, resolution_absolute)`

#### `def configure_measurement_digits(self, measurement_function, range, resolution_digits)`

#### `def configure_multi_point(self, trigger_count, sample_count, sample_trigger, sample_interval)`

#### `def configure_rtd_custom(self, rtd_a, rtd_b, rtd_c)`

#### `def configure_rtd_type(self, rtd_type, rtd_resistance)`

#### `def configure_thermistor_custom(self, thermistor_a, thermistor_b, thermistor_c)`

#### `def configure_thermocouple(self, thermocouple_type, reference_junction_type)`

#### `def configure_trigger(self, trigger_source, trigger_delay)`

#### `def configure_waveform_acquisition(self, measurement_function, range, rate, waveform_points)`

#### `def disable(self)`

#### `def export_attribute_configuration_buffer(self)`

#### `def export_attribute_configuration_file(self, file_path)`

#### `def fetch(self, maximum_time)`

#### `def fetch_multi_point(self, maximum_time, array_size)`

#### `def fetch_waveform(self, maximum_time, array_size)`

#### `def fetch_waveform_into(self, waveform_array, maximum_time)`

#### `def get_attribute_vi_boolean(self, channel_name, attribute_id)`

#### `def get_attribute_vi_int32(self, channel_name, attribute_id)`

#### `def get_attribute_vi_real64(self, channel_name, attribute_id)`

#### `def get_attribute_vi_string(self, channel_name, attribute_id)`

#### `def get_cal_date_and_time(self, cal_type)`

#### `def get_dev_temp(self, options)`

#### `def get_error(self)`

#### `def get_ext_cal_recommended_interval(self)`

#### `def get_last_cal_temp(self, cal_type)`

#### `def get_self_cal_supported(self)`

#### `def import_attribute_configuration_buffer(self, configuration)`

#### `def import_attribute_configuration_file(self, file_path)`

#### `def init_with_options(self, resource_name, id_query, reset_device, option_string)`

#### `def initiate(self)`

#### `def lock(self)`

#### `def perform_open_cable_comp(self)`

#### `def perform_short_cable_comp(self)`

#### `def read(self, maximum_time)`

#### `def read_multi_point(self, maximum_time, array_size)`

#### `def read_status(self)`

#### `def read_waveform(self, maximum_time, array_size)`

#### `def reset_with_defaults(self)`

#### `def self_cal(self)`

#### `def send_software_trigger(self)`

#### `def set_attribute_vi_boolean(self, channel_name, attribute_id, attribute_value)`

#### `def set_attribute_vi_int32(self, channel_name, attribute_id, attribute_value)`

#### `def set_attribute_vi_real64(self, channel_name, attribute_id, attribute_value)`

#### `def set_attribute_vi_string(self, channel_name, attribute_id, attribute_value)`

#### `def set_runtime_environment(self, environment, environment_version, reserved1, reserved2)`

#### `def unlock(self)`

#### `def close(self)`

#### `def error_message(self, error_code)`

#### `def reset(self)`

#### `def self_test(self)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nidmm/nidmm/_library_singleton.py -->
## PYTHON MODULE: generated/nidmm/nidmm/_library_singleton.py

### `def _get_library_name()`

### `def _get_library_type()`

### `def get()`

get

    Returns the library.Library singleton for nidmm.
    

<!--NI_PYTHON_API repo=nimi-python path=generated/nidmm/nidmm/enums.py -->
## PYTHON MODULE: generated/nidmm/nidmm/enums.py

### `class ADCCalibration(Enum)`

### `class AcquisitionStatus(Enum)`

### `class ApertureTimeUnits(Enum)`

### `class AutoZero(Enum)`

### `class CableCompensationType(Enum)`

### `class DCNoiseRejection(Enum)`

### `class Function(Enum)`

### `class LCCalculationModel(Enum)`

### `class MeasurementCompleteDest(Enum)`

### `class OperationMode(Enum)`

### `class RTDType(Enum)`

### `class SampleTrigger(Enum)`

### `class ThermistorType(Enum)`

### `class ThermocoupleReferenceJunctionType(Enum)`

### `class ThermocoupleType(Enum)`

### `class TransducerType(Enum)`

### `class TriggerSource(Enum)`

### `class WaveformCoupling(Enum)`

<!--NI_PYTHON_API repo=nimi-python path=generated/nidmm/nidmm/errors.py -->
## PYTHON MODULE: generated/nidmm/nidmm/errors.py

### `def _is_success(code)`

### `def _is_error(code)`

### `def _is_warning(code)`

### `class Error(Exception)`

Base error class for NI-DMM

#### `def __init__(self, message)`

### `class DriverError(Error)`

An error originating from the NI-DMM driver

#### `def __init__(self, code, description)`

### `class DriverWarning(Warning)`

A warning originating from the NI-DMM driver

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

An error due to using this module with an older version of the NI-DMM driver runtime.

#### `def __init__(self)`

### `class DriverTooNewError(Error)`

An error due to the NI-DMM driver runtime being too new for this module.

#### `def __init__(self)`

### `class InvalidRepeatedCapabilityError(Error)`

An error due to an invalid character in a repeated capability

#### `def __init__(self, invalid_character, invalid_string)`

### `class SelfTestError(Error)`

An error due to a failed self-test

#### `def __init__(self, code, msg)`

### `def handle_error(library_interpreter, code, ignore_warnings, is_error_handling)`

handle_error

    Helper function for handling errors returned by nidmm.Library.
    It calls back into the LibraryInterpreter to get the corresponding error
    description and raises if necessary.
    

<!--NI_PYTHON_API repo=nimi-python path=generated/nidmm/nidmm/grpc_session_options.py -->
## PYTHON MODULE: generated/nidmm/nidmm/grpc_session_options.py

- `GRPC_SERVICE_INTERFACE_NAME = 'nidmm_grpc.NiDmm'`

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
        

<!--NI_PYTHON_API repo=nimi-python path=generated/nidmm/nidmm/nidevice_pb2.py -->
## PYTHON MODULE: generated/nidmm/nidmm/nidevice_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0enidevice.proto\x12\rnidevice_grpc"2\n\x0fNIComplexNumber\x12\x0c\n\x04real\x18\x01 \x01(\x01\x12\x11\n\timaginary\x18\x02 \x01(\x01"5\n\x12NIComplexNumberF32\x12\x0c\n\x04real\x18\x01 \x01(\x02\x12\x11\n\timaginary\x18\x02 \x01(\x02"/\n\x0cNIComplexI16\x12\x0c\n\x04real\x18\x01 \x01(\x11\x12\x11\n\timaginary\x18\x02 \x01(\x11"r\n\x0fSmtSpectrumInfo\x12\x15\n\rspectrum_type\x18\x01 \x01(\r\x12\x11\n\tlinear_db\x18\x02 \x01(\r\x12\x0e\n\x06window\x18\x03 \x01(\r\x12\x13\n\x0bwindow_size\x18\x04 \x01(\x11\x12\x10\n\x08fft_size\x18\x05 \x01(\x11BB\n\x12com.ni.grpc.deviceB\x08NiDeviceP\x01\xaa\x02\x1fNationalInstruments.Grpc.Deviceb\x06proto3')`

<!--NI_PYTHON_API repo=nimi-python path=generated/nidmm/nidmm/nidevice_pb2_grpc.py -->
## PYTHON MODULE: generated/nidmm/nidmm/nidevice_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

<!--NI_PYTHON_API repo=nimi-python path=generated/nidmm/nidmm/nidmm_pb2.py -->
## PYTHON MODULE: generated/nidmm/nidmm/nidmm_pb2.py

### MODULE DOCSTRING

Generated protocol buffer code.

- `DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bnidmm.proto\x12\nnidmm_grpc\x1a\rsession.proto"\xb1\x01\n\x0bInitRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\x10\n\x08id_query\x18\x03 \x01(\x08\x12\x14\n\x0creset_device\x18\x04 \x01(\x08\x12M\n\x17initialization_behavior\x18\x05 \x01(\x0e2,.nidevice_grpc.SessionInitializationBehavior"~\n\x0cInitResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12"\n\x02vi\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x19\n\rerror_message\x18\x03 \x01(\tB\x02\x18\x01\x12\x1f\n\x17new_session_initialized\x18\x04 \x01(\x08"\xd3\x01\n\x16InitWithOptionsRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\x10\n\x08id_query\x18\x03 \x01(\x08\x12\x14\n\x0creset_device\x18\x04 \x01(\x08\x12\x15\n\roption_string\x18\x05 \x01(\t\x12M\n\x17initialization_behavior\x18\x06 \x01(\x0e2,.nidevice_grpc.SessionInitializationBehavior"\x89\x01\n\x17InitWithOptionsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12"\n\x02vi\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x19\n\rerror_message\x18\x03 \x01(\tB\x02\x18\x01\x12\x1f\n\x17new_session_initialized\x18\x04 \x01(\x08"2\n\x0cCloseRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\x1f\n\rCloseResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"5\n\x0fGetErrorRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"K\n\x10GetErrorResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nerror_code\x18\x02 \x01(\x11\x12\x13\n\x0bdescription\x18\x03 \x01(\t"P\n\x16GetErrorMessageRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x12\n\nerror_code\x18\x02 \x01(\x11"@\n\x17GetErrorMessageResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rerror_message\x18\x02 \x01(\t"7\n\x11ClearErrorRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"$\n\x12ClearErrorResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"2\n\x0cResetRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\x1f\n\rResetResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"5\n\x0fSelfTestRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"W\n\x10SelfTestResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x18\n\x10self_test_result\x18\x02 \x01(\x11\x12\x19\n\x11self_test_message\x18\x03 \x01(\t"4\n\x0eSelfCalRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"!\n\x0fSelfCalResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05":\n\x14RevisionQueryRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"f\n\x15RevisionQueryResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12"\n\x1ainstrument_driver_revision\x18\x02 \x01(\t\x12\x19\n\x11firmware_revision\x18\x03 \x01(\t">\n\x18ResetWithDefaultsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"+\n\x19ResetWithDefaultsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"4\n\x0eDisableRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"!\n\x0fDisableResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"A\n\x1bGetMeasurementPeriodRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session">\n\x1cGetMeasurementPeriodResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0e\n\x06period\x18\x02 \x01(\x01"\x8e\x02\n\x17ConfigureTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x123\n\x0etrigger_source\x18\x02 \x01(\x0e2\x19.nidmm_grpc.TriggerSourceH\x00\x12\x1c\n\x12trigger_source_raw\x18\x03 \x01(\x11H\x00\x122\n\rtrigger_delay\x18\x04 \x01(\x0e2\x19.nidmm_grpc.TriggerDelaysH\x01\x12\x1b\n\x11trigger_delay_raw\x18\x05 \x01(\x01H\x01B\x15\n\x13trigger_source_enumB\x14\n\x12trigger_delay_enum"*\n\x18ConfigureTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x91\x01\n\x0bReadRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12-\n\x0cmaximum_time\x18\x02 \x01(\x0e2\x15.nidmm_grpc.TimeLimitH\x00\x12\x1a\n\x10maximum_time_raw\x18\x03 \x01(\x11H\x00B\x13\n\x11maximum_time_enum"/\n\x0cReadResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07reading\x18\x02 \x01(\x01"\x92\x01\n\x0cFetchRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12-\n\x0cmaximum_time\x18\x02 \x01(\x0e2\x15.nidmm_grpc.TimeLimitH\x00\x12\x1a\n\x10maximum_time_raw\x18\x03 \x01(\x11H\x00B\x13\n\x11maximum_time_enum"0\n\rFetchResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07reading\x18\x02 \x01(\x01"2\n\x0cAbortRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\x1f\n\rAbortResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"5\n\x0fInitiateRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session""\n\x10InitiateResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"S\n\x12IsOverRangeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x19\n\x11measurement_value\x18\x02 \x01(\x01"<\n\x13IsOverRangeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\ris_over_range\x18\x02 \x01(\x08"T\n\x13IsUnderRangeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x19\n\x11measurement_value\x18\x02 \x01(\x01">\n\x14IsUnderRangeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x16\n\x0eis_under_range\x18\x02 \x01(\x08"\x83\x01\n\x1bConfigureACBandwidthRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1f\n\x17ac_minimum_frequency_hz\x18\x02 \x01(\x01\x12\x1f\n\x17ac_maximum_frequency_hz\x18\x03 \x01(\x01".\n\x1cConfigureACBandwidthResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xba\x01\n%ConfigureFrequencyVoltageRangeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12:\n\rvoltage_range\x18\x02 \x01(\x0e2!.nidmm_grpc.FrequencyVoltageRangeH\x00\x12\x1b\n\x11voltage_range_raw\x18\x03 \x01(\x01H\x00B\x14\n\x12voltage_range_enum"8\n&ConfigureFrequencyVoltageRangeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"i\n ConfigureMeasCompleteDestRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12!\n\x19meas_complete_destination\x18\x02 \x01(\x11"3\n!ConfigureMeasCompleteDestResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xe0\x03\n\x1aConfigureMultiPointRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x121\n\rtrigger_count\x18\x02 \x01(\x0e2\x18.nidmm_grpc.TriggerCountH\x00\x12\x1b\n\x11trigger_count_raw\x18\x03 \x01(\x11H\x00\x12/\n\x0csample_count\x18\x04 \x01(\x0e2\x17.nidmm_grpc.SampleCountH\x01\x12\x1a\n\x10sample_count_raw\x18\x05 \x01(\x11H\x01\x123\n\x0esample_trigger\x18\x06 \x01(\x0e2\x19.nidmm_grpc.SampleTriggerH\x02\x12\x1c\n\x12sample_trigger_raw\x18\x07 \x01(\x11H\x02\x125\n\x0fsample_interval\x18\x08 \x01(\x0e2\x1a.nidmm_grpc.SampleIntervalH\x03\x12\x1d\n\x13sample_interval_raw\x18\t \x01(\x01H\x03B\x14\n\x12trigger_count_enumB\x13\n\x11sample_count_enumB\x15\n\x13sample_trigger_enumB\x16\n\x14sample_interval_enum"-\n\x1bConfigureMultiPointResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xaf\x01\n\x15ReadMultiPointRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12-\n\x0cmaximum_time\x18\x02 \x01(\x0e2\x15.nidmm_grpc.TimeLimitH\x00\x12\x1a\n\x10maximum_time_raw\x18\x03 \x01(\x11H\x00\x12\x12\n\narray_size\x18\x04 \x01(\x11B\x13\n\x11maximum_time_enum"`\n\x16ReadMultiPointResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rreading_array\x18\x02 \x03(\x01\x12\x1f\n\x17actual_number_of_points\x18\x03 \x01(\x11"\xb0\x01\n\x16FetchMultiPointRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12-\n\x0cmaximum_time\x18\x02 \x01(\x0e2\x15.nidmm_grpc.TimeLimitH\x00\x12\x1a\n\x10maximum_time_raw\x18\x03 \x01(\x11H\x00\x12\x12\n\narray_size\x18\x04 \x01(\x11B\x13\n\x11maximum_time_enum"a\n\x17FetchMultiPointResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rreading_array\x18\x02 \x03(\x01\x12\x1f\n\x17actual_number_of_points\x18\x03 \x01(\x11"\xa8\x01\n\x1cConfigureTriggerSlopeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x121\n\rtrigger_slope\x18\x02 \x01(\x0e2\x18.nidmm_grpc.TriggerSlopeH\x00\x12\x1b\n\x11trigger_slope_raw\x18\x03 \x01(\x11H\x00B\x14\n\x12trigger_slope_enum"/\n\x1dConfigureTriggerSlopeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"@\n\x1aSendSoftwareTriggerRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"-\n\x1bSendSoftwareTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"@\n\x1aGetApertureTimeInfoRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\xd6\x01\n\x1bGetApertureTimeInfoResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12/\n\raperture_time\x18\x02 \x01(\x0e2\x18.nidmm_grpc.ApertureTime\x12\x19\n\x11aperture_time_raw\x18\x03 \x01(\x01\x12:\n\x13aperture_time_units\x18\x04 \x01(\x0e2\x1d.nidmm_grpc.ApertureTimeUnits\x12\x1f\n\x17aperture_time_units_raw\x18\x05 \x01(\x11">\n\x18GetAutoRangeValueRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"A\n\x19GetAutoRangeValueResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x14\n\x0cactual_range\x18\x02 \x01(\x01"Z\n\x1cConfigureAutoZeroModeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x16\n\x0eauto_zero_mode\x18\x02 \x01(\x11"/\n\x1dConfigureAutoZeroModeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xd4\x01\n"ConfigurePowerLineFrequencyRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12C\n\x17power_line_frequency_hz\x18\x02 \x01(\x0e2 .nidmm_grpc.PowerLineFrequenciesH\x00\x12%\n\x1bpower_line_frequency_hz_raw\x18\x03 \x01(\x01H\x00B\x1e\n\x1cpower_line_frequency_hz_enum"5\n#ConfigurePowerLineFrequencyResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xe8\x01\n!ConfigureMeasurementDigitsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x124\n\x14measurement_function\x18\x02 \x01(\x0e2\x14.nidmm_grpc.FunctionH\x00\x12"\n\x18measurement_function_raw\x18\x03 \x01(\x11H\x00\x12\r\n\x05range\x18\x04 \x01(\x01\x12\x19\n\x11resolution_digits\x18\x05 \x01(\x01B\x1b\n\x19measurement_function_enum"4\n"ConfigureMeasurementDigitsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xec\x01\n#ConfigureMeasurementAbsoluteRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x124\n\x14measurement_function\x18\x02 \x01(\x0e2\x14.nidmm_grpc.FunctionH\x00\x12"\n\x18measurement_function_raw\x18\x03 \x01(\x11H\x00\x12\r\n\x05range\x18\x04 \x01(\x01\x12\x1b\n\x13resolution_absolute\x18\x05 \x01(\x01B\x1b\n\x19measurement_function_enum"6\n$ConfigureMeasurementAbsoluteResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"d\n!ConfigureMeasCompleteSlopeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x1b\n\x13meas_complete_slope\x18\x02 \x01(\x11"4\n"ConfigureMeasCompleteSlopeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xc6\x01\n"ConfigureSampleTriggerSlopeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12;\n\x14sample_trigger_slope\x18\x02 \x01(\x0e2\x1b.nidmm_grpc.SampleTrigSlopeH\x00\x12"\n\x18sample_trigger_slope_raw\x18\x03 \x01(\x11H\x00B\x1b\n\x19sample_trigger_slope_enum"5\n#ConfigureSampleTriggerSlopeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"7\n\x11ReadStatusRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"\x9c\x01\n\x12ReadStatusResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1b\n\x13acquisition_backlog\x18\x02 \x01(\x11\x129\n\x12acquisition_status\x18\x03 \x01(\x0e2\x1d.nidmm_grpc.AcquisitionStatus\x12\x1e\n\x16acquisition_status_raw\x18\x04 \x01(\x11"\x9e\x01\n\x0eControlRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x123\n\x0econtrol_action\x18\x02 \x01(\x0e2\x19.nidmm_grpc.ControlCommitH\x00\x12\x1c\n\x12control_action_raw\x18\x03 \x01(\x11H\x00B\x15\n\x13control_action_enum"!\n\x0fControlResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"]\n\x1eConfigureADCCalibrationRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x17\n\x0fadc_calibration\x18\x02 \x01(\x11"1\n\x1fConfigureADCCalibrationResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xb6\x01\n\x1eConfigureOffsetCompOhmsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x127\n\x10offset_comp_ohms\x18\x02 \x01(\x0e2\x1b.nidmm_grpc.CompensatedOhmsH\x00\x12\x1e\n\x14offset_comp_ohms_raw\x18\x03 \x01(\x11H\x00B\x17\n\x15offset_comp_ohms_enum"1\n\x1fConfigureOffsetCompOhmsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"[\n\x1dConfigureCurrentSourceRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x16\n\x0ecurrent_source\x18\x02 \x01(\x01"0\n\x1eConfigureCurrentSourceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\\\n\x1dConfigureCableCompTypeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x17\n\x0fcable_comp_type\x18\x02 \x01(\x11"0\n\x1eConfigureCableCompTypeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"A\n\x1bPerformOpenCableCompRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"X\n\x1cPerformOpenCableCompResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0bconductance\x18\x02 \x01(\x01\x12\x13\n\x0bsusceptance\x18\x03 \x01(\x01"B\n\x1cPerformShortCableCompRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"V\n\x1dPerformShortCableCompResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nresistance\x18\x02 \x01(\x01\x12\x11\n\treactance\x18\x03 \x01(\x01"s\n#ConfigureOpenCableCompValuesRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x13\n\x0bconductance\x18\x02 \x01(\x01\x12\x13\n\x0bsusceptance\x18\x03 \x01(\x01"6\n$ConfigureOpenCableCompValuesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"q\n$ConfigureShortCableCompValuesRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x12\n\nresistance\x18\x02 \x01(\x01\x12\x11\n\treactance\x18\x03 \x01(\x01"7\n%ConfigureShortCableCompValuesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xf6\x01\n#ConfigureWaveformAcquisitionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x124\n\x14measurement_function\x18\x02 \x01(\x0e2\x14.nidmm_grpc.FunctionH\x00\x12"\n\x18measurement_function_raw\x18\x03 \x01(\x11H\x00\x12\r\n\x05range\x18\x04 \x01(\x01\x12\x0c\n\x04rate\x18\x05 \x01(\x01\x12\x17\n\x0fwaveform_points\x18\x06 \x01(\x11B\x1b\n\x19measurement_function_enum"6\n$ConfigureWaveformAcquisitionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"a\n ConfigureWaveformCouplingRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x19\n\x11waveform_coupling\x18\x02 \x01(\x11"3\n!ConfigureWaveformCouplingResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xae\x01\n\x14FetchWaveformRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12-\n\x0cmaximum_time\x18\x02 \x01(\x0e2\x15.nidmm_grpc.TimeLimitH\x00\x12\x1a\n\x10maximum_time_raw\x18\x03 \x01(\x11H\x00\x12\x12\n\narray_size\x18\x04 \x01(\x11B\x13\n\x11maximum_time_enum"`\n\x15FetchWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x16\n\x0ewaveform_array\x18\x02 \x03(\x01\x12\x1f\n\x17actual_number_of_points\x18\x03 \x01(\x11"\xad\x01\n\x13ReadWaveformRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12-\n\x0cmaximum_time\x18\x02 \x01(\x0e2\x15.nidmm_grpc.TimeLimitH\x00\x12\x1a\n\x10maximum_time_raw\x18\x03 \x01(\x11H\x00\x12\x12\n\narray_size\x18\x04 \x01(\x11B\x13\n\x11maximum_time_enum"_\n\x14ReadWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x16\n\x0ewaveform_array\x18\x02 \x03(\x01\x12\x1f\n\x17actual_number_of_points\x18\x03 \x01(\x11"\x88\x01\n\x1aGetAttributeViInt32Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x120\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1a.nidmm_grpc.NiDmmAttribute"F\n\x1bGetAttributeViInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fattribute_value\x18\x02 \x01(\x11"\x81\x02\n\x1aSetAttributeViInt32Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x120\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1a.nidmm_grpc.NiDmmAttribute\x12@\n\x0fattribute_value\x18\x04 \x01(\x0e2%.nidmm_grpc.NiDmmInt32AttributeValuesH\x00\x12\x1d\n\x13attribute_value_raw\x18\x05 \x01(\x11H\x00B\x16\n\x14attribute_value_enum"-\n\x1bSetAttributeViInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x83\x02\n\x1cCheckAttributeViInt32Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x120\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1a.nidmm_grpc.NiDmmAttribute\x12@\n\x0fattribute_value\x18\x04 \x01(\x0e2%.nidmm_grpc.NiDmmInt32AttributeValuesH\x00\x12\x1d\n\x13attribute_value_raw\x18\x05 \x01(\x11H\x00B\x16\n\x14attribute_value_enum"/\n\x1dCheckAttributeViInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x89\x01\n\x1bGetAttributeViReal64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x120\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1a.nidmm_grpc.NiDmmAttribute"G\n\x1cGetAttributeViReal64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fattribute_value\x18\x02 \x01(\x01"\xd3\x02\n\x1bSetAttributeViReal64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x120\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1a.nidmm_grpc.NiDmmAttribute\x12A\n\x0fattribute_value\x18\x04 \x01(\x0e2&.nidmm_grpc.NiDmmReal64AttributeValuesH\x00\x12\x1d\n\x13attribute_value_raw\x18\x05 \x01(\x01H\x00\x12N\n\x16attribute_value_mapped\x18\x06 \x01(\x0e2,.nidmm_grpc.NiDmmReal64AttributeValuesMappedH\x00B\x16\n\x14attribute_value_enum".\n\x1cSetAttributeViReal64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xd5\x02\n\x1dCheckAttributeViReal64Request\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x120\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1a.nidmm_grpc.NiDmmAttribute\x12A\n\x0fattribute_value\x18\x04 \x01(\x0e2&.nidmm_grpc.NiDmmReal64AttributeValuesH\x00\x12\x1d\n\x13attribute_value_raw\x18\x05 \x01(\x01H\x00\x12N\n\x16attribute_value_mapped\x18\x06 \x01(\x0e2,.nidmm_grpc.NiDmmReal64AttributeValuesMappedH\x00B\x16\n\x14attribute_value_enum"0\n\x1eCheckAttributeViReal64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x89\x01\n\x1bGetAttributeViStringRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x120\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1a.nidmm_grpc.NiDmmAttribute"G\n\x1cGetAttributeViStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fattribute_value\x18\x02 \x01(\t"\xa6\x01\n\x1bSetAttributeViStringRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x120\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1a.nidmm_grpc.NiDmmAttribute\x12\x1b\n\x13attribute_value_raw\x18\x04 \x01(\t".\n\x1cSetAttributeViStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa8\x01\n\x1dCheckAttributeViStringRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x120\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1a.nidmm_grpc.NiDmmAttribute\x12\x1b\n\x13attribute_value_raw\x18\x04 \x01(\t"0\n\x1eCheckAttributeViStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x8a\x01\n\x1cGetAttributeViSessionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x120\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1a.nidmm_grpc.NiDmmAttribute"`\n\x1dGetAttributeViSessionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12/\n\x0fattribute_value\x18\x02 \x01(\x0b2\x16.nidevice_grpc.Session"\xbb\x01\n\x1cSetAttributeViSessionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x120\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1a.nidmm_grpc.NiDmmAttribute\x12/\n\x0fattribute_value\x18\x04 \x01(\x0b2\x16.nidevice_grpc.Session"/\n\x1dSetAttributeViSessionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xbd\x01\n\x1eCheckAttributeViSessionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x120\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1a.nidmm_grpc.NiDmmAttribute\x12/\n\x0fattribute_value\x18\x04 \x01(\x0b2\x16.nidevice_grpc.Session"1\n\x1fCheckAttributeViSessionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x8a\x01\n\x1cGetAttributeViBooleanRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x120\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1a.nidmm_grpc.NiDmmAttribute"H\n\x1dGetAttributeViBooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fattribute_value\x18\x02 \x01(\x08"\xa3\x01\n\x1cSetAttributeViBooleanRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x120\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1a.nidmm_grpc.NiDmmAttribute\x12\x17\n\x0fattribute_value\x18\x04 \x01(\x08"/\n\x1dSetAttributeViBooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa5\x01\n\x1eCheckAttributeViBooleanRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cchannel_name\x18\x02 \x01(\t\x120\n\x0cattribute_id\x18\x03 \x01(\x0e2\x1a.nidmm_grpc.NiDmmAttribute\x12\x17\n\x0fattribute_value\x18\x04 \x01(\x08"1\n\x1fCheckAttributeViBooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"`\n\'ImportAttributeConfigurationFileRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tfile_path\x18\x02 \x01(\t":\n(ImportAttributeConfigurationFileResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"`\n\'ExportAttributeConfigurationFileRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x11\n\tfile_path\x18\x02 \x01(\t":\n(ExportAttributeConfigurationFileResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"f\n)ImportAttributeConfigurationBufferRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x15\n\rconfiguration\x18\x02 \x01(\x0c"<\n*ImportAttributeConfigurationBufferResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"O\n)ExportAttributeConfigurationBufferRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"S\n*ExportAttributeConfigurationBufferResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rconfiguration\x18\x02 \x01(\x0c"B\n\x1cResetInterchangeCheckRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"/\n\x1dResetInterchangeCheckResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"E\n\x1fClearInterchangeWarningsRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"2\n ClearInterchangeWarningsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"J\n\x15GetChannelNameRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\r\n\x05index\x18\x02 \x01(\x11"@\n\x16GetChannelNameResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x16\n\x0echannel_string\x18\x02 \x01(\t"I\n#GetExtCalRecommendedIntervalRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"F\n$GetExtCalRecommendedIntervalResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0e\n\x06months\x18\x02 \x01(\x11"@\n\x1aGetSelfCalSupportedRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"I\n\x1bGetSelfCalSupportedResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1a\n\x12self_cal_supported\x18\x02 \x01(\x08"\x98\x01\n\x18GetCalDateAndTimeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12/\n\x08cal_type\x18\x02 \x01(\x0e2\x1b.nidmm_grpc.CalibrationTypeH\x00\x12\x16\n\x0ccal_type_raw\x18\x03 \x01(\x11H\x00B\x0f\n\rcal_type_enum"s\n\x19GetCalDateAndTimeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\r\n\x05month\x18\x02 \x01(\x11\x12\x0b\n\x03day\x18\x03 \x01(\x11\x12\x0c\n\x04year\x18\x04 \x01(\x11\x12\x0c\n\x04hour\x18\x05 \x01(\x11\x12\x0e\n\x06minute\x18\x06 \x01(\x11"\x95\x01\n\x15GetLastCalTempRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12/\n\x08cal_type\x18\x02 \x01(\x0e2\x1b.nidmm_grpc.CalibrationTypeH\x00\x12\x16\n\x0ccal_type_raw\x18\x03 \x01(\x11H\x00B\x0f\n\rcal_type_enum"=\n\x16GetLastCalTempResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0btemperature\x18\x02 \x01(\x01"H\n\x11GetDevTempRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x0f\n\x07options\x18\x02 \x01(\t"9\n\x12GetDevTempResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0btemperature\x18\x02 \x01(\x01"]\n\x1eConfigureTransducerTypeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x17\n\x0ftransducer_type\x18\x02 \x01(\x11"1\n\x1fConfigureTransducerTypeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xd1\x02\n\x1cConfigureThermocoupleRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x129\n\x11thermocouple_type\x18\x02 \x01(\x0e2\x1c.nidmm_grpc.ThermocoupleTypeH\x00\x12\x1f\n\x15thermocouple_type_raw\x18\x03 \x01(\x11H\x00\x12P\n\x17reference_junction_type\x18\x04 \x01(\x0e2-.nidmm_grpc.ThermocoupleReferenceJunctionTypeH\x01\x12%\n\x1breference_junction_type_raw\x18\x05 \x01(\x11H\x01B\x18\n\x16thermocouple_type_enumB\x1e\n\x1creference_junction_type_enum"/\n\x1dConfigureThermocoupleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"h\n ConfigureFixedRefJunctionRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12 \n\x18fixed_reference_junction\x18\x02 \x01(\x01"3\n!ConfigureFixedRefJunctionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\xa7\x01\n\x17ConfigureRTDTypeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\'\n\x08rtd_type\x18\x02 \x01(\x0e2\x13.nidmm_grpc.RtdTypeH\x00\x12\x16\n\x0crtd_type_raw\x18\x03 \x01(\x11H\x00\x12\x16\n\x0ertd_resistance\x18\x04 \x01(\x01B\x0f\n\rrtd_type_enum"*\n\x18ConfigureRTDTypeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"l\n\x19ConfigureRTDCustomRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\r\n\x05rtd_a\x18\x02 \x01(\x01\x12\r\n\x05rtd_b\x18\x03 \x01(\x01\x12\r\n\x05rtd_c\x18\x04 \x01(\x01",\n\x1aConfigureRTDCustomResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"]\n\x1eConfigureThermistorTypeRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x17\n\x0fthermistor_type\x18\x02 \x01(\x11"1\n\x1fConfigureThermistorTypeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"\x88\x01\n ConfigureThermistorCustomRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session\x12\x14\n\x0cthermistor_a\x18\x02 \x01(\x01\x12\x14\n\x0cthermistor_b\x18\x03 \x01(\x01\x12\x14\n\x0cthermistor_c\x18\x04 \x01(\x01"3\n!ConfigureThermistorCustomResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05"D\n\x1eInvalidateAllAttributesRequest\x12"\n\x02vi\x18\x01 \x01(\x0b2\x16.nidevice_grpc.Session"1\n\x1fInvalidateAllAttributesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05*\x8a\x1b\n\x0eNiDmmAttribute\x12\x1f\n\x1bNIDMM_ATTRIBUTE_UNSPECIFIED\x10\x00\x12!\n\x1bNIDMM_ATTRIBUTE_RANGE_CHECK\x10\x92\x8b@\x12-\n\'NIDMM_ATTRIBUTE_QUERY_INSTRUMENT_STATUS\x10\x93\x8b@\x12\x1b\n\x15NIDMM_ATTRIBUTE_CACHE\x10\x94\x8b@\x12\x1e\n\x18NIDMM_ATTRIBUTE_SIMULATE\x10\x95\x8b@\x12&\n NIDMM_ATTRIBUTE_RECORD_COERCIONS\x10\x96\x8b@\x12\'\n!NIDMM_ATTRIBUTE_INTERCHANGE_CHECK\x10\xa5\x8b@\x12>\n8NIDMM_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION\x10\x93\x8f@\x12>\n8NIDMM_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION\x10\x94\x8f@\x121\n+NIDMM_ATTRIBUTE_SPECIFIC_DRIVER_DESCRIPTION\x10\x92\x8f@\x12,\n&NIDMM_ATTRIBUTE_SPECIFIC_DRIVER_PREFIX\x10\xbe\x8d@\x12,\n&NIDMM_ATTRIBUTE_SPECIFIC_DRIVER_VENDOR\x10\x91\x8f@\x12.\n(NIDMM_ATTRIBUTE_SPECIFIC_DRIVER_REVISION\x10\xb7\x8f@\x12#\n\x1dNIDMM_ATTRIBUTE_CHANNEL_COUNT\x10\xdb\x8c@\x121\n+NIDMM_ATTRIBUTE_SUPPORTED_INSTRUMENT_MODELS\x10\xd7\x8d@\x12(\n"NIDMM_ATTRIBUTE_GROUP_CAPABILITIES\x10\xa1\x8e@\x12-\n\'NIDMM_ATTRIBUTE_INSTRUMENT_MANUFACTURER\x10\x8f\x8f@\x12&\n NIDMM_ATTRIBUTE_INSTRUMENT_MODEL\x10\x90\x8f@\x122\n,NIDMM_ATTRIBUTE_INSTRUMENT_FIRMWARE_REVISION\x10\x8e\x8f@\x12"\n\x1cNIDMM_ATTRIBUTE_LOGICAL_NAME\x10\xc1\x8d@\x12,\n&NIDMM_ATTRIBUTE_IO_RESOURCE_DESCRIPTOR\x10\xc0\x8d@\x12"\n\x1cNIDMM_ATTRIBUTE_DRIVER_SETUP\x10\x97\x8b@\x12\x1e\n\x18NIDMM_ATTRIBUTE_FUNCTION\x10\xd1\xa5L\x12\x1b\n\x15NIDMM_ATTRIBUTE_RANGE\x10\xd2\xa5L\x12)\n#NIDMM_ATTRIBUTE_RESOLUTION_ABSOLUTE\x10\xd8\xa5L\x12\'\n!NIDMM_ATTRIBUTE_RESOLUTION_DIGITS\x10\xd3\xa5L\x12#\n\x1dNIDMM_ATTRIBUTE_TRIGGER_DELAY\x10\xd5\xa5L\x12$\n\x1eNIDMM_ATTRIBUTE_TRIGGER_SOURCE\x10\xd4\xa5L\x12!\n\x1bNIDMM_ATTRIBUTE_AC_MAX_FREQ\x10\xd7\xa5L\x12!\n\x1bNIDMM_ATTRIBUTE_AC_MIN_FREQ\x10\xd6\xa5L\x12(\n"NIDMM_ATTRIBUTE_FREQ_VOLTAGE_RANGE\x10\xb5\xa6L\x12(\n"NIDMM_ATTRIBUTE_MEAS_COMPLETE_DEST\x10\x81\xa8L\x12"\n\x1cNIDMM_ATTRIBUTE_SAMPLE_COUNT\x10\xfd\xa7L\x12%\n\x1fNIDMM_ATTRIBUTE_SAMPLE_INTERVAL\x10\xff\xa7L\x12$\n\x1eNIDMM_ATTRIBUTE_SAMPLE_TRIGGER\x10\xfe\xa7L\x12#\n\x1dNIDMM_ATTRIBUTE_TRIGGER_COUNT\x10\x80\xa8L\x12#\n\x1dNIDMM_ATTRIBUTE_APERTURE_TIME\x10\x91\xa8L\x12)\n#NIDMM_ATTRIBUTE_APERTURE_TIME_UNITS\x10\x92\xa8L\x12&\n NIDMM_ATTRIBUTE_AUTO_RANGE_VALUE\x10\x9b\xa8L\x12\x1f\n\x19NIDMM_ATTRIBUTE_AUTO_ZERO\x10\x9c\xa8L\x12$\n\x1eNIDMM_ATTRIBUTE_POWERLINE_FREQ\x10\x9d\xa8L\x12#\n\x1dNIDMM_ATTRIBUTE_TRIGGER_SLOPE\x10\x9e\xa8L\x12*\n$NIDMM_ATTRIBUTE_SAMPLE_TRIGGER_SLOPE\x10\xba\x98F\x12%\n\x1fNIDMM_ATTRIBUTE_MEAS_DEST_SLOPE\x10\xb2\x98F\x12%\n\x1fNIDMM_ATTRIBUTE_ADC_CALIBRATION\x10\xc6\x98F\x12&\n NIDMM_ATTRIBUTE_OFFSET_COMP_OHMS\x10\xc7\x98F\x12(\n"NIDMM_ATTRIBUTE_NUMBER_OF_AVERAGES\x10\xd0\x98F\x12$\n\x1eNIDMM_ATTRIBUTE_CURRENT_SOURCE\x10\xc9\x98F\x12(\n"NIDMM_ATTRIBUTE_DC_NOISE_REJECTION\x10\xca\x98F\x12!\n\x1bNIDMM_ATTRIBUTE_SETTLE_TIME\x10\xcc\x98F\x12&\n NIDMM_ATTRIBUTE_INPUT_RESISTANCE\x10\xcd\x98F\x12\x1d\n\x17NIDMM_ATTRIBUTE_LATENCY\x10\xd2\x98F\x12!\n\x1bNIDMM_ATTRIBUTE_BUFFER_SIZE\x10\xd5\x98F\x12!\n\x1bNIDMM_ATTRIBUTE_SHUNT_VALUE\x10\xb3\x98F\x12$\n\x1eNIDMM_ATTRIBUTE_OPERATION_MODE\x10\xbe\x98F\x12#\n\x1dNIDMM_ATTRIBUTE_WAVEFORM_RATE\x10\xc2\x98F\x12%\n\x1fNIDMM_ATTRIBUTE_WAVEFORM_POINTS\x10\xc3\x98F\x12\'\n!NIDMM_ATTRIBUTE_WAVEFORM_COUPLING\x10\xcb\x98F\x123\n-NIDMM_ATTRIBUTE_FREQ_VOLTAGE_AUTO_RANGE_VALUE\x10\xdc\x98F\x12%\n\x1fNIDMM_ATTRIBUTE_CABLE_COMP_TYPE\x10\xdd\x98F\x120\n*NIDMM_ATTRIBUTE_SHORT_CABLE_COMP_REACTANCE\x10\xde\x98F\x121\n+NIDMM_ATTRIBUTE_SHORT_CABLE_COMP_RESISTANCE\x10\xdf\x98F\x121\n+NIDMM_ATTRIBUTE_OPEN_CABLE_COMP_SUSCEPTANCE\x10\xe0\x98F\x121\n+NIDMM_ATTRIBUTE_OPEN_CABLE_COMP_CONDUCTANCE\x10\xe1\x98F\x12*\n$NIDMM_ATTRIBUTE_LC_CALCULATION_MODEL\x10\xe4\x98F\x12\x1d\n\x17NIDMM_ATTRIBUTE_DC_BIAS\x10\xe5\x98F\x12/\n)NIDMM_ATTRIBUTE_LC_NUMBER_MEAS_TO_AVERAGE\x10\xe7\x98F\x12#\n\x1dNIDMM_ATTRIBUTE_SERIAL_NUMBER\x10\xe6\x98F\x12+\n%NIDMM_ATTRIBUTE_CONFIG_PRODUCT_NUMBER\x10\xed\x98F\x12*\n$NIDMM_ATTRIBUTE_TEMP_TRANSDUCER_TYPE\x10\x99\xa7L\x12+\n%NIDMM_ATTRIBUTE_TEMP_TC_REF_JUNC_TYPE\x10\xb8\xa7L\x12"\n\x1cNIDMM_ATTRIBUTE_TEMP_TC_TYPE\x10\xb7\xa7L\x12,\n&NIDMM_ATTRIBUTE_TEMP_TC_FIXED_REF_JUNC\x10\xb9\xa7L\x12#\n\x1dNIDMM_ATTRIBUTE_TEMP_RTD_TYPE\x10\xa8\x99F\x12"\n\x1cNIDMM_ATTRIBUTE_TEMP_RTD_RES\x10\xc2\xa7L\x12 \n\x1aNIDMM_ATTRIBUTE_TEMP_RTD_A\x10\xa9\x99F\x12 \n\x1aNIDMM_ATTRIBUTE_TEMP_RTD_B\x10\xaa\x99F\x12 \n\x1aNIDMM_ATTRIBUTE_TEMP_RTD_C\x10\xab\x99F\x12*\n$NIDMM_ATTRIBUTE_TEMP_THERMISTOR_TYPE\x10\xac\x99F\x12\'\n!NIDMM_ATTRIBUTE_TEMP_THERMISTOR_A\x10\xad\x99F\x12\'\n!NIDMM_ATTRIBUTE_TEMP_THERMISTOR_B\x10\xae\x99F\x12\'\n!NIDMM_ATTRIBUTE_TEMP_THERMISTOR_C\x10\xaf\x99F\x123\n-NIDMM_ATTRIBUTE_SPECIFIC_DRIVER_MAJOR_VERSION\x10\x87\x8f@\x123\n-NIDMM_ATTRIBUTE_SPECIFIC_DRIVER_MINOR_VERSION\x10\x88\x8f@*\xbb\x04\n\x08Function\x12\x18\n\x14FUNCTION_UNSPECIFIED\x10\x00\x12\x1f\n\x1bFUNCTION_NIDMM_VAL_DC_VOLTS\x10\x01\x12\x1f\n\x1bFUNCTION_NIDMM_VAL_AC_VOLTS\x10\x02\x12!\n\x1dFUNCTION_NIDMM_VAL_DC_CURRENT\x10\x03\x12!\n\x1dFUNCTION_NIDMM_VAL_AC_CURRENT\x10\x04\x12!\n\x1dFUNCTION_NIDMM_VAL_2_WIRE_RES\x10\x05\x12!\n\x1dFUNCTION_NIDMM_VAL_4_WIRE_RES\x10e\x12\x1b\n\x17FUNCTION_NIDMM_VAL_FREQ\x10h\x12\x1d\n\x19FUNCTION_NIDMM_VAL_PERIOD\x10i\x12"\n\x1eFUNCTION_NIDMM_VAL_TEMPERATURE\x10l\x12+\n&FUNCTION_NIDMM_VAL_AC_VOLTS_DC_COUPLED\x10\xe9\x07\x12\x1d\n\x18FUNCTION_NIDMM_VAL_DIODE\x10\xea\x07\x12(\n#FUNCTION_NIDMM_VAL_WAVEFORM_VOLTAGE\x10\xeb\x07\x12(\n#FUNCTION_NIDMM_VAL_WAVEFORM_CURRENT\x10\xec\x07\x12#\n\x1eFUNCTION_NIDMM_VAL_CAPACITANCE\x10\xed\x07\x12"\n\x1dFUNCTION_NIDMM_VAL_INDUCTANCE\x10\xee\x07*\xe4\x04\n\rTriggerSource\x12\x1e\n\x1aTRIGGER_SOURCE_UNSPECIFIED\x10\x00\x12&\n"TRIGGER_SOURCE_NIDMM_VAL_IMMEDIATE\x10\x01\x12%\n!TRIGGER_SOURCE_NIDMM_VAL_EXTERNAL\x10\x02\x12*\n&TRIGGER_SOURCE_NIDMM_VAL_SOFTWARE_TRIG\x10\x03\x12&\n"TRIGGER_SOURCE_NIDMM_VAL_PXI_TRIG0\x10o\x12&\n"TRIGGER_SOURCE_NIDMM_VAL_PXI_TRIG1\x10p\x12&\n"TRIGGER_SOURCE_NIDMM_VAL_PXI_TRIG2\x10q\x12&\n"TRIGGER_SOURCE_NIDMM_VAL_PXI_TRIG3\x10r\x12&\n"TRIGGER_SOURCE_NIDMM_VAL_PXI_TRIG4\x10s\x12&\n"TRIGGER_SOURCE_NIDMM_VAL_PXI_TRIG5\x10t\x12&\n"TRIGGER_SOURCE_NIDMM_VAL_PXI_TRIG6\x10u\x12&\n"TRIGGER_SOURCE_NIDMM_VAL_PXI_TRIG7\x10v\x12&\n!TRIGGER_SOURCE_NIDMM_VAL_PXI_STAR\x10\x83\x01\x12\'\n"TRIGGER_SOURCE_NIDMM_VAL_AUX_TRIG1\x10\xe9\x07\x12\'\n"TRIGGER_SOURCE_NIDMM_VAL_LBR_TRIG1\x10\xec\x07*\x8b\x05\n\rSampleTrigger\x12\x1e\n\x1aSAMPLE_TRIGGER_UNSPECIFIED\x10\x00\x12&\n"SAMPLE_TRIGGER_NIDMM_VAL_IMMEDIATE\x10\x01\x12%\n!SAMPLE_TRIGGER_NIDMM_VAL_EXTERNAL\x10\x02\x12*\n&SAMPLE_TRIGGER_NIDMM_VAL_SOFTWARE_TRIG\x10\x03\x12%\n!SAMPLE_TRIGGER_NIDMM_VAL_INTERVAL\x10\n\x12&\n"SAMPLE_TRIGGER_NIDMM_VAL_PXI_TRIG0\x10o\x12&\n"SAMPLE_TRIGGER_NIDMM_VAL_PXI_TRIG1\x10p\x12&\n"SAMPLE_TRIGGER_NIDMM_VAL_PXI_TRIG2\x10q\x12&\n"SAMPLE_TRIGGER_NIDMM_VAL_PXI_TRIG3\x10r\x12&\n"SAMPLE_TRIGGER_NIDMM_VAL_PXI_TRIG4\x10s\x12&\n"SAMPLE_TRIGGER_NIDMM_VAL_PXI_TRIG5\x10t\x12&\n"SAMPLE_TRIGGER_NIDMM_VAL_PXI_TRIG6\x10u\x12&\n"SAMPLE_TRIGGER_NIDMM_VAL_PXI_TRIG7\x10v\x12&\n!SAMPLE_TRIGGER_NIDMM_VAL_PXI_STAR\x10\x83\x01\x12\'\n"SAMPLE_TRIGGER_NIDMM_VAL_AUX_TRIG1\x10\xe9\x07\x12\'\n"SAMPLE_TRIGGER_NIDMM_VAL_LBR_TRIG1\x10\xec\x07*Z\n\x0cTriggerSlope\x12$\n TRIGGER_SLOPE_NIDMM_VAL_POSITIVE\x10\x00\x12$\n TRIGGER_SLOPE_NIDMM_VAL_NEGATIVE\x10\x01*e\n\x0fSampleTrigSlope\x12(\n$SAMPLE_TRIG_SLOPE_NIDMM_VAL_POSITIVE\x10\x00\x12(\n$SAMPLE_TRIG_SLOPE_NIDMM_VAL_NEGATIVE\x10\x01*\x9c\x01\n\x14PowerLineFrequencies\x12&\n"POWER_LINE_FREQUENCIES_UNSPECIFIED\x10\x00\x12-\n)POWER_LINE_FREQUENCIES_NIDMM_VAL_50_HERTZ\x102\x12-\n)POWER_LINE_FREQUENCIES_NIDMM_VAL_60_HERTZ\x10<*s\n\x11ApertureTimeUnits\x12)\n%APERTURE_TIME_UNITS_NIDMM_VAL_SECONDS\x10\x00\x123\n/APERTURE_TIME_UNITS_NIDMM_VAL_POWER_LINE_CYCLES\x10\x01*z\n\x0fCompensatedOhms\x123\n/COMPENSATED_OHMS_NIDMM_VAL_OFFSET_COMP_OHMS_OFF\x10\x00\x122\n.COMPENSATED_OHMS_NIDMM_VAL_OFFSET_COMP_OHMS_ON\x10\x01*m\n\x0fCalibrationType\x12,\n(CALIBRATION_TYPE_NIDMM_VAL_INTERNAL_AREA\x10\x00\x12,\n(CALIBRATION_TYPE_NIDMM_VAL_EXTERNAL_AREA\x10\x01*\xa1\x01\n!ThermocoupleReferenceJunctionType\x124\n0THERMOCOUPLE_REFERENCE_JUNCTION_TYPE_UNSPECIFIED\x10\x00\x12F\nBTHERMOCOUPLE_REFERENCE_JUNCTION_TYPE_NIDMM_VAL_TEMP_REF_JUNC_FIXED\x10\x02*\x8d\x03\n\x10ThermocoupleType\x12!\n\x1dTHERMOCOUPLE_TYPE_UNSPECIFIED\x10\x00\x12)\n%THERMOCOUPLE_TYPE_NIDMM_VAL_TEMP_TC_B\x10\x01\x12)\n%THERMOCOUPLE_TYPE_NIDMM_VAL_TEMP_TC_E\x10\x04\x12)\n%THERMOCOUPLE_TYPE_NIDMM_VAL_TEMP_TC_J\x10\x06\x12)\n%THERMOCOUPLE_TYPE_NIDMM_VAL_TEMP_TC_K\x10\x07\x12)\n%THERMOCOUPLE_TYPE_NIDMM_VAL_TEMP_TC_N\x10\x08\x12)\n%THERMOCOUPLE_TYPE_NIDMM_VAL_TEMP_TC_R\x10\t\x12)\n%THERMOCOUPLE_TYPE_NIDMM_VAL_TEMP_TC_S\x10\n\x12)\n%THERMOCOUPLE_TYPE_NIDMM_VAL_TEMP_TC_T\x10\x0b*\xa1\x02\n\x07RtdType\x12&\n"RTD_TYPE_NIDMM_VAL_TEMP_RTD_CUSTOM\x10\x00\x12&\n"RTD_TYPE_NIDMM_VAL_TEMP_RTD_PT3750\x10\x01\x12&\n"RTD_TYPE_NIDMM_VAL_TEMP_RTD_PT3851\x10\x02\x12&\n"RTD_TYPE_NIDMM_VAL_TEMP_RTD_PT3911\x10\x03\x12&\n"RTD_TYPE_NIDMM_VAL_TEMP_RTD_PT3916\x10\x04\x12&\n"RTD_TYPE_NIDMM_VAL_TEMP_RTD_PT3920\x10\x05\x12&\n"RTD_TYPE_NIDMM_VAL_TEMP_RTD_PT3928\x10\x06*\xa4\x02\n\x11AcquisitionStatus\x126\n2ACQUISITION_STATUS_NIDMM_VAL_RUNNING_ANTICOLLISION\x10\x00\x126\n2ACQUISITION_STATUS_NIDMM_VAL_FINISHED_WITH_BACKLOG\x10\x01\x129\n5ACQUISITION_STATUS_NIDMM_VAL_FINISHED_WITH_NO_BACKLOG\x10\x02\x12\'\n#ACQUISITION_STATUS_NIDMM_VAL_PAUSED\x10\x03\x12;\n7ACQUISITION_STATUS_NIDMM_VAL_NO_ACQUISITION_IN_PROGRESS\x10\x04*\xe1\x02\n\x0cApertureTime\x12\x1d\n\x19APERTURE_TIME_UNSPECIFIED\x10\x00\x127\n*APERTURE_TIME_NIDMM_VAL_APERTURE_TIME_AUTO\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12!\n\x1dAPERTURE_TIME_NIDMM_VAL_1_PLC\x10\x01\x12!\n\x1dAPERTURE_TIME_NIDMM_VAL_5_PLC\x10\x05\x12!\n\x1dAPERTURE_TIME_NIDMM_VAL_6_PLC\x10\x06\x12"\n\x1eAPERTURE_TIME_NIDMM_VAL_10_PLC\x10\n\x12"\n\x1eAPERTURE_TIME_NIDMM_VAL_12_PLC\x10\x0c\x12#\n\x1fAPERTURE_TIME_NIDMM_VAL_100_PLC\x10d\x12#\n\x1fAPERTURE_TIME_NIDMM_VAL_120_PLC\x10x*<\n\rControlCommit\x12+\n\'CONTROL_COMMIT_NIDMM_VAL_CONTROL_COMMIT\x10\x00*\xbd\x01\n\x15FrequencyVoltageRange\x12\'\n#FREQUENCY_VOLTAGE_RANGE_UNSPECIFIED\x10\x00\x12<\n/FREQUENCY_VOLTAGE_RANGE_NIDMM_VAL_AUTO_RANGE_ON\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12=\n0FREQUENCY_VOLTAGE_RANGE_NIDMM_VAL_AUTO_RANGE_OFF\x10\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01*?\n\x0bSampleCount\x120\n,SAMPLE_COUNT_NIDMM_VAL_SAMPLE_COUNT_INFINITE\x10\x00*d\n\x0eSampleInterval\x12\x1f\n\x1bSAMPLE_INTERVAL_UNSPECIFIED\x10\x00\x121\n$SAMPLE_INTERVAL_NIDMM_VAL_AUTO_DELAY\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01*Z\n\tTimeLimit\x12\x1a\n\x16TIME_LIMIT_UNSPECIFIED\x10\x00\x121\n$TIME_LIMIT_NIDMM_VAL_TIME_LIMIT_AUTO\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01*?\n\x0cTriggerCount\x12/\n+TRIGGER_COUNT_NIDMM_VAL_TRIG_COUNT_INFINITE\x10\x00*\x9a\x01\n\rTriggerDelays\x12\x1e\n\x1aTRIGGER_DELAYS_UNSPECIFIED\x10\x00\x123\n&TRIGGER_DELAYS_NIDMM_VAL_AUTO_DELAY_ON\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x124\n\'TRIGGER_DELAYS_NIDMM_VAL_AUTO_DELAY_OFF\x10\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01*\xd2.\n\x19NiDmmInt32AttributeValues\x12\x1b\n\x17NIDMM_INT32_UNSPECIFIED\x10\x00\x127\n3NIDMM_INT32_ADC_CALIBRATION_VAL_ADC_CALIBRATION_OFF\x10\x00\x12A\n4NIDMM_INT32_ADC_CALIBRATION_VAL_ADC_CALIBRATION_AUTO\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x126\n2NIDMM_INT32_ADC_CALIBRATION_VAL_ADC_CALIBRATION_ON\x10\x01\x12/\n+NIDMM_INT32_APERTURE_TIME_UNITS_VAL_SECONDS\x10\x00\x129\n5NIDMM_INT32_APERTURE_TIME_UNITS_VAL_POWER_LINE_CYCLES\x10\x01\x12+\n\'NIDMM_INT32_AUTO_ZERO_VAL_AUTO_ZERO_OFF\x10\x00\x125\n(NIDMM_INT32_AUTO_ZERO_VAL_AUTO_ZERO_AUTO\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12*\n&NIDMM_INT32_AUTO_ZERO_VAL_AUTO_ZERO_ON\x10\x01\x12,\n(NIDMM_INT32_AUTO_ZERO_VAL_AUTO_ZERO_ONCE\x10\x02\x129\n,NIDMM_INT32_BUFFER_SIZE_VAL_BUFFER_SIZE_AUTO\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12;\n7NIDMM_INT32_CABLE_COMPENSATION_TYPE_VAL_CABLE_COMP_NONE\x10\x00\x12;\n7NIDMM_INT32_CABLE_COMPENSATION_TYPE_VAL_CABLE_COMP_OPEN\x10\x01\x12<\n8NIDMM_INT32_CABLE_COMPENSATION_TYPE_VAL_CABLE_COMP_SHORT\x10\x02\x12E\nANIDMM_INT32_CABLE_COMPENSATION_TYPE_VAL_CABLE_COMP_OPEN_AND_SHORT\x10\x03\x129\n5NIDMM_INT32_COMPENSATED_OHMS_VAL_OFFSET_COMP_OHMS_OFF\x10\x00\x128\n4NIDMM_INT32_COMPENSATED_OHMS_VAL_OFFSET_COMP_OHMS_ON\x10\x01\x12\'\n#NIDMM_INT32_DC_BIAS_VAL_DC_BIAS_OFF\x10\x00\x12&\n"NIDMM_INT32_DC_BIAS_VAL_DC_BIAS_ON\x10\x01\x122\n.NIDMM_INT32_DC_NOISE_REJECTION_VAL_DCNR_NORMAL\x10\x00\x129\n,NIDMM_INT32_DC_NOISE_REJECTION_VAL_DCNR_AUTO\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x128\n4NIDMM_INT32_DC_NOISE_REJECTION_VAL_DCNR_SECOND_ORDER\x10\x01\x126\n2NIDMM_INT32_DC_NOISE_REJECTION_VAL_DCNR_HIGH_ORDER\x10\x02\x12%\n!NIDMM_INT32_FUNCTION_VAL_DC_VOLTS\x10\x01\x12%\n!NIDMM_INT32_FUNCTION_VAL_AC_VOLTS\x10\x02\x12\'\n#NIDMM_INT32_FUNCTION_VAL_DC_CURRENT\x10\x03\x12\'\n#NIDMM_INT32_FUNCTION_VAL_AC_CURRENT\x10\x04\x12\'\n#NIDMM_INT32_FUNCTION_VAL_2_WIRE_RES\x10\x05\x12\'\n#NIDMM_INT32_FUNCTION_VAL_4_WIRE_RES\x10e\x12!\n\x1dNIDMM_INT32_FUNCTION_VAL_FREQ\x10h\x12#\n\x1fNIDMM_INT32_FUNCTION_VAL_PERIOD\x10i\x12(\n$NIDMM_INT32_FUNCTION_VAL_TEMPERATURE\x10l\x121\n,NIDMM_INT32_FUNCTION_VAL_AC_VOLTS_DC_COUPLED\x10\xe9\x07\x12#\n\x1eNIDMM_INT32_FUNCTION_VAL_DIODE\x10\xea\x07\x12.\n)NIDMM_INT32_FUNCTION_VAL_WAVEFORM_VOLTAGE\x10\xeb\x07\x12.\n)NIDMM_INT32_FUNCTION_VAL_WAVEFORM_CURRENT\x10\xec\x07\x12)\n$NIDMM_INT32_FUNCTION_VAL_CAPACITANCE\x10\xed\x07\x12(\n#NIDMM_INT32_FUNCTION_VAL_INDUCTANCE\x10\xee\x07\x121\n$NIDMM_INT32_LATENCY_VAL_LATENCY_AUTO\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12:\n6NIDMM_INT32_LC_CALCULATION_MODEL_VAL_CALC_MODEL_SERIES\x10\x00\x12A\n4NIDMM_INT32_LC_CALCULATION_MODEL_VAL_CALC_MODEL_AUTO\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12<\n8NIDMM_INT32_LC_CALCULATION_MODEL_VAL_CALC_MODEL_PARALLEL\x10\x01\x12;\n.NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_NONE\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x126\n2NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_EXTERNAL\x10\x02\x127\n3NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG0\x10o\x127\n3NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG1\x10p\x127\n3NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG2\x10q\x127\n3NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG3\x10r\x127\n3NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG4\x10s\x127\n3NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG5\x10t\x127\n3NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG6\x10u\x127\n3NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_PXI_TRIG7\x10v\x128\n3NIDMM_INT32_MEASUREMENT_COMPLETE_DEST_VAL_LBR_TRIG0\x10\xeb\x07\x12:\n6NIDMM_INT32_MEASUREMENT_DESTINATION_SLOPE_VAL_POSITIVE\x10\x00\x12:\n6NIDMM_INT32_MEASUREMENT_DESTINATION_SLOPE_VAL_NEGATIVE\x10\x01\x12.\n*NIDMM_INT32_OPERATION_MODE_VAL_IVIDMM_MODE\x10\x00\x120\n,NIDMM_INT32_OPERATION_MODE_VAL_WAVEFORM_MODE\x10\x01\x12,\n(NIDMM_INT32_RTD_TYPE_VAL_TEMP_RTD_CUSTOM\x10\x00\x12,\n(NIDMM_INT32_RTD_TYPE_VAL_TEMP_RTD_PT3750\x10\x01\x12,\n(NIDMM_INT32_RTD_TYPE_VAL_TEMP_RTD_PT3851\x10\x02\x12,\n(NIDMM_INT32_RTD_TYPE_VAL_TEMP_RTD_PT3911\x10\x03\x12,\n(NIDMM_INT32_RTD_TYPE_VAL_TEMP_RTD_PT3916\x10\x04\x12,\n(NIDMM_INT32_RTD_TYPE_VAL_TEMP_RTD_PT3920\x10\x05\x12,\n(NIDMM_INT32_RTD_TYPE_VAL_TEMP_RTD_PT3928\x10\x06\x126\n2NIDMM_INT32_SAMPLE_COUNT_VAL_SAMPLE_COUNT_INFINITE\x10\x00\x12.\n*NIDMM_INT32_SAMPLE_TRIG_SLOPE_VAL_POSITIVE\x10\x00\x12.\n*NIDMM_INT32_SAMPLE_TRIG_SLOPE_VAL_NEGATIVE\x10\x01\x12,\n(NIDMM_INT32_SAMPLE_TRIGGER_VAL_IMMEDIATE\x10\x01\x12+\n\'NIDMM_INT32_SAMPLE_TRIGGER_VAL_EXTERNAL\x10\x02\x120\n,NIDMM_INT32_SAMPLE_TRIGGER_VAL_SOFTWARE_TRIG\x10\x03\x12+\n\'NIDMM_INT32_SAMPLE_TRIGGER_VAL_INTERVAL\x10\n\x12,\n(NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_TRIG0\x10o\x12,\n(NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_TRIG1\x10p\x12,\n(NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_TRIG2\x10q\x12,\n(NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_TRIG3\x10r\x12,\n(NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_TRIG4\x10s\x12,\n(NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_TRIG5\x10t\x12,\n(NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_TRIG6\x10u\x12,\n(NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_TRIG7\x10v\x12,\n\'NIDMM_INT32_SAMPLE_TRIGGER_VAL_PXI_STAR\x10\x83\x01\x12-\n(NIDMM_INT32_SAMPLE_TRIGGER_VAL_AUX_TRIG1\x10\xe9\x07\x12-\n(NIDMM_INT32_SAMPLE_TRIGGER_VAL_LBR_TRIG1\x10\xec\x07\x12:\n6NIDMM_INT32_THERMISTOR_TYPE_VAL_TEMP_THERMISTOR_CUSTOM\x10\x00\x129\n5NIDMM_INT32_THERMISTOR_TYPE_VAL_TEMP_THERMISTOR_44004\x10\x01\x129\n5NIDMM_INT32_THERMISTOR_TYPE_VAL_TEMP_THERMISTOR_44006\x10\x02\x129\n5NIDMM_INT32_THERMISTOR_TYPE_VAL_TEMP_THERMISTOR_44007\x10\x03\x12L\nHNIDMM_INT32_THERMOCOUPLE_REFERENCE_JUNCTION_TYPE_VAL_TEMP_REF_JUNC_FIXED\x10\x02\x12/\n+NIDMM_INT32_THERMOCOUPLE_TYPE_VAL_TEMP_TC_B\x10\x01\x12/\n+NIDMM_INT32_THERMOCOUPLE_TYPE_VAL_TEMP_TC_E\x10\x04\x12/\n+NIDMM_INT32_THERMOCOUPLE_TYPE_VAL_TEMP_TC_J\x10\x06\x12/\n+NIDMM_INT32_THERMOCOUPLE_TYPE_VAL_TEMP_TC_K\x10\x07\x12/\n+NIDMM_INT32_THERMOCOUPLE_TYPE_VAL_TEMP_TC_N\x10\x08\x12/\n+NIDMM_INT32_THERMOCOUPLE_TYPE_VAL_TEMP_TC_R\x10\t\x12/\n+NIDMM_INT32_THERMOCOUPLE_TYPE_VAL_TEMP_TC_S\x10\n\x12/\n+NIDMM_INT32_THERMOCOUPLE_TYPE_VAL_TEMP_TC_T\x10\x0b\x120\n,NIDMM_INT32_TRANSDUCER_TYPE_VAL_THERMOCOUPLE\x10\x01\x12.\n*NIDMM_INT32_TRANSDUCER_TYPE_VAL_THERMISTOR\x10\x02\x12.\n*NIDMM_INT32_TRANSDUCER_TYPE_VAL_2_WIRE_RTD\x10\x03\x12.\n*NIDMM_INT32_TRANSDUCER_TYPE_VAL_4_WIRE_RTD\x10\x04\x125\n1NIDMM_INT32_TRIGGER_COUNT_VAL_TRIG_COUNT_INFINITE\x10\x00\x12*\n&NIDMM_INT32_TRIGGER_SLOPE_VAL_POSITIVE\x10\x00\x12*\n&NIDMM_INT32_TRIGGER_SLOPE_VAL_NEGATIVE\x10\x01\x12,\n(NIDMM_INT32_TRIGGER_SOURCE_VAL_IMMEDIATE\x10\x01\x12+\n\'NIDMM_INT32_TRIGGER_SOURCE_VAL_EXTERNAL\x10\x02\x120\n,NIDMM_INT32_TRIGGER_SOURCE_VAL_SOFTWARE_TRIG\x10\x03\x12,\n(NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_TRIG0\x10o\x12,\n(NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_TRIG1\x10p\x12,\n(NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_TRIG2\x10q\x12,\n(NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_TRIG3\x10r\x12,\n(NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_TRIG4\x10s\x12,\n(NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_TRIG5\x10t\x12,\n(NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_TRIG6\x10u\x12,\n(NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_TRIG7\x10v\x12,\n\'NIDMM_INT32_TRIGGER_SOURCE_VAL_PXI_STAR\x10\x83\x01\x12-\n(NIDMM_INT32_TRIGGER_SOURCE_VAL_AUX_TRIG1\x10\xe9\x07\x12-\n(NIDMM_INT32_TRIGGER_SOURCE_VAL_LBR_TRIG1\x10\xec\x07\x12:\n6NIDMM_INT32_WAVEFORM_COUPLING_VAL_WAVEFORM_COUPLING_AC\x10\x00\x12:\n6NIDMM_INT32_WAVEFORM_COUPLING_VAL_WAVEFORM_COUPLING_DC\x10\x01\x1a\x02\x10\x01*\xac\x08\n\x1aNiDmmReal64AttributeValues\x12\x1c\n\x18NIDMM_REAL64_UNSPECIFIED\x10\x00\x12>\n1NIDMM_REAL64_APERTURE_TIME_VAL_APERTURE_TIME_AUTO\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12(\n$NIDMM_REAL64_APERTURE_TIME_VAL_1_PLC\x10\x01\x12(\n$NIDMM_REAL64_APERTURE_TIME_VAL_5_PLC\x10\x05\x12(\n$NIDMM_REAL64_APERTURE_TIME_VAL_6_PLC\x10\x06\x12)\n%NIDMM_REAL64_APERTURE_TIME_VAL_10_PLC\x10\n\x12)\n%NIDMM_REAL64_APERTURE_TIME_VAL_12_PLC\x10\x0c\x12*\n&NIDMM_REAL64_APERTURE_TIME_VAL_100_PLC\x10d\x12*\n&NIDMM_REAL64_APERTURE_TIME_VAL_120_PLC\x10x\x12C\n6NIDMM_REAL64_FREQUENCY_VOLTAGE_RANGE_VAL_AUTO_RANGE_ON\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12D\n7NIDMM_REAL64_FREQUENCY_VOLTAGE_RANGE_VAL_AUTO_RANGE_OFF\x10\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01\x124\n0NIDMM_REAL64_POWER_LINE_FREQUENCIES_VAL_50_HERTZ\x102\x124\n0NIDMM_REAL64_POWER_LINE_FREQUENCIES_VAL_60_HERTZ\x10<\x121\n$NIDMM_REAL64_RANGE_VAL_AUTO_RANGE_ON\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x122\n%NIDMM_REAL64_RANGE_VAL_AUTO_RANGE_OFF\x10\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01\x123\n&NIDMM_REAL64_RANGE_VAL_AUTO_RANGE_ONCE\x10\xfd\xff\xff\xff\xff\xff\xff\xff\xff\x01\x128\n+NIDMM_REAL64_SAMPLE_INTERVAL_VAL_AUTO_DELAY\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12:\n-NIDMM_REAL64_SETTLE_TIME_VAL_SETTLE_TIME_AUTO\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12:\n-NIDMM_REAL64_TRIGGER_DELAYS_VAL_AUTO_DELAY_ON\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12;\n.NIDMM_REAL64_TRIGGER_DELAYS_VAL_AUTO_DELAY_OFF\x10\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01\x1a\x02\x10\x01*\xac\x03\n NiDmmReal64AttributeValuesMapped\x12#\n\x1fNIDMM_REAL64_MAPPED_UNSPECIFIED\x10\x00\x12.\n*NIDMM_REAL64_CURRENT_SOURCE_VAL_1_MICROAMP\x10\x01\x12/\n+NIDMM_REAL64_CURRENT_SOURCE_VAL_10_MICROAMP\x10\x02\x120\n,NIDMM_REAL64_CURRENT_SOURCE_VAL_100_MICROAMP\x10\x03\x12.\n*NIDMM_REAL64_CURRENT_SOURCE_VAL_1_MILLIAMP\x10\x04\x12/\n+NIDMM_REAL64_INPUT_RESISTANCE_VAL_1_MEGAOHM\x10\x05\x120\n,NIDMM_REAL64_INPUT_RESISTANCE_VAL_10_MEGAOHM\x10\x06\x12=\n9NIDMM_REAL64_INPUT_RESISTANCE_VAL_GREATER_THAN_10_GIGAOHM\x10\x072\xe6D\n\x05NiDmm\x129\n\x04Init\x12\x17.nidmm_grpc.InitRequest\x1a\x18.nidmm_grpc.InitResponse\x12Z\n\x0fInitWithOptions\x12".nidmm_grpc.InitWithOptionsRequest\x1a#.nidmm_grpc.InitWithOptionsResponse\x12<\n\x05Close\x12\x18.nidmm_grpc.CloseRequest\x1a\x19.nidmm_grpc.CloseResponse\x12E\n\x08GetError\x12\x1b.nidmm_grpc.GetErrorRequest\x1a\x1c.nidmm_grpc.GetErrorResponse\x12Z\n\x0fGetErrorMessage\x12".nidmm_grpc.GetErrorMessageRequest\x1a#.nidmm_grpc.GetErrorMessageResponse\x12K\n\nClearError\x12\x1d.nidmm_grpc.ClearErrorRequest\x1a\x1e.nidmm_grpc.ClearErrorResponse\x12<\n\x05Reset\x12\x18.nidmm_grpc.ResetRequest\x1a\x19.nidmm_grpc.ResetResponse\x12E\n\x08SelfTest\x12\x1b.nidmm_grpc.SelfTestRequest\x1a\x1c.nidmm_grpc.SelfTestResponse\x12B\n\x07SelfCal\x12\x1a.nidmm_grpc.SelfCalRequest\x1a\x1b.nidmm_grpc.SelfCalResponse\x12T\n\rRevisionQuery\x12 .nidmm_grpc.RevisionQueryRequest\x1a!.nidmm_grpc.RevisionQueryResponse\x12`\n\x11ResetWithDefaults\x12$.nidmm_grpc.ResetWithDefaultsRequest\x1a%.nidmm_grpc.ResetWithDefaultsResponse\x12B\n\x07Disable\x12\x1a.nidmm_grpc.DisableRequest\x1a\x1b.nidmm_grpc.DisableResponse\x12i\n\x14GetMeasurementPeriod\x12\'.nidmm_grpc.GetMeasurementPeriodRequest\x1a(.nidmm_grpc.GetMeasurementPeriodResponse\x12]\n\x10ConfigureTrigger\x12#.nidmm_grpc.ConfigureTriggerRequest\x1a$.nidmm_grpc.ConfigureTriggerResponse\x129\n\x04Read\x12\x17.nidmm_grpc.ReadRequest\x1a\x18.nidmm_grpc.ReadResponse\x12<\n\x05Fetch\x12\x18.nidmm_grpc.FetchRequest\x1a\x19.nidmm_grpc.FetchResponse\x12<\n\x05Abort\x12\x18.nidmm_grpc.AbortRequest\x1a\x19.nidmm_grpc.AbortResponse\x12E\n\x08Initiate\x12\x1b.nidmm_grpc.InitiateRequest\x1a\x1c.nidmm_grpc.InitiateResponse\x12N\n\x0bIsOverRange\x12\x1e.nidmm_grpc.IsOverRangeRequest\x1a\x1f.nidmm_grpc.IsOverRangeResponse\x12Q\n\x0cIsUnderRange\x12\x1f.nidmm_grpc.IsUnderRangeRequest\x1a .nidmm_grpc.IsUnderRangeResponse\x12i\n\x14ConfigureACBandwidth\x12\'.nidmm_grpc.ConfigureACBandwidthRequest\x1a(.nidmm_grpc.ConfigureACBandwidthResponse\x12\x87\x01\n\x1eConfigureFrequencyVoltageRange\x121.nidmm_grpc.ConfigureFrequencyVoltageRangeRequest\x1a2.nidmm_grpc.ConfigureFrequencyVoltageRangeResponse\x12x\n\x19ConfigureMeasCompleteDest\x12,.nidmm_grpc.ConfigureMeasCompleteDestRequest\x1a-.nidmm_grpc.ConfigureMeasCompleteDestResponse\x12f\n\x13ConfigureMultiPoint\x12&.nidmm_grpc.ConfigureMultiPointRequest\x1a\'.nidmm_grpc.ConfigureMultiPointResponse\x12W\n\x0eReadMultiPoint\x12!.nidmm_grpc.ReadMultiPointRequest\x1a".nidmm_grpc.ReadMultiPointResponse\x12Z\n\x0fFetchMultiPoint\x12".nidmm_grpc.FetchMultiPointRequest\x1a#.nidmm_grpc.FetchMultiPointResponse\x12l\n\x15ConfigureTriggerSlope\x12(.nidmm_grpc.ConfigureTriggerSlopeRequest\x1a).nidmm_grpc.ConfigureTriggerSlopeResponse\x12f\n\x13SendSoftwareTrigger\x12&.nidmm_grpc.SendSoftwareTriggerRequest\x1a\'.nidmm_grpc.SendSoftwareTriggerResponse\x12f\n\x13GetApertureTimeInfo\x12&.nidmm_grpc.GetApertureTimeInfoRequest\x1a\'.nidmm_grpc.GetApertureTimeInfoResponse\x12`\n\x11GetAutoRangeValue\x12$.nidmm_grpc.GetAutoRangeValueRequest\x1a%.nidmm_grpc.GetAutoRangeValueResponse\x12l\n\x15ConfigureAutoZeroMode\x12(.nidmm_grpc.ConfigureAutoZeroModeRequest\x1a).nidmm_grpc.ConfigureAutoZeroModeResponse\x12~\n\x1bConfigurePowerLineFrequency\x12..nidmm_grpc.ConfigurePowerLineFrequencyRequest\x1a/.nidmm_grpc.ConfigurePowerLineFrequencyResponse\x12{\n\x1aConfigureMeasurementDigits\x12-.nidmm_grpc.ConfigureMeasurementDigitsRequest\x1a..nidmm_grpc.ConfigureMeasurementDigitsResponse\x12\x81\x01\n\x1cConfigureMeasurementAbsolute\x12/.nidmm_grpc.ConfigureMeasurementAbsoluteRequest\x1a0.nidmm_grpc.ConfigureMeasurementAbsoluteResponse\x12{\n\x1aConfigureMeasCompleteSlope\x12-.nidmm_grpc.ConfigureMeasCompleteSlopeRequest\x1a..nidmm_grpc.ConfigureMeasCompleteSlopeResponse\x12~\n\x1bConfigureSampleTriggerSlope\x12..nidmm_grpc.ConfigureSampleTriggerSlopeRequest\x1a/.nidmm_grpc.ConfigureSampleTriggerSlopeResponse\x12K\n\nReadStatus\x12\x1d.nidmm_grpc.ReadStatusRequest\x1a\x1e.nidmm_grpc.ReadStatusResponse\x12B\n\x07Control\x12\x1a.nidmm_grpc.ControlRequest\x1a\x1b.nidmm_grpc.ControlResponse\x12r\n\x17ConfigureADCCalibration\x12*.nidmm_grpc.ConfigureADCCalibrationRequest\x1a+.nidmm_grpc.ConfigureADCCalibrationResponse\x12r\n\x17ConfigureOffsetCompOhms\x12*.nidmm_grpc.ConfigureOffsetCompOhmsRequest\x1a+.nidmm_grpc.ConfigureOffsetCompOhmsResponse\x12o\n\x16ConfigureCurrentSource\x12).nidmm_grpc.ConfigureCurrentSourceRequest\x1a*.nidmm_grpc.ConfigureCurrentSourceResponse\x12o\n\x16ConfigureCableCompType\x12).nidmm_grpc.ConfigureCableCompTypeRequest\x1a*.nidmm_grpc.ConfigureCableCompTypeResponse\x12i\n\x14PerformOpenCableComp\x12\'.nidmm_grpc.PerformOpenCableCompRequest\x1a(.nidmm_grpc.PerformOpenCableCompResponse\x12l\n\x15PerformShortCableComp\x12(.nidmm_grpc.PerformShortCableCompRequest\x1a).nidmm_grpc.PerformShortCableCompResponse\x12\x81\x01\n\x1cConfigureOpenCableCompValues\x12/.nidmm_grpc.ConfigureOpenCableCompValuesRequest\x1a0.nidmm_grpc.ConfigureOpenCableCompValuesResponse\x12\x84\x01\n\x1dConfigureShortCableCompValues\x120.nidmm_grpc.ConfigureShortCableCompValuesRequest\x1a1.nidmm_grpc.ConfigureShortCableCompValuesResponse\x12\x81\x01\n\x1cConfigureWaveformAcquisition\x12/.nidmm_grpc.ConfigureWaveformAcquisitionRequest\x1a0.nidmm_grpc.ConfigureWaveformAcquisitionResponse\x12x\n\x19ConfigureWaveformCoupling\x12,.nidmm_grpc.ConfigureWaveformCouplingRequest\x1a-.nidmm_grpc.ConfigureWaveformCouplingResponse\x12T\n\rFetchWaveform\x12 .nidmm_grpc.FetchWaveformRequest\x1a!.nidmm_grpc.FetchWaveformResponse\x12Q\n\x0cReadWaveform\x12\x1f.nidmm_grpc.ReadWaveformRequest\x1a .nidmm_grpc.ReadWaveformResponse\x12f\n\x13GetAttributeViInt32\x12&.nidmm_grpc.GetAttributeViInt32Request\x1a\'.nidmm_grpc.GetAttributeViInt32Response\x12f\n\x13SetAttributeViInt32\x12&.nidmm_grpc.SetAttributeViInt32Request\x1a\'.nidmm_grpc.SetAttributeViInt32Response\x12l\n\x15CheckAttributeViInt32\x12(.nidmm_grpc.CheckAttributeViInt32Request\x1a).nidmm_grpc.CheckAttributeViInt32Response\x12i\n\x14GetAttributeViReal64\x12\'.nidmm_grpc.GetAttributeViReal64Request\x1a(.nidmm_grpc.GetAttributeViReal64Response\x12i\n\x14SetAttributeViReal64\x12\'.nidmm_grpc.SetAttributeViReal64Request\x1a(.nidmm_grpc.SetAttributeViReal64Response\x12o\n\x16CheckAttributeViReal64\x12).nidmm_grpc.CheckAttributeViReal64Request\x1a*.nidmm_grpc.CheckAttributeViReal64Response\x12i\n\x14GetAttributeViString\x12\'.nidmm_grpc.GetAttributeViStringRequest\x1a(.nidmm_grpc.GetAttributeViStringResponse\x12i\n\x14SetAttributeViString\x12\'.nidmm_grpc.SetAttributeViStringRequest\x1a(.nidmm_grpc.SetAttributeViStringResponse\x12o\n\x16CheckAttributeViString\x12).nidmm_grpc.CheckAttributeViStringRequest\x1a*.nidmm_grpc.CheckAttributeViStringResponse\x12l\n\x15GetAttributeViSession\x12(.nidmm_grpc.GetAttributeViSessionRequest\x1a).nidmm_grpc.GetAttributeViSessionResponse\x12l\n\x15SetAttributeViSession\x12(.nidmm_grpc.SetAttributeViSessionRequest\x1a).nidmm_grpc.SetAttributeViSessionResponse\x12r\n\x17CheckAttributeViSession\x12*.nidmm_grpc.CheckAttributeViSessionRequest\x1a+.nidmm_grpc.CheckAttributeViSessionResponse\x12l\n\x15GetAttributeViBoolean\x12(.nidmm_grpc.GetAttributeViBooleanRequest\x1a).nidmm_grpc.GetAttributeViBooleanResponse\x12l\n\x15SetAttributeViBoolean\x12(.nidmm_grpc.SetAttributeViBooleanRequest\x1a).nidmm_grpc.SetAttributeViBooleanResponse\x12r\n\x17CheckAttributeViBoolean\x12*.nidmm_grpc.CheckAttributeViBooleanRequest\x1a+.nidmm_grpc.CheckAttributeViBooleanResponse\x12\x8d\x01\n ImportAttributeConfigurationFile\x123.nidmm_grpc.ImportAttributeConfigurationFileRequest\x1a4.nidmm_grpc.ImportAttributeConfigurationFileResponse\x12\x8d\x01\n ExportAttributeConfigurationFile\x123.nidmm_grpc.ExportAttributeConfigurationFileRequest\x1a4.nidmm_grpc.ExportAttributeConfigurationFileResponse\x12\x93\x01\n"ImportAttributeConfigurationBuffer\x125.nidmm_grpc.ImportAttributeConfigurationBufferRequest\x1a6.nidmm_grpc.ImportAttributeConfigurationBufferResponse\x12\x93\x01\n"ExportAttributeConfigurationBuffer\x125.nidmm_grpc.ExportAttributeConfigurationBufferRequest\x1a6.nidmm_grpc.ExportAttributeConfigurationBufferResponse\x12l\n\x15ResetInterchangeCheck\x12(.nidmm_grpc.ResetInterchangeCheckRequest\x1a).nidmm_grpc.ResetInterchangeCheckResponse\x12u\n\x18ClearInterchangeWarnings\x12+.nidmm_grpc.ClearInterchangeWarningsRequest\x1a,.nidmm_grpc.ClearInterchangeWarningsResponse\x12W\n\x0eGetChannelName\x12!.nidmm_grpc.GetChannelNameRequest\x1a".nidmm_grpc.GetChannelNameResponse\x12\x81\x01\n\x1cGetExtCalRecommendedInterval\x12/.nidmm_grpc.GetExtCalRecommendedIntervalRequest\x1a0.nidmm_grpc.GetExtCalRecommendedIntervalResponse\x12f\n\x13GetSelfCalSupported\x12&.nidmm_grpc.GetSelfCalSupportedRequest\x1a\'.nidmm_grpc.GetSelfCalSupportedResponse\x12`\n\x11GetCalDateAndTime\x12$.nidmm_grpc.GetCalDateAndTimeRequest\x1a%.nidmm_grpc.GetCalDateAndTimeResponse\x12W\n\x0eGetLastCalTemp\x12!.nidmm_grpc.GetLastCalTempRequest\x1a".nidmm_grpc.GetLastCalTempResponse\x12K\n\nGetDevTemp\x12\x1d.nidmm_grpc.GetDevTempRequest\x1a\x1e.nidmm_grpc.GetDevTempResponse\x12r\n\x17ConfigureTransducerType\x12*.nidmm_grpc.ConfigureTransducerTypeRequest\x1a+.nidmm_grpc.ConfigureTransducerTypeResponse\x12l\n\x15ConfigureThermocouple\x12(.nidmm_grpc.ConfigureThermocoupleRequest\x1a).nidmm_grpc.ConfigureThermocoupleResponse\x12x\n\x19ConfigureFixedRefJunction\x12,.nidmm_grpc.ConfigureFixedRefJunctionRequest\x1a-.nidmm_grpc.ConfigureFixedRefJunctionResponse\x12]\n\x10ConfigureRTDType\x12#.nidmm_grpc.ConfigureRTDTypeRequest\x1a$.nidmm_grpc.ConfigureRTDTypeResponse\x12c\n\x12ConfigureRTDCustom\x12%.nidmm_grpc.ConfigureRTDCustomRequest\x1a&.nidmm_grpc.ConfigureRTDCustomResponse\x12r\n\x17ConfigureThermistorType\x12*.nidmm_grpc.ConfigureThermistorTypeRequest\x1a+.nidmm_grpc.ConfigureThermistorTypeResponse\x12x\n\x19ConfigureThermistorCustom\x12,.nidmm_grpc.ConfigureThermistorCustomRequest\x1a-.nidmm_grpc.ConfigureThermistorCustomResponse\x12r\n\x17InvalidateAllAttributes\x12*.nidmm_grpc.InvalidateAllAttributesRequest\x1a+.nidmm_grpc.InvalidateAllAttributesResponseB9\n\x0fcom.ni.grpc.dmmB\x05NiDmmP\x01\xaa\x02\x1cNationalInstruments.Grpc.Dmmb\x06proto3')`

<!--NI_PYTHON_API repo=nimi-python path=generated/nidmm/nidmm/nidmm_pb2_grpc.py -->
## PYTHON MODULE: generated/nidmm/nidmm/nidmm_pb2_grpc.py

### MODULE DOCSTRING

Client and server classes corresponding to protobuf-defined services.

### `class NiDmmStub(object)`

Missing associated documentation comment in .proto file.

#### `def __init__(self, channel)`

Constructor.

        Args:
            channel: A grpc.Channel.
        

### `class NiDmmServicer(object)`

Missing associated documentation comment in .proto file.

#### `def Init(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def InitWithOptions(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Close(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetError(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetErrorMessage(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ClearError(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Reset(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SelfTest(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SelfCal(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def RevisionQuery(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ResetWithDefaults(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Disable(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetMeasurementPeriod(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Read(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Fetch(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Abort(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Initiate(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def IsOverRange(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def IsUnderRange(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureACBandwidth(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureFrequencyVoltageRange(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureMeasCompleteDest(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureMultiPoint(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadMultiPoint(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def FetchMultiPoint(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureTriggerSlope(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SendSoftwareTrigger(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetApertureTimeInfo(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAutoRangeValue(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureAutoZeroMode(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigurePowerLineFrequency(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureMeasurementDigits(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureMeasurementAbsolute(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureMeasCompleteSlope(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureSampleTriggerSlope(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadStatus(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def Control(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureADCCalibration(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureOffsetCompOhms(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureCurrentSource(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureCableCompType(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def PerformOpenCableComp(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def PerformShortCableComp(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureOpenCableCompValues(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureShortCableCompValues(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureWaveformAcquisition(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureWaveformCoupling(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def FetchWaveform(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ReadWaveform(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetAttributeViInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def SetAttributeViInt32(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def CheckAttributeViInt32(self, request, context)`

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

#### `def ImportAttributeConfigurationFile(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ExportAttributeConfigurationFile(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ImportAttributeConfigurationBuffer(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ExportAttributeConfigurationBuffer(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ResetInterchangeCheck(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ClearInterchangeWarnings(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetChannelName(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetExtCalRecommendedInterval(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetSelfCalSupported(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetCalDateAndTime(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetLastCalTemp(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def GetDevTemp(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureTransducerType(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureThermocouple(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureFixedRefJunction(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureRTDType(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureRTDCustom(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureThermistorType(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def ConfigureThermistorCustom(self, request, context)`

Missing associated documentation comment in .proto file.

#### `def InvalidateAllAttributes(self, request, context)`

Missing associated documentation comment in .proto file.

### `def add_NiDmmServicer_to_server(servicer, server)`

### `class NiDmm(object)`

Missing associated documentation comment in .proto file.

#### `def Init(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def InitWithOptions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Close(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetError(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetErrorMessage(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ClearError(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Reset(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SelfTest(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SelfCal(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def RevisionQuery(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ResetWithDefaults(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Disable(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetMeasurementPeriod(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Read(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Fetch(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Abort(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Initiate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def IsOverRange(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def IsUnderRange(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureACBandwidth(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureFrequencyVoltageRange(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureMeasCompleteDest(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureMultiPoint(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadMultiPoint(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def FetchMultiPoint(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureTriggerSlope(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SendSoftwareTrigger(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetApertureTimeInfo(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAutoRangeValue(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureAutoZeroMode(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigurePowerLineFrequency(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureMeasurementDigits(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureMeasurementAbsolute(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureMeasCompleteSlope(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureSampleTriggerSlope(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadStatus(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def Control(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureADCCalibration(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureOffsetCompOhms(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureCurrentSource(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureCableCompType(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def PerformOpenCableComp(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def PerformShortCableComp(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureOpenCableCompValues(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureShortCableCompValues(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureWaveformAcquisition(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureWaveformCoupling(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def FetchWaveform(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ReadWaveform(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetAttributeViInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def SetAttributeViInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def CheckAttributeViInt32(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

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

#### `def ImportAttributeConfigurationFile(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ExportAttributeConfigurationFile(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ImportAttributeConfigurationBuffer(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ExportAttributeConfigurationBuffer(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ResetInterchangeCheck(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ClearInterchangeWarnings(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetChannelName(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetExtCalRecommendedInterval(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetSelfCalSupported(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetCalDateAndTime(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetLastCalTemp(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def GetDevTemp(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureTransducerType(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureThermocouple(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureFixedRefJunction(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureRTDType(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureRTDCustom(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureThermistorType(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def ConfigureThermistorCustom(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`

#### `def InvalidateAllAttributes(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None)`
