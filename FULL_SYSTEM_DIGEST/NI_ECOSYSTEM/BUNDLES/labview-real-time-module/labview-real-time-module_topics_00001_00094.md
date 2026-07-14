# NI DOCUMENT BUNDLE: labview-real-time-module

<!--NI_BUNDLE_CHUNK bundle=labview-real-time-module start=1 end=94 -->
<!--NI_TOPIC bundle=labview-real-time-module path=adding-new-entries-to-browser-access-list-of-an-rt-target-real-time-module.html language=enus -->
## TOPIC 00001: Adding New Entries to Browser Access List of an RT Target

- bundle_id: `labview-real-time-module`
- source_path: `adding-new-entries-to-browser-access-list-of-an-rt-target-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/adding-new-entries-to-browser-access-list-of-an-rt-target-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You must enable the Web Server on an RT target and add a computer to the access list of the target to view and control the front panel of a VI running on the target from the computer using LabVIEW. Complete the following steps to add a computer to the access list of an RT target: Right-click an RT t

### Adding New Entries to Browser Access List of an RT Target

You must enable the Web Server on an RT target and add a computer to the access list of the
 target to view and control the front panel of a VI running on the target from the
 computer using LabVIEW.

Complete the following steps to add a computer to the access list of an RT
 target:

1. Right-click an RT target in the Project
 Explorer window and select Properties from the
 shortcut menu to display the RT target Properties dialog box.
2. Click Web Server in the Category 
 list. The Web Server page appears in the right pane.
3. Scroll the page to view the Browser Access section.
4. Click the Add button to add a new entry in the
 Browser Access List .
5. Enter the IP address of the computer to which you want to allow access in the
 Browser Address text box. You can enter a domain
 name, such as mydomain.com , or use wildcard characters in the
 IP address, such as *.164.123.123 to allow access to an entire
 domain. Note If the Web Server runs on an RT target that does
 not have access to a DNS server, do not use domain name entries in the
 Browser Access List.
6. Select Allow Viewing and Controlling , Allow
 Viewing , or Deny Access to set the access
 for the IP address. Two green checkmarks appear to the left of the item when you
 allow viewing and controlling of the front panel, a single green checkmark
 appears when you allow only viewing of the front panel, and a red
 X appears when you deny access. Note If an entry does not
 have one or two green checkmarks or a red X by its name,
 the syntax for the entry is incorrect. Edit the entry or click the
 Remove button to delete the entry.
7. Click the OK button to close the RT target
 Properties dialog box and save the changes.

Parent topic:

Using Remote Front Panels to Access RT Target VIs

Related tasks:

- Enable Remote Front Panel Connections to RT Target VIs

<!--NI_TOPIC bundle=labview-real-time-module path=adding-rt-targets-to-a-labview-project-real-time-module.html language=enus -->
## TOPIC 00002: Adding RT Targets to a LabVIEW Project

- bundle_id: `labview-real-time-module`
- source_path: `adding-rt-targets-to-a-labview-project-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/adding-rt-targets-to-a-labview-project-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You must use a LabVIEW project to work with an RT target. Complete the following steps to add an RT target to a project: Create a project using the Real-Time Project Wizard or the Project Explorer window. Right-click the project root and select New»Targets and Devices from the shortcut menu to displ

### Adding RT Targets to a LabVIEW Project

You must use a LabVIEW
 project to work with an RT target. Complete the following steps to add an
 RT target to a project:

1. Create a project using the Real-Time Project Wizard or the Project Explorer window.
2. Right-click the project root and select New»Targets and
 Devices from the shortcut menu to display the Add Targets and Devices dialog box. If an RT target
 in the project supports other targets, you also can right-click the target and
 select New»Targets and Devices from the shortcut menu to
 add a target under the existing target. For example, if you have an NI FPGA
 target installed in an NI PXI target, you can add the device under the RT
 target.
3. Select the type of RT target you want to add from the Targets and
 Devices section of the Add Targets and
 Devices dialog box. You can select from the following options to
 specify an RT target:
  - Existing target or device —Allows you to display
 all targets and devices on the local subnet or with a specified address.
    - Discover an existing target(s) or
 device(s) —Displays all targets and devices on
 the local subnet.
    - Specify a target or device by IP
 address —Displays supported device types. Select a
 device from the list and enter an IP address for the device to
 add the device to the project.
  - New target or device —Displays targets and devices
 that you can create without a physical target or device present. You
 must change the properties for the target from the General Properties page of the RT target
 Properties dialog box to specify a name and IP address and
 bind it to an existing RT Series device before you attempt to connect to
 or run a VI on the target.
4. Select a target and then click the OK button. An item
 representing the RT target appears in the Project
 Explorer window.

You can add and remove
 items under an RT target.

Parent topic:

Organizing and Managing a LabVIEW Project with the Real-Time Module

Related concepts:

- Creating a LabVIEW Project with the Real-Time Project Wizard
- Creating a LabVIEW Project with the Project Explorer Window
- Configuring RT Target Properties in a LabVIEW Project

<!--NI_TOPIC bundle=labview-real-time-module path=adding-rt-targets-to-a-labview-project.html language=enus -->
## TOPIC 00003: Adding RT Targets to a LabVIEW Project

- bundle_id: `labview-real-time-module`
- source_path: `adding-rt-targets-to-a-labview-project.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/adding-rt-targets-to-a-labview-project.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Add Targets and Devices dialog box to add a target or device to a LabVIEW project. Right-click the project root and select New»Targets and Devices from the shortcut menu to display the Add Targets and Devices dialog box. When you add an RT target to a project, LabVIEW creates an item in the

### Adding RT Targets to a LabVIEW Project

Use the Add Targets and Devices dialog box to add a target or
 device to a LabVIEW project. Right-click the project root and select
 New»Targets and Devices from the shortcut menu to display
 the Add Targets and Devices dialog box. When you add an RT
 target to a project, LabVIEW creates an item in the Project
 Explorer window to represent the RT target. If the RT target you add
 supports other targets, you can right-click the RT target and select
 New»Targets and Devices from the shortcut menu to add a
 target under the existing RT target. For example, if you have an FPGA target
 installed in an RT Series PXI controller, you can add the FPGA target under the RT
 PXI controller.

#### Using Palettes with Multiple RT Targets

LabVIEW loads a separate palette set for each RT target. If you have VIs open on
 multiple RT targets in a project, multiple palette sets exist in memory. When you
 switch between RT targets, LabVIEW attempts to map each pinned palette to its
 counterpart in the active RT target. If a pinned palette does not have a
 counterpart, LabVIEW displays the top-level palette for the active RT target.

Parent topic:

Organizing and Managing a LabVIEW Project with the Real-Time Module

<!--NI_TOPIC bundle=labview-real-time-module path=adhere-to-security-best-practices-real-time-module.html language=enus -->
## TOPIC 00004: Adhere to Security Best Practices

- bundle_id: `labview-real-time-module`
- source_path: `adhere-to-security-best-practices-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/adhere-to-security-best-practices-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can deploy real-time systems to widely varying threat environments. To help reduce the likelihood and impact of realized security threats in your environment, National Instruments offers multiple security options for real-time targets and applications. By understanding which security options app

### Adhere to Security Best Practices

You can deploy real-time systems to widely varying threat environments. To help reduce the
 likelihood and impact of realized security threats
 in your environment, National Instruments offers
 multiple security options for real-time targets
 and applications. By understanding which security
 options apply to your system, you can assess the
 importance of including those options with your
 real-time deployment. Visit
 ni.com/info and enter
 RTSecurity to learn about
 security issues.

Parent topic:

Real-Time Module Best Practices

<!--NI_TOPIC bundle=labview-real-time-module path=avoid-jitter-real-time-module.html language=enus -->
## TOPIC 00005: Avoid Jitter

- bundle_id: `labview-real-time-module`
- source_path: `avoid-jitter-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/avoid-jitter-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Precise timing is essential to the operation of a real-time application. Jitter is a measure of the extent to which execution timing fails to meet deterministic expectations. Use the information in this topic to minimize jitter in your RT application. Avoid Common Sources of Jitter To minimize jitte

### Avoid Jitter

Precise timing is essential to the operation of a real-time application. Jitter is a measure of the extent to which execution


 timing fails to meet deterministic expectations. Use the information in this topic


 to minimize jitter in your RT application.

#### Avoid Common Sources of Jitter

To minimize jitter, avoid including non-deterministic operations in time-sensitive


 loops. Common sources of jitter include:

- Memory allocation —Preallocate arrays before using them in


 deterministic loops, and avoid variable-size data structures in deterministic


 loops. Use the Replace Array


 Subset function to operate on pre-allocated arrays within a


 deterministic loop. Use the Real-Time Trace Viewer to identify Wait


 for Memory 
system


 event flags, which indicate memory management operations.
- Opening and closing references —Open references in an


 initialization phase, before entering a deterministic loop, then close the


 references in a shutdown phase, after the deterministic loop terminates. Opening


 and closing references can impact the determinism of a loop.
- Communication —When communicating with a deterministic


 loop, use either the RT FIFO


 functions or shared variables with the Real-Time FIFO enabled. RT


 FIFOs buffer data so that a deterministic loop can access the data without being


 blocked by a lower-priority loop.
- Shared resources —Avoid accessing shared resources, such as hardware resources, I/O


 channels, or non-reentrant VIs in both a deterministic loop and another loop.


 Contention over shared resources is a common cause of jitter. When a


 deterministic loop uses a hardware resource or non-reentrant VI also used by


 another loop, the deterministic loop might have to wait for the other loop to


 release the shared resource.
- File I/O —Avoid file I/O operations within deterministic


 loops. Hard disk access can introduce unbounded jitter in a deterministic


 loop.
- Asynchronous I/O —Avoid asynchronous I/O operations inside


 a Timed Loop or time-critical VI. LabVIEW polls asynchronous operations to


 determine whether the operation has finished. This polling contributes to jitter


 and can prevent lower-priority tasks from running. Use synchronous operations


 instead. Synchronous operations run to completion, which ensures the read/write


 operation finishes without polling. This distinction is important when using the


 GPIB Read, GPIB Write,


 VISA Read, VISA Write,


 and VISA Wait on Event functions. If you need to use


 these functions inside a Timed Loop or time-critical VI, switch the function to


 Synchronous I/O Mode by right-clicking the function and selecting


 Synchronous I/O Mode»Synchronous from the shortcut


 menu. Other functions also might require this configuration.
- Networking —Avoid networking operations within


 deterministic loops. Networking can introduce unbounded jitter in a


 deterministic loop.
- Unbounded algorithms —Certain algorithms are


 non-deterministic by nature. Do not include unbounded algorithms in a


 deterministic loop. If you are not sure about the jitter characteristics of a VI


 or function, benchmark it.

#### Create a Timing Scheme

To ensure precision timing for ongoing, repetitive loops, establish a consistent


 timing scheme for your application. The timing scheme of a LabVIEW Real-Time Module


 application consists of a loop structure and a timing source. The LabVIEW Real-Time


 Module includes a variety of timing methods and timing sources you can use to


 control the timing of your loops.

#### Select a Loop

In addition to the standard While Loop, LabVIEW


 includes a Timed Loop with built-in timing capabilities. The Timed


 Loop also includes a robust set of inputs and outputs that you can use to alter and


 verify the timing characteristics of your application. The following table


 summarizes the characteristics of these two loop structures:

| Loop Structure | Characteristics | Advantages | Disadvantages |
| --- | --- | --- | --- |
| While Loop | Basic looping structure, multi-threaded | Low CPU overhead | No built-in timing abilities |
| Timed Loop | Single-threaded looping structure designed for multi-rate applications | Built-in timing control, timing data, CPU selection, and priority control; single-threaded to facilitate deterministic scheduling | Slightly more CPU overhead than a While Loop |

#### Select a Timing Source

Whether you use a Timed Loop or a While Loop, select an appropriate timing source to


 drive the iteration timing of the loop.

#### While Loop Timing Sources

To control the timing of a While Loop, place a timing VI or function inside the loop.


 The following table summarizes the built-in timing VIs and functions available with


 the LabVIEW Real-Time Module:

| Use Case | Timing Method | Underlying Timing Source |
| --- | --- | --- |
| Synchronizing a loop with hardware-timed I/O | Hardware-timed I/O methods such as a DAQmx Read VI or a wait method on an FPGA I/O Method Node | External (depends on the hardware platform) |
| Delaying loop execution for x milliseconds | Wait | CPU-derived millisecond or microsecond timer |
| Controlling loop execution rates and synchronize loops | Wait Until Next Multiple | CPU-derived millisecond or microsecond timer |
| Triggering a loop to run after each scan of the NI Scan Engine | Synchronize to Scan Engine | NI Scan Engine |

#### Timed Loop Timing Sources

Refer to the Selecting a Timing Source for a Timed Structure topic for information


 about selecting a Timed Loop timing source.

#### Create a Time Budget

To prevent undesired timing behavior, create a time budget for your application. Time


 budgeting involves determining the amount of time required to execute each loop in


 the application and setting the rates of the loops accordingly. Creating and


 following a time budget helps ensure that your application performs as expected.

#### Measure Loop Execution Times

After separating your application into multiple loops, use RT benchmarking techniques to determine the duration of each loop in


 your application. Allow the benchmark to run for several thousand iterations and


 record the worst-case execution time as the loop duration.

Note

Highlight Execution

#### Create a Time Budgeting Table

After you measure the execution times of your loops, create a time budgeting table


 for the application by recording the duration and period of each loop, as shown in


 the following example:

| Task/Loop | Duration (µS) | Period (µS) |
| --- | --- | --- |
| Control | 400 | 1000 |
| Monitor | 3,000 | 10,000 |
| Log | 16,000 | 30,000 |

#### Keep CPU Usage Low

By targeting a CPU usage well below 100%, you can minimize jitter and ensure that the


 tasks in your application do not need to compete for CPU time. After you construct


 the time budgeting table, you can determine the theoretical CPU usage of the


 application using the following formula.

CPU Usage (%) = 100 * Sum[Loop 1, Loop 2,.., Loop n](Duration /


 Period)

By plugging the numbers from the table into this formula, you can see that the CPU


 usage in this example is 100 * (400/1,000 + 3,000/10,000 + 16,000/30,000) = 123%.


 Because the monitoring loop in this example is set to a higher priority than the


 logging loop, the RTOS schedules the monitoring task immediately after the control


 loop finishes its iteration. The RTOS schedules the logging loop only after the


 monitoring loop finishes an iteration, leaving insufficient time for the logging


 loop to meet the requested period.

In this case, you can increase the period of one or more loops to ensure that each


 loop executes at the requested rate. For example, by increasing the period of the


 monitoring loop to 25,000 µS and increasing the period of the logging loop to 80,000


 µS, the theoretical CPU usage becomes 100 * (400/1,000 + 3,000/25,000 +


 16,000/80,000) = 72%.

Note

Parent topic:

Real-Time Module Best Practices

Related concepts:

- Get the Benchmarking Right
- Minimize CPU Usage

<!--NI_TOPIC bundle=labview-real-time-module path=avoiding-contiguous-memory-conflicts-real-time-module.html language=enus -->
## TOPIC 00006: Avoiding Contiguous Memory Conflicts

- bundle_id: `labview-real-time-module`
- source_path: `avoiding-contiguous-memory-conflicts-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/avoiding-contiguous-memory-conflicts-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabVIEW handles many of the memory details that you normally must account for in a conventional, text-based language. For example, when you add new information to an array or a string, LabVIEW allocates new memory to accommodate the new array or string. When that data is no longer needed, LabVIEW de

### Avoiding Contiguous Memory Conflicts

LabVIEW handles many of the memory details that you normally must account for in a
 conventional, text-based language. For example, when you add new information to an
 array or a string, LabVIEW allocates new memory to accommodate the new array or
 string. When that data is no longer needed, LabVIEW deallocates the associated
 memory. However, keep the following memory considerations in mind when using
 LabVIEW:

- Allocating memory can cause jitter.
- RT targets can run out of memory.
- RT targets can run out of contiguous memory. Contiguous memory is a consecutive
 set of memory addresses assigned to a process. (NI Linux Real-Time) Running out
 of contiguous memory is less likely on NI Linux Real-Time targets because these
 targets have memory management units.

#### Designing Memory-Conscious VIs

NI provides the following recommendations to design memory-conscious VIs for RT
 targets:

- Always preallocate space for arrays equal to the largest array size that you
 might encounter.
- When defining LabVIEW classes for use on RT targets, avoid defining default
 values that require a large amount of memory, such as large arrays or strings.
 Note that when using LabVIEW classes on RT targets, the Request
 Deallocation function can actually allocate memory in certain cases.
 If the default value of the class includes large, variable-size data structures,
 such as large arrays or strings, and the application sets the value of the class
 instance to include smaller arrays or strings, the Request Deallocation function
 allocates memory because the function resets data to the default value of the
 data type.

#### Contiguous Memory Conflict Example

The following illustration shows how failing to preallocate sufficient space for the
 largest array size in your application can lead to a contiguous memory conflict.

[IMAGE alt='image' src='GUID-A302BB2F-98CF-45F7-AA14-21ABE3DD9C25-a5.png']

[IMAGE alt='image' src='GUID-E078C60E-5C4D-49FF-ADA4-05F3744289F7-a5.png']

When you reboot or reset an RT target, the RTOS and the RT Engine load into memory.
 The RT Engine uses available memory for running RT target VIs and storing data.

[IMAGE alt='image' src='GUID-11CF636E-4D2C-4A73-B63D-2BBB61FDDF75-a5.png']

ArrayMaker.vi creates Array 1. All elements in Array 1 must be
 contiguous in memory. The RTOS reserves a contiguous memory space equal to the
 memory used for Array 1.

[IMAGE alt='image' src='GUID-FD1FC3DE-A096-4BDA-BE63-802CF7ED5459-a5.png']

The RTOS reuses the same memory addresses if you stop a VI and then run it again with
 arrays of the same size or smaller. In diagram 3, ArrayMaker.vi
 creates Array 2. The RTOS creates Array 2 in the reserved memory space previously
 occupied by Array 1. Array 2 is small enough to fit in the reserved memory space
 that was allocated to Array 1, so it does not create a contiguous memory conflict.
 The extra contiguous memory used for Array 1 remains in the reserved memory
 space.

[IMAGE alt='image' src='GUID-B5C7BD0F-3D7E-45BA-867B-6DC1D0221ECB-a5.png']

When ArrayMaker.vi runs for a third time with a larger array or if
 another VI generates a larger array, the RT Engine must find a large enough
 contiguous space. In diagram 4, ArrayMaker.vi must create Array 3,
 larger than the previous arrays, in the available memory. Even when
 ArrayMaker.vi stops running, the RT Engine continues to run and
 previously reserved memory is not available. If ArrayMaker.vi runs
 a fourth time and attempts to create an array larger than Array 3, the operation
 fails. There is no contiguous memory area large enough to create the array because
 of the memory fragmentation.

To avoid the contiguous memory conflict in diagram 4, you can preserve memory space
 by preallocating array space equal to the largest use case.

Parent topic:

Optimizing Deterministic Applications

Related concepts:

- Optimizing Deterministic Applications

<!--NI_TOPIC bundle=labview-real-time-module path=avoiding-shared-resources-real-time-module.html language=enus -->
## TOPIC 00007: Avoiding Shared Resources

- bundle_id: `labview-real-time-module`
- source_path: `avoiding-shared-resources-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/avoiding-shared-resources-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: In LabVIEW, there are resources that two or more VIs might need to share. Shared resources can cause jitter and prevent applications from taking advantage of multiple CPUs. Common examples of shared resources include: global variables non-reentrant subVIs The LabVIEW memory manager Queue Operations

### Avoiding Shared Resources

In LabVIEW, there are resources that two or more VIs might need to share. Shared
 resources can cause jitter and prevent applications from taking advantage of
 multiple CPUs. Common examples of shared resources include:

- global variables
- non-reentrant subVIs
- The LabVIEW memory manager
- Queue
 Operations functions
- Semaphore VIs
- Single-threaded DLLs

If a VI uses a shared resource, the VI acquires an operating system mutex around the
 resource to protect the resource from access by other VIs. A
 mutex locks the resource so that other VIs may not access the
 resource. If a time-critical priority VI preempts a lower priority VI and attempts
 to use a locked resource, the deterministic VI must wait because the shared resource
 is not available. The lower priority VI becomes more important than the
 deterministic VI because it must finish its work and release the shared resource
 before the deterministic VI can proceed. This scenario is a priority
 inversion and can affect the determinism of a deterministic VI.

#### Memory Allocations and Preallocating Arrays

When a VI allocates memory, the VI accesses the LabVIEW memory manager. The LabVIEW
 memory manager allocates memory for data storage. The LabVIEW memory manager is a
 shared resource and might be locked by a mutex for up to several milliseconds.
 Allocating memory within a deterministic VI can affect the determinism of the
 VI.

If you are using arrays in deterministic VI control loops, you can reduce jitter by
 preallocating the arrays before entering the loop.

The following block diagram builds an array within a control loop. The Build
 Array function inside the loop uses the LabVIEW memory manager at every
 iteration to allocate memory for the array, which affects the determinism of the
 loop.

[IMAGE alt='image' src='GUID-11CB2DB5-0D7E-405D-AD32-B9016FF34D2C-a5.png']

The following block diagram uses the Initialize
 Array function outside the loop and the Replace Array
 Subset function inside the loop to create the array. Because the array is
 preallocated outside the control loop, the control loop no longer needs to access
 the LabVIEW memory manager at every iteration.

[IMAGE alt='image' src='GUID-957124C0-315E-424D-8F70-F44AD5BAE317-a5.png']

#### Casting Data to Proper Data Types

Cast data to the proper data type in VIs running on the RT target. Every time LabVIEW
 performs a type conversion, LabVIEW makes a copy of the data buffer in memory to
 retain the new data type after the conversion. The LabVIEW memory manager must
 allocate memory for the copy, which might affect the determinism of deterministic
 VIs. Also, creating copies of the data buffer takes up memory resources on an RT
 target.

Use the smallest data type possible when casting data. If you must convert the data
 type of an array, do the conversion before you build the array. Also, keep in mind
 that a function output reuses an input buffer only if the output and the input have
 the same data type. Arrays must have the same structure and number of elements for
 function outputs to reuse the input buffer.

#### Reducing the Use of Global Variables

LabVIEW creates an extra copy in memory of every global variable you use in a VI.
 Reduce the number of global variables to improve the efficiency and performance of
 VIs. Creating copies of global variables takes up memory resources on an RT
 target.

Parent topic:

Optimizing Deterministic Applications

Related concepts:

- Determining When to Use Multiple CPUs
- Optimizing Deterministic Applications
- Optimizing RT Applications for Multiple-CPU Systems
- Using Parallel Operations in Multiple-CPU RT Applications

<!--NI_TOPIC bundle=labview-real-time-module path=avoiding-subvi-overhead-real-time-module.html language=enus -->
## TOPIC 00008: Avoiding SubVI Overhead

- bundle_id: `labview-real-time-module`
- source_path: `avoiding-subvi-overhead-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/avoiding-subvi-overhead-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Calling a subVI from a VI running on an RT target adds a small amount of overhead to the overall application. Although the overhead is small, calling a subVI multiple times in a loop can add a significant amount of overhead. You can embed the loop in the subVI to reduce the overhead. You also can co

### Avoiding SubVI Overhead

Calling a subVI from a VI running on an RT target adds a small amount of overhead to
 the overall application. Although the overhead is small, calling a subVI multiple
 times in a loop can add a significant amount of overhead. You can embed the loop in
 the subVI to reduce the overhead.

You also can convert subVIs into subroutines by changing the VI priority. The LabVIEW execution system minimizes the overhead to call
 subroutines. Subroutines are short, frequently executed tasks that generally do not
 require user interaction. Subroutines cannot display front panel data and do not
 multitask with other VIs.

Parent topic:

Optimizing Deterministic Applications

Related concepts:

- Creating Deterministic Applications Using VIs Set to Different Priorities
- Optimizing Deterministic Applications

<!--NI_TOPIC bundle=labview-real-time-module path=building-and-deploying-a-stand-alone-real-time-application-real-time-module.html language=enus -->
## TOPIC 00009: Building and Deploying a Stand-Alone Real-Time Application

- bundle_id: `labview-real-time-module`
- source_path: `building-and-deploying-a-stand-alone-real-time-application-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/building-and-deploying-a-stand-alone-real-time-application-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to build a stand-alone real-time application and deploy it to an RT target:Before deploying the application, determine which method of deployment best suits your application needs. Open the project you want to use to build the stand-alone real-time application. Right-cli

### Building and Deploying a Stand-Alone Real-Time Application

Complete the following steps to build a
 stand-alone real-time application and deploy it to an RT target:

Note

1. Open the project you want to use to build the stand-alone real-time
 application.
2. Right-click Build Specifications under the RT target and
 select New»Real-Time Application from the shortcut menu
 to display the Real-Time Application Properties dialog box.
3. Complete the following items on the Information page of the Real-Time
 Application Properties dialog box:
  1. Enter a name for the build specification in the Build
 specification name text box. This name appears under
 Build Specifications . The name must be unique
 among other build specification names under the RT target.
  2. Enter a name for the stand-alone real-time application in the
 Target filename text box. Stand-alone
 real-time applications must have a .rtexe 
 extension.
  3. Explore the remaining items on the Application Information page.
4. Complete the following items on the Source Files page:
  1. In the Project Files tree, select the VI you want
 to define as a startup VI, also known as a top-level VI, for the
 stand-alone real-time application. Startup VIs open and run when you
 power on the RT target. You must define at least one VI as a startup VI
 for each stand-alone real-time application you build.
  2. Click the right arrow button next to the Startup
 VIs listbox to move the selected VIs into the
 Startup VIs listbox.
  3. In the Project Files tree, select the items you
 want to define as dynamically called VIs or support files, such as VIs
 you want to call using the VI Server or text files that you read from a
 VI.
  4. Click the right arrow button next to the Always
 Included listbox to move the selected items into the
 Always Included listbox.

Note

Startup VIs

Always
 Included

1. On the Destinations page, configure destination settings and add destination
 directories for the stand-alone real-time application.
2. From the Source File Settings page, edit destinations and properties for
 individual files and folders in the stand-alone real-time application. Note If you plan to
 distribute a stand-alone application that uses shared variables, do not
 include the .lvlib file in an LLB or in the executable.
 Change the Destination of the .lvlib
 file to a destination outside the executable or LLB.
3. On the Advanced page, configure advanced settings for the stand-alone real-time
 application.
4. On the Additional Exclusions page, configure settings to reduce the size of the
 stand-alone real-time application, improve load time, and reduce memory usage
 when you load the resulting build.
5. On the Pre/Post Build Actions page, specify VIs for LabVIEW to execute before or
 after the build.
6. On the Preview page, click the Generate Preview button to
 review the generated files for the stand-alone real-time application. Note Save changes to
 VIs in memory before you create or edit a build specification to ensure that
 the preview is accurate.
7. Deploy the application from the Project Explorer window or outside of the
 LabVIEW development environment. Note If you make
 modifications to your code and want to redeploy your application,
 right-click the build specification and select
 Undeploy from the shortcut menu to remove files
 from earlier deployments. This operation removes all files previously
 deployed to the target, not just the files deployed by the individual build
 specification. To avoid conflicts, use this option to remove deployed files
 from a target before using a different system to transfer files, such as
 installation through SystemLink.

#### Deploying from the Project Explorer
 Window

Complete the following steps to build a stand-alone application and
 deploy that application to an RT target from the Project Explorer window:

1. Use the Real-Time Application Properties dialog box to specify settings for the
 application.
2. Click the Build button. The build specification name
 appears in the project in the Build Specifications tree
 under the RT target in the Project Explorer window, and LabVIEW places the
 application in the directory you specified on the Destinations page of the
 Real-Time Application Properties dialog box.
3. Right-click the build specification and select Set as
 startup from the shortcut menu. Note You can create
 multiple build specifications that configure the settings of stand-alone
 real-time applications under an RT target. However, you can set only one
 stand-alone real-time application as startup for an RT target. When you set
 a build specification as the startup application for an RT target, LabVIEW
 displays a green border around the icon for the build specification in the
 Project Explorer window.
4. Right-click the build specification and select Deploy 
 from the shortcut menu to deploy the application to the RT target.
5. Right-click the RT target and select Utilities»Restart to
 reboot the RT target and run the stand-alone real-time application.

Note

#### Deploying from outside of the LabVIEW
 Development Environment

To deploy a stand-alone real-time application
 without using the LabVIEW IDE, create a package for your RT executable:

1. Build the Real-Time Executable (.rtexe) In your LabVIEW
 project, right-click the RT target and select Build Specifications»New»Real-Time Application. Configure the build settings and build the
 .rtexe file.
2. Create a Package for Deployment In the same project, right-click Build
 Specifications and select New » Package. In the Package Properties
 dialog:Enter a lowercase, no-space package name.
 Under Source Files, include your
 .rtexe and any dependencies.
 Under Destinations, set the install path (for
 example, /home/lvuser/natinst/bin/).
 Configure startup behavior under Advanced if
 needed.
 Set version information under Version
 Info.Note Optionally, you
 can configure a feed for SystemLink or a local
 repository.
3. Build and Deploy the Package Click Build to generate an .ipk
 file in the specified output folder. Use NI Package Manager or SystemLink to
 install the .ipk on the RT target.

For more information about deploying stand-alone real-time applications from
 outside the LabVIEW development environment, refer to Using Application Components
 to Deploy LabVIEW Real-Time Applications, available on ni.com.

Parent topic:

Building, Deploying, and Debugging Deterministic Applications

<!--NI_TOPIC bundle=labview-real-time-module path=building-deploying-and-debugging-deterministic-applications-real-time-module.html language=enus -->
## TOPIC 00010: Building, Deploying, and Debugging Deterministic Applications

- bundle_id: `labview-real-time-module`
- source_path: `building-deploying-and-debugging-deterministic-applications-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/building-deploying-and-debugging-deterministic-applications-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the LabVIEW Application Builder to build a stand-alone real-time application that you can deploy to an RT target from the Project Explorer window or from outside of the LabVIEW development environment. Use the following table to determine which deployment method is appropriate for your applicati

### Building, Deploying, and Debugging Deterministic Applications

Use the LabVIEW Application Builder to
 build a stand-alone real-time application that you can deploy to an RT target from
 the Project Explorer window or from outside of the LabVIEW development environment.
 Use the following table to determine which deployment method is appropriate for your
 application:

Note

| Use Case | Method |
| --- | --- |
| You are developing a stand-alone real-time application that you will deploy to a small number of targets. You do not plan to update the application or its dependencies. | Deploy from the Project Explorer window. |
| You need to deploy a stand-alone real-time application programmatically to one or more targets. | Deploy from outside of the LabVIEW development environment. |
| You are developing a stand-alone real-time application, and you will give that application to someone else to deploy. | Deploy from outside of the LabVIEW development environment. |
| You need to deploy a stand-alone real-time application in an environment where you do not have access to LabVIEW, such as a factory floor. | Deploy from outside of the LabVIEW development environment. |
| You plan to update a stand-alone real-time application in the future to use upgraded versions of its dependencies. For example, the current version of your application uses NI-DAQmx, you plan to upgrade your application to leverage features available in newer versions of NI-DAQmx, and you want to ensure that your application always gets deployed alongside the correct version of NI-DAQmx. | Deploy from outside of the LabVIEW development environment. |

Parent topic:

Real-Time Module How-To

Related concepts:

- Building and Deploying a Stand-Alone Real-Time Application
- Debugging a Stand-Alone Real-Time Application
- Real-Time Tracing

<!--NI_TOPIC bundle=labview-real-time-module path=capturing-trace-sessions-real-time.html language=enus -->
## TOPIC 00011: Capturing Traces

- bundle_id: `labview-real-time-module`
- source_path: `capturing-trace-sessions-real-time.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/capturing-trace-sessions-real-time.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn how to capture trace sessions using Real-Time Tracing VIs on an RT target. Use the Start Trace VI to begin logging and the Stop Trace and Save VI to end logging and save trace data for analysis with KernelShark. KernelShark displays trace sessions that you capture using the Real-Time Tracing V

### Capturing Traces

Learn how to capture trace sessions using Real-Time Tracing VIs on an RT target. Use
 the Start Trace VI to begin logging and the Stop Trace and Save VI to end logging and save
 trace data for analysis with KernelShark.

KernelShark displays trace sessions that you capture using the Real-Time Tracing VIs.
 To start and stop the logging of timing and event data from operating system
 threads, you must add Real-Time Tracing VIs to the block diagram of an application
 running on the RT target.

#### Starting a Trace

Figure 1.

[IMAGE alt='Diagram showing VIs for starting, running, and stopping a serial trace sequence.' src='GUID-32473BA0-0F9A-4096-9A98-1EB8ECA524DD-a5.png']

Buffer Size

#### Stopping a Trace

Use the
 Stop Trace and Save VI to stop logging event data and save the trace to a file on
 the RT target. You can transfer the trace file to the host computer using a standard
 file transfer method like sFTP. You can then view the trace using
 KernelShark.

#### Starting and Stopping a Trace at a
 Specific Location

You can start and stop a trace at the beginning and end
 of an application. However, it might be useful to start and stop a trace in a
 specific location of the application depending on the situation.

- Capturing a single subVI: You can start and stop the trace around a subVI if you
 want to log only the execution of a single VI. The trace captures events from
 other VIs running on the target, but the trace begins before the subVI executes
 and ends immediately after. Note The Start Trace VI captures the events of other VIs that execute
 in parallel if they start executing after the Start Trace VI
 executes.
- Capturing a defined event: You can start logging at the beginning of an
 application and then stop logging when an event occurs. In the following
 example, the Stop Trace and Save VI executes when the Case structure receives a
 TRUE value. The Start Trace VI might overwrite old event data in the memory
 buffer several times during execution, but the trace always retains the most
 recent event data. Figure 2.Stop Condition using
 Stop Trace and Save.vi
 
 
[IMAGE alt='Diagram showing Stop Trace And Save VI in a Case structure.' src='GUID-2D4CF587-31B1-4484-A52E-47FD289564FD-a5.png']
- Capturing a specific time span: You can start and stop the trace in an
 independent VI to log a specific time slice of an application. Add the Wait (ms)
 function with the appropriate time value to the VI and then start the trace
 session. Add another Wait (ms) function with the appropriate time and then stop
 the trace session. For example, the following VI starts and stops a trace to
 capture all events on the RT target that occur during a 10000 ms time span that
 begins 5000 ms after you start the VI. You can start the VI when you start the
 application you want to analyze.

Note

Figure 3.

[IMAGE alt='VI diagram showing Wait, Start Trace, and Stop Trace and Save functions.' src='GUID-87C4F2C9-D069-4FA6-989A-C9B9507D6FA0-a5.png']

Parent topic:

Real-Time Tracing

Related information:

- Tracing on NI Linux Real-Time

<!--NI_TOPIC bundle=labview-real-time-module path=configuring-rt-target-properties-in-a-labview-project-real-time-module.html language=enus -->
## TOPIC 00012: Configuring RT Target Properties in a LabVIEW Project

- bundle_id: `labview-real-time-module`
- source_path: `configuring-rt-target-properties-in-a-labview-project-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/configuring-rt-target-properties-in-a-labview-project-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to configure the project settings of an RT target: Right-click the RT target in the Project Explorer window and select Properties from the shortcut menu to open the RT target Properties dialog box. Select a configuration page from the Category list. From the configuratio

