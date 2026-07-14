# NI DOCUMENT BUNDLE: labview-nxg-rt-module-programming-with-rt-target

<!--NI_BUNDLE_CHUNK bundle=labview-nxg-rt-module-programming-with-rt-target start=1 end=22 -->
<!--NI_TOPIC bundle=labview-nxg-rt-module-programming-with-rt-target path=automatic-load-balancing.html language=enus -->
## TOPIC 00001: Automatic Load Balancing

- bundle_id: `labview-nxg-rt-module-programming-with-rt-target`
- source_path: `automatic-load-balancing.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-programming-with-rt-target/raw/resource/enus/automatic-load-balancing.html
- document_id: `labview-nxg-rt-module-programming-with-rt-target`
- page_type: `leaf`
- content_type: `concept`
- source_description: Automatic load balancing is the process of assigning threads to CPUs in a way that balances the processing load across CPUs in a real-time operating system (RTOS). LabVIEW maintains two pools of CPUs available for automatic load balancing: a Timed Structures pool and a System pool. CPUs in the Timed

Automatic Load Balancing

Automatic load balancing is the process of assigning threads to CPUs in a way that balances the processing load across CPUs in a real-time operating system (RTOS).

LabVIEW maintains two pools of CPUs available for automatic load balancing: a Timed Structures pool and a System pool. CPUs in the Timed Structures pool are available for automatic load balancing of Timed Loops configured for automatic processor assignment. CPUs in the System pool are for all other processes, including low-level operating system tasks.

At startup, LabVIEW assigns all available CPUs to both the Timed Structures pool and the System pool. As a result, the RTOS performs automatic load balancing across all CPUs. However, you can use the RT Set CPU Pools node to specify arbitrary System and Timed Structures pools.

An RTOS performs automatic load balancing on all threads, with the exception of manually-assigned Timed Loop threads. An RTOS maps code execution from each Timed Loop to its own dedicated thread, but performs automatic load balancing on only Timed Loop threads configured for automatic CPU assignment.

Parent topic:

Programming with a Real-Time Target

Related information:

- RT Set CPU Pools

<!--NI_TOPIC bundle=labview-nxg-rt-module-programming-with-rt-target path=benchmarking-rt-applications.html language=enus -->
## TOPIC 00002: Benchmarking in Real-Time Applications

- bundle_id: `labview-nxg-rt-module-programming-with-rt-target`
- source_path: `benchmarking-rt-applications.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-programming-with-rt-target/raw/resource/enus/benchmarking-rt-applications.html
- document_id: `labview-nxg-rt-module-programming-with-rt-target`
- page_type: `leaf`
- content_type: `concept`
- source_description: Benchmarking is the act of measuring how long specific sections of code take to execute, often over extended periods of time, in order to evaluate the performance and determinism of the measured code. Benchmarking your code helps to ensure that your real-time application meets your timing requiremen

Benchmarking in Real-Time Applications

Benchmarking is the act of measuring how long specific sections of code take to execute, often over extended periods of time, in order to evaluate the performance and determinism of the measured code. 
 Benchmarking your code helps to ensure that your real-time application meets your timing requirements consistently over an extended execution period.

Benchmarking typically involves carefully controlling the sequence in which the code executes and using timing nodes before, during, and after code execution to gather execution time metrics. You can process those metrics to determine average execution rates, standard deviation, maximum jitter, and many other calculations.

You can use the 
 *Benchmarking Template for Real-Time Code* example as a starting point for benchmarking code that you intend to run in a Timed Loop. This benchmarking template provides accurate average-case and worst-case jitter execution time over thousands of iterations.

You can also use the RT Execution Trace Tool nodes to log 
 *trace sessions*, or sets of timing and event data from VIs and operating system threads. You can view and analyze trace session data using the Real-Time Trace Viewer application. You can find the Real-Time Trace Viewer by searching from the Start menu of the host computer.

Parent topic:

Programming with a Real-Time Target

Related tasks:

- Minimizing Jitter in a Deterministic Loop
- Minimizing CPU Usage on an RT Controller

<!--NI_TOPIC bundle=labview-nxg-rt-module-programming-with-rt-target path=creating-time-budget.html language=enus -->
## TOPIC 00003: Creating a Time Budget

- bundle_id: `labview-nxg-rt-module-programming-with-rt-target`
- source_path: `creating-time-budget.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-programming-with-rt-target/raw/resource/enus/creating-time-budget.html
- document_id: `labview-nxg-rt-module-programming-with-rt-target`
- page_type: `leaf`
- content_type: `task`
- source_description: Minimize CPU usage and jitter in your application by creating a time budget for each task in your application. To create a time budget, you must determine the amount of time required to execute each task and set the rates of the loops accordingly. Determine the required period of each task in your a

Creating a Time Budget

Minimize CPU usage and jitter in your application by creating a time budget for each task in your application. To create a time budget, you must determine the amount of time required to execute each task and set the rates of the loops accordingly.

1. Determine the required period of each task in your application.
2. Benchmark your application to determine the duration of each task in your application. Allow the benchmark to run for several thousand iterations and record the worst-case execution time as the duration.
3. Record the duration and period of each task in a time budget table, as shown in the following example. 
 Task
 Duration (µS)
 Period (µS)Control
 400
 1,000
 Monitor
 3,000
 10,000
 Log
 16,000
 30,000
4. Use the following formula to target CPU usage at well below 100%: CPU Usage⁢(%)=100×∑1n[loopn×(durationperiod)]. 
 By plugging the numbers from the table into this formula, you can see that the CPU usage in this example is 100×(4001,000+3,00010,000+16,00030,000)=123%.
5. To decrease CPU usage, you can increase the period of one or more loops while ensuring that each loop executes at the requested rate. 
 For example, by increasing the period of the monitoring loop to 25,000 µS and increasing the period of the logging loop to 80,000 µS, the theoretical CPU usage becomes 100×(4001,000+3,00025,000+16,00080,000)=72%
 .

Parent topic:

Minimizing Jitter in a Deterministic Loop

Related concepts:

- Benchmarking in Real-Time Applications

Related tasks:

- Minimizing CPU Usage on an RT Controller
- Minimizing Jitter in a Deterministic Loop

Related information:

- Designing a Real-Time Application
- Designing a Real-Time Application

<!--NI_TOPIC bundle=labview-nxg-rt-module-programming-with-rt-target path=data-transfer-real-time.html language=enus -->
## TOPIC 00004: Types of Data Transfer in Real-Time Applications

- bundle_id: `labview-nxg-rt-module-programming-with-rt-target`
- source_path: `data-transfer-real-time.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-programming-with-rt-target/raw/resource/enus/data-transfer-real-time.html
- document_id: `labview-nxg-rt-module-programming-with-rt-target`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use the following table to determine which types of data transfer to use in your real-time application. Use Case Type(s) of Data Transfer Additional Information Sending data between non-deterministic code on the same controller, when you only need the most recent set of data and do not need to avoid

