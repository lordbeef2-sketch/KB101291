# NI DOCUMENT BUNDLE: labview-nxg-nodes-api-ref

<!--NI_BUNDLE_CHUNK bundle=labview-nxg-nodes-api-ref start=251 end=455 -->
<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=obtain-queue.html language=enus -->
## TOPIC 00251: Obtain Queue

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `obtain-queue.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/obtain-queue.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a reference to a queue or creates a new reference to a queue. Use this reference when calling other nodes that perform queue operations. max queue size The maximum number of elements you want the queue to hold. If a queue with the same name exists, the node ignores this input and uses the ma

Obtain Queue

Returns a reference to a queue or creates a new reference to a
 queue.

Use this reference when calling other nodes that perform queue operations.

[IMAGE alt='1378' src='ObtainQueue.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### max queue size

The maximum number of elements you want the queue to hold.

If a queue with the same name exists, the node ignores this input and uses the maximum queue size from the existing queue.

Default value: -1 — The queue can hold an unlimited number of elements.

##### Preallocating Memory for Queues

To preallocate memory for a queue, enqueue the number of elements you want to include and then flush the queue. The memory remains allocated for further use of the queue.

##### What Happens When Maximum Queue Size Is Reached?

If a queue reaches the maximum queue size, the Enqueue Element or Enqueue Element at Opposite End nodes wait until the Dequeue Element or Flush Queue nodes remove elements from the queue.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### name

The name of the queue that you want to obtain or create.

Default value: Empty string — Creates an unnamed queue.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### element data type

The type of data that you want the queue to contain.

You can wire any data type to this input.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### create if not found

A Boolean value that determines whether to create a new queue if one with the same name as name does not exist.

| True | The node creates a queue if one with the same name as name does not exist. |
| --- | --- |
| False | The node does not create a queue if one with the same name as name does not exist. |

Default value: True

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: no error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### queue out

A reference to an existing queue or to a new queue created by this node.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### created new?

A Boolean value that indicates whether this node created a new queue.

| True | This node created a new queue. |
| --- | --- |
| False | This node did not create a new queue. |

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

The node produces this output according to standard error behavior.

This node can return the following error codes.

| 1094 | You tried to obtain an existing queue or notifier reference with the incorrect data type. You can get this error when you obtain a reference to the same queue or notifier but do not wire the same data type as the original specified data type. Unnamed queues and notifiers do not have this restriction, because each request to obtain an unnamed queue or notifier creates a new reference. |
| --- | --- |
| 1100 | You tried to obtain a queue or notifier that does not exist, so no reference could be returned. You can use the Obtain Queue or Obtain Notifier nodes to look up a queue or notifier by name. This error occurs if create if not found is set to False, and a queue or notifier with the name you specify was not found. |
| 1548 | A queue reference cannot be obtained with a maximum queue size of zero. The max queue size input must either be a positive number or -1 for unlimited size. |

Note

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

Transferring Data Between Loops Using Queue Nodes

#### Queue Memory Usage

When you enqueue and dequeue elements with resizable data types, such as paths, strings and arrays, you do not affect how much memory the queue uses. Queues transfer data but do not generate copies of the data.

#### Preventing Unintended Memory
 Allocation Inside a Loop

When called inside a loop, the Obtain Queue node creates a new
 reference to the queue each time the loop iterates and memory usage increases because each
 new reference is an additional few bytes. These bytes are released automatically when the
 VI stops running. However, in a long-running application, there may appear to be leaking
 memory as memory usage keeps increasing. To prevent unintended memory allocation, use the
 Release Queue node in the loop to release the queue reference from
 memory for each iteration or use Obtain Queue once before the loop
 begins executing.

Parent topic:

Queue Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=octal-digit.html language=enus -->
## TOPIC 00252: Octal Digit?

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `octal-digit.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/octal-digit.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns True if a value represents an octal digit ranging from 0 through 7. Otherwise, this node returns False. If the value is a string, this node uses the first character in the string. If the value is a number, this node interprets it as the ASCII value of a character. If the value is a floating-

Octal Digit?

Returns True if a value represents an octal digit ranging from 0 through 7. Otherwise, this node returns False.

If the value is a string, this node uses the first character in the string. If the value is a number, this node interprets it as the ASCII value of a character. If the value is a floating-point number, this node rounds to the nearest integer.

