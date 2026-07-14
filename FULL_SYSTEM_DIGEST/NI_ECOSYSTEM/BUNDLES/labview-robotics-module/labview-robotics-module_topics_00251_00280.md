# NI DOCUMENT BUNDLE: labview-robotics-module

<!--NI_BUNDLE_CHUNK bundle=labview-robotics-module start=251 end=280 -->
<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/skit_direct_io_pal.html language=enus -->
## TOPIC 00251: Direct Input and Output VIs

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/skit_direct_io_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/skit_direct_io_pal.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Direct Input and Output VIs

**Owning Palette:** [Starter Kit 1.0 VIs](../lvrobovi/starter_kit_1_pal.html), [Starter Kit 2.0 VIs](../lvrobovi/starter_kit_2_pal.html)

**Requires:** [LabVIEW Robotics Starter Kit](../lvrobogsm/robo_skit_overview.html). This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Direct Input and Output VIs to read or write values to I/O resources connected to the FPGA on the Starter Kit robot. These VIs allow you to [communicate with additional I/O resources](../lvrobogsm/robo_skit_programming.html#direct_io) on the FPGA without writing or compiling an FPGA VI.

Refer to the user guide for the specific Single-Board RIO on your robot for dimensions, pinouts, and specifications. You can find the user guide and other resources in the National Instruments Product Manuals Library at ni.com/manuals.

| Palette Object | Description |
| --- | --- |
| Read AI Line | Reads the voltage value from an analog input line on the Starter Kit FPGA. |
| Read DIO Line | Disables digital output and reads the value of a digital I/O line on the Starter Kit FPGA. |
| Write AO Line | Writes a voltage value to an analog output line on the Starter Kit FPGA. |
| Write DIO Line | Enables digital output and writes a value to a digital I/O line on the Starter Kit FPGA. |
| Write PWM Line | Generates a pulse width modulation (PWM) output on a digital I/O line of the Starter Kit FPGA. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/skit_init_2.html language=enus -->
## TOPIC 00252: Initialize Starter Kit 2.0 (sbRIO-9632) VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/skit_init_2.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/skit_init_2.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Initialize Starter Kit 2.0 (sbRIO-9632) VI

**Owning Palette:** [Starter Kit 2.0 VIs](../lvrobovi/starter_kit_2_pal.html)

**Requires:** [LabVIEW Robotics Starter Kit](../lvrobogsm/robo_skit_overview.html)

Begins a communication session with the FPGA on the robot you want to control and returns a reference you use to [read from or write to the FPGA](../lvrobogsm/robo_skit_programming.html#comm_overview). You must call this VI before you access I/O on the FPGA.

|  | Note You must configure the sbRIO-9632 chassis to use the LabVIEW FPGA Interface programming mode or the Starter Kit VIs do not run on the sbRIO. |
| --- | --- |

Use the [Close Starter Kit](../lvrobovi/skit_close.html) VI to end the communication session with the robot.

[Details](#details)  [Example](#examples)

[IMAGE alt='image' src='initialize_skit_2.gif']

|  | IP address specifies the IP address of an sbRIO connected to the host computer. By default, this VI uses the IP address defined for the sbRIO target in the Project Explorer window. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | FPGA starter kit host 2.0 out is a reference to the communication session between the host VI and the FPGA on the robot. You can wire this output to other Starter Kit VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Initialize Starter Kit 2.0 (sbRIO-9632) Details

To [simulate a Starter Kit application](../lvrobogsm/robo_skit_sim.html), use the [Initialize Simulated Starter Kit 2.0](../lvrobovi/skit_init_sim_2.html) VI instead of this VI.

#### Example

Refer to the Starter Kit 2.0.lvproj in the labview\examples\robotics\Starter Kit 2.0 directory for an example of using the Initialize Starter Kit 2.0 (sbRIO-9632) VI.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/skit_init_sim_1.html language=enus -->
## TOPIC 00253: Initialize Simulated Starter Kit 1.0 VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/skit_init_sim_1.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/skit_init_sim_1.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Initialize Simulated Starter Kit 1.0 VI

**Owning Palette:** [Starter Kit 1.0 VIs](../lvrobovi/starter_kit_1_pal.html)

**Requires:** [LabVIEW Robotics Starter Kit](../lvrobogsm/robo_skit_overview.html)

Begins a communication session for a [simulated Starter Kit 1.0 robot](../lvrobogsm/robo_skit_sim.html).

Use this VI with the [Start Simulator Service](../lvrobovi/sim_start_service.html) VI to begin a simulation program. Use the [Close Starter Kit](../lvrobovi/skit_close.html) VI to end the communication session when you finish simulating the robot.

[Details](#details)  [Example](#examples)

[IMAGE alt='image' src='initialize_sim_skit_1.gif']

|  | robot ID specifies the ID assigned to the robot in the simulation instance the Start Simulator Service VI runs. To identify the robot you want to reference, you must find and specify its ID. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | simulated starter kit host 1.0 out is a reference to the communication session between the host VI and the FPGA on the robot. You can wire this output to other Starter Kit VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Initialize Simulated Starter Kit 1.0 Details

You must replace this VI with the [Initialize Starter Kit 1.0 (sbRIO-9631)](../lvrobovi/skit_init_1.html) VI before you [deploy the Starter Kit application](../lvrobogsm/robo_sim_deploying.html) to a real robot.

#### Example

Refer to the Starter Kit 1.0.lvproj in the labview\examples\robotics\Starter Kit 1.0 directory for an example of using the Initialize Simulated Starter Kit 1.0 VI.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/skit_init_sim_2.html language=enus -->
## TOPIC 00254: Initialize Simulated Starter Kit 2.0 VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/skit_init_sim_2.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/skit_init_sim_2.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Initialize Simulated Starter Kit 2.0 VI

**Owning Palette:** [Starter Kit 2.0 VIs](../lvrobovi/starter_kit_2_pal.html)

**Requires:** [LabVIEW Robotics Starter Kit](../lvrobogsm/robo_skit_overview.html)

Begins a communication session for a [simulated Starter Kit 2.0 robot](../lvrobogsm/robo_skit_sim.html).

Use this VI with the [Start Simulator Service](../lvrobovi/sim_start_service.html) VI to begin a simulation program. Use the [Close Starter Kit](../lvrobovi/skit_close.html) VI to end the communication session when you finish simulating the robot.

[Details](#details)  [Example](#examples)

[IMAGE alt='image' src='initialize_sim_skit_2.gif']

|  | robot ID specifies the ID assigned to the robot in the simulation instance the Start Simulator Service VI runs. To identify the robot you want to reference, you must find and specify its ID. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | simulated starter kit host 2.0 out is a reference to the communication session between the host VI and the FPGA on the robot. You can wire this output to other Starter Kit VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Initialize Simulated Starter Kit 2.0 Details

You must replace this VI with the [Initialize Starter Kit 2.0 (sbRIO-9632)](../lvrobovi/skit_init_2.html) VI before you [deploy the Starter Kit application](../lvrobogsm/robo_sim_deploying.html) to a real robot.

#### Example

Refer to the Starter Kit 2.0.lvproj in the labview\examples\robotics\Starter Kit 2.0 directory for an example of using the Initialize Simulated Starter Kit 2.0 VI.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/skit_read_ai.html language=enus -->
## TOPIC 00255: Read AI Line VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/skit_read_ai.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/skit_read_ai.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Read AI Line VI

**Owning Palette:** [Direct Input and Output VIs](../lvrobovi/skit_direct_io_pal.html)

**Requires:** [LabVIEW Robotics Starter Kit](../lvrobogsm/robo_skit_overview.html)

Reads the voltage value from an analog input line on the Starter Kit FPGA.

[IMAGE alt='image' src='read_ai_line.gif']

|  | AI line specifies the analog input line from which you want to read data. 4000ModA/AI0 (default)4001ModA/AI14002ModA/AI24003ModA/AI34004ModA/AI44005ModA/AI54006ModA/AI64007ModA/AI74008ModA/AI84009ModA/AI9 |
| --- | --- |
| 4000 | ModA/AI0 (default) |
| 4001 | ModA/AI1 |
| 4002 | ModA/AI2 |
| 4003 | ModA/AI3 |
| 4004 | ModA/AI4 |
| 4005 | ModA/AI5 |
| 4006 | ModA/AI6 |
| 4007 | ModA/AI7 |
| 4008 | ModA/AI8 |
| 4009 | ModA/AI9 |
|  | starter kit host in is a reference to the communication session between the host VI and the FPGA on the robot. Use the Starter Kit initialization VI that is appropriate for your application to generate this LabVIEW class object. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | starter kit host out is a reference to the communication session between the host VI and the FPGA on the robot. You can wire this output to other Starter Kit VIs. |
|  | data returns the voltage value from the AI line you specify. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/skit_read_dio.html language=enus -->
## TOPIC 00256: Read DIO Line VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/skit_read_dio.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/skit_read_dio.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Read DIO Line VI

**Owning Palette:** [Direct Input and Output VIs](../lvrobovi/skit_direct_io_pal.html)

**Requires:** [LabVIEW Robotics Starter Kit](../lvrobogsm/robo_skit_overview.html)

Disables digital output and reads the value of a digital I/O line on the Starter Kit FPGA.

[IMAGE alt='image' src='read_dio_line.gif']

|  | DIO line identifies the digital I/O line you want to access. 1300Port3/DIO0 (default)1301Port3/DIO11302Port3/DIO21303Port3/DIO31304Port3/DIO41305Port3/DIO51306Port3/DIO61307Port3/DIO71308Port3/DIO81309Port3/DIO96000FPGA LED |
| --- | --- |
| 1300 | Port3/DIO0 (default) |
| 1301 | Port3/DIO1 |
| 1302 | Port3/DIO2 |
| 1303 | Port3/DIO3 |
| 1304 | Port3/DIO4 |
| 1305 | Port3/DIO5 |
| 1306 | Port3/DIO6 |
| 1307 | Port3/DIO7 |
| 1308 | Port3/DIO8 |
| 1309 | Port3/DIO9 |
| 6000 | FPGA LED |
|  | starter kit host in is a reference to the communication session between the host VI and the FPGA on the robot. Use the Starter Kit initialization VI that is appropriate for your application to generate this LabVIEW class object. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | starter kit host out is a reference to the communication session between the host VI and the FPGA on the robot. You can wire this output to other Starter Kit VIs. |
|  | data returns the value from the DIO line you specify. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/skit_read_motor_vel.html language=enus -->
## TOPIC 00257: Read DC Motor Velocities VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/skit_read_motor_vel.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/skit_read_motor_vel.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Read DC Motor Velocities VI

**Requires:** [LabVIEW Robotics Starter Kit](../lvrobogsm/robo_skit_overview.html)

**Owning Palette:** [Starter Kit 1.0 VIs](../lvrobovi/starter_kit_1_pal.html), [Starter Kit 2.0 VIs](../lvrobovi/starter_kit_2_pal.html)

Reads and returns the velocities of the left and right drive motors on the Starter Kit robot in the counterclockwise direction. The left and right motors are defined by their positions as you view the robot from behind.

[Use this VI with the Steering VIs](../lvrobogsm/robo_skit_programming.html#skit_steering) to convert between individual motor velocities and the overall steering frame velocity and to implement other steering behavior for a Starter Kit robot.

[Examples](#examples)

[IMAGE alt='image' src='read_dc_motor_velocities.gif']

|  | starter kit host in is a reference to the communication session between the host VI and the FPGA on the robot. Use the Starter Kit initialization VI that is appropriate for your application to generate this LabVIEW class object. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | starter kit host out is a reference to the communication session between the host VI and the FPGA on the robot. You can wire this output to other Starter Kit VIs. |
|  | left motor ccw velocity (rad/s) returns the velocity, in radians per second, at which the left motor moves. The velocity value this VI returns is that which turns the left-side wheels in the counterclockwise direction when you view the wheels from on end. Thus, positive values move the robot forward, and negative values move the robot backward. |
|  | right motor ccw velocity (rad/s) specifies the velocity, in radians per second, at which the right motor moves. The velocity value this VI returns is that which turns the right-side wheels in the counterclockwise direction when you view the wheels from on end. Thus, negative values move the robot forward, and positive values move the robot backward. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the Read DC Motor Velocities VI:

- labview\examples\robotics\Starter Kit 1.0\Starter Kit 1.0.lvproj
- labview\examples\robotics\Starter Kit 2.0\Starter Kit 2.0.lvproj

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/skit_read_ping.html language=enus -->
## TOPIC 00258: Read PING))) Sensor Distance VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/skit_read_ping.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/skit_read_ping.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Read PING))) Sensor Distance VI

**Requires:** [LabVIEW Robotics Starter Kit](../lvrobogsm/robo_skit_overview.html)

**Owning Palette:** [Starter Kit 1.0 VIs](../lvrobovi/starter_kit_1_pal.html), [Starter Kit 2.0 VIs](../lvrobovi/starter_kit_2_pal.html)

Reads and returns the distance between the PING))) ultrasonic distance sensor and the nearest obstacle the sensor detects. The PING))) sensor has a maximum detection range of three meters.

If the sensor does not detect any obstacle within range, **timed out?** is TRUE.

[Details](#details)  [Examples](#examples)

[IMAGE alt='image' src='read_ping_sensor_distance.gif']

|  | starter kit host in is a reference to the communication session between the host VI and the FPGA on the robot. Use the Starter Kit initialization VI that is appropriate for your application to generate this LabVIEW class object. |
| --- | --- |
|  | default distance specifies the distance value this VI returns if the sensor does not detect an obstacle within its maximum range and the read times out. The behavior is useful because it allows you to define code to run when the robot is not within range of any obstacles. The default is NaN. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | starter kit host out is a reference to the communication session between the host VI and the FPGA on the robot. You can wire this output to other Starter Kit VIs. |
|  | distance (m) returns the distance, in meters, between the distance sensor and the nearest obstacle, if the sensor detects one. Otherwise, this output returns the default distance. |
|  | timed out?, if TRUE, indicates the sensor did not detect an obstacle within its maximum range. If timed out? is TRUE, this output returns the default distance you specify in the distance output. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Read PING))) Sensor Distance Details