Types of Data Transfer in Real-Time Applications

Use the following table to determine which types of data transfer to use in your real-time application.

| Use Case | Type(s) of Data Transfer | Additional Information |
| --- | --- | --- |
| Sending data between non-deterministic code on the same controller, when you only need the most recent set of data and do not need to avoid overwriting or losing data | Tag Data Value Reference Duplicated terminal | Tag Nodes Storing Data with Data Value References to Manage Memory Dataflow between Duplicates of the Same Terminal |
| Sending between non-deterministic sections of code on the same controller, when you need to avoid overwriting or losing data | Queue | Queue Nodes |
| Sending data to and receiving data from deterministic code, in a single real-time VI or across multiple real-time VIs | RT FIFO | Transferring Data to Deterministic Code |
| Sending and receiving short, non-critical messages over a network | UDP | Transferring Data Over a Network Using UDP |
| Sending and receiving data over a network | TCP Network Stream | Transferring Data Over a Network Using TCP Streaming Data Using Network Streams |
| Sending and receiving data between an FPGA and non-deterministic sections of code on the PC or real-time controller | DMA FIFO Read/Write FPGA Control | Direct Memory Access (DMA) FIFOs Read/Write FPGA Control |

Parent topic:

Programming with a Real-Time Target

<!--NI_TOPIC bundle=labview-nxg-rt-module-programming-with-rt-target path=debugging-rt-application.html language=enus -->
## TOPIC 00005: Debugging a Real-Time Application

- bundle_id: `labview-nxg-rt-module-programming-with-rt-target`
- source_path: `debugging-rt-application.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-programming-with-rt-target/raw/resource/enus/debugging-rt-application.html
- document_id: `labview-nxg-rt-module-programming-with-rt-target`
- page_type: `leaf`
- content_type: `task`
- source_description: If your real-time application does not run properly after you deploy it to the real-time controller, you can debug the application. Navigate to the Design diagram of SystemDesigner. Right-click the application you added to the real-time controller and select Debug. If you select Debug without buildi

Debugging a Real-Time Application

If your real-time application does not run properly after you deploy it to the real-time controller, you can debug the application.

1. Navigate to the Design diagram of SystemDesigner.
2. Right-click the application you added to the real-time controller and select 
 Debug. 
 org.dita.html5/xsl/topic.xsl 455Note If you select 
 Debug without building the application, LabVIEW automatically builds the application before deploying and running the application in debugging mode.
3. When prompted, click 
 Deploy and Restart. 
 org.dita.html5/xsl/topic.xsl 455Note If another application is already running on the real-time controller, SystemDesigner prompts you to replace the running application with the new one. Because only one application can run on a real-time controller at a time, you must replace the running application to run the new one. 
 SystemDesigner deploys the application to the real-time controller. The controller restarts and executes the deployed application. The top-level VI and the application start running in debugging mode. LabVIEW locks the entire hierarchy of VIs in the Application document to avoid VI changes during the debugging process.
4. In the diagram of the top-level VI, debug the application using the same techniques for debugging a VI.
5. After you finish debugging, click 
 Stop debugging. LabVIEW stops running the application and unlocks the entire hierarchy of VIs in the Application document.

Parent topic:

Programming with a Real-Time Target

<!--NI_TOPIC bundle=labview-nxg-rt-module-programming-with-rt-target path=deploy-rt-executable.html language=enus -->
## TOPIC 00006: Manually Deploying a Real-Time Application

- bundle_id: `labview-nxg-rt-module-programming-with-rt-target`
- source_path: `deploy-rt-executable.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-programming-with-rt-target/raw/resource/enus/deploy-rt-executable.html
- document_id: `labview-nxg-rt-module-programming-with-rt-target`
- page_type: `leaf`
- content_type: `task`
- source_description: If the LabVIEW NXG Development Environment is not installed on the host PC, you can manually install and deploy a real-time application to the target. You must have SSH and SFTP software installed on the host PC. Windows 10 users can run ssh and sftp commands on the command line to perform the requi

Manually Deploying a Real-Time
 Application

If the LabVIEW NXG Development Environment is not installed on the host PC, you can
 manually install and deploy a real-time application to the target.

Note

ssh

sftp

1. Locate the IPK file in your project directory. 
 You can find this file in
 <project directory>\Packages\<rt target
 name>\<packageName> after you build or run a real-time application in
 LabVIEW NXG.
2. Copy the IPK file to the real-time target using SFTP.
3. Open the command line and enter opkg remove {packageName} to
 remove any previously installed versions of the file.
4. Enter the command opkg install {file} to install the IPK file onto the
 target. 
 The IPK file contains everything you need to run the real-time application, including the necessary Bash scripts.
5. Configure the application to run at startup by running the following script: 
 update-rc.d {packageName} start 97 4 5 . stop 3 0 1 2 3 6
  1. Replace
 {packageName} with the name of the package file,
 omitting the extension.
6. Restart the target to launch the real-time application.

Parent topic:

Programming with a Real-Time Target

<!--NI_TOPIC bundle=labview-nxg-rt-module-programming-with-rt-target path=deploying-running-code-on-rt-controller.html language=enus -->
## TOPIC 00007: Deploying and Running an Application on a Real-Time Controller

- bundle_id: `labview-nxg-rt-module-programming-with-rt-target`
- source_path: `deploying-running-code-on-rt-controller.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-programming-with-rt-target/raw/resource/enus/deploying-running-code-on-rt-controller.html
- document_id: `labview-nxg-rt-module-programming-with-rt-target`
- page_type: `leaf`
- content_type: `task`
- source_description: After testing your real-time application design using interactive execution, run the application on a real-time controller by building the application as a startup application and deploying it from SystemDesigner. Before you build and deploy your real-time application, test the design using interact

Deploying and Running an Application on a Real-Time Controller

After testing your real-time application design using interactive execution, run the application on a real-time controller by building the application as a startup application and deploying it from SystemDesigner.

Before you build and deploy your real-time application, test the design using interactive execution to ensure that it runs as you expect. Refer to [Testing a Real-Time VI Using Interactive Execution](/csh?topicname=testing-rt-vi-interactive-execution.html) for help testing your design using interactive execution.

To complete this task, you need to establish a network connection to a real-time controller and place the controller on the Design diagram of SystemDesigner.

1. Navigate to the Design diagram of SystemDesigner.
2. Select the application targeted to the real-time controller and, on the 
 Item tab, enable 
 Set as startup. 
 Setting an application as startup configures it to execute automatically whenever the real-time controller boots.
3. Right-click the application you added to the controller and select 
 Run. 
 org.dita.html5/xsl/topic.xsl 455Note If another application is already running on the real-time controller, SystemDesigner prompts you to replace the already running application with the new one. Because only one application can run on a real-time controller at a time, you must replace the running application in order to run the new one.
4. When prompted, click 
 Deploy and Restart. 
 SystemDesigner builds the application and deploys it to the physical real-time controller. The controller restarts and executes the built application.

- You run a VI interactively while the application is running and choose to abort the running application. If you choose to abort, you must repeat the steps listed above to continue running the application.
- You deploy a new startup application to the real-time controller and choose to replace the running application with the new one.
- You disable 
 Set as startup in SystemDesigner for the application running on the real-time controller and re-deploy it. This tactic is the only way to stop the application from running without running a new application or VI on the target.

Parent topic:

Programming with a Real-Time Target

<!--NI_TOPIC bundle=labview-nxg-rt-module-programming-with-rt-target path=determining-where-to-implement-task-rt.html language=enus -->
## TOPIC 00008: Determining Where to Run a Task in a Real-Time System

- bundle_id: `labview-nxg-rt-module-programming-with-rt-target`
- source_path: `determining-where-to-implement-task-rt.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-programming-with-rt-target/raw/resource/enus/determining-where-to-implement-task-rt.html
- document_id: `labview-nxg-rt-module-programming-with-rt-target`
- page_type: `leaf`
- content_type: `task`
- source_description: A task is a sequence of operations, typically contained within a loop, that collectively accomplish a high-level goal, such as data logging or controlling a hardware device. In a real-time system, you can choose to run a task on one of a few different targets. However, where you run the task depends

