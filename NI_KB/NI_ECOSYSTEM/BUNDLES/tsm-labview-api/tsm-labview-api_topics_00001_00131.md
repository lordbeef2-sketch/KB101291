# NI DOCUMENT BUNDLE: tsm-labview-api

<!--NI_BUNDLE_CHUNK bundle=tsm-labview-api start=1 end=131 -->
<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/advancedpal.html language=enus -->
## TOPIC 00001: Advanced VIs (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/advancedpal.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/advancedpal.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Advanced VIs (TSM)

Use the Advanced VIs to query the site numbers in the Semiconductor Module context, return the status of the Offline Mode setting, and transform per-instrument to per-site data.

The VIs on this palette return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html).

| Palette Object | Description |
| --- | --- |
| Get Site Numbers | Returns the site numbers and number of sites in the Semiconductor Module context. |
| Get Session And Channel Index | Returns the index of the channel group and channel that corresponds to a pin query. Use this VI to access an individual pin when you take a measurement across multiple instruments and pins. When you call a pin query VI, such as the Pins to NI-HSDIO Sessions VI, the VI returns an array of sessions and a channel list. Use the Get Session and Channel Index VI to identify which session and which channel refers to a pin and site number you specify. |
| Get Input Data | Returns per-site input data as defined in the Semiconductor Multi Test step. You must manually select the polymorphic instance you want to use. |
| Filter Pins | Filters the pins by instrument type ID. Pass a list of all pins or pin groups to return the pins connected to instruments of the type you specify in the Instrument Type Id parameter. If no pins are connected to instruments of the type you specify in the Instrument Type Id parameter, this VI returns an empty array. |
| Extract Pin Data | Extracts the measurement data for a specified pin from measurements obtained from an instrument and arranges the data in the order of sites in the Semiconductor Module context. |
| Get Offline Mode | Returns the current status of the Offline Mode setting. Offline Mode allows you to detect if your test program is using simulated instruments in Offline Mode. |
| Get Pins In Pin Group(s) | Returns a list of pins contained in the pin group or list of pin groups you specify. You must manually select the polymorphic instance you want to use. |
| Get Relays In Relay Group(s) | Returns a list of relays contained in the relay group or list of relay groups you specify. You must manually select the polymorphic instance you want to use. |
| Get Site Semiconductor Module Contexts | Returns an array of Semiconductor Module context objects, each of which represents a single site. The size and ordering of the array match the size and ordering of the sites in the Semiconductor Module Context input. |
| Per-Instrument to Per-Site Data | Transforms the measurement data from measurements obtained from an instrument and arranges the data in the order of sites and pins in the Semiconductor Module context. Use this VI when you have raw measurement data from an instrument that you need to manipulate in a site-specific way. |

#### Input Data Id Control

The Advanced palette also contains the input data ID control, which you can use to create a control populated with the input data IDs from a [linked sequence file](linkingtsmfiletolabviewproject.html). This allows you to select a value from the control's populated list rather than entering the value as a string. If there is no sequence file linked to the LabVIEW project, or if you are editing the LabVIEW project on a system that cannot access the sequence file, the control acts a string.

|  | Note To create a control, place it on the front panel. Placing a control on the block diagram creates a constant. |
| --- | --- |

| Palette Object | Description |
| --- | --- |
| Input Data Id | Contains a list of input data IDs for the linked sequence file(s). Displays only input data IDs on Semiconductor steps whose code module is set to the current VI. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/controlrelay(s).html language=enus -->
## TOPIC 00002: Control Relay(s) (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/controlrelay(s).html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/controlrelay(s).html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Control Relay(s) (TSM)

**Requires:** TSM

Performs relay actions on one or more relays. You must manually select the polymorphic instance you want to use. Select the single relay or multiple relays polymorphic instance based on the number of relays for which you perform the actions.

#### Relay Configuration

Performs the relay actions on the relays in the relay configuration.