You can use the [Write Sensor Servo Angle](../lvrobovi/skit_write_servo_angle.html) VI to change the orientation of the sensor and then use this VI to read the distance to any obstacles at that sensor angle. Pair the servo angle you write with the Write Sensor Servo Angle VI and the distance value this VI reads to identify the exact location of obstacles in relation to the robot. When you know the angle and distance to an obstacle, you can write code to adjust the robot motor velocities to avoid the obstacle.

For more information about the PING))) ultrasonic sensor, refer to the Parallax Web site.

#### Examples

Refer to the following VIs for examples of using the Read PING))) Sensor Distance VI:

- labview\examples\robotics\Starter Kit 1.0\Starter Kit 1.0.lvproj
- labview\examples\robotics\Starter Kit 2.0\Starter Kit 2.0.lvproj

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/skit_read_servo_offset.html language=enus -->
## TOPIC 00259: Read Sensor Servo Offset VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/skit_read_servo_offset.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/skit_read_servo_offset.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Read Sensor Servo Offset VI

**Requires:** [LabVIEW Robotics Starter Kit](../lvrobogsm/robo_skit_overview.html)

**Owning Palette:** [Starter Kit 1.0 VIs](../lvrobovi/starter_kit_1_pal.html), [Starter Kit 2.0 VIs](../lvrobovi/starter_kit_2_pal.html)