Determining Where to Run a Task in a Real-Time System

A 
 *task* is a sequence of operations, typically contained within a loop, that collectively accomplish a high-level goal, such as data logging or controlling a hardware device. 
 In a real-time system, you can choose to run a task on one of a few different targets. However, where you run the task depends on the timing, performance, and reliability requirements for your application.

Using the following table, select a target in the real-time system for each task in your application. In SystemDesigner, place the VI that contains the task on the target you identify.

Note

| Target | Considerations | Example Tasks |
| --- | --- | --- |
| FPGA | Advantages Maximum performance—Because an FPGA is a hardware solution, algorithms that run on an FPGA are capable of highly deterministic continuous execution, at rates down to the tens of nanoseconds, and true parallel processing that is not possible in a software implementation. Maximum reliability—Because FPGAs have no operating system, they are not susceptible to crashes or priority conflicts. Offload processing—You can run computationally intensive processes on an FPGA to free up the real-time controller for other tasks. If CPU usage is high on your real-time controller and you have resources to spare on your FPGA, you can move computational tasks to the FPGA. Disadvantages Limited resources—Because an FPGA is a hardware solution, FPGA applications are limited to the number of memory items available on the FPGA chip. Potentially complex programming—Because FPGA resources are limited, you often have to optimize the code to fit on the FPGA and meet your requirements. Optimizing FPGA code can require programming practices, such as handshaking and pipelining, that are typically unnecessary for applications that run on a processor. Limited data types and available operations—FPGAs support a limited number of data types, such as numeric, Boolean, and reference data types. FPGA applications do not support many operations that processor-based applications do, such as file I/O and networking capabilities. | High-performance control loops 200 kHz analog Proportional-Integral-Derivative (PID) control loop High-speed signal acquisition and generation Vibration Tachometers Custom digital protocols Signal processing and analysis Spectral analysis Filtering Third-party IP integration Viterbi and Turbo decoders Safe state logic Set all hardware to safe states in case of emergency Communicate with real-time processor |
| Real-time controller | Advantages Deterministic timing—A real-time application can consistently respond to events and perform tasks within a short, bounded amount of time, down to the tens of microseconds, while ensuring that high priority tasks execute first. High reliability—You can maintain determinism in an application that runs continuously for months. Ease of programming—You can reuse code directly from the PC on a real-time controller and even debug code as it runs on the real-time controller. Disadvantages Limited performance—As a software solution, real-time controllers are incapable of true parallel processing and cannot achieve the execution speeds of an FPGA. Limited resources—High-performance real-time applications can quickly occupy full CPU usage. High CPU usage can lead to jitter. | Log data to file Signal processing and analysis Spectral analysis Filtering Communicate with FPGA Communicate with PC over a network Monitor system health |
| PC | Advantages User interface—You can visualize data sent from the real-time system and send commands to the real-time system. Offload processing—You can use the PC to run processing tasks that do not need to happen deterministically or as part of the real-time system to make more CPU and FPGA resources available. Disadvantages Non-deterministic—PC operating systems are not designed to execute tasks deterministically. Limited reliability—General purpose operating systems are typically more susceptible to crashes than real-time operating systems or FPGAs. | Remotely connect to real-time system over a network Display relevant data on the user interface Update settings and send commands to the real-time system Retrieve data log files from the real-time system Perform offline data analysis and processing |

#### Examples

The following image illustrates tasks you might run on each target in a control and monitoring system.

[IMAGE alt='1378' src='GUID-BA2C70B8-6143-4352-8068-77B48B7063D5-a5.png']

Parent topic:

Programming with a Real-Time Target

Related concepts:

- Parts of a Real-Time Development Setup
- Introduction to Real-Time Operating Systems
- Determinism and Jitter in a Real-Time System

Related tasks:

- Separating Tasks to Optimize a Real-Time Application

Related information:

- Designing a Real-Time Application

<!--NI_TOPIC bundle=labview-nxg-rt-module-programming-with-rt-target path=determinism-real-time.html language=enus -->
## TOPIC 00009: Determinism and Jitter in a Real-Time System

- bundle_id: `labview-nxg-rt-module-programming-with-rt-target`
- source_path: `determinism-real-time.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-programming-with-rt-target/raw/resource/enus/determinism-real-time.html
- document_id: `labview-nxg-rt-module-programming-with-rt-target`
- page_type: `leaf`
- content_type: `concept`
- source_description: When programmed appropriately, a real-time system can guarantee that tasks consistently execute in a specified time constraint. Determinism is the characteristic that describes how consistently a system executes tasks within a time constraint. A perfectly deterministic system would experience no var

Determinism and Jitter in a Real-Time System

When programmed appropriately, a real-time system can guarantee that tasks consistently execute in a specified time constraint. 
 *Determinism* is the characteristic that describes how consistently a system executes tasks within a time constraint.

A perfectly deterministic system would experience no variation in timing for tasks. However, in the real world, even highly deterministic systems experience slight variations in timing for tasks. The variation between the expected timing and the actual timing for a task is known as 
 *jitter*. Jitter occurs both when actual timing is later than expected timing and when actual timing is earlier than expected timing for a task. The following illustration shows the jitter for multiple executions of one task.

[IMAGE alt='1378' src='GUID-16E5F55B-D40E-49BB-BCCB-5C45994A291C-a5.png']

1. When actual timing is later than expected, the task can fail to finish executing within the timing requirements of an application.
2. When actual timing is earlier than expected, the task can get out of sync with other tasks in the application.

The amount of jitter that a task can tolerate while still meeting the timing requirements of the task defines the acceptable jitter for the task. In the following illustration, mean execution time for each normal distribution graph corresponds to the expected timing for the task. The range of actual execution times shown along the x-axis is the jitter for the task. When the jitter for the task falls within the range of acceptable execution times, the task is sufficiently deterministic.

[IMAGE alt='1378' src='ISHPUBLILLUSTRATIONMISSING-a5.jpg']

Parent topic:

Programming with a Real-Time Target

Related concepts:

- Introduction to Real-Time Operating Systems

Related tasks:

- Organizing Deterministic and Non-Deterministic Tasks in a Real-Time VI
- Separating Tasks to Optimize a Real-Time Application
- Minimizing Jitter in a Deterministic Loop

<!--NI_TOPIC bundle=labview-nxg-rt-module-programming-with-rt-target path=deterministic-non-deterministic-rt-tasks.html language=enus -->
## TOPIC 00010: Organizing Deterministic and Non-Deterministic Tasks in a Real-Time VI

- bundle_id: `labview-nxg-rt-module-programming-with-rt-target`
- source_path: `deterministic-non-deterministic-rt-tasks.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-programming-with-rt-target/raw/resource/enus/deterministic-non-deterministic-rt-tasks.html
- document_id: `labview-nxg-rt-module-programming-with-rt-target`
- page_type: `leaf`
- content_type: `task`
- source_description: In a real-time VI, a task that must finish on time for the VI to accomplish its purpose is a deterministic task. By proactively separating a deterministic task like reading a signal from a non-deterministic task like transferring data to a user interface, you mitigate jitter in the deterministic tas