### Configuring RT Target Properties in a LabVIEW Project

Complete the following steps to configure the project settings of an RT target:

1. Right-click the RT target in the Project
 Explorer window and select Properties from the
 shortcut menu to open the RT target Properties dialog box.
2. Select a configuration page from the Category list.
3. From the configuration page, configure the settings for the RT target.
4. Click the OK button to accept the settings and close the
 RT target Properties dialog box.
5. Save the project, by selecting Project»Save Project from
 the Project Explorer window, to save the settings you
 selected for the RT target in the RT target Properties 
 dialog box.You must deploy the RT target before the settings take effect.
 Deploying an RT target refers to applying settings defined in the project to a
 target. Note Deploying an RT target overwrites the current target
 settings with the latest settings specified in the RT target
 Properties dialog box.
6. Right-click the RT target and select Deploy from the
 shortcut menu to deploy the settings to the target.

Parent topic:

Organizing and Managing a LabVIEW Project with the Real-Time Module

<!--NI_TOPIC bundle=labview-real-time-module path=creating-a-labview-project-with-the-project-explorer-window-real-time-module.html language=enus -->
## TOPIC 00013: Creating a LabVIEW Project with the Project Explorer Window

- bundle_id: `labview-real-time-module`
- source_path: `creating-a-labview-project-with-the-project-explorer-window-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/creating-a-labview-project-with-the-project-explorer-window-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You must use a project to work with an RT target. Use projects to group together LabVIEW files and files not specific to LabVIEW, create build specifications, and deploy or download files to RT targets. Complete the following steps to create a project manually: Select File»New Project to display the

### Creating a LabVIEW Project with the Project Explorer Window

You must use a project to work with an RT target. Use projects to group together LabVIEW files and files not specific to
 LabVIEW, create build specifications, and deploy or download files to RT
 targets.

Complete the following steps to create a project manually:

1. Select File»New Project to display the Project
 Explorer window. You also can select Project»New
 Project or select Empty Project in the
 New dialog box to display the Project
 Explorer window.
2. Add an RT target to the project.
3. Add items you want to include in the project under
 an RT target.
4. Select File»Save Project to save the
 project.

You also can interactively create projects using the RT Project Wizard.

Parent topic:

Organizing and Managing a LabVIEW Project with the Real-Time Module

Related concepts:

- Adding RT Targets to a LabVIEW Project
- Creating a LabVIEW Project with the Real-Time Project Wizard

<!--NI_TOPIC bundle=labview-real-time-module path=creating-a-labview-project-with-the-real-time-project-wizard-real-time-module.html language=enus -->
## TOPIC 00014: Creating a LabVIEW Project with the Real-Time Project Wizard

- bundle_id: `labview-real-time-module`
- source_path: `creating-a-labview-project-with-the-real-time-project-wizard-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/creating-a-labview-project-with-the-real-time-project-wizard-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Real-Time Project Wizard to create a new project, configure project settings, define RT targets, and include VIs and other application files. Creating a New Project Complete the following steps to create a project with the Real-Time Project Wizard: Select Tools»Real-Time Module»Project Wizar

### Creating a LabVIEW Project with the Real-Time Project Wizard

Use the Real-Time Project Wizard to create a new project, configure project settings,
 define RT targets, and include VIs and other application files.

#### Creating a New Project

Complete the following steps to create a project with the Real-Time Project
 Wizard:

1. Select Tools»Real-Time Module»Project Wizard to launch
 the Real-Time Project Wizard. You also can click Real-Time
 Project in the New section of the Getting Started window to launch the Real-Time
 Project Wizard.
2. Select the type of project you want to create from the Project
 type pull-down menu of the Select project type, name,
 and folder page. Tip You can create projects
 with the Real-Time Project Wizard using one of three architectures—continuous
 communication, state machine, or custom. If you select Continuous
 communication architecture, enable Application
 includes deterministic components if you require
 deterministic performance for time-critical tasks.
3. Enter a name for the new project in the Project name text
 box and enter the directory in which you want to save the project in the
 Project folder text box.
4. Click the Next button to accept the settings and
 continue.

#### Configuring Project Settings

The Real-Time Project Wizard offers different settings according to the type of
 project architecture you select. Complete the steps for the project architecture you
 selected.

Continuous Communication

Customize architecture options

1. Select the number of Timed Loops you require from the Target
 Configuration section. Note If you want to create
 an application that includes deterministic behavior and file I/O on the RT
 target, you must select Two Loops.
2. Enable Include file I/O if you want to create an
 application that logs data to disk on the RT target.
3. Enable Include user interface and then select the type of
 user interface from the Host Configuration section to
 create an application that provides a user interface on the host computer.
4. Click the Next button to accept the settings and
 continue.

State Machine—The state machine architecture does not require
 extra configuration. Click the Next button to continue.

Custom

Add top-level VIs

1. Choose to add a blank VI or import existing VIs to the project.

- Select Add blank VI to target to add a blank VI that runs
 on the RT target. Skip to step 4.
- Select Import existing VIs to host and target to import
 existing VIs that run on the target or host computer.

1. Click the Add VIs button under the VIs
 imported to run on host listbox to add VIs that run on the host
 computer.
2. Click the Add VIs button under the VIs
 imported to run on target listbox to add VIs that run on the RT
 target.
3. Click the Next button to accept the settings and
 continue.

#### Selecting an RT Target for the Project

Complete the following steps to add an RT target to the project:

1. Click the Browse button on the Browse
 targets page to select a target you want to add to the project
 and on which to run the target VIs. The Real-Time Project Wizard displays the
 name of the target you select in the Selected target text
 box.
2. Click the Next button to accept the settings and
 continue.

#### Generating the Project

Complete the following steps to generate the project:

1. Review the new project configuration on the Preview
 project page.
2. Disable Open VIs when finished if you do not want to open
 the VIs that the Real-Time Project Wizard creates.
3. Click the Finish button to accept the settings and
 generate the new project.

Parent topic:

Organizing and Managing a LabVIEW Project with the Real-Time Module

<!--NI_TOPIC bundle=labview-real-time-module path=creating-a-shared-variable-with-real-time-fifo-real-time-module.html language=enus -->
## TOPIC 00015: Creating a Shared Variable with Real-Time FIFO

- bundle_id: `labview-real-time-module`
- source_path: `creating-a-shared-variable-with-real-time-fifo-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/creating-a-shared-variable-with-real-time-fifo-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can create a shared variable and enable the real-time FIFO to deterministically share data locally on an RT target or across a network with VIs on another target. However, RT FIFOs do not support data types of variable size, such as clusters, strings, and variants. Complete the following steps t

### Creating a Shared Variable with Real-Time
 FIFO

You can create a shared
 variable and enable the real-time
 FIFO to deterministically share data locally on an RT target or across a
 network with VIs on another target. However, RT FIFOs do not support data types of
 variable size, such as clusters, strings, and variants.

Complete the following steps to create a shared variable and enable the real-time
 FIFO:

1. Right-click the RT target on which you want to create the shared variable and
 select New»Variable from the shortcut menu to open the
 Shared Variable Properties dialog box.
2. Enter a name for the variable in the Name text box.
3. Select the data type for the variable from the Data Type 
 pull-down menu.
4. Select Single-Process or
 Network-Published from the Variable
 Type pull-down menu.
5. Click Real-Time FIFO in the
 Category list to open the Real-Time
 FIFO page.
6. Place a checkmark in the Enable Real-Time FIFO 
 checkbox.
7. Select Single element or
 Multi-element to create a FIFO buffer with a single
 element or a FIFO buffer with multiple elements.
8. If you select Single element , configure the size for the
 array elements or the size of the waveform for the FIFO element if you select an
 array or waveform data type.If you select Multi-element ,
 configure the size and the elements of the FIFO buffer to match the settings
 from the Use Buffering section of the Network page, or you can configure a custom size for the FIFO and
 the FIFO elements.
9. Click the OK button.

Parent topic:

Sharing Data in Deterministic Applications

<!--NI_TOPIC bundle=labview-real-time-module path=creating-an-appropriate-memory-buffer-real-time.html language=enus -->
## TOPIC 00016: Creating an Appropriate Memory Buffer

- bundle_id: `labview-real-time-module`
- source_path: `creating-an-appropriate-memory-buffer-real-time.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/creating-an-appropriate-memory-buffer-real-time.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn how to set the Buffer Size input of the Start Trace VI to allocate an appropriately sized memory buffer on the RT target. This ensures all event data is captured without loss, as the buffer overwrites the oldest data when full. The Buffer Size input of the Start Trace VI sets the size of the m

### Creating an Appropriate Memory
 Buffer

Learn how to set the Buffer Size input of the Start Trace VI to allocate an
 appropriately sized memory buffer on the RT target. This ensures all event data is captured
 without loss, as the buffer overwrites the oldest data when full.

The Buffer Size input of the Start Trace VI sets the size of
 the memory buffer that stores thread events. The Start Trace VI allocates a memory
 space for the buffer.

To capture all event data, you must create an appropriately sized memory buffer. When
 the buffer fills, the Start Trace VI overwrites the least recent event data with the
 most recent event data.

If you reach the memory buffer limit, the Start Trace VI overwrites the oldest data
 in the buffer. Therefore, the trace session always contains the latest event data.
 You can improve the efficiency of the memory buffer by increasing its size. The
 default memory buffer size is 1410 KB. Use the Buffer
 Size input of the Start Trace VI to set the buffer size equal to the largest
 contiguous block of memory available on the RT target.

Parent topic:

Capturing Traces

<!--NI_TOPIC bundle=labview-real-time-module path=creating-and-editing-labview-projects-with-the-project-explorer-window-real-time-module.html language=enus -->
## TOPIC 00017: Creating and Editing LabVIEW Projects with the Project Explorer Window

- bundle_id: `labview-real-time-module`
- source_path: `creating-and-editing-labview-projects-with-the-project-explorer-window-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/creating-and-editing-labview-projects-with-the-project-explorer-window-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Project Explorer window to create and edit LabVIEW projects. Select File»New Project to display the Project Explorer window. You also can select Project»New Project or select Empty Project in the New dialog box to display the Project Explorer window. The Project Explorer window enables you t

### Creating and Editing LabVIEW Projects with the
 Project Explorer Window

Use the Project Explorer window to create and edit LabVIEW
 projects. Select File»New Project to display the
 Project Explorer window. You also can select
 Project»New Project or select Empty
 Project in the New dialog box to display the
 Project Explorer window.

The Project Explorer window enables you to manage the targets,
 VIs, and other support files of a project from one location. Use the
 Project Explorer window to connect to RT targets, set
 target properties, and deploy VIs to targets. When you add an RT target, the
 Project Explorer window includes the following
 sections:

- Project root —Contains the host computer and the RT
 targets you add to the current project. The label on the project root includes
 the filename for the project. Right-click the project root and select
 New»Targets and Devices from the shortcut menu to add
 an RT target to the project.
  - My
 Computer —Represents the local, or host computer, as a target
 in the project.
  - RT Target —Represents the
 RT targets you add to the project. By default, the heading for an RT
 target is the name of the target as specified in NI Measurement &
 Automation Explorer (MAX). VIs and libraries that you add to an RT
 target appear under the target in the Project
 Explorer window. Right-click an RT target and select
 Properties from the shortcut menu to configure the settings of the target.
    - Dependencies —Includes items
 that VIs under a target
 require.
    - Build
 Specifications —Includes specifications for
 building source distributions, stand-alone real-time
 applications, and zip files. If you have the LabVIEW
 Professional Development System or the Application Builder
 installed, right-click Build
 Specifications and select
 New»Real-Time Application from the
 shortcut menu to create a build specification that defines how
 you want to build stand-alone real-time applications.

Parent topic:

Organizing and Managing a LabVIEW Project with the Real-Time Module

Related concepts:

- Using LabVIEW Projects with the Real-Time Module

<!--NI_TOPIC bundle=labview-real-time-module path=creating-deterministic-applications-real-time-module.html language=enus -->
## TOPIC 00018: Creating Deterministic Applications

- bundle_id: `labview-real-time-module`
- source_path: `creating-deterministic-applications-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/creating-deterministic-applications-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Determinism is the characteristic of a system that describes how consistently the system responds to external events or performs operations within a given time limit. Jitter is a measure of the extent to which execution timing fails to meet deterministic expectations. Most real-time applications req

### Creating Deterministic Applications

Determinism is the characteristic of a system that describes how consistently the
 system responds to external events or performs operations within a given time limit.
 Jitter is a measure of the extent to which execution timing fails to meet
 deterministic expectations. Most real-time applications require timing behavior to
 consistently execute within a small window of acceptable jitter, as shown in the
 following illustration:

[IMAGE alt='image' src='GUID-2AB441CD-703D-4CD8-9689-973FA4E55BE5-a5.png']

If you intend to build deterministic applications to execute deterministic tasks, use
 the programming techniques in this section to reduce jitter in VIs running on RT
 targets.

Note

Parent topic:

Real-Time Module Concepts

Related concepts:

- Real-Time Tracing

<!--NI_TOPIC bundle=labview-real-time-module path=creating-deterministic-applications-using-the-timed-loop-real-time-module.html language=enus -->
## TOPIC 00019: Creating Deterministic Applications Using the Timed Loop

- bundle_id: `labview-real-time-module`
- source_path: `creating-deterministic-applications-using-the-timed-loop-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/creating-deterministic-applications-using-the-timed-loop-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Separate deterministic tasks from non-deterministic tasks and place them in different loops in an RT target VI to ensure the deterministic tasks receive enough processor resources. A Timed Loop executes a subdiagram each iteration of the loop at the period and priority you specify. The higher the pr

### Creating Deterministic Applications Using the
 Timed Loop

Separate deterministic tasks from non-deterministic tasks and place them in
 different loops in an RT target VI to ensure the deterministic tasks receive enough
 processor resources. A Timed Loop executes a subdiagram each iteration of the
 loop at the period and priority you specify. The higher the priority of a Timed
 Loop, the greater priority the structure has relative to other timed structures on the block diagram. Use deterministic
 communication methods to share data locally from the deterministic Timed Loop or to share data remotely across a network.

Note

The following block diagram shows an RT target VI that contains a Timed Loop and a
 While Loop to control a data acquisition and logging application:

[IMAGE alt='image' src='GUID-B0873D51-63E8-4A3C-867A-50C6A236E9E7-a5.png']

The deterministic loop set to a priority of 100 contains a subVI that performs a data
 acquisition task every iteration of the loop. The deterministic loop shares the
 acquired data with the non-deterministic loop using a shared variable,
 data. Shared variables with the real-time FIFO enabled
 can share data deterministically from a VI running on an RT target without
 affecting the determinism of the VI. The non-deterministic loop logs the acquired
 data that it reads from the shared variable data to disk on
 the RT target.

#### Cooperatively Yielding Timed Loop Execution

Because of the preemptive nature of Timed Loops, they can monopolize processor
 resources. A Timed Loop might use all of the processor resources, not allowing lower
 priority tasks on the block diagram to execute.

You must configure a deterministic Timed Loop with a period large enough to perform
 the deterministic task and still have idle time during the iteration to allow lower
 priority tasks to execute. By timing Timed Loops, you can yield the execution of deterministic tasks
 and cooperatively relinquish processor resources to lower priority tasks on the
 block diagram.

Note

Parent topic:

Creating Deterministic Applications

Related concepts:

- Sharing Data Locally on an RT Target
- Sharing Data Remotely across a Network
- Sharing Data Using Shared Variables
- Timing Deterministic Applications
- Optimizing RT Applications for Multiple-CPU Systems
- Creating Deterministic Applications with the Real-Time Module

<!--NI_TOPIC bundle=labview-real-time-module path=creating-deterministic-applications-using-vis-set-to-different-priorities-real-time-module.html language=enus -->
## TOPIC 00020: Creating Deterministic Applications Using VIs Set to Different Priorities

- bundle_id: `labview-real-time-module`
- source_path: `creating-deterministic-applications-using-vis-set-to-different-priorities-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/creating-deterministic-applications-using-vis-set-to-different-priorities-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Separate deterministic tasks from non-deterministic tasks and place deterministic tasks in different VIs to ensure they receive enough processor resources. You can prioritize the VIs and then categorize them into one of the available execution systems to control the amount of processor resources eac

### Creating Deterministic Applications Using VIs
 Set to Different Priorities

Separate deterministic tasks from non-deterministic tasks and place deterministic
 tasks in different VIs to ensure they receive enough processor resources. You can
 prioritize the VIs and then categorize them into one of the available execution
 systems to control the amount of processor resources each VI receives.

LabVIEW assigns each VI to an execution system thread according to the VI priority
 and execution system you specify. The threads execute on the processor
 accordingly.

#### Assigning Priorities to VIs

You can change the priority of a VI by right-clicking the VI in the Project Explorer window and selecting
 Properties from the shortcut menu to open the VI Properties dialog box. Select
 Execution from the Category
 pull-down menu in the VI Properties dialog box to open the
 Execution page where you can set the priority of a VI. You can select
 from the following VI priorities, listed in order from lowest to highest, to assign
 VIs a priority level:

- background priority (lowest)
- normal priority (default)
- above normal priority
- high priority
- time-critical priority (highest)

Caution

Normal priority is the default priority for all VIs you create in LabVIEW. However,
 subVIs inherit the priority of the caller VI. For example, a subVI called in a
 deterministic VI runs at time-critical priority. The time-critical priority preempts
 all other priorities. A time-critical priority VI does not relinquish processor
 resources until it completes all tasks. However, a deterministic VI can explicitly
 relinquish control of processor resources to ensure that the VI does not monopolize
 the processor resources.

Note

In addition to the five priority levels listed above, you can set VIs to subroutine
 priority. VIs set for subroutine priority do not share execution time with other
 VIs. When a VI runs at the subroutine priority level, it effectively takes control
 of the thread in which it is running, and it runs in the same thread as its caller.
 No other VI can run in that thread until the subroutine VI finishes running, even if
 the other VI is at the subroutine priority level.

#### Assigning VIs to an Execution System

You can change the execution system of a VI by right-clicking the VI in the
 Project Explorer window and selecting
 Properties from the shortcut menu to open the VI Properties dialog box. Select
 Execution from the Category
 pull-down menu in the VI Properties dialog box to open the
 Execution page where you can set the execution system of a VI. LabVIEW
 has the following six execution systems to help you categorize VIs:

- user interface
- standard
- instrument I/O
- data acquisition
- other 1
- other 2

By default, all VIs run in the standard execution system, but you can assign VIs to
 other execution systems. In addition to the six execution systems, you also can
 assign subVIs to the same as caller execution system. The same as
 caller execution system runs subVIs in the same execution system as the top-level VI
 that called the subVI.

Every execution system except user interface has a thread queue to execute VIs at the
 priority you specify. For example, if you have three VIs assigned to an execution
 system, at any time, one VI might run as the other two wait in the queue. Assuming
 all VIs have the same priority, one thread runs for a certain amount of time. The
 thread then moves to the end of the queue, and the next thread runs. When a thread
 completes, the execution system removes the thread from the queue.

The user interface execution system handles all user interface tasks. The other
 execution systems are not responsible for managing the user interface. If a VI needs
 to update the user interface, the execution system passes the task responsibility to
 the user interface execution system, which updates the user interface.

#### Cooperatively Yielding Deterministic VI Execution

Because of the preemptive nature of deterministic VIs, they can monopolize processor
 resources. A deterministic VI might use all of the processor resources, not allowing
 lower priority tasks, such as lower priority VIs and the FTP server of an RT target,
 to execute.

You must build deterministic VIs that periodically yield to allow lower priority
 tasks to execute without affecting the determinism of the deterministic code. By
 timing a deterministic VI, you can ensure the VI will cooperatively
 relinquish processor resources.

Note

Parent topic:

Creating Deterministic Applications

Related concepts:

- Avoiding SubVI Overhead
- Timing Deterministic Applications
- Optimizing RT Applications for Multiple-CPU Systems
- Creating Deterministic Applications with the Real-Time Module
- Sharing Data Locally on an RT Target

<!--NI_TOPIC bundle=labview-real-time-module path=creating-deterministic-applications-with-the-real-time-module-real-time-module.html language=enus -->
## TOPIC 00021: Creating Deterministic Applications with the Real-Time Module

- bundle_id: `labview-real-time-module`
- source_path: `creating-deterministic-applications-with-the-real-time-module-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/creating-deterministic-applications-with-the-real-time-module-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Deterministic applications benefit from multithreading and from the priority-based scheduling model of the real-time operating system (RTOS). When creating deterministic applications, divide and separate application tasks to create multithreaded applications that receive dedicated processor resource

### Creating Deterministic Applications with the
 Real-Time Module

Deterministic applications benefit from multithreading and from the priority-based
 scheduling model of the real-time operating system (RTOS). When creating
 deterministic applications, divide and separate application tasks to create
 multithreaded applications that receive dedicated processor resources based on the
 priorities set by the RTOS.

#### Multithreading

Single-CPU computers achieve multitasking by running one application for a short
 amount of time and then running other applications for short amounts of time. As
 long as the amount of processor time allocated for each application is small enough,
 computers appear to have multiple applications running simultaneously. Systems with
 multiple CPUs, on the other hand, can achieve true parallelism.

Multithreading applies the concept of multitasking to a single application by
 breaking it into smaller tasks that execute for short amounts of time in different
 execution system threads. A thread is a completely independent
 flow of execution for an application within the execution system. Multithreaded
 applications maximize the efficiency of the processor because the processor does not
 sit idle if there are other threads ready to run. An application that reads from and
 writes to a file, performs I/O, or polls the user interface for activity can benefit
 from multithreading because it can use the processor to run other tasks during
 breaks in these activities.

#### Priority-based Scheduling
 Model

The RTOS on RT targets uses a combination of round robin and preemptive scheduling to
 execute threads in the execution system.

Round robin scheduling—Applies to threads of equal priority.
 Equal shares of processor time are allocated among equal priority threads. For
 example, each normal priority thread is allotted 10 ms to run. The processor
 executes all the tasks it can in 10 ms and any remaining tasks at the end of that
 period must wait to complete during the next allocation of time.

Preemptive scheduling—Higher priority threads execute
 immediately while lower priority threads pause execution. A time-critical priority
 thread is the highest priority and preempts all priorities.

#### Priority of Timed
 Structures

LabVIEW executes timed structures threads below time-critical priority and above high
 priority. You can specify the priority level of Timed Loops relative to other timed
 structures within a VI by setting the priority of the Timed Loop. Use the Configure
 Timed Loop Dialog Box to configure a timing source, period, priority, and other
 advanced options for the execution of the Timed Loop.

#### Dividing Tasks to Create
 Deterministic Multithreaded Applications

Deterministic applications depend on deterministic tasks to complete on time, every
 time. Therefore, deterministic tasks need dedicated processor resources to ensure
 timely completion. Dividing tasks helps to ensure that each task receives the
 processor resources it needs to execute on time.

Separate deterministic tasks from all other tasks to ensure deterministic tasks
 receive enough processor resources. For example, if a control application acquires
 data at regular intervals and stores the data on disk, you must handle the timing
 and control of the data acquisition deterministically. However, storing the data on
 disk is inherently a non-deterministic task because file I/O operations have
 unpredictable response times that depend on the hardware and the availability of the
 hardware resource. You can use Timed Loops or VIs with different priorities to
 control the execution and timing of deterministic tasks.

Note

Parent topic:

Creating Deterministic Applications

Related concepts:

- Creating Deterministic Applications Using the Timed Loop
- Creating Deterministic Applications Using VIs Set to Different Priorities
- Optimizing RT Applications for Multiple-CPU Systems
- Introduction to the LabVIEW Real-Time Module
- Real-Time System Components
- Timing Deterministic Applications

<!--NI_TOPIC bundle=labview-real-time-module path=creating-labview-projects-with-the-real-time-project-wizard-real-time-module.html language=enus -->
## TOPIC 00022: Creating LabVIEW Projects with the Real-Time Project Wizard

- bundle_id: `labview-real-time-module`
- source_path: `creating-labview-projects-with-the-real-time-project-wizard-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/creating-labview-projects-with-the-real-time-project-wizard-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Real-Time Project Wizard to create a new project that defines RT targets and includes VIs and other application files. You can create projects with the Real-Time Project Wizard using one of three architectures—continuous communication, state machine, or custom. Continuous Communication Archi

### Creating LabVIEW Projects with the Real-Time Project Wizard

Use the Real-Time Project Wizard to create a new project that defines RT targets and
 includes VIs and other application files. You can create projects with the Real-Time Project Wizard using one of three
 architectures—continuous communication, state machine, or custom.

#### Continuous Communication Architecture

Use a continuous communication architecture to create data acquisition applications
 that can log data to disk and continuously communicate with a host computer to
 provide a user interface.

With the continuous communication architecture, you can select an application
 configuration that uses one or two Timed Loops in the RT target VI.

- One loop—The RT target VI uses a Timed Loop to control the timing and execution
 of the application tasks.
- Two loops—The RT target VI uses two Timed Loops running at different priorities
 to control the timing and execution of the application tasks. The higher
 priority Timed Loop controls the deterministic tasks. The lower priority Timed
 Loop controls user interface communication and file I/O tasks.

You can provide a user interface for the real-time application using a VI running on
 the host computer or using a LabVIEW remote front panel to connect to the RT target
 VI.

- Host VI—Uses LabVIEW shared variables to send user interface data out of the RT
 target VI. A VI that runs on the host computer accesses the user interface data
 and displays the data on a front panel.
- Remote Panel—Uses a LabVIEW remote front panel to view the front panel controls
 and indicators of the RT target VI. You cannot use remote front panels with a
 single Timed Loop configuration if the application requires determinism. The
 Real-Time Project Wizard creates an HTML file that you can publish using the Web Server of the RT target. You
 can use this HTML file to access the front panel of an RT target VI from the
 host computer.

#### State Machine Architecture

Use a state machine architecture to implement complex decision-making algorithms
 represented by state diagrams or flow charts. The state machine architecture can
 implement any algorithm described by a Moore machine. For each state in a state
 diagram, a Moore machine performs a specific action that runs for a finite amount of
 time. To prevent data loss, the time to execute each action must be short enough to
 keep all acquired data in memory on the target. The RT target also must be able to
 send all the data back to the host computer in one package. The state machine
 architecture separates communication and non-deterministic tasks from deterministic
 tasks and executes them before and after deterministic tasks.

The Real-Time Project Wizard generates an RT target VI that uses a Case structure to define the states of the state diagram. The Real-Time
 Project Wizard also generates a VI that runs on the host computer to provide a user
 interface, which you can use to select the state to execute on the RT target. The
 host VI uses shared variables to trigger the execution of a particular state on the
 RT target. The RT target VI executes the subdiagram for the state you select and
 returns the results to the host VI.

Note

#### Custom Project

Use a custom project architecture to add a blank VI or import existing VIs to run on
 the host computer or RT target.

Parent topic:

Organizing and Managing a LabVIEW Project with the Real-Time Module

<!--NI_TOPIC bundle=labview-real-time-module path=creating-stand-alone-real-time-applications-real-time-module.html language=enus -->
## TOPIC 00023: Creating Stand-Alone Real-Time Applications

- bundle_id: `labview-real-time-module`
- source_path: `creating-stand-alone-real-time-applications-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/creating-stand-alone-real-time-applications-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the LabVIEW Application Builder to build a stand-alone real-time application that runs automatically when you power on an RT target. You can deploy a stand-alone real-time application from the Project Explorer window or from outside of the LabVIEW development environment, depending on your appli

### Creating Stand-Alone Real-Time Applications

Use the LabVIEW Application Builder to build a
 stand-alone real-time application that runs automatically when you power
 on an RT target. You can deploy a
 stand-alone real-time application from the Project
 Explorer window or from outside of the LabVIEW development environment,
 depending on your application needs.

Note

Parent topic:

Real-Time Module Concepts

<!--NI_TOPIC bundle=labview-real-time-module path=customizing-how-front-panels-display-on-the-embedded-ui-real-time-module.html language=enus -->
## TOPIC 00024: Customizing How Front Panels Display on the Embedded UI

- bundle_id: `labview-real-time-module`
- source_path: `customizing-how-front-panels-display-on-the-embedded-ui-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/customizing-how-front-panels-display-on-the-embedded-ui-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: For some applications, it may be convenient to customize how front panels display on the embedded UI. These customizations are useful if you want to create an end user experience that focuses only on the front panel and its functionality. For example, you may want to display the front panel full-scr

### Customizing How Front Panels Display on the Embedded UI

For some applications, it may be convenient to customize how front panels display on
 the embedded UI. These customizations are useful if you want to create an end user
 experience that focuses only on the front panel and its functionality. For example,
 you may want to display the front panel full-screen to hide the desktop, remove
 unwanted LabVIEW objects such as title bars and menus from the screen, or prevent
 end users from switching away from the front panel.

#### Setting a Front Panel to Display Full-Screen

Complete the following steps to display front panels full-screen on the embedded UI,
 so they match the resolution of the display device connected to the RT target:

1. In LabVIEW, select File»VI Properties to open the
 VI Properties dialog box.
2. Select Window Size from the Category pull-down menu.
3. Specify Width and Height to match
 the screen resolution of the display device connected to the RT target.
4. Select Window Run-Time Position from the
 Category pull-down menu.
5. Select Centered from the Position pull-down menu.
6. Disable the Use Current Panel Size checkbox and specify
 Width and Height to match the
 screen resolution of the display device connected to the RT target.
7. Click OK to save your changes.

When you run and view the VI on the RT target, the front panel matches the resolution
 of the display device.

#### Removing LabVIEW Objects from the Front Panel

Complete the following steps to remove unwanted LabVIEW objects, such as title bars
 and menus, from the front panel of a VI:

1. In LabVIEW, select File»VI Properties to open the
 VI Properties dialog box.
2. Select Window Appearance from the Category pull-down menu.
3. Enable the Custom button, and then click
 Customize to open the Customize Window
 Appearance dialog box.
4. Specify the options you want to remove from the front panel based on your
 application needs.
5. Click OK to close the Customize Window
 Appearance dialog box.
6. Click OK to save your changes.

When you run and view the VI on the RT target, the front panel displays a custom set
 of objects.

#### Removing Embedded UI Elements from Displaying

Complete the following steps to remove unwanted embedded UI elements from displaying.
 Examples of embedded UI elements include desktop icons that open the Xfce file
 manager, terminal emulator, and display settings.

1. Place a System Exec VI on the block diagram of the RT target VI, outside of
 time-critical loops.
2. Specify the System Exec VI to run the following command:
 hidepanel

When you run and view the VI on the RT target, Xfce elements do not display on
 screen.

Tip

wait until
 completion?

showpanel

Parent topic:

Using the Embedded UI to Access RT Target VIs

Related concepts:

- Enabling the Embedded UI on RT Targets
- Viewing and Controlling the Front Panels of RT Target VIs Using the Embedded UI

<!--NI_TOPIC bundle=labview-real-time-module path=debugging-a-stand-alone-real-time-application-real-time-module.html language=enus -->
## TOPIC 00025: Debugging a Stand-Alone Real-Time Application

- bundle_id: `labview-real-time-module`
- source_path: `debugging-a-stand-alone-real-time-application-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/debugging-a-stand-alone-real-time-application-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can debug stand-alone real-time applications that you create with the LabVIEW Application Builder from a remote host computer. Complete the following steps to debug a stand-alone real-time application: Enable debugging in the build specification for the stand-alone real-time application by placi

### Debugging a Stand-Alone Real-Time Application

You can debug stand-alone real-time applications that you create with the LabVIEW
 Application Builder from a remote host computer.

Complete the following steps to debug a stand-alone real-time application:

1. Enable debugging in the build specification for the stand-alone real-time application by
 placing a checkmark in the Enable debugging checkbox on
 the Advanced page of the Real-Time
 Application Properties dialog box.
2. Right-click the build specification for the stand-alone real-time application
 and select Build from the shortcut menu to build the
 application.
3. Reboot the RT target to run the stand-alone real-time application.
4. From the Project Explorer window, select
 Operate»Debug Application or Shared Library to
 display the Debug Application or Shared Library dialog box.
5. Enter the IP address of the RT target in the Machine name or IP
 address text box. Click the Refresh 
 button to view the list of stand-alone real-time applications that you can debug
 on the RT target.
6. Select the stand-alone real-time application you want to debug.
7. Click the Connect button to open the front panel window
 of the startup VI for debugging. Use the block diagram of the startup VI to
 debug the application using probes, breakpoints,
 and other debugging techniques.
8. After you finish debugging, close the startup VI, which also closes the
 stand-alone real-time application on the RT target and then reboot the RT target
 to restart the stand-alone real-time application. If you want to disconnect
 without closing the startup VI, right-click the front panel window of the
 startup VI and select Remote Debugging»Quit Debug Session 
 from the shortcut menu.

Parent topic:

Building, Deploying, and Debugging Deterministic Applications

Related concepts:

- Building and Deploying a Stand-Alone Real-Time Application

<!--NI_TOPIC bundle=labview-real-time-module path=debugging-deterministic-applications-real-time-module.html language=enus -->
## TOPIC 00026: Debugging Deterministic Applications

- bundle_id: `labview-real-time-module`
- source_path: `debugging-deterministic-applications-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/debugging-deterministic-applications-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Debugging deterministic LabVIEW applications requires techniques different from typical LabVIEW debugging. With deterministic applications, there are two levels of debugging to verify—application behavior and timing behavior.

### Debugging Deterministic Applications

Debugging deterministic LabVIEW applications requires techniques different from
 typical LabVIEW debugging. With deterministic applications, there are two levels of
 debugging to verify—application behavior and timing behavior.

Parent topic:

Real-Time Module Concepts

Related concepts:

- Verifying Correct Application Behavior
- Verifying Correct Timing Behavior

<!--NI_TOPIC bundle=labview-real-time-module path=deploying-and-running-vis-on-an-rt-target-real-time-module.html language=enus -->
## TOPIC 00027: Deploying and Running VIs on an RT Target

- bundle_id: `labview-real-time-module`
- source_path: `deploying-and-running-vis-on-an-rt-target-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/deploying-and-running-vis-on-an-rt-target-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Deploying refers to downloading VIs and dependent files to an RT target. When you run a VI under a target, LabVIEW deploys the VI, all items required by the VI, and the target settings to the RT target. Deploying VIs from the Project Explorer WindowYou can add VIs and dependent files under an RT tar

### Deploying and Running VIs on an RT Target

Deploying refers to downloading VIs and dependent files to an RT target. When you
 run a VI under a target, LabVIEW deploys the VI, all items required by the VI, and
 the target settings to the RT target.

#### Deploying VIs from the Project
 Explorer Window

You can add VIs and dependent files under an RT target in
 the Project Explorer window. Right-click an item under an RT target in the
 Project Explorer window and select
 Deploy from the shortcut menu to deploy the item and any
 support files for the item to the target.

#### Deployment Locations on an RT
 Target

The following table describes what items download to disk and what
 items download to memory on an RT target.

| Items | Download Location |
| --- | --- |
| Properties, settings, and built applications and their dependencies | Disk |
| VIs, libraries, and shared libraries (when running interactively) | Memory |

#### Deploying VIs that Use a LabVIEW
 Class or Call a Member VI

If you deploy a VI that uses a LabVIEW class or
 calls a member VI, only the VIs and classes referenced in the application deploy to
 the target. If the deployed VIs reference any dynamic dispatch member VIs, all the
 VIs that override the dynamic dispatch member VI in descendant classes also
 deploy.

#### Disabling Automatic Variable
 Deployment

By default, when you run a VI LabVIEW automatically deploys all
 shared variables that the VI references, including I/O variables. However, in some
 cases it is useful to disable automatic variable deployment. The following table
 provides examples of when to enable and disable automatic variable deployment.

| Automatic Variable Deployment | Use Case | Benefit |
| --- | --- | --- |
| Enabled | Developing a VI. | Allows you to run a VI simply by pressing the Run button, without separately deploying or redeploying variables that the VI references. |
| Disabled | Running a host VI that references a variable hosted on an RT target running a startup VI. | Allows you to run the host VI without encountering a deployment conflict. |

You can disable automatic variable deployment on the host computer or on an
 RT target by right-clicking the host computer or RT target in the Project
 Explorer window and selecting Disable Autodeploy
 Variables from the shortcut menu.

#### Compiled Object
 Cache

LabVIEW stores the compiled code for deployed VIs in the compiled
 object cache. If you edit and redeploy a VI, LabVIEW updates the compiled object
 cache.

Note

Note

#### Accessing the Front Panel of an RT
 Target VI

You can connect to an RT target and access the front panels of
 VIs in memory on the target.

Connecting—Right-click an
 RT target in the Project Explorer window and select
 Connect from the shortcut menu to open a front panel
 connection with the target. LabVIEW opens the front panels of VIs, indicating that
 the VIs are in memory on the RT target. Closing the front panel removes the VIs from
 memory on the target.

Disconnecting—Right-click an RT
 target in the Project Explorer window and select
 Disconnect from the shortcut menu to disconnect the front
 panel connection with the target and leave VIs running or in memory on the
 target.

#### Deploying Settings on CompactRIO
 Targets

Deploying configuration settings to a CompactRIO target with a
 connected I/O chassis involves three distinct domains:

- Project —The target settings configured in the LabVIEW
 project.
- Target —The target settings currently deployed on the
 target.
- Chassis —The physical I/O modules connected to the
 chassis.

#### Maintaining Synchronization between
 the Project, Target, and Chassis Configuration

You can lose
 synchronization among the project, target, and chassis configurations when you add a
 module, remove a module, or change the module in a chassis slot.

- Adding an I/O Module —To maintain synchronization when you
 add a module to a previously empty chassis slot, you must add the new module to
 the project and deploy the new project item to the target. Right-click the
 chassis item in the Project Explorer window and select
 New»C Series Modules to display the Add Targets and
 Devices dialog box, which you can use to discover the new module and add it to
 the project. After you add the new module to the project, right-click the module
 and select Deploy to synchronize the new configuration
 with the target. If you add multiple new modules to the project, right-click the
 chassis item and select Deploy to deploy all the new
 modules to the target at once.
- Removing an I/O Module —To maintain synchronization when
 you remove a module from a chassis slot, you must right-click the module in the
 Project Explorer window and select
 Undeploy to remove the module configuration from the
 target. You then can delete the module from the project.
- Changing the Type of an I/O Module —If a module at a given
 chassis location in the project does not match the module at that location in
 the actual CompactRIO chassis, right-click the old module item in the
 Project Explorer window and select
 Undeploy from the shortcut menu. Then right-click the
 chassis item in the Project Explorer window and select
 New»C Series Modules to display the Add
 Targets and Devices dialog box. Use the Add Targets
 and Devices dialog box to discover the new module and add the
 module to the project.

#### Troubleshooting Steps for NI Scan
 Engine Deployment

If you encounter deployment difficulties while using features that depend on the NI
 Scan Engine, you can attempt the following troubleshooting steps:

1. Installing and Initializing the NI Scan Engine —You must
 install NI Scan Engine support on an RT target to deploy items and settings that
 use the NI Scan Engine. If you recently powered up or restarted a target with
 the NI Scan Engine installed, you must wait for the NI Scan Engine to initialize
 before deploying the target.
2. Forcing Deployment —To minimize target communication,
 LabVIEW only deploys I/O modules and I/O variables upon detecting that the
 configuration differs from the previously deployed configuration. Therefore, in
 some cases a deployment operation might appear successful or display a
 Nothing to deploy message although no information was sent
 to the target and the target remains unsynchronized. If you experience recurrent
 difficulty synchronizing the target, project, and chassis, you can force
 deployment by undeploying an I/O item and then redeploying the item.
3. Cleaning out NI Scan Engine Configuration Settings —If
 forcing deployment does not solve the problem, you might need to clean out the
 deployed NI Scan Engine settings from the target. To clean out NI Scan Engine
 settings, establish an FTP connection to the target and remove all files from
 the ni-rt/config/ directory on the target. (NI Linux Real-Time)
 Establish an SSH connection to the target and remove all files from the
 /var/local/natinst/deployfwk/config/ directory. After you
 clean out the appropriate directory, restart the target, then right-click the
 target in the Project Explorer window and select
 Connect from the shortcut menu to redeploy the target
 settings.
4. Reformatting the Target —If all else fails, you might need
 to reformat and reinstall software on the target. After reinstalling software on
 the target, you should be able to redeploy the target successfully.

Note

Parent topic:

Organizing and Managing a LabVIEW Project with the Real-Time Module

<!--NI_TOPIC bundle=labview-real-time-module path=design-considerations-for-displaying-rt-target-vis-real-time-module.html language=enus -->
## TOPIC 00028: Design Considerations for Displaying RT Target VIs

- bundle_id: `labview-real-time-module`
- source_path: `design-considerations-for-displaying-rt-target-vis-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/design-considerations-for-displaying-rt-target-vis-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following table provides design considerations for developing RT target VIs you intend to display using the embedded UI or remote front panel connections. In general, you should keep UI updates outside of time-critical loops to prevent negative effects on determinism. Also keep in mind that enab

### Design Considerations for Displaying RT Target VIs

The following table provides design considerations for developing RT target VIs you
 intend to display using the embedded UI or remote front panel connections. In
 general, you should keep UI updates outside of time-critical loops to prevent
 negative effects on determinism. Also keep in mind that enabling the embedded UI
 affects determinism. The additional jitter should remain acceptable for most
 applications, but if you want to guarantee the best determinism for your system,
 disable the embedded UI.

| Place Front Panel Controls and Indicators Outside of Time-Critical Loops | Updating front panel controls and indicators within time-critical loops negatively affects determinism. |
| --- | --- |
| Place Property Nodes Outside of Time-Critical Loops | Updating property nodes within time-critical loops negatively affects determinism. |
| Do Not Enable the Synchronous Display Property | Enabling the synchronous display property for controls and indicators negatively affects determinism. |
| Allow Time for the UI to Update | The code that updates the front panel display executes at a lower priority than code inside timed structures. You may notice delays in front panel updates when time-critical code utilizes the majority of the available RT target resources. To prevent these delays, specify sufficient duration for the periods of timed structures so that time-critical code does not utilize all of the allocated resources during a cycle. |

#### Display Parity

Due to differences between operating systems, front panel elements, such as fonts and controls,
 may look different when you display them on the
 embedded UI or through a remote front panel
 connection than when you display them on your host
 computer. Visit ni.com/info and
 enter DisplayParity to
 learn more about display parity across operating
 systems.

#### Language Support on the Embedded UI

The embedded UI does not support localized versions of the Real-Time Module.
 Therefore, to use the embedded UI, ensure that both your host computer and RT target
 use the English versions of the Real-Time Module.

#### Xfce and the Embedded UI

NI uses Xfce to create the embedded UI for RT targets. Xfce is a collection of
 components that provides a lightweight desktop environment for UNIX-like operating
 systems. To learn about using and configuring Xfce, refer to the Xfce help available
 on the Xfce website.

#### Embedded UI Template

Visit ni.com/info and enter RTUITemplate to access an
 application that demonstrates a producer/consumer
 design pattern with embedded UI functionality.

#### Unsupported Features on the Embedded UI

In addition to the unsupported features of each RT target, the embedded UI
 does not support the following LabVIEW features. In most cases, you will not find
 these features on the applicable palette when you enable the embedded UI. If an
 existing VI includes these features, the VI will not run when you enable the
 embedded UI.

- Subpanels
- XControls
- 3D graphs
- 3D Picture Control VIs

Parent topic:

Interacting with the Front Panels of RT Target VIs

<!--NI_TOPIC bundle=labview-real-time-module path=determining-when-to-use-multiple-cpus-real-time-module.html language=enus -->
## TOPIC 00029: Determining When to Use Multiple CPUs

- bundle_id: `labview-real-time-module`
- source_path: `determining-when-to-use-multiple-cpus-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/determining-when-to-use-multiple-cpus-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: When you install the NI RT Extensions for SMP, the Real-Time Module balances threads across available CPUs in a process called automatic load balancing. Automatic load balancing enables RT target VIs that incorporate parallelism to take advantage of multiple-CPU systems, also known as multi-core, mu

### Determining When to Use Multiple CPUs

When you install the NI RT Extensions for SMP, the Real-Time Module balances threads
 across available CPUs in a process called automatic load balancing. Automatic load
 balancing enables RT target VIs that incorporate parallelism to take advantage of
 multiple-CPU systems, also known as multi-core, multi-processor, or SMP systems.
 However, transferring data between CPUs takes longer than transferring data from one
 operation to the next on a single CPU. Also, the overhead of the CPU scheduler
 slightly increases latency on the RT system, which can slow down single-point I/O
 applications that do not benefit from parallelism. In general, an application will
 benefit from multiple CPUs only if the time saved through parallel processing
 exceeds the time spent allocating system resources and transferring data between
 CPUs.

Note

Measurement & Automation Explorer Help

#### Applications that Benefit from Multiple CPUs

Real-time applications often include data logging or host communication tasks that
 run in parallel to time-critical tasks. For example, the following block diagram
 shows an RT target VI with two parallel loops. Because of the parallelism of the
 architecture, running this type of application on a multiple-CPU RT system can
 improve performance without any need to rewrite the VI.

[IMAGE alt='image' src='GUID-1EE72561-8DA2-4575-A749-66771C8E0955-a5.png']

Applications that require multiple time-critical processes might also benefit from
 multiple CPUs. Because of the preemptive nature of time-critical tasks, it is
 generally best to include only one time-critical loop on a single-CPU system.
 However, on a multiple-CPU system you can include a time-critical loop on each
 CPU.

#### Applications that Do Not Benefit from Multiple CPUs

Although most real-time applications realize an immediate performance boost by
 switching to a multiple-CPU system, some VIs must be rewritten to benefit from
 additional CPUs and other VIs cannot benefit from additional CPUs. Real-time
 applications that consist of a single sequential loop do not benefit immediately
 from additional CPUs. If the loop consists of intensive processing, you might be
 able to increase performance by implementing a pipelined
 architecture. However, applications that consist primarily of single-point I/O
 processing usually do not benefit from multiple CPUs because the CPU scheduler
 contributes a slight amount of additional latency.

Applications that contain shared resources might not benefit from additional CPUs until you
 rewrite the application to avoid shared resource conflicts. Simultaneous requests
 for a shared resource impede parallel execution and diminish the performance benefit
 of a multiple-CPU system.

Note

Parent topic:

Optimizing RT Applications for Multiple-CPU Systems

Related concepts:

- Avoiding Shared Resources
- Optimizing RT Applications for Multiple-CPU Systems

<!--NI_TOPIC bundle=labview-real-time-module path=enabling-remote-front-panel-connections-to-rt-target-vis-real-time-module.html language=enus -->
## TOPIC 00030: Enable Remote Front Panel Connections to RT Target VIs

- bundle_id: `labview-real-time-module`
- source_path: `enabling-remote-front-panel-connections-to-rt-target-vis-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/enabling-remote-front-panel-connections-to-rt-target-vis-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `task`
- source_description: Learn how to enable remote front panel access for VIs running on an RT target by configuring the Web Server and visible VIs. You can view the front panel of a VI running on an RT target from a computer using LabVIEW. To allow remote access, enable the Web Server on the RT target and make the VI visi

### Enable Remote Front Panel Connections to
 RT Target VIs

Learn how to enable remote front panel access for VIs running on an RT target by
 configuring the Web Server and visible VIs.

You can view the front panel of a VI running on an RT target from a computer using
 LabVIEW. To allow remote access, enable the Web Server on the RT target and make the
 VI visible to the Web Server, and add the computer to the access list of the
 target.

Complete the following steps to enable remote front panel connections to RT target
 VIs.

1. Right-click an RT target in the Project Explorer window and select
 Properties from the shortcut menu.
2. Click Web Server in the Category list.
3. Place a checkmark in the Enable Remote Panel Server
 checkbox.
4. Add the filename of a VI that is in memory on the RT
 target to the Visible VIs list. 
 Note If you deployed
 a VI to the RT target before enabling the Web Server, you must redeploy the
 VI to access the front panel.
5. Click OK to close the RT target
 Properties dialog box.

Parent topic:

Using Remote Front Panels to Access RT Target VIs

Related concepts:

- Adding New Entries to Browser Access List of an RT Target
- Viewing and Controlling the Front Panels of RT Target VIs Remotely (Real-Time Module)

<!--NI_TOPIC bundle=labview-real-time-module path=enabling-the-embedded-ui-on-rt-targets-real-time-module.html language=enus -->
## TOPIC 00031: Enabling the Embedded UI on RT Targets

- bundle_id: `labview-real-time-module`
- source_path: `enabling-the-embedded-ui-on-rt-targets-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/enabling-the-embedded-ui-on-rt-targets-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Complete the following steps to enable the embedded UI on an RT target. If you enable the embedded UI, you can access a desktop environment on your RT target from which you can browse files, access terminals and settings, and interact with the front panel of a VI running on the RT target. Some RT

### Enabling the Embedded UI on RT Targets

Complete the following steps to enable the embedded UI on an RT target. If you enable
 the embedded UI, you can access a desktop environment on your RT target from which
 you can browse files, access terminals and settings, and interact with the front
 panel of a VI running on the RT target.

Note

1. Connect a display device to the RT target. You also can connect other UI
 devices, such as a mouse and keyboard.
2. Connect the RT target to the same subnet as the host computer. Refer to the
 Connecting to LabVIEW Real-Time Targets topic of the
 Measurement & Automation Explorer Help for
 information about connecting to RT targets. To open the Measurement
 & Automation Explorer Help , select Help»MAX
 Help from NI Measurement & Automation Explorer (MAX).
3. If the recommended software set (for example, NI CompactRIO version -
 version date ) is installed on the RT target, proceed to
 step 4. Otherwise, complete the following steps to install the recommended
 software set. MAX displays the progress of the installation, and then restarts the
 target.
  1. In MAX, expand Remote Systems in the
 configuration tree, and then expand your RT target.
  2. Select Software in the configuration tree.
  3. Click the Add/Remove Software icon on the toolbar
 to launch the LabVIEW Real-Time Software Wizard.
  4. Select the recommended software set that the wizard displays and click
 Next .
4. Enable the embedded UI checkbox in MAX: 
 Note You also can enable the embedded UI checkbox using NI Web-based
 Configuration & Monitoring.
  1. Expand Remote Systems in the configuration tree,
 and then select your RT target.
  2. In the Startup Settings section of the
 System Settings tab, place a checkmark in the
 Enable Embedded UI checkbox.
  3. Click Save , and then Yes 
 when prompted to restart the target.

The target restarts and displays the embedded UI desktop.

Note

Parent topic:

Using the Embedded UI to Access RT Target VIs

Related concepts:

- Viewing and Controlling the Front Panels of RT Target VIs Using the Embedded UI
- Customizing How Front Panels Display on the Embedded UI

<!--NI_TOPIC bundle=labview-real-time-module path=exploring-remote-communication-methods-real-time-module.html language=enus -->
## TOPIC 00032: Exploring Remote Communication Methods

- bundle_id: `labview-real-time-module`
- source_path: `exploring-remote-communication-methods-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/exploring-remote-communication-methods-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use high-level software protocols to communicate between VIs running on the RT target and VIs running on other targets, such as the host computer. Each protocol has its advantages and disadvantages. The following list classifies the different communication methods: Network Communication—Used

### Exploring Remote Communication Methods

You can use high-level software protocols to communicate between VIs running on the
 RT target and VIs running on other targets, such as the host computer. Each protocol
 has its advantages and disadvantages. The following list classifies the different
 communication methods:

- Network Communication—Used for communication over Ethernet networks.
  - Network Streams
  - Network-Published Shared Variables
  - TCP
  - UDP
  - VI Server
  - Logos
  - SMTP (send only)
- Bus Communication—Used for communication over different bus communication ports.
  - Serial
  - CAN

#### Network Communication

This section describes the most common network communication protocols used with the
 LabVIEW Real-Time Module. Use this information to help you select the right
 networking protocol(s) for your application.

#### Network Streams

You can use network streams to stream data or send
 commands between an RT target and a host computer. A network stream is a
 lossless, unidirectional, one-to-one communication channel that consists of a writer
 and a reader endpoint.

#### Network-Published Shared Variables

You can use network-published shared variables to share data between VIs running on
 different targets across a network. By enabling the
 real-time FIFO of a shared variable, you can share data across a network without affecting the determinism of the
 VIs. However, the transfer of the data across the network is not deterministic. Due
 to network latency, the most recently written data may not be available to a VI
 running on a machine across the network. In this case, the VI attempting to read
 from the network-published shared variable returns the previous value. For data
 logging applications, you can use timestamps to programmatically ensure that each
 value is logged once and only once.

#### TCP

TCP is an industry-standard protocol for communicating over networks. VIs running on
 the host computer can communicate with RT target VIs using the TCP VIs and functions. However, TCP is non-deterministic, and using TCP
 communication inside a deterministic VI can affect the determinism of the VI.

The Real-Time Module extends the capabilities of the existing TCP functions to enable
 communication with networked RT Series devices.

#### UDP

UDP is a network transmission protocol for transferring data between two locations on
 a network. UDP is not a connection-based protocol, so the transmitting and receiving
 computers do not establish a network connection. Because there is no network
 connection, there is little overhead when transmitting data. However, UDP is
 non-deterministic, and using UDP communication inside a deterministic VI can affect
 the determinism of the VI.

When using the UDP VI and functions to send data, the receiving
 computer must have a read port open before the transmitting computer sends the data.
 Use the UDP Open function to open a write port and specify the IP address and
 port of the receiving computer. The data transfer occurs in byte streams of varying
 lengths called datagrams. Datagrams arrive at the listening port, and the receiving
 computer buffers and then reads the data.

You can transfer data bidirectionally with UDP. With bidirectional data transfers,
 both computers specify a read and write port and transmit data back and forth using
 the specified ports. You can use bidirectional UDP data transfers to send and
 receive data from a VI on the RT target.

UDP has the ability to perform fast data transmissions. However, UDP cannot guarantee
 that all datagrams arrive at the receiving computer. Because UDP is not
 connection-based, you cannot verify the arrival of datagrams. You must ensure that
 network congestion does not affect the transmission of datagrams. Also, you must
 read data stored in the data buffer of the receiving computer fast enough to prevent
 overflow and loss of data.

#### VI Server

Use VI
 Server to monitor and control VIs on an RT target. Using VI Server, a
 LabVIEW VI can invoke RT target VIs remotely. The LabVIEW VI can pass parameter
 values to and from the RT target VIs, creating a distributed application.

A host VI can invoke only VIs that are already stored on the RT target. The host VI
 cannot dynamically download LabVIEW VIs to the RT target for use with the VI
 Server.

One advantage to communicating using the VI Server is that the VI Server allows you
 to access the functionality of TCP while working within the framework of LabVIEW.
 However, the VI Server is non-deterministic and using VI Server communication can
 affect the determinism of the VI.

#### SMTP Email

Use the SMTP Email VIs to send data from a VI running on the RT target to VIs
 running on another computer. The SMTP VIs can send email, including attached data
 and files, using the Simple Mail Transfer Protocol (SMTP). You cannot use the SMTP
 VIs to receive information.

SMTP is non-deterministic and using SMTP communication inside a deterministic VI can
 affect the determinism of the VI.

#### Logos (FieldPoint Only)

You can use Logos to transfer host interface data to and from traditional FieldPoint
 and Compact FieldPoint Ethernet modules. Ethernet-enabled FieldPoint modules have an
 embedded Logos Server, which enables reads and writes to the physical I/O modules on
 the FieldPoint bank from a remote system.

#### Bus Communication

#### Serial

Serial communication is the transmission of data between two locations through the
 serial ports. The Serial
 VIs and functions provide serial communication support in LabVIEW for communication
 between RT targets with serial devices and serial instruments or computers that have
 a serial connection. Serial communication is ideal when transfer data rates are low
 or for transmitting data over long distances. You must add the NI-Serial RT software
 on the RT target from NI Measurement & Automation Explorer (MAX). Refer to the
 Measurement & Automation Explorer Help for information
 about adding software on an RT target.

Serial communication is non-deterministic and using serial communication inside a
 deterministic VI can affect the determinism of the VI.

#### CAN

Controller Area Network (CAN) is a deterministic, multi-drop communication bus
 standardized as ISO 11898. Using CAN, you can transfer up to 8 data bytes per frame
 at a rate of up to 1 Mbit per second. You can network multiple RT systems using
 NI-CAN interface cards and NI-CAN driver software. You must add the NI-CAN RT
 software on the RT target from MAX. Refer to the Measurement &
 Automation Explorer Help for information about adding software on an
 RT target.

Visit ni.com/info and enter CANManual to view the NI-CAN
 Hardware and Software Manual, which contains information about using NI-CAN hardware
 and software with LabVIEW.

Parent topic:

Sharing Data in Deterministic Applications

Related concepts:

- Sharing Data Using Shared Variables
- Sharing Data Remotely across a Network

<!--NI_TOPIC bundle=labview-real-time-module path=get-the-benchmarking-right-real-time-module.html language=enus -->
## TOPIC 00033: Get the Benchmarking Right

- bundle_id: `labview-real-time-module`
- source_path: `get-the-benchmarking-right-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/get-the-benchmarking-right-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Before deploying a real-time application, you need to know that the application meets your timing requirements consistently over an extended execution period. This topic describes best practices for benchmarking the performance and determinism of an RT application. Avoid execution highlighting while

### Get the Benchmarking Right

Before deploying a real-time application, you need to know that the application


 meets your timing


 requirements consistently over an extended execution period. This topic


 describes best practices for benchmarking the performance and determinism of an RT


 application.

Note

#### Benchmark with Deployment Settings

Before benchmarking an RT application, switch to deployment settings to ensure that your benchmarks accurately


 reflect the performance of the final application.

#### Using the RT Benchmarking Example

National Instruments recommends benchmarking the entire contents of a time-sensitive


 loop before deploying your application. Use the RT Benchmark example project as a


 starting point when benchmarking code that will be included in a time-sensitive


 loop. The RT Benchmark example is designed to provide accurate average-case and


 worst-case jitter execution time over thousands of iterations. Refer to the


 Benchmark Project.lvproj in the


 labview\examples\Real-Time Module\RT Benchmarking


 directory.

National Instruments created the RT Benchmark example project as a tool for


 benchmarking code that needs to run deterministically. You also can use this project


 to benchmark non-time-critical code. However, first change the priority of the


 benchmarking VI to match the priority at which the code will run in your


 application. Use the Priority pull-down menu on the Execution page of the VI


 Properties dialog box to set the priority of a VI.

Note

#### Using the Real-Time Trace Viewer

Use the Real-Time Trace


 Viewer VIs to capture the timing and execution data of VI and thread events for


 applications running on an RT target. The Real-Time Trace Viewer displays the timing and event data, or trace session, on the host


 computer. In LabVIEW, select Tools»Real-Time Module»Trace


 Viewer to display the Real-Time Trace Viewer.

For a mapping of thread names across different operating systems, refer to the KnowledgeBase.

#### Using the NI Distributed System Manager

Use the NI Distributed System Manager to monitor CPU and memory usage, alerts, VI


 states, and shared variables on an RT target. Select Tools»Distributed


 System Manager to display the NI Distributed System Manager.

Parent topic:

Real-Time Module Best Practices

Related concepts:

- Switch to Deployment Settings

<!--NI_TOPIC bundle=labview-real-time-module path=install-rt-module.html language=enus -->
## TOPIC 00034: Installing the LabVIEW Real-Time Module

- bundle_id: `labview-real-time-module`
- source_path: `install-rt-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/install-rt-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can install the LabVIEW Real-Time Module with either NI Package Manager or with the LabVIEW Platform media. Application Software SupportThe LabVIEW 2024 Q1 Real-Time Module supports LabVIEW 2024 Q1. For information about the Application Software Support in earlier versions of the LabVIEW Real-Ti

### Installing the LabVIEW
 Real-Time Module

You can install the LabVIEW
 Real-Time Module with either NI Package Manager or with the LabVIEW Platform
 media.

#### Application Software Support

The LabVIEW 2024 Q1 Real-Time Module supports LabVIEW 2024 Q1. For
 information about the Application Software Support in earlier versions of the LabVIEW
 Real-Time Module, refer to the Readmes for those
 versions.

#### Installing the LabVIEW
 Real-Time Module using Package
 Manager

Refer to *Package Manager* for information about
 installing, removing, and upgrading NI software using Package Manager.

#### Installing the LabVIEW
 Real-Time Module using LabVIEW Platform
 Media

- LabVIEW
- Modules
- Toolkits
- Drivers

Note

NI Installer Hangs
 While Installing Visual C++ 2015 Run-Time

Note

Note

License
 Manager

#### Installing and Using Japanese and Simplified Chinese Languages on an RT
 Target

1. Use the LabVIEW Real-Time Software Wizard in NI Measurement & Automation
 Explorer (NI MAX) to install language support. Choose either Japanese or
 Simplified Chinese for the RT target. Refer to the Measurement &
 Automation Explorer Help for information about the LabVIEW Real-Time
 Software Wizard.
2. Open the System Settings tab and select Japanese or Simplified Chinese as
 the Locale. Note You cannot
 use Japanese or Simplified Chinese characters in directory names or file
 names on the RT target. Note The Real-Time Module
 (64-bit) supports English only.

#### Configuring RT Targets

Use NI MAX to configure RT targets and to install
 software and drivers on targets. You can install NI MAX from the NI Package Manager
 or the LabVIEW Platform media.

- Networked RT Targets—To configure networked RT targets, refer to the Remote
 Systems book in the Measurement & Automation Explorer Help. Access it by
 selecting Help»MAX Help from MAX.

Related information:

- Package Manager
- NI Installer Hangs While Installing Visual C++ 2015 Run-Time
- License Manager

<!--NI_TOPIC bundle=labview-real-time-module path=interacting-with-the-front-panels-of-rt-target-vis-real-time-module.html language=enus -->
## TOPIC 00035: Interacting with the Front Panels of RT Target VIs

- bundle_id: `labview-real-time-module`
- source_path: `interacting-with-the-front-panels-of-rt-target-vis-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/interacting-with-the-front-panels-of-rt-target-vis-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can interact with the front panels of RT target VIs using the following methods: Enabling the Embedded UI on RT Targets—Allows you to connect a display device directly to the RT target and interact with a graphical working environment, including the front panel of a VI running on the RT target.

### Interacting with the Front Panels of RT Target VIs

You can interact with the front panels of RT target VIs using the following
 methods:

- Enabling the Embedded UI on RT Targets—Allows you to
 connect a display device directly to the RT target and interact with a graphical
 working environment, including the front panel of a VI running on the RT
 target.
- Using Remote Front Panels to Access RT Target
 VIs—Allows you to view and control the front panel of a VI
 running on the RT target from a remote computer. Only one user can control the
 front panel of a VI at any specific time, but several users at different
 locations can view the front panel simultaneously.

Parent topic:

Real-Time Module How-To

Related concepts:

- Enabling the Embedded UI on RT Targets
- Using Remote Front Panels to Access RT Target VIs

<!--NI_TOPIC bundle=labview-real-time-module path=interacting-with-the-front-panels-of-rt-target-vis.html language=enus -->
## TOPIC 00036: Interacting with the Front Panels of RT Target VIs

- bundle_id: `labview-real-time-module`
- source_path: `interacting-with-the-front-panels-of-rt-target-vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/interacting-with-the-front-panels-of-rt-target-vis.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can interact with the front panels of RT target VIs using the host computer, using the embedded UI on the RT target, or using remote front panels to access RT target VIs. A—Host Computer The host computer is the primary system you use to develop VIs and perform initial testing. Using the host co

### Interacting with the Front Panels of RT Target VIs

You can interact with the front panels of RT target VIs using the host computer,
 using the embedded UI on the RT target, or using remote front panels to access RT
 target VIs.

[IMAGE alt='image' src='GUID-74461BAE-A827-43B6-B209-65F138DB9DC7-a5.png']

#### A—Host Computer

The host computer is the primary system you use to develop VIs and perform initial
 testing. Using the host computer, you can view and control the front panel and block
 diagram of a VI running on the RT target. While the host computer is connected to
 the RT target, it retains control of the front panel, allowing you to interact with
 UI elements on the front panel using input devices connected to the host computer.
 If the front panel requires updates to control and indicator values, the host
 computer updates these values with values made by the RT target.

#### B—Embedded UI

Many RT targets run headless, with only a basic console output display, but some RT
 targets support an embedded UI that provides advanced display capabilities. The
 embedded UI enables you to interact with the front panel of an RT target VI using
 devices connected directly to the RT target, eliminating the need to view the front
 panel through a host computer after development is complete. For example, when you
 enable the embedded UI on an applicable RT target, you can view the front panel of a
 VI on a display device connected to the RT target. Furthermore, you can control the
 front panel of a VI using input devices connected to the RT target if you disconnect
 the host computer from the RT target. In addition to these benefits, the embedded UI
 also provides a graphical working environment that includes a file browser and a
 text editor, thereby facilitating browsing and editing files on your RT target.

#### C—Remote Front Panels

Remote front panel connections provide a way to interact with front panels by
 connecting to the RT target via a web server. With remote front panel connections,
 you can view and control the front panel of a VI running on the RT target from
 remote computers. Only one user can control the front panel of a VI at any specific
 time, but several users at different locations can view the front panel
 simultaneously.

Parent topic:

Real-Time Module Concepts

<!--NI_TOPIC bundle=labview-real-time-module path=introduction-to-the-labview-real-time-module-real-time-module.html language=enus -->
## TOPIC 00037: Introduction to the LabVIEW Real-Time Module

- bundle_id: `labview-real-time-module`
- source_path: `introduction-to-the-labview-real-time-module-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/introduction-to-the-labview-real-time-module-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Most LabVIEW applications run on a general-purpose operating system (OS) like Windows, Linux, or Mac OS X. Some applications require real-time performance that general-purpose operating systems cannot guarantee. The LabVIEW Real-Time Module extends the capabilities of LabVIEW to address the need for

### Introduction to the LabVIEW Real-Time Module

Most LabVIEW applications run on a general-purpose operating system (OS) like
 Windows, Linux, or Mac OS X. Some applications require real-time performance that
 general-purpose operating systems cannot guarantee. The LabVIEW Real-Time Module
 extends the capabilities of LabVIEW to address the need for real-time
 performance.

The Real-Time Module combines LabVIEW graphical programming with the power of a
 real-time operating system, enabling you to build deterministic applications. You develop VIs in LabVIEW and execute the
 VIs on an RT target. The RT target can run VIs in a stable platform optimized for
 real-time performance.

Parent topic:

Real-Time Module Concepts

Related concepts:

- Creating Deterministic Applications with the Real-Time Module

<!--NI_TOPIC bundle=labview-real-time-module path=labview-real-time-module-platforms-real-time-module.html language=enus -->
## TOPIC 00038: LabVIEW Real-Time Module Platforms

- bundle_id: `labview-real-time-module`
- source_path: `labview-real-time-module-platforms-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/labview-real-time-module-platforms-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Real-Time Module executes VIs on the NI Linux Real-Time operating system. The NI Linux Real-Time operating system runs on NI RT Series hardware to enable deterministic behavior and extended reliability. The LabVIEW Real-Time Module does not support certain LabVIEW features. Refer to The

### LabVIEW Real-Time Module Platforms

The LabVIEW Real-Time Module executes VIs on the NI Linux Real-Time operating system.

The NI Linux Real-Time operating system runs on NI RT Series hardware to enable deterministic
 behavior and extended reliability.

The LabVIEW Real-Time Module does not support
 certain LabVIEW features. Refer to *The NI Linux Real-Time
 Operating System* for information about unsupported
 LabVIEW features on the NI Linux Real-Time OS.

Parent topic:

Introduction to the LabVIEW Real-Time Module

Related concepts:

- The NI Linux Real-Time Operating System

<!--NI_TOPIC bundle=labview-real-time-module path=legacy-trace-support.html language=enus -->
## TOPIC 00039: Legacy Trace Support for Versions through LabVIEW Real-Time Module 2023 Q1