Reads and returns the amount by which the zero, or straight-forward, position of the ultrasonic distance sensor is calibrated to differ from the zero position of the sensor servo.

If you use the Robotics Hardware Setup Wizard to set up your Starter Kit robot, the wizard guides you through calibrating the sensor to be offset by the appropriate amount, and then saves the offset value on the Single-Board RIO (sbRIO). This VI reads that value from the sbRIO.

[Examples](#examples)

[IMAGE alt='image' src='read_sensor_servo_offset.gif']

|  | starter kit host in is a reference to the communication session between the host VI and the FPGA on the robot. Use the Starter Kit initialization VI that is appropriate for your application to generate this LabVIEW class object. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | starter kit host out is a reference to the communication session between the host VI and the FPGA on the robot. You can wire this output to other Starter Kit VIs. |
|  | ccw offset angle (rad) returns the angle, in radians, by which the zero, or straight-forward, position of the ultrasonic distance sensor is offset from the zero position of the sensor servo. The angle is measured counterclockwise from the center of the robot as you view the robot from above. Thus, positive values fall to the left of center, and negative values fall to the right. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Examples

Refer to the following VIs for examples of using the Read Sensor Servo Offset VI:

- labview\examples\robotics\Starter Kit 1.0\Starter Kit 1.0.lvproj
- labview\examples\robotics\Starter Kit 2.0\Starter Kit 2.0.lvproj

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/skit_write_ao.html language=enus -->
## TOPIC 00260: Write AO Line VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/skit_write_ao.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/skit_write_ao.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Write AO Line VI

**Owning Palette:** [Direct Input and Output VIs](../lvrobovi/skit_direct_io_pal.html)

**Requires:** [LabVIEW Robotics Starter Kit](../lvrobogsm/robo_skit_overview.html)

Writes a voltage value to an analog output line on the Starter Kit FPGA.

[IMAGE alt='image' src='write_ao_line.gif']

|  | AO line specifies the analog output line to which you want to write data. 5100ModB/AO0 (default)5101ModB/AO15102ModB/AO25103ModB/AO3 |
| --- | --- |
| 5100 | ModB/AO0 (default) |
| 5101 | ModB/AO1 |
| 5102 | ModB/AO2 |
| 5103 | ModB/AO3 |
|  | starter kit host in is a reference to the communication session between the host VI and the FPGA on the robot. Use the Starter Kit initialization VI that is appropriate for your application to generate this LabVIEW class object. |
|  | data specifies the value you want to write to the AO line you specify. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | starter kit host out is a reference to the communication session between the host VI and the FPGA on the robot. You can wire this output to other Starter Kit VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/skit_write_dio.html language=enus -->
## TOPIC 00261: Write DIO Line VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/skit_write_dio.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/skit_write_dio.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Write DIO Line VI

**Owning Palette:** [Direct Input and Output VIs](../lvrobovi/skit_direct_io_pal.html)

**Requires:** [LabVIEW Robotics Starter Kit](../lvrobogsm/robo_skit_overview.html)

Enables digital output and writes a value to a digital I/O line on the Starter Kit FPGA.

[IMAGE alt='image' src='write_dio_line.gif']

|  | DIO line identifies the digital I/O line you want to access. 1300Port3/DIO0 (default)1301Port3/DIO11302Port3/DIO21303Port3/DIO31304Port3/DIO41305Port3/DIO51306Port3/DIO61307Port3/DIO71308Port3/DIO81309Port3/DIO96000FPGA LED |
| --- | --- |
| 1300 | Port3/DIO0 (default) |
| 1301 | Port3/DIO1 |
| 1302 | Port3/DIO2 |
| 1303 | Port3/DIO3 |
| 1304 | Port3/DIO4 |
| 1305 | Port3/DIO5 |
| 1306 | Port3/DIO6 |
| 1307 | Port3/DIO7 |
| 1308 | Port3/DIO8 |
| 1309 | Port3/DIO9 |
| 6000 | FPGA LED |
|  | starter kit host in is a reference to the communication session between the host VI and the FPGA on the robot. Use the Starter Kit initialization VI that is appropriate for your application to generate this LabVIEW class object. |
|  | data specifies the value you want to write to the DIO line you specify. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | starter kit host out is a reference to the communication session between the host VI and the FPGA on the robot. You can wire this output to other Starter Kit VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/skit_write_motor_setpts.html language=enus -->
## TOPIC 00262: Write DC Motor Velocity Setpoints VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/skit_write_motor_setpts.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/skit_write_motor_setpts.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Write DC Motor Velocity Setpoints VI

**Requires:** [LabVIEW Robotics Starter Kit](../lvrobogsm/robo_skit_overview.html)

**Owning Palette:** [Starter Kit 1.0 VIs](../lvrobovi/starter_kit_1_pal.html), [Starter Kit 2.0 VIs](../lvrobovi/starter_kit_2_pal.html)

Applies velocity values to the drive motors on the Starter Kit robot. The left and right motors are defined by their positions as you view the robot from behind. The maximum motor velocity is 15.7 rad/s.

[Use this VI with the Steering VIs](../lvrobogsm/robo_skit_programming.html#skit_steering) to convert between the overall steering frame velocity and individual motor velocities and to implement other steering behavior for a Starter Kit robot.

[Details](#details)  [Examples](#examples)

[IMAGE alt='image' src='write_dc_motor_velocity_setpoints.gif']

|  | starter kit host in is a reference to the communication session between the host VI and the FPGA on the robot. Use the Starter Kit initialization VI that is appropriate for your application to generate this LabVIEW class object. |
| --- | --- |
|  | left motor ccw velocity (rad/s) specifies the velocity, in radians per second, at which you want the left motor to move. If you specify a value greater than the maximum velocity of 15.7 rad/s, the motor moves at the maximum velocity. The velocity you specify turns the left-side wheels in the counterclockwise direction when you view the wheels from on end. Thus, positive values move the robot forward, and negative values move the robot backward. |
|  | right motor ccw velocity (rad/s) specifies the velocity, in radians per second, at which the right motor moves. If you specify a value greater than the maximum velocity of 15.7 rad/s, the motor moves at the maximum velocity. The velocity you specify turns the right-side wheels in the counterclockwise direction when you view the wheels from on end. Thus, negative values move the robot forward, and positive values move the robot backward. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | starter kit host out is a reference to the communication session between the host VI and the FPGA on the robot. You can wire this output to other Starter Kit VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Write DC Motor Velocity Setpoints Details

The maximum motor velocity of 15.7 rad/s corresponds to a maximum forward robot velocity of about 0.39 m/s for the Starter Kit 1.0 robot and about 0.79 m/s for the Starter Kit 2.0 robot. Use caution to avoid collisions between the robot and other objects.

#### Examples

Refer to the following VIs for examples of using the Write DC Motor Velocity Setpoints VI:

- labview\examples\robotics\Starter Kit 1.0\Starter Kit 1.0.lvproj
- labview\examples\robotics\Starter Kit 2.0\Starter Kit 2.0.lvproj

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/skit_write_pwm.html language=enus -->
## TOPIC 00263: Write PWM Line VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/skit_write_pwm.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/skit_write_pwm.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Write PWM Line VI

**Owning Palette:** [Direct Input and Output VIs](../lvrobovi/skit_direct_io_pal.html)

**Requires:** [LabVIEW Robotics Starter Kit](../lvrobogsm/robo_skit_overview.html)

Generates a pulse width modulation (PWM) output on a digital I/O line of the Starter Kit FPGA.

[IMAGE alt='image' src='write_pwm_line.gif']

|  | PWM line specifies the digital I/O line to which you want to generate the PWM output. 1004Port0/DIO4 (Left Motor) (default)1005Port0/DIO5 (Right Motor)1007Port0/DIO7 (Servo)1700Port7/DIO01701Port7/DIO11702Port7/DIO21703Port7/DIO3 |
| --- | --- |
| 1004 | Port0/DIO4 (Left Motor) (default) |
| 1005 | Port0/DIO5 (Right Motor) |
| 1007 | Port0/DIO7 (Servo) |
| 1700 | Port7/DIO0 |
| 1701 | Port7/DIO1 |
| 1702 | Port7/DIO2 |
| 1703 | Port7/DIO3 |
|  | starter kit host in is a reference to the communication session between the host VI and the FPGA on the robot. Use the Starter Kit initialization VI that is appropriate for your application to generate this LabVIEW class object. |
|  | period (us) specifies the period, in microseconds, of the PWM output you want to write. |
|  | pulse width (us) specifies the pulse width, in microseconds, of the PWM output you want to write. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | starter kit host out is a reference to the communication session between the host VI and the FPGA on the robot. You can wire this output to other Starter Kit VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/skit_write_servo_angle.html language=enus -->
## TOPIC 00264: Write Sensor Servo Angle VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/skit_write_servo_angle.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/skit_write_servo_angle.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Write Sensor Servo Angle VI

**Requires:** [LabVIEW Robotics Starter Kit](../lvrobogsm/robo_skit_overview.html)

**Owning Palette:** [Starter Kit 1.0 VIs](../lvrobovi/starter_kit_1_pal.html), [Starter Kit 2.0 VIs](../lvrobovi/starter_kit_2_pal.html)

Writes an angle to the servo on which the distance sensor is mounted to turn the servo to that angle. Note that the servo angle is different from the sensor angle if the servo and the sensor are not aligned.

|  | Note The maximum range the servo motor can turn is ± / 2 radians, or ±90°. |
| --- | --- |

[Details](#details)  [Examples](#examples)

[IMAGE alt='image' src='write_sensor_servo_angle.gif']

|  | starter kit host in is a reference to the communication session between the host VI and the FPGA on the robot. Use the Starter Kit initialization VI that is appropriate for your application to generate this LabVIEW class object. |
| --- | --- |
|  | ccw servo angle (rad) specifies the angle, in radians, to which to turn the sensor servo. The angle is measured counterclockwise from the center of the robot as you view the robot from above. Thus, positive values turn the servo to the left of center, and negative values turn the servo to the right. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | starter kit host out is a reference to the communication session between the host VI and the FPGA on the robot. You can wire this output to other Starter Kit VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Write Sensor Servo Angle Details

You can use this VI to change the orientation of the sensor and then use the [Read PING))) Sensor Distance](../lvrobovi/skit_read_ping.html) VI to read the distance to any obstacles at that sensor angle. Pair the servo angle you write with this VI and the distance value the Read PING))) Sensor Distance VI reads to identify the exact location of obstacles in relation to the robot. When you know the angle and distance to an obstacle, you can write code to adjust the robot motor velocities to avoid the obstacle.

