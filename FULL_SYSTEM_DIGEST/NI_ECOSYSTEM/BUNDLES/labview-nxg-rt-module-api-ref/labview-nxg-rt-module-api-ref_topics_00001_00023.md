# NI DOCUMENT BUNDLE: labview-nxg-rt-module-api-ref

<!--NI_BUNDLE_CHUNK bundle=labview-nxg-rt-module-api-ref start=1 end=23 -->
<!--NI_TOPIC bundle=labview-nxg-rt-module-api-ref path=rt-board-leds.html language=enus -->
## TOPIC 00001: RT Board LEDs

- bundle_id: `labview-nxg-rt-module-api-ref`
- source_path: `rt-board-leds.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-api-ref/raw/resource/enus/rt-board-leds.html
- document_id: `labview-nxg-rt-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Controls the LEDs on all RT Series devices. LED num Number of the LED that the VI modifies. The LED number depends on the type of hardware. LED num is zero-indexed. You can specify LED num 0 to control the User1 LED for most LabVIEW Real-Time targets. state State to assign to the LED. Off Turns off

RT Board LEDs

Controls the LEDs on all RT Series devices.

[IMAGE alt='1378' src='RT_Board_LEDs.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### LED num

Number of the LED that the VI modifies. The LED number depends on the type of hardware.
 LED num is zero-indexed. You can specify LED
 num 0 to control the User1 LED for most LabVIEW Real-Time targets.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### state

State to assign to the LED.

| Off | Turns off the LED |
| --- | --- |
| Default Color 1 | Sets the LED to the device default color 1 |
| Default Color 2 | Sets the LED to the device default color 2 (if available) |
| Toggle | Toggles between off and device default color 1 |

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### LED state

Boolean value that indicates whether the LED is on or off.

| True | The LED is on. |
| --- | --- |
| False | The LED is off. |

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Real-Time Nodes

<!--NI_TOPIC bundle=labview-nxg-rt-module-api-ref path=rt-debug-string.html language=enus -->
## TOPIC 00002: RT Debug String

- bundle_id: `labview-nxg-rt-module-api-ref`
- source_path: `rt-debug-string.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-api-ref/raw/resource/enus/rt-debug-string.html
- document_id: `labview-nxg-rt-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a string to an output port for display, or writes a string to the system log. string to write Defines the data string to write to the output port or system log. interface Defines whether to send the string to an output port or to write the string to the system log. Write to monitor 0 Sends the

RT Debug String

Sends a string to an output port for display, or writes a string to the system log.

[IMAGE alt='1378' src='RT_Debug_String.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### string to write

Defines the data string to write to the output port or system log.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### interface

Defines whether to send the string to an output port or to write the string to the system log.

| Write to monitor | 0 | Sends the debug string to the video port. If no video port is available, this option sends the debug string to the console. |
| --- | --- | --- |
| Write to system log | 1 | Sends the debug string to the nierrlog system log located in /var/local/natinst/log/errlog.txt on the target. |

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

Parent topic:

Real-Time Nodes

<!--NI_TOPIC bundle=labview-nxg-rt-module-api-ref path=rt-fifo-create.html language=enus -->
## TOPIC 00003: RT FIFO Create

- bundle_id: `labview-nxg-rt-module-api-ref`
- source_path: `rt-fifo-create.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-api-ref/raw/resource/enus/rt-fifo-create.html
- document_id: `labview-nxg-rt-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an RT FIFO or obtains a reference to an existing RT FIFO that you can use with other RT FIFO nodes. elements in array The number of elements in the array for each RT FIFO element. This input only applies if the RT FIFO elements are arrays. RT FIFOs do not support multi-dimensional arrays. De

RT FIFO Create

Creates an RT FIFO or obtains a reference to an existing RT FIFO that you can use with other RT FIFO nodes.

[IMAGE alt='1378' src='RTFIFOCreate.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### elements in array

The number of elements in the array for each RT FIFO element.

This input only applies if the RT FIFO elements are arrays. RT FIFOs do not support multi-dimensional arrays.

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### size

The number of elements in the RT FIFO.

Default value: 10

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### name

The name of the RT FIFO that you want to obtain or create.

Default value: Empty string

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### type

Defines the type of data that you want the RT FIFO to contain. RT FIFOs do not support data types of variable size, such as clusters, strings, and variants. RT FIFOs also do not support multi-dimensional arrays.

##### Waveform Data Transfer with RT FIFOs

If you use an RT FIFO to transfer waveform data, the attributes of the waveform do not transfer. The attributes element of a waveform is a variant, which is variable-sized and therefore incompatible with the RT FIFO.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### create if not found?

A Boolean that determines whether to create a new RT FIFO if the FIFO specified by name does not currently exist.

| True | The node creates a new RT FIFO if the FIFO specified by name does not exist. |
| --- | --- |
| False | The node does not create a new RT FIFO and returns an error if the FIFO specified by name does not exist. |

Default value: True

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### datapoints in waveform

The number of datapoints for every element of the array of waveforms. This input only applies if the RT FIFO elements are waveforms.

Default value: 1

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### r/w modes

Read and write modes for a new RT FIFO. The read and write modes define the behavior of an RT FIFO that reads a value from an empty RT FIFO or writes a value to an RT FIFO that does not have an empty slot.

polling

polling

timeout in ms

RT FIFO Read

RT FIFO Write

blocking

timeout in ms

RT FIFO Read

RT FIFO Write

RT FIFO Create

r/w modes

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### read mode

Read mode for the RT FIFO.

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### write mode

Write mode for the RT FIFO.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### rt fifo

References an existing or newly created RT FIFO.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### created new?

A Boolean that indicates whether the node created a new FT FIFO.

| True | The node created a new RT FIFO. |
| --- | --- |
| False | The node did not create a new RT FIFO. |

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

- Transferring Data to Deterministic Code

Parent topic:

RT FIFO Nodes

<!--NI_TOPIC bundle=labview-nxg-rt-module-api-ref path=rt-fifo-delete.html language=enus -->
## TOPIC 00004: RT FIFO Delete

- bundle_id: `labview-nxg-rt-module-api-ref`
- source_path: `rt-fifo-delete.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-api-ref/raw/resource/enus/rt-fifo-delete.html
- document_id: `labview-nxg-rt-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes one or all references to a specified RT FIFO. You must delete an RT FIFO reference to free memory resources allocated for the FIFO when you created the reference. Deleting a reference to an RT FIFO does not delete the original RT FIFO by default. Use the force destroy? input to specify to de

RT FIFO Delete

Deletes one or all references to a specified RT FIFO.

You must delete an RT FIFO reference to free memory resources allocated for the FIFO when you created the reference. Deleting a reference to an RT FIFO does not delete the original RT FIFO by default. Use the force destroy? input to specify to delete all reference to the RT FIFO.

[IMAGE alt='1378' src='RTFIFODelete.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### rt fifo

References an existing RT FIFO.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### force destroy?

A Boolean that determines whether to delete all references to the RT FIFO.

| True | Deletes all references to the RT FIFO. |
| --- | --- |
| False | Deletes the individual reference wired to rt fifo. |

Default value: False

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

#### Programming Patterns

- Transferring Data to Deterministic Code

Parent topic:

RT FIFO Nodes

<!--NI_TOPIC bundle=labview-nxg-rt-module-api-ref path=rt-fifo-read.html language=enus -->
## TOPIC 00005: RT FIFO Read

- bundle_id: `labview-nxg-rt-module-api-ref`
- source_path: `rt-fifo-read.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-api-ref/raw/resource/enus/rt-fifo-read.html
- document_id: `labview-nxg-rt-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the oldest element in an RT FIFO. If no new data exists in the RT FIFO or if the RT FIFO is empty, this node waits for the amount of time specified in timeout in ms for new data. If the value of timeout in ms expires, the node returns the value wired to element in the element out output and re

RT FIFO Read

Reads the oldest element in an RT FIFO.

If no new data exists in the RT FIFO or if the RT FIFO is empty, this node waits for the amount of time specified in timeout in ms for new data. If the value of timeout in ms expires, the node returns the value wired to element in the element out output and returns True in the empty? output.

[IMAGE alt='1378' src='RTFIFORead.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### rt fifo

References an existing RT FIFO.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### element

Sets the default return value of an empty RT FIFO. This data type changes to match the type of the default return value you wire.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### timeout in ms

Time, in milliseconds, that the node waits to receive a new value if the RT FIFO is empty. Wire a -1 to the timeout in ms input to wait indefinitely.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### rt fifo out

A reference to the RT FIFO defined in rt fifo.

[IMAGE alt='datatype_icon' src='/assets/img/istr.png']

##### element out

The data read from the RT FIFO. If the node does not read new data, the node returns the default element.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### empty?

A Boolean that indicates whether the RT FIFO is empty when you read it.

| True | The RT FIFO is empty and the FIFO timed out. |
| --- | --- |
| False | The RT FIFO is not empty. |

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### number of elements

Number of elements remaining in the RT FIFO after the read or write operation.

#### Programming Patterns

- Transferring Data to Deterministic Code

Parent topic:

RT FIFO Nodes

<!--NI_TOPIC bundle=labview-nxg-rt-module-api-ref path=rt-fifo-write.html language=enus -->
## TOPIC 00006: RT FIFO Write

- bundle_id: `labview-nxg-rt-module-api-ref`
- source_path: `rt-fifo-write.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-api-ref/raw/resource/enus/rt-fifo-write.html
- document_id: `labview-nxg-rt-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes an element to an RT FIFO. If the RT FIFO does not have empty elements, this node waits for an amount of time equal to the value of timeout in ms for an element to become available. If an empty element does not become available before the value of timeout in ms expires and overwrite on timeout

RT FIFO Write

Writes an element to an RT FIFO.
 If the RT FIFO does not have empty elements, this node waits for an amount of time equal to the value of timeout in ms for an element to become available. If an empty element does not become available before the value of timeout in ms expires and overwrite on timeout is True, this node overwrites the oldest element in the RT FIFO and returns True in timed out?.

Note

[IMAGE alt='1378' src='RTFIFOWrite.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdvrn.png']

##### rt fifo

References an existing RT FIFO.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### element

The data to write to the RT FIFO. This data type changes to match the type of the value you want to write.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### timeout in ms

Time, in milliseconds, that the node waits for an empty slot to write the data in the RT FIFO. Wire a 
-1 to the timeout in ms input to wait infinitely.

Default value: 0

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### overwrite on timeout

Defines whether to overwrite the oldest value in the RT FIFO if the FIFO does not have an available open slot and the value of the timeout in ms input expires.

timeout in ms

| True | The RT FIFO overwrites the oldest value and returns True in the timed out? output if the FIFO times out. |
| --- | --- |
| False | The RT FIFO does not overwrite the oldest value if the FIFO times out. |

Default value: True

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### rt fifo out

A reference to the RT FIFO defined in rt fifo.

[IMAGE alt='datatype_icon' src='/assets/img/ibool.png']

##### timed out?

A Boolean that indicates whether the FIFO times out before an empty slot becomes available for the write operation.

| True | The FIFO timed out before an empty slot became available. |
| --- | --- |
| False | The FIFO did not time out. |

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### number of elements

Number of elements remaining in the RT FIFO after the read or write operation.

#### Programming Patterns

- Transferring Data to Deterministic Code

Parent topic:

RT FIFO Nodes

<!--NI_TOPIC bundle=labview-nxg-rt-module-api-ref path=rt-get-cpu-loads.html language=enus -->
## TOPIC 00007: RT Get CPU Loads

- bundle_id: `labview-nxg-rt-module-api-ref`
- source_path: `rt-get-cpu-loads.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-api-ref/raw/resource/enus/rt-get-cpu-loads.html
- document_id: `labview-nxg-rt-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Monitors the distribution of load on the CPUs in the system. For each CPU in the system, this node returns the total load as a percentage of capacity. This node also returns the percentage of CPU time devoted to each priority level, the percentage of idle CPU time, and the percentage of CPU time dev

RT Get CPU Loads

Monitors the distribution of load on the CPUs in the system. For each CPU in the system, this node returns the total load as a percentage of capacity. This node also returns the percentage of CPU time devoted to each priority level, the percentage of idle CPU time, and the percentage of CPU time devoted to Timed Structures and interrupt service routines (ISRs).

[IMAGE alt='1378' src='RT_Get_CPU_Loads.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/i1dcclst.png']

##### CPU loads

Data corresponding to the distribution of load for each CPU in the system. The Nth element of this array corresponds to the Nth CPU in the system.

CPU numbering begins at zero.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### Total (%)

Returns the total CPU usage as a percentage of capacity.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### Time Critical (%)

Returns the CPU usage devoted to time-critical threads as a percentage of total CPU capacity.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### Timed Structures (%)

Returns the CPU usage devoted to timed structures as a percentage of total CPU capacity.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### High (%)

Returns the CPU usage devoted to high priority threads as a percentage of total CPU capacity. (Real-Time Linux) CPU usage data is unavailable for this priority level. This output returns a value of 0.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### Above Normal (%)

Returns the CPU usage devoted to above normal priority threads as a percentage of total CPU capacity. (Real-Time Linux) CPU usage data is unavailable for this priority level. This output returns a value of 0.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### Normal (%)

Returns the CPU usage devoted to normal priority threads as a percentage of total CPU capacity.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### Background (%)

Returns the CPU usage devoted to background priority threads as a percentage of total CPU capacity. (Real-Time Linux) CPU usage data is unavailable for this priority level. This output returns a value of 0.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### Idle (%)

Returns the amount of idle CPU time as a percentage of total CPU capacity.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### ISR (%)

Returns the CPU usage devoted to interrupt service routines (ISRs) as a percentage of total CPU capacity.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

CPU Utility Nodes

<!--NI_TOPIC bundle=labview-nxg-rt-module-api-ref path=rt-get-number-of-cpus.html language=enus -->
## TOPIC 00008: RT Get Number of CPUs

- bundle_id: `labview-nxg-rt-module-api-ref`
- source_path: `rt-get-number-of-cpus.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-api-ref/raw/resource/enus/rt-get-number-of-cpus.html
- document_id: `labview-nxg-rt-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the number of CPUs in the system. error in Error conditions that occur before this node runs. The node responds to this input according to standard error behavior. Standard Error Behavior Default value: No error # of CPUs Number of CPUs in the system. error out Error information. The node prod

RT Get Number of CPUs

Reads the number of CPUs in the system.

[IMAGE alt='1378' src='RT_Get_Number_of_CPUs.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### # of CPUs

Number of CPUs in the system.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

CPU Utility Nodes

<!--NI_TOPIC bundle=labview-nxg-rt-module-api-ref path=rt-get-timestamp.html language=enus -->
## TOPIC 00009: RT Get Timestamp

- bundle_id: `labview-nxg-rt-module-api-ref`
- source_path: `rt-get-timestamp.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-api-ref/raw/resource/enus/rt-get-timestamp.html
- document_id: `labview-nxg-rt-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Inserts a 64-bit timestamp value from a high-precision timing source into a preallocated array at an index value specified by iteration. The timestamp value indicates the time when the RT Get Timestamp node executes on the RT target. Use the RT Timestamp Analysis node to analyze the timestamp array

RT Get Timestamp

Inserts a 64-bit timestamp value from a high-precision timing source into a preallocated array at an index value specified by iteration. The timestamp value indicates the time when the RT Get Timestamp node executes on the RT target.

Use the RT Timestamp Analysis node to analyze the timestamp array returned by the RT Get Timestamp node.

[IMAGE alt='1378' src='RT_Get_Timestamp.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1du64.png']

##### timestamp array in

Preallocated array used to store timestamps for each iteration of the RT Get Timestamp node.

You must preallocate an array with enough elements to store all of the timestamps you want to collect.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### iteration

Index value where the RT Get Timestamp node inserts the current timestamp in the timestamp array.

Wire a loop iteration terminal to index the timestamps relative to their execution order.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: no error

[IMAGE alt='datatype_icon' src='/assets/img/i1du64.png']

##### timestamp array out

Returns an array that contains a timestamp for each iteration of the RT Get Timestamp node.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

Unlike most nodes, this node runs normally even if error in contains an error.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Real-Time Nodes

<!--NI_TOPIC bundle=labview-nxg-rt-module-api-ref path=rt-set-cpu-pool-assignments.html language=enus -->
## TOPIC 00010: Set Pool Assignments

- bundle_id: `labview-nxg-rt-module-api-ref`
- source_path: `rt-set-cpu-pool-assignments.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-api-ref/raw/resource/enus/rt-set-cpu-pool-assignments.html
- document_id: `labview-nxg-rt-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the pool assignment of each CPU in the real-time operating system (RTOS) for automatic load balancing. CPU pools Pools to assign for each CPU in the system. Each element of the array represents a CPU. The array indices 0 - N correspond to the CPU indices 0 - N. System and Timed Structures Assig

Set Pool Assignments

Sets the pool assignment of each CPU in the real-time operating system (RTOS) for automatic load balancing.

[IMAGE alt='1378' src='RT_Set_CPU_Pool_Assignments.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1du16.png']

##### CPU pools

Pools to assign for each CPU in the system.

Each element of the array represents a CPU. The array indices 0 - N correspond to the CPU indices 0 - N.

| System and Timed Structures | Assigns the CPU to both the System pool and the Timed Structures pool for automatic load balancing of all threads that are not manually assigned to a particular CPU. |
| --- | --- |
| System | Assigns the CPU to the System pool for automatic load balancing of non-Timed-Loop threads. |
| Timed Structures | Assigns the CPU to the Timed Structures pool for automatic load balancing of Timed Loop threads. |
| Reserved | Assigns the CPU to neither pool. The CPU is reserved for Timed Loops configured for manual processor assignment. |

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/i1du16.png']

##### assigned CPU pools

Pool assignment of each CPU.

| System and Timed Structures | The CPU is assigned to both the System pool and the Timed Structures pool for automatic load balancing of all threads that are not manually assigned to a particular CPU. |
| --- | --- |
| System | The CPU is assigned to the System pool for automatic load balancing of non-Timed-Loop threads. |
| Timed Structures | The CPU is assigned to the Timed Structures pool for automatic load balancing of Timed Loop threads. |
| Reserved | The CPU is not assigned to a pool. The CPU is reserved for Timed Loops configured for manual processor assignment. |

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### system mask

Bit mask corresponding to the System pool assignments.

[IMAGE alt='datatype_icon' src='/assets/img/iu32.png']

##### timed structures mask

Bit mask corresponding to the Timed Structures pool assignments.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Maximizing Performance of Deterministic Timed Loops

You can maximize performance in a deterministic Timed Loop by assigning the Timed Loop to a high-index CPU that is Reserved. For example, if the real-time operating system (RTOS) contains four CPU cores indexed 0-3, consider setting the state of CPU 3 as Reserved and assigning the deterministic Timed Loop to CPU 3.

Assigning high-performance and deterministic Timed Loops to high-index CPUs minimizes latency because an RTOS begins at the highest-index CPU and increments down when scheduling Timed Loops. If multiple Timed Loops of equal priority are scheduled to wake up at the same time, the wake-up latency of Timed Loops executing on lower-index CPUs can be higher than that of Timed Loops executing on higher-index CPUs by up to several microseconds. The reverse is true for non-Timed-Loop threads because for these threads the scheduler starts at CPU 0 and increments up. NI recommends that you assign lower-index CPUs to the System pool and higher-index CPUs to deterministic Timed Loops to minimize latency.

Setting a CPU to the Reserved state ensures that the CPU is reserved to run only the Timed Loop(s) that you manually assign to that CPU. If you assign only one Timed Loop to a reserved CPU, you can monopolize the processing capacity of that CPU and achieve high frequency or throughput rates.

#### Maximizing CPU Utilization

To maximize processor utilization, you can adjust the number of CPUs to assign to each pool based on the estimation of the proportion of total processing time dedicated to Timed Loops versus system threads. You can estimate the processing load distribution using the RT Get CPU Loads node.

Another way to maximize CPU utilization is avoiding partial pool overlapping. If you define the System and Timed Structures pools such that the two pools partially overlap, the automatic load balancing process might not make optimal processor-utilization decisions.

#### Preventing Thread Starvation

To prevent starvation of system threads, consider reserving at least one CPU for system threads only. For example, if you assign CPU 0 to the System pool but not to the Timed Structures pool, and you avoid targeting any Timed Loops to CPU 0, CPU 0 is always available to run system threads.

Parent topic:

RT Set CPU Pools

Related information:

- Automatic Load Balancing

<!--NI_TOPIC bundle=labview-nxg-rt-module-api-ref path=rt-set-cpu-pool-sizes.html language=enus -->
## TOPIC 00011: Set Pool Sizes

- bundle_id: `labview-nxg-rt-module-api-ref`
- source_path: `rt-set-cpu-pool-sizes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-api-ref/raw/resource/enus/rt-set-cpu-pool-sizes.html
- document_id: `labview-nxg-rt-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of CPUs in the CPU pools for automatic load balancing. This node creates the System and Timed Structures pools as adjacent pools of contiguous CPUs. The System pool begins at CPU 0 and the Timed Structures pool begins where the System pool ends. You cannot use this node to create emp

Set Pool Sizes

Sets the number of CPUs in the CPU pools for automatic load balancing.

This node creates the System and Timed Structures pools as adjacent pools of contiguous CPUs. The System pool begins at CPU 0 and the Timed Structures pool begins where the System pool ends.

Note

[IMAGE alt='1378' src='RT_Set_CPU_Pool_Sizes.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### system pool

Number of CPUs to assign to the System pool.

This node returns an error if you specify 0 in this input or if the values you specify for system pool and timed structures pool add up to more than the number of CPUs available in the real-time operating system (RTOS).

If you set both system pool and timed structures pool to -1, this node assigns all CPUs in the RTOS to both pools. If you set either system pool or timed structures pool to -1, this node assigns all remaining CPUs to that pool.

Default value: -1

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### timed structures pool

Number of CPUs to assign to the Timed Structures pool.

This node returns an error if you specify 0 in this input or if the values you specify for system pool and timed structures pool add up to more than the number of CPUs available in the real-time operating system (RTOS).

If you set both system pool and timed structures pool to -1, this node assigns all CPUs in the RTOS to both pools. If you set either system pool or timed structures pool to -1, this node assigns all remaining CPUs to that pool.

Default value: -1

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/i1du16.png']

##### assigned CPU pools

Pool assignment of each CPU.

| System and Timed Structures | The CPU is assigned to both the System pool and the Timed Structures pool for automatic load balancing of all threads that are not manually assigned to a particular CPU. |
| --- | --- |
| System | The CPU is assigned to the System pool for automatic load balancing of non-Timed-Loop threads. |
| Timed Structures | The CPU is assigned to the Timed Structures pool for automatic load balancing of Timed Loop threads. |
| Reserved | The CPU is not assigned to a pool. The CPU is reserved for Timed Loops configured for manual processor assignment. |

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Examples

system pool

timed structures pool

#### Maximizing CPU Utilization

To maximize processor utilization, you can adjust the number of CPUs to assign to each pool based on the estimation of the proportion of total processing time dedicated to Timed Loops versus system threads. You can estimate the processing load distribution using the RT Get CPU Loads node.

Parent topic:

RT Set CPU Pools

Related information:

- Automatic Load Balancing

<!--NI_TOPIC bundle=labview-nxg-rt-module-api-ref path=rt-set-cpu-pool.html language=enus -->
## TOPIC 00012: Set Pool

- bundle_id: `labview-nxg-rt-module-api-ref`
- source_path: `rt-set-cpu-pool.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-api-ref/raw/resource/enus/rt-set-cpu-pool.html
- document_id: `labview-nxg-rt-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the CPUs to include in the System pool or the Timed Structures pool for automatic load balancing. pool Pool to set. System Set the System pool. Timed Structures Set the Timed Structures pool. CPU mask CPUs to assign to the pool. This input is a bit mask in which the right-most bit correspo

Set Pool

Specifies the CPUs to include in the System pool or the Timed Structures pool for automatic load balancing.

[IMAGE alt='1378' src='RT_Set_CPU_Pool.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu16.png']

##### pool

Pool to set.

| System | Set the System pool. |
| --- | --- |
| Timed Structures | Set the Timed Structures pool. |

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### CPU mask

CPUs to assign to the pool.

This input is a bit mask in which the right-most bit corresponds to CPU 0 and the left-most bit corresponds to CPU 31, if such a CPU exists in the real-time operating system. To include a CPU in the pool, set the value of the corresponding bit to 1. To exclude a CPU from the pool, set the value of the corresponding bit to 0.

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

Parent topic:

RT Set CPU Pools

Related information:

- Automatic Load Balancing

<!--NI_TOPIC bundle=labview-nxg-rt-module-api-ref path=rt-set-cpu-pools-multimode-function.html language=enus -->
## TOPIC 00013: RT Set CPU Pools

- bundle_id: `labview-nxg-rt-module-api-ref`
- source_path: `rt-set-cpu-pools-multimode-function.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-api-ref/raw/resource/enus/rt-set-cpu-pools-multimode-function.html
- document_id: `labview-nxg-rt-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures CPU pools for automatic load balancing.

RT Set CPU Pools

Configures CPU pools for automatic load balancing.

CPU Utility Nodes

Manage CPU configuration on the real-time target.

Set Pool

Specifies the CPUs to include in the System pool or the Timed Structures pool for automatic load balancing.

Set Pool Assignments

Sets the pool assignment of each CPU in the real-time operating system (RTOS) for automatic load balancing.

Set Pool Sizes

Sets the number of CPUs in the CPU pools for automatic load balancing.

Automatic Load Balancing

Parent topic:

CPU Utility Nodes

Related information:

- Automatic Load Balancing

<!--NI_TOPIC bundle=labview-nxg-rt-module-api-ref path=rt-timestamp-analysis.html language=enus -->
## TOPIC 00014: RT Timestamp Analysis

- bundle_id: `labview-nxg-rt-module-api-ref`
- source_path: `rt-timestamp-analysis.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-api-ref/raw/resource/enus/rt-timestamp-analysis.html
- document_id: `labview-nxg-rt-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Analyzes the array of timestamps returned by the RT Get Timestamp node. timestamp array Array of 64-bit timestamps returned from the RT Get Timestamp node that you want to analyze. calibration array An array used to account for the time required for the RT Get Timestamp node to execute. The RT Times

RT Timestamp Analysis

Analyzes the array of timestamps returned by the RT Get Timestamp node.

[IMAGE alt='1378' src='RT_Timestamp_Analysis.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/c1du64.png']

##### timestamp array

Array of 64-bit timestamps returned from the RT Get Timestamp node that you want to analyze.

[IMAGE alt='datatype_icon' src='/assets/img/c1du64.png']

##### calibration array

An array used to account for the time required for the RT Get Timestamp node to execute. The RT Timestamp Analysis node subtracts the mean value of all elements in calibration array from each element in timestamp array to remove the timestamp errors introduced when the RT Get Timestamp node adds the element to the timestamp array in memory on the RT target.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### warmup iterations

Number of timestamps to ignore from the beginning of timestamp array.

Warmup iterations

timestamp array

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: no error

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### mean time (μS)

Average execution time for the values in the execution times array.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### standard deviation (μS)

Standard deviation for the values in the execution times array.

[IMAGE alt='datatype_icon' src='/assets/img/i1ddbl.png']

##### execution times (μS)

Execution time, in microseconds, between each element of timestamp array.

[IMAGE alt='datatype_icon' src='/assets/img/icclst.png']

##### execution histogram

Histogram values for the elements of execution times.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### max jitter (μS)

Maximum deviation between elements of execution time and the value of mean time.

The value can represent a positive or negative deviation.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

Unlike most nodes, this node runs normally even if error in contains an error.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

Real-Time Nodes

<!--NI_TOPIC bundle=labview-nxg-rt-module-api-ref path=rt-tracetool-nodes.html language=enus -->
## TOPIC 00015: RT Execution TraceTool Nodes

- bundle_id: `labview-nxg-rt-module-api-ref`
- source_path: `rt-tracetool-nodes.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-api-ref/raw/resource/enus/rt-tracetool-nodes.html
- document_id: `labview-nxg-rt-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Manage execution tracing on the Real-Time target.

RT Execution TraceTool Nodes

Manage execution tracing on the Real-Time target.

Real-Time Nodes

TraceTool Load Trace and Send

Loads a trace session file and sends the trace session to the Real-Time Trace Viewer running on the host computer.

TraceTool Log User Event

Logs a user-defined event in the trace session.

TraceTool Start Trace

Starts a trace session and logs VI and thread events from all VIs that begin executing after the TraceTool Start Trace node executes. You must ensure that you wire the TraceTool Start Trace node in sequence with all of the VIs that you want to log.

TraceTool Stop Trace and Save

Stops logging event data from the application and saves the trace session to file on the RT target.

TraceTool Stop Trace and Send

Stops logging data from the application running on the RT target and sends the trace session to the Real-Time Trace Viewer running on the host computer.

Parent topic:

Real-Time Nodes

<!--NI_TOPIC bundle=labview-nxg-rt-module-api-ref path=tracetool-load-trace-and-send.html language=enus -->
## TOPIC 00016: TraceTool Load Trace and Send

- bundle_id: `labview-nxg-rt-module-api-ref`
- source_path: `tracetool-load-trace-and-send.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-api-ref/raw/resource/enus/tracetool-load-trace-and-send.html
- document_id: `labview-nxg-rt-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Loads a trace session file and sends the trace session to the Real-Time Trace Viewer running on the host computer. Find the Real-Time Trace Viewer by searching from the Start menu of the host computer. Use the TraceTool Stop Trace and Save node to save a trace session to file on the RT target. path

TraceTool Load Trace and Send

Loads a trace session file and sends the trace session to the Real-Time Trace Viewer running on the host computer.
 Find the Real-Time Trace Viewer by searching from the Start menu of the host computer.

Use the TraceTool Stop Trace and Save node to save a trace session to file on the RT target.

[IMAGE alt='1378' src='TraceTool_Load_Trace_and_Send.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cpath.png']

##### path to trace log

Path to the trace session file on the RT target.

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### trace host network address

The IP address of the host computer where you want to send the trace session.

The Real-Time Trace Viewer must be running on the host computer to receive the trace session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: no error

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

Unlike most nodes, this node runs normally even if error in contains an error.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

RT Execution TraceTool Nodes

<!--NI_TOPIC bundle=labview-nxg-rt-module-api-ref path=tracetool-log-user-event.html language=enus -->
## TOPIC 00017: TraceTool Log User Event

- bundle_id: `labview-nxg-rt-module-api-ref`
- source_path: `tracetool-log-user-event.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-api-ref/raw/resource/enus/tracetool-log-user-event.html
- document_id: `labview-nxg-rt-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Logs a user-defined event in the trace session. Use the Flag Configuration dialog box in the Real-Time Trace Viewer to configure user event flags. Find the Real-Time Trace Viewer by searching from the Start menu of the host computer. event ID The event code (0-255) you assign to the custom event fla

TraceTool Log User Event

Logs a user-defined event in the trace session.

Use the Flag Configuration dialog box in the Real-Time Trace Viewer to configure user event flags.

Find the Real-Time Trace Viewer by searching from the Start menu of the host computer.

[IMAGE alt='1378' src='TraceTool_Log_User_Event.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu32.png']

##### event ID

The event code (0-255) you assign to the custom event flag.

Use the Flag Configuration dialog box of the Real-Time Trace Viewer to configure user event flags.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: no error

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

Unlike most nodes, this node runs normally even if error in contains an error.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

RT Execution TraceTool Nodes

<!--NI_TOPIC bundle=labview-nxg-rt-module-api-ref path=tracetool-start-trace.html language=enus -->
## TOPIC 00018: TraceTool Start Trace

- bundle_id: `labview-nxg-rt-module-api-ref`
- source_path: `tracetool-start-trace.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-api-ref/raw/resource/enus/tracetool-start-trace.html
- document_id: `labview-nxg-rt-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Starts a trace session and logs VI and thread events from all VIs that begin executing after the TraceTool Start Trace node executes. You must ensure that you wire the TraceTool Start Trace node in sequence with all of the VIs that you want to log. detailed tracing? Enables logging of analysis and c

TraceTool Start Trace

Starts a trace session and logs VI and thread events from all VIs that begin executing after the TraceTool Start Trace node executes. You must ensure that you wire the TraceTool Start Trace node in sequence with all of the VIs that you want to log.

[IMAGE alt='1378' src='TraceTool_Start_Trace.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### detailed tracing?

Enables logging of analysis and custom events in the trace session. You must set the detailed tracing? input to TRUE to log analysis and custom events. The default is FALSE.

[IMAGE alt='datatype_icon' src='/assets/img/ci32.png']

##### buffer size

Defines the size of the memory buffer, in bytes, that logs all events from VIs in memory on the RT target. You must create an appropriately-sized memory buffer to capture all event data. You must not exceed the memory buffer size. Otherwise, the log file may become unusable because overflow may occur from multiple event sources and at different speeds.

Note

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### thread tracing?

Enables the logging of thread event data from the application running on the RT target. The default is TRUE.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### VI tracing?

Enables the logging of VI event data from the application running on the RT target. The default is TRUE.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: no error

[IMAGE alt='datatype_icon' src='/assets/img/ii32.png']

##### actual buffer size

Actual size of the memory buffer, in bytes, allocated for event logging if the real-time operating system cannot allocate the requested buffer size.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

Unlike most nodes, this node runs normally even if error in contains an error.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

RT Execution TraceTool Nodes

<!--NI_TOPIC bundle=labview-nxg-rt-module-api-ref path=tracetool-stop-trace-and-save.html language=enus -->
## TOPIC 00019: TraceTool Stop Trace and Save

- bundle_id: `labview-nxg-rt-module-api-ref`
- source_path: `tracetool-stop-trace-and-save.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-api-ref/raw/resource/enus/tracetool-stop-trace-and-save.html
- document_id: `labview-nxg-rt-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops logging event data from the application and saves the trace session to file on the RT target. Use the TraceTool Load Trace and Send node to transfer the trace session file to the host computer. path to trace log Path to the trace session file on the RT target. error in Error conditions that oc

TraceTool Stop Trace and Save

Stops logging event data from the application and saves the trace session to file on the RT target.

Use the TraceTool Load Trace and Send node to transfer the trace session file to the host computer.

[IMAGE alt='1378' src='TraceTool_Stop_Trace_and_Save.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cpath.png']

##### path to trace log

Path to the trace session file on the RT target.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: no error

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

Unlike most nodes, this node runs normally even if error in contains an error.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

RT Execution TraceTool Nodes

<!--NI_TOPIC bundle=labview-nxg-rt-module-api-ref path=tracetool-stop-trace-and-send.html language=enus -->
## TOPIC 00020: TraceTool Stop Trace and Send

- bundle_id: `labview-nxg-rt-module-api-ref`
- source_path: `tracetool-stop-trace-and-send.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-api-ref/raw/resource/enus/tracetool-stop-trace-and-send.html
- document_id: `labview-nxg-rt-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops logging data from the application running on the RT target and sends the trace session to the Real-Time Trace Viewer running on the host computer. Find the Real-Time Trace Viewer by searching from the Start menu of the host computer. trace host network address The IP address of the host comput

TraceTool Stop Trace and Send

Stops logging data from the application running on the RT target and sends the trace session to the Real-Time Trace Viewer running on the host computer.
 Find the Real-Time Trace Viewer by searching from the Start menu of the host computer.

[IMAGE alt='1378' src='TraceTool_Stop_Trace_and_Send.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cstr.png']

##### trace host network address

The IP address of the host computer where you want to send the trace session.

The Real-Time Trace Viewer must be running on the host computer to receive the trace session.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: no error

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

Unlike most nodes, this node runs normally even if error in contains an error.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Parent topic:

RT Execution TraceTool Nodes

<!--NI_TOPIC bundle=labview-nxg-rt-module-api-ref path=watchdog-timer-clear.html language=enus -->
## TOPIC 00021: Watchdog Timer Clear

- bundle_id: `labview-nxg-rt-module-api-ref`
- source_path: `watchdog-timer-clear.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-api-ref/raw/resource/enus/watchdog-timer-clear.html
- document_id: `labview-nxg-rt-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the watchdog timer object and the associated attributes and actions to the default power-on state and closes the watchdog timer object. A real-time target typically contains only one watchdog timer. If a watchdog timer object is running, you must close the watchdog timer object before you can

Watchdog Timer Clear

Resets the watchdog timer object and the associated attributes and actions to the default power-on state and closes the watchdog timer object.

A real-time target typically contains only one watchdog timer. If a watchdog timer object is running, you must close the watchdog timer object before you can use another one.

[IMAGE alt='1378' src='Watchdog_Timer_Clear.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu64.png']

##### watchdog ID in

ID of the watchdog timer object.

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: no error

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

Unlike most nodes, this node runs normally even if error in contains an error.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

- Incorporating Recovery Procedures in a Real-Time VI

Parent topic:

Real-Time Watchdog Timer Nodes

<!--NI_TOPIC bundle=labview-nxg-rt-module-api-ref path=watchdog-timer-configure.html language=enus -->
## TOPIC 00022: Watchdog Timer Configure

- bundle_id: `labview-nxg-rt-module-api-ref`
- source_path: `watchdog-timer-configure.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-api-ref/raw/resource/enus/watchdog-timer-configure.html
- document_id: `labview-nxg-rt-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures a new watchdog timer object to control a watchdog timer. Configuring a watchdog timer object does not start the watchdog timer. Use the Watchdog Timer Restart node to start the watchdog timer. desired timeout Time in seconds that you want the watchdog timer to wait before it expires. Defa

Watchdog Timer Configure

Configures a new watchdog timer object to control a watchdog timer.

Configuring a watchdog timer object does not start the watchdog timer. Use the Watchdog Timer Restart node to start the watchdog timer.

[IMAGE alt='1378' src='Watchdog_Timer_Configure.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cdbl.png']

##### desired timeout

Time in seconds that you want the watchdog timer to wait before it expires.

Default value: 1 s

##### Setting an Appropriate Timeout

The appropriate range of timeout values depends on the specific performance characteristics and up-time requirements of the embedded application. You must set the timeout long enough so that the watchdog timer does not expire due to acceptable levels of system jitter. However, you must set the timeout short enough so that the system can recover from failure quickly and meet system up-time requirements.

[IMAGE alt='datatype_icon' src='/assets/img/ccclst.png']

##### expiration actions

Actions that the node takes when the watchdog timer expires.

Note

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### restart system

Boolean value that specifies whether to restart the real-time controller when the watchdog timer expires.

| True | Restarts the real-time controller and ignores restart LabVIEW Runtime and trigger occurrence. |
| --- | --- |
| False | Does not restart the real-time controller. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### restart LabVIEW Runtime

Boolean value that specifies whether to restart the current application on the controller when the watchdog timer expires.

| True | Restarts the current application on the controller and ignores trigger occurrence. |
| --- | --- |
| False | Does not restart the current application on the controller. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### trigger occurrence

Boolean value that specifies whether to trigger the occurrence without restarting the real-time controller or the current application on the controller when the watchdog timer expires.

| True | Triggers the occurrence without restarting the real-time controller or the current application on the controller. |
| --- | --- |
| False | Does not trigger the occurrence. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cu64.png']

##### trigger protocol

Protocol used for trigger action on the PXI bus when the watchdog timer expires.

| active high | Sets the trigger action to be active when the line is high. |
| --- | --- |
| active low | Sets the trigger action to be active when the line is low. |
| open collector | Sets the trigger action to operate as an open collector output. |

Default value: active high

[IMAGE alt='datatype_icon' src='/assets/img/cu64.png']

##### trigger line

Trigger line on the PXI bus to be asserted when the watchdog timer expires.

If you specify a trigger line that has been reserved elsewhere, the watchdog timer object overwrites the existing value on the trigger line when the watchdog timer expires.

| none | Does not assert any of the trigger lines when the watchdog timer expires. |
| --- | --- |
| line 0 | Asserts line 0 when the watchdog timer expires. |
| line 1 | Asserts line 1 when the watchdog timer expires. |
| line 2 | Asserts line 2 when the watchdog timer expires. |
| line 3 | Asserts line 3 when the watchdog timer expires. |
| line 4 | Asserts line 4 when the watchdog timer expires. |
| line 5 | Asserts line 5 when the watchdog timer expires. |
| line 6 | Asserts line 6 when the watchdog timer expires. |
| line 7 | Asserts line 7 when the watchdog timer expires. |
| SMB line 0 | Asserts SMB line 0 when the watchdog timer expires. |

Default value: none

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### disable watchdog on VI exit

Boolean value that specifies whether to disable the watchdog timer object when this node stops running.

| True | Disables the watchdog timer object when this node stops running. |
| --- | --- |
| False | Does not disable the watchdog timer object when this node stops running. |

Default value: True

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

##### watchdog ID

ID of the watchdog timer object.

[IMAGE alt='datatype_icon' src='/assets/img/idbl.png']

##### actual timeout

Actual time in seconds that the watchdog timer will wait before it expires.

actual timeout equals desired timeout if the current target supports the value of desired timeout. Otherwise, actual timeout equals the next supported value that is greater than desired timeout.

[IMAGE alt='datatype_icon' src='/assets/img/idvrn.png']

##### occurrence

Occurrence associated with the interrupt action that asserts when the watchdog timer expires.

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

- Incorporating Recovery Procedures in a Real-Time VI

#### Creating Multiple Watchdog Timer Objects

A real-time target typically contains only one watchdog timer. However, you can create multiple watchdog timer objects and use one object at a time. If a watchdog timer object is running, you must use the Watchdog Timer Clear node to close the watchdog timer object before you can use another one.

Use this node to create multiple watchdog timer objects with separate configurations for applications that include distinct states of operation with different timing characteristics. For example, if you implement a state machine architecture with states A and B, you can use a watchdog timer object with a timeout value of 5 seconds in state A and another watchdog timer object with a timeout value of 10 seconds in state B.

Parent topic:

Real-Time Watchdog Timer Nodes

<!--NI_TOPIC bundle=labview-nxg-rt-module-api-ref path=watchdog-timer-restart.html language=enus -->
## TOPIC 00023: Watchdog Timer Restart

- bundle_id: `labview-nxg-rt-module-api-ref`
- source_path: `watchdog-timer-restart.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-api-ref/raw/resource/enus/watchdog-timer-restart.html
- document_id: `labview-nxg-rt-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Restarts the watchdog timer using the values you specify in the Watchdog Timer Configure node. If the countdown of the watchdog timer has not yet started, this node starts the countdown. watchdog ID in ID of the watchdog timer object. restart after expiration Boolean value that specifies whether to

Watchdog Timer Restart

Restarts the watchdog timer using the values you specify in the Watchdog Timer Configure node.

If the countdown of the watchdog timer has not yet started, this node starts the countdown.

[IMAGE alt='1378' src='Watchdog_Timer_Restart.gvi.png']

#### Inputs/Outputs

[IMAGE alt='datatype_icon' src='/assets/img/cu64.png']

##### watchdog ID in

ID of the watchdog timer object.

[IMAGE alt='datatype_icon' src='/assets/img/cbool.png']

##### restart after expiration

Boolean value that specifies whether to restart the watchdog timer if it has expired.

| True | Restarts the watchdog timer if it has expired. |
| --- | --- |
| False | Does not restart the watchdog timer if it has expired. |

Default value: False

[IMAGE alt='datatype_icon' src='/assets/img/cerrcodeclst.png']

##### error in

Error conditions that occur before this node runs.

The node responds to this input according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

Default value: No error

[IMAGE alt='datatype_icon' src='/assets/img/iu64.png']

##### watchdog ID out

ID of the watchdog timer object.

[IMAGE alt='datatype_icon' src='/assets/img/iu16.png']

##### watchdog status

Status of the watchdog timer.

| disabled | The watchdog timer is disabled. |
| --- | --- |
| expired | The watchdog timer has expired. |
| running | The watchdog timer is running. |

[IMAGE alt='datatype_icon' src='/assets/img/ierrcodeclst.png']

##### error out

Error information.

The node produces this output according to standard error behavior.

[Standard Error Behavior](/csh?topicname=LABVIEW-STANDARD-ERROR-BEHAVIOR.HTML)

#### Programming Patterns

- Incorporating Recovery Procedures in a Real-Time VI

Parent topic:

Real-Time Watchdog Timer Nodes