- bundle_id: `labview-real-time-module`
- source_path: `legacy-trace-support.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/legacy-trace-support.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn how to capture, view, and analyze VI and thread execution data on NI Linux Real-Time targets using the Real-Time Trace Viewer. OverviewThe Real-Time Trace Viewer is a diagnostic toolset for LabVIEW Real-Time applications. It captures timing and execution data of VIs and threads running on NI L

### Legacy Trace Support for Versions through
 LabVIEW Real-Time Module 2023 Q1

Learn how to capture, view, and analyze VI and thread execution data on NI Linux
 Real-Time targets using the Real-Time Trace Viewer.

#### Overview

The Real-Time Trace Viewer is a diagnostic toolset for LabVIEW
 Real-Time applications. It captures timing and execution data of VIs and threads
 running on NI Linux Real-Time targets and displays the information graphically on
 the host computer. This tool helps developers identify performance bottlenecks,
 resource contention, and timing anomalies.

Note

LabVIEW
 Real-Time Module

#### Real-Time Trace Viewer Features

Trace Capture

Trace Visualisation

Multi-CPU Support

Event Flags

Trace Session Management

Performance Analysis

#### Getting Started

1. Add Trace VIs to Your Application
  - Use TraceTool Start Trace VI to begin logging. Configure:
    - Buffer Size: Allocate enough memory to avoid overwriting
 data.
    - Event Types: Enable VI, thread, and detailed tracing as
 needed.
  - Use TraceTool Stop Trace and Send VI to stop logging and send data
 to the host.
  - Alternatively, use TraceTool Stop Trace and Save VI to save the
 trace on the RT target for later transfer.
2. View Trace Sessions
  - Launch the Real-Time Trace Viewer from Tools»Real-Time Module»Trace Viewer in LabVIEW.
  - Use VI and Thread views to analyze execution timelines, priorities,
 and CPU usage.
3. Log User Events
  - Insert TraceTool Log User Event VI to mark custom events in the
 trace.
  - Configure flag styles and colors in the Flag
 Configuration dialog.
4. Optimize Buffer Usage
  - Default buffer size is 250 KB ;
 increase if needed.
  - Disable unused event types to conserve memory.

#### Analyzing Trace Data

When you load a
 trace session in the Real-Time Trace Viewer, you can explore different views and
 tools to understand application behavior and timing characteristics. The following
 components help you analyze the data effectively:

VI View

Thread View

System Events

Use these tools to examine trace sessions in detail and measure
 performance:

- Zoom & Pan : Use this tool to navigate large traces
 easily.
- Measure Tool : Use this tool to calculate the timing
 between events.
- Highlight CPU Mode : Use this tool to focus on activity
 for each CPU in multi-core systems.

#### Best Practices

- Start and stop traces around critical code sections to minimize
 overhead.
- Allocate sufficient buffer size before starting a trace.
- Disable tracing when not needed to reduce CPU load.
- Combine trace analysis with other tools (e.g., NI Distributed System
 Manager) for a complete performance profile.

Parent topic:

Real-Time Tracing

<!--NI_TOPIC bundle=labview-real-time-module path=leverage-design-patterns-real-time-module.html language=enus -->
## TOPIC 00040: Leverage Design Patterns

- bundle_id: `labview-real-time-module`
- source_path: `leverage-design-patterns-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/leverage-design-patterns-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: A design pattern is a building block you can use within your LabVIEW Real-Time Module application to address common problems in software engineering. By using design patterns in your applications, you can take advantage of the accumulated experience of the software engineering community. The benefit

### Leverage Design Patterns

A design pattern is a building block you can use within your LabVIEW Real-Time


 Module application to address common problems in software engineering. By using


 design patterns in your applications, you can take advantage of the accumulated


 experience of the software engineering community. The benefits of design patterns


 include:

- Faster development time
- Greater robustness
- Better code reusability
- Easier debugging
- Enhanced maintainability

National Instruments recommends the following design patterns for LabVIEW Real-Time


 Module applications on all RT hardware platforms. If you have installed NI-DAQ or


 NI-RIO drivers, you can view examples of these design patterns in LabVIEW


 applications by using the Create


 Project dialog box to open sample projects designed for CompactDAQ, PXI


 with DAQ, and CompactRIO platforms.

| Use Case | Design Pattern | Description |
| --- | --- | --- |
| Transitioning between program states | Simple State Machine, available from the Create Project dialog box. | An application design composed of a finite number of states, transitions between those states, and actions associated with each state. |
| Communicating between parallel loops | Queued Message Handler, available from the Create Project dialog box. | An application design used to transfer data between processes that produce and consume data at different rates. |
| Creating an RT data server | Client-Server | An application design in which the client requests an action or service from the provider of service, the server. |

Refer to the NI LabVIEW for CompactRIO Developer's


 Guide, available at ni.com, for information about


 CompactRIO-specific design patterns.

Note

Parent topic:

Real-Time Module Best Practices

<!--NI_TOPIC bundle=labview-real-time-module path=logging-user-events-real-time.html language=enus -->
## TOPIC 00041: Logging User Events

- bundle_id: `labview-real-time-module`
- source_path: `logging-user-events-real-time.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/logging-user-events-real-time.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn how to log custom user events in trace sessions using the Log User String VI. These events help mark specific application sections and can be searched and analyzed in KernelShark alongside standard trace data. You can log user events in a trace to show the execution of specific sections of an

### Logging User Events

Learn how to log custom user events in trace sessions using the Log User String VI.
 These events help mark specific application sections and can be searched and analyzed in
 KernelShark alongside standard trace data.

You can log user events in a
 trace to show the execution of specific sections of an application.

Figure 4.

[IMAGE alt='LabVIEW block diagram showing trace logging with user events, including Start Trace, Log User String, and Stop Trace and Save VIs.' src='GUID-2D26BF52-F85A-4088-AFA3-44336FE00450-a5.png']

The following illustration shows user events logged by the VI. The VI runs in a
 LabVIEW thread with normal priority in the Standard execution system. The user
 events shown in KernelShark indicate the exact time the Log User Event VI executes
 in the application.

Figure 5.

[IMAGE alt='KernelShark interface showing user events with timestamps and details.' src='GUID-AEC31156-9751-4C1D-967E-C20DFD2BE6F6-a5.png']

Parent topic:

Capturing Traces

<!--NI_TOPIC bundle=labview-real-time-module path=mass-compiling-vis-real-time-module.html language=enus -->
## TOPIC 00042: Mass Compiling VIs

- bundle_id: `labview-real-time-module`
- source_path: `mass-compiling-vis-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/mass-compiling-vis-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Mass compiling a VI is another way to improve performance. Mass compiling a VI compiles the top-level VI and also recompiles and relinks all the subVIs and functions on the block diagram with the top-level VI. Select Tools»Advanced»Mass Compile to select a VI to mass compile.

### Mass Compiling VIs

Mass compiling a VI is another way to improve performance. Mass compiling a VI
 compiles the top-level VI and also recompiles and relinks all the subVIs and
 functions on the block diagram with the top-level VI. Select
 Tools»Advanced»Mass Compile to select a VI to mass
 compile.

Parent topic:

Optimizing Deterministic Applications

Related concepts:

- Optimizing Deterministic Applications

<!--NI_TOPIC bundle=labview-real-time-module path=minimize-cpu-usage-real-time-module.html language=enus -->
## TOPIC 00043: Minimize CPU Usage

- bundle_id: `labview-real-time-module`
- source_path: `minimize-cpu-usage-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/minimize-cpu-usage-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic contains guidelines for minimizing RT target CPU usage. By targeting a CPU usage well below 100%, you can minimize jitter and ensure that the tasks in your application do not need to compete for CPU time. Refer to the following topics for general LabVIEW performance tips: VI Execution Spe

### Minimize CPU Usage

This topic contains guidelines for minimizing RT target CPU usage. By targeting a


 CPU usage well below 100%, you can minimize jitter and ensure that the tasks in your application do not


 need to compete for CPU time.

Refer to the following topics for general LabVIEW performance tips:

- VI Execution Speed
- Memory Management for Large Data Sets

#### Run Loops Only as Fast as Necessary

Although it can be tempting to try to run each loop in your application as fast as


 possible, this practice can lead to undesired timing behavior, including increased


 jitter and even system deadlocks. For example, running a user interface data


 publishing loop faster than the human operator can process and respond to the data


 merely taxes the CPU of the RT target needlessly. In most cases, a rate of 2 Hz to


 15 Hz is adequate for a loop that publishes user interface data over the


 network.

Tip

#### Avoid Excessive Parallelism

The graphical dataflow paradigm of the LabVIEW block diagram makes it easy to


 parallelize the execution of code in your VIs, which can increase performance on


 multi-core systems. However, greater parallelism also requires LabVIEW to create and


 manage more threads. The overhead caused by these additional threads can impact


 performance. Generally, parallelism only increases performance on multi-core


 systems.

1. The RT target includes multiple CPU cores.
2. The total computation time required to execute the code serially exceeds the


 time required to execute the longest parallel branch plus the time required for


 thread management and switching overhead.

To determine whether a VI can benefit from parallelism, you might need to benchmark both the serial form and the parallel form of the VI. Refer to


 Optimizing RT Applications for Multiple-CPU Systems for information


 about using parallelism on multi-core RT targets.

#### Understand the Performance Benchmarks for Network-Published Shared


 Variables

Network-published shared variables exhibit a linear relationship between CPU


 utilization, data transfer frequency, and the number of variables in an application.


 Refer to the performance benchmarks, available at


 ni.com, for information about the CPU performance of


 network-published shared variables. You should use network-published shared


 variables primarily for low-frequency, latest-value data transfer applications. If


 you need to send a continuous stream of data from one computing device to another


 computing device, use the Network


 Streams functions. In general, you can use a large number of


 network-published shared variables without over-utilizing CPU resources if you use a


 low data transfer frequency. However, if you need to optimize CPU utilization by


 reducing the number of network-published shared variables, consider packing the


 individual data items into an array or cluster and transferring the array or cluster


 using a single network-published shared variable.

#### Offload Tasks When Possible

To minimize CPU usage on the RT target, consider offloading certain tasks either to a


 desktop PC or an FPGA target, if available. For example, consider hosting


 network-published shared variables on the host PC rather than on the RT target


 itself.

Note

Use the following guidelines to determine the most appropriate device for performing


 specific types of tasks:

| Task | Appropriate Devices |
| --- | --- |
| Data acquisition | RT or FPGA |
| Control loop | RT or FPGA |
| Data analysis for logging or monitoring purposes (offline analysis) | Desktop PC |
| Data logging | RT or Desktop PC |
| Hosting network-published shared variables | Desktop PC or RT |

Note

Parent topic:

Real-Time Module Best Practices

Related concepts:

- Avoid Jitter
- Get the Benchmarking Right

<!--NI_TOPIC bundle=labview-real-time-module path=minimizing-memory-usage-by-the-rt-target-web-server-real-time-module.html language=enus -->
## TOPIC 00044: Minimizing Memory Usage by the RT Target Web Server

- bundle_id: `labview-real-time-module`
- source_path: `minimizing-memory-usage-by-the-rt-target-web-server-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/minimizing-memory-usage-by-the-rt-target-web-server-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: To minimize memory usage when you enable the Web Server on an RT target, include only the VIs you want to access remotely on the Web Server: Visible VIs page of the RT Target Properties dialog box. Right-click an RT target in the Project Explorer window and select Properties from the shortcut menu t

### Minimizing Memory Usage by the RT Target Web Server

To minimize memory usage when you enable the Web Server on an RT target, include only
 the VIs you want to access remotely on the Web Server: Visible
 VIs page of the RT Target
 Properties dialog box. Right-click an RT target in the Project Explorer window and select
 Properties from the shortcut menu to open the
 RT Target Properties dialog box. By default, a
 * entry appears in the Visible VIs
 listbox, indicating that all VIs are visible. To save memory, remove the
 * entry and add only the VIs you want to be visible on the Web
 Server.

Parent topic:

Optimizing Deterministic Applications

Related concepts:

- Optimizing Deterministic Applications

<!--NI_TOPIC bundle=labview-real-time-module path=network-the-user-interface-real-time-module.html language=enus -->
## TOPIC 00045: Network the User Interface

- bundle_id: `labview-real-time-module`
- source_path: `network-the-user-interface-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/network-the-user-interface-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Some RT targets include an embedded user interface you can use to view and control the front panel of RT target VIs. However, other RT targets supported by the LabVIEW Real-Time Module are designed to run headless, with only a basic output display. For RT targets that do not support the embedded use

### Network the User Interface

Some RT targets include an embedded user interface you can use to view and control
 the front panel of RT target VIs. However, other RT targets supported by the LabVIEW
 Real-Time Module are designed to run headless, with only a basic output display. For
 RT targets that do not support the embedded user interface, creating a graphical
 user interface (GUI) for a LabVIEW Real-Time Module application requires a
 distributed computing approach. If your real-time application needs a user interface
 and you cannot use the embedded UI, display the GUI on a general-purpose operating
 system and use a remote communication protocol to transfer data between the RT
 target and the GUI device.

#### Avoid Front Panel Objects,
 Methods, and Events

When developing an RT VI for a target that does not support the embedded UI, you can
 use front panel controls and indicators for debugging, but you cannot use the front
 panel of an RT VI as the user interface of your final stand-alone RT application.
 When you deploy a VI as a stand-alone RT application, LabVIEW removes the front
 panel of the VI, including all objects, properties, methods, and events associated
 with it. Although event-driven programming can be a powerful user interface design
 pattern for many LabVIEW VIs, you cannot use the typical LabVIEW event-driven UI
 design pattern for a VI that runs on an RT target. However, you can use the
 event-driven design pattern to create a user interface VI running on a host computer
 that uses a networking protocol to communicate with the RT target VI.

#### Use the Right Networking
 Equipment

It can be tempting to use the networking equipment you already have or select the
 cheapest equipment available. However, the quality of commercial off-the-shelf
 networking equipment varies widely, so take the time to decide what type of
 networking equipment is most appropriate for your application. For some
 applications, lower-quality networking equipment is adequate. However, for
 applications that depend on network throughput, latency, or reliability,
 high-quality networking equipment can be crucial.

#### Use the Right Networking
 Protocol

The following table summarizes the advantages, disadvantages, and common use cases of
 the most common remote communication protocols for transferring data between RT
 targets and GUI devices:

| Use Case | Protocol | Advantages | Disadvantages |
| --- | --- | --- | --- |
| Monitoring latest values | Network-Published Shared Variable | Easy to program, publishes to many computers at once, safe to include in deterministic loops when the RT FIFO is enabled, integrates with industrial protocols | High CPU overhead, proprietary, requires the Shared Variable Engine |
| Streaming data between an RT target and a host computer, sending commands to an RT target | Network Streams | High throughput, lossless, automatic connection management, native LabVIEW data type support | Single writer — single reader, unidirectional data transfer, non-deterministic, proprietary |
| Starting point for custom protocols such as STM, available at ni.com | TCP or UDP | Efficient CPU and memory usage, flexible, standard protocol for interoperability | Programming difficulty, string data only, no built-in method to identify data |
| Dynamic control of RT VIs | VI Server | Good abstraction for local or remote control of VIs and other LabVIEW constructs | Low speed, proprietary |
| Web-based user interfaces, integration with standard Web technologies | Web Services | Web standard, client connection does not require LabVIEW | High overhead, programming difficulty, need to create a thin-client in a non-LabVIEW language |

The following table presents networking protocol recommendations for the most common
 RT GUI use cases:

| Use Case | Example | Recommended Protocols |
| --- | --- | --- |
| Command (one to one) | Sending user interface value changes from a host PC to an RT target | Network Streams functions |
| Command (one to many) | Sending user interface value changes from a host PC to multiple RT targets | Network-published shared variables |
| Command (many to one) | Sending user interface value changes from multiple Web clients to an RT target | Web services VIs or network-published shared variables |
| Monitor (one to one) | Using a host PC to monitor latest values published by an RT target | Network-published shared variables or STM |
| Monitor (one to many) | Using multiple Web clients to monitor latest values published by an RT target | Web services VIs or network-published shared variables |
| Monitor (many to one) | Using a host PC to monitor latest values published by multiple RT targets | Network-published shared variables |
| Stream (one to one) | Sending a continuous stream of data from an RT target to be logged on a host PC | Network Streams functions |
| Stream (one to many) | Web video server | TCP or UDP |
| Stream (many to one) | Web video client | TCP or UDP |

Note

ni.com

#### Creating a Dedicated
 Interface

For applications that require a single, dedicated user interface terminal, use the
 Network Streams functions to stream data continuously and to send commands. Use
 network-published shared variables or the Simple Messaging Reference Library (STM),
 available at ni.com, to monitor the latest value of each variable.
 Use the STM library to send commands to the RT target.

#### Creating a SCADA Interface

For supervisory control and data acquisition (SCADA) user interfaces typically
 involve one or more user interface terminals interacting with numerous embedded
 controllers. For SCADA applications, use network-published shared variables to send
 commands and monitor latest values. For maximum expandability in large applications,
 you can find, read, and write shared variables programmatically.

Refer to the RT FIFO Variables - networked.lvproj in the
 labview\examples\Real-Time Module\RT Communication\RT FIFO
 Variables directory for an example of using Shared Variables to publish
 user interface data.

Note

#### Use the Right Payload
 Sizes

Payload size is the amount of data you send over the network at once. Throughput and
 CPU efficiency increase as payload size increases. However, waiting to accumulate a
 large amount of data before sending the data increases the latency of your network
 transfers. When streaming data, the goal usually is to maximize throughput. By
 contrast, when sending commands, the goal usually is to minimize latency.

#### Streaming Data
 Continuously

To maximize throughput, follow these guidelines:

- Use an efficient networking protocol, such as UDP, TCP, or Streams.
- Accumulate data before sending the data over the network. By sending data in
 payloads of 1 KB (1024 bytes) or a multiple thereof, you can achieve high
 throughput and low CPU overhead while maintaining reasonable latency for most
 applications. However, if you need to minimize latency while streaming data, use
 a smaller payload size.
- Consider switching to polling mode for Ethernet packet detection. The
 Packet Detection setting of an RT target is on the
 Network Settings tab, under the More
 Settings pull-down menu in NI Measurement & Automation
 Explorer. Note 
 Polling mode provides lower jitter than interrupt mode. However, the CPU
 overhead required by polling mode decreases the maximum throughput you can
 achieve. Not all real-time targets support polling mode.

#### Sending Commands

To minimize latency, follow these guidelines:

- Use an efficient networking protocol, such as UDP, TCP, or Streams.
- Send each command as soon as possible. For example, you can use the Flush Stream
 function to send a command over the network immediately after writing the
 command.

Parent topic:

Real-Time Module Best Practices

<!--NI_TOPIC bundle=labview-real-time-module path=new-features-and-changes.html language=enus -->
## TOPIC 00046: LabVIEW Real-Time Module New Features and Changes

- bundle_id: `labview-real-time-module`
- source_path: `new-features-and-changes.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/new-features-and-changes.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn about updates, including new features and behavior changes, introduced in each version of LabVIEW Real-Time Module. Discover what is new in the latest releases of LabVIEW Real-Time Module.If you cannot find new features and changes for your version, it might not include user-facing updates. Ho

### LabVIEW Real-Time Module
 New Features and Changes

Learn about updates, including new features and behavior changes, introduced in each
 version of LabVIEW Real-Time Module.

LabVIEW Real-Time Module

Note

Release Notes

#### LabVIEW Real-Time Module
 2026 Q1 Changes

Learn about new features, behavior changes, and other updates in LabVIEW Real-Time Module 2026 Q1.

##### New
 Features

LabVIEW Real-Time Module

- Introduces new RT Tracing VIs, which utilize ftrace and produce trace
 files that are compatible with KernelShark. These VIs are available for NI Linux Real-Time x64 targets.

#### LabVIEW Real-Time Module 2023 Q1
 Changes

- LabVIEW 2023 Q1 Real-Time Module 64-bit version does not support the Modbus IO server.
 As a workaround, use the direct communication option with the Modbus
 LabVIEW API.
- LabVIEW 2023 Q1 Real-Time Module 32-bit and 64-bit versions do not support Real-Time
 Trace Viewer. Use KernelShark , a similar open source tool, as an
 alternative.

#### LabVIEW Real-Time Module 2022 Q3
 Changes

- Support for RT Series devices. Install and manage software using the Manage
 Software dialog in LabVIEW instead of using NI MAX .

#### LabVIEW Real-Time Module 2020
 Changes

- Support for RT Series devices. Use the RT Board LEDs node to control the LEDs on all RT Series devices.
- Support for CompactRIO Controllers.

<!--NI_TOPIC bundle=labview-real-time-module path=optimizing-deterministic-applications-real-time-module.html language=enus -->
## TOPIC 00047: Optimizing Deterministic Applications

- bundle_id: `labview-real-time-module`
- source_path: `optimizing-deterministic-applications-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/optimizing-deterministic-applications-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The programming techniques in this section can reduce execution jitter in applications that run on an RT target. Avoiding Shared Resources Avoiding Contiguous Memory Conflicts Avoiding SubVI Overhead Setting VI Properties Mass Compiling VIs Minimizing Memory Usage by the RT Target Web Server Optimiz

### Optimizing Deterministic Applications

The programming techniques in this section can reduce execution jitter in
 applications that run on an RT target.

- Avoiding Shared Resources
- Avoiding Contiguous Memory Conflicts
- Avoiding SubVI Overhead
- Setting VI Properties
- Mass Compiling VIs
- Minimizing Memory Usage by the RT Target Web Server
- Optimizing RT Applications for Multiple-CPU Systems

Parent topic:

Real-Time Module Concepts

Related concepts:

- Avoiding Shared Resources
- Avoiding Contiguous Memory Conflicts
- Avoiding SubVI Overhead
- Setting VI Properties
- Mass Compiling VIs
- Minimizing Memory Usage by the RT Target Web Server
- Optimizing RT Applications for Multiple-CPU Systems

<!--NI_TOPIC bundle=labview-real-time-module path=optimizing-rt-applications-for-multiple-cpu-systems-real-time-module.html language=enus -->
## TOPIC 00048: Optimizing RT Applications for Multiple-CPU Systems

- bundle_id: `labview-real-time-module`
- source_path: `optimizing-rt-applications-for-multiple-cpu-systems-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/optimizing-rt-applications-for-multiple-cpu-systems-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: With the LabVIEW Real-Time Module, you can take advantage of parallel processing on multiple-CPU systems, also known as multi-core, multi-processor, or SMP systems. The Real-Time Module includes a CPU scheduler that allocates threads among available CPUs. You can take advantage of the CPU scheduler

### Optimizing RT Applications for Multiple-CPU Systems

With the LabVIEW Real-Time Module, you can take advantage of parallel processing on
 multiple-CPU systems, also known as multi-core, multi-processor, or SMP systems.

The Real-Time Module includes a CPU scheduler that allocates threads among available
 CPUs. You can take advantage of the CPU scheduler to achieve parallel execution on
 multiple-CPU systems. Many RT applications can benefit from additional CPUs without
 rewriting the application. However, by writing the RT application with multiple CPUs
 in mind, you might be able to achieve significant performance gains. To realize the
 full benefits of an RT system with multiple CPUs, you must implement a parallel or
 pipelined architecture in the RT target VI.

Note

When writing a VI to run on a system with multiple CPUs, avoid shared resource
 conflicts whenever possible. The advantage of a system with multiple CPUs is that
 separate threads can execute simultaneously on separate CPUs. Simultaneous requests
 for a shared resource impede parallel execution and diminish the performance benefit
 of a multiple-CPU system.

The Real-Time Module automatically balances threads across all available CPUs.
 However, you might be able to optimize the performance of some applications using
 manual CPU assignment with timed structure and CPU pools.

Note

- When you open a VI created in a version of LabVIEW prior to 8.5, all Timed
 Loops automatically run on the default CPU. In this case, you can use manual
 CPU assignment with timed structure and CPU pools to take advantage of
 multiple CPUs.
- Refer to the NI website for more information about optimizing performance in
 a multiple-CPU RT system.

Parent topic:

Optimizing Deterministic Applications

Related concepts:

- Creating Deterministic Applications Using the Timed Loop
- Creating Deterministic Applications Using VIs Set to Different Priorities
- Creating Deterministic Applications with the Real-Time Module
- Optimizing Deterministic Applications
- Determining When to Use Multiple CPUs
- Using Parallel Operations in Multiple-CPU RT Applications
- Avoiding Shared Resources

<!--NI_TOPIC bundle=labview-real-time-module path=organizing-and-managing-a-labview-project-with-the-real-time-module-real-time-module.html language=enus -->
## TOPIC 00049: Organizing and Managing a LabVIEW Project with the Real-Time Module

- bundle_id: `labview-real-time-module`
- source_path: `organizing-and-managing-a-labview-project-with-the-real-time-module-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/organizing-and-managing-a-labview-project-with-the-real-time-module-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use LabVIEW projects to group LabVIEW files and files not specific to LabVIEW, create build specifications, and deploy settings or deploy VIs to an RT target. You can create a project with the Real-Time Project Wizard or create a project with the Project Explorer window. You can add RT targets to a

### Organizing and Managing a LabVIEW Project with
 the Real-Time Module

Use LabVIEW projects to group LabVIEW files and files not specific to LabVIEW, create
 build specifications, and deploy settings or deploy VIs to an RT target. You can
 create a project with the Real-Time Project Wizard or create a project with the Project Explorer window. You can add RT targets to a project and configure the settings of an RT target from the Project
 Explorer window.

Parent topic:

Real-Time Module How-To

Related concepts:

- Creating a LabVIEW Project with the Real-Time Project Wizard
- Creating a LabVIEW Project with the Project Explorer Window
- Adding RT Targets to a LabVIEW Project
- Configuring RT Target Properties in a LabVIEW Project

<!--NI_TOPIC bundle=labview-real-time-module path=organizing-and-managing-a-labview-project-with-the-real-time-module.html language=enus -->
## TOPIC 00050: Organizing and Managing a LabVIEW Project with the Real-Time Module

- bundle_id: `labview-real-time-module`
- source_path: `organizing-and-managing-a-labview-project-with-the-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/organizing-and-managing-a-labview-project-with-the-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Before you design a project, you might find it useful to complete the exercises in the Getting Started with the LabVIEW Real-Time Module document to familiarize yourself with projects and other new features of the Real-Time Module.

### Organizing and Managing a LabVIEW Project
 with the Real-Time Module

Before you design a project, you might find it useful to complete the exercises in
 the Getting Started with the LabVIEW Real-Time Module document to familiarize
 yourself with projects and other new features of the Real-Time Module.

Parent topic:

Real-Time Module Concepts

<!--NI_TOPIC bundle=labview-real-time-module path=part-1-generating-data-on-the-rt-target-real-time-module.html language=enus -->
## TOPIC 00051: Part 1: Generating Data on the RT Target

- bundle_id: `labview-real-time-module`
- source_path: `part-1-generating-data-on-the-rt-target-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/part-1-generating-data-on-the-rt-target-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The real-time operating system on your RT target allows you to specify processes to run deterministically. A deterministic process has preferential access to hardware resources, meaning it executes within a bound time frame without risk of being interrupted by lower priority processes. In this tutor

### Part 1: Generating Data on the RT
 Target

The real-time operating system on your RT target allows you to specify processes to run
 deterministically. A deterministic process has preferential access to hardware
 resources, meaning it executes within a bound time frame without risk of being
 interrupted by lower priority processes. In this tutorial, we use a Timed Loop to
 specify a deterministic process that generates data on the RT target. In a
 producer/consumer design, we refer to this loop as the producer loop because it
 generates data for another loop to process. We discuss the consumer loop in the next
 part of this tutorial. Visit ni.com/info and enter
 PCdesign to learn about producer/consumer designs.

#### Setting up Your LabVIEW Project

Before you start designing your application, you need to add your RT target to a
 LabVIEW project, and then add a VI to run on your RT target. A VI runs on the
 hardware you add it to within the LabVIEW project hierarchy. If you add a VI to
 My Computer, it runs on the host computer. If you add a
 VI to the RT target project item, it runs on the RT target.

Complete the following steps to create your LabVIEW project:

1. In the LabVIEW Getting Started window, select
 File»Create Project to display the Create
 Project dialog box.
2. Select Blank Project and click
 Finish .
3. Select File»Save to save the project.
4. Name the project Getting Started .
5. Click OK.

Complete the following steps to discover your RT target:

1. In the Project Explorer window, right-click the project
 root and select New»Targets and Devices from the
 short-cut menu to display the Add Targets and Devices 
 dialog box.
2. Select Existing target or device .
3. Select Discover an existing target(s) or device(s) .
4. Specify the type of RT target you have in the Targets and Device
 Types list box. For example, if your RT target is a cRIO-9033,
 expand the Real-Time CompactRIO folder and select
 cRIO-9033 .
5. Click OK to display the Select Programming
 Mode dialog box.
6. (FPGA Targets) Select Scan Interface . Note You can select LabVIEW FPGA Interface instead of
 Scan Interface to program the FPGA for maximum
 performance and flexibility.
7. Click Continue .

Complete the following steps to add a new VI to your project:

1. Right-click the RT target in the Project Explorer window
 and select New»VI .
2. On the front panel, select File»Save to save the VI.
3. Name the VI Real-Time Main .
4. Click OK .

#### Creating a Timed Loop

The real-time operating system assigns priorities to every process in LabVIEW.
 Background tasks receive the lowest priority. LabVIEW processes receive low, normal,
 or high priority. VIs set to time-critical priority receive the highest priority.
 Timed Loops are deterministic structures that execute above high priority but below
 time-critical priority. When you add a Timed Loop to a VI, you must specify a period
 and priority for the loop. The period is the allotted execution time for one
 iteration of the loop. The priority tells LabVIEW which loop to execute first when
 there are multiple loops in the VI.

Note

Complete the following steps to configure a Timed Loop in the RT target VI:

1. Add a Timed Loop to the block diagram of Real-Time Main.vi using the
 Functions palette under
 Programming»Structures»Timed Structures .
2. Double-click the Input node of the Timed Loop to display the
 Configure Timed Loop dialog box.
3. Select 1 kHz Clock from the Source
 Type list box.
4. Enter 250 in the Period text box so that
 the loop runs four times per second. Note The period that you set
 should provide adequate time for the code within the Timed Loop to execute.
 Additionally, the period should allow extra time for lower priority
 processes to execute in order to prevent CPU starvation.
5. Enter 100 in the Priority text box.
6. Click OK .
7. Right-click the Loop Condition terminal of the Timed Loop and select
 Create Control from the short-cut menu. LabVIEW adds
 a Stop button to the front panel.

#### Adding Code to Generate Data

In this section, you use a Random Number function to generate data on the RT target.
 The Random Number function is a placeholder for application-specific code. For
 real-world applications, replace the Random Number function with code that generates
 data you want to process deterministically.

Complete the following steps to generate and display data:

1. Add a Random Number function inside the Timed Loop.
2. Right-click the Random Number function and select
 Create»Indicator from the short-cut menu. Note As a best practice, do not include indicators inside
 time-critical code. It is important to generate data deterministically, but
 it is not important to display data deterministically. The indicator in this
 step is for testing that the RT target generates data. You remove it in a
 later part of this tutorial.
3. Save the VI.

The block diagram should match the following image.

[IMAGE alt='image' src='GUID-CAD9DB3C-9BD2-487E-99D5-74C0D3CF9510-a5.png']

#### Running a VI on Your RT Target

Before you can start running the code, you must enable the VI to run on the RT target
 by deploying it. When you deploy the VI, LabVIEW saves the VI and any associated
 files to the RT target memory.

Complete the following steps to deploy the VI to your RT target:

1. In the Project Explorer window, right-click the RT
 target and select Properties from the short-cut menu to
 display the RT Target Properties dialog box.
2. Specify the IP address in the IP Address / DNS Name text box. Note You
 can use Measurement & Automation Explorer (MAX) to
 determine the IP address for your RT target.
3. Click OK .
4. In the Project Explorer window, right-click the VI and
 select Deploy from the short-cut menu.

#### Result

When you run Real-Time Main.vi, the RT target deterministically produces random
 numbers, and the indicator displays the numbers on the front panel.

Parent topic:

Tutorial: Creating a Real-Time Application

Related concepts:

- Tutorial: Creating a Real-Time Application
- Part 2: Processing Data on the RT Target

<!--NI_TOPIC bundle=labview-real-time-module path=part-2-processing-data-on-the-rt-target-real-time-module.html language=enus -->
## TOPIC 00052: Part 2: Processing Data on the RT Target

- bundle_id: `labview-real-time-module`
- source_path: `part-2-processing-data-on-the-rt-target-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/part-2-processing-data-on-the-rt-target-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: In this part of the tutorial, you create the consumer loop that processes the data generated by the producer loop. The consumer loop uses a While Loop instead of a Timed Loop because processing the data is a lower priority task than generating the data. That is, if hardware resources become limited,

### Part 2: Processing Data on the RT
 Target

In this part of the tutorial, you create the consumer loop that processes the data
 generated by the producer loop. The consumer loop uses a While Loop instead of a
 Timed Loop because processing the data is a lower priority task than generating the
 data. That is, if hardware resources become limited, it is more important to
 generate the data within a bound timeframe than it is to process it.

[IMAGE alt='image' src='GUID-E409C7BB-01E0-4622-A036-A77F64FE3C74-a5.png']

#### Creating the Consumer Loop

It is typical to synchronize the While Loop and the Timed Loop using a Wait Until
 Next ms Multiple function. Synchronizing the loops in this fashion is not necessary,
 but it provides the While Loop with the execution time that remains in a period
 after the Timed Loop finishes executing.

Complete the following steps to create a consumer loop with the same period as a
 producer loop:

1. Within the block diagram of Real-Time Main.vi, place a While Loop below the
 Timed Loop.
2. Place a Wait Until Next ms Multiple function within the While Loop.
3. Right-click the millisecond multiple input of the Wait
 Until Next ms Multiple function and select
 Create»Constant from the short-cut menu.
4. Enter 250 as the constant to match the period of the Timed
 Loop.

#### Transferring Data Deterministically from the Producer Loop to the Consumer
 Loop

LabVIEW provides many methods for transferring data, some of which are deterministic
 and some of which are not. RT FIFOs are an example of a deterministic data
 communication method. To achieve determinism, RT FIFOs preallocate memory for the
 data transfer before run time, thereby preventing unforeseen delays writing to
 memory. RT FIFOs buffer and transfer data in a first-in, first-out order. You can
 find the RT FIFO functions on the Functions palette under Real-Time»RT
 FIFO. Refer to the Data Communication
 Methods in LabVIEW help topic to learn about other data communication
 methods available to you.