#### Examples

Refer to the following VIs for examples of using the Write Sensor Servo Angle VI:

- labview\examples\robotics\Starter Kit 1.0\Starter Kit 1.0.lvproj
- labview\examples\robotics\Starter Kit 2.0\Starter Kit 2.0.lvproj

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/skit_write_servo_offset.html language=enus -->
## TOPIC 00265: Write Sensor Servo Offset VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/skit_write_servo_offset.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/skit_write_servo_offset.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Write Sensor Servo Offset VI

**Requires:** [LabVIEW Robotics Starter Kit](../lvrobogsm/robo_skit_overview.html)

**Owning Palette:** [Starter Kit 1.0 VIs](../lvrobovi/starter_kit_1_pal.html), [Starter Kit 2.0 VIs](../lvrobovi/starter_kit_2_pal.html)

Defines the amount by which the zero, or straight-forward, position of the distance sensor differs from the zero position of the sensor servo on which the sensor is mounted. You can use this VI to save the offset value to a file so the value is associated with the same robot in the future.

[Examples](#examples)

[IMAGE alt='image' src='write_sensor_servo_offset.gif']

|  | save to file, if TRUE, specifies to save the offset value to a file so you can use the value in the future. When you run subsequent applications on the same robot, LabVIEW automatically reads the offset value from the file. If this VI runs on the Single-Board RIO, LabVIEW saves the file on the device. If this VI runs on a desktop computer, LabVIEW saves the file in the LabVIEW Data directory. |
| --- | --- |
|  | starter kit host in is a reference to the communication session between the host VI and the FPGA on the robot. Use the Starter Kit initialization VI that is appropriate for your application to generate this LabVIEW class object. |
|  | ccw offset angle (rad) specifies the angle, in radians, to define for the difference between the straight-forward position of the sensor and the position of the sensor servo. The angle is measured counterclockwise from the center of the robot as you view the robot from above. Thus, positive values fall to the left of center, and negative values fall to the right. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |

#### Examples

Refer to the following VIs for examples of using the Write Sensor Servo Offset VI:

- labview\examples\robotics\Starter Kit 1.0\Starter Kit 1.0.lvproj
- labview\examples\robotics\Starter Kit 2.0\Starter Kit 2.0.lvproj

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/starter_kit_1_pal.html language=enus -->
## TOPIC 00266: Starter Kit 1.0 VIs

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/starter_kit_1_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/starter_kit_1_pal.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Starter Kit 1.0 VIs

**Owning Palette:** [Starter Kit VIs](../lvrobovi/starter_kit_pal.html)

**Requires:** [LabVIEW Robotics Starter Kit](../lvrobogsm/robo_skit_overview.html). This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

[Use the Starter Kit 1.0 VIs](../lvrobogsm/robo_skit_programming.html) to control the [Robotics Starter Kit 1.0 robot](../lvrobogsm/robo_skit_overview.html), which is a four-wheeled mobile robot that contains an NI sbRIO-9631 controller, drive motors, and a Parallax PING))) ultrasonic distance sensor.

