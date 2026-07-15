# NI DOCUMENT BUNDLE: labview-simulation-interface-toolkit-api-ref

<!--NI_BUNDLE_CHUNK bundle=labview-simulation-interface-toolkit-api-ref start=1 end=95 -->
<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/control_data_logging.html language=enus -->
## TOPIC 00001: Control Data Logging VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/control_data_logging.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/control_data_logging.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Control Data Logging VI

**Owning Palette:** [Data Logging VIs](../lvsit/mi_data_logging.html)

**Requires:** Simulation Interface Toolkit

[IMAGE alt='image' src='control_data_logging.gif']

|  | Simulation Data In specifies unique information about the model DLL. |
| --- | --- |
|  | Operation indicates whether to start, pause, or stop logging data in the simulation. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Simulation Data Out returns unique information about the model DLL. |
|  | error out contains error information. With the following exception, this output provides standard error out functionality. For Mobile and Touch Panel VIs, you cannot select Explain Error from the shortcut menu to receive more information about the error. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/control_file_playback.html language=enus -->
## TOPIC 00002: Control File Playback VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/control_file_playback.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/control_file_playback.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Control File Playback VI

**Owning Palette:** [File Playback VIs](../lvsit/mi_file_playback.html)

**Requires:** Simulation Interface Toolkit (Windows)

[IMAGE alt='image' src='control_file_playback.gif']

|  | Simulation Data In specifies unique information about the model DLL. |
| --- | --- |
|  | Operation specifies the playback action to take. 0Play—Begins playback of logged data.1Pause—Pauses playback of logged data.2Stop—Stops playback of logged data.3Rewind—Rewinds logged data. |
| 0 | Play—Begins playback of logged data. |
| 1 | Pause—Pauses playback of logged data. |
| 2 | Stop—Stops playback of logged data. |
| 3 | Rewind—Rewinds logged data. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Simulation Data Out returns unique information about the model DLL. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/get_data_logging_status.html language=enus -->
## TOPIC 00003: Get Data Logging Status VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/get_data_logging_status.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/get_data_logging_status.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Get Data Logging Status VI

**Owning Palette:** [Data Logging VIs](../lvsit/mi_data_logging.html)

**Requires:** Simulation Interface Toolkit

[IMAGE alt='image' src='get_data_logging_status.gif']

|  | Simulation Data In specifies unique information about the model DLL. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Simulation Data Out returns unique information about the model DLL. |
|  | Logging Status indicates the current status of data logging. |
|  | Active Log Configuration displays information about the currently active data log configuration including the configuration name and information about the individual logged signals. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | All Log Configurations lists all data log configurations set up to run on the target. You must create configurations before running the driver VI. You can enable any of the configurations listed here during run time. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/get_file_playbk_stat.html language=enus -->
## TOPIC 00004: Get File Playback Status VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/get_file_playbk_stat.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/get_file_playbk_stat.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Get File Playback Status VI

**Owning Palette:** [File Playback VIs](../lvsit/mi_file_playback.html)

**Requires:** Simulation Interface Toolkit (Windows)

[IMAGE alt='image' src='get_file_playback_status.gif']

|  | Simulation Data In specifies unique information about the model DLL. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Simulation Data Out returns unique information about the model DLL. |
|  | Playing Status indicates whether file playback is currently playing, paused, stopped, or disabled. |
|  | Active File Playback Configuration displays information about the currently active file playback configuration, including the configuration name and information about the individual playback channels. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | All File Playback Configurations lists all the file playback configurations set up to run on the target. You must create configurations before running the driver VI. You can enable any of the configurations listed here during run time. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/mi_data_logging.html language=enus -->
## TOPIC 00005: Data Logging VIs

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/mi_data_logging.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/mi_data_logging.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Data Logging VIs

**Owning Palette:** [Model Interface VIs](../lvsit/model_interface_vis.html)

**Requires:** Simulation Interface Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

|  | Note You must install the LabVIEW Real-Time Module in order to place these VIs on the block diagram. |
| --- | --- |

The VIs on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html) or [specific Simulation Interface Toolkit error codes](sit_error_codes.html).

| Palette Object | Description |
| --- | --- |
| Control Data Logging | Controls data logging during run time. This VI can start, pause, or stop data logging. |
| Get Data Logging Status | Returns current data logging status information, including whether data logging is enabled or disabled. This VI also returns all configurations set up to run on the target, as well as information about the active data log configuration. |
| Set Data Log Group Enabled State | Enables or disables a specified channel group in the data log file. Disabling a channel group stops logging for all channels in the channel group. This does not affect any previously logged data. Enabling a channel group resumes logging for all channels in the channel group. |
| SIT Log Continuously | Run this VI as a background task. If logging is enabled, this VI logs simulation data. This VI can log either all samples continuously, or only the last N time steps worth of data. |
| SIT Probe Data Log Signals | Probes the available signals in the model DLL and sends the signal data to the SIT Log Continuously VI for logging. |
| Specify Data Log Configuration | Specifies the data log configuration to use in the simulation. If the specified configuration does not exist, or if you specify a blank configuration name, this VI disables logging. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/mi_file_playback.html language=enus -->
## TOPIC 00006: File Playback VIs

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/mi_file_playback.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/mi_file_playback.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### File Playback VIs

**Owning Palette:** [Model Interface VIs](../lvsit/model_interface_vis.html)

**Requires:** Simulation Interface Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the File Playback VIs to configure playback from the driver VI.

|  | Note You must install the LabVIEW Real-Time Module in order to place these VIs on the block diagram. |
| --- | --- |

The VIs on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html) or [specific Simulation Interface Toolkit error codes](sit_error_codes.html).

| Palette Object | Description |
| --- | --- |
| Control File Playback | Controls playback during runtime, which replaces the model input values with data from the logged data you are replaying. This VI can set playback to play, pause, rewind, or stop. |
| Get File Playback Status | Gives current file playback status information, including whether file playback is playing, paused, stopped, or disabled. This VI also returns all the configurations set up to run on the target, as well as information about the active playback configuration. |
| Set File Playback Channel Enabled Status | Enables or disables the specified file playback channel. Disabling a channel stops playback for that channel into all its mapped model inputs. If you do not specify a channel name, this VI enables or disables all the channels in the specified channel group. If this VI does not find the channel name you specified in the group you specified, or if this VI does not find the group you specified, this VI takes no action. |
| SIT Read Replay FIFO | Reads values from the Replay FIFO and inserts them into the appropriate spots in the input array of the model. Use this VI in the IO Base Rate Loop VI. |
| SIT Replay From File | Run this VI as a background task. This VI reads the selected channel data from file and updates the Replay FIFO with the data. |
| Specify File Playback Configuration | Specifies the file playback configuration to use in the simulation. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/model_interface_vis.html language=enus -->
## TOPIC 00007: Model Interface VIs

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/model_interface_vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/model_interface_vis.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Model Interface VIs

**Owning Palette:** [Simulation Interface VIs](../lvsit/simulation_interface_vis.html)

**Requires:** Simulation Interface Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Model Interface VIs to create a [driver VI](../lvsitconcepts/sit_c_components_of_a_simulation.html#real_time_components). You also can use the [SIT Connection Manager](../lvsit/sit_connection_manager_db.html) dialog box to generate a driver VI.

|  | Note You must install the LabVIEW Real-Time Module in order to place these VIs on the block diagram. |
| --- | --- |

The VIs on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html) or [specific Simulation Interface Toolkit error codes](sit_error_codes.html).

| Palette Object | Description |
| --- | --- |
| SIT Configure Timing | Configures timing information for the simulation. If the simulation does not use a hardware timing source, this VI determines whether the simulation uses 1 kHz timing or 1 MHz timing. |
| SIT Control Simulation | Reads a real-time (RT) FIFO for commands from the host VI. |
| SIT Finalize Driver and Model | Finalizes the driver VI by finishing the logging, closing references and checking for errors. This VI also finalizes and unloads the model DLL. |
| SIT Finalize Model | Unloads the model DLL and notifies the SIT Server that the model DLL finished executing. You must use this VI after all model steps are complete. |
| SIT Initialize Driver and Wait for Start | Initializes the driver VI and starts running the simulation. This VI configures timing information and launches task loops for multirate simulations. |
| SIT Initialize Model | Loads the model DLL, initializes the model, registers the model with the SIT Server, and sets the final time. This VI returns the model time step and the number of input ports and output ports needed. You must call this VI before taking any model steps. |
| SIT Probe Signals | Probes the available signals in the model DLL and sends the signal data to the SIT Server. |
| SIT Resolve Model DLL Path | This VI resolves the path for the Model DLL you specify using Model DLL Path In. If the model is running on RT or you provide an absolute path to the Model DLL, this VI does not modify the path. If the model is running on a Windows system and you provide a relative path to the Model DLL, this VI qualifies that path using the directory of the Driver VI. |
| SIT Scheduler | Inserts the data from the model inputs array into the model DLL inputs, takes a single step of the model DLL, and sends the data from the model DLL outputs to the model outputs array. Use the SIT Initialize Model VI before executing any steps in the model DLL. Use the SIT Finalize Model VI when you finish executing all the steps in the model. |
| SIT Set Model Parameters | Sets a new parameter value in the model. The elements of non-scalars such as arrays can be set individually. The parameter you want to set is specified by its param index and subindex. |
| SIT Start Simulation | Starts the simulation. |
| SIT Take Model Time Step | Calls the model to advance it one time step. The model DLL calculates the new Model Outputs based on the Model Inputs and current state of the model. |
| SITs Server Loop | Manages the communication between the model and the Host VI. This VI handles requests from the Host VI to start and stop the model as well as to set parameters and probe signals. |

| Subpalette | Description |
| --- | --- |
| Data Logging VIs | Use the Data Logging VIs to configure data logging from the driver VI. |
| File Playback VIs | Use the File Playback VIs to configure playback from the driver VI. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/set_data_log_grp_enbl_st.html language=enus -->
## TOPIC 00008: Set Data Log Group Enabled State VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/set_data_log_grp_enbl_st.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/set_data_log_grp_enbl_st.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Set Data Log Group Enabled State VI

**Owning Palette:** [Data Logging VIs](../lvsit/mi_data_logging.html)

**Requires:** Simulation Interface Toolkit

[IMAGE alt='image' src='set_data_log_group_enabled_state.gif']

|  | Simulation Data In specifies unique information about the model DLL. |
| --- | --- |
|  | Channel Group Name specifies the name of the data log channel group you want to enable or disable. Disabling a channel group stops logging for all channels in the channel group. |
|  | Enabled specifies whether the channel group is enabled or disabled. If a channel group is disabled, logging stops for all channels in the channel group. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Simulation Data Out returns unique information about the model DLL. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/set_fl_plbk_chn_enbl_stat.html language=enus -->
## TOPIC 00009: Set File Playback Channel Enabled Status VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/set_fl_plbk_chn_enbl_stat.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/set_fl_plbk_chn_enbl_stat.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Set File Playback Channel Enabled Status VI

**Owning Palette:** [File Playback VIs](../lvsit/mi_file_playback.html)

**Requires:** Simulation Interface Toolkit (Windows)

[IMAGE alt='image' src='set_file_playback_channel_enabled_status.gif']

|  | Simulation Data In specifies unique information about the model DLL. |
| --- | --- |
|  | Channel Group Name specifies the name of the playback file channel group for the channel you specify. If you do not specify a channel name, this VI enables or disables all the channels in the specified channel group. |
|  | Channel Name specifies the name of the channel you want to enable or disable. Disabling a channel stops playback for that channel into all its mapped model inputs. If you do not specify a channel name, this VI enables or disables all the channels in the specified channel group. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Enabled specifies whether the channel or channel group is enabled or disabled. Disabling a channel stops playback for that channel into all its mapped model inputs. |
|  | Simulation Data Out returns unique information about the model DLL. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/simulation_interface_vis.html language=enus -->
## TOPIC 00010: Simulation Interface VIs

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/simulation_interface_vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/simulation_interface_vis.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Simulation Interface VIs

June 2010, 370421J-01

**Requires:** Simulation Interface Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the Simulation Interface VIs to create [host VIs](../lvsitconcepts/sit_c_components_of_a_simulation.html) and [driver VIs](../lvsitconcepts/sit_c_components_of_a_simulation.html) in LabVIEW. You also can generate host VIs and driver VIs using the [SIT Connection Manager](../lvsit/sit_connection_manager_db.html) dialog box.

The VIs on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html) or [specific Simulation Interface Toolkit error codes](sit_error_codes.html).

| Subpalette | Description |
| --- | --- |
| Model Interface VIs | Use the Model Interface VIs to create a driver VI. You also can use the SIT Connection Manager dialog box to generate a driver VI. |
| User Interface VIs | Use the User Interface VIs to create a host VI. You also can use the SIT Connection Manager dialog box to generate a host VI. |

© 2002–2010 National Instruments Corporation. All rights reserved.

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_close_simulation_vi.html language=enus -->
## TOPIC 00011: SIT Close Simulation VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_close_simulation_vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_close_simulation_vi.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Close Simulation VI

**Owning Palette:** [User Interface VIs](../lvsit/user_interface_vis.html)

**Requires:** Simulation Interface Toolkit

Closes the current connection to the [SIT Server](../lvsitconcepts/sit_c_components_of_a_simulation.html).

|  | Note This VI does not stop the simulation. If you want to stop the simulation before closing the connection to the SIT Server, you must run the SIT Run Pause Stop VI before running the SIT Close Simulation VI. |
| --- | --- |