Complete the following steps to transfer data from the producer loop to the consumer
 loop using RT FIFOs:

1. Place an RT FIFO Create function outside and to the left of the loops.
2. Replace the indicator in the Timed Loop with an RT FIFO Write function. Note Make sure to wire the output of the Random Number function to
 the element input of the RT FIFO Write
 function.
3. Place an RT FIFO Read function inside the While Loop.
4. Place an RT FIFO Delete function outside and to the right of the loops.
5. Wire a DBL Numeric Constant to the type input of the RT
 FIFO Create function.
6. Wire the rt fifo output of the RT FIFO Create function to
 the rt fifo input of the other three RT FIFO
 functions.
7. Right-click the Loop Condition icon of the While Loop and select
 Create Control from the short-cut menu to create a
 Stop button.
8. Place a Case structure within the While Loop.
9. Select False in the Case structure selector label.
10. Wire the empty? output of the RT FIFO Read function to
 the case selector of the Case structure.
11. Right-click the element out output of the RT FIFO Read
 function and select Create»Indicator from the short-cut
 menu.
12. Place the indicator inside the Case structure.
13. Wire the indicator to the element out output of the RT
 FIFO Read function.

#### Adding Error Handling

It is a best practice to wire the error terminals for functions. This allows you to
 pass error information through the VI and handle errors appropriately without
 suspending the execution of the VI.

Complete the following steps to wire errors in Real-Time Main.vi:

1. Resize the Input node of the Timed Loop to include five inputs.
2. Right-click the bottom input of the Timed Loop Input node and select
 Select Input»Error from the short-cut menu.
3. Wire the error out output of the RT FIFO Create function
 to the Error input of the Timed Loop Input node.
4. Wire the Error output of the Left Data node of the Timed
 Loop to the error in input of the RT FIFO Write
 function.
5. Wire the error out output of the RT FIFO Write function
 to the Error input of the Right Data node of the Timed
 Loop.
6. Place a Merge Errors function outside and to the right of the loops.
7. Wire the Error output of the Output node of the Timed
 Loop to the top input of the Merge Errors function.
8. Wire the error out output of the RT FIFO Create function
 to the error in input of the RT FIFO Read function.
9. Wire the error out output of the RT FIFO Read function
 through the Case structure and to the bottom error in 
 input of the Merge Errors function.
10. Wire the error out output of the Merge Errors function to
 the error in input of the RT FIFO Delete function.
11. Right-click the error out output of the RT FIFO Delete
 function and select Create»Indicator .
12. Right-click one of the two While Loop error tunnels and select
 Replace with Shift Register from the short-cut
 menu.
13. Click the other While Loop error tunnel to replace it with a shift
 register.
14. Select True in the Case structure selector label.
15. Connect the error wire through the Case structure.
16. Save the VI.
17. In the Project Explorer window, right-click the VI and
 select Deploy from the short-cut menu.

#### Result

When you run Real-Time Main.vi, the producer loop assumes highest priority and writes
 values generated by the RT target to the RT FIFO buffer. The consumer loop reads the
 values from the RT FIFO buffer whenever the CPU is available during each period.

Note

Parent topic:

Tutorial: Creating a Real-Time Application

Related concepts:

- Part 1: Generating Data on the RT Target
- Tutorial: Creating a Real-Time Application
- Part 3: Stopping Multiple Loops Simultaneously

<!--NI_TOPIC bundle=labview-real-time-module path=part-3-stopping-multiple-loops-simultaneously-real-time-module.html language=enus -->
## TOPIC 00053: Part 3: Stopping Multiple Loops Simultaneously