[Example](#examples)

| Palette Object | Description |
| --- | --- |
| Create Starter Kit 1.0 Steering Frame | Generates a steering frame object for the Starter Kit 1.0 robot. You can use the steering frame object with the Steering VIs to implement steering for the Starter Kit robot. |
| Initialize Simulated Starter Kit 1.0 | Begins a communication session for a simulated Starter Kit 1.0 robot. |
| Initialize Starter Kit 1.0 (sbRIO-9631) | Begins a communication session with the FPGA on the robot you want to control and returns a reference you use to read from or write to the FPGA. You must call this VI before you access I/O on the FPGA. |

The Starter Kit 1.0 palette also includes the following VIs that appear on both this palette and the [Starter Kit 2.0](../lvrobovi/starter_kit_2_pal.html) palette.

| Palette Object | Description |
| --- | --- |
| Close Starter Kit | Terminates a communication session with the FPGA on a real or simulated Starter Kit robot. When the communication session ends, the drive motors, distance sensor, and sensor servo stop operating. |
| Read DC Motor Velocities | Reads and returns the velocities of the left and right drive motors on the Starter Kit robot in the counterclockwise direction. The left and right motors are defined by their positions as you view the robot from behind. |
| Read PING))) Sensor Distance | Reads and returns the distance between the PING))) ultrasonic distance sensor and the nearest obstacle the sensor detects. The PING))) sensor has a maximum detection range of three meters. |
| Read Sensor Servo Offset | Reads and returns the amount by which the zero, or straight-forward, position of the ultrasonic distance sensor is calibrated to differ from the zero position of the sensor servo. |
| Write DC Motor Velocity Setpoints | Applies velocity values to the drive motors on the Starter Kit robot. The left and right motors are defined by their positions as you view the robot from behind. The maximum motor velocity is 15.7 rad/s. |
| Write Sensor Servo Angle | Writes an angle to the servo on which the distance sensor is mounted to turn the servo to that angle. Note that the servo angle is different from the sensor angle if the servo and the sensor are not aligned. |
| Write Sensor Servo Offset | Defines the amount by which the zero, or straight-forward, position of the distance sensor differs from the zero position of the sensor servo on which the sensor is mounted. You can use this VI to save the offset value to a file so the value is associated with the same robot in the future. |