[IMAGE alt='ApplyRelayConfiguration.vi' src='applyrelayconfiguration.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Relay Configuration specifies the name of the relay configuration. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Wait (s) specifies the time to wait, in seconds, for the relays to settle after performing the relay action. This input is optional. The default is 0s. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Single Relay - Single Relay Action

Performs the relay action on the relay.

[IMAGE alt='ControlRelaySingleAction.vi' src='controlrelaysingleaction.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Relay specifies the name of the relay or relay group that identifies the relays. |
|  | Relay Action specifies to open or close all identified relays. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Wait (s) specifies the time to wait, in seconds, for the relays to settle after performing the relay action. This input is optional. The default is 0s. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Multiple Relays - Single Relay Action

Performs the relay action on the relays.

[IMAGE alt='ControlRelaysSingleAction.vi' src='controlrelayssingleaction.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Relays specifies the names of the relays or relay groups that identify the relays. |
|  | Relay Action specifies to open or close all identified relays. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Wait (s) specifies the time to wait, in seconds, for the relays to settle after performing the relay action. This input is optional. The default is 0s. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Multiple Relays - Multiple Relay Actions

Performs the relay actions on the relays.

[IMAGE alt='ControlRelaysMultipleActions.vi' src='controlrelaysmultipleactions.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Relays specifies the names of the relays or relay groups that identify the relays. |
|  | Relay Actions specifies to open or close the relays identified by the corresponding relay or relay group. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Wait (s) specifies the time to wait, in seconds, for the relays to settle after performing all relay actions. This input is optional. The default is 0s. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/createmultisitedatafordaqmxanalogoutput.html language=enus -->
## TOPIC 00003: Create Multisite Data for Analog Output (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/createmultisitedatafordaqmxanalogoutput.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/createmultisitedatafordaqmxanalogoutput.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Create Multisite Data for Analog Output (TSM)

**Requires:** TSM

Accepts per site/pin data and returns data for all channels in the tasks. Use this data with the DAQmx Write VI. You must manually select the polymorphic instance you want to use. Select the single pin or multiple pins polymorphic instances based on the number of pins the test is designed to test. Select the single data to all sites or per site data polymorphic instances based on the data being passed to the VI. If data exists for each pin but not for each site, use the single data to all sites polymorphic instances. If data exists for each pin and for each site, use the per site data polymorphic instances.

#### DAQmx Single Data To All Sites (1 Pin 1 Task)

Accepts data for the pin and returns data for all channels in the task. Use this data with the DAQmx Write VI.

[IMAGE alt='SameDataToAllSites(1Pin1Task).vi' src='samedatatoallsites(1pin1task).gif']

|  | Pin Query Context is the pin query context a pin query returns. |
| --- | --- |
|  | Pin Data specifies data for the pin in a pin query. |
|  | Idle Value specifies the data value to use for channels in the task that are not connected to sites in the Semiconductor Module context. Because the DAQmx Write VI always writes to all channels in a task, use the Idle Value to write a constant value to channels that are not in the Semiconductor Module context. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context Out returns the Pin Query Context parameter unchanged. |
|  | Task Data returns a 2D array of data, where the rows correspond to channels in the task and the columns corresponds to the data to write to each channel in the task. Pass this data to the NI-DAQmx Write VI. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### DAQmx Single Data to All Sites (1 Pin M Tasks)

Accepts data for the pin and returns data for all channels in the tasks. Use this data with the DAQmx Write VI.

[IMAGE alt='SameDataToAllSites(1PinMTasks).vi' src='samedatatoallsites(1pinmtasks).gif']

|  | Pin Query Context is the pin query context a pin query returns. |
| --- | --- |
|  | Pin Data specifies data for the pin in a pin query. |
|  | Idle Value specifies the data value to use for channels in the task that are not connected to sites in the Semiconductor Module context. Because the DAQmx Write VI always writes to all channels in a task, use the Idle Value to write a constant value to channels that are not in the Semiconductor Module context. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context Out returns the Pin Query Context parameter unchanged. |
|  | Task Data returns a 3D array of data, where the first dimension corresponds to NI-DAQmx Tasks and the second dimension corresponds to channels. Because each NI-DAQmx Task can have a different number of channels, use the Number of Channels per Task output to determine the number of elements in the second dimension to pass to the NI-DAQmx Write VI for each task. |
|  | Number of Channels per Task returns a 1D array of the number of channels for each NI-DAQmx Task, with the same size as the first dimension of the Task Data output. Use this output to determine the subset of the task data arrays to pass to the NI-DAQmx Write VI. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### DAQmx Single Data To All Sites (N Pins 1 Task)

Accepts data for the pins and returns data for all channels in the task. Use this data with the DAQmx Write VI.

[IMAGE alt='SameDataToAllSites(NPins1Task).vi' src='samedatatoallsites(npins1task).gif']

|  | Pin Query Context is the pin query context object a pin query returns. |
| --- | --- |
|  | Pin Data specifies data for each pin in a pin query. Ensure that the pin order matches the order of the pins passed to the pin query. |
|  | Idle Value specifies the data value to use for channels in the task that are not connected to sites in the Semiconductor Module context. Because the DAQmx Write VI always writes to all channels in a task, use the Idle Value to write a constant value to channels that are not in the Semiconductor Module context. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context Out returns the Pin Query Context parameter unchanged. |
|  | Task Data returns a 2D array of data, where the rows correspond to channels and the columns corresponds to the data to write to each channel in the task. Pass this data to the NI-DAQmx Write VI. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### DAQmx Single Data To All Sites (N Pins M Tasks)

Accepts data for the pins and returns data for all channels in the tasks. Use this data with the DAQmx Write VI.

[IMAGE alt='SameDataToAllSites(NPinsMTasks).vi' src='samedatatoallsites(npinsmtasks).gif']

|  | Pin Query Context is the pin query context object a pin query returns. |
| --- | --- |
|  | Pin Data specifies data for each pin in a pin query. Ensure that the pin order matches the order of the pins passed to the pin query. |
|  | Idle Value specifies the data value to use for channels in the task that are not connected to sites in the Semiconductor Module context. Because the DAQmx Write VI always writes to all channels in a task, use the Idle Value to write a constant value to channels that are not in the Semiconductor Module context. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context Out returns the Pin Query Context parameter unchanged. |
|  | Task Data returns a 3D array of data, where the first dimension corresponds to NI-DAQmx Tasks and the second dimension corresponds to channels. Because each NI-DAQmx Task can have a different number of channels, use the Number of Channels per Task output to determine the number of elements in the second dimension to pass to the NI-DAQmx Write VI for each task. |
|  | Number of Channels per Task returns a 1D array of the number of channels for each NI-DAQmx Task, with the same size as the first dimension of the Task Data output. Use this output to determine the subset of the task data arrays to pass to the NI-DAQmx Write VI. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### DAQmx Per Site Data (1 Pin 1 Task)

Accepts data for all sites in the Semiconductor Module Context that the pin is connected to and returns data for all channels in the task. Use this data with the DAQmx Write VI.

[IMAGE alt='DifferentDataForEachSite(1Pin1Task).vi' src='differentdataforeachsite(1pin1task).gif']

|  | Pin Query Context is the pin query context object a pin query returns. |
| --- | --- |
|  | Site Pin Data specifies per pin data for every site in the Semiconductor Module Context. Specify data such that rows of the data array correspond the sites while columns correspond to the samples to write to each pin. Ensure that the site order matches the order of sites the Get Site Numbers VI returns. |
|  | Idle Value specifies the data value to use for channels in the task that are not connected to sites in the Semiconductor Module context. Because the DAQmx Write VI always writes to all channels in a task, use the Idle Value to write a constant value to channels that are not in the pin query context. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context Out returns the Pin Query Context parameter unchanged. |
|  | Task Data returns a 2D array of data, where the rows correspond to channels in the task and the columns corresponds to the data to write to each channel in the task. Pass this data to the NI-DAQmx Write VI. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### DAQmx Per Site Data (1 Pin M Tasks)

Accepts data for all sites in the Semiconductor Module Context that the pin is connected to and returns data for all channels in the tasks. Use this data with the DAQmx Write VI.

[IMAGE alt='DifferentDataForEachSite(1PinMTasks).vi' src='differentdataforeachsite(1pinmtasks).gif']

|  | Pin Query Context is the pin query context object a pin query returns. |
| --- | --- |
|  | Site Pin Data specifies per pin data for every site in the Semiconductor Module Context. Specify data such that rows of the data array correspond the sites while columns correspond to the samples to write to each pin. Ensure that the site order matches the order of sites the Get Site Numbers VI returns. |
|  | Idle Value specifies the data value to use for channels in the task that are not connected to sites in the Semiconductor Module context. Because the DAQmx Write VI always writes to all channels in a task, use the Idle Value to write a constant value to channels that are not in the Semiconductor Module context. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context Out returns the Pin Query Context parameter unchanged. |
|  | Task Data returns a 3D array of data, where the first dimension corresponds to NI-DAQmx Tasks and the second dimension corresponds to channels. Because each NI-DAQmx Task can have a different number of channels, use the Number of Channels per Task output to determine the number of elements in the second dimension to pass to the NI-DAQmx Write VI for each task. |
|  | Number of Channels per Task returns a 1D array of the number of channels for each NI-DAQmx Task, with the same size as the first dimension of the Task Data output. Use this output to determine the subset of the task data arrays to pass to the NI-DAQmx Write VI. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### DAQmx Per Site Data (N Pins 1 Task)

Accepts data for all sites in the Semiconductor Module Context that the pins are connected to and returns data for all channels in the task. Use this data with the DAQmx Write VI.

[IMAGE alt='DifferentDataForEachSite(NPins1Task).vi' src='differentdataforeachsite(npins1task).gif']

|  | Pin Query Context is the pin query context a pin query returns. |
| --- | --- |
|  | Site Pin Data specifies per pin data for every pin in the pin query context and every site in the Semiconductor Module Context. Specify data in a 3D array such that pages of the data array correspond to sites, rows of the data array correspond to pins, and columns correspond to the samples to write to each pin. Ensure that the site order matches the order of sites the Get Site Numbers VI returns and that the pin order matches the order of the pins passed to the pin query. |
|  | Idle Value specifies the data value to use for channels in the task that are not connected to sites in the Semiconductor Module context. Because the DAQmx Write VI always writes to all channels in a task, use the Idle Value to write a constant value to channels that are not in the Semiconductor Module context. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context Out returns the Pin Query Context parameter unchanged. |
|  | Task Data returns a 2D array of data, where the first dimension corresponds to channels in the task and the second dimension corresponds to the data to write to each channel in the task. Pass this data to the NI-DAQmx Write VI. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### DAQmx Per Site Data (N Pins M Tasks)

Accepts data for all sites in the Semiconductor Module Context that the pins are connected to and returns data for all channels in the tasks. Use this data with the DAQmx Write VI.

[IMAGE alt='DifferentDataForEachSite(NPinsMTasks).vi' src='differentdataforeachsite(npinsmtasks).gif']

|  | Pin Query Context is the pin query context a pin query returns. |
| --- | --- |
|  | Site Pin Data specifies per pin data for every pin in the pin query context and every site in the Semiconductor Module Context. Specify data in a 3D array such that pages of the data array correspond to sites, rows of the data array correspond to pins, and columns correspond to the samples to write to each pin. Ensure that the site order matches the order of sites the Get Site Numbers VI returns and that the pin order matches the order of the pins passed to the pin query. |
|  | Idle Value specifies the data value to use for channels in the task that are not connected to sites in the Semiconductor Module context. Because the DAQmx Write VI always writes to all channels in a task, use the Idle Value to write a constant value to channels that are not in the Semiconductor Module context. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context Out returns the Pin Query Context parameter unchanged. |
|  | Task Data returns a 3D array of data, where the first dimension corresponds to NI-DAQmx Tasks and the second dimension corresponds to channels. Because each NI-DAQmx Task can have a different number of channels, use the Number of Channels per Task output to determine the number of elements in the second dimension to pass to the NI-DAQmx Write VI for each task. |
|  | Number of Channels per Task returns a 1D array of the number of channels for each NI-DAQmx Task, with the same size as the first dimension of the Task Data output. Use this output to determine the subset of the task data arrays to pass to the NI-DAQmx Write VI. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/createmultisitedigitalwaveformswithcontext.html language=enus -->
## TOPIC 00004: Create Multisite Digital Waveforms (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/createmultisitedigitalwaveformswithcontext.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/createmultisitedigitalwaveformswithcontext.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Create Multisite Digital Waveforms (TSM)

**Requires:** TSM

Creates multisite digital waveforms based on the pin map. Use the Single Waveform to All Sites instance when you want to write the same waveform for each site. Use the Per Site Waveforms instance when you want to write different waveforms for each site.

#### Single Waveform to All Sites

Creates an output array of one or multiple digital waveforms that you can download to NI-HSDIO instruments and that contain data properly organized for multiple sites according to the pin map. Use this VI when all sites require the same digital waveform. The order of signals in the **Single Site Waveform** parameter should match the order of the **Pins** parameter used in the Pin(s) to NI-HSDIO Session(s) VI instance that generated the pin query context.

[IMAGE alt='CreateMultisiteDigitalWaveformFromSingleWaveformWithContext.vi' src='createmultisitedigitalwaveformfromsinglewaveformwithcontext.gif']

|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, extract data from a set of measurements, and create or rearrange waveforms. You create a pin query context object with a Pin(s) to NI-HSDIO Sessions VI. |
| --- | --- |
|  | Single Site Waveform specifies the digital waveform that contains the digital pattern for a single site. The signals in the digital waveform must be in the same order as the Pins parameter used in the Pin(s) to NI-HSDIO Session(s) VI instance that generated the pin query context. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context Out returns the pin query context object unchanged. |
|  | Per Instrument Waveforms returns an array of digital waveforms in which each element is the waveform an NI-HSDIO instrument requires to generate the data in the Single Site Waveform parameter for all sites. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Per Site Waveforms

Creates an output array of one or multiple digital waveforms that you can download to NI-HSDIO instruments and that contain data properly organized for multiple sites according to the pin map. Use this VI when each site requires a different waveform. The order of signals in the **Single Site Waveform** parameter should match the order of the **Pins** parameter used in the Pin(s) to NI-HSDIO Session(s) VI instance that generated the pin query context.

[IMAGE alt='CreateMultisiteDigitalWaveformFromMultipleWaveformsWithContext.vi' src='createmultisitedigitalwaveformfrommultiplewaveformswithcontext.gif']

|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, extract data from a set of measurements, and create or rearrange waveforms. You create a pin query context object with a Pin(s) to NI-HSDIO Sessions VI. |
| --- | --- |
|  | Per Site Waveform specifies an array of digital waveforms in which each element is a waveform that corresponds to a site. The site order must correspond to the site order in Semiconductor Module context. Use the Get Site Numbers VI to obtain the site order. The signals in the digital waveform must be in the same order as the Pins parameter used in the Pin(s) to NI-HSDIO Session(s) VI instance that generated the pin query context. All waveforms in the array must have the same number of signals as the number of elements in the array. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context Out returns the pin query context object unchanged. |
|  | Per Instrument Digital Data returns an array of digital waveforms in which each element is the waveform an NI-HSDIO instrument requires to generate the data in the Per Site Waveform parameter. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/custominstrumentpal.html language=enus -->
## TOPIC 00005: Custom Instrument VIs (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/custominstrumentpal.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/custominstrumentpal.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Custom Instrument VIs (TSM)

Use the Custom Instruments VIs to manage custom instruments and sessions for instruments that TSM does not natively support.

The VIs on this palette return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html).

| Palette Object | Description |
| --- | --- |
| Get All Session Data | Returns all sessions in the Semiconductor Module context that belong to instruments of the type you specify in the Instrument Type Id parameter. |
| Get All Instrument Definitions | Returns the channel group ID and associated instrument names and channel lists of all instruments of type Instrument Type Id defined in the Semiconductor Module context. You can use instrument names, channel group IDs, and channel lists to open driver sessions. |
| Set Session Data | Associates a session with an instrument and channel group. |
| Get Session Data | Returns the session data, channel group IDs, and channel lists required to access one or more pins for a specified instrument type ID. You must manually select the polymorphic instance you want to use. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/daqmxtsmconcepts.html language=enus -->
## TOPIC 00006: Using NI-DAQmx with TSM

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/daqmxtsmconcepts.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/daqmxtsmconcepts.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Using NI-DAQmx with TSM

Refer to the following [pin map](#pinmap), [process setup](#processsetup), [analog input](#analoginput), [analog output](#analogoutput), and [process cleanup](#processcleanup) suggestions when you use NI-DAQmx with TSM.

#### Pin Map

The TSM pin map defines NI-DAQmx tasks instead of NI-DAQmx instruments to support channel expansion. Each task in the pin map uses a channelList attribute, which can contain channels from one or more NI-DAQmx instruments. Format the channel list in the pin map the same way you format channel lists you use with the NI-DAQmx API, where:

- Channel names consist of a device identifier and a slash (/) followed by a channel identifier.
- Channel ranges are specified using a colon between two channel numbers.
- Lists of channel names and ranges are separated using commas.
- For example, dev1/ai0:1, dev1/ai2 .

Each task in the pin map also uses a taskType attribute. Multiple tasks can use the same task type. Pin queries that refer to tasks of more than one task type return an error.

#### Process Setup

Use the TSM Get All NI-DAQmx Task Names VI to return the task names and channel lists the pin map defines. Use the **Task Type** input of the VI to specify which type of tasks to return. Pass an empty string to obtain the names of all tasks regardless of task type.

Use the NI-DAQmx API to create and set up tasks. Use the **Task Names** output of the Get All NI-DAQmx Task Names VI to specify the task names for the DAQmx Create Task VI. Use the **Channel Lists** output from the Get All NI-DAQmx Task Names VI to specify the channels in the **Physical Channels** input of the DAQmx Create Channel VI.

For the best performance, start tasks in the process setup of the test program. You can associate channels with a single task only in the Started state.

Use the Set NI-DAQmx Task VI to store the task.

Refer to the NI-DAQmx Create AI Voltage Tasks step type with template code or to the following figure for an example of how to complete these tasks:

[IMAGE alt='image' src='setup.png']

#### Analog Input

Use the TSM Pin(s) to NI-DAQmx Task(s) VI to perform pin queries. Connect the **Channel Lists** or **Channel List** output of this VI to the ChannelsToRead property of a DAQmx Read property node. Use the DAQmx Read VI to read data from the channel to read. Use the TSM Publish Data VI to publish the measurement data to the Semiconductor Multi Test step type instances for all sites in the Semiconductor Module context.

Refer to the NI-DAQmx Acquire AI Voltage Waveforms step type with template code or to the following figure for an example of how to complete these tasks:

[IMAGE alt='image' src='analoginput.png']

#### Analog Output

Use the TSM Pin(s) to NI-DAQmx Task(s) VI to perform pin queries. Use the TSM Create Multisite Data for Analog Output VI to write data to the correct channels in the task. You can use per pin or per site input data. For per site data, the first dimension of the input array corresponds to the sites and the second dimension corresponds to the pins. Use the Idle Value input of the VI to specify the data value to use for channels in the task that are not connected to the sites in the Semiconductor Module context. Connect the **Task Data** output of the VI to the DAQmx Write VI.

Refer to the following figure for an example of how to complete these tasks:

[IMAGE alt='image' src='analogoutput.png']

#### Process Cleanup

Use the TSM Get All NI-DAQmx Tasks VI to return tasks with a task type you specify. Pass an empty string to the **Task Type** input to obtain the names of all tasks regardless of task type. Use the NI-DAQmx API to stop and clear all tasks.

Refer to the NI-DAQmx Clear Tasks step type with template code or to the following figure for an example of how to complete these tasks:

[IMAGE alt='image' src='cleanup.png']

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/extractpindata.html language=enus -->
## TOPIC 00007: Extract Pin Data (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/extractpindata.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/extractpindata.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Extract Pin Data (TSM)

**Requires:** TSM

Extracts the measurement data for a specified pin from measurements obtained from an instrument session and arranges the data in the order of sites in the Semiconductor Module context.

Use this VI when you have raw measurement data from an instrument session that you need to manipulate in a site-specific way. For example, if you need to perform an operation on the measurement data using per-site input data, this VI puts the measurement data for the selected pin into the same per-site order as the input data. Similarly, if you need to modify the data from a specific site before publishing, this VI puts the measurement data for the selected pin into a per-site array that you can then index to retrieve the data for the specific site. The order of the per-site array matches the order of the **Site Numbers** output parameter of the Get Site Numbers VI. You can use the Per-Site Publish VI to publish the resulting manipulated data.

#### Parametric:1D Array

Extracts the measurement data for a specified pin from a 1D array of double measurements obtained from an instrument session and arranges the data in the order of sites in the Semiconductor Module Context.

[IMAGE alt='Extract Pin Data 1D Array Double.vi' src='extract_pin_data_1d_array_double.gif']

|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
| --- | --- |
|  | Data In is a 1D array of double measurements obtained from multiple sites. |
|  | Pin specifies the pin for which to extract data. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Data Out the multisite measurement from the Data In parameter for the specified pin rearranged into a 1D array with the order of the elements matching the site order in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Pass/Fail:1D Array

Extracts the measurement data for a specified pin from a 1D array of Boolean measurements obtained from an instrument session and arranges the data in the order of sites in the Semiconductor Module Context.

[IMAGE alt='Extract Pin Data 1D Array Bool.vi' src='extract_pin_data_1d_array_bool.gif']

|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
| --- | --- |
|  | Data In is a 1D array of Boolean measurements obtained from multiple sites. |
|  | Pin specifies the pin for which to extract data. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Data Out the multisite measurement from the Data In parameter for the specified pin rearranged into a 1D array with the order of the elements matching the site order in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Parametric:2D Array

Extracts the measurement data for a specified pin from a 2D array of double measurements obtained from an instrument session and arranges the data in the order of sites in the Semiconductor Module Context.

[IMAGE alt='Extract Pin Data 2D Array Double.vi' src='extract_pin_data_2d_array_double.gif']

|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
| --- | --- |
|  | Data In is a 2D array of double measurements obtained from multiple sites. |
|  | Pin specifies the pin for which to extract data. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Data Out the multisite measurement from the Data In parameter for the specified pin rearranged into a 1D array with the order of the elements matching the site order in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Pass/Fail:2D Array

Extracts the measurement data for a specified pin from a 2D array of Boolean measurements obtained from an instrument session and arranges the data in the order of sites in the Semiconductor Module Context.

[IMAGE alt='Extract Pin Data 2D Array Bool.vi' src='extract_pin_data_2d_array_bool.gif']

|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
| --- | --- |
|  | Data In is a 2D array of Boolean measurements obtained from multiple sites. |
|  | Pin specifies the pin for which to extract data. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Data Out the multisite measurement from the Data In parameter for the specified pin rearranged into a 1D array with the order of the elements matching the site order in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/filterpinsbyinstrumenttype.html language=enus -->
## TOPIC 00008: Filter Pins (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/filterpinsbyinstrumenttype.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/filterpinsbyinstrumenttype.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Filter Pins (TSM)

**Requires:** TSM

Filters the pins by instrument type ID. Pass a list of all pins or pin groups to return the pins connected to instruments of the type you specify in the **Instrument Type Id** parameter. If no pins are connected to instruments of the type you specify in the **Instrument Type Id** parameter, this VI returns an empty array.

[IMAGE alt='FilterPinsByInstrumentType.vi' src='filterpinsbyinstrumenttype.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pins specifies an array of pins or pin groups to filter. The array must contain only pins or pin groups that are included in the Semiconductor Module context. |
|  | Instrument Type Id specifies the type of instrument for which you want to return DUT and system pins. For instruments that TSM natively supports, right-click the Instrument Type Id parameter, select Create Constant from the shortcut menu, and select the type of instrument you need. All custom instruments defined in the pin map specify an associated type ID. Typically, this type ID is an instrument driver name or other ID that is common for instruments that users program in a similar way. For custom instruments, you must pass the type ID associated with the instrument in the pin map file. For model-based instruments, pass the string you passed to the Set Custom Session VI to store sessions for the instruments. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Capability limits the filtered pins to those connected to a channel that defines the capability you specify. Use this parameter to differentiate between pins in the same instrument with different capabilities, such as NI-HSDIO Dynamic DIO channels and PFI lines. If a pin is connected to channels in which the capability is defined only for a subset of sites, the VI returns an error. Pass an empty string to return all elements in the Pins parameter that match the instrument type ID you specify. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Filtered Pins returns an array subset of pin names in the Pins parameter that are connected to an instrument of the filtered instrument type ID. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/fpgapal.html language=enus -->
## TOPIC 00009: NI-VST VIs (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/fpgapal.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/fpgapal.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

FPGA VIs (TSM)

Use the FPGA VIs to manage FPGA sessions for RF RIO instruments (RF LabVIEW FPGA enabled instruments).

The VIs on this palette return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html).

| Palette Object | Description |
| --- | --- |
| Get All FPGA Instrument Names | Returns the instrument names for all FPGA-enabled RF instruments in the Semiconductor Module context. You can use instrument names to open driver sessions. |
| Set FPGA VI Reference | Associates an instrument session with an FPGA-enabled instrument name. |
| Get All FPGA VI References | Returns all FPGA VI references in the Semiconductor Module context. |
| Pin To FPGA VI Reference(s) | Returns the FPGA VI references of the instruments connected to the pin. You must manually select the polymorphic instance you want to use. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getallfpgainstrumentnames.html language=enus -->
## TOPIC 00010: Get All FPGA Instrument Names (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getallfpgainstrumentnames.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getallfpgainstrumentnames.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get All FPGA Instrument Names (TSM)

**Requires:** TSM

Returns the instrument names for all FPGA-enabled RF instruments in the Semiconductor Module context. You can use instrument names to open driver sessions.

[IMAGE alt='GetAllFPGAInstrumentNames.vi' src='getallfpgainstrumentnames.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Names returns an array of names of NI-RF instruments that support NI-RIO in the Semiconductor Module context. |
|  | FPGA File Paths returns an array of FPGA file paths associated with the Instrument Names parameter. If the path is an absolute path, the VI returns the absolute path whether the file exists or not. If the path is a relative path and the file exists relative to the path of the pin map file, the VI returns the absolute path of the existing file. Otherwise, the VI returns a string without error. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getallfpgavireferences.html language=enus -->
## TOPIC 00011: Get All FPGA VI References (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getallfpgavireferences.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getallfpgavireferences.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get All FPGA VI References (TSM)

**Requires:** TSM

Returns all FPGA VI references in the Semiconductor Module context.

[IMAGE alt='GetAllFPGAVIReferences.vi' src='getallfpgavireferences.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | FPGA VI References returns all FPGA VI references in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getallinstrumentdefinitions.html language=enus -->
## TOPIC 00012: Get All Instrument Definitions (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getallinstrumentdefinitions.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getallinstrumentdefinitions.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get All Instrument Definitions (TSM)

**Requires:** TSM

Returns the channel group ID and associated instrument names and channel lists of all instruments of type **Instrument Type Id** defined in the Semiconductor Module context. You can use instrument names, channel group IDs, and channel lists to open driver sessions. The **Instrument Names**, **Channel Group Ids**, and **Channel Lists** parameters always return the same number of elements. Instrument names repeat in the **Instrument Names** parameter if the instrument has multiple channel groups.

[IMAGE alt='GetAllInstrumentDefinitions.vi' src='getallinstrumentdefinitions.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Instrument Type Id specifies the type ID for the instrument in the pin map file. All custom instruments defined in the pin map specify an associated type ID. Typically, this type ID is an instrument driver name or other ID that is common for instruments that users program in a similar way. For custom instruments, you must pass the type ID associated with the instrument in the pin map file. For model-based instruments, pass the string you passed to the Set Custom Session VI to store sessions for the instruments. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Channel Lists returns the channel lists for each of the channel group IDs. Each channel list is a comma-separated list of channels. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Names returns the names of all instruments in the Semiconductor Module context that are of type you specify in the Instrument Type Id parameter. |
|  | Channel Group Ids returns the IDs of all channel groups in the Semiconductor Module context that belong to an instrument of the type you specify in the Instrument Type Id parameter. For channels that do not belong to a channel group in the pin map, the Semiconductor Module creates a channel group with the same ID as the channel. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getallmodelbasedinstrumentnames.html language=enus -->
## TOPIC 00013: Get All Model-Based Instrument Names (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getallmodelbasedinstrumentnames.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getallmodelbasedinstrumentnames.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get All Model-Based Instrument Names (TSM)

**Requires:** TSM

Returns the instrument names and models for all Model-Based instruments in the Semiconductor Module context. You can use instrument names to query the model properties for the information needed to create the appropriate sessions to drive the instrument.

[IMAGE alt='GetAllModelBasedInstrumentNames.vi' src='getallmodelbasedinstrumentnames.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Category specifies the category of instruments for which to return instrument names. |
|  | Subcategory specifies the subcategory (under the given category) of instruments for which to return instrument names. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Model-Based Instruments returns an array of ModelBasedInstrumentInstanceData objects, each containing the instrument name and model of the Model-Based instrument in the Semiconductor Module Context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getallnidaqmxtasknames.html language=enus -->
## TOPIC 00014: Get All NI-DAQmx Task Names (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getallnidaqmxtasknames.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getallnidaqmxtasknames.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get All NI-DAQmx Task Names (TSM)

**Requires:** TSM

Returns the task names for all NI-DAQmx tasks of type **Task Type** in the Semiconductor Module context. You can use task names to create DAQmx tasks.

[IMAGE alt='GetAllNIDAQmxTaskNames.vi' src='getallnidaqmxtasknames.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Task Type specifies the type of NI-DAQmx tasks to return. Pass an empty string to obtain the names of all tasks regardless of task type. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Channel Lists returns an array of strings that contains the physical channel names for all channels in the Semiconductor Module Context. |
|  | Task Names returns an array of the NI-DAQmx task names in the Semiconductor Module context with a type of Task Type. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getallnidaqmxtasks.html language=enus -->
## TOPIC 00015: Get All NI-DAQmx Tasks (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getallnidaqmxtasks.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getallnidaqmxtasks.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get All NI-DAQmx Tasks (TSM)

**Requires:** TSM

Returns all NI-DAQmx tasks of type **Task Type** in the Semiconductor Module context. You can use tasks to perform NI-DAQmx operations.

[IMAGE alt='GetAllNIDAQmxTasks.vi' src='getallnidaqmxtasks.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Task Type specifies the type of tasks to return. All tasks defined in the pin map specify an associated task type. Pass an empty string to obtain the names of all tasks regardless of task type. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | DAQmx Tasks returns an array of the NI-DAQmx tasks in the Semiconductor Module context with a type of Task Type. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getallnidcpowerresourcestrings.html language=enus -->
## TOPIC 00016: Get All NI-DCPower Resource Strings (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getallnidcpowerresourcestrings.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getallnidcpowerresourcestrings.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get All NI-DCPower Resource Strings (TSM)

**Requires:** TSM

Returns the resource strings associated with each channel group in the ISemiconductorModuleContext. A resource string is a comma-separated list of NI-DCPower resources associated with the NI-DCPower channel group, each resource is defined by <instrument>/<channel>. You can use the resource strings to open driver sessions. All resources within the same resource string will be controlled by the same session.

[IMAGE alt='GetAllNIDCPowerResourceStrings.vi' src='getallnidcpowerresourcestrings.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Resource Strings returns an array of the NI-DCPower Resource Strings. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getallnidcpowersessions.html language=enus -->
## TOPIC 00017: Get All NI-DCPower Sessions (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getallnidcpowersessions.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getallnidcpowersessions.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get All NI-DCPower Sessions (TSM)

**Requires:** TSM

Returns all NI-DCPower instrument sessions in the Semiconductor Module context. You can use instrument sessions to close driver sessions.

[IMAGE alt='GetAllNIDCPowerSessions.vi' src='getallnidcpowersessions.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Sessions returns the instrument sessions for all NI-DCPower instruments in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getallnidigitalpatterninstrumentnames.html language=enus -->
## TOPIC 00018: Get All NI-Digital Pattern Instrument Names (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getallnidigitalpatterninstrumentnames.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getallnidigitalpatterninstrumentnames.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get All NI-Digital Pattern Instrument Names (TSM)

**Requires:** TSM

Returns the instrument names and comma-separated lists of instrument names that belong to the same group for all NI-Digital Pattern instruments in the Semiconductor Module context. You can use instrument names and comma-separated lists of instrument names to open driver sessions. This VI is available only in 64-bit LabVIEW.

[IMAGE alt='GetAllNIDigitalPatternInstrumentNames.vi' src='getallnidigitalpatterninstrumentnames.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Names returns an array of instrument names and comma-separated lists of instrument names that belong to the same group for all NI-Digital Pattern instruments in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getallnidigitalpatternsessions.html language=enus -->
## TOPIC 00019: Get All NI-Digital Pattern Sessions (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getallnidigitalpatternsessions.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getallnidigitalpatternsessions.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get All NI-Digital Pattern Sessions (TSM)

**Requires:** TSM

Returns all NI-Digital Pattern instrument sessions in the Semiconductor Module context. You can use instrument sessions to close driver sessions. This VI is available only in 64-bit LabVIEW.

[IMAGE alt='GetAllNIDigitalPatternSessions.vi' src='getallnidigitalpatternsessions.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Sessions returns the instrument sessions for all NI-Digital Pattern instruments in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getallnidmminstrumentnames.html language=enus -->
## TOPIC 00020: Get All NI-DMM Instrument Names (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getallnidmminstrumentnames.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getallnidmminstrumentnames.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get All NI-DMM Instrument Names (TSM)

**Requires:** TSM

Returns instrument names for all NI-DMM instruments in the Semiconductor Module context. You can use instrument names to open driver sessions.

[IMAGE alt='GetAllNIDMMInstrumentNames.vi' src='getallnidmminstrumentnames.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Names returns an array of the NI-DMM instrument names in the Semiconductor Module Context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getallnidmmsessions.html language=enus -->
## TOPIC 00021: Get All NI-DMM Sessions (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getallnidmmsessions.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getallnidmmsessions.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get All NI-DMM Sessions (TSM)

**Requires:** TSM

Returns all NI-DMM instrument sessions in the Semiconductor Module context. You can use instrument sessions to close driver sessions.

[IMAGE alt='GetAllNIDMMSessions.vi' src='getallnidmmsessions.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Sessions returns all NI-DMM instrument sessions in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getallnifgeninstrumentnames.html language=enus -->
## TOPIC 00022: Get All NI-FGEN Instrument Names (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getallnifgeninstrumentnames.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getallnifgeninstrumentnames.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get All NI-FGEN Instrument Names (TSM)

**Requires:** TSM

Returns the instrument names for all NI-FGEN instruments in the Semiconductor Module context. You can use instrument names to open driver sessions.

[IMAGE alt='GetAllNIFGenInstrumentNames.vi' src='getallnifgeninstrumentnames.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Names returns an array of the NI-FGEN instrument names in the Semiconductor Module Context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getallnifgensessions.html language=enus -->
## TOPIC 00023: Get All NI-FGEN Sessions (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getallnifgensessions.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getallnifgensessions.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get All NI-FGEN Sessions (TSM)

**Requires:** TSM

Returns all NI-FGEN instrument sessions in the Semiconductor Module context. You can use instrument sessions to close driver sessions.

[IMAGE alt='GetAllNIFGenSessions.vi' src='getallnifgensessions.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Sessions returns the instrument sessions for all NI-FGEN instruments in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getallnihsdioinstrumentnames.html language=enus -->
## TOPIC 00024: Get All NI-HSDIO Instrument Names (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getallnihsdioinstrumentnames.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getallnihsdioinstrumentnames.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get All NI-HSDIO Instrument Names (TSM)

**Requires:** TSM

Returns the instrument names for all NI-HSDIO instruments in the Semiconductor Module context. You can use instrument names to open driver sessions.

[IMAGE alt='GetAllNIHSDIOInstrumentNames.vi' src='getallnihsdioinstrumentnames.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Names returns an array of NI-HSDIO instrument names in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getallnihsdiosessions.html language=enus -->
## TOPIC 00025: Get All NI-HSDIO Sessions (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getallnihsdiosessions.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getallnihsdiosessions.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get All NI-HSDIO Sessions (TSM)

**Requires:** TSM

Returns all NI-HSDIO acquisition sessions and all NI-HSDIO generation sessions in the Semiconductor Module context.

[IMAGE alt='GetAllNIHSDIOSessions.vi' src='getallnihsdiosessions.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Acquisition Sessions returns the acquisition sessions for all NI-HSDIO instruments in the Semiconductor Module context. |
|  | Generation Sessions returns the generation sessions for all NI-HSDIO instruments in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getallnirfmxinstrumentnames.html language=enus -->
## TOPIC 00026: Get All NI-RFmx Instrument Names (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getallnirfmxinstrumentnames.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getallnirfmxinstrumentnames.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get All NI-RFmx Instrument Names (TSM)

**Requires:** TSM

Returns the instrument names for all NI-RFmx instruments in the Semiconductor Module context. You can use instrument names to open driver sessions.

[IMAGE alt='GetAllNIRFmxInstrumentNames.vi' src='getallnirfmxinstrumentnames.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Names returns an array of NI-RFmx instrument names in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getallnirfmxsessions.html language=enus -->
## TOPIC 00027: Get All NI-RFmx Sessions (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getallnirfmxsessions.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getallnirfmxsessions.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get All NI-RFmx Sessions (TSM)

**Requires:** TSM

Returns all NI-RFmx instrument sessions in the Semiconductor Module context. You can use instrument sessions to close driver sessions.

[IMAGE alt='GetAllNIRFmxSessions.vi' src='getallnirfmxsessions.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Sessions returns the NI-RFmx instrument sessions for all sites in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getallnirfpmdeembeddingdatawithpaths.html language=enus -->
## TOPIC 00028: Get All NI-RFPM De-embedding Data (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getallnirfpmdeembeddingdatawithpaths.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getallnirfpmdeembeddingdatawithpaths.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get All NI-RFPM De-embedding Data (TSM)

**Requires:** TSM

Returns the NI-RFPM subsystem sessions and paths and orientations of the S2P files that characterize the de-embedding network for every port connected to a DUT pin in the Semiconductor Module context.

[IMAGE alt='GetAllNIRFPMDeembeddingDataWithPaths.vi' src='getallnirfpmdeembeddingdatawithpaths.gif']

|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | De-embedding Files returns an array of de-embedding files, where each element is a cluster that includes the path and orientation of data in the S2P file that characterizes the de-embedding network for each port in the Ports List parameter. If the path is an absolute path, the VI returns the absolute path whether the file exists or not. If the path is a relative path and the file exists relative to the path of the pin map file, the VI returns the absolute path of the existing file. Otherwise, the VI returns a string without error. |
|  | Ports Lists returns an array of ports for each pin connected to an NI-RFPM subsystem in the Semiconductor Module Context |
|  | Instrument Sessions returns an array of NI-RFPM subsystem sessions, where each element is the session for each port in the Ports List parameter. |
|  | Semiconductor Module Context out returns the Semiconductor Module Context parameter unchanged. |
|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getallnirfpminstrumentnames.html language=enus -->
## TOPIC 00029: Get All NI-RFPM Instrument Names (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getallnirfpminstrumentnames.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getallnirfpminstrumentnames.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get All NI-RFPM Instrument Names (TSM)

**Requires:** TSM

Returns the names of all NI-RFPM subsystems and respective calibration file paths, IVI Switch names, and FPGA file paths in the Semiconductor Module context. You can use instrument names, IVI Switch names, FPGA file paths, and calibration file paths to open instrument and calibration sessions.

[IMAGE alt='GetAllNIRFPMInstrumentNames.vi' src='getallnirfpminstrumentnames.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | FPGA File Paths returns the paths to the FPGA files for the NI-VST instrument associated with NI-RFPM subsystems in the Semiconductor Module context. If the path is an absolute path, the VI returns the absolute path whether the file exists or not. If the path is a relative path and the file exists relative to the path of the pin map file, the VI returns the absolute path of the existing file. Otherwise, the VI returns a string without error. |
|  | IVI Switch Names returns the IVI Switch resource names associated with the NI-RFPM subsystems in the Semiconductor Module context. |
|  | Semiconductor Module Context out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Names returns the names of all the NI-RFPM subsystems in the Semiconductor Module context. |
|  | Calibration File Paths returns the paths to calibration files associated with NI-RFPM subsystems in the Semiconductor Module context. If the path is an absolute path, the VI returns the absolute path whether the file exists or not. If the path is a relative path and the file exists relative to the path of the pin map file, the VI returns the absolute path of the existing file. Otherwise, the VI returns a string without error. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getallnirfpmsessions.html language=enus -->
## TOPIC 00030: Get All NI-RFPM Sessions (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getallnirfpmsessions.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getallnirfpmsessions.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get All NI-RFPM Sessions (TSM)

**Requires:** TSM

Returns all NI-RFPM subsystem sessions in the Semiconductor Module context. You can use subsystem sessions to close driver sessions.

[IMAGE alt='GetAllNIRFPMSessions.vi' src='getallnirfpmsessions.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Sessions returns the NI-RFPM subsystem sessions of the instruments for all sites in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getallnirfsainstrumentnames.html language=enus -->
## TOPIC 00031: Get All NI-RFSA Instrument Names (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getallnirfsainstrumentnames.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getallnirfsainstrumentnames.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get All NI-RFSA Instrument Names (TSM)

**Requires:** TSM

Returns the instrument names for all NI-RFSA instruments in the Semiconductor Module context. You can use instrument names to open driver sessions.

[IMAGE alt='GetAllNIRFSAInstrumentNames.vi' src='getallnirfsainstrumentnames.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Names returns an array of NI-RFSA instrument names in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getallnirfsasessions.html language=enus -->
## TOPIC 00032: Get All NI-RFSA Sessions (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getallnirfsasessions.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getallnirfsasessions.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get All NI-RFSA Sessions (TSM)

**Requires:** TSM

Returns all NI-RFSA instrument sessions in the Semiconductor Module context. You can use instrument sessions to close driver sessions.

[IMAGE alt='GetAllNIRFSASessions.vi' src='getallnirfsasessions.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Sessions returns the NI-RFSA instrument sessions for all sites in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getallnirfsginstrumentnames.html language=enus -->
## TOPIC 00033: Get All NI-RFSG Instrument Names (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getallnirfsginstrumentnames.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getallnirfsginstrumentnames.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get All NI-RFSG Instrument Names (TSM)

**Requires:** TSM

Returns the instrument names for all NI-RFSG instruments in the Semiconductor Module context. You can use instrument names to open driver sessions.

[IMAGE alt='GetAllNIRFSGInstrumentNames.vi' src='getallnirfsginstrumentnames.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Names returns an array of NI-RFSG instrument names in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getallnirfsgsessions.html language=enus -->
## TOPIC 00034: Get All NI-RFSG Sessions (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getallnirfsgsessions.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getallnirfsgsessions.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get All NI-RFSG Sessions (TSM)

**Requires:** TSM

Returns all NI-RFSG instrument sessions in the Semiconductor Module context. You can use instrument sessions to close driver sessions.

[IMAGE alt='GetAllNIRFSGSessions.vi' src='getallnirfsgsessions.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Sessions returns the NI-RFSG instrument sessions for all sites in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getallniscopeinstrumentnames.html language=enus -->
## TOPIC 00035: Get All NI-SCOPE Instrument Names (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getallniscopeinstrumentnames.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getallniscopeinstrumentnames.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get All NI-SCOPE Instrument Names (TSM)

**Requires:** TSM

Returns instrument names and comma-separated instrument names that belong to the same group for all NI-SCOPE instruments in the Semiconductor Module context. You can use instrument names and comma-separated lists of instrument names to open driver sessions.

[IMAGE alt='GetAllNISCOPEInstrumentNames.vi' src='getallniscopeinstrumentnames.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Names returns an array of instrument names and comma-separated lists of instrument names that belong to the same group for all NI-SCOPE instruments in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getallniscopesessions.html language=enus -->
## TOPIC 00036: Get All NI-SCOPE Sessions (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getallniscopesessions.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getallniscopesessions.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get All NI-SCOPE Sessions (TSM)

**Requires:** TSM

Returns all NI-SCOPE instrument sessions in the Semiconductor Module context. You can use instrument sessions to close driver sessions.

[IMAGE alt='GetAllNISCOPESessions.vi' src='getallniscopesessions.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Sessions returns the instrument sessions for all NI-SCOPE instruments in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getallrelaydriverniswitchsessions.html language=enus -->
## TOPIC 00037: Get All Relay Driver NI-SWITCH Sessions (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getallrelaydriverniswitchsessions.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getallrelaydriverniswitchsessions.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get All Relay Driver NI-SWITCH Sessions (TSM)

**Requires:** TSM

Returns NI-SWITCH sessions for all relay driver modules in the Semiconductor Module context. You can use the NI-SWITCH sessions to close the relay driver module sessions. Note: Calling the Close VI on the returned sessions does not close the sessions if you did not open the session in LabVIEW.

[IMAGE alt='GetAllRelayDriverNISWITCHSessions.vi' src='getallrelaydriverniswitchsessions.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | NI-SWITCH Sessions returns the NI-SWITCH sessions for all relay driver modules in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getallsessiondata.html language=enus -->
## TOPIC 00038: Get All Session Data (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getallsessiondata.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getallsessiondata.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get All Session Data (TSM)

**Requires:** TSM

Returns all sessions in the Semiconductor Module context that belong to instruments of the type you specify in the **Instrument Type Id** parameter.

[IMAGE alt='GetAllSessionData.vi' src='getallsessiondata.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Instrument Type Id specifies the type ID for the instrument in the pin map file. All custom instruments defined in the pin map specify an associated type ID. Typically, this type ID is an instrument driver name or other ID that is common for instruments that users program in a similar way. For custom instruments, you must pass the type ID associated with the instrument in the pin map file. For model-based instruments, pass the string you passed to the Set Custom Session VI to store sessions for the instruments. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Channel Lists returns the channel lists for each of the channel group IDs. Each channel list is a comma-separated list of channels. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Session Data returns an array of session data set in the Semiconductor Module context. |
|  | Channel Group Ids returns the IDs of the channel groups on which Session Data was stored. For channels that do not belong to a channel group in the pin map, the Semiconductor Module creates a channel group with the same ID as the channel. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getdigitalpatternprojectcapturewaveformfilepaths.html language=enus -->
## TOPIC 00039: Get Digital Pattern Project Capture Waveform File Paths (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getdigitalpatternprojectcapturewaveformfilepaths.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getdigitalpatternprojectcapturewaveformfilepaths.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get Digital Pattern Project Capture Waveform File Paths (TSM)

**Requires:** TSM

Returns the file paths of all capture waveform files listed in the digital pattern project associated with the test program. This VI is available only in 64-bit LabVIEW.

[IMAGE alt='GetDigitalPatternProjectCaptureWaveformFilePaths.vi' src='getdigitalpatternprojectcapturewaveformfilepaths.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Capture Waveform File Paths returns the absolute paths of capture waveform files listed in the digital pattern project associated with the test program. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getdigitalpatternprojectpatternfilepaths.html language=enus -->
## TOPIC 00040: Get Digital Pattern Project Pattern File Paths (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getdigitalpatternprojectpatternfilepaths.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getdigitalpatternprojectpatternfilepaths.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get Digital Pattern Project Pattern File Paths (TSM)

**Requires:** TSM

Returns the file paths of all pattern files listed in the digital pattern project associated with the test program. This VI is available only in 64-bit LabVIEW.

[IMAGE alt='GetDigitalPatternProjectPatternFilePaths.vi' src='getdigitalpatternprojectpatternfilepaths.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Pattern File Paths returns the absolute paths of pattern files listed in the digital pattern project associated with the test program. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getdigitalpatternprojectsourcewaveformfilepaths.html language=enus -->
## TOPIC 00041: Get Digital Pattern Project Source Waveform File Paths (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getdigitalpatternprojectsourcewaveformfilepaths.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getdigitalpatternprojectsourcewaveformfilepaths.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get Digital Pattern Project Source Waveform File Paths (TSM)

**Requires:** TSM

Returns the file paths of all source waveform files listed in the digital pattern project associated with the test program. This VI is available only in 64-bit LabVIEW.

[IMAGE alt='GetDigitalPatternProjectSourceWaveformFilePaths.vi' src='getdigitalpatternprojectsourcewaveformfilepaths.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Source Waveform File Paths returns the absolute paths of source waveform files listed in the digital pattern project associated with the test program. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getdigitalpatternprojectspecificationslevelsandtimingfilepaths.html language=enus -->
## TOPIC 00042: Get Digital Pattern Project Specifications, Levels, and Timing File Paths (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getdigitalpatternprojectspecificationslevelsandtimingfilepaths.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getdigitalpatternprojectspecificationslevelsandtimingfilepaths.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get Digital Pattern Project Specifications, Levels, and Timing File Paths (TSM)

**Requires:** TSM

Returns the file paths of all specifications files, levels files, and timing files listed in the digital pattern project associated with the test program. This VI is available only in 64-bit LabVIEW.

[IMAGE alt='GetDigitalPatternProjectSpecificationsLevelsAndTimingFilePaths.vi' src='getdigitalpatternprojectspecificationslevelsandtimingfilepaths.gif']

|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Timing File Paths returns the absolute paths of timing files listed in the digital pattern project associated with the test program. |
|  | Levels File Paths returns the absolute paths of levels files listed in the digital pattern project associated with the test program. |
|  | Specifications File Paths returns the absolute paths of specifications files listed in the digital pattern project associated with the test program. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getglobaldata.html language=enus -->
## TOPIC 00043: Get Global Data (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getglobaldata.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getglobaldata.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get Global Data (TSM)

**Requires:** TSM

Returns a global data item that a previous call to the Set Global Data VI stored. You cannot obtain LabVIEW class references from this VI.

[IMAGE alt='GetGlobalData.vi' src='getglobaldata.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Data Id specifies the unique ID to distinguish the data. This parameter must match a value you specify in a call to the Set Global Data VI. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Data returns the specified global data item that a previous call to the Set Global Data VI stores. If no data with the specified Data Id parameter exists, the VI returns an error. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getinputdata.html language=enus -->
## TOPIC 00044: Get Input Data (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getinputdata.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getinputdata.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get Input Data (TSM)

**Requires:** TSM

Returns per-site input data as defined in the Semiconductor Multi Test step. You must manually select the polymorphic instance you want to use.

#### Double

Returns per-site double-precision, floating-point data as defined in the Semiconductor Multi Test step.

[IMAGE alt='GetInputDataDouble.vi' src='getinputdatadouble.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin specifies the name of the pin associated with the Data Out parameter. This parameter must match the values you specify on the Per-Site Inputs tab of the Semiconductor Multi Test step. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Input Data Id is the unique ID to distinguish the data. This parameter must match the values you specify on the Per-Site Inputs tab of the Semiconductor Multi Test step. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Data Out returns the per-site double-precision, floating-point data associated with the Data Source column for the row with a matching pin and Input Data Id parameter values in the Per-Site Inputs table on the Per-Site Inputs tab of the Semiconductor Multi Test step. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Boolean

Returns per-site Boolean data as defined in the Semiconductor Multi Test step.

[IMAGE alt='GetInputDataBoolean.vi' src='getinputdataboolean.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin specifies the name of the pin associated with the Data Out parameter. This parameter must match the values you specify on the Per-Site Inputs tab of the Semiconductor Multi Test step. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Input Data Id is the unique ID to distinguish the data. This parameter must match the values you specify on the Per-Site Inputs tab of the Semiconductor Multi Test step. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Data Out returns the per-site Boolean data associated with the Data Source column for the row with a matching pin and Input Data Id parameter values in the Per-Site Inputs table on the Per-Site Inputs tab of the Semiconductor Multi Test step. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### String

Returns per-site string data as defined in the Semiconductor Multi Test step.

[IMAGE alt='GetInputDataString.vi' src='getinputdatastring.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin specifies the name of the pin associated with the Data Out parameter. This parameter must match the values you specify on the Per-Site Inputs tab of the Semiconductor Multi Test step. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Input Data Id is the unique ID to distinguish the data. This parameter must match the values you specify on the Per-Site Inputs tab of the Semiconductor Multi Test step. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Data Out returns the per-site string data associated with the Data Source column for the row with matching the pin and Input Data Id parameter values in the Per-Site Inputs table on the Per-Site Inputs tab of the Semiconductor Multi Test step. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getmodelbasedinstrumentpropertylist.html language=enus -->
## TOPIC 00045: Get Model-Based Instrument Property List (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getmodelbasedinstrumentpropertylist.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getmodelbasedinstrumentpropertylist.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get Model-Based Instrument Property List (TSM)

**Requires:** TSM

Returns an object containing the name of the model and an array of model-based instrument property objects that contain the names and values of the instrument properties.

[IMAGE alt='GetModelBasedInstrumentPropertyList.vi' src='getmodelbasedinstrumentpropertylist.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Instrument Name the name of the instrument you want to query for instrument properties. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Model-Based Instrument Property List returns an object containing the name of the instrument model and an array of model-based instrument property objects that contain the name and value of a property defined for the instrument. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getmodelbasedinstrumentpropertyvalue.html language=enus -->
## TOPIC 00046: Get Model-Based Instrument Property Value (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getmodelbasedinstrumentpropertyvalue.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getmodelbasedinstrumentpropertyvalue.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get Model-Based Instrument Property Value (TSM)

**Requires:** TSM

Returns the value of a named property and a Boolean value indicating whether or not the named property was found in the property list supplied.

[IMAGE alt='GetModelBasedInstrumentPropertyValue.vi' src='getmodelbasedinstrumentpropertyvalue.gif']

|  | Properties an array of Model-Based Instrument Property elements to search. |
| --- | --- |
|  | Property Name specifies the name of the property for which to search. |
|  | Properties Out returns the array of model-based instrument property elements unchanged. |
|  | Property Value returns the found value for the named property. |
|  | Is Found returns TRUE if a property matching the supplied Property Name was found in the supplied array of model-based instrument property elements. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getmodelbasedinstrumentresourcepropertylist.html language=enus -->
## TOPIC 00047: Get Model-Based Instrument Resource Property List (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getmodelbasedinstrumentresourcepropertylist.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getmodelbasedinstrumentresourcepropertylist.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get Model-Based Instrument Resource Property List (TSM)

**Requires:** TSM

Returns an array of IModelBasedInstrumentResourcePropertyList objects where each element contains the name of a resource as well as an array of model-based instrument property objects that contain the names and values of the instrument resource properties.

[IMAGE alt='GetModelBasedInstrumentResourcePropertyList.vi' src='getmodelbasedinstrumentresourcepropertylist.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Instrument Name the name of the instrument you want to query for instrument properties. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Model-Based Instrument Resource Property List returns an array of IModelBasedInstrumentResourcePropertyList objects where each element contains the name of the instrument resource and an array of model-based instrument property objects, each containing the name and value of a property defined for the instrument. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getmodelbasedinstrumentresourcepropertyvalue.html language=enus -->
## TOPIC 00048: Get Model-Based Instrument Resource Property Value (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getmodelbasedinstrumentresourcepropertyvalue.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getmodelbasedinstrumentresourcepropertyvalue.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get Model-Based Instrument Resource Property Value (TSM)

**Requires:** TSM

Returns the value of a named property from a named resource and a Boolean value indicating whether or not the named property was found in the array of resource property lists supplied.

[IMAGE alt='GetModelBasedInstrumentResourcePropertyValue.vi' src='getmodelbasedinstrumentresourcepropertyvalue.gif']

|  | Model-Based Instrument Resource Property List an array of Model-Based Resource Property List elements to search. |
| --- | --- |
|  | Property Name specifies the name of the property for which to search. |
|  | Resource Name specifies the name of the resource to search for the specified property. |
|  | Model-Based Instrument Resource Property List Out returns the array of Model-Based Resource Property List elements unchanged. |
|  | Property Value returns the found value for the named property. |
|  | Is Found returns TRUE if a property matching the supplied Property Name was found in the supplied array of model-based instrument property elements. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getofflinemode.html language=enus -->
## TOPIC 00049: Get Offline Mode (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getofflinemode.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getofflinemode.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get Offline Mode (TSM)

**Requires:** TSM

Returns the current status of the Offline Mode setting. Offline Mode allows you to develop, run, and debug test programs on a computer without access to NI instruments.

[IMAGE alt='GetOfflineMode.vi' src='getofflinemode.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Is Semiconductor Module In Offline Mode returns a Boolean that indicates whether Semiconductor Module is currently in Offline Mode. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getpinmapfilepath.html language=enus -->
## TOPIC 00050: Get Pin Map File Path (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getpinmapfilepath.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getpinmapfilepath.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get Pin Map File Path (TSM)

**Requires:** TSM

Returns the file path of the pin map file associated with the test program. This VI is available only in 64-bit LabVIEW.

[IMAGE alt='GetPinMapFilePath.vi' src='getpinmapfilepath.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Pin Map File Path returns the absolute path of the pin map file associated with the test program. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getpinnames.html language=enus -->
## TOPIC 00051: Get Pin Names (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getpinnames.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getpinnames.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get Pin Names (TSM)

**Requires:** TSM

Returns all DUT and system pins available in the Semiconductor Module context that are connected to an instrument of the type you specify in the **Instrument Type Id** parameter. This VI returns only the pins specified on the Options tab of the Semiconductor Multi Test step. Pass an empty string to the **Instrument Type Id** parameter to return all available pins.

[IMAGE alt='GetPinNames.vi' src='getpinnames.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Instrument Type Id specifies the type of instrument for which you want to return DUT and system pins. For instruments that TSM natively supports, right-click the Instrument Type Id parameter, select Create Constant from the shortcut menu, and select the type of instrument you need. All custom instruments defined in the pin map specify an associated type ID. Typically, this type ID is an instrument driver name or other ID that is common for instruments that users program in a similar way. For custom instruments, you must pass the type ID associated with the instrument in the pin map file. For model-based instruments, pass the string you passed to the Set Custom Session VI to store sessions for the instruments. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Capability limits the filtered pins to those connected to a channel that defines the capability you specify. Use this parameter to differentiate between pins in the same instrument with different capabilities, such as NI-HSDIO Dynamic DIO channels and PFI lines. If a pin is connected to channels in which the capability is define only for a subset of sites, the VI returns an error. Pass an empty string to return all pins that match the type you specify in the Instrument Type Id parameter. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | DUT Pins returns an array of strings that contains the DUT pins in the Semiconductor Module context that are connected to an instrument of the type you specify in the Instrument Type Id parameter. |
|  | System Pins returns an array of strings that contains the system pins in the Semiconductor Module context that are connected to an instrument of the type you specify in the Instrument Type Id parameter. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getpinsinpingroup(s).html language=enus -->
## TOPIC 00052: Get Pins In Pin Group(s) (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getpinsinpingroup(s).html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getpinsinpingroup(s).html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get Pins In Pin Group(s) (TSM)

**Requires:** TSM

Returns a list of pins contained in the pin group or list of pin groups you specify. You must manually select the polymorphic instance you want to use. Select the single pin group or multiple pin groups polymorphic instance based on the number of pin groups you want to query.

#### Single Pin Group

Returns a list of pins contained in the pin group you specify in the **Pin Group** parameter.

[IMAGE alt='GetPinsInPinGroup.vi' src='getpinsinpingroup.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin Group specifies a pin group. The pin group must be included in the Semiconductor Module context. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Pins returns an array of pin names that are contained in the Pin Group parameter. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Multiple Pin Groups

Returns a list of pins contained in the pin groups you specify in the **Pin Groups** parameter.

[IMAGE alt='GetPinsInPinGroups.vi' src='getpinsinpingroups.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin Groups specifies an array of pin groups. The array must contain only pin groups that are included in the Semiconductor Module context. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Pins returns an array of pin names that are contained in the Pin Groups parameter. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getrelaydrivermodulenames.html language=enus -->
## TOPIC 00053: Get Relay Driver Module Names (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getrelaydrivermodulenames.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getrelaydrivermodulenames.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get Relay Driver Module Names (TSM)

**Requires:** TSM

Returns the names of all relay driver modules in the Semiconductor Module context. You can use the relay driver module names to open NI-SWITCH driver sessions for the relay driver modules.

[IMAGE alt='GetRelayDriverModuleNames.vi' src='getrelaydrivermodulenames.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Module Names returns an array of the relay driver module names in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getrelaynames.html language=enus -->
## TOPIC 00054: Get Relay Names (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getrelaynames.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getrelaynames.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get Relay Names (TSM)

**Requires:** TSM

Returns all site and system relays available in the Semiconductor Module context.

[IMAGE alt='GetRelayNames.vi' src='getrelaynames.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Site Relays returns an array of strings that contains the site relays in the Semiconductor Module context. |
|  | System Relays returns an array of strings that contains the system relays in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getrelaysinrelaygroup(s).html language=enus -->
## TOPIC 00055: Get Relays In Relay Group(s) (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getrelaysinrelaygroup(s).html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getrelaysinrelaygroup(s).html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get Relays In Relay Group(s) (TSM)

**Requires:** TSM

Returns a list of relays contained in the relay group or list of relay groups you specify. You must manually select the polymorphic instance you want to use. Select the single relay group or multiple relay groups polymorphic instance based on the number of relay groups you want to query.

#### Single Relay Group

Returns a list of relays contained in the relay group you specify in the **Relay Group** parameter.

[IMAGE alt='GetRelaysInRelayGroup.vi' src='getrelaysinrelaygroup.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Relay Group specifies a relay group. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Relays returns an array of relay names that are contained in the Relay Group parameter. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Multiple Relay Groups

Returns a list of relays contained in the relay groups you specify in the **Relay Groups** parameter.

[IMAGE alt='GetRelaysInRelayGroups.vi' src='getrelaysinrelaygroups.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Relay Groups specifies an array of relay groups. The array must contain only relay groups that are included in the Semiconductor Module context. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Relays returns an array of relay names that are contained in the Relay Groups parameter. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getsessionandchannelindexwithcontext.html language=enus -->
## TOPIC 00056: Get Session And Channel Index (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getsessionandchannelindexwithcontext.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getsessionandchannelindexwithcontext.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get Session And Channel Index (TSM)

**Requires:** TSM

Returns the index of the channel group and channel that corresponds to a pin query. Use this VI to access an individual pin when you take a measurement across multiple instruments and pins. When you call a pin query VI, such as the Pins to NI-HSDIO Sessions VI, the VI returns an array of sessions and a channel list. Use the Get Session and Channel Index VI to identify which session and which channel refers to a pin and site number you specify.

[IMAGE alt='GetSessionAndChannelIndexWithContext.vi' src='getsessionandchannelindexwithcontext.gif']

|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, and extract data from a set of measurements. |
| --- | --- |
|  | Pin specifies the name of the pin to obtain from the channel group and channel index in a previous pin query. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Site Number is the site number of the pin to obtain from the channel group and channel index in a previous pin query. To obtain a system pin, do not wire this input. |
|  | Pin Query Context Out returns the pin query context object unchanged. |
|  | Session Index returns the index of the session for a measurement taken on the pin and site number you specify. |
|  | Channel Index returns the index of the channel for a measurement taken on the pin and site number you specify. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getsessiondatapolymorphic.html language=enus -->
## TOPIC 00057: Get Session Data (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getsessiondatapolymorphic.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getsessiondatapolymorphic.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get Session Data (TSM)

**Requires:** TSM

Returns the session data, channel group IDs, and channel lists required to access one or more pins for a specified instrument type ID. You must manually select the polymorphic instance you want to use.

#### Multiple Pins - Multiple Sessions

Returns all sessions in the Semiconductor Module context associated with the pins.

[IMAGE alt='GetSessionData.vi' src='getsessiondata.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pins specifies the names of the pins or pin groups to translate to session data, channel group IDs, and channel lists. |
|  | Instrument Type Id specifies the type ID for the instrument in the pin map file. All custom instruments defined in the pin map specify an associated type ID. Typically, this type ID is an instrument driver name or other ID that is common for instruments that users program in a similar way. For custom instruments, you must pass the type ID associated with the instrument in the pin map file. For model-based instruments, pass the string you passed to the Set Custom Session VI to store sessions for the instruments. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, and extract data from a set of measurements. |
|  | Channel Lists returns the channel lists that correspond to the pins associated with session data and channel group IDs. Each channel list is a comma-separated list of channels. If any of the pins are connected to the same instrument channel for multiple sites, the channel appears only once in the list. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Session Data returns an array of session data associated with channel group IDs. |
|  | Channel Group Ids returns the IDs of the channel groups that contain the channels connected to the pins. For channels that do not belong to a channel group in the pin map, the Semiconductor Module creates a channel group with the same ID as the channel. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Single Pin - Multiple Sessions

Returns all sessions in the Semiconductor Module context associated with the pin.

[IMAGE alt='GetSessionDataSinglePinMultipleInstr.vi' src='getsessiondatasinglepinmultipleinstr.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin specifies the name of the pin or pin group to translate to session data, channel group IDs, and channel lists. |
|  | Instrument Type Id specifies the type ID for the instrument in the pin map file. All custom instruments defined in the pin map specify an associated type ID. Typically, this type ID is an instrument driver name or other ID that is common for instruments that users program in a similar way. For custom instruments, you must pass the type ID associated with the instrument in the pin map file. For model-based instruments, pass the string you passed to the Set Custom Session VI to store sessions for the instruments. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, and extract data from a set of measurements. |
|  | Channel Lists returns the channel lists that correspond to the pin associated with session data and channel group IDs. Each channel list is a comma-separated list of channels. If the pin is connected to the same instrument channel for multiple sites, the channel appears only once in the list. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Session Data returns an array of session data associated with channel group IDs. |
|  | Channel Group Ids returns the IDs of the channel groups that contain the channels connected to the pin. For channels that do not belong to a channel group in the pin map, the Semiconductor Module creates a channel group with the same ID as the channel. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Multiple Pins - Single Session

Returns the session in the Semiconductor Module context associated with the pins.

[IMAGE alt='GetSessionDataMultiplePinSingleInstr.vi' src='getsessiondatamultiplepinsingleinstr.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pins specifies the names of the pins or pin groups to translate to session data, channel group IDs, and channel lists. |
|  | Instrument Type Id specifies the type ID for the instrument in the pin map file. All custom instruments defined in the pin map specify an associated type ID. Typically, this type ID is an instrument driver name or other ID that is common for instruments that users program in a similar way. For custom instruments, you must pass the type ID associated with the instrument in the pin map file. For model-based instruments, pass the string you passed to the Set Custom Session VI to store sessions for the instruments. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, and extract data from a set of measurements. |
|  | Channel List returns the channel list that corresponds to the pins associated with session data and channel group ID. The channel list is a comma-separated list of channels. If any of the pins are connected to the same instrument channel for multiple sites, the channel appears only once in the list. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Session Data returns the session data associated with the channel group ID. |
|  | Channel Group Id returns the ID of the channel groups that contain the channels connected to the pins. For channels that do not belong to a channel group in the pin map, the Semiconductor Module creates a channel group with the same ID as the channel. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Single Pin - Single Session

Returns the session in the Semiconductor Module context associated with the pin.

[IMAGE alt='GetSessionDataSinglePinSingleInstr.vi' src='getsessiondatasinglepinsingleinstr.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin specifies the name of the pin or pin group to translate to session data, channel group ID, and channel list |
|  | Instrument Type Id specifies the type ID for the instrument in the pin map file. All custom instruments defined in the pin map specify an associated type ID. Typically, this type ID is an instrument driver name or other ID that is common for instruments that users program in a similar way. For custom instruments, you must pass the type ID associated with the instrument in the pin map file. For model-based instruments, pass the string you passed to the Set Custom Session VI to store sessions for the instruments. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, and extract data from a set of measurements. |
|  | Channel List returns the channel list that correspond to the pin associated with session data and channel group ID. The channel list is a comma-separated list of channels. If the pin is connected to the same instrument channel for multiple sites, the channel appears only once in the list. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Session Data returns the session data associated with the channel group ID. |
|  | Channel Group Id returns the ID of the channel group that contains the channels connected to the pin. For channels that do not belong to a channel group in the pin map, the Semiconductor Module creates a channel group with the same ID as the channel. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getsitedata.html language=enus -->
## TOPIC 00058: Get Site Data (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getsitedata.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getsitedata.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get Site Data (TSM)

**Requires:** TSM

Returns per-site data that a previous call to the Set Site Data VI stores. The returned array contains the data the Semiconductor Module context stores for each site in the same order as the sites that the Get Site Numbers VI returns. If data with the specified **Data Id** does not exist for every site in the Semiconductor Module Context, the VI returns an error. You cannot obtain LabVIEW class references from this VI.

[IMAGE alt='GetSiteData.vi' src='getsitedata.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Data Id specifies the unique ID to distinguish the data. This parameter must match a value you specify in a call to the Set Site Data VI. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Site Data specifies an array of data with one element for each site in the system or one element for each site in the Semiconductor Module Context. If the array is empty, the VI deletes any data with the specified Data Id parameter if it exists. If the array contains data for each site in the Semiconductor Module context, each item in the array contains data for the site specified by the corresponding item in the Get Site Numbers VI. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getsitenumbers.html language=enus -->
## TOPIC 00059: Get Site Numbers (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getsitenumbers.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getsitenumbers.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get Site Numbers (TSM)

**Requires:** TSM

Returns the site numbers and number of sites in the Semiconductor Module context.

[IMAGE alt='GetSiteNumbers.vi' src='getsitenumbers.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Site Numbers returns an array of site numbers for the test sites in the Semiconductor Module context. The site numbers can be different each time a step executes because some sites might not be active. The site numbers are in numerical order. |
|  | Number Of Sites returns the number of elements in the Site Numbers parameter. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getsitesemiconductormodulecontexts.html language=enus -->
## TOPIC 00060: Get Site Semiconductor Module Contexts (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getsitesemiconductormodulecontexts.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getsitesemiconductormodulecontexts.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get Site Semiconductor Module Contexts (TSM)

**Requires:** TSM

Returns an array of Semiconductor Module context objects, each of which represents a single site. The size and ordering of the array match the size and ordering of the sites in the Semiconductor Module Context input. You must always close references to the Semiconductor Module contexts, even if you do not use them in your code module.

[IMAGE alt='GetSiteSemiconductorModuleContexts.vi' src='getsitesemiconductormodulecontexts.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Site Semiconductor Module Contexts returns an array of Semiconductor Module context objects, each of which represents a single site. The size and ordering of the array match the size and ordering of the array returned by the GetSiteNumbers VI. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getswitchnames.html language=enus -->
## TOPIC 00061: Get All Switch Names (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getswitchnames.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getswitchnames.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get All Switch Names (TSM)

**Requires:** TSM

Returns the names of all switches of the type you specify in the **Multiplexer Type Id** parameter in the Semiconductor Module context. You can use switch names to open driver sessions.

[IMAGE alt='GetSwitchNames.vi' src='getswitchnames.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Multiplexer Type Id specifies the type ID for the multiplexer in the pin map file. When you add a multiplexer to the pin map file, you can define a type ID for the multiplexer, such as the driver name. Multiplexers in the pin map that do not specify a type ID have a default ID of NIGenericMultiplexer. Leave this parameter unwired to use the default value. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Switch Names returns the names of all switches in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/getswitchsessions.html language=enus -->
## TOPIC 00062: Get All Switch Sessions (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/getswitchsessions.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/getswitchsessions.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get All Switch Sessions (TSM)

**Requires:** TSM

Returns all sessions for switches of the type you specify in the **Multiplexer Type Id** parameter in the Semiconductor Module context.

[IMAGE alt='GetSwitchSessions.vi' src='getswitchsessions.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Multiplexer Type Id specifies the type ID for the multiplexer in the pin map file. When you add a multiplexer to the pin map file, you can define a type ID for the multiplexer, such as the driver name. Multiplexers in the pin map that do not specify a type ID have a default ID of NIGenericMultiplexer. Leave this parameter unwired to use the default value. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Session Data returns sessions to all switches of the type you specify in the Multiplexer Type Id in the Semiconductor Module context for which you set session data. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/globaldataexists.html language=enus -->
## TOPIC 00063: Global Data Exists? (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/globaldataexists.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/globaldataexists.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Global Data Exists? (TSM)

**Requires:** TSM

Returns a Boolean value indicating whether global data exists for the data ID specified by the **Data Id** parameter.

[IMAGE alt='GlobalDataExists.vi' src='globaldataexists.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Data Id specifies the unique ID to distinguish the data. This parameter must match a value you specify in a call to the Set Global Data VI. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Global Data Exists? indicates whether the specified Data Id parameter has data associated with it. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/linkingtsmfiletolabviewproject.html language=enus -->
## TOPIC 00064: Linking a Sequence File to a LabVIEW Project File (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/linkingtsmfiletolabviewproject.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/linkingtsmfiletolabviewproject.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Linking a Sequence File to a LabVIEW Project File (TSM)

Use the Semiconductor Module Link Manager dialog box to link sequence files to a LabVIEW project file, which allows the selected sequence file(s) to populate [pin](pincontrol.html), [relay](relaydriverpal.html), [relay configuration](relaydriverpal.html), [specification](specificationspal.html), [published data ID](publisheddataidcontrol.html), and [input data ID controls](advancedpal.html) in the selected LabVIEW project. Choose one of the following options to launch the Semiconductor Module Link Manager dialog box:

- Click the Semiconductor Module Link Manager button in the Project Explorer window.
- Right-click the project root in the Project Explorer window and select Semiconductor Module Link Manager .
- Right-click the control and select Semiconductor Module Link Manager .

The Semiconductor Module Link Manager dialog box allows you to add or remove linked sequence files and displays all sequence files linked to the open LabVIEW project file. If you link multiple sequence files with different pin map or specification files, TSM combines the values into a single list when populating the controls. The order of the sequence files determines the order in which the values are listed in the control. To reorder the sequence files, use drag and drop.

If you make any changes in the Semiconductor Module Link Manager dialog box, the dialog box prompts you to save now or to save the project later. If you do not save now, you must save later for the changes to persist.

If you modify the pin map, specification files, published data IDs, or input data IDs of a linked sequence file while the LabVIEW project file is open, right-click the corresponding control and click **Refresh** to update the listed values.

You can also link a TSM sequence file to a LabVIEW project file in TSM. Refer to *LabVIEW Project Panel* in the *TestStand Semiconductor Module Help* for more information.

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/lvtssemiconductor.html language=enus -->
## TOPIC 00065: TestStand Semiconductor Module Code Module VIs Help

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/lvtssemiconductor.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/lvtssemiconductor.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

TestStand Semiconductor Module Code Module VIs Help

April 2022, 373951M-01

Use the TestStand Semiconductor Module™ (TSM) [Code Module API](/csh?topicname=tssemiconductor/codemoduledevelopmentapi.html) to develop code modules to perform tests using DUT pin or pin group names. You can use this API to manage pins, instruments, sessions, sites, data, switching, specifications, and to publish measurement data.

The VIs on this palette return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html).

| Palette Object | Description |
| --- | --- |
| Get Pin Names | Returns all DUT and system pins available in the Semiconductor Module context that are connected to an instrument of the type you specify in the Instrument Type Id parameter. This VI returns only the pins specified on the Options tab of the Semiconductor Multi Test step. Pass an empty string to the Instrument Type Id parameter to return all available pins or pin groups. |
| Publish Data | Publishes measurement data for one or more pins to the Semiconductor Multi Test step type instances for all sites in the Semiconductor Module context. If you are publishing site data, the polymorphic instance must publish data for each site in the Semiconductor Module context. If you are publishing pin data, the polymorphic instance must support the pin query context obtained from the specific Pin(s) to Session(s), Pin to FPGA VI Reference(s), or Get Session Data VI you previously created. Pin(s) to Session(s) VIs include the following: Pin(s) to NI-Digital Pattern Sessions Pin(s) to NI-DMM Session(s) Pin(s) to NI-FGEN Session(s) Pin(s) to NI-SCOPE Session(s) Pin(s) to NI-HSDIO Session(s) Pin(s) to NI-DCPower Session(s) Pin to NI-RFSA Session(s) Pin to NI-RFSG Session(s) Pin to NI-RFmx Session(s) |
| Pin Control | Use the pin control to create a control populated with the pins from a linked sequence file. This allows you to select a value from the control's populated list rather than entering the value as a string. If there is no sequence file linked to the LabVIEW project, or if you are editing the LabVIEW project on a system that cannot access the sequence file, the control acts as a string. |
| Published Data Id Control | Use the published data ID control to create a control populated with the published data IDs from a linked sequence file. This allows you to select a value from the control's populated list rather than entering the value as a string. If there is no sequence file linked to the LabVIEW project, or if you are editing the LabVIEW project on a system that cannot access the sequence file, the control acts as a string. |

| Subpalette | Description |
| --- | --- |
| NI-Digital Pattern VIs | Use the NI-Digital Pattern VIs to manage NI-Digital Pattern instruments and sessions, to manage NI-Digital Pattern waveform data, and to access digital pattern project files. |
| NI-DCPower VIs | Use the NI-DCPower VIs to manage NI-DCPower instruments and sessions. |
| NI-DAQmx VIs | Use the NI-DAQmx VIs to manage NI-DAQmx tasks. |
| NI-DMM VIs | Use the NI-DMM VIs to manage NI-DMM instruments and sessions. |
| NI-FGEN VIs | Use the NI-FGEN VIs to manage NI-FGEN instruments and sessions. |
| NI-SCOPE VIs | Use the NI-SCOPE VIs to manage NI-SCOPE instruments and sessions. |
| RF VIs | Use the NI-RFSA, NI-RFSG, NI-RFmx, NI-RFPM, and FPGA VIs to manage NI-RFSA, NI-RFSG, NI-RFPM, and RF RIO (RF LabVIEW FPGA enabled) instruments. |
| Model-Based Instrument VIs | Use Model-Based Instrument VIs to return the names, properties, and values of model-based instruments. |
| NI-HSDIO VIs | Use the NI-HSDIO VIs to manage NI-HSDIO instruments and sessions and to create and rearrange multisite digital waveforms. |
| Switching VIs | Use the Switching VIs to store and return switch sessions, return the names of all switches defined in the pin map, and access a switched pin. |
| Relay Driver VIs | Use the Relay Driver VIs to manage PXI-2567 relay driver modules and sessions and to switch relays. This palette also contains the relay and relay configuration controls, which you can use to create controls populated with the relays and relay configurations from a linked sequence file. |
| Custom Instrument VIs | Use the Custom Instruments VIs to manage custom instruments and sessions for instruments that TSM does not natively support. |
| Specifications VIs | Use the Specifications VIs to obtain resolved values defined in the specification file the test program specifies. This palette also contains the specification control, which you can use to create a control populated with the specifications from a linked sequence file. |
| Site and Global Data VIs | Use the Site and Global data VIs to manage site and global data |
| Advanced VIs | Use the Advanced VIs to query the site numbers in the Semiconductor Module context, return the status of the Offline Mode setting, and transform per-instrument to per-site data. This palette also contains the input data ID control, which you can use to create a control populated with the input data IDs from a linked sequence file. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/modelbasedinstrumentpal.html language=enus -->
## TOPIC 00066: Model-Based Instrument VIs (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/modelbasedinstrumentpal.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/modelbasedinstrumentpal.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Model-Based Instrument VIs (TSM)

Use Model-Based Instrument VIs to return the names, properties, and values of model-based instruments.

The VIs on this palette return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html).

| Palette Object | Description |
| --- | --- |
| Get All Model-Based Instrument Names | Returns the instrument names and models for all model-based instruments in the Semiconductor Module context. You can use instrument names to query the model properties for the information needed to create the appropriate sessions to drive the instrument. |
| Get Model-Based Instrument Property List | Returns an object containing the name of the model and an array of ModelBasedInstrumentProperty objects that contain the names and values of the instrument properties. |
| Get Model-Based Instrument Resource Property List | Returns an array of IModelBasedInstrumentResourcePropertyList objects where each element contains the name of a resource as well as an array of ModelBasedInstrumentProperty objects that contain the names and values of the instrument resource properties. |
| Get Model-Based Instrument Property Value | Returns the value of a named property and a Boolean value indicating whether or not the named property was found in the property list supplied. |
| Get Model-Based Instrument Resource Property Value | Returns the value of a named property from a named resource and a Boolean value indicating whether or not the named property was found in the array of resource property lists supplied. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/namespacedsymbol(s)tovalue(s).html language=enus -->
## TOPIC 00067: Get Specification(s) Value(s) (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/namespacedsymbol(s)tovalue(s).html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/namespacedsymbol(s)tovalue(s).html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get Specification(s) Value(s) (TSM)

**Requires:** TSM

Returns the value or values calculated for the variables in the Semiconductor Module context specifications file.

#### One Symbol - One Value

Returns the value calculated from the **Symbol** parameter in the Semiconductor Module context specifications file. If the associated specifications file or symbols cannot be found, the VI returns an error.

[IMAGE alt='NamespacedSymbolToValue.vi' src='namespacedsymboltovalue.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Symbol is the variable string to look up in the Semiconductor Module context specifications file to obtain a calculated value. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Value returns the calculated value for the Symbol parameter in the Semiconductor Module context specifications file. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Multiple Symbols - Multiple Values

Returns the values calculated from the **Symbols** parameter in the Semiconductor Module context specifications file. If the associated specifications file or symbols cannot be found, the VI returns an error.

[IMAGE alt='NamespacedSymbolsToValues.vi' src='namespacedsymbolstovalues.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Symbols is the array of variable strings to look up in the Semiconductor Module context specifications file to obtain calculated values. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Values returns the calculated values for the symbols in the Semiconductor Module context specifications file. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/nidaqmxpal.html language=enus -->
## TOPIC 00068: NI-DAQmx VIs (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/nidaqmxpal.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/nidaqmxpal.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

NI-DAQmx VIs (TSM)

Use the NI-DAQmx VIs to manage NI-DAQmx tasks.

The VIs on this palette return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html).

| Palette Object | Description |
| --- | --- |
| Get All NI-DAQmx Task Names | Returns task names for all NI-DAQmx tasks of type Task Type in the Semiconductor Module context. You can use task names to create tasks. |
| Set NI-DAQmx Task | Associates an NI-DAQmx task with an NI-DAQmx task name. |
| Get All NI-DAQmx Tasks | Returns all NI-DAQmx tasks of type Task Type in the Semiconductor Module context. You can use tasks to perform NI-DAQmx operations. |
| Pin(s) To NI-DAQmx Task(s) | Returns the NI-DAQmx tasks and channel lists required to access one or more pins. You must manually select the polymorphic instance you want to use. |
| Create Multisite Data For Analog Output | Accepts per site/pin data and returns data for all channels in the tasks. Use this data with the DAQmx Write VI. You must manually select the polymorphic instance you want to use. |

##### Related Information

[Using NI-DAQmx with TSM](daqmxtsmconcepts.html)

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/nidcpowerpal.html language=enus -->
## TOPIC 00069: NI-DCPower VIs (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/nidcpowerpal.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/nidcpowerpal.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

NI-DCPower VIs (TSM)

Use the NI-DCPower VIs to manage NI-DCPower instruments and sessions.

The VIs on this palette return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html).

| Palette Object | Description |
| --- | --- |
| Get All NI-DCPower Sessions | Returns all NI-DCPower instrument sessions in the Semiconductor Module context. |
| Set NI-DCPower Session with Resource String | Associates an NI-DCPower session with all resources of an NI-DCPower resource string. |
| Get All NI-DCPower Resource Strings | Returns the resource strings associated with each channel group in the ISemiconductorModuleContext. A resource string is a comma-separated list of NI-DCPower resources, each resource is defined by <instrument>/<channel> associated with the NI-DCPower channel group. You can use the resource strings to open driver sessions. All resources within the same resource string will be controlled by the same session. |
| Pin(s) To NI-DCPower Session(s) | Returns the NI-DCPower instrument sessions and channel lists required to access one or more pins. You must manually select the polymorphic instance you want to use. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/nidigitalpal.html language=enus -->
## TOPIC 00070: NI-Digital Pattern VIs (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/nidigitalpal.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/nidigitalpal.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

NI-Digital Pattern VIs (TSM)

Use the NI-Digital Pattern VIs to manage NI-Digital Pattern instruments and sessions, to manage NI-Digital Pattern waveform data, and to access digital pattern project files.

|  | Note The VIs on this palette are available only in 64-bit LabVIEW. |
| --- | --- |

The VIs on this palette return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html).

| Palette Object | Description |
| --- | --- |
| Get All NI-Digital Pattern Instrument Names | Returns the names of all NI-Digital Pattern instruments in the Semiconductor Module context. You can use instrument names to open driver sessions. This VI is available only in 64-bit LabVIEW. |
| Set NI-Digital Pattern Session | Associates an instrument session with an NI-Digital Pattern instrument name. This VI is available only in 64-bit LabVIEW. |
| Get All NI-Digital Pattern Sessions | Returns all NI-Digital Pattern instrument sessions in the Semiconductor Module context. This VI is available only in 64-bit LabVIEW. |
| Pin(s) to NI-Digital Pattern Sessions | Returns the NI-Digital Pattern sessions, channel lists, and site lists required to access one or more pins. You must manually select the polymorphic instance you want to use. This VI is available only in 64-bit LabVIEW. |
| Per-Instrument to Per-Site Pattern Results | Converts pattern results indexed by instruments to pattern results indexed by sites. Pass input pattern results indexed by instruments in the same order that the Pin(s) to NI-Digital Pattern Sessions VI returns. The VI returns pattern results indexed by sites in the same order that the Get Site Numbers VI returns. This VI is available only in 64-bit LabVIEW. |

| Subpalettes | Description |
| --- | --- |
| Source/Capture VIs | Use the Source/Capture VIs to manage NI-Digital Pattern waveform data. |
| Setup VIs | Use the Setup VIs to obtain file paths for digital pattern project files. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/nidigitalsetuppal.html language=enus -->
## TOPIC 00071: Setup VIs (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/nidigitalsetuppal.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/nidigitalsetuppal.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Setup VIs (TSM)

Use the Setup VIs to obtain file paths for digital pattern project files.

|  | Note The VIs on this palette are available only in 64-bit LabVIEW. |
| --- | --- |

The VIs on this palette return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html).

| Palette Object | Description |
| --- | --- |
| Get Pin Map File Path | Returns the file path of the pin map file associated with the test program. This VI is available only in 64-bit LabVIEW. |
| Get Digital Pattern Project Specifications, Levels, and Timing File Paths | Returns the file paths of all specifications files, levels files, and timing files listed in the digital pattern project associated with the test program. This VI is available only in 64-bit LabVIEW. |
| Get Digital Pattern Project Pattern File Paths | Returns the file paths of all pattern files listed in the digital pattern project associated with the test program. This VI is available only in 64-bit LabVIEW. |
| Get Digital Pattern Project Source Waveform File Paths | Returns the file paths of all source waveform files listed in the digital pattern project associated with the test program. This VI is available only in 64-bit LabVIEW. |
| Get Digital Pattern Project Capture Waveform File Paths | Returns the file paths of all capture waveform files listed in the digital pattern project associated with the test program. This VI is available only in 64-bit LabVIEW. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/nidigitalsourcecapturepal.html language=enus -->
## TOPIC 00072: Source/Capture VIs (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/nidigitalsourcecapturepal.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/nidigitalsourcecapturepal.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Source Capture VIs (TSM)

Use the Source/Capture VIs to manage NI-Digital Pattern waveform data.

|  | Note The VIs on this palette are available only in 64-bit LabVIEW. |
| --- | --- |

The VIs on this palette return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html).

| Palette Object | Description |
| --- | --- |
| Per-Instrument to Per-Site Waveforms | Converts digital waveforms indexed by instruments in the same order that the Pin(s) to NI-Digital Pattern Sessions VI returns into waveforms indexed by sites in the same order that the Get Site Numbers VI returns. This VI is available only in 64-bit LabVIEW. |
| Per-Site to Per-Instrument Waveforms | Converts digital waveforms indexed by sites in the same order that the Get Site Numbers VI returns into waveforms indexed by instruments in the same order that the Pin(s) to NI-Digital Pattern Sessions VI returns. This VI is available only in 64-bit LabVIEW. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/nidmmpal.html language=enus -->
## TOPIC 00073: NI-DMM VIs (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/nidmmpal.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/nidmmpal.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

NI-DMM VIs (TSM)

Use the NI-DMM VIs to manage NI-DMM instruments and sessions.

The VIs on this palette return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html).

| Palette Object | Description |
| --- | --- |
| Get All NI-DMM Instrument Names | Returns instrument names for all NI-DMM instruments in the Semiconductor Module context. You can use instrument names to open driver sessions. |
| Set NI-DMM Session | Associates an instrument session with an NI-DMM instrument name. |
| Get All NI-DMM Sessions | Returns all NI-DMM instrument sessions in the Semiconductor Module context. |
| Pin(s) To NI-DMM Session(s) | Returns the NI-DMM instrument sessions required to access one or more pins. You must manually select the polymorphic instance you want to use. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/nifgenpal.html language=enus -->
## TOPIC 00074: NI-FGEN VIs (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/nifgenpal.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/nifgenpal.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

NI-FGEN VIs (TSM)

Use the NI-FGEN VIs to manage NI-FGEN instruments and sessions.

The VIs on this palette return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html).

| Palette Object | Description |
| --- | --- |
| Get All NI-FGEN Instrument Names | Returns the instrument names for all NI-FGEN instruments in the Semiconductor Module context. You can use instrument names to open driver sessions. |
| Set NI-FGEN Session | Associates an instrument session with an NI-FGEN instrument name. |
| Get All NI-FGEN Sessions | Returns all NI-FGEN instrument sessions in the Semiconductor Module context. |
| Pin(s) To NI-FGEN Session(s) | Returns the NI-FGEN instrument sessions required to access one or more pins. You must manually select the polymorphic instance you want to use. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/nihsdiopal.html language=enus -->
## TOPIC 00075: NI-HSDIO VIs (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/nihsdiopal.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/nihsdiopal.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

NI-HSDIO VIs (TSM)

Use the NI-HSDIO VIs to manage NI-HSDIO instruments and sessions and to create and rearrange multisite digital waveforms.

The VIs on this palette return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html).

| Palette Object | Description |
| --- | --- |
| Get All NI-HSDIO Instrument Names | Returns the instrument names for all NI-HSDIO instruments in the Semiconductor Module context. You can use instrument names to open driver sessions. |
| Set NI-HSDIO Sessions | Associates an NI-HSDIO acquisition session and an NI-HSDIO generation session with an NI-HSDIO instrument name. |
| Get All NI-HSDIO Sessions | Returns all NI-HSDIO acquisition sessions and all NI-HSDIO generation sessions in the Semiconductor Module context. |
| Pin(s) To NI-HSDIO Session(s) | Returns the NI-HSDIO acquisition sessions, generation sessions, and channel lists required to access one or more pins. You must manually select the polymorphic instance you want to use. |
| Get NI-HSDIO Masks | Returns an array of channel masks in which each element corresponds to a site in the Semiconductor Module context. Each element in the array is an unsigned number in which a bit is asserted if a pin is connected to that channel. You can use the masks to identify which site failed in a functional test. |
| Create Multisite Digital Waveforms | Creates multisite digital waveforms based on the pin map. Use the Single Waveform to All Sites instance when you want to write the same waveform for each site. Use the Per Site Waveforms instance when you want to write different waveforms for each site. |
| Rearrange Multisite Digital Waveforms | Rearranges multisite waveforms read from NI-HSDIO instruments into per-site digital waveforms. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/niscopepal.html language=enus -->
## TOPIC 00076: NI-SCOPE VIs (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/niscopepal.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/niscopepal.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

NI-SCOPE VIs (TSM)

Use the NI-SCOPE VIs to manage NI-SCOPE instruments and sessions.

The VIs on this palette return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html).

| Palette Object | Description |
| --- | --- |
| Get All NI-SCOPE Instrument Names | Returns instrument names for all NI-SCOPE instruments in the Semiconductor Module context. You can use instrument names to open driver sessions. |
| Set NI-SCOPE Session | Associates an instrument session with an NI-SCOPE instrument name. |
| Get All NI-SCOPE Sessions | Returns all NI-SCOPE instrument sessions in the Semiconductor Module context. |
| Pin(s) To NI-SCOPE Session(s) | Returns the NI-SCOPE instrument sessions required to access one or more pins. You must manually select the polymorphic instance you want to use. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/obsoletetsmvis.html language=enus -->
## TOPIC 00077: Obsolete VIs (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/obsoletetsmvis.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/obsoletetsmvis.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Obsolete VIs (TSM)

The following VIs are now obsolete. NI supports these VIs but recommends that you update files to reflect these changes to ensure compatibility with future versions of TSM.

|  | Note Because the name of some of the VIs remains the same, verify the filename of the VI to ensure you are using the updated version of the VI. |
| --- | --- |

| Obsolete VI | Preferred VI |
| --- | --- |
| 2 Pins to NI-RFPM Sessions 2PinsToNIRFPMSessions.vi | 2 Pins to NI-RFPM Sessions 2PinsToNIRFPMSessionsWithPaths.vi |
| Create Multisite Data For Analog Output CreateMultisiteDataForAnalogOutput.vi | Create Multisite Data For Analog Output CreateMultisiteDataForDAQmxAnalogOutput.vi |
| Create Multisite Digital Waveforms CreateMultisiteDigitalWaveforms.vi | Create Multisite Digital Waveforms CreateMultisiteDigitalWaveformsWithContext.vi |
| Get All NI-DCPower Instrument Names GetAllNIDCPowerInstrumentNames.vi | Get All NI-DCPower Resource Strings GetAllNIDCPowerResourceStrings.vi |
| Get All NI-RFPM De-embedding Data GetAllNIRFPMDeembeddingData.vi | Get All NI-RFPM De-embedding Data GetAllNIRFPMDeembeddingDataWithPaths.vi |
| Get Session and Channel Index GetSessionAndChannelIndex.vi | Get Session and Channel Index GetSessionAndChannelIndexWithContext.vi |
| Pins to NI-HSDIO Channel Masks PinsToNIHSDIOChannelMasks.vi | Get NI-HSDIO Channel Masks PinsToNIHSDIOChannelMasksWithContext.vi |
| Pin(s) to NI-RFPM Sessions PinsToNIRFPMSessions.vi | Pin(s) to NI-RFPM Sessions PinsToNIRFPMSessionsWithPaths.vi |
| Publish Data PublishData.vi | Publish Data PublishDataWithContext.vi |
| Rearrange Digital Multisite Waveforms RearrangeDigitalMultisiteWaveforms.vi | Rearrange Digital Multisite Waveforms RearrangeDigitalMultisiteWaveformsWithContext.vi |
| Set NI-DCPower Session SetNIDCPowerSession.vi | Set NI-DCPower Session with Resource String SetNIDCPowerSessionWithResourceString.vi |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/perinstrumenttopersitedata.html language=enus -->
## TOPIC 00078: Per-Instrument to Per-Site Data (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/perinstrumenttopersitedata.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/perinstrumenttopersitedata.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Per-Instrument to Per-Site Data (TSM)

**Requires:** TSM

Transforms the measurement data from measurements obtained from an instrument session and arranges the data in the order of sites and pins in the Semiconductor Module context.

Use this VI when you have raw measurement data from an instrument session that you need to manipulate in a site-specific way. For example, if you need to perform an operation on the measurement data using per-site input data, this VI puts the measurement data for all pins into the same per-site order as the input data. Similarly, if you need to modify the data from a specific site before publishing, this VI puts the measurement data for the all pins into a per-site array that you can then index to retrieve the data for the specific site. The order of the per-site array matches the order of the **Site Numbers** output parameter of the Get Site Numbers VI.

#### Parametric:1D Array

Converts measurement data from a 1D array of double measurements that is ordered by channels on a single instrument session into a 2D array that is arranged by the sites and pins in the Semiconductor Module Context.

[IMAGE alt='Per-Instrument To Per-Site Data 1D Array Double.vi' src='per-instrument_to_per-site_data_1d_array_double.gif']

|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
| --- | --- |
|  | Per-Instrument Data specifies the multisite measurement data from multiple pins connected to one or more instrument sessions. The array consists of either a collection of single measurements made from multiple instrument sessions or a collection of multiple measurements made from a single instrument session. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Per-Site/Pin Data the multisite measurement data from the Data In parameter rearranged by sites and pins. Each row represents measurements for one site, and each column represents a measurement for a pin in the pin query context. Use the Get Site Numbers VI to get the site number for each row. The order of the columns matches the order of the pins parameter in the pin query. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Pass/Fail:1D Array

Converts measurement data from a 1D array of Boolean measurements that is ordered by channels on a single instrument session into a 2D array that is arranged by the sites and pins in the Semiconductor Module Context.

[IMAGE alt='Per-Instrument To Per-Site Data 1D Array Bool.vi' src='per-instrument_to_per-site_data_1d_array_bool.gif']

|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
| --- | --- |
|  | Per-Instrument Data specifies the multisite measurement data from multiple pins connected to one or more instrument sessions. The array consists of either a collection of single measurements made from multiple instrument sessions or a collection of multiple measurements made from a single instrument session. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Per-Site/Pin Data the multisite measurement data from the Data In parameter rearranged by sites and pins. Each row represents measurements for one site, and each column represents a measurement for a pin in the pin query context. Use the Get Site Numbers VI to get the site number for each row. The order of the columns matches the order of the pins parameter in the pin query. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Parametric:2D Array

Transforms measurement data from a 2D array of double measurements that is arranged by instrument sessions and channels into a 2D array that is arranged by the sites and pins in the Semiconductor Module Context.

[IMAGE alt='Per-Instrument To Per-Site Data 2D Array Double.vi' src='per-instrument_to_per-site_data_2d_array_double.gif']

|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
| --- | --- |
|  | Per-Instrument Data specifies the multisite measurement data from multiple pins connected to multiple instrument sessions. Each row represents measurements from one instrument session, and each column represents each channel on that instrument session. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Per-Site/Pin Data the multisite measurement data from the Data In parameter rearranged by sites and pins. Each row represents measurements for one site, and each column represents a measurement for a pin in the pin query context. Use the Get Site Numbers VI to get the site number for each row. The order of the columns matches the order of the pins parameter in the pin query. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Pass/Fail:2D Array

Transforms measurement data from a 2D array of Boolean measurements that is arranged by instrument sessions and channels into a 2D array that is arranged by the sites and pins in the Semiconductor Module Context.

[IMAGE alt='Per-Instrument To Per-Site Data 2D Array Bool.vi' src='per-instrument_to_per-site_data_2d_array_bool.gif']

|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
| --- | --- |
|  | Per-Instrument Data specifies the multisite measurement data from multiple pins connected to multiple instrument sessions. Each row represents measurements from one instrument session, and each column represents each channel on that instrument session. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Per-Site/Pin Data the multisite measurement data from the Data In parameter rearranged by sites and pins. Each row represents measurements for one site, and each column represents a measurement for a pin in the pin query context. Use the Get Site Numbers VI to get the site number for each row. The order of the columns matches the order of the pins parameter in the pin query. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/perinstrumenttopersitepatternresults.html language=enus -->
## TOPIC 00079: Per-Instrument to Per-Site Pattern Results (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/perinstrumenttopersitepatternresults.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/perinstrumenttopersitepatternresults.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Per-Instrument to Per-Site Pattern Results (TSM)

**Requires:** TSM

Converts pattern results indexed by instrument sessions to pattern results indexed by sites. Pass input pattern results indexed by instrument sessions in the same order that the Pin(s) to NI-Digital Pattern Sessions VI returns. The VI returns pattern results indexed by sites in the same order that the Get Site Numbers VI returns. This VI is available only in 64-bit LabVIEW.

[IMAGE alt='PerInstrumentToPerSitePatternResults.vi' src='perinstrumenttopersitepatternresults.gif']

|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. You must create a pin query context object from a Pin(s) to Sessions VI. |
| --- | --- |
|  | Per-Instrument Pattern Results specifies the pattern results indexed by instrument sessions in the same order as the instrument sessions that the Pin(s) to NI-Digital Pattern Sessions VI returns. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context Out returns the pin query context object unchanged. |
|  | Per-Site Pattern Results returns the pattern results indexed by site in the same order as the sites that the Get Site Numbers VI returns. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/perinstrumenttopersitewaveforms.html language=enus -->
## TOPIC 00080: Per-Instrument to Per-Site Waveforms (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/perinstrumenttopersitewaveforms.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/perinstrumenttopersitewaveforms.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Per-Instrument to Per-Site Waveforms (TSM)

**Requires:** TSM

Converts digital waveforms indexed by instrument sessions in the same order that the Pin(s) to NI-Digital Pattern Sessions VI returns into waveforms indexed by sites in the same order that the Get Site Numbers VI returns. This VI is available only in 64-bit LabVIEW.

[IMAGE alt='PerInstrumentToPerSiteWaveforms.vi' src='perinstrumenttopersitewaveforms.gif']

|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. You must create a pin query context object from a Pin(s) to Sessions VI. |
| --- | --- |
|  | Per-Instrument Waveforms specifies the digital waveforms indexed by instrument sessions in the same order as the instrument sessions that the Pin(s) to NI-Digital Pattern Sessions VI returns. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context Out returns the pin query context object unchanged. |
|  | Per-Site Waveforms returns the digital waveforms indexed by site in the same order as the sites that the Get Site Numbers VI returns. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/persitetoperinstrumentwaveforms.html language=enus -->
## TOPIC 00081: Per-Site to Per-Instrument Waveforms (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/persitetoperinstrumentwaveforms.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/persitetoperinstrumentwaveforms.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Per-Site to Per-Instrument Waveforms (TSM)

**Requires:** TSM

Converts digital waveforms indexed by sites in the same order that the Get Site Numbers VI returns into waveforms indexed by instrument sessions in the same order that the Pin(s) to NI-Digital Pattern Sessions VI returns. This VI is available only in 64-bit LabVIEW.

[IMAGE alt='PerSiteToPerInstrumentWaveforms.vi' src='persitetoperinstrumentwaveforms.gif']

|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. You must create a pin query context object from a Pin(s) to Sessions VI. |
| --- | --- |
|  | Per-Site Waveforms specifies the digital waveforms indexed by site in the same order as the sites that the Get Site Numbers VI returns. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context Out returns the pin query context object unchanged. |
|  | Per-Instrument Waveforms returns the digital waveforms indexed by instrument sessions in the same order as the instrument sessions that the by Pin(s) to NI-Digital Pattern Sessions VI returns. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/pin(s)tonidaqmxtask(s).html language=enus -->
## TOPIC 00082: Pin(s) to NI-DAQmx Task(s) (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/pin(s)tonidaqmxtask(s).html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/pin(s)tonidaqmxtask(s).html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Pin(s) to NI-DAQmx Task(s) (TSM)

**Requires:** TSM

Returns the NI-DAQmx tasks and channel lists required to access one or more pins. You must manually select the polymorphic instance you want to use. Select the single pin or multiple pins polymorphic instance based on the number of pins the test is designed to test. Select the single task or multiple task polymorphic instance based on the number of tasks you expect the pin to be connected to in the pin map. Use the multiple task polymorphic instances to ensure that code modules work with any pin map. Use the single task instance only when you know the code module will never be used with a pin map that has more than one task connected to the specified pins.

#### Multiple Pins - Multiple Tasks

Returns the NI-DAQmx tasks and channel lists required to access the pins or pin groups.

[IMAGE alt='PinsToNIDAQmxTasks.vi' src='pinstonidaqmxtasks.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pins specifies the names of the pins or pin groups to translate to tasks and channel lists. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context is the pin query context object that tracks the task and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | DAQmx Tasks returns the NI-DAQmx tasks connected to the pins for all sites in the Semiconductor Module context. |
|  | Channel Lists returns the comma-separated channel lists required to access the pins for all sites in the Semiconductor Module context. For input tasks, connect this output to the ChannelsToRead property of a DAQmx Read property node to specify which channels to read. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Single Pin - Multiple Tasks

Returns the NI-DAQmx tasks and channel lists required to access the pin or pin group.

[IMAGE alt='PinToNIDAQmxTasks.vi' src='pintonidaqmxtasks.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin specifies the name of the pin or pin group to translate to tasks and channel lists. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context is the pin query context object that tracks the task and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | DAQmx Tasks returns the NI-DAQmx tasks connected to the pin for all sites in the Semiconductor Module context. |
|  | Channel Lists returns the comma-separated channel lists required to access the pins for all sites in the Semiconductor Module context. For input tasks, connect this output to the ChannelsToRead property of a DAQmx Read property node to specify which channels to read. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Multiple Pins - Single Task

Returns the NI-DAQmx task and channel list required to access the pins. If more than one task is required to access the pins, the VI returns an error.

[IMAGE alt='PinsToNIDAQmxTask.vi' src='pinstonidaqmxtask.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pins specifies the names of the pins or pin groups to translate to a task and a channel list. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context is the pin query context object that tracks the task and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | DAQmx Task returns the NI-DAQmx task connected to pins for all sites in the Semiconductor Module context. |
|  | Channel List returns the comma-separated channel list required to access the pins for all sites in the Semiconductor Module context. For an input task, connect this output to the ChannelsToRead property of a DAQmx Read property node to specify which channels to read. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Single Pin - Single Task

Returns the NI-DAQmx task and channel list required to access the pin. If more than one task is required to access the pin, the VI returns an error.

[IMAGE alt='PinToNIDAQmxTask.vi' src='pintonidaqmxtask.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin specifies the name of the pin or pin group to translate to a task and channel list. If multiple tasks are required, the VI returns an error. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context is the pin query context object that tracks the task and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | DAQmx Task returns the NI-DAQmx task connected to the pin for all sites in the Semiconductor Module context. |
|  | Channel List returns the comma-separated channel list required to access the pins for all sites in the Semiconductor Module context. For an input task, connect this output to the ChannelsToRead property of a DAQmx Read property node to specify which channels to read. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/pin(s)tonidcpowersession(s).html language=enus -->
## TOPIC 00083: Pin(s) to NI-DCPower Session(s) (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/pin(s)tonidcpowersession(s).html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/pin(s)tonidcpowersession(s).html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Pin(s) to NI-DCPower Session(s) (TSM)

**Requires:** TSM

Returns the NI-DCPower instrument sessions and channel strings required to access one or more pins. You must manually select the polymorphic instance you want to use. Select the single pin or multiple pins polymorphic instance based on the number of pins the test is designed to test. Select the single instrument or multiple instrument polymorphic instance based on the number of instruments you expect the pin to be connected to in the pin map. Use the multiple instrument polymorphic instances to ensure that code modules work with any pin map. Use the single instrument instance only when you know the code module will never be used with a pin map that has more than one instrument connected to the specified pins.

#### Multiple Pins - Multiple Sessions

Returns the NI-DCPower sessions and channel strings required to access the pins.

[IMAGE alt='PinsToNIDCPowerSessions.vi' src='pinstonidcpowersessions.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pins specifies the names of the pins or pin groups to translate to Instrument Sessions and Channel Strings. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Channel Strings returns the channel string for each instrument session required to access the Pins for all sites in the Semiconductor Module Context. Each channel string is a comma-separated list of channels, where each channel is defined as <instrument>/<channel>. |
|  | Instrument Sessions returns the NI-DCPower sessions for the instruments and channels connected to Pins for all sites in the Semiconductor Module Context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Single Pin - Multiple Sessions

Returns the NI-DCPower sessions and channel strings required to access the pin.

[IMAGE alt='PinToNIDCPowerSessions.vi' src='pintonidcpowersessions.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin specifies the name of the pin or pin group to translate to Instrument Sessions and Channel Strings. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Channel Strings returns the channel string for the NI-DCPower session required to access the Pin for all sites in the Semiconductor Module context. Each channel string is a comma-separated list of channels, where each channel is defined as <instrument>/<channel>. |
|  | Instrument Sessions returns the NI-DCPower sessions for the instruments and channels connected to the Pin for all sites in the Semiconductor Module Context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Single Pin - Single Session

Returns the NI-DCPower session and channel string required to access the pin. If more than one session is required to access the pin, the VI returns an error.

[IMAGE alt='PinToNIDCPowerSession.vi' src='pintonidcpowersession.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin specifies the name of the pin to translate to an Instrument Session and Channel String. If multiple sessions are required, the VI returns an error. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Channel String returns the channel string for the instrument Session required to access the Pin for all sites in the Semiconductor Module Context. The channel string is a comma-separated list of channels, where each channel is defined as <instrument>/<channel>. |
|  | Instrument Session returns the NI-DCPower instrument session for the instrument and channel connected to Pin. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Multiple Pins - Single Session

Returns the NI-DCPower session and channel string required to access the pins. If multiple sessions are required, the VI returns an error.

[IMAGE alt='PinsToNIDCPowerSession.vi' src='pinstonidcpowersession.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pins specifies the names of the pins or pin groups to translate to an instrument session and channel resource name list. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Channel String returns the channel string for the NI-DCPower instrument session required to access the pins for all sites in the Semiconductor Module Context. The channel string is a comma-separated list of resources, where each resource is defined as <instrument>/<channel>. |
|  | Instrument Session returns the NI-DCPower instrument session for the instruments and channels connected to Pins for all sites in the Semiconductor Module Context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/pin(s)tonidigitalpatternsessions.html language=enus -->
## TOPIC 00084: Pin(s) to NI-Digital Pattern Session(s) (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/pin(s)tonidigitalpatternsessions.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/pin(s)tonidigitalpatternsessions.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Pin(s) to NI-Digital Pattern Session(s) (TSM)

**Requires:** TSM

Returns the NI-Digital Pattern sessions, channel lists, and site lists required to access one or more pins. You must manually select the polymorphic instance you want to use. Select the single pin or multiple pins polymorphic instance based on the number of pins the test is designed to test. Select the single instrument or multiple instrument polymorphic instance based on the number of instruments you expect the pins to be connected to in the pin map. Use the multiple instrument polymorphic instances to ensure that code modules work with any pin map. Use the single instrument instance only when you know the code module will never be used with a pin map that has more than one instrument connected to the specified pins, or when the NI-Digital Pattern instruments are grouped together in the same group in the pin map. This VI is available only in 64-bit LabVIEW.

#### Multiple Pins - Single Instrument

Returns the NI-Digital Pattern instrument session, channel list, and site list required to access the pins. If more than one instrument session is required to access the pin, the VI returns an error. Each group of NI-Digital Pattern instruments in the pin map creates a single instrument session.

[IMAGE alt='PinsToNIDigitalPatternSession.vi' src='pinstonidigitalpatternsession.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pins specifies the names of the pins or pin groups to translate to an instrument session, channel list, and site list. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context is the pin query context object that tracks the session and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
|  | Site List returns the site list associated with the instrument session to access the pins for all sites in the Semiconductor Module context. The site list is a comma-separated list of sites. If you use a digital pattern instrument connected to multiple sites, you must connect this output to the site list input of the NI-Digital Pattern Driver VIs, such as the niDigital Apply Levels and Timing VI, the niDigital Burst Pattern VI, the niDigital Configure Pattern Burst Sites VI, the niDigital Fetch Capture Waveform (U32) VI, the niDigital Get Site Pass Fail VI, and the niDigital Write Source Waveform (Site Unique U32) instance of the niDigital Write Source Waveform VI. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Session returns the NI-Digital Pattern instrument session for the instruments connected to pins for all sites in the Semiconductor Module context. |
|  | Channel List returns the comma-separated channel list required to access the pins for all sites in the Semiconductor Module context. Each channel is specified by site and pin, e.g. "site0/A" as expected by the NI-Digital Pattern driver. If any of the pins are connected to the same instrument channel for multiple sites, the channel appears only once in the string and is identified by one of the site/pin combinations to which it is connected. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Single Pin - Single Instrument

Returns the NI-Digital Pattern instrument session, channel list, and site list required to access the pin. If more than one instrument session is required to access the pin, the VI returns an error. Each group of NI-Digital Pattern instruments in the pin map creates a single instrument session.

[IMAGE alt='PinToNIDigitalPatternSession.vi' src='pintonidigitalpatternsession.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin specifies the name of the pin or pin group to translate to an instrument session, channel list, and site list. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context |
|  | Site List returns the site list associated with the instrument session to access the pin for all sites in the Semiconductor Module context. The site list is a comma-separated list of sites. If you use a digital pattern instrument connected to multiple sites, you must connect this output to the site list input of the NI-Digital Pattern Driver VIs, such as the niDigital Apply Levels and Timing VI, the niDigital Burst Pattern VI, the niDigital Configure Pattern Burst Sites VI, the niDigital Fetch Capture Waveform (U32) VI, the niDigital Get Site Pass Fail VI, and the niDigital Write Source Waveform (Site Unique U32) instance of the niDigital Write Source Waveform VI. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Session returns the NI-Digital Pattern instrument session for the instruments connected to the pin for all sites in the Semiconductor Module context. |
|  | Channel List returns the comma-separated channel list required to access the pin for all sites in the Semiconductor Module context. Each channel is specified by site and pin, e.g. "site0/A" as expected by the NI-Digital Pattern driver. If the pin is connected to the same instrument channel for multiple sites, the channel appears only once in the string and is identified by one of the site/pin combinations to which it is connected. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Multiple Pins - Multiple Instruments

Returns the NI-Digital Pattern instrument sessions, channel lists, and site lists required to access the pins.

[IMAGE alt='PinsToNIDigitalPatternSessions.vi' src='pinstonidigitalpatternsessions.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pins specifies the names of the pins or pin groups to translate to instrument sessions, channel lists, and site lists. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
|  | Site Lists returns the site lists associated with the instrument sessions to access pins for all sites in the Semiconductor Module context. Each site list is a comma-separated list of sites. If you use a digital pattern instrument connected to multiple sites, you must connect this output to the site list input of the NI-Digital Pattern Driver VIs, such as the niDigital Apply Levels and Timing VI, the niDigital Burst Pattern VI, the niDigital Configure Pattern Burst Sites VI, the niDigital Fetch Capture Waveform (U32) VI, the niDigital Get Site Pass Fail VI, and the niDigital Write Source Waveform (Site Unique U32) instance of the niDigital Write Source Waveform VI. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Sessions returns the NI-Digital Pattern instrument sessions for the instruments connected to pins for all sites in the Semiconductor Module context. |
|  | Channel Lists returns the comma-separated channel lists required to access the pins for all sites in the Semiconductor Module context. Each channel is specified by site and pin, e.g. "site0/A" as expected by the NI-Digital Pattern driver. If any of the pins are connected to the same instrument channel for multiple sites, the channel appears only once in the string and is identified by one of the site/pin combinations to which it is connected. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Single Pin - Multiple Instruments

Returns the NI-Digital Pattern instrument sessions, channel lists, and site lists required to access the pin.

[IMAGE alt='PinToNIDigitalPatternSessions.vi' src='pintonidigitalpatternsessions.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin specifies the name of the pin or pin group to translate to instrument sessions, channel lists, and site lists. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context Out is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
|  | Site Lists returns the site lists associated with the instrument sessions to access the pin for all sites in the Semiconductor Module context. Each site list is a comma-separated list of sites. If you use a digital pattern instrument connected to multiple sites, you must connect this output to the site list input of the NI-Digital Pattern Driver VIs, such as the niDigital Apply Levels and Timing VI, the niDigital Burst Pattern VI, the niDigital Configure Pattern Burst Sites VI, the niDigital Fetch Capture Waveform (U32) VI, the niDigital Get Site Pass Fail VI, and the niDigital Write Source Waveform (Site Unique U32) instance of the niDigital Write Source Waveform VI. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Sessions returns the NI-Digital Pattern instrument sessions for the instruments connected to the pin for all sites in the Semiconductor Module context. |
|  | Channel Lists returns the comma-separated channel lists required to access the pin for all sites in the Semiconductor Module context. Each channel is specified by site and pin, e.g. "site0/A" as expected by the NI-Digital Pattern driver. If the pin is connected to the same instrument channel for multiple sites, the channel appears only once in the string and is identified by one of the site/pin combinations to which it is connected. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/pin(s)tonidmmsession(s).html language=enus -->
## TOPIC 00085: Pin(s) to NI-DMM Session(s) (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/pin(s)tonidmmsession(s).html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/pin(s)tonidmmsession(s).html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Pin(s) to NI-DMM Session(s) (TSM)

**Requires:** TSM

Returns the NI-DMM instrument sessions required to access one or more pins. You must manually select the polymorphic instance you want to use. Select the single pin or multiple pins polymorphic instance based on the number of pins the test is designed to test. Select the single instrument or multiple instrument polymorphic instance based on the number of instruments you expect the pin to be connected to in the pin map. Use the multiple instrument polymorphic instances to ensure that code modules work with any pin map. Use the single instrument instance when the **Semiconductor Module Context** contains only a single site.

#### Multiple Pins - Multiple Instruments

Returns the NI-DMM instrument sessions required to access the pins.

[IMAGE alt='PinsToNIDMMSessions.vi' src='pinstonidmmsessions.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pins specifies the names of the pins or pin groups to translate to instrument sessions. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Sessions returns the NI-DMM instrument sessions for the instruments connected to pins for all sites in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Single Pin - Multiple Instruments

Returns the NI-DMM instrument sessions required to access the pin.

[IMAGE alt='PinToNIDMMSessions.vi' src='pintonidmmsessions.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin specifies the name of the pin or pin group to translate to instrument sessions. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Sessions returns the NI-DMM instrument sessions for the instruments connected to the pin for all sites in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Single Pin - Single Instrument

Returns the NI-DMM instrument session required to access the pin. If the Semiconductor Module context has more than one site, the VI returns an error.

[IMAGE alt='PinToNIDMMSession.vi' src='pintonidmmsession.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin specifies the name of the pin to translate to an instrument session. If multiple sessions are required, the VI returns an error. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Session returns the NI-DMM instrument session for the instrument connected to the pin on the site in the Semiconductor Module Context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/pin(s)tonifgensession(s).html language=enus -->
## TOPIC 00086: Pin(s) To NI-FGEN Session(s) (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/pin(s)tonifgensession(s).html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/pin(s)tonifgensession(s).html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Pin(s) To NI-FGEN Session(s) (TSM)

**Requires:** TSM

Returns the NI-FGEN instrument sessions and channel lists required to access one or more pins. You must manually select the polymorphic instance you want to use. Select the single pin or multiple pins polymorphic instance based on the number of pins the test is designed to test. Select the single instrument or multiple instrument polymorphic instance based on the number of instruments you expect the pin to be connected to in the pin map. Use the multiple instrument polymorphic instances to ensure that code modules work with any pin map. Use the single instrument instance only when you know the code module will never be used with a pin map that has more than one instrument connected to the specified pins.

#### Multiple Pins - Multiple Instruments

Returns the NI-FGEN instrument sessions and channel lists required to access the pins.

[IMAGE alt='PinsToNIFGenSessions.vi' src='pinstonifgensessions.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pins specifies the names of the pins or pin groups to translate to instrument sessions and channel lists. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Sessions returns the NI-FGEN instrument sessions for the instruments connected to pins for all sites in the Semiconductor Module context. |
|  | Channel Lists returns the channel lists required to access pins for all sites in the Semiconductor Module context. Each channel list is a comma-separated list of channels. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Single Pin - Multiple Instruments

Returns the NI-FGEN instrument sessions and channel lists required to access the pin.

[IMAGE alt='PinToNIFGenSessions.vi' src='pintonifgensessions.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin is the name of the pin or pin group to translate to instrument sessions and channel lists. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Sessions returns the NI-FGEN instrument sessions for the instruments connected to the pin for all sites in the Semiconductor Module context. |
|  | Channel Lists returns the channel lists required to access the pin for all sites in the Semiconductor Module context. Each channel list is a comma-separated list of channels. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Multiple Pins - Single Instrument

Returns the NI-FGEN instrument session and channel list required to access the pins. If more than one instrument is required to access the pins, the VI returns an error.

[IMAGE alt='PinsToNIFGenSession.vi' src='pinstonifgensession.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pins specifies the names of the pins or pin groups to translate to an instrument session and a channel list. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context is the pin query context object that tracks the session and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Session returns the NI-FGEN instrument session for the instrument connected to pins for all sites in the Semiconductor Module context. |
|  | Channel List returns the comma-separated list of channels required to access pins for all sites in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Single Pin - Single Instrument

Returns the NI-FGEN instrument session and channel list required to access the pin. If more than one instrument is required to access the pin, the VI returns an error.

[IMAGE alt='PinToNIFGenSession.vi' src='pintonifgensession.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin is the name of the pin or pin group to translate to an instrument session and a channel list. If more than one session is required, the VI returns an error. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Session returns the NI-FGEN instrument session for the instrument connected to the pin in the Semiconductor Module context. |
|  | Channel List returns the comma-separated list of channels required to access the pin for all sites in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/pin(s)tonihsdiosession(s).html language=enus -->
## TOPIC 00087: Pin(s) to NI-HSDIO Session(s) (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/pin(s)tonihsdiosession(s).html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/pin(s)tonihsdiosession(s).html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Pin(s) to NI-HSDIO Session(s) (TSM)

**Requires:** TSM

Returns the NI-HSDIO acquisition sessions, generation sessions, and channel lists required to access one or more pins. You must manually select the polymorphic instance you want to use. Select the single pin or multiple pins polymorphic instance based on the number of pins the test is designed to test. Select the single instrument or multiple instrument polymorphic instance based on the number of instruments you expect the pin to be connected to in the pin map. Use the multiple instrument polymorphic instances to ensure that code modules work with any pin map. Use the single instrument instance only when you know the code module will never be used with a pin map that has more than one instrument connected to the specified pins.

#### Multiple Pins - Multiple Instruments

Returns the NI-HSDIO acquisition sessions, generation sessions, and channel lists required to access the pins.

[IMAGE alt='PinsToNIHSDIOSessions.vi' src='pinstonihsdiosessions.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pins specifies the names of the pins or pin groups to translate to generation sessions, acquisition sessions, and channel lists. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, extract data from a set of measurements, and create or rearrange waveforms. |
|  | Channel Lists returns the channel lists required to access pins for all sites in the Semiconductor Module context. Each channel list is a comma-separated list of channels. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Acquisition Sessions returns the NI-HSDIO acquisition sessions for the instruments connected to pins for all sites in the Semiconductor Module context. |
|  | Generation Sessions returns the NI-HSDIO generation sessions for the instruments connected to pins for all sites in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Single Pin - Multiple Instruments

Returns the NI-HSDIO acquisition sessions, generation sessions, and channel lists required to access the pin.

[IMAGE alt='PinToNIHSDIOSessions.vi' src='pintonihsdiosessions.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin specifies the name of the pin or pin group to translate to generation sessions, acquisition sessions, and channel lists. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, extract data from a set of measurements, or rearrange waveforms. |
|  | Channel Lists returns the comma-separated list of channels required to access the pin for all sites in the Semiconductor Module context. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Acquisition Sessions returns the NI-HSDIO acquisition sessions for the instruments connected to the pin for all sites in the Semiconductor Module context. |
|  | Generation Sessions returns the NI-HSDIO generation sessions for the instruments connected to the pin for all sites in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Multiple Pins - Single Instrument

Returns the NI-HSDIO acquisition session, generation session, and channel list required to access the pins. If more than one instrument is required to access the pins, the VI returns an error.

[IMAGE alt='PinsToNIHSDIOSession.vi' src='pinstonihsdiosession.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pins specifies the names of the pins or pin groups to translate to a generation session, an acquisition session, and a channel list. If more than one instrument is required to access the pins, the VI returns an error. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, extract data from a set of measurements, and create or rearrange waveforms. |
|  | Channel List returns the comma-separated list of channels required to access pins for all sites in the Semiconductor Module context. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Acquisition Session returns the NI-HSDIO acquisition session for the instrument connected to pins for all sites in the Semiconductor Module context. |
|  | Generation Session returns the NI-HSDIO generation session for the instrument connected to pins for all sites in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Single Pin - Single Instrument

Returns the NI-HSDIO acquisition session, generation session, and channel list required to access the pin. If more than one instrument is required to access the pin, the VI returns an error.

[IMAGE alt='PinToNIHSDIOSession.vi' src='pintonihsdiosession.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin specifies the name of the pin or pin group to translate to a generation session, an acquisition session, and a channel list. If more than one instrument is required to access the pin, the VI returns an error. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, extract data from a set of measurements, and create or rearrange waveforms. |
|  | Channel List returns the comma-separated list of channels required to access the pin for all sites in the Semiconductor Module context. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Acquisition Session returns the NI-HSDIO acquisition session for the instrument connected to the pin for all sites in the Semiconductor Module context. |
|  | Generation Session returns the NI-HSDIO generation session for the instrument connected to the pin for all sites in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/pin(s)tonirfpmsessionswithpaths.html language=enus -->
## TOPIC 00088: Pin(s) To NI-RFPM Sessions (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/pin(s)tonirfpmsessionswithpaths.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/pin(s)tonirfpmsessionswithpaths.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Pin(s) To NI-RFPM Sessions (TSM)

**Requires:** TSM

Returns the NI-RFPM sessions and ports required to access one or more pins, as well as paths and orientations of the S2P files that characterize the de-embedding network for each port. You must always close references to the Semiconductor Module contexts, even if you do not use them in your code module. You must manually select the polymorphic instance you want to use. Select the single pin, two pins, or multiple pins polymorphic instance based on the number of pins the test is designed to test. The two pins polymorphic instance is a convenient option for tests that involve a stimulus and response pin.

#### Single Pin - Multiple Instruments

Returns the NI-RFPM sessions and ports required to access the pin, as well as paths and orientations of the S2P files that characterize the de-embedding network for each port.

[IMAGE alt='PinToNIRFPMSessionsWithPaths.vi' src='pintonirfpmsessionswithpaths.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin specifies the name of the pin to translate to instrument sessions and include in the Ports List parameter. The pin must be a DUT pin. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Ports List returns an array of ports, where each element is the port for the instrument session required to access the pin on the corresponding site. |
|  | De-embedding Files returns the paths and orientations of the S2P files that characterize the de-embedding network for each port in the Ports List parameter. If the path is an absolute path, the VI returns the absolute path whether the file exists or not. If the path is a relative path and the file exists relative to the path of the pin map file, the VI returns the absolute path of the existing file. Otherwise, the VI returns a string without error. |
|  | Semiconductor Module Context out returns the Semiconductor Module Context parameter unchanged. |
|  | Semiconductor Module Contexts returns an array of Semiconductor Module context objects. Each element in the array represents a site that must be executed serially. Use each Semiconductor Module context object to query the pin map and publish data. You must always close references to the Semiconductor Module contexts, even if you do not use them in your code module. |
|  | Instrument Sessions returns the NI-RFPM subsystem sessions of the instruments for each site in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Two Pins - Multiple Instruments

Returns the NI-RFPM sessions and ports required to access Pin 1 and Pin 2 and the paths and orientations to S2P files that characterize the de-embedding network for each port. This polymorphic instance is a convenient option for tests that involve a stimulus and response pin.

[IMAGE alt='2PinsToNIRFPMSessionsWithPaths.vi' src='2pinstonirfpmsessionswithpaths.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin 1 specifies the name of the first pin to translate to instrument sessions and include in the Ports List 1 parameter. The pin must be a DUT pin. |
|  | Pin 2 specifies the name of the second pin to translate to instrument sessions and include in the Ports List 2 parameter. The pin must be a DUT pin. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Ports List 1 returns an array of ports where each element is the port for the instrument session required to access Pin 1 on the corresponding site. |
|  | De-embedding Files 1 returns the paths and orientations of the S2P files that characterize the de-embedding network for each port in the Ports List 1 parameter. If the path is an absolute path, the VI returns the absolute path whether the file exists or not. If the path is a relative path and the file exists relative to the path of the pin map file, the VI returns the absolute path of the existing file. Otherwise, the VI returns a string without error. |
|  | Ports List 2 returns an array of ports where each element is the port for the instrument session required to access Pin 2 on the corresponding site. |
|  | De-embedding Files 2 returns the paths and orientations of the S2P files that characterize the de-embedding network for each port in the Ports List 2 parameter. If the path is an absolute path, the VI returns the absolute path whether the file exists or not. If the path is a relative path and the file exists relative to the path of the pin map file, the VI returns the absolute path of the existing file. Otherwise, the VI returns a string without error. |
|  | Semiconductor Module Context out returns the Semiconductor Module Context parameter unchanged. |
|  | Semiconductor Module Contexts returns an array of Semiconductor Module context objects. Each element in the array represents a site that must be executed serially. Use each Semiconductor Module context object to query the pin map and publish data. You must always close references to the Semiconductor Module contexts, even if you do not use them in your code module. |
|  | Instrument Sessions returns the NI-RFPM subsystem sessions of the instruments for each site in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Multiple Pins - Multiple Instruments

Returns the NI-RFPM sessions and ports required to access the pins, as well as paths and orientations of the S2P files that characterize the de-embedding network for each port.

[IMAGE alt='PinsToNIRFPMSessionsWithPaths.vi' src='pinstonirfpmsessionswithpaths.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pins specifies the names of the pins or pin groups to translate to instrument sessions and include in the Ports Lists parameter. The pins must be DUT pins. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Ports List returns a 2D array of ports. Each row represents ports from a site, and each column represents the ports for the instrument session required to access the pins on the corresponding site. |
|  | De-embedding Files returns the paths and orientations of the S2P files that characterize the de-embedding network for each port in the Ports List parameter. If the path is an absolute path, the VI returns the absolute path whether the file exists or not. If the path is a relative path and the file exists relative to the path of the pin map file, the VI returns the absolute path of the existing file. Otherwise, the VI returns a string without error. |
|  | Semiconductor Module Context out returns the Semiconductor Module Context parameter unchanged. |
|  | Semiconductor Module Contexts returns an array of Semiconductor Module context objects. Each element in the array represents a site that must be executed serially. Use each Semiconductor Module context object to query the pin map and publish data. You must always close references to the Semiconductor Module contexts, even if you do not use them in your code module. |
|  | Instrument Sessions returns the NI-RFPM subsystem sessions of the instruments for each site in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/pin(s)toniscopesession(s).html language=enus -->
## TOPIC 00089: Pin(s) To NI-SCOPE Session(s) (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/pin(s)toniscopesession(s).html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/pin(s)toniscopesession(s).html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Pin(s) To NI-SCOPE Session(s) (TSM)

**Requires:** TSM

Returns the NI-SCOPE instrument sessions and channel lists required to access one or more pins. You must manually select the polymorphic instance you want to use. Select the single pin or multiple pins polymorphic instance based on the number of pins the test is designed to test. Select the single instrument or multiple instrument polymorphic instance based on the number of instruments you expect the pin to be connected to in the pin map. Use the multiple instrument polymorphic instances to ensure that code modules work with any pin map. Use the single instrument instance only when you know the code module will never be used with a pin map that has more than one instrument connected to the specified pins.

#### Multiple Pins - Single Instrument

Returns the NI-SCOPE instrument session and channel list required to access the pins. If more than one instrument session is required to access the pins, the VI returns an error. Each group of NI-SCOPE instruments in the pin map creates a single instrument session.

[IMAGE alt='PinsToNISCOPESession.vi' src='pinstoniscopesession.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pins specifies the names of the pins or pin groups to translate to an instrument session and a channel list. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context is the pin query context object that tracks the session and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Session returns the NI-SCOPE instrument session for the instrument connected to pins for all sites in the Semiconductor Module context. |
|  | Channel List returns the comma-separated channel lists required to access pins for all sites in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Multiple Pins - Multiple Instruments

Returns the NI-SCOPE instrument sessions and channel lists required to access the pins.

[IMAGE alt='PinsToNISCOPESessions.vi' src='pinstoniscopesessions.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pins specifies the names of the pins or pin groups to translate to instrument sessions and channel lists. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Sessions returns the NI-SCOPE instrument sessions for the instruments connected to pins for all sites in the Semiconductor Module context. |
|  | Channel Lists returns the comma-separated channel lists required to access the pins for all sites in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Single Pin - Single Instrument

Returns the NI-SCOPE instrument session and channel list required to access the pin. If more than one instrument session is required to access the pin, the VI returns an error. Each group of NI-SCOPE instruments in the pin map creates a single instrument session.

[IMAGE alt='PinToNISCOPESession.vi' src='pintoniscopesession.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin is the name of the pin or pin group to translate to an instrument session and a channel list. If multiple sessions are required, the VI returns an error. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Session returns the NI-SCOPE instrument session for the instrument connected to the pin in the Semiconductor Module context. |
|  | Channel List returns the comma-separated channel lists required to access the pin for all sites in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Single Pin - Multiple Instruments

Returns the NI-SCOPE instrument sessions and channel lists required to access the pin.

[IMAGE alt='PinToNISCOPESessions.vi' src='pintoniscopesessions.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin is the name of the pin or pin group to translate to instrument sessions and channel lists. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Sessions returns the NI-SCOPE instrument sessions for the instruments connected to the pin for all sites in the Semiconductor Module context. |
|  | Channel Lists returns the comma-separated channel lists required to access the pin for all sites in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/pincontrol.html language=enus -->
## TOPIC 00090: Pin Control (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/pincontrol.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/pincontrol.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Pin Control (TSM)

Use the pin control to create a control populated with the pins from a [linked sequence file](linkingtsmfiletolabviewproject.html). This allows you to select a value from the control's populated list rather than entering the value as a string. If there is no sequence file linked to the LabVIEW project, or if you are editing the LabVIEW project on a system that cannot access the sequence file, the control acts a string.

|  | Note To create a control, place it on the front panel. Placing a control on the block diagram creates a constant. |
| --- | --- |

| Palette Object | Description |
| --- | --- |
| Pin | Contains a list of pins for the linked sequence file(s). |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/pinstonihsdiochannelmaskswithcontext.html language=enus -->
## TOPIC 00091: Get NI-HSDIO Masks (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/pinstonihsdiochannelmaskswithcontext.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/pinstonihsdiochannelmaskswithcontext.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Get NI-HSDIO Masks (TSM)

**Requires:** TSM

Returns an array of channel masks in which each element corresponds to a site in the Semiconductor Module context. Each element in the array is an unsigned number in which a bit is asserted if a pin is connected to that channel. You can use the masks to identify which site failed in a functional test.

#### Channel Masks - Multiple Instruments

Returns a two-dimensional array of channel masks with one array for each instrument and one element for each site stored in the Semiconductor Module context. Each element in the array is an unsigned number in which a bit is asserted if a pin or pin group is connected to that channel. You can use the masks to identify which site failed in a functional test in which a single instrument services multiple sites. The first dimension of the array corresponds to an instrument, and the second dimension corresponds to a site. Use this VI when you write code modules that service multiple NI-HSDIO instruments.

[IMAGE alt='PinsToNIHSDIOChannelMasksMultipleInstrumentsWithContext.vi' src='pinstonihsdiochannelmasksmultipleinstrumentswithcontext.gif']

|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, extract data from a set of measurements, and create or rearrange waveforms. You must create a pin query context object from a Pin(s) to NI-HSDIO Sessions VI. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Channel Masks returns the two-dimensional array of channel masks with a row for each instrument and a column for each site in the Semiconductor Module context. Each element in the array is an unsigned number in which a bit is asserted if a pin is connected to that channel. You can use the masks to identify which site failed in a functional test in which a single instrument services multiple sites. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Channel Masks - Single Instrument

Returns a one-dimensional array of channel masks with one element for each site in the Semiconductor Module context. Each element in the array is an unsigned number in which a bit is asserted if a pin or pin group is connected to that channel. You can use the masks to identify which site failed in a functional test.

[IMAGE alt='PinsToNIHSDIOChannelMasksSingleInstrumentWithContext.vi' src='pinstonihsdiochannelmaskssingleinstrumentwithcontext.gif']

|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, extract data from a set of measurements, and create or rearrange waveforms. You must create a pin query context object from a Pin(s) to NI-HSDIO Sessions VI. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Channel Masks returns the one-dimensional array of channel masks with one element for each site in the Semiconductor Module context. Each element in the array is an unsigned number in which a bit is asserted if a pin is connected to that channel. You can use the masks to identify which site failed in a functional test. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/pintofpgavireference(s).html language=enus -->
## TOPIC 00092: Pin to FPGA VI Reference(s) (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/pintofpgavireference(s).html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/pintofpgavireference(s).html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Pin to FPGA VI Reference(s) (TSM)

**Requires:** TSM

Returns the FPGA VI references of the instruments connected to the pin. You must manually select the polymorphic instance you want to use. Select the single instrument or multiple instrument polymorphic instance based on the number of instruments you expect the pin to be connected to in the pin map. The multiple instrument polymorphic instances are recommended to ensure that your code module will work with any pin map, but you can use the single instrument instance if you know that the code module will never be used with a pin map that has more than one instrument connected to the specified pins.

#### Single Pin - Multiple Instruments

Returns the FPGA VI References on instruments connected to the pin.

[IMAGE alt='PinToFPGAVIReferences.vi' src='pintofpgavireferences.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin specifies the name of the pin or pin group to translate to FPGA VI references. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | FPGA VI References returns the FPGA VI references of the instruments connected to the pin for all sites in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Single Pin - Single Instrument

Returns the FPGA VI References on instruments connected to the pin. If more than one instrument is connected to the pin, the VI returns an error.

[IMAGE alt='PinToFPGAVIReference.vi' src='pintofpgavireference.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin specifies the name of the pin to translate to an FPGA VI reference. If multiple FPGA VI references are required, the VI returns an error. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | FPGA VI Reference returns the FPGA VI reference of the instrument connected to the pin for all sites in the Semiconductor Module Context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/pintonirfmxdeembeddingdata.html language=enus -->
## TOPIC 00093: Pin to NI-RFmx De-Embedding Data (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/pintonirfmxdeembeddingdata.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/pintonirfmxdeembeddingdata.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Pin to NI-RFmx De-Embedding Data (TSM)

**Requires:** TSM

Returns the NI-RFmx de-embedding data associated with the connection(s) to a single pin. You must manually select the polymorphic instance you want to use. Select the single file or multiple files polymorphic instance based on the number of connections you expect the pin to be connected to in the pin map. The multiple file polymorphic instances are recommended to ensure that your code module will work with any pin map, but you can use the single file instance if you know that the code module will never be used with a pin map that has more than one connection to the specified pin.

#### Single Pin - Single Port

Returns the NI-RFmx de-embedding path and orientation associated with the instrument connection to the pin. If more than one pin connection is found, the VI returns an error.

[IMAGE alt='PinToNIRFmxSingleDeembeddingData.vi' src='pintonirfmxsingledeembeddingdata.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin specifies the name of the pin associated with the instrument. If more than one pin connection is found, the VI returns an error. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | De-Embedding File returns the paths and RFmx orientation of the S2P file that characterizes the de-embedding network. If the path is an absolute path, the VI returns the absolute path whether the file exists or not. If the path is a relative path and the file exists relative to the path of the pin map file, the VI returns the absolute path of the existing file. Otherwise, the VI returns a string without error. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Single Pin- Multiple Ports

Returns the NI-RFmx de-embedding data associated with the connections to the pin. If any instrument in the Semiconductor Module context contains more than a single connection to the pin, the VI returns an error.

[IMAGE alt='PinToNIRFmxMultipleDeembeddingData.vi' src='pintonirfmxmultipledeembeddingdata.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin specifies the name of the pin or pin group to translate to de-embedding data on the connection. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | De-Embedding Files returns the paths and RFmx orientations of the S2P files that characterize the de-embedding network. If the path is an absolute path, the VI returns the absolute path whether the file exists or not. If the path is a relative path and the file exists relative to the path of the pin map file, the VI returns the absolute path of the existing file. Otherwise, the VI returns a string without error. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/pintonirfmxsession(s).html language=enus -->
## TOPIC 00094: Pin to NI-RFmx Session(s) (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/pintonirfmxsession(s).html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/pintonirfmxsession(s).html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Pin to NI-RFmx Session(s) (TSM)

**Requires:** TSM

Returns the NI-RFmx session required to access one pin. You must manually select the polymorphic instance you want to use. Select the single instrument or multiple instrument polymorphic instance based on the number of instruments you expect the pin to be connected to in the pin map. The multiple instrument polymorphic instances are recommended to ensure that your code module will work with any pin map, but you can use the single instrument instance if you know that the code module will never be used with a pin map that has more than one instrument connected to the specified pins.

#### Single Pin - Single Port

Returns the NI-RFmx instrument session required to access the pin. If more than one instrument is required to access the pin, or if the instrument has more than one port connected to that pin in other sites within the given context, the VI returns an error.

[IMAGE alt='PinToNIRFmxSession.vi' src='pintonirfmxsession.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin specifies the name of the pin to translate to an instrument session. If multiple sessions are required, the VI returns an error. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Session returns the NI-RFmx instrument session for the instrument connected to the pin. |
|  | Port returns the instrument port connected to the pin. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Single Pin - Multiple Ports

Returns the NI-RFmx instrument sessions required to access the pin. If any instrument has more than one port connected to that pin in other sites within the given context, the VI returns an error.

[IMAGE alt='PinToNIRFmxSessions.vi' src='pintonirfmxsessions.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin specifies the name of the pin or pin group to translate to instrument sessions. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Sessions returns the NI-RFmx instrument sessions for the instruments connected to the pin for all sites in the Semiconductor Module context. |
|  | Ports returns the port information for the associated instrument sessions connections to the pin. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/pintonirfsadeembeddingdata.html language=enus -->
## TOPIC 00095: Pin to NI-RFSA De-Embedding Data (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/pintonirfsadeembeddingdata.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/pintonirfsadeembeddingdata.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Pin to NI-RFSA De-Embedding Data (TSM)

**Requires:** TSM

Returns the NI-RFSA de-embedding data associated with the connection(s) to a single pin. You must manually select the polymorphic instance you want to use. Select the single file or multiple files polymorphic instance based on the number of connections you expect the pin to be connected to in the pin map. The multiple file polymorphic instances are recommended to ensure that your code module will work with any pin map, but you can use the single file instance if you know that the code module will never be used with a pin map that has more than one connection to the specified pin.

#### Single Pin- Multiple Ports

Returns the NI-RFSA de-embedding data associated with the connections to the pin. If any instrument in the Semiconductor Module context contains more than a single connection to the pin, the VI returns an error.

[IMAGE alt='PinToNIRFSAMultipleDeembeddingData.vi' src='pintonirfsamultipledeembeddingdata.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin specifies the name of the pin or pin group to translate de-embedding data on the connection. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | De-Embedding Files returns the paths and RFSA orientations of the S2P files that characterize the de-embedding network. If the path is an absolute path, the VI returns the absolute path whether the file exists or not. If the path is a relative path and the file exists relative to the path of the pin map file, the VI returns the absolute path of the existing file. Otherwise, the VI returns a string without error. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Single Pin - Single Port

Returns the NI-RFSA de-embedding path and orientation associated with the instrument connection to the pin. If more than one pin connection is found, the VI returns an error.

[IMAGE alt='PinToNIRFSASingleDeembeddingData.vi' src='pintonirfsasingledeembeddingdata.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin specifies the name of the pin associated with the instrument. If more than one pin connection is found, the VI returns an error. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out |
|  | De-Embedding File returns the paths and RFSA orientation of the S2P file that characterizes the de-embedding network. If the path is an absolute path, the VI returns the absolute path whether the file exists or not. If the path is a relative path and the file exists relative to the path of the pin map file, the VI returns the absolute path of the existing file. Otherwise, the VI returns a string without error. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/pintonirfsasession(s).html language=enus -->
## TOPIC 00096: Pin to NI-RFSA Session(s) (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/pintonirfsasession(s).html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/pintonirfsasession(s).html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Pin to NI-RFSA Session(s) (TSM)

**Requires:** TSM

Returns the NI-RFSA session required to access one pin. You must manually select the polymorphic instance you want to use. Select the single instrument or multiple instrument polymorphic instance based on the number of instruments you expect the pin to be connected to in the pin map. Use the multiple instrument polymorphic instances to ensure that code modules work with any pin map. Use the single instrument instance only when you know the code module will never be used with a pin map that has more than one instrument connected to the specified pins.

#### Single Pin - Multiple Ports

Returns the NI-RFSA instrument sessions required to access the pin. If any instrument has more than one port connected to that pin in other sites within the given context the VI returns an error.

[IMAGE alt='PinToNIRFSASessions.vi' src='pintonirfsasessions.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin specifies the name of the pin or pin group to translate to instrument sessions. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Sessions returns the NI-RFSA instrument sessions for the instruments connected to the pin for all sites in the Semiconductor Module context. |
|  | Ports returns the port information for the associated instrument sessions connections to the pin. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Single Pin - Single Port

Returns the NI-RFSA instrument session required to access the pin. If more than one instrument is required to access the pin, or if the instrument has more than one port connected to that pin in other sites within the given context, the VI returns an error.

[IMAGE alt='PinToNIRFSASession.vi' src='pintonirfsasession.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin specifies the name of the pin to translate to an instrument session. If multiple sessions are required, the VI returns an error. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Session returns the NI-RFSA instrument session for the instrument connected to the pin. |
|  | Port returns the instrument port connected to the pin. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/pintonirfsgdeembeddingdata.html language=enus -->
## TOPIC 00097: Pin to NI-RFSG De-Embedding Data (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/pintonirfsgdeembeddingdata.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/pintonirfsgdeembeddingdata.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Pin to NI-RFSG De-Embedding Data (TSM)

**Requires:** TSM

Returns the NI-RFSG de-embedding data associated with the connection(s) to a single pin. You must manually select the polymorphic instance you want to use. Select the single file or multiple files polymorphic instance based on the number of connections you expect the pin to be connected to in the pin map. The multiple file polymorphic instances are recommended to ensure that your code module will work with any pin map, but you can use the single file instance if you know that the code module will never be used with a pin map that has more than one connection to the specified pin.

#### Single Pin- Multiple Ports

Returns the NI-RFmx de-embedding data associated with the connections to the pin. If any instrument in the Semiconductor Module context contains more than a single connection to the pin, the VI returns an error.

[IMAGE alt='PinToNIRFSGMultipleDeembeddingData.vi' src='pintonirfsgmultipledeembeddingdata.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin specifies the name of the pin or pin group to translate to de-embedding data on the connection. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | De-Embedding Files returns the paths and RFmx orientations of the S2P files that characterize the de-embedding network. If the path is an absolute path, the VI returns the absolute path whether the file exists or not. If the path is a relative path and the file exists relative to the path of the pin map file, the VI returns the absolute path of the existing file. Otherwise, the VI returns a string without error. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Single Pin - Single Port

Returns the NI-RFSG de-embedding path and orientation associated with the instrument connection to the pin. If more than one pin connection is found, the VI returns an error.

[IMAGE alt='PinToNIRFSGSingleDeembeddingData.vi' src='pintonirfsgsingledeembeddingdata.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin specifies the name of the pin associated with the instrument. If more than one pin connection is found, the VI returns an error. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out |
|  | De-Embedding File returns the paths and RFSG orientation of the S2P file that characterizes the de-embedding network. If the path is an absolute path, the VI returns the absolute path whether the file exists or not. If the path is a relative path and the file exists relative to the path of the pin map file, the VI returns the absolute path of the existing file. Otherwise, the VI returns a string without error. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/pintonirfsgsession(s).html language=enus -->
## TOPIC 00098: Pin to NI-RFSG Session(s) (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/pintonirfsgsession(s).html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/pintonirfsgsession(s).html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Pin to NI-RFSG Session(s) (TSM)

**Requires:** TSM

Returns the NI-RFSG session required to access one pin. You must manually select the polymorphic instance you want to use. Select the single instrument or multiple instrument polymorphic instance based on the number of instruments you expect the pin to be connected to in the pin map. The multiple instrument polymorphic instances are recommended to ensure that your code module will work with any pin map, but you can use the single instrument instance if you know that the code module will never be used with a pin map that has more than one instrument connected to the specified pins.

#### Single Pin - Multiple Ports

Returns the NI-RFSG instrument sessions required to access the pin. If any instrument has more than one port connected to that pin in other sites within the given context, the VI returns an error.

[IMAGE alt='PinToNIRFSGSessions.vi' src='pintonirfsgsessions.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin specifies the name of the pin or pin group to translate to instrument sessions. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Sessions returns the NI-RFSG instrument sessions for the instruments connected to the pin for all sites in the Semiconductor Module context. |
|  | Ports returns the port information for the associated instrument sessions connections to the pin. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Single Pin - Single Port

Returns the NI-RFSG instrument session required to access the pin. If more than one instrument is required to access the pin, or if the instrument has more than one port connected to that pin in other sites within the given context, the VI returns an error.

[IMAGE alt='PinToNIRFSGSession.vi' src='pintonirfsgsession.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin specifies the name of the pin to translate to an instrument session. If multiple sessions are required, the VI returns an error. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Instrument Session returns the NI-RFSG instrument session for the instrument connected to the pin. |
|  | Port returns the instrument port connected to the pin. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/pintoswitchsessions.html language=enus -->
## TOPIC 00099: Pin to Switch Sessions (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/pintoswitchsessions.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/pintoswitchsessions.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Pin to Switch Sessions (TSM)

**Requires:** TSM

Returns the switch sessions, switch routes, and new Semiconductor Module context objects required to access a switched pin. You must always close references to the Semiconductor Module contexts, even if you do not use them in your code module.

[IMAGE alt='PinToSwitchSessions.vi' src='pintoswitchsessions.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin specifies the name of the pin to translate to sessions and switch routes parameters. |
|  | Multiplexer Type Id specifies the type ID for the multiplexer in the pin map file. When you add a multiplexer to the pin map file, you can define a type ID for the multiplexer, such as the driver name. Multiplexers in the pin map that do not specify a type ID have a default ID of NIGenericMultiplexer. Leave this parameter unwired to use the default value. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Switch Routes returns the routes required to connect an instrument channel to the pin. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Semiconductor Module Contexts returns an array of Semiconductor Module context objects. Each element in the array represents a site that must be executed serially. Use each Semiconductor Module context object to query the pin map and publish data. You must always close references to the Semiconductor Module contexts, even if you do not use them in your code module. |
|  | Session Data returns the session data required to access the switch that connects an instrument channel to the pin. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/publishdatawithcontext.html language=enus -->
## TOPIC 00100: Publish Data (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/publishdatawithcontext.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/publishdatawithcontext.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Publish Data (TSM)

**Requires:** TSM

Publishes measurement data for one or more pins to the Semiconductor Multi Test step type instances for all sites in the Semiconductor Module context. If you are publishing site data, the polymorphic instance must publish data for each site in the Semiconductor Module context. If you are publishing pin data or pattern results, the polymorphic instance must support the pin query context obtained from the specific Pin(s) to Session(s), Pin to FPGA VI Reference(s), or Get Session Data VI you previously created. Pin(s) to Session(s) VIs include the following: Pin(s) to NI-Digital Pattern Sessions, Pin(s) to NI-DCPower Session(s), Pin(s) to NI-DAQmx Task(s), Pin(s) to NI-DMM Session(s), Pin(s) to NI-FGEN Session(s), Pin(s) to NI-SCOPE Session(s), Pin(s) to NI-HSDIO Session(s), Pin to NI-RFSA Session(s), Pin to NI-RFSG Session(s), and Pin to NI-RFmx Session(s).

#### Pin-Based:Pattern Results:2D Array

Publishes the results obtained from calls to the Get Site Pass Fail VI or the Burst Pattern VI of the NI-Digital Pattern instrument driver on multiple instrument sessions. Leave the Pin column blank for the test on the Semiconductor Multi Test step when publishing pattern results with this VI.

[IMAGE alt='PublishPatternResults.vi' src='publishpatternresults.gif']

|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
| --- | --- |
|  | History RAM Information is the History RAM information returned by the niDigital Fetch Multi-Site History RAM Information VI of the NI-Digital Pattern instrument driver after a pattern burst. The niDigital Fetch Multi-Site History RAM Information VI does not appear on the NI-Digital Pattern Driver palette. Browse to and select the VI from the NI-Digital Pattern Driver library file (niDigital.llb), located in the \\instr.lib\\niDigital directory. |
|  | Pattern Results is the site pass/fail results returned by the Get Site Pass Fail VI or Burst Pattern VI of the NI-Digital Pattern instrument driver. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Published Data Id is the unique ID for distinguishing the measurement when you publish multiple measurements within the same code module. |
|  | Pin Query Context Out returns the pin query context object unchanged. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Pin-Based:Pattern Results:1D Array

Publishes the results obtained from calls to the Get Site Pass Fail VI or the Burst Pattern VI of the NI-Digital Pattern instrument driver on a single instrument session. Leave the Pin column blank for the test on the Semiconductor Multi Test step when publishing pattern results with this VI.

[IMAGE alt='PublishPatternResults1D.vi' src='publishpatternresults1d.gif']

|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. |
| --- | --- |
|  | History RAM Information is the History RAM information returned by the niDigital Fetch Multi-Site History RAM Information VI of the NI-Digital Pattern instrument driver after a pattern burst. The niDigital Fetch Multi-Site History RAM Information VI does not appear on the NI-Digital Pattern Driver palette. Browse to and select the VI from the NI-Digital Pattern Driver library file (niDigital.llb), located in the \\instr.lib\\niDigital directory. |
|  | Pattern Results is the site pass/fail results returned by the Get Site Pass Fail VI or Burst Pattern VI of the NI-Digital Pattern instrument driver. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Published Data Id is the unique ID for distinguishing the measurement when you publish multiple measurements within the same code module. |
|  | Pin Query Context Out returns the pin query context object unchanged. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Pin-Based:Parametric:2D Array

Publishes numeric results or data from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context.

[IMAGE alt='PublishDataDouble2D.vi' src='publishdatadouble2d.gif']

|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, and extract data from a set of measurements. You must create a pin query context object from a Pin(s) to Sessions VI. |
| --- | --- |
|  | Data In specifies the multisite measurement data from multiple pins connected to multiple instrument sessions. Each row represents measurements from one instrument session, and each column represents each channel on that instrument session. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Published Data Id is the unique ID for distinguishing the measurement when you publish multiple measurements within the same code module. |
|  | Pin Query Context Out returns the pin query context object unchanged. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Pin-Based:Parametric:1D Array

Publishes numeric results or data from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context.

[IMAGE alt='PublishDataDouble1D.vi' src='publishdatadouble1d.gif']

|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, and extract data from a set of measurements. You must create a pin query context object from a Pin(s) to Session(s) VI. |
| --- | --- |
|  | Data In specifies the multisite measurement data from multiple pins connected to one or more instrument sessions. The array consists of either a collection of single measurements made from multiple instrument sessions or a collection of multiple measurements made from a single instrument session. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Published Data Id is the unique ID for distinguishing the measurement when you publish multiple measurements within the same code module. |
|  | Pin Query Context Out returns the pin query context object unchanged. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Pin-Based:Parametric:Scalar

Publishes numeric results or data from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context.

[IMAGE alt='PublishDataDoubleScalar.vi' src='publishdatadoublescalar.gif']

|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, and extract data from a set of measurements. You must create a pin query context object from a Pin to Session VI. |
| --- | --- |
|  | Data In specifies the double measurement data for a single pin in a single site. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Published Data Id is the unique ID for distinguishing the measurement when you publish multiple measurements within the same code module. |
|  | Pin Query Context Out returns the pin query context object unchanged. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Pin-Based:Pass/Fail:2D Array

Publishes Boolean measurements from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context.

[IMAGE alt='PublishDataBool2D.vi' src='publishdatabool2d.gif']

|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, and extract data from a set of measurements. You must create a pin query context object from a Pin(s) to Sessions VI. |
| --- | --- |
|  | Data In specifies the multisite measurement data from multiple pins connected to multiple instrument sessions. Each row represents measurements from one instrument session, and each column represents each channel on that instrument session. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Published Data Id is the unique ID for distinguishing the measurement when you publish multiple measurements within the same code module. |
|  | Pin Query Context Out returns the pin query context object unchanged. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Pin-Based:Pass/Fail:1D Array

Publishes Boolean measurements from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context.

[IMAGE alt='PublishDataBool1D.vi' src='publishdatabool1d.gif']

|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, and extract data from a set of measurements. You must create a pin query context object from a Pin(s) to Session(s) VI. |
| --- | --- |
|  | Data In specifies the multisite measurement data from multiple pins connected to one or more instrument sessions. The array consists of either a collection of single measurements made from multiple instrument sessions or a collection of multiple measurements made from a single instrument session. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Published Data Id is the unique ID for distinguishing the measurement when you publish multiple measurements within the same code module. |
|  | Pin Query Context Out returns the pin query context object unchanged. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Pin-Based:Pass/Fail:Scalar

Publishes Boolean measurements from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context.

[IMAGE alt='PublishDataBoolScalar.vi' src='publishdataboolscalar.gif']

|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, and extract data from a set of measurements. You must create a pin query context object from a Pin to Session VI. |
| --- | --- |
|  | Data In specifies the Boolean measurement data for a single pin in a single site. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Published Data Id is the unique ID for distinguishing the measurement when you publish multiple measurements within the same code module. |
|  | Pin Query Context Out returns the pin query context object unchanged. |
|  | error out Contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Site-Based:N Sites:Numeric

Publishes double measurements from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context.

[IMAGE alt='PublishDataDoubleFunctionalTest.vi' src='publishdatadoublefunctionaltest.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin is the name of the pin that corresponds to the Data In parameter. |
|  | Data In specifies the double measurement data for all sites in the Semiconductor Module context. The number of elements in the array must be equal to the number of sites. You must return results in the same order as the sites in the Semiconductor Module context. Use the Get Site Numbers VI to obtain the list of site numbers. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Published Data Id is the unique ID for distinguishing the measurement when you publish multiple measurements within the same code module. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Site-Based:N Sites:Boolean

Publishes Boolean measurements from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context.

[IMAGE alt='PublishDataBoolFunctionalTest.vi' src='publishdataboolfunctionaltest.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin is the name of the pin that corresponds to the Data In parameter. |
|  | Data In specifies the Boolean measurement data for all sites in the Semiconductor Module context. The number of elements in the array must be equal to the number of sites. You must return results in the same order as the sites in the Semiconductor Module context. Use the Get Site Numbers VI to obtain the list of site numbers. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Published Data Id is the unique ID for distinguishing the measurement when you publish multiple measurements within the same code module. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Site-Based:N Sites:String

Publishes strings from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context.

[IMAGE alt='PublishDataStringFunctionalTest.vi' src='publishdatastringfunctionaltest.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin is the name of the pin that corresponds to the Data In parameter. |
|  | Data In specifies strings for all sites in the Semiconductor Module context. The number of elements in the array must be equal to the number of sites. You must return results in the same order as the sites in the Semiconductor Module context. Use the Get Site Numbers VI to obtain the list of site numbers. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Published Data Id is the unique ID for distinguishing the measurement when you publish multiple measurements within the same code module. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Site-Based:1 Site:Numeric

Publishes a double measurement from a single site for the Semiconductor Multi Test step to consume. Use this VI to publish data for single site defined in the Semiconductor Module context. If the Semiconductor Module context contains more than one site, this VI returns an error.

[IMAGE alt='PublishDataPerSiteDoubleScalar.vi' src='publishdatapersitedoublescalar.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin is the name of the pin that corresponds to the Data In parameter. |
|  | Data In specifies the double measurement data for a single site in the Semiconductor Module context. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Published Data Id is the unique ID for distinguishing the measurement when you publish multiple measurements within the same code module. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Site-Based:1 Site:Boolean

Publishes a Boolean measurement from a single site for the Semiconductor Multi Test step to consume. Use this VI to publish data for single site defined in the Semiconductor Module context. If the Semiconductor Module context contains more than one site, this VI returns an error.

[IMAGE alt='PublishDataPerSiteBooleanScalar.vi' src='publishdatapersitebooleanscalar.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin is the name of the pin that corresponds to the Data In parameter. |
|  | Data In specifies the Boolean measurement data for a single site in the Semiconductor Module context. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Published Data Id is the unique ID for distinguishing the measurement when you publish multiple measurements within the same code module. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Site-Based:1 Site:String

Publishes a string measurement from a single site for the Semiconductor Multi Test step to consume. Use this VI to publish data for single site defined in the Semiconductor Module context. If the Semiconductor Module context contains more than one site, this VI returns an error.

[IMAGE alt='PublishDataPerSiteStringScalar.vi' src='publishdatapersitestringscalar.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Pin is the name of the pin that corresponds to the Data In parameter. |
|  | Data In specifies the string measurement data for a single site in the Semiconductor Module context. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Published Data Id is the unique ID for distinguishing the measurement when you publish multiple measurements within the same code module. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/publisheddataidcontrol.html language=enus -->
## TOPIC 00101: Published Data Id Control (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/publisheddataidcontrol.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/publisheddataidcontrol.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Published Data Id Control (TSM)

Use the published data ID control to create a control populated with the published data IDs from a [linked sequence file](linkingtsmfiletolabviewproject.html). This allows you to select a value from the control's populated list rather than entering the value as a string. If there is no sequence file linked to the LabVIEW project, or if you are editing the LabVIEW project on a system that cannot access the sequence file, the control acts a string.

|  | Note To create a control, place it on the front panel. Placing a control on the block diagram creates a constant. |
| --- | --- |

| Palette Object | Description |
| --- | --- |
| Published Data Id | Contains a list of published data IDs for the linked sequence file(s). Displays only published data IDs for tests on a Semiconductor Multi Test step whose code module is set to the current VI. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/rearrangemultisitedigitalwaveformswithcontext.html language=enus -->
## TOPIC 00102: Rearrange Multisite Digital Waveforms (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/rearrangemultisitedigitalwaveformswithcontext.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/rearrangemultisitedigitalwaveformswithcontext.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Rearrange Multisite Digital Waveforms (TSM)

**Requires:** TSM

Rearranges multisite waveforms read from NI-HSDIO instruments into per-site digital waveforms.

[IMAGE alt='RearrangeMultisiteDigitalWaveformsWithContext.vi' src='rearrangemultisitedigitalwaveformswithcontext.gif']

|  | Pin Query Context is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, extract data from a set of measurements, and create or rearrange waveforms. You must create a pin query context object from a Pin(s) to NI-HSDIO Sessions VI. |
| --- | --- |
|  | Per Instrument Waveforms specifies an array of digital waveforms in which each element is a waveform acquired from an instrument. The waveform order must correspond to the instrument order the Pin(s) to NI-HSDIO Session(s) VI returns. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Pin Query Context Out returns the pin query context object unchanged. |
|  | Per Site Waveforms returns an array of digital waveforms in which each element is the waveform for a site in the Semiconductor Module context. The order of the sites matches the values from the Get Site Numbers VI. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/relay(s)torelaydriverniswitchsession(s).html language=enus -->
## TOPIC 00103: Relay(s) To Relay Driver NI-SWITCH Session(s) (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/relay(s)torelaydriverniswitchsession(s).html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/relay(s)torelaydriverniswitchsession(s).html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Relay(s) To Relay Driver NI-SWITCH Session(s) (TSM)

**Requires:** TSM

Returns the NI-SWITCH sessions and relay names required to access one or more relays connected to relay driver modules. You must manually select the polymorphic instance you want to use. Select the single relay or multiple relays polymorphic instance based on the number of relays the test is designed to test. Select the single module or multiple module polymorphic instance based on the number of relay driver modules you expect the relay to be connected to in the pin map. Use the multiple module polymorphic instances to ensure that code modules work with any pin map. Use the single module instance only when you know the code module will never be used with a pin map that has more than one relay driver module connected to the specified relays.

#### Multiple Relays - Single Module

Returns the NI-SWITCH session and relay names required to access the relays connected to a relay driver module. If more than one session is required to access the relays, the VI returns an error.

[IMAGE alt='RelaysToRelayDriverNISWITCHSession.vi' src='relaystorelaydriverniswitchsession.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Relays is the names of the relays or relay groups to translate to an NI-SWITCH session and relay names. If more than one session is required, the VI returns an error. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | NI-SWITCH Session returns the NI-SWITCH session for the relay driver module connected to the relays for all sites in the Semiconductor Module context. |
|  | NI-SWITCH Relay Names returns a comma-separated list of relay names for the relay driver module session connected to the relays for all sites in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Multiple Relays - Multiple Modules

Returns the NI-SWITCH sessions and relay names required to access the relays connected to relay driver modules.

[IMAGE alt='RelaysToRelayDriverNISWITCHSessions.vi' src='relaystorelaydriverniswitchsessions.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Relays is the names of the relays or relay groups to translate to NI-SWITCH sessions and relay names. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | NI-SWITCH Sessions returns NI-SWITCH sessions for the relay driver modules connected to the relays for all sites in the Semiconductor Module context. |
|  | NI-SWITCH Relay Names returns comma-separated lists of relay names for the relay driver module sessions connected to the relays for all sites in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Single Relay - Single Module

Returns the NI-SWITCH session and relay names required to access the relay connected to a relay driver module. If more than one session is required to access the relay, the VI returns an error.

[IMAGE alt='RelayToRelayDriverNISWITCHSession.vi' src='relaytorelaydriverniswitchsession.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Relay is the name of the relay or relay group to translate to an NI-SWITCH session and relay names. If more than one session is required, the VI returns an error. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | NI-SWITCH Session returns the NI-SWITCH session for the relay driver module connected to the relay for all sites in the Semiconductor Module context. |
|  | NI-SWITCH Relay Names returns a comma-separated list of relay names for the relay driver module session connected to the relay for all sites in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### Single Relay - Multiple Modules

Returns the NI-SWITCH sessions and relay names required to access the relay connected to relay driver modules.

[IMAGE alt='RelayToRelayDriverNISWITCHSessions.vi' src='relaytorelaydriverniswitchsessions.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Relay is the name of the relay or relay group to translate to NI-SWITCH sessions and relay names. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | NI-SWITCH Sessions returns NI-SWITCH sessions for the relay driver modules connected to the relay for all sites in the Semiconductor Module context. |
|  | NI-SWITCH Relay Names returns comma-separated lists of relay names for the relay driver module sessions connected to the relay for all sites in the Semiconductor Module context. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/relaydriverpal.html language=enus -->
## TOPIC 00104: Relay Driver VIs (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/relaydriverpal.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/relaydriverpal.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Relay Driver VIs (TSM)

Use the Relay Driver VIs to manage PXI-2567 relay driver modules and sessions and to switch relays.

The VIs on this palette return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html).

| Palette Object | Description |
| --- | --- |
| Get Relay Driver Module Names | Returns the names of all relay driver modules in the Semiconductor Module context. You can use the relay driver module names to open driver sessions. |
| Get All Relay Driver NI-SWITCH Sessions | Returns NI-SWITCH sessions for all relay driver modules in the Semiconductor Module context. |
| Set Relay Driver NI-SWITCH Session | Associates an NI-SWITCH session with a relay driver module. |
| Relay(s) To Relay Driver NI-SWITCH Session(s) | Returns the NI-SWITCH sessions and relay names required to access one or more relays connected to relay driver modules. You must manually select the polymorphic instance you want to use. |
| Control Relay(s) | Performs relay actions to relays. You must manually select the polymorphic instance you want to use. Select the single relay or multiple relays polymorphic instance based on the number of relays for which you perform the actions. |
| Get Relay Names | Returns all site and system relays available in the Semiconductor Module context that are connected to relay driver modules. This VI returns all relays defined in the Semiconductor Module context. |

#### TSM Controls

The Relay Driver palette also contains the relay and relay configuration controls, which you can use to create controls populated with the relays and relay configurations from a [linked sequence file](linkingtsmfiletolabviewproject.html). This allows you to select a value from the control's populated list rather than entering the value as a string. If there is no sequence file linked to the LabVIEW project, or if you are editing the LabVIEW project on a system that cannot access the sequence file, the control acts a string.

|  | Note To create a control, place it on the front panel. Placing a control on the block diagram creates a constant. |
| --- | --- |

| Palette Object | Description |
| --- | --- |
| Relay | Contains a list of relays for the linked sequence file(s). |
| Relay Configuration | Contains a list of relay configurations for the linked sequence file(s). |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/rfmxpal.html language=enus -->
## TOPIC 00105: NI-RFmx VIs (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/rfmxpal.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/rfmxpal.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

NI-RFmx VIs (TSM)

Use the NI-RFmx VIs to manage NI-RFmx instruments and sessions.

The VIs on this palette return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html).

| Palette Object | Description |
| --- | --- |
| Get All NI-RFmx Instrument Names | Returns the instrument names for all NI-RFmx instruments in the Semiconductor Module context. You can use instrument names to open driver sessions. |
| Set NI-RFmx Session | Associates an instrument session with an NI-RFmx instrument name. |
| Get All NI-RFmx Sessions | Returns all NI-RFmx instrument sessions in the Semiconductor Module context. |
| Pin To NI-RFmx Session(s) | Returns the NI-RFmx session required to access one pin. You must manually select the polymorphic instance you want to use. |
| Pin To NI-RFmx De-Embedding Data | Returns the NI-RFmx de-embedding data associated with the connection(s) to a single pin. You must manually select the polymorphic instance you want to use. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/rfpal.html language=enus -->
## TOPIC 00106: RF VIs (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/rfpal.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/rfpal.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

RF VIs (TSM)

Use the NI-RFSA, NI-RFSG, NI-RFmx, NI-RFPM, and FPGA VIs to manage NI-RFSA, NI-RFSG, NI-RFPM, and RF RIO (RF LabVIEW FPGA enabled) instruments.

The VIs on this palette return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html).

| Palette Object | Description |
| --- | --- |
| NI-RFSA VIs | Use the NI-RFSA VIs to manage NI-RFSA instruments and sessions. |
| NI-RFSG VIs | Use the NI-RFSG VIs to manage NI-RFSG instruments and sessions. |
| NI-RFmx | Use the NI-RFmx VIs to manage NI-RFmx instruments and sessions. |
| NI-RFPM | Use the NI-RFPM VIs to manage NI-RFPM subsystems and sessions. |
| FPGA VIs | Use the FPGA VIs to manage FPGA sessions for RF RIO instruments (RF LabVIEW FPGA enabled instruments). |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/rfpmpal.html language=enus -->
## TOPIC 00107: NI-RFPM VIs (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/rfpmpal.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/rfpmpal.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

NI-RFPM VIs (TSM)

Use the NI-RFPM VIs to manage NI-RFPM subsystems and sessions.

The VIs on this palette return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html).

| Palette Object | Description |
| --- | --- |
| Get All NI-RFPM Instrument Names | Returns the names of all NI-RFPM subsystems and respective calibration file paths, IVI Switch names, and FPGA file paths in the Semiconductor Module context. You can use instrument names, IVI Switch names, FPGA file paths, and calibration file paths to open instrument and calibration sessions. |
| Set NI-RFPM Session | Associates an open NI-RFPM session and IVI Switch session with the NI-RFPM instrument name. |
| Get All NI-RFPM Sessions | Returns all NI-RFPM subsystem sessions in the Semiconductor Module context. |
| Pin(s) To NI-RFPM Sessions | Returns the NI-RFPM sessions and ports required to access one or more pins, as well as paths and orientations of the S2P files that characterize the de-embedding network for each port. You must manually select the polymorphic instance you want to use. |
| Get All NI-RFPM De-embedding Data | Returns the NI-RFPM subsystem sessions and paths and orientations of the S2P files that characterize the de-embedding network for every port connected to a DUT pin in the Semiconductor Module context. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/rfsapal.html language=enus -->
## TOPIC 00108: NI-RFSA VIs (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/rfsapal.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/rfsapal.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

NI-RFSA VIs (TSM)

Use the NI-RFSA VIs to manage NI-RFSA instruments and sessions.

The VIs on this palette return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html).

| Palette Object | Description |
| --- | --- |
| Get All NI-RFSA Instrument Names | Returns the instrument names for all NI-RFSA instruments in the Semiconductor Module context. You can use instrument names to open driver sessions. |
| Set NI-RFSA Session | Associates an instrument session with an NI-RFSA instrument name. |
| Get All NI-RFSA Sessions | Returns all NI-RFSA instrument sessions in the Semiconductor Module context. |
| Pin To NI-RFSA Session(s) | Returns the NI-RFSA session required to access one pin. You must manually select the polymorphic instance you want to use. |
| Pin To NI-RFSA De-Embedding Data | Returns the NI-RFSA de-embedding data associated with the connection(s) to a single pin. You must manually select the polymorphic instance you want to use. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/rfsgpal.html language=enus -->
## TOPIC 00109: NI-RFSG VIs (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/rfsgpal.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/rfsgpal.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

NI-RFSG VIs (TSM)

Use the NI-RFSG VIs to manage NI-RFSG instruments and sessions.

The VIs on this palette return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html).

| Palette Object | Description |
| --- | --- |
| Get All NI-RFSG Instrument Names | Returns the instrument names for all NI-RFSG instruments in the Semiconductor Module context. You can use instrument names to open driver sessions. |
| Set NI-RFSG Session | Associates an instrument session with an NI-RFSG instrument name. |
| Get All NI-RFSG Sessions | Returns all NI-RFSG instrument sessions in the Semiconductor Module context. |
| Pin To NI-RFSG Session(s) | Returns the NI-RFSG session required to access one pin. You must manually select the polymorphic instance you want to use. |
| Pin To NI-RFSG De-Embedding Data | Returns the NI-RFSG de-embedding data associated with the connection(s) to a single pin. You must manually select the polymorphic instance you want to use. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/setfpgavireference.html language=enus -->
## TOPIC 00110: Set FPGA VI Reference (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/setfpgavireference.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/setfpgavireference.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Set FPGA VI Reference (TSM)

**Requires:** TSM

Associates an instrument session with an FPGA-enabled instrument name.

[IMAGE alt='SetFPGAVIReference.vi' src='setfpgavireference.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Instrument Name is the instrument name in the pin map file for the corresponding session. |
|  | FPGA VI Reference is the FPGA reference associated with the corresponding Instrument Name. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/setglobaldata.html language=enus -->
## TOPIC 00111: Set Global Data (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/setglobaldata.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/setglobaldata.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Set Global Data (TSM)

**Requires:** TSM

Associates a data item with a data ID. You can use this VI to store an instrument session or other data you initialize in a central location but access from multiple sites. The data item is accessible from a process model controller execution and all of its test socket executions. You cannot pass LabVIEW class references to this VI.

[IMAGE alt='SetGlobalData.vi' src='setglobaldata.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Data Id specifies a unique ID to distinguish the data. |
|  | Data specifies a data item to store and later retrieve using the specified data ID. If the data item is an empty variant, the VI deletes the data with the specified Data Id if it exists. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/setnidaqmxtask.html language=enus -->
## TOPIC 00112: Set NI-DAQmx Task (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/setnidaqmxtask.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/setnidaqmxtask.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Set NI-DAQmx Task (TSM)

**Requires:** TSM

Associates an NI-DAQmx task with an NI-DAQmx task name defined in the pin map.

[IMAGE alt='SetNIDAQmxTask.vi' src='setnidaqmxtask.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | DAQmx Task specifies the NI-DAQmx task for the corresponding task name. |
|  | Task Name is the task name in the pin map file for the corresponding task. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/setnidcpowersessionwithresourcestring.html language=enus -->
## TOPIC 00113: Set NI-DCPower Session (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/setnidcpowersessionwithresourcestring.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/setnidcpowersessionwithresourcestring.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Set NI-DCPower Session (TSM)

**Requires:** TSM

Associates an NI-DCPower session with all resources of an NI-DCPower resource string.

[IMAGE alt='SetNIDCPowerSessionWithResourceString.vi' src='setnidcpowersessionwithresourcestring.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Resource String specifies the Resource String associated with the the corresponding Instrument Session, the resource string is a comma-separated list of resources where each resource is defined as <instrument>/<channel>. |
|  | Instrument Session specifies the NI-DCPower session for the corresponding Resource String. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/setnidigitalpatternsession.html language=enus -->
## TOPIC 00114: Set NI-Digital Pattern Session (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/setnidigitalpatternsession.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/setnidigitalpatternsession.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Set NI-Digital Pattern Session (TSM)

**Requires:** TSM

Associates an instrument session with an NI-Digital Pattern instrument name. This VI is available only in 64-bit LabVIEW.

[IMAGE alt='SetNIDigitalPatternSession.vi' src='setnidigitalpatternsession.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Instrument Name is the instrument name in the pin map file for the corresponding session. |
|  | Instrument Session specifies the instrument session for the corresponding instrument name. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/setnidmmsession.html language=enus -->
## TOPIC 00115: Set NI-DMM Session (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/setnidmmsession.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/setnidmmsession.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Set NI-DMM Session (TSM)

**Requires:** TSM

Associates an instrument session with an NI-DMM instrument name.

[IMAGE alt='SetNIDMMSession.vi' src='setnidmmsession.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Instrument Name is the instrument name in the pin map file for the corresponding session. |
|  | Instrument Session specifies the instrument session for the corresponding instrument name. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/setnifgensession.html language=enus -->
## TOPIC 00116: Set NI-FGEN Session (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/setnifgensession.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/setnifgensession.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Set NI-FGEN Session (TSM)

**Requires:** TSM

Associates an instrument session with an NI-FGEN instrument name.

[IMAGE alt='SetNIFGenSession.vi' src='setnifgensession.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Instrument Name is the instrument name in the pin map file for the corresponding session. |
|  | Instrument Session specifies the instrument session for the corresponding instrument name. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/setnihsdiosessions.html language=enus -->
## TOPIC 00117: Set NI-HSDIO Sessions (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/setnihsdiosessions.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/setnihsdiosessions.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Set NI-HSDIO Sessions (TSM)

**Requires:** TSM

Associates an NI-HSDIO acquisition session and an NI-HSDIO generation session with an NI-HSDIO instrument name.

[IMAGE alt='SetNIHSDIOSessions.vi' src='setnihsdiosessions.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Instrument Name specifies the instrument name in the pin map file for the corresponding acquisition session and generation session. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Acquisition Session specifies the NI-HSDIO acquisition session for the corresponding instrument name. |
|  | Generation Session specifies the NI-HSDIO generation session for the corresponding instrument name. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/setnirfmxsession.html language=enus -->
## TOPIC 00118: Set NI-RFmx Session (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/setnirfmxsession.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/setnirfmxsession.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Set NI-RFmx Session (TSM)

**Requires:** TSM

Associates an instrument session with an NI-RFmx instrument name.

[IMAGE alt='SetNIRFmxSession.vi' src='setnirfmxsession.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Instrument Name is the instrument name in the pin map file for the corresponding session. |
|  | NI-RFmx Session is the instrument session for the corresponding instrument name. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/setnirfpmsession.html language=enus -->
## TOPIC 00119: Set NI-RFPM Session (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/setnirfpmsession.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/setnirfpmsession.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Set NI-RFPM Session (TSM)

**Requires:** TSM

Associates an open NI-RFPM session and IVI Switch session with the NI-RFPM instrument name.

[IMAGE alt='SetNIRFPMSession.vi' src='setnirfpmsession.gif']

|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- | --- |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | NI-RFPM Session is the NI-RFPM subsystem session for the corresponding instrument name. |
|  | Instrument Name is the instrument name in the pin map file for the corresponding sessions. |
|  | Semiconductor Module Context out returns the Semiconductor Module Context parameter unchanged. |
|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/setnirfsasession.html language=enus -->
## TOPIC 00120: Set NI-RFSA Session (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/setnirfsasession.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/setnirfsasession.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Set NI-RFSA Session (TSM)

**Requires:** TSM

Associates an instrument session with an NI-RFSA instrument name.

[IMAGE alt='SetNIRFSASession.vi' src='setnirfsasession.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Instrument Name is the instrument name in the pin map file for the corresponding session. |
|  | NI-RFSA Session is the instrument session for the corresponding instrument name. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/setnirfsgsession.html language=enus -->
## TOPIC 00121: Set NI-RFSG Session (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/setnirfsgsession.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/setnirfsgsession.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Set NI-RFSG Session (TSM)

**Requires:** TSM

Associates an instrument session with an NI-RFSG instrument name.

[IMAGE alt='SetNIRFSGSession.vi' src='setnirfsgsession.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Instrument Name is the instrument name in the pin map file for the corresponding session. |
|  | NI-RFSG Session is the instrument session for the corresponding instrument name. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/setniscopesession.html language=enus -->
## TOPIC 00122: Set NI-SCOPE Session (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/setniscopesession.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/setniscopesession.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Set NI-SCOPE Session (TSM)

**Requires:** TSM

Associates an instrument session with an NI-SCOPE instrument name.

[IMAGE alt='SetNISCOPESession.vi' src='setniscopesession.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Instrument Name is the instrument name in the pin map file for the corresponding session. |
|  | Instrument Session specifies the instrument session for the corresponding instrument name. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/setrelaydriverniswitchsession.html language=enus -->
## TOPIC 00123: Set Relay Driver NI-SWITCH Session (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/setrelaydriverniswitchsession.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/setrelaydriverniswitchsession.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Set Relay Driver NI-SWITCH Session (TSM)

**Requires:** TSM

Associates an NI-SWITCH session with a relay driver module.

[IMAGE alt='SetRelayDriverNISWITCHSession.vi' src='setrelaydriverniswitchsession.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Relay Driver Module Name is the relay driver module name in the pin map file for the corresponding session. |
|  | NI-SWITCH Session specifies the NI-SWITCH session for the corresponding relay driver module name. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/setsessiondata.html language=enus -->
## TOPIC 00124: Set Session Data (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/setsessiondata.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/setsessiondata.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Set Session Data (TSM)

**Requires:** TSM

Associates a session with an instrument and channel group.

[IMAGE alt='SetSessionData.vi' src='setsessiondata.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Instrument Name is the instrument name in the pin map file for the corresponding session. |
|  | Channel Group Id is the channel group in the pin map file for the corresponding session. For channels that do not belong to a channel group in the pin map, the Semiconductor Module creates a channel group with the same ID as the channel. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Instrument Type Id specifies the type ID for the instrument in the pin map file. All custom instruments defined in the pin map specify an associated type ID. Typically, this type ID is an instrument driver name or other ID that is common for instruments that users program in a similar way. For custom instruments, you must pass the type ID associated with the instrument in the pin map file. For model-based instruments, you can pass any string that does not start with "ni" for the type ID. |
|  | Session Data is the session for the corresponding instrument name and channel group ID. Use the variant data type to properly store different types of sessions. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/setsitedatapoly.html language=enus -->
## TOPIC 00125: Set Site Data (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/setsitedatapoly.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/setsitedatapoly.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Set Site Data (TSM)

**Requires:** TSM

Associates a data item with each site. You can associate data with all sites or with the subset of sites in the Semiconductor Module context. You can use this VI to store instrument sessions or other per-site data you initialize in a central location but access within each site. The data item is accessible from a process model controller execution and the site with which the data is associated.

#### 1D Array

Associates a data item with each site. You can associate data with all sites or with the subset of sites in the Semiconductor Module context. You can use this VI to store instrument sessions or other per-site data you initialize in a central location but access within each site. The data item is accessible from a process model controller execution and the site with which the data is associated. You cannot pass LabVIEW class references to this VI.

[IMAGE alt='SetSiteData.vi' src='setsitedata.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Data Id specifies a unique ID to distinguish the data. |
|  | Site Data specifies an array of data with one element for each site in the system or one element for each site in the Semiconductor Module Context. If the array is empty, the VI deletes any data with the specified Data Id parameter if it exists. If the array contains data for each site in the Semiconductor Module context, each item in the array contains data for the site specified by the corresponding item in the Get Site Numbers VI. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

#### 2D Array

Associates a data item with each site. You can associate data with all sites or with the subset of sites in the Semiconductor Module context. You can use this VI to store instrument sessions or other per-site data you initialize in a central location but access within each site. The data item is accessible from a process model controller execution and the site with which the data is associated. You cannot pass LabVIEW class references to this VI.

[IMAGE alt='SetSiteData2D.vi' src='setsitedata2d.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Data Id specifies a unique ID to distinguish the data. |
|  | Site Data specifies a 2D array of data with one row for each site in the system or one row for each site in the Semiconductor Module Context. If the array is empty, the VI deletes any data with the specified Data Id parameter if it exists. If the array contains data for each site in the Semiconductor Module context, each row in the array contains data for the site specified by the corresponding item in the Get Site Numbers VI. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/setswitchsession.html language=enus -->
## TOPIC 00126: Set Switch Session (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/setswitchsession.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/setswitchsession.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Set Switch Session (TSM)

**Requires:** TSM

Associates an open switch session with the switch name of the type you specify in the **Multiplexer Type Id** parameter.

[IMAGE alt='SetSwitchSession.vi' src='setswitchsession.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Switch Name is the switch name in the pin map file for the corresponding session. |
|  | Session Data is the switch session for the switch name. Use the variant data type to properly store different types of sessions. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Multiplexer Type Id specifies the type ID for the multiplexer in the pin map file. When you add a multiplexer to the pin map file, you can define a type ID for the multiplexer, such as the driver name. Multiplexers in the pin map that do not specify a type ID have a default ID of NIGenericMultiplexer. Leave this parameter unwired to use the default value. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/sitedataexists.html language=enus -->
## TOPIC 00127: Site Data Exists? (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/sitedataexists.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/sitedataexists.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Site Data Exists? (TSM)

**Requires:** TSM

Returns a Boolean value indicating whether site data exists for the data ID specified by the **Data Id** parameter. If a data item with the specified **Data Id** exists for some, but not all, sites in the Semiconductor Module Context, the VI returns an error.

[IMAGE alt='SiteDataExists.vi' src='sitedataexists.gif']

|  | Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. |
| --- | --- |
|  | Data Id specifies the unique ID to distinguish the data. This parameter must match a value you specify in a call to the Set Site Data VI. |
|  | error in (no error) describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. |
|  | Semiconductor Module Context Out returns the Semiconductor Module Context parameter unchanged. |
|  | Site Data Exists? indicates whether the specified Data Id parameter has data associated with it. |
|  | error out contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/siteglobaldatapal.html language=enus -->
## TOPIC 00128: Site and Global Data VIs (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/siteglobaldatapal.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/siteglobaldatapal.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Site and Global Data VIs (TSM)

Use the Site and Global Data VIs to manage site and global data.

The VIs on this palette return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html).

| Palette Object | Description |
| --- | --- |
| Set Site Data | Associates a data item with each site. You can associate data with all sites or with the subset of sites in the Semiconductor Module context. You can use this VI to store instrument sessions or other per-site data you initialize in a central location but access within each site. The data item is accessible from a process model controller execution and the site with which the data is associated. You must manually select the polymorphic instance you want to use. |
| Get Site Data | Returns per-site data that a previous call to the Set Site Data VI stores. The returned array contains the data the Semiconductor Module context stores for each site in the same order as the sites that the Get Site Numbers VI returns. |
| Site Data Exists? | Returns a Boolean value indicating whether site data exists for the data ID specified by the Data Id parameter. |
| Set Global Data | Associates a data item with a data ID. You can use this VI to store an instrument session or other data you initialize in a central location but access from multiple sites. The data item is accessible from a process model controller execution and all of its test socket executions. |
| Get Global Data | Returns a global data item with the data ID that a previous call to the Set Global Data VI stores. |
| Global Data Exists? | Returns a Boolean value indicating whether global data exists for the data ID specified by the Data Id parameter. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/specificationspal.html language=enus -->
## TOPIC 00129: Specifications VIs (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/specificationspal.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/specificationspal.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Specifications VIs (TSM)

Use the Specifications VIs to obtain resolved values defined in the specification file the test program specifies.

The VIs on this palette return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html).

| Palette Object | Description |
| --- | --- |
| Get Specification(s) Value(s) | Returns the value or values calculated for the variables in the Semiconductor Module context specifications file. |

#### TSM Controls

The Specifications palette also contains the specification control, which you can use to create a control populated with the specifications from a [linked sequence file](linkingtsmfiletolabviewproject.html). This allows you to select a value from the control's populated list rather than entering the value as a string. If there is no sequence file linked to the LabVIEW project, or if you are editing the LabVIEW project on a system that cannot access the sequence file, the control acts a string.

|  | Note To create a control, place it on the front panel. Placing a control on the block diagram creates a constant. |
| --- | --- |

| Palette Object | Description |
| --- | --- |
| Specification | Contains a list of specifications for the linked sequence file(s). |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/switchingpal.html language=enus -->
## TOPIC 00130: Switching VIs (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/switchingpal.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/switchingpal.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Switching VIs (TSM)

Use the Switching VIs to store and return switch sessions, return the names of all switches defined in the pin map, and access a switched pin.

The VIs on this palette return [general LabVIEW error codes](/csh?topicname=lverror/misc_lv_error_codes.html).

| Palette Object | Description |
| --- | --- |
| Get All Switch Names | Returns the names of all switches in the Semiconductor Module context. You can use switch names to open driver sessions. |
| Set Switch Session | Associates an open switch session with the switch name. |
| Get Switch Sessions | Returns all sessions for switches in the Semiconductor Module context. |
| Pin to Switch Sessions | Returns the switch sessions, switch routes, and new Semiconductor Module context objects required to access a switched pin. |

<!--NI_TOPIC bundle=tsm-labview-api path=lvtssemiconductor/tsmappapi.html language=enus -->
## TOPIC 00131: Using the TSM Application API in LabVIEW Applications (TSM)

- bundle_id: `tsm-labview-api`
- source_path: `lvtssemiconductor/tsmappapi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-api/raw/resource/enus/lvtssemiconductor/tsmappapi.html
- document_id: `tsm-labview-api`
- page_type: `leaf`
- content_type: ``

Using the TSM Application API in LabVIEW Applications (TSM)

TSM does not provide a full set of VIs for every [TSM Application API](../tssemiconductor/tssmapplicationapi.html) method and property. You can access the methods and properties on the TSM Application API COM server using the LabVIEW ActiveX Invoke and Property nodes. The Application Development palette in LabVIEW includes a set of wrapper VIs that use the TSM Application API COM server for some functionality. To access the wrapper VIs, add the SemiconductorModuleManager.mnu palette from the <LabVIEW>\vi.lib\NI_TestStand_SemiconductorModule\NI_TestStand_Semiconductor_Module.lvlibp project library to the palette in LabVIEW.

Refer to the *TestStand Semiconductor Module Application API* topic in the *TestStand Semiconductor Module Help* for more information about the TSM Application API. Select **Help»TestStand Help** and navigate to the *TestStand Semiconductor Module* book in the table of contents of the *TestStand Help* to launch the *TestStand Semiconductor Module Help*.