- bundle_id: `labview-real-time-module`
- source_path: `part-3-stopping-multiple-loops-simultaneously-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/part-3-stopping-multiple-loops-simultaneously-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Creating a safe shutdown procedure is a fundamental component of a real-time application. For example, if one part of your application controls a piece of equipment and another part of your application monitors for alarm conditions, you may want to stop the equipment when you encounter an alarm cond

### Part 3: Stopping Multiple Loops
 Simultaneously

Creating a safe shutdown procedure is a fundamental component of a real-time
 application. For example, if one part of your application controls a piece of
 equipment and another part of your application monitors for alarm conditions, you
 may want to stop the equipment when you encounter an alarm condition. In such a
 scenario, you can use a network-published shared variable to merge the stop and
 error functions of multiple loops into one.

[IMAGE alt='image' src='GUID-555256A3-7405-4625-91A5-9E933A9E0A15-a5.png']

#### Creating a Shared Variable

Network-published shared variables are ideal for broadcasting shutdown events because
 they can communicate to multiple VIs and because the read and write operations for
 network-published shared variables do not block each other.

Complete the following steps to configure a network-published shared variable:

1. In the Project Explorer window, right-click the RT target
 and select New»Variable from the short-cut menu to
 display the Shared Variable Properties dialog box.
2. Configure the variable by completing the following steps:
  1. In the Variable page of the Shared
 Variable Properties dialog box, enter
 Active? in the Name text
 box.
  2. Select Network-Published from the
 Variable Type pull-down menu.
  3. Select Boolean from the Data
 Type pull-down menu.
  4. In the RT FIFO page of the Shared
 Variable Properties dialog box, place a check mark in
 the Enable RT FIFO check box.
  5. Click OK .
3. In the Project Explorer window, right-click the library
 that contains the Active? variable and select
 Save»Save from the short-cut menu.
4. Name the library Variables .
5. Click OK .
6. Click and drag the Active? variable from the Project
 Explorer window onto the block diagram of Real-Time Main.vi and
 place it to the left of the RT FIFO Create function.
7. Right-click the Active? variable and select Access
 Mode»Write from the short-cut menu.
8. Wire a True constant to the Active? input of the
 Active? variable.

#### Initializing the Variable

When you launch your application, many parts of code load in parallel. This means
 that some parts of your application might load before other parts are ready. To
 prevent the application from stopping because of insufficient initialization time
 for the network-published shared variable, it is a best practice to check for proper
 initialization using a While Loop.

Complete the following steps to initialize the Active? variable:

1. Add a While Loop between the Active? variable and the RT FIFO
 Create function.
2. Create a copy of the Active? variable and place it within the
 While Loop.
3. Right-click the Active? variable within the While Loop and
 select Access Mode»Read from the short-cut menu.
4. Add an Unbundle by Name function within the While Loop.
5. Wire the Unbundle by Name function input to the error out 
 output of the Active? variable.
6. Right-click the Unbundle by Name function and select Select
 Item»Code from the short-cut menu.
7. Add a Not Equal? function within the While Loop.
8. Wire the code output of the Unbundle by Name function to
 the x input of the Not Equal? function.
9. Right-click the y input of the Not Equal? function and
 select Create»Constant from the short-cut menu.
10. Enter -1950679034 as the constant. This is the error code
 that LabVIEW returns if the shared variable has no value.
11. Wire the x!=y? output of the Not Equal? function to the
 stop condition of the While Loop.
12. Add a Wait (ms) function within the While Loop.
13. Right-click the milliseconds to wait input of the Wait
 (ms) function and select Create»Constant from the
 short-cut menu.
14. Enter 10 as the constant to check whether the variable is
 initialized every 10 milliseconds.

#### Creating the Shutdown Condition

A shutdown condition ensures that every process stops when there is a critical error
 in one part of the application or when the user stops the application.

Complete the following steps to create a safe shutdown condition using the shared
 variable:

1. Wire the error out output of the Active? 
 variable to the error in input of the
 Active? variable within the While Loop.
2. Wire the error out output of the Active? 
 variable within the While Loop to the error in input of
 the RT FIFO Create function.
3. Delete the error wire between the RT FIFO Write function and the Right Data node
 of the Timed Loop.
4. Delete the error wire between the Output node of the Timed Loop and the Merge
 Errors function.
5. Copy the Active? variable and paste the copy within the Timed
 Loop and to the right of the RT FIFO Write function.
6. Wire the error out output of the RT FIFO Write function
 to the error in input of the Active? 
 variable within the Timed Loop.
7. Right-click the Active? variable within the Timed Loop and
 select Access Mode»Read from the short-cut menu.
8. Place a Not function to the right of the Active? variable
 within the Timed Loop.
9. Wire the Active? output of the Active? 
 variable to the x input of the Not function.
10. Place an Or function to the right of the Not function.
11. Wire the .not. x? output of the Not function to the
 x input of the Or function.
12. Wire the error out output of the Active? 
 variable within the Timed Loop to the y input of the Or
 function.
13. Place a Case structure outside and to the right of the Timed Loop.
14. Connect the error wire of the Active? variable within the Timed
 Loop to the Error input of the Right Data node of the
 Timed Loop.
15. Wire the Error output of the Output node of the Timed
 Loop to the case selector of the Case structure.
16. With Error selected in the selector label, place a copy of the
 Active? variable within the Case structure.
17. Right-click the Active? variable and select Access
 Mode»Write from the short-cut menu.
18. Wire a False constant to the Active? input of the
 Active? variable.
19. Connect the error wire through the Case structure, but do not wire it to the
 Active? variable. Note Make sure to complete
 this step again with No Error selected in the selector
 label.
20. Connect the error wire leaving the Case structure to the error
 in input of the Merge Errors function.
21. Delete the Stop button of the Loop Condition for the Timed Loop.
22. Wire the x .or. y? output of the Or function to the Loop
 Condition of the Timed Loop.
23. Repeat steps 3 through 22 for the consumer loop to match the image. Note Make sure that the error wire from the RT FIFO Read function
 to the Active? variable goes through the Case
 structure.
24. Save the VI.

#### Stopping the VI

At this point in the tutorial, the VI runs continuously because you cannot change the
 Active? variable to False from the front panel. To stop the VI,
 you can use the NI Distributed System Manager to change the value of the
 Active? variable. The NI Distributed System Manager is a useful
 tool for monitoring your network-published shared variables while your code is
 executing.

Complete the following steps to shut down the VI without using the Abort Execution
 button.

1. Open the NI Distributed System Manager.
2. Expand the Network Items folder in the
 Name column.
3. Locate and expand your RT target root.
4. Expand the Variables folder.
5. Select the Active? variable.
6. In the Auto View window, set New
 Value to False .
7. Click Set .
8. Close the Distributed System Manager.

#### Result

When you run the VI, the loops stop simultaneously if the Active?
 variable is False or if LabVIEW detects an error.

Parent topic:

Tutorial: Creating a Real-Time Application

Related concepts:

- Part 2: Processing Data on the RT Target
- Tutorial: Creating a Real-Time Application
- Part 4: Building the User Interface

<!--NI_TOPIC bundle=labview-real-time-module path=part-4-building-the-user-interface-real-time-module.html language=enus -->
## TOPIC 00054: Part 4: Building the User Interface

- bundle_id: `labview-real-time-module`
- source_path: `part-4-building-the-user-interface-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/part-4-building-the-user-interface-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: While many RT targets run headless, it is often useful to display information from the RT target or send commands to the real-time application. To accomplish these tasks, you can create a user interface that runs on the host computer or on the RT target (for RT targets that support the embedded UI o

### Part 4: Building the User Interface

While many RT targets run headless, it is often useful to display information from
 the RT target or send commands to the real-time application. To accomplish these
 tasks, you can create a user interface that runs on the host computer or on the RT
 target (for RT targets that support the embedded UI or remote front panels). In this
 part of the tutorial, we create a UI that allows the user to stop the real-time
 application from the host computer.

[IMAGE alt='image' src='GUID-0513D353-7E5A-47A0-ACCD-D5A18B64009A-a5.png']

#### Adding a VI to the Host Computer

Unlike RT target VIs, you do not need to deploy a host computer VI before running.
 Because you are developing on the host computer, LabVIEW automatically saves the VI
 to the computer.

Complete the following steps to add a new VI to the host computer:

1. In the Project Explorer window, right-click My
 Computer and select New»VI from the
 short-cut menu.
2. In the front panel, select File»Save to save the VI.
3. Name the VI Windows Main .
4. Click OK .

#### Creating an Event Case to Stop the Application

In the tutorial's UI, the Event structure waits for the user to press the Stop
 button. You set the period of the Event structure to match the Timed Loop to
 synchronize the Event structure with the loops running on the RT target.

Complete the following steps to create an Event structure that waits for the user to
 press the Stop button:

1. Add a Stop button to the front panel of Window Main.vi.
2. Enter Stop Application in the Stop button label.
3. Add a While Loop to the block diagram of the VI.
4. Add an Event structure within the While Loop.
5. Right-click the selector label of the Event structure and select Add
 Event Case from the short-cut menu to display the
 Edit Events dialog box.
6. Select Stop Application in the Event
 Sources list box.
7. Select Value Change in the Events 
 list box.
8. Click OK .
9. Place the Stop Application control within the Event
 structure.
10. Right-click the Event Timeout terminal of the Event structure and select
 Create Constant from the short-cut menu.
11. Enter 250 as the constant to match the period of the Timed Loop
 in Real-Time Main.vi.

#### Synchronizing the Stop Functions of Both VIs

This section explains how to synchronize the stop functions of all of the loops in
 the application using the same shared variable that you used in Real-Time Main.vi.
 With the entire application linked to one Stop button, you can stop all processes
 within the application safely and simultaneously.

Complete the following steps to synchronize the stop functions of the
 application:

1. Place a copy of the Active? variable within the Event structure
 in Windows Main.vi.
2. Right-click the Active? variable and select Access
 Mode»Write from the short-cut menu.
3. Add a Not function within the Event structure.
4. Add an Or function outside of the Event structure but within the While
 Loop.
5. Wire the output of the Stop Application control to the
 x input of the Not function.
6. Wire the output of the Stop Application control to the
 x input of the Or function.
7. Wire the .not. x? output of the Not function to the
 Active? input of the Active? 
 variable.
8. Wire the x .or. y? output of the Or function to the
 conditional terminal of the While Loop.

#### Adding Error Handling

As in other parts of the tutorial, it is recommended to wire the error terminals for
 functions.

Complete the following steps to connect error wires in Windows Main.vi:

1. Right-click the error out output of the
 Active? variable and select
 Create»Indicator from the short-cut menu.
2. Right-click the error in input of the
 Active? variable and select
 Create»Constant from the short-cut menu.
3. Place the error in constant outside and to the left of
 the While Loop.
4. Wire the error in constant through the While Loop and the
 Event structure and connect it to the error in input of
 the Active? variable.
5. Wire the error out output of the Active? 
 variable to the y input of the Or function.
6. Place the error out indicator outside and to the right of
 the While Loop.
7. Wire the error out output of the Active? 
 variable to the input of the error out indicator.
8. Select Timeout in the Event structure selector
 label.
9. Connect the error wire through the Event structure.
10. Right-click one of the two While Loop error tunnels and select
 Replace with Shift Register from the short-cut
 menu.
11. Click the other While Loop error tunnel to replace it with a shift
 register.
12. Save the VI.

#### Result

When you run Real-Time Main.vi and Windows Main.vi and click the Stop
 Application button in Windows Main.vi, LabVIEW stops the entire
 application, including the loops running within Real-Time Main.vi.

Parent topic:

Tutorial: Creating a Real-Time Application

Related concepts:

- Part 3: Stopping Multiple Loops Simultaneously
- Tutorial: Creating a Real-Time Application
- Part 5: Sending RT Data to the Host Computer

<!--NI_TOPIC bundle=labview-real-time-module path=part-5-sending-rt-data-to-the-host-computer-real-time-module.html language=enus -->
## TOPIC 00055: Part 5: Sending RT Data to the Host Computer

- bundle_id: `labview-real-time-module`
- source_path: `part-5-sending-rt-data-to-the-host-computer-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/part-5-sending-rt-data-to-the-host-computer-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: In this part of the tutorial you use Network Streams functions to send streaming data across the network. Refer to the Data Communication Methods in LabVIEW topic in the LabVIEW Help for information about other methods of data transfer. Configuring the Network Stream Writer To configure a network st

### Part 5: Sending RT Data to the Host
 Computer

In this part of the tutorial you use Network Streams functions to send streaming data
 across the network. Refer to the Data Communication
 Methods in LabVIEW topic in the LabVIEW Help for
 information about other methods of data transfer.

[IMAGE alt='image' src='GUID-74436463-E39F-47B9-827F-709028EE6FE1-a5.png']

#### Configuring the Network Stream Writer

To configure a network stream for sending data, you must specify the writer name,
 data type, and writer buffer size. These properties specify the endpoint sending the
 data, the type of data being sent, and how much data to send.

Complete the following steps to configure a Create Network Stream Writer Endpoint
 function:

1. Add a Create Network Stream Writer Endpoint function to the block diagram of
 Real-Time Main.vi.
2. Delete the error wire between the RT FIFO Create function and the RT FIFO Read
 function.
3. Connect the error wires sequentially between the RT FIFO Create function, the
 Create Network Stream Writer Endpoint function, and the RT FIFO Read
 function.
4. Right-click the writer name input of the Create Network
 Stream Writer Endpoint function and select
 Create»Constant from the short-cut menu.
5. Enter RTAcqData as the constant to name the writer
 endpoint.
6. Wire a DBL Numeric Constant to the data type input of the
 Create Network Stream Writer Endpoint function.
7. Right-click the writer buffer size input of the Create
 Network Stream Writer Endpoint function and select
 Create»Constant from the short-cut menu. Note The buffer size you set should be large enough to accommodate
 the data you need to stream. Using an inadequate buffer size results in
 errors.
8. Set the constant to 4096 .

#### Transferring Data from the RT FIFO Function to the Network Stream

Like RT FIFOs, network streams transfer buffered data. However, because networks
 streams transfer data over the network instead of within the RT target, they do not
 guarantee deterministic communication. All network communication is inherently
 non-deterministic because execution time and transfer rates over a network vary from
 iteration to iteration.

Complete the following steps to set up a network stream writer to stream data to the
 network:

1. Select False from the Case structure selector label.
2. Add a Write Single Element to Stream function within the Case structure.
3. Delete the error wire running through the Case structure.
4. Connect the error wires sequentially between the RT FIFO Read function, the
 Write Single Element to Stream function, and the Active? 
 variable.
5. Wire the writer endpoint output of the Create Network
 Stream Writer Endpoint function to the endpoint in input
 of the Write Single Element to Stream function.
6. Delete the error out indicator.
7. Wire the element out output of the RT FIFO Read function
 to the data in input of the Write Single Element to
 Stream function.
8. Add a Destroy Stream Endpoint function outside and to the right of the loops.
 This function closes the network stream safely.
9. Delete the error wire between the Merge Errors function and the RT FIFO Delete
 function.
10. Connect the error wires sequentially between the Merge Errors function, the
 Destroy Stream Endpoint function, and the RT FIFO Delete function.
11. Wire the endpoint out output of the Write Single Element
 to Stream function to the endpoint in input of the
 Destroy Stream Endpoint function.
12. Select True from the Case structure selector label.
13. Connect the error wire through the Case structure.
14. Connect the endpoint wire through the Case structure.
15. Save the VI.

#### Result

Do not run your VI at this time. The network stream can send data using the writer
 endpoint, but it cannot receive data until you add a reader endpoint. You can test
 your VI after you add a reader endpoint in the next part of this tutorial.

Parent topic:

Tutorial: Creating a Real-Time Application

Related concepts:

- Part 4: Building the User Interface
- Tutorial: Creating a Real-Time Application
- Part 6: Displaying RT Data on the User Interface

<!--NI_TOPIC bundle=labview-real-time-module path=part-6-displaying-rt-data-on-the-user-interface-real-time-module.html language=enus -->
## TOPIC 00056: Part 6: Displaying RT Data on the User Interface

- bundle_id: `labview-real-time-module`
- source_path: `part-6-displaying-rt-data-on-the-user-interface-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/part-6-displaying-rt-data-on-the-user-interface-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: In this part of the tutorial, you use network streams to receive RT target data over the network. You also display the data graphically on the user interface. Visit ni.com/info and enter EmbUIOptions to learn more about creating interfaces for displaying RT target data. Configuring the Network Strea

### Part 6: Displaying RT Data on the User
 Interface

In this part of the tutorial, you use network streams to receive RT target data over
 the network. You also display the data graphically on the user interface. Visit
 ni.com/info and enter EmbUIOptions to
 learn more about creating interfaces for displaying RT target data.

[IMAGE alt='image' src='GUID-497E4030-CA61-4545-A310-4EFBB6C9EF54-a5.png']

#### Configuring the Network Stream Reader

To configure a network stream for receiving data, you must specify the reader name,
 data type, and reader buffer size. These properties specify the endpoint reading the
 data, the type of data being read, and how much data to read. You also specify a
 time limit, which specifies how long the reader endpoint waits for data.

Complete the following steps to configure a Create Network Stream Reader Endpoint
 function:

1. Add a Create Network Stream Reader Endpoint function to the block diagram of
 Windows Main.vi.
2. Delete the error wire between the error in constant and
 the left error tunnel of the While Loop.
3. With Stop Application selected in the Event structure selector
 label, connect the error wires sequentially between the error in constant, the Create Network Stream Reader Endpoint function, and
 the Active? variable.
4. Right-click the reader name input of the Create Network
 Stream Reader Endpoint function and select
 Create»Constant from the short-cut menu.
5. Enter HostDataReader as the constant to name the reader
 endpoint.
6. Wire a DBL Numeric Constant to the data type input of the
 Create Network Stream Reader Endpoint function.
7. Right-click the timeout in ms input of the Create Network
 Stream Reader Endpoint function and select
 Create»Constant from the short-cut menu.
8. Enter 1000 as the constant to specify that the reader waits one
 second for new data before passing execution to the next part of the VI.
9. Right-click the reader buffer size input of the Create
 Network Stream Reader Endpoint function and select
 Create»Constant from the short-cut menu.
10. Enter 4096 as the constant.

#### Creating a Control to Specify the RT Target

Before a network stream can read data, it needs the IP address or hostname of the RT
 target sending the data.

Complete the following steps to create a control on the front panel to specify the IP
 address of your RT target:

1. Add a Concatenate Strings function to the left of the Create Network Stream
 Reader Endpoint function.
2. Expand the Concatenate Strings function to include three inputs.
3. Right-click the top input of the Concatenate Strings function and select
 Create»Constant from the short-cut menu.
4. Enter // as the constant.
5. Right-click the bottom input of the Concatenate Strings function and select
 Create»Constant from the short-cut menu.
6. Enter /RTAcqData as the constant to specify the writer
 endpoint.
7. Add a string control to the front panel.
8. Name the string control Target IP Address .
9. In the Target IP Address text box, enter the IP address
 for your RT target. Note Any time you reopen the application,
 ensure that the IP address you enter in the front panel matches the IP
 address of your RT target. Depending on your network settings, the IP
 address of your RT target may change.
10. In the block diagram, wire the Target IP Address control
 to the middle input of the Concatenate Strings function.
11. Wire the concatenated string output of the Concatenate
 Strings function to the writer URL input of the Create
 Network Stream Reader Endpoint function.

#### Receiving Streaming Data from the RT Target

Similar to the network streams writer endpoint, the reader endpoint requires a Read
 Single Element from Stream function and a Destroy Stream Endpoint function to
 receive data.

Complete the following steps to complete the networks streams reader endpoint in
 Window Main.vi:

1. With Timeout selected in the selector label, place a Read
 Single Element from Stream function within the Event structure.
2. Add a Destroy Stream Endpoint function outside and to the right of the While
 Loop.
3. Delete the error wire between the While Loop and the error
 out indicator.
4. Delete the error wire within the Event structure.
5. Connect the error wires sequentially between the Create Network Stream Reader
 Endpoint function, the Read Single Element from Stream function, the Destroy
 Stream Endpoint function, and the error out 
 indicator.
6. Wire the reader endpoint output of the Create Network
 Stream Reader Endpoint function to the endpoint in input
 of the Read Single Element from Stream function.
7. Wire the endpoint out output of the Read Single Element
 from Stream function to the endpoint in input of the
 Destroy Stream Endpoint function.

#### Displaying the Data in the Front Panel

To display the data from the RT target on the UI, you can use a waveform chart.

Complete the following steps to display the data from the RT target on the Windows
 Main.vi front panel:

1. Right-click the data out output of the Read Single
 Element from Stream function and select Create»Indicator 
 from the short-cut menu.
2. In the front panel, right-click the data out indicator
 and select Replace»Silver»Graph»Waveform Chart from the
 short-cut menu.
3. In the block diagram, right-click the Boolean tunnel in the Event structure and
 select Create»Constant from the short-cut menu.
4. Specify a False constant.
5. Save the VI.
6. Run Real-Time Main.vi.
7. Run Windows Main.vi.

The front panel should match the following image.

[IMAGE alt='image' src='GUID-CE4B4C60-6055-4456-9295-5D5C1CA6B278-a5.png']

Parent topic:

Tutorial: Creating a Real-Time Application

Related concepts:

- Part 5: Sending RT Data to the Host Computer
- Tutorial: Creating a Real-Time Application
- Related Documentation

<!--NI_TOPIC bundle=labview-real-time-module path=pipelining-to-optimize-multiple-cpu-rt-applications-real-time-module.html language=enus -->
## TOPIC 00057: Pipelining to Optimize Multiple-CPU RT Applications

- bundle_id: `labview-real-time-module`
- source_path: `pipelining-to-optimize-multiple-cpu-rt-applications-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/pipelining-to-optimize-multiple-cpu-rt-applications-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use pipelining to increase the throughput of a sequential process in an RT application that runs on a system with multiple CPUs, also known as a multi-core, multi-processor, or SMP system. Pipelining Using a While Loop The most streamlined way to implement a pipeline is to use a While Loop a

### Pipelining to Optimize Multiple-CPU RT Applications

You can use pipelining to increase the throughput of a sequential process in an RT
 application that runs on a system with multiple CPUs, also known as a multi-core,
 multi-processor, or SMP system.

#### Pipelining Using a While Loop

The most streamlined way to implement a pipeline is to use a While Loop and pass data through shift registers.

#### Pipelining Using a Timed Loop

If you want to use features such as priorities or manual CPU assignment, use the
 Timed Loop. You cannot use shift registers in a Timed Loop to implement a pipeline
 because LabVIEW treats each Timed Loop as a single thread. To implement a pipeline
 with Timed Loops, you must place each pipeline stage in a parallel Timed Loop and
 pass data between the Timed Loops using a queue, a local variable, a global variable,
 or an RT FIFO. The following block diagram demonstrates the
 use of an RT FIFO to implement a pipeline.

[IMAGE alt='image' src='GUID-630E9686-417D-42E7-B4FC-1D12B0C1E2BC-a5.png']

#### Selecting the Data Transfer Method

The pipeline dataflow works differently depending on the method you use to transfer
 data. The method you choose should reflect whether the application requires each
 pipeline input to correspond one-to-one to a pipeline output.

- RT FIFO —To ensure that pipeline inputs correspond
 one-to-one to pipeline outputs, you must use a method that waits for each data
 element. The previous example creates an RT FIFO and uses the timeout
 in ms input of the RT FIFO Read
 function to ensure that subVI B does not execute until the data from subVI A is
 available.
- Local or Global Variable —If the application does not
 require pipeline inputs to correspond one-to-one to pipeline outputs, you can
 transfer data using a local or global variable or a single-element RT FIFO with
 a zero timeout.

For more information about the advantages and disadvantages of various data transfer
 methods, refer to the topics in the Sharing Data in Deterministic Applications book.

#### Automatic Load Balancing

When you use Timed Loops to implement a pipeline, the CPU scheduler performs
 automatic load balancing to distribute execution threads across multiple CPUs. You
 also can use the Assigned CPU input of the Timed
 Loop to manually assign each Timed Loop to a particular CPU for increased
 execution control.

Tip

#### Additional Resources for Optimizing Multiple-CPU RT Systems

Refer to the Multicore Programming Resources at ni.com/info and
 enter RTSMP for more information about optimizing
 performance in a multiple-CPU RT system.

Parent topic:

Optimizing RT Applications for Multiple-CPU Systems

Related concepts:

- Sharing Data in Deterministic Applications

<!--NI_TOPIC bundle=labview-real-time-module path=reading-and-writing-shared-variable-values-deterministically-real-time-module.html language=enus -->
## TOPIC 00058: Reading and Writing Shared Variable Values Deterministically

- bundle_id: `labview-real-time-module`
- source_path: `reading-and-writing-shared-variable-values-deterministically-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/reading-and-writing-shared-variable-values-deterministically-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: After you create a shared variable, you can access the shared variable data from VIs using a Shared Variable node. A Shared Variable node is a block diagram object that references a shared variable in the Project Explorer window. Use a Shared Variable node to read and write values to a shared variab

### Reading and Writing Shared Variable Values
 Deterministically

After you create a shared
 variable, you can access the shared variable data from VIs using a Shared
 Variable node. A Shared Variable node is a block diagram object that references a
 shared variable in the Project Explorer window. Use a Shared
 Variable node to read and write values to a shared variable. Drag a shared variable
 from the Project Explorer window to the block diagram of a VI
 to create a Shared Variable node.

You also can place a Shared Variable node from the Data Communication
 palette on the block diagram. To bind a Shared Variable node on the block diagram to
 a shared variable in the active project, right-click the Shared Variable node and
 select Select Variable»Browse from the shortcut menu to open
 the Browse for Variable dialog box. Select a shared variable
 from the tree control and click the OK button.

By default, the Shared Variable node is set to read. To change the Shared Variable
 node on the block diagram to write, right-click the Shared Variable node and select
 Change to Write from the shortcut menu.

#### Sharing Data Locally on the RT Target

Use a single-process shared variable with the real-time FIFO enabled to share data
 between two locations in a block diagram that cannot be connected with wires or
 between two VIs running on an RT target. Enabling the
 real-time FIFO of a shared variable ensures that sharing data from
 deterministic sections of a block diagram or VIs running on an RT target does not
 affect the determinism of the section of the block diagram or VI.

The following block diagram shows a VI that runs on an RT target and uses two Timed
 Loops to acquire waveform data and then log the data to file. The VI uses
 a single-process shared variable with the real-time FIFO enabled,
 RT_Single-Process, to share data between a deterministic
 Timed Loop, labeled Deterministic Acquisition Loop, and a lower priority Timed Loop,
 labeled Data Logging Loop. With the real-time FIFO of the shared variable enabled, the
 Deterministic Acquisition Loop can share data with the Data Logging Loop without
 affecting the determinism of the data acquisition.

[IMAGE alt='image' src='GUID-E7F0239F-52E7-4A86-9848-2BEFBF960763-a5.png']

#### Sharing Data with a Remote Target

Use a network-published shared variable with the real-time FIFO enabled to share data
 between VIs on different targets. enabling the
 real-time FIFO of a shared variable ensures that sharing data from a
 deterministic VI across a network does not affect the determinism of the VI.

The following block diagram shows a VI that runs on a host computer and publishes a
 Boolean value to stop a VI on an RT target. The host VI writes the Boolean value to
 a network-published shared variable with the real-time FIFO enabled,
 RT_Network-Published.

[IMAGE alt='image' src='GUID-D2085419-0930-4642-8A31-FD6F397D68CB-a5.png']

By enabling the real-time FIFO of the shared variable, the Deterministic Acquisition
 Loop in the following block diagram can receive data from across a network without
 affecting the determinism of the data acquisition. You also can share data from the
 Deterministic Acquisition Loop using a network-published shared variable with the
 real-time FIFO enabled.

[IMAGE alt='image' src='GUID-15DA2BA2-1ED4-4781-A2A7-67EF3633EA82-a5.png']

Parent topic:

Sharing Data in Deterministic Applications

<!--NI_TOPIC bundle=labview-real-time-module path=real-time-module-best-practices.html language=enus -->
## TOPIC 00059: Real-Time Module Best Practices

- bundle_id: `labview-real-time-module`
- source_path: `real-time-module-best-practices.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/real-time-module-best-practices.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Developing complex LabVIEW Real-Time applications requires an understanding of how LabVIEW maps to the real-time computing model. Some LabVIEW programming strategies that work well when developing for a general-purpose operating system do not translate to the headless, priority-driven execution mode

### Real-Time Module Best Practices

Developing complex LabVIEW Real-Time applications requires an understanding of how


 LabVIEW maps to the real-time computing model. Some LabVIEW programming strategies


 that work well when developing for a general-purpose operating system do not


 translate to the headless, priority-driven execution model of a real-time operating


 system (RTOS).

This documentation provides best practices for designing, developing, and deploying applications
 with the LabVIEW Real-Time Module. Following these
 best practices can mean the difference between
 success and failure for a deployed system. Use the
 *RT Best Practices Portal* as a
 graphical navigation window for finding best
 practices documents.

Related concepts:

- What is the Real-Time Module?
- RT Best Practices Portal

<!--NI_TOPIC bundle=labview-real-time-module path=real-time-module-concepts.html language=enus -->
## TOPIC 00060: Real-Time Module Concepts

- bundle_id: `labview-real-time-module`
- source_path: `real-time-module-concepts.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/real-time-module-concepts.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The topics in this section introduce the LabVIEW Real-Time Module and real-time programming techniques to help you build deterministic applications.

### Real-Time Module Concepts

The topics in this section introduce the LabVIEW Real-Time Module and real-time programming
 techniques to help you build deterministic
 applications.

- [Introduction to the LabVIEW Real-Time Module](introduction-to-the-labview-real-time-module-real-time-module.html)
- [Organizing and Managing a LabVIEW Project with the Real-Time Module](organizing-and-managing-a-labview-project-with-the-real-time-module.html)
- [Creating Deterministic Applications](creating-deterministic-applications-real-time-module.html)
- [Sharing Data in Deterministic Applications](sharing-data-in-deterministic-applications.html)
- [Timing Deterministic Applications](timing-deterministic-applications-real-time-module.html)
- [Creating Stand-Alone Real-Time Applications](creating-stand-alone-real-time-applications-real-time-module.html)
- [Debugging Deterministic Applications](debugging-deterministic-applications-real-time-module.html)
- [Optimizing Deterministic Applications](optimizing-deterministic-applications-real-time-module.html)
- [Interacting with the Front Panels of RT Target VIs](interacting-with-the-front-panels-of-rt-target-vis.html)

<!--NI_TOPIC bundle=labview-real-time-module path=real-time-module-how-to.html language=enus -->
## TOPIC 00061: Real-Time Module How-To

- bundle_id: `labview-real-time-module`
- source_path: `real-time-module-how-to.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/real-time-module-how-to.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The topics in this section provide procedures to help you configure the settings of real-time projects, share data within real-time applications, and build deterministic applications.

### Real-Time Module How-To

The topics in this section provide procedures to help you configure the settings of
 real-time projects, share data within real-time applications, and build
 deterministic applications.

- [Organizing and Managing a LabVIEW Project with the Real-Time Module](organizing-and-managing-a-labview-project-with-the-real-time-module-real-time-module.html)
- [Tutorial: Creating a Real-Time Application](tutorial-creating-a-real-time-application.html)
- [Sharing Data in Deterministic Applications](sharing-data-in-deterministic-applications-real-time-module.html)
- [Building, Deploying, and Debugging Deterministic Applications](building-deploying-and-debugging-deterministic-applications-real-time-module.html)
- [Interacting with the Front Panels of RT Target VIs](interacting-with-the-front-panels-of-rt-target-vis-real-time-module.html)

<!--NI_TOPIC bundle=labview-real-time-module path=real-time-operating-systems-real-time-module.html language=enus -->
## TOPIC 00062: The NI Linux Real-Time Operating System

- bundle_id: `labview-real-time-module`
- source_path: `real-time-operating-systems-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/real-time-operating-systems-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn how to use the NI Linux Real-Time Operating System to run VIs with the LabVIEW Real-Time Module, manage secure file transfers, handle case-sensitive paths, and understand supported and unsupported features. The LabVIEW Real-Time Module executes VIs on the NI Linux Real-Time operating system. H

### The NI Linux Real-Time Operating
 System

Learn how to use the NI Linux Real-Time Operating System to run VIs with the LabVIEW
 Real-Time Module, manage secure file transfers, handle case-sensitive paths, and understand
 supported and unsupported features.

Note

NI Linux Real-Time Documentation and
 Tutorials

#### Special Considerations

Keep
 the following considerations in mind when using an NI Linux Real-Time target. You
 also can visit ni.com/info and enter Linux
 to learn more about the NI Linux Real-Time operating system.

#### General

- By default, the system disables the FTP server, and you cannot use it in safe
 mode. NI recommends using WebDAV as the file transfer mechanism for improved
 security.
- NI Linux Real-Time targets support virtual memory, which implies the following:
  - The system restarts a process after a crash without restarting the
 target.
  - Monitoring the largest contiguous memory block does not provide useful
 or necessary information on NI Linux Real-Time targets.
- The system supports System Exec VI.
- Time zone changes do not require a target restart.

#### File System and Directory
 Structure

- The file system is case-sensitive.
- Directory paths display in Linux format. For example, paths use forward slashes
 and do not contain drive letters.
- NI Linux Real-Time targets enforce file and folder access permissions. Refer to
 the KnowledgeBase article Working with File Paths on Real-Time
 Targets for information about these permissions.
- The RTOS deletes the content in the temporary folder /tmp on
 target restart. The temporary folder allocates space from RAM up to a maximum
 size of 64 MB.
- The c:\ni-rt directory does not exist on NI Linux Real-Time
 targets. Refer to the KnowledgeBase article Working with File Paths on
 Real-Time Targets for information about the directory mapping on NI
 Linux Real-Time targets.
- We highly discourage directly modifying the ni-rt.ini 
 configuration file. Modifying this file may result in incorrect system
 behavior. Note Some NI troubleshooting procedures require manual edits to this file. Take
 care to precisely follow troubleshooting documentation in these
 scenarios.

#### Web Services

- The system enables WebDAV by default.
- The system enables SSL by default.
- NI Web-based Configuration & Monitoring is available in safe mode.
- Configuring a target is only possible if the target is reachable via an IP
 address (DHCP, link-local, or static). mDNS is used for target discovery.
- You cannot use the Console Out using NI Web-based Configuration & Monitoring
 on NI Linux Real-Time targets. Instead, connect your NI Linux Real-Time targets
 to a computer using a serial port to view the output of the Console Out. Refer
 to the KnowledgeBase article Console Out on cRIO, sbRIO and cFP
 Controllers for detailed information about how to use the Console
 Out.

#### Authentication

- You can log in to a target using NI Web-based Configuration & Monitoring,
 SSH, or a serial connection. Refer to your hardware documentation to learn about
 enabling SSH on your RT target. Note NI recommends you
 set a password to log in using SSH or a serial connection.
- To reset a forgotten administrator password, you must physically access the
 target and reset all settings to the factory default. Contact NI for assistance
 with this process.
- Your target creates an admin user that is equivalent to the
 root user in Linux systems. [IMAGE alt='image' src='GUID-195F57EC-A4AB-46A2-93C4-28002EA40F31-a5.png']
 Caution Do not create users in NI
 Web-based Configuration & Monitoring with the same name
 as system accounts. For example, do not create a user named
 root or ssh. Doing so
 overwrites the system account.
- SSH supports public keys as an alternate form of authentication.

#### Security

- Visit ni.com/info and enter RTSecurity 
 to keep informed about security as it relates to NI products.

#### Unsupported Features

The
 LabVIEW Real-Time Module does not support certain LabVIEW features for VIs that run
 on RT targets. If you try to deploy and run a VI with unsupported functionality on
 an RT target, the VI might still execute. However, the unsupported functions do not
 work and return standard LabVIEW error codes. The LabVIEW Real-Time Module does not
 support the following features on RT targets that run the NI Linux Real-Time RTOS:

- ActiveX VIs
- NI TestStand VIs (ActiveX-based)
- .NET VIs
- Report Generation VIs
- Windows Registry Access VIs
- Report Express VI (Uses the unsupported Report Generation VIs)
- Graphics & Sound VIs
- Database Connectivity VIs
- Menu functions
- Cursor VIs
- IrDA functions
- File System Web Service LabVIEW API
- Call Library Function Nodes that access an operating system API other than NI
 Linux Real-Time
- Open/Create/Replace File function interactively using a file dialog box
- Clear indicators when called option of the Execution
 Properties page
- Auto Configure option of the Create Histogram Express
 VI
- Certain Advanced TDMS functions
- Profile Buffer Allocations window
- Largest Available Memory Block Property Node—This property node does not provide
 useful information for NI Linux Real-Time targets and returns an error if used.
 Use the Free Physical Memory property node instead.
- Latch Until Released and Switch Until
 Released Boolean mechanical actions—For details on why these
 Boolean mechanical actions do not function on RT targets, refer to the
 KnowledgeBase article Boolean "Until Released" Mechanical Action Not
 Supported on Real-Time Targets .

#### Modifying Front Panel Objects of RT
 Target VIs

When a VI or stand-alone application runs on a headless RT
 target, or if you disable the embedded UI, you cannot execute VIs that modify a
 front panel.You cannot change or read the properties of front panel objects using
 property nodes. This limitation exists because VIs running on the RT target do not
 have a front panel. The VI still runs on the RT target but the front panel object is
 not affected and returns an error. In some cases, you can establish a front panel
 connection with the RT target to use some unsupported LabVIEW features. Right-click
 the RT target in the Project Explorer window. From the shortcut menu, select
 Connect. This action opens a front panel connection with
 the target..

The following features only work on an RT target with a front
 panel connection:

- Front panel property nodes and control references. Note An RT target
 updates the values of property nodes and control references asynchronously.
 This means a property node or control reference might not always have the
 most recent value of the indicator or control.
- Dialog VIs and functions
- VI Server front panel functions

Note

#### Real-Time Module and Express VI
 Considerations

LabVIEW Express VIs enhance ease of use and boost
 productivity in LabVIEW by providing interactive dialog boxes. These dialog boxes
 reduce the need for extensive programming in measurement applications. Express VIs
 require additional performance overhead during execution; therefore, do not use
 Express VIs in deterministic or processor-intensive applications. Instead, develop
 real-time applications with standard LabVIEW VIs.

#### Debugging Reentrant
 VIs

LabVIEW debugging tools are not available for copies of reentrant VIs
 executing on RT targets. LabVIEW identifies copies of reentrant VIs by their front
 panels. VIs running on RT targets do not have front panels. As a result, LabVIEW
 cannot open reentrant VI copies for debugging. However, you can run and debug your
 application on Windows prior to deploying the application to the RT
 target.

Related concepts:

- Real-Time Target
- LabVIEW Real-Time Module Platforms

Related information:

- Working with File Paths on Real-Time Targets
- Console Out on cRIO, sbRIO and cFP Controllers
- Boolean "Until Released" Mechanical Action Not Supported on
 Real-Time Targets
- NI Linux Real-Time Documentation and Tutorials

<!--NI_TOPIC bundle=labview-real-time-module path=real-time-system-components-real-time-module.html language=enus -->
## TOPIC 00063: Real-Time System Components

- bundle_id: `labview-real-time-module`
- source_path: `real-time-system-components-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/real-time-system-components-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: A real-time system consists of software and hardware components. The software components include LabVIEW, the RT Engine, and the LabVIEW projects and VIs you create. The hardware components of a real-time system include a host computer and an RT target. The following sections describe the different

### Real-Time System Components

A real-time system consists of software and hardware components. The software
 components include LabVIEW, the RT Engine, and the LabVIEW projects and VIs you
 create. The hardware components of a real-time system include a host computer and an
 RT target. The following sections describe the different components of a real-time
 system.

#### Host Computer

The host computer is a computer with LabVIEW and the LabVIEW Real-Time Module
 installed on which you develop the VIs for the real-time system. After developing
 the real-time system VIs, you can download and run the VIs on RT targets. The host
 computer can run VIs that communicate with VIs running on RT targets to provide a
 user interface.

#### LabVIEW

You develop VIs with LabVIEW on the host computer. The Real-Time Module extends the
 capabilities of LabVIEW with additional tools for creating, debugging, and deploying
 deterministic VIs.

#### LabVIEW Projects

Use LabVIEW projects to group LabVIEW files and files not specific to
 LabVIEW, create stand-alone real-time applications, and deploy or download VIs and
 other files to RT targets. When you save a project, LabVIEW creates a project file
 (.lvproj), which includes references to files in the project,
 configuration information, build information, and deployment information.

#### RT Engine

The RT Engine is a version of LabVIEW that runs on RT targets. The RT Engine runs
 the VIs you download to RT targets. The RT Engine provides deterministic real-time
 performance for the following reasons:

- The RT Engine runs on a real-time operating system (RTOS), which ensures that
 the LabVIEW execution system and other services adhere to real-time
 operation.
- The RT Engine runs on RT Series hardware. RT targets are designed to run only
 the VIs and device drivers necessary for RT applications, which prevents other
 applications from impeding the execution of RT VIs.
- RT targets do not use virtual memory, because virtual memory can cause
 unpredictable performance.

#### RT Target

An RT target refers to RT Series hardware that runs the RT Engine and VIs you create
 using LabVIEW. A networked RT Series device is a networked hardware platform with an
 embedded processor and a real-time operating system that runs the RT Engine and
 LabVIEW VIs. You can use a separate host computer to communicate with and control
 VIs on a networked RT Series device through an Ethernet connection. Some examples of
 networked RT Series devices include the following:

- NI RT Series PXI Controller —A networked device installed
 in an NI PXI chassis that communicates with NI PXI modules installed in the
 chassis. You can write VIs that use all the input/output (I/O) capabilities of
 the PXI modules, SCXI modules, and other signal conditioning devices installed
 in a PXI chassis. The RT Engine also supports features of the RT Series PXI
 controller. Refer to the LabVIEW Real-Time Support page on the NI website for
 information about the features supported by the RT Engine on specific networked
 devices.
- NI CompactRIO Series —A reconfigurable control and
 acquisition system designed for applications that require high performance and
 reliability.
- NI RT Series FieldPoint and Compact FieldPoint —A
 networked device that runs an RTOS.
- NI CVS-1457RT Compact Vision System —An easy-to-use,
 distributed, real-time imaging system that acquires, processes, and displays
 images from GigE Vision cameras.
- Desktop PCs as RT Targets —A desktop PC configured with RT
 Engine software. Refer to the Using Desktop PCs as RT Targets with the Real-Time
 Module document for information about desktop PC targets.

Note

LabVIEW Help

#### USB Storage Devices

The Real-Time Module includes support for USB storage devices, such as thumb drives
 and external USB hard drives, for RT targets that have onboard USB hardware. Connect
 an external USB storage device to a USB port of an RT target and then access the
 device from VIs running on the RT target.

When you plug a USB thumb drive into the RT system, the thumb drive is automatically
 assigned a drive letter of U:. Each additional drive you add is
 automatically assigned the next available drive letter. For example,
 V:, W::, X:, and so on.

|  | Caution Disconnecting a USB drive during operation can cause data corruption. To maintain data integrity, close all files on the USB drive before disconnecting the drive. |
| --- | --- |

Parent topic:

Introduction to the LabVIEW Real-Time Module

Related concepts:

- Using LabVIEW Projects with the Real-Time Module
- Creating Deterministic Applications with the Real-Time Module

<!--NI_TOPIC bundle=labview-real-time-module path=real-time-target.html language=enus -->
## TOPIC 00064: Real-Time Target

- bundle_id: `labview-real-time-module`
- source_path: `real-time-target.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/real-time-target.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Real-Time target runs the NI Linux Real-Time operating system. The real-time platform running on the RT target defines the features supported by the target. Target Configuration and Properties You can use the NI Measurement & Automation Explorer to configure network settings, install software, a

### Real-Time Target

The Real-Time target runs the NI Linux Real-Time operating
 system. The real-time platform running on the RT target defines the features supported by
 the target.

#### Target Configuration and Properties

Properties

Note

#### Deploying RT Target Settings

When you change the settings of an RT target in the target Properties dialog box, the
 settings persist in the project but do not propagate to the target until you deploy the
 target. To deploy the target, right-click the RT target in the Project Explorer window and
 select Deploy from the shortcut menu.

#### Connecting and Disconnecting from the Target

You can open a front panel connection with an RT target in a project. To connect to the
 target, right-click the RT target and select Connect from the
 shortcut menu. To disconnect, right-click the RT target and select
 Disconnect.

The status of the RT target is represented by an icon on the Project Explorer window, as
 shown in the following table.

|  | An open front panel connection exists with the RT target. |
| --- | --- |
|  | No front panel connection exists with the RT target. |

Parent topic:

Introduction to the LabVIEW Real-Time Module

Related concepts:

- The NI Linux Real-Time Operating System

<!--NI_TOPIC bundle=labview-real-time-module path=real-time-tracing.html language=enus -->
## TOPIC 00065: Real-Time Tracing

- bundle_id: `labview-real-time-module`
- source_path: `real-time-tracing.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/real-time-tracing.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the Real-Time Tracing VIs to capture timing and execution data for thread events on an RT target. To view the trace, use KernelShark on the host computer.Introduced in LabVIEW Real-Time Module 2026 Q1: KernelShark integration with the Real-Time Tracing VIs are officially introduced in this relea

### Real-Time Tracing

Use the Real-Time Tracing VIs to capture
 timing and execution data for thread events on an
 RT target. To view the trace, use KernelShark on
 the host computer.

Introduced in LabVIEW
 Real-Time Module 2026 Q1:
 KernelShark integration with the Real-Time Tracing
 VIs are officially introduced in this release.
 This is the first version where KernelShark is
 fully supported and documented as the primary
 trace viewing tool.

Creating Deterministic Applications

Building, Deploying, and Debugging
 Deterministic Applications

Tracing on NI Linux
 Real-Time

Related concepts:

- Creating Deterministic Applications
- Building, Deploying, and Debugging Deterministic Applications

Related information:

- Tracing on NI Linux Real-Time

<!--NI_TOPIC bundle=labview-real-time-module path=related-documentation-real-time-module.html language=enus -->
## TOPIC 00066: Related Documentation

- bundle_id: `labview-real-time-module`
- source_path: `related-documentation-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/related-documentation-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The following resources expand on real-time concepts that this tutorial does not detail. Types of RT Targets Visit ni.com/info and enter the info code RTSystems to learn about building real-time systems with NI hardware and software. Determinism and Warm-up Iterations Refer to Creating Deterministic

### Related Documentation

The following resources expand on real-time concepts that this tutorial does not
 detail.

#### Types of RT
 Targets

Visit ni.com/info and enter the info code
 RTSystems to learn about building
 real-time systems with NI hardware and software.

#### Determinism and Warm-up Iterations

Refer to *Creating Deterministic Applications* to learn about determinism and when to
 expect real-time loops to begin executing deterministically.

#### Preallocating an Array to Minimize Jitter

If you are using an array to manage large sections of data, preallocate the array to minimize
 jitter. Visit ni.com/info and enter
 PreAllocateArrays to learn about preallocating arrays for
 deterministic loops.

Parent topic:

Tutorial: Creating a Real-Time Application

Related concepts:

- Part 6: Displaying RT Data on the User Interface
- Tutorial: Creating a Real-Time Application
- Creating Deterministic Applications

<!--NI_TOPIC bundle=labview-real-time-module path=rt-best-practices-portal.html language=enus -->
## TOPIC 00067: RT Best Practices Portal

- bundle_id: `labview-real-time-module`
- source_path: `rt-best-practices-portal.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/rt-best-practices-portal.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Understand the Priority-Based Scheduling Model Avoid Jitter Switch to Deployment Settings Leverage Design Patterns Network the User Interface Get the Benchmarking Right Separate Your Tasks Use Shared Variables Effectively Minimize CPU Usage

### RT Best Practices Portal

[IMAGE alt='image' src='GUID-441E11BE-9514-415E-8FC4-3CA4512C098D-a5.png']

| Understand the Priority-Based Scheduling Model | Avoid Jitter | Switch to Deployment Settings |
| --- | --- | --- |
| Leverage Design Patterns | Network the User Interface | Get the Benchmarking Right |
| Separate Your Tasks | Use Shared Variables Effectively | Minimize CPU Usage |

Parent topic:

Real-Time Module Best Practices

Related concepts:

- Understand the Priority-Based Scheduling Model
- Avoid Jitter
- Switch to Deployment Settings
- Leverage Design Patterns
- Network the User Interface
- Get the Benchmarking Right
- Separate Your Tasks
- Use Shared Variables Effectively
- Minimize CPU Usage

<!--NI_TOPIC bundle=labview-real-time-module path=separate-your-tasks-real-time-module.html language=enus -->
## TOPIC 00068: Separate Your Tasks

- bundle_id: `labview-real-time-module`
- source_path: `separate-your-tasks-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/separate-your-tasks-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Task separation involves running distinct tasks in parallel loops to create a multi-rate application. Task separation is a key aspect of most real-time applications for two reasons: Determinism—To minimize jitter in a deterministic loop, ensure that the loop does not contain potentially non-determin

### Separate Your Tasks

Task separation involves running distinct tasks in parallel loops to create a

 multi-rate application. Task separation is a key aspect of most real-time

 applications for two reasons:

- Determinism —To minimize jitter in a deterministic loop,

 ensure that the loop does not contain potentially non-deterministic code.

 Because most large applications include non-deterministic tasks, identifying and

 separating these tasks is crucial to the success of an RT application.
- CPU Efficiency —Because CPU cycles often are at a premium

 on RT targets, CPU efficiency is a common design constraint in RT applications.

 By running tasks in separate loops at distinct rates, you can maximize CPU

 efficiency by executing each task only as often as necessary.

#### Define Your Tasks

Before you begin coding, think through the high-level design of your application by

 defining the tasks your application must perform, the required rate of each task (if applicable), and the data

 transfer relationships between the tasks. For example, your RT application

 requirements might include the following tasks:

- Control —Control the temperature and level of liquid in a

 tank. The minimum rate for this task is 1 kHz.
- Log —Log a historical record of the temperature and level

 data collected. The requirement for this task is to log every process variable

 value collected by the control task. There is no minimum rate requirement for

 this task.
- Network —Transfer user

 interface data over the network to receive commands from the user and

 display continuous data graphs that the user can monitor. The minimum rate for

 this task is 10 Hz.

After you define the high-level tasks that make up your application, define the data

 transfer relationships between those tasks. For example, the following illustration

 shows the data transfer relationships between the three example tasks defined in the

 previous list:

[IMAGE alt='image' src='GUID-F54C79C6-9BAC-4CB9-8049-3DCCCC52E0EB-a5.png']

#### Translate Your Design into a LabVIEW Block Diagram

After you define the high-level design of your application, you can begin translating

 your design into LabVIEW code. For example, the following block diagram shows a

 top-level VI that includes the ongoing tasks defined in the previous section:

[IMAGE alt='image' src='GUID-46A37A37-41E2-4F55-B682-32CB54592748-a5.png']

Note

The following block diagram shows the control loop contained in the

 Control.vi subVI:

[IMAGE alt='image' src='GUID-C8FF913F-E056-4954-9AA9-723D40C7ED6C-a5.png']

The following block diagram shows the data logging loop contained in the

 Log.vi subVI:

[IMAGE alt='image' src='GUID-7F8FCF7E-3B56-4EA4-95F1-99C4C2F54147-a5.png']

The following block diagram shows the networking loop contained in the

 User_Interface.vi subVI:

[IMAGE alt='image' src='GUID-24B85AC9-32DD-4923-9FD1-A9F5043CD16A-a5.png']

#### Create an Initialization Routine

Create an initialization routine to handle preliminary tasks that need to occur

 before your ongoing tasks start executing. Depending on the nature of your

 application, an initialization routine might include the following actions:

- Initialize shared variables
- Open file references
- Preallocate arrays

The following block diagram shows the initialization routine contained in the

 Initialize.vi subVI:

[IMAGE alt='image' src='GUID-8221DFC8-6CC1-4983-B1B3-3C93D3E860F8-a5.png']

#### Create a Shutdown Routine

National Instruments recommends switching your application to a shutdown state before

 turning off your RT target. To ensure that your RT target is in a shutdown state,

 create a shutdown routine that runs after your ongoing application tasks stop executing. Depending on the nature of your application, a

 shutdown routine might include the following actions:

- Set outputs to known values
- Close file references
- Notify the operator when they can turn off the RT target using a

 network-published shared variable or the RT LEDs

 VI

Note

The following block diagram shows the shutdown routine contained in the

 Shutdown.vi subVI.

[IMAGE alt='image' src='GUID-DCC48CE0-BDD0-4AC7-8CF3-FB2736DF25F3-a5.png']

Parent topic:

Real-Time Module Best Practices

Related concepts:

- Use Shared Variables Effectively
- Separate Your Tasks

<!--NI_TOPIC bundle=labview-real-time-module path=setting-vi-properties-real-time-module.html language=enus -->
## TOPIC 00069: Setting VI Properties

- bundle_id: `labview-real-time-module`
- source_path: `setting-vi-properties-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/setting-vi-properties-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: To reduce memory requirements and increase performance of VIs, disable nonessential options in the VI Properties dialog box available by right-clicking a VI in the Project Explorer window and selecting Properties from the shortcut menu. Select Execution from the Category pull-down menu and remove ch

### Setting VI Properties

To reduce memory requirements and increase performance of VIs, disable nonessential
 options in the VI
 Properties dialog box available by right-clicking a VI in the Project Explorer window and selecting
 Properties from the shortcut menu. Select
 Execution from the Category
 pull-down menu and remove checkmarks from the Allow debugging
 and Auto handle menus at launch checkboxes. By disabling
 these options, VIs use less memory, compile more quickly, and exhibit less
 jitter.

Parent topic:

Optimizing Deterministic Applications

Related concepts:

- Optimizing Deterministic Applications

<!--NI_TOPIC bundle=labview-real-time-module path=sharing-data-in-deterministic-applications-real-time-module.html language=enus -->
## TOPIC 00070: Sharing Data in Deterministic Applications

- bundle_id: `labview-real-time-module`
- source_path: `sharing-data-in-deterministic-applications-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/sharing-data-in-deterministic-applications-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use shared variables to read and write data among VIs in a project or across a network. Shared variables are configured software items that can send data between two locations in a block diagram that cannot be connected with wires, between two VIs running on an RT target, or between two VIs

### Sharing Data in Deterministic Applications

You can use shared
 variables to read and write data among VIs in a project or across a
 network. Shared variables are configured software items that can send data between
 two locations in a block diagram that cannot be connected with wires, between two
 VIs running on an RT target, or between two VIs across a network running on
 different targets. The Real-Time Module adds a real-time FIFO to the shared
 variable. By enabling the real-time FIFO of a shared variable, you can
 deterministically share live data without affecting the determinism of VIs running
 on an RT target.

Parent topic:

Real-Time Module How-To

Related concepts:

- Creating a Shared Variable with Real-Time FIFO

<!--NI_TOPIC bundle=labview-real-time-module path=sharing-data-in-deterministic-applications.html language=enus -->
## TOPIC 00071: Sharing Data in Deterministic Applications

- bundle_id: `labview-real-time-module`
- source_path: `sharing-data-in-deterministic-applications.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/sharing-data-in-deterministic-applications.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: After separating deterministic tasks from non-deterministic tasks in an application, you must use deterministic communication methods to share data. You can use deterministic communication methods to share data between locations in a VI that cannot be connected with wires, between VIs running on an

### Sharing Data in Deterministic Applications

After separating deterministic tasks from non-deterministic tasks in an application,
 you must use deterministic communication methods to share data. You can use
 deterministic communication methods to share data between locations in a VI that
 cannot be connected with wires, between VIs running on an RT target, and between VIs
 across a network running on different targets.

Parent topic:

Real-Time Module Concepts

Related concepts:

- Pipelining to Optimize Multiple-CPU RT Applications

<!--NI_TOPIC bundle=labview-real-time-module path=sharing-data-locally-on-an-rt-target-real-time-module.html language=enus -->
## TOPIC 00072: Sharing Data Locally on an RT Target

- bundle_id: `labview-real-time-module`
- source_path: `sharing-data-locally-on-an-rt-target-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/sharing-data-locally-on-an-rt-target-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: After dividing tasks in an application into separate Timed Loops or VIs of different priorities, you might need to communicate between the loops on a block diagram or between the different VIs on the RT target. Use shared variables and Real-Time FIFO VIs to share data in a VI or between VIs running

### Sharing Data Locally on an RT Target

After dividing tasks in an application into separate Timed Loops or VIs of different priorities, you might need to communicate between the
 loops on a block diagram or between the different VIs on the RT target. Use shared
 variables and Real-Time FIFO VIs to share data in a VI or between VIs running on an
 RT target.

Note

#### Single-Process Shared Variables

Use single-process shared
 variables to share data between two locations in a block diagram or
 between VIs running on an RT target. Right-click an RT target in the Project Explorer window and select
 New»Variable from the shortcut menu to open the Shared Variable Properties dialog box, which you can use to create a
 single-process shared variable.

The Real-Time Module adds real-time FIFO (first in, first out) buffer capability to
 the shared variable. By enabling the
 real-time FIFO of a shared variable, you can share data without affecting the determinism of VIs running on an RT
 target. From the Real-Time FIFO page of the Shared Variable
 Properties dialog box, place a checkmark in the Enable
 Real-Time FIFO checkbox to enable the real-time FIFO of a shared
 variable.

Single-process shared variables provide a communication method that is easy to use
 and deterministic when you enable the Real-Time FIFO.

Note

#### Real-Time FIFO Functions

Use the RT FIFO functions to share data between VIs running on
 an RT target. An RT FIFO acts like a fixed-sized queue, where the first value you
 write to the FIFO is the first value that you can read from the FIFO. An RT FIFO
 ensures deterministic behavior by imposing a size restriction on the data you share
 and by preallocating memory for the data. You must define the number and size of the
 RT FIFO elements and ensure that you do not attempt to read and write data of
 different sizes.

Use the RT FIFO Create function to create a new FIFO or to
 create a reference to a FIFO that you previously created. Use the RT
 FIFO Read and RT FIFO Write
 functions to read and write data to the FIFO. Use the RT FIFO Delete
 function to delete a reference to an RT FIFO and release the memory allocated to the
 FIFO on the RT target.

Note

#### Defining Read and Write Modes for Real-Time FIFOs

An RT FIFO can wait until an empty slot becomes available for a write operation or
 wait until a value is available for a read operation. You can specify a read and
 write mode for an RT FIFO that defines the way you read a value from an empty FIFO
 or write a value to a FIFO that does not have an empty slot. You can specify one of
 the following modes for reads and writes:

polling—Use this mode to optimize the throughput performance
 of read and write operations. The polling mode continually polls the FIFO for new
 data or an open slot. The polling mode responds quicker than the blocking mode to
 new data or new empty slots, but requires more CPU overhead. Use the
 timeout in ms input of the RT FIFO Read or RT FIFO Write
 function to specify the amount of time that a write operation should poll for an
 empty slot or the amount of time a read operation should poll for new data. You also
 can use the overwrite on timeout input of the RT FIFO Write
 VI to specify whether to overwrite the oldest value in the RT FIFO when the value of
 the timeout in ms input expires.

blocking—Use this mode to optimize the utilization of the CPU
 during read and write operations. The blocking mode allows the thread of the VI to
 sleep while it waits, allowing other tasks in the system to execute. Use the
 timeout in ms input of the RT FIFO Read or RT FIFO Write
 function to specify an amount of time a read operation can wait for a new value or
 an amount of time a write operation can wait for an empty slot. You also can use the
 overwrite on timeout input of the RT FIFO Write VI to
 specify whether to overwrite the oldest value in the RT FIFO when the value of the
 timeout in ms input expires.

Note

#### Using the RT FIFO Functions to Create Scalable Block Diagrams for Large
 Applications

When you need a scalable inter-task communication architecture for a large
 application, use the RT FIFO Create
 function to create RT FIFOs programmatically. For example, you can use the RT FIFO
 Create function inside a For Loop to create as many RT FIFOs as you need. You
 then can use the RT FIFO Read and RT FIFO Write
 functions inside For Loops to read from and write to all your RT FIFOs
 consecutively. Using this technique, you can scale your application up to use as
 many RT FIFOs as you need while keeping the size of your block diagram
 manageable.

Note

RT FIFO Create

#### Global Variables

Use global variables to access and pass small amounts of data between VIs,
 such as from a time-critical VI to a lower priority VI. Global variables can share
 data smaller than 32-bits, such as scalar data, between VIs deterministically.
 However, global variables of larger data types are shared
 resources that you must use carefully in a time-critical VI. If you use a
 global variable of a data type larger than 32-bits to pass data out of a
 time-critical VI, you must ensure that a lower priority VI reads the data before the
 time-critical VI attempts to write to the global again.

Global variables are a lossy form of communication, meaning the global variable can
 overwrite the data before you read the data. Tasks in a lower priority VI might not
 have enough processor time to read the data before other tasks in a different VI
 overwrite the data.

#### Functional Global Variables

Use functional global variables to pass data between VIs. A functional global
 variable is a subVI set to subroutine priority. The subVI contains a While
 Loop with a nested Case structure
 for read and write access. The following block diagram shows the read and write
 cases of the Case structure for a functional global variable:

[IMAGE alt='image' src='GUID-5A6CC14F-7AB8-46DA-B916-FF68BC3C9922-a5.png']

The While Loop contains uninitialized shift registers that store data. A functional
 global variable receives an action input that specifies which task the VI performs,
 as shown in the previous block diagram, by the Mode input
 parameter. Any subsequent calls to the functional global variable can access the
 most recent data. Functional global variables resemble queues because you can add
 more shift registers to store a longer history of values. You also can add more than
 one set of shift registers to pass more than one set of data.

Unlike global variables, you can implement functional global variables such that they
 are not a shared
 resource. Right-click a subVI set to subroutine priority and select
 Skip Subroutine Call If Busy from the shortcut menu to
 force the execution system to skip the subVI if the subVI is currently running in
 another thread. Skipping a subVI helps in time-critical VIs because the VI does not
 wait for the subVI. If you skip the execution of a subVI, the subVI returns the
 default indicator value. If you want to detect the execution of a functional global
 variable, wire a TRUE constant to a Boolean output on the functional global variable
 block diagram, and ensure that the default indicator value is set to FALSE. If the
 Boolean output returns TRUE, the functional global variable executed. If the Boolean
 output returns the default value of FALSE, the functional global variable did not
 execute. Skip functional global variables in time-critical VIs but not in lower
 priority VIs. In lower priority VIs, you can wait to receive non-default values.

Functional global variables can be a lossy form of communication if a VI overwrites
 the shift register data before another VI reads the data.

Parent topic:

Sharing Data in Deterministic Applications

Related concepts:

- Creating Deterministic Applications Using the Timed Loop
- Creating Deterministic Applications Using VIs Set to Different Priorities
- Sharing Data Using Shared Variables
- Sharing Data Remotely across a Network

<!--NI_TOPIC bundle=labview-real-time-module path=sharing-data-remotely-across-a-network-real-time-module.html language=enus -->
## TOPIC 00073: Sharing Data Remotely across a Network

- bundle_id: `labview-real-time-module`
- source_path: `sharing-data-remotely-across-a-network-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/sharing-data-remotely-across-a-network-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: After creating VIs that run on an RT target, you might need to share data with VIs running on other targets, such as the host computer. Use remote communication methods to share data between VIs running on an RT target and VIs on another target across a network. Using remote communication methods, a

### Sharing Data Remotely across a Network

After creating VIs that run on an RT target, you might need to share data with VIs
 running on other targets, such as the host computer. Use remote communication methods to share data between VIs running on an RT
 target and VIs on another target across a network.

Using remote communication methods, a VI running on an RT target can share data with
 VIs running on other targets across a network. You might use remote communication
 for the following reasons:

- You want to control the data exchanged between a host computer and the RT target
 to provide a user interface. You can customize communication VIs to specify
 which components you want to view from the host computer.
- You want to control timing and sequencing of the data transfer.
- You want to perform additional data processing or logging on a different
 target.

For example, you can use a shared variable to share data locally with another VI on an RT target. You then can use
 remote communication methods to share data with VIs running on other targets, such
 as the host computer.

Parent topic:

Sharing Data in Deterministic Applications

Related concepts:

- Creating Deterministic Applications Using the Timed Loop
- Exploring Remote Communication Methods
- Sharing Data Locally on an RT Target

<!--NI_TOPIC bundle=labview-real-time-module path=sharing-data-using-shared-variables-real-time-module.html language=enus -->
## TOPIC 00074: Sharing Data Using Shared Variables

- bundle_id: `labview-real-time-module`
- source_path: `sharing-data-using-shared-variables-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/sharing-data-using-shared-variables-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use shared variables to read and write data among VIs in a project or across a network. From the Project Explorer window, right-click an RT target and select New»Variable from the shortcut menu to open the Shared Variable Properties dialog box, which you can use to create and configure the o

### Sharing Data Using Shared Variables

You can use shared
 variables to read and write data among VIs in a project or across a
 network. From the Project Explorer window, right-click an RT
 target and select New»Variable from the shortcut menu to open
 the Shared Variable Properties dialog box, which you can use
 to create and configure the options for a shared variable. Shared variables are
 configured software items that can send data between two locations in a block
 diagram that cannot be connected with wires, between two VIs running on an RT
 target, or between two VIs across a network running on different targets. Use
 single-process shared variables to share data locally on an RT target and
 network-published shared variables to share data between VIs on different machines
 for data logging.

The Real-Time Module adds real-time FIFO capability to the shared variable. By enabling the real-time FIFO of a shared variable, you
 can share data without affecting the determinism of the VIs. However, RT FIFOs do
 not support data types of variable size, such as clusters, strings, and variants.

Note

#### Creating a Shared Variable

Use the Shared Variable Properties dialog box to create a shared variable on an RT target. To access this
 dialog box, right-click the target or a library under the target in the
 Project Explorer window and select
 New»Variable from the shortcut menu. When you select
 New»Variable on a target, you create a new library under
 the target and add the variable under that library. When you select
 New»Variable on an existing library, you create a new
 variable under that library. Right-click a library and select
 Deploy from the shortcut menu to deploy the shared
 variable to the target.

Note

#### Shared Variable Engine

When you create a network-published shared variable on a target, the Shared Variable
 Engine on the target hosts the shared variable. The Shared Variable Engine sends the
 data you share to other targets across the network. You can choose the target that
 you want to host the shared variable by creating the shared variable under the
 target in the Project Explorer window.

When an RT target hosts a network-published shared variable, that target controls the
 data and other targets do not affect the availability of the shared variable. If
 availability is not a concern, consider hosting the shared variable on the host
 computer. This frees up processor time on the target, permits the shared variable to
 be accessed by targets that do not support the Shared Variable Engine, and allows
 you to use the security features provided by the LabVIEW DSC Module.

The following illustration shows a Real-Time Module application that uses
 single-process and network-published shared variables to share data locally and
 across the network between VIs:

[IMAGE alt='image' src='GUID-B5561B61-FD8B-4510-8BCE-902CF5161C84-a5.png']

The Deterministic VI running on the RT target shares data with Other VI on the target
 using variable B, a single-process shared variable. The Deterministic VI also shares
 data with a VI on the host computer using variable A, a network-published shared
 variable with the RT FIFO enabled. The network-published shared variable on the RT
 target sends data to the Shared Variable Engine running on the target, which then
 shares the data with the host computer.

Note

After you create a shared variable, you can use the Shared Variable
 Properties dialog box to change its configuration. To open this dialog
 box, right-click a shared variable in the Project Explorer
 window and select Properties from the shortcut menu. When you
 change a shared variable's properties, those changes do not take effect until the
 variable is deployed.

#### Enabling the Real-Time FIFO

You can enable the real-time FIFO of a shared variable from the Real-Time FIFO page of the Shared Variable
 Properties dialog box. Place a checkmark in the Enable
 Real-Time FIFO checkbox to deterministically share data using single
 element or multi-element FIFOs.

#### Single Element FIFO

A single-element FIFO shares the most recent data value. The shared variable
 overwrites the data value when it receives a new data value. Use this option when
 you need only the most recent value. Configure the size of the array elements or the
 size of the waveform for the FIFO buffer if you select an array or waveform data
 type.

#### Multi-Element FIFO

A multi-element FIFO buffers the values shared by the shared variable. You can
 configure the size and the elements of the FIFO buffer to match the settings from
 the Use Buffering section of the Network page, or
 you can configure a custom size for the FIFO and the FIFO elements.

Note

Note

Parent topic:

Sharing Data in Deterministic Applications

Related concepts:

- Creating Deterministic Applications Using the Timed Loop
- Exploring Remote Communication Methods
- Sharing Data Locally on an RT Target

<!--NI_TOPIC bundle=labview-real-time-module path=specifying-the-set-of-cpus-available-for-automatic-load-balancing-real-time-module.html language=enus -->
## TOPIC 00075: Specifying the Set of CPUs Available for Automatic Load Balancing

- bundle_id: `labview-real-time-module`
- source_path: `specifying-the-set-of-cpus-available-for-automatic-load-balancing-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/specifying-the-set-of-cpus-available-for-automatic-load-balancing-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Installing the NI RT Extensions for Symmetric Multiprocessing (SMP) on a multi-CPU RT target adds automatic load balancing features that distribute application threads across CPUs. Use the LabVIEW Real-Time Software Wizard in Measurement & Automation Explorer to install the NI RT Extensions for SMP.

### Specifying the Set of CPUs Available for
 Automatic Load Balancing

Installing the NI RT Extensions for Symmetric Multiprocessing (SMP) on a multi-CPU
 RT target adds automatic load balancing features that distribute application threads
 across CPUs. Use the LabVIEW Real-Time Software Wizard in Measurement &
 Automation Explorer to install the NI RT Extensions for SMP. Refer to the
 Measurement & Automation Explorer Help for information
 about the using the Real-Time Software Wizard.

Note

Use the RT SMP CPU Utilities VIs to specify the set of CPUs
 available for automatic load balancing and to reserve certain CPUs for exclusive use
 by specific Timed Structures.

#### CPU Pools

With the NI RT Extensions for SMP installed, the real-time operating system (RTOS)
 maintains two pools of CPUs available for automatic load balancing: a Timed
 Structures pool and a System pool. CPUs in the Timed Structures pool are available
 for automatic load balancing of Timed Loops and Timed Sequences configured for
 automatic processor assignment. CPUs in the System pool are used for all other
 processes, including low-level operating system tasks.

#### Automatic Load Balancing

Automatic load balancing is the process of assigning threads to CPUs in a way that
 balances the processing load across CPUs. At startup, the LabVIEW Real-Time Module
 assigns all available CPUs to both the System pool and the Timed Structures pool,
 and therefore performs automatic load balancing across all CPUs. However, you can
 use the SMP CPU Utilities VIs to specify arbitrary System and Timed Structures
 pools.

LabVIEW Real-Time performs automatic load balancing on all threads, with the
 exception of manually-assigned Timed Structure threads. LabVIEW maps code execution
 from each Timed Structure to its own dedicated thread, but performs automatic load
 balancing only on Timed Structure threads configured for automatic CPU assignment.
 You can manually assign a Timed Structure to a particular CPU by wiring the CPU
 index to the Processor input of the Timed Structure. The
 default Processor value of -2 configures the Timed Structure
 for automatic processor assignment through automatic load balancing. You also can
 manually assign a Timed Structure to a processor by using the Processor
 Assignment section of the Configure
 Timed Loop dialog box or the Configure
 Timed Sequence dialog box.

Generally, the automatic load balancing process avoids switching a given thread
 between CPUs to minimize inter-CPU data transfer overhead. However, the SMP
 scheduler might switch a thread repeatedly from one CPU to another if the load due
 to other threads of equal or higher priority running on each CPU fluctuates
 significantly. You can use the Real-Time
 Trace Viewer to determine whether a Timed Structure thread moves from CPU
 to CPU.

To ensure that the SMP scheduler does not unexpectedly assign Timed Structures to a
 particular CPU, you can remove that CPU from the Timed Structures pool using the SMP
 CPU Utilities VIs. However, to ensure that a Timed Structure has exclusive access to
 a manually-assigned CPU, you also must remove that CPU from the System pool. By
 doing so, you can maximize the performance of a deterministic Timed Loop, as
 described in the Isolating a Deterministic Timed Structure section of this
 topic.

#### Pool Configurations

There are four possible states for a CPU in an SMP-enabled RT target. A CPU can
 belong to:

- The Timed Structures Pool, in which case the SMP scheduler can use the CPU to
 execute Timed Structures configured for automatic processor
 assignment.
- The System pool, in which case the SMP scheduler can use the CPU to execute
 threads that do not correspond to Timed Structures.
- Both pools, in which case the SMP scheduler can use the CPU for either of the
 above.
- Neither pool (reserved), in which case the CPU is dedicated solely to executing
 Timed Structures that you manually assign to that CPU.

When an SMP-enabled RT target starts up, LabVIEW assigns all CPUs to both pools by
 default. However, you can use the SMP CPU Utilities VIs to assign each CPU to any of
 the four states listed above.

Note

#### Isolating a Deterministic Timed Structure

To maximize performance and minimize jitter in a deterministic Timed Loop, you can
 isolate that Timed Structure on a particular CPU. To isolate a Timed Structure, you
 must assign the Timed Structure to a CPU that is not contained in either the System
 pool or the Timed Structures pool. When a CPU is not assigned to a pool, the CPU is
 reserved to run only the Timed Structure(s) that you manually assign to that CPU.
 Isolating a Timed Structure on a single CPU allows you to monopolize the processing
 capacity of that CPU and achieve high frequency or throughput rates. For example,
 you can take advantage of isolation to achieve a high polling rate in a Timed Loop
 that performs data acquisition.

To minimize the latency of a high-performance, deterministic Timed Loop, consider
 isolating that Timed Loop on a high-index CPU. For example, if the system contains
 four CPU cores indexed 0-3, consider isolating the deterministic Timed Loop on CPU
 3. When scheduling Timed Structures, the real-time operating system begins at the
 highest-index CPU and increments down. Therefore, if multiple Timed Structures of
 equal priority are scheduled to wake up at the same time, the wake-up latency of
 Timed Structures executing on lower-index CPUs can be higher than that of Timed
 Structures executing on higher-index cores by up to several microseconds. The
 reverse is true for non-Timed-Loop threads, because for these threads the scheduler
 starts at CPU 0 and increments up. Therefore, to minimize latency, NI recommends
 assigning lower-numbered CPUs to the System pool and reserving higher-numbered CPUs
 for deterministic Timed Structures.

#### Preventing Thread Starvation

To prevent starvation of System threads, consider reserving at least one CPU for
 System threads only. For example, if you assign CPU 0 to the System pool but not to
 the Timed Structures pool, and you avoid targeting any Timed Structures to CPU 0,
 CPU 0 is always available to run System threads.

#### Maximizing CPU Utilization

To maximize processor utilization, it helps to determine the number of CPUs in each
 pool based on the proportion of load that corresponds to Timed Structure threads
 versus System threads. You can use the RT Get CPU
 Loads VI to estimate the proportion of total processing time dedicated to
 Timed Structures and System threads and assign CPUs to the Timed Structures and
 System pools accordingly. If the RT target is connected to a monitor, you also can
 use the on-screen CPU Load Measurement utility to estimate load distribution.

#### Avoiding Partial Pool Overlap

If you define the System and Timed Structures pools such that the two pools partially
 overlap, the automatic load balancing process might not make optimal
 processor-utilization decisions, as illustrated in the following examples:

#### Example 1

Assume you have an application with three Timed Loops. The periods of the Timed Loops
 are configured such that most of the time only one of the three Timed Loops is
 running. However, occasionally the periods of the Timed Loops align, and you want to
 ensure that when this happens all three Timed Loops can execute in parallel. You
 might be tempted to assign three CPUs (such as CPUs 0-2) of a quad-core system to
 the System pool and three CPUs (such as CPUs 1-3) to the Timed Structures pool,
 assuming that CPU 3 would always run one of the three Timed Loops while CPUs 1 and 2
 would generally run System threads but would each run a Timed Loop when the periods
 align. However, because the SMP scheduler starts timed structures at the
 highest-index CPU and attempts to run each thread on the same CPU from iteration to
 iteration, the first two Timed Loops might both execute on CPU 3 and the third on
 CPU 2. The first time the periods align, one of the Timed Loops would transfer to
 CPU 1, causing a jitter spike. In this case, a better solution would be to manually
 assign each Timed Loop to a different CPU and to assign all four CPUs to the System
 pool.

#### Example 2

Assume you have an application with two Timed Loops that perform continuous polling
 and two Timed Loops that run intermittently. You might be tempted to assign all four
 CPUs of a quad-core system to the Timed Structures pool and two of the CPUs, such as
 CPUs 2 and 3, to the System pool. You might assume that the two polling Timed Loops
 would execute on CPUs 0 and 1, and that the intermittent Timed Loops would share
 processing time on CPUs 2 and 3. However, the SMP scheduler might assign the polling
 Timed Loops to CPUs 2 and 3, starving the other System threads and leaving CPUs 0
 and 1 under-utilized. In this case, the best solution would be to isolate the
 polling Timed Loops on two CPUs and assign the remaining two CPUs to both pools.

#### Using the SMP CPU Utilities VIs

Use the SMP CPU Utilities VIs to define the System and Timed Structures pools. The
 SMP CPU Utilities palette includes three VIs that offer three different ways to
 define the CPU pools, so you can choose the VI that best matches your programming
 style and application requirements. The RT Set CPU Pool
 Sizes VI is built on top of the RT Set CPU
 Pool Assignments VI, which is built on top of the RT Set CPU
 Pool VI. The RT Set CPU Pool Sizes VI is a good choice for most use
 cases. You can use the RT Set CPU Pool Sizes VI to create either the default pool
 configuration in which both pools contain all CPUs or to create contiguous, adjacent
 pools. For custom CPU pool configurations, the RT Set CPU Pool Assignments VI is a
 good choice. You can use the RT Set CPU Pool Assignments VI to create any pool
 configuration as long as each pool contains at least one CPU. If you prefer to work
 with bit masks, you can use the RT Set CPU Pool VI.

Parent topic:

Optimizing RT Applications for Multiple-CPU Systems

<!--NI_TOPIC bundle=labview-real-time-module path=switch-to-deployment-settings-real-time-module.html language=enus -->
## TOPIC 00076: Switch to Deployment Settings

- bundle_id: `labview-real-time-module`
- source_path: `switch-to-deployment-settings-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/switch-to-deployment-settings-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: By default, RT targets and VIs use a variety of settings designed to facilitate development and debugging. However, these settings can affect the performance and determinism of your RT application. This topic describes steps you can take to optimize application performance for deployment. Selecting

### Switch to Deployment Settings

By default, RT targets and VIs use a variety of settings designed to facilitate

 development and debugging. However, these settings can affect the performance and

 determinism of your RT application. This topic describes steps you can take to

 optimize application performance for deployment.

#### Selecting Optimal Deployment Settings

Before benchmarking or deploying an RT application, consider the following settings

 to optimize performance and determinism:

| Setting Name | Location | Optimal Performance Setting | Details |
| --- | --- | --- | --- |
| Hyperthreading | RT target BIOS | Disabled | NI recommends that you avoid using hyperthreading, which can cause severe jitter. NI disables hyperthreading on RT targets by default. However, if you are using a third-party desktop PC as an RT target, hyperthreading might be enabled by default. Use the RT target BIOS to determine whether hyperthreading is enabled and to disable hyperthreading if necessary. |
| Packet Detection | Network Settings tab under the More Settings pull-down menu in NI Measurement & Automation Explorer | Polling | Polling mode provides lower jitter than interrupt mode. However, polling mode increases CPU overhead. Not all real-time targets support polling mode. |
| Enable CPU Load Monitoring | Miscellaneous Properties page | Disabled | CPU load monitoring increases CPU and memory overhead. |
| Allow debugging | Execution page | Disabled | Debugging support increases CPU and memory overhead. |

#### Additional Deployment Actions

In addition to the settings described above, you can take the following actions to

 optimize the performance of your deployed RT application:

- Install only the minimum software set.
- Minimize the size of the VI to optimize caching effects.
- Build and run your RT project as a stand-alone application

Parent topic:

Real-Time Module Best Practices

<!--NI_TOPIC bundle=labview-real-time-module path=timing-deterministic-applications-real-time-module.html language=enus -->
## TOPIC 00077: Timing Deterministic Applications

- bundle_id: `labview-real-time-module`
- source_path: `timing-deterministic-applications-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/timing-deterministic-applications-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Because of the preemptive nature of the real-time operating system (RTOS) on RT targets, deterministic tasks can monopolize the processor on the target. A deterministic task might use all processor resources and not allow non-deterministic tasks in the application to execute. After separating the de

### Timing Deterministic Applications

Because of the preemptive nature of the real-time operating system (RTOS) on RT
 targets, deterministic tasks can monopolize the processor on the target. A
 deterministic task might use all processor resources and not allow non-deterministic
 tasks in the application to execute. After separating the deterministic tasks from non-deterministic tasks, you can
 use timing methods to ensure deterministic performance for deterministic tasks while
 allowing non-deterministic tasks to execute as needed.

You can use the Real-Time Timing VIs, timed structures, or external timing sources to
 time and control loop execution rates.

Note

Note

#### Timing Control Loops Using the Real-Time Timing VIs

Use the Real-Time Timing VIs, Wait and Wait Until Next Multiple, to time loops on RT targets. With the
 Real-Time Timing VIs, you can use the millisecond or microsecond timer of the RTOS
 running on an RT target to control the resolution of loops.

#### Wait VI

The Wait VI causes a VI to sleep for the specified amount of time. For example, you
 can use the Wait VI with Counter Unit set to milliseconds in
 a VI running on the RT target to provide loop rates up to 1 kHz. If the millisecond
 timer value of the RTOS is 112 ms when the Wait VI executes and the
 Count input equals 10, then the VI sleeps and does not
 return until the millisecond timer value equals 122 ms.

The following illustration shows the timing of a real-time application using the Wait
 VI. The application executes Function A, executes Function B, and then uses the Wait
 VI to sleep 10 ms after the execution of Function B.

[IMAGE alt='image' src='GUID-C04E0876-748D-46D1-92CB-B7A8787AAAFB-a5.png']

#### Wait Until Next Multiple VI

The Wait Until Next Multiple VI causes a thread to sleep until the value of the RTOS
 millisecond or microsecond timer equals a multiple of the
 Count input. For example, if the Wait Until Next Multiple
 VI executes with a Count input of 10 ms and the RTOS
 millisecond timer value is 112 ms, the VI that calls the Wait Until Next Multiple VI
 sleeps until the millisecond timer value equals 120 ms because 120 ms is the first
 multiple of 10 ms after the execution of the Wait Until Next Multiple VI.

The following illustration shows the timing of a real-time application using the Wait
 Until Next Multiple VI. The application executes Function A, executes Function B,
 and then sleeps until the value of the RTOS millisecond timer equals a multiple of
 20 ms, which is the time specified by the Count input of the
 Wait Until Next Multiple VI.

[IMAGE alt='image' src='GUID-6386D12C-3A0C-44F8-B655-422748036095-a5.png']

In the preceding illustration, the time of execution for the Wait Until Next Multiple
 VI varies depending on the execution of Function A and B. When Function A and B
 finish executing, the Wait Until Next Multiple VI executes until the operating
 system timer reaches the next multiple of 20 ms.

#### Defining the Order of Execution for Real-Time Timing VIs

Avoid using the Wait VI or Wait Until Next Multiple VI in parallel with other LabVIEW
 code, which can lead to unexpected timing behavior. Within a timed structure or a VI
 set to time-critical priority, only one thread is available, so the timing VI
 executes in sequence with the rest of the LabVIEW code despite being placed in
 parallel. In this case, LabVIEW serializes the parallel code paths while compiling
 the VI, and the execution order of the timing VI is subject to change from one
 compile to the next. On the other hand, when the code is not inside a timed
 structure or a time-critical VI, LabVIEW executes the timing VIs in parallel with
 the other LabVIEW code, which changes the effect of the timing VI.

To ensure well-defined timing behavior, use a Sequence structure to force a specific
 execution order. In the following block diagram, the Wait Until Next Multiple VI
 causes the VI to sleep until the millisecond timer reaches a multiple of 100 ms.
 When the VI returns from sleep, the VI begins to execute the next frame of the
 Sequence structure.

[IMAGE alt='image' src='GUID-B5DA77F8-3C3F-449D-B5E4-DD7760953987-a5.png']

#### Timing RT Target VIs Using Timed Structures

A Timed structure executes a subdiagram in a specific
 order with time bounds at a priority you specify. The priority setting of a timed
 structure specifies the priority of that timed structure relative to other timed
 structures executing on the target.

|  | Caution LabVIEW uses two separate but related priority schemes: VI priorities and timed structure priorities. Timed structure priorities are numeric, and a higher value represents a higher priority relative to other timed structures executing on the target. However, all timed structure priorities fall between the high and time-critical VI priority levels. To prevent undesired behavior, NI recommends using only one priority scheme in your application. If the application uses timed structures, keep all VIs at normal priority. |
| --- | --- |

#### Timed Loop

A Timed
 Loop executes a subdiagram, or frame, each iteration of the loop at the
 period you specify. Use the Timed Loop when you want to develop VIs with multirate
 timing capabilities, feedback on loop execution, timing characteristics that change
 dynamically, or several levels of execution priority.

Use the Configure Timed Loop dialog box to configure a timing source, period, priority, and other advanced options for the execution of the Timed Loop.

Because of the preemptive nature of Timed Loops, they can monopolize processor
 resources. A Timed Loop might use all of the processor resources, not allowing other
 tasks on the block diagram to execute. You must configure the highest priority Timed
 Loop with a period large enough to perform the deterministic task and have idle time
 during every iteration to allow lower priority loops to execute. The following Timed
 Loop contains a subVI that performs a data acquisition for 50 ms.

[IMAGE alt='image' src='GUID-97A7DDC5-C414-490D-8958-E5EF757191E4-a5.png']

The Timed Loop has a period of 100 ms that allows the loop to remain idle for 50 ms
 during each iteration. During the time when the Timed Loop remains idle, LabVIEW can
 execute lower priority tasks on the block diagram.

#### Timed Sequence

A Timed Sequence consists of one or more task subdiagrams, or frames, that
 execute sequentially and can be timed with an internal or external timing source.
 Use the Timed Sequence when you want to develop VIs with execution feedback, timing
 characteristics that change dynamically, or several levels of execution
 priority.

Use the Configure Timed Sequence dialog box to configure a timing source, priority, and other advanced options for the execution of the Timed Sequence.

#### Timed Loop with Frames Structure

You can add frames to a Timed Loop to execute multiple subdiagrams in sequence. A
 Timed Loop with frames behaves like a regular Timed Loop with an embedded Sequence
 structure.

#### Timing Deterministic Applications Using External Timing Sources

The NI drivers that run on RT targets support VIs or functions that can cause sleep
 in the current LabVIEW thread and then return when the driver detects a specific
 event. For example, you can use NI-DAQmx and NI data acquisition hardware to time
 real-time applications. Refer to the specific NI driver documentation for
 information about VIs or functions that you can use to sleep and wait for driver
 events.

#### Timing Real-Time Applications with NI-DAQmx

You can use NI data acquisition hardware with NI-DAQmx to match loop rates to match
 the rate of the hardware clock. With NI-DAQmx, you can use the following methods to
 time real-time applications:

- Hardware-Timed Single-Point —NI-DAQmx supports
 hardware-timed, single-point sample mode in which samples are acquired or
 generated continuously using hardware timing and no buffering. You can use
 hardware-timed, single-point mode for control applications that require input
 and/or output within a deterministic period of time. Refer to the
 NI-DAQmx Single-Point Real-Time Applications topic of the
 NI-DAQmx Help for information about using hardware-timed,
 single-point operations to time your deterministic application.
- Counter Timers —NI-DAQmx supports using hardware-timed
 counter input operations to drive a control loop. Use the Wait For Next Sample
 Clock VI to synchronize the counter operations with the counter's sample clock.
 Refer to the Hardware-Timed Counter Tasks topic of the
 NI-DAQmx Help for information about using counter input
 operations to time deterministic applications.
- DAQmx Timing Sources for Timed Structures —Timed
 structures can be hardware-timed and are ideal for multirate applications. By
 default, timed structures use the 1 kHz clock on Windows or the real-time
 operating system of an RT target as a timing source. You also can use an
 external signal on a DAQ device as the timing source of a timed structure using
 NI-DAQmx. Use the DAQmx Create Timing Source VI to create a timing source that
 can synchronize the timed structure with the hardware clock. Refer to the
 Hardware-Timed Simultaneously Updated I/O Using the Timed
 Loop topic of the NI-DAQmx Help for information
 about using an external signal on a DAQ device to control a timed
 structure.

Refer to the NI-DAQmx Help for more information about timing
 control loops using NI data acquisition hardware and NI-DAQmx software. Select
 Start»All Programs»National Instruments»NI-DAQ»NI-DAQmx
 Help to display the NI-DAQmx help.

Parent topic:

Real-Time Module Concepts

Related concepts:

- Creating Deterministic Applications Using the Timed Loop
- Creating Deterministic Applications Using VIs Set to Different Priorities
- Creating Deterministic Applications with the Real-Time Module

<!--NI_TOPIC bundle=labview-real-time-module path=tips-for-improving-ftp-transfers.html language=enus -->
## TOPIC 00078: Tips for Improving FTP Transfers

- bundle_id: `labview-real-time-module`
- source_path: `tips-for-improving-ftp-transfers.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/tips-for-improving-ftp-transfers.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: None Ensuring File Integrity To ensure file integrity when using FTP transfers, select the correct transfer mode for a file. The following transfer modes are available. ASCII—A transfer mode primarily used for text files Binary—A transfer mode primarily used for non-text files If you do not select a

### Tips for Improving FTP Transfers

None

#### Ensuring File Integrity

To ensure file integrity when using FTP transfers, select the correct transfer mode
 for a file. The following transfer modes are available.

- ASCII —A transfer mode primarily used for text files
- Binary —A transfer mode primarily used for non-text
 files

If you do not select a transfer mode, the FTP VIs detect which
 transfer mode to use by checking a file's extension. If you transfer files with
 uncommon extensions or no file extensions, this process can select the incorrect
 transfer mode and corrupt files.

To avoid file corruption when using the FTP VIs, wire TRUE to the
 binary input, as shown in the following block diagram, to
 transfer files in binary mode:

[IMAGE alt='image' src='GUID-10B0151D-B654-45A7-BCD6-AEB3290CC0AC-a5.png']

When using third-party FTP programs, refer to your FTP client's help for information
 about maintaining file integrity.

#### Ensuring Connection Stability

To prevent connections from being blocked by a firewall on the host computer, NI
 recommends using passive FTP transfers. Passive transfers reduce firewall-related
 connection instability by having the host computer initiate the connection with the
 RT target.

To set the transfer type as passive when using the FTP VIs, wire FALSE to the
 active input, as shown in the following block
 diagram:

[IMAGE alt='image' src='GUID-03296F5E-5CB4-4C5D-B9CD-A60003C93107-a5.png']

Note

- Passive FTP transfers take up more temporary connection ports than active
 FTP transfers. When designing applications, be aware of the number of
 connection ports the application uses.
- Additional connection issues can occur when using the FTP VIs to send files
 from the RT target to a third-party FTP program on another computer. Refer
 to your FTP client's help for more information.

As an alternative to using passive transfers, you can configure the firewall to make
 exceptions for FTP transfers. The programs requiring exceptions can range from
 LabVIEW or LabVIEW-built executables to third-party FTP programs.

Parent topic:

Organizing and Managing a LabVIEW Project with the Real-Time Module

<!--NI_TOPIC bundle=labview-real-time-module path=tutorial-creating-a-real-time-application.html language=enus -->
## TOPIC 00079: Tutorial: Creating a Real-Time Application

- bundle_id: `labview-real-time-module`
- source_path: `tutorial-creating-a-real-time-application.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/tutorial-creating-a-real-time-application.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: This tutorial teaches you how to create a basic real-time application using the Real-Time Module. The real-time application you learn about consists of two VIs: one that runs on the RT target and one that runs on the host computer. The VI on the RT target generates data from the RT target and stream

### Tutorial: Creating a Real-Time Application

This tutorial teaches you how to create a basic real-time application using the
 Real-Time Module. The real-time application you learn about consists of two VIs: one
 that runs on the RT target and one that runs on the host computer. The VI on the RT
 target generates data from the RT target and streams the data to the VI on the host
 computer. The VI on the host computer reads the data and displays it in a waveform
 graph.

This tutorial starts from a blank VI in order to provide a comprehensive learning
 experience. If you prefer to learn by modifying a working application, there are
 several templates and sample projects available to you. To access these templates,
 select Create Project from the LabVIEW Getting
 Started window to display the Create Project
 dialog box.

[IMAGE alt='image' src='GUID-74436463-E39F-47B9-827F-709028EE6FE1-a5.png']

[IMAGE alt='image' src='GUID-497E4030-CA61-4545-A310-4EFBB6C9EF54-a5.png']

[IMAGE alt='image' src='GUID-CE4B4C60-6055-4456-9295-5D5C1CA6B278-a5.png']

#### Before You Get Started

Verify that you can discover your RT target on the network and that it has software
 installed. Refer to the Remote Systems topic in the
 Measurement & Automation Explorer Help for more
 information about discovering RT targets and installing software. To open the
 Measurement & Automation Explorer Help, select
 Help»MAX Help from NI MAX.

#### Tutorial Contents

Part 1: Generating Data on the RT Target Learn how to create a producer loop that
 generates data on the RT target.

Part 2: Processing Data on the RT Target Learn how to create a consumer loop that
 processes data on the RT target, and how to transfer data deterministically from the
 producer loop to the consumer loop.

Part 3: Stopping Multiple Loops Simultaneously Learn how to use a network-published
 shared variable to create a means of stopping the producer loop and the consumer
 loop simultaneously.

Part 4: Building the User Interface Learn how to create a basic user interface on the
 host computer, and how to stop the loops running on the RT target using the UI you
 create.

Part 5: Sending RT Data to the Host Computer Learn how to use network streams to send
 data from the RT target to the host computer.

Part 6: Displaying RT Data on the User Interface Learn how to use network streams to
 receive RT target data on the host computer, and how to display the data on the user
 interface.

Parent topic:

Real-Time Module How-To

Related concepts:

- What is the Real-Time Module?
- Part 1: Generating Data on the RT Target
- Part 2: Processing Data on the RT Target
- Part 3: Stopping Multiple Loops Simultaneously
- Part 4: Building the User Interface
- Part 5: Sending RT Data to the Host Computer
- Part 6: Displaying RT Data on the User Interface
- Related Documentation

<!--NI_TOPIC bundle=labview-real-time-module path=understand-the-priority-based-scheduling-model-real-time-module.html language=enus -->
## TOPIC 00080: Understand the Priority-Based Scheduling Model

- bundle_id: `labview-real-time-module`
- source_path: `understand-the-priority-based-scheduling-model-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/understand-the-priority-based-scheduling-model-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic explains how the LabVIEW Real-Time Module handles priorities and execution systems when creating and scheduling threads. By understanding the priority-based scheduling model, you can leverage the strengths of the LabVIEW Real-Time Module to create deterministic applications. Threads, Prio

### Understand the Priority-Based Scheduling
 Model

This topic explains how the LabVIEW Real-Time Module handles priorities and

 execution systems when creating and scheduling threads. By understanding the

 priority-based scheduling model, you can leverage the strengths of the LabVIEW

 Real-Time Module to create deterministic applications.

#### Threads, Priorities, and Execution Systems

LabVIEW is a structured dataflow language that abstracts many of the underlying

 complexities of computer operation to create an intuitive graphical programming

 environment. To understand how LabVIEW schedules parallel tasks based on priority,

 it helps to define some key concepts that underlie the scheduling process in

 LabVIEW:

- Thread —The basic unit of concurrency in the LabVIEW

 Real-Time Module. Operations within a thread execute sequentially, while each

 thread executes independently.
- Scheduler —An algorithm the operating system uses to

 schedule threads. The scheduler determines which thread to run on each CPU in

 the system at any given time.
- Run Queue —The queue of threads ready to be

 scheduled.
- Preemptive Scheduling —The process whereby the scheduler

 interrupts a lower-priority thread as soon as a higher-priority thread is ready

 to run.
- Round-Robin Scheduling —The process whereby the scheduler

 switches periodically between threads of equal priority to promote equal sharing

 of processor time.
- Execution System —A pool of related threads. Use the Execution page of the VI

 Properties dialog box to configure the execution system of a VI.
- VI Priority —The priority you assign to a VI on the Execution page of the VI

 Properties dialog box.
- Timed Loop Priority —The priority you assign to a Timed

 Loop using either the Priority input or the

 Configure Timed Loop dialog box.
- OS Priority —The priority assigned to a thread by the

 real-time operating system. LabVIEW assigns each thread an OS priority based on

 the priority of the containing VI or Timed Loop.
- Time-Critical —The highest priority available for a

 LabVIEW VI. Time-critical threads run above the priority of the scheduler

 itself. Therefore, time-critical threads always run to completion or until

 blocked.
- Priority Inheritance —The process whereby a thread

 temporarily assumes the priority of the calling thread. Priority inheritance

 helps to prevent priority inversions.
- Jitter —A measure of the extent to which execution timing

 fails to meet deterministic expectations.

The following illustration summarizes the priorities and execution systems available

 in LabVIEW.

[IMAGE alt='image' src='GUID-C25FC6FF-559C-4561-88FA-41877AD3A536-a5.png']

The preceding illustration shows the following facts:

- Execution systems are independent of priority levels. LabVIEW uses execution

 systems only as thread pools and does not prioritize threads based on execution

 system. For each execution system, LabVIEW creates up to four threads at each

 priority level. This rule extends to each core in a multi-core system, so on a

 dual-core system, LabVIEW could create up to eight threads at each priority

 level for each execution system. Because the number of threads per execution

 system is limited, balancing your execution system assignments can be important.

 If you assign too many VIs to the same execution system, the VIs must share

 threads, limiting the potential parallelism of the VIs.
- Timed structure priorities fall between the high and time-critical VI priority

 levels.
- When you place parallel code inside a single Timed

 Structure, LabVIEW serializes the code because each timed structure

 comprises one and only one thread.
- LabVIEW Real-Time Module systems include many system threads running in

 parallel to the threads that comprise your LabVIEW VIs. These system threads

 execute at various priorities. For example, the NI Scan

 Engine thread, when present, runs by default at a priority above

 time-critical.

#### Priority Inheritance

LabVIEW implements priority inheritance to prevent unintended priority reductions. If

 a subVI is configured with a lower priority than that of the calling VI and both run

 within the same execution system, the subVI inherits the priority of the calling VI.

 If a subVI is configured with a priority higher than that of the calling VI, the

 subVI maintains its configured priority.

Note

The real-time operating system (RTOS) also implements priority inheritance. When a

 lower-priority thread holds a shared resource needed by a higher-priority thread,

 the RTOS temporarily increases the priority of the thread holding the shared

 resource so that the resource can return promptly to the higher-priority thread.

#### Time-Critical Priorities

There are two types of time-critical threads:

- VIs set to time-critical priority —VIs set to

 time-critical priority run above the priority of the scheduler itself.

 Therefore, VIs set to time-critical priority always run to completion or until

 blocked, typically by the inclusion of a timing function or a function that

 waits for an external event.
- Timed Structures —A Timed Structure can be interrupted by

 another Timed Structure of higher priority or by a VI set to time-critical

 priority.

Note

#### Timed Structure Priorities

LabVIEW uses two separate but related priority schemes: VI priorities and timed

 structure priorities. Timed structure priorities are numeric, and a higher value

 represents a higher priority relative to other timed structures executing on the

 target. However, all timed structure priorities fall between the high and

 time-critical VI priority levels.

Note

#### Avoiding Errors When Using Priority Schemes

National Instruments recommends using only one priority scheme in your application,

 as shown in the following examples:

- If the application uses timed structures, keep all VIs at normal priority.
- If the application uses VIs set to time-critical priority, do not place timed

 structures inside the VIs set to time-critical priority.

Using a single priority scheme makes the application easier to understand and less

 error prone.

#### Scheduling

Scheduling is the process of determining which task to run at a given time.

 Scheduling is a key task for any modern operating system, but especially for a

 real-time operating system (RTOS). In addition to threads spawned by your VIs, an RT

 target runs numerous OS and driver threads at various priorities. To ensure that

 your tasks execute according to your timing requirements, it helps to understand how

 LabVIEW Real-Time schedules threads.

#### Basic RT Scheduling Rules

The following rules summarize the operation of the LabVIEW Real-Time scheduler when a

 new thread enters the run queue:

1. Perform preemptive scheduling among threads of different priority.
2. Perform round-robin scheduling among threads of equal priority.
3. Time-critical threads always run to completion.

#### Understanding How LabVIEW Real-Time Module Scheduling Works

At any given time, each thread in the system is either running or blocked:

- Running —The thread is in the run queue, which means it is

 either ready to execute or is currently executing.
- Blocked —The thread cannot execute until some event

 occurs, such as the completion of an I/O operation or a timing function.

When a thread begins executing, it runs until one of the following conditions

 arises:

- The thread becomes blocked by a Wait VI within a

 While Loop, the built-in timing mechanism of a Timed

 Loop, or a blocking function such as the Read Variable with

 Timeout function.
- The thread is interrupted by a higher-priority thread.
- The thread finishes executing.

When a thread becomes unblocked, it enters the run queue. The run queue is always

 sorted in priority order, so when a thread enters this queue, it immediately moves

 ahead of all lower-priority threads. If a thread entering the run queue is

 higher-priority than a currently-running thread, the higher-priority thread either

 runs on a different CPU core or interrupts the currently-running thread in a process

 called preemptive scheduling.

#### Preemptive Scheduling

Preemptive scheduling is the process of ordering thread execution based on the

 relative priorities of the threads. When a thread of higher priority than the

 current thread enters the run queue, the scheduler interrupts the current thread if

 necessary so that the higher-priority thread can execute immediately. The

 interrupted thread then returns to the run queue behind the higher-priority

 thread.

#### Round Robin Scheduling

Round robin scheduling is the process of alternating between threads such that each

 thread receives roughly equivalent CPU time. During round robin scheduling, the

 scheduler interrupts and switches between the threads at regular intervals, keeping

 track of the CPU time given to each thread.

The LabVIEW Real-Time Module performs round robin scheduling among threads of equal

 priority. However, the LabVIEW Real-Time Module does not perform round-robin

 scheduling among VIs set to time-critical priority.

#### Setting Loop Priorities Based on Timing Requirements

Although it seems intuitive to set the priority of each loop based on the perceived

 importance of the loop, this strategy can cause jitter. Set the priority of each

 loop not based on how critical the task is within the application but rather based

 on how important it is that the task fulfill a certain timing guarantee. For

 example, in a data logging application with a data acquisition loop and a logging

 loop, you might be tempted to make the logging loop the higher-priority loop.

 However, data acquisition must occur at regular intervals to avoid missed data

 points. However, it does not matter when you log each data point to disk, as long as

 you log each point eventually. In this case, you should assign a higher priority to

 the data acquisition loop, even though data logging is the primary purpose of the

 application.

Parent topic:

Real-Time Module Best Practices

<!--NI_TOPIC bundle=labview-real-time-module path=use-shared-variables-effectively-real-time-module.html language=enus -->
## TOPIC 00081: Use Shared Variables Effectively

- bundle_id: `labview-real-time-module`
- source_path: `use-shared-variables-effectively-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/use-shared-variables-effectively-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic contains guidelines for using shared variables effectively in LabVIEW Real-Time Module applications. Use the Appropriate Number of Shared Variables To minimize CPU usage, avoid using too many network-published shared variables. For high-channel-count applications, consider combining the c

### Use Shared Variables Effectively

This topic contains guidelines for using shared variables effectively in LabVIEW


 Real-Time Module applications.

#### Use the Appropriate Number of Shared Variables

To minimize CPU usage, avoid using too many network-published shared variables. For


 high-channel-count applications, consider combining the channels into a single array


 and using a single network-published shared variable to transfer the array.

#### Use Shared Variables with the RT FIFO Enabled for Deterministic


 Communication

LabVIEW provides several


 options for transferring data between tasks running in separate loops.


 However, most of these options can impact determinism. Therefore, the LabVIEW


 Real-Time Module provides shared


 variables with the RT FIFO enabled for communication between a


 deterministic loop and a non-deterministic loop.

Refer to the RT FIFO Variables - local.lvproj in the


 labview\examples\Real-Time Module\RT Communication\RT FIFO


 Variables directory for examples of using Shared Variables with RT FIFO


 enabled.

#### Avoid Unnecessary Buffering

Buffering consumes CPU and memory resources. Place a checkmark in the


 Use Buffering checkbox on the Network page of


 the Shared Variable Properties dialog box only when you need


 to read every value written to a network-published shared variable. Although


 buffering can help prevent data loss caused by temporary networking delays,


 buffering does not guarantee lossless data transfer. Buffers can overflow, causing


 LabVIEW to overwrite old data and generate a warning.

#### Use Programmatic Access in High-Channel-Count Applications

Use the programmatic access functions on the Shared Variable palette to create clean, scalable block


 diagrams in high-channel-count applications.

#### Serialize Shared Variable Execution

Improve performance and prevent race conditions by executing shared variable


 accessors serially. Use the error in and error


 out terminals of the Shared Variable node or the Shared Variable


 programmatic access functions to serialize execution. By explicitly serializing


 execution, you can minimize scheduling overhead and thus improve performance.

For example, the following block diagram reads from three shared variables in


 parallel:

[IMAGE alt='image' src='GUID-A957C4C6-9C04-4535-A792-69DD1C8C73A1-a5.png']

The following block diagram uses the error in and


 error out terminals of the Shared Variable nodes to


 serialize execution:

[IMAGE alt='image' src='GUID-B513C6FE-308F-4E5C-A8FB-27A708BB3242-a5.png']

#### Avoid Reading Stale Shared Variable Data

To prevent reading the same value repeatedly in a loop, use the ms


 timeout input of a Shared Variable


 node or the Read Variable with Timeout function. To add a


 ms timeout input to the Shared Variable node, right-click


 the Shared Variable node and select Show Timeout from the


 shortcut menu. You only can enable a timeout period for Shared Variable nodes


 configured to read data. You cannot enable a timeout period for nodes that access


 I/O variables locally.

To prevent reading stale data from a previous run of your application, undeploy and


 redeploy shared variable libraries to clear all shared variable values. Use the


 Shared Variable Deployment page of the Application Properties dialog box to configure a stand-alone RT application to deploy shared variables


 before running the application and undeploy shared variable libraries when the


 application exits.

#### Initialize Your Shared Variables

To safeguard your application against stale shared variable data, initialize all your


 shared variables before running the ongoing task loops of your application. To


 initialize an unbuffered network-published shared variable hosted on another


 computer, write the default value to the shared variable, then wait for the


 initialized value to propagate through the network to the Shared Variable Engine


 running on the host computer and back to the RT target. The following block diagram


 shows an example of unbuffered network-published shared variable initialization:

[IMAGE alt='image' src='GUID-5A1C43D5-58FE-4291-A9AF-16626D7D2A10-a5.png']

Note

#### Select an Appropriate Device to Host Shared Variables

In some cases, hosting shared variables on the RT target makes sense. In other cases,


 it is more appropriate to host shared variables on a host PC. Before finalizing your


 application, ensure that you are hosting shared variables on the most appropriate


 device. The following table summarizes the advantages and disadvantages of hosting


 shared variables on an RT target:

| Advantages | Disadvantages |
| --- | --- |
| Multiple PCs can access shared variables hosted by a single RT target | Adds CPU overhead on the RT target |
| High uptime due to the stability of the RT target | Adds memory overhead on the RT target |

Parent topic:

Real-Time Module Best Practices

Related concepts:

- Minimize CPU Usage

<!--NI_TOPIC bundle=labview-real-time-module path=user-manual-welcome.html language=enus -->
## TOPIC 00082: LabVIEW Real-Time Module User Manual

- bundle_id: `labview-real-time-module`
- source_path: `user-manual-welcome.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/user-manual-welcome.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The LabVIEW Real-Time Module User Manual provides detailed descriptions of the product functionality and the step by step processes for use. Looking for Something Else?For information not found in the User Manual for your product, such as specifications and API reference, browse Related Information.

### LabVIEW
 Real-Time Module
 User Manual

The LabVIEW
 Real-Time Module User Manual provides detailed
 descriptions of the product functionality and the step by step processes for use.

#### Looking for Something Else?

For information not found in the User Manual
 for your product, such as specifications and API reference, browse *Related
 Information*.

Related information:

- Software and Driver Downloads
- Release Notes
- Interactive Activation Guide
- Dimensional Drawings
- Product Certifications
- Letter of Volatility
- Discussion Forums
- NI Learning Center

<!--NI_TOPIC bundle=labview-real-time-module path=using-and-defining-error-codes-real-time-module.html language=enus -->
## TOPIC 00083: Using and Defining Error Codes

- bundle_id: `labview-real-time-module`
- source_path: `using-and-defining-error-codes-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/using-and-defining-error-codes-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use error handling to debug and manage errors in VIs. The LabVIEW error handler VIs return error codes when an error occurs in a VI. Error codes reveal the specific problem the VI encountered. When you configure an RT target, LabVIEW automatically copies the error code files used by the error handle

### Using and Defining Error Codes

Use error handling to debug and manage errors in VIs. The LabVIEW error handler VIs
 return error codes when an error occurs in a VI. Error codes reveal the specific
 problem the VI encountered. When you configure an RT target, LabVIEW automatically
 copies the error code files used by the error handler VIs to the target.

You can use custom error codes with VIs that run on an RT target.
 Create error files using the Error Code
 Editor dialog box. Select Tools»Advanced»Edit Error
 Codes to open the Error Code File Editor
 dialog box. If you use custom errors on an RT target, you must rename the files to
 use a *.err extension and then place the error files in the
 c:\ni-rt\system\user.lib\errors directory or the
 c:\ni-rt\system\errors directory on the target. (NI Linux
 Real-Time) Place the error files in the
 /usr/local/natinst/labview/errors directory.

Parent topic:

Debugging Deterministic Applications

<!--NI_TOPIC bundle=labview-real-time-module path=using-labview-projects-with-the-real-time-module-real-time-module.html language=enus -->
## TOPIC 00084: Using LabVIEW Projects with the Real-Time Module

- bundle_id: `labview-real-time-module`
- source_path: `using-labview-projects-with-the-real-time-module-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/using-labview-projects-with-the-real-time-module-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use LabVIEW projects to group LabVIEW files and files not specific to LabVIEW, create build specifications, and deploy or download VIs to an RT target. When you save a project, LabVIEW creates a project file (.lvproj), which includes references to files in the project, configuration information, bui

### Using LabVIEW Projects with the Real-Time Module

Use LabVIEW projects to group LabVIEW files and files not specific to LabVIEW,
 create build specifications, and deploy or download VIs to an RT target. When you
 save a project, LabVIEW creates a project file
 (.lvproj), which includes references to files in the project,
 configuration information, build information, and deployment information. You must
 use a project to work with an RT target and to build stand-alone applications.

#### Real-Time Project Wizard

You can create a new project with the Real-Time Project Wizard, available by
 selecting Tools»Real-Time Module»Project Wizard.

#### Project Explorer Window

You also can create a new project manually with the Project Explorer window. Use the
 Project Explorer window to create and edit LabVIEW
 projects. Select File»New Project to display the
 Project Explorer window.

Parent topic:

Organizing and Managing a LabVIEW Project with the Real-Time Module

Related concepts:

- Real-Time System Components
- Creating and Editing LabVIEW Projects with the Project Explorer Window

<!--NI_TOPIC bundle=labview-real-time-module path=using-parallel-operations-in-multiple-cpu-rt-applications-real-time-module.html language=enus -->
## TOPIC 00085: Using Parallel Operations in Multiple-CPU RT Applications

- bundle_id: `labview-real-time-module`
- source_path: `using-parallel-operations-in-multiple-cpu-rt-applications-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/using-parallel-operations-in-multiple-cpu-rt-applications-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: LabVIEW's multithreaded graphical programming environment makes it easy to take advantage of parallel execution on multiple-CPU systems, also known as multi-core, multi-processor, or SMP systems. To implement a parallel architecture in LabVIEW, place two or more objects on the block diagram without

### Using Parallel Operations in Multiple-CPU RT Applications

LabVIEW's multithreaded graphical programming environment makes it easy to take
 advantage of parallel execution on multiple-CPU systems, also known as multi-core,
 multi-processor, or SMP systems. To implement a parallel architecture in LabVIEW,
 place two or more objects on the block diagram without wiring them in sequence. When
 a VI executes on a system with N CPUs, up to N
 threads can execute in parallel. You can separate code into parallel loops or you
 can take advantage of parallel data processing by separating multiple input channels
 to be processed on separate CPUs.

Note

#### Parallel Loops

When you include parallel loops in an RT application that runs on a multiple-CPU
 system, the CPU scheduler performs automatic load balancing to distribute execution
 threads across the CPUs. You also can use the Assigned CPU
 input of a Timed Loop to manually assign a Timed Loop to a given
 CPU.

Note

#### Parallel Data Processing

You can separate multiple data channels into groups and process the groups in
 parallel on separate CPUs. For example, if you need to process 16 input channels on
 a dual core system, you can separate them into two groups of eight, as shown in the
 following block diagram:

[IMAGE alt='image' src='GUID-F42E48FC-3FED-49C6-A6EA-1B01DE5D657F-a5.png']

In this example, Process Data.vi is configured as a reentrant subVI,
 so each instance of the subVI receives a dedicated memory space, and the two
 instances do not have to execute on the same CPU. Because there is no dataflow
 dependency between the two instances of Process Data.vi, the CPU scheduler
 automatically balances the two instances across the available CPUs.

Note

Parent topic:

Optimizing RT Applications for Multiple-CPU Systems

Related concepts:

- Optimizing RT Applications for Multiple-CPU Systems
- Avoiding Shared Resources

<!--NI_TOPIC bundle=labview-real-time-module path=using-remote-front-panels-to-access-rt-target-vis-real-time-module.html language=enus -->
## TOPIC 00086: Using Remote Front Panels to Access RT Target VIs

- bundle_id: `labview-real-time-module`
- source_path: `using-remote-front-panels-to-access-rt-target-vis-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/using-remote-front-panels-to-access-rt-target-vis-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use remote front panels to view and control the front panel of a VI running on an RT target with LabVIEW. Only one user may control the front panel of a VI at any specific time, but several users at different locations can view the front panel simultaneously. You must enable the Web Server on the

### Using Remote Front Panels to Access RT Target VIs

Use remote front panels to view and control the front panel of a VI running on an RT target with
 LabVIEW. Only one user may control the front panel of a VI at any specific time, but
 several users at different locations can view the front panel simultaneously.

Note

Refer to the following topics to learn more about using remote front panels to access
 RT target VIs:

- Enabling Remote Front Panel Connections to RT Target VIs
- Adding New Entries to Browser Access List of an RT Target
- Viewing and Controlling the Front Panels of RT Target VIs Remotely

For an overview of the different methods you can use to display the front panels of
 RT target VIs, refer to the Interacting with the
 Front Panels of RT Target VIs topic.

Parent topic:

Interacting with the Front Panels of RT Target VIs

Related concepts:

- Viewing and Controlling the Front Panels of RT Target VIs Remotely (Real-Time Module)
- Adding New Entries to Browser Access List of an RT Target

Related tasks:

- Enable Remote Front Panel Connections to RT Target VIs

<!--NI_TOPIC bundle=labview-real-time-module path=using-the-embedded-ui-to-access-rt-target-vis-real-time-module.html language=enus -->
## TOPIC 00087: Using the Embedded UI to Access RT Target VIs

- bundle_id: `labview-real-time-module`
- source_path: `using-the-embedded-ui-to-access-rt-target-vis-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/using-the-embedded-ui-to-access-rt-target-vis-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Refer to the following topics to learn about using the embedded UI to access RT target VIs: Enabling the Embedded UI on RT Targets Viewing and Controlling the Front Panels of RT Target VIs Using the Embedded UI Customizing How Front Panels Display on the Embedded UI For an overview of the different

### Using the Embedded UI to Access RT Target VIs

Refer to the following topics to learn about using the embedded UI to access RT
 target VIs:

- Enabling the Embedded UI on RT Targets
- Viewing and Controlling the Front Panels of RT Target VIs Using the
 Embedded UI
- Customizing How Front Panels Display on the Embedded UI

For an overview of the different methods you can use to display the front panels of
 RT target VIs, refer to the Interacting with the
 Front Panels of RT Target VIs topic.

Parent topic:

Interacting with the Front Panels of RT Target VIs

Related concepts:

- Enabling the Embedded UI on RT Targets
- Viewing and Controlling the Front Panels of RT Target VIs Using the Embedded UI
- Customizing How Front Panels Display on the Embedded UI

<!--NI_TOPIC bundle=labview-real-time-module path=using-watchdog-hardware-to-recover-from-embedded-software-failures-real-time-module.html language=enus -->
## TOPIC 00088: Using Watchdog Hardware to Recover from Embedded Software Failures

- bundle_id: `labview-real-time-module`
- source_path: `using-watchdog-hardware-to-recover-from-embedded-software-failures-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/using-watchdog-hardware-to-recover-from-embedded-software-failures-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Many embedded real-time systems need to be self-reliant. It is often impractical to wait for someone to restart an embedded system if a software failure occurs. Therefore, the embedded system itself must be able to detect a failure condition and execute a graceful recovery procedure. To detect and r

### Using Watchdog Hardware to Recover from
 Embedded Software Failures

Many embedded real-time systems need to be self-reliant. It is often impractical to
 wait for someone to restart an embedded system if a software failure occurs.
 Therefore, the embedded system itself must be able to detect a failure condition and
 execute a graceful recovery procedure. To detect and recover from software failures,
 many embedded systems contain a built-in hardware timer known as a watchdog timer or
 a dead man's switch. You can use a watchdog timer to ensure that an embedded
 software process continues to execute normally and to initiate a recovery procedure
 if the software becomes unresponsive.

#### Understanding the Hardware-Software Interface

A watchdog timer is a hardware counter that interfaces with the embedded software
 application to detect and recover from software failures. During normal operation,
 the software application initiates the hardware timer to count down from a specific
 number at a known increment and defines the action to take if the timer reaches
 zero. After the application starts the watchdog timer, it periodically resets the
 timer to ensure that the timer never reaches zero, as shown in the illustration
 below:

[IMAGE alt='image' src='GUID-44BE7180-1E4A-4141-84D1-1AC1D7E00C7F-a5.png']

If a software failure prevents the application from resetting the timer, the timeout
 eventually expires because the hardware counter is independent of the software and
 thus continues to count down until it reaches zero. When the watchdog timer expires,
 the hardware triggers the recovery procedure, as shown in the illustration
 below:

[IMAGE alt='image' src='GUID-DB769972-8882-4CB5-9200-B9A92A8D630B-a5.png']

RT Series PXI, CompactRIO, and Compact FieldPoint controllers contain built-in
 watchdog timer hardware that you can access using the RT
 Watchdog VIs. Use the Watchdog
 Configure VI to set a timeout for the watchdog timer, and to specify the
 action(s) to perform if the timeout expires. Use the Watchdog
 Whack VI to periodically reset the counter before the timeout
 expires.

Note

#### Choosing an Appropriate Timeout Setting

The appropriate range of timeout values depends on the specific performance
 characteristics and up-time requirements of the embedded application. You must set
 the timeout long enough so that it does not expire due to acceptable levels of
 system jitter. However, you must set the timeout short enough so that the system can
 recover from failure quickly enough to meet system up-time requirements.

#### Using the Advanced Watchdog VIs

The high-level Watchdog VIs, Watchdog Configure, Watchdog Whack, and Watchdog Clear,
 are built from the low-level Advanced
 Watchdog VIs. If you cannot meet your application requirements using the
 high-level Watchdog VIs, you can use the Advanced Watchdog VIs to implement custom
 watchdog applications.

#### Creating Multiple Watchdog Objects

You can create multiple watchdog objects with separate properties using either the
 Watchdog Configure VI or the Advanced Watchdog VIs. Multiple watchdog objects might
 be useful for applications that include distinct states of operation with different
 timing characteristics. For example, if you implement a state machine architecture
 with states A and B, you can use a watchdog object with a timeout value of 5 seconds
 in state A and another watchdog object with a timeout value of 10 seconds in state
 B.

However, because RT targets typically contain only one hardware watchdog timer, you
 can use only one watchdog object at a time. After using a watchdog object, you must
 use the Watchdog Clear VI or the Advanced Watchdog VIs to close
 the current watchdog object before you can use another watchdog object.

Parent topic:

Creating Stand-Alone Real-Time Applications

<!--NI_TOPIC bundle=labview-real-time-module path=verifying-correct-application-behavior-real-time-module.html language=enus -->
## TOPIC 00089: Verifying Correct Application Behavior

- bundle_id: `labview-real-time-module`
- source_path: `verifying-correct-application-behavior-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/verifying-correct-application-behavior-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: To debug an RT application, first use the LabVIEW debugging tools to detect errors and step through the flow of execution to locate the error source. Then, use the Profile Performance and Memory window or the Real-Time Trace Viewer to test the execution timing and memory usage of the application. La

### Verifying Correct Application Behavior

To debug an RT application, first use the LabVIEW debugging
 tools to detect errors and step through the flow of execution to locate
 the error source. Then, use the Profile Performance and
 Memory window or the Real-Time Trace Viewer to test the execution timing and
 memory usage of the application.

#### LabVIEW Debugging Tools

Use the LabVIEW debugging tools, such as execution highlighting and single-stepping,
 while the host computer is connected to an RT target to step through LabVIEW
 code.

Note

The only feature not supported by the Real-Time Module is the Call
 list pull-down menu, which appears in the toolbar of a subVI block
 diagram window while single-stepping.

Note

Allow
 debugging

Execution

#### Profile Performance and Memory Window

The Profile Performance and Memory window is a powerful tool for
 statistically analyzing how an application uses execution time and memory. You can
 use the Profile Performance and Memory window to display
 performance information for all VIs and subVIs in memory. This information can help
 you optimize the performance of your VIs by identifying potential bottlenecks.
 Select Tools»Profile»Performance and Memory to display the
 Profile Performance and Memory window.

You must place a checkmark in the Profile memory usage
 checkbox before starting a profiling session. Collecting information about VI memory
 use adds a significant amount of overhead to VI execution, which affects the
 accuracy of any timing statistics gathered during the profiling session. Therefore,
 perform memory profiling separate from time profiling to return an accurate
 profile.

During a profiling session, you can take a snapshot of the available data and save it
 to an ASCII spreadsheet file. The timing measurements accumulate each time you run a
 VI.

Note

Profile Performance and
 Memory

#### NI Distributed System Manager

The NI
 Distributed System Manager displays details about VIs running on an RT
 target and provides a dynamic display of the memory and CPU resources for the
 target. You can stop VIs and start idle VIs on the RT target using NI Distributed
 System Manager. To launch the NI Distributed System Manager from LabVIEW, select
 Tools»Distributed System Manager.

#### Debug Application or Shared Library Dialog Box

Use the Debug Application or Shared Library dialog box to debug
 stand-alone real-time applications running on an RT target.

Note

Enable
 debugging

Parent topic:

Debugging Deterministic Applications

Related concepts:

- Debugging Deterministic Applications

<!--NI_TOPIC bundle=labview-real-time-module path=verifying-correct-timing-behavior-real-time-module.html language=enus -->
## TOPIC 00090: Verifying Correct Timing Behavior

- bundle_id: `labview-real-time-module`
- source_path: `verifying-correct-timing-behavior-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/verifying-correct-timing-behavior-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Timing is crucial in a deterministic application. Use one of the following methods to verify the timing of an application. Real-Time Benchmarking VIs Use the RT Get Timestamp VI and the RT Timestamp Analysis VI to benchmark the performance of VIs and sections of VIs running on an RT target. You can

### Verifying Correct Timing Behavior

Timing is crucial in a deterministic application. Use one of the following methods to
 verify the timing of an application.

#### Real-Time Benchmarking VIs

Use the RT Get Timestamp VI and the RT Timestamp
 Analysis VI to benchmark the performance of VIs and sections of VIs
 running on an RT target. You can use the benchmark information to optimize the
 design of RT target VIs.

Use the RT Get Timestamp VI to return a 64-bit timestamp value from a high-precision
 timing source. Use the RT Timestamp Analysis VI to analyze the timestamp values
 returned by the RT Get Timestamp VI.

#### Real-Time Trace Viewer

The Real-Time
 Trace Viewer is a real-time event and execution tracing tool that allows
 you to capture and display the timing and event data of VI and thread events for
 LabVIEW Real-Time Module applications. The Real-Time Trace Viewer includes the
 Real-Time Trace Viewer VIs. You can use the Real-Time Trace Viewer VIs to capture
 the timing and execution data of VI and thread events for applications running on an
 RT target. The Real-Time Trace Viewer displays the timing and event data on the host
 computer for analysis.

#### Monitoring Real-Time Target Resources

You can use the NI Distributed System Manager to monitor the resource
 utilization of an RT target and to view details about VIs running on the target. In
 some cases, application timing failures are caused by insufficient memory or CPU
 resources on the RT target.

Note

Parent topic:

Debugging Deterministic Applications

Related concepts:

- Debugging Deterministic Applications

<!--NI_TOPIC bundle=labview-real-time-module path=viewing-and-controlling-the-front-panels-of-rt-target-vis-remotely-real-time-module.html language=enus -->
## TOPIC 00091: Viewing and Controlling the Front Panels of RT Target VIs Remotely (Real-Time Module)

- bundle_id: `labview-real-time-module`
- source_path: `viewing-and-controlling-the-front-panels-of-rt-target-vis-remotely-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/viewing-and-controlling-the-front-panels-of-rt-target-vis-remotely-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can view and control the front panel of a VI running on an RT target with LabVIEW. If more than one remote connection requests control of the VI, the first connection assumes control. The RT target grants control to the other remote connections according to the order in which they requested cont

### Viewing and Controlling the Front Panels of RT Target VIs Remotely (Real-Time
 Module)

You can view and control the front panel of a VI running on an RT target with
 LabVIEW. If more than one remote connection requests control of the VI, the first
 connection assumes control. The RT target grants control to the other remote
 connections according to the order in which they requested control.

Note

Complete the following steps to view and control the front panel of an RT target VI
 from a remote computer using LabVIEW:

Note

1. Select Operate»Connect to Remote Panel from the Project
 Explorer window to launch the Connect to Remote Panel dialog box.
2. Enter the IP address or name of the RT target you want to connect to in the
 Server address text box.
3. Enter the name of the VI whose front panel you want to view in the VI
 name text box.
4. Enter the HTTP port for the Web Server on the RT target in the
 Port text box. The default is 80.
5. Place a checkmark in the Request control checkbox if you
 want to immediately request control of the front panel.
6. Click the Connect button. The front panel appears on the
 host computer, allowing you to view and control it.
7. If you did not place a checkmark in the Request control 
 checkbox, right-click on the front panel and select Request Control
 of VI from the shortcut menu to request control of the VI.

To completely close the connection to the Web Server running on the RT target, close
 the LabVIEW window. However, if you want to release control of the front panel but
 maintain a connection so you can view the front panel, right-click on the front
 panel and select Remote Panel Client»Release Control of VI
 from the shortcut menu.

Parent topic:

Using Remote Front Panels to Access RT Target VIs

Related concepts:

- Viewing and Controlling the Front Panels of RT Target VIs Remotely (Real-Time Module)
- Adding New Entries to Browser Access List of an RT Target

Related tasks:

- Enable Remote Front Panel Connections to RT Target VIs

<!--NI_TOPIC bundle=labview-real-time-module path=viewing-and-controlling-the-front-panels-of-rt-target-vis-using-the-embedded-ui-real-time-module.html language=enus -->
## TOPIC 00092: Viewing and Controlling the Front Panels of RT Target VIs Using the Embedded UI

- bundle_id: `labview-real-time-module`
- source_path: `viewing-and-controlling-the-front-panels-of-rt-target-vis-using-the-embedded-ui-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/viewing-and-controlling-the-front-panels-of-rt-target-vis-using-the-embedded-ui-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can view the front panels of VIs running on the RT target on a display device connected to the RT target. Additionally, you can transfer control of the front panel to the RT target in order to interact with front panel objects using input devices connected directly to the RT target. Viewing Fron

### Viewing and Controlling the Front Panels of RT
 Target VIs Using the Embedded UI

You can view the front panels of VIs running on the RT target on a display device
 connected to the RT target. Additionally, you can transfer control of the front
 panel to the RT target in order to interact with front panel objects using input
 devices connected directly to the RT target.

#### Viewing Front Panels

Complete the following steps to view front panels using the embedded UI:

1. Connect a display device to the RT target. You also can connect other UI
 devices, such as a mouse and keyboard.
2. Enable the embedded UI on the RT target.
3. Add the RT target to a LabVIEW project.
4. Add a VI under the RT target in the Project Explorer 
 window.
5. Right-click a VI under the RT target in the Project
 Explorer window and select Deploy .
6. Run the VI from the host computer.

The front panel of the VI displays on the display device connected to the RT target.
 Although you can now view the front panel, you cannot yet interact with front panel
 objects using input devices connected to the RT target. To transfer control of the
 front panel from the host computer to the RT target, complete the steps in the next
 section.

#### Controlling Front Panels

After you deploy a VI to an RT target, complete the following steps to transfer
 control of the front panel to the embedded UI:

1. If necessary, run the VI from the host computer to display the front panel on
 the embedded UI.
2. Right-click the RT target in the Project Explorer window
 and select Disconnect .

You can now interact with front panel controls, indicators, and menu items, as well
 as stop and run the VI, using the embedded UI.

Tip

Parent topic:

Using the Embedded UI to Access RT Target VIs

Related concepts:

- Enabling the Embedded UI on RT Targets
- Adding RT Targets to a LabVIEW Project
- Building and Deploying a Stand-Alone Real-Time Application
- Customizing How Front Panels Display on the Embedded UI

<!--NI_TOPIC bundle=labview-real-time-module path=viewing-trace-sessions-real-time.html language=enus -->
## TOPIC 00093: Viewing Traces

- bundle_id: `labview-real-time-module`
- source_path: `viewing-trace-sessions-real-time.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/viewing-trace-sessions-real-time.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: Learn how to analyze timing and execution behavior by opening trace sessions captured on an RT target in KernelShark. Use trace viewing to investigate latency spikes, missed iterations, preemption, blocking, and hangs by correlating thread activity and event timestamps. After you capture and export

### Viewing Traces

Learn how to analyze timing and execution behavior by opening trace sessions captured
 on an RT target in KernelShark. Use trace viewing to investigate latency spikes, missed
 iterations, preemption, blocking, and hangs by correlating thread activity and event
 timestamps.

After you capture and export a trace from an RT target, you can open the trace on the
 host computer in KernelShark to review timing and execution behavior on a timeline. Use
 trace viewing when you need to understand what the operating system and application
 threads were doing around a latency spike, missed loop iteration, or hang.

#### What
 to Look for in a Trace

A trace helps you investigate timing problems that
 are difficult to explain with logs alone, such as:

- Latency spikes and jitter that affect deterministic code paths
- Missed Timed Loop iterations and unexpected execution gaps
- Preemption patterns where other work repeatedly interrupts time-critical
 execution
- Blocking and contention that align with shared resources or I/O
- Hangs or stalls where execution stops progressing as expected

If your trace includes user events, use those markers to align the trace
 timeline with key application milestones during analysis.

#### How
 to Interpret LabVIEW Real-Time Activity in KernelShark

KernelShark helps
 you correlate thread execution, event timestamps, and timing patterns in the same
 view. Start by narrowing the view to the time window where the problem occurs, then
 focus on the threads that matter to your analysis.

- A critical thread staying runnable but not running
- Frequent preemption during intervals where you expect deterministic
 behavior
- Repeated blocking intervals that align with shared resources or I/O
 boundaries

- Timed Loop threads often map to time-sensitive execution you care about
 most
- Worker and execution threads can indicate where diagram execution
 occurs
- Background or infrastructure activity can explain competing CPU demand
 during the problem window

Note

Tracing on NI Linux
 Real-Time

Parent topic:

Real-Time Tracing

Related information:

- Tracing on NI Linux Real-Time

<!--NI_TOPIC bundle=labview-real-time-module path=what-is-real-time-module.html language=enus -->
## TOPIC 00094: What is the Real-Time Module?

- bundle_id: `labview-real-time-module`
- source_path: `what-is-real-time-module.html`
- source_url: https://docs-be.ni.com/bundle/labview-real-time-module/raw/resource/enus/what-is-real-time-module.html
- document_id: `labview-real-time-module`
- page_type: `leaf`
- content_type: `concept`
- source_description: The Real-Time Module is a LabVIEW add-on used to create reliable, stand-alone applications that execute on embedded hardware devices. The LabVIEW Real-Time (RT) Module extends the capabilities of LabVIEW to address the need for real-time performance. The Real-Time Module combines LabVIEW graphical p

### What is the Real-Time Module?

The *Real-Time Module* is a LabVIEW add-on used to create reliable,
 stand-alone applications that execute on embedded hardware
 devices.

The LabVIEW Real-Time (RT) Module extends the capabilities of LabVIEW to address the need
 for real-time performance. The Real-Time Module combines LabVIEW graphical programming
 with the power of a real-time operating system, enabling you to build deterministic
 applications. You develop VIs in LabVIEW and execute the VIs on an RT target. The RT
 target can run VIs in a stable platform optimized for real-time performance.

Browse the related topics to help you get started building a LabVIEW Real-Time application.

Related concepts:

- Real-Time Module Best Practices
- Tutorial: Creating a Real-Time Application