| Subpalette | Description |
| --- | --- |
| Direct Input and Output VIs | Use the Direct Input and Output VIs to read or write values to I/O resources connected to the FPGA on the Starter Kit robot. These VIs allow you to communicate with additional I/O resources on the FPGA without writing or compiling an FPGA VI. |

#### Example

Refer to the Starter Kit 1.0.lvproj in the labview\examples\robotics\Starter Kit 1.0 directory for an example of using the Starter Kit 1.0 VIs.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/starter_kit_2_pal.html language=enus -->
## TOPIC 00267: Starter Kit 2.0 VIs

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/starter_kit_2_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/starter_kit_2_pal.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Starter Kit 2.0 VIs

**Owning Palette:** [Starter Kit VIs](../lvrobovi/starter_kit_pal.html)

**Requires:** [LabVIEW Robotics Starter Kit](../lvrobogsm/robo_skit_overview.html). This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

[Use the Starter Kit 2.0 VIs](../lvrobogsm/robo_skit_programming.html) to control the [Robotics Starter Kit 2.0 robot](../lvrobogsm/robo_skit_overview.html), which is a three-wheeled mobile robot that contains an NI sbRIO-9632 controller, drive motors, and a Parallax PING))) ultrasonic distance sensor.

[Example](#examples)

|  | Note You must configure the sbRIO-9632 chassis to use the LabVIEW FPGA Interface programming mode or the Starter Kit VIs do not run on the sbRIO. |
| --- | --- |

| Palette Object | Description |
| --- | --- |
| Create Starter Kit 2.0 Steering Frame | Generates a steering frame object for the Starter Kit 2.0 robot. You can use the steering frame object with the Steering VIs to implement steering for the Starter Kit robot. |
| Initialize Simulated Starter Kit 2.0 | Begins a communication session for a simulated Starter Kit 2.0 robot. |
| Initialize Starter Kit 2.0 (sbRIO-9632) | Begins a communication session with the FPGA on the robot you want to control and returns a reference you use to read from or write to the FPGA. You must call this VI before you access I/O on the FPGA. |

The Starter Kit 2.0 palette also includes the following VIs that appear on both this palette and the [Starter Kit 1.0](../lvrobovi/starter_kit_1_pal.html) palette.

| Palette Object | Description |
| --- | --- |
| Close Starter Kit | Terminates a communication session with the FPGA on a real or simulated Starter Kit robot. When the communication session ends, the drive motors, distance sensor, and sensor servo stop operating. |
| Read DC Motor Velocities | Reads and returns the velocities of the left and right drive motors on the Starter Kit robot in the counterclockwise direction. The left and right motors are defined by their positions as you view the robot from behind. |
| Read PING))) Sensor Distance | Reads and returns the distance between the PING))) ultrasonic distance sensor and the nearest obstacle the sensor detects. The PING))) sensor has a maximum detection range of three meters. |
| Read Sensor Servo Offset | Reads and returns the amount by which the zero, or straight-forward, position of the ultrasonic distance sensor is calibrated to differ from the zero position of the sensor servo. |
| Write DC Motor Velocity Setpoints | Applies velocity values to the drive motors on the Starter Kit robot. The left and right motors are defined by their positions as you view the robot from behind. The maximum motor velocity is 15.7 rad/s. |
| Write Sensor Servo Angle | Writes an angle to the servo on which the distance sensor is mounted to turn the servo to that angle. Note that the servo angle is different from the sensor angle if the servo and the sensor are not aligned. |
| Write Sensor Servo Offset | Defines the amount by which the zero, or straight-forward, position of the distance sensor differs from the zero position of the sensor servo on which the sensor is mounted. You can use this VI to save the offset value to a file so the value is associated with the same robot in the future. |

| Subpalette | Description |
| --- | --- |
| Direct Input and Output VIs | Use the Direct Input and Output VIs to read or write values to I/O resources connected to the FPGA on the Starter Kit robot. These VIs allow you to communicate with additional I/O resources on the FPGA without writing or compiling an FPGA VI. |

#### Example

Refer to the Starter Kit 2.0.lvproj in the labview\examples\robotics\Starter Kit 2.0 directory for an example of using the Starter Kit 2.0 VIs.

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/starter_kit_pal.html language=enus -->
## TOPIC 00268: Starter Kit VIs

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/starter_kit_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/starter_kit_pal.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Starter Kit VIs

**Owning Palette:** [Robotics VIs](../lvrobovi/robotics_pal.html)

**Requires:** [LabVIEW Robotics Starter Kit](../lvrobogsm/robo_skit_overview.html). This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the VIs on the subpalette that corresponds to your [LabVIEW Robotics Starter Kit robot](../lvrobogsm/robo_skit_overview.html) to [control the robot without writing an FPGA VI](../lvrobogsm/robo_skit_programming.html).

| Subpalette | Description |
| --- | --- |
| Starter Kit 1.0 VIs | Use the Starter Kit 1.0 VIs to control the Robotics Starter Kit 1.0 robot, which is a four-wheeled mobile robot that contains an NI sbRIO-9631 controller, drive motors, and a Parallax PING))) ultrasonic distance sensor. |
| Starter Kit 2.0 VIs | Use the Starter Kit 2.0 VIs to control the Robotics Starter Kit 2.0 robot, which is a three-wheeled mobile robot that contains an NI sbRIO-9632 controller, drive motors, and a Parallax PING))) ultrasonic distance sensor. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/steering_advanced_pal.html language=enus -->
## TOPIC 00269: Advanced VIs

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/steering_advanced_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/steering_advanced_pal.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Advanced VIs

**Owning Palette:** [Steering VIs](../lvrobovi/steering_pal.html)

**Requires:** Robotics Module. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Advanced VIs to add wheels to a steering frame, replace a wheel with another wheel, return information about wheels, and so on.