[Example](#examples)

[IMAGE alt='image' src='sit_close_simulationc.gif']

|  | SIT Reference in specifies information about the current simulation. TCP Connection specifies the TCP reference for the current connection to the SIT Server. Model Name specifies the name of the current model. Server Type specifies the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| --- | --- |
|  | TCP Connection specifies the TCP reference for the current connection to the SIT Server. |
|  | Model Name specifies the name of the current model. |
|  | Server Type specifies the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| 0 | Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software. |
| 1 | MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option. |
| 2 | RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the batch simulation VI in the labview\examples\Simulation Interface\Batch Simulation directory for an example of using the SIT Close Simulation VI.

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_configure_timing_vi.html language=enus -->
## TOPIC 00012: SIT Configure Timing VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_configure_timing_vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_configure_timing_vi.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Configure Timing VI

**Owning Palette:** [Model Interface VIs](../lvsit/model_interface_vis.html)

**Requires:** Simulation Interface Toolkit

Configures timing information for the simulation. If the simulation does not use a hardware timing source, this VI determines whether the simulation uses 1 kHz timing or 1 MHz timing.

[IMAGE alt='image' src='sit_configure_timingc.gif']

|  | Simulation Data In specifies unique information about the model DLL. |
| --- | --- |
|  | Using Output Loop? is TRUE when the driver VI uses a separate output loop for multirate models. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Timing Source Type returns the type of software timing source that the simulation uses. If HW Timing Src is TRUE, this VI ignores the value of Timing Source Type. 01kHz (SW)— Specifies a timing source running at a rate of 1 kHz.11MHz (SW)—Specifies a timing source running at a rate of 1 MHz. |
| 0 | 1kHz (SW)— Specifies a timing source running at a rate of 1 kHz. |
| 1 | 1MHz (SW)—Specifies a timing source running at a rate of 1 MHz. |
|  | Simulation Data out returns unique information about the model DLL. |
|  | Timed Loop Names returns the names of any Timed Loops that this VI uses to configure the simulation. |
|  | Timed Loops Config out returns timing information about any Timed Loops this VI uses to configure the simulation. If you are running a single-rate simulation, tloops out is an array consisting of one element. Task returns a number that uniquely identifies the task. Source returns the name of the timing source for Task. Period returns the sample period of Task. The sample period defines the deadline, or the time limit in which Task must finish operating. Offset returns the offset for the execution of Task. The offset delays the execution of the selected task by the specified time period. Priority returns the priority of Task relative to other tasks in the model. The LabVIEW Simulation Interface Toolkit uses rate-monotonic scheduling, which prioritizes tasks with shorter periods over tasks with longer periods. Name returns the name of Task. |
|  | Task returns a number that uniquely identifies the task. |
|  | Source returns the name of the timing source for Task. |
|  | Period returns the sample period of Task. The sample period defines the deadline, or the time limit in which Task must finish operating. |
|  | Offset returns the offset for the execution of Task. The offset delays the execution of the selected task by the specified time period. |
|  | Priority returns the priority of Task relative to other tasks in the model. The LabVIEW Simulation Interface Toolkit uses rate-monotonic scheduling, which prioritizes tasks with shorter periods over tasks with longer periods. |
|  | Name returns the name of Task. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_control_simulation_vi.html language=enus -->
## TOPIC 00013: SIT Control Simulation VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_control_simulation_vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_control_simulation_vi.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Control Simulation VI

**Owning Palette:** [Model Interface VIs](../lvsit/model_interface_vis.html)

**Requires:** Simulation Interface Toolkit

Reads a real-time (RT) FIFO for commands from the [host VI](../lvsitconcepts/sit_c_components_of_a_simulation.html).

[IMAGE alt='image' src='sit_control_simulationc.gif']

|  | Simulation Data In specifies unique information about the model DLL. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Simulation Data out returns unique information about the model DLL. |
|  | command returns the most recent command the host VI sent. 0No Operation (default)—Indicates the host VI did not send a command to the simulation.1Run Simulation—Indicates the host VI sent a run command to the simulation.2Pause Simulation—Indicates the host VI sent a pause command to the simulation.3Stop Simulation—Indicates the host VI sent a stop command to the simulation. |
| 0 | No Operation (default)—Indicates the host VI did not send a command to the simulation. |
| 1 | Run Simulation—Indicates the host VI sent a run command to the simulation. |
| 2 | Pause Simulation—Indicates the host VI sent a pause command to the simulation. |
| 3 | Stop Simulation—Indicates the host VI sent a stop command to the simulation. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_ctrl_data_log.html language=enus -->
## TOPIC 00014: SIT Control Data Logging VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_ctrl_data_log.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_ctrl_data_log.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Control Data Logging VI

**Owning Palette:** [Data Logging VIs](../lvsit/ui_data_logging.html)

**Requires:** Simulation Interface Toolkit (Windows)

[IMAGE alt='image' src='sit_control_data_logging.gif']

|  | SIT Reference in specifies information about the current simulation. TCP Connection specifies the TCP reference for the current connection to the SIT Server. Model Name specifies the name of the current model. Server Type specifies the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| --- | --- |
|  | TCP Connection specifies the TCP reference for the current connection to the SIT Server. |
|  | Model Name specifies the name of the current model. |
|  | Server Type specifies the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| 0 | Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software. |
| 1 | MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option. |
| 2 | RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | Operation indicates whether to start, pause, or stop logging data in the simulation. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | SIT Reference out returns information about the current simulation. TCP Connection returns the TCP reference for the current connection to the SIT Server. Model Name returns the name of the current model. Server Type returns the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | TCP Connection returns the TCP reference for the current connection to the SIT Server. |
|  | Model Name returns the name of the current model. |
|  | Server Type returns the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| 0 | Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software. |
| 1 | MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option. |
| 2 | RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_enable_replay.html language=enus -->
## TOPIC 00015: SIT Control File Playback VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_enable_replay.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_enable_replay.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Control File Playback VI

**Owning Palette:** [File Playback VIs](../lvsit/ui_file_playback.html)

**Requires:** Simulation Interface Toolkit

Enables playback during runtime.

[IMAGE alt='image' src='sit_control_file_playback.gif']

|  | SIT Reference in specifies information about the current simulation. TCP Connection specifies the TCP reference for the current connection to the SIT Server. Model Name specifies the name of the current model. Server Type specifies the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| --- | --- |
|  | TCP Connection specifies the TCP reference for the current connection to the SIT Server. |
|  | Model Name specifies the name of the current model. |
|  | Server Type specifies the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| 0 | Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software. |
| 1 | MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option. |
| 2 | RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | Operation specifies the playback action to take. 0Play—Begins playback of logged data.1Pause—Pauses playback of logged data.2Stop—Stops playback of logged data.3Rewind—Rewinds logged data. |
| 0 | Play—Begins playback of logged data. |
| 1 | Pause—Pauses playback of logged data. |
| 2 | Stop—Stops playback of logged data. |
| 3 | Rewind—Rewinds logged data. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | SIT Reference out returns information about the current simulation. TCP Connection returns the TCP reference for the current connection to the SIT Server. Model Name returns the name of the current model. Server Type returns the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | TCP Connection returns the TCP reference for the current connection to the SIT Server. |
|  | Model Name returns the name of the current model. |
|  | Server Type returns the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| 0 | Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software. |
| 1 | MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option. |
| 2 | RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_error_codes.html language=enus -->
## TOPIC 00016: Error Codes (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_error_codes.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_error_codes.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Error Codes (Simulation Interface Toolkit)

The [Simulation Interface VIs](../lvsit/simulation_interface_vis.html) and dialog boxes can return the following error codes. Refer to the KnowledgeBase for more information about correcting errors in LabVIEW.

| Code | Description |
| --- | --- |
| 14104 | The model DLL failed to load. The specified path might be invalid, or the specified file is not a valid model DLL. Select Tools»SIT Connection Manager from the pull-down menu to launch the SIT Connection Manager dialog box and specify a valid model DLL. |
| 14105 | The model DLL is not compatible with the current version of SIT. You must rebuild the model DLL with the current version of SIT before you can use the model DLL. |
| 14106 | The execution host reported an error. |
| 14107 | Could not create the data logging file. The specified filename might be invalid. Select Tools»SIT Connection Manager to display the SIT Connection Manager dialog box. Under Data Logging, select the data log configuration page and enter a valid filename in the Data Log Filename field . |
| 14108 | Cannot probe some signals. The signals might not exist in the model. |
| 14109 | The model failed to receive expected model input data in time. |
| 14110 | TDMS data logging only supports fixed-step solvers. Switch to a fixed-step solver, disable data logging, or log data as text to resolve this error. |
| 14112 | The TDMS playback file could not be found at the specified location. Select Tools»SIT Connection Manager to launch the SIT Connection Manager dialog box and specify a valid TDMS playback file path on the File Playback configuration page. |
| 14113 | The version of the SIT Server and the version of the client are not compatible. |
| 14119 | An error occurred in the model DLL. |
| 14120 | The base rate loop did not finish in time. The combined time of computing the model and performing input and output is too long. Increase the model time step, switch to a simpler solver, or reduce the number of inputs and outputs used. |
| 14121 | One or more simulation model tasks did not finish in time. The combined time of computing the task and higher priority tasks in the model, together with performing input and output, is too long. Increase the model time step, switch to a simpler solver, or reduce the number of inputs and outputs used. |
| 14131 | Data loss occurred while logging data. The background loop did not have enough time to process the data in the logging buffer. To help avoid future data loss, try reducing the number of signals to log or increasing the logging decimation for these channels. You also can choose to log only the last N samples to achieve lossless data logging. |
| 14132 | The logging configuration data does not match the logging configuration data used to create the log file. The specified channel is new, but belongs to a channel group that already contains time channel data. The time channel values will not correspond to the specified channel. To avoid this issue, use unique filenames for each data log configuration, or do not use the same channel group name in separate data log configurations that share a file. |
| 14151 | Microsecond timing is not enabled. Microsecond timing allows the National Instruments Scheduler to take advantage of the microsecond timing source. Complete the following steps to enable microsecond timing. 1. Open an FTP connection to the real-time (RT) target and download the c:\\ni-rt.ini file to the host. 2. Edit the ni-rt.ini file and locate the MicrosecondTimingMode key under the [SYSTEMSETTINGS] section. Change the value of this key from 0 to 1. 3. Save ni-rt.ini to the host, upload the saved file back to the RT target, and reboot the RT target. |
| 14152 | File transfer failed for model DLL. An error occurred in the attempt to FTP the model DLL to the RT target. A possible reason for this is a permissions conflict on the target. |
| 14153 | An error occurred while attempting to deploy the driver project and VI, or the operation was cancelled by the user. Verify that you are using the correct IP address, the target is turned on, and the Target Access permissions are set correctly. |
| 14154 | The server type specified by the client and the server type of the SIT Server do not match. For example, the client VI might be expecting a SIT driver VI, but the server is already running in the simulation environment with the same port number. If the intended execution host is the simulation environment, ensure there are no SIT driver VIs running. If the intended server is a driver VI on Localhost, ensure that the SIT Server is not running in the simulation environment on the local machine. If the intended server is a RT target, ensure that the IP address specifies a LabVIEW Real-Time Target. You can either stop the other SIT Server or use a different port number. |
| 14155 | Data loss occurred between the SIT Server and the host VI. Refer to the Halting Simulations on Data Loss topic of the LabVIEW Help for information about reducing the possibility of data loss. |
| 14156 | The specified driver VI name does not match the SIT naming conventions. Driver VIs must be named modelname_Driver.vi, where modelname is the name of the model the driver VI is configured to run. |
| 14160 | The driver VI was created in a previous version of SIT. You must update the driver VI before it can be rebuilt. |
| 14161 | An I/O plugin attempted to add an invalid channel name. Channel names within a device cannot be duplicated, and should not start or end with whitespace. |
| 14198 | The communication settings in the configured host VI are invalid. You have specified to not launch the SIT Connection Manager dialog box to modify these settings. |
| 14199 | The communication settings in the configured host VI are invalid. You have specified to launch the SIT Connection Manager dialog box to modify these settings. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_finalize_driver_and_model_vi.html language=enus -->
## TOPIC 00017: SIT Finalize Driver and Model VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_finalize_driver_and_model_vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_finalize_driver_and_model_vi.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Finalize Driver and Model VI

**Owning Palette:** [Model Interface VIs](../lvsit/model_interface_vis.html)

**Requires:** Simulation Interface Toolkit

Finalizes the driver VI by finishing the logging, closing references and checking for errors. This VI also finalizes and unloads the model DLL.

[IMAGE alt='image' src='sit_finalize_driver_and_model.gif']

|  | Simulation Data In specifies unique information about the model DLL. |
| --- | --- |
|  | scheduler overrun? is TRUE if the Scheduler Loop did not finish executing before its deadline. You specify the deadline for a task when you build a model in The MathWorks, Inc. Simulink® application software. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | logfile refnum (Deprecated) contains the file format type and file refnum for the data log file. This output is no longer relevant for the Driver VI. It is only a placeholder for SIT 3.0.x Driver VIs. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_finalize_model.html language=enus -->
## TOPIC 00018: SIT Finalize Model VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_finalize_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_finalize_model.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Finalize Model VI

**Owning Palette:** [Model Interface VIs](../lvsit/model_interface_vis.html)

**Requires:** Simulation Interface Toolkit

Unloads the [model DLL](../lvsitconcepts/sit_c_components_of_a_simulation.html#real_time_components) and notifies the [SIT Server](../lvsitconcepts/sit_c_components_of_a_simulation.html) that the model DLL finished executing. You must use this VI after all model steps are complete.

Use the [SIT Initialize Model](../lvsit/sit_initialize_model.html) VI to load the model DLL so you can begin executing the simulation model.

[IMAGE alt='image' src='sit_finalize_modelc.gif']

|  | Simulation Data In specifies unique information about the model DLL. |
| --- | --- |
|  | unload library? is TRUE if you want to unload the model DLL. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_get_data_log_stat.html language=enus -->
## TOPIC 00019: SIT Get Data Logging Status VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_get_data_log_stat.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_get_data_log_stat.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Get Data Logging Status VI

**Owning Palette:** [Data Logging VIs](../lvsit/ui_data_logging.html)

**Requires:** Simulation Interface Toolkit (Windows)

[IMAGE alt='image' src='sit_get_data_logging_status.gif']

|  | SIT Reference in specifies information about the current simulation. TCP Connection specifies the TCP reference for the current connection to the SIT Server. Model Name specifies the name of the current model. Server Type specifies the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| --- | --- |
|  | TCP Connection specifies the TCP reference for the current connection to the SIT Server. |
|  | Model Name specifies the name of the current model. |
|  | Server Type specifies the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| 0 | Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software. |
| 1 | MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option. |
| 2 | RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | SIT Reference out returns information about the current simulation. TCP Connection returns the TCP reference for the current connection to the SIT Server. Model Name returns the name of the current model. Server Type returns the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | TCP Connection returns the TCP reference for the current connection to the SIT Server. |
|  | Model Name returns the name of the current model. |
|  | Server Type returns the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| 0 | Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software. |
| 1 | MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option. |
| 2 | RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | Logging Status indicates the current status of data logging. |
|  | Active Log Configuration displays information about the currently active data log configuration including the configuration name and information about the individual logged signals. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | All Log Configurations lists all data log configurations set up to run on the target. You must create configurations before running the driver VI. You can enable any of the configurations listed here during run time. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_get_file_plybk_stat.html language=enus -->
## TOPIC 00020: SIT Get File Playback Status VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_get_file_plybk_stat.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_get_file_plybk_stat.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Get File Playback Status VI

**Owning Palette:** [File Playback VIs](../lvsit/ui_file_playback.html)

**Requires:** Simulation Interface Toolkit

[IMAGE alt='image' src='sit_get_file_playback_status.gif']

|  | SIT Reference in specifies information about the current simulation. TCP Connection specifies the TCP reference for the current connection to the SIT Server. Model Name specifies the name of the current model. Server Type specifies the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| --- | --- |
|  | TCP Connection specifies the TCP reference for the current connection to the SIT Server. |
|  | Model Name specifies the name of the current model. |
|  | Server Type specifies the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| 0 | Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software. |
| 1 | MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option. |
| 2 | RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | SIT Reference out returns information about the current simulation. TCP Connection returns the TCP reference for the current connection to the SIT Server. Model Name returns the name of the current model. Server Type returns the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | TCP Connection returns the TCP reference for the current connection to the SIT Server. |
|  | Model Name returns the name of the current model. |
|  | Server Type returns the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| 0 | Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software. |
| 1 | MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option. |
| 2 | RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | Playing Status indicates whether file playback is currently playing, paused, stopped, or disabled. |
|  | Active Configuration displays information about the currently active file playback configuration including the configuration name and information about the individual playback channels. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | Configuration Names lists all file playback configurations set up to run on the target. You must create configurations before running the driver VI. You can enable any of the configurations listed here during run-time. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_get_parameter_vi.html language=enus -->
## TOPIC 00021: SIT Get Parameter VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_get_parameter_vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_get_parameter_vi.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Get Parameter VI

**Owning Palette:** [User Interface VIs](../lvsit/user_interface_vis.html)

**Requires:** Simulation Interface Toolkit

Returns the value of a [model](../lvsitconcepts/sit_c_components_of_a_simulation.html) parameter you specify.

[IMAGE alt='image' src='sit_get_parameterc.gif']

|  | SIT Reference in specifies information about the current simulation. TCP Connection specifies the TCP reference for the current connection to the SIT Server. Model Name specifies the name of the current model. Server Type specifies the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| --- | --- |
|  | TCP Connection specifies the TCP reference for the current connection to the SIT Server. |
|  | Model Name specifies the name of the current model. |
|  | Server Type specifies the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| 0 | Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software. |
| 1 | MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option. |
| 2 | RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | Parameter Name specifies the path to a model parameter. You must format Parameter Name with the following syntax: modelname/subsystem1/subsystem2/subsystemN/Block/Parameter For example, if you want to manipulate the Amplitude parameter of the Sine Wave block in a model named sinewave, format Parameter Name as sinewave/Sine Wave/Amplitude. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | SIT Reference out returns information about the current simulation. TCP Connection returns the TCP reference for the current connection to the SIT Server. Model Name returns the name of the current model. Server Type returns the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | TCP Connection returns the TCP reference for the current connection to the SIT Server. |
|  | Model Name returns the name of the current model. |
|  | Server Type returns the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| 0 | Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software. |
| 1 | MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option. |
| 2 | RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | Parameter Value returns the value of the parameter you specify in the Parameter Name control. Parameter Value always returns a two-dimensional array of double-precision floating-point numbers. If the value is a scalar or a vector, use the Index Array function to convert Parameter Value into the necessary form. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_get_sim_state.html language=enus -->
## TOPIC 00022: SIT Get Simulation State VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_get_sim_state.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_get_sim_state.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Get Simulation State VI

**Owning Palette:** [User Interface VIs](../lvsit/user_interface_vis.html)

**Requires:** Simulation Interface Toolkit

Returns the current status of the simulation.

[Example](#examples)

[IMAGE alt='image' src='sit_get_simulation_statec.gif']

|  | SIT Reference in specifies information about the current simulation. TCP Connection specifies the TCP reference for the current connection to the SIT Server. Model Name specifies the name of the current model. Server Type specifies the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| --- | --- |
|  | TCP Connection specifies the TCP reference for the current connection to the SIT Server. |
|  | Model Name specifies the name of the current model. |
|  | Server Type specifies the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| 0 | Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software. |
| 1 | MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option. |
| 2 | RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | SIT Reference out returns information about the current simulation. TCP Connection returns the TCP reference for the current connection to the SIT Server. Model Name returns the name of the current model. Server Type returns the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | TCP Connection returns the TCP reference for the current connection to the SIT Server. |
|  | Model Name returns the name of the current model. |
|  | Server Type returns the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| 0 | Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software. |
| 1 | MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option. |
| 2 | RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | State returns the current status of the simulation. 0Default (default)—Specifies that this VI could not determine the state of the simulation.1Idle—Specifies that the simulation loaded but is not running.2Running—Specifies that the simulation is running.3Paused—Specifies that the simulation is paused.4Stopped—Specifies that the simulation is stopped.5Error—Specifies that an error occurred during the simulation. |
| 0 | Default (default)—Specifies that this VI could not determine the state of the simulation. |
| 1 | Idle—Specifies that the simulation loaded but is not running. |
| 2 | Running—Specifies that the simulation is running. |
| 3 | Paused—Specifies that the simulation is paused. |
| 4 | Stopped—Specifies that the simulation is stopped. |
| 5 | Error—Specifies that an error occurred during the simulation. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the updatingindicators VI in the labview\examples\Simulation Interface\Updating Indicators directory for an example of using the SIT Get Simulation State VI.

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_initialize_model.html language=enus -->
## TOPIC 00023: SIT Initialize Model VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_initialize_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_initialize_model.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Initialize Model VI

**Owning Palette:** [Model Interface VIs](../lvsit/model_interface_vis.html)

**Requires:** Simulation Interface Toolkit

Loads the [model DLL](../lvsitconcepts/sit_c_components_of_a_simulation.html#real_time_components), initializes the [model](../lvsitconcepts/sit_c_components_of_a_simulation.html), registers the model with the [SIT Server](../lvsitconcepts/sit_c_components_of_a_simulation.html), and sets the final time. This VI returns the model time step and the number of input ports and output ports needed. You must call this VI before taking any model steps.

Use the [SIT Finalize Model](../lvsit/sit_finalize_model.html) VI to unload the model DLL when you finish executing the model.

[IMAGE alt='image' src='sit_initialize_modelc.gif']

|  | Buffer Sizes specifies the sizes of the buffers that the SIT Server uses to communicate with real-time (RT) targets. number of signals specifies the maximum number of model signals that you can probe. The default value is 50. circular buffer size specifies the depth of the buffer. The default value is 1000. num data points specifies the width of the buffer. The default value is 100. The total width of all the signals you probe in one time step must be less than or equal to num data points. The width of a signal is equal to the number of elements in that signal. For example, the width of a 2×2 array is 4. Note num data points has a large impact on the performance of the SIT Server. To ensure that the LabVIEW Simulation Interface Toolkit does not allocate more buffer space than necessary, set num data points to the lowest possible value. |
| --- | --- |
|  | number of signals specifies the maximum number of model signals that you can probe. The default value is 50. |
|  | circular buffer size specifies the depth of the buffer. The default value is 1000. |
|  | num data points specifies the width of the buffer. The default value is 100. The total width of all the signals you probe in one time step must be less than or equal to num data points. The width of a signal is equal to the number of elements in that signal. For example, the width of a 2×2 array is 4. Note num data points has a large impact on the performance of the SIT Server. To ensure that the LabVIEW Simulation Interface Toolkit does not allocate more buffer space than necessary, set num data points to the lowest possible value. |
|  | Note num data points has a large impact on the performance of the SIT Server. To ensure that the LabVIEW Simulation Interface Toolkit does not allocate more buffer space than necessary, set num data points to the lowest possible value. |
|  | path to model DLL specifies the path to the model DLL on the RT target. |
|  | stop time specifies the simulated time in seconds after which the model DLL terminates. If you wire -1 to the stop time, the model DLL does not terminate until you stop the VI. The default value is -1. |
|  | time step returns the simulated time increment, in seconds, for each step of the model DLL during execution. |
|  | Server On? is TRUE if you can start the SIT Server. Server On? is FALSE if you cannot start the SIT Server. The default value is TRUE. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | base period returns the base time step of the simulation, in microseconds. |
|  | Simulation Data out returns unique information about the model DLL. |
|  | number of model inputs returns the number of inputs to the model DLL. |
|  | number of model outputs returns the number of outputs from the model DLL. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | Signal Info returns information about the signals in the model DLL that you can probe. You must create a mapping for a signal in order to probe that signal. Index returns the index number of the signal. ID returns a unique string that identifies the signal. Block Name returns the path of the signal, for example, sinewave/Sine Wave. Port Number returns the port number of the signal. Signal Name returns the user-defined name of the signal. Data Type returns the data type of the signal. Dimensions returns the dimensions of the signal. |
|  | Index returns the index number of the signal. |
|  | ID returns a unique string that identifies the signal. |
|  | Block Name returns the path of the signal, for example, sinewave/Sine Wave. |
|  | Port Number returns the port number of the signal. |
|  | Signal Name returns the user-defined name of the signal. |
|  | Data Type returns the data type of the signal. |
|  | Dimensions returns the dimensions of the signal. |
|  | Param Info returns information about the parameters in the model DLL that you can manipulate. You must create a mapping for a parameter in order to manipulate that parameter. paramidx returns the index of the parameter. ID returns a unique string that identifies the parameter. paramname returns the path of the parameter, for example, sinewave/Sine Wave/Amplitude. datatype returns the data type of the parameter. Dimensions returns the dimensions of the parameter. value returns the current value of the parameter. |
|  | paramidx returns the index of the parameter. |
|  | ID returns a unique string that identifies the parameter. |
|  | paramname returns the path of the parameter, for example, sinewave/Sine Wave/Amplitude. |
|  | datatype returns the data type of the parameter. |
|  | Dimensions returns the dimensions of the parameter. |
|  | value returns the current value of the parameter. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_initialize_sim.html language=enus -->
## TOPIC 00024: SIT Initialize Simulation VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_initialize_sim.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_initialize_sim.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Initialize Simulation VI

**Owning Palette:** [User Interface VIs](../lvsit/user_interface_vis.html)

**Requires:** Simulation Interface Toolkit

Initializes the [host VI](../lvsitconcepts/sit_c_components_of_a_simulation.html) by creating a connection to the [execution host](../lvsitconcepts/sit_c_components_of_a_simulation.html) on which the [SIT Server](../lvsitconcepts/sit_c_components_of_a_simulation.html) is running. This VI also opens all the necessary models that the host VI specifies.

[Example](#examples)

[IMAGE alt='image' src='sit_initialize_simulationc.gif']

|  | Project Directory specifies the path to the directory that contains the data logging and file playback configuration files. |
| --- | --- |
|  | Model Path specifies the path to the model. |
|  | hostname specifies the name of the computer on which the SIT Server is running. The default value is localhost. |
|  | port specifies the TCP/IP port on hostname on which the SIT Server is running. The default is 6011. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Path to Driver VI specifies the local path to the driver VI you want to download to the real-time (RT) target. Note Wire a value to this input only when you download the simulation model to an RT target. |
|  | Note Wire a value to this input only when you download the simulation model to an RT target. |
|  | Path to Model DLL specifies the local path to the model DLL you want to download to an RT target. Note Wire a value to this input only when you download the simulation model to an RT target. |
|  | Note Wire a value to this input only when you download the simulation model to an RT target. |
|  | SIT Reference out returns information about the current simulation. TCP Connection returns the TCP reference for the current connection to the SIT Server. Model Name returns the name of the current model. Server Type returns the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | TCP Connection returns the TCP reference for the current connection to the SIT Server. |
|  | Model Name returns the name of the current model. |
|  | Server Type returns the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| 0 | Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software. |
| 1 | MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option. |
| 2 | RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the batch simulation VI in the labview\examples\Simulation Interface\Batch Simulation directory for an example of using the SIT Initialize Simulation VI.

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_intialize_driver_and_wait_for_start_vi.html language=enus -->
## TOPIC 00025: SIT Initialize Driver and Wait for Start VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_intialize_driver_and_wait_for_start_vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_intialize_driver_and_wait_for_start_vi.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Initialize Driver and Wait for Start VI

**Owning Palette:** [Model Interface VIs](../lvsit/model_interface_vis.html)

**Requires:** Simulation Interface Toolkit

Initializes the driver VI and starts running the simulation. This VI configures timing information and launches task loops for multirate simulations.

By default, this VI waits for a start command from the [host VI](../lvsitconcepts/sit_c_components_of_a_simulation.html) before starting the simulation.

[IMAGE alt='image' src='sit_intialize_driver_and_wait_for_start.gif']

|  | Simulation Data in specifies unique information about the model. |
| --- | --- |
|  | Task Loops Processor specifies the processor on which to run the task loops for multirate simulations. You must specify a number between 0 and 255. The default is 0. Note You cannot specify -2 for this input because automatic processor selection interferes with the scheduling of the model tasks. |
|  | Note You cannot specify -2 for this input because automatic processor selection interferes with the scheduling of the model tasks. |
|  | Wait for Start Command specifies whether to wait for a start command from the host VI before starting the simulation. The default is TRUE. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Simulation Data Out returns unique information about the model DLL. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_log_continuously_vi.html language=enus -->
## TOPIC 00026: SIT Log Continuously VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_log_continuously_vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_log_continuously_vi.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Log Continuously VI

**Owning Palette:** [Data Logging VIs](../lvsit/mi_data_logging.html)

**Requires:** Simulation Interface Toolkit

Run this VI as a background task. If logging is enabled, this VI logs simulation data. This VI can log either all samples continuously, or only the last *N* time steps worth of data.



Set the **Last Run** control to TRUE on the last iteration of the loop containing this VI to flush the remaining data in the log data buffer to file.

[IMAGE alt='image' src='sit_log_continuously.gif']

|  | Simulation Data in specifies unique information about the model. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Last Run specifies to send no more data to the Base Rate Loop. Set this control to TRUE on the last iteration of the loop containing this VI. |
|  | Simulation Data out returns unique information about the model DLL. |
|  | Logfile Refnum (Deprecated) contains the file format type and file refnum for the data log file. This output is no longer relevant for the Driver VI. It is only a placeholder for SIT 3.0.x Driver VIs. |
|  | TCL Active indicates whether the Base Rate Loop is active. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | Loop Shut Down indicates whether the logging operation is complete. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_model_error.html language=enus -->
## TOPIC 00027: SIT Model Error VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_model_error.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_model_error.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Model Error VI

**Owning Palette:** [User Interface VIs](../lvsit/user_interface_vis.html)

**Requires:** Simulation Interface Toolkit

Receives errors specific to the [model DLL](../lvsitconcepts/sit_c_components_of_a_simulation.html#real_time_components) and reports these errors to the [host VI](../lvsitconcepts/sit_c_components_of_a_simulation.html).

[IMAGE alt='image' src='sit_model_errorc.gif']

|  | Simulation Data In specifies unique information about the model DLL. |
| --- | --- |
|  | Scheduler Loop Overrun? is TRUE if the Scheduler Loop did not finish executing before its deadline. You specify the deadline for a task when you build a model in The MathWorks, Inc. Simulink® application software. |
|  | Single rate? is TRUE if the model is a single-rate model. Single rate? is FALSE if the model is a multirate model. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Simulation Data out returns unique information about the model DLL. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_probe_data_log_signals.html language=enus -->
## TOPIC 00028: SIT Probe Data Log Signals VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_probe_data_log_signals.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_probe_data_log_signals.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Probe Data Log Signals VI

**Owning Palette:** [Data Logging VIs](../lvsit/mi_data_logging.html)

**Requires:** Simulation Interface Toolkit

Probes the available signals in the [model DLL](../lvsitconcepts/sit_c_components_of_a_simulation.html#real_time_components) and sends the signal data to the [SIT Log Continuously](../lvsit/sit_log_continuously_vi.html) VI for logging.

[IMAGE alt='image' src='sit_probe_data_log_signalsc.gif']

|  | Simulation Data specifies unique information about the model DLL. |
| --- | --- |
|  | Time specifies the current simulation time that the SIT Scheduler VI returns. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Simulation Data out returns unique information about the model DLL. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_probe_signals_vi.html language=enus -->
## TOPIC 00029: SIT Probe Signals VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_probe_signals_vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_probe_signals_vi.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Probe Signals VI

**Owning Palette:** [Model Interface VIs](../lvsit/model_interface_vis.html)

**Requires:** Simulation Interface Toolkit

Probes the available signals in the [model DLL](../lvsitconcepts/sit_c_components_of_a_simulation.html#real_time_components) and sends the signal data to the [SIT Server](../lvsitconcepts/sit_c_components_of_a_simulation.html).

[IMAGE alt='image' src='sit_probe_signalsc.gif']

|  | Simulation Data In specifies unique information about the model DLL. |
| --- | --- |
|  | Time specifies the current simulation time that the SIT Scheduler VI returns. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Simulation Data out returns unique information about the model DLL. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_read.html language=enus -->
## TOPIC 00030: SIT Read VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_read.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_read.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Read VI

**Owning Palette:** [User Interface VIs](../lvsit/user_interface_vis.html)

**Requires:** Simulation Interface Toolkit

Reads data from all probed [model signals](../lvsitconcepts/sit_c_components_of_a_simulation.html).

[Example](#examples)

[IMAGE alt='image' src='sit_readc.gif']

|  | SIT Reference in specifies information about the current simulation. TCP Connection specifies the TCP reference for the current connection to the SIT Server. Model Name specifies the name of the current model. Server Type specifies the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| --- | --- |
|  | TCP Connection specifies the TCP reference for the current connection to the SIT Server. |
|  | Model Name specifies the name of the current model. |
|  | Server Type specifies the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| 0 | Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software. |
| 1 | MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option. |
| 2 | RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | SIT Reference out returns information about the current simulation. TCP Connection returns the TCP reference for the current connection to the SIT Server. Model Name returns the name of the current model. Server Type returns the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | TCP Connection returns the TCP reference for the current connection to the SIT Server. |
|  | Model Name returns the name of the current model. |
|  | Server Type returns the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| 0 | Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software. |
| 1 | MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option. |
| 2 | RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | Raw Data returns the values and dimensions of all probed signals. Data returns the values of all probed signals. Dimensions returns the dimensions of all probed signals. Each element pair specifies the length and width of a signal. |
|  | Data returns the values of all probed signals. |
|  | Dimensions returns the dimensions of all probed signals. Each element pair specifies the length and width of a signal. |
|  | Valid Data? is TRUE if the simulation returned valid data. If Valid Data? is FALSE, the simulation might not have provided any new signal values. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | Model Running? returns TRUE if the simulation is running. Model Running? returns FALSE if the simulation is either paused or stopped. You can use the SIT Get Simulation State VI to determine the state of the simulation. |

#### Example

Refer to the batch simulation VI in the labview\examples\Simulation Interface\Batch Simulation directory for an example of using the SIT Read VI.

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_read_replay_fifo.html language=enus -->
## TOPIC 00031: SIT Read Replay FIFO VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_read_replay_fifo.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_read_replay_fifo.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Read Replay FIFO VI

**Owning Palette:** [File Playback VIs](../lvsit/mi_file_playback.html)

**Requires:** Simulation Interface Toolkit

IO Base Rate Loop VI

[IMAGE alt='image' src='sit_read_replay_fifoc.gif']

|  | Simulation Data specifies unique information about the model DLL. |
| --- | --- |
|  | Input Values (in) is the array of input values contained in the presized input array element of the Simulation Data cluster. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Simulation Data Out returns unique information about the model DLL. |
|  | Input Values (out) returns the array of input values this VI reads from the Replay FIFO. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_replay_from_file_vi.html language=enus -->
## TOPIC 00032: SIT Replay From File VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_replay_from_file_vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_replay_from_file_vi.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Replay From File VI

**Owning Palette:** [File Playback VIs](../lvsit/mi_file_playback.html)

**Requires:** Simulation Interface Toolkit

Run this VI as a background task. This VI reads the selected channel data from file and updates the Replay FIFO with the data.

Use the [SIT Read Replay FIFO](../lvsit/sit_read_replay_fifo.html) VI in the [I/O Base Rate Loop VI](../lvsitconcepts/sit_c_understanding_the_driver_vi.html#blockdiagram) to read the channel data from the Replay FIFO and insert the values into the appropriate place in the input array.

[IMAGE alt='image' src='sit_replay_from_file.gif']

|  | Simulation Data In specifies unique information about the model DLL. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Last Run specifies to send no more data to the Base Rate Loop. Set this control to TRUE on the last iteration of the loop containing this VI. |
|  | Simulation Data out returns unique information about the model DLL. |
|  | TCL Active indicates whether the Base Rate Loop is active. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | Loop Shut Down indicates whether the playback operation is complete. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_resolve_model_dll_path_vi.html language=enus -->
## TOPIC 00033: SIT Resolve Model DLL Path VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_resolve_model_dll_path_vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_resolve_model_dll_path_vi.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Resolve Model DLL Path VI

**Owning Palette:** [Model Interface VIs](../lvsit/model_interface_vis.html)

**Requires:** Simulation Interface Toolkit

This VI resolves the path for the Model DLL you specify using **Model DLL Path In**. If the model is running on RT or you provide an absolute path to the Model DLL, this VI does not modify the path. If the model is running on a Windows system and you provide a relative path to the Model DLL, this VI qualifies that path using the directory of the Driver VI.



If a client deploys this model and the model is running on RT, the client copies the Model DLL to the ni-rt\system folder on the RT target. That folder is in the default search path for shared libraries, so an absolute path is not necessary.

[IMAGE alt='image' src='sit_resolve_model_dll_path.gif']

|  | Model DLL Path In is the absolute or relative path to the Model DLL. |
| --- | --- |
|  | Driver VI Path is the path to the top-level Driver VI. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Resolved Model DLL Path specifies either the input path if absolute, or the resolved relative path to the Model DLL. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_run_pause_stop.html language=enus -->
## TOPIC 00034: SIT Run Pause Stop VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_run_pause_stop.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_run_pause_stop.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Run Pause Stop VI

**Owning Palette:** [User Interface VIs](../lvsit/user_interface_vis.html)

**Requires:** Simulation Interface Toolkit

Runs, pauses, or stops the simulation.

[Example](#examples)

[IMAGE alt='image' src='sit_run_pause_stopc.gif']

|  | SIT Reference in specifies information about the current simulation. TCP Connection specifies the TCP reference for the current connection to the SIT Server. Model Name specifies the name of the current model. Server Type specifies the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| --- | --- |
|  | TCP Connection specifies the TCP reference for the current connection to the SIT Server. |
|  | Model Name specifies the name of the current model. |
|  | Server Type specifies the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| 0 | Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software. |
| 1 | MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option. |
| 2 | RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | Operation specifies the action to perform on the simulation. 0Run (default)—Runs the simulation.1Pause—Pauses the simulation.2Stop—Stops the simulation. |
| 0 | Run (default)—Runs the simulation. |
| 1 | Pause—Pauses the simulation. |
| 2 | Stop—Stops the simulation. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | SIT Reference out returns information about the current simulation. TCP Connection returns the TCP reference for the current connection to the SIT Server. Model Name returns the name of the current model. Server Type returns the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | TCP Connection returns the TCP reference for the current connection to the SIT Server. |
|  | Model Name returns the name of the current model. |
|  | Server Type returns the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| 0 | Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software. |
| 1 | MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option. |
| 2 | RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the batch simulation VI in the labview\examples\Simulation Interface\Batch Simulation directory for an example of using the SIT Run Pause Stop VI.

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_scheduler_vi.html language=enus -->
## TOPIC 00035: SIT Scheduler VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_scheduler_vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_scheduler_vi.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Scheduler VI

**Owning Palette:** [Model Interface VIs](../lvsit/model_interface_vis.html)

**Requires:** Simulation Interface Toolkit

Inserts the data from the **model inputs** array into the [model DLL](../lvsitconcepts/sit_c_components_of_a_simulation.html#real_time_components) inputs, takes a single step of the model DLL, and sends the data from the model DLL outputs to the **model outputs** array. Use the [SIT Initialize Model](../lvsit/sit_initialize_model.html) VI before executing any steps in the model DLL. Use the [SIT Finalize Model](../lvsit/sit_finalize_model.html) VI when you finish executing all the steps in the model.

[IMAGE alt='image' src='sit_schedulerc.gif']

|  | Simulation Data In specifies unique information about the model DLL. |
| --- | --- |
|  | model inputs specifies the values you want to send to the model DLL before the step. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | dispatchlist returns the list of tasks in a multirate model that the simulation needs to send to the model DLL at the current time step. |
|  | Simulation Data out returns unique information about the model DLL. |
|  | model outputs returns the values that the model DLL returns after the step. |
|  | time returns the updated time in seconds in the simulation model after the step is complete. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | last step? returns TRUE when the simulation is complete. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_set_dtalg_grp_enbl_st.html language=enus -->
## TOPIC 00036: SIT Set Data Log Group Enabled State VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_set_dtalg_grp_enbl_st.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_set_dtalg_grp_enbl_st.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Set Data Log Group Enabled State VI

**Owning Palette:** [Data Logging VIs](../lvsit/ui_data_logging.html)

**Requires:** Simulation Interface Toolkit (Windows)

[IMAGE alt='image' src='sit_set_data_log_group_enabled_state.gif']

|  | SIT Reference in specifies information about the current simulation. TCP Connection specifies the TCP reference for the current connection to the SIT Server. Model Name specifies the name of the current model. Server Type specifies the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| --- | --- |
|  | TCP Connection specifies the TCP reference for the current connection to the SIT Server. |
|  | Model Name specifies the name of the current model. |
|  | Server Type specifies the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| 0 | Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software. |
| 1 | MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option. |
| 2 | RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | Channel Group Name specifies the name of the data log channel group you want to enable or disable. Disabling a channel group stops logging for all channels in the channel group. |
|  | Enabled specifies whether the channel group is enabled or disabled. If a channel group is disabled, logging stops for all channels in the channel group. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | SIT Reference out returns information about the current simulation. TCP Connection returns the TCP reference for the current connection to the SIT Server. Model Name returns the name of the current model. Server Type returns the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | TCP Connection returns the TCP reference for the current connection to the SIT Server. |
|  | Model Name returns the name of the current model. |
|  | Server Type returns the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| 0 | Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software. |
| 1 | MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option. |
| 2 | RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_set_mdl_param.html language=enus -->
## TOPIC 00037: SIT Set Model Parameters VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_set_mdl_param.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_set_mdl_param.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Set Model Parameters VI

**Owning Palette:** [Model Interface VIs](../lvsit/model_interface_vis.html)

**Requires:** Simulation Interface Toolkit

Sets a new parameter value in the model. The elements of non-scalars such as arrays can be set individually. The parameter you want to set is specified by its param index and subindex.



The parameter structure is double buffered. Changes can be made to the parameters while the model is running. The model will not see the changes until they are applied. To apply changes to multiple parameters at the same time, set **apply changes (T)** to FALSE except for the last parameter of the group. This is useful if you want to change multiple values such as the elements of an array or multiple related parameters and want the changes to take affect in the same model time step.

[IMAGE alt='image' src='sit_set_model_parameters.gif']

|  | apply changes (T) specifies if you want to apply the new parameter value as well as any previously unapplied changes. This is the default. Set apply changes (T) to FALSE if you do not want to apply the changes immediately. When you set apply changes (T) to FALSE, the VI applies the changes the next time you call the VI with apply changes set to TRUE. |
| --- | --- |
|  | Simulation Data In specifies unique information about the model DLL. |
|  | param index specifies the index number of a scalar or nonscalar parameter. If the parameter is nonscalar, sub index specifies the index number of an element in that nonscalar parameter. |
|  | sub index specifies the index number of an element in a nonscalar parameter. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | value specifies the new parameter value. |
|  | setparam (F) specifies whether you want to set the parameter value. Set setparam (F) to TRUE if you want to set the parameter value. Set setparam (F) to FALSE if you do not want to set the parameter value. |
|  | Simulation Data out returns unique information about the model DLL. |
|  | set returns TRUE if you set a new parameter value. set returns FALSE if you did not set a new parameter value. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_spec_dtalog_config.html language=enus -->
## TOPIC 00038: SIT Specify Data Log Configuration VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_spec_dtalog_config.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_spec_dtalog_config.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Specify Data Log Configuration VI

**Owning Palette:** [Data Logging VIs](../lvsit/ui_data_logging.html)

**Requires:** Simulation Interface Toolkit

[IMAGE alt='image' src='sit_specify_data_log_configuration.gif']

|  | SIT Reference in specifies information about the current simulation. TCP Connection specifies the TCP reference for the current connection to the SIT Server. Model Name specifies the name of the current model. Server Type specifies the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| --- | --- |
|  | TCP Connection specifies the TCP reference for the current connection to the SIT Server. |
|  | Model Name specifies the name of the current model. |
|  | Server Type specifies the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| 0 | Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software. |
| 1 | MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option. |
| 2 | RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | Configuration Name specifies the name of the configuration you select. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | SIT Reference out returns information about the current simulation. TCP Connection returns the TCP reference for the current connection to the SIT Server. Model Name returns the name of the current model. Server Type returns the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | TCP Connection returns the TCP reference for the current connection to the SIT Server. |
|  | Model Name returns the name of the current model. |
|  | Server Type returns the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| 0 | Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software. |
| 1 | MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option. |
| 2 | RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_spec_fl_plybk_cfg.html language=enus -->
## TOPIC 00039: SIT Specify File Playback Configuration VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_spec_fl_plybk_cfg.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_spec_fl_plybk_cfg.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Specify File Playback Configuration VI

**Owning Palette:** [File Playback VIs](../lvsit/ui_file_playback.html)

**Requires:** Simulation Interface Toolkit (Windows)

[IMAGE alt='image' src='sit_specify_file_playback_configuration.gif']

|  | SIT Reference in specifies information about the current simulation. TCP Connection specifies the TCP reference for the current connection to the SIT Server. Model Name specifies the name of the current model. Server Type specifies the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| --- | --- |
|  | TCP Connection specifies the TCP reference for the current connection to the SIT Server. |
|  | Model Name specifies the name of the current model. |
|  | Server Type specifies the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| 0 | Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software. |
| 1 | MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option. |
| 2 | RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | Configuration Name specifies the name of the configuration you select. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | SIT Reference out returns information about the current simulation. TCP Connection returns the TCP reference for the current connection to the SIT Server. Model Name returns the name of the current model. Server Type returns the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | TCP Connection returns the TCP reference for the current connection to the SIT Server. |
|  | Model Name returns the name of the current model. |
|  | Server Type returns the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| 0 | Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software. |
| 1 | MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option. |
| 2 | RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_specify_signals_to_probe_vi.html language=enus -->
## TOPIC 00040: SIT Specify Signals to Probe VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_specify_signals_to_probe_vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_specify_signals_to_probe_vi.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Specify Signals to Probe VI

**Owning Palette:** [User Interface VIs](../lvsit/user_interface_vis.html)

**Requires:** Simulation Interface Toolkit

Specifies the [model](../lvsitconcepts/sit_c_components_of_a_simulation.html) signals you want to probe. This VI also specifies any decimation factor you want to apply to the probed signals.

[Example](#examples)

[IMAGE alt='image' src='sit_specify_probe_signalsc.gif']

|  | SIT Reference in specifies information about the current simulation. TCP Connection specifies the TCP reference for the current connection to the SIT Server. Model Name specifies the name of the current model. Server Type specifies the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| --- | --- |
|  | TCP Connection specifies the TCP reference for the current connection to the SIT Server. |
|  | Model Name specifies the name of the current model. |
|  | Server Type specifies the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| 0 | Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software. |
| 1 | MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option. |
| 2 | RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | Signals to Probe specifies the model signals you want to probe. Note You must format each element of Signals to Probe with the following syntax: <modelname>/<subsystem1>/<subsystem2>/<subsystemN>/<Block>:<PortNumber> For example, if you want to probe the Sine Wave block of a model named sinewave, format Signals to Probe as sinewave/Sine Wave:1. |
|  | Note You must format each element of Signals to Probe with the following syntax: <modelname>/<subsystem1>/<subsystem2>/<subsystemN>/<Block>:<PortNumber> For example, if you want to probe the Sine Wave block of a model named sinewave, format Signals to Probe as sinewave/Sine Wave:1. |
|  | Signal Decimation specifies the decimation factor of the probed signals. For example, if you enter a decimation of 10, the SIT Server only returns every 10th data point for each signal you are probing. Increasing the Signal Decimation value can resolve performance problems and timing errors during the simulation. The default is 1, which specifies no decimation factor. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | SIT Reference out returns information about the current simulation. TCP Connection returns the TCP reference for the current connection to the SIT Server. Model Name returns the name of the current model. Server Type returns the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | TCP Connection returns the TCP reference for the current connection to the SIT Server. |
|  | Model Name returns the name of the current model. |
|  | Server Type returns the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| 0 | Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software. |
| 1 | MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option. |
| 2 | RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the batch simulation VI in the labview\examples\Simulation Interface\Batch Simulation directory for an example of using the SIT Specify Signals to Probe VI.

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_st_fl_plbk_ch_enbl_st.html language=enus -->
## TOPIC 00041: SIT Set File Playback Channel Enabled State VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_st_fl_plbk_ch_enbl_st.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_st_fl_plbk_ch_enbl_st.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Set File Playback Channel Enabled State VI

**Owning Palette:** [File Playback VIs](../lvsit/ui_file_playback.html)

**Requires:** Simulation Interface Toolkit

[IMAGE alt='image' src='sit_set_file_playback_channel_enabled_state.gif']

|  | SIT Reference in specifies information about the current simulation. TCP Connection specifies the TCP reference for the current connection to the SIT Server. Model Name specifies the name of the current model. Server Type specifies the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| --- | --- |
|  | TCP Connection specifies the TCP reference for the current connection to the SIT Server. |
|  | Model Name specifies the name of the current model. |
|  | Server Type specifies the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| 0 | Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software. |
| 1 | MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option. |
| 2 | RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | Channel Group Name specifies the name of the playback file channel group for the channel you specify. If you do not specify a channel name, this VI enables or disables all the channels in the specified channel group. |
|  | Channel Name specifies the name of the channel you want to enable or disable. Disabling a channel stops playback for that channel into all its mapped model inputs. If you do not specify a channel name, this VI enables or disables all the channels in the specified channel group. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Enabled specifies whether the channel or channel group is enabled or disabled. Disabling a channel stops playback for that channel into all its mapped model inputs. |
|  | SIT Reference out returns information about the current simulation. TCP Connection returns the TCP reference for the current connection to the SIT Server. Model Name returns the name of the current model. Server Type returns the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | TCP Connection returns the TCP reference for the current connection to the SIT Server. |
|  | Model Name returns the name of the current model. |
|  | Server Type returns the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| 0 | Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software. |
| 1 | MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option. |
| 2 | RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | error out contains error information. With the following exception, this output provides standard error out functionality. For Mobile and Touch Panel VIs, you cannot select Explain Error from the shortcut menu to receive more information about the error. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_start_simulation_vi.html language=enus -->
## TOPIC 00042: SIT Start Simulation VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_start_simulation_vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_start_simulation_vi.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Start Simulation VI

**Owning Palette:** [Model Interface VIs](../lvsit/model_interface_vis.html)

**Requires:** Simulation Interface Toolkit

Starts the simulation.

[IMAGE alt='image' src='sit_start_simulationc.gif']

|  | Simulation Data In specifies unique information about the model DLL. |
| --- | --- |
|  | Wait for Start Command specifies whether to wait for a start command from the host VI before starting the simulation. The default is TRUE. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Simulation Data out returns unique information about the model DLL. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_take_mdl_time_step.html language=enus -->
## TOPIC 00043: SIT Take Model Time Step VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_take_mdl_time_step.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_take_mdl_time_step.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Take Model Time Step VI

**Owning Palette:** [Model Interface VIs](../lvsit/model_interface_vis.html)

**Requires:** Simulation Interface Toolkit (Windows)

Model Outputs

[IMAGE alt='image' src='sit_take_mdl_time_step.gif']

|  | Simulation Data In specifies unique information about the model DLL. |
| --- | --- |
|  | Model Inputs specifies the values you want to send to the model DLL before the step. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Overrun (n-1)? indicates, when TRUE, that the base rate loop did not finish in time the previous iteration. |
|  | Simulation Data Out returns unique information about the model DLL. |
|  | Model Outputs specifies the values the model DLL sends after the step. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | last step? indicates, when TRUE, that the model DLL has signaled for the simulation to stop. The following list includes some reasons the model DLL might set last step? to TRUE: An error has occurred in the simulation. The simulation may contain code requesting a stop. The simulation time has reached the Stop Time specified when the model DLL was initialized. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_update_indicator_vi.html language=enus -->
## TOPIC 00044: SIT Update Indicator VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_update_indicator_vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_update_indicator_vi.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Update Indicator VI

**Owning Palette:** [User Interface VIs](../lvsit/user_interface_vis.html)

**Requires:** Simulation Interface Toolkit

Updates the [host VI](../lvsitconcepts/sit_c_components_of_a_simulation.html) front panel indicators with values obtained from the [SIT Read](../lvsit/sit_read.html) VI.

Place the [SIT Update Indicator](../lvsit/sit_update_indicator_vi.html) VI next to a [Case Structure](/csh?topicname=glang/case_structure.html) inside a [For Loop](/csh?topicname=glang/for_loop.html). The iteration of the For Loop determines the signal value that this VI writes to the current indicator. The value wired to the selector terminal of the Case Structure determines the indicator that this VI updates. For example, Case 0 specifies the value and indicator that correspond with the first probed signal, Case 1 specifies the value and indicator that correspond with the second probed signal, and so on.

[Example](#examples)

[IMAGE alt='image' src='sit_update_indicatorc.gif']

|  | Raw Data specifies the values and dimensions of all probed signals. Data specifies the values of all probed signals. Dimensions specifies the dimensions of all probed signals. Each element pair specifies the length and width of a signal. |
| --- | --- |
|  | Data specifies the values of all probed signals. |
|  | Dimensions specifies the dimensions of all probed signals. Each element pair specifies the length and width of a signal. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Iteration specifies the index number of current probed signal that this VI is writing to an indicator. The default value is 0, which corresponds to the first signal probed. |
|  | Indicator Data returns the values specific to the current signal. |
|  | Last Row Index returns the index number of the last row of Indicator Data. Use Last Row Index if you are probing a scalar or one-dimensional signal and are interested in only the latest data from that signal. |
|  | error out contains error information. This output provides standard error out functionality. |
|  | Timestamps returns the simulation time steps at which this VI returned each row of the Indicator Data parameter. The ith element of the Timestamps parameter corresponds to the ith row of the Indicator Data parameter. |

#### Example

Refer to the updatingindicators VI in the labview\examples\Simulation Interface\Updating Indicators directory for an example of using the SIT Update Indicator VI.

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_write.html language=enus -->
## TOPIC 00045: SIT Write VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_write.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_write.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Write VI

**Owning Palette:** [User Interface VIs](../lvsit/user_interface_vis.html)

**Requires:** Simulation Interface Toolkit

Writes a new value to a [model](../lvsitconcepts/sit_c_components_of_a_simulation.html) parameter.

[Example](#examples)

[IMAGE alt='image' src='sit_writec.gif']

|  | SIT Reference in specifies information about the current simulation. TCP Connection specifies the TCP reference for the current connection to the SIT Server. Model Name specifies the name of the current model. Server Type specifies the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| --- | --- |
|  | TCP Connection specifies the TCP reference for the current connection to the SIT Server. |
|  | Model Name specifies the name of the current model. |
|  | Server Type specifies the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| 0 | Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software. |
| 1 | MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option. |
| 2 | RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | Parameter Name specifies the path to a model parameter. You must format Parameter Name with the following syntax: modelname/subsystem1/subsystem2/subsystemN/Block/Parameter For example, if you want to manipulate the Amplitude parameter of the Sine Wave block in a model named sinewave, format Parameter Name as sinewave/Sine Wave/Amplitude. |
|  | NewVal specifies the value you want to write to the model parameter. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | OldVal specifies the previous value of Parameter Name. If the simulation is running on an RT target and Parameter Name is nonscalar, the SIT Server updates only the changed elements of Parameter Name. Wiring a value to OldVal helps ensure that the current task completes within the task deadline, because the SIT Server updates only the necessary element of Parameter Name. If you do not specify a value for OldVal, the SIT Server updates every element of Parameter Name. OldVal has no effect on a non-RT simulation. |
|  | SIT Reference out returns information about the current simulation. TCP Connection returns the TCP reference for the current connection to the SIT Server. Model Name returns the name of the current model. Server Type returns the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | TCP Connection returns the TCP reference for the current connection to the SIT Server. |
|  | Model Name returns the name of the current model. |
|  | Server Type returns the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| 0 | Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software. |
| 1 | MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option. |
| 2 | RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | error out contains error information. This output provides standard error out functionality. |

#### Example

Refer to the batch simulation VI in the labview\examples\Simulation Interface\Batch Simulation directory for an example of using the SIT Write VI.

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_write_log_settings.html language=enus -->
## TOPIC 00046: SIT Write Log Settings to Configuration File VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_write_log_settings.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_write_log_settings.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Write Log Settings to Configuration File VI

**Owning Palette:** [Data Logging VIs](../lvsit/ui_data_logging.html)

**Requires:** Simulation Interface Toolkit

Saves data logging configuration data to a configuration file.

[IMAGE alt='image' src='sit_write_log.gif']

|  | Configuration Name specifies the name of the configuration file. This VI appends a .ini file extension to the name you specify. |
| --- | --- |
|  | Project Directory in specifies the path to the directory that contains the configuration file. |
|  | Data Log Settings specifies the data log settings of the logged data file. Logging Enabled specifies to log simulation data. Data Log Filename specifies the name of the data log file. Timestamp Filename specifies to append a timestamp to the data log filename. Halt Simulation on Logging Data Loss specifies to stop logging data upon data loss. Log Last N Points specifies to log the only the number of points you specify in the Last N Points control. Last N Points specifies the number of simulation data points that you want to log. For example, if you enter a value of 3, the LabVIEW Simulation Interface Toolkit logs only the last three data points that the simulation returns. Default Configuration specifies to begin logging data automatically when the simulation starts. If you do not select this option, you must use the SIT Control Data Logging VI to begin logging. |
|  | Logging Enabled specifies to log simulation data. |
|  | Data Log Filename specifies the name of the data log file. |
|  | Timestamp Filename specifies to append a timestamp to the data log filename. |
|  | Halt Simulation on Logging Data Loss specifies to stop logging data upon data loss. |
|  | Log Last N Points specifies to log the only the number of points you specify in the Last N Points control. |
|  | Last N Points specifies the number of simulation data points that you want to log. For example, if you enter a value of 3, the LabVIEW Simulation Interface Toolkit logs only the last three data points that the simulation returns. |
|  | Default Configuration specifies to begin logging data automatically when the simulation starts. If you do not select this option, you must use the SIT Control Data Logging VI to begin logging. |
|  | Signals to Log specifies the signals to log and the group and decimation information for the signals to log. Group Name specifies the name of the logged data group. Decimation specifies the decimation factor of the signals to log. For example, if you enter a decimation of 10, the SIT Server only returns every 10th data point for each signal you are logging. Increasing the Signal Decimation value can resolve performance problems and timing errors during the simulation. The default value is 1, which specifies no decimation factor. Signals to Log specifies the signals to include in the logged data file. |
|  | Group Name specifies the name of the logged data group. |
|  | Decimation specifies the decimation factor of the signals to log. For example, if you enter a decimation of 10, the SIT Server only returns every 10th data point for each signal you are logging. Increasing the Signal Decimation value can resolve performance problems and timing errors during the simulation. The default value is 1, which specifies no decimation factor. |
|  | Signals to Log specifies the signals to include in the logged data file. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Model Path specifies the path to the model. |
|  | Project Directory out returns the path to the logging or playback configuration file. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_write_multiple_vi.html language=enus -->
## TOPIC 00047: SIT Write Multiple VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_write_multiple_vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_write_multiple_vi.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Write Multiple VI

**Owning Palette:** [User Interface VIs](../lvsit/user_interface_vis.html)

**Requires:** Simulation Interface Toolkit

Writes values to multiple parameters in the same [model](../lvsitconcepts/sit_c_components_of_a_simulation.html) simultaneously.

[IMAGE alt='image' src='sit_write_multiplec.gif']

|  | SIT Reference in specifies information about the current simulation. TCP Connection specifies the TCP reference for the current connection to the SIT Server. Model Name specifies the name of the current model. Server Type specifies the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| --- | --- |
|  | TCP Connection specifies the TCP reference for the current connection to the SIT Server. |
|  | Model Name specifies the name of the current model. |
|  | Server Type specifies the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| 0 | Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software. |
| 1 | MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option. |
| 2 | RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | Parameter List specifies the parameters you want to change and the new values for these parameters. Parameter Name specifies the path to a model parameter. You must format Parameter Name with the following syntax: modelname/subsystem1/subsystem2/subsystemN/Block/Parameter For example, if you want to manipulate the Amplitude parameter of the Sine Wave block in a model named sinewave, format Parameter Name as sinewave/Sine Wave/Amplitude. value specifies the value to which you want Parameter Name to change. This value must be a two-dimensional array of double-precision floating-point numbers. If you are changing the value of a scalar parameter, you must create a two-dimensional array consisting of the value as the only element. |
|  | Parameter Name specifies the path to a model parameter. You must format Parameter Name with the following syntax: modelname/subsystem1/subsystem2/subsystemN/Block/Parameter For example, if you want to manipulate the Amplitude parameter of the Sine Wave block in a model named sinewave, format Parameter Name as sinewave/Sine Wave/Amplitude. |
|  | value specifies the value to which you want Parameter Name to change. This value must be a two-dimensional array of double-precision floating-point numbers. If you are changing the value of a scalar parameter, you must create a two-dimensional array consisting of the value as the only element. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | SIT Reference out returns information about the current simulation. TCP Connection returns the TCP reference for the current connection to the SIT Server. Model Name returns the name of the current model. Server Type returns the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | TCP Connection returns the TCP reference for the current connection to the SIT Server. |
|  | Model Name returns the name of the current model. |
|  | Server Type returns the type of execution host on which the SIT Server is running. 0Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software.1MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option.2RT—Specifies that the SIT Server is running on a real-time (RT) target. |
| 0 | Simulation Environment (default)—Specifies that the SIT Server is running on an execution host that is running The MathWorks, Inc. MATLAB® application software. |
| 1 | MATRIXx—Specifies that the SIT Server is running on an execution host that is running Xmath. The LabVIEW Simulation Interface Toolkit does not currently support this option. |
| 2 | RT—Specifies that the SIT Server is running on a real-time (RT) target. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sit_write_pb_settings.html language=enus -->
## TOPIC 00048: SIT Write Playback Settings to Configuration File VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sit_write_pb_settings.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sit_write_pb_settings.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SIT Write Playback Settings to Configuration File VI

**Owning Palette:** [File Playback VIs](../lvsit/ui_file_playback.html)

**Requires:** Simulation Interface Toolkit

Saves playback configuration data to a configuration file.

[IMAGE alt='image' src='sit_write_playback.gif']

|  | Configuration Name specifies the name of the configuration file. This VI appends a .ini file extension to the name you specify. |
| --- | --- |
|  | Project Directory in specifies the path to the directory that contains the configuration file. |
|  | Playback Settings specifies the playback settings of the logged data file. Playback Enabled specifies to play back logged simulation data. Playback File Path specifies the path to the logged data file to play back. Read behavior specifies what action this VI takes when a buffer underflow occurs. 0Error on underflow (default)—Stops playback if data is not available at the correct time.1Ignore underflow—Continues playback if data is not available at the correct time. Default Configuration specifies to begin replaying the data automatically when the model starts. If you do not select this option, you must specify to begin data playback manually by using the SIT Control File Playback VI. |
|  | Playback Enabled specifies to play back logged simulation data. |
|  | Playback File Path specifies the path to the logged data file to play back. |
|  | Read behavior specifies what action this VI takes when a buffer underflow occurs. 0Error on underflow (default)—Stops playback if data is not available at the correct time.1Ignore underflow—Continues playback if data is not available at the correct time. |
| 0 | Error on underflow (default)—Stops playback if data is not available at the correct time. |
| 1 | Ignore underflow—Continues playback if data is not available at the correct time. |
|  | Default Configuration specifies to begin replaying the data automatically when the model starts. If you do not select this option, you must specify to begin data playback manually by using the SIT Control File Playback VI. |
|  | Playback Channels specifies the property information and the step interval for the selected channel. Group Name specifies the name of the logged data group. Channel Name specifies the name of the channel you are configuring. Inport Numbers specifies the model inputs to send data to. Use Default Step Interval specifies to use the interval setting from the channel file information. Custom Step Interval specifies the step interval to use for the channel. The step interval determines how often to read a new sample from the file into the model. Loop Channel specifies whether to loop the data on the channel. If you do not select this option, file playback runs through each value once and then returns the last value on the channel continuously until you stop playback. The default is TRUE. |
|  | Group Name specifies the name of the logged data group. |
|  | Channel Name specifies the name of the channel you are configuring. |
|  | Inport Numbers specifies the model inputs to send data to. |
|  | Use Default Step Interval specifies to use the interval setting from the channel file information. |
|  | Custom Step Interval specifies the step interval to use for the channel. The step interval determines how often to read a new sample from the file into the model. |
|  | Loop Channel specifies whether to loop the data on the channel. If you do not select this option, file playback runs through each value once and then returns the last value on the channel continuously until you stop playback. The default is TRUE. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Model Path specifies the path to the model. |
|  | Project Directory out returns the path to the logging or playback configuration file. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/sits_server_loop_vi.html language=enus -->
## TOPIC 00049: SITs Server Loop VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/sits_server_loop_vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/sits_server_loop_vi.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### SITs Server Loop VI

**Owning Palette:** [Model Interface VIs](../lvsit/model_interface_vis.html)

**Requires:** Simulation Interface Toolkit

Manages the communication between the model and the Host VI. This VI handles requests from the Host VI to start and stop the model as well as to set parameters and probe signals.



This VI does not return data until you stop the model or a communication error occurs.

[IMAGE alt='image' src='sits_server_loop.gif']

|  | timeout limits the time that the VI waits for data to be returned from the database. A timeout value of less than or equal to 0 indicates no timeout. The VI waits indefinitely until the data is returned. |
| --- | --- |
|  | port specifies the port number used for TCP communication. Default is port 6011. |
|  | Simulation Data in specifies unique information about the model. |
|  | Param Info in contains information about the parameters you can manipulate in the model. |
|  | Signal Info in contains information about the signals you can probe in the model. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Server Loop Processor specifies the processor on which to execute the loop that controls the timing of the SIT Server. The default is -2 (any available processor). If you specify an invalid processor, the loop executes on the first available processor. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/spec_fl_plybk_cfg.html language=enus -->
## TOPIC 00050: Specify File Playback Configuration VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/spec_fl_plybk_cfg.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/spec_fl_plybk_cfg.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Specify File Playback Configuration VI

**Owning Palette:** [File Playback VIs](../lvsit/mi_file_playback.html)

**Requires:** Simulation Interface Toolkit (Windows)

[IMAGE alt='image' src='specify_file_playback_configuration.gif']

|  | Simulation Data In specifies unique information about the model DLL. |
| --- | --- |
|  | Configuration Name specifies the name of the configuration you select. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Simulation Data out returns unique information about the model DLL. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/specify_data_log_config.html language=enus -->
## TOPIC 00051: Specify Data Log Configuration VI

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/specify_data_log_config.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/specify_data_log_config.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Specify Data Log Configuration VI

**Owning Palette:** [Data Logging VIs](../lvsit/mi_data_logging.html)

**Requires:** Simulation Interface Toolkit (Windows)

[IMAGE alt='image' src='specify_data_log_configuration.gif']

|  | Simulation Data In specifies unique information about the model DLL. |
| --- | --- |
|  | Configuration Name specifies the name of the configuration you select. |
|  | error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Simulation Data out returns unique information about the model DLL. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/ui_data_logging.html language=enus -->
## TOPIC 00052: Data Logging VIs

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/ui_data_logging.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/ui_data_logging.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Data Logging VIs

**Owning Palette:** [User Interface VIs](../lvsit/user_interface_vis.html)

**Requires:** Simulation Interface Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

|  | Note You must install the LabVIEW Real-Time Module in order to place these VIs on the block diagram. |
| --- | --- |

The VIs on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html) or [specific Simulation Interface Toolkit error codes](sit_error_codes.html).

| Palette Object | Description |
| --- | --- |
| SIT Control Data Logging | Controls data logging during run time. This VI can start, pause, or stop data logging. |
| SIT Get Data Logging Status | Returns current data logging status information, including whether data logging is enabled or disabled. This VI also returns all configurations set up to run on the target, as well as information about the active data log configuration. |
| SIT Set Data Log Group Enabled State | Enables or disables a specified channel group in the data log file. Disabling a channel group stops logging for all channels in the channel group. This does not affect any previously logged data. Enabling a channel group resumes logging for all channels in the channel group. |
| SIT Specify Data Log Configuration | Specifies the data log configuration to use in the simulation. If the specified configuration does not exist, or if you specify a blank configuration name, this VI disables logging. |
| SIT Write Log Settings to Configuration File | Saves data logging configuration data to a configuration file. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/ui_file_playback.html language=enus -->
## TOPIC 00053: File Playback VIs

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/ui_file_playback.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/ui_file_playback.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### File Playback VIs

**Owning Palette:** [User Interface VIs](../lvsit/user_interface_vis.html)

**Requires:** Simulation Interface Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the File Playback VIs to configure playback from the host VI.

|  | Note You must install the LabVIEW Real-Time Module in order to place these VIs on the block diagram. |
| --- | --- |

The VIs on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html) or [specific Simulation Interface Toolkit error codes](sit_error_codes.html).

| Palette Object | Description |
| --- | --- |
| SIT Control File Playback | Enables playback during runtime. |
| SIT Get File Playback Status | Returns current file playback status information including whether file playback is playing, paused, stopped, or disabled. This VI also returns all configurations set up to run on the target as well as information about the active playback configuration. |
| SIT Set File Playback Channel Enabled State | Enables or disables the specified file playback channel. Disabling a channel stops playback for that channel into all its mapped model inputs. If you do not specify a channel name, this VI enables or disables all the channels in the specified channel group. If this VI does not find the channel name you specified in the group you specified, or if this VI does not find the group you specified, this VI takes no action. |
| SIT Specify File Playback Configuration | Specifies the file playback configuration to use in the simulation. |
| SIT Write Playback Settings to Configuration File | Saves playback configuration data to a configuration file. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsit/user_interface_vis.html language=enus -->
## TOPIC 00054: User Interface VIs

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsit/user_interface_vis.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsit/user_interface_vis.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### User Interface VIs

**Owning Palette:** [Simulation Interface VIs](../lvsit/simulation_interface_vis.html)

**Requires:** Simulation Interface Toolkit. This topic might not match its corresponding palette in LabVIEW depending on your operating system, licensed product(s), and target.

Use the User Interface VIs to create a [host VI](../lvsitconcepts/sit_c_components_of_a_simulation.html). You also can use the [SIT Connection Manager](../lvsit/sit_connection_manager_db.html) dialog box to generate a host VI.

The VIs on this palette can return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html) or [specific Simulation Interface Toolkit error codes](sit_error_codes.html).

| Palette Object | Description |
| --- | --- |
| SIT Close Simulation | Closes the current connection to the SIT Server. |
| SIT Get Parameter | Returns the value of a model parameter you specify. |
| SIT Get Simulation State | Returns the current status of the simulation. |
| SIT Initialize Simulation | Initializes the host VI by creating a connection to the execution host on which the SIT Server is running. This VI also opens all the necessary models that the host VI specifies. |
| SIT Model Error | Receives errors specific to the model DLL and reports these errors to the host VI. |
| SIT Read | Reads data from all probed model signals. |
| SIT Run Pause Stop | Runs, pauses, or stops the simulation. |
| SIT Specify Signals to Probe | Specifies the model signals you want to probe. This VI also specifies any decimation factor you want to apply to the probed signals. |
| SIT Update Indicator | Updates the host VI front panel indicators with values obtained from the SIT Read VI. |
| SIT Write | Writes a new value to a model parameter. |
| SIT Write Multiple | Writes values to multiple parameters in the same model simultaneously. |

| Subpalette | Description |
| --- | --- |
| Data Logging VIs | Use the Data Logging VIs to configure data logging from the host VI. |
| File Playback VIs | Use the File Playback VIs to configure playback from the host VI. |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsitconcepts/sit_c_bd_batch.html language=enus -->
## TOPIC 00055: Understanding the Block Diagram of the Batch Simulation Host VI (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsitconcepts/sit_c_bd_batch.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsitconcepts/sit_c_bd_batch.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Understanding the Block Diagram of the Batch Simulation Host VI (Simulation Interface Toolkit)

The block diagram for the Batch Simulation VI has three parts—the code to initialize the batch simulation, the code to set the parameter values, and the code to receive indicator updates from the simulation. This VI performs these tasks programmatically instead of waiting for you to set parameter values and run the simulation.

#### Initializing the Batch Simulation

The initialization code uses the [SIT Initialize Simulation](../lvsit/sit_initialize_sim.html) VI to start the simulation. This VI initiates a connection to the [SIT Server](../lvsitconcepts/sit_c_components_of_a_simulation.html), which resides on the computer that the **hostname** control specifies. The **port** control specifies the port number through which the Batch Simulation VI communicates with the [sinewave](../lvsithowto/sit_h_building_a_model.html) model. The **Model path** control specifies the path to the model that you want to run.

#### Setting the Parameter Values

The [For Loop](/csh?topicname=glang/for_loop.html) contains the code that sets the parameter values and the code that updates the **Output** indicator. The For Loop uses automatic indexing to determine the number of times it executes. Specifically, the For Loop executes one time for every element in the **Array of parameter values** control.

The block diagram code that sets the parameter values uses the [SIT Write](../lvsit/sit_write.html) VI to set the parameter values in the sinewave model. Given a path to a model parameter, this VI sets the initial value of that parameter using the value specified in the **Array of parameter values** control. The [SIT Specify Signals to Probe](../lvsit/sit_specify_signals_to_probe_vi.html) VI tells the SIT Server which signals to probe. After the SIT Write VI sets the initial values for the simulation, the [SIT Run Pause Stop](../lvsit/sit_run_pause_stop.html) VI notifies the SIT Server to start running the simulation.

#### Updating the Indicator

The [While Loop](/csh?topicname=glang/while_loop.html) contains block diagram code that receives signal data from the model and updates the front panel XY graph. The While Loop contains the [SIT Read](../lvsit/sit_read.html) VI and the [SIT Update Indicator](../lvsit/sit_update_indicator_vi.html) VI. The SIT Read VI contains all the probed signal data. This VI wires the **Raw Data** output containing the signal data to the **Raw Data** input of the SIT Update Indicator VI, which creates an array of signal values. The SIT Update Indicator VI collects this array using shift registers and updates the host VI indicators at the end of the simulation.

The SIT Read VI executes until the While Loop receives an indication from the SIT Server that the simulation is complete. The result, for this example, is a plot of three sine waves with different amplitudes and frequencies.

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsitconcepts/sit_c_communicating_with_the_sit_server.html language=enus -->
## TOPIC 00056: Communicating with the SIT Server (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsitconcepts/sit_c_communicating_with_the_sit_server.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsitconcepts/sit_c_communicating_with_the_sit_server.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Communicating with the SIT Server (Simulation Interface Toolkit)

The [host VI](../lvsitconcepts/sit_c_components_of_a_simulation.html) communicates with the [execution host](../lvsitconcepts/sit_c_components_of_a_simulation.html) through the [SIT Server](../lvsitconcepts/sit_c_components_of_a_simulation.html). As you change parameter values using host VI front panel controls, the host VI sends a request to the model to change the appropriate parameter values. The SIT Server transmits this request. Using the new parameter values, the model executes and updates the appropriate signals. The model then sends the new signal values to the SIT Server, which passes the new values to the host VI. The host VI uses these new values to update the front panel indicators.

If you are not running a simulation on a real-time (RT) target, you must launch The MathWorks, Inc. MATLAB[®](/csh?topicname=lvhelp/trademarks.html) application software before starting the SIT Server. By default, the LabVIEW Simulation Interface Toolkit configures the SIT Server to start automatically when you launch the MATLAB application software. However, you can [configure the SIT Server](../lvsitconcepts/sit_c_configuring_the_sit_server.html) to start on a different port.

If you are running a simulation on an RT target, the [driver VI](../lvsitconcepts/sit_c_components_of_a_simulation.html#real_time_components) starts the SIT Server, so you do not need to launch the MATLAB application software. You also can [run a simulation on an RT target without the SIT Server](../lvsithowto/sit_h_run_wo_server.html).

|  | Note If you installed the MATLAB application software files as read-only, the Simulation Interface Toolkit does not configure the SIT Server to start automatically and the SignalProbe block does not appear in the Simulink Library Browser window. To see these changes, add the following lines to the matlabrc.m file. If you only want to start the SIT Server for certain users or configurations, add the following lines to the startup.m file. addpath('X:\\SimulationInterfaceToolkit'); NISIT_AddPaths; NISITServer; where X is the drive letter on which you installed the Simulation Interface Toolkit. |
| --- | --- |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsitconcepts/sit_c_components_of_a_simulation.html language=enus -->
## TOPIC 00057: Components of a Simulation (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsitconcepts/sit_c_components_of_a_simulation.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsitconcepts/sit_c_components_of_a_simulation.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Components of a Simulation (Simulation Interface Toolkit)

A simulation consists of the following components:

- Model —A simulation block diagram in graphical form, another source code form (e.g., C code), or compiled form. Models contain inputs and outputs that send and receive data. Models contain parameters you can manipulate and signals whose values you can view. For example, a model that generates a sine wave contains parameters that adjust the amplitude and frequency of the sine wave. You can view the value of the sine wave using the model signal. Models can be built using The MathWorks, Inc. Simulink ® application software. You can run a model either on a Windows computer or on a supported National Instruments real-time (RT) target .
- Host VI —The VI that you use to manipulate a model. The host VI consists of a front panel and a block diagram. You use front panel controls to manipulate model parameters. For example, you can use a control to change the amplitude of a sine wave. You use front panel indicators to view the values of the model signals. For example, you can use a waveform chart to view a sine wave as you change the amplitude. 
 The block diagram of the host VI contains the code that defines mappings between front panel controls/indicators and model parameters/signals. You create a host VI using LabVIEW and the SIT Connection Manager dialog box. 
 [IMAGE alt='image' src='note.gif']
**Note** Advanced users can create a host VI using the [User Interface VIs](../lvsit/user_interface_vis.html).
- SIT Server —The server that uses a TCP/IP connection to transmit data between the host VI and the model. You must launch the SIT Server, which starts automatically when you launch The MathWorks, Inc. MATLAB ® application software, before running a simulation. By default, the SIT Server runs on port 6011.
- Host Computer —The computer on which you run the host VI. The host computer must be a PC running Windows 7/Vista/XP/Server 2008 (64-bit)/Server 2003 (32-bit).
 [IMAGE alt='image' src='note.gif']
**Note** The LabVIEW Simulation Interface Toolkit runs as a 32-bit application on all operating systems.
- Execution Host —The computer on which you run the MATLAB application software, the SIT Server, and the simulation itself. The execution host can be the host computer or a Windows computer on the same TCP/IP network as the host computer.

The following figure shows how these components work together:

[IMAGE alt='image' src='runsimulinkmodelinlv.gif']

When you run the host VI, the diagram code initializes the simulation and defines the relationship between host VI controls/indicators and model parameters/signals. As you change the values of front panel controls, the simulation executes the following steps:

1. The host VI block diagram uses TCP/IP to send the new parameter values to the SIT Server.
2. The SIT Server transmits these new parameter values to the model.
3. The model uses these new parameter values to execute the blocks, which update the appropriate signal values.
4. The SIT Server probes the model signals for which you created mappings.
5. The SIT Server transmits the new signal values to the host VI, which updates the front panel indicators.

#### Real-Time Simulations

You can use the LabVIEW Simulation Interface Toolkit to run a simulation on a real-time (RT) target. The Simulation Interface Toolkit supports [certain types of National Instruments RT Series hardware](../lvsitconcepts/sit_c_supported_ni_hardware.html). You also can [execute an RT simulation on a Windows computer](../lvsithowto/sit_h_dll_windows.html).

RT simulations involve the following additional components:

- LabVIEW Real-Time Module —You need this module to run a deterministic RT simulation.
- LabVIEW FPGA Module —(Optional) If you are creating mappings between National Instruments FPGA targets and a model DLL , any FPGA target you specify must have an associated FPGA lvbit file. The Simulation Interface Toolkit provides FPGA lvbit files for the NI PXI-7831R, NI PCI-7831R, and NI PXI-7811R. If you want to customize these FPGA VIs or create an FPGA VI for another FPGA target, you need the FPGA Module.
- National Instruments Driver Software —You need the appropriate National Instruments driver software to communicate with hardware installed in an RT target. For FPGA targets, you need NI-RIO3.0 or later. For CAN interfaces, you need NI-CAN 2.6 or later. For DAQ devices, you need NI-DAQmx 8.7.2 or later.
- Driver VI —The VI that manipulates the model DLL. The driver VI and the model DLL run on an RT target. You manipulate the driver VI with a host VI. You create a driver VI using the SIT Connection Manager dialog box.
- Model DLL —A model compiled to run on an RT target. You enable a model to run on an RT target by using The MathWorks, Inc. Real-Time Workshop ® and Microsoft Visual C++.
 To enable a model to run on an RT target, Real-Time Workshop converts the model and any subsystems into a C code version of the model. Note this C code version of the model is the same Simulink block diagram model, just in a C code form. Microsoft Visual C++ then compiles the C code model into a model DLL named ModelName .dll , where ModelName is the name of the model. Real-Time Workshop places the model DLL into the current working directory. The following figure shows this conversion process.
 
 [IMAGE alt='image' src='convertsimulinktodll.gif'] 
 
 The LabVIEW Simulation Interface Toolkit supports Microsoft Visual C++ 6.0, Microsoft Visual C++ .NET 2003, Microsoft Visual C++ .NET 2005 (Professional or Express), and Microsoft Visual C++ .NET 2008 (Professional or Express).
 
 [IMAGE alt='image' src='note.gif']
**Note** Advanced users can create a driver VI using the [Model Interface VIs](../lvsit/model_interface_vis.html).
- SIT Server —The SIT Server transmits data between the host VI and the driver VI. If you do not need to communicate with an RT simulation, you can run an RT simulation without the SIT Server . You do not need to launch the MATLAB application software to run a simulation on an RT target.

The following figure shows how these components work together:

[IMAGE alt='image' src='runsimonrtdevice.gif']

When you run the host VI, the Simulation Interface Toolkit downloads the model DLL and driver VI to the RT target. The Simulation Interface Toolkit then starts the SIT Server on the RT target, and the driver VI initializes the model DLL. As you change the values of front panel controls, the simulation executes the following steps:

1. The host VI block diagram uses TCP/IP to send the new parameter values to the SIT Server.
2. The driver VI transmits these new parameter values to the model DLL.
3. The model DLL uses these new parameter values to execute the C code and update the appropriate signal values.
4. The driver VI probes the model signals for which you created mappings.
5. The SIT Server transmits the new signal values to the host VI, which updates the front panel indicators.

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsitconcepts/sit_c_configuring_the_sit_server.html language=enus -->
## TOPIC 00058: Configuring the SIT Server (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsitconcepts/sit_c_configuring_the_sit_server.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsitconcepts/sit_c_configuring_the_sit_server.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Configuring the SIT Server (Simulation Interface Toolkit)

By default, the LabVIEW Simulation Interface Toolkit adds the command NISITServer('start',6011) to the matlabrc file. This command starts the SIT Server on port 6011 when The MathWorks, Inc. MATLAB[®](/csh?topicname=lvhelp/trademarks.html) application software launches. To start the SIT Server on a different port, open matlabrc.m in a text editor and change 6011 to the port that you want to use. The matlabrc.m file is located in the <MATLAB>\toolbox\local\ directory.

If you want to temporarily change the port number, first stop the SIT Server by entering the command NISITServer('stop'). You do not need to specify the port number when you stop the SIT Server. Then enter the command NISITServer('start',XXXX), where XXXX is the port number you want to use.

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsitconcepts/sit_c_creating_mappings.html language=enus -->
## TOPIC 00059: Creating Mappings (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsitconcepts/sit_c_creating_mappings.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsitconcepts/sit_c_creating_mappings.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Creating Mappings (Simulation Interface Toolkit)

The block diagram code of the host VI contains mappings that connect LabVIEW controls to model parameters and LabVIEW indicators to model signals. You can create mappings using the [SIT Connection Manager](../lvsit/sit_connection_manager_db.html) dialog box. To access this dialog box, launch LabVIEW and select **Tools»SIT Connection Manager**.

#### Parameters and Workspace Variables

When you map a control directly to a model parameter, the parameter itself is updated with the value of the control. When you map a control to a workspace variable, the variable is updated, as well as all parameters that are dependent on it. Thus, one workspace variable can effectively tune multiple model parameters. For a given model, you can choose to map to either model parameters or workspace variables. To use workspace variables, you must inline the model parameters, and then specify which workspace variables you want to use.

Complete the following steps to inline model parameters:

1. Launch The MathWorks, Inc. Simulink® application software and load the model that contains the parameters you want to inline.
2. Launch the Simulation Parameters dialog box:
  1. For The MathWorks, Inc. MATLAB® application software release 13, select Simulation»Simulation parameters to launch the Simulation Parameters dialog box.
  2. For the MATLAB® application software release 14 and later, select Simulation»Configuration parameters to launch the Configuration Parameters dialog box.
3. Display the Inline parameters field:
  1. For the MATLAB® application software release 13, click the Advanced tab.
  2. For the MATLAB® application software release 14 and later, click the Optimization item in the configuration tree on the left.
4. Select Inline parameters , and click the Configure button.
5. Select the appropriate variable(s) in the Source list.
6. Click the Add to Table» button.
7. Click the Apply button, and then click the OK button.
8. Click the OK button to return to the model.

|  | Tip Click the Help button in the Simulation Parameters or Configuration Parameters dialog box to launch the MATLAB® help and find additional information about this process. |
| --- | --- |

|  | Note When you build a model into a DLL using the The MathWorks, Inc. Real-Time Workshop®, some types of expressions may not be tunable. Refer to the Tunable Expression Limitations section in The MathWorks, Inc. Real-Time Workshop® documentation for more information. |
| --- | --- |

You can create mappings using a one-to-one relationship or a one-to-many relationship. The following figure shows a one-to-one relationship, mapping to model parameters:

[IMAGE alt='image' src='mappings11.gif']

In the previous figure, the **Sine Wave Amplitude** control of the host VI manipulates the amplitude parameter of the **Sine Wave** block in the model. The same relationship applies to the rest of the controls and parameters. You also can map one host VI control to multiple parameters and one indicator to multiple signals. The following figure shows this one-to-many relationship, mapping from model signals:

[IMAGE alt='image' src='mappings1m.gif']

In the previous figure, **All My Signals** displays all the signals in the model. To define a one-to-many relationship, press the Ctrl key while clicking on multiple parameters or signals.

You can map controls to workspace variables to update all the model parameters which are dependent on them:

[IMAGE alt='image' src='ctrlstowspacvar.gif']

If the host VI is not running, you can use the **SIT Connection Manager** dialog box to modify mappings and generate new block diagram code. If the host VI is running, you must use the [Remap Controls and Indicators](../lvsit/sit_remap_ci_db.html) dialog box to modify mappings.

#### Valid Mappings

The following list describes the front panel controls and indicators you can use in a host VI and the valid mappings you can make to each control or indicator.

- Array —You can map array objects to any vector or matrix value in The MathWorks, Inc. Simulink ® application software. The objects in the array must be a supported object from this list.
- Boolean —You can map Boolean objects to any scalar value in the Simulink application software. Boolean controls encode FALSE as 0 and TRUE as 1. Boolean indicators display 0 as FALSE and any nonzero value as TRUE.
- String —You can map string objects to any Simulink data type. A Simulink vector or matrix appears as a tab-delimited string.
- Numeric, Enum, Ring, Combo Box, Color Box, Radio Buttons Control —You can map these objects to any scalar value in the Simulink application software.
- Knob, Dial, Meter, Gauge —You can map these objects to any scalar value in the Simulink application software. If you enable multiple needles on an object, you can map the object to a vector.
- Slider, Tank, Thermometer —You can map these objects to any scalar value in the Simulink application software. If you enable multiple sliders on an object, you can map the object to a vector. 
 
 [IMAGE alt='image' src='note.gif']
**Note** By default, the LabVIEW Simulation Interface Toolkit does not automatically adjust the scale range of knobs and sliders. LabVIEW Simulation Interface Toolkit can automatically adjust the scale range based on the initial value of the parameter in the Simulink application software. You can enable this autoscaling by placing a checkmark in the **Autoscale Controls** checkbox on the **Mappings** tab of the [SIT Connection Manager](../lvsit/sit_connection_manager_db.html) dialog box.
- Intensity Chart, Intensity Graph —You can map these objects only to a two-dimensional matrix in the Simulink application software.
- Waveform Graph —You can map waveform graphs only to a one-dimensional vector or two-dimensional matrix in the Simulink application software.
- XY Graph —You can map XY graphs to any two scalar values in the Simulink application software. When you create the mapping, click the signal you want to associate with the x value. Then press the <Ctrl> key and click the signal you want to associate with the y value. 
 [IMAGE alt='image' src='note.gif']
**Note** The Simulation Interface Toolkit converts Express XY graphs into regular XY graphs.
- Waveform Chart —You can map waveform charts to any scalar, vector, or matrix signal in the Simulink application software.

The Simulation Interface Toolkit does not support mappings to parameters or signals that have three or more dimensions.

#### Fixing Invalid Mappings

Mappings typically become invalid if the Simulation Interface Toolkit cannot communicate with a model parameter or signal correctly. Additionally, certain simulation options you set in the Simulink application software can cause mappings to become invalid. The following sections provide information about fixing invalid mappings.

##### Models or Host VIs with Broken Mappings

If you create a mapping, generate block diagram code for the host VI, and change the model or front panel in a way that breaks the mapping, the block diagram code of the host VI still references the mapping. To avoid errors, you must launch the **SIT Connection Manager** dialog box, remove or change any erroneous mappings, and generate new block diagram code.

##### Models Using Signal Storage Reuse, Block Reduction Optimization, or Virtual Blocks

Mappings might appear invalid if the model uses either **Signal Storage Reuse** or **Block Reduction Optimization**. These items are options you can set in the Simulink application software to reduce the memory footprint of the model. Disabling these options for the entire model makes all signals available for probing but increases the memory footprint of the model. You can mark individual signals as test points to maintain a reduced memory footprint while keeping certain signals available for probing. To make this change, load the model in the Simulink application software and perform the following actions:

For The MathWorks, Inc. MATLAB[®](/csh?topicname=lvhelp/trademarks.html) application software release 13, right-click a signal and select **Signal properties** from the shortcut menu. Place a checkmark in the **SimulinkGlobal(Test Point)** checkbox and click the **OK** button to save changes.

For the MATLAB application software release 14 and later, right-click a signal and select **Signal properties** from the shortcut menu. Click the **Logging and accessibility** tab, place a checkmark in the **Test point** checkbox, and click the **OK** button to save changes.

|  | Note If you previously converted this model to a model DLL, you must convert the model to a model DLL again after marking signals as test points. |
| --- | --- |

Similarly, you might not be able to probe signals from Virtual Blocks such as Mux, Demux, Bus Selector, and so on. Marking signals from these blocks as test points makes the signals available for probing.

Refer to the Simulink documentation for information about Signal Storage Reuse, Block Reduction Optimization, Virtual Blocks, and test points.

##### Models Using Inline Parameters

You might not be able to manipulate model parameters if that model uses the **Inline parameters** option in the Simulink application software. This option writes a constant value to each model parameter. You must launch the Simulink application software and disable this option so the Simulation Interface Toolkit can manipulate the model parameters. Alternatively, you can mark the variables as tunable as described in the Parameters and Workspace Variables section above.

Refer to the Simulink documentation for information about inline parameters.

##### Models Containing Linked or Masked Subsystems

You can create mappings to parameters and signals of masked subsystems. However, if a subsystem is linked, or linked and masked, any mappings to parameters and signals of that subsystem appear invalid. Refer to the Simulink documentation for information about linked and masked subsystems.

##### Subsystems without Parameters or Signals

If a model contains a subsystem that does not have any parameters or signals, that subsystem appears in the model tree when you create mappings. However, you cannot create mappings to/from that subsystem.

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsitconcepts/sit_c_custfpgarules.html language=enus -->
## TOPIC 00060: Rules for Naming Custom FPGA Bitfiles and VIs (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsitconcepts/sit_c_custfpgarules.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsitconcepts/sit_c_custfpgarules.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Rules for Naming Custom FPGA Bitfiles and VIs (Simulation Interface Toolkit)

[Custom bitfiles and FPGA VIs](../lvsithowto/sit_h_custfpga.html) must have a filename in the following format:

sitfpga Device IO CustomPart .lvbit.

This filename consists of the following components:

- sitfpga defines the VI as a custom FPGA VI for the LabVIEW Simulation Interface Toolkit.
- Device is the FPGA target on which you want to run the simulation. For CompactRIO targets, Device is the type of chassis, for example, cRIO-9103 .
- CustomPart is any custom text you specify.

For example, the filename sitfpga PXI-7831R IO MyFPGA.lvbit specifies this FPGA lvbit file runs on the NI PXI-7831R device.

Additionally, you must place custom bitfiles in the labview\vi.lib\addons\Simulation Interface\_IOTypes\Plugins\NI-FPGA\FPGA Bitfiles directory.

If you do not follow these rules, the [SIT Connection Manager](../lvsit/sit_connection_manager_db.html) dialog box does not recognize the custom FPGA bitfile, and you cannot [create mappings between a model DLL and the FPGA target](../lvsithowto/sit_h_ni_fpga.html).

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsitconcepts/sit_c_design_batch_sim.html language=enus -->
## TOPIC 00061: Designing a Batch Simulation (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsitconcepts/sit_c_design_batch_sim.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsitconcepts/sit_c_design_batch_sim.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Designing a Batch Simulation (Simulation Interface Toolkit)

A batch simulation is a series of simulations that use different initial conditions or parameter values. This topic describes an example batch simulation that executes the sinewave model several times. You can [build this model](../lvsithowto/sit_h_building_a_model.html) or open sinewave.mdl located in the labview\examples\Simulation Interface\Sine Wave\ directory.

Each time this simulation runs, the simulation uses different initial parameter values for the amplitude and frequency of the sine wave.

|  | Windows To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsitconcepts/sit_c_fpgadatatypes.html language=enus -->
## TOPIC 00062: Representing Data Types on FPGA Targets (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsitconcepts/sit_c_fpgadatatypes.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsitconcepts/sit_c_fpgadatatypes.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Representing Data Types on FPGA Targets (Simulation Interface Toolkit)

FPGA targets cannot handle [double-precision, floating-point numbers](/csh?topicname=lvhowto/floating_point_numbers.html) (DBLs). However, Windows computers and real-time (RT) targets often use DBL numbers to perform accurate and precise calculations. To address this compatibility issue, the LabVIEW Simulation Interface Toolkit installs FPGA VIs that represent FPGA I/O connections by using the following data types:

- Signed 16-bit integers (I16) to represent FPGA analog inputs and outputs
- A 1 x 2 array of unsigned 32-bit integers (U32) to represent FPGA pulse width modulation (PWM) inputs and outputs
- Booleans to represent FPGA digital inputs and outputs

After reading a value from an FPGA input, the [driver VI](../lvsitconcepts/sit_c_components_of_a_simulation.html#real_time_components) converts these data types to DBL for more accurate processing on a Windows computer or RT target. Before writing a value to an FPGA output, the driver VI converts these data types back into I16, an array of U32s, or Boolean as appropriate. The driver VI does not convert other data types.

|  | Note The VIs that perform these conversions are located in the labview\\vi.lib\\addons\\Simulation Interface\\driversupportVIs\\Conversion\\ directory. You can eliminate the need for this conversion by configuring the FPGA VI to read and write fixed-point values. The driver VI does not perform any conversion on fixed-point values. |
| --- | --- |

The following sections describe these conversion processes for each type of FPGA input and output.

#### Analog Inputs and Outputs

By default, the driver VI assumes analog inputs have a range of +/- 10 volts. Therefore, when reading analog inputs, the driver VI converts values received from I16 to DBL by using the following formula:

x* 10 / 32767, where x is the value the driver VI reads from the analog input.

For example, if the driver VI reads a value of 20000 from an analog input, the resulting DBL is 6.1037. The driver VI interprets this value as a reading of 6.1037 volts.

When writing to an analog output, the driver VI converts a DBL to I16 representation by using the formula x* 32767 / 10. For example, when writing a value of 4.3659 volts, the driver VI converts this value to 14306 first.

|  | Note If you are using analog inputs or outputs with a range different from +/- 10 volts, these conversions are inaccurate. For example, if you are using an analog input with a range of +/- 60 volts, these conversions are inaccurate by a factor of 6. In this situation, you can use a fixed-point number to ensure that the values are converted exactly as you want. |
| --- | --- |

#### Pulse Width Modulation

When reading PWM inputs as arrays of U32s, the driver VI assumes the first two array elements represent the low and high time, respectively, of a PWM signal. The driver VI then converts these values to a DBL between 0.0 and 1.0, where 0.0 represents a 0% [duty cycle](/csh?topicname=measfunds/dutycycle.html) and 1.0 represents a 100% duty cycle. The driver VI performs this conversion by executing the following steps:

1. Adds the low time to the high time. This sum is called the pulse period.
2. Divides the high time by the pulse period.

For example consider a situation where a driver VI reads a PWM input of [50000 2000000]. The resulting duty cycle is 0.97561, or 97.561%.

When writing to PWM outputs, the driver VI uses the duty cycle and the specified PWM frequency to produce a 1 x 2 array of U32s, where the first element is the low time and the second element is the high time. The driver VI then writes this array to the PWM outputs.

#### Digital Inputs and Outputs

When reading values from a digital input, the driver VI converts TRUE values to a DBL value of 1.0. The driver VI converts FALSE values to a DBL value of 0.0.

When writing values to a digital output, the driver VI converts any non-zero DBL value to TRUE. The driver VI converts a DBL value of 0.0 to FALSE.

#### Fixed-Point Data

You can use fixed-point values in custom FPGA VIs. The driver VI does not perform any conversion on fixed-point values. The value is directly coerced to a to a double without applying any scaling, which gives you the most control over the scale and range of the value. For CompactRIO modules with Analog Inputs or Outputs, use the calibrated mode, which returns the values as calibrated and scaled fixed-point values.

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsitconcepts/sit_c_halting_simulations_on_data_loss.html language=enus -->
## TOPIC 00063: Halting Simulations on Data Loss (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsitconcepts/sit_c_halting_simulations_on_data_loss.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsitconcepts/sit_c_halting_simulations_on_data_loss.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Halting Simulations on Data Loss (Simulation Interface Toolkit)

The [SIT Server](../lvsitconcepts/sit_c_components_of_a_simulation.html) uses buffers to communicate with the [execution host](../lvsitconcepts/sit_c_components_of_a_simulation.html). When these buffers fill up, they behave differently depending on the execution host. If the simulation is not running on a real-time (RT) target, the SIT Server pauses the simulation while the host VI retrieves the necessary data from the buffer. If the simulation is running on an RT target, the SIT Server overwrites data in the buffer. This action results in data loss. When data loss occurs, you might see gaps in front panel indicators, because the SIT Server cannot send the appropriate amount of data to the [host VI](../lvsitconcepts/sit_c_components_of_a_simulation.html).

You can configure how the simulation behaves in the event of data loss. To specify that the simulation halts on data loss, place a checkmark in the **Halt Simulation on Data Loss** checkbox on the **Mappings** page of the [SIT Connection Manager](../lvsit/sit_connection_manager_db.html). The next time the SIT Server loses data from an RT target, the simulation aborts. If you remove the checkmark from this checkbox and click the **Apply** button, the simulation continues uninterrupted despite any data loss. You also can change this setting while the simulation runs from the **Settings** tab of the [Simulation Details](../lvsit/sit_simulation_details_db.html) dialog box.

|  | Note The Halt Simulation on Data Loss checkbox does not affect simulations running on a non-RT target. |
| --- | --- |

#### Reducing the Possibility of Data Loss

You can reduce the possibility of data loss in the following ways:

- Apply a decimation factor to the signals you probe.
- Configure the num data points front panel control of the driver VI using the Driver VI Buffer Settings dialog box.
- Launch The MathWorks, Inc. Simulink ® application software and configure the ordinary differential equation (ODE) solver to take larger time steps. Taking larger time steps slows down the simulation. For example, increasing the time step from 0.001 to 0.01 slows the simulation down by a factor of 10. Refer to the Simulink documentation for more information about changing the time step of a simulation.

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsitconcepts/sit_c_intro.html language=enus -->
## TOPIC 00064: Simulation Interface Toolkit Concepts (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsitconcepts/sit_c_intro.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsitconcepts/sit_c_intro.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Simulation Interface Toolkit Concepts (Simulation Interface Toolkit)

The Simulation Interface Toolkit Concepts book provides an overview of how to use the LabVIEW Simulation Interface Toolkit.

|  | Windows To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsitconcepts/sit_c_labview_simulation_interface_toolkit_help.html language=enus -->
## TOPIC 00065: Simulation Interface Toolkit

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsitconcepts/sit_c_labview_simulation_interface_toolkit_help.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsitconcepts/sit_c_labview_simulation_interface_toolkit_help.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Simulation Interface Toolkit

June 2010, 371504F-01

The LabVIEW Simulation Interface Toolkit interfaces LabVIEW with The MathWorks, Inc. Simulink[®](/csh?topicname=lvhelp/trademarks.html) application software and The MathWorks, Inc. Real-Time Workshop[®](/csh?topicname=lvhelp/trademarks.html) application software in a way that enables you to develop, prototype, and test control systems using models developed in the Simulink simulation environment. You use the Simulation Interface Toolkit to [create a LabVIEW user interface for a model developed in the Simulink simulation environment](../lvsithowto/sit_h_creating_a_host_vi.html) and [run a simulation on a real-time (RT) target](../lvsithowto/sit_h_running_a_simulation.html).

This help file contains:

- Concepts —An overview of how to use the Simulation Interface Toolkit.
- How-To —Step-by-step instructions on accomplishing tasks using the Simulation Interface Toolkit.
- Reference —Detailed information about the Simulation Interface VIs.

Use the NI Example Finder, available by selecting **Help»Find Examples**, to browse examples that show you how to use the Simulation Interface Toolkit. Select **Toolkits and Modules»Simulation Interface** from the example tree on the **Browse** page to find the relevant examples. You must launch the [SIT Server](../lvsitconcepts/sit_c_components_of_a_simulation.html), which starts automatically when you launch The MathWorks, Inc. MATLAB[®](/csh?topicname=lvhelp/trademarks.html) application software, before you can run an example VI.

|  | Note If you installed the MATLAB application software files as read-only, you must modify the matlabrc.m file to launch the SIT Server automatically. |
| --- | --- |

LabVIEW is a graphical programming language that uses icons instead of lines of text to create applications. LabVIEW applications often are called virtual instruments, or VIs, because the appearance and operation of these applications often imitate physical instruments, such as oscilloscopes and multimeters.

Simulink, an add-on toolkit for the MATLAB application software, provides a graphical environment for designing and executing dynamic system models. You can create models in the Simulink software environment using blocks you can customize and graphical wires to specify data flow.

Real-Time Workshop is an add-on package for the Simulink application software that generates C code versions of models from the model diagrams developed in the Simulink simulation environment. Real-Time Workshop then uses a C compiler to compile the C code for execution on RT targets.

© 2002–2010 National Instruments Corporation. All rights reserved.

LabVIEW™, National Instruments™, NI™, ni.com™, NI-CAN™, NI-RIO™, and NI-DAQmx™ are trademarks of National Instruments Corporation. Simulink[®](/csh?topicname=lvhelp/trademarks.html), Real-Time Workshop[®](/csh?topicname=lvhelp/trademarks.html), and MATLAB[®](/csh?topicname=lvhelp/trademarks.html) are registered trademarks of The MathWorks, Inc. Further, other product and company names mentioned herein are trademarks, registered trademarks, or trade names of their respective companies. For patents covering National Instruments products, refer to the appropriate location: **Help»Patents** in the software, the patents.txt file on your CD, or ni.com/patents. You are only permitted to use this product in accordance with the accompanying license agreement. All rights not expressly granted to you in the license agreement accompanying the product are reserved to NI. Further, and without limiting the forgoing, no license or any right of any kind (whether by express license, implied license, the doctrine of exhaustion or otherwise) is granted under any NI patents or other intellectual property right of NI with respect to any other product(s) of NI or of anyone else (including without limitation, the Simulink and the Real-Time Workshop products of The MathWorks, Inc.), including without limitation, the right to use any of these other products.

Where NI software may be used to reproduce software or other materials belonging to others, you may use NI software only to reproduce materials that you may reproduce in accordance with the terms of any applicable license or other legal restriction.

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsitconcepts/sit_c_set_batch.html language=enus -->
## TOPIC 00066: Setting the Initial Conditions for the Batch Simulation (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsitconcepts/sit_c_set_batch.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsitconcepts/sit_c_set_batch.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Setting the Initial Conditions for the Batch Simulation (Simulation Interface Toolkit)

Open the Batch Simulation VI located in the labview\examples\Simulation Interface\Batch Simulation directory. Notice the **Array of parameter values** control, which contains three pairs of initial values for the **Amplitude** and **Frequency** parameters of the model. The **Output** chart displays the results of this batch simulation. Launch The MathWorks, Inc. MATLAB[®](/csh?topicname=lvhelp/trademarks.html) application software and the [SIT Server](../lvsitconcepts/sit_c_components_of_a_simulation.html), then [run the simulation](../lvsithowto/sit_h_running_a_simulation.html) to display the results of this batch simulation.

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsitconcepts/sit_c_supported_ni_hardware.html language=enus -->
## TOPIC 00067: Supported National Instruments Real-Time Hardware (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsitconcepts/sit_c_supported_ni_hardware.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsitconcepts/sit_c_supported_ni_hardware.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Supported National Instruments Real-Time Hardware (Simulation Interface Toolkit)

The LabVIEW Simulation Interface Toolkit supports running a simulation on the following types of National Instruments RT Series hardware.

- PXI/PCI
  - Any PXI-RT controller
- FieldPoint
  - Any FieldPoint or Compact Fieldpoint controller with at least 32 MB of RAM. National Instruments recommends at least 64 MB of RAM. For targets with less than 32 MB of RAM, you should not install VISA if you want to use the SIT server in the driver VI.
- CompactRIO
  - NI cRIO-9961

Refer to the KnowledgeBase for information about configuring hardware devices for use with the Simulation Interface Toolkit.

The following table shows the features available with each type of hardware.

| Feature | NI-CAN Interfaces | NI-DAQ Devices | NI FPGA Targets |
| --- | --- | --- | --- |
| Single-rate models | Yes | Yes | Yes |
| Multi-rate models | Yes | Yes | Yes |
| Single device configurable I/O | Yes | Yes | Yes |
| Multiple device configurable I/O | Yes | Yes | Yes |
| Mixed configurable I/O | Yes | Yes | Yes |
| Custom FPGA VIs | – | – | Yes1 |
| Hardware timing | – | Yes | Yes |
| Analog I/O | Yes2 | Yes | Yes |
| Digital I/O | Yes2 | Yes | Yes |
| Pulse Width Modulation (PWM) I/O | Yes2 | – | Yes |
| Auto-detection of installed devices and I/O modules | Yes | – | Yes |

<sup>1</sup>The Simulation Interface Toolkit ships with bitfiles and FPGA VIs for several National Instruments FPGA targets, including the following targets:

- NI PCI-7811R
- NI PXI-7811R
- NI PCI-7813R
- NI PXI-7813R
- NI PCI-7831R
- NI PXI-7831R
- NI PCI-7833R
- NI PXI-7833R
- NI cRIO-9103

Refer to the *LabVIEW Simulation Interface Toolkit Readme*, located in the labview\readme directory, for the most up-to-date list of installed bitfiles. You can use the LabVIEW FPGA Module to [create custom FPGA VIs](../lvsithowto/sit_h_custfpga.html) for other FPGA targets.

<sup>2</sup>The Simulation Interface Toolkit uses .dbc and/or .ncd files to determine the properties of a particular CAN channel.

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsitconcepts/sit_c_understanding_the_driver_vi.html language=enus -->
## TOPIC 00068: Understanding the Driver VI (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsitconcepts/sit_c_understanding_the_driver_vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsitconcepts/sit_c_understanding_the_driver_vi.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Understanding the Driver VI (Simulation Interface Toolkit)

The [driver VI](../lvsitconcepts/sit_c_components_of_a_simulation.html#real_time_components) contains the code that communicates between the [host VI](../lvsitconcepts/sit_c_components_of_a_simulation.html) and the target on which you run a simulation. This VI consists of a top-level driver VI, modelname_driver.vi, and a support library, modelname_IO.llb. modelname is the name of the [model DLL](../lvsitconcepts/sit_c_components_of_a_simulation.html#real_time_components). These VIs and LLBs exist in the project directory you specified in the [SIT Connection Manager](../lvsit/sit_connection_manager_db.html) dialog box.

|  | Note Refer to the labview\\examples\\Simulation Interface\\Sine Wave\\ directory for an example of this structure. |
| --- | --- |

After you click the **OK** button in the [SIT Connection Manager](../lvsit/sit_connection_manager_db.html) dialog box, the LabVIEW Simulation Interface Toolkit creates a driver VI unique to that simulation. The driver VI contains values you specified for the model, such as timing information, and the [mappings you created](../lvsithowto/sit_h_driver_vi.html) between the model and any I/O hardware on the RT target.

|  | Note You can use the SIT Connection Manager dialog box to generate a driver VI only for certain hardware device configurations. To run a simulation that uses an unsupported hardware configuration, you can create a custom driver VI. |
| --- | --- |

The Simulation Interface Toolkit uses a template, located in the labview\vi.lib\addons\Simulation Interface\_ConnectionManager\scriptdriver\templates directory, to create this driver VI. This template creates a top-level driver VI that executes the following steps:

1. Initializes the model DLL .
2. Starts the SIT Server on the RT target.
3. Initiates data logging and playback.
4. Configures timing parameters .
5. Calls the IO Base Rate Loop VI , which transfers data to and from the hardware inputs and outputs.
6. Finalizes the model DLL .

#### The Front Panel of the Driver VI

The front panel of the driver VI contains the following controls that affect the simulation.

|  | Note To save the current value of a control as a default value, right-click the control and select Data Operations»Make Current Value Default. Setting default values ensures you do not have to edit the driver VI each time you run the same simulation. You can configure the following options by using the Driver VI Buffer Settings dialog box. |
| --- | --- |

- number of signals —Specifies the maximum number of signals that the simulation probes. For example, if you know that a model only has ten signals, set the value of this control to 10 . The default value for this control is 50 .
- num data points —Specifies the maximum width of the data buffer that probes the model signals. The total width of all the signals you want to probe must be less than or equal to the width of this data buffer. The width of a signal is equal to the total number of elements in a signal. The default value of this control is 100 .
 
 For example, a 2×2 array has a width of 4. If you want to probe 25 of these signals, the total width equals 100. Because 100 is the width of the data buffer, the driver VI probes all the signals. If you added a 26 th signal to probe, the total width equals 104, which exceeds the width of the data buffer. The simulation does not return probed data for the 26 th signal.
 The num data points control has a large impact on the performance of the simulation. If you set the value of num data points too high, the Simulation Interface Toolkit allocates buffer space for signals that do not exist. This allocation wastes system resources and reduces the ability of the simulation to execute in real time. If you set the value of num data points too low, you cannot probe all the signals you want to. To maximize simulation performance, determine the maximum width of model signals that you want to probe in one time step. Then, set num data points to the lowest possible value. You also can improve simulation performance by decimating the simulation data .
- circular buffer size —Specifies the depth of the data buffer. The default value for this control is 1000 .
- Start Server? —Specifies if the SIT Server starts when you run the simulation. If you set this switch to FALSE, you cannot use the host VI to communicate with the simulation. In this situation, the driver VI starts the simulation immediately on execution. The default value of this switch is TRUE, which allows you to use the host VI to communicate with the simulation. In this situation, the driver VI waits for the Run command from the host VI before starting the simulation.

#### The IO Base Rate VI

The block diagram of the driver VI includes the IO Base Rate Loop VI, which is circled in the following figure.

[IMAGE alt='image' src='bd_sit_single_driver_template.gif']

Like the driver VI, the Simulation Interface Toolkit creates the IO Base Rate Loop VI from a template in the labview\vi.lib\addons\Simulation Interface\_ConnectionManager\scriptdriver\templates directory. The IO Base Rate template is sit Base Rate Loop.vi. This template creates a VI named modelname_IO IO Base Rate Loop.vi.

The IO Base Rate Loop VI contains the following four custom VIs:

- modelname _IO IO Init.vi
- modelname _IO IO Read.vi
- modelname _IO IO Write.vi
- modelname _IO IO Close.vi

|  | Note The templates for these VIs also are located in the labview\\vi.lib\\addons\\Simulation Interface\\_ConnectionManager\\scriptdriver\\templates directory |
| --- | --- |

If you previously created a driver VI, the Simulation Interface Toolkit generates these VIs when you click the **OK** button on the [SIT Connection Manager](../lvsit/sit_connection_manager_db.html) dialog box. The block diagram code in these VIs depends on the [mappings you create between the model DLL and any hardware devices](../lvsithowto/sit_h_driver_vi.html). If you did not previously create a driver VI, the Simulation Interface Toolkit uses a template for the VIs.

The following figure shows these VIs, circled from left to right, on the block diagram of the IO Base Rate Loop VI.

[IMAGE alt='image' src='bd_base_rate_loop.gif']

The IO Base Rate Loop VI uses these four VIs to execute the following steps:

1. Initialize the simulation.
2. Execute the following steps for the duration of the simulation.
  1. Read data from the hardware inputs.
  2. Run the SIT Scheduler VI, which takes the hardware input values, runs a single step of the simulation, and receives output values from the simulation.
  3. Probe the values of the model DLL and send these values to the SIT Server.
  4. Write the values the model DLL returns to the hardware outputs.
  5. Perform any commands the host VI sends.
3. Free hardware resources after the simulation finishes.

#### How the Driver VI Schedules Simulations

Single-rate simulations use only the IO Base Rate Loop, located on the block diagram, to control the timing of the simulation. However, multirate simulations use additional [Timed Loops](/csh?topicname=glang/timed_loop.html). Because each model task might have a different time step, the Scheduler Loop runs at the base rate of the simulation, which is the greatest common divisor of all the discrete time steps in the simulation. For example, if a multirate simulation contains two discrete tasks, one with a time step of 100 microseconds and one with a time step of 500 microseconds, the base rate is 100 microseconds. The Scheduler Loop then uses 100 microseconds as the time step of the simulation.

The Simulation Interface Toolkit uses rate-monotonic scheduling to prioritize different model tasks in the same model. Rate-monotonic scheduling gives higher priority to model tasks that have shorter time steps. A higher-priority task can interrupt a lower-priority task.

To view detailed information about each task in a multirate simulation, run the host VI and click the **Simulation Details** front panel button to launch the [Simulation Details](../lvsit/sit_simulation_details_db.html) dialog box.

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsitconcepts/sit_related_documentation.html language=enus -->
## TOPIC 00069: Related Documentation (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsitconcepts/sit_related_documentation.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsitconcepts/sit_related_documentation.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Related Documentation (Simulation Interface Toolkit)

The following documents contain information that you might find helpful as you use the Simulation Interface Toolkit.

- LabVIEW Simulation Interface Toolkit Readme —This document provides system requirements, installation instructions, and late-breaking information about the version of the Simulation Interface Toolkit that you are installing. The readme_SIT.html file is located in the LabVIEW\readme directory.
- Getting Started with LabVIEW—This manual contains an in-depth introduction to LabVIEW, including several tutorials that showcase LabVIEW features.
- The LabVIEW Real-Time Module documentation.
- The LabVIEW FPGA Module documentation.
- The documentation for any hardware devices you want to use with a simulation.
- The MathWorks, Inc. Simulink ® documentation.
- The MathWorks, Inc. MATLAB ® documentation.
- The MathWorks, Inc. Real-Time Workshop ® documentation.
- LabVIEW Simulation Interface Toolkit Example VIs —Refer to the labview\examples\Simulation Interface\ directory for example VIs that demonstrate common tasks using the LabVIEW Simulation Interface Toolkit. You also can access these VIs by selecting Help»Find Examples and selecting Toolkits and Modules»Simulation Interface Toolkit in the NI Example Finder window.

You must have Adobe Reader 6.0.1 or later installed to view or [search](/csh?topicname=lvhowto/searching_pdfs.html) the PDF versions of these manuals.

Refer to the Adobe Systems Incorporated Web site to download Acrobat Reader. Refer to the National Instruments Product Manuals Library for updated documentation resources.

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsithowto/sit_h_building_a_driver_vi_startup_application.html language=enus -->
## TOPIC 00070: Building a Driver VI Startup Application (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsithowto/sit_h_building_a_driver_vi_startup_application.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsithowto/sit_h_building_a_driver_vi_startup_application.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Building a Driver VI Startup Application (Simulation Interface Toolkit)

Complete the following steps to create a driver VI and model DLL for a standalone startup application on a real-time (RT) target. To complete these steps, you must install the LabVIEW Real-Time Module and the LabVIEW Application Builder add-on. The Application Builder comes with the LabVIEW Professional Development System. You also can purchase the Application Builder as an add-on for the LabVIEW Full Development System.

First, [convert the model to a model DLL](../lvsithowto/sit_h_convert_model_to_dll.html). Then complete the following steps:

1. Open the driver projected <model>_Driver.lvproj.
2. Expand the RT target in the Project Explorer window.
3. Add the model DLL to the RT Target.
4. Right-click Build Specifications , and select New»Real-Time Application from the shortcut menu.
5. Select the driver VI as the top-level VI and add the model DLL as a support file.
6. On the Destinations page change the Support Directory to c:\ni-rt\system .
7. Click the OK button to create the build specification.
8. Right-click the new build specification and select Set as startup from the shortcut menu.
9. Right-click the new build specification and select Deploy from the shortcut menu. After the deployment process is complete, restart the RT target.

You can communicate with the simulation at any time by [specifying the RT target](../lvsithowto/sit_h_specify_dll_and_host.html) and running the host VI.

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsithowto/sit_h_building_a_model.html language=enus -->
## TOPIC 00071: Building a Model (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsithowto/sit_h_building_a_model.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsithowto/sit_h_building_a_model.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Building a Model (Simulation Interface Toolkit)

Complete the following steps to build a [model](../lvsitconcepts/sit_c_components_of_a_simulation.html) in The MathWorks, Inc. Simulink[®](/csh?topicname=lvhelp/trademarks.html) application software that generates a sine wave.

|  | Note You can find an example of this model in the labview\\examples\\Simulation Interface\\Sine Wave directory. |
| --- | --- |

1. Launch the The MathWorks, Inc. MATLAB ® application software on the host computer . The command window displays the following message: Starting the SIT Server on Port 6011 
 SIT Server started 
 This message indicates that the SIT Server is running.
2. Enter simulink in the command window to launch the Simulink® Library Browser window.
3. Place a Sine Wave block, located in the Math Operations library, in a new model window.
4. Place an In1 block, located in the Sources library, in the model window.
5. Place a Sum block, located in the Math Operations library, in the model window.
6. Place an Out1 block, located in the Sinks library, in the model window.
7. Place a SignalProbe block, located in the NI SIT Blocks library, in the model window. [IMAGE alt='image' src='note.gif']
**Note** The LabVIEW Simulation Interface Toolkit uses the SignalProbe block to probe the signals in the model. The SignalProbe block must be on the top level of the model hierarchy. You can have only one SignalProbe block per model file. Do not rename the SignalProbe block. Do not change the name of another model block to SignalProbe. If you installed the MATLAB application software files as read-only, you must [modify](../lvsitconcepts/sit_c_communicating_with_the_sit_server.html) the matlabrc.m file to see the SignalProbe block in the **Simulink Library Browser** window.
8. Wire the sources, functions, and signals together so the model looks like the diagram in the following figure: [IMAGE alt='image' src='simulinkmodel.gif']
9. Save the model as sinewave.mdl to an easily accessible location.

#### Setting Simulation Options

Complete the following steps to change simulation options in the Simulink application software.

1. For the MATLAB application software release 13, select Simulation»Simulation parameters to launch the Simulation Parameters dialog box. For the MATLAB application software release 14 and later, select Simulation»Configuration Parameters to launch the Configuration Parameters dialog box.
2. Click the Solver tab.
3. Enter inf in the Stop time text box. inf specifies that the simulation runs until you stop the simulation.
4. Set the Type option to Fixed-step in the Solver Options section.
5. Click the OK button to return to the Simulink application software window.
6. Save the model.

The LabVIEW Simulation Interface Toolkit might not be able to probe signals from models that use Signal Storage Reuse or Block Reduction Optimization. Additionally, the Simulation Interface Toolkit might not be able to probe signals that originate from Virtual Blocks. If the model uses any of these options or blocks, you can [mark individual signals as test points](../lvsitconcepts/sit_c_creating_mappings.html#broken_mappings). Refer to the Simulink documentation for information about these and other simulation options you can set.

|  | Note You can see a completed version of sinewave.mdl in the labview\\examples\\Simulation Interface\\Sine Wave\\ directory. |
| --- | --- |

|  | Next StepCreating a Host VI or Converting a Model into a Model DLL |
| --- | --- |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsithowto/sit_h_configuring_a_simulation.html language=enus -->
## TOPIC 00072: Configuring a Simulation (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsithowto/sit_h_configuring_a_simulation.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsithowto/sit_h_configuring_a_simulation.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Configuring a Simulation (Simulation Interface Toolkit)

Configuring a simulation that does not run on a real-time (RT) target involves the following steps:

1. Build a model .
2. Create a host VI .
3. Run the simulation .

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsithowto/sit_h_configuring_sim_rt.html language=enus -->
## TOPIC 00073: Configuring a Simulation on a Real-Time Target (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsithowto/sit_h_configuring_sim_rt.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsithowto/sit_h_configuring_sim_rt.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Configuring a Simulation on a Real-Time Target (Simulation Interface Toolkit)

The LabVIEW Simulation Interface Toolkit supports hardware-in-the-loop (HIL) testing using [supported National Instruments RT Series hardware](../lvsitconcepts/sit_c_supported_ni_hardware.html). You must install the LabVIEW Real-Time Module in order to execute a simulation on an RT target. Refer to the KnowledgeBase for information about configuring hardware devices for use with the Simulation Interface Toolkit.

|  | Note You also can execute a model DLL on a Windows computer. For example, you can install a National Instruments DAQ device in a Windows computer and execute a simulation using that device. |
| --- | --- |

Configuring a simulation on a real-time (RT) target involves the following steps:

1. Build a model .
 [IMAGE alt='image' src='note.gif']
**Note** In order to communicate with RT Series hardware, the model must have at least one input port and one output port.
2. Create a host VI with controls and indicators.
3. Convert the model to a model DLL .
4. Specify the model, model DLL, and execution host .
5. Create a driver VI .
6. Run the simulation . When you run the simulation, the Simulation Interface Toolkit downloads the necessary files to the RT target.

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsithowto/sit_h_controlling_a_simulation.html language=enus -->
## TOPIC 00074: Controlling a Simulation (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsithowto/sit_h_controlling_a_simulation.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsithowto/sit_h_controlling_a_simulation.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Controlling a Simulation (Simulation Interface Toolkit)

After you have created the necessary model, host VI, model DLL, and/or
 driver VI, you can run the simulation. While the simulation is [running](../lvsithowto/sit_h_running_a_simulation.html), you can control the simulation by [editing the value of multiple parameters at once](../lvsithowto/sit_h_emp.html), [modifying mappings](../lvsithowto/sit_h_modifying_mappings.html), and [decimating data the simulation returns](../lvsithowto/sit_h_decimating_simulation_data.html). You also can [log simulation data](../lvsithowto/sit_h_logging_simulation_data.html).

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsithowto/sit_h_convert_model_to_dll.html language=enus -->
## TOPIC 00075: Converting a Model into a Model DLL (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsithowto/sit_h_convert_model_to_dll.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsithowto/sit_h_convert_model_to_dll.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Converting a Model into a Model DLL (Simulation Interface Toolkit)

Complete the following steps to convert a [model](../lvsitconcepts/sit_c_components_of_a_simulation.html) into a [model DLL](../lvsitconcepts/sit_c_components_of_a_simulation.html#real_time_components). You can convert models that use only a fixed step-size ordinary differential equation (ODE) solver. Additionally, you must turn off data logging in The MathWorks, Inc. Simulink[®](/csh?topicname=lvhelp/trademarks.html) application software and instead log simulation data using the **Data Logging** page of the [SIT Connection Manager](../lvsit/sit_connection_manager_db.html) dialog box. Refer to the Simulink documentation for information about using the Simulink application software to change the ODE solver of a model and turn off data logging.

|  | Note If you do not have a compiler set up to compile the C code, or if you have set up an unsupported compiler, you must run mex -setup in the The MathWorks, Inc. MATLAB® application software before converting a model into a model DLL. |
| --- | --- |

1. Launch the Simulink application software and load the model you want to convert.
2. For the MATLAB application software release 13, select Simulation»Simulation parameters to launch the Simulation Parameters dialog box. For the MATLAB application software release 14 and later, select Simulation»Configuration Parameters to launch the Configuration Parameters dialog box.
3. Click the Real-Time Workshop tab.
4. Click the Browse button to launch the System Target File Browser dialog box.
5. Select nidll.tlc—NI Real-Time Target from
 the list.
6. Click the OK button.
7. Click the Build button in the Category section to begin building the model DLL. The MATLAB command window displays the status of the build process. The following message in the MATLAB command window indicates that Real-Time Workshop ® has completed building the model DLL. ### Successful completion of Real-Time Workshop build procedure for model: ModelName

After Real-Time Workshop builds a model DLL, the LabVIEW Simulation Interface Toolkit places the model DLL in a directory named <ModelName>_nidll_rtw, which is located in the current working directory. The Simulation Interface Toolkit also generates a text file, <ModelName>_portsReadme.txt, which specifies the lengths and positions of all model input and model output array data.

#### Including External Source Code in a Model DLL

If the model you are converting specifies any .c or .h files, you must specify the locations of these files so the Simulation Interface Toolkit includes the code in the model DLL. Both of these changes require editing the makefile nidll_vc.tmf, which is located in the C:\SimulationInterfaceToolkit\ModelInterface\tmw\ directory.

Complete the following steps to specify a directory containing .h files a model uses.

1. Open nidll_vc.tmf in any text editor.
2. Locate the line that reads USER_INCLUDES = .
3. Add directory paths, separated by spaces, between the quotes. For example, USER_INCLUDES ="-Ic:\source1 -Ic:\source2" .
4. Save the file and close the text editor.

Complete the following steps to specify any .c files a model uses.

1. Open nidll_vc.tmf in any text editor.
2. Locate the line that reads USER_SRCS = .
3. Add file locations, separated by spaces, between the quotes. For example, USER_SRCS ="c:\source1\mySource1.c c:\source2\mySource2.c" .
4. Save the file and close the text editor.

Refer to the Real-Time Workshop documentation for more information about makefiles and how Real-Time Workshop generates C code.

| Previous StepBuilding a Model | Next StepCreating a Host VIor Specifying the Model DLL and Execution Host |
| --- | --- |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsithowto/sit_h_creating_a_host_vi.html language=enus -->
## TOPIC 00076: Creating a Host VI (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsithowto/sit_h_creating_a_host_vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsithowto/sit_h_creating_a_host_vi.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Creating a Host VI (Simulation Interface Toolkit)

Complete the following steps to create a [host VI](../lvsitconcepts/sit_c_components_of_a_simulation.html) and map it to a model or model DLL.

|  | Note For demonstration purposes, this procedure uses the sinewave.mdl file you created in the Building a Model procedure. You can follow a similar process to create host VIs for your other model files or model DLLs. |
| --- | --- |

#### Creating the Front Panel of the Host VI

Complete the following steps to create the front panel of a host VI for the sinewave model.

1. Launch LabVIEW on the host computer .
2. Create a new blank VI.
3. Add two knob controls to the front panel. Label the first control Amplitude and the second control Frequency .
4. Add a waveform chart indicator to the front panel and label the indicator Sine Wave . The front panel of the host VI resembles the following figure: [IMAGE alt='image' src='sinewavefp.gif']

#### Creating Mappings between the Host VI and the Model

Complete the following steps to create mappings between the host VI and the sinewave model.

1. From the host VI, select Tools»SIT Connection Manager to launch the SIT Connection Manager dialog box. You use this dialog box to establish mappings between LabVIEW controls/indicators and model parameters/signals. This dialog box also contains options for the simulation such as data logging .
2. Under Execution Host , select Simulation Environment . 
 [IMAGE alt='image' src='note.gif']
**Note** The [execution host](../lvsitconcepts/sit_c_components_of_a_simulation.html) is the machine on which the SIT Server is running. If you want to select **Real-Time Target** or **Driver VI on Localhost**, you must [convert your model to a model DLL](../lvsithowto/sit_h_convert_model_to_dll.html) before you can create mappings.
3. Click the Browse button next to the Current Model field to navigate to the sinewave.mdl file. A copy of this file is located in the labview\examples\Simulation Interface\Sine Wave\ directory.
4. Click the OK button. The Current Model file path indicator updates to show the path to sinewave.mdl .
5. From the Category list, select Mappings to display the Mappings page. The Current Mappings table displays the controls and indicator you created.
6. Select the Amplitude control and click the Change Mapping button to display the Specify Parameter(s) for Control dialog box. You also can access this dialog box by double-clicking the row containing the Amplitude control.
7. Select Amplitude from the sinewave»Sine Wave tree and click the OK button to map the knob to the Amplitude parameter of the Sine Wave block and return to the SIT Connection Manager dialog box. The Mapped Parameter/Signal column updates to show the mapping you just created.
8. Map the Frequency knob to the Frequency parameter of the Sine Wave block.
9. Double-click the row containing the Sine Wave indicator to display the Specify Signal(s) for Indicator dialog box. This dialog box contains model signals, whereas the Specify Parameter(s) for Control dialog box contains model parameters.
10. Double-click Port 1 under the sinewave»Sine Wave tree to create the mapping and return to the SIT Connection Manager dialog box. 
 [IMAGE alt='image' src='note.gif']
**Note** To remove a mapping, select a row in the mappings table and click the **Remove Mapping** button. To change a mapping, select a row in the mappings table and click the **Change Mapping** button.
11. Click the OK button to close the SIT Connection Manager dialog box and generate the block diagram code for the host VI. If you have not saved the host VI already, LabVIEW prompts you for a location to save the host VI. You do not need to edit this code because the generated code already contains the necessary VIs and functions to interact with sinewave.mdl .
12. Save the host VI as Sine Wave.vi . 
 [IMAGE alt='image' src='note.gif']
**Note** You can see a completed version of Sine Wave.vi in the labview\examples\Simulation Interface\Sine Wave\ directory.

| Previous StepBuilding a Model or Converting a Model into a Model DLL | Next StepRunning a Simulation |
| --- | --- |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsithowto/sit_h_custfpga.html language=enus -->
## TOPIC 00077: Creating a Custom FPGA Bitfile (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsithowto/sit_h_custfpga.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsithowto/sit_h_custfpga.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Creating a Custom FPGA Bitfile (Simulation Interface Toolkit)

The LabVIEW Simulation Interface Toolkit ships with FPGA bitfiles for many National Instruments R Series Intelligent DAQ devices. These VIs and bitfiles define the analog, digital, and pulse width modulation (PWM) inputs and outputs of the FPGA target. You use this information to [create mappings between a model DLL and one or more FPGA targets](../lvsithowto/sit_h_ni_fpga.html). The Simulation Interface Toolkit also ships with a project file you can use with the NI cRIO-9103 chassis.

These default bitfiles are sufficient for many applications. However, in some situations, you might need to create a custom FPGA bitfile to use with a simulation. For example, if you want to use additional digital I/O lines, more than two PWM outputs, or digital filtering built into the FPGA, you must create a custom bitfile. If you are running a simulation on a CompactRIO chassis, you also must create a custom bitfile, because CompactRIO chassis do not contain any built-in I/O modules. You must install the LabVIEW FPGA Module to create these files.

The following sections provide information about creating a custom FPGA bitfile.

Creating a custom FPGA bitfile includes the following three steps:

- Make a Copy of the Sample FPGA VI and Project
- Customize the FPGA VI
- Compile the FPGA VI into a Bitfile

#### Making a Copy of the Sample FPGA VI and Project

The first step is to make a copy of a default FPGA VI and project. This step is different depending on whether you are using an R Series device or a CompactRIO chassis.

##### R Series Devices

1. Browse to the labview\vi.lib\addons\Simulation Interface\_IOTypes\Plugins\NI-FPGA\FPGA IO Source\ directory.
2. Create a copy of sitfpga IO.lvproj and place this copy in this same directory.
3. Open this copy in LabVIEW.
4. Expand the My Computer item in the Project Explorer window.
5. Expand the PXI-7831R (PXI-7831R) item in the Project Explorer window. This example project defines a PXI-7831R device as the target. If you are using this configuration, proceed to step 6. If you are using a different configuration, you must create a new FPGA target for the device. In this situation, complete the following steps to add a new R Series device to the project.
  1. Right-click the target that controls the R Series device and select New»Targets and Devices from the shortcut menu.
  2. Select the New target or device option in the Targets and Devices dialog box.
  3. Select the device type from the list and click the OK button.
  4. In the Project Explorer window, click and drag sitfpga master.vi from the PXI-7831R (PXI-7831R) target to the new target.
  5. Refer to Using the FPGA I/O Node (FPGA Module) for information about adding I/O to the project.
6. Double-click sit IO.vi in the Project Explorer window to open it.
7. Select File»Save As from the pull-down menu of the sit IO VI window.
8. Ensure the Substitute copy for original option is selected and click the Continue button.
9. Rename the VI and save it to the labview\vi.lib\addons\Simulation Interface\_IOTypes\Plugins\NI-FPGA\FPGA IO Source\ directory.
10. Save the project by clicking the Save button in the Project Explorer window.

The next step is [customizing the FPGA VI](#rules).

##### CompactRIO Chassis

1. Browse to the labview\vi.lib\addons\Simulation Interface\_IOTypes\Plugins\NI-FPGA\FPGA IO Source\ directory.
2. Create a copy of sitfpga cRIO IO.lvproj and place this copy in this directory.
3. Open this copy in LabVIEW.
4. Expand the FPGA Target (cRIO-9103) item in the Project Explorer window. This example project defines a cRIO-9103 chassis as the target. If you are using this configuration, proceed to step 6. If you are using a different chassis, you must create a new FPGA target for this chassis. In this situation, complete the following steps to add a new CompactRIO chassis to the project.
  1. Right-click the project root in the Project Explorer window and select New»Targets and Devices from the shortcut menu.
  2. Select the New target or device option in the Targets and Devices dialog box.
  3. Select the CompactRIO chassis type from the list and click the OK button.
  4. In the Project Explorer window, click and drag sit IO cRIO.vi from the FPGA Target (cRIO-9103) target to the new target.
5. Double-click sit IO cRIO.vi in the Project Explorer window.
6. Select File»Save As from the pull-down menu.
7. Ensure the Substitute copy for original option is selected and click the Continue button.
8. Rename the VI and save it to the labview\vi.lib\addons\Simulation Interface\_IOTypes\Plugins\NI-FPGA\FPGA IO Source\ directory.
9. Save the project by clicking the Save button in the Project Explorer window.

The next step is [customizing the FPGA VI](#rules).

#### Customizing the FPGA VI

The process of creating the custom FPGA VI differs depending on the hardware devices you are using. Refer to the FPGA Module documentation for information about
 creating FPGA VIs and bitfiles for an FPGA target.

The default project defines the following FPGA I/O items for the PXI-7831R device: analog input channels 0–7, analog output channels 0–7, and digital lines 0–39 on both connectors 1 and 2 and digital line 0—15 on connector 0. You can add or remove FPGA I/O items depending on the device and the needs of the simulation. For example, the PXI-7811R device has 160 DIO lines available; however, by default this sample FPGA VI uses only the first 40 lines on connectors 1 and 2. You can add more FPGA I/O items to this project if you want to use the additional DIO lines available on the PXI-7811R. Conversely, the PXI-7811R has no analog inputs or outputs, so if you are using this device, you can remove the analog I/O items from the project and the corresponding FPGA I/O Nodes from the FPGA VI.

Similarly, the default sample FPGA VI defines the digital lines on connector 0 as 8 PWM inputs and 8 PWM outputs. You might want more or fewer PWM channels. You might also add other custom I/O not defined in the sample FPGA VI.

|  | Note The driver VI converts analog, digital, and PWM information to double-precision, floating-point numbers for greater accuracy and precision on Windows computers and RT targets. You can avoid this conversion by creating an FPGA VI that transmits this information by using fixed-point numbers. For more information about how SIT handles data types on FPGA, refer to Representing Data Types on FPGA Targets. |
| --- | --- |

If you created a new target for an R Series device, you can drag the FPGA I/O folders from the original **PXI-7831R (PXI-7831R)** target to the new target. The FPGA VI shows broken wires from any FPGA I/O Nodes with undefined channels.

(CompactRIO Chassis) If you are using the existing cRIO-9103 target, the project defines an NI 9215 module for analog input, an NI 9263 module for analog output, an NI 9411 module for digital input, and an NI 9474 module for digital output. You can delete or modify these modules based on the ones you are using for the simulation. If you need to add modules to the target, or if you created a new target, you can add the necessary modules by right-clicking the target and selecting **New»C Series Modules**.

|  | Note In the sit IO cRIO.vi example, the FPGA I/O mode calibrates the analog input and analog output channels of the NI 9215 and NI 9263 modules. The host VI running on the CompactRIO real-time controller returns the data as a scaled fixed-point value. |
| --- | --- |

|  | Note Refer to the National Instruments Web site for information about these devices and modules. |
| --- | --- |

While you are creating/modifying the FPGA VI, pay attention to the following guidelines to ensure the [SIT Connection Manager](../lvsit/sit_connection_manager_db.html) dialog box recognizes this FPGA VI.

- Do not modify, remove, or rename any objects in the gray areas of the sample FPGA VI.
- As you create controls and indicators to represent FPGA I/O connections, do not begin the name of these new objects with an underscore or asterisk. The SIT Connection Manager dialog box ignores any objects with an underscores or asterisks at the beginning of the name. Conversely, if you want use a control or indicator as an intermediate value, such as those in the PWM I/O loops, prepend an underscore to the name of these objects. This underscore ensures the user does not see the object as available for a mapping.
- Do not use the following control indicator names : Loop Rate (used), Loop Rate (ticks), Late? Latched, Reset, Start 0, Local Stop 0, _IRQ Bit (0—31), _Master3, _use RTSI).
- Add PWM I/O by copying and renaming an existing PWM control or indicator. For example, the two default PWM input controls are named PWM in 0 (C 0 DIO 0) and PWM in 1 (C 0 DIO 1) . A third PWM input must be named PWM in 2 (C *connector number* DIO *DIO line number* ) .
- National Instruments recommends that you start control names with AI for analog in, AO for analog out, and so on.

When you are finished creating the FPGA VI, select **File»Save** to save this VI.

The next step is compiling the custom FPGA VI into a bitfile.

#### Compiling the Custom FPGA VI into a Bitfile

Complete the following steps to compile the custom FPGA VI and create the bitfile.

1. Display the Project Explorer window.
2. Right-click the FPGA VI in the tree and select Compile from the shortcut menu to compile the FPGA VI. LabVIEW then creates a bitfile for this VI.
3. Copy the resulting bitfile to the labview\vi.lib\addons\Simulation Interface\_IOTypes\NI FPGA\FPGA IO VIs\FPGA Bitfiles\ directory. The compiler places the bitfile in a subdirectory, FPGA Bitfiles ,relative to the project file directory. By default, the bitfile name is name of project_name of FPGA VI .lvbit .
4. Rename the bitfile according to the rules for naming custom bitfiles .

The next step is using the **SIT Connection Manager** dialog box to create mappings between the model DLL and the FPGA target.

#### Using the Custom FPGA VI with the SIT Connection Manager

As you [create mappings](../lvsithowto/sit_h_ni_fpga.html), you associate the custom FPGA bitfile you created with the appropriate FPGA target. You then can create mappings between the model DLL and the FPGA target using the custom FPGA VI you created.

|  | Tip If the bitfile does not show up, it is likely that it does not follow the naming conventions listed above or that it is not in the correct directory. |
| --- | --- |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsithowto/sit_h_customdrivervi.html language=enus -->
## TOPIC 00078: Creating a Custom Driver VI (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsithowto/sit_h_customdrivervi.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsithowto/sit_h_customdrivervi.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Creating a Custom Driver VI (Simulation Interface Toolkit)

You can use the LabVIEW Simulation Interface Toolkit to run a simulation on a National Instruments real-time (RT) controller by [creating a driver VI](../lvsithowto/sit_h_driver_vi.html). A driver VI contains mappings between a [model DLL](../lvsitconcepts/sit_c_components_of_a_simulation.html#real_time_components) and a variety of National Instruments [FPGA](../lvsithowto/sit_h_ni_fpga.html), [CAN](../lvsithowto/sit_h_ni_can.html), and [DAQ](../lvsithowto/sit_h_ni_daq.html) devices. You can use the [SIT Connection Manager](../lvsit/sit_connection_manager_db.html) dialog box to create a driver VI for many [supported hardware configurations](../lvsitconcepts/sit_c_supported_ni_hardware.html).

If you want to run a simulation using a hardware configuration that this dialog box does not support, you can create a custom driver VI to support that configuration. For example, you need a custom driver VI in the following situations:

- You want to run a simulation that uses RS232 (serial), GPIB, third-party, or custom I/O hardware devices.
- You want to add extended capabilities to the driver VI.

|  | Note This topic assumes you are familiar with the architecture and operation of the driver VI. If you are using third-party or custom hardware devices, this topic assumes you already have a compatible RT driver for that hardware and that you know how to write LabVIEW code to interface with that hardware device. |
| --- | --- |

You can customize the driver VI and still use the **SIT Connection Manager** dialog box to change [mappings](../lvsitconcepts/sit_c_creating_mappings.html) between LabVIEW controls/indicators and model parameters/signals. You can create and maintain one driver VI per DLL for use with different models and hardware configurations. LabVIEW saves any changes you make to the driver VI when you rebuild the driver VI, with the following exceptions:

- LabVIEW does not preserve changes to controls with green labels.
- LabVIEW does not preserve changes to the four I/O VIs.
- LabVIEW does not preserve changes to the project if you select a new target type.
- LabVIEW does not preserve changes to IP addresses or target aliases.

#### Adding Custom I/O to the Driver VI

You can add I/O that is not supported by the **SIT Connection Manager** dialog box to the driver VI. Adding I/O is useful if you want to use a combination of National Instruments hardware devices with serial, third-party, or custom hardware devices.

|  | Note To create a custom driver VI, you must correctly index into the pre-sized data array, which is where the Simulation Interface Toolkit places data from I/O channels. Refer to the modelname _portsReadme.txt file, located in the model DLL build directory, for a list of the ordering and widths of all model inputs and outputs. The index number of these arrays is the sum of the width of all previous elements. For example, the index number of element 3 equals the width of element 2 plus the width of element 1. |
| --- | --- |

Adding I/O involves creating four VIs: one each that initializes, reads from, writes to, and closes the custom hardware. You then place these VIs on the block diagram of the generated [IO Base Rate Loop VI](../lvsitconcepts/sit_c_understanding_the_driver_vi.html#blockdiagram).

For example, you can use the **SIT Connection Manager** dialog box to create the part of the driver VI that uses National Instruments FPGA target. If you modify the driver VI to contain four custom VIs that interact with a serial device, you still can change the FPGA mappings by using the **SIT Connection Manager** dialog box. These changes do not affect the four custom VIs, even if you generate the driver VI again.

|  | Note You also can edit the template VIs in the labview\\vi.lib\\addons\\Simulation Interface\\_Connection Manager\\scriptdriver\\templates. However, if you edit the template VIs, each time you generate a new driver VI the driver VI contains the modified template VIs. Before you edit the template VIs, browse to the labview\\vi.lib\\addons\\Simulation Interface\\_Connection Manager\\scriptdriver\\templates directory and make a backup copies of SIT Driver.vi and sit Base Rate Loop.vi. These VIs are templates LabVIEW uses when you generate a new driver VI. This file is the IO Base Rate Loop VI template. National Instruments recommends you maintain a copy of the original template. |
| --- | --- |

As you create these VIs, you might want to create a [type definition](/csh?topicname=lvconcepts/custom_cont_ind_type.html) to pass resource names, control parameters the hardware needs, VISA resource names, and/or DAQmx Task Name controls between these four VIs. This setup is similar to how the modelname _IO IO Ref.ctl type definition, which the **SIT Connection Manager** dialog box uses, works.

After you create these VIs, place each one on the block diagram of the generated IO Base Rate Loop VI. Place each custom VI in the appropriate [Sequence structure](/csh?topicname=glang/sequence_structure.html). Wire the custom VIs to maintain the data flow already present in the generated VI. For example, make sure the custom VIs share the same error cluster as the generated VIs.

The following figure shows the I/O Base Rate Loop VI before placing the custom VIs on the block diagram. The VIs with the **SIT I/O** icons are the VIs that LabVIEW generates.

[IMAGE alt='image' src='bd_template_beforeadd.gif']

The following figure shows the IO Base Rate Loop VI after you place the custom VIs on the block diagram. National Instruments recommends that you place custom VIs in the empty Sequence structures on the block diagram. However, you can place custom VIs anywhere on the block diagram. Three of the four custom VIs are circled.

[IMAGE alt='image' src='bd_template_afteradd.gif']

In the previous figure, notice how each custom VI is in a Sequence structure. This method ensures that the custom driver VI executes.

After you save the I/O Base Rate Loop VI with the custom VIs included, using the **SIT Connection Manager** dialog box does not overwrite changes you made to the driver VI except for the caveats described in this topic. If you have multiple models and/or hardware configurations, you can generate multiple VIs for each model and/or configuration.

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsithowto/sit_h_decimating_simulation_data.html language=enus -->
## TOPIC 00079: Decimating Simulation Data (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsithowto/sit_h_decimating_simulation_data.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsithowto/sit_h_decimating_simulation_data.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Decimating Simulation Data (Simulation Interface Toolkit)

Sometimes, the [SIT Server](../lvsitconcepts/sit_c_components_of_a_simulation.html) cannot process all the data that the [execution host](../lvsitconcepts/sit_c_components_of_a_simulation.html) returns at once. This situation results in [data loss](../lvsitconcepts/sit_c_halting_simulations_on_data_loss.html). To reduce the possibility of data loss, you can decimate the data that the execution host returns so the host VI indicators can display the data in real time. Complete the following steps to decimate simulation data.

1. Click the Simulation Details front panel button of the host VI to launch the Simulation Details dialog box. You can click this button only while the host VI is running.
2. Click the Settings tab.
3. Enter an integer value n in the Signal Decimation text box.
4. Click the Apply button. The SIT Server now returns every n th signal update to the host VI. To probe the model continuously again, enter 1 in the Signal Decimation text box and click the Apply button.

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsithowto/sit_h_dll_windows.html language=enus -->
## TOPIC 00080: Executing a Model DLL on a Windows Computer (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsithowto/sit_h_dll_windows.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsithowto/sit_h_dll_windows.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Executing a Model DLL on a Windows Computer (Simulation Interface Toolkit)

You typically create a [model DLL](../lvsitconcepts/sit_c_components_of_a_simulation.html#real_time_components) to control a simulation in real time. However, you also can execute a model DLL on a Windows computer, typically the [host computer](../lvsitconcepts/sit_c_components_of_a_simulation.html). You also can use hardware I/O devices, such as a National Instruments DAQ device, if you installed those devices in the Windows computer.

|  | Note Although you use the following procedure to execute a model DLL on a Windows computer, you must install the LabVIEW Real-Time Module as if you were executing the model DLL on an real-time (RT) target. Additionally, National Instruments does not guarantee deterministic applications when running on a Windows computer. Therefore, you might need to increase the sampling period of the model to ensure the model DLL executes on the Windows computer. |
| --- | --- |

Complete the following steps to execute a model DLL on a Windows computer:

1. Specify the model DLL and execution host . In this situation, select the Driver VI on Localhost option.
2. Click the Hardware I/O tab.
3. (Optional) If you have any DAQ or CAN devices or FPGA targets installed on the Windows PC, create mappings between the host VI and those devices.
4. Click the Build Model Files button to generate the driver VI . The LabVIEW Simulation Interface Toolkit places the driver VI, < ModelName > _driver.vi , in the same directory as the model DLL you specified.
5. Click the OK button in the SIT Connection Manager dialog box. If you have not saved the host VI already, LabVIEW prompts you for a location to save the host VI.
6. Close the simulation environment or manually stop the SIT Server . Also, ensure that no other driver VIs are running on the Windows computer. If you do not stop the SIT Server before continuing, LabVIEW returns an error when you try to run the VIs.
7. Enter a name and location for the host VI and click the OK button to save the host VI. The Simulation Interface Toolkit generates the block diagram code of the host VI.
8. Open and run the driver VI.
9. Open and run the host VI.

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsithowto/sit_h_downloading_driver_vi_lvrt.html language=enus -->
## TOPIC 00081: Downloading the Driver VI Using the LabVIEW Real-Time Module (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsithowto/sit_h_downloading_driver_vi_lvrt.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsithowto/sit_h_downloading_driver_vi_lvrt.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Downloading the Driver VI Using the LabVIEW Real-Time Module (Simulation Interface Toolkit)

Complete the following steps to manually run the [driver VI](../lvsitconcepts/sit_c_components_of_a_simulation.html#real_time_components) using the LabVIEW Real-Time Module. This is not necessary if you are using a Host VI generated by the [SIT Connection Manager](../lvsit/sit_connection_manager_db.html). The Host VI will automatically download the driver VI.

1. FTP the model DLL to the real-time (RT) target. Place the model DLL in the C:\ni-rt\system\ directory.
2. Launch LabVIEW and open the driver VI project.
3. In the project, expand the real-time target.
4. Run the driver VI that is under the target. LabVIEW downloads the necessary files to the RT target and starts running the simulation. You now can disconnect LabVIEW from the RT target by right-clicking a target and selecting Disconnect from the shortcut menu.

You can communicate with the simulation at any time by [specifying the RT target](../lvsithowto/sit_h_specify_dll_and_host.html) and running the host VI.

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsithowto/sit_h_driver_vi.html language=enus -->
## TOPIC 00082: Creating a Driver VI (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsithowto/sit_h_driver_vi.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsithowto/sit_h_driver_vi.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Creating a Driver VI (Simulation Interface Toolkit)

A [driver VI](../lvsitconcepts/sit_c_understanding_the_driver_vi.html) contains mappings between [National Instruments RT Series hardware](../lvsitconcepts/sit_c_supported_ni_hardware.html) and [model DLL](../lvsitconcepts/sit_c_components_of_a_simulation.html#real_time_components) inputs/outputs. You can create mappings for certain types of National Instruments [CAN interfaces](../lvsithowto/sit_h_ni_can.html), [DAQ devices](../lvsithowto/sit_h_ni_daq.html), and [FPGA targets](../lvsithowto/sit_h_ni_fpga.html).

| Previous StepCreating a Host VIor Specifying the Model DLL and Execution Host | Next StepCreating Mappings for National Instruments CAN Interfacesor Creating Mappings for National Instruments DAQ Deviceor Creating Mappings for National Instruments FPGA Targetsor Creating a Custom Driver VI |
| --- | --- |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsithowto/sit_h_emp.html language=enus -->
## TOPIC 00083: Editing Multiple Parameters at Run Time (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsithowto/sit_h_emp.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsithowto/sit_h_emp.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Editing Multiple Parameters at Run Time (Simulation Interface Toolkit)

Use the [Edit Multiple Parameters](../lvsit/sit_edit_multiple_params_db.html) dialog box to edit multiple parameters at run time and apply changes all at once. You can save a set of parameter values to a file that you can load at a later time. Complete the following steps to edit multiple parameters at run time.

1. Click the Edit Multiple Parameters front panel button of the host VI to launch the Edit Multiple Parameters dialog box.
 You can click this button only while the host VI is running.
2. Click the Add Parameter button to launch the Edit Parameter Value dialog box. You use this dialog box to specify the new value of the parameter. You also can access this dialog box by double-clicking a row in the table.
3. Select the parameter you want to edit from the Parameter pull-down list. You can change the value of any parameter associated with the model, even a parameter that does not have a front panel control. When you select a parameter, the data type of that parameter appears below the Parameter pull-down list.
4. Enter the new value of the parameter in the Value text box.
5. Click the OK button to save the updated value and return to the Edit Multiple Parameters dialog box. The New Parameter Values table on this dialog box updates to show the changes you made. [IMAGE alt='image' src='note.gif']
**Note** Any values that you change do not affect the simulation until you click either the **Apply** button or the **OK** button in the **Edit Multiple Parameters** dialog box.
6. Click the Save button to save the updated parameter values to a text file.
7. Click the OK button to apply the updated parameter value(s) to the simulation. If a parameter has a front panel control, that control updates to show the new value.

By default, the LabVIEW Simulation Interface Toolkit does not automatically adjust the scale range of knobs and sliders. LabVIEW Simulation Interface Toolkit can automatically adjust the scale range if the new value is outside the current range. You can enable autoscaling by placing a checkmark in the **Autoscale Controls** checkbox on the **Mappings** tab of the [SIT Connection Manager](../lvsit/sit_connection_manager_db.html) dialog box. If autoscaling is disabled and you enter a parameter value outside the scale range, the control saves the value but shows only the maximum value of the scale range. For example, if the scale range of a knob is 0?10 and you enter a value of 20, the front panel shows the value of the control as 10, even though the actual value is 20.

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsithowto/sit_h_file_playback.html language=enus -->
## TOPIC 00084: Configuring a File Playback (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsithowto/sit_h_file_playback.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsithowto/sit_h_file_playback.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Configuring a File Playback (Simulation Interface Toolkit)

Complete the following steps to configure a file playback.

1. Ensure that the host VI 
 is not running.
2. Select Tools»SIT Connection Manager to
 launch the SIT Connection Manager dialog box.
3. Click the File Playback page. [IMAGE alt='image' src='note.gif']
**Note** LabVIEW disables
 this page if you have not specified a .mdl or .dll
 file.
4. Click the New button to create a file playback configuration.
5. On the Configuration Settings tab, enter the name and description of the file playback configuration. The Simulation Details dialog box displays this name when you run the simulation, allowing you to select the file playback configuration.
6. Enter the name of the playback file in the Playback Filename text box.
7. On the Configuration Mappings tab of the file playback configuration page, select the signal pairs to map in the File Channel Mappings and Model Signals tree controls, and then click the Add button to map the signals.
8. Repeat steps1 thru 7 to create multiple file playback configurations. You can select between these configurations when you run the simulation by opening the Simulation Details dialog box and clicking the File Playback page.

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsithowto/sit_h_ftp_model_dll.html language=enus -->
## TOPIC 00085: Manually Downloading the Model DLL to a Real-Time Target (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsithowto/sit_h_ftp_model_dll.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsithowto/sit_h_ftp_model_dll.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Manually Downloading the Model DLL to a Real-Time Target (Simulation Interface Toolkit)

If you need to download the [model DLL](../lvsitconcepts/sit_c_components_of_a_simulation.html#real_time_components) to a real-time (RT) target manually, you must use File Transfer Protocol (FTP) to transfer the model DLL. When you download the model DLL to the RT target, place the model DLL in the C:\ni-rt\system\ directory.

You must manually download the model DLL to an RT target if you want to [download the driver VI to the RT target using the LabVIEW Real-Time Module](../lvsithowto/sit_h_downloading_driver_vi_lvrt.html).

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsithowto/sit_h_intro.html language=enus -->
## TOPIC 00086: Simulation Interface Toolkit How-To (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsithowto/sit_h_intro.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsithowto/sit_h_intro.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Simulation Interface Toolkit How-To (Simulation Interface Toolkit)

June 2010, 371503F-01

The Simulation Interface Toolkit How-To book provides instructions on
 configuring, running, and manipulating a simulation.

|  | (Windows) To view related topics, click the Locate button, shown at left, in the toolbar at the top of this window. The LabVIEW Help highlights this topic in the Contents tab so you can navigate the related topics. |
| --- | --- |

© 2002–2010 National Instruments Corporation. All rights reserved.

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsithowto/sit_h_logging_simulation_data.html language=enus -->
## TOPIC 00087: Logging Simulation Data (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsithowto/sit_h_logging_simulation_data.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsithowto/sit_h_logging_simulation_data.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Logging Simulation Data (Simulation Interface Toolkit)

You can log the values of model signals while a [simulation is running](../lvsithowto/sit_h_running_a_simulation.html). Complete the following steps to log simulation data to a text or .tdmsfile.

1. Ensure that the host VI is not running.
2. Select Tools»SIT Connection Manager to launch the SIT Connection Manager dialog box.
3. Click the Data Logging page. [IMAGE alt='image' src='note.gif']
**Note** LabVIEW disables this page if you have not specified a .mdl or .dll file.
4. Click the New button to create a new logging configuration.
5. On the Configuration Settings tab, enter the name and description of the data log configuration. The Simulation Details dialog box displays this name when you run the simulation, allowing you to select the log configuration.
6. Enter the name of the log file in the Data Log Filename text box.
7. On the Configuration Mappings tab of the data log configuration page, click the New Group button to create a new channel group for logged signals. Give the channel group a name. You can rename the group by double-clicking the channel group name in the Logged Signals tree control, or by right-clicking the channel group and selecting Rename .
8. Add signals to this channel group by dragging and dropping them from the Model Signals tree into the appropriate channel group in the Logged Signals tree control, or by selecting one or more signals in the Mode Signalsl tree control and the appropriate channel group in the Logged Signals tree control and clicking the Add button.
9. Right click a channel group in the Logged Signals tree control and select the Decimation option to specify an integer value n as the decimation value. When you run the simulation, the LabVIEW Simulation Interface Toolkit logs every n th data point for all the channels in the group instead of every data point. Each channel group can have its own decimation.
10. Repeat steps1 thru 9 to create multiple data log configurations. You can select between these configurations when you run the simulation by opening the Simulation Details dialog box and clicking the Data Logging page.

|  | Note Use the Import and Export buttons to load or save data logging configuration options. |
| --- | --- |

|  | Note National Instruments recommends you use a unique filename for each data logging configuration or you enable a timestamp for the file names. Consider using the same name for the log file and the log configuration. |
| --- | --- |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsithowto/sit_h_modifying_mappings.html language=enus -->
## TOPIC 00088: Modifying Mappings at Run Time (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsithowto/sit_h_modifying_mappings.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsithowto/sit_h_modifying_mappings.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Modifying Mappings at Run Time (Simulation Interface Toolkit)

Use the [Remap Controls and Indicators](../lvsit/sit_remap_ci_db.html) dialog box to change [mappings](../lvsitconcepts/sit_c_creating_mappings.html) between LabVIEW controls/indicators and model parameters/signals while the simulation is running. Complete the following steps to modify mappings at run time.

1. Click the Remap Controls and Indicators front panel button of the host VI to launch the Remap Controls and Indicators dialog box. You can click this button only while the host VI is running.
2. Select a control or indicator from the Current Mappings table. If you select a control, the Model Parameters tree appears on the right side of the dialog box. If you select an indicator, the Model Signals tree appears instead.
3. Select the new parameter or signal from the appropriate tree.
4. Click the Apply Selected Mapping button to apply the new mapping to the control or indicator. The Current Mappings table updates to show the mapping you just made. You also can double-click a parameter or signal to apply the mapping. [IMAGE alt='image' src='note.gif']
**Note** To remove a mapping, select the mapping that you want to remove and click the **Remove Selected Mapping** button.
5. Click the Close button to return to the front panel of the host VI.

|  | Note The label of the front panel control associated with the new mapping does not change. |
| --- | --- |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsithowto/sit_h_multiple_dll.html language=enus -->
## TOPIC 00089: Executing Multiple Model DLLs on the Same Real-Time Target Simultaneously (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsithowto/sit_h_multiple_dll.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsithowto/sit_h_multiple_dll.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Executing Multiple Model DLLs on the Same Real-Time Target Simultaneously (Simulation Interface Toolkit)

Executing multiple model DLL on the same real-time (RT) target simultaneously involves running multiple [SIT Servers](../lvsitconcepts/sit_c_components_of_a_simulation.html#real_time_components) on different ports on the same RT target. The following example uses model1.vi and model2.vi as sample [host VIs](../lvsitconcepts/sit_c_components_of_a_simulation.html) that specify the same RT target. This example also assumes you have [created the appropriate driver VIs](../lvsithowto/sit_h_driver_vi.html)
 model1_driver.vi and model2_driver.vi. By default, both of these driver VIs start the SIT Server on port 6011. Complete the following steps to have model2_driver.vi start the SIT Server on a different port.

1. Launch LabVIEW and open the host VI model2.vi .
2. Select Tools»SIT Connection Manager to launch the SIT Connection Manager dialog box.
3. Click the Model and Host tab.
4. Enter a port number other than 6011 in the Port text box. For this example, enter 6012 .
5. Click the OK button to generate the block diagram code of the host VI and driver VI again.
6. Save model2.vi .
 
 After making these changes, model1.vi starts the SIT Server on port 6011, and model2.vi starts the SIT Server on port 6012. Both SIT Servers run on the same RT target. You can repeat this procedure to run as many SIT Servers simultaneously as you like. However, running more than one SIT Server on the same RT target can reduce the ability of the simulation to run in real time. 
 After scripting both Driver VIs, open the base-rate loop of one of the VIs and change the VI Priority to High Priority, or something other than Time-critical. An RT system with one core runs only one time-critical thread by default, which results in one of the model DLL base-rate loops being starved. This limitation does not occur on a multi-core RT target with SMP installed, and it does not happen when running the simulation on Windows, regardless of the number of cores available.
7. Create a top level VI for the RT target that calls both driver VIs.
8. Place the top level VI under the RT target in the project and deploy the VIs to the target.
9. Run the host (client) VIs.

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsithowto/sit_h_ni_can.html language=enus -->
## TOPIC 00090: Creating Mappings for National Instruments CAN Interfaces (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsithowto/sit_h_ni_can.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsithowto/sit_h_ni_can.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Creating Mappings for National Instruments CAN Interfaces (Simulation Interface Toolkit)

Complete the following steps to create mappings between National Instruments CAN interfaces and a [model DLL](../lvsitconcepts/sit_c_components_of_a_simulation.html#real_time_components).

1. Specify the model DLL and real-time (RT) target or the localhost .
2. Click the
 Hardware I/O page of the SIT Connection Manager dialog box.
3. Click the Configure HW I/O button.
4. In the Configure HW I/O dialog box, complete the following steps to configure mappings between an NI-CAN device and a model DLL.
  1. Right-click the IP address or target name in the Device Tree and select Add Device»NI-CAN .
  2. Configure the NI-CAN device .
  3. Select the appropriate signal pairs in the Device Tree and the Model Tree and click the Add button.
  4. Click the OK button to exit the Configure HW I/O Mappings dialog box. The newly defined mappings appear in the Hardware Mappings table of the Hardware I/O page in the SIT Connection Manager.
  5. Click the OK button to exit the SIT Connection Manager and rebuild the host VI with the new mappings.

| Previous StepSpecifying the Model DLL and Execution Host | Next StepRunning a Simulation |
| --- | --- |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsithowto/sit_h_ni_daq.html language=enus -->
## TOPIC 00091: Creating Mappings for a National Instruments DAQ Device (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsithowto/sit_h_ni_daq.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsithowto/sit_h_ni_daq.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Creating Mappings for a National Instruments DAQ Device (Simulation Interface Toolkit)

|  | Note National Instruments DAQ devices must support single-point timed hardware I/O to be used with the Simulation Interface Toolkit. |
| --- | --- |

Complete the following steps to create mappings between National Instruments DAQ devices and a [model DLL](../lvsitconcepts/sit_c_components_of_a_simulation.html#real_time_components).

1. Specify the model DLL and real-time (RT) target or the localhost .
2. Click the Hardware I/O page of the SIT Connection Manager dialog box.
3. Click the Configure HW I/O button.
4. In the Configure HW I/O dialog box, complete the following steps to configure mappings between an NI-DAQ device and a model DLL.
  1. Right-click the IP address or target name in the Device Tree and select Add Device»NI-FPGA .
  2. Configure the NI-DAQ device .
  3. Select the appropriate signal pairs in the Device Tree and the Model Tree and click the Add button.
  4. Click the OK button to exit the Configure HW I/O Mappings dialog box. The newly defined mappings appear in the Hardware Mappings table of the Hardware I/O page in the SIT Connection Manager.
  5. Click the OK button to exit the SIT Connection Manager and rebuild the host VI with the new mappings.

| Previous StepSpecifying the Model DLL and Execution Host | Next Step Running a Simulation |
| --- | --- |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsithowto/sit_h_ni_fpga.html language=enus -->
## TOPIC 00092: Creating Mappings for National Instruments FPGA Targets (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsithowto/sit_h_ni_fpga.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsithowto/sit_h_ni_fpga.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Creating Mappings for National Instruments FPGA Targets (Simulation Interface Toolkit)

Complete the following steps to create mappings between National Instruments FPGA targets and a [model DLL](../lvsitconcepts/sit_c_components_of_a_simulation.html#real_time_components).

1. Specify the model DLL and real-time (RT) target or the localhost .
2. Click the Hardware I/O page of the SIT Connection Manager dialog box.
3. Click the Configure HW I/O button.
4. In the Configure HW I/O dialog box, complete the following steps to configure mappings between an FPGA target and a model DLL.
  1. Right-click the IP address or target name in the Device Tree and select Add Device»NI-FPGA .
  2. Configure the NI-FPGA target .
  3. Select the appropriate signal pairs in the Device Tree and the Model Tree and click the Add button.
  4. Click the OK button to exit the Configure HW I/O Mappings dialog box. The newly defined mappings appear in the Hardware Mappings table of the Hardware I/O page in the SIT Connection Manager.
  5. Click the OK button to exit the SIT Connection Manager and rebuild the host VI with the new mappings.

| Previous StepSpecifying the Model DLL and Execution Host | Next StepRunning a Simulation |
| --- | --- |

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsithowto/sit_h_run_wo_server.html language=enus -->
## TOPIC 00093: Running a Simulation Without the SIT Server (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsithowto/sit_h_run_wo_server.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsithowto/sit_h_run_wo_server.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Running a Simulation Without the SIT Server (Simulation Interface Toolkit)

If the real-time (RT) target you are using does not have at least 32 MB of RAM, or if you do not need to interact with the simulation while the simulation is running, you can run a simulation on an RT target without starting the [SIT Server](../lvsitconcepts/sit_c_components_of_a_simulation.html). When a simulation is running without the SIT Server, you cannot use a [host VI](../lvsitconcepts/sit_c_components_of_a_simulation.html) to communicate with the [model DLL](../lvsitconcepts/sit_c_components_of_a_simulation.html#real_time_components).

Complete the following steps to run a simulation without the SIT Server.

1. FTP the model DLL to the C:\ni-rt\system\ directory of the RT target.
2. Open the driver VI project that was generated by the SIT Connection Manager.
3. Expand the RT target in the project window.
4. Open the driver VI from the RT target in the project window.
5. Set the Start Server? front panel switch of the driver VI to FALSE.
6. Run the driver VI. When you run the driver VI, LabVIEW downloads the driver VI to the RT target and starts the simulation.

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsithowto/sit_h_running_a_simulation.html language=enus -->
## TOPIC 00094: Running a Simulation (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsithowto/sit_h_running_a_simulation.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsithowto/sit_h_running_a_simulation.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Running a Simulation (Simulation Interface Toolkit)

Complete the following steps to run a simulation.

|  | Note If you are not running the simulation on a real-time (RT) target, you must launch The MathWorks, Inc. MATLAB® application software on the host computer. The command window displays the following message: Starting the SIT Server on Port 6011 SIT Server started This message indicates that the SIT Server is running. |
| --- | --- |

1. Launch LabVIEW and open the host VI .
2. Select Tools»SIT Connection Manager to launch the SIT Connection Manager dialog box.
3. Enter the IP address and port of the SIT Server in the Simulation Environment text box. If the host computer is the same as the execution host , use the default value of localhost to specify that the SIT Server is running on the host computer.
4. Click the OK button.
5. Display the front panel of the host VI.
6. Click the Run button in LabVIEW to run the host VI. (Real-Time Target) When you run the host VI, the LabVIEW Simulation Interface Toolkit downloads the model DLL and driver VI to the real-time (RT) target.
7. Click the Run Simulation front panel button of the host VI to start the simulation.
8. Adjust the values of the LabVIEW controls and observe the changes on the LabVIEW indicators. Because you created mappings between these controls to the model parameters, when you adjust the values of the controls, the parameter values of the model change. Using LabVIEW, you can change the parameters of the model and immediately view the results. You also can change the value of multiple parameters at once . If you try to change the value of a parameter whose value cannot change at run time, you receive an error.
9. Click the Pause Simulation front panel button to pause the simulation. To resume the simulation, click the Pause Simulation button again. You cannot pause a simulation that is running on an RT target.
10. Click the Stop Simulation front panel button to stop the simulation. [IMAGE alt='image' src='note.gif']
**Note** If you are running the simulation on an RT target, or if you are running a [model DLL on a Windows PC](../lvsithowto/sit_h_dll_windows.html), clicking the **Stop Simulation** button also stops the host VI. In these situations, you do not need to click the **Stop Host VI** button also.
11. If you are running the simulation in a simulation environment, click the Stop Host VI front panel button to stop the host VI. [IMAGE alt='image' src='note.gif']
**Note** If the simulation is running when you click the **Stop Host VI** button, the simulation continues to run. To stop the simulation, you must run the host VI again and click the **Stop Simulation** button.

<!--NI_TOPIC bundle=labview-simulation-interface-toolkit-api-ref path=lvsithowto/sit_h_specify_dll_and_host.html language=enus -->
## TOPIC 00095: Specifying the Model DLL and Execution Host (Simulation Interface Toolkit)

- bundle_id: `labview-simulation-interface-toolkit-api-ref`
- source_path: `lvsithowto/sit_h_specify_dll_and_host.html`
- source_url: https://docs-be.ni.com/bundle/labview-simulation-interface-toolkit-api-ref/raw/resource/enus/lvsithowto/sit_h_specify_dll_and_host.html
- document_id: `labview-simulation-interface-toolkit-api-ref`
- page_type: `leaf`
- content_type: ``

### Specifying the Model DLL and Execution Host (Simulation Interface Toolkit)

Complete the following steps to specify the [model DLL](../lvsitconcepts/sit_c_components_of_a_simulation.html#real_time_components) and [execution host](../lvsitconcepts/sit_c_components_of_a_simulation.html) for a real-time (RT) simulation.

1. Configure any necessary RT Series hardware and ensure the hardware is working properly.
2. Launch LabVIEW and create a host VI .
3. Select Tools»SIT Connection Manager to launch the SIT Connection Manager dialog box.
4. Create mappings for parameters and signals you want to manipulate and probe.
5. Select the Real-Time Target button. If you have not already selected a model DLL, LabVIEW prompts you for the location of the model DLL. If you have not already selected an RT target for the model DLL, LabVIEW prompts you to select the RT target.
6. Select the appropriate model DLL and click the OK button to return to the SIT Connection Manager dialog box. The Model DLL file path indicator updates to show the path to the model DLL you selected.
7. Click the Change button next to the Target indicator and specify the IP address of the RT target.

| Previous StepConverting a Model into a Model DLL | Next StepCreating a Driver VI |
| --- | --- |