[IMAGE alt='1378' src='IsOctalDigit.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### char

An input to this operation.

This input supports scalar strings or numbers, clusters of strings or numbers, arrays of strings or numbers, and so on.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### octal?

Boolean result of the operation.

This output assumes the same data type structure as 
 char.

Parent topic:

Comparison Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=octal-string-to-number.html language=enus -->
## TOPIC 00253: Octal String to Number

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `octal-string-to-number.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/octal-string-to-number.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the characters 0 through 7 in a string to an octal integer. string The string that you want to convert. This input can also be any data type that contains only strings, such as an array or cluster of strings. offset The number of characters into the input string at which this node begins it

Octal String to Number

Converts the characters 0 through 7 in a string to an octal integer.

[IMAGE alt='1378' src='OctalStringToNumber.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### string

The string that you want to convert.

This input can also be any data type that contains only strings, such as an array or cluster of strings.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### offset

The number of characters into the input string at which this node begins its operation.

The offset of the first character in the input string is 0. If offset is beyond the end of the input string, this node returns an empty string.

Note

16

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### default

A numeric value whose representation determines the representation of 
number.

Default value: 32-bit unsigned integer

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### offset past number

The index in string of the first character following the number.

If string is an array of strings, offset past number reflects the offset within the last string.

Note

16

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### number

The result of converting string into a number.

number

string

string

number

If the input string represents a number outside the range of the representation of 
 number, 
 number is set to the maximum value for that representation.

#### Examples

string

offset

default

number

| string | offset | default | offset past number | number | Comments |
| --- | --- | --- | --- | --- | --- |
| 92 | 0 | 0 | 0 | 0 | 9 is not an octal digit. |
| 071a | 0 | 0 | 3 | 57 | a is not an octal digit, so conversion stops there. |

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=one-button-dialog.html language=enus -->
## TOPIC 00254: One Button Dialog

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `one-button-dialog.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/one-button-dialog.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Displays a dialog box that contains a custom message and a single button. message The text to display in the dialog box. button name The text to display in the button that appears in the dialog box. Default value: OK true A Boolean value of TRUE when the user clicks the button. TRUE The user clicked

One Button Dialog

Displays a dialog box that contains a custom message and a single button.

[IMAGE alt='1378' src='OneButtonDialog.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### message

The text to display in the dialog box.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### button name

The text to display in the button that appears in the dialog box.

Default value: OK

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### true

A Boolean value of TRUE when the user clicks the button.

| TRUE | The user clicked the button. |
| --- | --- |
| FALSE | This output cannot return FALSE. |

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=one-over-e.html language=enus -->
## TOPIC 00255: 1/e

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `one-over-e.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/one-over-e.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the value 0.36787944117144233.

1/e

Represents the value 0.36787944117144233.

[IMAGE alt='1378' src='Literal.Numeric.1Overe.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=one-over-pi.html language=enus -->
## TOPIC 00256: 1/Pi

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `one-over-pi.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/one-over-pi.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the value 0.31830988618379069.

1/Pi

Represents the value 0.31830988618379069.

[IMAGE alt='1378' src='Literal.Numeric.1OverPi.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=open-component-reference.html language=enus -->
## TOPIC 00257: Open Component Reference (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `open-component-reference.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/open-component-reference.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `lvFunction`
- source_description: Returns a reference to a component, such as a library or GLL, you specify with a name string. Use Open Component Reference to create a component reference for Open VI Reference. Creating a Plugin-Based Test Application component name Name of the component you want to reference. Do not include the fi

Open Component Reference

Returns a reference
 to a component, such as a library or GLL, you specify with a name string.

Use Open Component Reference to create a component reference for
 Open VI Reference.

###### Programming Patterns

- Creating a Plugin-Based Test Application

[IMAGE alt='connector_pane_image' src='OpenComponentReference.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

#### component name

Name of the component you want to reference.

Do not include the file extension in the name you enter.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

#### component reference

Reference to the specified component.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

The node produces this output according to standard error behavior.

This node can return the following error codes.

| -4503 | Some of the Application's GLLs contain incompatible or missing exports. Make sure all VIs and DLLs called by the application are exported in the GLL and have the expected connector pane configuration. Make sure all G Types are compatible. |
| --- | --- |
| 1571 | Packed project libraries are not supported. |
| 1753 or 1754 | The specified component was not found. Make sure the component name you specified is correct. |
| 1755 | One or more dependency GLL was not found. |
| 1757 | Cannot open an application component. Only library components are supported. |
| 1758 | Multiple components with the same name were found. |

Note

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Where This Node Can Run:**

Desktop OS: Windows

FPGA:

Web Server:

Parent topic:

Execution Control

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=open-http-handle.html language=enus -->
## TOPIC 00258: Open HTTP Handle

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `open-http-handle.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/open-http-handle.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a client handle. Use client handles to wire together multiple HTTP nodes while preserving authentication credentials, HTTP headers, and cookies. cookie file Path that allows you to store a client-side cookie. Cookies store data across multiple web requests. Cookie File Storage HTTP nodes on th

Open HTTP Handle

Opens a client handle.
 Use client handles to wire together multiple HTTP nodes while preserving authentication credentials, HTTP headers, and cookies.

[IMAGE alt='1378' src='Open_HTTP_Handle.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cpath.png']

##### cookie file

Path that allows you to store a client-side cookie. Cookies store data across multiple web requests.

##### Cookie File Storage

HTTP nodes on the Web Server target store and maintain cookies that a server creates based on the browser environment and server configurations. The HTTP nodes cannot observe the cookies a server creates or add additional cookies to send to the server. You must set cookie file to an empty path or not a path.

On non-Web Server targets, you must manually specify how to manage the cookies the server creates. If you do not add a cookie file path or extract the cookies from the headers output, you cannot include the cookies in subsequent requests to the server.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### username

Log-in username for the SMTP server you specify. On most public servers, this is your email address.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### password

Log-in password for the SMTP server you specify.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### verify server

Boolean value that determines whether to verify the server's identity and establish a secure connection. Use this input to allow HTTP nodes to communicate using the HTTPS protocol.

| True | Verifies the servers identity and establishes a secure connection. |
| --- | --- |
| False | Does not verify the servers identity or establish a secure connection. |

Default value: True

##### Server Verification on a Web Server Target

HTTP nodes on a Web Server target do not allow you to configure verification of HTTPS servers. You must set this input to True. To work around server verification, you must configure your browser or operating system to connect to servers that you cannot verify.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### client handle out

Unique value that identifies the web request. Use this value to refer to this web request in subsequent node calls.

You can use the same client handle to wire together multiple HTTP nodes to preserve authentication credentials, HTTP headers, and cookies.

Client handles are not required when making independent web requests without persistent data such as headers or credentials.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

HTTP Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=open-item.html language=enus -->
## TOPIC 00259: Open Item

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `open-item.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/open-item.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Expands an item in a tree control to display the child items. reference in Reference to the tree control. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error location Hierarc

Open Item

Expands an item in a tree control to display the child items.

[IMAGE alt='1378' src='OpenTreeItem.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### reference in

Reference to the tree control.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### location

Hierarchical location of the tree item to expand.

If location is empty or unwired, the node expands all items in the tree.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### reference out

Reference to the tree control.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Tree Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=open-python-session.html language=enus -->
## TOPIC 00260: Open Python Session (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `open-python-session.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/open-python-session.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Creates a new Python session. Virtual EnvironmentsYou can reference a Python virtual environment using the virtualenv tool. LabVIEW NXG does not support venv or conda virtual environments. python version Version of Python the session uses when it runs. LabVIEW NXG only supports Python 3.6. Using oth

Open Python Session

Creates a new Python session.

[IMAGE alt='connector_pane_image' src='OpenPythonSession.png']

- Inputs/Outputs
- Details
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

#### python version

Version of Python the session uses when it runs.

Note

[IMAGE alt='datatype_icon' src='/assets/img/cpath.png']

#### python path

Location of the installed Python executable you want to use with this
 session.

Find more information about default Python install paths [here](https://docs.python.org/3/using/).

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

#### session out

Reference to the Python session.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

#### Virtual
 Environments

You can reference a Python virtual environment using the
 [virtualenv](https://virtualenv.pypa.io/en/latest/) tool. LabVIEW NXG does not
 support venv or conda virtual
 environments.

**Where This Node Can Run:**

Desktop OS: Windows

FPGA:

Web Server:

Parent topic:

Python Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=open-registry-key.html language=enus -->
## TOPIC 00261: Open Registry Key

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `open-registry-key.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/open-registry-key.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a reference to a key or subkey in the Windows registry. Incorrectly modifying the registry can damage Windows or prevent you from starting Windows. machine Name of the networked machine. Default value: Empty — The local machine. root key Windows registry root key. HKEY_CLASSES_ROOT Contains in

Open Registry Key

Opens a reference to a key or subkey in the Windows registry.

Caution

[IMAGE alt='1378' src='Open_Registry_Key.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### machine

Name of the networked machine.

Default value: Empty — The local machine.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### root key

Windows registry root key.

| HKEY_CLASSES_ROOT | Contains information about registered applications. |
| --- | --- |
| HKEY_CURRENT_USER | Stores settings that are specific to the currently logged-in user. |
| HKEY_LOCAL_MACHINE | Stores settings that are specific to the local computer. |
| HKEY_USERS | Contains subkeys corresponding to the HKEY_CURRENT_USER keys for each user profile actively loaded on the machine. |
| HKEY_PERFORMANCE_DATA | Provides runtime information into performance data provided by either the Windows NT kernel, or running system drivers, programs and services. |
| HKEY_CURRENT_CONFIG | Contains information gathered at runtime. |
| HKEY_DYN_DATA | Contains information about hardware devices. This key is used only on Windows 95, Windows 98 and Windows ME. |

Default value: HKEY_LOCAL_MACHINE

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### subkey

Name of a subkey of root key.

A beginning backslash 
 \ might cause an error.

Default value: Empty string

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### security access mask

Access rights to assign the key.

| KEY_QUERY_VALUE | Access right to query the values of a registry key. |
| --- | --- |
| KEY_SET_VALUE | Access right to create, delete, or set a registry value. |
| KEY_CREATE_SUB_KEY | Access right to create a subkey of a registry key. |
| KEY_ENUMERATE_SUB_KEYS | Access right to enumerate the subkeys of a registry key. |
| KEY_NOTIFY | Access right to request change notifications for a registry key or for subkeys of a registry key. |
| KEY_CREATE_LINK | Access right reserved for system use. |
| KEY_READ | Access right that combines the STANDARD_RIGHTS_READ, KEY_QUERY_VALUE, KEY_ENUMERATE_SUB_KEYS, and KEY_NOTIFY values. |
| KEY_WRITE | Access right that combines the STANDARD_RIGHTS_WRITE, KEY_SET_VALUE, and KEY_CREATE_SUB_KEY values. |
| KEY_ALL_ACCESS | Access right that combines the STANDARD_RIGHTS_REQUIRED, KEY_QUERY_VALUE, KEY_SET_VALUE, KEY_CREATE_SUB_KEY, KEY_ENUMERATE_SUB_KEYS, KEY_NOTIFY, and KEY_CREATE_LINK values. |
| KEY_READ \| KEY_WRITE | Access right that combines the KEY_READ and KEY_WRITE values. |

Default value: KEY_READ | KEY_WRITE

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### registry view

Value that specifies whether to open a 32-bit key or a 64-bit key on a 64-bit operating system.

| Default | 0 | This node selects the type of key based on the version of the software product that is installed. For example, if the 64-bit version is installed, this node opens a 64-bit key. |
| --- | --- | --- |
| KEY_WOW64_64KEY | 8 | This node opens a 64-bit key. |
| KEY_WOW64_32KEY | 9 | This node opens a 32-bit key. |

Default value: Default

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### reference

Reference to the open registry key.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Registry Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=open-url-in-default-browser.html language=enus -->
## TOPIC 00262: Open URL in Default Browser

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `open-url-in-default-browser.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/open-url-in-default-browser.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Displays a URL or HTML file in the default web browser. URL The URL you want to display in the default web browser. path Path to the file or folder you want to open in your default browser. error in Error conditions that occur before this node runs. The node responds to this input according to stand

Open URL in Default Browser

Displays a URL or HTML file in the default web browser.

[IMAGE alt='1378' src='Open_URL_in_Default_Browser_(string).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### URL

The URL you want to display in the default web browser.

[IMAGE alt='datatype_icon' src='/assets/img/cpath.png']

##### path

Path to the file or folder you want to open in your default browser.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### escaped URL

URL displayed in the web browser.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Space Characters in Path or URL

If the URL or path you wire to this node contains a space character, the node encodes the space as 
 %20 before displaying the URL or HTML file in escaped URL and in the web browser.

Parent topic:

Data Exchange Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=open-vi-reference.html language=enus -->
## TOPIC 00263: Open VI Reference

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `open-vi-reference.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/open-vi-reference.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a reference to a VI you specify with a name string. For a VI exported from a specific library, wire the component reference input. Open VI Reference prepares a VI reference for Call by Reference, Start Asynchronous Call, or Wait on Asynchronous Call to make dynamic calls. Use the Item tab fo

Open VI Reference

Returns a reference to a VI you specify
 with a name string. For a VI exported from a specific library, wire the component
 reference input.

Open VI Reference prepares a VI reference for Call by Reference, Start Asynchronous Call, or Wait on Asynchronous Call to make dynamic calls. Use the 
 **Item** tab for this node to configure the type of call you want to make.

[IMAGE alt='1378' src='OpenVIReference.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### type specifier VI reference

The connector pane information and data type of the VI reference output you specify.

The compiler ignores the actual value of this input. By default, the node returns a generic VI reference.

If you want to use thevi reference output with Call by Reference or Start Asynchronous Call, you must wire a strictly typed VI reference to this input. The connector pane of the VI specified by vi name must match the connector pane of this input.

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### component reference

A reference to a component.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### vi name

The name of the VI you want to reference.

The string you wire to the vi name string must match the full delimited name of a VI in memory on that target.

If you want to use the vi referenceoutput with Call by
 Reference or Start Asynchronous Call, you must wire a
 strictly typed VI reference to type specifier vi reference. The
 connector pane of the VI specified by vi name must match the
 connector pane of type specifier vi reference.

The node does not wait until the user interface is idle, as it does not load a VI from disk.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### vi reference

A reference to the requested VI.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

#### Configuring References for Dynamic VI Calls

If you want to call the specified VI dynamically with Call by Reference or Start Asynchronous Call, you must use appropriate data for the following items:

- type specifier VI reference (for type only)—Wire a strictly typed VI reference to this input.
- Item tab—Use the 
 Item tab for this node to configure the type of call you want to make:
  - Enable simultaneous calls on reentrant
 VIs
    - Prepare for synchronous
 call —Uses Run VI to run multiple instances of
 a reentrant target VI in parallel. Setting this option causes the application to
 allocate a dedicated parallel data space in which a clone of the target VI can
 run. Without this option, Open VI Reference always returns
 a reference to the same data space of the original target VI, preventing
 multiple calls to that VI from executing simultaneously.
    - Prepare for asynchronous
 call without wait —Prepare to call and forget: Use this option when
 you want to call a target VI asynchronously with Start Asynchronous
 Call but you do not need to know when or what the VI returns.
    - Prepare for asynchronous
 call with wait —Prepare to call and collect: Use this option when
 you want to collect the results of an asynchronous call to a target VI with
 Wait on Asynchronous Call . If you use this option, you
 must include one Wait on Asynchronous Call for every call
 that you begin with a Start Asynchronous Call node to
 ensure that the application does not retain any started calls in memory
 indefinitely.

#### Criteria for Opening Strictly Typed References

If you wire a strictly typed VI reference to the type specifier VI reference (for type only), the VI that vi name specifies must meet the following criteria:

- The VI cannot be broken.
- The VI cannot be active as a top-level VI unless the VI is reentrant.
- The connector pane of the VI must match the connector pane of type specifier VI reference (for type only).

#### Opening References to Reentrant VIs

- Dynamic calls to reentrant target VIs execute serially unless you specify otherwise in the 
 Item tab.
- If you configure the VI reference to execute instances of a reentrant target VI in parallel, vi reference refers to the target VI rather than to a clone of the target VI. However, both Call by Reference and Start Asynchronous Call call a clone of the target VI.
- Equal? always returns True when you compare two references to the same reentrant VI. To determine whether the references refer to the same instance of the reentrant VI, use Type Cast to convert the references to 32-bit signed integers. Then use Equal? to compare those integers.

#### Aborting Open References

You can abort all open VI references either manually from the front panel of the VI or by using Abort VI. However, VI references prepared for asynchronous execution have important caveats depending on how you configure the reference:

- Prepare for asynchronous call without wait —A call-and-forget VI aborts only if you manually abort it from its front panel or call Abort VI on it. Otherwise, the VI runs to completion, even if you close the reference or abort the calling VI.
- Prepare for asynchronous call with wait —Call-and-collect VIs abort for the following reasons:
  - You abort the VI that opened the call-and-collect VI reference. In this case, the application aborts all running instances of the VI.
  - You manually abort a specific instance of the VI. In this case, exactly one Wait on Asynchronous Call node returns an error indicating that the called VI aborted. All other Wait on Asynchronous Call nodes that are waiting on calls to the same VI reference continue waiting.
  - You call Abort VI on the call-and-collect VI reference. In this case, the application aborts all currently running instances of the VI. A corresponding number of Wait on Asynchronous Call nodes return errors.

#### Closing Open References

After you finish using a reference that you obtain with this function, close the reference with Close Reference. Explicitly closing a reference enables the application to free the resources involved in maintaining that reference, thereby contributing to optimal memory allocation and performance. Otherwise, the application cannot close the reference until the VI that opened the reference finishes executing.

Note

Prepare for asynchronous call without wait

Parent topic:

Execution Control

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=or-array-elements.html language=enus -->
## TOPIC 00264: OR Array Elements

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `or-array-elements.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/or-array-elements.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns False if all the elements in the input array are False or if the array is empty. Otherwise, this node returns True. This node accepts an array of any size but returns only a single value based on all values in the array. array Array of Boolean elements. logical OR A value that indicates if a

OR Array Elements

Returns False if all the elements in the input array are False or if the array is empty. Otherwise, this node returns True.
 This node accepts an array of any size but returns only a single value based on all values in the array.

[IMAGE alt='1378' src='OrArrayElements.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1dbool.png']

##### array

Array of Boolean elements.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### logical OR

A value that indicates if all of the elements in 
array are False.

| True | One or more elements in array are True, or the array is empty. |
| --- | --- |
| False | All the elements in array are False. |

Parent topic:

Boolean Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=or.html language=enus -->
## TOPIC 00265: OR

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `or.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/or.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the logical OR of the inputs. If all inputs are False, this node returns False. Otherwise, it returns True. This node performs bitwise operations on numeric inputs. input An input to the operation. This input can be any data type that contains only Boolean values, numbers, or error clusters

OR

Computes the logical OR of the inputs. If all inputs are False, this node returns False. Otherwise, it returns True.

This node performs bitwise operations on numeric inputs.

[IMAGE alt='1378' src='LogicalOr.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### input

An input to the operation.

This input can be any data type that contains only Boolean values, numbers, or error clusters, such as an array of numbers or a cluster of Booleans. If this input is an error cluster, the node uses only the 
 status element of the error cluster.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### logical OR

The logical OR of all inputs.

#### Examples

| input 0 | input 1 | logical OR |
| --- | --- | --- |
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |

Parent topic:

Boolean Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=panel-manipulation-nodes.html language=enus -->
## TOPIC 00266: Panel Manipulation Nodes

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `panel-manipulation-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/panel-manipulation-nodes.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configure and manipulate controls and panels.

Panel Manipulation Nodes

Configure and manipulate controls and panels.

Property Node

Reads and/or writes properties of a control reference.

Reinitialize to Default

Resets a control to its default value.

Busy State Nodes

Enable or disable user interactions on the panel.

Tree Nodes

Modify trees.

String Nodes

Modify behavior of string controls.

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=path-to-url.html language=enus -->
## TOPIC 00267: Path to URL

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `path-to-url.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/path-to-url.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a file path into URL format. path Path to the file or folder you want to convert to URL format. URL URL corresponding to the file or folder specified by the path input if the path input is an absolute path. If the path input is a relative path, this node appends the path input to the path o

Path to URL

Converts a file path into URL format.

[IMAGE alt='1378' src='Path_to_URL.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cpath.png']

##### path

Path to the file or folder you want to convert to URL format.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### URL

URL corresponding to the file or folder specified by the path input if the path input is an absolute path.

If the path input is a relative path, this node appends the path input to the path of the folder containing the VI that calls this node.

[IMAGE alt='datatype_icon' src='/assets/img/ipath.png']

##### resolved path

Resolved path corresponding to the path input.

If the path input is an absolute path, the resolved path is the same as the path input. If the path input is a relative path, this node appends the path input to the absolute path of the folder containing the VI that calls this node.

Parent topic:

Data Exchange Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=pi-over-two.html language=enus -->
## TOPIC 00268: Pi/2

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `pi-over-two.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/pi-over-two.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the value 1.5707963267948966.

Pi/2

Represents the value 1.5707963267948966.

[IMAGE alt='1378' src='Literal.Numeric.PiOver2.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=pi-times-two.html language=enus -->
## TOPIC 00269: Pi*2

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `pi-times-two.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/pi-times-two.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the value 6.2831853071795864.

Pi*2

Represents the value 6.2831853071795864.

[IMAGE alt='1378' src='Literal.Numeric.PiTimes2.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=pi.html language=enus -->
## TOPIC 00270: Pi

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `pi.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/pi.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the value 3.1415926535897932.

Pi

Represents the value 3.1415926535897932.

[IMAGE alt='1378' src='Literal.Numeric.Pi.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=pick-line.html language=enus -->
## TOPIC 00271: Pick Line

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `pick-line.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/pick-line.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Copies a specified line from one string and appends that line to another string. string A string to which this node appends the line selected from multi-line string. Default value: Empty string multi-line string One or more substrings separated by linefeeds. line index The number of the line within

Pick Line

Copies a specified line from one string and appends that line to another string.

[IMAGE alt='1378' src='PickLine.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### string

A string to which this node appends the line selected from 
multi-line string.

Default value: Empty string

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### multi-line string

One or more substrings separated by linefeeds.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### line index

The number of the line within a multi-line string that you want to append to string.

The index of the first line is 0. If this input is negative or is greater than or equal to the number of lines in the multi-line string, the node returns string.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### output string

The result of concatenating string and the line selected from multi-line string.

Parent topic:

String Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=plancks.html language=enus -->
## TOPIC 00272: Planck's Constant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `plancks.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/plancks.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value 6.626070040e-34. Planck's constant is a physical constant that is the quantum of action in quantum mechanics.

Planck's Constant

Returns the value 6.626070040e-34. Planck's constant is a physical constant that is the quantum of action in quantum mechanics.

[IMAGE alt='1378' src='Literal.Numeric.Planck_Constant.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=play-sound-file.html language=enus -->
## TOPIC 00273: Play Sound File

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `play-sound-file.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/play-sound-file.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `lvFunction`
- source_description: Opens a file and starts playing it immediately. device ID The input or output device you access for a sound operation. The value ranges from 0 to n-1, where n is the number of input or output devices on the computer. 0 path The absolute path to the file from which you want to play sound data. error

Play Sound File

Opens a file and starts playing it immediately.

[IMAGE alt='connector_pane_image' src='Play_Sound_File.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

#### device ID

The input or output device you access for a sound operation. The value ranges from 0 to 
*n*-1, where 
*n* is the number of input or output devices on the computer.

**Default:**0

[IMAGE alt='datatype_icon' src='/assets/img/cpath.png']

#### path

The absolute path to the file from which you want to play sound data.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

#### timeout

Time, in seconds, that the node waits for the sound operation to complete. This node returns an error if the time elapses, unless **timeout** is set to 0. If you set **timeout** to -1, the node waits indefinitely.

**Default:**0

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

#### task ID

Reference to the configured sound device. You can pass **task ID** to other sound operation nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

Sound Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=polar-to-complex.html language=enus -->
## TOPIC 00274: Polar to Complex

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `polar-to-complex.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/polar-to-complex.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a complex number from two values in polar notation. Given z in rectangular form z = a + bi, this node converts the polar components according to the following equation: z = r * cos ⁡ ( t h e t a ) + i   r * sin ⁡ ( t h e t a ) z = r * cos ⁡ ( t h e t a ) + i   r * sin ⁡ ( t h e t a ) r The d

Polar to Complex

Creates a complex number from two values in polar notation.

Given z in rectangular form z = a + b*i*, this node converts the polar components according to the following equation:

z

=

r

*

cos

⁡

(

t

h

e

t

a

)

+

i

r

*

sin

⁡

(

t

h

e

t

a

)

z

=

r

*

cos

⁡

(

t

h

e

t

a

)

+

i

r

*

sin

⁡

(

t

h

e

t

a

)

[IMAGE alt='1378' src='PolarToComplex.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### r

The distance from the origin to the point, z.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### theta

The angle for the line, r, from the origin to the point, z, in radians.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/icdb.png']

##### z

The complex number.

z

r

theta

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=polar-to-real-and-imaginary.html language=enus -->
## TOPIC 00275: Polar to Real and Imaginary

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `polar-to-real-and-imaginary.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/polar-to-real-and-imaginary.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the polar components of a complex number into its rectangular components. This node converts the polar components to rectangular components using following equations: x = r * cos ⁡ ( t h e t a ) x = r * cos ⁡ ( t h e t a ) y = r * sin ⁡ ( t h e t a ) y = r * sin ⁡ ( t h e t a ) r The distan

Polar to Real and Imaginary

Converts the polar components of a complex number into its rectangular components.

This node converts the polar components to rectangular components using following equations:

x

=

r

*

cos

⁡

(

t

h

e

t

a

)

x

=

r

*

cos

⁡

(

t

h

e

t

a

)

y

=

r

*

sin

⁡

(

t

h

e

t

a

)

y

=

r

*

sin

⁡

(

t

h

e

t

a

)

[IMAGE alt='1378' src='PolarToRealAndImaginary.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### r

The distance from the origin to the point, z.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### theta

The angle for the line, r, from the origin to the point, z, in radians.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### x

The x rectangular component of x + yi.

x

r

theta

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### y

The y rectangular component of x + yi.

y

r

theta

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=positive-infinity.html language=enus -->
## TOPIC 00276: Positive Infinity

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `positive-infinity.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/positive-infinity.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the value infinity.

Positive Infinity

Represents the value infinity.

[IMAGE alt='1378' src='Literal.Numeric.Positive_Infinity.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=post-buffer.html language=enus -->
## TOPIC 00277: POST Buffer

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `post-buffer.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/post-buffer.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends data within the buffer input to the URL you specify. This node uses the POST HTTP method. Unlike a PUT request, POST requests do not require all available property and attribute values when updating a resource. You can choose to send all values to update the entire resource or just a subset of

POST Buffer

Sends data within the buffer input to the URL you specify.

This node uses the POST HTTP method. Unlike a PUT request, POST requests do not require all available property and attribute values when updating a resource. You can choose to send all values to update the entire resource or just a subset of the available values.

[IMAGE alt='1378' src='POST_Buffer.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cpath.png']

##### output file

File to save body data returned by the server. If you do not specify an output file, the node does not save the body data to a file.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### client handle

Unique value that identifies the web request. You can use the same client handle to wire together multiple HTTP nodes to preserve authentication credentials, HTTP headers, and cookies. Client handles are not required when making independent web requests without persistent data such as headers or credentials.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### url

URL of the server, web page, or web service where this node will send the web request.

##### Relative URL behavior

If you do not specify a URL scheme on a Web Server target, each URL you enter is relative to the location the WebVI is hosted. The WebVI sends HTTP requests to the server at the relative URL. For example, if you host the WebVI on http://website.com/MyApp/, specifying the relative URL 
 subdirectory/myfile.txt sends an HTTP request to http://website.com/MyApp/subdirectory/myfile.txt.

If you do not specify a URL scheme on a non-Web Server target, the node prefixes http:// to the URL and treats it as an absolute URL.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### buffer

String of data to send to the server.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### timeout

Amount of time in milliseconds you must wait to obtain a response from the server before the web request times out. A value of -1 defers timeout monitoring to the operating system.

Default value: 10000 ms

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### status code

Status code information returned by the server.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### client handle out

Unique value that returns data back to the node. You can use the same client handle to wire together multiple HTTP nodes to preserve authentication credentials, HTTP headers, and cookies. Client handles are not required when making independent web requests without persistent data such as headers or credentials.

[IMAGE alt='datatype_icon' src='/assets/img/i1dstr.png']

##### headers

Header fields returned by the server. Refer to the World Wide Web Consortium website at [www.w3.org](http://digital.ni.com/express.nsf/bycode/exctg8) for more information about header field definitions including available headers, descriptions, and syntax.

[IMAGE alt='datatype_icon' src='/assets/img/i1dstr.png']

##### body

Body data that is returned by the server.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### CORS Restrictions on HTTP Requests

Requests from HTTP clients are subject to CORS restrictions when the WebVI communicates with a web service on a different origin. The web service responding to the HTTP request must return a valid CORS configuration for the HTTP request to complete successfully.

On non-Web Server targets, HTTP requests are not subject to CORS restrictions. The VI can make HTTP requests regardless of the CORS configuration of the server.

Note

#### Cached Response Behavior for Repeat Requests

HTTP nodes on a Web Server target may create caches of responses to HTTP requests. If a duplicate request occurs, the HTTP nodes can avoid querying the network by returning a previous response from the cache. The specific browser environment and server configuration determine the behavior of the cache.

On non-Web Server targets, every HTTP request creates a unique network request.

#### Forbidden Headers on a Web Server

A WebVI cannot transmit or receive specific 
 [forbidden headers](https://developer.mozilla.org/en-us/docs/glossary/forbidden_header_name) in HTTP requests. For header transmissions, the request to the server does not include forbidden headers. When the HTTP nodes receive a forbidden header from a server, they exclude the header from the headers output. Additionally, the CORS configuration of a server may exclude some headers in server requests or from server responses.

On non-Web Server targets, you do not need to account for forbidden headers in HTTP requests.

#### Default Content-Type for HTTP Request

If you do not specify a Content-Type header for an HTTP request, this node adds the 
 application/x-www-url-formencoded Content-Type header to the request by default.

Parent topic:

POST

Related reference:

- PUT
- PUT Buffer

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=post.html language=enus -->
## TOPIC 00278: POST

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `post.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/post.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends data to the URL you specify. This node uses the POST HTTP method. Unlike a PUT request, POST requests do not require all available property and attribute values when updating a resource. You can choose to send all values to update the entire resource or just a subset of the available values.

POST

Sends data to the URL you specify.

This node uses the POST HTTP method. Unlike a PUT request, POST requests do not require all available property and attribute values when updating a resource. You can choose to send all values to update the entire resource or just a subset of the available values.

HTTP Nodes

Build a web client that interacts with servers, web pages, and web services with Hypertext Transfer Protocol (HTTP).

POST Buffer

buffer

PUT

Creates or updates data and sends it to the URL you specify.

PUT Buffer

buffer

Parent topic:

HTTP Nodes

Related reference:

- PUT
- PUT Buffer

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=preserve-run-time-class.html language=enus -->
## TOPIC 00279: Preserve Run-Time Class

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `preserve-run-time-class.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/preserve-run-time-class.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `lvFunction`
- source_description: Typecasts a class object to a class you specify if both are in the same inheritance hierarchy. Automatic Typecasting Behavior If you wire a child class to a subVI that accepts and returns a parent class in the inheritance hierarchy, the subVI automatically typecasts the class output to the same chil

Preserve Run-Time Class

Typecasts a class object to a class you specify if both are in the same inheritance hierarchy.

[IMAGE alt='connector_pane_image' src='PreserveRunTimeClass.png']

- Inputs/Outputs
- Details
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/clabview_objectlvclass.png']

#### target object

Class object whose class you want **object in** to match.

[IMAGE alt='datatype_icon' src='/assets/img/clabview_objectlvclass.png']

#### object in

Class object whose class you want to typecast to that of **target object**.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/ilabview_objectlvclass.png']

#### object out

Class object of the same class as **target object**.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

#### Automatic Typecasting Behavior

If you wire a child class to a subVI that accepts and returns a parent class in the inheritance hierarchy, the subVI automatically typecasts the class output to the same child class as the input. However, the class output is not automatically typecast if the subVI cannot verify that the class data type of a wire does not change across the diagram. When the class data type of a wire does not change across the diagram of a subVI, use Preserve Run-Time Class to typecast the class output immediately before returning it from the subVI.

Parent topic:

Classes Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=preview-queue-element.html language=enus -->
## TOPIC 00280: Preview Queue Element

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `preview-queue-element.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/preview-queue-element.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the element at the front of the queue without removing the element from the queue. If the queue becomes invalid because the queue reference is released, this node stops waiting and returns an error. To return and remove the element from the queue, use Dequeue Element instead. queue A referen

Preview Queue Element

Returns the element at the front of the queue without removing the element from the queue.

If the queue becomes invalid because the queue reference is released, this node stops waiting and returns an error.

Note

[IMAGE alt='1378' src='PreviewQueueElement.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### queue

A reference to a queue.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### timeout in milliseconds

The number of milliseconds that the node waits for an element to become available in the queue if the queue is empty.

If an element becomes available in the queue during the wait, the node removes and returns the element and does not time out.

Default value: -1 — The node never times out.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: no error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### queue out

Reference to the queue.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### element

A copy of the element at the front of the queue.

The data type of this output changes to match the data type of the queue elements.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### timed out?

A Boolean value that indicates whether an element became available in the queue before the node timed out or if an error occurred.

| True | An element did not become available before the node timed out or this node generated an error. |
| --- | --- |
| False | An element did become available before the node timed out or an error occurred before this node executed. |

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

The node produces this output according to standard error behavior.

This node can return the following error codes.

| 1122 | The reference became invalid while the node was waiting for it. |
| --- | --- |

Note

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Queue Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=programming-flow-nodes.html language=enus -->
## TOPIC 00281: Program Flow Nodes

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `programming-flow-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/programming-flow-nodes.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`

Program Flow Nodes

Call Chain

Returns an array of every VI that calls this node, from the current VI to the top-level VI.

Case Structure

Contains one or more subdiagrams, or cases, exactly one of which executes when the structure executes.

Disable Structure

Contains one or more subdiagrams, or cases, of which only the enabled subdiagram executes.

Event Loop

Creates an Event Structure within a While Loop.

First Call?

Indicates whether the diagram or subdiagram containing this node is running for the first time since the top-level caller began execution.

For Loop

n

Select

Returns one of two specified values depending on a Boolean value.

Sequence Structure

Consists of one or more subdiagrams, or frames, that execute sequentially.

Use the Sequence Structure to ensure that a subdiagram executes before or after another subdiagram.

Timer Count

Returns the value of the timer.

Wait

Waits a specified amount of time.

Wait Until Next Multiple

Waits until the value of the operating system's timer becomes a multiple of a specified amount of time. Use this node to synchronize activities.

While Loop

Repeats the code on its subdiagram until a specific condition occurs.

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=property-node.html language=enus -->
## TOPIC 00282: Property Node

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `property-node.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/property-node.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads and/or writes properties of a control reference. This node adapts to the class of the object you reference. instance in Control reference associated with the object for which you want to set or get properties. error in Error conditions that occur before this node runs. The node responds to thi

Property Node

Reads and/or writes properties of a control reference. This node adapts to the class of the object you reference.

[IMAGE alt='1378' src='PropertyNode.Void.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cvoid.png']

##### instance in

Control reference associated with the object for which you want to set or get properties.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ivoid.png']

##### instance out

Control reference specified by instance in.

If you wrote any values to Property Node, the value of instance out may differ from instance in.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ivoid.png']

##### (property)

The element of the node that you want to read or write.

By default, this element is configured to read. To write this element, right-click the element and select 
 Change to write.

To access more elements, resize the node.

Parent topic:

.NET Nodes

Parent topic:

Panel Manipulation Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=put-buffer.html language=enus -->
## TOPIC 00283: PUT Buffer

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `put-buffer.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/put-buffer.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates or updates data within the buffer input and sends the data to the URL you specify. Unlike a POST request, PUT requests require all available property and attribute values to be present because the PUT request updates all data within the resource. Adding all available property and attribute v

PUT Buffer

Creates or updates data within the buffer input and sends the data to the URL you specify.

Unlike a POST request, PUT requests require all available property and attribute values to be present because the PUT request updates all data within the resource. Adding all available property and attribute values will guarantee that the operation can be performed multiple times without changing the result beyond the initial application.

[IMAGE alt='1378' src='PUT_Buffer.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cpath.png']

##### output file

File to save body data returned by the server. If you do not specify an output file, the node does not save the body data to a file.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### client handle

Unique value that identifies the web request. You can use the same client handle to wire together multiple HTTP nodes to preserve authentication credentials, HTTP headers, and cookies. Client handles are not required when making independent web requests without persistent data such as headers or credentials.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### url

URL of the server, web page, or web service where this node will send the web request.

##### Relative URL behavior

If you do not specify a URL scheme on a Web Server target, each URL you enter is relative to the location the WebVI is hosted. The WebVI sends HTTP requests to the server at the relative URL. For example, if you host the WebVI on http://website.com/MyApp/, specifying the relative URL 
 subdirectory/myfile.txt sends an HTTP request to http://website.com/MyApp/subdirectory/myfile.txt.

If you do not specify a URL scheme on a non-Web Server target, the node prefixes http:// to the URL and treats it as an absolute URL.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### buffer

String of data to send to the server.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### timeout

Amount of time in milliseconds you must wait to obtain a response from the server before the web request times out. A value of -1 defers timeout monitoring to the operating system.

Default value: 10000 ms

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### status code

Status code information returned by the server.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### client handle out

Unique value that returns data back to the node. You can use the same client handle to wire together multiple HTTP nodes to preserve authentication credentials, HTTP headers, and cookies. Client handles are not required when making independent web requests without persistent data such as headers or credentials.

[IMAGE alt='datatype_icon' src='/assets/img/i1dstr.png']

##### headers

Header fields returned by the server. Refer to the World Wide Web Consortium website at [www.w3.org](http://digital.ni.com/express.nsf/bycode/exctg8) for more information about header field definitions including available headers, descriptions, and syntax.

[IMAGE alt='datatype_icon' src='/assets/img/i1dstr.png']

##### body

Body data that is returned by the server.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### CORS Restrictions on HTTP Requests

Requests from HTTP clients are subject to CORS restrictions when the WebVI communicates with a web service on a different origin. The web service responding to the HTTP request must return a valid CORS configuration for the HTTP request to complete successfully.

On non-Web Server targets, HTTP requests are not subject to CORS restrictions. The VI can make HTTP requests regardless of the CORS configuration of the server.

Note

#### Cached Response Behavior for Repeat Requests

HTTP nodes on a Web Server target may create caches of responses to HTTP requests. If a duplicate request occurs, the HTTP nodes can avoid querying the network by returning a previous response from the cache. The specific browser environment and server configuration determine the behavior of the cache.

On non-Web Server targets, every HTTP request creates a unique network request.

#### Forbidden Headers on a Web Server

A WebVI cannot transmit or receive specific 
 [forbidden headers](https://developer.mozilla.org/en-us/docs/glossary/forbidden_header_name) in HTTP requests. For header transmissions, the request to the server does not include forbidden headers. When the HTTP nodes receive a forbidden header from a server, they exclude the header from the headers output. Additionally, the CORS configuration of a server may exclude some headers in server requests or from server responses.

On non-Web Server targets, you do not need to account for forbidden headers in HTTP requests.

#### Default Content-Type for HTTP Request

If you do not specify a Content-Type header for an HTTP request, this node adds the 
 application/x-www-url-formencoded Content-Type header to the request by default. However, on non-Web Server targets this node does not add a Content-Type header to requests.

Parent topic:

PUT

Related reference:

- POST
- POST Buffer

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=put.html language=enus -->
## TOPIC 00284: PUT

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `put.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/put.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates or updates data and sends it to the URL you specify. Unlike a POST request, PUT requests require all available property and attribute values to be present because the PUT request updates all data within the resource. Adding all available property and attribute values will guarantee that the

PUT

Creates or updates data and sends it to the URL you specify.

Unlike a POST request, PUT requests require all available property and attribute values to be present because the PUT request updates all data within the resource. Adding all available property and attribute values will guarantee that the operation can be performed multiple times without changing the result beyond the initial application.

HTTP Nodes

Build a web client that interacts with servers, web pages, and web services with Hypertext Transfer Protocol (HTTP).

PUT Buffer

buffer

POST

Sends data to the URL you specify.

POST Buffer

buffer

Parent topic:

HTTP Nodes

Related reference:

- POST
- POST Buffer

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=python.html language=enus -->
## TOPIC 00285: Python Nodes (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `python.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/python.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `nodeCollection`
- source_description: Open and close Python sessions, and call Python functions.

Python
 Nodes

Open and close Python sessions, and call Python functions.

Call Python Function

Calls a function within a Python file and returns the output.

Close Python Session

Closes a Python session.

Open Python Session

Creates a new Python session.

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=query-input-devices.html language=enus -->
## TOPIC 00286: Query Input Devices

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `query-input-devices.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/query-input-devices.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Obtains information about the devices connected to the computer. Behavior with Multiple Devices of the Same Type If you connect more than one mouse or keyboard to your computer, this node recognizes only the first mouse or keyboard. error in Error conditions that occur before this node runs. The nod

Query Input Devices

Obtains information about the devices connected to the computer.

[IMAGE alt='connector_pane_image' src='Query_Input_Devices.gvi.png']

- Inputs/Outputs
- Details
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/i1dcclst.png']

#### joystick info

An array of information about the joysticks connected to the computer.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### axes total

Total number of axes for each joystick connected to the computer.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### buttons total

Total number of buttons for each joystick connected to the computer.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### pov total

Total number of points of view for each joystick connected to the computer.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### device name

Device name of each joystick connected to the computer.

[IMAGE alt='datatype_icon' src='/assets/img/i1dcclst.png']

#### keyboard info

An array of information about the keyboards connected to the computer.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### buttons total

Number of keys on the keyboard connected to the computer.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### device name

Device name of the keyboard connected to the computer.

[IMAGE alt='datatype_icon' src='/assets/img/i1dcclst.png']

#### mouse info

An array of information about the mouse connected to the computer.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### axes total

Total number of axes for the mouse connected to the computer.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### buttons total

Total number of buttons for the mouse connected to the computer.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### device name

Device name of the mouse connected to the computer.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

#### Behavior with Multiple Devices of the Same Type

If you connect more than one mouse or keyboard to your computer, this node recognizes only the first mouse or keyboard.

Parent topic:

Input Device Control Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=query-registry-key-info.html language=enus -->
## TOPIC 00287: Query Registry Key Info

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `query-registry-key-info.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/query-registry-key-info.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Retrieves information about keys. Incorrectly modifying the registry can damage Windows or prevent you from starting Windows. reference in Reference to the open registry key. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behav

Query Registry Key Info

Retrieves information about keys.

Caution

[IMAGE alt='1378' src='Query_Registry_Key_Info.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### reference in

Reference to the open registry key.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### reference out

Reference to the open registry key.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### class

Class or object type of the key.

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### value info

Set of parameters describing the set of values and data.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### numValues

Number of values under the key specified by hKey.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### maxValueNameLen

Length of the longest value name under the key specified by hKey.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### maxValueDataLen

Length of the longest datum under the key specified by hKey.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### subkey info

Set of parameters describing the subkeys.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### numSubKeys

Number of subkeys under the key specified by hKey.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### maxSubKeyLen

Length of the longest subkey name under the key specified by hKey.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### maxSubKeyClassLen

Length of the longest class name under the key specified by hKey.

Parent topic:

Registry Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=queue-nodes.html language=enus -->
## TOPIC 00288: Queue Nodes

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `queue-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/queue-nodes.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create a queue for communicating data between sections of a diagram or from another VI.

Queue Nodes

Create a queue for communicating data between sections of a diagram or from another VI.

Data Exchange Nodes

Dequeue Element

Removes an element from the front of a queue and returns the element.

Enqueue Element

Adds an element to the back of a queue.

Enqueue Element At Opposite End

Adds an element to the front of a queue.

Flush Queue

Removes all elements from a queue and returns the elements as an array.

Get Queue Status

Returns information about the current state of a queue, such as the number of elements currently in the queue.

Lossy Enqueue Element

Adds an element to the back of a queue. Unlike Enqueue Element, this node does not wait for space in the queue to become available. If no space is available in the queue, this node discards an element from the front of the queue to make space.

Obtain Queue

Returns a reference to a queue or creates a new reference to a queue.

Preview Queue Element

Returns the element at the front of the queue without removing the element from the queue.

Release Queue

Releases a reference to a queue.

Parent topic:

Data Exchange Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=quotient-and-remainder.html language=enus -->
## TOPIC 00289: Quotient and Remainder

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `quotient-and-remainder.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/quotient-and-remainder.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the integer quotient and the remainder of the inputs. x The dividend. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. y The divisor. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. re

Quotient and Remainder

Computes the integer quotient and the remainder of the inputs.

[IMAGE alt='1378' src='QuotientAndRemainder.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

The dividend.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### y

The divisor.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### remainder

The remainder.

y

x

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### quotient

The integer quotient.

quotient

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=random-number-range-dbl.html language=enus -->
## TOPIC 00290: DBL

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `random-number-range-dbl.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/random-number-range-dbl.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates a random value from a specified range. This node returns a value greater than or equal to lower bound and less than upper bound. If upper bound is less than or equal to lower bound, this node returns lower bound. upper bound The upper limit of the range. Default value: 100 lower bound The

DBL

Generates a random value from a specified range.

This node returns a value greater than or equal to lower bound and less than upper bound. If upper bound is less than or equal to lower bound, this node returns lower bound.

[IMAGE alt='1378' src='Random_Number_(Range)_DBL.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### upper bound

The upper limit of the range.

Default value: 100

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### lower bound

The lower limit of the range.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### number

A random number greater than or equal to lower bound and less than upper bound.

Parent topic:

Random Number (Range)

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=random-number-range.html language=enus -->
## TOPIC 00291: Random Number (Range)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `random-number-range.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/random-number-range.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates a random value from a specified range.

Random Number (Range)

Generates a random value from a specified range.

Numeric Nodes

DBL

Generates a random value from a specified range.

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=random-number.html language=enus -->
## TOPIC 00292: Random Number

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `random-number.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/random-number.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Generates a double-precision, floating-point number between 0 and 1. random number A double-precision, floating-point number between 0 and 1. The generated number is greater than or equal to 0, but less than 1. The distribution is uniform.

Random Number

Generates a double-precision, floating-point number between 0 and 1.

[IMAGE alt='1378' src='RandomNumber.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### random number

A double-precision, floating-point number between 0 and 1.

The generated number is greater than or equal to 0, but less than 1. The distribution is uniform.

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=read-call-chain.html language=enus -->
## TOPIC 00293: Read Call Chain

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `read-call-chain.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/read-call-chain.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the call chain from where the error or warning occurred. error in An error cluster that you use to check for errors or warnings. Standard Error Behavior call chain An array of names representing the chain of callers from the location that the error or warning occurred to the current VI. This

Read Call Chain

Returns the call chain from where the error or warning occurred.

[IMAGE alt='1378' src='Read_Call_Chain.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

An error cluster that you use to check for errors or warnings.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/i1dstr.png']

##### call chain

An array of names representing the chain of callers from the location that the error or warning occurred to the current VI.

This array is empty if there is no error, the call chain has been overwritten with a string that describes the location at which the error occurred, or there is no location information at all.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### has location?

A Boolean that indicates whether you replaced the call chain with a string that describes the location at which the error occurred.

| True | The error cluster has location information other than a call chain. Use Read Location to access the information. |
| --- | --- |
| False | The error cluster has no location information. |

Parent topic:

Error Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=read-error-code.html language=enus -->
## TOPIC 00294: Read Error Code

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `read-error-code.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/read-error-code.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the error code of an error cluster. error in An error cluster that you use to check for errors or warnings. Standard Error Behavior code The error or warning code of the error cluster. If there is no error, this is 0.

Read Error Code

Returns the error code of an error cluster.

[IMAGE alt='1378' src='Read_Error_Code.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

An error cluster that you use to check for errors or warnings.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### code

The error or warning code of the error cluster.

0

Parent topic:

Error Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=read-location.html language=enus -->
## TOPIC 00295: Read Location

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `read-location.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/read-location.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string that describes where the error or warning occurred. Use this node if the code that generated the error overrides the call chain because the location at which the error occurred cannot be described by a call chain. For example, if the error occurred across a network connection the lo

Read Location

Returns a string that describes where the error or warning occurred. Use this node if the code that generated the error overrides the call chain because the location at which the error occurred cannot be described by a call chain. For example, if the error occurred across a network connection the location might be network URL or a more specific string describing the location.

[IMAGE alt='1378' src='Read_Location.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

An error cluster that you use to check for errors or warnings.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### location

A string describing where the error or warning occurred.

This string is empty if the error cluster contains no location information. If the error cluster contains a call chain, this node returns the call chain formatted as a single, multiline string.

Parent topic:

Error Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=read-registry-value-simple-string.html language=enus -->
## TOPIC 00296: String

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `read-registry-value-simple-string.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/read-registry-value-simple-string.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads data and the simplified data type from a registry value. If the key or value does not exist or an unrecoverable error occurs, the node returns the default data. Incorrectly modifying the registry can damage Windows or prevent you from starting Windows. reference in Reference to the open regist

String

Reads data and the simplified data type from a registry value.

If the key or value does not exist or an unrecoverable error occurs, the node returns the default data.

Caution

[IMAGE alt='1378' src='Read_Registry_Value_Simple_STR.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### reference in

Reference to the open registry key.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### value

Name of the registry value.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### default data

Data to return if value is not found or if an unrecoverable error occurs.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### reference out

Reference to the open registry key.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### simple data type

Simplified Windows registry type.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### string/binary data

Data of Windows registry type 
String or 
Binary.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Read Registry Value Simple

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=read-registry-value-simple-u32.html language=enus -->
## TOPIC 00297: U32

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `read-registry-value-simple-u32.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/read-registry-value-simple-u32.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads data and the simplified data type from a registry value. If the key or value does not exist or an unrecoverable error occurs, the node returns the default data. Incorrectly modifying the registry can damage Windows or prevent you from starting Windows. reference in Reference to the open regist

U32

Reads data and the simplified data type from a registry value.

If the key or value does not exist or an unrecoverable error occurs, the node returns the default data.

Caution

[IMAGE alt='1378' src='Read_Registry_Value_Simple_U32.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### reference in

Reference to the open registry key.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### value

Name of the registry value.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### default data

Data to return if value is not found or if an unrecoverable error occurs.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### reference out

Reference to the open registry key.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### simple data type

Simplified Windows registry type.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### DWORD data

Data of Windows registry type 
DWORD.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Read Registry Value Simple

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=read-registry-value-simple.html language=enus -->
## TOPIC 00298: Read Registry Value Simple

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `read-registry-value-simple.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/read-registry-value-simple.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads data and the simplified data type from a registry value.

Read Registry Value Simple

Reads data and the simplified data type from a registry value.

Registry Nodes

String

Reads data and the simplified data type from a registry value.

U32

Reads data and the simplified data type from a registry value.

Parent topic:

Registry Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=real-and-imaginary-to-complex.html language=enus -->
## TOPIC 00299: Real and Imaginary to Complex

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `real-and-imaginary-to-complex.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/real-and-imaginary-to-complex.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a complex number from two values in rectangular notation. x The x rectangular component of x + yi. This input supports scalar numbers, arrays or clusters of numbers, arrays of clusters of numbers, and waveforms. y The y rectangular component of x + yi. This input supports scalar numbers, arr

Real and Imaginary to Complex

Creates a complex number from two values in rectangular notation.

[IMAGE alt='1378' src='RealAndImaginaryToComplex.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

The x rectangular component of x + yi.

This input supports scalar numbers, arrays or clusters of numbers, arrays of clusters of numbers, and waveforms.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### y

The y rectangular component of x + yi.

This input supports scalar numbers, arrays or clusters of numbers, arrays of clusters of numbers, and waveforms.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/icdb.png']

##### x + yi

The complex number.

x + yi has the same structure as the input, with complex representation instead of scalar.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=real-and-imaginary-to-polar.html language=enus -->
## TOPIC 00300: Real and Imaginary to Polar

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `real-and-imaginary-to-polar.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/real-and-imaginary-to-polar.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the rectangular components of a complex number into its polar components. This node converts the rectangular components to polar components using the following equations: r = x 2 + y 2 r = x 2 + y 2 t h e t a = arctan 2 ( y , x )   r a d i a n s t h e t a = arctan 2 ( y , x )   r a d i a n

Real and Imaginary to Polar

Converts the rectangular components of a complex number into its polar components.

This node converts the rectangular components to polar components using the following equations:

r

=

x

2

+

y

2

r

=

x

2

+

y

2

t

h

e

t

a

=

arctan

2

(

y

,

x

)

r

a

d

i

a

n

s

t

h

e

t

a

=

arctan

2

(

y

,

x

)

r

a

d

i

a

n

s

[IMAGE alt='1378' src='RealAndImaginaryToPolar.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

The x rectangular component of x + yi.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### y

The y rectangular component of x + yi.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### r

The distance from the origin to the point.

r

x

y

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### theta

The angle for the line, r, from the origin to the point in radians.

theta

x

y

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=reciprocal.html language=enus -->
## TOPIC 00301: Reciprocal

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `reciprocal.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/reciprocal.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Divides 1 by the input value. x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, arrays of clusters of numbers, and waveforms. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, this input has a default data type that use

Reciprocal

Divides 1 by the input value.

[IMAGE alt='1378' src='Reciprocal.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, arrays of clusters of numbers, and waveforms.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### 1 / x

The reciprocal of the input value.

##### Behavior with Various x Input Types

If x is 0, 1 / x is infinity. If x is an integer, 1 / x is a double-precision, floating-point number.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=register-for-events.html language=enus -->
## TOPIC 00302: Register For Events

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `register-for-events.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/register-for-events.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Registers events for use with an Event Structure. The events that you can register depend on the type of the reference you wire to each event source input. event registration refnum Reference to an existing event registration that a Register For Events node created. error in Error conditions that oc

Register For Events

Registers events for use with an Event Structure.
 The events that you can register depend on the type of the reference you wire to each event source input.

[IMAGE alt='1378' src='RegisterForEvents.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### event registration refnum

Reference to an existing event registration that a Register For Events node created.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### event source 1..n

Reference to a user event or device event, such as a DAQ event. The reference you wire to this input must be to a local object. You cannot wire a reference to an object on a remote computer or other hardware.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### event registration refnum

Reference to the new or modified event registration. Wire this output to another Event node that accepts event registration refnums, such as an Event Structure or Register For Events node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

- Executing
 Code Based on a User Event

#### Dynamic Event Registration

With dynamic events, you can design an application to make programmatic changes to elements in the VI and the VI generates events for these changes. Use the Register for Events node to perform event registration for dynamic events.

#### Behavior when Dynamically Modifying Event Registration

You can dynamically modify event registration by wiring theevent registration refnum output of one Register for Events node to the event registration refnum input of a second Register for Events node. In this configuration, the second Register for Events node inherits the event sources from the first Register for Events node. The following caveats apply to the Register for Events node when you wire its event registration refnum input:

- You must place the Register for Events node inside an event case.
- You cannot manually resize or reconfigure the Register for Events node while the event registration refnum input is wired.
- You must wire the event source 1..n inputs with the same types of references you specified in the Register for Events node that originally created the event registration reference.
- When you wire an event source 1..n input, Register for Events unregisters the original event source and registers the new event source.
- Wire a Not A Refnum constant to an event source 1..n input to unregister the original event source without registering a new event source.

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=registry-nodes.html language=enus -->
## TOPIC 00303: Registry Nodes

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `registry-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/registry-nodes.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`

Registry Nodes

Close Registry Key

Closes a key in the Windows registry.

Create Registry Key

Creates a key in the Windows registry or opens the key, if it already exists.

Delete Registry Key

Deletes a specific key or subkey.

Delete Registry Value

Deletes a specific value for a specific key.

Enum Registry Keys

Enumerates subkeys of a specific key or subkey.

Enum Registry Values Simple

Enumerates the values for a specific key or subkey.

Open Registry Key

Opens a reference to a key or subkey in the Windows registry.

Query Registry Key Info

Retrieves information about keys.

Read Registry Value Simple

Reads data and the simplified data type from a registry value.

Write Registry Value Simple

Writes data to a registry value under a key.

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=reinitialize-to-default.html language=enus -->
## TOPIC 00304: Reinitialize to Default

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `reinitialize-to-default.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/reinitialize-to-default.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets a control to its default value. This node does not change the value of a dynamically created control. reference in Reference to the control. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavio

Reinitialize to Default

Resets a control to its default value.

This node does not change the value of a dynamically created control.

[IMAGE alt='1378' src='ReinitializeToDefault.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### reference in

Reference to the control.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### reference out

Reference to the control.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Panel Manipulation Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=release-queue.html language=enus -->
## TOPIC 00305: Release Queue

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `release-queue.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/release-queue.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Releases a reference to a queue. queue A reference to a queue. force destroy A Boolean value that determines whether to release all references to the queue. Releasing all references to a queue destroys the queue, which deletes any elements in the queue and invalidates all references to the queue. Yo

Release Queue

Releases a reference to a queue.

[IMAGE alt='1378' src='ReleaseQueue.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### queue

A reference to a queue.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### force destroy

A Boolean value that determines whether to release all references to the queue.

Note

| True | The node releases all references to the queue. |
| --- | --- |
| False | The node only releases the specified reference to the queue. This does not destroy the queue unless a reference to the queue has only been obtained once. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### queue name

The name of the queue, if the queue is named.

[IMAGE alt='datatype_icon' src='/assets/img/i1dstr.png']

##### remaining elements

The array of elements that were in the queue before the node released the queue.

The first element in the array is the element from the front of the queue, and the last element in the array is the element from the back of the queue.

The data type of the array elements changes to match the data type of the queue elements.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

Transferring Data Between Loops Using Queue Nodes

#### Releasing Multiple References to the Same Queue

If you obtain a reference to the same queue multiple times, you can release multiple references to that queue by calling Release Queue up to the same number of times that you obtained the reference. Releasing all references to a queue destroys the queue and deletes any elements in the queue.

If you are not using a loop to release references as they are obtained or otherwise keeping track of the number of times you obtain a reference, you can also destroy a queue with a single Release Queue node using force destroy?.

Parent topic:

Queue Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=remove-header.html language=enus -->
## TOPIC 00306: Remove Header

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `remove-header.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/remove-header.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes a header field line from all web requests associated with the client handle. Headers define attributes of the data exchanged between the client and server. client handle Unique value that identifies the web request. You can use the same client handle to wire together multiple HTTP nodes to p

Remove Header

Removes a header field line from all web requests associated with the client handle.
 Headers define attributes of the data exchanged between the client and server.

[IMAGE alt='1378' src='Remove_Header.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### client handle

Unique value that identifies the web request.

You can use the same client handle to wire together multiple HTTP nodes to preserve authentication credentials, HTTP headers, and cookies.

Client handles are not required when making web requests without persistent data such as headers or credentials.

[IMAGE alt='datatype_icon' src='/assets/img/c1dstr.png']

##### header

Header field included in the web requests of the client handle. The header control provides a pull-down menu with available header fields.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### client handle out

Unique value that returns data back to the node. You can use the same client handle to wire together multiple HTTP nodes to preserve authentication credentials, HTTP headers, and cookies. Client handles are not required when making independent web requests without persistent data such as headers or credentials.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

HTTP Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=replace-array-subset.html language=enus -->
## TOPIC 00307: Replace Array Subset

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `replace-array-subset.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/replace-array-subset.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Replaces an element or subarray in an array at the index you specify. array The array in which you want to replace elements, rows, columns, or pages. This input is an n-dimension array of any type. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, this input has a d

Replace Array Subset

Replaces an element or subarray in an array at the index you specify.

[IMAGE alt='1378' src='ReplaceArraySubset.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### array

The array in which you want to replace elements, rows, columns, or pages. This input is an 
n-dimension array of any type.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### index

Location within 
array of the element, row, column, or page you want to replace.

Default value: 0

##### Relationship between index Inputs and array Dimensions

For multidimensional arrays, index inputs correspond to row-major order. Thus, the first index corresponds last dimension of the array input, and the last index corresponds to the first dimension of the array input. The following table shows the relationship between four index inputs and the dimensions of a 4D array input.

| index Order | Corresponding Dimension in array Input | index Name |
| --- | --- | --- |
| 1 | 4th | volume index |
| 2 | 3rd | page index |
| 3 | 2nd | row index |
| 4 | 1st | column index |

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### waveform

The waveform whose array of y values you want to use in this operation. This input becomes available when you wire a waveform to array.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### new element/subarray

The element or array that replaces an element, row, column, or page in the array specified in 
array.

This input changes to new element/waveform subset when you wire a waveform to array.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### new element/waveform subset

The element or waveform subset that replaces an element in the array of y values in the waveform specified in 
waveform.

This input becomes available when you wire a waveform to array.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### output array

The array this node returns with the replaced elements, rows, columns, or pages. This output changes to output waveform when the input data type is a waveform.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/imsdt.png']

##### output waveform

The waveform this node returns with the replaced elements. This output becomes available only when the input data type is a waveform.

#### Replacing Multiple Elements or Array Subsets

Resize this node to replace multiple elements or array subsets at one time.

#### Behavior for Oversized Subarrays

This node crops any subarray that is too large to fit as a column, row, or page in the input array.

#### Behavior for Non-Matching Index Values

If any index is negative or larger than the corresponding dimension in array, the node has no effect.

Parent topic:

Array Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=replace-substring.html language=enus -->
## TOPIC 00308: Replace Substring

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `replace-substring.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/replace-substring.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes a specified length of characters in a string and replaces the deleted portion with another string. string The string in which you want to replace characters. substring Substring that replaces a specified length of characters in the input string. Default value: Empty string offset The number

Replace Substring

Deletes a specified length of characters in a string and replaces the deleted portion with another string.

[IMAGE alt='1378' src='ReplaceSubstring.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### string

The string in which you want to replace characters.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### substring

Substring that replaces a specified length of characters in the input string.

Default value: Empty string

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### offset

The number of characters into the string at which the node places the substring.

Note

16

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### length

The number of characters the substring will replace in the input string.

If the substring is empty, the specified length of characters is deleted starting at the offset.

Note

16

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### result string

The edited string that includes the replaced characters.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### replaced substring

Characters that were replaced in the string.

#### Reducing Performance Burden

Characters in UTF-8 can be multiple bytes so string nodes count the number of characters in a string instead of jumping to a point in memory. Since the length and offset parameters are in units of characters, avoid nesting this node with large strings because that can create exponential functions that carry a higher performance burden.

Parent topic:

String Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=reshape-array.html language=enus -->
## TOPIC 00309: Reshape Array

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `reshape-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/reshape-array.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Changes the dimensions of an array according to a specified dimension size. This node reads the array data in memory from left to right, row by row and populates the reshaped array the same way. For example, if you pass a 2D array of 8 elements, 2 columns of {0,1,2,3}, to this node with two dimensio

Reshape Array

Changes the dimensions of an array according to a specified dimension size.

This node reads the array data in memory from left to right, row by row and populates the reshaped array the same way. For example, if you pass a 2D array of 8 elements, 2 columns of {0,1,2,3}, to this node with two dimensions defined with sizes of 2 and 4, respectively, the node returns an array containing {{0,0,1,1}, {2,2,3,3}}.

[IMAGE alt='1378' src='ReshapeArray.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### array

An 
n-dimensional array of any type.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### dimension size

New size for a single dimension of array.

The node creates an empty array if any dimension size is 0. You must have 
 ndimension size inputs for 
 ndimensions.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### output array

The array reshaped with dimension size.

If the product of the dimension sizes is greater than the number of elements in the input array, the node pads the new array with the default of the data type of array. If the product of the dimension sizes is less than the number of elements in the input array, the node truncates the array.

#### Examples

[IMAGE alt='1378' src='GUID-5F1EC0F2-4DD2-458B-8247-DF2E9AEE9D71-a5.png']

| Output | Panel Indicator | Comments |
| --- | --- | --- |
| reshape to 1D Array |  | Reshape Array populates reshape to 1D array left to right, row by row. Because the output array contains the same number of elements as the input array, no data is truncated or padded in the output array. |
| reshape to 2D 2x4 Array |  | Reshape Array populates reshape to 2x4 2D array left to right until it reaches the width limit of the array, row by row. Because the output array contains the same number of elements as the input array, no data is truncated or padded in the output array. |

#### Modifying Array Data Using Dimension Size

output array has one dimension for each dimension size input. You can resize the node to increase the number of dimension size parameters. Reshape Array pads or truncates array data if necessary to match dimension size parameters. For example, if you pass a 1D array with 9 elements {0, 1, 2, 3, 4, 5, 6, 7, 8} to this node with two dimensions defined with sizes of 2 and 3, respectively, the node returns a 2D array containing {{0, 1, 2}, {3, 4, 5}}. The node truncates the last three input elements because the output array has room for only six values. Similarly, if you pass the same 1D array to this node with two dimensions defined with sizes of 2 and 5, respectively, the node returns a 2D array containing {{0,1,2,3,4}, {5,6,7,8,0}}. The node pads the last element to match the values for dimension size.

Parent topic:

Array Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=resize-matrix.html language=enus -->
## TOPIC 00310: Resize Matrix (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `resize-matrix.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/resize-matrix.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `lvFunction`
- source_description: Resizes matrix with new row and column dimensions based on number of rows and number of columns. Indexing Outside Values If you increase the row or column dimensions of matrix, this node returns 0 at each exterior location. matrix 2D array of any numeric type. number of rows New row dimension. numbe

Resize Matrix

Resizes **matrix** with new row and column dimensions based on **number of rows** and **number of columns**.

[IMAGE alt='connector_pane_image' src='ResizeMatrix.png']

- Inputs/Outputs
- Details
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

#### matrix

2D array of any numeric type.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### number of rows

New row dimension.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### number of columns

New column dimension.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

#### resized matrix

**matrix** with the number of rows and columns you specify in **number of rows** and **number of columns**.

#### Indexing Outside Values

If you increase the row or column dimensions of **matrix**, this node returns 0 at each exterior location.

Parent topic:

Matrix Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=reverse-1d-array.html language=enus -->
## TOPIC 00311: Reverse 1D Array

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `reverse-1d-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/reverse-1d-array.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reverses the order of the elements in an array. array A 1D array of any type. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time. reversed array array in reverse order. If array has

Reverse 1D Array

Reverses the order of the elements in an array.

[IMAGE alt='1378' src='Reverse1DArray.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### array

A 1D array of any type.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### reversed array

array in reverse order. If array has 
n elements, array[0] becomesreversed array[n-1], array[1] becomes reversed array[n-2], and so on.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

Parent topic:

Array Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=reverse-string.html language=enus -->
## TOPIC 00312: Reverse String

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `reverse-string.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/reverse-string.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Produces a string whose characters are in reverse order of those in an input string. string The string you want to modify. This input can also be any data type that contains only strings, such as an array or cluster of strings. reversed The result of reversing the string. The data type of this outpu

Reverse String

Produces a string whose characters are in reverse order of those in an input string.

[IMAGE alt='1378' src='ReverseString.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### string

The string you want to modify.

This input can also be any data type that contains only strings, such as an array or cluster of strings.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### reversed

The result of reversing the string.

string

Parent topic:

String Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=ring-constant.html language=enus -->
## TOPIC 00313: Ring Constant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `ring-constant.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/ring-constant.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a list of values you can select on the diagram. Each value consists of a numeric value and corresponding string label.

Ring Constant

Represents a list of values you can select on the diagram. Each value consists of a numeric value and corresponding string label.

[IMAGE alt='1378' src='Literal.Ring.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=rotate-1d-array.html language=enus -->
## TOPIC 00314: Rotate 1D Array

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `rotate-1d-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/rotate-1d-array.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Rotates the elements of an array a specified number of places and direction. array A 1D array of any type. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time. n The number of places

Rotate 1D Array

Rotates the elements of an array a specified number of places and direction.

[IMAGE alt='1378' src='Rotate1DArray.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### array

A 1D array of any type.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### n

The number of places and the direction to rotate array.

If n is positive, the indices of elements move right, and if n is negative, the indices of elements move left. For example, if n is 1, all elements in array move right one index place, so the first element becomes the second element and the last element becomes the first. If n is -1, all elements move left one index place, so the second element becomes the first element and the first element becomes the last. The node coerces n to a 32-bit integer if you wire another representation to it.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### rotated array

array rotated according to n.

For example, if n is 1, the input array[0] becomes rotated array[1], input array[1] becomes rotated array[2], and so on, and input array[m-1] becomes rotated array[0], where 
 m is the number of elements in the array. If n is -2, input array[0] becomes rotated array[m-2], input array[1] becomes rotated array[m-1], and so on, and input array[m-1] becomes rotated array[m-3], where 
 m is the number of elements in the array.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

#### Examples

| Diagram | Panel Indicator | Comments |
| --- | --- | --- |
|  |  | When n is 1, all elements in the array input move right one index place, so the first element becomes the second element and the last element becomes the first. |
|  |  | When n is -1. all elements in the array input move left one index place, so the second element becomes the first element and the first element becomes the last. |

Parent topic:

Array Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=rotate-string.html language=enus -->
## TOPIC 00315: Rotate String

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `rotate-string.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/rotate-string.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Moves the first character of a string to the end of the string. The remaining characters move forward one position. For example, the string abcd becomes bcda. string The string you want to modify. This input can also be any data type that contains only strings, such as an array or cluster of strings

Rotate String

Moves the first character of a string to the end of the string.

The remaining characters move forward one position. For example, the string abcd becomes bcda.

[IMAGE alt='1378' src='RotateString.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### string

The string you want to modify.

This input can also be any data type that contains only strings, such as an array or cluster of strings.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### first char last

The rotated string.

string

Parent topic:

String Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=round-to-nearest.html language=enus -->
## TOPIC 00316: Round to Nearest

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `round-to-nearest.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/round-to-nearest.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Expresses the input to the nearest round integer. x An input to this operation. This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. nearest integer value The resulting nearest integer to

Round to Nearest

Expresses the input to the nearest round integer.

[IMAGE alt='1378' src='RoundToNearest.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### nearest integer value

The resulting nearest integer to the input value.

##### Complex Numbers

When x is complex, this node returns a complex number defined by the nearest integer to the real and imaginary parts of x. The following equation defines 
 nearest integer value:

nearest integer value(x) = nearest integer value(a) + 
 i * nearest integer value(b)

##### Rounding Behavior

If the value of the input is midway between two integers, this node returns the nearest even integer.

For example, if x is 1.5 or 2.5, nearest integer value is 2.

Note

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=round-toward-negative-infinity.html language=enus -->
## TOPIC 00317: Round toward Negative Infinity

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `round-toward-negative-infinity.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/round-toward-negative-infinity.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Expresses the input to the next lower round integer. For example, if the input is 3.8, the result is 3. If the input is -3.8, the result is -4. x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPG

Round toward Negative Infinity

Expresses the input to the next lower round integer.

For example, if the input is 3.8, the result is 3. If the input is -3.8, the result is -4.

[IMAGE alt='1378' src='RoundTowardNegativeInfinity.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### rounded number

The resulting lowest integer, closest to the input value.

When 
 x is of the form 
 x = a + bi, that is, when 
 x is complex, the function returns a complex number defined by the next lowest integers to the real and imaginary parts of 
 x. The following equation defines 
 rounded number:

floor(x) = floor(a) + 
 i floor(b)

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=round-toward-positive-infinity.html language=enus -->
## TOPIC 00318: Round toward Positive Infinity

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `round-toward-positive-infinity.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/round-toward-positive-infinity.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Expresses the input to the next higher round integer. For example, if the input is 3.1, the result is 4. If the input is -3.1, the result is -3. x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FP

Round toward Positive Infinity

Expresses the input to the next higher round integer.

For example, if the input is 3.1, the result is 4. If the input is -3.1, the result is -3.

[IMAGE alt='1378' src='RoundTowardPositiveInfinity.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### rounded number

The resulting highest integer, closest to the input.

When 
 x is of the form 
 x = a + bi, that is, when 
 x is complex, the function returns a complex number defined by the next highest integers to the real and imaginary parts of 
 x. The following equation defines 
 rounded number:

ceil(x) = ceil(a) + 
 i ceil(b)

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=run-vi.html language=enus -->
## TOPIC 00319: Run VI

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `run-vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/run-vi.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `lvFunction`
- source_description: Starts the VI execution, similar to the Run button. This node is different than calling a VI, because it uses the current values of all front panel controls for execution rather than using data passed through parameters. You can use this node to run a reserved VI unless another calling VI is already

Run VI

Starts the VI execution, similar to the 
Run button. This node is different than calling a VI, because it uses the current values of all front panel controls for execution rather than using data passed through parameters.

You can use this node to run a reserved VI unless another calling VI is already running.

[IMAGE alt='connector_pane_image' src='RunVI.png']

- Inputs/Outputs
- Details
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

#### reference in

A reference to a VI.

Use Open VI Reference or Static VI Reference to obtain a valid reference for this input.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

#### wait until done

Boolean that determines whether to wait until the referenced VI completes execution.

| True | Waits until the referenced VI completes execution. |
| --- | --- |
| False | Does not wait until the referenced VI completes execution. |

If you set this parameter to True, make sure the referenced VI terminates execution on its own.

**Default:**False

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

#### auto dispose

Boolean that specifies whether the compiler clears a referenced VI from memory when the panel of the VI is closed.

| True | The compiler clears the reference and memory space when the panel of the referenced VI is closed. |
| --- | --- |
| False | The compiler clears the reference but does not clear the memory space when the panel of the referenced VI is closed. |

Reference Disposal Behaviors

If True, the compiler disposes of the reference, along with the parallel data space, when the target VI goes idle, not when the VI that opened the reference goes idle. The reference can still be used by the calling VI until the target VI closes the reference. The calling VI does not need to close the reference unless Run VIreturns an error. If the calling VI does close the reference, the target VI can abort and leave memory.

If True and the node returns an error, the compiler does not transfer ownership of the reference to the target VI. The compiler does not automatically dispose of the reference when the target VI goes idle.

If False, the application automatically disposes of the VI reference when the VI that opened it goes idle.

**Default:**False

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

#### reference out

Unchanged reference to the same VI.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

#### Using Run VI

This node requires the referenced VI to have a panel. To use this node to retrieve data from an application, make sure you include the panel when you build the application.

#### Using Run VI with a Reentrant VI

Use the 
 Enable Simultaneous call on reentrant VIs configuration in the Open VI Reference node to prepare the VI for reentrant run.

#### Running Target VIs Asynchronously

To run a referenced VI asynchronously, use Start Asynchronous Call instead of Run VI. In addition to having a simpler interface, you can use Start Asynchronous Call to collect the outputs of the referenced VI with a corresponding Wait on Asynchronous Call.

#### Using Strictly Typed VI References with Run VI

A strictly typed static VI reference also reserves any subVIs when a top-level VI is reserved, thus making it ineligible for Run VI if the reserved VI does not have a caller that is already running.

Parent topic:

Execution Control

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=rydberg.html language=enus -->
## TOPIC 00320: Rydberg Constant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `rydberg.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/rydberg.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value 10973731.568508. The Rydberg constant represents the limiting value of the highest wavenumber (the inverse wavelength) of any photon that can be emitted from the hydrogen atom, or, alternatively, the wavenumber of the lowest-energy photon capable of ionizing the hydrogen atom from

Rydberg Constant

Returns the value 10973731.568508. The Rydberg constant represents the limiting value of the highest wavenumber (the inverse wavelength) of any photon that can be emitted from the hydrogen atom, or, alternatively, the wavenumber of the lowest-energy photon capable of ionizing the hydrogen atom from its ground state.

[IMAGE alt='1378' src='Literal.Numeric.Rydberg_Constant.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=scale-by-power-of-2.html language=enus -->
## TOPIC 00321: Scale by Power of 2

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `scale-by-power-of-2.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/scale-by-power-of-2.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Multiplies the input by 2 raised to a specified power. n The power to raise the input by. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Any value larger than 32 bits wraps to a 32-bit signed or unsigned integer. Rounding and Coercion Behavior I

Scale by Power of 2

Multiplies the input by 2 raised to a specified power.

[IMAGE alt='1378' src='ScaleByPowerOf2.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci16.png']

##### n

The power to raise the input by.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Rounding and Coercion Behavior

If n is a floating-point number, this function rounds n before it scales x (0.5 rounds to 0; 0.51 rounds to 1). If n is a 64-bit integer, this function coerces n to a 32-bit integer.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

The value to multiply by 2 raised to the specified power.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### x * 2^n

The result of multiplying the input by 2 raised to the specified power.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=scale-delta-t.html language=enus -->
## TOPIC 00322: Scale Delta t

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `scale-delta-t.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/scale-delta-t.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Multiplies the delta t component of the waveform by the specified scale factor, which lengthens or shortens the sample rate of the waveform. waveform in Waveform to use to scale the delta t. This input accepts a waveform or a digital waveform. scale factor Number by which this node multiplies the de

Scale Delta t

Multiplies the delta 
*t* component of the waveform by the specified scale factor, which lengthens or shortens the sample rate of the waveform.

[IMAGE alt='1378' src='WDT_Scale_Delta_t_DBL.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cmsdt.png']

##### waveform in

Waveform to use to scale the delta 
t.

This input accepts a waveform or a digital waveform.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### scale factor

Number by which this node multiplies the delta 
t of the waveform. A value greater than zero but less than one shortens the sample rate. A value greater than one increases the sample rate.

Default value: 1000

[IMAGE alt='datatype_icon' src='/assets/img/imsdt.png']

##### waveform out

Resulting waveform with the new delta 
t value.

This output is a digital waveform when you wire a digital waveform to waveform in.

Parent topic:

Waveform Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=scan-from-string.html language=enus -->
## TOPIC 00323: Scan from String

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `scan-from-string.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/scan-from-string.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Scans a string for text that matches a specified format and returns the matches as the data type you specify. format string String that includes a format specifier for each output. You can also include any additional text that you know appears in the input string, but which you do not want to appear

Scan from String

Scans a string for text that matches a specified format and returns the matches as the data type you specify.

[IMAGE alt='1378' src='ScanFromString.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### format string

String that includes a format specifier for each output. You can also include any additional text that you know appears in the input string, but which you do not want to appear in an output.

%

Each format specifier uses the following general syntax:

% 
 widthspecifier

This input accepts a maximum of 255 characters.

Default value: Empty string — Causes this node to scan the text according to the default behavior for the data types of the wired outputs.

##### Specifiers

| Specifier | Definition |
| --- | --- |
| x | hexadecimal integer |
| o | octal integer |
| b | binary integer |
| d | signed decimal integer |
| u | unsigned decimal integer |
| f | floating-point number with fractional format |
| e | floating-point number in scientific notation |
| g | floating-point number in either fractional format (f) or scientific notation (e) depending on the exponent of the number: f—The exponent is greater than -4 and less than the precision specifiede—exponent is less than -4 or greater than the precision specified |
| ^e or ^g | floating-point number in engineering notation |
| p | floating-point number in SI notation |
| s | string. This specifier scans to the next whitespace character. If the current scanning location begins with a whitespace character, the node scans all contiguous whitespace. |
| [ ] | character combinations from within a specified set. [ ] matches a string that contains any combination of the characters specified between the brackets. Character matches are case sensitive. You can specify a range of characters by using a -. For example, [0-9a-zA-Z ] matches any string that contains numbers, letters, or spaces. You can exclude characters from the scan by using ^ as the first character in the set. For example, [^,;] matches any string of characters up to but not including the first comma or semicolon. To allow hyphens within the character set, specify it as the first or last character in the set. To allow ^ within the character set, include it anywhere other than as the first character in the set. |
| T | absolute time, most commonly used to interpret timestamp data |
| t | relative time, most commonly used to interpret numeric data as elapsed seconds |

##### Syntax for Matching Literal Text That You Do Not Want To Output

| Syntax | Definition |
| --- | --- |
| \\00 - \\FF | Hex value of an 8-bit character; must be uppercase |
| \\b | Backspace (ASCII BS, equivalent to \\08) |
| \\f | Form feed (ASCII FF, equivalent to \\0C) |
| \\n | Linefeed (ASCII LF, equivalent to \\0A). Format into File automatically converts this code into the platform-dependent end-of-line character. |
| \\r | Carriage return (ASCII CR, equivalent to \\0D) |
| \\t | Tab (ASCII HT, equivalent to \\09) |
| \\s | Space (equivalent to \\20) |
| \\\\ | Backslash (ASCII \\, equivalent to \\5C) |
| %% | Percent sign |
| non-escaped spaces | Any contiguous spaces in the format string match any whitespace in the input string, including new lines and tabs. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### input string

The string this node searches for data to format.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### initial scan location

The number of characters into the string at which the scan begins.

Note

16

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### default value

Default data type and default value for the corresponding output. The node uses this information only if you do not wire a string constant to format string. If you wire a string constant to format string, the node uses the format specifiers in that constant to determine the data type of each output.

Each default value can be a string, path, Boolean, enumerated type, timestamp, or numeric value. You cannot use arrays and clusters with this node.

Default value: A double-precision floating point number with a value of 0 or an empty string, depending on the output data type defined by format string

##### Implications of Using an Enumerated Type

If you wire an enumerated type to 
 default value, the node scans for substrings within the input text that match the string values in the enumerated type and returns the corresponding value of the enumerated type.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### remaining string

Portion of the string that remains after scanning all arguments.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### offset past scan

The index in input string of the first character following the last scanned argument.

Note

16

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### output

Output data obtained from a single format specifier in format string.

The data type of this parameter matches the data type specified by the corresponding format specifier in format string or the corresponding default value. Possible data types include strings, paths, enumerated types, timestamps, and numerics, but not arrays and clusters. If you scan a string that does not fit into the numeric representation you specify, this node returns the largest number that fits into that representation.

#### Examples

| input string | format string | default(s) | output(s) | remaining string |
| --- | --- | --- | --- | --- |
| abc, xyz 12.3+56i 7200 | %3s, %s%f%2d | -- | abc | 00 |
| -- | xyz |  |  |  |
| 0+00i | 12.3+56i |  |  |  |
| -- | 72 |  |  |  |
| Q+1.27E-3 tail | Q%f t | -- | 1.27E-3 | ail |
| 0123456789 | %3d%3d | -- | 12 | 6789 |
| 345 |  |  |  |  |
| X:9.860 Z:3.450 | X:%fY:%f | 100 (I32) | 10 | Z: 3450 |
| 100.00 (DBL) | 100.00 |  |  |  |
| set49.4.2 | set%d | -- | 49 | .4.2 |
| color: red | color: %s | blue (enum {red, green, blue}) | red | -- |
| abcd012xyz3 | %[a-z]%d %[a-z]%d | -- | abcd | -- |
| 12 |  |  |  |  |
| xyz |  |  |  |  |
| 3 |  |  |  |  |
| welcome to LabVIEW, John Smith | %[^,],%s | -- | welcome to LabVIEW | Smith |
| John |  |  |  |  |

#### Does Whitespace Matter?

If you set 
 format string to return numeric values in the output parameters, white spaces in the 
 input string are ignored. Otherwise, a single space in format string matches any amount of whitespace in the input.

#### Scanning Values with Data Types Other Than Double-Precision Floating-Point

format string determines what data types to expect in the input text. If you do not wire a string constant to format string, you must wire the expected data type for each expected output to the corresponding default value.

#### Troubleshooting "Too few/many format specifiers" Error

These errors occur when you wire a string to format string that contains a different number of format specifiers than there are output parameters. To fix this mismatch, either resize the node to display the same number of outputs as format specifiers, or modify the number of format specifiers in format string to match the number of output parameters.

#### Troubleshooting "Format specifier type mismatch" Error

This error occurs when you wire a string to 
 format string that contains at least one format specifier whose data type specifier is incompatible with the data type of the corresponding output. The text of the error specifies which parameter caused the mismatch. To fix this mismatch, you must change either the data type specifier in the relevant format specifier or wire a compatible data type to the relevant output.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=scan-value.html language=enus -->
## TOPIC 00324: Scan Value

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `scan-value.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/scan-value.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the characters at the beginning of a string to a numeric value, using format specifiers to determine the representation and precision of the resulting number. This node also returns the remainder of the input string that follows the converted value. string The string you want to scan for a

Scan Value

Converts the characters at the beginning of a string to a numeric value, using format specifiers to determine the representation and precision of the resulting number.

This node also returns the remainder of the input string that follows the converted value.

[IMAGE alt='1378' src='ScanValue.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### string

The string you want to scan for a numeric value.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### format string

A string that uses format specifiers to determine how to convert the input text into a numeric value.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### default

A numeric value whose representation determines the representation of value.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### output string

The characters in string that follow format string. If there is no match for format string, this node returns string in its entirety.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### value

A portion of string converted into a numeric value according to the format specifiers in format string.

format string

default

If the input string represents a number outside the range of the representation of this output, this output returns the maximum or minimum value for the representation. For example, if the input string is 300, and the representation of this output is an 8-bit signed integer, this output returns 127.

Parent topic:

String Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=scroll-to-end.html language=enus -->
## TOPIC 00325: Scroll To End

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `scroll-to-end.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/scroll-to-end.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the vertical scroll position to the end of the string you specify. User interactions to scroll within the string control override this node. reference in Reference to the string. error in Error conditions that occur before this node runs. The node responds to this input according to standard er

Scroll To End

Sets the vertical scroll position to the end of the string you specify.

User interactions to scroll within the string control override this node.

[IMAGE alt='1378' src='ScrollToEnd.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### reference in

Reference to the string.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### reference out

Reference to the string.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

String Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=search-1d-array.html language=enus -->
## TOPIC 00326: Search 1D Array

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `search-1d-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/search-1d-array.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Searches for an element in a 1D array starting at a specified index. The node stops searching as soon as the element is found. 1D array A 1D array of any type. element The value to search for in the input array. The representation of element should match the representation of 1D array. start index T

Search 1D Array

Searches for an element in a 1D array starting at a specified index.
 The node stops searching as soon as the element is found.

[IMAGE alt='1378' src='Search1DArray.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### 1D array

A 1D array of any type.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### element

The value to search for in the input array.

The representation of element should match the representation of 1D array.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### start index

The index of 1D array to start searching for element.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### index of element

The index of 1D array where element is found.

If the node does not find element, index of element is -1.

#### Limitations on Fractional Indexes

You cannot use this node to retrieve the index of a value that is not an element of the array. For example, if you have an array of two elements (0.0 and 1.0), this node does not find the index of the value 0.5, as that value is not an element of the array. Use Threshold 1D Array to find a fractional index.

#### Matching an Element in a String Array

This node only finds a string if the element you specify matches an array element exactly. For example, if you have an array of two elements (upper limit and 
 lower limit), this node does not find the index of the value 
 limit, because 
 limit does not match an array element exactly. To search a string for any occurrence of a regular expression, such as in the previous example, use Match 1D String Array.

#### Search Method Used by Search 1D Array

This node uses a linear search to match the element in 1D array. Because the search is linear, you do not need to sort the array before calling this node.

Parent topic:

Array Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=search-and-replace-pattern.html language=enus -->
## TOPIC 00327: Search and Replace Pattern

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `search-and-replace-pattern.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/search-and-replace-pattern.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Searches for a pattern in the input string and replaces either the first match or every match with a substring you specify. This node performs more quickly than Search and Replace Regular Expression but gives you fewer options for matching strings. For example, Search and Replace Pattern does not su

Search and Replace Pattern

Searches for a pattern in the input string and replaces either the first match or every match with a substring you specify.

This node performs more quickly than Search and Replace Regular Expression but gives you fewer options for matching strings. For example, Search and Replace Pattern does not support the parenthesis or vertical bar (|) characters.

[IMAGE alt='1378' src='Search_and_Replace_Pattern.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### replace all

Boolean value that determines whether to replace all substrings that match the pattern you specify or just the first.

| True | The node replaces all matching substrings. |
| --- | --- |
| False | The node replaces the first matching substring. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### string

String on which the node operates.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### pattern

The pattern you want to search for and replace. This input is limited to the following regular expression characters: . (period), *, +, ?, [], ^, $, \, \b, \f, \n, \s, \r, \t, and \xx. Furthermore, this input does not support character grouping, alternate pattern matching, backreferences, or non-greedy quantification.

##### Definitions of Special Characters

| Special Character | Description | Examples |
| --- | --- | --- |
| . (period) | Matches any single character except a newline character. Within square brackets, . is literal. | Input String: Welcome to LabVIEW. Regular Expression: t.... Match: to La If you use [z.] as the regular expression, the period is literal and matches either . or z. In this example, [z.] returns . as the match. |
| * | Marks the single preceding character or character class as one that can appear zero or more times in the input. Because an asterisk can mark a pattern as one that appears zero times, regular expressions that include an asterisk can return an empty string if the whole pattern is marked with an asterisk. This quantifier applies to as many characters as possible. | Input String: Hello LabVIEW! Regular Expression: el* Match: ell Expressions such as w* or (welcome)* match an empty string if the node finds no other matches. |
| + | Marks the single preceding character or character class as one that can appear one or more times in the input. This quantifier applies to as many characters as possible. | Input String: Hello LabVIEW! Regular Expression: el+ Match: ell |
| ? | Marks the single preceding character or character class as one that can appear zero or one time in the input. This quantifier applies to as many characters as possible. | Input String: Hello LabVIEW! Regular Expression: el? Match: el |
| [] | Creates a character class, which allows you to match any one of a set of characters that you specify. For example, [abc] matches a, b, or c. This node interprets special characters inside square brackets literally, with the following exceptions: - (dash)—Indicates a range when used between digits, or lowercase or uppercase letters; for example, [0-5], [a-g], or [L-Q]. ~—Matches any character, including non-displayable characters, except for the characters or range of characters in brackets. For example, [~0-9] matches any character other than 0 through 9. ^—Matches any displayable character, including the space character, except the characters or range of characters enclosed in the brackets. For example, [^0-9] matches all displayable characters, including the space character, except 0 through 9. | Input String: version=14.0.1 Regular Expression: [0-9]+\\.[0-9]+\\.[0-9]+ Match: 14.0.1 The expression [0-9] matches any digit. The plus sign matches the previous character class, [0-9], one or more times but as many times as possible. The expression \\. matches a literal . character. The plus sign matches the previous character class, [0-9], one or more times but matches as many times as possible. You can use this regular expression to match a three-part version number. |
| ^ | If ^ is the first character of the specified search string, it anchors the match to the offset in string. The match fails unless the specified search string matches that portion of string that begins with the character at offset. If ^ is not the first character in the regular expression, it is treated as a regular character. | Input String: Hello LabVIEW! Regular Expression: ^[^ ]+ Match: Hello From the beginning of the input string, this regular expression matches as many characters – other than a space character – as possible. You can use this regular expression to isolate the first word, numeral, or other character combination of a string. |
| $ | If $ is the last character of the specified search string, it anchors the match to the last element of string. The match fails unless the specified search string matches up to and including the last character in the string. If $ is not the last character in the regular expression, it is treated as a regular character. | Input String: Hello LabVIEW! Regular Expression: [^ ]+$ Match: LabVIEW! From the end of the input string, this regular expression matches as many characters – other than a space character – as possible. You can use this regular expression to isolate the last word, numeral, or other character combination of a string. |
| \\ | Cancels the interpretation of any special character in this list. For example, \\? matches a question mark, \\. matches a period, and \\\\ matches a backslash. You also can use the following constructions for the following non-displayable characters: \\b—Backspace\\f—Form feed\\n—New line\\s—Space\\r—Carriage return\\t—Tab\\xx—Any character, where xx is the hex code using 0 through 9 and upper case A through F. | Input String: Welcome to the LabVIEW Help! Regular Expression: come\\nto\\tthe\\sLabVIEW\\sHelp\\21 Match: come to the LabVIEW Help! The expression come\\n matches the literal letters followed by a newline character. The expression to\\t matches the literal characters to followed by a tab. The two \\s expressions match the spaces between the and LabVIEW and between LabVIEW and Help!. The expression \\21 matches the exclamation point because 21 is the hexadecimal code for an exclamation point. |

Note

hz+

hz[+]

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### replace string

String that replaces the search pattern in the input string.

##### Definitions of Special Characters

Use the following special characters in replace string.

| Special Character | Description | Example(s) |
| --- | --- | --- |
| $n or ${n} | Inserts a string you specify before or after the submatch you specify. Refer to the Specifying Backreferences in replace string section below for more information about using backreferences in replace string. Use ${n} if you have more than nine submatches in a regular expression and want to refer to a submatch after the ninth. $12 inserts only the first submatch because the function reads only the first digit that immediately follows $. However, ${12} inserts the twelfth submatch. | Input String: Welcome LabVIEW! Pattern: (LabVIEW) Replace String: to $1! Result: Welcome to LabVIEW! |
| Input String: Welcome to the LabVIEW Help! Pattern: We(l)(co(m)e)( )(to)( )t(he) (Lab)(VIE(W)) He(lp)(!) Replace String: $7${11}ful${12} Result: helpful! |  |  |
| \\$n | Cancels the interpretation of any special character you use in replace string. | Input String: total=123 per day Pattern: (\\d+)(per \\w*)? Replace String: \\$$1$2 Result: total=$123 per day As in this example, use \\$ to insert the literal character $. Use \\\\ to indicate a literal backslash. |

##### Specifying Backreferences in replace string

You can specify a backreference in replace string that refers to submatches in the input string. Use 
 $1 to refer to the first submatch, 
 $2 to refer to the second submatch, and so on. Consider the following example:

Input String: 
 $value "TRUE"TRUE" *NULL

Pattern: 
 (["*$])(\w+)\1\2\1

Replace String: 
 $1$2value$1

Result: 
 $value "TRUEvalue" *NULL

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### offset

Number of characters into the input string at which the node starts searching for a match.

offset

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### result string

String that this node produces after operating on the input string.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### offset past match

Index in string of the first character after the last match. If the node does not find a match, offset past match is -1.

#### What Happens When There Is No Match?

If the node does not find pattern, result string returns an empty string and offset past match returns -1.

#### Reducing Performance Burden

Characters in UTF-8 can be multiple bytes so string nodes count the number of characters in a string instead of jumping to a point in memory. Since the length and offset parameters are in units of characters, avoid nesting this node with large strings because that can create exponential functions that carry a higher performance burden.

Parent topic:

String Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=search-split-string.html language=enus -->
## TOPIC 00328: Search/Split String

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `search-split-string.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/search-split-string.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Divides a single string into two substrings. This node searches a string for the string or character in search string/char and splits the string when it finds a match. This node returns two strings: the substring before the match, and the match plus the rest of the original string. string The input

Search/Split String

Divides a single string into two substrings.

This node searches a string for the string or character in search string/char and splits the string when it finds a match. This node returns two strings: the substring before the match, and the match plus the rest of the original string.

[IMAGE alt='1378' src='SearchOrSplitString.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### string

The input string the node searches or splits.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### search string/char

The string or character to search for in the input string.

If you do not wire this input or it contains an empty string, the function splits the string at the specified offset.

Default value: 
 -

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### offset

Number of characters into the string at which the node begins searching.

The offset of the first character in the string is 0. If the offset is unwired or less than 0, the node interprets the offset as 0.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### substring before match

Portion of the string before the search string or before the offset if the search string is unwired. If the node does not find the search string, this output returns the entire string.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### match and rest of string

The search string and all subsequent characters in the string. If the node does not find the search string, this output returns an empty string.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### offset of match

The position of the search string/char in the string. If there is no match, this output returns 
-1.

#### Reducing Performance Burden

Characters in UTF-8 can be multiple bytes so string nodes count the number of characters in a string instead of jumping to a point in memory. Since the length and offset parameters are in units of characters, avoid nesting this node with large strings because that can create exponential functions that carry a higher performance burden.

Parent topic:

String Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=secant.html language=enus -->
## TOPIC 00329: Secant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `secant.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/secant.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the secant of a specified value (x) in radians. x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, this input has a default da

Secant

Computes the secant of a specified value (x) in radians.

[IMAGE alt='1378' src='Secant.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### sec

Result of the operation.

This output assumes the same numeric representation as 
 x.

Parent topic:

Trigonometric Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=select.html language=enus -->
## TOPIC 00330: Select

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `select.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/select.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns one of two specified values depending on a Boolean value. true value Value that this node returns if selector passes a True value. true value and false value must be of the same base type, but they can have different numeric representations. This input supports all data types. selector A Boo

Select

Returns one of two specified values depending on a Boolean value.

[IMAGE alt='1378' src='Select.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### true value

Value that this node returns if selector passes a True value.

true value and false value must be of the same base type, but they can have different numeric representations.

This input supports all data types.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### selector

A Boolean value that determines whether this node returns true value or false value.

| True | This node returns true value for value. |
| --- | --- |
| False | This node returns false value for value. |

If you wire an error cluster to selector and an error occurs, the error cluster passes a True value to the node. Otherwise, the error cluster passes a False value to the node.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### false value

Value that this node returns if selector passes a False value.

true value and false value must be of the same base type, but they can have different numeric representations.

This input supports all data types.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### value

Value wired to true value or false value depending on the current value of selector.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

Parent topic:

Program Flow Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sequence-structure.html language=enus -->
## TOPIC 00331: Sequence Structure

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sequence-structure.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sequence-structure.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Consists of one or more subdiagrams, or frames, that execute sequentially. Use the Sequence Structure to ensure that a subdiagram executes before or after another subdiagram. Dataflow for the Sequence Structure differs from dataflow for other structures. Frames in a Sequence Structure execute from l

Sequence Structure

Consists of one or more subdiagrams, or frames, that execute sequentially.
 Use the Sequence Structure to ensure that a subdiagram executes before or after another subdiagram.

Dataflow for the Sequence Structure differs from dataflow for other structures. Frames in a Sequence Structure execute from left to right and when all data values wired to a frame are available. The data leaves each frame as the frame finishes executing. This means the input of one frame can depend on the output of another frame.

#### Inputs/Outputs

##### Tunnel

Point through which data enters or exits a structure.

[IMAGE alt='1378' src='GUID-43DB7847-2DDA-4B38-86E0-27BE4951A189-a5.png']

[IMAGE alt='1378' src='GUID-576AD071-36DE-4DB2-812C-E5C8DBC156BA-a5.png']

#### Tunnel Restrictions

You cannot drag tunnels across the frames of a Sequence Structure.

#### Avoid Unnecessary Use

Dataflow dependencies between nodes automatically establish sequential execution in your code. Wherever possible, attempt to control the dataflow of your VI by establishing data dependency or using flow-through parameters instead of a Sequence Structure to avoid using unnecessary device resources.

Parent topic:

Program Flow Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=set-busy.html language=enus -->
## TOPIC 00332: Set Busy

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `set-busy.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/set-busy.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Changes the cursor on the panel to the busy state and disables mouse and keyboard input on both the panel and the menu. When the panel is inside a panel container, the node disables user interactions only within the panel. In a WebVI, the node shows a loading spinner on the panel, instead of updatin

Set Busy

Changes the cursor on the panel to the busy state and disables mouse and keyboard
 input on both the panel and the menu.

When the panel is inside a panel container, the node disables user interactions only within the
 panel. In a WebVI, the node shows a loading spinner on the panel, instead of updating
 the cursor.

[IMAGE alt='1378' src='SetBusy.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### panel reference in

Reference to the panel.

If you leave this input unwired, the node changes the cursor on the panel of the current
 VI.

Note

panel reference
 in

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### panel reference out

Reference to the panel.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Busy State Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=set-control-value.html language=enus -->
## TOPIC 00333: Set Control Value

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `set-control-value.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/set-control-value.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `lvFunction`
- source_description: Specifies the value of a named control or indicator. You can wire a value of any data type to this method. Using Set Control ValueThis node requires the referenced VI to have a panel. To use this node to retrieve data from an application, make sure you include the panel when you build the applicatio

Set Control Value

Specifies the value of a named control or indicator. You can wire a value of any data type to this method.

[IMAGE alt='connector_pane_image' src='SetControlValue.png']

- Inputs/Outputs
- Details
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

#### reference in

A reference to a VI.

Use Open VI Reference or Static VI Reference to obtain a valid reference for this input.

[IMAGE alt='datatype_icon' src='/assets/img/cfxdt.png']

#### control value

Value of the control or indicator you want.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

#### control name

Label for the control or indicator whose value you want.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

#### reference out

Unchanged reference to the same VI.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

#### Using Set Control Value

This node requires the referenced VI to have a panel. To use this node to retrieve data from an application, make sure you include the panel when you build the application.

Parent topic:

Execution Control

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=set-matrix-diagonal.html language=enus -->
## TOPIC 00334: Set Matrix Diagonal (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `set-matrix-diagonal.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/set-matrix-diagonal.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `lvFunction`
- source_description: Sets the diagonal of matrix beginning at index (row), index (col). Leaving Inputs Unwired If you leave inputs unwired, this node behaves as described in the following table. Input Result You wire matrix and no other inputs. output matrix returns matrix with the main diagonal set to zero. You wire in

Set Matrix Diagonal

Sets the diagonal of **matrix** beginning at **index (row)**, **index (col)**.

[IMAGE alt='connector_pane_image' src='SetMatrixDiagonal.png']

- Inputs/Outputs
- Details
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

#### matrix

2D array of any numeric type.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### index (row)

Starting row index in the output.

Can be an integer or real number.

To add additional **index (row)** inputs, resize the node.

**Default:**0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### index (col)

Starting column index in the output.

Can be an integer or real number.

To add additional **index (col)** inputs, resize the node.

**Default:**0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

#### new diagonal/fill element

2D array of any numeric type that replaces the diagonal elements in **matrix**.

To add additional **new diagonal/fill element** inputs, resize the node.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

#### output matrix

**matrix** with the new diagonal.

To add additional **output matrix** outputs, resize the node.

#### Leaving Inputs Unwired

If you leave inputs unwired, this node behaves as described in the following table.

| Input | Result |
| --- | --- |
| You wire matrix and no other inputs. | output matrix returns matrix with the main diagonal set to zero. |
| You wire index (col) and do not wire index (row). | output matrix returns matrix with the upper diagonal starting at (0, index (col)) set to the new diagonal elements. |
| You wire index (row) and do not wire index (col). | output matrix returns matrix with the lower diagonal starting at (index (row), 0) set to the new diagonal elements. |

#### Wiring the New Diagonal/Fill Element Input

When you wire inputs to **new diagonal/fill element**, this node behaves as described in the following table.

| Input | Result |
| --- | --- |
| You wire a matrix to new diagonal/fill element. | If you wire a matrix containing one column, this node returns a matrix with the diagonal set to the elements in that column. If you wire a matrix with more than one column, this node ignores the additional columns. |
| You wire an empty matrix to new diagonal/fill element. | output matrix returns matrix. |
| You wire an input to new diagonal/fill element that contains fewer elements than the diagonal or subdiagonal that starts at index (row), index (col). | output matrix returns matrix with only the first elements in the diagonal or subdiagonal set to the new diagonal elements. |
| You wire an input to new diagonal/fill element that contains more elements than the diagonal or subdiagonal that starts at index (row), index (col). | output matrix resizes to receive the new diagonal elements. |
| You wire an input to new diagonal/fill element with a different numeric type than matrix. | This node converts matrix to the new numeric type if this node cannot set new diagonal elements without losing precision. If the node can set new diagonal elements without losing precision, the numeric type of new diagonal/fill element converts to the numeric type of matrix. |

Parent topic:

Matrix Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=set-matrix-elements.html language=enus -->
## TOPIC 00335: Set Matrix Elements (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `set-matrix-elements.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/set-matrix-elements.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `lvFunction`
- source_description: Sets one or more elements in matrix at the indexes you specify in index (row) and index (col). If you wire scalar values i and j to index (row) and index (col), respectively, these inputs correspond to a single matrix element at location (i, j). Output Behavior with 1D Arrays If you wire a 1D array

Set Matrix Elements

Sets one or more elements in **matrix** at the indexes you specify in **index (row)** and **index (col)**.

###### Programming Patterns

If you wire scalar values 
 i and 
 j to **index (row)** and **index (col)**, respectively, these inputs correspond to a single matrix element at location (i, 
 j).

[IMAGE alt='connector_pane_image' src='SetMatrixElements.png']

- Inputs/Outputs
- Details
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

#### matrix

2D array of any numeric type.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### index (row)

Integer, floating-point numeric, 1D array of integers, or 1D array of a floating-point numeric.

To add additional **index (row)** inputs, resize the node.

**Default:**0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### index (col)

Integer, floating-point numeric, 1D array of integers, or 1D array of a floating-point numeric.

To add additional **index (col)** inputs, resize the node.

**Default:**0

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

#### new element/submatrix

Scalar or 2D array that replaces one or more elements in **matrix**.

To add additional **new element/submatrix** inputs, resize the node.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

#### output matrix

**matrix** with the new elements. If **matrix** is an empty matrix, **output matrix** resizes to receive the new elements.

To add additional **output matrix** outputs, resize the node.

#### Output Behavior with 1D Arrays

If you wire a 1D array of numeric data to **index (row)** or **index (col)**, this node sets one matrix element for each location specified. To determine these locations this node pairs each row index in **index (row)** with each column index in **index (col)**. For example, if you pass the array of integers {1, 2, 4} to **index (row)** and the integer {5} to **index (col)**, this node modifies matrix elements at indexes (1, 5), (2, 5), and (4, 5).

#### Empty or Unwired Input Values

If you leave inputs empty or unwired, this node behaves as described in the following table.

| Input | Result |
| --- | --- |
| You wire an empty 1D array to index (row) or index (col). | output matrix returns matrix. |
| You do not wire index (row) or index (col). | This node assigns the new element to the input matrix starting at index (0, 0). |
| You do not wire an input to new element/submatrix. | This node sets the element at location (index (row), index (col)) in matrix to 0. |

#### Indexing Outside Input Values

If you wire certain values to **index (row)** or **index (col)** that are outside the existing elements of **matrix**, output matrix resizes as described in the following table.

| Input | Result |
| --- | --- |
| You wire a value to index (row) or index (col) that is greater than or equal to the row or column dimension of matrix. | output matrix resizes to receive elements at the corresponding location. If you increase the row or column dimensions of matrix, this node returns an invalid operation value at each exterior location. |
| The location you specify in index (row) and index (col) is outside matrix and all the inputs are non-negative. | output matrix resizes to accept the new element or matrix. |

#### Indexing Identical Values

If you wire identical values to **index (row)** or **index (col)** and you wire a matrix to **new element/submatrix**, the order in which this node sets the new matrix elements determines **output matrix**.

#### Wiring the New Element/Submatrix Input

When you wire inputs to **new element/submatrix**, this node behaves as described in the following table.

| Input | Result |
| --- | --- |
| You wire a matrix to new element/submatrix that has a dimension larger than matrix. | output matrix resizes to receive the new matrix elements. If you increase the row or column dimensions of matrix, this node returns 0 at each exterior location. |
| You wire a matrix to new element/submatrix that is larger than the largest submatrix at the starting location. | output matrix resizes to receive the new matrix elements. If you increase the row or column dimensions of matrix, this node returns 0 at each exterior location. |
| You wire a matrix to new element/submatrix in which the row or column dimensions exceed the respective number of row indexes in index (row) or column indexes in index (col). | This node ignores the additional row and column elements. |
| You wire a matrix to new element/submatrix in which the number of row indexes is less than the row dimension of output matrix and you wire a 1D array to index (row). | This node inserts an invalid operation value at each exterior location. |
| You wire a matrix to new element/submatrix in which the number of column indexes is less than the column dimension of output matrix and you wire a 1D array to index (col). | This node inserts an invalid operation value at each exterior location. |
| You wire an input to new element/submatrix with a different numeric type than matrix. | This node converts matrix to a new numeric type if this node cannot set new elements without losing precision. If this node can set new elements without losing precision, the numeric type of new element/submatrix converts to the numeric type of matrix. |

Parent topic:

Matrix Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=set-submatrix.html language=enus -->
## TOPIC 00336: Set Submatrix

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `set-submatrix.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/set-submatrix.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `lvFunction`
- source_description: Adds a submatrix to matrix starting at (row 1, column 1) and ending at (row N, column N). Leaving Inputs Unwired If you wire an input to matrix and you do not wire the other inputs, output matrix returns matrix with every element set to 0. Indexing Outside Input Values If you wire certain input valu

Set Submatrix

Adds a submatrix to **matrix** starting at (**row 1**, **column 1**) and ending at (**row N**, **column N**).

[IMAGE alt='connector_pane_image' src='SetSubMatrix.png']

- Inputs/Outputs
- Details
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

#### matrix

2D array of any numeric type.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### row 1

First row in **matrix** you want to appear in the output.

Must be an integer or real numeric.

To add additional **row 1** inputs, resize the node.

**Default:**0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### row N

Last row in **matrix** you want to appear in the output.

Must be an integer or real numeric.

To add additional **row N** inputs, resize the node.

**Default:**The index of the last row in **matrix**.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### column 1

First column in **matrix** you want to appear in the output.

Must be an integer or real numeric.

To add additional **column 1** inputs, resize the node.

**Default:**0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### column N

Last column in **matrix** you want to appear in the output.

Must be an integer or real numeric.

To add additional **column N** inputs, resize the node.

**Default:**The index of the last column in **matrix**.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

#### new submatrix/fill element

2D array of any numeric type or a numeric scalar.

To add additional **new submatrix/fill element** inputs, resize the node.

**Default:**If you do not wire an input to **new submatrix/fill element**, the default is 0.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

#### output matrix

**matrix** with the new submatrix. If **matrix** is an empty matrix, **output matrix** resizes to receive the new elements.

To add additional **output matrix** outputs, resize the node.

#### Leaving Inputs Unwired

If you wire an input to **matrix** and you do not wire the other inputs, **output matrix** returns **matrix** with every element set to 0.

#### Indexing Outside Input Values

If you wire certain input values that are outside the existing elements of **matrix**, this node returns outputs as described in the following table.

| Input | Result |
| --- | --- |
| You wire an input to matrix and a matrix to new submatrix/fill element. | matrix resizes with the new submatrix elements in output matrix. If this node needs to add rows or columns to the output matrix, this node returns 0 at each exterior location. |
| You wire a negative value to row or column inputs. | This node ignores the rows and columns of the submatrix with negative indexes. If new submatrix/fill element is a matrix, this node also ignores the new submatrix elements that fill these rows and columns. |

#### Wiring the New Submatrix/Fill Element Input

When you wire certain inputs to **new submatrix/fill element**, this node behaves as described in the following table.

| Input | Result |
| --- | --- |
| You wire a matrix to new submatrix/fill element that has a dimension larger than matrix. | output matrix resizes to receive the new submatrix elements. If you increase the row or column dimensions of matrix, this node sets the new elements to an invalid operation value at each exterior location. |
| You wire a matrix to new submatrix/fill element when the dimensions of the row or column inputs are less than the number of rows or columns in the submatrix. | This node ignores the additional row and column elements in the new submatrix. |
| You wire a matrix to new submatrix/fill element when the dimensions of the row or column inputs exceed the number of rows or columns in the submatrix. | This node inserts an invalid operation value at each exterior location. |
| You wire an input to new submatrix/fill element with a different numeric type than matrix. | This node converts matrix to a new numeric type if this node cannot set new submatrix elements without losing precision. If this node cannot set new submatrix elements without losing precision, the numeric type of new submatrix/fill element converts to the numeric type of matrix. |

Parent topic:

Matrix Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=set-variant-attribute.html language=enus -->
## TOPIC 00337: Set Variant Attribute

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `set-variant-attribute.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/set-variant-attribute.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates or replaces a variant attribute. variant The variant data for which you want to create or replace an attribute value. name The name of the attribute you want to replace or create. If name matches an attribute, this node replaces the attribute with the value specified. If name does not match

Set Variant Attribute

Creates or replaces a variant attribute.

[IMAGE alt='1378' src='SetVariantAttribute.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cfxdt.png']

##### variant

The variant data for which you want to create or replace an attribute value.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### name

The name of the attribute you want to replace or create.

name

value

name

name

[IMAGE alt='datatype_icon' src='/assets/img/cvoid.png']

##### value

The value of the attribute. You can wire any data type to this input.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ifxdt.png']

##### variant out

The resulting variant data.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### replaced

A Boolean that indicates whether the node replaced an attribute.

| True | The node replaced an attribute. |
| --- | --- |
| False | The node did not replace an attribute. |

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Variant Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sign.html language=enus -->
## TOPIC 00338: Sign

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sign.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sign.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the sign of the input value. For nonzero complex numbers, this node returns a complex value with the same phase as the input and with a magnitude of 1. number An input to this operation. This input supports waveforms and any data type that contains only numbers, such as scalar numbers, array

Sign

Returns the sign of the input value.

Note

[IMAGE alt='1378' src='Sign.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### number

An input to this operation.

This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### sign

The sign of the input value.

sign

| -1 | number is less than 0. |
| --- | --- |
| 0 | number is equal to 0. |
| 1 | number is greater than 0. |

number

i

number

sign

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sinc.html language=enus -->
## TOPIC 00339: Sinc

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sinc.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sinc.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the sine of a specified value divided by that value (sin(x)/x) in radians. x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA,

Sinc

Computes the sine of a specified value divided by that value (sin(x)/x) in radians.

[IMAGE alt='1378' src='Sinc.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### sinc

Result of the operation.

This output assumes the same numeric representation as 
 x.

Parent topic:

Trigonometric Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sine-and-cosine.html language=enus -->
## TOPIC 00340: Sine and Cosine

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sine-and-cosine.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sine-and-cosine.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes both the sine and cosine of a specified value (x) in radians. Use this node only when you need both results. x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA When you add this node t

Sine and Cosine

Computes both the sine and cosine of a specified value (x) in radians.

Use this node only when you need both results.

[IMAGE alt='1378' src='SineAndCosine.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### sin

Result of the operation.

x

x

x

i

x

sin

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### cos

Result of the operation.

x

x

x

i

x

cos

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

Parent topic:

Trigonometric Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sine.html language=enus -->
## TOPIC 00341: Sine

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sine.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sine.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the sine of a specified value (x) in radians. x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, this input has a default data

Sine

Computes the sine of a specified value (x) in radians.

[IMAGE alt='1378' src='Sine.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### sin

Result of the operation.

x

x

x

i

x

sin

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

Parent topic:

Trigonometric Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sort-1d-array.html language=enus -->
## TOPIC 00342: Sort 1D Array

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sort-1d-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sort-1d-array.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a sorted version of an array with the elements arranged in ascending order. If the specified array is an array of clusters, the node sorts the elements by comparing the first elements. If the first elements match, the node compares the second and subsequent elements. array A 1D array of any

Sort 1D Array

Returns a sorted version of an array with the elements arranged in ascending order.
 If the specified array is an array of clusters, the node sorts the elements by comparing the first elements. If the first elements match, the node compares the second and subsequent elements.

[IMAGE alt='1378' src='Sort1DArray.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### array

A 1D array of any type.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### sorted array

array sorted in ascending order.

#### Sorting String Arrays

Sort 1D Array sorts string arrays based on case-sensitivity. For example, if array is {b, C, A}, Sort 1D Array returns {A, C, b} for sorted array.

Parent topic:

Array Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sound-file-close.html language=enus -->
## TOPIC 00343: Sound File Close (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sound-file-close.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sound-file-close.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Closes a .wav file. To create a sound file reference, use the Sound File Open node and wire the absolute path of a .wav file to the sound file input. Then, wire the reference output of Sound File Open to the input of this node. reference Reference to the .wav file in memory. error in Error condition

Sound File Close

Closes a 
.wav file.

###### Programming Patterns

To create a sound file reference, use the Sound File Open node and wire the absolute path of a 
 .wav file to the **sound file** input. Then, wire the **reference** output of Sound File Open to the input of this node.

[IMAGE alt='connector_pane_image' src='Sound_File_Close.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

#### reference

Reference to the 
.wav file in memory.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs. Unlike most nodes, this node runs normally even if an error occurs before this node runs.

**Default:**no error

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

Unlike most nodes, this node runs normally even if **error in** contains an error.

Parent topic:

Sound Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sound-file-info.html language=enus -->
## TOPIC 00344: Sound File Info (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sound-file-info.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sound-file-info.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Retrieves data about a .wav file. To create a sound file reference, use the Sound File Open node and wire the absolute path of a .wav file to the sound file input. Then, wire the reference output of Sound File Open to the input of this node. sound file Absolute path to the .wav file. If the path is

Sound File Info

Retrieves data about a 
.wav file.

###### Programming Patterns

To create a sound file reference, use the Sound File Open node and wire the absolute path of a 
 .wav file to the **sound file** input. Then, wire the **reference** output of Sound File Open to the input of this node.

[IMAGE alt='connector_pane_image' src='Sound_File_Info_(path).gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cpath.png']

#### sound file

Absolute path to the 
.wav file.

If the path is empty or invalid, the node returns an error in **error out**.

If you wire a reference to **sound file**, this input changes to **reference in**.

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

#### reference in

Reference to the 
.wav file in memory.

This input appears when you wire a reference to **sound file**. If you wire a path to **reference in**, this input changes back to **sound file**.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

#### reference out

Reference to the 
.wav file specified by **reference in**.

This output is available only when you wire a reference to **sound file**.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

#### total number of samples/ch

Total number of samples per channel in the 
.wav file.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

#### sound format

Sample rate, number of channels, and number of bits per sample in the 
.wav file.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### sample rate (S/s)

Sampling rate for the 
.wav file. Common rates are 44,100 S/s, 22,050 S/s, and 11,025 S/s.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### number of channels

Number of channels in the 
.wav file.

This output can accept as many channels as the sound card supports. For most sound cards 1 is mono and 2 is stereo.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### bits per sample

Quality of each sample in bits. Common resolutions are 16 bits and 8 bits.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

The node produces this output according to standard error behavior.

This node can return the following error codes.

| 4805 | Could not find the sound file. |
| --- | --- |

Note

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

Sound Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sound-file-open.html language=enus -->
## TOPIC 00345: Sound File Open (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sound-file-open.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sound-file-open.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `multimodeFunction`
- source_description: Opens a .wav file for reading or creates a new .wav for writing.

Sound File Open

Opens a 
.wav file for reading or creates a new 
.wav for writing.

Sound Nodes

Sound File Read Open

.wav

Sound File Write Open

.wav

Parent topic:

Sound Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sound-file-read-dbl.html language=enus -->
## TOPIC 00346: DBL (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sound-file-read-dbl.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sound-file-read-dbl.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Reads double-precision, floating-point numeric data from a .wav file into an array of waveforms. The Y component of the waveform this node returns is an array of double-precision, floating-point numbers. This node retrieves only uncompressed .wav files. Read .wav files in chunks to avoid using large

DBL

Reads double-precision, floating-point numeric data from a 
.wav file into an array of waveforms.

The Y component of the waveform this node returns is an array of double-precision, floating-point numbers.

Note

.wav

.wav

###### Programming Patterns

To create a sound file reference, use the Sound File Open node and wire the absolute path of a 
 .wav file to the **sound file** input. Then, wire the **reference** output of Sound File Open to the input of this node.

[IMAGE alt='connector_pane_image' src='Sound_File_Read_(DBL).gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### number of samples/ch

Number of samples per channel to read from the file.

**Default:**-1—Specifies all samples.

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

#### reference in

Reference to the 
.wav file in memory.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

#### position mode

The position at which the read operation begins, together with **position offset**.

| Name | Value | Description |
| --- | --- | --- |
| Absolute | 0 | Starts the operation at the beginning of the file plus position offset, so the offset is relative to the beginning of the file. |
| Relative | 1 | Starts the operation at the current location of the file mark plus position offset. |

**Default:**Relative

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### position offset

The position at which the read operation begins away from **position mode**, in units of samples.

**Default:**0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

#### end of file

A Boolean that indicates whether the node has read the entire file.

| True | The node has read the entire file. |
| --- | --- |
| False | The node did not finish reading the entire file. |

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

#### reference out

Reference to the 
.wav file specified by **reference in**.

[IMAGE alt='datatype_icon' src='/assets/img/i1dmsdt.png']

#### data

Any sound data read from the file. For multi-channel sound data, **data** is an array of waveforms where each element of the array is a single channel.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

#### offset

The new location of the file marker relative to the beginning of the file, in units of samples.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

Sound File Read

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sound-file-read-i16.html language=enus -->
## TOPIC 00347: I16 (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sound-file-read-i16.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sound-file-read-i16.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Reads 16-bit signed integer numeric data from a .wav file into an array of waveforms. The Y component of the waveform this node returns is an array of signed 16-bit integers. This node retrieves only uncompressed .wav files. Read .wav files in chunks to avoid using large amounts of memory. To create

I16

Reads 16-bit signed integer numeric data from a 
.wav file into an array of waveforms.

The Y component of the waveform this node returns is an array of signed 16-bit integers.

Note

.wav

.wav

###### Programming Patterns

To create a sound file reference, use the Sound File Open node and wire the absolute path of a 
 .wav file to the **sound file** input. Then, wire the **reference** output of Sound File Open to the input of this node.

[IMAGE alt='connector_pane_image' src='Sound_File_Read_(I16).gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### number of samples/ch

Number of samples per channel to read from the file.

**Default:**-1—Specifies all samples.

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

#### reference in

Reference to the 
.wav file in memory.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

#### position mode

The position at which the read operation begins, together with **position offset**.

| Name | Value | Description |
| --- | --- | --- |
| Absolute | 0 | Starts the operation at the beginning of the file plus position offset, so the offset is relative to the beginning of the file. |
| Relative | 1 | Starts the operation at the current location of the file mark plus position offset. |

**Default:**Relative

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### position offset

The position at which the read operation begins away from **position mode**, in units of samples.

**Default:**0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

#### end of file

A Boolean that indicates whether the node has read the entire file.

| True | The node has read the entire file. |
| --- | --- |
| False | The node did not finish reading the entire file. |

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

#### reference out

Reference to the 
.wav file specified by **reference in**.

[IMAGE alt='datatype_icon' src='/assets/img/i1dmsdt.png']

#### data

Any sound data read from the file. For multi-channel sound data, **data** is an array of waveforms where each element of the array is a single channel.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

#### offset

The new location of the file marker relative to the beginning of the file, in units of samples.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

Sound File Read

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sound-file-read-i32.html language=enus -->
## TOPIC 00348: I32 (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sound-file-read-i32.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sound-file-read-i32.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Reads 32-bit signed integer numeric data from a .wav file into an array of waveforms. The Y component of the waveform this node returns is an array of signed 32-bit integers. This node retrieves only uncompressed .wav files. Read .wav files in chunks to avoid using large amounts of memory. To create

I32

Reads 32-bit signed integer numeric data from a 
.wav file into an array of waveforms.

The Y component of the waveform this node returns is an array of signed 32-bit integers.

Note

.wav

.wav

###### Programming Patterns

To create a sound file reference, use the Sound File Open node and wire the absolute path of a 
 .wav file to the **sound file** input. Then, wire the **reference** output of Sound File Open to the input of this node.

[IMAGE alt='connector_pane_image' src='Sound_File_Read_(I32).gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### number of samples/ch

Number of samples per channel to read from the file.

**Default:**-1—Specifies all samples.

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

#### reference in

Reference to the 
.wav file in memory.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

#### position mode

The position at which the read operation begins, together with **position offset**.

| Name | Value | Description |
| --- | --- | --- |
| Absolute | 0 | Starts the operation at the beginning of the file plus position offset, so the offset is relative to the beginning of the file. |
| Relative | 1 | Starts the operation at the current location of the file mark plus position offset. |

**Default:**Relative

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### position offset

The position at which the read operation begins away from **position mode**, in units of samples.

**Default:**0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

#### end of file

A Boolean that indicates whether the node has read the entire file.

| True | The node has read the entire file. |
| --- | --- |
| False | The node did not finish reading the entire file. |

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

#### reference out

Reference to the 
.wav file specified by **reference in**.

[IMAGE alt='datatype_icon' src='/assets/img/i1dmsdt.png']

#### data

Any sound data read from the file. For multi-channel sound data, **data** is an array of waveforms where each element of the array is a single channel.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

#### offset

The new location of the file marker relative to the beginning of the file, in units of samples.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

Sound File Read

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sound-file-read-open.html language=enus -->
## TOPIC 00349: Sound File Read Open (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sound-file-read-open.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sound-file-read-open.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Opens a .wav file for reading. sound file Absolute path to the .wav file. If the path is empty or invalid, the node returns an error in error out. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. No error Standard Error

Sound File Read Open

Opens a 
.wav file for reading.

[IMAGE alt='connector_pane_image' src='Sound_File_Read_Open.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cpath.png']

#### sound file

Absolute path to the 
.wav file.

If the path is empty or invalid, the node returns an error in **error out**.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

#### reference

Reference to the 
.wav file specified by **sound file**. You can pass **reference** to other Sound Files nodes to interact with the 
.wav file.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

The node produces this output according to standard error behavior.

This node can return the following error codes.

| 4805 | Could not find the sound file. |
| --- | --- |

Note

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

Sound File Open

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sound-file-read-sgl.html language=enus -->
## TOPIC 00350: SGL

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sound-file-read-sgl.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sound-file-read-sgl.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Reads single-precision, floating-point numeric data from a .wav file into an array of waveforms. The Y component of the waveform this node returns is an array of single-precision, floating-point numbers. This node retrieves only uncompressed .wav files. Read .wav files in chunks to avoid using large

SGL

Reads single-precision, floating-point numeric data from a 
.wav file into an array of waveforms.

The Y component of the waveform this node returns is an array of single-precision, floating-point numbers.

Note

.wav

.wav

###### Programming Patterns

To create a sound file reference, use the Sound File Open node and wire the absolute path of a 
 .wav file to the **sound file** input. Then, wire the **reference** output of Sound File Open to the input of this node.

[IMAGE alt='connector_pane_image' src='Sound_File_Read_(SGL).gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### number of samples/ch

Number of samples per channel to read from the file.

**Default:**-1—Specifies all samples.

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

#### reference in

Reference to the 
.wav file in memory.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

#### position mode

The position at which the read operation begins, together with **position offset**.

| Name | Value | Description |
| --- | --- | --- |
| Absolute | 0 | Starts the operation at the beginning of the file plus position offset, so the offset is relative to the beginning of the file. |
| Relative | 1 | Starts the operation at the current location of the file mark plus position offset. |

**Default:**Relative

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### position offset

The position at which the read operation begins away from **position mode**, in units of samples.

**Default:**0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

#### end of file

A Boolean that indicates whether the node has read the entire file.

| True | The node has read the entire file. |
| --- | --- |
| False | The node did not finish reading the entire file. |

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

#### reference out

Reference to the 
.wav file specified by **reference in**.

[IMAGE alt='datatype_icon' src='/assets/img/i1dmsdt.png']

#### data

Any sound data read from the file. For multi-channel sound data, **data** is an array of waveforms where each element of the array is a single channel.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

#### offset

The new location of the file marker relative to the beginning of the file, in units of samples.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

Sound File Read

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sound-file-read-simple.html language=enus -->
## TOPIC 00351: Sound File Read Simple (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sound-file-read-simple.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sound-file-read-simple.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Reads data from a .wav file into an array of waveforms. This node automatically opens, reads, and closes the .wav file. This node retrieves only uncompressed .wav files. Read .wav files in chunks to avoid using large amounts of memory. number of samples/ch Number of samples per channel to read from

Sound File Read Simple

Reads data from a 
.wav file into an array of waveforms. This node automatically opens, reads, and closes the 
.wav file.

Note

.wav

.wav

[IMAGE alt='connector_pane_image' src='Sound_File_Read_Simple.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### number of samples/ch

Number of samples per channel to read from the file.

**Default:**-1—Specifies all samples.

[IMAGE alt='datatype_icon' src='/assets/img/cpath.png']

#### sound file

Absolute path to the 
.wav file.

If the path is empty or invalid, the node returns an error in **error out**.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

#### position mode

The position at which the read operation begins, together with **position offset**.

| Name | Value | Description |
| --- | --- | --- |
| Absolute | 0 | Starts the operation at the beginning of the file plus position offset, so the offset is relative to the beginning of the file. |
| Relative | 1 | Starts the operation at the current location of the file mark plus position offset. |

**Default:**Relative

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### position offset

The position at which the read operation begins away from **position mode**, in units of samples.

**Default:**0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/i1dmsdt.png']

#### data

Any sound data read from the file. For multi-channel sound data, **data** is an array of waveforms where each element of the array is a single channel.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

#### offset

The new location of the file marker relative to the beginning of the file, in units of samples.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

The node produces this output according to standard error behavior.

This node can return the following error codes.

| 4805 | Could not find the sound file. |
| --- | --- |

Note

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

Sound Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sound-file-read-u8.html language=enus -->
## TOPIC 00352: U8 (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sound-file-read-u8.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sound-file-read-u8.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Reads 8-bit unsigned integer numeric data from a .wav file into an array of waveforms. The Y component of the waveform this node returns is an array of unsigned 8-bit integers. This node retrieves only uncompressed .wav files. Read .wav files in chunks to avoid using large amounts of memory. To crea

U8

Reads 8-bit unsigned integer numeric data from a 
.wav file into an array of waveforms.

The Y component of the waveform this node returns is an array of unsigned 8-bit integers.

Note

.wav

.wav

###### Programming Patterns

To create a sound file reference, use the Sound File Open node and wire the absolute path of a 
 .wav file to the **sound file** input. Then, wire the **reference** output of Sound File Open to the input of this node.

[IMAGE alt='connector_pane_image' src='Sound_File_Read_(U8).gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### number of samples/ch

Number of samples per channel to read from the file.

**Default:**-1—Specifies all samples.

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

#### reference in

Reference to the 
.wav file in memory.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

#### position mode

The position at which the read operation begins, together with **position offset**.

| Name | Value | Description |
| --- | --- | --- |
| Absolute | 0 | Starts the operation at the beginning of the file plus position offset, so the offset is relative to the beginning of the file. |
| Relative | 1 | Starts the operation at the current location of the file mark plus position offset. |

**Default:**Relative

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### position offset

The position at which the read operation begins away from **position mode**, in units of samples.

**Default:**0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

#### end of file

A Boolean that indicates whether the node has read the entire file.

| True | The node has read the entire file. |
| --- | --- |
| False | The node did not finish reading the entire file. |

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

#### reference out

Reference to the 
.wav file specified by **reference in**.

[IMAGE alt='datatype_icon' src='/assets/img/i1dmsdt.png']

#### data

Any sound data read from the file. For multi-channel sound data, **data** is an array of waveforms where each element of the array is a single channel.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

#### offset

The new location of the file marker relative to the beginning of the file, in units of samples.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

Sound File Read

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sound-file-read.html language=enus -->
## TOPIC 00353: Sound File Read (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sound-file-read.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sound-file-read.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `multimodeFunction`
- source_description: Reads data from a .wav file into an array of waveforms. This node retrieves only uncompressed .wav files. Read .wav files in chunks to avoid using large amounts of memory.

Sound File Read

Reads data from a 
.wav file into an array of waveforms.

Note

.wav

.wav

Sound Nodes

DBL

.wav

I16

.wav

I32

.wav

SGL

.wav

U8

.wav

Parent topic:

Sound Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sound-file-write-open.html language=enus -->
## TOPIC 00354: Sound File Write Open (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sound-file-write-open.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sound-file-write-open.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Opens a .wav file for writing. sound file Absolute path to the .wav file. If the path is empty or invalid, the node returns an error in error out. sound format The acquisition rate, the number of channels, and the bits per sample of the sound operation. The values for each of these elements is depen

Sound File Write Open

Opens a 
.wav file for writing.

[IMAGE alt='connector_pane_image' src='Sound_File_Write_Open.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cpath.png']

#### sound file

Absolute path to the 
.wav file.

If the path is empty or invalid, the node returns an error in **error out**.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

#### sound format

The acquisition rate, the number of channels, and the bits per sample of the sound operation. The values for each of these elements is dependent on your sound card.

Not all operating systems and sound cards support all **sample rate (S/s)**, **number of channels**, or **bits per sample** options.

Performance Details

**sample rate (S/s)** and **bits per sample** use more computer memory when set to a higher value.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### sample rate (S/s)

Sampling rate for the sound operation. Common rates are 44,100 S/s, 22,050 S/s, and 11,025 S/s.

**Default:**22,050 S/s

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### number of channels

Number of channels. This input can accept as many channels as the sound card supports. For most sound cards 1 is mono and 2 is stereo.

**Default:**2

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### bits per sample

Quality of each sample in bits. Available resolutions are 8 bits, 16 bits, and 32 bits.

**Default:**16 bits

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

#### reference

Reference to the 
.wav file specified by **sound file**. You can pass **reference** to other Sound Files nodes to interact with the 
.wav file.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

The node produces this output according to standard error behavior.

This node can return the following error codes.

| 4805 | Could not find the sound file. |
| --- | --- |

Note

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

Sound File Open

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sound-file-write-simple.html language=enus -->
## TOPIC 00355: Sound File Write Simple (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sound-file-write-simple.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sound-file-write-simple.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Writes data from an array of waveforms to a .wav file. This node automatically opens, writes to, and closes the .wav file. sound file Absolute path to the .wav file. If the path is empty or invalid, the node returns an error in error out. If you specify the path to a file that already exists, you ca

Sound File Write Simple

Writes data from an array of waveforms to a 
.wav file. This node automatically opens, writes to, and closes the 
.wav file.

[IMAGE alt='connector_pane_image' src='Sound_File_Write_Simple.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cpath.png']

#### sound file

Absolute path to the 
.wav file.

If the path is empty or invalid, the node returns an error in **error out**. If you specify the path to a file that already exists, you can overwrite the contents of the file.

[IMAGE alt='datatype_icon' src='/assets/img/c1dmsdt.png']

#### data

Sound data to write to the 
.wav file. For multi-channel sound data, **data** is an array of waveforms where each element of the array is a single channel.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### bits per sample

Quality of each sample in bits. Common resolutions are 16 bits and 8 bits.

**Default:**16 bits

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

The node produces this output according to standard error behavior.

This node can return the following error codes.

| 4805 | Could not find the sound file. |
| --- | --- |

Note

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

Sound Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sound-file-write.html language=enus -->
## TOPIC 00356: Sound File Write (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sound-file-write.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sound-file-write.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Writes data from a waveform or an array of waveforms to a .wav file. To create a sound file reference, use the Sound File Open node and wire the absolute path of a .wav file to the sound file input. Then, wire the reference output of Sound File Open to the input of this node. reference in Reference

Sound File Write

Writes data from a waveform or an array of waveforms to a 
.wav file.

###### Programming Patterns

To create a sound file reference, use the Sound File Open node and wire the absolute path of a 
 .wav file to the **sound file** input. Then, wire the **reference** output of Sound File Open to the input of this node.

[IMAGE alt='connector_pane_image' src='Sound_File_Write_(DBL).gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

#### reference in

Reference to the 
.wav file in memory.

[IMAGE alt='datatype_icon' src='/assets/img/c1dmsdt.png']

#### data

Sound data to write to the 
.wav file. For multi-channel sound data, **data** is an array of waveforms where each element of the array is a single channel.

- An array of waveforms, where the Y array contains single-precision, floating-point numeric data
- An array of waveforms, where the Y array contains double-precision, floating-point numeric data
- A single waveform of double-precision, floating-point numeric data
- An array of waveforms, where the Y array contains signed 16-bit integer data
- An array of waveforms, where the Y array contains signed 32-bit integer data
- An array of waveforms, where the Y array contains unsigned 8-bit integer data

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

#### reference out

Reference to the 
.wav file specified by **reference in**.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

Sound Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sound-input-clear.html language=enus -->
## TOPIC 00357: Sound Input Clear

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sound-input-clear.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sound-input-clear.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Stops acquisition of data, clears the buffer, returns the task ID to the default state, and clears the resources associated with the task ID. When you run this node, you can no longer use the task ID because this node removes all resources associated with the task ID. To create a task ID, use the So

Sound Input Clear

Stops acquisition of data, clears the buffer, returns the task ID to the default state, and clears the resources associated with the task ID. When you run this node, you can no longer use the task ID because this node removes all resources associated with the task ID.

###### Programming Patterns

To create a task ID, use the Sound Input Configure node and wire the**task ID** output to the input of this node.

[IMAGE alt='connector_pane_image' src='Sound_Input_Clear.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

#### task ID

Reference to the configured sound device you want to manipulate or input.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs. Unlike most nodes, this node runs normally even if an error occurs before this node runs.

**Default:**no error

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

Unlike most nodes, this node runs normally even if **error in** contains an error.

**Where This Node Can Run:**

Desktop OS: Windows

FPGA:

Web Server:

Parent topic:

Sound Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sound-input-configure.html language=enus -->
## TOPIC 00358: Sound Input Configure

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sound-input-configure.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sound-input-configure.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Configures a sound input device to acquire data and then sends the data to a buffer. Use Sound Input Read to read the data. number of samples/ch Number of samples per channel in the buffer. Continuous operations require an increased number of samples to improve data quality but require the use of mo

Sound Input Configure

Configures a sound input device to acquire data and then sends the data to a buffer. Use Sound Input Read to read the data.

[IMAGE alt='connector_pane_image' src='Sound_Input_Configure.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### number of samples/ch

Number of samples per channel in the buffer. Continuous operations require an increased number of samples to improve data quality but require the use of more memory.

**Default:**100,000

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### sample mode

Setting to acquire samples once or continuously.

| Name | Value | Description |
| --- | --- | --- |
| Finite Samples | 0 | Acquire samples once. In this mode, call this node only until you have written the number of samples specified in number of samples/ch. |
| Continuous Samples | 1 | Acquire samples continuously. In this mode, you can call this node repeatedly as needed. |

**Default:**1—Continuous Samples

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

#### device ID

The input or output device you access for a sound operation. The value ranges from 0 to 
*n*-1, where 
*n* is the number of input or output devices on the computer.

**Default:**0

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

#### sound format

The acquisition rate, the number of channels, and the bits per sample of the sound operation. The values for each of these elements is dependent on your sound card.

Not all operating systems and sound cards support all **sample rate (S/s)**, **number of channels**, or **bits per sample** options.

Performance Details

**sample rate (S/s)** and **bits per sample** use more computer memory when set to a higher value.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### sample rate (S/s)

Sampling rate for the sound operation. Common rates are 44,100 S/s, 22,050 S/s, and 11,025 S/s.

**Default:**22,050 S/s

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### number of channels

Number of channels. This input can accept as many channels as the sound card supports. For most sound cards 1 is mono and 2 is stereo.

**Default:**2

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### bits per sample

Quality of each sample in bits. Available resolutions are 8 bits, 16 bits, and 32 bits.

**Default:**16 bits

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

#### task ID

Reference to the configured sound device. You can pass **task ID** to other sound operation nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Where This Node Can Run:**

Desktop OS: Windows

FPGA:

Web Server:

Parent topic:

Sound Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sound-input-read-dbl.html language=enus -->
## TOPIC 00359: DBL

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sound-input-read-dbl.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sound-input-read-dbl.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Reads double-precision, floating-point numeric data from a sound input device. The Y component of the waveform this node returns is an array of double-precision, floating-point numbers. To create a task ID, use the Sound Input Configure node and wire the task ID output to the input of this node. num

DBL

Reads double-precision, floating-point numeric data from a sound input device.

The Y component of the waveform this node returns is an array of double-precision, floating-point numbers.

###### Programming Patterns

To create a task ID, use the Sound Input Configure node and wire the**task ID** output to the input of this node.

[IMAGE alt='connector_pane_image' src='Sound_Input_Read_(DBL).gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### number of samples/ch

Number of samples per channel in the buffer. Use a large number of samples for continuous operations. Use a smaller number of samples if you want to use less memory.

**Default:**10,000

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

#### task ID in

Reference to the configured sound device you want to manipulate or input.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

#### timeout

Time, in seconds, that the node waits for the sound operation to complete. This node returns an error if the time elapses. If you set **timeout** to -1, the node waits indefinitely.

**Default:**10

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

#### task ID out

Reference to the configured sound device originally passed to the **task ID in** parameter.

[IMAGE alt='datatype_icon' src='/assets/img/i1dmsdt.png']

#### data

Any sound data read from the file. For multi-channel sound data, **data** is an array of waveforms where each element of the array is a single channel.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Where This Node Can Run:**

Desktop OS: Windows

FPGA:

Web Server:

Parent topic:

Sound Input Read

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sound-input-read-i16.html language=enus -->
## TOPIC 00360: I16

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sound-input-read-i16.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sound-input-read-i16.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Reads 16-bit signed integer numeric data from a sound input device. The Y component of the waveform this node returns is an array of signed 16-bit integers. To create a task ID, use the Sound Input Configure node and wire the task ID output to the input of this node. number of samples/ch Number of s

I16

Reads 16-bit signed integer numeric data from a sound input device.

The Y component of the waveform this node returns is an array of signed 16-bit integers.

###### Programming Patterns

To create a task ID, use the Sound Input Configure node and wire the**task ID** output to the input of this node.

[IMAGE alt='connector_pane_image' src='Sound_Input_Read_(I16).gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### number of samples/ch

Number of samples per channel in the buffer. Use a large number of samples for continuous operations. Use a smaller number of samples if you want to use less memory.

**Default:**10,000

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

#### task ID in

Reference to the configured sound device you want to manipulate or input.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

#### timeout

Time, in seconds, that the node waits for the sound operation to complete. This node returns an error if the time elapses. If you set **timeout** to -1, the node waits indefinitely.

**Default:**10

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

#### task ID out

Reference to the configured sound device originally passed to the **task ID in** parameter.

[IMAGE alt='datatype_icon' src='/assets/img/i1dmsdt.png']

#### data

Any sound data read from the file. For multi-channel sound data, **data** is an array of waveforms where each element of the array is a single channel.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Where This Node Can Run:**

Desktop OS: Windows

FPGA:

Web Server:

Parent topic:

Sound Input Read

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sound-input-read-i32.html language=enus -->
## TOPIC 00361: I32

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sound-input-read-i32.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sound-input-read-i32.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Reads 32-bit signed integer numeric data from a sound input device. The Y component of the waveform this node returns is an array of signed 32-bit integers. To create a task ID, use the Sound Input Configure node and wire the task ID output to the input of this node. number of samples/ch Number of s

I32

Reads 32-bit signed integer numeric data from a sound input device.

The Y component of the waveform this node returns is an array of signed 32-bit integers.

###### Programming Patterns

To create a task ID, use the Sound Input Configure node and wire the**task ID** output to the input of this node.

[IMAGE alt='connector_pane_image' src='Sound_Input_Read_(I32).gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### number of samples/ch

Number of samples per channel in the buffer. Use a large number of samples for continuous operations. Use a smaller number of samples if you want to use less memory.

**Default:**10,000

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

#### task ID in

Reference to the configured sound device you want to manipulate or input.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

#### timeout

Time, in seconds, that the node waits for the sound operation to complete. This node returns an error if the time elapses. If you set **timeout** to -1, the node waits indefinitely.

**Default:**10

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

#### task ID out

Reference to the configured sound device originally passed to the **task ID in** parameter.

[IMAGE alt='datatype_icon' src='/assets/img/i1dmsdt.png']

#### data

Any sound data read from the file. For multi-channel sound data, **data** is an array of waveforms where each element of the array is a single channel.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Where This Node Can Run:**

Desktop OS: Windows

FPGA:

Web Server:

Parent topic:

Sound Input Read

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sound-input-read-sgl.html language=enus -->
## TOPIC 00362: SGL

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sound-input-read-sgl.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sound-input-read-sgl.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Reads single-precision, floating-point numeric data from a sound input device. The Y component of the waveform this node returns is an array of single-precision, floating-point numbers. To create a task ID, use the Sound Input Configure node and wire the task ID output to the input of this node. num

SGL

Reads single-precision, floating-point numeric data from a sound input device.

The Y component of the waveform this node returns is an array of single-precision, floating-point numbers.

###### Programming Patterns

To create a task ID, use the Sound Input Configure node and wire the**task ID** output to the input of this node.

[IMAGE alt='connector_pane_image' src='Sound_Input_Read_(SGL).gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### number of samples/ch

Number of samples per channel in the buffer. Use a large number of samples for continuous operations. Use a smaller number of samples if you want to use less memory.

**Default:**10,000

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

#### task ID in

Reference to the configured sound device you want to manipulate or input.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

#### timeout

Time, in seconds, that the node waits for the sound operation to complete. This node returns an error if the time elapses. If you set **timeout** to -1, the node waits indefinitely.

**Default:**10

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

#### task ID out

Reference to the configured sound device originally passed to the **task ID in** parameter.

[IMAGE alt='datatype_icon' src='/assets/img/i1dmsdt.png']

#### data

Any sound data read from the file. For multi-channel sound data, **data** is an array of waveforms where each element of the array is a single channel.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Where This Node Can Run:**

Desktop OS: Windows

FPGA:

Web Server:

Parent topic:

Sound Input Read

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sound-input-read-u8.html language=enus -->
## TOPIC 00363: U8

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sound-input-read-u8.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sound-input-read-u8.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Reads 8-bit unsigned integer numeric data from a sound input device. The Y component of the waveform this node returns is an array of unsigned 8-bit integers. To create a task ID, use the Sound Input Configure node and wire the task ID output to the input of this node. number of samples/ch Number of

U8

Reads 8-bit unsigned integer numeric data from a sound input device.

The Y component of the waveform this node returns is an array of unsigned 8-bit integers.

###### Programming Patterns

To create a task ID, use the Sound Input Configure node and wire the**task ID** output to the input of this node.

[IMAGE alt='connector_pane_image' src='Sound_Input_Read_(U8).gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### number of samples/ch

Number of samples per channel in the buffer. Use a large number of samples for continuous operations. Use a smaller number of samples if you want to use less memory.

**Default:**10,000

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

#### task ID in

Reference to the configured sound device you want to manipulate or input.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

#### timeout

Time, in seconds, that the node waits for the sound operation to complete. This node returns an error if the time elapses. If you set **timeout** to -1, the node waits indefinitely.

**Default:**10

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

#### task ID out

Reference to the configured sound device originally passed to the **task ID in** parameter.

[IMAGE alt='datatype_icon' src='/assets/img/i1dmsdt.png']

#### data

Any sound data read from the file. For multi-channel sound data, **data** is an array of waveforms where each element of the array is a single channel.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Where This Node Can Run:**

Desktop OS: Windows

FPGA:

Web Server:

Parent topic:

Sound Input Read

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sound-input-read.html language=enus -->
## TOPIC 00364: Sound Input Read

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sound-input-read.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sound-input-read.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `multimodeFunction`
- source_description: Reads data from a sound input device.

Sound Input Read

Reads data from a sound input device.

Sound Nodes

DBL

Reads double-precision, floating-point numeric data from a sound input device.

I16

Reads 16-bit signed integer numeric data from a sound input device.

I32

Reads 32-bit signed integer numeric data from a sound input device.

SGL

Reads single-precision, floating-point numeric data from a sound input device.

U8

Reads 8-bit unsigned integer numeric data from a sound input device.

Parent topic:

Sound Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sound-input-start.html language=enus -->
## TOPIC 00365: Sound Input Start

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sound-input-start.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sound-input-start.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Starts data acquisition from the device. This node is only necessary when you call Sound Input Stop. To create a task ID, use the Sound Input Configure node and wire the task ID output to the input of this node. task ID in Reference to the configured sound device you want to manipulate or input. err

Sound Input Start

Starts data acquisition from the device. This node is only necessary when you call Sound Input Stop.

###### Programming Patterns

To create a task ID, use the Sound Input Configure node and wire the**task ID** output to the input of this node.

[IMAGE alt='connector_pane_image' src='Sound_Input_Start.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

#### task ID in

Reference to the configured sound device you want to manipulate or input.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

#### task ID out

Reference to the configured sound device originally passed to the **task ID in** parameter.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Where This Node Can Run:**

Desktop OS: Windows

FPGA:

Web Server:

Parent topic:

Sound Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sound-input-stop.html language=enus -->
## TOPIC 00366: Sound Input Stop

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sound-input-stop.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sound-input-stop.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Stops data acquisition from the device. Use Sound Input Start to restart the acquisition after calling Sound Input Stop. To create a task ID, use the Sound Input Configure node and wire the task ID output to the input of this node. task ID in Reference to the configured sound device you want to mani

Sound Input Stop

Stops data acquisition from the device. Use Sound Input Start to restart the acquisition after calling Sound Input Stop.

###### Programming Patterns

To create a task ID, use the Sound Input Configure node and wire the**task ID** output to the input of this node.

[IMAGE alt='connector_pane_image' src='Sound_Input_Stop.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

#### task ID in

Reference to the configured sound device you want to manipulate or input.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

#### task ID out

Reference to the configured sound device originally passed to the **task ID in** parameter.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Where This Node Can Run:**

Desktop OS: Windows

FPGA:

Web Server:

Parent topic:

Sound Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sound-nodes.html language=enus -->
## TOPIC 00367: Sound Nodes

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sound-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sound-nodes.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `nodeCollection`

Sound Nodes

Sound File Close

.wav

Sound File Info

.wav

Sound File Open

.wav

.wav

Sound File Read

.wav

Sound File Read Simple

.wav

.wav

Sound File Write

.wav

Sound File Write Simple

.wav

.wav

Sound Input Clear

Stops acquisition of data, clears the buffer, returns the task ID to the default state, and clears the resources associated with the task ID.

Sound Input Configure

Sound Input Read

Sound Input Read

Reads data from a sound input device.

Sound Input Start

Sound Input Stop

Sound Input Stop

Sound Input Start

Sound Input Stop

Sound Output Clear

Stops the device from playing sound, clears the buffer, returns the task to the default state, and clears the resources associated with the task.

Sound Output Configure

Sound Output Write

Sound Output Info

Returns information about the current state of a sound output task.

Sound Output Set Volume

Sets the volume at which the sound output device plays.

Sound Output Start

Sound Input Stop

Sound Output Stop

Stops the device from playing sound from the buffer.

Sound Output Wait

Waits until the output device plays the entire sound file.

Sound Output Write

Sound Output Configure

Play Sound File

Opens a file and starts playing it immediately.

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sound-output-clear.html language=enus -->
## TOPIC 00368: Sound Output Clear

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sound-output-clear.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sound-output-clear.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Stops the device from playing sound, clears the buffer, returns the task to the default state, and clears the resources associated with the task. When you run this node, you can no longer use the task ID because this node removes all resources associated with the task ID. To create a task ID, use th

Sound Output Clear

Stops the device from playing sound, clears the buffer, returns the task to the default state, and clears the resources associated with the task. When you run this node, you can no longer use the task ID because this node removes all resources associated with the task ID.

###### Programming Patterns

To create a task ID, use the Sound Output Configure node and wire the **task ID** output to the input of this node.

[IMAGE alt='connector_pane_image' src='Sound_Output_Clear.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

#### task ID

Reference to the configured sound device you want to manipulate or input.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs. Unlike most nodes, this node runs normally even if an error occurs before this node runs.

**Default:**no error

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

Unlike most nodes, this node runs normally even if **error in** contains an error.

**Where This Node Can Run:**

Desktop OS: Windows

FPGA:

Web Server:

Parent topic:

Sound Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sound-output-configure.html language=enus -->
## TOPIC 00369: Sound Output Configure

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sound-output-configure.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sound-output-configure.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Configures a sound output device to receive data. Use Sound Output Write to write data to the device. number of samples/ch Number of samples per channel in the buffer. Continuous operations require an increased number of samples to improve data quality but require the use of more memory. 100,000 sam

Sound Output Configure

Configures a sound output device to receive data. Use Sound Output Write to write data to the device.

[IMAGE alt='connector_pane_image' src='Sound_Output_Configure.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### number of samples/ch

Number of samples per channel in the buffer. Continuous operations require an increased number of samples to improve data quality but require the use of more memory.

**Default:**100,000

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

#### sample mode

Setting to generate samples once or continuously.

| Name | Value | Description |
| --- | --- | --- |
| Finite Samples | 0 | Generate samples once. This mode calls Sound Output Write and only writes until you reach the number of samples specified in number of samples/ch. |
| Continuous Samples | 1 | Generate samples continuously. This mode calls Sound Output Write repeatedly as needed. |

**Default:**1—Continuous Samples

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

#### device ID

The input or output device you access for a sound operation. The value ranges from 0 to 
*n*-1, where 
*n* is the number of input or output devices on the computer.

**Default:**0

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

#### sound format

The acquisition rate, the number of channels, and the bits per sample of the sound operation. The values for each of these elements is dependent on your sound card.

Not all operating systems and sound cards support all **sample rate (S/s)**, **number of channels**, or **bits per sample** options.

Performance Details

**sample rate (S/s)** and **bits per sample** use more computer memory when set to a higher value.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### sample rate (S/s)

Sampling rate for the sound operation. Common rates are 44,100 S/s, 22,050 S/s, and 11,025 S/s.

**Default:**22,050 S/s

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### number of channels

Number of channels. This input can accept as many channels as the sound card supports. For most sound cards 1 is mono and 2 is stereo.

**Default:**2

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### bits per sample

Quality of each sample in bits. Available resolutions are 8 bits, 16 bits, and 32 bits.

**Default:**16 bits

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

#### task ID

Reference to the configured sound device. You can pass **task ID** to other sound operation nodes.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Where This Node Can Run:**

Desktop OS: Windows

FPGA:

Web Server:

Parent topic:

Sound Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sound-output-info.html language=enus -->
## TOPIC 00370: Sound Output Info

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sound-output-info.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sound-output-info.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Returns information about the current state of a sound output task. To create a task ID, use the Sound Output Configure node and wire the task ID output to the input of this node. task ID in Reference to the configured sound device you want to manipulate or input. error in Error conditions that occu

Sound Output Info

Returns information about the current state of a sound output task.

###### Programming Patterns

To create a task ID, use the Sound Output Configure node and wire the **task ID** output to the input of this node.

[IMAGE alt='connector_pane_image' src='Sound_Output_Info.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

#### task ID in

Reference to the configured sound device you want to manipulate or input.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

#### task ID out

Reference to the configured sound device originally passed to the **task ID in** parameter.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

#### is playing?

A Boolean that indicates if the sound output task is playing.

| True | The sound output task is playing. |
| --- | --- |
| False | The sound output task is not playing. |

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

#### volume

Volume of the sound operation, one value per channel. 0 is silent, and 100 is the loudest volume.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Where This Node Can Run:**

Desktop OS: Windows

FPGA:

Web Server:

Parent topic:

Sound Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sound-output-set-volume.html language=enus -->
## TOPIC 00371: Sound Output Set Volume

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sound-output-set-volume.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sound-output-set-volume.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Sets the volume at which the sound output device plays. To create a task ID, use the Sound Output Configure node and wire the task ID output to the input of this node. task ID in Reference to the configured sound device you want to manipulate or input. volume Volume of the sound operation. 0 is sile

Sound Output Set Volume

Sets the volume at which the sound output device plays.

###### Programming Patterns

To create a task ID, use the Sound Output Configure node and wire the **task ID** output to the input of this node.

[IMAGE alt='connector_pane_image' src='Sound_Output_Set_Volume_(Single).gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

#### task ID in

Reference to the configured sound device you want to manipulate or input.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

#### volume

Volume of the sound operation. 
0 is silent, and 
100 is the loudest volume.

This input accepts either a single numeric value or a 1D array of numeric values.

**Default:**100

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

#### task ID out

Reference to the configured sound device originally passed to the **task ID in** parameter.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Where This Node Can Run:**

Desktop OS: Windows

FPGA:

Web Server:

Parent topic:

Sound Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sound-output-start.html language=enus -->
## TOPIC 00372: Sound Output Start

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sound-output-start.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sound-output-start.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Starts playback from the device. This node is only necessary when you call Sound Input Stop. To create a task ID, use the Sound Output Configure node and wire the task ID output to the input of this node. task ID in Reference to the configured sound device you want to manipulate or input. error in E

Sound Output Start

Starts playback from the device. This node is only necessary when you call Sound Input Stop.

###### Programming Patterns

To create a task ID, use the Sound Output Configure node and wire the **task ID** output to the input of this node.

[IMAGE alt='connector_pane_image' src='Sound_Output_Start.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

#### task ID in

Reference to the configured sound device you want to manipulate or input.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

#### task ID out

Reference to the configured sound device originally passed to the **task ID in** parameter.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Where This Node Can Run:**

Desktop OS: Windows

FPGA:

Web Server:

Parent topic:

Sound Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sound-output-stop.html language=enus -->
## TOPIC 00373: Sound Output Stop

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sound-output-stop.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sound-output-stop.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Stops the device from playing sound from the buffer. To create a task ID, use the Sound Output Configure node and wire the task ID output to the input of this node. task ID in Reference to the configured sound device you want to manipulate or input. error in Error conditions that occur before this n

Sound Output Stop

Stops the device from playing sound from the buffer.

###### Programming Patterns

To create a task ID, use the Sound Output Configure node and wire the **task ID** output to the input of this node.

[IMAGE alt='connector_pane_image' src='Sound_Output_Stop.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

#### task ID in

Reference to the configured sound device you want to manipulate or input.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

#### task ID out

Reference to the configured sound device originally passed to the **task ID in** parameter.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Where This Node Can Run:**

Desktop OS: Windows

FPGA:

Web Server:

Parent topic:

Sound Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sound-output-wait.html language=enus -->
## TOPIC 00374: Sound Output Wait

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sound-output-wait.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sound-output-wait.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Waits until the output device plays the entire sound file. To create a task ID, use the Sound Output Configure node and wire the task ID output to the input of this node. task ID in Reference to the configured sound device you want to manipulate or input. error in Error conditions that occur before

Sound Output Wait

Waits until the output device plays the entire sound file.

###### Programming Patterns

To create a task ID, use the Sound Output Configure node and wire the **task ID** output to the input of this node.

[IMAGE alt='connector_pane_image' src='Sound_Output_Wait.gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

#### task ID in

Reference to the configured sound device you want to manipulate or input.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

#### timeout

Time, in seconds, that the node waits for the sound operation to complete. This node returns an error if the time elapses. If you set **timeout** to -1, the node waits indefinitely.

**Default:**10

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

#### task ID out

Reference to the configured sound device originally passed to the **task ID in** parameter.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Where This Node Can Run:**

Desktop OS: Windows

FPGA:

Web Server:

Parent topic:

Sound Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=sound-output-write.html language=enus -->
## TOPIC 00375: Sound Output Write

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `sound-output-write.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/sound-output-write.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `vi`
- source_description: Writes data to a sound output device. You must use Sound Output Configure to configure the device if you are writing continuously. If the buffer you set using the number of samples/ch input of Sound File Read is full when the node executes, an automatic wait is implemented on Sound Output Write even

Sound Output Write

Writes data to a sound output device. You must use Sound Output Configure to configure the device if you are writing continuously.

Note

number of samples/ch

Sound File Read

Sound Output Write

timeout

###### Programming Patterns

To create a task ID, use the Sound Output Configure node and wire the **task ID** output to the input of this node.

[IMAGE alt='connector_pane_image' src='Sound_Output_Write_(DBL_Single).gvi.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

#### task ID in

Reference to the configured sound device you want to manipulate or input.

[IMAGE alt='datatype_icon' src='/assets/img/c1dmsdt.png']

#### data

Sound data to write to the 
.wav file. For multi-channel sound data, **data** is an array of waveforms where each element of the array is a single channel.

- An array of waveforms, where the Y array contains single-precision, floating-point numeric data
- An array of waveforms, where the Y array contains double-precision, floating-point numeric data
- A single waveform of double-precision, floating-point numeric data
- An array of waveforms, where the Y array contains signed 16-bit integer data
- An array of waveforms, where the Y array contains signed 32-bit integer data
- An array of waveforms, where the Y array contains unsigned 8-bit integer data

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

#### timeout

Time, in seconds, that the function waits for the sound operation to complete. This node returns an error if the time elapses. If you set **timeout** to -1, the node waits indefinitely. If you set **timeout** to 0, the node returns immediately while the sound continues to play. You can use Sound Output Wait to wait for playback to complete.

**Default:**10

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

#### task ID out

Reference to the configured sound device originally passed to the **task ID in** parameter.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Where This Node Can Run:**

Desktop OS: Windows

FPGA:

Web Server:

Parent topic:

Sound Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=space.html language=enus -->
## TOPIC 00376: Space Constant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `space.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/space.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use this constant to supply a one-character space string to the diagram.

Space Constant

Use this constant to supply a one-character space string to the diagram.

[IMAGE alt='1378' src='Literal.String.Space_Constant.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=speed-of-light.html language=enus -->
## TOPIC 00377: Speed of Light Constant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `speed-of-light.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/speed-of-light.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value 299792458.

Speed of Light Constant

Returns the value 299792458.

[IMAGE alt='1378' src='Literal.Numeric.Speed_Of_Light_Constant.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=split-1d-array.html language=enus -->
## TOPIC 00378: Split 1D Array

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `split-1d-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/split-1d-array.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Divides an array at a specified index and returns the two portions. The element at the specified index appears at the beginning of the second portion. array A 1D array of any type. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, this input has a default data type

Split 1D Array

Divides an array at a specified index and returns the two portions.

The element at the specified index appears at the beginning of the second portion.

[IMAGE alt='1378' src='Split1DArray.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### array

A 1D array of any type.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### index

The location that specifies where to split array. If index is negative or 0, first subarray is empty. If index is equal to or greater than the size of array, second subarray is empty.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### first subarray

array[0] through array[index-1].

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### second subarray

The remaining array elements not already contained in first subarray.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

Parent topic:

Array Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=split-number.html language=enus -->
## TOPIC 00379: Split Number

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `split-number.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/split-number.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Breaks a number into its component bytes or words. x An 8-, 16-, 32-, or 64-bit integer, or an array or cluster of those representations. high(x) An integer that is half the width of x. This output is an 8-bit, 16-bit, or 32-bit unsigned integers, respectively, or an array or cluster of those repres

Split Number

Breaks a number into its component bytes or words.

[IMAGE alt='1378' src='SplitNumber.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### x

An 8-, 16-, 32-, or 64-bit integer, or an array or cluster of those representations.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### high(x)

An integer that is half the width of x.

This output is an 8-bit, 16-bit, or 32-bit unsigned integers, respectively, or an array or cluster of those representations.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### low(x)

An integer that is half the width of x.

This output is an 8-bit, 16-bit, or 32-bit unsigned integers, respectively, or an array or cluster of those representations.

Parent topic:

Data Manipulation Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=square-root.html language=enus -->
## TOPIC 00380: Square Root

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `square-root.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/square-root.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the square root of an input value. x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, arrays of clusters of numbers, and waveforms. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, this input has a default data

Square Root

Computes the square root of an input value.

[IMAGE alt='1378' src='SquareRoot.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, arrays of clusters of numbers, and waveforms.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### square root

The square root of the input value.

##### Behavior with Various x Input Types

square root is a double-precision, floating-point number if x is an integer.

If x is less than 0, sqrt(x) is not a number (NaN), unless x is complex. When x is complex, this node defines the magnitude and phase with the following equations:

where |x| is the magnitude of x and arg(x) is the phase of x:

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=square.html language=enus -->
## TOPIC 00381: Square

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `square.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/square.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the square of the input value. x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, arrays of clusters of numbers, and waveforms. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, this input has a default data typ

Square

Computes the square of the input value.

[IMAGE alt='1378' src='Square.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, arrays of clusters of numbers, and waveforms.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### x^2

The square of the input value.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=start-asynchronous-call.html language=enus -->
## TOPIC 00382: Start Asynchronous Call

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `start-asynchronous-call.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/start-asynchronous-call.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Begins an asynchronous call to the VI you specify with a reference. Depending on how you set up Open VI Reference to prepare reference in for asynchronous execution, you can either ignore the node after calling it or collect its outputs at a later time with the Wait on Asynchronous Call node. refere

Start Asynchronous Call

Begins an asynchronous call to the VI you specify with a reference.
 Depending on how you set up Open VI Reference to prepare reference in for asynchronous execution, you can either ignore the node after calling it or collect its outputs at a later time with the Wait on Asynchronous Call node.

[IMAGE alt='1378' src='StartAsynchronousCall.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### reference in

Reference to a target node you want to call asynchronously.

Open VI Reference

Item

Open VI Reference

Prepare for asynchronous call without wait

Prepare for asynchronous call with wait

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### reference out

Unchanged reference associated with the strictly typed VI reference.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

#### Accessing Inputs and Outputs of the Referenced VI

When you wire a strictly typed VI reference to Start Asynchronous Call, the node automatically displays the input terminals of the referenced VI. Wire data to the input terminals of Start Asynchronous Call to pass the data to the called VI.

Because the purpose of the Start Asynchronous Call node is to start a VI call without waiting for it to complete, the outputs of the VI are not available from the Start Asynchronous Call node. To retrieve data from the outputs of the target VI, use the Wait on Asynchronous Call node.

#### Serial or Parallel Execution

When you pass the same VI reference to multiple Start Asynchronous Call nodes, the application serializes the calls by default. To allow parallel execution, make the target VI reentrant and configure it as 
 Enable simultaneous calls for reentrant VIs when you open its reference with Open VI Reference. Regardless of whether the calls execute serially or simultaneously, this node returns immediately, allowing dataflow to continue in the calling VI.

#### Start Asynchronous Call Does Not Modify VI Clones

If you configure the VI reference to execute parallel instances of a reentrant target VI when you open a reference to a target VI, the Start Asynchronous Call node starts a call to a clone of the referenced VI, not to the referenced VI itself. Therefore, if you call a VI server node on the original reference that the Open VI Reference node returns, the effects of that node are not reflected in the VI clone that Start Asynchronous Call actually calls. To perform tasks such as opening or positioning the panel on the VI that is actually called, you must call the node within the reentrant VI itself.

Parent topic:

Execution Control

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=static-vi-reference.html language=enus -->
## TOPIC 00383: Static VI Reference

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `static-vi-reference.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/static-vi-reference.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `lvFunction`
- source_description: Maintains a static reference to a VI. Configure this node to return a generic or strictly typed VI reference. After you place this node on a diagram, drag a VI onto the node. Configuring a Static VI Reference To configure a Static VI Reference navigate to the Item tab, click the button next to the R

Static VI Reference

Maintains a static reference to a VI. Configure this node to return a generic or strictly typed VI reference. After you place this node on a diagram, drag a VI onto the node.

[IMAGE alt='connector_pane_image' src='StaticVIReference.png']

- Inputs/Outputs
- Details
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

#### VI reference

The reference to the configured VI.

#### Configuring a Static VI Reference

Static VI Reference

Item

Note

Static VI Reference

Static VI Reference

Specify whether the Static VI Reference is strictly typed on the 
 Item tab.

#### Static VI Reference Output

Static VI Reference

To change the output of this node to a strictly typed VI reference, select 
 Strictly Typed Reference on the 
 Item tab. The strictly typed VI reference identifies the VI you are calling. You can create a strictly typed VI reference only from a VI, not from a non-VI file such as a control.

#### Strictly Typed VI References

Use a strictly typed VI reference if you want to call the referenced VI with Call by Reference or Start Asynchronous Call. When you create a strictly typed VI reference, you can wire **VI reference** to the Run VI node.

The application loads the referenced VI into memory when you load the top-level VI. When Static VI Reference outputs a strictly typed VI reference, the application reserves the referenced VI as long as the top-level VI is running. The application closes this reference when the top-level VI is no longer in memory. You do not have to explicitly close the reference this node returns.

Note

Static VI Reference

Open VI Reference

If you want the compiler to check for a broken referenced VI before you run the top-level VI, use the referenced VI directly in the top-level VI instead of using Static VI Reference.

#### Using Strictly Typed VI References with Run VI

A strictly typed static VI reference also reserves any subVIs when a top-level VI is reserved, therefore you get a runtime error if you attempt to run the referenced VI using the RunVI node and any of the reserved VIs have a caller that is already running.

Parent topic:

Execution Control

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=storage-nodes.html language=enus -->
## TOPIC 00384: Storage Nodes

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `storage-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/storage-nodes.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Access data via files.

Storage Nodes

Access data via files.

Write Delimited Spreadsheet

Converts data to a text string and writes the string to a file.

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=string-constant.html language=enus -->
## TOPIC 00385: String Constant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `string-constant.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/string-constant.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a text string that you enter on the diagram.

String Constant

Represents a text string that you enter on the diagram.

[IMAGE alt='1378' src='Literal.String.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=string-length.html language=enus -->
## TOPIC 00386: String Length

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `string-length.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/string-length.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of characters in a string. string A string whose number of characters you want to compute. This input also supports any data type that includes only strings, such as an array of strings or a cluster of strings. length Number of characters in a string. The structure of this output

String Length

Returns the number of characters in a string.

[IMAGE alt='1378' src='StringLength.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### string

A string whose number of characters you want to compute.

This input also supports any data type that includes only strings, such as an array of strings or a cluster of strings.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### length

Number of characters in a string.

The structure of this output matches the structure of the string. For example, if you wire an array of strings to string, this output returns an array of integers. Likewise, if you wire a cluster of strings to string, this output returns a cluster of integers.

Note

16

#### Reducing Performance Burden

Characters in UTF-8 can be multiple bytes so string nodes count the number of characters in a string instead of jumping to a point in memory. Since the length and offset parameters are in units of characters, avoid nesting this node with large strings because that can create exponential functions that carry a higher performance burden.

Parent topic:

String Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=string-nodes.html language=enus -->
## TOPIC 00387: String Nodes

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `string-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/string-nodes.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`

String Nodes

Append True Or False String

Appends one of two possible strings, determined by a Boolean value, to another string you specify.

Concatenate Strings

Concatenates input strings and/or 1D arrays of strings into a single output string.

Format Value

Converts a number into a regular string and appends the result to the input string.

Match Pattern

Searches for a pattern of characters in a string as specified by a limited set of regular expressions.

Pick Line

Copies a specified line from one string and appends that line to another string.

Replace Substring

Deletes a specified length of characters in a string and replaces the deleted portion with another string.

Reverse String

Produces a string whose characters are in reverse order of those in an input string.

Rotate String

Moves the first character of a string to the end of the string.

Scan Value

Converts the characters at the beginning of a string to a numeric value, using format specifiers to determine the representation and precision of the resulting number.

Search and Replace Pattern

Searches for a pattern in the input string and replaces either the first match or every match with a substring you specify.

Search/Split String

Divides a single string into two substrings.

String Length

Returns the number of characters in a string.

String Subset

Returns a portion, or substring, of a string.

To Lowercase

Converts all alphabetic characters in a string to lowercase characters.

To Uppercase

Converts all alphabetic characters in a string to uppercase characters.

Trim Whitespace

Removes all ASCII whitespace, such as spaces, tabs, carriage returns, and linefeeds, from the beginning, end, or both ends of the input string.

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=string-subset.html language=enus -->
## TOPIC 00388: String Subset

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `string-subset.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/string-subset.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a portion, or substring, of a string. string The string from which you want to obtain a subset. offset The number of characters into the input string at which this node begins its operation. The offset of the first character in the input string is 0. If offset is beyond the end of the input

String Subset

Returns a portion, or substring, of a string.

[IMAGE alt='1378' src='StringSubset.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### string

The string from which you want to obtain a subset.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### offset

The number of characters into the input string at which this node begins its operation.

The offset of the first character in the input string is 0. If offset is beyond the end of the input string, this node returns an empty string.

Note

16

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### length

The number of characters you want to include in the substring.

If length is negative or 0, this node returns an empty string.

Note

Default value: The entire length of string minus offset.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### substring

The portion of the input string that is the specified length beginning at the offset.

Note

#### Reducing Performance Burden

Characters in UTF-8 can be multiple bytes so string nodes count the number of characters in a string instead of jumping to a point in memory. Since the length and offset parameters are in units of characters, avoid nesting this node with large strings because that can create exponential functions that carry a higher performance burden.

Parent topic:

String Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=string-to-byte-array.html language=enus -->
## TOPIC 00389: String To Byte Array

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `string-to-byte-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/string-to-byte-array.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a string into an array of unsigned bytes. encoding The character encoding the node uses to convert the input. UTF-8 Converts the input using UTF-8 encoding. UTF-16 Converts the input using UTF-16 encoding. Extended ASCII Converts the input using extended ASCII encoding. string String you wa

String To Byte Array

Converts a string into an array of unsigned bytes.

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### encoding

The character encoding the node uses to convert the input.

| UTF-8 | Converts the input using UTF-8 encoding. |
| --- | --- |
| UTF-16 | Converts the input using UTF-16 encoding. |
| Extended ASCII | Converts the input using extended ASCII encoding. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### string

String you want the node to convert.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Default value: No error

Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/i1du8.png']

##### unsigned byte array

Converted array.

string

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=subtract.html language=enus -->
## TOPIC 00390: Subtract

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `subtract.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/subtract.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the difference between numbers, timestamps, or waveforms. You cannot subtract a timestamp from a numeric value. x The value to subtract from. This input supports scalar numbers, enumerated type values, timestamps, waveforms, and any data type that contains only these data types, such as an

Subtract

Computes the difference between numbers, timestamps, or waveforms.

You cannot subtract a timestamp from a numeric value.

[IMAGE alt='1378' src='Subtract.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

The value to subtract from.

This input supports scalar numbers, enumerated type values, timestamps, waveforms, and any data type that contains only these data types, such as an array or cluster of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### y

The value to subtract from the other input.

This input supports scalar numbers, enumerated type values, timestamps, waveforms, and any data type that contains only these data types, such as an array or cluster of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

This input appears only when you wire a waveform to input.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### x - y

The difference between the two inputs.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this output has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

The node produces this output according to standard error behavior.

This output appears only when you wire a waveform to input.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Numeric Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=tab.html language=enus -->
## TOPIC 00391: Tab Constant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `tab.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/tab.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Consists of a constant string containing the horizontal tab value. Use this constant when you do not want to type in the backslash code for the character.

Tab Constant

Consists of a constant string containing the horizontal tab value.

Use this constant when you do not want to type in the backslash code for the character.

[IMAGE alt='1378' src='Literal.String.Tab_Constant.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=tangent.html language=enus -->
## TOPIC 00392: Tangent

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `tangent.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/tangent.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the tangent of a specified value (x) in radians. x An input to this operation. This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA When you add this node to a document targeted to an FPGA, this input has a default d

Tangent

Computes the tangent of a specified value (x) in radians.

[IMAGE alt='1378' src='Tangent.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### x

An input to this operation.

This input supports scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### tan

Result of the operation.

x

x

x

i

x

tan

Parent topic:

Trigonometric Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=this-vi-reference.html language=enus -->
## TOPIC 00393: This VI Reference (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `this-vi-reference.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/this-vi-reference.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `lvFunction`
- source_description: Returns a static VI reference to the current VI. You can use this reference to access the properties of the VI. reference out Static VI reference to the current VI.

This VI Reference

Returns a static VI reference to the current VI. You can use this reference to access
 the properties of the VI.

[IMAGE alt='connector_pane_image' src='ThisVIReference.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

#### reference out

Static VI reference to the current VI.

Parent topic:

Execution Control

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=threshold-1d-array.html language=enus -->
## TOPIC 00394: Threshold 1D Array

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `threshold-1d-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/threshold-1d-array.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Interpolates points in a 1D array that represents a 2D non-descending graph. This node compares a threshold to the values in an array, starting at a specified index, until it finds a pair of consecutive elements such that the threshold is greater than the value of the first element and less than or

Threshold 1D Array

Interpolates points in a 1D array that represents a 2D non-descending graph.
 This node compares a threshold to the values in an array, starting at a specified index, until it finds a pair of consecutive elements such that the threshold is greater than the value of the first element and less than or equal to the value of the second element.

[IMAGE alt='1378' src='Threshold1DArray.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### array of numbers or points

An array of numbers or an array of points where each point is a cluster of x- and y-coordinates.

If this input is an array of numbers, this node assumes the x-coordinates are the same as the indexes of the array itself.

If this input is an array of points, this node uses the second elements in the clusters, or the y-coordinates, to obtain a fractional index that it then uses to interpolate the corresponding x value.

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### threshold y

The threshold value for the node. If threshold y is less than or equal to the array value at start index, the node returns start index for fractional index or x. If threshold y is greater than every value in the array, the node returns the index of the last value. If the array is empty, the node returns 
NaN.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### start index

The index to start interpolation.

Default value: 0—The node returns the result calculated from the entire array rather than a specified section of the array.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### fractional index or x

The interpolated result calculated for the array of numbers or points 1D input array.

If array of numbers or points is an array of points where each point is a cluster of x- and y-coordinates, fractional index or x is the interpolated x value corresponding to the interpolated position of threshold y among the y-coordinates, rather than the fractional index of the array. fractional index or x returns the interpolated x value associated with the given y value if you graphed the points.

#### Examples

| array of numbers or points | start index | threshold y | fractional index or x | comments |
| --- | --- | --- | --- | --- |
| [4, 5, 5, 6] | 0 | 5 | 1 | The output is 1, corresponding to the index of the first value of 5 the node finds. |
| [2.3, 5.2, 7.8, 7.9, 10.0] | 0 | 6.5 | 1.5 | The output is 1.5 because 6.5 is halfway between 5.2 (index 1) and 7.8 (index 2). |
| [0, 1, 2, 3, 4, 9.1, 10.3, 12.9, 15.5] | 5 | 14.2 | 7.5 | threshold y falls between elements 7 and 8 because 14.2 is midway between 12.9 and 15.5. Therefore, the output is 7.5, halfway between 7 and 8. |
| Array of points [(1,1), (2,2), (3,3), (4,4), (-2.5,5), (0,6) | 0 | 5.5 | -1.25 | The output is not an index value of 4.5 as it would be for a numeric array, but rather an x value of -1.25, which is the interpolated x value associated with the given y value if you graphed the points. |

#### Method for Calculating Fractional Index

This node calculates the fractional distance between the first value and threshold y and returns the fractional index at which threshold y would be placed within array of numbers or points using linear interpolation.

#### Use Threshold 1D Array Only with Non-Descending Arrays

This node only returns a reliable fractional index or x result for non-descending arrays. This node might return unexpected data for the following reasons:

- This node does not recognize the index of a negative slope crossing.
- This node does not return multiple fractional index or x results if the input array crosses threshold y at multiple points.
- This node returns the start index value if threshold y is less than the value at start index .

Use Threshold Detector for more advanced analysis of arrays.

Parent topic:

Array Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=tick-count-ms.html language=enus -->
## TOPIC 00395: Milliseconds

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `tick-count-ms.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/tick-count-ms.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value of the millisecond timer. millisecond timer value Value of the operating system's millisecond timer. Timer Count Time vs. Real-World Time The base reference time (millisecond zero) for this node is undefined, so you cannot convert the output value to a real-world time or date. Mill

Milliseconds

Returns the value of the millisecond timer.

[IMAGE alt='1378' src='TickCount.Milliseconds.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### millisecond timer value

Value of the operating system's millisecond timer.

#### Timer Count Time vs. Real-World Time

The base reference time (millisecond zero) for this node is undefined, so you cannot convert the output value to a real-world time or date.

#### Millisecond Timer Wrap Behavior

Be careful when you use this node in comparisons because the value of the millisecond timer wraps from 
 (2^32)-1 to 
 0. You can also change the value at which the millisecond timer wraps by changing the size of the output integer.

Parent topic:

Timer Count

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=tick-count-ticks.html language=enus -->
## TOPIC 00396: Ticks

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `tick-count-ticks.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/tick-count-ticks.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value of the tick timer. tick timer value Value of the operating system's tick timer. Timer Count Time vs. Real-World Time The base reference time (tick zero) for this node is undefined, so you cannot convert the output value to a real-world time or date. Tick Timer Wrap Behavior Be care

Ticks

Returns the value of the tick timer.

[IMAGE alt='1378' src='TickCount.Ticks.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### tick timer value

Value of the operating system's tick timer.

#### Timer Count Time vs. Real-World Time

The base reference time (tick zero) for this node is undefined, so you cannot convert the output value to a real-world time or date.

#### Tick Timer Wrap Behavior

Be careful when you use this node in comparisons because the value of the tick timer wraps from 
 (2^32)-1 to 
 0. You can also change the value at which the tick timer wraps by changing the size of the output integer.

Parent topic:

Timer Count

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=tick-count-us.html language=enus -->
## TOPIC 00397: Microseconds

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `tick-count-us.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/tick-count-us.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value of the microsecond timer. microsecond timer value Value of the operating system's microsecond timer. Timer Count Time vs. Real-World Time The base reference time (microsecond zero) for this node is undefined, so you cannot convert the output value to a real-world time or date. Micr

Microseconds

Returns the value of the microsecond timer.

[IMAGE alt='1378' src='TickCount.Microseconds.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### microsecond timer value

Value of the operating system's microsecond timer.

#### Timer Count Time vs. Real-World Time

The base reference time (microsecond zero) for this node is undefined, so you cannot convert the output value to a real-world time or date.

#### Microsecond Timer Wrap Behavior

Be careful when you use this node in comparisons because the value of the microsecond timer wraps from 
 (2^32)-1 to 
 0. You can also change the value at which the microsecond timer wraps by changing the size of the output integer.

Parent topic:

Timer Count

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=tick-count.html language=enus -->
## TOPIC 00398: Timer Count

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `tick-count.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/tick-count.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value of the timer.

Timer Count

Returns the value of the timer.

Program Flow Nodes

Milliseconds

Returns the value of the millisecond timer.

Microseconds

Returns the value of the microsecond timer.

Ticks

Returns the value of the tick timer.

Parent topic:

Program Flow Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=timestamp-constant.html language=enus -->
## TOPIC 00399: Timestamp Constant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `timestamp-constant.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/timestamp-constant.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a date and time value on the diagram.

Timestamp Constant

Represents a date and time value on the diagram.

[IMAGE alt='1378' src='Literal.Timestamp.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=timestamp-nodes.html language=enus -->
## TOPIC 00400: Timestamp Nodes

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `timestamp-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/timestamp-nodes.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`

Timestamp Nodes

Get Current Time

Returns a timestamp of the current time.

Get Date and Time String

Converts a timestamp value or a number of seconds to a date and time string in the time zone configured for the computer.

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=timestamp-to-date-and-time.html language=enus -->
## TOPIC 00401: Timestamp to Date and Time

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `timestamp-to-date-and-time.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/timestamp-to-date-and-time.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a timestamp or a number of seconds to a set of individual values that represent a date and time. timestamp The time that you want to convert. The year in this timestamp must be between 1600 and 3000. If you wire a numeric value to this input, the node interprets the number as the time-zone-

Timestamp to Date and Time

Converts a timestamp or a number of seconds to a set of individual values that represent a date and time.

[IMAGE alt='1378' src='TimestampToDateAndTime.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ctimestamp.png']

##### timestamp

The time that you want to convert.

The year in this timestamp must be between 1600 and 3000.

If you wire a numeric value to this input, the node interprets the number as the time-zone-independent number of seconds that have elapsed since 12:00 a.m. on January 1, 1904, Universal Time [01-01-1904 00:00:00]. The node interprets a negative number as the number of seconds before this time.

Default value: The current date and time

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### to UTC?

Boolean that changes date time record to Universal Time.

| True | date time record is in Universal Time. |
| --- | --- |
| False | date time record is in the configured time zone for the computer. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/inclst.png']

##### date time record

Date and time represented as a cluster of numeric values.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### fractional second

Fractions of a second since the start of the second. Values must be greater than or equal to 0 and less than 1.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### second

Number of complete seconds since the start of the minute. Values can be 0 to 59.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### minute

Number of complete minutes since the start of the hour. Values can be 0 to 59.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### hour

Number of complete hours since midnight. Values can be 0 to 23.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### day of month

Values can be 1 to 31.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### month

Values can be 1 to 12.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### year

Values can be from 1600 to 3000.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### day of week

Values can be 1 to 7, which correspond to Sunday through Saturday, respectively.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### day of year

Values can be 1 to 366.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### DST

Value can be 0 for standard or 1 for daylight saving time. If to UTC? is TRUE, DST is 0 (standard).

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=to-double-precision-complex.html language=enus -->
## TOPIC 00402: To Double Precision Complex

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `to-double-precision-complex.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/to-double-precision-complex.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a number to a double-precision, complex number. number An input to this operation. This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA When you add thi

To Double Precision Complex

Converts a number to a double-precision, complex number.

[IMAGE alt='1378' src='ToDoublePrecisionComplex.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### number

An input to this operation.

This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/icdb.png']

##### double precision complex

Result of the conversion.

This output assumes the same data type structure as 
 number.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=to-double-precision-float.html language=enus -->
## TOPIC 00403: To Double Precision Float

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `to-double-precision-float.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/to-double-precision-float.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a number to a double-precision, floating-point number. number An input to this operation. This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA When you

To Double Precision Float

Converts a number to a double-precision, floating-point number.

[IMAGE alt='1378' src='ToDoublePrecisionFloat.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### number

An input to this operation.

This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### double precision float

Result of the conversion.

This output assumes the same data type structure as 
 number.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=to-lowercase.html language=enus -->
## TOPIC 00404: To Lowercase

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `to-lowercase.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/to-lowercase.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts all alphabetic characters in a string to lowercase characters. This node does not modify non-alphabetic characters. string The string you want to modify. This input can also be any data type that contains only strings, such as an array or cluster of strings. all lowercase string The convert

To Lowercase

Converts all alphabetic characters in a string to lowercase characters.
 This node does not modify non-alphabetic characters.

[IMAGE alt='1378' src='ToLowerCase.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### string

The string you want to modify.

This input can also be any data type that contains only strings, such as an array or cluster of strings.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### all lowercase string

The converted version of the input string in which all uppercase characters are now lowercase.

string

Parent topic:

String Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=to-more-generic-class.html language=enus -->
## TOPIC 00405: To More Generic Class

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `to-more-generic-class.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/to-more-generic-class.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Typecasts a class object or a class reference to a class above the object or reference in the inheritance hierarchy. You can use this node to typecast any object or reference in a class hierarchy, including VI Server references, .NET/ActiveX references, and classes you create. reference Class refere

To More Generic Class

Typecasts a class object or a class reference to a class above the object or reference in the inheritance hierarchy.

You can use this node to typecast any object or reference in a class hierarchy, including VI Server references, .NET/ActiveX references, and classes you create.

[IMAGE alt='1378' src='ToMoreGenericClass.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/clabview_objectlvclass.png']

##### reference

Class reference or class object you want to typecast to a target class within the inheritance hierarchy.

[IMAGE alt='datatype_icon' src='/assets/img/clabview_objectlvclass.png']

##### target class

Class you want reference to match.

[IMAGE alt='datatype_icon' src='/assets/img/ilabview_objectlvclass.png']

##### generic class reference

Class reference or class object typecast to the target class.

#### Typecasting Classes

Typecasting changes the data type of an input to that of the class you specify. This allows you to access the object or reference you input as if it is the target class you specify.

Parent topic:

Classes Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=to-more-specific-class.html language=enus -->
## TOPIC 00406: To More Specific Class (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `to-more-specific-class.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/to-more-specific-class.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `lvFunction`
- source_description: Typecasts a class object or class reference to a class below the object or reference in the inheritance hierarchy. You can use this node to typecast any object or reference in a class hierarchy, including VI Server references, .NET/ActiveX references, and classes you create. reference Class referenc

To More Specific Class

Typecasts a class object or class reference to a class below the object or reference in the inheritance hierarchy.

You can use this node to typecast any object or reference in a class hierarchy, including VI Server references, .NET/ActiveX references, and classes you create.

[IMAGE alt='connector_pane_image' src='ToMoreSpecificClass.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/clabview_objectlvclass.png']

#### reference

Class reference or class object you want to typecast to a **target class** within the inheritance hierarchy.

[IMAGE alt='datatype_icon' src='/assets/img/clabview_objectlvclass.png']

#### target class

Class you want **reference** to match.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/ilabview_objectlvclass.png']

#### specific class reference

Class reference or class object typecast to the **target class**.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Where This Node Can Run:**

Desktop OS: Windows

FPGA:

Web Server:

Parent topic:

Classes Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=to-signed-16-bit-integer.html language=enus -->
## TOPIC 00407: To Signed 16-bit Integer

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `to-signed-16-bit-integer.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/to-signed-16-bit-integer.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a number to a 16-bit integer in the range -32,768 to 32,767. number An input to this operation. This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA Whe

To Signed 16-bit Integer

Converts a number to a 16-bit integer in the range -32,768 to 32,767.

[IMAGE alt='1378' src='ToSigned16BitInteger.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### number

An input to this operation.

This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/ii16.png']

##### 16-bit integer

Result of the conversion.

This output assumes the same data type structure as 
 number.

#### Examples

| number | 16-bit integer (range: -32,768 to 32,767) | Comments |
| --- | --- | --- |
| 0 | 0 | 0 is within the allowable range, so no value change occurs. |
| 1 | 1 | Same as above. |
| ... | ... | ... |
| 32,766 | 32,766 | Same as above. |
| 32,767 | 32,767 | number is the maximum allowable value, so no value change occurs. |
| 32,768 | -32,768 | number exceeds the maximum allowable value by 1, so the node returns the first allowable value at the bottom of the range. |
| 32,769 | -32,767 | number exceeds the maximum allowable value by 2, so the node returns the second allowable value at the bottom of the range. |
| -32,767 | -32,767 | number is within the allowable range, so no value change occurs. |
| -32,768 | -32,768 | number is the minimum allowable value, so no value change occurs. |
| -32,769 | 32,767 | number undershoots the minimum allowable value by 1, so the node returns the first allowable value at the top of the range. |
| -32,770 | 32,766 | number undershoots the minimum allowable value by 2, so the node returns the second allowable value at the top of the range. |
| 13.7 | 14 | The node rounds 13.7 up to 14 because 14 is the nearest integer. |
| 13.5 | 14 | The node rounds 13.5 up to 14 because 14 is the nearest even integer. |
| 14.5 | 14 | The node rounds 14.5 down to 14 because 14 is the nearest even integer. |

#### Rounding Behavior for Floating-Point Values

This node rounds all floating-point numeric values to the nearest integer. If the fractional part of the floating-point value is 
 .5, the node rounds the value to the nearest even integer. For example, the node rounds 
 13.5 to 
 14 and rounds 
 14.5 to 
 14.

#### Wrapping Behavior for Out-of-Range Values

If this node receives an input value that falls outside of the range of values that the output can represent, the node returns a value that wraps to the other end of the range. This differs from the behavior for nodes that convert values to unsigned integers.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=to-signed-32-bit-integer.html language=enus -->
## TOPIC 00408: To Signed 32-bit Integer

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `to-signed-32-bit-integer.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/to-signed-32-bit-integer.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a number to a 32-bit integer in the range -(2^31) to (2^31)-1. number An input to this operation. This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA W

To Signed 32-bit Integer

Converts a number to a 32-bit integer in the range -(2<sup>31</sup>) to (2<sup>31</sup>)-1.

[IMAGE alt='1378' src='ToSigned32BitInteger.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### number

An input to this operation.

This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### 32-bit integer

Result of the conversion.

This output assumes the same data type structure as 
 number.

#### Examples

| number | 32-bit integer (range: -(231) to (231)-1) | Comments |
| --- | --- | --- |
| 0 | 0 | number is within the allowable range, so no value change occurs. |
| 1 | 1 | Same as above. |
| ... | ... | ... |
| (231)-2 | (231)-2 | Same as above. |
| (231)-1 | (231)-1 | number is the maximum allowable value, so no value change occurs. |
| 231 | -(231) | number exceeds the maximum allowable value by 1, so the node returns the first allowable value at the bottom of the range. |
| (231)+1 | -(231)+1 | number exceeds the maximum allowable value by 2, so the node returns the second allowable value at the bottom of the range. |
| -(231)+1 | -(231)+1 | number is within the allowable range, so no value change occurs. |
| -(231) | -(231) | number is the minimum allowable value, so no value change occurs. |
| -(231)-1 | (231)-1 | number undershoots the minimum allowable value by 1, so the node returns the first allowable value at the top of the range. |
| -(231)-1 | (231)-2 | number undershoots the minimum allowable value by 2, so the node returns the second allowable value at the top of the range. |
| 13.7 | 14 | The node rounds 13.7 up to 14 because 14 is the nearest integer. |
| 13.5 | 14 | The node rounds 13.5 up to 14 because 14 is the nearest even integer. |
| 14.5 | 14 | The node rounds 14.5 down to 14 because 14 is the nearest even integer. |

#### Rounding Behavior for Floating-Point Values

This node rounds all floating-point numeric values to the nearest integer. If the fractional part of the floating-point value is 
 .5, the node rounds the value to the nearest even integer. For example, the node rounds 
 13.5 to 
 14 and rounds 
 14.5 to 
 14.

#### Wrapping Behavior for Out-of-Range Values

If this node receives an input value that falls outside of the range of values that the output can represent, the node returns a value that wraps to the other end of the range. This differs from the behavior for nodes that convert values to unsigned integers.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=to-signed-64-bit-integer.html language=enus -->
## TOPIC 00409: To Signed 64-bit Integer

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `to-signed-64-bit-integer.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/to-signed-64-bit-integer.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a number to a 64-bit integer in the range -(2^63) to (2^63)-1. number An input to this operation. This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA W

To Signed 64-bit Integer

Converts a number to a 64-bit integer in the range -(2<sup>63</sup>) to (2<sup>63</sup>)-1.

[IMAGE alt='1378' src='ToSigned64BitInteger.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### number

An input to this operation.

This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/ii64.png']

##### 64-bit integer

Result of the conversion.

This output assumes the same data type structure as 
 number.

#### Examples

| number | 64-bit integer (range: -(263) to (263)-1 | Comments |
| --- | --- | --- |
| 0 | 0 | number is within the allowable range, so no value change occurs. |
| 1 | 1 | Same as above. |
| ... | ... | ... |
| (263)-2 | (263)-2 | Same as above. |
| (263)-1 | (263)-1 | number is the maximum allowable value, so no value change occurs. |
| 263 | -(263) | number exceeds the maximum allowable value by 1, so the node returns the first allowable value at the bottom of the range. |
| (263)+1 | -(263)+1 | number exceeds the maximum allowable value by 2, so the node returns the second allowable value at the bottom of the range. |
| -(263)+1 | -(263)+1 | number is within the allowable range, so no value change occurs. |
| -(263) | -(263) | number is the minimum allowable value, so no value change occurs. |
| -(263)-1 | (263)-1 | number undershoots the minimum allowable value by 1, so the node returns the first allowable value at the top of the range. |
| -(263)-1 | (263)-2 | number undershoots the minimum allowable value by 2, so the node returns the second allowable value at the top of the range. |
| 13.7 | 14 | The node rounds 13.7 up to 14 because 14 is the nearest integer. |
| 13.5 | 14 | The node rounds 13.5 up to 14 because 14 is the nearest even integer. |
| 14.5 | 14 | The node rounds 14.5 down to 14 because 14 is the nearest even integer. |

#### Rounding Behavior for Floating-Point Values

This node rounds all floating-point numeric values to the nearest integer. If the fractional part of the floating-point value is 
 .5, the node rounds the value to the nearest even integer. For example, the node rounds 
 13.5 to 
 14 and rounds 
 14.5 to 
 14.

#### Wrapping Behavior for Out-of-Range Values

If this node receives an input value that falls outside of the range of values that the output can represent, the node returns a value that wraps to the other end of the range. This differs from the behavior for nodes that convert values to unsigned integers.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=to-signed-8-bit-integer.html language=enus -->
## TOPIC 00410: To Signed 8-bit Integer

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `to-signed-8-bit-integer.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/to-signed-8-bit-integer.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a number to an 8-bit integer in the range -128 to 127. number An input to this operation. This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA When you

To Signed 8-bit Integer

Converts a number to an 8-bit integer in the range -128 to 127.

[IMAGE alt='1378' src='ToSigned8BitInteger.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### number

An input to this operation.

This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/ii8.png']

##### 8-bit integer

Result of the conversion.

This output assumes the same data type structure as 
 number.

#### Examples

| number | 8-bit integer (range: -128 to 127) | Comments |
| --- | --- | --- |
| 0 | 0 | number is within the allowable range, so no value change occurs. |
| 1 | 1 | Same as above. |
| ... | ... | ... |
| 126 | 126 | Same as above. |
| 127 | 127 | number is the maximum allowable value, so no value change occurs. |
| 128 | -128 | number exceeds the maximum allowable value by 1, so the node returns the first allowable value at the bottom of the range. |
| 129 | -127 | number exceeds the maximum allowable value by 2, so the node returns the second allowable value at the bottom of the range. |
| -127 | -127 | number is within the allowable range, so no value change occurs. |
| -128 | -128 | number is the minimum allowable value, so no value change occurs. |
| -129 | 127 | number undershoots the minimum allowable value by 1, so the node returns the first allowable value at the top of the range. |
| -130 | 126 | number undershoots the minimum allowable value by 2, so the node returns the second allowable value at the top of the range. |
| 13.7 | 14 | The node rounds 13.7 up to 14 because 14 is the nearest integer. |
| 13.5 | 14 | The node rounds 13.5 up to 14 because 14 is the nearest even integer. |
| 14.5 | 14 | The node rounds 14.5 down to 14 because 14 is the nearest even integer. |

#### Rounding Behavior for Floating-Point Values

This node rounds all floating-point numeric values to the nearest integer. If the fractional part of the floating-point value is 
 .5, the node rounds the value to the nearest even integer. For example, the node rounds 
 13.5 to 
 14 and rounds 
 14.5 to 
 14.

#### Wrapping Behavior for Out-of-Range Values

If this node receives an input value that falls outside of the range of values that the output can represent, the node returns a value that wraps to the other end of the range. This differs from the behavior for nodes that convert values to unsigned integers.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=to-single-precision-complex.html language=enus -->
## TOPIC 00411: To Single Precision Complex

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `to-single-precision-complex.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/to-single-precision-complex.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a number to a single-precision, complex number. number An input to this operation. This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA When you add thi

To Single Precision Complex

Converts a number to a single-precision, complex number.

[IMAGE alt='1378' src='ToSinglePrecisionComplex.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### number

An input to this operation.

This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/icsg.png']

##### single precision complex

Result of the conversion.

This output assumes the same data type structure as 
 number.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=to-single-precision-float.html language=enus -->
## TOPIC 00412: To Single Precision Float

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `to-single-precision-float.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/to-single-precision-float.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a number to a single-precision, floating-point number. number An input to this operation. This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA When you

To Single Precision Float

Converts a number to a single-precision, floating-point number.

[IMAGE alt='1378' src='ToSinglePrecisionFloat.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### number

An input to this operation.

This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/isgl.png']

##### single precision float

Result of the conversion.

This output assumes the same data type structure as 
 number.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=to-timestamp.html language=enus -->
## TOPIC 00413: To Timestamp

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `to-timestamp.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/to-timestamp.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a timestamp for the date and time represented by a specified number of seconds since 12:00 a.m., January 1, 1904, Universal Time. number Number of seconds elapsed since the epoch time of 12:00 a.m., January 1, 1904, Universal Time [01-01-1904 00:00:00]. This input can also be any data type t

To Timestamp

Creates a timestamp for the date and time represented by a specified number of seconds since 12:00 a.m., January 1, 1904, Universal Time.

[IMAGE alt='1378' src='ToTimestamp.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### number

Number of seconds elapsed since the epoch time of 12:00 a.m., January 1, 1904, Universal Time [01-01-1904 00:00:00].

This input can also be any data type that contains only numerics, such as an array or cluster of numerics.

[IMAGE alt='datatype_icon' src='/assets/img/itimestamp.png']

##### timestamp

Date and time that results from adding number to 12:00 a.m., January 1, 1904, Universal Time [01-01-1904 00:00:00].

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=to-unsigned-16-bit-integer.html language=enus -->
## TOPIC 00414: To Unsigned 16-bit Integer

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `to-unsigned-16-bit-integer.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/to-unsigned-16-bit-integer.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a number to a 16-bit unsigned integer in the range 0 to 65,535. number An input to this operation. This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA

To Unsigned 16-bit Integer

Converts a number to a 16-bit unsigned integer in the range 0 to 65,535.

[IMAGE alt='1378' src='ToUnsigned16BitInteger.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### number

An input to this operation.

This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### unsigned 16-bit integer

Result of the conversion.

This output assumes the same data type structure as 
 number.

#### Examples

| number | unsigned 16-bit integer (range: 0 to 65,535) | Comments |
| --- | --- | --- |
| -100 | 0 | number undershoots the allowable values, so the node rounds the output to the lower end of the range. |
| -1 | 0 | number undershoots the allowable values, so the node rounds the output to the lower end of the range. |
| 0 | 0 | number is within the allowable range, so no value change occurs. |
| 1 | 1 | Same as above. |
| ... | ... | ... |
| 65,534 | 65,534 | Same as above. |
| 65,535 | 65,535 | number is the maximum allowable value, so no value change occurs. |
| 65,536 | 65,535 | number exceeds the maximum allowable value by 1, so the node rounds the output to the upper end of the range. |
| 13.7 | 14 | The node rounds 13.7 up to 14 because 14 is the nearest integer. |
| 13.5 | 14 | The node rounds 13.5 up to 14 because 14 is the nearest even integer. |
| 14.5 | 14 | The node rounds 14.5 down to 14 because 14 is the nearest even integer. |

#### Rounding Behavior for Floating-Point Values

This node rounds all floating-point numeric values to the nearest integer. If the fractional part of the floating-point value is 
 .5, the node rounds the value to the nearest even integer. For example, the node rounds 
 13.5 to 
 14 and rounds 
 14.5 to 
 14.

#### Rounding Behavior for Out-of-Range Values

If this node receives an input that falls outside the range of values that the output can represent, the node rounds the value to the closer end of the range. This differs from the out-of-range behavior for nodes that convert values to signed integers.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=to-unsigned-32-bit-integer.html language=enus -->
## TOPIC 00415: To Unsigned 32-bit Integer

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `to-unsigned-32-bit-integer.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/to-unsigned-32-bit-integer.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a number to a 32-bit unsigned integer in the range 0 to (2^32)-1. number An input to this operation. This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPG

To Unsigned 32-bit Integer

Converts a number to a 32-bit unsigned integer in the range 0 to (2^32)-1.

[IMAGE alt='1378' src='ToUnsigned32BitInteger.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### number

An input to this operation.

This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### unsigned 32-bit integer

Result of the conversion.

This output assumes the same data type structure as 
 number.

#### Examples

| number | unsigned 32-bit integer (range: 0 to 2^32-1) | Comments |
| --- | --- | --- |
| -100 | 0 | number undershoots the allowable values, so the node rounds the output to the lower end of the range. |
| -1 | 0 | number undershoots the allowable values, so the node rounds the output to the lower end of the range. |
| 0 | 0 | number is within the allowable range, so no value change occurs. |
| 1 | 1 | Same as above. |
| ... | ... | ... |
| 2^32-2 | 2^32-2 | Same as above. |
| 2^32-1 | 2^32-1 | number is the maximum allowable value, so no value change occurs. |
| 2^32 | 2^32-1 | number exceeds the maximum allowable value by 1, so the node rounds the output to the upper end of the range. |
| 13.7 | 14 | The node rounds 13.7 up to 14 because 14 is the nearest integer. |
| 13.5 | 14 | The node rounds 13.5 up to 14 because 14 is the nearest even integer. |
| 14.5 | 14 | The node rounds 14.5 down to 14 because 14 is the nearest even integer. |

#### Rounding Behavior for Floating-Point Values

This node rounds all floating-point numeric values to the nearest integer. If the fractional part of the floating-point value is 
 .5, the node rounds the value to the nearest even integer. For example, the node rounds 
 13.5 to 
 14 and rounds 
 14.5 to 
 14.

#### Rounding Behavior for Out-of-Range Values

If this node receives an input that falls outside the range of values that the output can represent, the node rounds the value to the closer end of the range. This differs from the out-of-range behavior for nodes that convert values to signed integers.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=to-unsigned-64-bit-integer.html language=enus -->
## TOPIC 00416: To Unsigned 64-bit Integer

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `to-unsigned-64-bit-integer.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/to-unsigned-64-bit-integer.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a number to a 64-bit unsigned integer in the range 0 to (2^64)-1. number An input to this operation. This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPG

To Unsigned 64-bit Integer

Converts a number to a 64-bit unsigned integer in the range 0 to (2^64)-1.

[IMAGE alt='1378' src='ToUnsigned64BitInteger.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### number

An input to this operation.

This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

##### unsigned 64-bit integer

Result of the conversion.

This output assumes the same data type structure as 
 number.

#### Examples

| number | unsigned 64-bit integer (range: 0 to 2^64-1) | Comments |
| --- | --- | --- |
| -100 | 0 | number undershoots the allowable values, so the node rounds the output to the lower end of the range. |
| -1 | 0 | number undershoots the allowable values, so the node rounds the output to the lower end of the range. |
| 0 | 0 | number is within the allowable range, so no value change occurs. |
| 1 | 1 | Same as above. |
| ... | ... | ... |
| 2^64-2 | 2^64-2 | Same as above. |
| 2^64-1 | 2^64-1 | number is the maximum allowable value, so no value change occurs. |
| 2^64 | 2^64-1 | number exceeds the maximum allowable value by 1, so the node rounds the output to the upper end of the range. |
| 13.7 | 14 | The node rounds 13.7 up to 14 because 14 is the nearest integer. |
| 13.5 | 14 | The node rounds 13.5 up to 14 because 14 is the nearest even integer. |
| 14.5 | 14 | The node rounds 14.5 down to 14 because 14 is the nearest even integer. |

#### Rounding Behavior for Floating-Point Values

This node rounds all floating-point numeric values to the nearest integer. If the fractional part of the floating-point value is 
 .5, the node rounds the value to the nearest even integer. For example, the node rounds 
 13.5 to 
 14 and rounds 
 14.5 to 
 14.

#### Rounding Behavior for Out-of-Range Values

If this node receives an input that falls outside the range of values that the output can represent, the node rounds the value to the closer end of the range. This differs from the out-of-range behavior for nodes that convert values to signed integers.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=to-unsigned-8-bit-integer.html language=enus -->
## TOPIC 00417: To Unsigned 8-bit Integer

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `to-unsigned-8-bit-integer.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/to-unsigned-8-bit-integer.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a number to an 8-bit unsigned integer in the range 0 to 255. number An input to this operation. This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers. Data Type Changes on FPGA Whe

To Unsigned 8-bit Integer

Converts a number to an 8-bit unsigned integer in the range 0 to 255.

[IMAGE alt='1378' src='ToUnsigned8BitInteger.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### number

An input to this operation.

This input supports waveforms and any data type that contains only numbers, such as scalar numbers, arrays or clusters of numbers, and arrays of clusters of numbers.

##### Data Type Changes on FPGA

When you add this node to a document targeted to an FPGA, this input has a default data type that uses fewer hardware resources at compile time.

[IMAGE alt='datatype_icon' src='/assets/img/iu8.png']

##### unsigned 8-bit integer

Result of the conversion.

This output assumes the same data type structure as 
 number.

#### Examples

| number | unsigned 8-bit integer (range: 0 to 255) | Comments |
| --- | --- | --- |
| -100 | 0 | number undershoots the allowable values, so the node rounds the output to the lower end of the range. |
| -1 | 0 | number undershoots the allowable values, so the node rounds the output to the lower end of the range. |
| 0 | 0 | number is within the allowable range, so no value change occurs. |
| 1 | 1 | Same as above. |
| ... | ... | ... |
| 254 | 254 | Same as above. |
| 255 | 255 | number is the maximum allowable value, so no value change occurs. |
| 256 | 255 | number exceeds the maximum allowable value by 1, so the node rounds the output to the upper end of the range. |
| 13.7 | 14 | The node rounds 13.7 up to 14 because 14 is the nearest integer. |
| 13.5 | 14 | The node rounds 13.5 up to 14 because 14 is the nearest even integer. |
| 14.5 | 14 | The node rounds 14.5 down to 14 because 14 is the nearest even integer. |

#### Rounding Behavior for Floating-Point Values

This node rounds all floating-point numeric values to the nearest integer. If the fractional part of the floating-point value is 
 .5, the node rounds the value to the nearest even integer. For example, the node rounds 
 13.5 to 
 14 and rounds 
 14.5 to 
 14.

#### Rounding Behavior for Out-of-Range Values

If this node receives an input that falls outside the range of values that the output can represent, the node rounds the value to the closer end of the range. This differs from the out-of-range behavior for nodes that convert values to signed integers.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=to-upper-case.html language=enus -->
## TOPIC 00418: To Uppercase

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `to-upper-case.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/to-upper-case.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts all alphabetic characters in a string to uppercase characters. This node does not modify non-alphabetic characters. string The string you want to modify. This input can also be any data type that contains only strings, such as an array or cluster of strings. all uppercase string The convert

To Uppercase

Converts all alphabetic characters in a string to uppercase characters.
 This node does not modify non-alphabetic characters.

[IMAGE alt='1378' src='ToUpperCase.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### string

The string you want to modify.

This input can also be any data type that contains only strings, such as an array or cluster of strings.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### all uppercase string

The converted version of the string in which all lowercase characters are now uppercase.

string

Parent topic:

String Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=to-variant.html language=enus -->
## TOPIC 00419: To Variant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `to-variant.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/to-variant.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts any data to variant data. anything The data you want to convert. You can wire any data type to this input. This input accepts arrays and clusters of Booleans, floating-point numbers, and strings. This input can also accept an array of clusters, or a cluster of arrays, of those data types. H

To Variant

Converts any data to variant data.

[IMAGE alt='1378' src='ToVariant.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cvoid.png']

##### anything

The data you want to convert. You can wire any data type to this input.

This input accepts arrays and clusters of Booleans, floating-point numbers, and strings. This input can also accept an array of clusters, or a cluster of arrays, of those data types. However, anything does not support refnums.

[IMAGE alt='datatype_icon' src='/assets/img/ifxdt.png']

##### variant

The converted variant data.

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=transpose-2d-array.html language=enus -->
## TOPIC 00420: Transpose 2D Array

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `transpose-2d-array.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/transpose-2d-array.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Rearranges the elements of a 2D array such that the array [i,j] becomes a transposed array [j,i]. 2D array A 2D array of any type. transposed array The transposed 2D array.

Transpose 2D Array

Rearranges the elements of a 2D array such that the array [i,j] becomes a transposed array [j,i].

[IMAGE alt='1378' src='Transpose2DArray.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### 2D array

A 2D array of any type.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### transposed array

The transposed 2D array.

Parent topic:

Array Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=transpose-matrix.html language=enus -->
## TOPIC 00421: Transpose Matrix (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `transpose-matrix.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/transpose-matrix.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `lvFunction`
- source_description: Returns the conjugate transpose of matrix. Output Behavior The conjugate transpose of matrix rearranges the elements so that the element at index (i, j) in matrix becomes the conjugate of the element at (j, i) in transposed matrix. matrix 2D array of any numeric type. transposed matrix Output matrix

Transpose Matrix

Returns the conjugate transpose of **matrix**.

[IMAGE alt='connector_pane_image' src='TransposeMatrix.png']

- Inputs/Outputs
- Details
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

#### matrix

2D array of any numeric type.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

#### transposed matrix

Output matrix with transposed elements.

#### Output Behavior

The conjugate transpose of **matrix** rearranges the elements so that the element at index (i, 
 j) in **matrix** becomes the conjugate of the element at (j, 
 i) in **transposed matrix**.

Parent topic:

Matrix Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=tree-nodes.html language=enus -->
## TOPIC 00422: Tree Nodes

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `tree-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/tree-nodes.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Modify trees.

Tree Nodes

Modify trees.

Panel Manipulation Nodes

Configure and manipulate controls and panels.

Open Item

Expands an item in a tree control to display the child items.

Close Item

Closes an item in a tree control to hide the child items.

Parent topic:

Panel Manipulation Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=trigonometric-nodes.html language=enus -->
## TOPIC 00423: Trigonometric Nodes

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `trigonometric-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/trigonometric-nodes.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`

Trigonometric Nodes

Cosecant

x

Cosine

x

Cotangent

x

Inverse Cosecant

x

Inverse Cosine

x

Inverse Cotangent

x

Inverse Secant

x

Inverse Sine

x

Inverse Tangent

x

Inverse Tangent (2 Input)

y

x

Secant

x

Sinc

x

x

Sine

x

Sine and Cosine

x

Tangent

x

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=trim-whitespace.html language=enus -->
## TOPIC 00424: Trim Whitespace

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `trim-whitespace.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/trim-whitespace.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes all ASCII whitespace, such as spaces, tabs, carriage returns, and linefeeds, from the beginning, end, or both ends of the input string. This node does not remove double-byte characters. location Value that determines whether to remove whitespace from the beginning, end, or both ends of the i

Trim Whitespace

Removes all ASCII whitespace, such as spaces, tabs, carriage returns, and linefeeds, from the beginning, end, or both ends of the input string.

Note

[IMAGE alt='1378' src='Trim_Whitespace.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### location

Value that determines whether to remove whitespace from the beginning, end, or both ends of the input string.

| both | 0 | Removes whitespace from both ends of the input string. |
| --- | --- | --- |
| start of string | 1 | Removes whitespace from the start of the input string. |
| end of string | 2 | Removes whitespace from the end of the input string. |

Default value: both

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### string

String on which the node operates.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### trimmed string

Input string with whitespace removed.

Parent topic:

String Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=two-button-dialog.html language=enus -->
## TOPIC 00425: Two Button Dialog

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `two-button-dialog.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/two-button-dialog.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Displays a dialog box that contains a custom message and two buttons. message The text to display in the dialog box. true button name The text displayed on the left button in the dialog box. Default value: OK false button name The text displayed on the right button in the dialog box. Default value:

Two Button Dialog

Displays a dialog box that contains a custom message and two buttons.

[IMAGE alt='1378' src='TwoButtonDialog.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### message

The text to display in the dialog box.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### true button name

The text displayed on the left button in the dialog box.

Default value: OK

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### false button name

The text displayed on the right button in the dialog box.

Default value: Cancel

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### true button?

A Boolean value that indicates whether the user clicked the dialog box button designated by true button name.

| True | The user clicked the dialog box button designated by true button name. |
| --- | --- |
| False | The user clicked the dialog box button designated by false button name. |

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=ui-string-nodes.html language=enus -->
## TOPIC 00426: String Nodes

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `ui-string-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/ui-string-nodes.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Modify behavior of string controls.

String
 Nodes

Modify behavior of string controls.

Panel Manipulation Nodes

Configure and manipulate controls and panels.

Scroll To End

Sets the vertical scroll position to the end of the string you specify.

Parent topic:

Panel Manipulation Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=unflatten-from-json.html language=enus -->
## TOPIC 00427: Unflatten from JSON

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `unflatten-from-json.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/unflatten-from-json.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a UTF-8 JavaScript Object Notation (JSON) string to another data type. enable LabVIEW extensions A Boolean that determines whether JSON extensions support NaN and Inf values of floating-point numbers. Not all JSON parsers support these extensions. True Enable JSON extension support of NaN a

Unflatten from JSON

Converts a UTF-8 JavaScript Object Notation (JSON) string to another data type.

[IMAGE alt='1378' src='UnflattenFromJson.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### enable LabVIEW extensions

A Boolean that determines whether JSON extensions support 
NaN and 
Inf values of floating-point numbers. Not all JSON parsers support these extensions.

| True | Enable JSON extension support of NaN and Inf values of floating-point numbers. |
| --- | --- |
| False | Disable JSON extension support of NaN and Inf values of floating-point numbers. |

Default value: True

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### path

A specific item in the JSON string. Use path if your JSON string contains multiple items and you would like to extract a specific item from it. path uses an array of strings to identify the item, where each element in the array references either the name of a cluster element or an integer index of an array. If you specify an item using path, you must wire a data type to type and defaults that corresponds to the data type of the specified item.

##### Type/Default Inputs and Corresponding Outputs

Consider the JSON string 
 {"0":"abc","1":false,"2":[9,8,7]}. The following table illustrates an example of type/defaults inputs required for various paths and the resulting value outputs.

| Path | Type and Defaults | Value | Comments |
| --- | --- | --- | --- |
|  |  |  | If path is empty, type and defaults must account for each element in the JSON string. You must wire a cluster containing a string, a Boolean, and an array to type and defaults. |
|  |  |  | In this example, the path points to the cluster element named 0, or string abc. You must wire a string to type and defaults. |
|  |  |  | In this example, the path points to the cluster element named 2, which is an array, and the element at index 0 of that array. This element is a floating-point number, so you must wire a DBL numeric to type and defaults. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### JSON string

The flattened UTF-8 string that you want to unflatten.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### type and defaults

The data type and default values to which you want to unflatten the JSON string. This input accepts Booleans, integers, floating-point numbers, strings, and arrays or clusters of these types. Cluster elements may be labeled or unlabeled, but not a combination of both. If elements in a cluster are labeled, then each name must be unique to that cluster.

JSON string

type and defaults

{"firstelement":"a","secondelement":"b"}

firstelement

secondelement

path

JSON string

type and defaults

path

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### default null elements?

A Boolean that determines how null values in JSON string are processed.

| True | Uses default values from the input cluster for null values in JSON string. |
| --- | --- |
| False | Returns an error for null values. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### strict validation?

A Boolean that determines whether to return an error when JSON string contains items not defined in type and defaults.

| True | Returns an error when JSON string contains items not defined in type and defaults. |
| --- | --- |
| False | The JSON object may contain items not defined in type and defaults. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### value

Unflattened data of the same data type and structure as type and defaults.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Converting Data Types not Supported by Type and Defaults

Unflatten From JSON

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=unregister-for-events.html language=enus -->
## TOPIC 00428: Unregister For Events

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `unregister-for-events.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/unregister-for-events.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Unregisters all events associated with an event registration refnum. Event Structures that use this event registration refnum no longer receive any dynamic events after this node executes. National Instruments recommends that you unregister for events when you no longer need to handle them. If you d

Unregister For Events

Unregisters all events associated with an event registration refnum.

Event Structures that use this event registration refnum no longer receive any dynamic events after this node executes.

National Instruments recommends that you unregister for events when you no longer need to handle them. If you do not unregister for events, the VI continues to generate and queue the events as long as the VI runs, even if no Event Structure is waiting to handle them. Allowing the VI to queue events without an Event Structure to handle them consumes memory and can hang the VI if you enable 
 Pause Panel Event Processing Until Complete for the events.

[IMAGE alt='1378' src='UnregisterForEvents.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### event registration refnum

Reference to an existing event registration that a Register For Events node created.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: no error

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

- Executing
 Code Based on a User Event

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=unset-busy.html language=enus -->
## TOPIC 00429: Unset Busy

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `unset-busy.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/unset-busy.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Changes the cursor from the busy cursor to the default cursor and enables mouse clicks on both the panel and the menu. In a WebVI, this node removes the loading spinner on the panel, instead of updating the cursor. panel reference in Reference to the panel. If you leave this input unwired, the node

Unset Busy

Changes the cursor from the busy cursor to the default cursor and enables mouse
 clicks on both the panel and the menu.

In a WebVI, this node removes the loading spinner on the panel, instead of updating the
 cursor.

[IMAGE alt='1378' src='UnsetBusy.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### panel reference in

Reference to the panel.

If you leave this input unwired, the node changes the cursor on the panel of the current
 VI.

Note

panel reference
 in

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### panel reference out

Reference to the panel.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Busy State Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=upgrade-to-error.html language=enus -->
## TOPIC 00430: Upgrade To Error

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `upgrade-to-error.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/upgrade-to-error.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Changes a warning to an error. error in An error cluster that you use to check for errors or warnings. Standard Error Behavior error out An error cluster including any values this node writes, removes, or replaces. If no values change, this node returns error in unchanged. Standard Error Behavior

Upgrade To Error

Changes a warning to an error.

[IMAGE alt='1378' src='Upgrade_To_Error.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

An error cluster that you use to check for errors or warnings.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

An error cluster including any values this node writes, removes, or replaces. If no values change, this node returns 
error in unchanged.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Error Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=variant-constant.html language=enus -->
## TOPIC 00431: Variant Constant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `variant-constant.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/variant-constant.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an empty variant on the diagram. You cannot set a value for a variant constant.

Variant Constant

Represents an empty variant on the diagram.

You cannot set a value for a variant constant.

[IMAGE alt='1378' src='Literal.Variant.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=variant-nodes.html language=enus -->
## TOPIC 00432: Variant Nodes

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `variant-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/variant-nodes.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`

Variant Nodes

Delete Variant Attribute

Deletes either a single variant attribute or all variant attributes.

Get Variant Attribute

Returns either the value of a single variant attribute or the names and values of all variant attributes.

Set Variant Attribute

Creates or replaces a variant attribute.

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=variant-to-data.html language=enus -->
## TOPIC 00433: Variant To Data

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `variant-to-data.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/variant-to-data.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts variant data to the data type that you specify so that you can display or process the data. type The data type of the data stored in variant. You can wire any data type to this input. If the data type wired to type does not match the data stored in variant, the node returns an error. If the

Variant To Data

Converts variant data to the data type that you specify so that you can display or process the data.

[IMAGE alt='1378' src='VariantToData.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cvoid.png']

##### type

The data type of the data stored in variant. You can wire any data type to this input.

type

variant

[IMAGE alt='datatype_icon' src='/assets/img/cfxdt.png']

##### variant

The variant data you want to convert to the data type that you specify in type.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ivoid.png']

##### data

The variant data changed to the data type specified by type. If variant could not be converted to the data type specified, this returns the default value for the data type.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Conversion Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=vi-ref-generic-constant.html language=enus -->
## TOPIC 00434: VI Reference Constant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `vi-ref-generic-constant.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/vi-ref-generic-constant.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `lvConstant`
- source_description: Represents a VI reference on the diagram. Use this reference constant to specify a type for the type specifier VI reference input of Open VI Reference. Only its type matters to Open VI Reference. Configuring a VI Reference Constant To configure a VI Reference Constant navigate to the Item tab, click

VI Reference Constant

Represents a VI reference on the diagram.

###### Programming Patterns

Use this reference constant to specify a type for the **type specifier VI reference** input of Open VI Reference. Only its type matters to Open VI Reference.

[IMAGE alt='connector_pane_image' src='Literal.VIReferenceLiteral.png']

- Details
- Compatibility

#### Configuring a VI Reference Constant

VI Reference Constant

Item

After configuring a VI Reference Constant, its output VI reference type is a strictly typed VI reference. You can reconfigure VI Reference Constant with another VI if necessary.

Parent topic:

Execution Control

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=vi-reference-properties.html language=enus -->
## TOPIC 00435: VI Reference Properties

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `vi-reference-properties.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/vi-reference-properties.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `lvFunction`
- source_description: Reads properties of a VI reference. VI reference in Reference to a VI. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. No error Standard Error Behavior Many nodes provide an error in input and an error out output so th

VI Reference Properties

Reads properties of a VI reference.

[IMAGE alt='connector_pane_image' src='PropertyNode.VIReference.png']

- Inputs/Outputs
- Compatibility

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

#### VI reference in

Reference to a VI.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

#### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

**Default:**No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

#### VI reference out

Reference to a VI.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

#### error out

Error information.

The node produces this output according to standard error behavior.

Standard Error Behavior

Many nodes provide an **error in** input and an **error out** output so that the node can respond to and communicate errors that occur while code is running. The value of **error in** specifies whether an error occurred before the node runs. Most nodes respond to values of **error in** in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/ienum.png']

#### Execution State

Enum representing the execution state of the VI.

| Name | Description |
| --- | --- |
| Bad | VI has errors and cannot execute. |
| Idle | VI is not running but it is in memory. |
| Run top level | VI is the top-level VI in an active hierarchy. |
| Running | VI is reserved for execution by one or more active top-level VIs. |

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

#### Panel

Reference to the panel of the VI, which you can use with the Panel Manipulation palette API or other LabVIEW APIs for working with VI panels.

Parent topic:

Execution Control

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=vi-reference-terminal.html language=enus -->
## TOPIC 00436: VI Reference

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `vi-reference-terminal.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/vi-reference-terminal.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `lvFunction`
- source_description: Passes a VI reference you opened as a parameter to another VI. Creates a VI reference you can use to control the behavior and properties of the VI. Using a VI Reference Terminal Use VI Reference terminals to pass a VI reference you opened as a parameter to another VI. Open VI Reference requires a st

VI Reference

Passes a VI reference you opened as a parameter to another VI. Creates a VI reference you can use to control the behavior and properties of the VI.

[IMAGE alt='connector_pane_image' src='DataAccessor.png']

- Details
- Compatibility

#### Using a VI Reference Terminal

Use VI Reference terminals to pass a VI reference you opened as a parameter to another VI. Open VI Reference requires a strictly typed VI reference terminal or constant as a type specifier input when you want a strictly typed reference to a VI. In this case, the value of the reference terminal is unimportant. The function uses only the type.

To configure a VI Reference terminal navigate to the 
 Item tab, click the button next to the Select VI Signature field, and find the VI you want to reference in the Select VI dialog box.

Parent topic:

Execution Control

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=wait-ms.html language=enus -->
## TOPIC 00437: Milliseconds

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `wait-ms.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/wait-ms.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits the specified number of milliseconds and returns the value of the millisecond timer. milliseconds to wait Number of milliseconds to wait. Wiring a value of 0 to this input forces the execution system to check for other available code to execute. Maximum Input before Timer Wrap-Around If the wa

Milliseconds

Waits the specified number of milliseconds and returns the value of the millisecond timer.

[IMAGE alt='1378' src='Wait.Milliseconds.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### milliseconds to wait

Number of milliseconds to wait.

Wiring a value of 0 to this input forces the execution system to check for other available code to execute.

##### Maximum Input before Timer Wrap-Around

If the wait time you specify is greater than the maximum allowed for the 
 Counter size of the Wait node, the expected program wait time wraps around and starts again from zero. You can configure the 
 Counter size of the node in the 
 Item tab.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### millisecond timer value

Value of the operating system's millisecond timer after the wait.

#### Programming Patterns

- Adjusting the Execution Speed of a Loop

#### Timer Accuracy

The accuracy of the timer varies across operating systems.
 If the operating system takes more time to process a request than the time that the input specifies, the actual wait time is longer than the time that the input specifies.

#### When to Use Wait Until Next Multiple instead of Wait

If you need to ensure that an operation waits at least the specified time before completing execution, you can use either a Wait node or a Wait Until Next Multiple node. However, for functions that feedback an output as an input and require consistent timing between iterations to achieve equilibrium, such as a PID node in a loop, use a Wait Until Next Multiple node. Compared to Wait nodes, Wait Until Next Multiple nodes have more periodic spacing between iterations, because even if one iteration finishes late, the following iteration still executes on the multiple of the Wait Until Next Multiple input.

#### Thread Availability During Wait Time

When an active execution system thread in a program reaches a Wait node in the millisecond configuration, the node execution is rescheduled cooperatively and the temporarily available thread is used by any other currently executing code until the wait time expires.

When you use the microsecond or tick configuration of this node, the thread which encounters the Wait node is blocked until the wait time expires.

Parent topic:

Wait

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=wait-on-asynchronous-call.html language=enus -->
## TOPIC 00438: Wait on Asynchronous Call

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `wait-on-asynchronous-call.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/wait-on-asynchronous-call.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Causes the diagram to wait for an asynchronous call to a target VI to finish executing and then returns the outputs of the target VI. To use the this node on a reference, navigate to the Item tab for Open VI Reference and select Prepare for asynchronous call with wait. You also must call the target

Wait on Asynchronous Call

Causes the diagram to wait for an asynchronous call to a target VI to finish executing and then returns the outputs of the target VI.

To use the this node on a reference, navigate to the 
 **Item** tab for Open VI Reference and select 
 Prepare for asynchronous call with wait. You also must call the target VI with Start Asynchronous Call.

[IMAGE alt='1378' src='WaitOnAsynchronousCall.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### reference in

A reference to a target node that you want to call asynchronously.

- Be strictly typed.
- Be configured for asynchronous execution with Open VI Reference . In the 
 Item tab for Open VI Reference , select 
 Prepare for asynchronous call without wait or 
 Prepare for asynchronous call with wait .
- Be called by a Start Asynchronous Call node elsewhere in the calling VI.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

Default value: No error

The node responds to this input according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### reference out

Unchanged reference associated with the strictly typed VI reference.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

##### Standard Error Behavior

Many nodes provide an error in input and an error out output so that the node can respond to and communicate errors that occur while code is running. The value of error in specifies whether an error occurred before the node runs. Most nodes respond to values of error in in a standard, predictable way.

| error in does not contain an error | error in contains an error |
| --- | --- |
|  |  |
| If no error occurred before the node runs, the node begins execution normally. If no error occurs while the node runs, it returns no error. If an error does occur while the node runs, it returns that error information as error out. | If an error occurred before the node runs, the node does not execute. Instead, it returns the error in value as error out. |

#### Accessing Inputs and Outputs

The interface of this node includes the following features:

- No access to inputs of the target VI— Wait on Asynchronous Call does not provide access to the inputs of the target VI. You can pass inputs to the target VI when you call it with Start Asynchronous Call .
- Access to outputs of the target VI—When you wire a strictly typed VI reference to the reference in input of Wait on Asynchronous Call , the node displays the output portion of the connector pane of the referenced VI. Use the output terminals of the connector pane to access the data returned by the target VI.

#### Wait Behaviors

This node exhibits the following wait behaviors:

- Ability to wait for only a specified amount of time—To specify how long this node waits for the associated asynchronous call to complete, select 
 Timeout from the 
 Item tab to specify how long the node waits on the corresponding VI call before returning a timeout error.
- Ability to wait on multiple calls to the same VI reference—If you pass the same VI reference to multiple Start Asynchronous Call nodes, you cannot predict which Wait on Asynchronous Call node will detect the completion of each call. You can take precautions to match a Wait on Asynchronous Call node to a specific VI call if necessary.

#### Conserving Memory by Releasing References

You can call this node before the corresponding Start Asynchronous Call node.

Every Start Asynchronous Call node that uses a reference configured as 
 Asynchronous with wait must have a corresponding Wait on Asynchronous Call. If you start an asynchronous call to a call-and-collect reference, the application cannot free the reference until a Wait on Asynchronous Call node collects the outputs of the VI call to that reference.

Parent topic:

Execution Control

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=wait-ticks.html language=enus -->
## TOPIC 00439: Ticks

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `wait-ticks.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/wait-ticks.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Causes the diagram or subdiagram to wait a specified number of ticks before completing execution. A single tick represents one nanosecond. ticks to wait Number of ticks to wait. Wiring a value of 0 to this input forces the execution system to check for other available code to execute. Maximum Input

Ticks

Causes the diagram or subdiagram to wait a specified number of ticks before completing execution.
 
 A single tick represents one nanosecond.

[IMAGE alt='1378' src='Wait.Ticks.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### ticks to wait

Number of ticks to wait.

Wiring a value of 0 to this input forces the execution system to check for other available code to execute.

##### Maximum Input before Timer Wrap-Around

If the wait time you specify is greater than the maximum allowed for the 
 Counter size of the Wait node, the expected program wait time wraps around and starts again from zero. You can configure the 
 Counter size of the node in the 
 Item tab.

##### Highest Timer Resolution

The highest timer resolution for this node is one millisecond. Microsecond or tick values are rounded to the nearest millisecond value.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### tick timer value

Value of the operating system's tick timer after the wait.

#### Programming Patterns

- Adjusting the Execution Speed of a Loop

#### Timer Accuracy

The accuracy of the timer varies across operating systems.
 If the operating system takes more time to process a request than the time that the input specifies, the actual wait time is longer than the time that the input specifies.

#### When to Use Wait Until Next Multiple instead of Wait

If you need to ensure that an operation waits at least the specified time before completing execution, you can use either a Wait node or a Wait Until Next Multiple node. However, for functions that feedback an output as an input and require consistent timing between iterations to achieve equilibrium, such as a PID node in a loop, use a Wait Until Next Multiple node. Compared to Wait nodes, Wait Until Next Multiple nodes have more periodic spacing between iterations, because even if one iteration finishes late, the following iteration still executes on the multiple of the Wait Until Next Multiple input.

#### Thread Availability During Wait Time

When an active execution system thread in a program reaches a Wait node in the millisecond configuration, the node execution is rescheduled cooperatively and the temporarily available thread is used by any other currently executing code until the wait time expires.

When you use the microsecond or tick configuration of this node, the thread which encounters the Wait node is blocked until the wait time expires.

Parent topic:

Wait

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=wait-until-next-multiple-ms.html language=enus -->
## TOPIC 00440: Milliseconds

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `wait-until-next-multiple-ms.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/wait-until-next-multiple-ms.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Causes the diagram or subdiagram to wait until the value of the operating system's millisecond timer becomes a multiple of the specified millisecond multiple before completing execution. Use this node inside a loop to control the execution rate of the loop. You can also use this node to synchronize

Milliseconds

Causes the diagram or subdiagram to wait until the value of the operating system's millisecond timer becomes a multiple of the specified millisecond multiple before completing execution.
 
 Use this node inside a loop to control the execution rate of the loop. You can also use this node to synchronize activities between two different sections of code (such as between two loops).

[IMAGE alt='1378' src='WaitUntilNextMultiple.Milliseconds.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### millisecond multiple

The number that millisecond timer value must be a multiple of.

0

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### millisecond timer value

Value of the operating system's millisecond timer after the wait.

#### Programming Patterns

- Synchronizing the Execution of Multiple Loops

#### Behavior of Wait Until Next Multiple for the First Iteration of a Loop

When using Wait Until Next Multiple inside a loop, the first loop iteration may be shorter than subsequent iterations. This is because the amount of time the first loop iteration waits depends on the value of the system clock when the loop begins executing. For example, consider a loop that contains a Wait Until Next Multiple (Milliseconds) node with 10 ms wired to millisecond multiple. This loop begins to execute when the value of the system clock is 112 ms. The first loop iteration lasts until the value of the system clock is 120 ms (a multiple of 10), which means that the iteration only lasts 8 ms. The loop then begins the second iteration, and each subsequent loop iteration begins every 10 ms.

#### Effect of the millisecond multiple input on Loop Execution Time

When specifying a value for the input of Wait Until Next Multiple, ensure that the value is greater than the time required to execute the code inside the loop. If a loop contains code that takes longer to execute than the time specified, Wait Until Next Multiple has no effect on the execution speed of the loop.

Parent topic:

Wait Until Next Multiple

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=wait-until-next-multiple-ticks.html language=enus -->
## TOPIC 00441: Ticks

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `wait-until-next-multiple-ticks.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/wait-until-next-multiple-ticks.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Causes the diagram or subdiagram to wait until the value of the operating system's tick timer becomes a multiple of the specified tick multiple before completing execution. A single tick represents one nanosecond. Use this node inside a loop to control the execution rate of the loop. You can also us

Ticks

Causes the diagram or subdiagram to wait until the value of the operating system's tick timer becomes a multiple of the specified tick multiple before completing execution.
 
 A single tick represents one nanosecond.
 Use this node inside a loop to control the execution rate of the loop. You can also use this node to synchronize activities between two different sections of code (such as between two loops).

[IMAGE alt='1378' src='WaitUntilNextMultiple.Ticks.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### tick multiple

The number that tick timer value must be a multiple of.

0

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### tick timer value

Value of the operating system's tick timer after the wait.

#### Programming Patterns

- Synchronizing the Execution of Multiple Loops

#### Behavior of Wait Until Next Multiple for the First Iteration of a Loop

When using Wait Until Next Multiple inside a loop, the first loop iteration may be shorter than subsequent iterations. This is because the amount of time the first loop iteration waits depends on the value of the system clock when the loop begins executing. For example, consider a loop that contains a Wait Until Next Multiple (Milliseconds) node with 10 ms wired to millisecond multiple. This loop begins to execute when the value of the system clock is 112 ms. The first loop iteration lasts until the value of the system clock is 120 ms (a multiple of 10), which means that the iteration only lasts 8 ms. The loop then begins the second iteration, and each subsequent loop iteration begins every 10 ms.

#### Effect of the tick multiple input on Loop Execution Time

When specifying a value for the input of Wait Until Next Multiple, ensure that the value is greater than the time required to execute the code inside the loop. If a loop contains code that takes longer to execute than the time specified, Wait Until Next Multiple has no effect on the execution speed of the loop.

Parent topic:

Wait Until Next Multiple

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=wait-until-next-multiple-us.html language=enus -->
## TOPIC 00442: Microseconds

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `wait-until-next-multiple-us.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/wait-until-next-multiple-us.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Causes the diagram or subdiagram to wait until the value of the operating system's microsecond timer becomes a multiple of the specified microsecond multiple before completing execution. Use this node inside a loop to control the execution rate of the loop. You can also use this node to synchronize

Microseconds

Causes the diagram or subdiagram to wait until the value of the operating system's microsecond timer becomes a multiple of the specified microsecond multiple before completing execution.
 
 Use this node inside a loop to control the execution rate of the loop. You can also use this node to synchronize activities between two different sections of code (such as between two loops).

[IMAGE alt='1378' src='WaitUntilNextMultiple.Microseconds.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### microsecond multiple

The number that microsecond timer value must be a multiple of.

0

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### microsecond timer value

Value of the operating system's microsecond timer after the wait.

#### Programming Patterns

- Synchronizing the Execution of Multiple Loops

#### Behavior of Wait Until Next Multiple for the First Iteration of a Loop

When using Wait Until Next Multiple inside a loop, the first loop iteration may be shorter than subsequent iterations. This is because the amount of time the first loop iteration waits depends on the value of the system clock when the loop begins executing. For example, consider a loop that contains a Wait Until Next Multiple (Milliseconds) node with 10 ms wired to millisecond multiple. This loop begins to execute when the value of the system clock is 112 ms. The first loop iteration lasts until the value of the system clock is 120 ms (a multiple of 10), which means that the iteration only lasts 8 ms. The loop then begins the second iteration, and each subsequent loop iteration begins every 10 ms.

#### Effect of the microsecond multiple input on Loop Execution Time

When specifying a value for the input of Wait Until Next Multiple, ensure that the value is greater than the time required to execute the code inside the loop. If a loop contains code that takes longer to execute than the time specified, Wait Until Next Multiple has no effect on the execution speed of the loop.

Parent topic:

Wait Until Next Multiple

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=wait-until-next-multiple.html language=enus -->
## TOPIC 00443: Wait Until Next Multiple

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `wait-until-next-multiple.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/wait-until-next-multiple.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits until the value of the operating system's timer becomes a multiple of a specified amount of time. Use this node to synchronize activities.

Wait Until Next Multiple

Waits until the value of the operating system's timer becomes a multiple of a specified amount of time. 
 Use this node to synchronize activities.

Program Flow Nodes

Microseconds

Causes the diagram or subdiagram to wait until the value of the operating system's microsecond timer becomes a multiple of the specified microsecond multiple before completing execution.

Milliseconds

Causes the diagram or subdiagram to wait until the value of the operating system's millisecond timer becomes a multiple of the specified millisecond multiple before completing execution.

Ticks

Causes the diagram or subdiagram to wait until the value of the operating system's tick timer becomes a multiple of the specified tick multiple before completing execution.

Parent topic:

Program Flow Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=wait-us.html language=enus -->
## TOPIC 00444: Microseconds

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `wait-us.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/wait-us.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Causes the diagram or subdiagram to wait a specified number of microseconds before completing execution. microseconds to wait Number of microseconds to wait. Wiring a value of 0 to this input forces the execution system to check for other available code to execute. Maximum Input before Timer Wrap-Ar

Microseconds

Causes the diagram or subdiagram to wait a specified number of microseconds before completing execution.

[IMAGE alt='1378' src='Wait.Microseconds.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### microseconds to wait

Number of microseconds to wait.

Wiring a value of 0 to this input forces the execution system to check for other available code to execute.

##### Maximum Input before Timer Wrap-Around

If the wait time you specify is greater than the maximum allowed for the 
 Counter size of the Wait node, the expected program wait time wraps around and starts again from zero. You can configure the 
 Counter size of the node in the 
 Item tab.

##### Highest Timer Resolution

The highest timer resolution for this node is one millisecond. Microsecond or tick values are rounded to the nearest millisecond value.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### microsecond timer value

Value of the operating system's microsecond timer after the wait.

#### Programming Patterns

- Adjusting the Execution Speed of a Loop

#### Timer Accuracy

The accuracy of the timer varies across operating systems.
 If the operating system takes more time to process a request than the time that the input specifies, the actual wait time is longer than the time that the input specifies.

#### When to Use Wait Until Next Multiple instead of Wait

If you need to ensure that an operation waits at least the specified time before completing execution, you can use either a Wait node or a Wait Until Next Multiple node. However, for functions that feedback an output as an input and require consistent timing between iterations to achieve equilibrium, such as a PID node in a loop, use a Wait Until Next Multiple node. Compared to Wait nodes, Wait Until Next Multiple nodes have more periodic spacing between iterations, because even if one iteration finishes late, the following iteration still executes on the multiple of the Wait Until Next Multiple input.

#### Thread Availability During Wait Time

When an active execution system thread in a program reaches a Wait node in the millisecond configuration, the node execution is rescheduled cooperatively and the temporarily available thread is used by any other currently executing code until the wait time expires.

When you use the microsecond or tick configuration of this node, the thread which encounters the Wait node is blocked until the wait time expires.

Parent topic:

Wait

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=wait.html language=enus -->
## TOPIC 00445: Wait

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `wait.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/wait.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits a specified amount of time.

Wait

Waits a specified amount of time.

Program Flow Nodes

Microseconds

Causes the diagram or subdiagram to wait a specified number of microseconds before completing execution.

Milliseconds

Waits the specified number of milliseconds and returns the value of the millisecond timer.

Ticks

Causes the diagram or subdiagram to wait a specified number of ticks before completing execution.

Parent topic:

Program Flow Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=waveform-constant.html language=enus -->
## TOPIC 00446: Waveform Constant

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `waveform-constant.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/waveform-constant.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents waveform data on the diagram, including the start time for the data, a delta t, and the y-value at each measurement point. start time (t0) A timestamp associated with the first measurement point in the waveform. delta t (dt) Time interval, in seconds, between any two points in the wavefor

Waveform Constant

Represents waveform data on the diagram, including the start time for the data, a delta t, and the y-value at each measurement point.

start time (t0)

delta t (dt)

Y values

To access these values, use Waveform Properties.

[IMAGE alt='1378' src='Literal.Waveform.png']

Parent topic:

Constants

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=waveform-duration.html language=enus -->
## TOPIC 00447: Waveform Duration

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `waveform-duration.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/waveform-duration.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes the duration of the specified waveform using the following equation: duration = (number of samples-1) x dx. open interval Interval over which the specified waveform extends. For example, assume a waveform contains 3 data elements at t = {0, dt, 2dt}. An open interval defines the waveform as

Waveform Duration

Computes the duration of the specified waveform using the following equation: 
*duration* = (*number of samples*-1) x *dx*.

[IMAGE alt='1378' src='WDT_Waveform_Duration_DBL.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### open interval

Interval over which the specified waveform extends.

t

dt

dt

t

dt

t

dt

| True | The specified waveform extends over an open interval. |
| --- | --- |
| False | The specified waveform extends over a closed interval. |

Default value: True

[IMAGE alt='datatype_icon' src='/assets/img/cmsdt.png']

##### waveform

Waveform for which you want the duration.

This input accepts a waveform or a digital waveform.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### duration

Duration of the waveform.

Parent topic:

Waveform Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=waveform-nodes.html language=enus -->
## TOPIC 00448: Waveform Nodes

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `waveform-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/waveform-nodes.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Create waveforms and access their components.

Waveform Nodes

Create waveforms and access their components.

Align Waveform Timestamps

Replaces the timestamp value (t0) of each waveform in waveform array with the timestamp value of the waveform at the index position you specify.

Copy Waveform dt

Replaces the dt value of each waveform in the waveform array with the dt value of the waveform at the index position you specify.

Get Final Time Value

xf

x

duration

Get Waveform Subset

Retrieves a subset of a waveform at a specified time or index.

Get Waveform Time Array

Creates an array of timestamps based on the specified waveform.

Get XY Value

Returns the X and Y value of a waveform or digital data set.

Index Waveform Array

Selects one waveform out of an array of analog or digital waveforms by array index or channel name.

Scale Delta t

t

Waveform Duration

duration

number of samples

dx

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=while-loop.html language=enus -->
## TOPIC 00449: While Loop

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `while-loop.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/while-loop.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Repeats the code on its subdiagram until a specific condition occurs. A While Loop always executes at least one time. A While Loop behaves similarly to a do while loop in other programming languages. Iteration Current loop iteration count. The loop count always starts at zero for the first iteration

While Loop

Repeats the code on its subdiagram until a specific condition occurs.
 
 A While Loop always executes at least one time.
 A While Loop behaves similarly to a 
 do while loop in other programming languages.

#### Inputs/Outputs

##### Iteration

Current loop iteration count. The loop count always starts at zero for the first iteration.

31

[IMAGE alt='1378' src='GUID-5E30A361-66F4-4AF5-9337-BA22F27F4B38-a5.png']

##### Condition

A Boolean input value to determine whether to continue executing the loop.

To specify whether the loop stops for a True or False Boolean value, configure the continuation behavior. You also can determine when the loop stops by wiring an error cluster to the condition terminal.

[IMAGE alt='1378' src='GUID-EC5CE940-A5DF-4D85-AE78-920340FF575B-a5.png']

##### Tunnel

Point through which data enters or exits a structure.

Tunnels can also assume the following types of functionality:

[IMAGE alt='1378' src='GUID-43DB7847-2DDA-4B38-86E0-27BE4951A189-a5.png']

[IMAGE alt='1378' src='GUID-0151FC5F-C6A8-4F4E-B434-909C7DF26499-a5.png']

Append Mode

»

Auto Index Values

[IMAGE alt='1378' src='GUID-50EAB18D-A07F-4B86-B609-A1531BCBF350-a5.png']

Build Array

You can configure a conditional output for any tunnel type by selecting the tunnel and clicking the 
 Conditional checkbox in the 
 Item tab. When the conditional input for a tunnel is True, the loop writes the corresponding value to the tunnel. When the condition input for the tunnel is False, the loop doesn't write the corresponding value to the tunnel.

[IMAGE alt='1378' src='GUID-43DB7847-2DDA-4B38-86E0-27BE4951A189-a5.png']

##### Shift Register

Member of a pair of terminals that passes a value from one iteration of a loop to the next iteration.After the initial loop iteration, the left shift register in the pair returns the value it receives from the right shift register from the previous iteration.

Refer to Accessing Data from the Previous Loop Iteration for more information about passing values from the previous iteration
 to the current iteration.

[IMAGE alt='1378' src='GUID-E948E02A-41FA-479B-955D-15152FA4BA46-a5.png']

##### Create Shift Register

Adds a pair of shift registers to the loop to pass data from one loop iteration to the next.

[IMAGE alt='1378' src='GUID-AE396CC4-A9DE-4BD1-B782-B59B66DBAC53-a5.png']

#### Programming Patterns

- Repeating Operations until a Condition Occurs

#### Controlling Loop Timing

Refer to Loop Timing for more information about controlling the execution speed of a
 loop.

#### Accessing Data from the Previous Loop Iteration

Refer to Accessing Data from the Previous Loop Iteration for more information about passing values from the previous iteration to
 the current iteration.

Parent topic:

Program Flow Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=white-space.html language=enus -->
## TOPIC 00450: White Space?

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `white-space.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/white-space.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns True if a value represents a white space character, such as Space, Tab, Newline, Carriage Return, Form Feed, or Vertical Tab. Otherwise, this node returns False. If the value is a string, this node uses the first character in the string. If the value is a number, this node interprets it as t

White Space?

Returns True if a value represents a white space character, such as Space, Tab, Newline, Carriage Return, Form Feed, or Vertical Tab. Otherwise, this node returns False.

If the value is a string, this node uses the first character in the string. If the value is a number, this node interprets it as the ASCII value of a character. If the value is a floating-point number, this node rounds to the nearest integer.

[IMAGE alt='1378' src='IsWhiteSpace.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### char

An input to this operation.

This input supports scalar strings or numbers, clusters of strings or numbers, arrays of strings or numbers, and so on.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### whitespace?

Boolean result of the operation.

This output assumes the same data type structure as 
 char.

Parent topic:

Comparison Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=word-report.html language=enus -->
## TOPIC 00451: Word Report (G Dataflow)

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `word-report.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/word-report.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `nodeCollection`
- source_description: Create Microsoft Word reports.

Word
 Report

Create Microsoft Word reports.

Close Word Report

Closes the reference to the Word report.

Insert Word Data

Adds text to the Word report.

Insert Word Table

Adds a 2D table with data to the Word report.

New Word Report

Creates a Word report.

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=write-delimited-spreadsheet.html language=enus -->
## TOPIC 00452: Write Delimited Spreadsheet

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `write-delimited-spreadsheet.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/write-delimited-spreadsheet.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts data to a text string and writes the string to a file. This node creates a text file readable by most spreadsheet applications. This node opens or creates the file before writing to it and closes it afterwards. format A string that uses format specifiers to determine how to convert the data

Write Delimited Spreadsheet

Converts data to a text string and writes the string to a file.

This node creates a text file readable by most spreadsheet applications. This node opens or creates the file before writing to it and closes it afterwards.

[IMAGE alt='1378' src='Write_Delimited_Spreadsheet_(DBL).gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### format

A string that uses format specifiers to determine how to convert the data into what you specify.

Default value: 
 %.3f

##### Syntax Elements for Creating a Format Specifier

Use the following syntax elements to create a format specifier for the input string.

| Syntax Element | Description |
| --- | --- |
| % | Syntax element that begins the format specifier. |
| $ (optional) | Modifier that specifies the order in which to display variables when used within a formatting node. Include the digit that represents the order of the variable immediately before this modifier. |
| - (optional) | Modifier that justifies the parameter to the left, within its width, when used within a formatting node. |
| + (optional) | Modifier that includes mathematical symbols when used within a formatting node. Note The mathematical symbols appear even when the number is positive. |
| ^ (optional) | Modifier that formats the number in engineering notation, where the exponent is always a multiple of three. Note This modifier must be used within a formatting node that has either an e or g conversion code in the format specifier. |
| # (optional) | Modifier that removes trailing zeros when used within a formatting node. If the number has no fractional part, this modifier also removes the description part. |
| 0 (optional) | Modifier that pads any excess space to the left of a numeric parameter with zeros, rather than spaces, to reach a minimum width when used within a formatting node. Note Using the - modifier with 0 nullifies the effect. |
| Width (optional) | Syntax element that specifies an exact field width to use. When used within a formatting node, the Width element specifies the minimum character field with of the output. The field is padded to the left or right of the parameter with spaces, depending on justification. Note As many characters as necessary are used to format the parameter without truncating it. |
| .Precision or _Significant Digits (optional) | Syntax element that controls the number of digits displayed when used within a formatting node. .precision—Yields the number of digits to the right of the decimal point. _Significant Digits—Rounds the data to the number of digits you specify. Note You cannot use precision and significant digits together in a single format specifier. |
| {Unit} (optional) | Syntax element that overrides the original unit of a VI when you use a node to convert a physical quantity. |
| <Embedded Time Format> (optional) | Contains a time-specific format string for use with the T (absolute time) and the t (relative time) conversion codes. Note Only %W, %D, %H, %M, %S, and %u apply to relative time. |
| Conversion Codes | Characters that specify how to scan or format a parameter. x—Hexadecimal integer o—Octal integer b—Binary integer d—Signed decimal integer u—Unsigned decimal integer f—Floating-point number with fractional format e—Floating-point number in scientific notation g—Uses f or e depending on the exponent of the number p—Floating-point number in SI notation s—Scans a string, matching only up to the next white-space character. [ ]—Scans characters in a set, matching a string that contains only the characters specified between the brackets. % [aeiou]—Scans characters in a set, matching any string that contains only lowercase vowels % [0-9a-zA-Z ]— Scans characters in a set, matching a string that contains numbers, letters, or spaces. You can use a hyphen to specify ranges of characters in the set. % [^,;]— Scans characters in a set, matching any string of characters up to but not including the first comma or semicolon. T—Absolute time t—Relative time |
| Localization Codes | Characters that determine whether to use a decimal or a comma to separate the whole number from the decimal part of the number. %,;—Comma decimal separator %.;—Period decimal separator %;—System default separator |
| Backslash (\\) Codes | Characters that specify hex values, spacing, backspaces, and other formatting options. |

##### Format Specifier Examples for Format

| format string | Description |
| --- | --- |
| %.3f | Creates a string to represent the number with three digits to the right of the decimal point. |
| %s | Copies the input string. |
| %d | Converts the data to integer form using as many characters as necessary to contain the entire number. |

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### time channel format

String that uses format specifiers to determine how to convert the time and channel
 data into what you specify.

This input becomes available only if you wire an array of digital waveforms to the node.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### include time channels

A Boolean value that determines whether the resulting spreadsheet will include a column of time values from the input array of waveforms.

This input becomes available only when you wire an array of waveforms to this node.

[IMAGE alt='datatype_icon' src='/assets/img/cpath.png']

##### file

The file to which this node writes.

If the path is empty, this node uses your default data directory (Documents>>LabVIEW Data).

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### 2D data

Data the node writes to the file.

This input accepts double-precision floating-point numbers, 64-bit integers, strings, and arrays of waveforms. This input changes to waveforms if you wire an array of waveforms to the node.

[IMAGE alt='datatype_icon' src='/assets/img/c1di64.png']

##### 2D data

Data the node writes to the file.

This input accepts double-precision floating-point numbers, 64-bit integers, strings, and
 arrays of waveforms. This input changes to match the data type you wire to the node.

[IMAGE alt='datatype_icon' src='/assets/img/c1dstr.png']

##### 2D data

Data the node writes to the file.

This input accepts double-precision floating-point numbers, 64-bit integers, strings, and
 arrays of waveforms. This input changes to waveforms if you
 wire an array of waveforms to the node.

[IMAGE alt='datatype_icon' src='/assets/img/c1di64.png']

##### 1D data

Data the node writes to the file.

This input accepts double-precision floating-point numbers, 64-bit integers, strings, and
 arrays of waveforms. This input changes to match the data type you wire to the node.

This input becomes available only if you wire a 1D array of 64-bit integers to the
 node.

[IMAGE alt='datatype_icon' src='/assets/img/c1ddbl.png']

##### 1D data

Data the node writes to the file.

This input accepts double-precision floating-point numbers, 64-bit integers, strings, and
 arrays of waveforms. This input changes to match the data type you wire to the node.

This input becomes available only if you wire a 1D array of double-precision
 floating-point numbers to the node.

[IMAGE alt='datatype_icon' src='/assets/img/c1dstr.png']

##### 1D data

Data the node writes to the file.

This input accepts double-precision floating-point numbers, 64-bit integers, strings, and
 arrays of waveforms. This input changes to match the data type you wire to the node.

This input becomes available only if you wire a 1D array of strings to the node.

[IMAGE alt='datatype_icon' src='/assets/img/c1di64.png']

##### 1D data

Data the node writes to the file.

This input accepts double-precision floating-point numbers, 64-bit integers, strings, and
 arrays of waveforms. This input changes to match the data type you wire to the node.

This input becomes available only if you wire a 1D array of 64-bit integers to the
 node.

[IMAGE alt='datatype_icon' src='/assets/img/cdigwfm.png']

##### digital waveform

Digital waveform whose y values the node writes to the spreadsheet
 file.

This input becomes available only if you wire a digital waveform to the node.

[IMAGE alt='datatype_icon' src='/assets/img/c1ddigwfm.png']

##### digital waveforms

Array of digital waveforms whose y values the node writes to the spreadsheet
 file.

This input becomes available only if you wire an array of digital waveforms to the node.

[IMAGE alt='datatype_icon' src='/assets/img/cmsdt.png']

##### waveform

Waveform whose y values the node writes to the spreadsheet file.

This input becomes available only if you wire a waveform to the node.

[IMAGE alt='datatype_icon' src='/assets/img/c1dmsdt.png']

##### waveforms

Array of waveforms whose y values the node writes to the spreadsheet file.

This input becomes available only if you wire an array of waveforms to the node.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### append to file

A Boolean that determines whether to add data to the end of the file you specify. If you do not specify a file, the node creates a new file.

| True | Appends data to the existing file. |
| --- | --- |
| False | Replaces the data in the file. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### delimiter

A character or string of characters used to separate fields in the spreadsheet text. For example, a value of 
, (comma) specifies a single comma as the delimiter.

Default value: 
 \t — single tab character

[IMAGE alt='datatype_icon' src='/assets/img/ipath.png']

##### new file

Path to the newly created file.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Storage Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=write-error-code.html language=enus -->
## TOPIC 00453: Write Error Code

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `write-error-code.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/write-error-code.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Replaces the error code in an error cluster. error in An error cluster that you use to check for errors or warnings. Standard Error Behavior code The error or warning code you want to write. error out An error cluster including any values this node writes, removes, or replaces. If no values change,

Write Error Code

Replaces the error code in an error cluster.

[IMAGE alt='1378' src='Write_Error_Code.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

An error cluster that you use to check for errors or warnings.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### code

The error or warning code you want to write.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

An error cluster including any values this node writes, removes, or replaces. If no values change, this node returns 
error in unchanged.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Error Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=write-registry-value-simple.html language=enus -->
## TOPIC 00454: Write Registry Value Simple

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `write-registry-value-simple.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/write-registry-value-simple.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes data to a registry value under a key. Incorrectly modifying the registry can damage Windows or prevent you from starting Windows. string/binary data Data of Windows registry type String or Binary. This input changes to DWORD data if you wire a 32-bit unsigned integer to this input. DWORD data

Write Registry Value Simple

Writes data to a registry value under a key.

Caution

[IMAGE alt='1378' src='Write_Registry_Value_Simple_STR.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### string/binary data

Data of Windows registry type 
String or 
Binary.

This input changes to DWORD data if you wire a 32-bit unsigned integer to this input.

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### DWORD data

Data of Windows registry type 
DWORD.

This input changes to string/binary data if you wire a string to this input.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### reference in

Reference to the open registry key.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### value

Name of the registry value.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### simple data type

Simplified Windows registry type.

| String | Windows registry type String. |
| --- | --- |
| Binary | Windows registry type Binary. |
| DWORD | Windows registry type DWORD. |

Default value: String

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### reference out

Reference to the open registry key.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Registry Nodes

<!--NI_TOPIC bundle=labview-nxg-nodes-api-ref path=write-to-system-log.html language=enus -->
## TOPIC 00455: Write to System Log

- bundle_id: `labview-nxg-nodes-api-ref`
- source_path: `write-to-system-log.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-nodes-api-ref/raw/resource/enus/write-to-system-log.html
- document_id: `labview-nxg-nodes-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes a message either for storage and subsequent viewing. The message is written to the nierrlog system log for non-web applications or the browser console or the G Web Development output window for WebVIs. message The text to write to the system log or browser console. severity The classification

Write to System Log

Writes a message either for storage and subsequent viewing. The message is written
 to the nierrlog system log for non-web applications
 or the browser console or the G Web Development output window for
 WebVIs.

[IMAGE alt='1378' src='Write_to_System_Log.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### message

The text to write to the system log or browser console.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### severity

The classification of the message this node writes to the
 system log or browser console.

| Error | 0 | Classifies the message as an error. |
| --- | --- | --- |
| Warning | 1 | Classifies the message as a warning. |
| Informational | 2 | Classifies the message as informational text. |

Default value: 0 — Error

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Accessing Log
 Data

View logs using Windows Event Viewer.

To create a file of logs generated in NXG, open
 Windows Event Viewer. Select Windows Logs»Applications to view all application logs. Select
 Filter Current Log in the
 Actions. Under the filter tab
 in the dialog, click on Event Sources
 and select National Instruments. Click
 OK. In the actions pane,
 select Save Filtered Log File As...
 to save a copy of the logs.

#### Logging Data to the Browser
 Console

Note

Mozilla Developer Network (MDN) documentation

Parent topic:

Interoperability Nodes