Organizing Deterministic and Non-Deterministic Tasks in a Real-Time VI

deterministic task

Timed Loop

#### What to Use

- Timed
 Loop
- While
 Loop
- RT FIFO Create , Write , Read , and Delete nodes from the Real-Time Nodes category
- Stop
 Timed Structure

#### What to Do

Create the following diagram to organize a deterministic and non-deterministic task in a real-time VI.

Customize the gray sections for your unique programming goals.

[IMAGE alt='1378' src='GUID-0BF2CA86-64AA-4D53-A639-5D172842C533-a5.png']

|  | Place a deterministic task in a Timed Loop. A Timed Loop executes each iteration at the period and priority you specify. The highest priority Timed Loop executes before lower priority items in a VI or application. |
| --- | --- |
|  | Place a non-deterministic task in a While Loop. In this example, the While Loop includes an indicator that transfers data to the user interface on the panel. Panel controls and indicators do not transfer data deterministically, so using an indicator in a Timed Loop could introduce enough jitter to prevent deterministic execution for the task. |
|  | Use RT FIFO Write to transfer data from a deterministic task to a non-deterministic task. |
|  | Use RT FIFO Read to access data produced by a deterministic task. When using RT FIFO Read in a non-deterministic task, set the timeout in ms to -1 to ensure that the node never returns null values. |
|  | Stop Timed Structure aborts the execution of the Timed Loop when the While Loop stops. In this example, the While Loop stops when it receives a True Boolean value from a control on the panel. Controls do not transfer data deterministically, so you should never stop a Timed Loop directly from a control on the panel. Stop Timed Structure allows both loops to stop based on the stop condition of the While Loop without placing a control directly in the Timed Loop. This avoids introducing jitter into the Timed Loop. |

#### Troubleshooting

Make sure to configure a Timed Loop with a period large enough to perform the deterministic task and still have idle time during the iteration to allow lower priority loops and structures to execute. Because Timed Loops preempt other tasks, a Timed Loop can monopolize all of the processor resources and prevent lower priority tasks from executing.

#### Examples

Search within the programming environment to access the following installed examples:

- Using the Timed Loop with RT FIFOs

Parent topic:

Programming with a Real-Time Target

Related concepts:

- Determinism and Jitter in a Real-Time System

Related tasks:

- Separating Tasks to Optimize a Real-Time Application
- Transferring Data to Deterministic Code

<!--NI_TOPIC bundle=labview-nxg-rt-module-programming-with-rt-target path=incorporating-recovery-procedures-in-rt-vis.html language=enus -->
## TOPIC 00011: Incorporating Recovery Procedures in a Real-Time VI

- bundle_id: `labview-nxg-rt-module-programming-with-rt-target`
- source_path: `incorporating-recovery-procedures-in-rt-vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-programming-with-rt-target/raw/resource/enus/incorporating-recovery-procedures-in-rt-vis.html
- document_id: `labview-nxg-rt-module-programming-with-rt-target`
- page_type: `leaf`
- content_type: `task`
- source_description: Some real-time controllers contain a built-in hardware timer known as a watchdog timer or a dead man's switch that interfaces with the embedded software application. If your real-time controller contains a watchdog timer, you can incorporate recovery procedures in your real-time VI to detect softwar

Incorporating Recovery Procedures in a Real-Time VI

watchdog timer

#### What to Use

[Real-Time Watchdog Timer Nodes](/csh?topicname=real-time-watchdog-timer-nodes.html)

#### What to Do

Create the following diagram to incorporate recovery procedures in your real-time VI.

Customize the gray sections for your unique programming goals.

[IMAGE alt='1378' src='GUID-6851855F-56E3-4358-97CB-2A3F5D66D97C-a5.png']

|  | Configure a watchdog timer object using the Watchdog Timer Configure node. The watchdog timer starts counting down as soon as the Watchdog Timer Configure node executes. You can define the recovery procedure in the expiration actions input of the node. In this example, the node restarts the current application on the controller when the watchdog timer expires. You also can configure the node to perform other actions in case of expiration, such as restarting the real-time controller. |
| --- | --- |
|  | Use the Watchdog Timer Restart node to periodically reset the watchdog timer to prevent the timer from expiring and triggering the recovery procedure. If a software failure prevents the application from resetting the watchdog timer, the timer eventually expires and triggers the recovery procedure. |
|  | Use the Watchdog Timer Clear node to reset and close the watchdog timer object. You must close the current object before using another one. |

Parent topic:

Programming with a Real-Time Target

<!--NI_TOPIC bundle=labview-nxg-rt-module-programming-with-rt-target path=intro-rtos.html language=enus -->
## TOPIC 00012: Introduction to Real-Time Operating Systems

- bundle_id: `labview-nxg-rt-module-programming-with-rt-target`
- source_path: `intro-rtos.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-programming-with-rt-target/raw/resource/enus/intro-rtos.html
- document_id: `labview-nxg-rt-module-programming-with-rt-target`
- page_type: `leaf`
- content_type: `concept`
- source_description: A real-time operating system (RTOS) enables a real-time system to run applications that require precise timing or high reliability. Rather than distributing processor resources evenly between running tasks, an RTOS can guarantee precise timing and high reliability because it manages the execution of

Introduction to Real-Time Operating Systems

A real-time operating system (RTOS) enables a real-time system to run applications that require precise timing or high reliability. Rather than distributing processor resources evenly between running tasks, an RTOS can guarantee precise timing and high reliability because it manages the execution of tasks based on the priority assigned to each task.