| Palette Object | Description |
| --- | --- |
| Add Wheels to Steering Frame | Adds the wheel or wheels you specify to steering frame in. You must manually select the polymorphic instance to use. |
| Create Steering Frame | Creates a steering frame of the type you specify. You must manually select the polymorphic instance to use. |
| Create Wheel | Creates a wheel of the type you specify that you can add to a steering frame. You must manually select the polymorphic instance to use. |
| Get Wheel Information | Returns information, such as wheel radius and gear ratio, for the wheel you specify. You must manually select the polymorphic instance to use. |
| Get Wheels in Steering Frame | Returns the wheels you specify in steering frame in and properties of those wheels. You must manually select the polymorphic instance to use. |
| Remove Wheels from Steering Frame | Removes the wheel or wheels you specify from steering frame in. You must manually select the polymorphic instance to use. |
| Replace Wheels in Steering Frame | Replaces wheels in steering frame in with the wheels you specify. You must manually select the polymorphic instance to use. |
| Reposition Wheels on Steering Frame | Changes the location of the wheel or wheels to the position and angle you specify. You must manually select the polymorphic instance to use. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/steering_pal.html language=enus -->
## TOPIC 00270: Steering VIs

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/steering_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/steering_pal.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Steering VIs

**Owning Palette:** [Robotics VIs](../lvrobovi/robotics_pal.html)

**Requires:** Robotics Module. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Steering VIs to create a mobile robotics system that consists of a built-in or user-defined steering frame and wheels. You can calculate and convert between robot and wheel velocity and connect with motors that drive wheels to implement motor control.

