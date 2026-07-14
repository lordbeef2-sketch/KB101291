# NI DOCUMENT BUNDLE: labview-nxg-c-node

<!--NI_BUNDLE_CHUNK bundle=labview-nxg-c-node start=1 end=1 -->
<!--NI_TOPIC bundle=labview-nxg-c-node path=c-node.html language=enus -->
## TOPIC 00001: C Node

- bundle_id: `labview-nxg-c-node`
- source_path: `c-node.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-c-node/raw/resource/enus/c-node.html
- document_id: `labview-nxg-c-node`
- page_type: `leaf`
- content_type: `reference`
- source_description: Executes the code inside the node, written in the C programming language. With the C Node, you can add text-based code into the graphical development environment. Press <Ctrl-Space> inside the node to get an overview of all available functions. To add an input, right-click the node frame and select

C Node

Executes the code inside the node, written in the C programming language. With the C Node, you can add text-based code into the graphical development environment.

Press <Ctrl-Space> inside the node to get an overview of all available functions.

To add an input, right-click the node frame and select 
 Create»Input. To add an output, right-click the node frame and select 
 Create»Output.

#### Inputs/Outputs

##### error in

Error conditions that occur before this node runs.

[IMAGE alt='1378' src='GUID-B361979B-77AD-499C-BF91-5331F7DDC4A9-a5.png']

##### error out

Error information. If 
error in indicates that an error occurred before this node ran, 
error out contains the same error information. Otherwise, it describes the error status that this node produces.

[IMAGE alt='1378' src='GUID-A2353E57-CE42-483E-AC87-0C6782CEDD66-a5.png']

##### input

The connection between the G dataflow code outside the node and the C code inside the node. The code within the node uses the values that are connected to the inputs for calculations inside the node.

By default, the data type of the input adapts to the data type of the terminal you wire. To ensure the data type of the variable in the C Node is static and always known, you can specify the data type in the 
 Item tab.

[IMAGE alt='1378' src='GUID-B34B40DB-0F9C-4BEB-9B23-81DD2D8846FC-a5.png']

##### input string

A string data connection between the G code outside the node and the C code inside the node. The input string is accessible in the C code as a nul-terminated C string represented by a char * variable with the same name as the tunnel. The value wired to the input tunnel is the initial value of this variable.

You can resize the string buffer using the cnode_size_string macro. You can get the length of the string using the strlen function.

By default, the data type of the input adapts to the data type of the terminal you wire. To ensure the data type of the variable in the C Node is static and always known, you can specify the data type in the 
 Item tab.

[IMAGE alt='1378' src='GUID-346FCDFC-D1F0-4918-A1C8-BD7270B96401-a5.png']

##### input array

An array data connection between the G code outside the node and the C code inside the node. The input array is accessible in the C code as a C array variable with the same name and type as the tunnel. The value wired to the input tunnel is the initial value of this variable.

You can get the number of elements in the array using the cnode_get_array_length macro. You can resize the array using the cnode_size_array macro. You can index the array using the [i] notation.

By default, the data type of the input adapts to the data type of the terminal you wire. To ensure the data type of the variable in the C Node is static and always known, you can specify the data type in the 
 Item tab.

[IMAGE alt='1378' src='GUID-B34B40DB-0F9C-4BEB-9B23-81DD2D8846FC-a5.png']

##### input string array

A string array data connection between the G code outside the node and the C code inside the node. The input string array is accessible in the C code as a C array of nul-terminated C strings represented by a char * [] variable with the same name as the tunnel. The value wired to the input tunnel is the initial value of this variable.

You can get the number of string elements in the array using the cnode_get_array_length macro. You can resize the string array using the cnode_size_array macro. You can index the array using the [i] notation. You can resize the ith element of a string array named 
 my_string_array using 
 cnode_size_string(string_array[i]). Because each element is a C string, you can use ANSI C string functions such as strlen, strcpy, strcat, and so on.

By default, the data type of the input adapts to the data type of the terminal you wire. To ensure the data type of the variable in the C Node is static and always known, you can specify the data type in the 
 Item tab.

[IMAGE alt='1378' src='GUID-346FCDFC-D1F0-4918-A1C8-BD7270B96401-a5.png']

##### output

The connection between the C code inside the node and the G dataflow code outside the node. The output contains the values calculated inside the node. The default type of an output terminal is double. For other data types, you can specify the data type of the terminal on the 
Item tab.

[IMAGE alt='1378' src='GUID-29E15268-EA70-44B6-B0A8-2710C0F81842-a5.png']

##### output string

A string data connection from the C code inside the node to the G code outside the node. The output string is represented in the C code by a char * nul-terminated C string variable with the same name as the tunnel. The final value of this variable is the value available at the output tunnel.

You can resize the string buffer using the cnode_size_string macro. Because this variable is a C string, you can use ANSI C string functions such as strlen, strcpy, strcat, and so on.

The default type of an output terminal is double. For other data types, you can specify the data type of the terminal on the 
Item tab.

[IMAGE alt='1378' src='GUID-1633BB4D-9356-4C2B-AB39-FE31725A17A8-a5.png']

##### output array

An array data connection from the C code inside the node to the G code outside the node. The output array is represented in the C code by a C array variable with the same name and type as the tunnel. The final value of this variable is the value available at the output tunnel.

You can get the number of elements in the array using the cnode_get_array_length macro. You can resize the array using the cnode_size_array macro. You can index the array using the [i] notation.

The default type of an output terminal is double. For other data types, you can specify the data type of the terminal on the 
Item tab.

[IMAGE alt='1378' src='GUID-29E15268-EA70-44B6-B0A8-2710C0F81842-a5.png']

##### output string array

A string array data connection from the C code inside the node to the G code outside the node. The output string array is represented in the C code by a char * [] C array of null-terminated C strings variable with the same name as the tunnel. The final value of this variable is the value available at the output tunnel.

You can get the number of elements in the array using the cnode_get_array_length macro. You can resize the string array using the cnode_size_array macro. You can index the array using the [i] notation. You can resize the ith element of a string array named 
 my_string_array using 
 cnode_size_string(my_string_array[i]). Because each element is a C string, you can use ANSI C string functions such as strlen, strcpy, strcat, and so on.

The default type of an output terminal is double. For other data types, you can specify the data type of the terminal on the 
Item tab.

[IMAGE alt='1378' src='GUID-1633BB4D-9356-4C2B-AB39-FE31725A17A8-a5.png']

[IMAGE alt='1378' src='GUID-C17148FE-A0F3-46C4-A0C8-8888C238B8D0-a5.png']