An RTOS provides an alternative to the scheduling strategy used to run tasks in general purpose operating systems. A general purpose OS, like Windows for a PC, automatically distributes available processor time between all running tasks and resolves conflicts to optimize multitasking. Because the time one task needs to execute depends on how the competing tasks are scheduled, a general purpose OS cannot guarantee that any one task executes within precise timing constraints.

Like a general purpose OS, an RTOS also supports multitasking for tasks with the same relative priority. However, in an RTOS, when a task has a high relative priority, the task preempts lower priority tasks and runs without interruption. Because an RTOS protects the high-priority task from interruption, it can guarantee that the high-priority task executes within precise time constraints.

Parent topic:

Programming with a Real-Time Target

Related concepts:

- Parts of a Real-Time Development Setup
- Determinism and Jitter in a Real-Time System

<!--NI_TOPIC bundle=labview-nxg-rt-module-programming-with-rt-target path=minimizing-cpu-usage.html language=enus -->
## TOPIC 00013: Minimizing CPU Usage on an RT Controller

- bundle_id: `labview-nxg-rt-module-programming-with-rt-target`
- source_path: `minimizing-cpu-usage.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-programming-with-rt-target/raw/resource/enus/minimizing-cpu-usage.html
- document_id: `labview-nxg-rt-module-programming-with-rt-target`
- page_type: `leaf`
- content_type: `task`
- source_description: By targeting CPU usage well below 100%, you can minimize jitter and ensure that the tasks in your application do not need to compete for CPU time. Refer to the following guidelines for minimizing CPU usage in your real-time application. Create a time budget to determine the amount of time required t

Minimizing CPU Usage on an RT Controller

By targeting CPU usage well below 100%, you can minimize jitter and ensure that the tasks in your application do not need to compete for CPU time. Refer to the following guidelines for minimizing CPU usage in your real-time application.

1. Create a time budget to determine the amount of time required to execute each task in the application.
2. Use the Real-Time Trace Viewer to identify which VIs and threads in your application use the most CPU time. You can then adjust them based on the following guidelines:
  1. Run loops only as fast as necessary. 
 Running each loop in your application as fast as possible can lead to undesired timing behavior, including increased jitter and even system deadlocks. For example, running the data publishing loop of a user interface faster than the human operator can process and respond to the data can unnecessarily tax the CPU of the real-time target. In most cases, a rate of 2 Hz to 15 Hz is adequate for a loop that publishes user interface data over the network.
  2. Avoid excessive parallelism. 
 Executing code in parallel can increase performance on multi-core systems, but greater parallelism also leads to greater overhead, which can impact performance. To determine whether a VI can benefit from parallelism, you might need to benchmark both the serial form and the parallel form of the VI.
  3. Consider offloading certain tasks to either a desktop PC or an FPGA. 
 Use the following guidelines to determine the most appropriate device for performing specific types of tasks. 
 TaskAppropriate DevicesData acquisitionRT or FPGAControl loopRT or FPGAData analysis for logging or monitoring purposes (offline analysis)RT or Desktop PCData loggingRT or Desktop PC

Parent topic:

Minimizing Jitter in a Deterministic Loop

Related tasks:

- Determining Where to Run a Task in a Real-Time System
- Creating a Time Budget
- Minimizing Jitter in a Deterministic Loop

<!--NI_TOPIC bundle=labview-nxg-rt-module-programming-with-rt-target path=minimizing-jitter.html language=enus -->
## TOPIC 00014: Minimizing Jitter in a Deterministic Loop

- bundle_id: `labview-nxg-rt-module-programming-with-rt-target`
- source_path: `minimizing-jitter.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-programming-with-rt-target/raw/resource/enus/minimizing-jitter.html
- document_id: `labview-nxg-rt-module-programming-with-rt-target`
- page_type: `leaf`
- content_type: `task`
- source_description: The variation between the expected timing and the actual timing for a task is known as jitter. Minimize jitter in deterministic loops to ensure precise timing in your real-time application. Refer to the following guidelines for interacting with deterministic loops: Memory allocation Pre-allocate arr

Minimizing Jitter in a Deterministic Loop

The variation between the expected timing and the actual timing for a task is known as 
 *jitter*.
 Minimize jitter in deterministic loops to ensure precise timing in your real-time application.

- Refer to the following guidelines for interacting with deterministic loops: 
 **Memory allocation**— Pre-allocate arrays before using them in deterministic loops. Use the Replace Array Subset node to modify pre-allocated arrays within a deterministic loop. Use the Real-Time Trace Viewer to identify Wait for Memory system event flags, which indicate memory management operations.
 **Opening and closing references**—Open references in an initialization phase before entering a deterministic loop. Close references in a shutdown phase after the deterministic loop terminates. Opening and closing references inside a loop can add jitter in a deterministic loop.
 **Communication**—Use the RT FIFO nodes to communicate with a deterministic loop. RT FIFOs buffer data so that a deterministic loop can access the data without being blocked by a lower-priority loop.
 **SubVIs**—For best performance, use inlined subVIs in deterministic loops. Inlined subVIs decrease CPU overhead because they do not need to be called at run time. If you do not use inlined subVIs, close all subVI documents before running a VI that contains a deterministic loop.
- Avoid placing the following items in deterministic loops: 
 **File I/O**—Accessing the hard disk using file I/O operations can introduce unbounded jitter in a deterministic loop.
 **Networking operations**— Networking operations can introduce unbounded jitter in a deterministic loop.
 **Variable-size data structures**—Using variable-size data structures in deterministic loops leads to variation in loop execution times. Instead, pre-allocate memory before using a data structure in a deterministic loop.
 **Shared resources**—Accessing resources that are shared between a deterministic loop and another loop, such as hardware resources, I/O channels, or non-reentrant subVIs, may cause the deterministic loop to wait for the other loop to release the shared resource.
 **Shared data**—Sharing data with a deterministic loop through objects such as queues, data value references, and duplicated terminals can introduce jitter in a deterministic loop . Instead, use RT FIFO nodes to communicate with a deterministic loop.
 **Algorithms with unbounded jitter**—Certain algorithms are non-deterministic by nature and can introduce unbounded jitter. Do not include algorithms with unbounded jitter in a deterministic loop. If you are not sure about the jitter characteristics of a program, benchmark it.
 **Controls and indicators**—Placing data terminals within a deterministic loop can negatively impact performance, which introduces jitter.

Parent topic:

Programming with a Real-Time Target

Related concepts:

- Benchmarking in Real-Time Applications

Related tasks:

- Creating a Time Budget
- Minimizing CPU Usage on an RT Controller

<!--NI_TOPIC bundle=labview-nxg-rt-module-programming-with-rt-target path=parts-real-time-system.html language=enus -->
## TOPIC 00015: Parts of a Real-Time Development Setup