[Examples](#examples)

|  | Note When you use the Steering VIs to create and operate on a steering frame, you specify the radius of wheels, the distance of separation between wheels, and so on. Always use a consistent unit of measurement when you specify values that represent distance. |
| --- | --- |

| Palette Object | Description |
| --- | --- |
| Apply Velocity to Motors | Calculates the velocity and angle of each motor necessary to satisfy the steering frame velocity or arc velocity at the center of a steering frame. You must manually select the polymorphic instance to use. |
| Apply Velocity to Wheels | Calculates the state of each wheel necessary to satisfy the steering frame velocity or arc velocity at the center of the steering frame. You must manually select the polymorphic instance to use. |
| Configure Steering Frame | Generates a wheeled steering frame that you design in an interactive dialog box. You can choose from pre-defined steering frame designs or create a custom frame design. |
| Draw Steering Frame Picture | Creates an image you can wire to a 2D picture control to visualize a steering frame on the front panel. The picture can display data about the directions and velocities at which wheels move. |
| Get Velocity from Motors | Calculates the steering frame velocity or arc velocity required to best satisfy the velocity and angle of each motor. You must manually select the polymorphic instance to use. |
| Get Velocity from Wheels | Calculates the steering frame velocity or arc velocity required to best satisfy the state of each wheel. You can read data for each wheel from wheel motors or specify the wheel data manually. You must manually select the polymorphic instance to use. |

| Subpalette | Description |
| --- | --- |
| Advanced VIs | Use the Advanced VIs to add wheels to a steering frame, replace a wheel with another wheel, return information about wheels, and so on. |
| Motor Communication VIs | Use the Motor Communication VIs to connect robot vehicle wheels to motors that control wheel angle and velocity. When you initiate a communication session between a wheel and the motor that controls the wheel, you can read and write motor data according to the position of the wheel as it moves. |

#### Examples

Refer to the following VIs for examples of using the Steering VIs:

- labview\examples\robotics\Steering\3D Mecanum Robot\3D Mecanum Robot.lvproj
- labview\examples\robotics\Steering\Differential Steering\Differential Steering.lvproj
- labview\examples\robotics\Steering\Mecanum Steering\Mecanum Steering.lvproj

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/take_sim_steps.html language=enus -->
## TOPIC 00271: Take Simulation Steps VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/take_sim_steps.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/take_sim_steps.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Take Simulation Steps VI

**Owning Palette:** [Simulator VIs](../lvrobovi/simulator_pal.html)

**Requires:** Robotics Module

Takes forward the [robotics simulator](../lvrobogsm/robo_sim_overview.html) the number of time steps that you specify to [advance the current time of the simulation](../lvrobogsm/robo_sim_programming.html#stepsize).

You can configure the length of a step by specifying the **step size** in the [Start Simulator Service](../lvrobovi/sim_start_service.html) VI. The Take Simulation Steps VI requires that the **timing mode** input in the [Start Simulator Service](../lvrobovi/sim_start_service.html) VI is **Synchronized**.

[IMAGE alt='image' src='take_simulation_steps.gif']

|  | number of steps specifies the number of time steps that the robotics simulator runs forward. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/youbot_arm_pal.html language=enus -->
## TOPIC 00272: Arm VIs

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/youbot_arm_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/youbot_arm_pal.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Arm VIs

**Owning Palette:** [KUKA youBot VIs](../lvrobovi/youbot_pal.html)

**Requires:** Robotics Module. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Arm VIs to configure KUKA youBot arms.

|  | Note LabVIEW supports only one-arm KUKA youBots. |
| --- | --- |

| Palette Object | Description |
| --- | --- |
| Calibrate Arm | Calibrates the motors of KUKA youBot arm joints to the home position. This VI moves each arm joint to the home position. Refer to the user manual of your KUKA youBot for more information about the home position. |
| Get Arm | Gets an arm instance from the KUKA youBot indicated by the arm index. |
| Get Motors Position | Gets the motors position, which the position encoder senses, of the joints of a KUKA youBot arm. |
| Set Motors Position Setpoint | Sets the position setpoint of the motors attached to the joints of a KUKA youBot arm. |

| Subpalette | Description |
| --- | --- |
| Gripper VIs | Use the Gripper VIs to configure KUKA youBot grippers. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/youbot_close.html language=enus -->
## TOPIC 00273: Close KUKA youBot VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/youbot_close.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/youbot_close.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Close KUKA youBot VI

**Owning Palette:** [KUKA youBot VIs](../lvrobovi/youbot_pal.html)

**Requires:** Robotics Module

Terminates the KUKA youBot host interface.

[IMAGE alt='image' src='close_kuka_youbot.gif']

|  | KUKA youBot host in specifies a reference to the communication session between the host VI and the KUKA youBot. Use the Initialize KUKA youBot VI or the Initialize Simulated KUKA youBot VI to generate this LabVIEW class object. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/youbot_get_mobile_platform.html language=enus -->
## TOPIC 00274: Get Mobile Platform VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/youbot_get_mobile_platform.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/youbot_get_mobile_platform.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Get Mobile Platform VI

**Owning Palette:** [Platform VIs](../lvrobovi/youbot_platform_pal.html)

**Requires:** Robotics Module

Returns a reference to the KUKA youBot mobile platform.

[IMAGE alt='image' src='get_mobile_platform.gif']

|  | KUKA youBot host in specifies a reference to the communication session between the host VI and the KUKA youBot. Use the Initialize KUKA youBot VI or the Initialize Simulated KUKA youBot VI to generate this LabVIEW class object. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | KUKA youBot host out returns a reference to the communication session between the host VI and the KUKA youBot. You can wire this output to other KUKA youBot VIs. |
|  | KUKA youBot platform out returns a reference to a KUKA youBot platform. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/youbot_get_wheel_motors_vel.html language=enus -->
## TOPIC 00275: Get Wheel Motors Velocity VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/youbot_get_wheel_motors_vel.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/youbot_get_wheel_motors_vel.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Get Wheel Motors Velocity VI

**Owning Palette:** [Platform VIs](../lvrobovi/youbot_platform_pal.html)

**Requires:** Robotics Module

Gets the sensed motors velocity of the wheels of a KUKA youBot mobile platform.

[IMAGE alt='image' src='get_wheel_motors_velocity.gif']

|  | KUKA youBot platform in specifies a reference to a KUKA youBot platform. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | KUKA youBot platform out returns a reference to a KUKA youBot platform. |
|  | ccw velocity (rad/s) returns an array of the counter clockwise velocity setpoints, in radians per second, for each wheel of a KUKA youBot mobile platform. The index of the array corresponds to each wheel, where the arm is at the front of the robot. Index 0 is the front left wheel. Index 1 is the front right wheel. Index 2 is the back left wheel. Index 3 is the back right wheel. Refer to the user manual of your KUKA youBot for more information about the KUKA youBot wheels. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/youbot_grip_get_motors_pos.html language=enus -->
## TOPIC 00276: Get Motors Position VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/youbot_grip_get_motors_pos.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/youbot_grip_get_motors_pos.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Get Motors Position VI

**Owning Palette:** [Gripper VIs](../lvrobovi/youbot_gripper_pal.html)

**Requires:** Robotics Module

Gets the motors position, which the position encoder senses, of the joints of a KUKA youBot gripper.

[IMAGE alt='image' src='get_motors_position_gripper.gif']

|  | KUKA youBot gripper in specifies a reference to a KUKA youBot gripper. Use the Get Gripper VI to generate this LabVIEW class object. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | KUKA youbot gripper out returns a reference to a KUKA youBot gripper. |
|  | position (m) returns the position setpoint, in meters, of each KUKA youBot gripper finger. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/youbot_grip_set_motors_pos_setpt.html language=enus -->
## TOPIC 00277: Set Motors Position Setpoint VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/youbot_grip_set_motors_pos_setpt.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/youbot_grip_set_motors_pos_setpt.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Set Motors Position Setpoint VI

**Owning Palette:** [Gripper VIs](../lvrobovi/youbot_gripper_pal.html)

**Requires:** Robotics Module

Sets the position setpoint of the motors attached to the joints of a KUKA youBot gripper.

[IMAGE alt='image' src='set_motors_position_setpoint_gripper.gif']

|  | KUKA youBot gripper in specifies a reference to a KUKA youBot gripper. Use the Get Gripper VI to generate this LabVIEW class object. |
| --- | --- |
|  | position (m) specifies the position setpoint, in meters, of each KUKA youBot gripper finger. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | KUKA youbot gripper out returns a reference to a KUKA youBot gripper. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/youbot_gripper_pal.html language=enus -->
## TOPIC 00278: Gripper VIs

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/youbot_gripper_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/youbot_gripper_pal.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Gripper VIs

**Owning Palette:** [Arm VIs](../lvrobovi/youbot_arm_pal.html)

**Requires:** Robotics Module. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Gripper VIs to configure KUKA youBot grippers.

| Palette Object | Description |
| --- | --- |
| Calibrate Gripper | Calibrates the motors of KUKA youBot gripper joints to the home position. |
| Get Gripper | Gets the KUKA youBot gripper instance from a KUKA youBot arm. |
| Get Motors Position | Gets the motors position, which the position encoder senses, of the joints of a KUKA youBot gripper. |
| Set Motors Position Setpoint | Sets the position setpoint of the motors attached to the joints of a KUKA youBot gripper. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/youbot_initialize_sim.html language=enus -->
## TOPIC 00279: Initialize Simulated KUKA youBot VI

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/youbot_initialize_sim.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/youbot_initialize_sim.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### Initialize Simulated KUKA youBot VI

**Owning Palette:** [KUKA youBot VIs](../lvrobovi/youbot_pal.html)

**Requires:** Robotics Module

Initializes a simulation host interface to a simulated KUKA youBot.

[IMAGE alt='image' src='initialize_simulated_kuka_youbot.gif']

|  | robot ID specifies the ID assigned to the KUKA youBot in the simulation instance the Start Simulator Service VI runs. To identify the KUKA youBot you want to reference, you must find and specify the robot ID. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | simulated KUKA youBot host out returns a reference to the communication session between the host VI and the KUKA youBot. You can wire this output to other KUKA youBot VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-robotics-module path=lvrobovi/youbot_pal.html language=enus -->
## TOPIC 00280: KUKA youBot VIs

- bundle_id: `labview-robotics-module`
- source_path: `lvrobovi/youbot_pal.html`
- source_url: https://docs-be.ni.com/bundle/labview-robotics-module/raw/resource/enus/lvrobovi/youbot_pal.html
- document_id: `labview-robotics-module`
- page_type: `leaf`
- content_type: ``

### KUKA youBot VIs

**Owning Palette:** [Robotics VIs](../lvrobovi/robotics_pal.html)

**Requires:** Robotics Module. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the KUKA youBot VIs to design and control a KUKA youBot.

[Example](#examples)

Refer to the KUKA website for more information about KUKA youBots.

| Palette Object | Description |
| --- | --- |
| Close KUKA youBot | Terminates the KUKA youBot host interface. |
| Initialize KUKA youBot | Initializes an EtherCAT host interface to a real KUKA youBot. |
| Initialize Simulated KUKA youBot | Initializes a simulation host interface to a simulated KUKA youBot. |

| Subpalette | Description |
| --- | --- |
| Arm VIs | Use the Arm VIs to configure KUKA youBot arms. |
| Platform VIs | Use the Platform VIs to configure the KUKA youBot platform. |

#### Example

Refer to the KUKA youBot.lvproj in the labview\examples\robotics\KUKA youBot directory for an example of using the KUKA youBot VIs.