- bundle_id: `labview-nxg-rt-module-programming-with-rt-target`
- source_path: `parts-real-time-system.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-programming-with-rt-target/raw/resource/enus/parts-real-time-system.html
- document_id: `labview-nxg-rt-module-programming-with-rt-target`
- page_type: `leaf`
- content_type: `concept`
- source_description: A real-time system includes hardware and software components that enable precise control over the execution of your code. You use a PC to develop code for a real-time system. The following figure shows a basic setup for developing a real-time application. Development PC—The PC manages connections be

Parts of a Real-Time Development Setup

A real-time system includes hardware and software components that enable precise control over the execution of your code. You use a PC to develop code for a real-time system.

The following figure shows a basic setup for developing a real-time application.

[IMAGE alt='1378' src='GUID-F4DD2D6A-68CD-4646-9264-1FB1280C7017-a5.png']

1. Development PC—The PC manages connections between devices in the system and provides a graphical environment to create and edit real-time code. When code runs on a real-time controller, you can use the PC as the user interface to modify VI panels and view data from the controller.
2. Real-time controller—A real-time controller runs a Linux real-time operating system and software that allows you to set precise timing directives and deterministic execution for real-time code. The real-time controller can also provide precise timing when communicating with FPGAs and I/O hardware. For example, if you need a set of FPGAs to each perform a unique data processing task in a particular order, you can use a real-time controller to communicate directly with the FPGAs to guarantee that each FPGA in the sequence receives instructions at a precise time.
3. Real-time system—A real-time system includes the chassis, real-time controller, and other modules in the chassis. You establish a connection between the real-time system and the development PC to access the real-time controller and other modules in the chassis.
4. Network connection—A PC and a real-time system must connect to the same network so the PC and real-time controller can communicate with each other. Over this network connection, the PC deploys code to the real-time controller and acts as a live graphical user interface for the real-time controller.

Parent topic:

Programming with a Real-Time Target

Related concepts:

- Introduction to Real-Time Operating Systems
- Determinism and Jitter in a Real-Time System

Related tasks:

- Connecting to a Real-Time Controller

<!--NI_TOPIC bundle=labview-nxg-rt-module-programming-with-rt-target path=priority-inheritance-of-threads.html language=enus -->
## TOPIC 00016: Priority Inheritance of Threads

- bundle_id: `labview-nxg-rt-module-programming-with-rt-target`
- source_path: `priority-inheritance-of-threads.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-programming-with-rt-target/raw/resource/enus/priority-inheritance-of-threads.html
- document_id: `labview-nxg-rt-module-programming-with-rt-target`
- page_type: `leaf`
- content_type: `concept`
- source_description: When a lower-priority thread holds a shared resource needed by a higher-priority thread, the real-time controller implements priority inheritance by temporarily increasing the priority of the thread holding the shared resource so that the resource can return promptly to the higher-priority thread. P

Priority Inheritance of Threads

When a lower-priority thread holds a shared resource needed by a higher-priority thread, the real-time controller implements 
 *priority inheritance* by temporarily increasing the priority of the thread holding the shared resource so that the resource can return promptly to the higher-priority thread.

Priority inheritance helps prevent 
 *priority inversion*, which is when threads of lower priority indirectly preempt threads of higher priority.

Parent topic:

Programming with a Real-Time Target

Related concepts:

- Determinism and Jitter in a Real-Time System
- Scheduling Behavior in Real-Time Operating Systems

Related tasks:

- Minimizing Jitter in a Deterministic Loop

<!--NI_TOPIC bundle=labview-nxg-rt-module-programming-with-rt-target path=registering-real-time-system.html language=enus -->
## TOPIC 00017: Connecting to a Real-Time Controller

- bundle_id: `labview-nxg-rt-module-programming-with-rt-target`
- source_path: `registering-real-time-system.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-programming-with-rt-target/raw/resource/enus/registering-real-time-system.html
- document_id: `labview-nxg-rt-module-programming-with-rt-target`
- page_type: `leaf`
- content_type: `task`
- source_description: You must establish a network connection from the host PC to a real-time controller in the Live view of SystemDesigner before you can run code on the controller. LabVIEW NXG cannot connect to a real-time controller through a VPN connection.Some devices appear on the Live view automatically. If your d

Connecting to a Real-Time Controller

You must establish a network connection from the host PC to a real-time
 controller in the Live view of SystemDesigner before you can run code on the controller.

Note

Some devices appear on the Live view automatically. If your device does not
 appear on the Live view, complete the following steps to add a device.

1. Open SystemDesigner and switch to the Live view.
2. On the document toolbar, click 
 Add hardware to open the 
 Add Hardware dialog box.
3. Locate your device in one of the following tabs. 
 Discovered hardware—shows the devices that SystemDesigner detects on the same local subnet as the host PC. Click 
 Add to display the device on the Live view.
 Add hardware by address—enter the IP address or hostname of the device to which you want to connect and click 
 Connect.You can find the IP address of a real-time controller using either of the following methods: 
 Connect a monitor to the real-time controller and watch the system boot. The IP address appears in the console display at the end of the system boot.Connect a monitor and keyboard to the real-time controller, enter your log in credentials into the console display, and then enter 
 ifconfig. The IP address displays with other network configuration information.org.dita.html5/xsl/topic.xsl 455Note Most controllers have multiple IP addresses. Make sure to identify the network port the controller uses to connect to the host.
4. If the device requires login credentials, enter them when you are prompted. 
 By default, the real-time system has the username admin and a blank
 password.
5. If the real-time target does not have a base system image installed, install an
 image by clicking Set up in the
 Actions column of the Add
 Hardware dialog for the target. Follow the steps in the dialog
 to install a base system image on the target.

After you establish a connection to the real-time controller, it is available in the Live Hardware palette category in the Design view.

Parent topic:

Programming with a Real-Time Target

<!--NI_TOPIC bundle=labview-nxg-rt-module-programming-with-rt-target path=rt-programming.html language=enus -->
## TOPIC 00018: Programming with a Real-Time Target

- bundle_id: `labview-nxg-rt-module-programming-with-rt-target`
- source_path: `rt-programming.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-programming-with-rt-target/raw/resource/enus/rt-programming.html
- document_id: `labview-nxg-rt-module-programming-with-rt-target`
- page_type: `leaf`
- content_type: `concept`
- source_description: Use this section to learn about real-time targets and creating, testing, running, and debugging real-time code.

Programming with a Real-Time Target

Use this section to learn about real-time targets and creating, testing, running, and
 debugging real-time code.

<!--NI_TOPIC bundle=labview-nxg-rt-module-programming-with-rt-target path=rtos-scheduling.html language=enus -->
## TOPIC 00019: Scheduling Behavior in Real-Time Operating Systems

- bundle_id: `labview-nxg-rt-module-programming-with-rt-target`
- source_path: `rtos-scheduling.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-programming-with-rt-target/raw/resource/enus/rtos-scheduling.html
- document_id: `labview-nxg-rt-module-programming-with-rt-target`
- page_type: `leaf`
- content_type: `concept`
- source_description: The way a real-time operating system (RTOS) schedules tasks guarantees that high-priority tasks execute within precise time constraints. Understanding how scheduling works in an RTOS can help you set the right priorities for deterministic tasks in your application. The following list contains some k

Scheduling Behavior in Real-Time Operating Systems

The way a real-time operating system (RTOS) schedules tasks guarantees that high-priority tasks execute within precise time constraints. Understanding how scheduling works in an RTOS can help you set the right priorities for deterministic tasks in your application.

The following list contains some key concepts that underlie the RTOS scheduling process:

Thread

Note

Timed Loop

Timed Loop

RTOS scheduler

Run queue

Timed Loop priority

Timed Loop

priority in

Execution System

Note

Timed Loop

Timed Loop

Priority-based scheduling

Parent topic:

Programming with a Real-Time Target

#### Thread States

At any given time, every thread in a real-time system is either 
 *running* or 
 *blocked*.

Running

- The thread finishes executing.
- The thread is preempted by a higher-priority thread.
- The thread becomes blocked by the built-in timing mechanism of a Timed Loop or by a blocking node, such as the Wait node within a While Loop .

Blocked

When a thread becomes unblocked, it enters the run queue in order of priority.

#### Priority-Based Scheduling of Timed Loops

The RTOS scheduler handles new Timed Loop threads that enter the run queue in different ways depending on their priorities.

Use the following table to decide how to set relative priorities for Timed Loops in a real-time application so that the application meets timing requirements.

| Priority of new Timed Loop thread | RTOS scheduler behavior |
| --- | --- |
| Higher priority than running thread | The scheduler preempts the running thread so that the new thread can execute immediately. The preempted thread then moves behind the new thread in the run queue. |
| Equal priority as running thread | The scheduler places the new thread behind all other threads of the same priority in the run queue. Threads of equal priority are scheduled according to a first-in, first-out policy. |
| Lower priority than running thread | The scheduler allows the new thread to run only after all higher-priority threads are blocked. |

Note

Although it seems intuitive to set the priority of each loop based on the importance of the loop, this strategy can cause jitter. Instead, set the priority of each loop based on how important it is for the task fulfill a certain timing guarantee.

Related concepts:

- Determinism and Jitter in a Real-Time System
- Priority Inheritance of Threads

<!--NI_TOPIC bundle=labview-nxg-rt-module-programming-with-rt-target path=separating-tasks-real-time.html language=enus -->
## TOPIC 00020: Separating Tasks to Optimize a Real-Time Application

- bundle_id: `labview-nxg-rt-module-programming-with-rt-target`
- source_path: `separating-tasks-real-time.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-programming-with-rt-target/raw/resource/enus/separating-tasks-real-time.html
- document_id: `labview-nxg-rt-module-programming-with-rt-target`
- page_type: `leaf`
- content_type: `task`
- source_description: Task separation involves running distinct tasks in parallel loops to create an application. Separating tasks provides the following benefits: Improved Determinism—To minimize jitter in a deterministic loop, ensure that the loop does not contain potentially non-deterministic code. Improved CPU Effici

Separating Tasks to Optimize a Real-Time Application

Task separation involves running distinct tasks in parallel loops to create an application.

Separating tasks provides the following benefits:

- Improved Determinism—To minimize jitter in a deterministic loop, ensure that the loop does not contain potentially non-deterministic code.
- Improved CPU Efficiency—CPU efficiency is a common design constraint in real-time applications. By running tasks in separate loops at distinct rates, you can maximize CPU efficiency by executing each task only as often as necessary.

Complete the following steps to separate the tasks you want to run on the real-time controller.

Note

1. Without writing any actual code, determine the high-level tasks your application must perform. 
 For example, your application might require the following tasks:
 Control—Control the temperature and level of liquid in a tank.
 Log—Log a historical record of the temperature and level data collected. The requirement for this task is to log every process variable value collected by the control task.
 Monitor—Transfer user interface data over the network to receive commands from the user and display continuous data graphs that the user can monitor.
2. Determine the minimum rate at which each task must execute. 
 If you are uncertain about the rates you need for each task, consider using estimates until you are able to deploy and benchmark the code to create a time budget. 
 Continuing the previous example, the tasks require the following minimum rates:
 Control—The minimum rate for this task is 1 kHz. This translates to a period of 1 ms.
 Log—There is no minimum rate requirement for this task. In this example, the period is 200 ms.
 Monitor—The minimum rate for this task is 10 Hz. This translates to a period of 100 ms.
3. Define the data transfer relationships among the tasks in your application. 
 The following image illustrates the data transfer relationships among the tasks from the previous example.
 
[IMAGE alt='1378' src='GUID-2C8B943B-3A34-4E51-9FB6-24C4C48AE4F3-a5.png']
4. Translate your design into code. 
 Organizing your code so that each task loop runs in a separate subVI helps to keep your application easily readable. 
 
 The following image illustrates the top-level real-time VI that includes the tasks defined in the previous example.
 
[IMAGE alt='1378' src='GUID-014C4882-4A0C-45D2-90B4-532B54446E63-a5.png']
  1. Create a separate subVI for each task you outlined in the previous steps and add the appropriate task loop to each subVI based on whether you want the task to be deterministic. 
 Continuing the previous example, use loops as described for the following tasks:
 Control—Because you need this task to execute exactly every 1 ms, use a Timed Loop.
 Log—Because this task is not time-critical, you can use a While Loop with a Wait node instead of a Timed Loop.
 Monitor—Because you don't need this task to execute exactly every 100 ms as long as it executes 10 times per second, you can use a While Loop with a Wait node instead of a Timed Loop.
  2. Create an initialization subVI to handle preliminary tasks that need to occur before your ongoing tasks, such as opening file references and preallocating arrays.
  3. Create a shutdown subVI to switch your application to a shutdown state before turning off your real-time system. 
 A shutdown routine might include the following actions: 
 Setting outputs to known valuesClosing file referencesNotifying the operator when they can turn off the real-time system

Parent topic:

Programming with a Real-Time Target

Related concepts:

- Determinism and Jitter in a Real-Time System

Related tasks:

- Creating a Time Budget
- Determining Where to Run a Task in a Real-Time System

Related information:

- Designing a Real-Time Application

<!--NI_TOPIC bundle=labview-nxg-rt-module-programming-with-rt-target path=testing-rt-vi-interactive-execution.html language=enus -->
## TOPIC 00021: Testing a Real-Time VI Using Interactive Execution

- bundle_id: `labview-nxg-rt-module-programming-with-rt-target`
- source_path: `testing-rt-vi-interactive-execution.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-programming-with-rt-target/raw/resource/enus/testing-rt-vi-interactive-execution.html
- document_id: `labview-nxg-rt-module-programming-with-rt-target`
- page_type: `leaf`
- content_type: `task`
- source_description: Running a VI targeted to a real-time controller in SystemDesigner deploys the code to the physical real-time controller and begins interactive execution of that code. You can interact with the running VI to test your design and make sure it executes as expected. To complete this task, you need to es

Testing a Real-Time VI Using Interactive Execution

Running a VI targeted to a real-time controller in SystemDesigner deploys the code to the physical real-time controller and begins interactive execution of that code. You can interact with the running VI to test your design and make sure it executes as expected.

To complete this task, you need to establish a network connection to a real-time controller and place the controller on the Design diagram of SystemDesigner.

1. Navigate to the Design diagram of SystemDesigner.
2. From the 
 Project Files tab, drag the application you want to run on the physical real-time controller to the 
 Software section of the controller on the diagram. If you don't have an existing application, create a new application and add a VI to it:
  1. On the controller in SystemDesigner, click 
 Add Software»Application to create a new Application document.
  2. Double-click the Application document, and add either an existing VI that you want to run on the real-time controller or a new VI using the 
 + menu.
  3. If you create a new VI, double-click the new VI and create whatever code you want to run on the real-time controller.
  4. Save the VI and the Application document.
3. On the Design diagram of System Designer, double-click the Application document you added to the controller on the diagram, and open the VI you want to run on the controller. 
 Opening the VI from the controller ensures you open a copy of the VI targeted to run on the controller. When you open a VI from the 
 Project Files tab, the target of that VI can vary depending on whether it is targeted to multiple devices in SystemDesigner. You can use the target selector, shown in the following image, to verify the target or to switch between instances of the VI on different targets.
 
[IMAGE alt='1378' src='GUID-FF731694-E6A6-4D35-BF59-25F12EF5A81F-a5.png']
4. Run the VI. 
 When you click the 
 Run button, the VI and its subVIs deploy to the memory of the real-time controller and begin executing. You can modify inputs and view output data to make sure your design executes and generates data as expected.
 org.dita.html5/xsl/topic.xsl 455Note Because the code deploys to the memory of the controller, it does not persist if the controller reboots. You have to re-run the VI if you reboot the controller.

When you have a final application design, you can build the application and deploy it to the real-time controller as a startup application.

Parent topic:

Programming with a Real-Time Target

Related tasks:

- Connecting to a Real-Time Controller

<!--NI_TOPIC bundle=labview-nxg-rt-module-programming-with-rt-target path=transfer-data-deterministic.html language=enus -->
## TOPIC 00022: Transferring Data to Deterministic Code

- bundle_id: `labview-nxg-rt-module-programming-with-rt-target`
- source_path: `transfer-data-deterministic.html`
- source_url: https://docs-be.ni.com/bundle/labview-nxg-rt-module-programming-with-rt-target/raw/resource/enus/transfer-data-deterministic.html
- document_id: `labview-nxg-rt-module-programming-with-rt-target`
- page_type: `leaf`
- content_type: `task`
- source_description: Data transfer to deterministic code requires the use of a communication method designed specifically for real-time (RT) applications. Other communication methods, such as queues, TCP, and UDP use variable size buffers and do not transfer data deterministically. Use the RT FIFO nodes to transfer data

Transferring Data to Deterministic Code

Data transfer to deterministic code requires the use of a communication method designed specifically for real-time (RT) applications. Other communication methods, such as queues, TCP, and UDP use variable size buffers and do not transfer data deterministically. Use the RT FIFO nodes to transfer data to and receive data from deterministic code.

#### What to Use

- Timed
 Loop
- While
 Loop
- RT FIFO nodes from the Real-Time Nodes palette category

#### What to Do

Create the following diagram to transfer data between two loops in a real-time VI using RT FIFOs.

Customize the gray sections for your unique programming goals.

[IMAGE alt='1378' src='GUID-6CECB426-ECC3-49CA-B752-080FA3929E70-a5.png']

|  | RT FIFOs ensure deterministic behavior by preallocating memory for the data and imposing a size restriction on the data you share. The RT FIFO Create node allocates a section of memory on the RT controller to create an RT FIFO. If you know your application requires a buffer size of more than the default size of 10 elements, configure the size as a number of elements that prevents data loss. Tip If you do not know how many elements the buffer needs to hold, you can adjust the size when you benchmark your application. If you want to use the RT FIFO that you create to transfer data between loops in separate VIs, you can use one of the following methods: Use Create RT FIFO in the top-level VI in your RT application and then wire rt fifo into multiple subVIs on the diagram. If you do not want to use wires, you can use a string constant and the name input of RT FIFO Create. Naming an RT FIFO that you create in the top-level VI of your RT application allows you to call a reference to an existing RT FIFO using the same name in a subVI. An example of the code that you would use to create and call a reference to an RT FIFO is shown in the following image. |
| --- | --- |
|  | When you use RT FIFO Write in a loop, it writes a value for every iteration of the Timed Loop. If the RT FIFO is full, RT FIFO Write overwrites the oldest value in the RT FIFO. Note You can prevent the node from overwriting the oldest value and ensure that no data is lost by using timeout in ms to configure RT FIFO Write to wait for space to become available. |
|  | If your application does not require that you receive a new value from the RT FIFO for every iteration of the Timed Loop, you can use a Feedback Node with RT FIFO Read instead of configuring timeout in ms and monitoring empty?. Wire a reverse Feedback Node to element and element out so RT FIFO Read produces data using the previous value if there is no new value available in the RT FIFO. In this diagram, RT FIFO Read uses the value from the previous iteration if Amplitude does not write a new value to the RT FIFO. |
|  | Configure the timeout in ms input of RT FIFO Read to wait infinitely for a new value from the Timed Loop. If this timing configuration causes high CPU usage in your application, consider using a Wait node in the While Loop that is configured to wait for longer than the period of the Timed Loop. |
|  | Create a safe shutdown process by using Stop Timed Structure to abort the Timed Loop when the While Loop stops executing due to an error or user action. Stopping the execution of the Timed Loop directly from a user control can result in execution aborting during unknown conditions. For example, if the application controls a piece of equipment and the stop control in the While Loop is wired to the part of your application that monitors conditions, the equipment can stop when conditions are not ideal. Note Stop Timed Structure does not stop the Timed Loop if error in contains an error, so you should use Clear Error Cluster to clear errors from the error wire. |
|  | Delete the reference to the RT FIFO to release the memory resources allocated on the RT controller when you created the reference. Because of the nature of dataflow, the error wire ensures that RT FIFO Delete executes after the Timed Loop stops. Note RT FIFO Delete does not delete the reference if error in contains an error, so you should use Clear Error Cluster to clear errors from the error wire. |

#### Troubleshooting

- If the application stops producing data but does not abort execution, you may need to update the configuration of one of the RT FIFO nodes: 
 If you configured RT FIFO Write in the Timed Loop to wait until space becomes available instead of writing over the oldest value in the RT FIFO, use the size input of RT Create FIFO to increase the buffer size of that RT FIFO.If you configured RT FIFO Read in the While Loop to wait infinitely and the Timed Loop stopped producing data, use a timing node to control the timing of the While Loop instead.

#### Examples

Search within the programming environment to access the following installed example:

Parent topic:

Types of Data Transfer in Real-Time Applications

Related concepts:

- Types of Data Transfer in Real-Time Applications

Related tasks:

- Minimizing Jitter in a Deterministic Loop
