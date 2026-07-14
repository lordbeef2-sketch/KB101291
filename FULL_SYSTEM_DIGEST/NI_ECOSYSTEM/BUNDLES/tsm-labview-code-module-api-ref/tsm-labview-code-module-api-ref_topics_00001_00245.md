# NI DOCUMENT BUNDLE: tsm-labview-code-module-api-ref

<!--NI_BUNDLE_CHUNK bundle=tsm-labview-code-module-api-ref start=1 end=245 -->
<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=Linking_SequenceFile_to_LVProject.html language=enus -->
## TOPIC 00001: Linking a Sequence File to a LabVIEW Project File (TSM)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `Linking_SequenceFile_to_LVProject.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/Linking_SequenceFile_to_LVProject.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `topic`
- source_description: Use the Semiconductor Module Link Manager dialog box to link sequence files to a LabVIEW project file, which allows the selected sequence file(s) to populate pin, relay, relay configuration, specification, published data ID, and input data ID controls in the selected LabVIEW project. Choose one of t

### Linking a Sequence File to a LabVIEW Project File (TSM)

Use the Semiconductor Module Link Manager dialog box to link sequence files to a LabVIEW project file, which allows the selected sequence file(s) to populate pin, relay, relay configuration, specification, published data ID, and input data ID controls in the selected LabVIEW project.

Choose one of the following options to launch the Semiconductor Module Link Manager dialog box:

- Click the Semiconductor Module Link Manager button in the Project Explorer window.
- Right-click the project root in the Project Explorer window and select Semiconductor Module Link Manager .
- Right-click the control and select Semiconductor Module Link Manager .

The Semiconductor Module Link Manager dialog box allows you to add or remove linked sequence files and displays all sequence files linked to the open LabVIEW project file. If you link multiple sequence files with different pin map or specification files, TSM combines the values into a single list when populating the controls. The order of the sequence files determines the order in which the values are listed in the control. To reorder the sequence files, use drag and drop.

If you make any changes in the Semiconductor Module Link Manager dialog box, the dialog box prompts you to save now or to save the project later. If you do not save now, you must save later for the changes to persist.

If you modify the pin map, specification files, published data IDs, or input data IDs of a linked sequence file while the LabVIEW project file is open, right-click the corresponding control and click **Refresh** to update the listed values.

You can also link a TSM sequence file to a LabVIEW project file in TSM. Refer to **LabVIEW Project Panel** in the **TestStand Semiconductor Module Help** for more information.

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/advanced/advanced-mnu.html language=enus -->
## TOPIC 00002: Advanced

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/advanced/advanced-mnu.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/advanced/advanced-mnu.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Advanced VIs to create custom VIs for instruments that the TestStand Semiconductor Module does not natively support, query the site numbers in the Semiconductor Module context, and manage per-site and global data. icon

### Advanced

Use the Advanced VIs to create custom VIs for instruments that the TestStand Semiconductor Module does not natively support, query the site numbers in the Semiconductor Module context, and manage per-site and global data.

[IMAGE alt='icon' src='advanced-mnu.png']

- [Get Site Numbers](../../../../../menus/categories/ni-semiconductormodule/pinmap/advanced/getsitenumbers-vi.html) Returns the site numbers and number of sites in the Semiconductor Module context.
- [Get Session And Channel Index](../../../../../menus/categories/ni-semiconductormodule/pinmap/advanced/getsessionandchannelindexwithcontext-vi.html) Returns the index of the channel group and channel that corresponds to a pin query. Use this VI to access an individual pin when you take a measurement across multiple instruments and pins. When you call a pin query VI, such as the Pins to NI-HSDIO Sessions VI, the VI returns an array of sessions and a channel list. Use the Get Session and Channel Index VI to identify which session and which channel refers to a pin and site number you specify.
- [Get Input Data](../../../../../menus/categories/ni-semiconductormodule/pinmap/input-data/getinputdata-vi.html) Returns per-site input data as defined in the Semiconductor Multi Test step. You must manually select the polymorphic instance you want to use.
- [Filter Pins](../../../../../menus/categories/ni-semiconductormodule/pinmap/advanced/filterpinsbyinstrumenttype-vi.html) Filters the pins by instrument type ID. Pass a list of all pins or pin groups to return the pins connected to instruments of the type you specify in the Instrument Type Id parameter. If no pins are connected to instruments of the type you specify in the Instrument Type Id parameter, this VI returns an empty array.
- [Extract Pin Data](../../../../../menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/extractpindata-vi.html) Extracts the measurement data for a specified pin from measurements obtained from an instrument session and arranges the data in the order of sites in the Semiconductor Module context. Use this VI when you have raw measurement data from an instrument session that you need to manipulate in a site-specific way. For example, if you need to perform an operation on the measurement data using per-site input data, this VI puts the measurement data for the selected pin into the same per-site order as the input data. Similarly, if you need to modify the data from a specific site before publishing, this VI puts the measurement data for the selected pin into a per-site array that you can then index to retrieve the data for the specific site. The order of the per-site array matches the order of the Site Numbers output parameter of the Get Site Numbers VI. You can use the Per-Site Publish VI to publish the resulting manipulated data.
- [Per-Instrument to Per-Site Data](../../../../../menus/categories/ni-semiconductormodule/pinmap/advanced/perinstrumenttopersitedata-vi.html) Transforms the measurement data from measurements obtained from an instrument session and arranges the data in the order of sites and pins in the Semiconductor Module context. Use this VI when you have raw measurement data from an instrument session that you need to manipulate in a site-specific way. For example, if you need to perform an operation on the measurement data using per-site input data, this VI puts the measurement data for all pins into the same per-site order as the input data. Similarly, if you need to modify the data from a specific site before publishing, this VI puts the measurement data for the all pins into a per-site array that you can then index to retrieve the data for the specific site. The order of the per-site array matches the order of the Site Numbers output parameter of the Get Site Numbers VI.
- [Get Offline Mode](../../../../../menus/categories/ni-semiconductormodule/pinmap/advanced/getofflinemode-vi.html) Returns the current status of the Offline Mode setting. Offline Mode allows you to develop, run, and debug test programs on a computer without access to NI instruments.
- [Get Pins In Pin Group(s)](../../../../../menus/categories/ni-semiconductormodule/pinmap/advanced/getpinsinpingroup-s-vi.html) Returns a list of pins contained in the pin group or list of pin groups you specify. You must manually select the polymorphic instance you want to use. Select the single pin group or multiple pin groups polymorphic instance based on the number of pin groups you want to query.
- [Get Relays In Relay Group(s)](../../../../../menus/categories/ni-semiconductormodule/pinmap/advanced/getrelaysinrelaygroup-s-vi.html) Returns a list of relays contained in the relay group or list of relay groups you specify. You must manually select the polymorphic instance you want to use. Select the single relay group or multiple relay groups polymorphic instance based on the number of relay groups you want to query.
- [Get Site Semiconductor Module Contexts](../../../../../menus/categories/ni-semiconductormodule/pinmap/advanced/getsitesemiconductormodulecontexts-vi.html) Returns an array of Semiconductor Module context objects, each of which represents a single site. The size and ordering of the array match the size and ordering of the sites in the Semiconductor Module Context input. You must always close references to the Semiconductor Module contexts, even if you do not use them in your code module.
- [Input Data Id](../../../../../menus/categories/ni-semiconductormodule/pinmap/tagprovider/tsm-inputdataid-ctl.html) Contains a list of input data IDs for the linked sequence file(s). Displays only input data IDs on Semiconductor steps whose code module is set to the current VI.
- [Filter Relays](../../../../../menus/categories/ni-semiconductormodule/pinmap/advanced/filterrelaysbyinstrumenttype-vi.html) Filters the relays by instrument type ID. Pass a list of all relays or relay groups to return the relays connected to instruments of the type you specify in the Instrument Type Id parameter. If no relays are connected to instruments of the type you specify in the Instrument Type Id parameter, this VI returns an empty array.

Parent topic:

Code Module Development

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/advanced/custom-instruments/custom-instruments-mnu.html language=enus -->
## TOPIC 00003: Custom Instruments

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/advanced/custom-instruments/custom-instruments-mnu.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/advanced/custom-instruments/custom-instruments-mnu.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Custom Instruments VIs to manage custom instruments and sessions. icon

### Custom Instruments

Use the Custom Instruments VIs to manage custom instruments and sessions.

[IMAGE alt='icon' src='custom-instruments-mnu.png']

- [Get All Instrument Definitions](../../../../../../menus/categories/ni-semiconductormodule/pinmap/advanced/custom-instruments/getallinstrumentdefinitions-vi.html) Returns the channel group ID and associated instrument names and channel lists of all instruments of type Instrument Type Id defined in the Semiconductor Module context. You can use instrument names, channel group IDs, and channel lists to open driver sessions. The Instrument Names , Channel Group Ids , and Channel Lists parameters always return the same number of elements. Instrument names repeat in the Instrument Names parameter if the instrument has multiple channel groups.
- [Set Session Data](../../../../../../menus/categories/ni-semiconductormodule/pinmap/advanced/custom-instruments/setsessiondata-vi.html) Associates a session with an instrument and channel group.
- [Get All Session Data](../../../../../../menus/categories/ni-semiconductormodule/pinmap/advanced/custom-instruments/getallsessiondata-vi.html) Returns all sessions in the Semiconductor Module context that belong to instruments of the type you specify in the Instrument Type Id parameter.
- [Get Session Data](../../../../../../menus/categories/ni-semiconductormodule/pinmap/advanced/custom-instruments/getsessiondata-vi.html) Returns all sessions in the Semiconductor Module context associated with the pins.

Parent topic:

Code Module Development

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/advanced/custom-instruments/getallinstrumentdefinitions-vi.html language=enus -->
## TOPIC 00004: Get All Instrument Definitions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/advanced/custom-instruments/getallinstrumentdefinitions-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/advanced/custom-instruments/getallinstrumentdefinitions-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the channel group ID and associated instrument names and channel lists of all instruments of type Instrument Type Id defined in the Semiconductor Module context. You can use instrument names, channel group IDs, and channel lists to open driver sessions. The Instrument Names, Channel Group Id

### Get All Instrument Definitions

Returns the channel group ID and associated instrument names and channel lists of all instruments of type **Instrument Type Id** defined in the Semiconductor Module context. You can use instrument names, channel group IDs, and channel lists to open driver sessions. The **Instrument Names**, **Channel Group Ids**, and **Channel Lists** parameters always return the same number of elements. Instrument names repeat in the **Instrument Names** parameter if the instrument has multiple channel groups.

[IMAGE alt='icon' src='getallinstrumentdefinitions-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Instrument Type Id — specifies the type ID for the instrument in the pin map file. All custom instruments defined in the pin map specify an associated type ID. Typically, this type ID is an instrument driver name or other ID that is common for instruments that users program in a similar way. For custom instruments, you must pass the type ID associated with the instrument in the pin map file. For model-based instruments, pass the string you passed to the Set Custom Session VI to store sessions for the instruments. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Names — returns the names of all instruments in the Semiconductor Module context that are of type you specify in the Instrument Type Id parameter. Channel Group Ids — returns the IDs of all channel groups in the Semiconductor Module context that belong to an instrument of the type you specify in the Instrument Type Id parameter. For channels that do not belong to a channel group in the pin map, the Semiconductor Module creates a channel group with the same ID as the channel. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. Channel Lists — returns the channel lists for each of the channel group IDs. Each channel list is a comma-separated list of channels. |
| --- |

Parent topic:

Custom Instruments

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/advanced/custom-instruments/getallsessiondata-vi.html language=enus -->
## TOPIC 00005: Get All Session Data

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/advanced/custom-instruments/getallsessiondata-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/advanced/custom-instruments/getallsessiondata-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns all sessions in the Semiconductor Module context that belong to instruments of the type you specify in the Instrument Type Id parameter. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cstr.png Instrument Type

### Get All Session Data

Returns all sessions in the Semiconductor Module context that belong to instruments of the type you specify in the **Instrument Type Id** parameter.

[IMAGE alt='icon' src='getallsessiondata-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Instrument Type Id — specifies the type ID for the instrument in the pin map file. All custom instruments defined in the pin map specify an associated type ID. Typically, this type ID is an instrument driver name or other ID that is common for instruments that users program in a similar way. For custom instruments, you must pass the type ID associated with the instrument in the pin map file. For model-based instruments, pass the string you passed to the Set Custom Session VI to store sessions for the instruments. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Session Data — returns an array of session data set in the Semiconductor Module context. Channel Group Ids — returns the IDs of the channel groups on which Session Data was stored. For channels that do not belong to a channel group in the pin map, the Semiconductor Module creates a channel group with the same ID as the channel. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. Channel Lists — returns the channel lists for each of the channel group IDs. Each channel list is a comma-separated list of channels. |
| --- |

Parent topic:

Custom Instruments

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/advanced/custom-instruments/getsessiondata-vi.html language=enus -->
## TOPIC 00006: Get Session Data

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/advanced/custom-instruments/getsessiondata-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/advanced/custom-instruments/getsessiondata-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns all sessions in the Semiconductor Module context associated with the pins. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. c1ddaqmxscale.png Pins specifies the names of the pins or pin groups to translate to se

### Get Session Data

Returns all sessions in the Semiconductor Module context associated with the pins.

[IMAGE alt='icon' src='getsessiondata-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pins — specifies the names of the pins or pin groups to translate to session data, channel group IDs, and channel lists. Instrument Type Id — specifies the type ID for the instrument in the pin map file. All custom instruments defined in the pin map specify an associated type ID. Typically, this type ID is an instrument driver name or other ID that is common for instruments that users program in a similar way. For custom instruments, you must pass the type ID associated with the instrument in the pin map file. For model-based instruments, pass the string you passed to the Set Custom Session VI to store sessions for the instruments. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, and extract data from a set of measurements. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Session Data — returns an array of session data associated with channel group IDs. Channel Group Ids — returns the IDs of the channel groups that contain the channels connected to the pins. For channels that do not belong to a channel group in the pin map, the Semiconductor Module creates a channel group with the same ID as the channel. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. Channel Lists — returns the channel lists that correspond to the pins associated with session data and channel group IDs. Each channel list is a comma-separated list of channels. If any of the pins are connected to the same instrument channel for multiple sites, the channel appears only once in the list. |
| --- |

Parent topic:

Custom Instruments

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/advanced/custom-instruments/setsessiondata-vi.html language=enus -->
## TOPIC 00007: Set Session Data

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/advanced/custom-instruments/setsessiondata-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/advanced/custom-instruments/setsessiondata-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Associates a session with an instrument and channel group. icon Inputs/Outputs cstr.png Instrument Type Id specifies the type ID for the instrument in the pin map file. All custom instruments defined in the pin map specify an associated type ID. Typically, this type ID is an instrument driver name o

### Set Session Data

Associates a session with an instrument and channel group.

[IMAGE alt='icon' src='setsessiondata-vi.png']

#### Inputs/Outputs

| Instrument Type Id — specifies the type ID for the instrument in the pin map file. All custom instruments defined in the pin map specify an associated type ID. Typically, this type ID is an instrument driver name or other ID that is common for instruments that users program in a similar way. For custom instruments, you must pass the type ID associated with the instrument in the pin map file. For model-based instruments, you can pass any string that does not start with "ni" for the type ID. Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Instrument Name — is the instrument name in the pin map file for the corresponding session. Channel Group Id — is the channel group in the pin map file for the corresponding session. For channels that do not belong to a channel group in the pin map, the Semiconductor Module creates a channel group with the same ID as the channel. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Session Data — is the session for the corresponding instrument name and channel group ID. Use the variant data type to properly store different types of sessions. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Custom Instruments

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/advanced/filterpinsbyinstrumenttype-vi.html language=enus -->
## TOPIC 00008: Filter Pins

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/advanced/filterpinsbyinstrumenttype-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/advanced/filterpinsbyinstrumenttype-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Filters the pins by instrument type ID. Pass a list of all pins or pin groups to return the pins connected to instruments of the type you specify in the Instrument Type Id parameter. If no pins are connected to instruments of the type you specify in the Instrument Type Id parameter, this VI returns

### Filter Pins

Filters the pins by instrument type ID. Pass a list of all pins or pin groups to return the pins connected to instruments of the type you specify in the **Instrument Type Id** parameter. If no pins are connected to instruments of the type you specify in the **Instrument Type Id** parameter, this VI returns an empty array.

[IMAGE alt='icon' src='filterpinsbyinstrumenttype-vi.png']

#### Inputs/Outputs

| DAQmx Task Type — specifies the types of NI-DAQmx tasks for which you want to return DUT and system pins. For pins connected to a NI-DAQmx task, this parameter limits the returned pins to those connected to tasks of the specified type. The method uses this parameter only if the Instrument Type Id parameter is niDAQmx or an empty string. Pass an empty string to include all pins that match the Instrument Type Id parameter. Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pins — specifies an array of pins or pin groups to filter. The array must contain only pins or pin groups that are included in the Semiconductor Module context. Instrument Type Id — specifies the type of instrument for which you want to return DUT and system pins. For instruments that TSM natively supports, right-click the Instrument Type Id parameter, select Create Constant from the shortcut menu, and select the type of instrument you need. All custom instruments defined in the pin map specify an associated type ID. Typically, this type ID is an instrument driver name or other ID that is common for instruments that users program in a similar way. For custom instruments, you must pass the type ID associated with the instrument in the pin map file. For model-based instruments, pass the string you passed to the Set Custom Session VI to store sessions for the instruments. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Capability — limits the filtered pins to those connected to a channel that defines the capability you specify. Use this parameter to differentiate between pins in the same instrument with different capabilities, such as NI-HSDIO Dynamic DIO channels and PFI lines. If a pin is connected to channels in which the capability is defined only for a subset of sites, the VI returns an error. Pass an empty string to return all elements in the Pins parameter that match the instrument type ID you specify. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Filtered Pins — returns an array subset of pin names in the Pins parameter that are connected to an instrument of the filtered instrument type ID. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/advanced/filterrelaysbyinstrumenttype-vi.html language=enus -->
## TOPIC 00009: Filter Relays

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/advanced/filterrelaysbyinstrumenttype-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/advanced/filterrelaysbyinstrumenttype-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Filters the relays by instrument type ID. Pass a list of all relays or relay groups to return the relays connected to instruments of the type you specify in the Instrument Type Id parameter. If no relays are connected to instruments of the type you specify in the Instrument Type Id parameter, this V

### Filter Relays

Filters the relays by instrument type ID. Pass a list of all relays or relay groups to return the relays connected to instruments of the type you specify in the **Instrument Type Id** parameter. If no relays are connected to instruments of the type you specify in the **Instrument Type Id** parameter, this VI returns an empty array.

[IMAGE alt='icon' src='filterrelaysbyinstrumenttype-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Relays — specifies an array of relays or relay groups to filter. The array must contain only relays or relay groups that are included in the Semiconductor Module context. Instrument Type Id — specifies the type of instrument for which you want to return DUT and system relays. For instruments that TSM natively supports, right-click the Instrument Type Id parameter, select Create Constant from the shortcut menu, and select the type of instrument you need. Supported instrument types are niRelayDriver and niDAQmx. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Filtered Relays — returns an array subset of relay names in the relays parameter that are connected to an instrument of the filtered instrument type ID. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/advanced/getofflinemode-vi.html language=enus -->
## TOPIC 00010: Get Offline Mode

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/advanced/getofflinemode-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/advanced/getofflinemode-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the current status of the Offline Mode setting. Offline Mode allows you to develop, run, and debug test programs on a computer without access to NI instruments. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. c

### Get Offline Mode

Returns the current status of the Offline Mode setting. Offline Mode allows you to develop, run, and debug test programs on a computer without access to NI instruments.

[IMAGE alt='icon' src='getofflinemode-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Is Semiconductor Module In Offline Mode — returns a Boolean that indicates whether Semiconductor Module is currently in Offline Mode. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/advanced/getpinsinpingroup-s-vi.html language=enus -->
## TOPIC 00011: Get Pins In Pin Group(s)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/advanced/getpinsinpingroup-s-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/advanced/getpinsinpingroup-s-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a list of pins contained in the pin group or list of pin groups you specify. You must manually select the polymorphic instance you want to use. Select the single pin group or multiple pin groups polymorphic instance based on the number of pin groups you want to query. icon

### Get Pins In Pin Group(s)

Returns a list of pins contained in the pin group or list of pin groups you specify. You must manually select the polymorphic instance you want to use. Select the single pin group or multiple pin groups polymorphic instance based on the number of pin groups you want to query.

[IMAGE alt='icon' src='getpinsinpingroup-s-vi.png']

- [Get Pins In Pin Group](../../../../../menus/categories/ni-semiconductormodule/pinmap/advanced/getpinsinpingroup-vi.html) Returns a list of pins contained in the pin group you specify in the Pin Group parameter.
- [Get Pins In Pin Groups](../../../../../menus/categories/ni-semiconductormodule/pinmap/advanced/getpinsinpingroups-vi.html) Returns a list of pins contained in the pin groups you specify in the Pin Groups parameter.

Parent topic:

Advanced

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/advanced/getpinsinpingroup-vi.html language=enus -->
## TOPIC 00012: Get Pins In Pin Group

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/advanced/getpinsinpingroup-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/advanced/getpinsinpingroup-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a list of pins contained in the pin group you specify in the Pin Group parameter. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cdaqmxscale.png Pin Group specifies a pin group. The pin group must be included

### Get Pins In Pin Group

Returns a list of pins contained in the pin group you specify in the **Pin Group** parameter.

[IMAGE alt='icon' src='getpinsinpingroup-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin Group — specifies a pin group. The pin group must be included in the Semiconductor Module context. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Pins — returns an array of pin names that are contained in the Pin Group parameter. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Get Pins In Pin Group(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/advanced/getpinsinpingroups-vi.html language=enus -->
## TOPIC 00013: Get Pins In Pin Groups

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/advanced/getpinsinpingroups-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/advanced/getpinsinpingroups-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a list of pins contained in the pin groups you specify in the Pin Groups parameter. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. c1ddaqmxscale.png Pin Groups specifies an array of pin groups. The array must

### Get Pins In Pin Groups

Returns a list of pins contained in the pin groups you specify in the **Pin Groups** parameter.

[IMAGE alt='icon' src='getpinsinpingroups-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin Groups — specifies an array of pin groups. The array must contain only pin groups that are included in the Semiconductor Module context. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Pins — returns an array of pin names that are contained in the Pin Groups parameter. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Get Pins In Pin Group(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/advanced/getrelaysinrelaygroup-s-vi.html language=enus -->
## TOPIC 00014: Get Relays In Relay Group(s)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/advanced/getrelaysinrelaygroup-s-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/advanced/getrelaysinrelaygroup-s-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a list of relays contained in the relay group or list of relay groups you specify. You must manually select the polymorphic instance you want to use. Select the single relay group or multiple relay groups polymorphic instance based on the number of relay groups you want to query. icon

### Get Relays In Relay Group(s)

Returns a list of relays contained in the relay group or list of relay groups you specify. You must manually select the polymorphic instance you want to use. Select the single relay group or multiple relay groups polymorphic instance based on the number of relay groups you want to query.

[IMAGE alt='icon' src='getrelaysinrelaygroup-s-vi.png']

- [Get Relays In Relay Group](../../../../../menus/categories/ni-semiconductormodule/pinmap/advanced/getrelaysinrelaygroup-vi.html) Returns a list of relays contained in the relay group you specify in the Relay Group parameter.
- [Get Relays In Relay Groups](../../../../../menus/categories/ni-semiconductormodule/pinmap/advanced/getrelaysinrelaygroups-vi.html) Returns a list of relays contained in the relay groups you specify in the Relay Groups parameter.

Parent topic:

Advanced

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/advanced/getrelaysinrelaygroup-vi.html language=enus -->
## TOPIC 00015: Get Relays In Relay Group

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/advanced/getrelaysinrelaygroup-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/advanced/getrelaysinrelaygroup-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a list of relays contained in the relay group you specify in the Relay Group parameter. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cdaqmxscale.png Relay Group specifies a relay group. cerrcodeclst.png erro

### Get Relays In Relay Group

Returns a list of relays contained in the relay group you specify in the **Relay Group** parameter.

[IMAGE alt='icon' src='getrelaysinrelaygroup-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Relay Group — specifies a relay group. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Relays — returns an array of relay names that are contained in the Relay Group parameter. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Get Relays In Relay Group(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/advanced/getrelaysinrelaygroups-vi.html language=enus -->
## TOPIC 00016: Get Relays In Relay Groups

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/advanced/getrelaysinrelaygroups-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/advanced/getrelaysinrelaygroups-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a list of relays contained in the relay groups you specify in the Relay Groups parameter. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. c1ddaqmxscale.png Relay Groups specifies an array of relay groups. The a

### Get Relays In Relay Groups

Returns a list of relays contained in the relay groups you specify in the **Relay Groups** parameter.

[IMAGE alt='icon' src='getrelaysinrelaygroups-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Relay Groups — specifies an array of relay groups. The array must contain only relay groups that are included in the Semiconductor Module context. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Relays — returns an array of relay names that are contained in the Relay Groups parameter. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Get Relays In Relay Group(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/advanced/getsessionandchannelindexwithcontext-vi.html language=enus -->
## TOPIC 00017: Get Session And Channel Index

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/advanced/getsessionandchannelindexwithcontext-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/advanced/getsessionandchannelindexwithcontext-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the index of the channel group and channel that corresponds to a pin query. Use this VI to access an individual pin when you take a measurement across multiple instruments and pins. When you call a pin query VI, such as the Pins to NI-HSDIO Sessions VI, the VI returns an array of sessions an

### Get Session And Channel Index

Returns the index of the channel group and channel that corresponds to a pin query. Use this VI to access an individual pin when you take a measurement across multiple instruments and pins. When you call a pin query VI, such as the Pins to NI-HSDIO Sessions VI, the VI returns an array of sessions and a channel list. Use the Get Session and Channel Index VI to identify which session and which channel refers to a pin and site number you specify.

[IMAGE alt='icon' src='getsessionandchannelindexwithcontext-vi.png']

#### Inputs/Outputs

| Site Number — is the site number of the pin to obtain from the channel group and channel index in a previous pin query. To obtain a system pin, do not wire this input. Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, and extract data from a set of measurements. Pin — specifies the name of the pin to obtain from the channel group and channel index in a previous pin query. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context Out — returns the pin query context object unchanged. Session Index — returns the index of the session for a measurement taken on the pin and site number you specify. Channel Index — returns the index of the channel for a measurement taken on the pin and site number you specify. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/advanced/getsitenumbers-vi.html language=enus -->
## TOPIC 00018: Get Site Numbers

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/advanced/getsitenumbers-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/advanced/getsitenumbers-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the site numbers and number of sites in the Semiconductor Module context. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cerrcodeclst.png error in (no error) describes error conditions that occur before this V

### Get Site Numbers

Returns the site numbers and number of sites in the Semiconductor Module context.

[IMAGE alt='icon' src='getsitenumbers-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Site Numbers — returns an array of site numbers for the test sites in the Semiconductor Module context. The site numbers can be different each time a step executes because some sites might not be active. The site numbers are in numerical order. Number Of Sites — returns the number of elements in the Site Numbers parameter. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/advanced/getsitesemiconductormodulecontexts-vi.html language=enus -->
## TOPIC 00019: Get Site Semiconductor Module Contexts

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/advanced/getsitesemiconductormodulecontexts-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/advanced/getsitesemiconductormodulecontexts-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of Semiconductor Module context objects, each of which represents a single site. The size and ordering of the array match the size and ordering of the sites in the Semiconductor Module Context input. You must always close references to the Semiconductor Module contexts, even if you

### Get Site Semiconductor Module Contexts

Returns an array of Semiconductor Module context objects, each of which represents a single site. The size and ordering of the array match the size and ordering of the sites in the Semiconductor Module Context input. You must always close references to the Semiconductor Module contexts, even if you do not use them in your code module.

[IMAGE alt='icon' src='getsitesemiconductormodulecontexts-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Site Semiconductor Module Contexts — returns an array of Semiconductor Module context objects, each of which represents a single site. The size and ordering of the array match the size and ordering of the array returned by the GetSiteNumbers VI. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/advanced/perinstrumenttopersitedata-vi.html language=enus -->
## TOPIC 00020: Per-Instrument to Per-Site Data

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/advanced/perinstrumenttopersitedata-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/advanced/perinstrumenttopersitedata-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Transforms the measurement data from measurements obtained from an instrument session and arranges the data in the order of sites and pins in the Semiconductor Module context. Use this VI when you have raw measurement data from an instrument session that you need to manipulate in a site-specific way

### Per-Instrument to Per-Site Data

Transforms the measurement data from measurements obtained from an instrument session and arranges the data in the order of sites and pins in the Semiconductor Module context.

Use this VI when you have raw measurement data from an instrument session that you need to manipulate in a site-specific way. For example, if you need to perform an operation on the measurement data using per-site input data, this VI puts the measurement data for all pins into the same per-site order as the input data. Similarly, if you need to modify the data from a specific site before publishing, this VI puts the measurement data for the all pins into a per-site array that you can then index to retrieve the data for the specific site. The order of the per-site array matches the order of the **Site Numbers** output parameter of the Get Site Numbers VI.

[IMAGE alt='icon' src='perinstrumenttopersitedata-vi.png']

- [Per-Instrument To Per-Site Parametric Data (1D)](../../../../../menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/per-instrument-to-per-site-data-1d-array-double-vi.html) Converts measurement data from a 1D array of double measurements that is ordered by channels on a single instrument session into a 2D array that is arranged by the sites and pins in the Semiconductor Module Context.
- [Per-Instrument To Per-Site Pass/Fail Data (1D)](../../../../../menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/per-instrument-to-per-site-data-1d-array-bool-vi.html) Converts measurement data from a 1D array of Boolean measurements that is ordered by channels on a single instrument session into a 2D array that is arranged by the sites and pins in the Semiconductor Module Context.
- [Per-Instrument To Per-Site Parametric Data (2D)](../../../../../menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/per-instrument-to-per-site-data-2d-array-double-vi.html) Transforms measurement data from a 2D array of double measurements that is arranged by instrument sessions and channels into a 2D array that is arranged by the sites and pins in the Semiconductor Module Context.
- [Per-Instrument To Per-Site Pass/Fail Data (2D)](../../../../../menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/per-instrument-to-per-site-data-2d-array-bool-vi.html) Transforms measurement data from a 2D array of Boolean measurements that is arranged by instrument sessions and channels into a 2D array that is arranged by the sites and pins in the Semiconductor Module Context.

Parent topic:

Advanced

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/alarms/alarms-mnu.html language=enus -->
## TOPIC 00021: Alarms

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/alarms/alarms-mnu.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/alarms/alarms-mnu.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Alarms VIs to enable alarms, disable alarms, and to query for raised alarms on supported instruments. icon

### Alarms

Use the Alarms VIs to enable alarms, disable alarms, and to query for raised alarms on supported instruments.

[IMAGE alt='icon' src='alarms-mnu.png']

- [Get Alarm Behavior](../../../../../menus/categories/ni-semiconductormodule/pinmap/alarms/getalarmbehavior-vi.html) Returns the behavior associated with an alarm on the pin on each site in the Semiconductor Module context. Use the Override Alarm Behavior VI and Restore Alarm Behavior VI to change the behavior associated with alarms on pins.
- [Override Alarm Behavior](../../../../../menus/categories/ni-semiconductormodule/pinmap/alarms/overridealarmbehavior-vi.html) Changes the behavior associated with one or more alarms on pins for all sites in the Semiconductor Module context. The new behavior remains in effect until the Restore Alarm Behavior VI is called or until the DUT completes testing. TSM restores the alarm behavior for all alarms and pins to the value specified in the Alarms panel of the Test Program Editor before testing each DUT.
- [Restore Alarm Behavior](../../../../../menus/categories/ni-semiconductormodule/pinmap/alarms/restorealarmbehavior-vi.html) Restores the behavior associated with one or more alarms on pins to the values specified in the Alarms panel of the Test Program Editor for all sites in the Semiconductor Module context. TSM restores the alarm behavior for all alarms and pins to the value specified in the Alarms panel of the Test Program Editor before testing each DUT.
- [Enable Alarms](../../../../../menus/categories/ni-semiconductormodule/pinmap/alarms/enablealarms-vi.html) Enables the alarm(s) specified in the Alarm Names parameter for the instruments connected to each pin or pin group specified in the Pins parameter. This VI is typically used to re-enable alarms that have previously been disabled using the Disable Alarms VI. For this VI to enable alarms, alarms must also be enabled for the current test program in the Alarms Panel of the Test Program Editor. This VI enables alarms only if it is called the same number of times that the Disable Alarms VI was called.
- [Disable Alarms](../../../../../menus/categories/ni-semiconductormodule/pinmap/alarms/disablealarms-vi.html) Disables the alarm(s) specified in the Alarm Names parameter for the instruments connected to each pin or pin group specified in the Pins parameter. If an instrument enters a state that would generate an alarm while the alarm is disabled, the alarm condition will be ignored. Once alarms are disabled with this VI, they remain disabled until the instrument is reset, the lot completes, or the alarms are re-enabled using the Enable Alarms VI.
- [Query for Raised Alarms](../../../../../menus/categories/ni-semiconductormodule/pinmap/alarms/queryforraisedalarms-vi.html) Returns true if there are any raised alarms on the sites in the Semiconductor Module context. You can use this method in a custom probe to break execution if an alarm was raised.

Parent topic:

Code Module Development

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/alarms/disablealarms-vi.html language=enus -->
## TOPIC 00022: Disable Alarms

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/alarms/disablealarms-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/alarms/disablealarms-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables the alarm(s) specified in the Alarm Names parameter for the instruments connected to each pin or pin group specified in the Pins parameter. If an instrument enters a state that would generate an alarm while the alarm is disabled, the alarm condition will be ignored. Once alarms are disabled

### Disable Alarms

Disables the alarm(s) specified in the **Alarm Names** parameter for the instruments connected to each pin or pin group specified in the **Pins** parameter. If an instrument enters a state that would generate an alarm while the alarm is disabled, the alarm condition will be ignored. Once alarms are disabled with this VI, they remain disabled until the instrument is reset, the lot completes, or the alarms are re-enabled using the **Enable Alarms** VI.

[IMAGE alt='icon' src='disablealarms-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pins — specifies the pins or pin groups for which the alarms should be disabled. The pins must be included in the Semiconductor Module context. Alarm Names — specifies the alarm names to disable. For multiple alarms, use a comma to separate each alarm name. Right-click the Alarm Names parameter, select Create Constant from the shortcut menu, and select the alarm you need. To disable all alarms supported by the instruments connected to the pins, select the value All from the constant or pass an empty string. Leaving this terminal unwired specifies all supported alarms. This VI ignores invalid or unsupported alarm names and does not generate an error. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Alarms

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/alarms/enablealarms-vi.html language=enus -->
## TOPIC 00023: Enable Alarms

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/alarms/enablealarms-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/alarms/enablealarms-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the alarm(s) specified in the Alarm Names parameter for the instruments connected to each pin or pin group specified in the Pins parameter. This VI is typically used to re-enable alarms that have previously been disabled using the Disable Alarms VI. For this VI to enable alarms, alarms must

### Enable Alarms

Enables the alarm(s) specified in the **Alarm Names** parameter for the instruments connected to each pin or pin group specified in the **Pins** parameter. This VI is typically used to re-enable alarms that have previously been disabled using the **Disable Alarms** VI. For this VI to enable alarms, alarms must also be enabled for the current test program in the Alarms Panel of the Test Program Editor. This VI enables alarms only if it is called the same number of times that the **Disable Alarms** VI was called.

[IMAGE alt='icon' src='enablealarms-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pins — specifies the pins or pin groups for which alarms should be enabled. The pins must be included in the Semiconductor Module context. Alarm Names — specifies the alarm names to enable. For multiple alarms, use a comma to separate each alarm name. Right-click the Alarm Names parameter, select Create Constant from the shortcut menu, and select the alarm you need. To enable all alarms supported by the instruments connected to the pins, select the value All from the constant or pass an empty string. Leaving this terminal unwired specifies all supported alarms. This VI ignores invalid or unsupported alarm names and does not generate an error. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Alarms

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/alarms/getalarmbehavior-vi.html language=enus -->
## TOPIC 00024: Get Alarm Behavior

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/alarms/getalarmbehavior-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/alarms/getalarmbehavior-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the behavior associated with an alarm on the pin on each site in the Semiconductor Module context. Use the Override Alarm Behavior VI and Restore Alarm Behavior VI to change the behavior associated with alarms on pins. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid Act

### Get Alarm Behavior

Returns the behavior associated with an alarm on the pin on each site in the Semiconductor Module context. Use the **Override Alarm Behavior** VI and **Restore Alarm Behavior** VI to change the behavior associated with alarms on pins.

[IMAGE alt='icon' src='getalarmbehavior-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — specifies the pin for which to get alarm behavior. Alarm Name — specifies the name of the alarm for which to get alarm behavior. Right-click the Alarm Name parameter, select Create Constant from the shortcut menu, and select the alarm name from the list of alarms supported by TSM. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Alarm Behavior — returns the alarm behavior associated with the alarm on the pin for each site. The order of the array matches the site order in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Alarms

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/alarms/overridealarmbehavior-vi.html language=enus -->
## TOPIC 00025: Override Alarm Behavior

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/alarms/overridealarmbehavior-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/alarms/overridealarmbehavior-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Changes the behavior associated with one or more alarms on pins for all sites in the Semiconductor Module context. The new behavior remains in effect until the Restore Alarm Behavior VI is called or until the DUT completes testing. TSM restores the alarm behavior for all alarms and pins to the value

### Override Alarm Behavior

Changes the behavior associated with one or more alarms on pins for all sites in the Semiconductor Module context. The new behavior remains in effect until the **Restore Alarm Behavior** VI is called or until the DUT completes testing. TSM restores the alarm behavior for all alarms and pins to the value specified in the Alarms panel of the Test Program Editor before testing each DUT.

[IMAGE alt='icon' src='overridealarmbehavior-vi.png']

- [Override Alarm Behavior (Single Pin)](../../../../../menus/categories/ni-semiconductormodule/pinmap/alarms/overridealarmbehaviorsinglepin-vi.html) Changes the behavior associated with one or more alarms on pins for all sites in the Semiconductor Module context. The new behavior remains in effect until the Restore Alarm Behavior VI is called or until the DUT completes testing. TSM restores the alarm behavior for all alarms and pins to the value specified in the Alarms panel of the Test Program Editor before testing each DUT.
- [Override Alarm Behavior (Multiple Pins)](../../../../../menus/categories/ni-semiconductormodule/pinmap/alarms/overridealarmbehaviormultiplepins-vi.html) Changes the behavior associated with one or more alarms on pins for all sites in the Semiconductor Module context. The new behavior remains in effect until the Restore Alarm Behavior VI is called or until the DUT completes testing. TSM restores the alarm behavior for all alarms and pins to the value specified in the Alarms panel of the Test Program Editor before testing each DUT.

Parent topic:

Alarms

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/alarms/overridealarmbehaviormultiplepins-vi.html language=enus -->
## TOPIC 00026: Override Alarm Behavior (Multiple Pins)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/alarms/overridealarmbehaviormultiplepins-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/alarms/overridealarmbehaviormultiplepins-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Changes the behavior associated with one or more alarms on pins for all sites in the Semiconductor Module context. The new behavior remains in effect until the Restore Alarm Behavior VI is called or until the DUT completes testing. TSM restores the alarm behavior for all alarms and pins to the value

### Override Alarm Behavior (Multiple Pins)

Changes the behavior associated with one or more alarms on pins for all sites in the Semiconductor Module context. The new behavior remains in effect until the **Restore Alarm Behavior** VI is called or until the DUT completes testing. TSM restores the alarm behavior for all alarms and pins to the value specified in the Alarms panel of the Test Program Editor before testing each DUT.

[IMAGE alt='icon' src='overridealarmbehaviormultiplepins-vi.png']

#### Inputs/Outputs

| Alarm Behavior — the new behavior to associate with the alarms. Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pins — specifies the pins or pin groups for which to change alarm behavior. Alarm Names — a comma-separated list of alarms names for which to change alarm behavior. Right-click the Alarm Names parameter, select Create Constant from the shortcut menu, and select the alarm name from the list of alarms supported by TSM. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Override Alarm Behavior

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/alarms/overridealarmbehaviorsinglepin-vi.html language=enus -->
## TOPIC 00027: Override Alarm Behavior (Single Pin)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/alarms/overridealarmbehaviorsinglepin-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/alarms/overridealarmbehaviorsinglepin-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Changes the behavior associated with one or more alarms on pins for all sites in the Semiconductor Module context. The new behavior remains in effect until the Restore Alarm Behavior VI is called or until the DUT completes testing. TSM restores the alarm behavior for all alarms and pins to the value

### Override Alarm Behavior (Single Pin)

Changes the behavior associated with one or more alarms on pins for all sites in the Semiconductor Module context. The new behavior remains in effect until the **Restore Alarm Behavior** VI is called or until the DUT completes testing. TSM restores the alarm behavior for all alarms and pins to the value specified in the Alarms panel of the Test Program Editor before testing each DUT.

[IMAGE alt='icon' src='overridealarmbehaviorsinglepin-vi.png']

#### Inputs/Outputs

| Alarm Behavior — the new behavior to associate with the alarms. Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — specifies the pin or pin group for which to change alarm behavior. Alarm Names — a comma-separated list of alarms names for which to change alarm behavior. Right-click the Alarm Names parameter, select Create Constant from the shortcut menu, and select the alarm name from the list of alarms supported by TSM. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Override Alarm Behavior

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/alarms/queryforraisedalarms-vi.html language=enus -->
## TOPIC 00028: Query for Raised Alarms

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/alarms/queryforraisedalarms-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/alarms/queryforraisedalarms-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns true if there are any raised alarms on the sites in the Semiconductor Module context. You can use this method in a custom probe to break execution if an alarm was raised. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context

### Query for Raised Alarms

Returns true if there are any raised alarms on the sites in the Semiconductor Module context. You can use this method in a custom probe to break execution if an alarm was raised.

[IMAGE alt='icon' src='queryforraisedalarms-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Clear Alarms — specifies whether to clear the raised alarms after querying for them. Raised alarms that are not cleared will continue to be in the raised state until they are cleared. Clearing a raised alarm does not affect the behavior associated with the alarm. For example, if the specified alarm behavior is "Log", then the raised alarm will still be logged even if the raised alarm was cleared. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Alarms Are Raised? — returns true if there are raised alarms. Raised Alarm Details — returns a string containing the details of each raised alarm, including the alarm name, pin name and site number. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Alarms

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/alarms/restorealarmbehavior-vi.html language=enus -->
## TOPIC 00029: Restore Alarm Behavior

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/alarms/restorealarmbehavior-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/alarms/restorealarmbehavior-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Restores the behavior associated with one or more alarms on pins to the values specified in the Alarms panel of the Test Program Editor for all sites in the Semiconductor Module context. TSM restores the alarm behavior for all alarms and pins to the value specified in the Alarms panel of the Test Pr

### Restore Alarm Behavior

Restores the behavior associated with one or more alarms on pins to the values specified in the Alarms panel of the Test Program Editor for all sites in the Semiconductor Module context. TSM restores the alarm behavior for all alarms and pins to the value specified in the Alarms panel of the Test Program Editor before testing each DUT.

[IMAGE alt='icon' src='restorealarmbehavior-vi.png']

- [Restore Alarm Behavior (Single Pin)](../../../../../menus/categories/ni-semiconductormodule/pinmap/alarms/restorealarmbehaviorsinglepin-vi.html) Restores the behavior associated with one or more alarms on pins to the values specified in the Alarms panel of the Test Program Editor for all sites in the Semiconductor Module context. TSM restores the alarm behavior for all alarms and pins to the value specified in the Alarms panel of the Test Program Editor before testing each DUT.
- [Restore Alarm Behavior (Multiple Pins)](../../../../../menus/categories/ni-semiconductormodule/pinmap/alarms/restorealarmbehaviormultiplepins-vi.html) Restores the behavior associated with one or more alarms on pins to the values specified in the Alarms panel of the Test Program Editor for all sites in the Semiconductor Module context. TSM restores the alarm behavior for all alarms and pins to the value specified in the Alarms panel of the Test Program Editor before testing each DUT.

Parent topic:

Alarms

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/alarms/restorealarmbehaviormultiplepins-vi.html language=enus -->
## TOPIC 00030: Restore Alarm Behavior (Multiple Pins)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/alarms/restorealarmbehaviormultiplepins-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/alarms/restorealarmbehaviormultiplepins-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Restores the behavior associated with one or more alarms on pins to the values specified in the Alarms panel of the Test Program Editor for all sites in the Semiconductor Module context. TSM restores the alarm behavior for all alarms and pins to the value specified in the Alarms panel of the Test Pr

### Restore Alarm Behavior (Multiple Pins)

Restores the behavior associated with one or more alarms on pins to the values specified in the Alarms panel of the Test Program Editor for all sites in the Semiconductor Module context. TSM restores the alarm behavior for all alarms and pins to the value specified in the Alarms panel of the Test Program Editor before testing each DUT.

[IMAGE alt='icon' src='restorealarmbehaviormultiplepins-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pins — specifies the pins or pin groups for which to restore alarm behavior. Alarm Names — a comma-separated list of alarms names for which to restore alarm behavior. Right-click the Alarm Names parameter, select Create Constant from the shortcut menu, and select the alarm name from the list of alarms supported by TSM. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Restore Alarm Behavior

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/alarms/restorealarmbehaviorsinglepin-vi.html language=enus -->
## TOPIC 00031: Restore Alarm Behavior (Single Pin)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/alarms/restorealarmbehaviorsinglepin-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/alarms/restorealarmbehaviorsinglepin-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Restores the behavior associated with one or more alarms on pins to the values specified in the Alarms panel of the Test Program Editor for all sites in the Semiconductor Module context. TSM restores the alarm behavior for all alarms and pins to the value specified in the Alarms panel of the Test Pr

### Restore Alarm Behavior (Single Pin)

Restores the behavior associated with one or more alarms on pins to the values specified in the Alarms panel of the Test Program Editor for all sites in the Semiconductor Module context. TSM restores the alarm behavior for all alarms and pins to the value specified in the Alarms panel of the Test Program Editor before testing each DUT.

[IMAGE alt='icon' src='restorealarmbehaviorsinglepin-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — specifies the pin or pin group for which to restore alarm behavior. Alarm Names — a comma-separated list of alarms names for which to restore alarm behavior. Right-click the Alarm Names parameter, select Create Constant from the shortcut menu, and select the alarm name from the list of alarms supported by TSM. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Restore Alarm Behavior

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/daqmx/createmultisitedatafordaqmxanalogoutput-vi.html language=enus -->
## TOPIC 00032: Create Multisite Data for Analog Output

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/daqmx/createmultisitedatafordaqmxanalogoutput-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/daqmx/createmultisitedatafordaqmxanalogoutput-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Accepts per site/pin data and returns data for all channels in the tasks. Use this data with the DAQmx Write VI. You must manually select the polymorphic instance you want to use. Select the single pin or multiple pins polymorphic instances based on the number of pins the test is designed to test. S

### Create Multisite Data for Analog Output

Accepts per site/pin data and returns data for all channels in the tasks. Use this data with the DAQmx Write VI. You must manually select the polymorphic instance you want to use. Select the single pin or multiple pins polymorphic instances based on the number of pins the test is designed to test. Select the single data to all sites or per site data polymorphic instances based on the data being passed to the VI. If data exists for each pin but not for each site, use the single data to all sites polymorphic instances. If data exists for each pin and for each site, use the per site data polymorphic instances.

[IMAGE alt='icon' src='createmultisitedatafordaqmxanalogoutput-vi.png']

- [DAQmx Single Data To All Sites (1 Pin 1 Task)](../../../../../menus/categories/ni-semiconductormodule/pinmap/daqmx/samedatatoallsites-1pin1task-vi.html) Accepts data for the pin and returns data for all channels in the task. Use this data with the DAQmx Write VI.
- [DAQmx Single Data to All Sites (1 Pin M Tasks)](../../../../../menus/categories/ni-semiconductormodule/pinmap/daqmx/samedatatoallsites-1pinmtasks-vi.html) Accepts data for the pin and returns data for all channels in the tasks. Use this data with the DAQmx Write VI.
- [DAQmx Single Data To All Sites (N Pins 1 Task)](../../../../../menus/categories/ni-semiconductormodule/pinmap/daqmx/samedatatoallsites-npins1task-vi.html) Accepts data for the pins and returns data for all channels in the task. Use this data with the DAQmx Write VI.
- [DAQmx Single Data To All Sites (N Pins M Tasks)](../../../../../menus/categories/ni-semiconductormodule/pinmap/daqmx/samedatatoallsites-npinsmtasks-vi.html) Accepts data for the pins and returns data for all channels in the tasks. Use this data with the DAQmx Write VI.
- [DAQmx Per Site Data (1 Pin 1 Task)](../../../../../menus/categories/ni-semiconductormodule/pinmap/daqmx/differentdataforeachsite-1pin1task-vi.html) Accepts data for all sites in the Semiconductor Module Context that the pin is connected to and returns data for all channels in the task. Use this data with the DAQmx Write VI.
- [DAQmx Per Site Data (1 Pin M Tasks)](../../../../../menus/categories/ni-semiconductormodule/pinmap/daqmx/differentdataforeachsite-1pinmtasks-vi.html) Accepts data for all sites in the Semiconductor Module Context that the pin is connected to and returns data for all channels in the tasks. Use this data with the DAQmx Write VI.
- [DAQmx Per Site Data (N Pins 1 Task)](../../../../../menus/categories/ni-semiconductormodule/pinmap/daqmx/differentdataforeachsite-npins1task-vi.html) Accepts data for all sites in the Semiconductor Module Context that the pins are connected to and returns data for all channels in the task. Use this data with the DAQmx Write VI.
- [DAQmx Per Site Data (N Pins M Tasks)](../../../../../menus/categories/ni-semiconductormodule/pinmap/daqmx/differentdataforeachsite-npinsmtasks-vi.html) Accepts data for all sites in the Semiconductor Module Context that the pins are connected to and returns data for all channels in the tasks. Use this data with the DAQmx Write VI.

Parent topic:

DAQmx

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/daqmx/daqmx-mnu.html language=enus -->
## TOPIC 00033: DAQmx

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/daqmx/daqmx-mnu.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/daqmx/daqmx-mnu.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-DAQmx VIs to manage NI-DAQmx tasks. icon

### DAQmx

Use the NI-DAQmx VIs to manage NI-DAQmx tasks.

[IMAGE alt='icon' src='daqmx-mnu.png']

- [Get All NI-DAQmx Task Names](../../../../../menus/categories/ni-semiconductormodule/pinmap/daqmx/getallnidaqmxtasknames-vi.html) Returns the task names for all NI-DAQmx tasks of type Task Type in the Semiconductor Module context. You can use task names to create DAQmx tasks.
- [Set NI-DAQmx Task](../../../../../menus/categories/ni-semiconductormodule/pinmap/daqmx/setnidaqmxtask-vi.html) Associates an NI-DAQmx task with an NI-DAQmx task name defined in the pin map.
- [Get All NI-DAQmx Tasks](../../../../../menus/categories/ni-semiconductormodule/pinmap/daqmx/getallnidaqmxtasks-vi.html) Returns all NI-DAQmx tasks of type Task Type in the Semiconductor Module context. You can use tasks to perform NI-DAQmx operations.
- [Pin(s) to NI-DAQmx Task(s)](../../../../../menus/categories/ni-semiconductormodule/pinmap/daqmx/pin-s-tonidaqmxtask-s-vi.html) Returns the NI-DAQmx tasks and channel lists required to access one or more pins. You must manually select the polymorphic instance you want to use. Select the single pin or multiple pins polymorphic instance based on the number of pins the test is designed to test. Select the single task or multiple task polymorphic instance based on the number of tasks you expect the pin to be connected to in the pin map. Use the multiple task polymorphic instances to ensure that code modules work with any pin map. Use the single task instance only when you know the code module will never be used with a pin map that has more than one task connected to the specified pins.
- [Create Multisite Data for Analog Output](../../../../../menus/categories/ni-semiconductormodule/pinmap/daqmx/createmultisitedatafordaqmxanalogoutput-vi.html) Accepts per site/pin data and returns data for all channels in the tasks. Use this data with the DAQmx Write VI. You must manually select the polymorphic instance you want to use. Select the single pin or multiple pins polymorphic instances based on the number of pins the test is designed to test. Select the single data to all sites or per site data polymorphic instances based on the data being passed to the VI. If data exists for each pin but not for each site, use the single data to all sites polymorphic instances. If data exists for each pin and for each site, use the per site data polymorphic instances.

Parent topic:

Code Module Development

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/daqmx/differentdataforeachsite-1pin1task-vi.html language=enus -->
## TOPIC 00034: DAQmx Per Site Data (1 Pin 1 Task)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/daqmx/differentdataforeachsite-1pin1task-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/daqmx/differentdataforeachsite-1pin1task-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Accepts data for all sites in the Semiconductor Module Context that the pin is connected to and returns data for all channels in the task. Use this data with the DAQmx Write VI. icon Inputs/Outputs cNI__TestStand__SemiconductorModule_lvlib_SinglePinSingleSessionQueryContextlvclass.png Pin Query Cont

### DAQmx Per Site Data (1 Pin 1 Task)

Accepts data for all sites in the Semiconductor Module Context that the pin is connected to and returns data for all channels in the task. Use this data with the DAQmx Write VI.

[IMAGE alt='icon' src='differentdataforeachsite-1pin1task-vi.png']

#### Inputs/Outputs

| Pin Query Context — is the pin query context object a pin query returns. Site Pin Data — specifies per pin data for every site in the Semiconductor Module Context. Specify data such that rows of the data array correspond the sites while columns correspond to the samples to write to each pin. Ensure that the site order matches the order of sites the Get Site Numbers VI returns. Idle Value — specifies the data value to use for channels in the task that are not connected to sites in the Semiconductor Module context. Because the DAQmx Write VI always writes to all channels in a task, use the Idle Value to write a constant value to channels that are not in the pin query context. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context Out — returns the Pin Query Context parameter unchanged. Task Data — returns a 2D array of data, where the rows correspond to channels in the task and the columns corresponds to the data to write to each channel in the task. Pass this data to the NI-DAQmx Write VI. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Create Multisite Data for Analog Output

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/daqmx/differentdataforeachsite-1pinmtasks-vi.html language=enus -->
## TOPIC 00035: DAQmx Per Site Data (1 Pin M Tasks)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/daqmx/differentdataforeachsite-1pinmtasks-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/daqmx/differentdataforeachsite-1pinmtasks-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Accepts data for all sites in the Semiconductor Module Context that the pin is connected to and returns data for all channels in the tasks. Use this data with the DAQmx Write VI. icon Inputs/Outputs cNI__TestStand__SemiconductorModule_lvlib_SinglePinMultipleSessionQueryContextlvclass.png Pin Query C

### DAQmx Per Site Data (1 Pin M Tasks)

Accepts data for all sites in the Semiconductor Module Context that the pin is connected to and returns data for all channels in the tasks. Use this data with the DAQmx Write VI.

[IMAGE alt='icon' src='differentdataforeachsite-1pinmtasks-vi.png']

#### Inputs/Outputs

| Pin Query Context — is the pin query context object a pin query returns. Site Pin Data — specifies per pin data for every site in the Semiconductor Module Context. Specify data such that rows of the data array correspond the sites while columns correspond to the samples to write to each pin. Ensure that the site order matches the order of sites the Get Site Numbers VI returns. Idle Value — specifies the data value to use for channels in the task that are not connected to sites in the Semiconductor Module context. Because the DAQmx Write VI always writes to all channels in a task, use the Idle Value to write a constant value to channels that are not in the Semiconductor Module context. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context Out — returns the Pin Query Context parameter unchanged. Task Data — returns a 3D array of data, where the first dimension corresponds to NI-DAQmx Tasks and the second dimension corresponds to channels. Because each NI-DAQmx Task can have a different number of channels, use the Number of Channels per Task output to determine the number of elements in the second dimension to pass to the NI-DAQmx Write VI for each task. Number of Channels per Task — returns a 1D array of the number of channels for each NI-DAQmx Task, with the same size as the first dimension of the Task Data output. Use this output to determine the subset of the task data arrays to pass to the NI-DAQmx Write VI. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Create Multisite Data for Analog Output

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/daqmx/differentdataforeachsite-npins1task-vi.html language=enus -->
## TOPIC 00036: DAQmx Per Site Data (N Pins 1 Task)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/daqmx/differentdataforeachsite-npins1task-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/daqmx/differentdataforeachsite-npins1task-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Accepts data for all sites in the Semiconductor Module Context that the pins are connected to and returns data for all channels in the task. Use this data with the DAQmx Write VI. icon Inputs/Outputs cNI__TestStand__SemiconductorModule_lvlib_MultiplePinSingleSessionQueryContextlvclass.png Pin Query

### DAQmx Per Site Data (N Pins 1 Task)

Accepts data for all sites in the Semiconductor Module Context that the pins are connected to and returns data for all channels in the task. Use this data with the DAQmx Write VI.

[IMAGE alt='icon' src='differentdataforeachsite-npins1task-vi.png']

#### Inputs/Outputs

| Pin Query Context — is the pin query context a pin query returns. Site Pin Data — specifies per pin data for every pin in the pin query context and every site in the Semiconductor Module Context. Specify data in a 3D array such that pages of the data array correspond to sites, rows of the data array correspond to pins, and columns correspond to the samples to write to each pin. Ensure that the site order matches the order of sites the Get Site Numbers VI returns and that the pin order matches the order of the pins passed to the pin query. Idle Value — specifies the data value to use for channels in the task that are not connected to sites in the Semiconductor Module context. Because the DAQmx Write VI always writes to all channels in a task, use the Idle Value to write a constant value to channels that are not in the Semiconductor Module context. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context Out — returns the Pin Query Context parameter unchanged. Task Data — returns a 2D array of data, where the first dimension corresponds to channels in the task and the second dimension corresponds to the data to write to each channel in the task. Pass this data to the NI-DAQmx Write VI. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Create Multisite Data for Analog Output

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/daqmx/differentdataforeachsite-npinsmtasks-vi.html language=enus -->
## TOPIC 00037: DAQmx Per Site Data (N Pins M Tasks)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/daqmx/differentdataforeachsite-npinsmtasks-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/daqmx/differentdataforeachsite-npinsmtasks-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Accepts data for all sites in the Semiconductor Module Context that the pins are connected to and returns data for all channels in the tasks. Use this data with the DAQmx Write VI. icon Inputs/Outputs cNI__TestStand__SemiconductorModule_lvlib_MultiplePinMultipleSessionQueryContextlvclass.png Pin Que

### DAQmx Per Site Data (N Pins M Tasks)

Accepts data for all sites in the Semiconductor Module Context that the pins are connected to and returns data for all channels in the tasks. Use this data with the DAQmx Write VI.

[IMAGE alt='icon' src='differentdataforeachsite-npinsmtasks-vi.png']

#### Inputs/Outputs

| Pin Query Context — is the pin query context a pin query returns. Site Pin Data — specifies per pin data for every pin in the pin query context and every site in the Semiconductor Module Context. Specify data in a 3D array such that pages of the data array correspond to sites, rows of the data array correspond to pins, and columns correspond to the samples to write to each pin. Ensure that the site order matches the order of sites the Get Site Numbers VI returns and that the pin order matches the order of the pins passed to the pin query. Idle Value — specifies the data value to use for channels in the task that are not connected to sites in the Semiconductor Module context. Because the DAQmx Write VI always writes to all channels in a task, use the Idle Value to write a constant value to channels that are not in the Semiconductor Module context. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context Out — returns the Pin Query Context parameter unchanged. Task Data — returns a 3D array of data, where the first dimension corresponds to NI-DAQmx Tasks and the second dimension corresponds to channels. Because each NI-DAQmx Task can have a different number of channels, use the Number of Channels per Task output to determine the number of elements in the second dimension to pass to the NI-DAQmx Write VI for each task. Number of Channels per Task — returns a 1D array of the number of channels for each NI-DAQmx Task, with the same size as the first dimension of the Task Data output. Use this output to determine the subset of the task data arrays to pass to the NI-DAQmx Write VI. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Create Multisite Data for Analog Output

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/daqmx/getallnidaqmxtasknames-vi.html language=enus -->
## TOPIC 00038: Get All NI-DAQmx Task Names

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/daqmx/getallnidaqmxtasknames-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/daqmx/getallnidaqmxtasknames-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the task names for all NI-DAQmx tasks of type Task Type in the Semiconductor Module context. You can use task names to create DAQmx tasks. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cstr.png Task Type spec

### Get All NI-DAQmx Task Names

Returns the task names for all NI-DAQmx tasks of type **Task Type** in the Semiconductor Module context. You can use task names to create DAQmx tasks.

[IMAGE alt='icon' src='getallnidaqmxtasknames-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Task Type — specifies the type of NI-DAQmx tasks to return. Pass an empty string to obtain the names of all tasks regardless of task type. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Channel Lists — returns an array of strings that contains the physical channel names for all channels in the Semiconductor Module Context. Task Names — returns an array of the NI-DAQmx task names in the Semiconductor Module context with a type of Task Type. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/daqmx/getallnidaqmxtasks-vi.html language=enus -->
## TOPIC 00039: Get All NI-DAQmx Tasks

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/daqmx/getallnidaqmxtasks-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/daqmx/getallnidaqmxtasks-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns all NI-DAQmx tasks of type Task Type in the Semiconductor Module context. You can use tasks to perform NI-DAQmx operations. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cstr.png Task Type specifies the type

### Get All NI-DAQmx Tasks

Returns all NI-DAQmx tasks of type **Task Type** in the Semiconductor Module context. You can use tasks to perform NI-DAQmx operations.

[IMAGE alt='icon' src='getallnidaqmxtasks-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Task Type — specifies the type of tasks to return. All tasks defined in the pin map specify an associated task type. Pass an empty string to obtain the names of all tasks regardless of task type. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. DAQmx Tasks — returns an array of the NI-DAQmx tasks in the Semiconductor Module context with a type of Task Type. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/daqmx/pin-s-tonidaqmxtask-s-vi.html language=enus -->
## TOPIC 00040: Pin(s) to NI-DAQmx Task(s)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/daqmx/pin-s-tonidaqmxtask-s-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/daqmx/pin-s-tonidaqmxtask-s-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-DAQmx tasks and channel lists required to access one or more pins. You must manually select the polymorphic instance you want to use. Select the single pin or multiple pins polymorphic instance based on the number of pins the test is designed to test. Select the single task or multipl

### Pin(s) to NI-DAQmx Task(s)

Returns the NI-DAQmx tasks and channel lists required to access one or more pins. You must manually select the polymorphic instance you want to use. Select the single pin or multiple pins polymorphic instance based on the number of pins the test is designed to test. Select the single task or multiple task polymorphic instance based on the number of tasks you expect the pin to be connected to in the pin map. Use the multiple task polymorphic instances to ensure that code modules work with any pin map. Use the single task instance only when you know the code module will never be used with a pin map that has more than one task connected to the specified pins.

[IMAGE alt='icon' src='pin-s-tonidaqmxtask-s-vi.png']

- [Pins to NI-DAQmx Tasks](../../../../../menus/categories/ni-semiconductormodule/pinmap/daqmx/pinstonidaqmxtasks-vi.html) Returns the NI-DAQmx tasks and channel lists required to access the pins or pin groups.
- [Pin to NI-DAQmx Tasks](../../../../../menus/categories/ni-semiconductormodule/pinmap/daqmx/pintonidaqmxtasks-vi.html) Returns the NI-DAQmx tasks and channel lists required to access the pin or pin group.
- [Pins to NI-DAQmx Task](../../../../../menus/categories/ni-semiconductormodule/pinmap/daqmx/pinstonidaqmxtask-vi.html) Returns the NI-DAQmx task and channel list required to access the pins. If more than one task is required to access the pins, the VI returns an error.
- [Pin to NI-DAQmx Task](../../../../../menus/categories/ni-semiconductormodule/pinmap/daqmx/pintonidaqmxtask-vi.html) Returns the NI-DAQmx task and channel list required to access the pin. If more than one task is required to access the pin, the VI returns an error.

Parent topic:

DAQmx

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/daqmx/pinstonidaqmxtask-vi.html language=enus -->
## TOPIC 00041: Pins to NI-DAQmx Task

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/daqmx/pinstonidaqmxtask-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/daqmx/pinstonidaqmxtask-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-DAQmx task and channel list required to access the pins. If more than one task is required to access the pins, the VI returns an error. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. c1ddaqmxscale.png P

### Pins to NI-DAQmx Task

Returns the NI-DAQmx task and channel list required to access the pins. If more than one task is required to access the pins, the VI returns an error.

[IMAGE alt='icon' src='pinstonidaqmxtask-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pins — specifies the names of the pins or pin groups to translate to a task and a channel list. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context — is the pin query context object that tracks the task and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. DAQmx Task — returns the NI-DAQmx task connected to pins for all sites in the Semiconductor Module context. Channel List — returns the comma-separated channel list required to access the pins for all sites in the Semiconductor Module context. For an input task, connect this output to the ChannelsToRead property of a DAQmx Read property node to specify which channels to read. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Pin(s) to NI-DAQmx Task(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/daqmx/pinstonidaqmxtasks-vi.html language=enus -->
## TOPIC 00042: Pins to NI-DAQmx Tasks

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/daqmx/pinstonidaqmxtasks-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/daqmx/pinstonidaqmxtasks-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-DAQmx tasks and channel lists required to access the pins or pin groups. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. c1ddaqmxscale.png Pins specifies the names of the pins or pin groups to translate

### Pins to NI-DAQmx Tasks

Returns the NI-DAQmx tasks and channel lists required to access the pins or pin groups.

[IMAGE alt='icon' src='pinstonidaqmxtasks-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pins — specifies the names of the pins or pin groups to translate to tasks and channel lists. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context — is the pin query context object that tracks the task and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. DAQmx Tasks — returns the NI-DAQmx tasks connected to the pins for all sites in the Semiconductor Module context. Channel Lists — returns the comma-separated channel lists required to access the pins for all sites in the Semiconductor Module context. For input tasks, connect this output to the ChannelsToRead property of a DAQmx Read property node to specify which channels to read. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Pin(s) to NI-DAQmx Task(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/daqmx/pintonidaqmxtask-vi.html language=enus -->
## TOPIC 00043: Pin to NI-DAQmx Task

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/daqmx/pintonidaqmxtask-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/daqmx/pintonidaqmxtask-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-DAQmx task and channel list required to access the pin. If more than one task is required to access the pin, the VI returns an error. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cdaqmxscale.png Pin s

### Pin to NI-DAQmx Task

Returns the NI-DAQmx task and channel list required to access the pin. If more than one task is required to access the pin, the VI returns an error.

[IMAGE alt='icon' src='pintonidaqmxtask-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — specifies the name of the pin or pin group to translate to a task and channel list. If multiple tasks are required, the VI returns an error. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context — is the pin query context object that tracks the task and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. DAQmx Task — returns the NI-DAQmx task connected to the pin for all sites in the Semiconductor Module context. Channel List — returns the comma-separated channel list required to access the pins for all sites in the Semiconductor Module context. For an input task, connect this output to the ChannelsToRead property of a DAQmx Read property node to specify which channels to read. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Pin(s) to NI-DAQmx Task(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/daqmx/pintonidaqmxtasks-vi.html language=enus -->
## TOPIC 00044: Pin to NI-DAQmx Tasks

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/daqmx/pintonidaqmxtasks-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/daqmx/pintonidaqmxtasks-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-DAQmx tasks and channel lists required to access the pin or pin group. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cdaqmxscale.png Pin specifies the name of the pin or pin group to translate to tasks

### Pin to NI-DAQmx Tasks

Returns the NI-DAQmx tasks and channel lists required to access the pin or pin group.

[IMAGE alt='icon' src='pintonidaqmxtasks-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — specifies the name of the pin or pin group to translate to tasks and channel lists. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context — is the pin query context object that tracks the task and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. DAQmx Tasks — returns the NI-DAQmx tasks connected to the pin for all sites in the Semiconductor Module context. Channel Lists — returns the comma-separated channel lists required to access the pins for all sites in the Semiconductor Module context. For input tasks, connect this output to the ChannelsToRead property of a DAQmx Read property node to specify which channels to read. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Pin(s) to NI-DAQmx Task(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/daqmx/samedatatoallsites-1pin1task-vi.html language=enus -->
## TOPIC 00045: DAQmx Single Data To All Sites (1 Pin 1 Task)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/daqmx/samedatatoallsites-1pin1task-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/daqmx/samedatatoallsites-1pin1task-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Accepts data for the pin and returns data for all channels in the task. Use this data with the DAQmx Write VI. icon Inputs/Outputs cNI__TestStand__SemiconductorModule_lvlib_SinglePinSingleSessionQueryContextlvclass.png Pin Query Context is the pin query context a pin query returns. c1ddbl.png Pin Da

### DAQmx Single Data To All Sites (1 Pin 1 Task)

Accepts data for the pin and returns data for all channels in the task. Use this data with the DAQmx Write VI.

[IMAGE alt='icon' src='samedatatoallsites-1pin1task-vi.png']

#### Inputs/Outputs

| Pin Query Context — is the pin query context a pin query returns. Pin Data — specifies data for the pin in a pin query. Idle Value — specifies the data value to use for channels in the task that are not connected to sites in the Semiconductor Module context. Because the DAQmx Write VI always writes to all channels in a task, use the Idle Value to write a constant value to channels that are not in the Semiconductor Module context. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context Out — returns the Pin Query Context parameter unchanged. Task Data — returns a 2D array of data, where the rows correspond to channels in the task and the columns corresponds to the data to write to each channel in the task. Pass this data to the NI-DAQmx Write VI. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Create Multisite Data for Analog Output

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/daqmx/samedatatoallsites-1pinmtasks-vi.html language=enus -->
## TOPIC 00046: DAQmx Single Data to All Sites (1 Pin M Tasks)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/daqmx/samedatatoallsites-1pinmtasks-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/daqmx/samedatatoallsites-1pinmtasks-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Accepts data for the pin and returns data for all channels in the tasks. Use this data with the DAQmx Write VI. icon Inputs/Outputs cNI__TestStand__SemiconductorModule_lvlib_SinglePinMultipleSessionQueryContextlvclass.png Pin Query Context is the pin query context a pin query returns. c1ddbl.png Pin

### DAQmx Single Data to All Sites (1 Pin M Tasks)

Accepts data for the pin and returns data for all channels in the tasks. Use this data with the DAQmx Write VI.

[IMAGE alt='icon' src='samedatatoallsites-1pinmtasks-vi.png']

#### Inputs/Outputs

| Pin Query Context — is the pin query context a pin query returns. Pin Data — specifies data for the pin in a pin query. Idle Value — specifies the data value to use for channels in the task that are not connected to sites in the Semiconductor Module context. Because the DAQmx Write VI always writes to all channels in a task, use the Idle Value to write a constant value to channels that are not in the Semiconductor Module context. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context Out — returns the Pin Query Context parameter unchanged. Task Data — returns a 3D array of data, where the first dimension corresponds to NI-DAQmx Tasks and the second dimension corresponds to channels. Because each NI-DAQmx Task can have a different number of channels, use the Number of Channels per Task output to determine the number of elements in the second dimension to pass to the NI-DAQmx Write VI for each task. Number of Channels per Task — returns a 1D array of the number of channels for each NI-DAQmx Task, with the same size as the first dimension of the Task Data output. Use this output to determine the subset of the task data arrays to pass to the NI-DAQmx Write VI. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Create Multisite Data for Analog Output

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/daqmx/samedatatoallsites-npins1task-vi.html language=enus -->
## TOPIC 00047: DAQmx Single Data To All Sites (N Pins 1 Task)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/daqmx/samedatatoallsites-npins1task-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/daqmx/samedatatoallsites-npins1task-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Accepts data for the pins and returns data for all channels in the task. Use this data with the DAQmx Write VI. icon Inputs/Outputs cNI__TestStand__SemiconductorModule_lvlib_MultiplePinSingleSessionQueryContextlvclass.png Pin Query Context is the pin query context object a pin query returns. c2ddbl.

### DAQmx Single Data To All Sites (N Pins 1 Task)

Accepts data for the pins and returns data for all channels in the task. Use this data with the DAQmx Write VI.

[IMAGE alt='icon' src='samedatatoallsites-npins1task-vi.png']

#### Inputs/Outputs

| Pin Query Context — is the pin query context object a pin query returns. Pin Data — specifies data for each pin in a pin query. Ensure that the pin order matches the order of the pins passed to the pin query. Idle Value — specifies the data value to use for channels in the task that are not connected to sites in the Semiconductor Module context. Because the DAQmx Write VI always writes to all channels in a task, use the Idle Value to write a constant value to channels that are not in the Semiconductor Module context. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context Out — returns the Pin Query Context parameter unchanged. Task Data — returns a 2D array of data, where the rows correspond to channels and the columns corresponds to the data to write to each channel in the task. Pass this data to the NI-DAQmx Write VI. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Create Multisite Data for Analog Output

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/daqmx/samedatatoallsites-npinsmtasks-vi.html language=enus -->
## TOPIC 00048: DAQmx Single Data To All Sites (N Pins M Tasks)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/daqmx/samedatatoallsites-npinsmtasks-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/daqmx/samedatatoallsites-npinsmtasks-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Accepts data for the pins and returns data for all channels in the tasks. Use this data with the DAQmx Write VI. icon Inputs/Outputs cNI__TestStand__SemiconductorModule_lvlib_MultiplePinMultipleSessionQueryContextlvclass.png Pin Query Context is the pin query context object a pin query returns. c2dd

### DAQmx Single Data To All Sites (N Pins M Tasks)

Accepts data for the pins and returns data for all channels in the tasks. Use this data with the DAQmx Write VI.

[IMAGE alt='icon' src='samedatatoallsites-npinsmtasks-vi.png']

#### Inputs/Outputs

| Pin Query Context — is the pin query context object a pin query returns. Pin Data — specifies data for each pin in a pin query. Ensure that the pin order matches the order of the pins passed to the pin query. Idle Value — specifies the data value to use for channels in the task that are not connected to sites in the Semiconductor Module context. Because the DAQmx Write VI always writes to all channels in a task, use the Idle Value to write a constant value to channels that are not in the Semiconductor Module context. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context Out — returns the Pin Query Context parameter unchanged. Task Data — returns a 3D array of data, where the first dimension corresponds to NI-DAQmx Tasks and the second dimension corresponds to channels. Because each NI-DAQmx Task can have a different number of channels, use the Number of Channels per Task output to determine the number of elements in the second dimension to pass to the NI-DAQmx Write VI for each task. Number of Channels per Task — returns a 1D array of the number of channels for each NI-DAQmx Task, with the same size as the first dimension of the Task Data output. Use this output to determine the subset of the task data arrays to pass to the NI-DAQmx Write VI. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Create Multisite Data for Analog Output

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/daqmx/setnidaqmxtask-vi.html language=enus -->
## TOPIC 00049: Set NI-DAQmx Task

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/daqmx/setnidaqmxtask-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/daqmx/setnidaqmxtask-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Associates an NI-DAQmx task with an NI-DAQmx task name defined in the pin map. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cgenclassrntag.png DAQmx Task specifies the NI-DAQmx task for the corresponding task name.

### Set NI-DAQmx Task

Associates an NI-DAQmx task with an NI-DAQmx task name defined in the pin map.

[IMAGE alt='icon' src='setnidaqmxtask-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. DAQmx Task — specifies the NI-DAQmx task for the corresponding task name. Task Name — is the task name in the pin map file for the corresponding task. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

DAQmx

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/dc-power/getallnidcpowerresourcestrings-vi.html language=enus -->
## TOPIC 00050: Get All NI-DCPower Resource Strings

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/dc-power/getallnidcpowerresourcestrings-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/dc-power/getallnidcpowerresourcestrings-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the resource strings associated with each channel group in the ISemiconductorModuleContext. A resource string is a comma-separated list of NI-DCPower resources associated with the NI-DCPower channel group, each resource is defined by <instrument>/<channel>. You can use the re

### Get All NI-DCPower Resource Strings

Returns the resource strings associated with each channel group in the ISemiconductorModuleContext. A resource string is a comma-separated list of NI-DCPower resources associated with the NI-DCPower channel group, each resource is defined by &#60;instrument&#62;/&#60;channel&#62;. You can use the resource strings to open driver sessions. All resources within the same resource string will be controlled by the same session.

[IMAGE alt='icon' src='getallnidcpowerresourcestrings-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Resource Strings — returns an array of the NI-DCPower Resource Strings. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

NI-DCPower

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/dc-power/getallnidcpowersessions-vi.html language=enus -->
## TOPIC 00051: Get All NI-DCPower Sessions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/dc-power/getallnidcpowersessions-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/dc-power/getallnidcpowersessions-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns all NI-DCPower instrument sessions in the Semiconductor Module context. You can use instrument sessions to close driver sessions. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cerrcodeclst.png error in (no er

### Get All NI-DCPower Sessions

Returns all NI-DCPower instrument sessions in the Semiconductor Module context. You can use instrument sessions to close driver sessions.

[IMAGE alt='icon' src='getallnidcpowersessions-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Sessions — returns the instrument sessions for all NI-DCPower instruments in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

NI-DCPower

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/dc-power/nidcpower-mnu.html language=enus -->
## TOPIC 00052: NI-DCPower

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/dc-power/nidcpower-mnu.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/dc-power/nidcpower-mnu.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-DCPower VIs to manage NI-DCPower instruments and sessions. icon

### NI-DCPower

Use the NI-DCPower VIs to manage NI-DCPower instruments and sessions.

[IMAGE alt='icon' src='nidcpower-mnu.png']

- [Get All NI-DCPower Resource Strings](../../../../../menus/categories/ni-semiconductormodule/pinmap/dc-power/getallnidcpowerresourcestrings-vi.html) Returns the resource strings associated with each channel group in the ISemiconductorModuleContext. A resource string is a comma-separated list of NI-DCPower resources associated with the NI-DCPower channel group, each resource is defined by <instrument>/<channel>. You can use the resource strings to open driver sessions. All resources within the same resource string will be controlled by the same session.
- [Set NI-DCPower Session](../../../../../menus/categories/ni-semiconductormodule/pinmap/dc-power/setnidcpowersessionwithresourcestring-vi.html) Associates an NI-DCPower session with all resources of an NI-DCPower resource string.
- [Get All NI-DCPower Sessions](../../../../../menus/categories/ni-semiconductormodule/pinmap/dc-power/getallnidcpowersessions-vi.html) Returns all NI-DCPower instrument sessions in the Semiconductor Module context. You can use instrument sessions to close driver sessions.
- [Pin(s) to NI-DCPower Session(s)](../../../../../menus/categories/ni-semiconductormodule/pinmap/dc-power/pin-s-tonidcpowersession-s-vi.html) Returns the NI-DCPower instrument sessions and channel strings required to access one or more pins. You must manually select the polymorphic instance you want to use. Select the single pin or multiple pins polymorphic instance based on the number of pins the test is designed to test. Select the single instrument or multiple instrument polymorphic instance based on the number of instruments you expect the pin to be connected to in the pin map. Use the multiple instrument polymorphic instances to ensure that code modules work with any pin map. Use the single instrument instance only when you know the code module will never be used with a pin map that has more than one instrument connected to the specified pins.

Parent topic:

Code Module Development

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/dc-power/pin-s-tonidcpowersession-s-vi.html language=enus -->
## TOPIC 00053: Pin(s) to NI-DCPower Session(s)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/dc-power/pin-s-tonidcpowersession-s-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/dc-power/pin-s-tonidcpowersession-s-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-DCPower instrument sessions and channel strings required to access one or more pins. You must manually select the polymorphic instance you want to use. Select the single pin or multiple pins polymorphic instance based on the number of pins the test is designed to test. Select the sing

### Pin(s) to NI-DCPower Session(s)

Returns the NI-DCPower instrument sessions and channel strings required to access one or more pins. You must manually select the polymorphic instance you want to use. Select the single pin or multiple pins polymorphic instance based on the number of pins the test is designed to test. Select the single instrument or multiple instrument polymorphic instance based on the number of instruments you expect the pin to be connected to in the pin map. Use the multiple instrument polymorphic instances to ensure that code modules work with any pin map. Use the single instrument instance only when you know the code module will never be used with a pin map that has more than one instrument connected to the specified pins.

[IMAGE alt='icon' src='pin-s-tonidcpowersession-s-vi.png']

- [Pins to NI-DCPower Sessions](../../../../../menus/categories/ni-semiconductormodule/pinmap/dc-power/pinstonidcpowersessions-vi.html) Returns the NI-DCPower sessions and channel strings required to access the pins.
- [Pin to NI-DCPower Sessions](../../../../../menus/categories/ni-semiconductormodule/pinmap/dc-power/pintonidcpowersessions-vi.html) Returns the NI-DCPower sessions and channel strings required to access the pin.
- [Pin to NI-DCPower Session](../../../../../menus/categories/ni-semiconductormodule/pinmap/dc-power/pintonidcpowersession-vi.html) Returns the NI-DCPower session and channel string required to access the pin. If more than one session is required to access the pin, the VI returns an error.
- [Pins to NI-DCPower Session](../../../../../menus/categories/ni-semiconductormodule/pinmap/dc-power/pinstonidcpowersession-vi.html) Returns the NI-DCPower session and channel string required to access the pins. If multiple sessions are required, the VI returns an error.

Parent topic:

NI-DCPower

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/dc-power/pinstonidcpowersession-vi.html language=enus -->
## TOPIC 00054: Pins to NI-DCPower Session

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/dc-power/pinstonidcpowersession-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/dc-power/pinstonidcpowersession-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-DCPower session and channel string required to access the pins. If multiple sessions are required, the VI returns an error. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. c1ddaqmxscale.png Pins specifie

### Pins to NI-DCPower Session

Returns the NI-DCPower session and channel string required to access the pins. If multiple sessions are required, the VI returns an error.

[IMAGE alt='icon' src='pinstonidcpowersession-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pins — specifies the names of the pins or pin groups to translate to an instrument session and channel resource name list. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Channel String — returns the channel string for the NI-DCPower instrument session required to access the pins for all sites in the Semiconductor Module Context. The channel string is a comma-separated list of resources, where each resource is defined as <instrument>/<channel>. Instrument Session — returns the NI-DCPower instrument session for the instruments and channels connected to Pins for all sites in the Semiconductor Module Context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Pin(s) to NI-DCPower Session(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/dc-power/pinstonidcpowersessions-vi.html language=enus -->
## TOPIC 00055: Pins to NI-DCPower Sessions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/dc-power/pinstonidcpowersessions-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/dc-power/pinstonidcpowersessions-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-DCPower sessions and channel strings required to access the pins. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. c1ddaqmxscale.png Pins specifies the names of the pins or pin groups to translate to Inst

### Pins to NI-DCPower Sessions

Returns the NI-DCPower sessions and channel strings required to access the pins.

[IMAGE alt='icon' src='pinstonidcpowersessions-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pins — specifies the names of the pins or pin groups to translate to Instrument Sessions and Channel Strings. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Channel Strings — returns the channel string for each instrument session required to access the Pins for all sites in the Semiconductor Module Context. Each channel string is a comma-separated list of channels, where each channel is defined as <instrument>/<channel>. Instrument Sessions — returns the NI-DCPower sessions for the instruments and channels connected to Pins for all sites in the Semiconductor Module Context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Pin(s) to NI-DCPower Session(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/dc-power/pintonidcpowersession-vi.html language=enus -->
## TOPIC 00056: Pin to NI-DCPower Session

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/dc-power/pintonidcpowersession-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/dc-power/pintonidcpowersession-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-DCPower session and channel string required to access the pin. If more than one session is required to access the pin, the VI returns an error. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cdaqmxscale

### Pin to NI-DCPower Session

Returns the NI-DCPower session and channel string required to access the pin. If more than one session is required to access the pin, the VI returns an error.

[IMAGE alt='icon' src='pintonidcpowersession-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — specifies the name of the pin to translate to an Instrument Session and Channel String. If multiple sessions are required, the VI returns an error. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Channel String — returns the channel string for the instrument Session required to access the Pin for all sites in the Semiconductor Module Context. The channel string is a comma-separated list of channels, where each channel is defined as <instrument>/<channel>. Instrument Session — returns the NI-DCPower instrument session for the instrument and channel connected to Pin. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Pin(s) to NI-DCPower Session(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/dc-power/pintonidcpowersessions-vi.html language=enus -->
## TOPIC 00057: Pin to NI-DCPower Sessions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/dc-power/pintonidcpowersessions-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/dc-power/pintonidcpowersessions-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-DCPower sessions and channel strings required to access the pin. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cdaqmxscale.png Pin specifies the name of the pin or pin group to translate to Instrument

### Pin to NI-DCPower Sessions

Returns the NI-DCPower sessions and channel strings required to access the pin.

[IMAGE alt='icon' src='pintonidcpowersessions-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — specifies the name of the pin or pin group to translate to Instrument Sessions and Channel Strings. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Channel Strings — returns the channel string for the NI-DCPower session required to access the Pin for all sites in the Semiconductor Module context. Each channel string is a comma-separated list of channels, where each channel is defined as <instrument>/<channel>. Instrument Sessions — returns the NI-DCPower sessions for the instruments and channels connected to the Pin for all sites in the Semiconductor Module Context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Pin(s) to NI-DCPower Session(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/dc-power/setnidcpowersessionwithresourcestring-vi.html language=enus -->
## TOPIC 00058: Set NI-DCPower Session

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/dc-power/setnidcpowersessionwithresourcestring-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/dc-power/setnidcpowersessionwithresourcestring-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Associates an NI-DCPower session with all resources of an NI-DCPower resource string. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cstr.png Resource String specifies the Resource String associated with the the corre

### Set NI-DCPower Session

Associates an NI-DCPower session with all resources of an NI-DCPower resource string.

[IMAGE alt='icon' src='setnidcpowersessionwithresourcestring-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Resource String — specifies the Resource String associated with the the corresponding Instrument Session, the resource string is a comma-separated list of resources where each resource is defined as <instrument>/<channel>. Instrument Session — specifies the NI-DCPower session for the corresponding Resource String. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

NI-DCPower

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/digital-pattern/getallnidigitalpatterninstrumentnames-vi.html language=enus -->
## TOPIC 00059: Get All NI-Digital Pattern Instrument Names

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/digital-pattern/getallnidigitalpatterninstrumentnames-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/digital-pattern/getallnidigitalpatterninstrumentnames-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the instrument names and comma-separated lists of instrument names that belong to the same group for all NI-Digital Pattern instruments in the Semiconductor Module context. You can use instrument names and comma-separated lists of instrument names to open driver sessions. This VI is availabl

### Get All NI-Digital Pattern Instrument Names

Returns the instrument names and comma-separated lists of instrument names that belong to the same group for all NI-Digital Pattern instruments in the Semiconductor Module context. You can use instrument names and comma-separated lists of instrument names to open driver sessions. This VI is available only in 64-bit LabVIEW.

[IMAGE alt='icon' src='getallnidigitalpatterninstrumentnames-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Names — returns an array of instrument names and comma-separated lists of instrument names that belong to the same group for all NI-Digital Pattern instruments in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

NI-Digital Pattern

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/digital-pattern/getallnidigitalpatternsessions-vi.html language=enus -->
## TOPIC 00060: Get All NI-Digital Pattern Sessions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/digital-pattern/getallnidigitalpatternsessions-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/digital-pattern/getallnidigitalpatternsessions-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns all NI-Digital Pattern instrument sessions in the Semiconductor Module context. You can use instrument sessions to close driver sessions. This VI is available only in 64-bit LabVIEW. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Mo

### Get All NI-Digital Pattern Sessions

Returns all NI-Digital Pattern instrument sessions in the Semiconductor Module context. You can use instrument sessions to close driver sessions. This VI is available only in 64-bit LabVIEW.

[IMAGE alt='icon' src='getallnidigitalpatternsessions-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Sessions — returns the instrument sessions for all NI-Digital Pattern instruments in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

NI-Digital Pattern

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/digital-pattern/instrument-setup/getdigitalpatternprojectcapturewaveformfilepaths-vi.html language=enus -->
## TOPIC 00061: Get Digital Pattern Project Capture Waveform File Paths

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/digital-pattern/instrument-setup/getdigitalpatternprojectcapturewaveformfilepaths-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/digital-pattern/instrument-setup/getdigitalpatternprojectcapturewaveformfilepaths-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the file paths of all capture waveform files listed in the digital pattern project associated with the test program. This VI is available only in 64-bit LabVIEW. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object.

### Get Digital Pattern Project Capture Waveform File Paths

Returns the file paths of all capture waveform files listed in the digital pattern project associated with the test program. This VI is available only in 64-bit LabVIEW.

[IMAGE alt='icon' src='getdigitalpatternprojectcapturewaveformfilepaths-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Capture Waveform File Paths — returns the absolute paths of capture waveform files listed in the digital pattern project associated with the test program. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Setup

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/digital-pattern/instrument-setup/getdigitalpatternprojectpatternfilepaths-vi.html language=enus -->
## TOPIC 00062: Get Digital Pattern Project Pattern File Paths

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/digital-pattern/instrument-setup/getdigitalpatternprojectpatternfilepaths-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/digital-pattern/instrument-setup/getdigitalpatternprojectpatternfilepaths-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the file paths of all pattern files listed in the digital pattern project associated with the test program. This VI is available only in 64-bit LabVIEW. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cerrcodec

### Get Digital Pattern Project Pattern File Paths

Returns the file paths of all pattern files listed in the digital pattern project associated with the test program. This VI is available only in 64-bit LabVIEW.

[IMAGE alt='icon' src='getdigitalpatternprojectpatternfilepaths-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Pattern File Paths — returns the absolute paths of pattern files listed in the digital pattern project associated with the test program. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Setup

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/digital-pattern/instrument-setup/getdigitalpatternprojectsourcewaveformfilepaths-vi.html language=enus -->
## TOPIC 00063: Get Digital Pattern Project Source Waveform File Paths

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/digital-pattern/instrument-setup/getdigitalpatternprojectsourcewaveformfilepaths-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/digital-pattern/instrument-setup/getdigitalpatternprojectsourcewaveformfilepaths-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the file paths of all source waveform files listed in the digital pattern project associated with the test program. This VI is available only in 64-bit LabVIEW. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. c

### Get Digital Pattern Project Source Waveform File Paths

Returns the file paths of all source waveform files listed in the digital pattern project associated with the test program. This VI is available only in 64-bit LabVIEW.

[IMAGE alt='icon' src='getdigitalpatternprojectsourcewaveformfilepaths-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Source Waveform File Paths — returns the absolute paths of source waveform files listed in the digital pattern project associated with the test program. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Setup

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/digital-pattern/instrument-setup/getdigitalpatternprojectspecificationslevelsandtimingfilepaths-vi.html language=enus -->
## TOPIC 00064: Get Digital Pattern Project Specifications, Levels, and Timing File Paths

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/digital-pattern/instrument-setup/getdigitalpatternprojectspecificationslevelsandtimingfilepaths-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/digital-pattern/instrument-setup/getdigitalpatternprojectspecificationslevelsandtimingfilepaths-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the file paths of all specifications files, levels files, and timing files listed in the digital pattern project associated with the test program. This VI is available only in 64-bit LabVIEW. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semicon

### Get Digital Pattern Project Specifications, Levels, and Timing File Paths

Returns the file paths of all specifications files, levels files, and timing files listed in the digital pattern project associated with the test program. This VI is available only in 64-bit LabVIEW.

[IMAGE alt='icon' src='getdigitalpatternprojectspecificationslevelsandtimingfilepaths-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Specifications File Paths — returns the absolute paths of specifications files listed in the digital pattern project associated with the test program. Levels File Paths — returns the absolute paths of levels files listed in the digital pattern project associated with the test program. Timing File Paths — returns the absolute paths of timing files listed in the digital pattern project associated with the test program. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Setup

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/digital-pattern/instrument-setup/getpinmapfilepath-vi.html language=enus -->
## TOPIC 00065: Get Pin Map File Path

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/digital-pattern/instrument-setup/getpinmapfilepath-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/digital-pattern/instrument-setup/getpinmapfilepath-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the file path of the pin map file associated with the test program. This VI is available only in 64-bit LabVIEW. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cerrcodeclst.png error in (no error) describes er

### Get Pin Map File Path

Returns the file path of the pin map file associated with the test program. This VI is available only in 64-bit LabVIEW.

[IMAGE alt='icon' src='getpinmapfilepath-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Pin Map File Path — returns the absolute path of the pin map file associated with the test program. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Setup

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/digital-pattern/instrument-setup/instrumentsetup-mnu.html language=enus -->
## TOPIC 00066: Setup

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/digital-pattern/instrument-setup/instrumentsetup-mnu.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/digital-pattern/instrument-setup/instrumentsetup-mnu.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Setup VIs to obtain file paths for digital pattern project files. icon

### Setup

Use the Setup VIs to obtain file paths for digital pattern project files.

[IMAGE alt='icon' src='instrumentsetup-mnu.png']

- [Get Pin Map File Path](../../../../../../menus/categories/ni-semiconductormodule/pinmap/digital-pattern/instrument-setup/getpinmapfilepath-vi.html) Returns the file path of the pin map file associated with the test program. This VI is available only in 64-bit LabVIEW.
- [Get Digital Pattern Project Specifications, Levels, and Timing File Paths](../../../../../../menus/categories/ni-semiconductormodule/pinmap/digital-pattern/instrument-setup/getdigitalpatternprojectspecificationslevelsandtimingfilepaths-vi.html) Returns the file paths of all specifications files, levels files, and timing files listed in the digital pattern project associated with the test program. This VI is available only in 64-bit LabVIEW.
- [Get Digital Pattern Project Pattern File Paths](../../../../../../menus/categories/ni-semiconductormodule/pinmap/digital-pattern/instrument-setup/getdigitalpatternprojectpatternfilepaths-vi.html) Returns the file paths of all pattern files listed in the digital pattern project associated with the test program. This VI is available only in 64-bit LabVIEW.
- [Get Digital Pattern Project Source Waveform File Paths](../../../../../../menus/categories/ni-semiconductormodule/pinmap/digital-pattern/instrument-setup/getdigitalpatternprojectsourcewaveformfilepaths-vi.html) Returns the file paths of all source waveform files listed in the digital pattern project associated with the test program. This VI is available only in 64-bit LabVIEW.
- [Get Digital Pattern Project Capture Waveform File Paths](../../../../../../menus/categories/ni-semiconductormodule/pinmap/digital-pattern/instrument-setup/getdigitalpatternprojectcapturewaveformfilepaths-vi.html) Returns the file paths of all capture waveform files listed in the digital pattern project associated with the test program. This VI is available only in 64-bit LabVIEW.

Parent topic:

NI-Digital Pattern

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/digital-pattern/nidigitalpattern-mnu.html language=enus -->
## TOPIC 00067: NI-Digital Pattern

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/digital-pattern/nidigitalpattern-mnu.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/digital-pattern/nidigitalpattern-mnu.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-Digital Pattern VIs to manage NI-Digital Pattern instruments and sessions, to manage NI-Digital Pattern waveform data, and to access digital pattern project files. icon

### NI-Digital Pattern

Use the NI-Digital Pattern VIs to manage NI-Digital Pattern instruments and sessions, to manage NI-Digital Pattern waveform data, and to access digital pattern project files.

[IMAGE alt='icon' src='nidigitalpattern-mnu.png']

- [Get All NI-Digital Pattern Instrument Names](../../../../../menus/categories/ni-semiconductormodule/pinmap/digital-pattern/getallnidigitalpatterninstrumentnames-vi.html) Returns the instrument names and comma-separated lists of instrument names that belong to the same group for all NI-Digital Pattern instruments in the Semiconductor Module context. You can use instrument names and comma-separated lists of instrument names to open driver sessions. This VI is available only in 64-bit LabVIEW.
- [Set NI-Digital Pattern Session](../../../../../menus/categories/ni-semiconductormodule/pinmap/digital-pattern/setnidigitalpatternsession-vi.html) Associates an instrument session with an NI-Digital Pattern instrument name. This VI is available only in 64-bit LabVIEW.
- [Get All NI-Digital Pattern Sessions](../../../../../menus/categories/ni-semiconductormodule/pinmap/digital-pattern/getallnidigitalpatternsessions-vi.html) Returns all NI-Digital Pattern instrument sessions in the Semiconductor Module context. You can use instrument sessions to close driver sessions. This VI is available only in 64-bit LabVIEW.
- [Pin(s) to NI-Digital Pattern Session(s)](../../../../../menus/categories/ni-semiconductormodule/pinmap/digital-pattern/pin-s-tonidigitalpatternsessions-vi.html) Returns the NI-Digital Pattern sessions, channel lists, and site lists required to access one or more pins. You must manually select the polymorphic instance you want to use. Select the single pin or multiple pins polymorphic instance based on the number of pins the test is designed to test. Select the single instrument or multiple instrument polymorphic instance based on the number of instruments you expect the pins to be connected to in the pin map. Use the multiple instrument polymorphic instances to ensure that code modules work with any pin map. Use the single instrument instance only when you know the code module will never be used with a pin map that has more than one instrument connected to the specified pins, or when the NI-Digital Pattern instruments are grouped together in the same group in the pin map. This VI is available only in 64-bit LabVIEW.
- [Per-Instrument to Per-Site Pattern Results](../../../../../menus/categories/ni-semiconductormodule/pinmap/digital-pattern/perinstrumenttopersitepatternresults-vi.html) Converts pattern results indexed by instrument sessions to pattern results indexed by sites. Pass input pattern results indexed by instrument sessions in the same order that the Pin(s) to NI-Digital Pattern Sessions VI returns. The VI returns pattern results indexed by sites in the same order that the Get Site Numbers VI returns. This VI is available only in 64-bit LabVIEW.
- [Source / Capture](../../../../../menus/categories/ni-semiconductormodule/pinmap/digital-pattern/sourcecapture-mnu.html) Use the Source / Capture VIs to manage NI-Digital Pattern waveform data.
- [Setup](../../../../../menus/categories/ni-semiconductormodule/pinmap/digital-pattern/instrument-setup/instrumentsetup-mnu.html) Use the Setup VIs to obtain file paths for digital pattern project files.

Parent topic:

Code Module Development

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/digital-pattern/perinstrumenttopersitepatternresults-vi.html language=enus -->
## TOPIC 00068: Per-Instrument to Per-Site Pattern Results

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/digital-pattern/perinstrumenttopersitepatternresults-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/digital-pattern/perinstrumenttopersitepatternresults-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts pattern results indexed by instrument sessions to pattern results indexed by sites. Pass input pattern results indexed by instrument sessions in the same order that the Pin(s) to NI-Digital Pattern Sessions VI returns. The VI returns pattern results indexed by sites in the same order that t

### Per-Instrument to Per-Site Pattern Results

Converts pattern results indexed by instrument sessions to pattern results indexed by sites. Pass input pattern results indexed by instrument sessions in the same order that the Pin(s) to NI-Digital Pattern Sessions VI returns. The VI returns pattern results indexed by sites in the same order that the Get Site Numbers VI returns. This VI is available only in 64-bit LabVIEW.

[IMAGE alt='icon' src='perinstrumenttopersitepatternresults-vi.png']

#### Inputs/Outputs

| Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. You must create a pin query context object from a Pin(s) to Sessions VI. Per-Instrument Pattern Results — specifies the pattern results indexed by instrument sessions in the same order as the instrument sessions that the Pin(s) to NI-Digital Pattern Sessions VI returns. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context Out — returns the pin query context object unchanged. Per-Site Pattern Results — returns the pattern results indexed by site in the same order as the sites that the Get Site Numbers VI returns. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

NI-Digital Pattern

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/digital-pattern/perinstrumenttopersitewaveforms-vi.html language=enus -->
## TOPIC 00069: Per-Instrument to Per-Site Waveforms

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/digital-pattern/perinstrumenttopersitewaveforms-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/digital-pattern/perinstrumenttopersitewaveforms-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts digital waveforms indexed by instrument sessions in the same order that the Pin(s) to NI-Digital Pattern Sessions VI returns into waveforms indexed by sites in the same order that the Get Site Numbers VI returns. This VI is available only in 64-bit LabVIEW. icon Inputs/Outputs cNI__TestStan

### Per-Instrument to Per-Site Waveforms

Converts digital waveforms indexed by instrument sessions in the same order that the Pin(s) to NI-Digital Pattern Sessions VI returns into waveforms indexed by sites in the same order that the Get Site Numbers VI returns. This VI is available only in 64-bit LabVIEW.

[IMAGE alt='icon' src='perinstrumenttopersitewaveforms-vi.png']

#### Inputs/Outputs

| Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. You must create a pin query context object from a Pin(s) to Sessions VI. Per-Instrument Waveforms — specifies the digital waveforms indexed by instrument sessions in the same order as the instrument sessions that the Pin(s) to NI-Digital Pattern Sessions VI returns. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context Out — returns the pin query context object unchanged. Per-Site Waveforms — returns the digital waveforms indexed by site in the same order as the sites that the Get Site Numbers VI returns. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Source / Capture

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/digital-pattern/persitetoperinstrumentwaveforms-vi.html language=enus -->
## TOPIC 00070: Per-Site to Per-Instrument Waveforms

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/digital-pattern/persitetoperinstrumentwaveforms-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/digital-pattern/persitetoperinstrumentwaveforms-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts digital waveforms indexed by sites in the same order that the Get Site Numbers VI returns into waveforms indexed by instrument sessions in the same order that the Pin(s) to NI-Digital Pattern Sessions VI returns. This VI is available only in 64-bit LabVIEW. icon Inputs/Outputs cNI__TestStan

### Per-Site to Per-Instrument Waveforms

Converts digital waveforms indexed by sites in the same order that the Get Site Numbers VI returns into waveforms indexed by instrument sessions in the same order that the Pin(s) to NI-Digital Pattern Sessions VI returns. This VI is available only in 64-bit LabVIEW.

[IMAGE alt='icon' src='persitetoperinstrumentwaveforms-vi.png']

#### Inputs/Outputs

| Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. You must create a pin query context object from a Pin(s) to Sessions VI. Per-Site Waveforms — specifies the digital waveforms indexed by site in the same order as the sites that the Get Site Numbers VI returns. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context Out — returns the pin query context object unchanged. Per-Instrument Waveforms — returns the digital waveforms indexed by instrument sessions in the same order as the instrument sessions that the by Pin(s) to NI-Digital Pattern Sessions VI returns. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Source / Capture

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/digital-pattern/pin-s-tonidigitalpatternsessions-vi.html language=enus -->
## TOPIC 00071: Pin(s) to NI-Digital Pattern Session(s)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/digital-pattern/pin-s-tonidigitalpatternsessions-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/digital-pattern/pin-s-tonidigitalpatternsessions-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-Digital Pattern sessions, channel lists, and site lists required to access one or more pins. You must manually select the polymorphic instance you want to use. Select the single pin or multiple pins polymorphic instance based on the number of pins the test is designed to test. Select

### Pin(s) to NI-Digital Pattern Session(s)

Returns the NI-Digital Pattern sessions, channel lists, and site lists required to access one or more pins. You must manually select the polymorphic instance you want to use. Select the single pin or multiple pins polymorphic instance based on the number of pins the test is designed to test. Select the single instrument or multiple instrument polymorphic instance based on the number of instruments you expect the pins to be connected to in the pin map. Use the multiple instrument polymorphic instances to ensure that code modules work with any pin map. Use the single instrument instance only when you know the code module will never be used with a pin map that has more than one instrument connected to the specified pins, or when the NI-Digital Pattern instruments are grouped together in the same group in the pin map. This VI is available only in 64-bit LabVIEW.

[IMAGE alt='icon' src='pin-s-tonidigitalpatternsessions-vi.png']

- [Pins to NI-Digital Pattern Session](../../../../../menus/categories/ni-semiconductormodule/pinmap/digital-pattern/pinstonidigitalpatternsession-vi.html) Returns the NI-Digital Pattern instrument session, channel list, and site list required to access the pins. If more than one instrument session is required to access the pin, the VI returns an error. Each group of NI-Digital Pattern instruments in the pin map creates a single instrument session.
- [Pin to NI-Digital Pattern Session](../../../../../menus/categories/ni-semiconductormodule/pinmap/digital-pattern/pintonidigitalpatternsession-vi.html) Returns the NI-Digital Pattern instrument session, channel list, and site list required to access the pin. If more than one instrument session is required to access the pin, the VI returns an error. Each group of NI-Digital Pattern instruments in the pin map creates a single instrument session.
- [Pins to NI-Digital Pattern Sessions](../../../../../menus/categories/ni-semiconductormodule/pinmap/digital-pattern/pinstonidigitalpatternsessions-vi.html) Returns the NI-Digital Pattern instrument sessions, channel lists, and site lists required to access the pins.
- [Pin to NI-Digital Pattern Sessions](../../../../../menus/categories/ni-semiconductormodule/pinmap/digital-pattern/pintonidigitalpatternsessions-vi.html) Returns the NI-Digital Pattern instrument sessions, channel lists, and site lists required to access the pin.

Parent topic:

NI-Digital Pattern

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/digital-pattern/pinstonidigitalpatternsession-vi.html language=enus -->
## TOPIC 00072: Pins to NI-Digital Pattern Session

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/digital-pattern/pinstonidigitalpatternsession-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/digital-pattern/pinstonidigitalpatternsession-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-Digital Pattern instrument session, channel list, and site list required to access the pins. If more than one instrument session is required to access the pin, the VI returns an error. Each group of NI-Digital Pattern instruments in the pin map creates a single instrument session. ico

### Pins to NI-Digital Pattern Session

Returns the NI-Digital Pattern instrument session, channel list, and site list required to access the pins. If more than one instrument session is required to access the pin, the VI returns an error. Each group of NI-Digital Pattern instruments in the pin map creates a single instrument session.

[IMAGE alt='icon' src='pinstonidigitalpatternsession-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pins — specifies the names of the pins or pin groups to translate to an instrument session, channel list, and site list. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context — is the pin query context object that tracks the session and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Session — returns the NI-Digital Pattern instrument session for the instruments connected to pins for all sites in the Semiconductor Module context. Channel List — returns the comma-separated channel list required to access the pins for all sites in the Semiconductor Module context. Each channel is specified by site and pin, e.g. "site0/A" as expected by the NI-Digital Pattern driver. If any of the pins are connected to the same instrument channel for multiple sites, the channel appears only once in the string and is identified by one of the site/pin combinations to which it is connected. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. Site List — returns the site list associated with the instrument session to access the pins for all sites in the Semiconductor Module context. The site list is a comma-separated list of sites. If you use a digital pattern instrument connected to multiple sites, you must connect this output to the site list input of the NI-Digital Pattern Driver VIs, such as the niDigital Apply Levels and Timing VI, the niDigital Burst Pattern VI, the niDigital Configure Pattern Burst Sites VI, the niDigital Fetch Capture Waveform (U32) VI, the niDigital Get Site Pass Fail VI, and the niDigital Write Source Waveform (Site Unique U32) instance of the niDigital Write Source Waveform VI. |
| --- |

Parent topic:

Pin(s) to NI-Digital Pattern Session(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/digital-pattern/pinstonidigitalpatternsessions-vi.html language=enus -->
## TOPIC 00073: Pins to NI-Digital Pattern Sessions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/digital-pattern/pinstonidigitalpatternsessions-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/digital-pattern/pinstonidigitalpatternsessions-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-Digital Pattern instrument sessions, channel lists, and site lists required to access the pins. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. c1ddaqmxscale.png Pins specifies the names of the pins or p

### Pins to NI-Digital Pattern Sessions

Returns the NI-Digital Pattern instrument sessions, channel lists, and site lists required to access the pins.

[IMAGE alt='icon' src='pinstonidigitalpatternsessions-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pins — specifies the names of the pins or pin groups to translate to instrument sessions, channel lists, and site lists. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Sessions — returns the NI-Digital Pattern instrument sessions for the instruments connected to pins for all sites in the Semiconductor Module context. Channel Lists — returns the comma-separated channel lists required to access the pins for all sites in the Semiconductor Module context. Each channel is specified by site and pin, e.g. "site0/A" as expected by the NI-Digital Pattern driver. If any of the pins are connected to the same instrument channel for multiple sites, the channel appears only once in the string and is identified by one of the site/pin combinations to which it is connected. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. Site Lists — returns the site lists associated with the instrument sessions to access pins for all sites in the Semiconductor Module context. Each site list is a comma-separated list of sites. If you use a digital pattern instrument connected to multiple sites, you must connect this output to the site list input of the NI-Digital Pattern Driver VIs, such as the niDigital Apply Levels and Timing VI, the niDigital Burst Pattern VI, the niDigital Configure Pattern Burst Sites VI, the niDigital Fetch Capture Waveform (U32) VI, the niDigital Get Site Pass Fail VI, and the niDigital Write Source Waveform (Site Unique U32) instance of the niDigital Write Source Waveform VI. |
| --- |

Parent topic:

Pin(s) to NI-Digital Pattern Session(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/digital-pattern/pintonidigitalpatternsession-vi.html language=enus -->
## TOPIC 00074: Pin to NI-Digital Pattern Session

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/digital-pattern/pintonidigitalpatternsession-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/digital-pattern/pintonidigitalpatternsession-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-Digital Pattern instrument session, channel list, and site list required to access the pin. If more than one instrument session is required to access the pin, the VI returns an error. Each group of NI-Digital Pattern instruments in the pin map creates a single instrument session. icon

### Pin to NI-Digital Pattern Session

Returns the NI-Digital Pattern instrument session, channel list, and site list required to access the pin. If more than one instrument session is required to access the pin, the VI returns an error. Each group of NI-Digital Pattern instruments in the pin map creates a single instrument session.

[IMAGE alt='icon' src='pintonidigitalpatternsession-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — specifies the name of the pin or pin group to translate to an instrument session, channel list, and site list. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context — Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Session — returns the NI-Digital Pattern instrument session for the instruments connected to the pin for all sites in the Semiconductor Module context. Channel List — returns the comma-separated channel list required to access the pin for all sites in the Semiconductor Module context. Each channel is specified by site and pin, e.g. "site0/A" as expected by the NI-Digital Pattern driver. If the pin is connected to the same instrument channel for multiple sites, the channel appears only once in the string and is identified by one of the site/pin combinations to which it is connected. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. Site List — returns the site list associated with the instrument session to access the pin for all sites in the Semiconductor Module context. The site list is a comma-separated list of sites. If you use a digital pattern instrument connected to multiple sites, you must connect this output to the site list input of the NI-Digital Pattern Driver VIs, such as the niDigital Apply Levels and Timing VI, the niDigital Burst Pattern VI, the niDigital Configure Pattern Burst Sites VI, the niDigital Fetch Capture Waveform (U32) VI, the niDigital Get Site Pass Fail VI, and the niDigital Write Source Waveform (Site Unique U32) instance of the niDigital Write Source Waveform VI. |
| --- |

Parent topic:

Pin(s) to NI-Digital Pattern Session(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/digital-pattern/pintonidigitalpatternsessions-vi.html language=enus -->
## TOPIC 00075: Pin to NI-Digital Pattern Sessions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/digital-pattern/pintonidigitalpatternsessions-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/digital-pattern/pintonidigitalpatternsessions-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-Digital Pattern instrument sessions, channel lists, and site lists required to access the pin. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cdaqmxscale.png Pin specifies the name of the pin or pin gro

### Pin to NI-Digital Pattern Sessions

Returns the NI-Digital Pattern instrument sessions, channel lists, and site lists required to access the pin.

[IMAGE alt='icon' src='pintonidigitalpatternsessions-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — specifies the name of the pin or pin group to translate to instrument sessions, channel lists, and site lists. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context Out — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Sessions — returns the NI-Digital Pattern instrument sessions for the instruments connected to the pin for all sites in the Semiconductor Module context. Channel Lists — returns the comma-separated channel lists required to access the pin for all sites in the Semiconductor Module context. Each channel is specified by site and pin, e.g. "site0/A" as expected by the NI-Digital Pattern driver. If the pin is connected to the same instrument channel for multiple sites, the channel appears only once in the string and is identified by one of the site/pin combinations to which it is connected. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. Site Lists — returns the site lists associated with the instrument sessions to access the pin for all sites in the Semiconductor Module context. Each site list is a comma-separated list of sites. If you use a digital pattern instrument connected to multiple sites, you must connect this output to the site list input of the NI-Digital Pattern Driver VIs, such as the niDigital Apply Levels and Timing VI, the niDigital Burst Pattern VI, the niDigital Configure Pattern Burst Sites VI, the niDigital Fetch Capture Waveform (U32) VI, the niDigital Get Site Pass Fail VI, and the niDigital Write Source Waveform (Site Unique U32) instance of the niDigital Write Source Waveform VI. |
| --- |

Parent topic:

Pin(s) to NI-Digital Pattern Session(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/digital-pattern/publishpatternresults-vi.html language=enus -->
## TOPIC 00076: Publish Pattern Results (2D)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/digital-pattern/publishpatternresults-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/digital-pattern/publishpatternresults-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Publishes the results obtained from calls to the Get Site Pass Fail VI or the Burst Pattern VI of the NI-Digital Pattern instrument driver on multiple instrument sessions. Leave the Pin column blank for the test on the Semiconductor Multi Test step when publishing pattern results with this VI. icon

### Publish Pattern Results (2D)

Publishes the results obtained from calls to the Get Site Pass Fail VI or the Burst Pattern VI of the NI-Digital Pattern instrument driver on multiple instrument sessions. Leave the Pin column blank for the test on the Semiconductor Multi Test step when publishing pattern results with this VI.

[IMAGE alt='icon' src='publishpatternresults-vi.png']

#### Inputs/Outputs

| Published Data Id — is the unique ID for distinguishing the measurement when you publish multiple measurements within the same code module. Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. History RAM Information — is the History RAM information returned by the niDigital Fetch Multi-Site History RAM Information VI of the NI-Digital Pattern instrument driver after a pattern burst. The niDigital Fetch Multi-Site History RAM Information VI does not appear on the NI-Digital Pattern Driver palette. Browse to and select the VI from the NI-Digital Pattern Driver library file (niDigital.llb), located in the \\instr.lib\\niDigital directory. pin names — number of cycles per site — cycle information — pattern name — time set name — vector number — cycle number — expected pin states — actual pin states — per pin pass fail — Pattern Results — is the site pass/fail results returned by the Get Site Pass Fail VI or Burst Pattern VI of the NI-Digital Pattern instrument driver. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context Out — returns the pin query context object unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |
| pin names — number of cycles per site — cycle information — pattern name — time set name — vector number — cycle number — expected pin states — actual pin states — per pin pass fail — |
| pattern name — time set name — vector number — cycle number — expected pin states — actual pin states — per pin pass fail — |

Parent topic:

Publish Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/digital-pattern/publishpatternresults1d-vi.html language=enus -->
## TOPIC 00077: Publish Pattern Results (1D)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/digital-pattern/publishpatternresults1d-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/digital-pattern/publishpatternresults1d-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Publishes the results obtained from calls to the Get Site Pass Fail VI or the Burst Pattern VI of the NI-Digital Pattern instrument driver on a single instrument session. Leave the Pin column blank for the test on the Semiconductor Multi Test step when publishing pattern results with this VI. icon I

### Publish Pattern Results (1D)

Publishes the results obtained from calls to the Get Site Pass Fail VI or the Burst Pattern VI of the NI-Digital Pattern instrument driver on a single instrument session. Leave the Pin column blank for the test on the Semiconductor Multi Test step when publishing pattern results with this VI.

[IMAGE alt='icon' src='publishpatternresults1d-vi.png']

#### Inputs/Outputs

| Published Data Id — is the unique ID for distinguishing the measurement when you publish multiple measurements within the same code module. Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. History RAM Information — is the History RAM information returned by the niDigital Fetch Multi-Site History RAM Information VI of the NI-Digital Pattern instrument driver after a pattern burst. The niDigital Fetch Multi-Site History RAM Information VI does not appear on the NI-Digital Pattern Driver palette. Browse to and select the VI from the NI-Digital Pattern Driver library file (niDigital.llb), located in the \\instr.lib\\niDigital directory. pin names — number of cycles per site — cycle information — pattern name — time set name — vector number — cycle number — expected pin states — actual pin states — per pin pass fail — Pattern Results — is the site pass/fail results returned by the Get Site Pass Fail VI or Burst Pattern VI of the NI-Digital Pattern instrument driver. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context Out — returns the pin query context object unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |
| pin names — number of cycles per site — cycle information — pattern name — time set name — vector number — cycle number — expected pin states — actual pin states — per pin pass fail — |
| pattern name — time set name — vector number — cycle number — expected pin states — actual pin states — per pin pass fail — |

Parent topic:

Publish Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/digital-pattern/setnidigitalpatternsession-vi.html language=enus -->
## TOPIC 00078: Set NI-Digital Pattern Session

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/digital-pattern/setnidigitalpatternsession-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/digital-pattern/setnidigitalpatternsession-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Associates an instrument session with an NI-Digital Pattern instrument name. This VI is available only in 64-bit LabVIEW. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cstr.png Instrument Name is the instrument name

### Set NI-Digital Pattern Session

Associates an instrument session with an NI-Digital Pattern instrument name. This VI is available only in 64-bit LabVIEW.

[IMAGE alt='icon' src='setnidigitalpatternsession-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Instrument Name — is the instrument name in the pin map file for the corresponding session. Instrument Session — specifies the instrument session for the corresponding instrument name. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

NI-Digital Pattern

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/digital-pattern/sourcecapture-mnu.html language=enus -->
## TOPIC 00079: Source / Capture

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/digital-pattern/sourcecapture-mnu.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/digital-pattern/sourcecapture-mnu.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Source / Capture VIs to manage NI-Digital Pattern waveform data. icon

### Source / Capture

Use the Source / Capture VIs to manage NI-Digital Pattern waveform data.

[IMAGE alt='icon' src='sourcecapture-mnu.png']

- [Per-Instrument to Per-Site Waveforms](../../../../../menus/categories/ni-semiconductormodule/pinmap/digital-pattern/perinstrumenttopersitewaveforms-vi.html) Converts digital waveforms indexed by instrument sessions in the same order that the Pin(s) to NI-Digital Pattern Sessions VI returns into waveforms indexed by sites in the same order that the Get Site Numbers VI returns. This VI is available only in 64-bit LabVIEW.
- [Per-Site to Per-Instrument Waveforms](../../../../../menus/categories/ni-semiconductormodule/pinmap/digital-pattern/persitetoperinstrumentwaveforms-vi.html) Converts digital waveforms indexed by sites in the same order that the Get Site Numbers VI returns into waveforms indexed by instrument sessions in the same order that the Pin(s) to NI-Digital Pattern Sessions VI returns. This VI is available only in 64-bit LabVIEW.

Parent topic:

NI-Digital Pattern

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/dmm/getallnidmminstrumentnames-vi.html language=enus -->
## TOPIC 00080: Get All NI-DMM Instrument Names

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/dmm/getallnidmminstrumentnames-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/dmm/getallnidmminstrumentnames-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns instrument names for all NI-DMM instruments in the Semiconductor Module context. You can use instrument names to open driver sessions. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cerrcodeclst.png error in (

### Get All NI-DMM Instrument Names

Returns instrument names for all NI-DMM instruments in the Semiconductor Module context. You can use instrument names to open driver sessions.

[IMAGE alt='icon' src='getallnidmminstrumentnames-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Names — returns an array of the NI-DMM instrument names in the Semiconductor Module Context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

NI-DMM

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/dmm/getallnidmmsessions-vi.html language=enus -->
## TOPIC 00081: Get All NI-DMM Sessions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/dmm/getallnidmmsessions-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/dmm/getallnidmmsessions-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns all NI-DMM instrument sessions in the Semiconductor Module context. You can use instrument sessions to close driver sessions. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cerrcodeclst.png error in (no error)

### Get All NI-DMM Sessions

Returns all NI-DMM instrument sessions in the Semiconductor Module context. You can use instrument sessions to close driver sessions.

[IMAGE alt='icon' src='getallnidmmsessions-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Sessions — returns all NI-DMM instrument sessions in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

NI-DMM

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/dmm/nidmm-mnu.html language=enus -->
## TOPIC 00082: NI-DMM

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/dmm/nidmm-mnu.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/dmm/nidmm-mnu.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-DMM VIs to manage NI-DMM instruments and sessions. icon

### NI-DMM

Use the NI-DMM VIs to manage NI-DMM instruments and sessions.

[IMAGE alt='icon' src='nidmm-mnu.png']

- [Get All NI-DMM Instrument Names](../../../../../menus/categories/ni-semiconductormodule/pinmap/dmm/getallnidmminstrumentnames-vi.html) Returns instrument names for all NI-DMM instruments in the Semiconductor Module context. You can use instrument names to open driver sessions.
- [Set NI-DMM Session](../../../../../menus/categories/ni-semiconductormodule/pinmap/dmm/setnidmmsession-vi.html) Associates an instrument session with an NI-DMM instrument name.
- [Get All NI-DMM Sessions](../../../../../menus/categories/ni-semiconductormodule/pinmap/dmm/getallnidmmsessions-vi.html) Returns all NI-DMM instrument sessions in the Semiconductor Module context. You can use instrument sessions to close driver sessions.
- [Pin(s) to NI-DMM Session(s)](../../../../../menus/categories/ni-semiconductormodule/pinmap/dmm/pin-s-tonidmmsession-s-vi.html) Returns the NI-DMM instrument sessions required to access one or more pins. You must manually select the polymorphic instance you want to use. Select the single pin or multiple pins polymorphic instance based on the number of pins the test is designed to test. Select the single instrument or multiple instrument polymorphic instance based on the number of instruments you expect the pin to be connected to in the pin map. Use the multiple instrument polymorphic instances to ensure that code modules work with any pin map. Use the single instrument instance when the Semiconductor Module Context contains only a single site.

Parent topic:

Code Module Development

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/dmm/pin-s-tonidmmsession-s-vi.html language=enus -->
## TOPIC 00083: Pin(s) to NI-DMM Session(s)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/dmm/pin-s-tonidmmsession-s-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/dmm/pin-s-tonidmmsession-s-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-DMM instrument sessions required to access one or more pins. You must manually select the polymorphic instance you want to use. Select the single pin or multiple pins polymorphic instance based on the number of pins the test is designed to test. Select the single instrument or multipl

### Pin(s) to NI-DMM Session(s)

Returns the NI-DMM instrument sessions required to access one or more pins. You must manually select the polymorphic instance you want to use. Select the single pin or multiple pins polymorphic instance based on the number of pins the test is designed to test. Select the single instrument or multiple instrument polymorphic instance based on the number of instruments you expect the pin to be connected to in the pin map. Use the multiple instrument polymorphic instances to ensure that code modules work with any pin map. Use the single instrument instance when the **Semiconductor Module Context** contains only a single site.

[IMAGE alt='icon' src='pin-s-tonidmmsession-s-vi.png']

- [Pins to NI-DMM Sessions](../../../../../menus/categories/ni-semiconductormodule/pinmap/dmm/pinstonidmmsessions-vi.html) Returns the NI-DMM instrument sessions required to access the pins.
- [Pin to NI-DMM Sessions](../../../../../menus/categories/ni-semiconductormodule/pinmap/dmm/pintonidmmsessions-vi.html) Returns the NI-DMM instrument sessions required to access the pin.
- [Pin to NI-DMM Session](../../../../../menus/categories/ni-semiconductormodule/pinmap/dmm/pintonidmmsession-vi.html) Returns the NI-DMM instrument session required to access the pin. If the Semiconductor Module context has more than one site, the VI returns an error.

Parent topic:

NI-DMM

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/dmm/pinstonidmmsessions-vi.html language=enus -->
## TOPIC 00084: Pins to NI-DMM Sessions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/dmm/pinstonidmmsessions-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/dmm/pinstonidmmsessions-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-DMM instrument sessions required to access the pins. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. c1ddaqmxscale.png Pins specifies the names of the pins or pin groups to translate to instrument sessio

### Pins to NI-DMM Sessions

Returns the NI-DMM instrument sessions required to access the pins.

[IMAGE alt='icon' src='pinstonidmmsessions-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pins — specifies the names of the pins or pin groups to translate to instrument sessions. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Sessions — returns the NI-DMM instrument sessions for the instruments connected to pins for all sites in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Pin(s) to NI-DMM Session(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/dmm/pintonidmmsession-vi.html language=enus -->
## TOPIC 00085: Pin to NI-DMM Session

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/dmm/pintonidmmsession-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/dmm/pintonidmmsession-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-DMM instrument session required to access the pin. If the Semiconductor Module context has more than one site, the VI returns an error. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cdaqmxscale.png Pin

### Pin to NI-DMM Session

Returns the NI-DMM instrument session required to access the pin. If the Semiconductor Module context has more than one site, the VI returns an error.

[IMAGE alt='icon' src='pintonidmmsession-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — specifies the name of the pin to translate to an instrument session. If multiple sessions are required, the VI returns an error. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Session — returns the NI-DMM instrument session for the instrument connected to the pin on the site in the Semiconductor Module Context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Pin(s) to NI-DMM Session(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/dmm/pintonidmmsessions-vi.html language=enus -->
## TOPIC 00086: Pin to NI-DMM Sessions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/dmm/pintonidmmsessions-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/dmm/pintonidmmsessions-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-DMM instrument sessions required to access the pin. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cdaqmxscale.png Pin specifies the name of the pin or pin group to translate to instrument sessions. cer

### Pin to NI-DMM Sessions

Returns the NI-DMM instrument sessions required to access the pin.

[IMAGE alt='icon' src='pintonidmmsessions-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — specifies the name of the pin or pin group to translate to instrument sessions. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Sessions — returns the NI-DMM instrument sessions for the instruments connected to the pin for all sites in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Pin(s) to NI-DMM Session(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/dmm/setnidmmsession-vi.html language=enus -->
## TOPIC 00087: Set NI-DMM Session

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/dmm/setnidmmsession-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/dmm/setnidmmsession-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Associates an instrument session with an NI-DMM instrument name. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cstr.png Instrument Name is the instrument name in the pin map file for the corresponding session. civrn.

### Set NI-DMM Session

Associates an instrument session with an NI-DMM instrument name.

[IMAGE alt='icon' src='setnidmmsession-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Instrument Name — is the instrument name in the pin map file for the corresponding session. Instrument Session — specifies the instrument session for the corresponding instrument name. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

NI-DMM

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/fgen/fgen-mnu.html language=enus -->
## TOPIC 00088: NI-FGEN

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/fgen/fgen-mnu.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/fgen/fgen-mnu.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-FGEN VIs to manage NI-FGEN instruments and sessions. icon

### NI-FGEN

Use the NI-FGEN VIs to manage NI-FGEN instruments and sessions.

[IMAGE alt='icon' src='fgen-mnu.png']

- [Get All NI-FGEN Instrument Names](../../../../../menus/categories/ni-semiconductormodule/pinmap/fgen/getallnifgeninstrumentnames-vi.html) Returns the instrument names for all NI-FGEN instruments in the Semiconductor Module context. You can use instrument names to open driver sessions.
- [Set NI-FGEN Session](../../../../../menus/categories/ni-semiconductormodule/pinmap/fgen/setnifgensession-vi.html) Associates an instrument session with an NI-FGEN instrument name.
- [Get All NI-FGEN Sessions](../../../../../menus/categories/ni-semiconductormodule/pinmap/fgen/getallnifgensessions-vi.html) Returns all NI-FGEN instrument sessions in the Semiconductor Module context. You can use instrument sessions to close driver sessions.
- [Pin(s) To NI-FGEN Session(s)](../../../../../menus/categories/ni-semiconductormodule/pinmap/fgen/pin-s-tonifgensession-s-vi.html) Returns the NI-FGEN instrument sessions and channel lists required to access one or more pins. You must manually select the polymorphic instance you want to use. Select the single pin or multiple pins polymorphic instance based on the number of pins the test is designed to test. Select the single instrument or multiple instrument polymorphic instance based on the number of instruments you expect the pin to be connected to in the pin map. Use the multiple instrument polymorphic instances to ensure that code modules work with any pin map. Use the single instrument instance only when you know the code module will never be used with a pin map that has more than one instrument connected to the specified pins.

Parent topic:

Code Module Development

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/fgen/getallnifgeninstrumentnames-vi.html language=enus -->
## TOPIC 00089: Get All NI-FGEN Instrument Names

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/fgen/getallnifgeninstrumentnames-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/fgen/getallnifgeninstrumentnames-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the instrument names for all NI-FGEN instruments in the Semiconductor Module context. You can use instrument names to open driver sessions. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cerrcodeclst.png error

### Get All NI-FGEN Instrument Names

Returns the instrument names for all NI-FGEN instruments in the Semiconductor Module context. You can use instrument names to open driver sessions.

[IMAGE alt='icon' src='getallnifgeninstrumentnames-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Names — returns an array of the NI-FGEN instrument names in the Semiconductor Module Context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

NI-FGEN

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/fgen/getallnifgensessions-vi.html language=enus -->
## TOPIC 00090: Get All NI-FGEN Sessions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/fgen/getallnifgensessions-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/fgen/getallnifgensessions-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns all NI-FGEN instrument sessions in the Semiconductor Module context. You can use instrument sessions to close driver sessions. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cerrcodeclst.png error in (no error

### Get All NI-FGEN Sessions

Returns all NI-FGEN instrument sessions in the Semiconductor Module context. You can use instrument sessions to close driver sessions.

[IMAGE alt='icon' src='getallnifgensessions-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Sessions — returns the instrument sessions for all NI-FGEN instruments in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

NI-FGEN

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/fgen/pin-s-tonifgensession-s-vi.html language=enus -->
## TOPIC 00091: Pin(s) To NI-FGEN Session(s)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/fgen/pin-s-tonifgensession-s-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/fgen/pin-s-tonifgensession-s-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-FGEN instrument sessions and channel lists required to access one or more pins. You must manually select the polymorphic instance you want to use. Select the single pin or multiple pins polymorphic instance based on the number of pins the test is designed to test. Select the single in

### Pin(s) To NI-FGEN Session(s)

Returns the NI-FGEN instrument sessions and channel lists required to access one or more pins. You must manually select the polymorphic instance you want to use. Select the single pin or multiple pins polymorphic instance based on the number of pins the test is designed to test. Select the single instrument or multiple instrument polymorphic instance based on the number of instruments you expect the pin to be connected to in the pin map. Use the multiple instrument polymorphic instances to ensure that code modules work with any pin map. Use the single instrument instance only when you know the code module will never be used with a pin map that has more than one instrument connected to the specified pins.

[IMAGE alt='icon' src='pin-s-tonifgensession-s-vi.png']

- [Pins To NI-FGEN Sessions](../../../../../menus/categories/ni-semiconductormodule/pinmap/fgen/pinstonifgensessions-vi.html) Returns the NI-FGEN instrument sessions and channel lists required to access the pins.
- [Pin To NI-FGEN Sessions](../../../../../menus/categories/ni-semiconductormodule/pinmap/fgen/pintonifgensessions-vi.html) Returns the NI-FGEN instrument sessions and channel lists required to access the pin.
- [Pins To NI-FGEN Session](../../../../../menus/categories/ni-semiconductormodule/pinmap/fgen/pinstonifgensession-vi.html) Returns the NI-FGEN instrument session and channel list required to access the pins. If more than one instrument is required to access the pins, the VI returns an error.
- [Pin To NI-FGEN Session](../../../../../menus/categories/ni-semiconductormodule/pinmap/fgen/pintonifgensession-vi.html) Returns the NI-FGEN instrument session and channel list required to access the pin. If more than one instrument is required to access the pin, the VI returns an error.

Parent topic:

NI-FGEN

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/fgen/pinstonifgensession-vi.html language=enus -->
## TOPIC 00092: Pins To NI-FGEN Session

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/fgen/pinstonifgensession-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/fgen/pinstonifgensession-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-FGEN instrument session and channel list required to access the pins. If more than one instrument is required to access the pins, the VI returns an error. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object.

### Pins To NI-FGEN Session

Returns the NI-FGEN instrument session and channel list required to access the pins. If more than one instrument is required to access the pins, the VI returns an error.

[IMAGE alt='icon' src='pinstonifgensession-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pins — specifies the names of the pins or pin groups to translate to an instrument session and a channel list. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context — is the pin query context object that tracks the session and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Session — returns the NI-FGEN instrument session for the instrument connected to pins for all sites in the Semiconductor Module context. Channel List — returns the comma-separated list of channels required to access pins for all sites in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Pin(s) To NI-FGEN Session(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/fgen/pinstonifgensessions-vi.html language=enus -->
## TOPIC 00093: Pins To NI-FGEN Sessions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/fgen/pinstonifgensessions-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/fgen/pinstonifgensessions-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-FGEN instrument sessions and channel lists required to access the pins. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. c1ddaqmxscale.png Pins specifies the names of the pins or pin groups to translate t

### Pins To NI-FGEN Sessions

Returns the NI-FGEN instrument sessions and channel lists required to access the pins.

[IMAGE alt='icon' src='pinstonifgensessions-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pins — specifies the names of the pins or pin groups to translate to instrument sessions and channel lists. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Sessions — returns the NI-FGEN instrument sessions for the instruments connected to pins for all sites in the Semiconductor Module context. Channel Lists — returns the channel lists required to access pins for all sites in the Semiconductor Module context. Each channel list is a comma-separated list of channels. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Pin(s) To NI-FGEN Session(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/fgen/pintonifgensession-vi.html language=enus -->
## TOPIC 00094: Pin To NI-FGEN Session

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/fgen/pintonifgensession-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/fgen/pintonifgensession-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-FGEN instrument session and channel list required to access the pin. If more than one instrument is required to access the pin, the VI returns an error. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cd

### Pin To NI-FGEN Session

Returns the NI-FGEN instrument session and channel list required to access the pin. If more than one instrument is required to access the pin, the VI returns an error.

[IMAGE alt='icon' src='pintonifgensession-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — is the name of the pin or pin group to translate to an instrument session and a channel list. If more than one session is required, the VI returns an error. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Session — returns the NI-FGEN instrument session for the instrument connected to the pin in the Semiconductor Module context. Channel List — returns the comma-separated list of channels required to access the pin for all sites in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Pin(s) To NI-FGEN Session(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/fgen/pintonifgensessions-vi.html language=enus -->
## TOPIC 00095: Pin To NI-FGEN Sessions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/fgen/pintonifgensessions-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/fgen/pintonifgensessions-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-FGEN instrument sessions and channel lists required to access the pin. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cdaqmxscale.png Pin is the name of the pin or pin group to translate to instrument s

### Pin To NI-FGEN Sessions

Returns the NI-FGEN instrument sessions and channel lists required to access the pin.

[IMAGE alt='icon' src='pintonifgensessions-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — is the name of the pin or pin group to translate to instrument sessions and channel lists. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Sessions — returns the NI-FGEN instrument sessions for the instruments connected to the pin for all sites in the Semiconductor Module context. Channel Lists — returns the channel lists required to access the pin for all sites in the Semiconductor Module context. Each channel list is a comma-separated list of channels. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Pin(s) To NI-FGEN Session(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/fgen/setnifgensession-vi.html language=enus -->
## TOPIC 00096: Set NI-FGEN Session

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/fgen/setnifgensession-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/fgen/setnifgensession-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Associates an instrument session with an NI-FGEN instrument name. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cstr.png Instrument Name is the instrument name in the pin map file for the corresponding session. civrn

### Set NI-FGEN Session

Associates an instrument session with an NI-FGEN instrument name.

[IMAGE alt='icon' src='setnifgensession-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Instrument Name — is the instrument name in the pin map file for the corresponding session. Instrument Session — specifies the instrument session for the corresponding instrument name. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

NI-FGEN

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/general/getpinnames-vi.html language=enus -->
## TOPIC 00097: Get Pin Names

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/general/getpinnames-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/general/getpinnames-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns all DUT and system pins available in the Semiconductor Module context that are connected to an instrument of the type you specify in the Instrument Type Id parameter. This VI returns only the pins specified on the Options tab of the Semiconductor Multi Test step. Pass an empty string to the

### Get Pin Names

Returns all DUT and system pins available in the Semiconductor Module context that are connected to an instrument of the type you specify in the **Instrument Type Id** parameter. This VI returns only the pins specified on the Options tab of the Semiconductor Multi Test step. Pass an empty string to the **Instrument Type Id** parameter to return all available pins.

[IMAGE alt='icon' src='getpinnames-vi.png']

#### Inputs/Outputs

| DAQmx Task Type — specifies the types of NI-DAQmx tasks for which you want to return pins. For pins connected to a NI-DAQmx task, this parameter limits the returned pins to those connected to tasks of the specified type. The method uses this parameter only if the Instrument Type Id parameter is niDAQmx or an empty string. Pass an empty string to include all pins that match the Instrument Type Id parameter. Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Instrument Type Id — specifies the type of instrument for which you want to return DUT and system pins. For instruments that TSM natively supports, right-click the Instrument Type Id parameter, select Create Constant from the shortcut menu, and select the type of instrument you need. All custom instruments defined in the pin map specify an associated type ID. Typically, this type ID is an instrument driver name or other ID that is common for instruments that users program in a similar way. For custom instruments, you must pass the type ID associated with the instrument in the pin map file. For model-based instruments, pass the string you passed to the Set Custom Session VI to store sessions for the instruments. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Capability — limits the filtered pins to those connected to a channel that defines the capability you specify. Use this parameter to differentiate between pins in the same instrument with different capabilities, such as NI-HSDIO Dynamic DIO channels and PFI lines. If a pin is connected to channels in which the capability is define only for a subset of sites, the VI returns an error. Pass an empty string to return all pins that match the type you specify in the Instrument Type Id parameter. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. DUT Pins — returns an array of strings that contains the DUT pins in the Semiconductor Module context that are connected to an instrument of the type you specify in the Instrument Type Id parameter. System Pins — returns an array of strings that contains the system pins in the Semiconductor Module context that are connected to an instrument of the type you specify in the Instrument Type Id parameter. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Code Module Development

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatabool1d-vi.html language=enus -->
## TOPIC 00098: Publish Pass/Fail Data (1D)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatabool1d-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatabool1d-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Publishes Boolean measurements from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context. icon Inputs/Outputs cdaqmxscale.png Published Data Id is the uniqu

### Publish Pass/Fail Data (1D)

Publishes Boolean measurements from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context.

[IMAGE alt='icon' src='publishdatabool1d-vi.png']

#### Inputs/Outputs

| Published Data Id — is the unique ID for distinguishing the measurement when you publish multiple measurements within the same code module. Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, and extract data from a set of measurements. You must create a pin query context object from a Pin(s) to Session(s) VI. Data In — specifies the multisite measurement data from multiple pins connected to one or more instrument sessions. The array consists of either a collection of single measurements made from multiple instrument sessions or a collection of multiple measurements made from a single instrument session. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context Out — returns the pin query context object unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Publish Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatabool2d-vi.html language=enus -->
## TOPIC 00099: Publish Pass/Fail Data (2D)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatabool2d-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatabool2d-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Publishes Boolean measurements from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context. icon Inputs/Outputs cdaqmxscale.png Published Data Id is the uniqu

### Publish Pass/Fail Data (2D)

Publishes Boolean measurements from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context.

[IMAGE alt='icon' src='publishdatabool2d-vi.png']

#### Inputs/Outputs

| Published Data Id — is the unique ID for distinguishing the measurement when you publish multiple measurements within the same code module. Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, and extract data from a set of measurements. You must create a pin query context object from a Pin(s) to Sessions VI. Data In — specifies the multisite measurement data from multiple pins connected to multiple instrument sessions. Each row represents measurements from one instrument session, and each column represents each channel on that instrument session. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context Out — returns the pin query context object unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Publish Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdataboolfunctionaltest-vi.html language=enus -->
## TOPIC 00100: Publish Per-Site Data (N Sites) (Boolean)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdataboolfunctionaltest-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdataboolfunctionaltest-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Publishes Boolean measurements from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context. icon Inputs/Outputs cdaqmxscale.png Published Data Id is the uniqu

### Publish Per-Site Data (N Sites) (Boolean)

Publishes Boolean measurements from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context.

[IMAGE alt='icon' src='publishdataboolfunctionaltest-vi.png']

#### Inputs/Outputs

| Published Data Id — is the unique ID for distinguishing the measurement when you publish multiple measurements within the same code module. Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — is the name of the pin that corresponds to the Data In parameter. Data In — specifies the Boolean measurement data for all sites in the Semiconductor Module context. The number of elements in the array must be equal to the number of sites. You must return results in the same order as the sites in the Semiconductor Module context. Use the Get Site Numbers VI to obtain the list of site numbers. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Publish Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdataboolscalar-vi.html language=enus -->
## TOPIC 00101: Publish Pass/Fail Data (Scalar)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdataboolscalar-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdataboolscalar-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Publishes Boolean measurements from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context. icon Inputs/Outputs cdaqmxscale.png Published Data Id is the uniqu

### Publish Pass/Fail Data (Scalar)

Publishes Boolean measurements from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context.

[IMAGE alt='icon' src='publishdataboolscalar-vi.png']

#### Inputs/Outputs

| Published Data Id — is the unique ID for distinguishing the measurement when you publish multiple measurements within the same code module. Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, and extract data from a set of measurements. You must create a pin query context object from a Pin to Session VI. Data In — specifies the Boolean measurement data for a single pin in a single site. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context Out — returns the pin query context object unchanged. error out — Contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Publish Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatadouble1d-vi.html language=enus -->
## TOPIC 00102: Publish Parametric Data (1D)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatadouble1d-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatadouble1d-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Publishes numeric results or data from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context. icon Inputs/Outputs cdaqmxscale.png Published Data Id is the un

### Publish Parametric Data (1D)

Publishes numeric results or data from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context.

[IMAGE alt='icon' src='publishdatadouble1d-vi.png']

#### Inputs/Outputs

| Published Data Id — is the unique ID for distinguishing the measurement when you publish multiple measurements within the same code module. Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, and extract data from a set of measurements. You must create a pin query context object from a Pin(s) to Session(s) VI. Data In — specifies the multisite measurement data from multiple pins connected to one or more instrument sessions. The array consists of either a collection of single measurements made from multiple instrument sessions or a collection of multiple measurements made from a single instrument session. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context Out — returns the pin query context object unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Publish Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatadouble2d-vi.html language=enus -->
## TOPIC 00103: Publish Parametric Data (2D)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatadouble2d-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatadouble2d-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Publishes numeric results or data from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context. icon Inputs/Outputs cdaqmxscale.png Published Data Id is the un

### Publish Parametric Data (2D)

Publishes numeric results or data from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context.

[IMAGE alt='icon' src='publishdatadouble2d-vi.png']

#### Inputs/Outputs

| Published Data Id — is the unique ID for distinguishing the measurement when you publish multiple measurements within the same code module. Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, and extract data from a set of measurements. You must create a pin query context object from a Pin(s) to Sessions VI. Data In — specifies the multisite measurement data from multiple pins connected to multiple instrument sessions. Each row represents measurements from one instrument session, and each column represents each channel on that instrument session. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context Out — returns the pin query context object unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Publish Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatadoublefunctionaltest-vi.html language=enus -->
## TOPIC 00104: Publish Per-Site Data (N Sites) (Numeric)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatadoublefunctionaltest-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatadoublefunctionaltest-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Publishes double measurements from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context. icon Inputs/Outputs cdaqmxscale.png Published Data Id is the unique

### Publish Per-Site Data (N Sites) (Numeric)

Publishes double measurements from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context.

[IMAGE alt='icon' src='publishdatadoublefunctionaltest-vi.png']

#### Inputs/Outputs

| Published Data Id — is the unique ID for distinguishing the measurement when you publish multiple measurements within the same code module. Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — is the name of the pin that corresponds to the Data In parameter. Data In — specifies the double measurement data for all sites in the Semiconductor Module context. The number of elements in the array must be equal to the number of sites. You must return results in the same order as the sites in the Semiconductor Module context. Use the Get Site Numbers VI to obtain the list of site numbers. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Publish Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatadoublescalar-vi.html language=enus -->
## TOPIC 00105: Publish Parametric Data (Scalar)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatadoublescalar-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatadoublescalar-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Publishes numeric results or data from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context. icon Inputs/Outputs cdaqmxscale.png Published Data Id is the un

### Publish Parametric Data (Scalar)

Publishes numeric results or data from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context.

[IMAGE alt='icon' src='publishdatadoublescalar-vi.png']

#### Inputs/Outputs

| Published Data Id — is the unique ID for distinguishing the measurement when you publish multiple measurements within the same code module. Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, and extract data from a set of measurements. You must create a pin query context object from a Pin to Session VI. Data In — specifies the double measurement data for a single pin in a single site. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context Out — returns the pin query context object unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Publish Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatapersitebooleanscalar-vi.html language=enus -->
## TOPIC 00106: Publish Per-Site Data (1 Site) (Boolean)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatapersitebooleanscalar-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatapersitebooleanscalar-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Publishes a Boolean measurement from a single site for the Semiconductor Multi Test step to consume. Use this VI to publish data for single site defined in the Semiconductor Module context. If the Semiconductor Module context contains more than one site, this VI returns an error. icon Inputs/Outputs

### Publish Per-Site Data (1 Site) (Boolean)

Publishes a Boolean measurement from a single site for the Semiconductor Multi Test step to consume. Use this VI to publish data for single site defined in the Semiconductor Module context. If the Semiconductor Module context contains more than one site, this VI returns an error.

[IMAGE alt='icon' src='publishdatapersitebooleanscalar-vi.png']

#### Inputs/Outputs

| Published Data Id — is the unique ID for distinguishing the measurement when you publish multiple measurements within the same code module. Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — is the name of the pin that corresponds to the Data In parameter. Data In — specifies the Boolean measurement data for a single site in the Semiconductor Module context. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Publish Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatapersitedoublescalar-vi.html language=enus -->
## TOPIC 00107: Publish Per-Site Data (1 Site) (Numeric)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatapersitedoublescalar-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatapersitedoublescalar-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Publishes a double measurement from a single site for the Semiconductor Multi Test step to consume. Use this VI to publish data for single site defined in the Semiconductor Module context. If the Semiconductor Module context contains more than one site, this VI returns an error. icon Inputs/Outputs

### Publish Per-Site Data (1 Site) (Numeric)

Publishes a double measurement from a single site for the Semiconductor Multi Test step to consume. Use this VI to publish data for single site defined in the Semiconductor Module context. If the Semiconductor Module context contains more than one site, this VI returns an error.

[IMAGE alt='icon' src='publishdatapersitedoublescalar-vi.png']

#### Inputs/Outputs

| Published Data Id — is the unique ID for distinguishing the measurement when you publish multiple measurements within the same code module. Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — is the name of the pin that corresponds to the Data In parameter. Data In — specifies the double measurement data for a single site in the Semiconductor Module context. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Publish Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatapersitestringscalar-vi.html language=enus -->
## TOPIC 00108: Publish Per-Site Data (1 Site) (String)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatapersitestringscalar-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatapersitestringscalar-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Publishes a string measurement from a single site for the Semiconductor Multi Test step to consume. Use this VI to publish data for single site defined in the Semiconductor Module context. If the Semiconductor Module context contains more than one site, this VI returns an error. icon Inputs/Outputs

### Publish Per-Site Data (1 Site) (String)

Publishes a string measurement from a single site for the Semiconductor Multi Test step to consume. Use this VI to publish data for single site defined in the Semiconductor Module context. If the Semiconductor Module context contains more than one site, this VI returns an error.

[IMAGE alt='icon' src='publishdatapersitestringscalar-vi.png']

#### Inputs/Outputs

| Published Data Id — is the unique ID for distinguishing the measurement when you publish multiple measurements within the same code module. Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — is the name of the pin that corresponds to the Data In parameter. Data In — specifies the string measurement data for a single site in the Semiconductor Module context. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Publish Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatastringfunctionaltest-vi.html language=enus -->
## TOPIC 00109: Publish Per-Site Data (N Sites) (String)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatastringfunctionaltest-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatastringfunctionaltest-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Publishes strings from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context. icon Inputs/Outputs cdaqmxscale.png Published Data Id is the unique ID for dist

### Publish Per-Site Data (N Sites) (String)

Publishes strings from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context.

[IMAGE alt='icon' src='publishdatastringfunctionaltest-vi.png']

#### Inputs/Outputs

| Published Data Id — is the unique ID for distinguishing the measurement when you publish multiple measurements within the same code module. Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — is the name of the pin that corresponds to the Data In parameter. Data In — specifies strings for all sites in the Semiconductor Module context. The number of elements in the array must be equal to the number of sites. You must return results in the same order as the sites in the Semiconductor Module context. Use the Get Site Numbers VI to obtain the list of site numbers. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Publish Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatawithcontext-vi.html language=enus -->
## TOPIC 00110: Publish Data

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatawithcontext-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatawithcontext-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Publishes measurement data for one or more pins to the Semiconductor Multi Test step type instances for all sites in the Semiconductor Module context. If you are publishing site data, the polymorphic instance must publish data for each site in the Semiconductor Module context. If you are publishing

### Publish Data

Publishes measurement data for one or more pins to the Semiconductor Multi Test step type instances for all sites in the Semiconductor Module context. If you are publishing site data, the polymorphic instance must publish data for each site in the Semiconductor Module context. If you are publishing pin data or pattern results, the polymorphic instance must support the pin query context obtained from the specific Pin(s) to Session(s), Pin to FPGA VI Reference(s), or Get Session Data VI you previously created. Pin(s) to Session(s) VIs include the following: Pin(s) to NI-Digital Pattern Sessions, Pin(s) to NI-DCPower Session(s), Pin(s) to NI-DAQmx Task(s), Pin(s) to NI-DMM Session(s), Pin(s) to NI-FGEN Session(s), Pin(s) to NI-SCOPE Session(s), Pin(s) to NI-HSDIO Session(s), Pin to NI-RFSA Session(s), Pin to NI-RFSG Session(s), and Pin to NI-RFmx Session(s).

[IMAGE alt='icon' src='publishdatawithcontext-vi.png']

- [Publish Pattern Results (2D)](../../../../../../menus/categories/ni-semiconductormodule/pinmap/digital-pattern/publishpatternresults-vi.html) Publishes the results obtained from calls to the Get Site Pass Fail VI or the Burst Pattern VI of the NI-Digital Pattern instrument driver on multiple instrument sessions. Leave the Pin column blank for the test on the Semiconductor Multi Test step when publishing pattern results with this VI.
- [Publish Pattern Results (1D)](../../../../../../menus/categories/ni-semiconductormodule/pinmap/digital-pattern/publishpatternresults1d-vi.html) Publishes the results obtained from calls to the Get Site Pass Fail VI or the Burst Pattern VI of the NI-Digital Pattern instrument driver on a single instrument session. Leave the Pin column blank for the test on the Semiconductor Multi Test step when publishing pattern results with this VI.
- [Publish Parametric Data (2D)](../../../../../../menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatadouble2d-vi.html) Publishes numeric results or data from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context.
- [Publish Parametric Data (1D)](../../../../../../menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatadouble1d-vi.html) Publishes numeric results or data from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context.
- [Publish Parametric Data (Scalar)](../../../../../../menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatadoublescalar-vi.html) Publishes numeric results or data from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context.
- [Publish Pass/Fail Data (2D)](../../../../../../menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatabool2d-vi.html) Publishes Boolean measurements from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context.
- [Publish Pass/Fail Data (1D)](../../../../../../menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatabool1d-vi.html) Publishes Boolean measurements from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context.
- [Publish Pass/Fail Data (Scalar)](../../../../../../menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdataboolscalar-vi.html) Publishes Boolean measurements from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context.
- [Publish Per-Site Data (N Sites) (Numeric)](../../../../../../menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatadoublefunctionaltest-vi.html) Publishes double measurements from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context.
- [Publish Per-Site Data (N Sites) (Boolean)](../../../../../../menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdataboolfunctionaltest-vi.html) Publishes Boolean measurements from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context.
- [Publish Per-Site Data (N Sites) (String)](../../../../../../menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatastringfunctionaltest-vi.html) Publishes strings from multiple sites for the Semiconductor Multi Test step to consume. Use this VI to publish data for multiple sites in the same order in which the sites are defined in the Semiconductor Module context.
- [Publish Per-Site Data (1 Site) (Numeric)](../../../../../../menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatapersitedoublescalar-vi.html) Publishes a double measurement from a single site for the Semiconductor Multi Test step to consume. Use this VI to publish data for single site defined in the Semiconductor Module context. If the Semiconductor Module context contains more than one site, this VI returns an error.
- [Publish Per-Site Data (1 Site) (Boolean)](../../../../../../menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatapersitebooleanscalar-vi.html) Publishes a Boolean measurement from a single site for the Semiconductor Multi Test step to consume. Use this VI to publish data for single site defined in the Semiconductor Module context. If the Semiconductor Module context contains more than one site, this VI returns an error.
- [Publish Per-Site Data (1 Site) (String)](../../../../../../menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatapersitestringscalar-vi.html) Publishes a string measurement from a single site for the Semiconductor Multi Test step to consume. Use this VI to publish data for single site defined in the Semiconductor Module context. If the Semiconductor Module context contains more than one site, this VI returns an error.

Parent topic:

Code Module Development

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/hsdio/createmultisitedigitalwaveformfrommultiplewaveformswithcontext-vi.html language=enus -->
## TOPIC 00111: Create Multisite Digital Waveforms (From Per-Site Waveforms)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/hsdio/createmultisitedigitalwaveformfrommultiplewaveformswithcontext-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/hsdio/createmultisitedigitalwaveformfrommultiplewaveformswithcontext-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an output array of one or multiple digital waveforms that you can download to NI-HSDIO instruments and that contain data properly organized for multiple sites according to the pin map. Use this VI when each site requires a different waveform. The order of signals in the Single Site Waveform

### Create Multisite Digital Waveforms (From Per-Site Waveforms)

Creates an output array of one or multiple digital waveforms that you can download to NI-HSDIO instruments and that contain data properly organized for multiple sites according to the pin map. Use this VI when each site requires a different waveform. The order of signals in the **Single Site Waveform** parameter should match the order of the **Pins** parameter used in the Pin(s) to NI-HSDIO Session(s) VI instance that generated the pin query context.

[IMAGE alt='icon' src='createmultisitedigitalwaveformfrommultiplewaveformswithcontext-vi.png']

#### Inputs/Outputs

| Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, extract data from a set of measurements, and create or rearrange waveforms. You create a pin query context object with a Pin(s) to NI-HSDIO Sessions VI. Per Site Waveform — specifies an array of digital waveforms in which each element is a waveform that corresponds to a site. The site order must correspond to the site order in Semiconductor Module context. Use the Get Site Numbers VI to obtain the site order. The signals in the digital waveform must be in the same order as the Pins parameter used in the Pin(s) to NI-HSDIO Session(s) VI instance that generated the pin query context. All waveforms in the array must have the same number of signals as the number of elements in the array. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context Out — returns the pin query context object unchanged. Per Instrument Digital Data — returns an array of digital waveforms in which each element is the waveform an NI-HSDIO instrument requires to generate the data in the Per Site Waveform parameter. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Create Multisite Digital Waveforms

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/hsdio/createmultisitedigitalwaveformfromsinglewaveformwithcontext-vi.html language=enus -->
## TOPIC 00112: Create Multisite Digital Waveforms (From Single Waveform)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/hsdio/createmultisitedigitalwaveformfromsinglewaveformwithcontext-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/hsdio/createmultisitedigitalwaveformfromsinglewaveformwithcontext-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an output array of one or multiple digital waveforms that you can download to NI-HSDIO instruments and that contain data properly organized for multiple sites according to the pin map. Use this VI when all sites require the same digital waveform. The order of signals in the Single Site Wavef

### Create Multisite Digital Waveforms (From Single Waveform)

Creates an output array of one or multiple digital waveforms that you can download to NI-HSDIO instruments and that contain data properly organized for multiple sites according to the pin map. Use this VI when all sites require the same digital waveform. The order of signals in the **Single Site Waveform** parameter should match the order of the **Pins** parameter used in the Pin(s) to NI-HSDIO Session(s) VI instance that generated the pin query context.

[IMAGE alt='icon' src='createmultisitedigitalwaveformfromsinglewaveformwithcontext-vi.png']

#### Inputs/Outputs

| Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, extract data from a set of measurements, and create or rearrange waveforms. You create a pin query context object with a Pin(s) to NI-HSDIO Sessions VI. Single Site Waveform — specifies the digital waveform that contains the digital pattern for a single site. The signals in the digital waveform must be in the same order as the Pins parameter used in the Pin(s) to NI-HSDIO Session(s) VI instance that generated the pin query context. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context Out — returns the pin query context object unchanged. Per Instrument Waveforms — returns an array of digital waveforms in which each element is the waveform an NI-HSDIO instrument requires to generate the data in the Single Site Waveform parameter for all sites. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Create Multisite Digital Waveforms

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/hsdio/createmultisitedigitalwaveformswithcontext-vi.html language=enus -->
## TOPIC 00113: Create Multisite Digital Waveforms

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/hsdio/createmultisitedigitalwaveformswithcontext-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/hsdio/createmultisitedigitalwaveformswithcontext-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates multisite digital waveforms based on the pin map. Use the Single Waveform to All Sites instance when you want to write the same waveform for each site. Use the Per Site Waveforms instance when you want to write different waveforms for each site. icon

### Create Multisite Digital Waveforms

Creates multisite digital waveforms based on the pin map. Use the Single Waveform to All Sites instance when you want to write the same waveform for each site. Use the Per Site Waveforms instance when you want to write different waveforms for each site.

[IMAGE alt='icon' src='createmultisitedigitalwaveformswithcontext-vi.png']

- [Create Multisite Digital Waveforms (From Single Waveform)](../../../../../menus/categories/ni-semiconductormodule/pinmap/hsdio/createmultisitedigitalwaveformfromsinglewaveformwithcontext-vi.html) Creates an output array of one or multiple digital waveforms that you can download to NI-HSDIO instruments and that contain data properly organized for multiple sites according to the pin map. Use this VI when all sites require the same digital waveform. The order of signals in the Single Site Waveform parameter should match the order of the Pins parameter used in the Pin(s) to NI-HSDIO Session(s) VI instance that generated the pin query context.
- [Create Multisite Digital Waveforms (From Per-Site Waveforms)](../../../../../menus/categories/ni-semiconductormodule/pinmap/hsdio/createmultisitedigitalwaveformfrommultiplewaveformswithcontext-vi.html) Creates an output array of one or multiple digital waveforms that you can download to NI-HSDIO instruments and that contain data properly organized for multiple sites according to the pin map. Use this VI when each site requires a different waveform. The order of signals in the Single Site Waveform parameter should match the order of the Pins parameter used in the Pin(s) to NI-HSDIO Session(s) VI instance that generated the pin query context.

Parent topic:

NI-HSDIO

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/hsdio/getallnihsdioinstrumentnames-vi.html language=enus -->
## TOPIC 00114: Get All NI-HSDIO Instrument Names

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/hsdio/getallnihsdioinstrumentnames-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/hsdio/getallnihsdioinstrumentnames-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the instrument names for all NI-HSDIO instruments in the Semiconductor Module context. You can use instrument names to open driver sessions. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cerrcodeclst.png erro

### Get All NI-HSDIO Instrument Names

Returns the instrument names for all NI-HSDIO instruments in the Semiconductor Module context. You can use instrument names to open driver sessions.

[IMAGE alt='icon' src='getallnihsdioinstrumentnames-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Names — returns an array of NI-HSDIO instrument names in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

NI-HSDIO

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/hsdio/getallnihsdiosessions-vi.html language=enus -->
## TOPIC 00115: Get All NI-HSDIO Sessions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/hsdio/getallnihsdiosessions-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/hsdio/getallnihsdiosessions-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns all NI-HSDIO acquisition sessions and all NI-HSDIO generation sessions in the Semiconductor Module context. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cerrcodeclst.png error in (no error) describes error c

### Get All NI-HSDIO Sessions

Returns all NI-HSDIO acquisition sessions and all NI-HSDIO generation sessions in the Semiconductor Module context.

[IMAGE alt='icon' src='getallnihsdiosessions-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Acquisition Sessions — returns the acquisition sessions for all NI-HSDIO instruments in the Semiconductor Module context. Generation Sessions — returns the generation sessions for all NI-HSDIO instruments in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

NI-HSDIO

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/hsdio/nihsdiopinmap-mnu.html language=enus -->
## TOPIC 00116: NI-HSDIO

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/hsdio/nihsdiopinmap-mnu.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/hsdio/nihsdiopinmap-mnu.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-HSDIO VIs to manage NI-HSDIO instruments and sessions and to create and rearrange multisite digital waveforms. icon

### NI-HSDIO

Use the NI-HSDIO VIs to manage NI-HSDIO instruments and sessions and to create and rearrange multisite digital waveforms.

[IMAGE alt='icon' src='nihsdiopinmap-mnu.png']

- [Get All NI-HSDIO Instrument Names](../../../../../menus/categories/ni-semiconductormodule/pinmap/hsdio/getallnihsdioinstrumentnames-vi.html) Returns the instrument names for all NI-HSDIO instruments in the Semiconductor Module context. You can use instrument names to open driver sessions.
- [Set NI-HSDIO Sessions](../../../../../menus/categories/ni-semiconductormodule/pinmap/hsdio/setnihsdiosessions-vi.html) Associates an NI-HSDIO acquisition session and an NI-HSDIO generation session with an NI-HSDIO instrument name.
- [Get All NI-HSDIO Sessions](../../../../../menus/categories/ni-semiconductormodule/pinmap/hsdio/getallnihsdiosessions-vi.html) Returns all NI-HSDIO acquisition sessions and all NI-HSDIO generation sessions in the Semiconductor Module context.
- [Pin(s) to NI-HSDIO Session(s)](../../../../../menus/categories/ni-semiconductormodule/pinmap/hsdio/pin-s-tonihsdiosession-s-vi.html) Returns the NI-HSDIO acquisition sessions, generation sessions, and channel lists required to access one or more pins. You must manually select the polymorphic instance you want to use. Select the single pin or multiple pins polymorphic instance based on the number of pins the test is designed to test. Select the single instrument or multiple instrument polymorphic instance based on the number of instruments you expect the pin to be connected to in the pin map. Use the multiple instrument polymorphic instances to ensure that code modules work with any pin map. Use the single instrument instance only when you know the code module will never be used with a pin map that has more than one instrument connected to the specified pins.
- [Get NI-HSDIO Masks](../../../../../menus/categories/ni-semiconductormodule/pinmap/hsdio/pinstonihsdiochannelmaskswithcontext-vi.html) Returns an array of channel masks in which each element corresponds to a site in the Semiconductor Module context. Each element in the array is an unsigned number in which a bit is asserted if a pin is connected to that channel. You can use the masks to identify which site failed in a functional test.
- [Create Multisite Digital Waveforms](../../../../../menus/categories/ni-semiconductormodule/pinmap/hsdio/createmultisitedigitalwaveformswithcontext-vi.html) Creates multisite digital waveforms based on the pin map. Use the Single Waveform to All Sites instance when you want to write the same waveform for each site. Use the Per Site Waveforms instance when you want to write different waveforms for each site.
- [Rearrange Multisite Digital Waveforms](../../../../../menus/categories/ni-semiconductormodule/pinmap/hsdio/rearrangemultisitedigitalwaveformswithcontext-vi.html) Rearranges multisite waveforms read from NI-HSDIO instruments into per-site digital waveforms.

Parent topic:

Code Module Development

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/hsdio/pin-s-tonihsdiosession-s-vi.html language=enus -->
## TOPIC 00117: Pin(s) to NI-HSDIO Session(s)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/hsdio/pin-s-tonihsdiosession-s-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/hsdio/pin-s-tonihsdiosession-s-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-HSDIO acquisition sessions, generation sessions, and channel lists required to access one or more pins. You must manually select the polymorphic instance you want to use. Select the single pin or multiple pins polymorphic instance based on the number of pins the test is designed to te

### Pin(s) to NI-HSDIO Session(s)

Returns the NI-HSDIO acquisition sessions, generation sessions, and channel lists required to access one or more pins. You must manually select the polymorphic instance you want to use. Select the single pin or multiple pins polymorphic instance based on the number of pins the test is designed to test. Select the single instrument or multiple instrument polymorphic instance based on the number of instruments you expect the pin to be connected to in the pin map. Use the multiple instrument polymorphic instances to ensure that code modules work with any pin map. Use the single instrument instance only when you know the code module will never be used with a pin map that has more than one instrument connected to the specified pins.

[IMAGE alt='icon' src='pin-s-tonihsdiosession-s-vi.png']

- [Pins to NI-HSDIO Sessions](../../../../../menus/categories/ni-semiconductormodule/pinmap/hsdio/pinstonihsdiosessions-vi.html) Returns the NI-HSDIO acquisition sessions, generation sessions, and channel lists required to access the pins.
- [Pin to NI-HSDIO Sessions](../../../../../menus/categories/ni-semiconductormodule/pinmap/hsdio/pintonihsdiosessions-vi.html) Returns the NI-HSDIO acquisition sessions, generation sessions, and channel lists required to access the pin.
- [Pins to NI-HSDIO Session](../../../../../menus/categories/ni-semiconductormodule/pinmap/hsdio/pinstonihsdiosession-vi.html) Returns the NI-HSDIO acquisition session, generation session, and channel list required to access the pins. If more than one instrument is required to access the pins, the VI returns an error.
- [Pin to NI-HSDIO Session](../../../../../menus/categories/ni-semiconductormodule/pinmap/hsdio/pintonihsdiosession-vi.html) Returns the NI-HSDIO acquisition session, generation session, and channel list required to access the pin. If more than one instrument is required to access the pin, the VI returns an error.

Parent topic:

NI-HSDIO

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/hsdio/pinstonihsdiochannelmasksmultipleinstrumentswithcontext-vi.html language=enus -->
## TOPIC 00118: Get NI-HSDIO Masks (Multiple Instruments)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/hsdio/pinstonihsdiochannelmasksmultipleinstrumentswithcontext-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/hsdio/pinstonihsdiochannelmasksmultipleinstrumentswithcontext-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a two-dimensional array of channel masks with one array for each instrument and one element for each site stored in the Semiconductor Module context. Each element in the array is an unsigned number in which a bit is asserted if a pin or pin group is connected to that channel. You can use the

### Get NI-HSDIO Masks (Multiple Instruments)

Returns a two-dimensional array of channel masks with one array for each instrument and one element for each site stored in the Semiconductor Module context. Each element in the array is an unsigned number in which a bit is asserted if a pin or pin group is connected to that channel. You can use the masks to identify which site failed in a functional test in which a single instrument services multiple sites. The first dimension of the array corresponds to an instrument, and the second dimension corresponds to a site. Use this VI when you write code modules that service multiple NI-HSDIO instruments.

[IMAGE alt='icon' src='pinstonihsdiochannelmasksmultipleinstrumentswithcontext-vi.png']

#### Inputs/Outputs

| Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, extract data from a set of measurements, and create or rearrange waveforms. You must create a pin query context object from a Pin(s) to NI-HSDIO Sessions VI. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Channel Masks — returns the two-dimensional array of channel masks with a row for each instrument and a column for each site in the Semiconductor Module context. Each element in the array is an unsigned number in which a bit is asserted if a pin is connected to that channel. You can use the masks to identify which site failed in a functional test in which a single instrument services multiple sites. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Get NI-HSDIO Masks

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/hsdio/pinstonihsdiochannelmaskssingleinstrumentwithcontext-vi.html language=enus -->
## TOPIC 00119: Get NI-HSDIO Masks (Single Instrument)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/hsdio/pinstonihsdiochannelmaskssingleinstrumentwithcontext-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/hsdio/pinstonihsdiochannelmaskssingleinstrumentwithcontext-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a one-dimensional array of channel masks with one element for each site in the Semiconductor Module context. Each element in the array is an unsigned number in which a bit is asserted if a pin or pin group is connected to that channel. You can use the masks to identify which site failed in a

### Get NI-HSDIO Masks (Single Instrument)

Returns a one-dimensional array of channel masks with one element for each site in the Semiconductor Module context. Each element in the array is an unsigned number in which a bit is asserted if a pin or pin group is connected to that channel. You can use the masks to identify which site failed in a functional test.

[IMAGE alt='icon' src='pinstonihsdiochannelmaskssingleinstrumentwithcontext-vi.png']

#### Inputs/Outputs

| Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, extract data from a set of measurements, and create or rearrange waveforms. You must create a pin query context object from a Pin(s) to NI-HSDIO Sessions VI. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Channel Masks — returns the one-dimensional array of channel masks with one element for each site in the Semiconductor Module context. Each element in the array is an unsigned number in which a bit is asserted if a pin is connected to that channel. You can use the masks to identify which site failed in a functional test. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Get NI-HSDIO Masks

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/hsdio/pinstonihsdiochannelmaskswithcontext-vi.html language=enus -->
## TOPIC 00120: Get NI-HSDIO Masks

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/hsdio/pinstonihsdiochannelmaskswithcontext-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/hsdio/pinstonihsdiochannelmaskswithcontext-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of channel masks in which each element corresponds to a site in the Semiconductor Module context. Each element in the array is an unsigned number in which a bit is asserted if a pin is connected to that channel. You can use the masks to identify which site failed in a functional tes

### Get NI-HSDIO Masks

Returns an array of channel masks in which each element corresponds to a site in the Semiconductor Module context. Each element in the array is an unsigned number in which a bit is asserted if a pin is connected to that channel. You can use the masks to identify which site failed in a functional test.

[IMAGE alt='icon' src='pinstonihsdiochannelmaskswithcontext-vi.png']

- [Get NI-HSDIO Masks (Multiple Instruments)](../../../../../menus/categories/ni-semiconductormodule/pinmap/hsdio/pinstonihsdiochannelmasksmultipleinstrumentswithcontext-vi.html) Returns a two-dimensional array of channel masks with one array for each instrument and one element for each site stored in the Semiconductor Module context. Each element in the array is an unsigned number in which a bit is asserted if a pin or pin group is connected to that channel. You can use the masks to identify which site failed in a functional test in which a single instrument services multiple sites. The first dimension of the array corresponds to an instrument, and the second dimension corresponds to a site. Use this VI when you write code modules that service multiple NI-HSDIO instruments.
- [Get NI-HSDIO Masks (Single Instrument)](../../../../../menus/categories/ni-semiconductormodule/pinmap/hsdio/pinstonihsdiochannelmaskssingleinstrumentwithcontext-vi.html) Returns a one-dimensional array of channel masks with one element for each site in the Semiconductor Module context. Each element in the array is an unsigned number in which a bit is asserted if a pin or pin group is connected to that channel. You can use the masks to identify which site failed in a functional test.

Parent topic:

NI-HSDIO

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/hsdio/pinstonihsdiosession-vi.html language=enus -->
## TOPIC 00121: Pins to NI-HSDIO Session

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/hsdio/pinstonihsdiosession-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/hsdio/pinstonihsdiosession-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-HSDIO acquisition session, generation session, and channel list required to access the pins. If more than one instrument is required to access the pins, the VI returns an error. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor

### Pins to NI-HSDIO Session

Returns the NI-HSDIO acquisition session, generation session, and channel list required to access the pins. If more than one instrument is required to access the pins, the VI returns an error.

[IMAGE alt='icon' src='pinstonihsdiosession-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pins — specifies the names of the pins or pin groups to translate to a generation session, an acquisition session, and a channel list. If more than one instrument is required to access the pins, the VI returns an error. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, extract data from a set of measurements, and create or rearrange waveforms. Channel List — returns the comma-separated list of channels required to access pins for all sites in the Semiconductor Module context. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Acquisition Session — returns the NI-HSDIO acquisition session for the instrument connected to pins for all sites in the Semiconductor Module context. Generation Session — returns the NI-HSDIO generation session for the instrument connected to pins for all sites in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Pin(s) to NI-HSDIO Session(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/hsdio/pinstonihsdiosessions-vi.html language=enus -->
## TOPIC 00122: Pins to NI-HSDIO Sessions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/hsdio/pinstonihsdiosessions-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/hsdio/pinstonihsdiosessions-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-HSDIO acquisition sessions, generation sessions, and channel lists required to access the pins. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. c1ddaqmxscale.png Pins specifies the names of the pins or p

### Pins to NI-HSDIO Sessions

Returns the NI-HSDIO acquisition sessions, generation sessions, and channel lists required to access the pins.

[IMAGE alt='icon' src='pinstonihsdiosessions-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pins — specifies the names of the pins or pin groups to translate to generation sessions, acquisition sessions, and channel lists. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, extract data from a set of measurements, and create or rearrange waveforms. Channel Lists — returns the channel lists required to access pins for all sites in the Semiconductor Module context. Each channel list is a comma-separated list of channels. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Acquisition Sessions — returns the NI-HSDIO acquisition sessions for the instruments connected to pins for all sites in the Semiconductor Module context. Generation Sessions — returns the NI-HSDIO generation sessions for the instruments connected to pins for all sites in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Pin(s) to NI-HSDIO Session(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/hsdio/pintonihsdiosession-vi.html language=enus -->
## TOPIC 00123: Pin to NI-HSDIO Session

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/hsdio/pintonihsdiosession-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/hsdio/pintonihsdiosession-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-HSDIO acquisition session, generation session, and channel list required to access the pin. If more than one instrument is required to access the pin, the VI returns an error. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Mo

### Pin to NI-HSDIO Session

Returns the NI-HSDIO acquisition session, generation session, and channel list required to access the pin. If more than one instrument is required to access the pin, the VI returns an error.

[IMAGE alt='icon' src='pintonihsdiosession-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — specifies the name of the pin or pin group to translate to a generation session, an acquisition session, and a channel list. If more than one instrument is required to access the pin, the VI returns an error. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, extract data from a set of measurements, and create or rearrange waveforms. Channel List — returns the comma-separated list of channels required to access the pin for all sites in the Semiconductor Module context. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Acquisition Session — returns the NI-HSDIO acquisition session for the instrument connected to the pin for all sites in the Semiconductor Module context. Generation Session — returns the NI-HSDIO generation session for the instrument connected to the pin for all sites in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Pin(s) to NI-HSDIO Session(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/hsdio/pintonihsdiosessions-vi.html language=enus -->
## TOPIC 00124: Pin to NI-HSDIO Sessions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/hsdio/pintonihsdiosessions-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/hsdio/pintonihsdiosessions-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-HSDIO acquisition sessions, generation sessions, and channel lists required to access the pin. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cdaqmxscale.png Pin specifies the name of the pin or pin gro

### Pin to NI-HSDIO Sessions

Returns the NI-HSDIO acquisition sessions, generation sessions, and channel lists required to access the pin.

[IMAGE alt='icon' src='pintonihsdiosessions-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — specifies the name of the pin or pin group to translate to generation sessions, acquisition sessions, and channel lists. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, extract data from a set of measurements, or rearrange waveforms. Channel Lists — returns the comma-separated list of channels required to access the pin for all sites in the Semiconductor Module context. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Acquisition Sessions — returns the NI-HSDIO acquisition sessions for the instruments connected to the pin for all sites in the Semiconductor Module context. Generation Sessions — returns the NI-HSDIO generation sessions for the instruments connected to the pin for all sites in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Pin(s) to NI-HSDIO Session(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/hsdio/rearrangemultisitedigitalwaveformswithcontext-vi.html language=enus -->
## TOPIC 00125: Rearrange Multisite Digital Waveforms

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/hsdio/rearrangemultisitedigitalwaveformswithcontext-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/hsdio/rearrangemultisitedigitalwaveformswithcontext-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Rearranges multisite waveforms read from NI-HSDIO instruments into per-site digital waveforms. icon Inputs/Outputs cNI__TestStand__SemiconductorModule_lvlib_MultipleSessionPinQueryContextlvclass.png Pin Query Context is the pin query context object that tracks the sessions and channels associated wi

### Rearrange Multisite Digital Waveforms

Rearranges multisite waveforms read from NI-HSDIO instruments into per-site digital waveforms.

[IMAGE alt='icon' src='rearrangemultisitedigitalwaveformswithcontext-vi.png']

#### Inputs/Outputs

| Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements, extract data from a set of measurements, and create or rearrange waveforms. You must create a pin query context object from a Pin(s) to NI-HSDIO Sessions VI. Per Instrument Waveforms — specifies an array of digital waveforms in which each element is a waveform acquired from an instrument. The waveform order must correspond to the instrument order the Pin(s) to NI-HSDIO Session(s) VI returns. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context Out — returns the pin query context object unchanged. Per Site Waveforms — returns an array of digital waveforms in which each element is the waveform for a site in the Semiconductor Module context. The order of the sites matches the values from the Get Site Numbers VI. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

NI-HSDIO

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/hsdio/setnihsdiosessions-vi.html language=enus -->
## TOPIC 00126: Set NI-HSDIO Sessions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/hsdio/setnihsdiosessions-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/hsdio/setnihsdiosessions-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Associates an NI-HSDIO acquisition session and an NI-HSDIO generation session with an NI-HSDIO instrument name. icon Inputs/Outputs civrn.png Acquisition Session specifies the NI-HSDIO acquisition session for the corresponding instrument name. coarn.png Semiconductor Module Context is a valid Active

### Set NI-HSDIO Sessions

Associates an NI-HSDIO acquisition session and an NI-HSDIO generation session with an NI-HSDIO instrument name.

[IMAGE alt='icon' src='setnihsdiosessions-vi.png']

#### Inputs/Outputs

| Acquisition Session — specifies the NI-HSDIO acquisition session for the corresponding instrument name. Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Instrument Name — specifies the instrument name in the pin map file for the corresponding acquisition session and generation session. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Generation Session — specifies the NI-HSDIO generation session for the corresponding instrument name. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

NI-HSDIO

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/input-data/getinputdata-vi.html language=enus -->
## TOPIC 00127: Get Input Data

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/input-data/getinputdata-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/input-data/getinputdata-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns per-site input data as defined in the Semiconductor Multi Test step. You must manually select the polymorphic instance you want to use. icon

### Get Input Data

Returns per-site input data as defined in the Semiconductor Multi Test step. You must manually select the polymorphic instance you want to use.

[IMAGE alt='icon' src='getinputdata-vi.png']

- [Get Input Data (Double)](../../../../../menus/categories/ni-semiconductormodule/pinmap/input-data/getinputdatadouble-vi.html) Returns per-site double-precision, floating-point data as defined in the Semiconductor Multi Test step.
- [Get Input Data (Boolean)](../../../../../menus/categories/ni-semiconductormodule/pinmap/input-data/getinputdataboolean-vi.html) Returns per-site Boolean data as defined in the Semiconductor Multi Test step.
- [Get Input Data (String)](../../../../../menus/categories/ni-semiconductormodule/pinmap/input-data/getinputdatastring-vi.html) Returns per-site string data as defined in the Semiconductor Multi Test step.

Parent topic:

Advanced

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/input-data/getinputdataboolean-vi.html language=enus -->
## TOPIC 00128: Get Input Data (Boolean)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/input-data/getinputdataboolean-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/input-data/getinputdataboolean-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns per-site Boolean data as defined in the Semiconductor Multi Test step. icon Inputs/Outputs cdaqmxscale.png Input Data Id is the unique ID to distinguish the data. This parameter must match the values you specify on the Per-Site Inputs tab of the Semiconductor Multi Test step. coarn.png Semic

### Get Input Data (Boolean)

Returns per-site Boolean data as defined in the Semiconductor Multi Test step.

[IMAGE alt='icon' src='getinputdataboolean-vi.png']

#### Inputs/Outputs

| Input Data Id — is the unique ID to distinguish the data. This parameter must match the values you specify on the Per-Site Inputs tab of the Semiconductor Multi Test step. Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — specifies the name of the pin associated with the Data Out parameter. This parameter must match the values you specify on the Per-Site Inputs tab of the Semiconductor Multi Test step. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Data Out — returns the per-site Boolean data associated with the Data Source column for the row with a matching pin and Input Data Id parameter values in the Per-Site Inputs table on the Per-Site Inputs tab of the Semiconductor Multi Test step. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Get Input Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/input-data/getinputdatadouble-vi.html language=enus -->
## TOPIC 00129: Get Input Data (Double)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/input-data/getinputdatadouble-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/input-data/getinputdatadouble-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns per-site double-precision, floating-point data as defined in the Semiconductor Multi Test step. icon Inputs/Outputs cdaqmxscale.png Input Data Id is the unique ID to distinguish the data. This parameter must match the values you specify on the Per-Site Inputs tab of the Semiconductor Multi T

### Get Input Data (Double)

Returns per-site double-precision, floating-point data as defined in the Semiconductor Multi Test step.

[IMAGE alt='icon' src='getinputdatadouble-vi.png']

#### Inputs/Outputs

| Input Data Id — is the unique ID to distinguish the data. This parameter must match the values you specify on the Per-Site Inputs tab of the Semiconductor Multi Test step. Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — specifies the name of the pin associated with the Data Out parameter. This parameter must match the values you specify on the Per-Site Inputs tab of the Semiconductor Multi Test step. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Data Out — returns the per-site double-precision, floating-point data associated with the Data Source column for the row with a matching pin and Input Data Id parameter values in the Per-Site Inputs table on the Per-Site Inputs tab of the Semiconductor Multi Test step. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Get Input Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/input-data/getinputdatastring-vi.html language=enus -->
## TOPIC 00130: Get Input Data (String)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/input-data/getinputdatastring-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/input-data/getinputdatastring-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns per-site string data as defined in the Semiconductor Multi Test step. icon Inputs/Outputs cdaqmxscale.png Input Data Id is the unique ID to distinguish the data. This parameter must match the values you specify on the Per-Site Inputs tab of the Semiconductor Multi Test step. coarn.png Semico

### Get Input Data (String)

Returns per-site string data as defined in the Semiconductor Multi Test step.

[IMAGE alt='icon' src='getinputdatastring-vi.png']

#### Inputs/Outputs

| Input Data Id — is the unique ID to distinguish the data. This parameter must match the values you specify on the Per-Site Inputs tab of the Semiconductor Multi Test step. Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — specifies the name of the pin associated with the Data Out parameter. This parameter must match the values you specify on the Per-Site Inputs tab of the Semiconductor Multi Test step. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Data Out — returns the per-site string data associated with the Data Source column for the row with matching the pin and Input Data Id parameter values in the Per-Site Inputs table on the Per-Site Inputs tab of the Semiconductor Multi Test step. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Get Input Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/modelbased/getallmodelbasedinstrumentnames-vi.html language=enus -->
## TOPIC 00131: Get All Model-Based Instrument Names

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/modelbased/getallmodelbasedinstrumentnames-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/modelbased/getallmodelbasedinstrumentnames-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the instrument names and models for all Model-Based instruments in the Semiconductor Module context. You can use instrument names to query the model properties for the information needed to create the appropriate sessions to drive the instrument. icon Inputs/Outputs coarn.png Semiconductor M

### Get All Model-Based Instrument Names

Returns the instrument names and models for all Model-Based instruments in the Semiconductor Module context. You can use instrument names to query the model properties for the information needed to create the appropriate sessions to drive the instrument.

[IMAGE alt='icon' src='getallmodelbasedinstrumentnames-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Category — specifies the category of instruments for which to return instrument names. Subcategory — specifies the subcategory (under the given category) of instruments for which to return instrument names. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Model-Based Instruments — returns an array of ModelBasedInstrumentInstanceData objects, each containing the instrument name and model of the Model-Based instrument in the Semiconductor Module Context. Instrument Name — Instrument Model — error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |
| Instrument Name — Instrument Model — |

Parent topic:

Model-Based

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/modelbased/getmodelbasedinstrumentpropertylist-vi.html language=enus -->
## TOPIC 00132: Get Model-Based Instrument Property List

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/modelbased/getmodelbasedinstrumentpropertylist-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/modelbased/getmodelbasedinstrumentpropertylist-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an object containing the name of the model and an array of model-based instrument property objects that contain the names and values of the instrument properties. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object.

### Get Model-Based Instrument Property List

Returns an object containing the name of the model and an array of model-based instrument property objects that contain the names and values of the instrument properties.

[IMAGE alt='icon' src='getmodelbasedinstrumentpropertylist-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Instrument Name — the name of the instrument you want to query for instrument properties. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Model-Based Instrument Property List — returns an object containing the name of the instrument model and an array of model-based instrument property objects that contain the name and value of a property defined for the instrument. Instrument Model — Properties — Property Name — Property Value — error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |
| Instrument Model — Properties — Property Name — Property Value — |
| Property Name — Property Value — |

Parent topic:

Model-Based

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/modelbased/getmodelbasedinstrumentpropertyvalue-vi.html language=enus -->
## TOPIC 00133: Get Model-Based Instrument Property Value

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/modelbased/getmodelbasedinstrumentpropertyvalue-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/modelbased/getmodelbasedinstrumentpropertyvalue-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value of a named property and a Boolean value indicating whether or not the named property was found in the property list supplied. icon Inputs/Outputs c1dcclst.png Properties an array of Model-Based Instrument Property elements to search. cstr.png Property Name cstr.png Property Value c

### Get Model-Based Instrument Property Value

Returns the value of a named property and a Boolean value indicating whether or not the named property was found in the property list supplied.

[IMAGE alt='icon' src='getmodelbasedinstrumentpropertyvalue-vi.png']

#### Inputs/Outputs

| Properties — an array of Model-Based Instrument Property elements to search. Property Name — Property Value — Property Name — specifies the name of the property for which to search. Properties Out — returns the array of model-based instrument property elements unchanged. Property Name — Property Value — Property Value — returns the found value for the named property. Is Found — returns TRUE if a property matching the supplied Property Name was found in the supplied array of model-based instrument property elements. |
| --- |
| Property Name — Property Value — |
| Property Name — Property Value — |

Parent topic:

Model-Based

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/modelbased/getmodelbasedinstrumentresourcepropertylist-vi.html language=enus -->
## TOPIC 00134: Get Model-Based Instrument Resource Property List

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/modelbased/getmodelbasedinstrumentresourcepropertylist-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/modelbased/getmodelbasedinstrumentresourcepropertylist-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of IModelBasedInstrumentResourcePropertyList objects where each element contains the name of a resource as well as an array of model-based instrument property objects that contain the names and values of the instrument resource properties. icon Inputs/Outputs coarn.png Semiconductor

### Get Model-Based Instrument Resource Property List

Returns an array of IModelBasedInstrumentResourcePropertyList objects where each element contains the name of a resource as well as an array of model-based instrument property objects that contain the names and values of the instrument resource properties.

[IMAGE alt='icon' src='getmodelbasedinstrumentresourcepropertylist-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Instrument Name — the name of the instrument you want to query for instrument properties. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Model-Based Instrument Resource Property List — returns an array of IModelBasedInstrumentResourcePropertyList objects where each element contains the name of the instrument resource and an array of model-based instrument property objects, each containing the name and value of a property defined for the instrument. Instrument Resource — Properties — Property Name — Property Value — error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |
| Instrument Resource — Properties — Property Name — Property Value — |
| Property Name — Property Value — |

Parent topic:

Model-Based

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/modelbased/getmodelbasedinstrumentresourcepropertyvalue-vi.html language=enus -->
## TOPIC 00135: Get Model-Based Instrument Resource Property Value

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/modelbased/getmodelbasedinstrumentresourcepropertyvalue-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/modelbased/getmodelbasedinstrumentresourcepropertyvalue-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value of a named property from a named resource and a Boolean value indicating whether or not the named property was found in the array of resource property lists supplied. icon Inputs/Outputs c1dcclst.png Model-Based Instrument Resource Property List an array of Model-Based Resource Pro

### Get Model-Based Instrument Resource Property Value

Returns the value of a named property from a named resource and a Boolean value indicating whether or not the named property was found in the array of resource property lists supplied.

[IMAGE alt='icon' src='getmodelbasedinstrumentresourcepropertyvalue-vi.png']

#### Inputs/Outputs

| Model-Based Instrument Resource Property List — an array of Model-Based Resource Property List elements to search. Instrument Resource — Properties — Property Name — Property Value — Property Name — specifies the name of the property for which to search. Resource Name — specifies the name of the resource to search for the specified property. Model-Based Instrument Resource Property List Out — returns the array of Model-Based Resource Property List elements unchanged. Instrument Resource — Properties — Property Name — Property Value — Property Value — returns the found value for the named property. Is Found — returns TRUE if a property matching the supplied Property Name was found in the supplied array of model-based instrument property elements. |
| --- |
| Instrument Resource — Properties — Property Name — Property Value — |
| Property Name — Property Value — |
| Instrument Resource — Properties — Property Name — Property Value — |
| Property Name — Property Value — |

Parent topic:

Model-Based

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/modelbased/modelbased-mnu.html language=enus -->
## TOPIC 00136: Model-Based

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/modelbased/modelbased-mnu.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/modelbased/modelbased-mnu.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-ModelBased VIs to manage NI-ModelBased instruments. icon

### Model-Based

Use the NI-ModelBased VIs to manage NI-ModelBased instruments.

[IMAGE alt='icon' src='modelbased-mnu.png']

- [Get All Model-Based Instrument Names](../../../../../menus/categories/ni-semiconductormodule/pinmap/modelbased/getallmodelbasedinstrumentnames-vi.html) Returns the instrument names and models for all Model-Based instruments in the Semiconductor Module context. You can use instrument names to query the model properties for the information needed to create the appropriate sessions to drive the instrument.
- [Get Model-Based Instrument Property List](../../../../../menus/categories/ni-semiconductormodule/pinmap/modelbased/getmodelbasedinstrumentpropertylist-vi.html) Returns an object containing the name of the model and an array of model-based instrument property objects that contain the names and values of the instrument properties.
- [Get Model-Based Instrument Resource Property List](../../../../../menus/categories/ni-semiconductormodule/pinmap/modelbased/getmodelbasedinstrumentresourcepropertylist-vi.html) Returns an array of IModelBasedInstrumentResourcePropertyList objects where each element contains the name of a resource as well as an array of model-based instrument property objects that contain the names and values of the instrument resource properties.
- [Get Model-Based Instrument Property Value](../../../../../menus/categories/ni-semiconductormodule/pinmap/modelbased/getmodelbasedinstrumentpropertyvalue-vi.html) Returns the value of a named property and a Boolean value indicating whether or not the named property was found in the property list supplied.
- [Get Model-Based Instrument Resource Property Value](../../../../../menus/categories/ni-semiconductormodule/pinmap/modelbased/getmodelbasedinstrumentresourcepropertyvalue-vi.html) Returns the value of a named property from a named resource and a Boolean value indicating whether or not the named property was found in the array of resource property lists supplied.

Parent topic:

Code Module Development

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/ni-teststand-semiconductormodule-mnu.html language=enus -->
## TOPIC 00137: Code Module Development

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/ni-teststand-semiconductormodule-mnu.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/ni-teststand-semiconductormodule-mnu.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI TestStand Semiconductor Module pin map VIs to query instrument names, open sessions on an instrument, obtain all open sessions, and translate pin names to sessions and channels. icon

### Code Module Development

Use the NI TestStand Semiconductor Module pin map VIs to query instrument names, open sessions on an instrument, obtain all open sessions, and translate pin names to sessions and channels.

[IMAGE alt='icon' src='ni-teststand-semiconductormodule-mnu.png']

- [Get Pin Names](../../../../menus/categories/ni-semiconductormodule/pinmap/general/getpinnames-vi.html) Returns all DUT and system pins available in the Semiconductor Module context that are connected to an instrument of the type you specify in the Instrument Type Id parameter. This VI returns only the pins specified on the Options tab of the Semiconductor Multi Test step. Pass an empty string to the Instrument Type Id parameter to return all available pins.
- [Publish Data](../../../../menus/categories/ni-semiconductormodule/pinmap/general/publish/publishdatawithcontext-vi.html) Publishes measurement data for one or more pins to the Semiconductor Multi Test step type instances for all sites in the Semiconductor Module context. If you are publishing site data, the polymorphic instance must publish data for each site in the Semiconductor Module context. If you are publishing pin data or pattern results, the polymorphic instance must support the pin query context obtained from the specific Pin(s) to Session(s), Pin to FPGA VI Reference(s), or Get Session Data VI you previously created. Pin(s) to Session(s) VIs include the following: Pin(s) to NI-Digital Pattern Sessions, Pin(s) to NI-DCPower Session(s), Pin(s) to NI-DAQmx Task(s), Pin(s) to NI-DMM Session(s), Pin(s) to NI-FGEN Session(s), Pin(s) to NI-SCOPE Session(s), Pin(s) to NI-HSDIO Session(s), Pin to NI-RFSA Session(s), Pin to NI-RFSG Session(s), and Pin to NI-RFmx Session(s).
- [Pin](../../../../menus/categories/ni-semiconductormodule/pinmap/tagprovider/tsm-pin-ctl.html) Contains a list of pins for the linked sequence file(s).
- [Published Data Id](../../../../menus/categories/ni-semiconductormodule/pinmap/tagprovider/tsm-publisheddataid-ctl.html) Contains a list of published data IDs for the linked sequence file(s). Displays only published data IDs for tests on a Semiconductor Multi Test step whose code module is set to the current VI.
- [NI-Digital Pattern](../../../../menus/categories/ni-semiconductormodule/pinmap/digital-pattern/nidigitalpattern-mnu.html) Use the NI-Digital Pattern VIs to manage NI-Digital Pattern instruments and sessions, to manage NI-Digital Pattern waveform data, and to access digital pattern project files.
- [NI-DCPower](../../../../menus/categories/ni-semiconductormodule/pinmap/dc-power/nidcpower-mnu.html) Use the NI-DCPower VIs to manage NI-DCPower instruments and sessions.
- [DAQmx](../../../../menus/categories/ni-semiconductormodule/pinmap/daqmx/daqmx-mnu.html) Use the NI-DAQmx VIs to manage NI-DAQmx tasks.
- [NI-DMM](../../../../menus/categories/ni-semiconductormodule/pinmap/dmm/nidmm-mnu.html) Use the NI-DMM VIs to manage NI-DMM instruments and sessions.
- [NI-FGEN](../../../../menus/categories/ni-semiconductormodule/pinmap/fgen/fgen-mnu.html) Use the NI-FGEN VIs to manage NI-FGEN instruments and sessions.
- [NI-SCOPE](../../../../menus/categories/ni-semiconductormodule/pinmap/scope/scope-mnu.html) Use the NI-SCOPE VIs to manage NI-SCOPE instruments and sessions.
- [RF](../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfintruments-mnu.html) Use the NI-RFSA, NI-RFSG, NI-RFmx, NI-RFPM, and FPGA VIs to manage NI-RFSA, NI-RFSG, NI-RFPM, and RF RIO (RF LabVIEW FPGA enabled) instruments.
- [Model-Based](../../../../menus/categories/ni-semiconductormodule/pinmap/modelbased/modelbased-mnu.html) Use the NI-ModelBased VIs to manage NI-ModelBased instruments.
- [NI-HSDIO](../../../../menus/categories/ni-semiconductormodule/pinmap/hsdio/nihsdiopinmap-mnu.html) Use the NI-HSDIO VIs to manage NI-HSDIO instruments and sessions and to create and rearrange multisite digital waveforms.
- [Switching](../../../../menus/categories/ni-semiconductormodule/pinmap/switching/switching-mnu.html) Use the Switching VIs to store and return switch sessions, return the names of all switches defined in the pin map, and access a switched pin.
- [Relay Driver](../../../../menus/categories/ni-semiconductormodule/pinmap/relay-driver/relaydriver-mnu.html) Use the Relay Driver VIs to manage NI PXI-2567 relay driver module sessions , NI-DAQmx tasks for the NI-DAQ digital output lines connected to the relays and to switch relays.
- [Custom Instruments](../../../../menus/categories/ni-semiconductormodule/pinmap/advanced/custom-instruments/custom-instruments-mnu.html) Use the Custom Instruments VIs to manage custom instruments and sessions.
- [Specifications](../../../../menus/categories/ni-semiconductormodule/pinmap/specs/specs-mnu.html) Use the Specifications VIs to obtain resolved values defined in the specification file the test program specifies.
- [Site and Global Data](../../../../menus/categories/ni-semiconductormodule/pinmap/site-and-global-data/site-and-global-data-mnu.html) Use the Site and Global data VIs to manage site and global data.
- [Alarms](../../../../menus/categories/ni-semiconductormodule/pinmap/alarms/alarms-mnu.html) Use the Alarms VIs to enable alarms, disable alarms, and to query for raised alarms on supported instruments.
- [Advanced](../../../../menus/categories/ni-semiconductormodule/pinmap/advanced/advanced-mnu.html) Use the Advanced VIs to create custom VIs for instruments that the TestStand Semiconductor Module does not natively support, query the site numbers in the Semiconductor Module context, and manage per-site and global data.

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/extract-pin-data-1d-array-bool-vi.html language=enus -->
## TOPIC 00138: Extract Pin Pass/Fail Data (1D)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/extract-pin-data-1d-array-bool-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/extract-pin-data-1d-array-bool-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Extracts the measurement data for a specified pin from a 1D array of Boolean measurements obtained from an instrument session and arranges the data in the order of sites in the Semiconductor Module Context. icon Inputs/Outputs cNI__TestStand__SemiconductorModule_lvlib_PinQueryContextlvclass.png Pin

### Extract Pin Pass/Fail Data (1D)

Extracts the measurement data for a specified pin from a 1D array of Boolean measurements obtained from an instrument session and arranges the data in the order of sites in the Semiconductor Module Context.

[IMAGE alt='icon' src='extract-pin-data-1d-array-bool-vi.png']

#### Inputs/Outputs

| Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Data In — is a 1D array of Boolean measurements obtained from multiple sites. Pin — specifies the pin for which to extract data. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Data Out — the multisite measurement from the Data In parameter for the specified pin rearranged into a 1D array with the order of the elements matching the site order in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Extract Pin Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/extract-pin-data-1d-array-double-vi.html language=enus -->
## TOPIC 00139: Extract Pin Parametric Data (1D)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/extract-pin-data-1d-array-double-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/extract-pin-data-1d-array-double-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Extracts the measurement data for a specified pin from a 1D array of double measurements obtained from an instrument session and arranges the data in the order of sites in the Semiconductor Module Context. icon Inputs/Outputs cNI__TestStand__SemiconductorModule_lvlib_PinQueryContextlvclass.png Pin Q

### Extract Pin Parametric Data (1D)

Extracts the measurement data for a specified pin from a 1D array of double measurements obtained from an instrument session and arranges the data in the order of sites in the Semiconductor Module Context.

[IMAGE alt='icon' src='extract-pin-data-1d-array-double-vi.png']

#### Inputs/Outputs

| Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Data In — is a 1D array of double measurements obtained from multiple sites. Pin — specifies the pin for which to extract data. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Data Out — the multisite measurement from the Data In parameter for the specified pin rearranged into a 1D array with the order of the elements matching the site order in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Extract Pin Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/extract-pin-data-2d-array-bool-vi.html language=enus -->
## TOPIC 00140: Extract Pin Pass/Fail Data (2D)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/extract-pin-data-2d-array-bool-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/extract-pin-data-2d-array-bool-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Extracts the measurement data for a specified pin from a 2D array of Boolean measurements obtained from an instrument session and arranges the data in the order of sites in the Semiconductor Module Context. icon Inputs/Outputs cNI__TestStand__SemiconductorModule_lvlib_PinQueryContextlvclass.png Pin

### Extract Pin Pass/Fail Data (2D)

Extracts the measurement data for a specified pin from a 2D array of Boolean measurements obtained from an instrument session and arranges the data in the order of sites in the Semiconductor Module Context.

[IMAGE alt='icon' src='extract-pin-data-2d-array-bool-vi.png']

#### Inputs/Outputs

| Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Data In — is a 2D array of Boolean measurements obtained from multiple sites. Pin — specifies the pin for which to extract data. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Data Out — the multisite measurement from the Data In parameter for the specified pin rearranged into a 1D array with the order of the elements matching the site order in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Extract Pin Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/extract-pin-data-2d-array-double-vi.html language=enus -->
## TOPIC 00141: Extract Pin Parametric Data (2D)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/extract-pin-data-2d-array-double-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/extract-pin-data-2d-array-double-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Extracts the measurement data for a specified pin from a 2D array of double measurements obtained from an instrument session and arranges the data in the order of sites in the Semiconductor Module Context. icon Inputs/Outputs cNI__TestStand__SemiconductorModule_lvlib_PinQueryContextlvclass.png Pin Q

### Extract Pin Parametric Data (2D)

Extracts the measurement data for a specified pin from a 2D array of double measurements obtained from an instrument session and arranges the data in the order of sites in the Semiconductor Module Context.

[IMAGE alt='icon' src='extract-pin-data-2d-array-double-vi.png']

#### Inputs/Outputs

| Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Data In — is a 2D array of double measurements obtained from multiple sites. Pin — specifies the pin for which to extract data. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Data Out — the multisite measurement from the Data In parameter for the specified pin rearranged into a 1D array with the order of the elements matching the site order in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Extract Pin Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/extractpindata-vi.html language=enus -->
## TOPIC 00142: Extract Pin Data

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/extractpindata-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/extractpindata-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Extracts the measurement data for a specified pin from measurements obtained from an instrument session and arranges the data in the order of sites in the Semiconductor Module context. Use this VI when you have raw measurement data from an instrument session that you need to manipulate in a site-spe

### Extract Pin Data

Extracts the measurement data for a specified pin from measurements obtained from an instrument session and arranges the data in the order of sites in the Semiconductor Module context.

Use this VI when you have raw measurement data from an instrument session that you need to manipulate in a site-specific way. For example, if you need to perform an operation on the measurement data using per-site input data, this VI puts the measurement data for the selected pin into the same per-site order as the input data. Similarly, if you need to modify the data from a specific site before publishing, this VI puts the measurement data for the selected pin into a per-site array that you can then index to retrieve the data for the specific site. The order of the per-site array matches the order of the **Site Numbers** output parameter of the Get Site Numbers VI. You can use the Per-Site Publish VI to publish the resulting manipulated data.

[IMAGE alt='icon' src='extractpindata-vi.png']

- [Extract Pin Parametric Data (1D)](../../../../../menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/extract-pin-data-1d-array-double-vi.html) Extracts the measurement data for a specified pin from a 1D array of double measurements obtained from an instrument session and arranges the data in the order of sites in the Semiconductor Module Context.
- [Extract Pin Pass/Fail Data (1D)](../../../../../menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/extract-pin-data-1d-array-bool-vi.html) Extracts the measurement data for a specified pin from a 1D array of Boolean measurements obtained from an instrument session and arranges the data in the order of sites in the Semiconductor Module Context.
- [Extract Pin Parametric Data (2D)](../../../../../menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/extract-pin-data-2d-array-double-vi.html) Extracts the measurement data for a specified pin from a 2D array of double measurements obtained from an instrument session and arranges the data in the order of sites in the Semiconductor Module Context.
- [Extract Pin Pass/Fail Data (2D)](../../../../../menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/extract-pin-data-2d-array-bool-vi.html) Extracts the measurement data for a specified pin from a 2D array of Boolean measurements obtained from an instrument session and arranges the data in the order of sites in the Semiconductor Module Context.

Parent topic:

Advanced

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/per-instrument-to-per-site-data-1d-array-bool-vi.html language=enus -->
## TOPIC 00143: Per-Instrument To Per-Site Pass/Fail Data (1D)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/per-instrument-to-per-site-data-1d-array-bool-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/per-instrument-to-per-site-data-1d-array-bool-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts measurement data from a 1D array of Boolean measurements that is ordered by channels on a single instrument session into a 2D array that is arranged by the sites and pins in the Semiconductor Module Context. icon Inputs/Outputs cNI__TestStand__SemiconductorModule_lvlib_PinQueryContextlvclas

### Per-Instrument To Per-Site Pass/Fail Data (1D)

Converts measurement data from a 1D array of Boolean measurements that is ordered by channels on a single instrument session into a 2D array that is arranged by the sites and pins in the Semiconductor Module Context.

[IMAGE alt='icon' src='per-instrument-to-per-site-data-1d-array-bool-vi.png']

#### Inputs/Outputs

| Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Per-Instrument Data — specifies the multisite measurement data from multiple pins connected to one or more instrument sessions. The array consists of either a collection of single measurements made from multiple instrument sessions or a collection of multiple measurements made from a single instrument session. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Per-Site/Pin Data — the multisite measurement data from the Data In parameter rearranged by sites and pins. Each row represents measurements for one site, and each column represents a measurement for a pin in the pin query context. Use the Get Site Numbers VI to get the site number for each row. The order of the columns matches the order of the pins parameter in the pin query. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Per-Instrument to Per-Site Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/per-instrument-to-per-site-data-1d-array-double-vi.html language=enus -->
## TOPIC 00144: Per-Instrument To Per-Site Parametric Data (1D)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/per-instrument-to-per-site-data-1d-array-double-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/per-instrument-to-per-site-data-1d-array-double-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts measurement data from a 1D array of double measurements that is ordered by channels on a single instrument session into a 2D array that is arranged by the sites and pins in the Semiconductor Module Context. icon Inputs/Outputs cNI__TestStand__SemiconductorModule_lvlib_PinQueryContextlvclass

### Per-Instrument To Per-Site Parametric Data (1D)

Converts measurement data from a 1D array of double measurements that is ordered by channels on a single instrument session into a 2D array that is arranged by the sites and pins in the Semiconductor Module Context.

[IMAGE alt='icon' src='per-instrument-to-per-site-data-1d-array-double-vi.png']

#### Inputs/Outputs

| Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Per-Instrument Data — specifies the multisite measurement data from multiple pins connected to one or more instrument sessions. The array consists of either a collection of single measurements made from multiple instrument sessions or a collection of multiple measurements made from a single instrument session. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Per-Site/Pin Data — the multisite measurement data from the Data In parameter rearranged by sites and pins. Each row represents measurements for one site, and each column represents a measurement for a pin in the pin query context. Use the Get Site Numbers VI to get the site number for each row. The order of the columns matches the order of the pins parameter in the pin query. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Per-Instrument to Per-Site Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/per-instrument-to-per-site-data-2d-array-bool-vi.html language=enus -->
## TOPIC 00145: Per-Instrument To Per-Site Pass/Fail Data (2D)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/per-instrument-to-per-site-data-2d-array-bool-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/per-instrument-to-per-site-data-2d-array-bool-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Transforms measurement data from a 2D array of Boolean measurements that is arranged by instrument sessions and channels into a 2D array that is arranged by the sites and pins in the Semiconductor Module Context. icon Inputs/Outputs cNI__TestStand__SemiconductorModule_lvlib_MultipleSessionPinQueryCo

### Per-Instrument To Per-Site Pass/Fail Data (2D)

Transforms measurement data from a 2D array of Boolean measurements that is arranged by instrument sessions and channels into a 2D array that is arranged by the sites and pins in the Semiconductor Module Context.

[IMAGE alt='icon' src='per-instrument-to-per-site-data-2d-array-bool-vi.png']

#### Inputs/Outputs

| Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Per-Instrument Data — specifies the multisite measurement data from multiple pins connected to multiple instrument sessions. Each row represents measurements from one instrument session, and each column represents each channel on that instrument session. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Per-Site/Pin Data — the multisite measurement data from the Data In parameter rearranged by sites and pins. Each row represents measurements for one site, and each column represents a measurement for a pin in the pin query context. Use the Get Site Numbers VI to get the site number for each row. The order of the columns matches the order of the pins parameter in the pin query. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Per-Instrument to Per-Site Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/per-instrument-to-per-site-data-2d-array-double-vi.html language=enus -->
## TOPIC 00146: Per-Instrument To Per-Site Parametric Data (2D)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/per-instrument-to-per-site-data-2d-array-double-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/pinquerycontext/per-instrument-to-per-site-data-2d-array-double-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Transforms measurement data from a 2D array of double measurements that is arranged by instrument sessions and channels into a 2D array that is arranged by the sites and pins in the Semiconductor Module Context. icon Inputs/Outputs cNI__TestStand__SemiconductorModule_lvlib_MultipleSessionPinQueryCon

### Per-Instrument To Per-Site Parametric Data (2D)

Transforms measurement data from a 2D array of double measurements that is arranged by instrument sessions and channels into a 2D array that is arranged by the sites and pins in the Semiconductor Module Context.

[IMAGE alt='icon' src='per-instrument-to-per-site-data-2d-array-double-vi.png']

#### Inputs/Outputs

| Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Per-Instrument Data — specifies the multisite measurement data from multiple pins connected to multiple instrument sessions. Each row represents measurements from one instrument session, and each column represents each channel on that instrument session. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Per-Site/Pin Data — the multisite measurement data from the Data In parameter rearranged by sites and pins. Each row represents measurements for one site, and each column represents a measurement for a pin in the pin query context. Use the Get Site Numbers VI to get the site number for each row. The order of the columns matches the order of the pins parameter in the pin query. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Per-Instrument to Per-Site Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/relay-driver/applyrelayconfiguration-vi.html language=enus -->
## TOPIC 00147: Apply Relay Configuration

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/relay-driver/applyrelayconfiguration-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/relay-driver/applyrelayconfiguration-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the relay actions on the relays in the relay configuration. icon Inputs/Outputs cdbl.png Wait (s) specifies the time to wait, in seconds, for the relays to settle after performing the relay action. This input is optional. The default is 0s. coarn.png Semiconductor Module Context is a valid

### Apply Relay Configuration

Performs the relay actions on the relays in the relay configuration.

[IMAGE alt='icon' src='applyrelayconfiguration-vi.png']

#### Inputs/Outputs

| Wait (s) — specifies the time to wait, in seconds, for the relays to settle after performing the relay action. This input is optional. The default is 0s. Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Relay Configuration — specifies the name of the relay configuration. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Control Relay(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/relay-driver/controlrelay-s-vi.html language=enus -->
## TOPIC 00148: Control Relay(s)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/relay-driver/controlrelay-s-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/relay-driver/controlrelay-s-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs relay actions on one or more relays. You must manually select the polymorphic instance you want to use. Select the single relay or multiple relays polymorphic instance based on the number of relays for which you perform the actions. icon

### Control Relay(s)

Performs relay actions on one or more relays. You must manually select the polymorphic instance you want to use. Select the single relay or multiple relays polymorphic instance based on the number of relays for which you perform the actions.

[IMAGE alt='icon' src='controlrelay-s-vi.png']

- [Apply Relay Configuration](../../../../../menus/categories/ni-semiconductormodule/pinmap/relay-driver/applyrelayconfiguration-vi.html) Performs the relay actions on the relays in the relay configuration.
- [Control Relay](../../../../../menus/categories/ni-semiconductormodule/pinmap/relay-driver/controlrelaysingleaction-vi.html) Performs the relay action on the relay.
- [Control Relays](../../../../../menus/categories/ni-semiconductormodule/pinmap/relay-driver/controlrelayssingleaction-vi.html) Performs the relay action on the relays.
- [Control Relays](../../../../../menus/categories/ni-semiconductormodule/pinmap/relay-driver/controlrelaysmultipleactions-vi.html) Performs the relay actions on the relays.

Parent topic:

Relay Driver

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/relay-driver/controlrelaysingleaction-vi.html language=enus -->
## TOPIC 00149: Control Relay

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/relay-driver/controlrelaysingleaction-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/relay-driver/controlrelaysingleaction-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the relay action on the relay. icon Inputs/Outputs cdbl.png Wait (s) specifies the time to wait, in seconds, for the relays to settle after performing the relay action. This input is optional. The default is 0s. coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semico

### Control Relay

Performs the relay action on the relay.

[IMAGE alt='icon' src='controlrelaysingleaction-vi.png']

#### Inputs/Outputs

| Wait (s) — specifies the time to wait, in seconds, for the relays to settle after performing the relay action. This input is optional. The default is 0s. Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Relay — specifies the name of the relay or relay group that identifies the relays. — specifies to open or close all identified relays. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Control Relay(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/relay-driver/controlrelaysmultipleactions-vi.html language=enus -->
## TOPIC 00150: Control Relays

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/relay-driver/controlrelaysmultipleactions-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/relay-driver/controlrelaysmultipleactions-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the relay actions on the relays. icon Inputs/Outputs cdbl.png Wait (s) specifies the time to wait, in seconds, for the relays to settle after performing all relay actions. This input is optional. The default is 0s. coarn.png Semiconductor Module Context is a valid ActiveX reference to a Sem

### Control Relays

Performs the relay actions on the relays.

[IMAGE alt='icon' src='controlrelaysmultipleactions-vi.png']

#### Inputs/Outputs

| Wait (s) — specifies the time to wait, in seconds, for the relays to settle after performing all relay actions. This input is optional. The default is 0s. Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Relays — specifies the names of the relays or relay groups that identify the relays. Relay Actions — specifies to open or close the relays identified by the corresponding relay or relay group. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Control Relay(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/relay-driver/controlrelayssingleaction-vi.html language=enus -->
## TOPIC 00151: Control Relays

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/relay-driver/controlrelayssingleaction-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/relay-driver/controlrelayssingleaction-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the relay action on the relays. icon Inputs/Outputs cdbl.png Wait (s) specifies the time to wait, in seconds, for the relays to settle after performing the relay action. This input is optional. The default is 0s. coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semic

### Control Relays

Performs the relay action on the relays.

[IMAGE alt='icon' src='controlrelayssingleaction-vi.png']

#### Inputs/Outputs

| Wait (s) — specifies the time to wait, in seconds, for the relays to settle after performing the relay action. This input is optional. The default is 0s. Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Relays — specifies the names of the relays or relay groups that identify the relays. — specifies to open or close all identified relays. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Control Relay(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/relay-driver/getallrelaydriverniswitchsessions-vi.html language=enus -->
## TOPIC 00152: Get All Relay Driver NI-SWITCH Sessions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/relay-driver/getallrelaydriverniswitchsessions-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/relay-driver/getallrelaydriverniswitchsessions-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns NI-SWITCH sessions for all relay driver modules in the Semiconductor Module context. You can use the NI-SWITCH sessions to close the relay driver module sessions. Note: Calling the Close VI on the returned sessions does not close the sessions if you did not open the session in LabVIEW. icon

### Get All Relay Driver NI-SWITCH Sessions

Returns NI-SWITCH sessions for all relay driver modules in the Semiconductor Module context. You can use the NI-SWITCH sessions to close the relay driver module sessions. Note: Calling the Close VI on the returned sessions does not close the sessions if you did not open the session in LabVIEW.

[IMAGE alt='icon' src='getallrelaydriverniswitchsessions-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. NI-SWITCH Sessions — returns the NI-SWITCH sessions for all relay driver modules in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Relay Driver

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/relay-driver/getrelaydrivermodulenames-vi.html language=enus -->
## TOPIC 00153: Get Relay Driver Module Names

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/relay-driver/getrelaydrivermodulenames-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/relay-driver/getrelaydrivermodulenames-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the names of all relay driver modules in the Semiconductor Module context. You can use the relay driver module names to open NI-SWITCH driver sessions for the relay driver modules. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Modu

### Get Relay Driver Module Names

Returns the names of all relay driver modules in the Semiconductor Module context. You can use the relay driver module names to open NI-SWITCH driver sessions for the relay driver modules.

[IMAGE alt='icon' src='getrelaydrivermodulenames-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Module Names — returns an array of the relay driver module names in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Relay Driver

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/relay-driver/getrelaynames-vi.html language=enus -->
## TOPIC 00154: Get Relay Names

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/relay-driver/getrelaynames-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/relay-driver/getrelaynames-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns all site and system relays available in the Semiconductor Module context. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cerrcodeclst.png error in (no error) describes error conditions that occur before this V

### Get Relay Names

Returns all site and system relays available in the Semiconductor Module context.

[IMAGE alt='icon' src='getrelaynames-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Site Relays — returns an array of strings that contains the site relays in the Semiconductor Module context. System Relays — returns an array of strings that contains the system relays in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Relay Driver

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/relay-driver/relay-s-torelaydrivernidaqmxtask-s-vi.html language=enus -->
## TOPIC 00155: Relay(s) To Relay Driver NI-DAQmx Task(s)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/relay-driver/relay-s-torelaydrivernidaqmxtask-s-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/relay-driver/relay-s-torelaydrivernidaqmxtask-s-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-DAQmx Tasks required to access one or more relays connected to NI-DAQ modules. You must manually select the polymorphic instance you want to use. Select the single relay or multiple relays polymorphic instance based on the number of relays the test is designed to test. Select the sing

### Relay(s) To Relay Driver NI-DAQmx Task(s)

Returns the NI-DAQmx Tasks required to access one or more relays connected to NI-DAQ modules. You must manually select the polymorphic instance you want to use. Select the single relay or multiple relays polymorphic instance based on the number of relays the test is designed to test. Select the single task or multiple task polymorphic instance based on the number of DAQmx tasks you expect to be returned. Use the single module instance only when you know the code module will never be used with a relay that will return more than one DAQmx task.

[IMAGE alt='icon' src='relay-s-torelaydrivernidaqmxtask-s-vi.png']

- [Relays To Relay Driver NI-DAQmx Tasks](../../../../../menus/categories/ni-semiconductormodule/pinmap/relay-driver/relaystorelaydrivernidaqmxtasks-vi.html) Returns the NI-DAQmx tasks required to control the relays connected to digital output lines of an NI-DAQ module.
- [Relay To Relay Driver NI-DAQmx Task](../../../../../menus/categories/ni-semiconductormodule/pinmap/relay-driver/relaytorelaydrivernidaqmxtask-vi.html) Returns the NI-DAQmx task required to control the relay connected to digital output line of an NI-DAQ module. If more than one task is required to access the relay, the VI returns an error.
- [Relay To Relay Driver NI-DAQmx Tasks](../../../../../menus/categories/ni-semiconductormodule/pinmap/relay-driver/relaytorelaydrivernidaqmxtasks-vi.html) Returns the NI-DAQmx tasks required to control the relays connected to digital output lines of an NI-DAQ module.

Parent topic:

Relay Driver

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/relay-driver/relay-s-torelaydriverniswitchsession-s-vi.html language=enus -->
## TOPIC 00156: Relay(s) To Relay Driver NI-SWITCH Session(s)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/relay-driver/relay-s-torelaydriverniswitchsession-s-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/relay-driver/relay-s-torelaydriverniswitchsession-s-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-SWITCH sessions and relay names required to access one or more relays connected to relay driver modules. You must manually select the polymorphic instance you want to use. Select the single relay or multiple relays polymorphic instance based on the number of relays the test is designe

### Relay(s) To Relay Driver NI-SWITCH Session(s)

Returns the NI-SWITCH sessions and relay names required to access one or more relays connected to relay driver modules. You must manually select the polymorphic instance you want to use. Select the single relay or multiple relays polymorphic instance based on the number of relays the test is designed to test. Select the single module or multiple module polymorphic instance based on the number of relay driver modules you expect the relay to be connected to in the pin map. Use the multiple module polymorphic instances to ensure that code modules work with any pin map. Use the single module instance only when you know the code module will never be used with a pin map that has more than one relay driver module connected to the specified relays.

[IMAGE alt='icon' src='relay-s-torelaydriverniswitchsession-s-vi.png']

- [Relays To Relay Driver NI-SWITCH Session](../../../../../menus/categories/ni-semiconductormodule/pinmap/relay-driver/relaystorelaydriverniswitchsession-vi.html) Returns the NI-SWITCH session and relay names required to access the relays connected to a relay driver module. If more than one session is required to access the relays, the VI returns an error.
- [Relays To Relay Driver NI-SWITCH Sessions](../../../../../menus/categories/ni-semiconductormodule/pinmap/relay-driver/relaystorelaydriverniswitchsessions-vi.html) Returns the NI-SWITCH sessions and relay names required to access the relays connected to relay driver modules.
- [Relay To Relay Driver NI-SWITCH Session](../../../../../menus/categories/ni-semiconductormodule/pinmap/relay-driver/relaytorelaydriverniswitchsession-vi.html) Returns the NI-SWITCH session and relay names required to access the relay connected to a relay driver module. If more than one session is required to access the relay, the VI returns an error.
- [Relay To Relay Driver NI-SWITCH Sessions](../../../../../menus/categories/ni-semiconductormodule/pinmap/relay-driver/relaytorelaydriverniswitchsessions-vi.html) Returns the NI-SWITCH sessions and relay names required to access the relay connected to relay driver modules.

Parent topic:

Relay Driver

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/relay-driver/relaydriver-mnu.html language=enus -->
## TOPIC 00157: Relay Driver

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/relay-driver/relaydriver-mnu.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/relay-driver/relaydriver-mnu.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Relay Driver VIs to manage NI PXI-2567 relay driver module sessions , NI-DAQmx tasks for the NI-DAQ digital output lines connected to the relays and to switch relays. icon

### Relay Driver

Use the Relay Driver VIs to manage NI PXI-2567 relay driver module sessions , NI-DAQmx tasks for the NI-DAQ digital output lines connected to the relays and to switch relays.

[IMAGE alt='icon' src='relaydriver-mnu.png']

- [Get Relay Driver Module Names](../../../../../menus/categories/ni-semiconductormodule/pinmap/relay-driver/getrelaydrivermodulenames-vi.html) Returns the names of all relay driver modules in the Semiconductor Module context. You can use the relay driver module names to open NI-SWITCH driver sessions for the relay driver modules.
- [Get All Relay Driver NI-SWITCH Sessions](../../../../../menus/categories/ni-semiconductormodule/pinmap/relay-driver/getallrelaydriverniswitchsessions-vi.html) Returns NI-SWITCH sessions for all relay driver modules in the Semiconductor Module context. You can use the NI-SWITCH sessions to close the relay driver module sessions. Note: Calling the Close VI on the returned sessions does not close the sessions if you did not open the session in LabVIEW.
- [Set Relay Driver NI-SWITCH Session](../../../../../menus/categories/ni-semiconductormodule/pinmap/relay-driver/setrelaydriverniswitchsession-vi.html) Associates an NI-SWITCH session with a relay driver module.
- [Relay(s) To Relay Driver NI-SWITCH Session(s)](../../../../../menus/categories/ni-semiconductormodule/pinmap/relay-driver/relay-s-torelaydriverniswitchsession-s-vi.html) Returns the NI-SWITCH sessions and relay names required to access one or more relays connected to relay driver modules. You must manually select the polymorphic instance you want to use. Select the single relay or multiple relays polymorphic instance based on the number of relays the test is designed to test. Select the single module or multiple module polymorphic instance based on the number of relay driver modules you expect the relay to be connected to in the pin map. Use the multiple module polymorphic instances to ensure that code modules work with any pin map. Use the single module instance only when you know the code module will never be used with a pin map that has more than one relay driver module connected to the specified relays.
- [Relay(s) To Relay Driver NI-DAQmx Task(s)](../../../../../menus/categories/ni-semiconductormodule/pinmap/relay-driver/relay-s-torelaydrivernidaqmxtask-s-vi.html) Returns the NI-DAQmx Tasks required to access one or more relays connected to NI-DAQ modules. You must manually select the polymorphic instance you want to use. Select the single relay or multiple relays polymorphic instance based on the number of relays the test is designed to test. Select the single task or multiple task polymorphic instance based on the number of DAQmx tasks you expect to be returned. Use the single module instance only when you know the code module will never be used with a relay that will return more than one DAQmx task.
- [Get Relay Names](../../../../../menus/categories/ni-semiconductormodule/pinmap/relay-driver/getrelaynames-vi.html) Returns all site and system relays available in the Semiconductor Module context.
- [Relay](../../../../../menus/categories/ni-semiconductormodule/pinmap/tagprovider/tsm-relay-ctl.html) Contains a list of relays for the linked sequence file(s).
- [Relay Configuration](../../../../../menus/categories/ni-semiconductormodule/pinmap/tagprovider/tsm-relayconfiguration-ctl.html) Contains a list of relay configurations for the linked sequence file(s).
- [Control Relay(s)](../../../../../menus/categories/ni-semiconductormodule/pinmap/relay-driver/controlrelay-s-vi.html) Performs relay actions on one or more relays. You must manually select the polymorphic instance you want to use. Select the single relay or multiple relays polymorphic instance based on the number of relays for which you perform the actions.

Parent topic:

Code Module Development

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/relay-driver/relaystorelaydrivernidaqmxtasks-vi.html language=enus -->
## TOPIC 00158: Relays To Relay Driver NI-DAQmx Tasks

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/relay-driver/relaystorelaydrivernidaqmxtasks-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/relay-driver/relaystorelaydrivernidaqmxtasks-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-DAQmx tasks required to control the relays connected to digital output lines of an NI-DAQ module. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. c1ddaqmxscale.png Relays The names of the relays or relay

### Relays To Relay Driver NI-DAQmx Tasks

Returns the NI-DAQmx tasks required to control the relays connected to digital output lines of an NI-DAQ module.

[IMAGE alt='icon' src='relaystorelaydrivernidaqmxtasks-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Relays — The names of the relays or relay groups to translate to NI-DAQmx tasks. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. DAQmx Tasks — Returns the NI-DAQmx tasks for the NI-DAQ digital output lines connected to the relays for all sites in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Relay(s) To Relay Driver NI-DAQmx Task(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/relay-driver/relaystorelaydriverniswitchsession-vi.html language=enus -->
## TOPIC 00159: Relays To Relay Driver NI-SWITCH Session

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/relay-driver/relaystorelaydriverniswitchsession-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/relay-driver/relaystorelaydriverniswitchsession-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-SWITCH session and relay names required to access the relays connected to a relay driver module. If more than one session is required to access the relays, the VI returns an error. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconduct

### Relays To Relay Driver NI-SWITCH Session

Returns the NI-SWITCH session and relay names required to access the relays connected to a relay driver module. If more than one session is required to access the relays, the VI returns an error.

[IMAGE alt='icon' src='relaystorelaydriverniswitchsession-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Relays — is the names of the relays or relay groups to translate to an NI-SWITCH session and relay names. If more than one session is required, the VI returns an error. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. NI-SWITCH Session — returns the NI-SWITCH session for the relay driver module connected to the relays for all sites in the Semiconductor Module context. NI-SWITCH Relay Names — returns a comma-separated list of relay names for the relay driver module session connected to the relays for all sites in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Relay(s) To Relay Driver NI-SWITCH Session(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/relay-driver/relaystorelaydriverniswitchsessions-vi.html language=enus -->
## TOPIC 00160: Relays To Relay Driver NI-SWITCH Sessions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/relay-driver/relaystorelaydriverniswitchsessions-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/relay-driver/relaystorelaydriverniswitchsessions-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-SWITCH sessions and relay names required to access the relays connected to relay driver modules. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. c1ddaqmxscale.png Relays is the names of the relays or rel

### Relays To Relay Driver NI-SWITCH Sessions

Returns the NI-SWITCH sessions and relay names required to access the relays connected to relay driver modules.

[IMAGE alt='icon' src='relaystorelaydriverniswitchsessions-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Relays — is the names of the relays or relay groups to translate to NI-SWITCH sessions and relay names. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. NI-SWITCH Sessions — returns NI-SWITCH sessions for the relay driver modules connected to the relays for all sites in the Semiconductor Module context. NI-SWITCH Relay Names — returns comma-separated lists of relay names for the relay driver module sessions connected to the relays for all sites in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Relay(s) To Relay Driver NI-SWITCH Session(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/relay-driver/relaytorelaydrivernidaqmxtask-vi.html language=enus -->
## TOPIC 00161: Relay To Relay Driver NI-DAQmx Task

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/relay-driver/relaytorelaydrivernidaqmxtask-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/relay-driver/relaytorelaydrivernidaqmxtask-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-DAQmx task required to control the relay connected to digital output line of an NI-DAQ module. If more than one task is required to access the relay, the VI returns an error. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Mod

### Relay To Relay Driver NI-DAQmx Task

Returns the NI-DAQmx task required to control the relay connected to digital output line of an NI-DAQ module. If more than one task is required to access the relay, the VI returns an error.

[IMAGE alt='icon' src='relaytorelaydrivernidaqmxtask-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Relay — is the name of the relay to translate to NI-DAQmx task. If more than one task is required, the VI returns an error. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. DAQmx Task — returns the NI-DAQmx task for the NI-DAQ digital output line connected to the relay. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Relay(s) To Relay Driver NI-DAQmx Task(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/relay-driver/relaytorelaydrivernidaqmxtasks-vi.html language=enus -->
## TOPIC 00162: Relay To Relay Driver NI-DAQmx Tasks

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/relay-driver/relaytorelaydrivernidaqmxtasks-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/relay-driver/relaytorelaydrivernidaqmxtasks-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-DAQmx tasks required to control the relays connected to digital output lines of an NI-DAQ module. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cdaqmxscale.png Relay is the name of the relay or relay g

### Relay To Relay Driver NI-DAQmx Tasks

Returns the NI-DAQmx tasks required to control the relays connected to digital output lines of an NI-DAQ module.

[IMAGE alt='icon' src='relaytorelaydrivernidaqmxtasks-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Relay — is the name of the relay or relay group to translate to NI-DAQmx Tasks. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. DAQmx Tasks — returns the NI-DAQmx tasks for the NI-DAQ digital output lines connected to the relays for all sites in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Relay(s) To Relay Driver NI-DAQmx Task(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/relay-driver/relaytorelaydriverniswitchsession-vi.html language=enus -->
## TOPIC 00163: Relay To Relay Driver NI-SWITCH Session

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/relay-driver/relaytorelaydriverniswitchsession-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/relay-driver/relaytorelaydriverniswitchsession-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-SWITCH session and relay names required to access the relay connected to a relay driver module. If more than one session is required to access the relay, the VI returns an error. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor

### Relay To Relay Driver NI-SWITCH Session

Returns the NI-SWITCH session and relay names required to access the relay connected to a relay driver module. If more than one session is required to access the relay, the VI returns an error.

[IMAGE alt='icon' src='relaytorelaydriverniswitchsession-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Relay — is the name of the relay or relay group to translate to an NI-SWITCH session and relay names. If more than one session is required, the VI returns an error. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. NI-SWITCH Session — returns the NI-SWITCH session for the relay driver module connected to the relay for all sites in the Semiconductor Module context. NI-SWITCH Relay Names — returns a comma-separated list of relay names for the relay driver module session connected to the relay for all sites in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Relay(s) To Relay Driver NI-SWITCH Session(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/relay-driver/relaytorelaydriverniswitchsessions-vi.html language=enus -->
## TOPIC 00164: Relay To Relay Driver NI-SWITCH Sessions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/relay-driver/relaytorelaydriverniswitchsessions-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/relay-driver/relaytorelaydriverniswitchsessions-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-SWITCH sessions and relay names required to access the relay connected to relay driver modules. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cdaqmxscale.png Relay is the name of the relay or relay gro

### Relay To Relay Driver NI-SWITCH Sessions

Returns the NI-SWITCH sessions and relay names required to access the relay connected to relay driver modules.

[IMAGE alt='icon' src='relaytorelaydriverniswitchsessions-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Relay — is the name of the relay or relay group to translate to NI-SWITCH sessions and relay names. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. NI-SWITCH Sessions — returns NI-SWITCH sessions for the relay driver modules connected to the relay for all sites in the Semiconductor Module context. NI-SWITCH Relay Names — returns comma-separated lists of relay names for the relay driver module sessions connected to the relay for all sites in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Relay(s) To Relay Driver NI-SWITCH Session(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/relay-driver/setrelaydriverniswitchsession-vi.html language=enus -->
## TOPIC 00165: Set Relay Driver NI-SWITCH Session

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/relay-driver/setrelaydriverniswitchsession-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/relay-driver/setrelaydriverniswitchsession-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Associates an NI-SWITCH session with a relay driver module. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cstr.png Relay Driver Module Name is the relay driver module name in the pin map file for the corresponding se

### Set Relay Driver NI-SWITCH Session

Associates an NI-SWITCH session with a relay driver module.

[IMAGE alt='icon' src='setrelaydriverniswitchsession-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Relay Driver Module Name — is the relay driver module name in the pin map file for the corresponding session. NI-SWITCH Session — specifies the NI-SWITCH session for the corresponding relay driver module name. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Relay Driver

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/fpga/getallfpgainstrumentnames-vi.html language=enus -->
## TOPIC 00166: Get All FPGA Instrument Names

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/fpga/getallfpgainstrumentnames-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/fpga/getallfpgainstrumentnames-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the instrument names for all FPGA-enabled RF instruments in the Semiconductor Module context. You can use instrument names to open driver sessions. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cerrcodeclst.p

### Get All FPGA Instrument Names

Returns the instrument names for all FPGA-enabled RF instruments in the Semiconductor Module context. You can use instrument names to open driver sessions.

[IMAGE alt='icon' src='getallfpgainstrumentnames-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Names — returns an array of names of NI-RF instruments that support NI-RIO in the Semiconductor Module context. FPGA File Paths — returns an array of FPGA file paths associated with the Instrument Names parameter. If the path is an absolute path, the VI returns the absolute path whether the file exists or not. If the path is a relative path and the file exists relative to the path of the pin map file, the VI returns the absolute path of the existing file. Otherwise, the VI returns a string without error. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FPGA

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/fpga/getallfpgavireferences-vi.html language=enus -->
## TOPIC 00167: Get All FPGA VI References

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/fpga/getallfpgavireferences-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/fpga/getallfpgavireferences-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns all FPGA VI references in the Semiconductor Module context. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cerrcodeclst.png error in (no error) describes error conditions that occur before this VI or function

### Get All FPGA VI References

Returns all FPGA VI references in the Semiconductor Module context.

[IMAGE alt='icon' src='getallfpgavireferences-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. FPGA VI References — returns all FPGA VI references in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FPGA

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/fpga/nivst-mnu.html language=enus -->
## TOPIC 00168: FPGA

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/fpga/nivst-mnu.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/fpga/nivst-mnu.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the FPGA VIs to manage FPGA sessions for RF RIO instruments (RF LabVIEW FPGA enabled instruments). icon

### FPGA

Use the FPGA VIs to manage FPGA sessions for RF RIO instruments (RF LabVIEW FPGA enabled instruments).

[IMAGE alt='icon' src='nivst-mnu.png']

- [Get All FPGA Instrument Names](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/fpga/getallfpgainstrumentnames-vi.html) Returns the instrument names for all FPGA-enabled RF instruments in the Semiconductor Module context. You can use instrument names to open driver sessions.
- [Set FPGA VI Reference](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/fpga/setfpgavireference-vi.html) Associates an instrument session with an FPGA-enabled instrument name.
- [Get All FPGA VI References](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/fpga/getallfpgavireferences-vi.html) Returns all FPGA VI references in the Semiconductor Module context.
- [Pin to FPGA VI Reference(s)](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/fpga/pintofpgavireference-s-vi.html) Returns the FPGA VI references of the instruments connected to the pin. You must manually select the polymorphic instance you want to use. Select the single instrument or multiple instrument polymorphic instance based on the number of instruments you expect the pin to be connected to in the pin map. The multiple instrument polymorphic instances are recommended to ensure that your code module will work with any pin map, but you can use the single instrument instance if you know that the code module will never be used with a pin map that has more than one instrument connected to the specified pins.

Parent topic:

RF

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/fpga/pintofpgavireference-s-vi.html language=enus -->
## TOPIC 00169: Pin to FPGA VI Reference(s)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/fpga/pintofpgavireference-s-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/fpga/pintofpgavireference-s-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the FPGA VI references of the instruments connected to the pin. You must manually select the polymorphic instance you want to use. Select the single instrument or multiple instrument polymorphic instance based on the number of instruments you expect the pin to be connected to in the pin map.

### Pin to FPGA VI Reference(s)

Returns the FPGA VI references of the instruments connected to the pin. You must manually select the polymorphic instance you want to use. Select the single instrument or multiple instrument polymorphic instance based on the number of instruments you expect the pin to be connected to in the pin map. The multiple instrument polymorphic instances are recommended to ensure that your code module will work with any pin map, but you can use the single instrument instance if you know that the code module will never be used with a pin map that has more than one instrument connected to the specified pins.

[IMAGE alt='icon' src='pintofpgavireference-s-vi.png']

- [Pin to FPGA VI References](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/fpga/pintofpgavireferences-vi.html) Returns the FPGA VI References on instruments connected to the pin.
- [Pin to FPGA VI Reference](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/fpga/pintofpgavireference-vi.html) Returns the FPGA VI References on instruments connected to the pin. If more than one instrument is connected to the pin, the VI returns an error.

Parent topic:

FPGA

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/fpga/pintofpgavireference-vi.html language=enus -->
## TOPIC 00170: Pin to FPGA VI Reference

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/fpga/pintofpgavireference-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/fpga/pintofpgavireference-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the FPGA VI References on instruments connected to the pin. If more than one instrument is connected to the pin, the VI returns an error. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cdaqmxscale.png Pin spec

### Pin to FPGA VI Reference

Returns the FPGA VI References on instruments connected to the pin. If more than one instrument is connected to the pin, the VI returns an error.

[IMAGE alt='icon' src='pintofpgavireference-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — specifies the name of the pin to translate to an FPGA VI reference. If multiple FPGA VI references are required, the VI returns an error. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. FPGA VI Reference — returns the FPGA VI reference of the instrument connected to the pin for all sites in the Semiconductor Module Context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Pin to FPGA VI Reference(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/fpga/pintofpgavireferences-vi.html language=enus -->
## TOPIC 00171: Pin to FPGA VI References

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/fpga/pintofpgavireferences-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/fpga/pintofpgavireferences-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the FPGA VI References on instruments connected to the pin. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cdaqmxscale.png Pin specifies the name of the pin or pin group to translate to FPGA VI references. cer

### Pin to FPGA VI References

Returns the FPGA VI References on instruments connected to the pin.

[IMAGE alt='icon' src='pintofpgavireferences-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — specifies the name of the pin or pin group to translate to FPGA VI references. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. FPGA VI References — returns the FPGA VI references of the instruments connected to the pin for all sites in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Pin to FPGA VI Reference(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/fpga/setfpgavireference-vi.html language=enus -->
## TOPIC 00172: Set FPGA VI Reference

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/fpga/setfpgavireference-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/fpga/setfpgavireference-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Associates an instrument session with an FPGA-enabled instrument name. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cstr.png Instrument Name is the instrument name in the pin map file for the corresponding session.

### Set FPGA VI Reference

Associates an instrument session with an FPGA-enabled instrument name.

[IMAGE alt='icon' src='setfpgavireference-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Instrument Name — is the instrument name in the pin map file for the corresponding session. FPGA VI Reference — is the FPGA reference associated with the corresponding Instrument Name. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

FPGA

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfintruments-mnu.html language=enus -->
## TOPIC 00173: RF

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfintruments-mnu.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfintruments-mnu.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-RFSA, NI-RFSG, NI-RFmx, NI-RFPM, and FPGA VIs to manage NI-RFSA, NI-RFSG, NI-RFPM, and RF RIO (RF LabVIEW FPGA enabled) instruments. icon

### RF

Use the NI-RFSA, NI-RFSG, NI-RFmx, NI-RFPM, and FPGA VIs to manage NI-RFSA, NI-RFSG, NI-RFPM, and RF RIO (RF LabVIEW FPGA enabled) instruments.

[IMAGE alt='icon' src='rfintruments-mnu.png']

- [NI-RFSA](../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/nirfsa-mnu.html) Use the NI-RFSA VIs to manage NI-RFSA instruments and sessions.
- [NI-RFSG](../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/nirfsg-mnu.html) Use the NI-RFSG VIs to manage NI-RFSG instruments and sessions.
- [NI-RFmx](../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/nirfmx-mnu.html) Use the NI-RFmx VIs to manage NI-RFmx instruments and sessions.
- [NI-RFPM](../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/nirfpm-mnu.html) Use the NI-RFPM VIs to manage NI-RFPM instruments and sessions.
- [FPGA](../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/fpga/nivst-mnu.html) Use the FPGA VIs to manage FPGA sessions for RF RIO instruments (RF LabVIEW FPGA enabled instruments).

Parent topic:

Code Module Development

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/getallnirfmxinstrumentnames-vi.html language=enus -->
## TOPIC 00174: Get All NI-RFmx Instrument Names

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/getallnirfmxinstrumentnames-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/getallnirfmxinstrumentnames-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the instrument names for all NI-RFmx instruments in the Semiconductor Module context. You can use instrument names to open driver sessions. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cerrcodeclst.png error

### Get All NI-RFmx Instrument Names

Returns the instrument names for all NI-RFmx instruments in the Semiconductor Module context. You can use instrument names to open driver sessions.

[IMAGE alt='icon' src='getallnirfmxinstrumentnames-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Names — returns an array of NI-RFmx instrument names in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

NI-RFmx

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/getallnirfmxsessions-vi.html language=enus -->
## TOPIC 00175: Get All NI-RFmx Sessions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/getallnirfmxsessions-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/getallnirfmxsessions-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns all NI-RFmx instrument sessions in the Semiconductor Module context. You can use instrument sessions to close driver sessions. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cerrcodeclst.png error in (no error

### Get All NI-RFmx Sessions

Returns all NI-RFmx instrument sessions in the Semiconductor Module context. You can use instrument sessions to close driver sessions.

[IMAGE alt='icon' src='getallnirfmxsessions-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Sessions — returns the NI-RFmx instrument sessions for all sites in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

NI-RFmx

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/nirfmx-mnu.html language=enus -->
## TOPIC 00176: NI-RFmx

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/nirfmx-mnu.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/nirfmx-mnu.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-RFmx VIs to manage NI-RFmx instruments and sessions. icon

### NI-RFmx

Use the NI-RFmx VIs to manage NI-RFmx instruments and sessions.

[IMAGE alt='icon' src='nirfmx-mnu.png']

- [Get All NI-RFmx Instrument Names](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/getallnirfmxinstrumentnames-vi.html) Returns the instrument names for all NI-RFmx instruments in the Semiconductor Module context. You can use instrument names to open driver sessions.
- [Set NI-RFmx Session](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/setnirfmxsession-vi.html) Associates an instrument session with an NI-RFmx instrument name.
- [Get All NI-RFmx Sessions](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/getallnirfmxsessions-vi.html) Returns all NI-RFmx instrument sessions in the Semiconductor Module context. You can use instrument sessions to close driver sessions.
- [Pin to NI-RFmx Session(s)](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/pintonirfmxsession-s-vi.html) Returns the NI-RFmx session required to access one pin. You must manually select the polymorphic instance you want to use. Select the single instrument or multiple instrument polymorphic instance based on the number of instruments you expect the pin to be connected to in the pin map. The multiple instrument polymorphic instances are recommended to ensure that your code module will work with any pin map, but you can use the single instrument instance if you know that the code module will never be used with a pin map that has more than one instrument connected to the specified pins.
- [Pin to NI-RFmx De-Embedding Data](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/pintonirfmxdeembeddingdata-vi.html) Returns the NI-RFmx de-embedding data associated with the connection(s) to a single pin. You must manually select the polymorphic instance you want to use. Select the single file or multiple files polymorphic instance based on the number of connections you expect the pin to be connected to in the pin map. The multiple file polymorphic instances are recommended to ensure that your code module will work with any pin map, but you can use the single file instance if you know that the code module will never be used with a pin map that has more than one connection to the specified pin.

Parent topic:

RF

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/pintonirfmxdeembeddingdata-vi.html language=enus -->
## TOPIC 00177: Pin to NI-RFmx De-Embedding Data

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/pintonirfmxdeembeddingdata-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/pintonirfmxdeembeddingdata-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-RFmx de-embedding data associated with the connection(s) to a single pin. You must manually select the polymorphic instance you want to use. Select the single file or multiple files polymorphic instance based on the number of connections you expect the pin to be connected to in the pi

### Pin to NI-RFmx De-Embedding Data

Returns the NI-RFmx de-embedding data associated with the connection(s) to a single pin. You must manually select the polymorphic instance you want to use. Select the single file or multiple files polymorphic instance based on the number of connections you expect the pin to be connected to in the pin map. The multiple file polymorphic instances are recommended to ensure that your code module will work with any pin map, but you can use the single file instance if you know that the code module will never be used with a pin map that has more than one connection to the specified pin.

[IMAGE alt='icon' src='pintonirfmxdeembeddingdata-vi.png']

- [Pin to Single NI-RFmx De-Embedding Data](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/pintonirfmxsingledeembeddingdata-vi.html) Returns the NI-RFmx de-embedding path and orientation associated with the instrument connection to the pin. If more than one pin connection is found, the VI returns an error.
- [Pin to Multiple NI-RFmx De-Embedding Data](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/pintonirfmxmultipledeembeddingdata-vi.html) Returns the NI-RFmx de-embedding data associated with the connections to the pin. If any instrument in the Semiconductor Module context contains more than a single connection to the pin, the VI returns an error.

Parent topic:

NI-RFmx

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/pintonirfmxmultipledeembeddingdata-vi.html language=enus -->
## TOPIC 00178: Pin to Multiple NI-RFmx De-Embedding Data

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/pintonirfmxmultipledeembeddingdata-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/pintonirfmxmultipledeembeddingdata-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-RFmx de-embedding data associated with the connections to the pin. If any instrument in the Semiconductor Module context contains more than a single connection to the pin, the VI returns an error. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference

### Pin to Multiple NI-RFmx De-Embedding Data

Returns the NI-RFmx de-embedding data associated with the connections to the pin. If any instrument in the Semiconductor Module context contains more than a single connection to the pin, the VI returns an error.

[IMAGE alt='icon' src='pintonirfmxmultipledeembeddingdata-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — specifies the name of the pin or pin group to translate to de-embedding data on the connection. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. De-Embedding Files — returns the paths and RFmx orientations of the S2P files that characterize the de-embedding network. If the path is an absolute path, the VI returns the absolute path whether the file exists or not. If the path is a relative path and the file exists relative to the path of the pin map file, the VI returns the absolute path of the existing file. Otherwise, the VI returns a string without error. Path — Orientation — Deembedding Orientation specifies the orientation of the data in the S2P file relative to the port you specify. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |
| Path — Orientation — Deembedding Orientation specifies the orientation of the data in the S2P file relative to the port you specify. |

Parent topic:

Pin to NI-RFmx De-Embedding Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/pintonirfmxsession-s-vi.html language=enus -->
## TOPIC 00179: Pin to NI-RFmx Session(s)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/pintonirfmxsession-s-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/pintonirfmxsession-s-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-RFmx session required to access one pin. You must manually select the polymorphic instance you want to use. Select the single instrument or multiple instrument polymorphic instance based on the number of instruments you expect the pin to be connected to in the pin map. The multiple in

### Pin to NI-RFmx Session(s)

Returns the NI-RFmx session required to access one pin. You must manually select the polymorphic instance you want to use. Select the single instrument or multiple instrument polymorphic instance based on the number of instruments you expect the pin to be connected to in the pin map. The multiple instrument polymorphic instances are recommended to ensure that your code module will work with any pin map, but you can use the single instrument instance if you know that the code module will never be used with a pin map that has more than one instrument connected to the specified pins.

[IMAGE alt='icon' src='pintonirfmxsession-s-vi.png']

- [Pin to NI-RFmx Session](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/pintonirfmxsession-vi.html) Returns the NI-RFmx instrument session required to access the pin. If more than one instrument is required to access the pin, or if the instrument has more than one port connected to that pin in other sites within the given context, the VI returns an error.
- [Pin to NI-RFmx Sessions](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/pintonirfmxsessions-vi.html) Returns the NI-RFmx instrument sessions required to access the pin. If any instrument has more than one port connected to that pin in other sites within the given context, the VI returns an error.

Parent topic:

NI-RFmx

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/pintonirfmxsession-vi.html language=enus -->
## TOPIC 00180: Pin to NI-RFmx Session

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/pintonirfmxsession-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/pintonirfmxsession-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-RFmx instrument session required to access the pin. If more than one instrument is required to access the pin, or if the instrument has more than one port connected to that pin in other sites within the given context, the VI returns an error. icon Inputs/Outputs coarn.png Semiconducto

### Pin to NI-RFmx Session

Returns the NI-RFmx instrument session required to access the pin. If more than one instrument is required to access the pin, or if the instrument has more than one port connected to that pin in other sites within the given context, the VI returns an error.

[IMAGE alt='icon' src='pintonirfmxsession-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — specifies the name of the pin to translate to an instrument session. If multiple sessions are required, the VI returns an error. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Session — returns the NI-RFmx instrument session for the instrument connected to the pin. Port — returns the instrument port connected to the pin. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Pin to NI-RFmx Session(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/pintonirfmxsessions-vi.html language=enus -->
## TOPIC 00181: Pin to NI-RFmx Sessions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/pintonirfmxsessions-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/pintonirfmxsessions-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-RFmx instrument sessions required to access the pin. If any instrument has more than one port connected to that pin in other sites within the given context, the VI returns an error. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconduc

### Pin to NI-RFmx Sessions

Returns the NI-RFmx instrument sessions required to access the pin. If any instrument has more than one port connected to that pin in other sites within the given context, the VI returns an error.

[IMAGE alt='icon' src='pintonirfmxsessions-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — specifies the name of the pin or pin group to translate to instrument sessions. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Sessions — returns the NI-RFmx instrument sessions for the instruments connected to the pin for all sites in the Semiconductor Module context. Ports — returns the port information for the associated instrument sessions connections to the pin. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Pin to NI-RFmx Session(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/pintonirfmxsingledeembeddingdata-vi.html language=enus -->
## TOPIC 00182: Pin to Single NI-RFmx De-Embedding Data

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/pintonirfmxsingledeembeddingdata-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/pintonirfmxsingledeembeddingdata-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-RFmx de-embedding path and orientation associated with the instrument connection to the pin. If more than one pin connection is found, the VI returns an error. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context obj

### Pin to Single NI-RFmx De-Embedding Data

Returns the NI-RFmx de-embedding path and orientation associated with the instrument connection to the pin. If more than one pin connection is found, the VI returns an error.

[IMAGE alt='icon' src='pintonirfmxsingledeembeddingdata-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — specifies the name of the pin associated with the instrument. If more than one pin connection is found, the VI returns an error. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. De-Embedding File — returns the paths and RFmx orientation of the S2P file that characterizes the de-embedding network. If the path is an absolute path, the VI returns the absolute path whether the file exists or not. If the path is a relative path and the file exists relative to the path of the pin map file, the VI returns the absolute path of the existing file. Otherwise, the VI returns a string without error. Path — Orientation — Deembedding Orientation specifies the orientation of the data in the S2P file relative to the port you specify. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |
| Path — Orientation — Deembedding Orientation specifies the orientation of the data in the S2P file relative to the port you specify. |

Parent topic:

Pin to NI-RFmx De-Embedding Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/setnirfmxsession-vi.html language=enus -->
## TOPIC 00183: Set NI-RFmx Session

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/setnirfmxsession-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfmx/setnirfmxsession-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Associates an instrument session with an NI-RFmx instrument name. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cstr.png Instrument Name is the instrument name in the pin map file for the corresponding session. cgenc

### Set NI-RFmx Session

Associates an instrument session with an NI-RFmx instrument name.

[IMAGE alt='icon' src='setnirfmxsession-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Instrument Name — is the instrument name in the pin map file for the corresponding session. NI-RFmx Session — is the instrument session for the corresponding instrument name. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

NI-RFmx

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/2pinstonirfpmsessionswithpaths-vi.html language=enus -->
## TOPIC 00184: 2 Pins To NI-RFPM Sessions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/2pinstonirfpmsessionswithpaths-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/2pinstonirfpmsessionswithpaths-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-RFPM sessions and ports required to access Pin 1 and Pin 2 and the paths and orientations to S2P files that characterize the de-embedding network for each port. This polymorphic instance is a convenient option for tests that involve a stimulus and response pin. icon Inputs/Outputs coa

### 2 Pins To NI-RFPM Sessions

Returns the NI-RFPM sessions and ports required to access Pin 1 and Pin 2 and the paths and orientations to S2P files that characterize the de-embedding network for each port. This polymorphic instance is a convenient option for tests that involve a stimulus and response pin.

[IMAGE alt='icon' src='2pinstonirfpmsessionswithpaths-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin 1 — specifies the name of the first pin to translate to instrument sessions and include in the Ports List 1 parameter. The pin must be a DUT pin. Pin 2 — specifies the name of the second pin to translate to instrument sessions and include in the Ports List 2 parameter. The pin must be a DUT pin. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Ports List 1 — returns an array of ports where each element is the port for the instrument session required to access Pin 1 on the corresponding site. Ports List 2 — returns an array of ports where each element is the port for the instrument session required to access Pin 2 on the corresponding site. Semiconductor Module Context out — returns the Semiconductor Module Context parameter unchanged. Semiconductor Module Contexts — returns an array of Semiconductor Module context objects. Each element in the array represents a site that must be executed serially. Use each Semiconductor Module context object to query the pin map and publish data. You must always close references to the Semiconductor Module contexts, even if you do not use them in your code module. Instrument Sessions — returns the NI-RFPM subsystem sessions of the instruments for each site in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. De-embedding Files 2 — returns the paths and orientations of the S2P files that characterize the de-embedding network for each port in the Ports List 2 parameter. If the path is an absolute path, the VI returns the absolute path whether the file exists or not. If the path is a relative path and the file exists relative to the path of the pin map file, the VI returns the absolute path of the existing file. Otherwise, the VI returns a string without error. Path — Orientation — Deembedding Orientation specifies the orientation of the data in the S2P file relative to the port you specify. De-embedding Files 1 — returns the paths and orientations of the S2P files that characterize the de-embedding network for each port in the Ports List 1 parameter. If the path is an absolute path, the VI returns the absolute path whether the file exists or not. If the path is a relative path and the file exists relative to the path of the pin map file, the VI returns the absolute path of the existing file. Otherwise, the VI returns a string without error. Path — Orientation — Deembedding Orientation specifies the orientation of the data in the S2P file relative to the port you specify. |
| --- |
| Path — Orientation — Deembedding Orientation specifies the orientation of the data in the S2P file relative to the port you specify. |
| Path — Orientation — Deembedding Orientation specifies the orientation of the data in the S2P file relative to the port you specify. |

Parent topic:

Pin(s) To NI-RFPM Sessions

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/getallnirfpmdeembeddingdatawithpaths-vi.html language=enus -->
## TOPIC 00185: Get All NI-RFPM De-embedding Data

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/getallnirfpmdeembeddingdatawithpaths-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/getallnirfpmdeembeddingdatawithpaths-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-RFPM subsystem sessions and paths and orientations of the S2P files that characterize the de-embedding network for every port connected to a DUT pin in the Semiconductor Module context. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semico

### Get All NI-RFPM De-embedding Data

Returns the NI-RFPM subsystem sessions and paths and orientations of the S2P files that characterize the de-embedding network for every port connected to a DUT pin in the Semiconductor Module context.

[IMAGE alt='icon' src='getallnirfpmdeembeddingdatawithpaths-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context out — returns the Semiconductor Module Context parameter unchanged. Instrument Sessions — returns an array of NI-RFPM subsystem sessions, where each element is the session for each port in the Ports List parameter. Ports Lists — returns an array of ports for each pin connected to an NI-RFPM subsystem in the Semiconductor Module Context De-embedding Files — returns an array of de-embedding files, where each element is a cluster that includes the path and orientation of data in the S2P file that characterizes the de-embedding network for each port in the Ports List parameter. If the path is an absolute path, the VI returns the absolute path whether the file exists or not. If the path is a relative path and the file exists relative to the path of the pin map file, the VI returns the absolute path of the existing file. Otherwise, the VI returns a string without error. Path — Orientation — Deembedding Orientation specifies the orientation of the data in the S2P file relative to the port you specify. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |
| Path — Orientation — Deembedding Orientation specifies the orientation of the data in the S2P file relative to the port you specify. |

Parent topic:

NI-RFPM

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/getallnirfpminstrumentnames-vi.html language=enus -->
## TOPIC 00186: Get All NI-RFPM Instrument Names

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/getallnirfpminstrumentnames-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/getallnirfpminstrumentnames-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the names of all NI-RFPM subsystems and respective calibration file paths, IVI Switch names, and FPGA file paths in the Semiconductor Module context. You can use instrument names, IVI Switch names, FPGA file paths, and calibration file paths to open instrument and calibration sessions. icon

### Get All NI-RFPM Instrument Names

Returns the names of all NI-RFPM subsystems and respective calibration file paths, IVI Switch names, and FPGA file paths in the Semiconductor Module context. You can use instrument names, IVI Switch names, FPGA file paths, and calibration file paths to open instrument and calibration sessions.

[IMAGE alt='icon' src='getallnirfpminstrumentnames-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context out — returns the Semiconductor Module Context parameter unchanged. Instrument Names — returns the names of all the NI-RFPM subsystems in the Semiconductor Module context. Calibration File Paths — returns the paths to calibration files associated with NI-RFPM subsystems in the Semiconductor Module context. If the path is an absolute path, the VI returns the absolute path whether the file exists or not. If the path is a relative path and the file exists relative to the path of the pin map file, the VI returns the absolute path of the existing file. Otherwise, the VI returns a string without error. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. IVI Switch Names — returns the IVI Switch resource names associated with the NI-RFPM subsystems in the Semiconductor Module context. FPGA File Paths — returns the paths to the FPGA files for the NI-VST instrument associated with NI-RFPM subsystems in the Semiconductor Module context. If the path is an absolute path, the VI returns the absolute path whether the file exists or not. If the path is a relative path and the file exists relative to the path of the pin map file, the VI returns the absolute path of the existing file. Otherwise, the VI returns a string without error. |
| --- |

Parent topic:

NI-RFPM

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/getallnirfpmsessions-vi.html language=enus -->
## TOPIC 00187: Get All NI-RFPM Sessions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/getallnirfpmsessions-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/getallnirfpmsessions-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns all NI-RFPM subsystem sessions in the Semiconductor Module context. You can use subsystem sessions to close driver sessions. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cerrcodeclst.png error in (no error)

### Get All NI-RFPM Sessions

Returns all NI-RFPM subsystem sessions in the Semiconductor Module context. You can use subsystem sessions to close driver sessions.

[IMAGE alt='icon' src='getallnirfpmsessions-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context out — returns the Semiconductor Module Context parameter unchanged. Instrument Sessions — returns the NI-RFPM subsystem sessions of the instruments for all sites in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

NI-RFPM

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/nirfpm-mnu.html language=enus -->
## TOPIC 00188: NI-RFPM

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/nirfpm-mnu.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/nirfpm-mnu.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-RFPM VIs to manage NI-RFPM instruments and sessions. icon

### NI-RFPM

Use the NI-RFPM VIs to manage NI-RFPM instruments and sessions.

[IMAGE alt='icon' src='nirfpm-mnu.png']

- [Get All NI-RFPM Instrument Names](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/getallnirfpminstrumentnames-vi.html) Returns the names of all NI-RFPM subsystems and respective calibration file paths, IVI Switch names, and FPGA file paths in the Semiconductor Module context. You can use instrument names, IVI Switch names, FPGA file paths, and calibration file paths to open instrument and calibration sessions.
- [Set NI-RFPM Session](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/setnirfpmsession-vi.html) Associates an open NI-RFPM session and IVI Switch session with the NI-RFPM instrument name.
- [Get All NI-RFPM Sessions](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/getallnirfpmsessions-vi.html) Returns all NI-RFPM subsystem sessions in the Semiconductor Module context. You can use subsystem sessions to close driver sessions.
- [Pin(s) To NI-RFPM Sessions](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/pin-s-tonirfpmsessionswithpaths-vi.html) Returns the NI-RFPM sessions and ports required to access one or more pins, as well as paths and orientations of the S2P files that characterize the de-embedding network for each port. You must always close references to the Semiconductor Module contexts, even if you do not use them in your code module. You must manually select the polymorphic instance you want to use. Select the single pin, two pins, or multiple pins polymorphic instance based on the number of pins the test is designed to test. The two pins polymorphic instance is a convenient option for tests that involve a stimulus and response pin.
- [Get All NI-RFPM De-embedding Data](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/getallnirfpmdeembeddingdatawithpaths-vi.html) Returns the NI-RFPM subsystem sessions and paths and orientations of the S2P files that characterize the de-embedding network for every port connected to a DUT pin in the Semiconductor Module context.

Parent topic:

RF

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/pin-s-tonirfpmsessionswithpaths-vi.html language=enus -->
## TOPIC 00189: Pin(s) To NI-RFPM Sessions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/pin-s-tonirfpmsessionswithpaths-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/pin-s-tonirfpmsessionswithpaths-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-RFPM sessions and ports required to access one or more pins, as well as paths and orientations of the S2P files that characterize the de-embedding network for each port. You must always close references to the Semiconductor Module contexts, even if you do not use them in your code mod

### Pin(s) To NI-RFPM Sessions

Returns the NI-RFPM sessions and ports required to access one or more pins, as well as paths and orientations of the S2P files that characterize the de-embedding network for each port. You must always close references to the Semiconductor Module contexts, even if you do not use them in your code module. You must manually select the polymorphic instance you want to use. Select the single pin, two pins, or multiple pins polymorphic instance based on the number of pins the test is designed to test. The two pins polymorphic instance is a convenient option for tests that involve a stimulus and response pin.

[IMAGE alt='icon' src='pin-s-tonirfpmsessionswithpaths-vi.png']

- [Pin To NI-RFPM Sessions](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/pintonirfpmsessionswithpaths-vi.html) Returns the NI-RFPM sessions and ports required to access the pin, as well as paths and orientations of the S2P files that characterize the de-embedding network for each port.
- [2 Pins To NI-RFPM Sessions](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/2pinstonirfpmsessionswithpaths-vi.html) Returns the NI-RFPM sessions and ports required to access Pin 1 and Pin 2 and the paths and orientations to S2P files that characterize the de-embedding network for each port. This polymorphic instance is a convenient option for tests that involve a stimulus and response pin.
- [Pins To NI-RFPM Sessions](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/pinstonirfpmsessionswithpaths-vi.html) Returns the NI-RFPM sessions and ports required to access the pins, as well as paths and orientations of the S2P files that characterize the de-embedding network for each port.

Parent topic:

NI-RFPM

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/pinstonirfpmsessionswithpaths-vi.html language=enus -->
## TOPIC 00190: Pins To NI-RFPM Sessions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/pinstonirfpmsessionswithpaths-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/pinstonirfpmsessionswithpaths-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-RFPM sessions and ports required to access the pins, as well as paths and orientations of the S2P files that characterize the de-embedding network for each port. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context o

### Pins To NI-RFPM Sessions

Returns the NI-RFPM sessions and ports required to access the pins, as well as paths and orientations of the S2P files that characterize the de-embedding network for each port.

[IMAGE alt='icon' src='pinstonirfpmsessionswithpaths-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pins — specifies the names of the pins or pin groups to translate to instrument sessions and include in the Ports Lists parameter. The pins must be DUT pins. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Ports List — returns a 2D array of ports. Each row represents ports from a site, and each column represents the ports for the instrument session required to access the pins on the corresponding site. Semiconductor Module Context out — returns the Semiconductor Module Context parameter unchanged. Semiconductor Module Contexts — returns an array of Semiconductor Module context objects. Each element in the array represents a site that must be executed serially. Use each Semiconductor Module context object to query the pin map and publish data. You must always close references to the Semiconductor Module contexts, even if you do not use them in your code module. Instrument Sessions — returns the NI-RFPM subsystem sessions of the instruments for each site in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. De-embedding Files — returns the paths and orientations of the S2P files that characterize the de-embedding network for each port in the Ports List parameter. If the path is an absolute path, the VI returns the absolute path whether the file exists or not. If the path is a relative path and the file exists relative to the path of the pin map file, the VI returns the absolute path of the existing file. Otherwise, the VI returns a string without error. Path — Orientation — Deembedding Orientation specifies the orientation of the data in the S2P file relative to the port you specify. |
| --- |
| Path — Orientation — Deembedding Orientation specifies the orientation of the data in the S2P file relative to the port you specify. |

Parent topic:

Pin(s) To NI-RFPM Sessions

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/pintonirfpmsessionswithpaths-vi.html language=enus -->
## TOPIC 00191: Pin To NI-RFPM Sessions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/pintonirfpmsessionswithpaths-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/pintonirfpmsessionswithpaths-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-RFPM sessions and ports required to access the pin, as well as paths and orientations of the S2P files that characterize the de-embedding network for each port. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context ob

### Pin To NI-RFPM Sessions

Returns the NI-RFPM sessions and ports required to access the pin, as well as paths and orientations of the S2P files that characterize the de-embedding network for each port.

[IMAGE alt='icon' src='pintonirfpmsessionswithpaths-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — specifies the name of the pin to translate to instrument sessions and include in the Ports List parameter. The pin must be a DUT pin. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Ports List — returns an array of ports, where each element is the port for the instrument session required to access the pin on the corresponding site. Semiconductor Module Context out — returns the Semiconductor Module Context parameter unchanged. Semiconductor Module Contexts — returns an array of Semiconductor Module context objects. Each element in the array represents a site that must be executed serially. Use each Semiconductor Module context object to query the pin map and publish data. You must always close references to the Semiconductor Module contexts, even if you do not use them in your code module. Instrument Sessions — returns the NI-RFPM subsystem sessions of the instruments for each site in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. De-embedding Files — returns the paths and orientations of the S2P files that characterize the de-embedding network for each port in the Ports List parameter. If the path is an absolute path, the VI returns the absolute path whether the file exists or not. If the path is a relative path and the file exists relative to the path of the pin map file, the VI returns the absolute path of the existing file. Otherwise, the VI returns a string without error. Path — Orientation — Deembedding Orientation specifies the orientation of the data in the S2P file relative to the port you specify. |
| --- |
| Path — Orientation — Deembedding Orientation specifies the orientation of the data in the S2P file relative to the port you specify. |

Parent topic:

Pin(s) To NI-RFPM Sessions

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/setnirfpmsession-vi.html language=enus -->
## TOPIC 00192: Set NI-RFPM Session

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/setnirfpmsession-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfpm/setnirfpmsession-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Associates an open NI-RFPM session and IVI Switch session with the NI-RFPM instrument name. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cstr.png Instrument Name is the instrument name in the pin map file for the co

### Set NI-RFPM Session

Associates an open NI-RFPM session and IVI Switch session with the NI-RFPM instrument name.

[IMAGE alt='icon' src='setnirfpmsession-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Instrument Name — is the instrument name in the pin map file for the corresponding sessions. NI-RFPM Session — is the NI-RFPM subsystem session for the corresponding instrument name. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context out — returns the Semiconductor Module Context parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

NI-RFPM

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/getallnirfsainstrumentnames-vi.html language=enus -->
## TOPIC 00193: Get All NI-RFSA Instrument Names

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/getallnirfsainstrumentnames-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/getallnirfsainstrumentnames-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the instrument names for all NI-RFSA instruments in the Semiconductor Module context. You can use instrument names to open driver sessions. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cerrcodeclst.png error

### Get All NI-RFSA Instrument Names

Returns the instrument names for all NI-RFSA instruments in the Semiconductor Module context. You can use instrument names to open driver sessions.

[IMAGE alt='icon' src='getallnirfsainstrumentnames-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Names — returns an array of NI-RFSA instrument names in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

NI-RFSA

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/getallnirfsasessions-vi.html language=enus -->
## TOPIC 00194: Get All NI-RFSA Sessions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/getallnirfsasessions-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/getallnirfsasessions-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns all NI-RFSA instrument sessions in the Semiconductor Module context. You can use instrument sessions to close driver sessions. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cerrcodeclst.png error in (no error

### Get All NI-RFSA Sessions

Returns all NI-RFSA instrument sessions in the Semiconductor Module context. You can use instrument sessions to close driver sessions.

[IMAGE alt='icon' src='getallnirfsasessions-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Sessions — returns the NI-RFSA instrument sessions for all sites in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

NI-RFSA

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/nirfsa-mnu.html language=enus -->
## TOPIC 00195: NI-RFSA

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/nirfsa-mnu.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/nirfsa-mnu.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-RFSA VIs to manage NI-RFSA instruments and sessions. icon

### NI-RFSA

Use the NI-RFSA VIs to manage NI-RFSA instruments and sessions.

[IMAGE alt='icon' src='nirfsa-mnu.png']

- [Get All NI-RFSA Instrument Names](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/getallnirfsainstrumentnames-vi.html) Returns the instrument names for all NI-RFSA instruments in the Semiconductor Module context. You can use instrument names to open driver sessions.
- [Set NI-RFSA Session](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/setnirfsasession-vi.html) Associates an instrument session with an NI-RFSA instrument name.
- [Get All NI-RFSA Sessions](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/getallnirfsasessions-vi.html) Returns all NI-RFSA instrument sessions in the Semiconductor Module context. You can use instrument sessions to close driver sessions.
- [Pin to NI-RFSA Session(s)](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/pintonirfsasession-s-vi.html) Returns the NI-RFSA session required to access one pin. You must manually select the polymorphic instance you want to use. Select the single instrument or multiple instrument polymorphic instance based on the number of instruments you expect the pin to be connected to in the pin map. Use the multiple instrument polymorphic instances to ensure that code modules work with any pin map. Use the single instrument instance only when you know the code module will never be used with a pin map that has more than one instrument connected to the specified pins.
- [Pin to NI-RFSA De-Embedding Data](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/pintonirfsadeembeddingdata-vi.html) Returns the NI-RFSA de-embedding data associated with the connection(s) to a single pin. You must manually select the polymorphic instance you want to use. Select the single file or multiple files polymorphic instance based on the number of connections you expect the pin to be connected to in the pin map. The multiple file polymorphic instances are recommended to ensure that your code module will work with any pin map, but you can use the single file instance if you know that the code module will never be used with a pin map that has more than one connection to the specified pin.

Parent topic:

RF

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/pintonirfsadeembeddingdata-vi.html language=enus -->
## TOPIC 00196: Pin to NI-RFSA De-Embedding Data

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/pintonirfsadeembeddingdata-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/pintonirfsadeembeddingdata-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-RFSA de-embedding data associated with the connection(s) to a single pin. You must manually select the polymorphic instance you want to use. Select the single file or multiple files polymorphic instance based on the number of connections you expect the pin to be connected to in the pi

### Pin to NI-RFSA De-Embedding Data

Returns the NI-RFSA de-embedding data associated with the connection(s) to a single pin. You must manually select the polymorphic instance you want to use. Select the single file or multiple files polymorphic instance based on the number of connections you expect the pin to be connected to in the pin map. The multiple file polymorphic instances are recommended to ensure that your code module will work with any pin map, but you can use the single file instance if you know that the code module will never be used with a pin map that has more than one connection to the specified pin.

[IMAGE alt='icon' src='pintonirfsadeembeddingdata-vi.png']

- [Pin to Multiple NI-RFSA De-Embedding Data](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/pintonirfsamultipledeembeddingdata-vi.html) Returns the NI-RFSA de-embedding data associated with the connections to the pin. If any instrument in the Semiconductor Module context contains more than a single connection to the pin, the VI returns an error.
- [Pin to Single NI-RFSA De-Embedding Data](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/pintonirfsasingledeembeddingdata-vi.html) Returns the NI-RFSA de-embedding path and orientation associated with the instrument connection to the pin. If more than one pin connection is found, the VI returns an error.

Parent topic:

NI-RFSA

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/pintonirfsamultipledeembeddingdata-vi.html language=enus -->
## TOPIC 00197: Pin to Multiple NI-RFSA De-Embedding Data

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/pintonirfsamultipledeembeddingdata-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/pintonirfsamultipledeembeddingdata-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-RFSA de-embedding data associated with the connections to the pin. If any instrument in the Semiconductor Module context contains more than a single connection to the pin, the VI returns an error. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference

### Pin to Multiple NI-RFSA De-Embedding Data

Returns the NI-RFSA de-embedding data associated with the connections to the pin. If any instrument in the Semiconductor Module context contains more than a single connection to the pin, the VI returns an error.

[IMAGE alt='icon' src='pintonirfsamultipledeembeddingdata-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — specifies the name of the pin or pin group to translate de-embedding data on the connection. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. De-Embedding Files — returns the paths and RFSA orientations of the S2P files that characterize the de-embedding network. If the path is an absolute path, the VI returns the absolute path whether the file exists or not. If the path is a relative path and the file exists relative to the path of the pin map file, the VI returns the absolute path of the existing file. Otherwise, the VI returns a string without error. Path — Orientation — Deembedding Orientation specifies the orientation of the data in the S2P file relative to the port you specify. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |
| Path — Orientation — Deembedding Orientation specifies the orientation of the data in the S2P file relative to the port you specify. |

Parent topic:

Pin to NI-RFSA De-Embedding Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/pintonirfsasession-s-vi.html language=enus -->
## TOPIC 00198: Pin to NI-RFSA Session(s)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/pintonirfsasession-s-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/pintonirfsasession-s-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-RFSA session required to access one pin. You must manually select the polymorphic instance you want to use. Select the single instrument or multiple instrument polymorphic instance based on the number of instruments you expect the pin to be connected to in the pin map. Use the multipl

### Pin to NI-RFSA Session(s)

Returns the NI-RFSA session required to access one pin. You must manually select the polymorphic instance you want to use. Select the single instrument or multiple instrument polymorphic instance based on the number of instruments you expect the pin to be connected to in the pin map. Use the multiple instrument polymorphic instances to ensure that code modules work with any pin map. Use the single instrument instance only when you know the code module will never be used with a pin map that has more than one instrument connected to the specified pins.

[IMAGE alt='icon' src='pintonirfsasession-s-vi.png']

- [Pin to NI-RFSA Sessions](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/pintonirfsasessions-vi.html) Returns the NI-RFSA instrument sessions required to access the pin. If any instrument has more than one port connected to that pin in other sites within the given context the VI returns an error.
- [Pin to NI-RFSA Session](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/pintonirfsasession-vi.html) Returns the NI-RFSA instrument session required to access the pin. If more than one instrument is required to access the pin, or if the instrument has more than one port connected to that pin in other sites within the given context, the VI returns an error.

Parent topic:

NI-RFSA

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/pintonirfsasession-vi.html language=enus -->
## TOPIC 00199: Pin to NI-RFSA Session

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/pintonirfsasession-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/pintonirfsasession-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-RFSA instrument session required to access the pin. If more than one instrument is required to access the pin, or if the instrument has more than one port connected to that pin in other sites within the given context, the VI returns an error. icon Inputs/Outputs coarn.png Semiconducto

### Pin to NI-RFSA Session

Returns the NI-RFSA instrument session required to access the pin. If more than one instrument is required to access the pin, or if the instrument has more than one port connected to that pin in other sites within the given context, the VI returns an error.

[IMAGE alt='icon' src='pintonirfsasession-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — specifies the name of the pin to translate to an instrument session. If multiple sessions are required, the VI returns an error. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Session — returns the NI-RFSA instrument session for the instrument connected to the pin. Port — returns the instrument port connected to the pin. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Pin to NI-RFSA Session(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/pintonirfsasessions-vi.html language=enus -->
## TOPIC 00200: Pin to NI-RFSA Sessions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/pintonirfsasessions-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/pintonirfsasessions-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-RFSA instrument sessions required to access the pin. If any instrument has more than one port connected to that pin in other sites within the given context the VI returns an error. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconduct

### Pin to NI-RFSA Sessions

Returns the NI-RFSA instrument sessions required to access the pin. If any instrument has more than one port connected to that pin in other sites within the given context the VI returns an error.

[IMAGE alt='icon' src='pintonirfsasessions-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — specifies the name of the pin or pin group to translate to instrument sessions. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Sessions — returns the NI-RFSA instrument sessions for the instruments connected to the pin for all sites in the Semiconductor Module context. Ports — returns the port information for the associated instrument sessions connections to the pin. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Pin to NI-RFSA Session(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/pintonirfsasingledeembeddingdata-vi.html language=enus -->
## TOPIC 00201: Pin to Single NI-RFSA De-Embedding Data

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/pintonirfsasingledeembeddingdata-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/pintonirfsasingledeembeddingdata-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-RFSA de-embedding path and orientation associated with the instrument connection to the pin. If more than one pin connection is found, the VI returns an error. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context obj

### Pin to Single NI-RFSA De-Embedding Data

Returns the NI-RFSA de-embedding path and orientation associated with the instrument connection to the pin. If more than one pin connection is found, the VI returns an error.

[IMAGE alt='icon' src='pintonirfsasingledeembeddingdata-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — specifies the name of the pin associated with the instrument. If more than one pin connection is found, the VI returns an error. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. De-Embedding File — returns the paths and RFSA orientation of the S2P file that characterizes the de-embedding network. If the path is an absolute path, the VI returns the absolute path whether the file exists or not. If the path is a relative path and the file exists relative to the path of the pin map file, the VI returns the absolute path of the existing file. Otherwise, the VI returns a string without error. Path — Orientation — Deembedding Orientation specifies the orientation of the data in the S2P file relative to the port you specify. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |
| Path — Orientation — Deembedding Orientation specifies the orientation of the data in the S2P file relative to the port you specify. |

Parent topic:

Pin to NI-RFSA De-Embedding Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/setnirfsasession-vi.html language=enus -->
## TOPIC 00202: Set NI-RFSA Session

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/setnirfsasession-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfsa/setnirfsasession-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Associates an instrument session with an NI-RFSA instrument name. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cstr.png Instrument Name is the instrument name in the pin map file for the corresponding session. civrn

### Set NI-RFSA Session

Associates an instrument session with an NI-RFSA instrument name.

[IMAGE alt='icon' src='setnirfsasession-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Instrument Name — is the instrument name in the pin map file for the corresponding session. NI-RFSA Session — is the instrument session for the corresponding instrument name. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

NI-RFSA

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/getallnirfsginstrumentnames-vi.html language=enus -->
## TOPIC 00203: Get All NI-RFSG Instrument Names

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/getallnirfsginstrumentnames-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/getallnirfsginstrumentnames-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the instrument names for all NI-RFSG instruments in the Semiconductor Module context. You can use instrument names to open driver sessions. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cerrcodeclst.png error

### Get All NI-RFSG Instrument Names

Returns the instrument names for all NI-RFSG instruments in the Semiconductor Module context. You can use instrument names to open driver sessions.

[IMAGE alt='icon' src='getallnirfsginstrumentnames-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Names — returns an array of NI-RFSG instrument names in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

NI-RFSG

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/getallnirfsgsessions-vi.html language=enus -->
## TOPIC 00204: Get All NI-RFSG Sessions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/getallnirfsgsessions-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/getallnirfsgsessions-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns all NI-RFSG instrument sessions in the Semiconductor Module context. You can use instrument sessions to close driver sessions. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cerrcodeclst.png error in (no error

### Get All NI-RFSG Sessions

Returns all NI-RFSG instrument sessions in the Semiconductor Module context. You can use instrument sessions to close driver sessions.

[IMAGE alt='icon' src='getallnirfsgsessions-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Sessions — returns the NI-RFSG instrument sessions for all sites in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

NI-RFSG

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/nirfsg-mnu.html language=enus -->
## TOPIC 00205: NI-RFSG

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/nirfsg-mnu.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/nirfsg-mnu.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-RFSG VIs to manage NI-RFSG instruments and sessions. icon

### NI-RFSG

Use the NI-RFSG VIs to manage NI-RFSG instruments and sessions.

[IMAGE alt='icon' src='nirfsg-mnu.png']

- [Get All NI-RFSG Instrument Names](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/getallnirfsginstrumentnames-vi.html) Returns the instrument names for all NI-RFSG instruments in the Semiconductor Module context. You can use instrument names to open driver sessions.
- [Set NI-RFSG Session](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/setnirfsgsession-vi.html) Associates an instrument session with an NI-RFSG instrument name.
- [Get All NI-RFSG Sessions](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/getallnirfsgsessions-vi.html) Returns all NI-RFSG instrument sessions in the Semiconductor Module context. You can use instrument sessions to close driver sessions.
- [Pin to NI-RFSG Session(s)](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/pintonirfsgsession-s-vi.html) Returns the NI-RFSG session required to access one pin. You must manually select the polymorphic instance you want to use. Select the single instrument or multiple instrument polymorphic instance based on the number of instruments you expect the pin to be connected to in the pin map. The multiple instrument polymorphic instances are recommended to ensure that your code module will work with any pin map, but you can use the single instrument instance if you know that the code module will never be used with a pin map that has more than one instrument connected to the specified pins.
- [Pin to NI-RFSG De-Embedding Data](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/pintonirfsgdeembeddingdata-vi.html) Returns the NI-RFSG de-embedding data associated with the connection(s) to a single pin. You must manually select the polymorphic instance you want to use. Select the single file or multiple files polymorphic instance based on the number of connections you expect the pin to be connected to in the pin map. The multiple file polymorphic instances are recommended to ensure that your code module will work with any pin map, but you can use the single file instance if you know that the code module will never be used with a pin map that has more than one connection to the specified pin.

Parent topic:

RF

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/pintonirfsgdeembeddingdata-vi.html language=enus -->
## TOPIC 00206: Pin to NI-RFSG De-Embedding Data

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/pintonirfsgdeembeddingdata-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/pintonirfsgdeembeddingdata-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-RFSG de-embedding data associated with the connection(s) to a single pin. You must manually select the polymorphic instance you want to use. Select the single file or multiple files polymorphic instance based on the number of connections you expect the pin to be connected to in the pi

### Pin to NI-RFSG De-Embedding Data

Returns the NI-RFSG de-embedding data associated with the connection(s) to a single pin. You must manually select the polymorphic instance you want to use. Select the single file or multiple files polymorphic instance based on the number of connections you expect the pin to be connected to in the pin map. The multiple file polymorphic instances are recommended to ensure that your code module will work with any pin map, but you can use the single file instance if you know that the code module will never be used with a pin map that has more than one connection to the specified pin.

[IMAGE alt='icon' src='pintonirfsgdeembeddingdata-vi.png']

- [Pin to Multiple NI-RFSG De-Embedding Data](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/pintonirfsgmultipledeembeddingdata-vi.html) Returns the NI-RFmx de-embedding data associated with the connections to the pin. If any instrument in the Semiconductor Module context contains more than a single connection to the pin, the VI returns an error.
- [Pin to Single NI-RFSG De-Embedding Data](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/pintonirfsgsingledeembeddingdata-vi.html) Returns the NI-RFSG de-embedding path and orientation associated with the instrument connection to the pin. If more than one pin connection is found, the VI returns an error.

Parent topic:

NI-RFSG

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/pintonirfsgmultipledeembeddingdata-vi.html language=enus -->
## TOPIC 00207: Pin to Multiple NI-RFSG De-Embedding Data

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/pintonirfsgmultipledeembeddingdata-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/pintonirfsgmultipledeembeddingdata-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-RFmx de-embedding data associated with the connections to the pin. If any instrument in the Semiconductor Module context contains more than a single connection to the pin, the VI returns an error. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference

### Pin to Multiple NI-RFSG De-Embedding Data

Returns the NI-RFmx de-embedding data associated with the connections to the pin. If any instrument in the Semiconductor Module context contains more than a single connection to the pin, the VI returns an error.

[IMAGE alt='icon' src='pintonirfsgmultipledeembeddingdata-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — specifies the name of the pin or pin group to translate to de-embedding data on the connection. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. De-Embedding Files — returns the paths and RFmx orientations of the S2P files that characterize the de-embedding network. If the path is an absolute path, the VI returns the absolute path whether the file exists or not. If the path is a relative path and the file exists relative to the path of the pin map file, the VI returns the absolute path of the existing file. Otherwise, the VI returns a string without error. Path — Orientation — Deembedding Orientation specifies the orientation of the data in the S2P file relative to the port you specify. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |
| Path — Orientation — Deembedding Orientation specifies the orientation of the data in the S2P file relative to the port you specify. |

Parent topic:

Pin to NI-RFSG De-Embedding Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/pintonirfsgsession-s-vi.html language=enus -->
## TOPIC 00208: Pin to NI-RFSG Session(s)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/pintonirfsgsession-s-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/pintonirfsgsession-s-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-RFSG session required to access one pin. You must manually select the polymorphic instance you want to use. Select the single instrument or multiple instrument polymorphic instance based on the number of instruments you expect the pin to be connected to in the pin map. The multiple in

### Pin to NI-RFSG Session(s)

Returns the NI-RFSG session required to access one pin. You must manually select the polymorphic instance you want to use. Select the single instrument or multiple instrument polymorphic instance based on the number of instruments you expect the pin to be connected to in the pin map. The multiple instrument polymorphic instances are recommended to ensure that your code module will work with any pin map, but you can use the single instrument instance if you know that the code module will never be used with a pin map that has more than one instrument connected to the specified pins.

[IMAGE alt='icon' src='pintonirfsgsession-s-vi.png']

- [Pin to NI-RFSG Sessions](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/pintonirfsgsessions-vi.html) Returns the NI-RFSG instrument sessions required to access the pin. If any instrument has more than one port connected to that pin in other sites within the given context, the VI returns an error.
- [Pin to NI-RFSG Session](../../../../../../menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/pintonirfsgsession-vi.html) Returns the NI-RFSG instrument session required to access the pin. If more than one instrument is required to access the pin, or if the instrument has more than one port connected to that pin in other sites within the given context, the VI returns an error.

Parent topic:

NI-RFSG

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/pintonirfsgsession-vi.html language=enus -->
## TOPIC 00209: Pin to NI-RFSG Session

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/pintonirfsgsession-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/pintonirfsgsession-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-RFSG instrument session required to access the pin. If more than one instrument is required to access the pin, or if the instrument has more than one port connected to that pin in other sites within the given context, the VI returns an error. icon Inputs/Outputs coarn.png Semiconducto

### Pin to NI-RFSG Session

Returns the NI-RFSG instrument session required to access the pin. If more than one instrument is required to access the pin, or if the instrument has more than one port connected to that pin in other sites within the given context, the VI returns an error.

[IMAGE alt='icon' src='pintonirfsgsession-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — specifies the name of the pin to translate to an instrument session. If multiple sessions are required, the VI returns an error. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Session — returns the NI-RFSG instrument session for the instrument connected to the pin. Port — returns the instrument port connected to the pin. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Pin to NI-RFSG Session(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/pintonirfsgsessions-vi.html language=enus -->
## TOPIC 00210: Pin to NI-RFSG Sessions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/pintonirfsgsessions-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/pintonirfsgsessions-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-RFSG instrument sessions required to access the pin. If any instrument has more than one port connected to that pin in other sites within the given context, the VI returns an error. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconduc

### Pin to NI-RFSG Sessions

Returns the NI-RFSG instrument sessions required to access the pin. If any instrument has more than one port connected to that pin in other sites within the given context, the VI returns an error.

[IMAGE alt='icon' src='pintonirfsgsessions-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — specifies the name of the pin or pin group to translate to instrument sessions. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Sessions — returns the NI-RFSG instrument sessions for the instruments connected to the pin for all sites in the Semiconductor Module context. Ports — returns the port information for the associated instrument sessions connections to the pin. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Pin to NI-RFSG Session(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/pintonirfsgsingledeembeddingdata-vi.html language=enus -->
## TOPIC 00211: Pin to Single NI-RFSG De-Embedding Data

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/pintonirfsgsingledeembeddingdata-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/pintonirfsgsingledeembeddingdata-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-RFSG de-embedding path and orientation associated with the instrument connection to the pin. If more than one pin connection is found, the VI returns an error. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context obj

### Pin to Single NI-RFSG De-Embedding Data

Returns the NI-RFSG de-embedding path and orientation associated with the instrument connection to the pin. If more than one pin connection is found, the VI returns an error.

[IMAGE alt='icon' src='pintonirfsgsingledeembeddingdata-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — specifies the name of the pin associated with the instrument. If more than one pin connection is found, the VI returns an error. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. De-Embedding File — returns the paths and RFSG orientation of the S2P file that characterizes the de-embedding network. If the path is an absolute path, the VI returns the absolute path whether the file exists or not. If the path is a relative path and the file exists relative to the path of the pin map file, the VI returns the absolute path of the existing file. Otherwise, the VI returns a string without error. Path — Orientation — Deembedding Orientation specifies the orientation of the data in the S2P file relative to the port you specify. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |
| Path — Orientation — Deembedding Orientation specifies the orientation of the data in the S2P file relative to the port you specify. |

Parent topic:

Pin to NI-RFSG De-Embedding Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/setnirfsgsession-vi.html language=enus -->
## TOPIC 00212: Set NI-RFSG Session

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/setnirfsgsession-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/rf/rfsg/setnirfsgsession-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Associates an instrument session with an NI-RFSG instrument name. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cstr.png Instrument Name is the instrument name in the pin map file for the corresponding session. civrn

### Set NI-RFSG Session

Associates an instrument session with an NI-RFSG instrument name.

[IMAGE alt='icon' src='setnirfsgsession-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Instrument Name — is the instrument name in the pin map file for the corresponding session. NI-RFSG Session — is the instrument session for the corresponding instrument name. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

NI-RFSG

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/scope/getallniscopeinstrumentnames-vi.html language=enus -->
## TOPIC 00213: Get All NI-SCOPE Instrument Names

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/scope/getallniscopeinstrumentnames-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/scope/getallniscopeinstrumentnames-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns instrument names and comma-separated instrument names that belong to the same group for all NI-SCOPE instruments in the Semiconductor Module context. You can use instrument names and comma-separated lists of instrument names to open driver sessions. icon Inputs/Outputs coarn.png Semiconducto

### Get All NI-SCOPE Instrument Names

Returns instrument names and comma-separated instrument names that belong to the same group for all NI-SCOPE instruments in the Semiconductor Module context. You can use instrument names and comma-separated lists of instrument names to open driver sessions.

[IMAGE alt='icon' src='getallniscopeinstrumentnames-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Names — returns an array of instrument names and comma-separated lists of instrument names that belong to the same group for all NI-SCOPE instruments in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

NI-SCOPE

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/scope/getallniscopesessions-vi.html language=enus -->
## TOPIC 00214: Get All NI-SCOPE Sessions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/scope/getallniscopesessions-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/scope/getallniscopesessions-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns all NI-SCOPE instrument sessions in the Semiconductor Module context. You can use instrument sessions to close driver sessions. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cerrcodeclst.png error in (no erro

### Get All NI-SCOPE Sessions

Returns all NI-SCOPE instrument sessions in the Semiconductor Module context. You can use instrument sessions to close driver sessions.

[IMAGE alt='icon' src='getallniscopesessions-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Sessions — returns the instrument sessions for all NI-SCOPE instruments in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

NI-SCOPE

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/scope/pin-s-toniscopesession-s-vi.html language=enus -->
## TOPIC 00215: Pin(s) To NI-SCOPE Session(s)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/scope/pin-s-toniscopesession-s-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/scope/pin-s-toniscopesession-s-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-SCOPE instrument sessions and channel lists required to access one or more pins. You must manually select the polymorphic instance you want to use. Select the single pin or multiple pins polymorphic instance based on the number of pins the test is designed to test. Select the single i

### Pin(s) To NI-SCOPE Session(s)

Returns the NI-SCOPE instrument sessions and channel lists required to access one or more pins. You must manually select the polymorphic instance you want to use. Select the single pin or multiple pins polymorphic instance based on the number of pins the test is designed to test. Select the single instrument or multiple instrument polymorphic instance based on the number of instruments you expect the pin to be connected to in the pin map. Use the multiple instrument polymorphic instances to ensure that code modules work with any pin map. Use the single instrument instance only when you know the code module will never be used with a pin map that has more than one instrument connected to the specified pins.

[IMAGE alt='icon' src='pin-s-toniscopesession-s-vi.png']

- [Pins To NI-SCOPE Session](../../../../../menus/categories/ni-semiconductormodule/pinmap/scope/pinstoniscopesession-vi.html) Returns the NI-SCOPE instrument session and channel list required to access the pins. If more than one instrument session is required to access the pins, the VI returns an error. Each group of NI-SCOPE instruments in the pin map creates a single instrument session.
- [Pins To NI-SCOPE Sessions](../../../../../menus/categories/ni-semiconductormodule/pinmap/scope/pinstoniscopesessions-vi.html) Returns the NI-SCOPE instrument sessions and channel lists required to access the pins.
- [Pin To NI-SCOPE Session](../../../../../menus/categories/ni-semiconductormodule/pinmap/scope/pintoniscopesession-vi.html) Returns the NI-SCOPE instrument session and channel list required to access the pin. If more than one instrument session is required to access the pin, the VI returns an error. Each group of NI-SCOPE instruments in the pin map creates a single instrument session.
- [Pin To NI-SCOPE Sessions](../../../../../menus/categories/ni-semiconductormodule/pinmap/scope/pintoniscopesessions-vi.html) Returns the NI-SCOPE instrument sessions and channel lists required to access the pin.

Parent topic:

NI-SCOPE

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/scope/pinstoniscopesession-vi.html language=enus -->
## TOPIC 00216: Pins To NI-SCOPE Session

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/scope/pinstoniscopesession-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/scope/pinstoniscopesession-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-SCOPE instrument session and channel list required to access the pins. If more than one instrument session is required to access the pins, the VI returns an error. Each group of NI-SCOPE instruments in the pin map creates a single instrument session. icon Inputs/Outputs coarn.png Semi

### Pins To NI-SCOPE Session

Returns the NI-SCOPE instrument session and channel list required to access the pins. If more than one instrument session is required to access the pins, the VI returns an error. Each group of NI-SCOPE instruments in the pin map creates a single instrument session.

[IMAGE alt='icon' src='pinstoniscopesession-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pins — specifies the names of the pins or pin groups to translate to an instrument session and a channel list. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context — is the pin query context object that tracks the session and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Session — returns the NI-SCOPE instrument session for the instrument connected to pins for all sites in the Semiconductor Module context. Channel List — returns the comma-separated channel lists required to access pins for all sites in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Pin(s) To NI-SCOPE Session(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/scope/pinstoniscopesessions-vi.html language=enus -->
## TOPIC 00217: Pins To NI-SCOPE Sessions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/scope/pinstoniscopesessions-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/scope/pinstoniscopesessions-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-SCOPE instrument sessions and channel lists required to access the pins. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. c1ddaqmxscale.png Pins specifies the names of the pins or pin groups to translate

### Pins To NI-SCOPE Sessions

Returns the NI-SCOPE instrument sessions and channel lists required to access the pins.

[IMAGE alt='icon' src='pinstoniscopesessions-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pins — specifies the names of the pins or pin groups to translate to instrument sessions and channel lists. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Sessions — returns the NI-SCOPE instrument sessions for the instruments connected to pins for all sites in the Semiconductor Module context. Channel Lists — returns the comma-separated channel lists required to access the pins for all sites in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Pin(s) To NI-SCOPE Session(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/scope/pintoniscopesession-vi.html language=enus -->
## TOPIC 00218: Pin To NI-SCOPE Session

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/scope/pintoniscopesession-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/scope/pintoniscopesession-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-SCOPE instrument session and channel list required to access the pin. If more than one instrument session is required to access the pin, the VI returns an error. Each group of NI-SCOPE instruments in the pin map creates a single instrument session. icon Inputs/Outputs coarn.png Semico

### Pin To NI-SCOPE Session

Returns the NI-SCOPE instrument session and channel list required to access the pin. If more than one instrument session is required to access the pin, the VI returns an error. Each group of NI-SCOPE instruments in the pin map creates a single instrument session.

[IMAGE alt='icon' src='pintoniscopesession-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — is the name of the pin or pin group to translate to an instrument session and a channel list. If multiple sessions are required, the VI returns an error. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Session — returns the NI-SCOPE instrument session for the instrument connected to the pin in the Semiconductor Module context. Channel List — returns the comma-separated channel lists required to access the pin for all sites in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Pin(s) To NI-SCOPE Session(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/scope/pintoniscopesessions-vi.html language=enus -->
## TOPIC 00219: Pin To NI-SCOPE Sessions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/scope/pintoniscopesessions-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/scope/pintoniscopesessions-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-SCOPE instrument sessions and channel lists required to access the pin. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cdaqmxscale.png Pin is the name of the pin or pin group to translate to instrument

### Pin To NI-SCOPE Sessions

Returns the NI-SCOPE instrument sessions and channel lists required to access the pin.

[IMAGE alt='icon' src='pintoniscopesessions-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — is the name of the pin or pin group to translate to instrument sessions and channel lists. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Pin Query Context — is the pin query context object that tracks the sessions and channels associated with a pin query. TSM uses this object to publish measurements and extract data from a set of measurements. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Instrument Sessions — returns the NI-SCOPE instrument sessions for the instruments connected to the pin for all sites in the Semiconductor Module context. Channel Lists — returns the comma-separated channel lists required to access the pin for all sites in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Pin(s) To NI-SCOPE Session(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/scope/scope-mnu.html language=enus -->
## TOPIC 00220: NI-SCOPE

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/scope/scope-mnu.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/scope/scope-mnu.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI-SCOPE VIs to manage NI-SCOPE instruments and sessions. icon

### NI-SCOPE

Use the NI-SCOPE VIs to manage NI-SCOPE instruments and sessions.

[IMAGE alt='icon' src='scope-mnu.png']

- [Get All NI-SCOPE Instrument Names](../../../../../menus/categories/ni-semiconductormodule/pinmap/scope/getallniscopeinstrumentnames-vi.html) Returns instrument names and comma-separated instrument names that belong to the same group for all NI-SCOPE instruments in the Semiconductor Module context. You can use instrument names and comma-separated lists of instrument names to open driver sessions.
- [Set NI-SCOPE Session](../../../../../menus/categories/ni-semiconductormodule/pinmap/scope/setniscopesession-vi.html) Associates an instrument session with an NI-SCOPE instrument name.
- [Get All NI-SCOPE Sessions](../../../../../menus/categories/ni-semiconductormodule/pinmap/scope/getallniscopesessions-vi.html) Returns all NI-SCOPE instrument sessions in the Semiconductor Module context. You can use instrument sessions to close driver sessions.
- [Pin(s) To NI-SCOPE Session(s)](../../../../../menus/categories/ni-semiconductormodule/pinmap/scope/pin-s-toniscopesession-s-vi.html) Returns the NI-SCOPE instrument sessions and channel lists required to access one or more pins. You must manually select the polymorphic instance you want to use. Select the single pin or multiple pins polymorphic instance based on the number of pins the test is designed to test. Select the single instrument or multiple instrument polymorphic instance based on the number of instruments you expect the pin to be connected to in the pin map. Use the multiple instrument polymorphic instances to ensure that code modules work with any pin map. Use the single instrument instance only when you know the code module will never be used with a pin map that has more than one instrument connected to the specified pins.

Parent topic:

Code Module Development

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/scope/setniscopesession-vi.html language=enus -->
## TOPIC 00221: Set NI-SCOPE Session

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/scope/setniscopesession-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/scope/setniscopesession-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Associates an instrument session with an NI-SCOPE instrument name. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cstr.png Instrument Name is the instrument name in the pin map file for the corresponding session. civr

### Set NI-SCOPE Session

Associates an instrument session with an NI-SCOPE instrument name.

[IMAGE alt='icon' src='setniscopesession-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Instrument Name — is the instrument name in the pin map file for the corresponding session. Instrument Session — specifies the instrument session for the corresponding instrument name. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

NI-SCOPE

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/site-and-global-data/getglobaldata-vi.html language=enus -->
## TOPIC 00222: Get Global Data

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/site-and-global-data/getglobaldata-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/site-and-global-data/getglobaldata-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a global data item that a previous call to the Set Global Data VI stored. You cannot obtain LabVIEW class references from this VI. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cstr.png Data Id specifies the

### Get Global Data

Returns a global data item that a previous call to the Set Global Data VI stored. You cannot obtain LabVIEW class references from this VI.

[IMAGE alt='icon' src='getglobaldata-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Data Id — specifies the unique ID to distinguish the data. This parameter must match a value you specify in a call to the Set Global Data VI. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Data — returns the specified global data item that a previous call to the Set Global Data VI stores. If no data with the specified Data Id parameter exists, the VI returns an error. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Site and Global Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/site-and-global-data/getsitedata-vi.html language=enus -->
## TOPIC 00223: Get Site Data

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/site-and-global-data/getsitedata-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/site-and-global-data/getsitedata-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns per-site data that a previous call to the Set Site Data VI stores. The returned array contains the data the Semiconductor Module context stores for each site in the same order as the sites that the Get Site Numbers VI returns. If data with the specified Data Id does not exist for every site

### Get Site Data

Returns per-site data that a previous call to the Set Site Data VI stores. The returned array contains the data the Semiconductor Module context stores for each site in the same order as the sites that the Get Site Numbers VI returns. If data with the specified **Data Id** does not exist for every site in the Semiconductor Module Context, the VI returns an error. You cannot obtain LabVIEW class references from this VI.

[IMAGE alt='icon' src='getsitedata-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Data Id — specifies the unique ID to distinguish the data. This parameter must match a value you specify in a call to the Set Site Data VI. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Site Data — specifies an array of data with one element for each site in the system or one element for each site in the Semiconductor Module Context. If the array is empty, the VI deletes any data with the specified Data Id parameter if it exists. If the array contains data for each site in the Semiconductor Module context, each item in the array contains data for the site specified by the corresponding item in the Get Site Numbers VI. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Site and Global Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/site-and-global-data/globaldataexists-vi.html language=enus -->
## TOPIC 00224: Global Data Exists?

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/site-and-global-data/globaldataexists-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/site-and-global-data/globaldataexists-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a Boolean value indicating whether global data exists for the data ID specified by the Data Id parameter. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cstr.png Data Id specifies the unique ID to distinguish

### Global Data Exists?

Returns a Boolean value indicating whether global data exists for the data ID specified by the **Data Id** parameter.

[IMAGE alt='icon' src='globaldataexists-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Data Id — specifies the unique ID to distinguish the data. This parameter must match a value you specify in a call to the Set Global Data VI. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Global Data Exists? — indicates whether the specified Data Id parameter has data associated with it. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Site and Global Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/site-and-global-data/setglobaldata-vi.html language=enus -->
## TOPIC 00225: Set Global Data

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/site-and-global-data/setglobaldata-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/site-and-global-data/setglobaldata-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Associates a data item with a data ID. You can use this VI to store an instrument session or other data you initialize in a central location but access from multiple sites. The data item is accessible from a process model controller execution and all of its test socket executions. You cannot pass La

### Set Global Data

Associates a data item with a data ID. You can use this VI to store an instrument session or other data you initialize in a central location but access from multiple sites. The data item is accessible from a process model controller execution and all of its test socket executions. You cannot pass LabVIEW class references to this VI.

[IMAGE alt='icon' src='setglobaldata-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Data Id — specifies a unique ID to distinguish the data. Data — specifies a data item to store and later retrieve using the specified data ID. If the data item is an empty variant, the VI deletes the data with the specified Data Id if it exists. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Site and Global Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/site-and-global-data/setsitedata-vi.html language=enus -->
## TOPIC 00226: Set Site Data

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/site-and-global-data/setsitedata-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/site-and-global-data/setsitedata-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Associates a data item with each site. You can associate data with all sites or with the subset of sites in the Semiconductor Module context. You can use this VI to store instrument sessions or other per-site data you initialize in a central location but access within each site. The data item is acc

### Set Site Data

Associates a data item with each site. You can associate data with all sites or with the subset of sites in the Semiconductor Module context. You can use this VI to store instrument sessions or other per-site data you initialize in a central location but access within each site. The data item is accessible from a process model controller execution and the site with which the data is associated. You cannot pass LabVIEW class references to this VI.

[IMAGE alt='icon' src='setsitedata-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Data Id — specifies a unique ID to distinguish the data. Site Data — specifies an array of data with one element for each site in the system or one element for each site in the Semiconductor Module Context. If the array is empty, the VI deletes any data with the specified Data Id parameter if it exists. If the array contains data for each site in the Semiconductor Module context, each item in the array contains data for the site specified by the corresponding item in the Get Site Numbers VI. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Site and Global Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/site-and-global-data/site-and-global-data-mnu.html language=enus -->
## TOPIC 00227: Site and Global Data

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/site-and-global-data/site-and-global-data-mnu.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/site-and-global-data/site-and-global-data-mnu.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Site and Global data VIs to manage site and global data. icon

### Site and Global Data

Use the Site and Global data VIs to manage site and global data.

[IMAGE alt='icon' src='site-and-global-data-mnu.png']

- [Set Site Data](../../../../../menus/categories/ni-semiconductormodule/pinmap/site-and-global-data/setsitedata-vi.html) Associates a data item with each site. You can associate data with all sites or with the subset of sites in the Semiconductor Module context. You can use this VI to store instrument sessions or other per-site data you initialize in a central location but access within each site. The data item is accessible from a process model controller execution and the site with which the data is associated. You cannot pass LabVIEW class references to this VI.
- [Get Site Data](../../../../../menus/categories/ni-semiconductormodule/pinmap/site-and-global-data/getsitedata-vi.html) Returns per-site data that a previous call to the Set Site Data VI stores. The returned array contains the data the Semiconductor Module context stores for each site in the same order as the sites that the Get Site Numbers VI returns. If data with the specified Data Id does not exist for every site in the Semiconductor Module Context, the VI returns an error. You cannot obtain LabVIEW class references from this VI.
- [Site Data Exists?](../../../../../menus/categories/ni-semiconductormodule/pinmap/site-and-global-data/sitedataexists-vi.html) Returns a Boolean value indicating whether site data exists for the data ID specified by the Data Id parameter. If a data item with the specified Data Id exists for some, but not all, sites in the Semiconductor Module Context, the VI returns an error.
- [Set Global Data](../../../../../menus/categories/ni-semiconductormodule/pinmap/site-and-global-data/setglobaldata-vi.html) Associates a data item with a data ID. You can use this VI to store an instrument session or other data you initialize in a central location but access from multiple sites. The data item is accessible from a process model controller execution and all of its test socket executions. You cannot pass LabVIEW class references to this VI.
- [Get Global Data](../../../../../menus/categories/ni-semiconductormodule/pinmap/site-and-global-data/getglobaldata-vi.html) Returns a global data item that a previous call to the Set Global Data VI stored. You cannot obtain LabVIEW class references from this VI.
- [Global Data Exists?](../../../../../menus/categories/ni-semiconductormodule/pinmap/site-and-global-data/globaldataexists-vi.html) Returns a Boolean value indicating whether global data exists for the data ID specified by the Data Id parameter.

Parent topic:

Code Module Development

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/site-and-global-data/sitedataexists-vi.html language=enus -->
## TOPIC 00228: Site Data Exists?

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/site-and-global-data/sitedataexists-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/site-and-global-data/sitedataexists-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a Boolean value indicating whether site data exists for the data ID specified by the Data Id parameter. If a data item with the specified Data Id exists for some, but not all, sites in the Semiconductor Module Context, the VI returns an error. icon Inputs/Outputs coarn.png Semiconductor Modu

### Site Data Exists?

Returns a Boolean value indicating whether site data exists for the data ID specified by the **Data Id** parameter. If a data item with the specified **Data Id** exists for some, but not all, sites in the Semiconductor Module Context, the VI returns an error.

[IMAGE alt='icon' src='sitedataexists-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Data Id — specifies the unique ID to distinguish the data. This parameter must match a value you specify in a call to the Set Site Data VI. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Site Data Exists? — indicates whether the specified Data Id parameter has data associated with it. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Site and Global Data

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/specs/namespacedsymbol-s-tovalue-s-vi.html language=enus -->
## TOPIC 00229: Get Specification(s) Value(s)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/specs/namespacedsymbol-s-tovalue-s-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/specs/namespacedsymbol-s-tovalue-s-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value or values calculated for the variables in the Semiconductor Module context specifications file. icon

### Get Specification(s) Value(s)

Returns the value or values calculated for the variables in the Semiconductor Module context specifications file.

[IMAGE alt='icon' src='namespacedsymbol-s-tovalue-s-vi.png']

- [Get Specification Value](../../../../../menus/categories/ni-semiconductormodule/pinmap/specs/namespacedsymboltovalue-vi.html) Returns the value calculated from the Symbol parameter in the Semiconductor Module context specifications file. If the associated specifications file or symbols cannot be found, the VI returns an error.
- [Get Specifications Values](../../../../../menus/categories/ni-semiconductormodule/pinmap/specs/namespacedsymbolstovalues-vi.html) Returns the values calculated from the Symbols parameter in the Semiconductor Module context specifications file. If the associated specifications file or symbols cannot be found, the VI returns an error.

Parent topic:

Specifications

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/specs/namespacedsymbolstovalues-vi.html language=enus -->
## TOPIC 00230: Get Specifications Values

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/specs/namespacedsymbolstovalues-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/specs/namespacedsymbolstovalues-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the values calculated from the Symbols parameter in the Semiconductor Module context specifications file. If the associated specifications file or symbols cannot be found, the VI returns an error. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Se

### Get Specifications Values

Returns the values calculated from the **Symbols** parameter in the Semiconductor Module context specifications file. If the associated specifications file or symbols cannot be found, the VI returns an error.

[IMAGE alt='icon' src='namespacedsymbolstovalues-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Symbols — is the array of variable strings to look up in the Semiconductor Module context specifications file to obtain calculated values. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Values — returns the calculated values for the symbols in the Semiconductor Module context specifications file. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Get Specification(s) Value(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/specs/namespacedsymboltovalue-vi.html language=enus -->
## TOPIC 00231: Get Specification Value

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/specs/namespacedsymboltovalue-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/specs/namespacedsymboltovalue-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value calculated from the Symbol parameter in the Semiconductor Module context specifications file. If the associated specifications file or symbols cannot be found, the VI returns an error. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semi

### Get Specification Value

Returns the value calculated from the **Symbol** parameter in the Semiconductor Module context specifications file. If the associated specifications file or symbols cannot be found, the VI returns an error.

[IMAGE alt='icon' src='namespacedsymboltovalue-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Symbol — is the variable string to look up in the Semiconductor Module context specifications file to obtain a calculated value. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Value — returns the calculated value for the Symbol parameter in the Semiconductor Module context specifications file. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Get Specification(s) Value(s)

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/specs/specs-mnu.html language=enus -->
## TOPIC 00232: Specifications

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/specs/specs-mnu.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/specs/specs-mnu.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Specifications VIs to obtain resolved values defined in the specification file the test program specifies. icon

### Specifications

Use the Specifications VIs to obtain resolved values defined in the specification file the test program specifies.

[IMAGE alt='icon' src='specs-mnu.png']

- [Get Specification(s) Value(s)](../../../../../menus/categories/ni-semiconductormodule/pinmap/specs/namespacedsymbol-s-tovalue-s-vi.html) Returns the value or values calculated for the variables in the Semiconductor Module context specifications file.
- [Specification](../../../../../menus/categories/ni-semiconductormodule/pinmap/tagprovider/tsm-specification-ctl.html) Contains a list of specifications for the linked sequence file(s).

Parent topic:

Code Module Development

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/switching/getswitchnames-vi.html language=enus -->
## TOPIC 00233: Get All Switch Names

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/switching/getswitchnames-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/switching/getswitchnames-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the names of all switches of the type you specify in the Multiplexer Type Id parameter in the Semiconductor Module context. You can use switch names to open driver sessions. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module cont

### Get All Switch Names

Returns the names of all switches of the type you specify in the **Multiplexer Type Id** parameter in the Semiconductor Module context. You can use switch names to open driver sessions.

[IMAGE alt='icon' src='getswitchnames-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Multiplexer Type Id — specifies the type ID for the multiplexer in the pin map file. When you add a multiplexer to the pin map file, you can define a type ID for the multiplexer, such as the driver name. Multiplexers in the pin map that do not specify a type ID have a default ID of NIGenericMultiplexer. Leave this parameter unwired to use the default value. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Switch Names — returns the names of all switches in the Semiconductor Module context. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Switching

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/switching/getswitchsessions-vi.html language=enus -->
## TOPIC 00234: Get All Switch Sessions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/switching/getswitchsessions-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/switching/getswitchsessions-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns all sessions for switches of the type you specify in the Multiplexer Type Id parameter in the Semiconductor Module context. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cstr.png Multiplexer Type Id specifies

### Get All Switch Sessions

Returns all sessions for switches of the type you specify in the **Multiplexer Type Id** parameter in the Semiconductor Module context.

[IMAGE alt='icon' src='getswitchsessions-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Multiplexer Type Id — specifies the type ID for the multiplexer in the pin map file. When you add a multiplexer to the pin map file, you can define a type ID for the multiplexer, such as the driver name. Multiplexers in the pin map that do not specify a type ID have a default ID of NIGenericMultiplexer. Leave this parameter unwired to use the default value. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Session Data — returns sessions to all switches of the type you specify in the Multiplexer Type Id in the Semiconductor Module context for which you set session data. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Switching

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/switching/pintoswitchsessions-vi.html language=enus -->
## TOPIC 00235: Pin to Switch Sessions

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/switching/pintoswitchsessions-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/switching/pintoswitchsessions-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the switch sessions, switch routes, and new Semiconductor Module context objects required to access a switched pin. You must always close references to the Semiconductor Module contexts, even if you do not use them in your code module. icon Inputs/Outputs coarn.png Semiconductor Module Conte

### Pin to Switch Sessions

Returns the switch sessions, switch routes, and new Semiconductor Module context objects required to access a switched pin. You must always close references to the Semiconductor Module contexts, even if you do not use them in your code module.

[IMAGE alt='icon' src='pintoswitchsessions-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Pin — specifies the name of the pin to translate to sessions and switch routes parameters. Multiplexer Type Id — specifies the type ID for the multiplexer in the pin map file. When you add a multiplexer to the pin map file, you can define a type ID for the multiplexer, such as the driver name. Multiplexers in the pin map that do not specify a type ID have a default ID of NIGenericMultiplexer. Leave this parameter unwired to use the default value. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. Semiconductor Module Contexts — returns an array of Semiconductor Module context objects. Each element in the array represents a site that must be executed serially. Use each Semiconductor Module context object to query the pin map and publish data. You must always close references to the Semiconductor Module contexts, even if you do not use them in your code module. Session Data — returns the session data required to access the switch that connects an instrument channel to the pin. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. Switch Routes — returns the routes required to connect an instrument channel to the pin. |
| --- |

Parent topic:

Switching

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/switching/setswitchsession-vi.html language=enus -->
## TOPIC 00236: Set Switch Session

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/switching/setswitchsession-vi.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/switching/setswitchsession-vi.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Associates an open switch session with the switch name of the type you specify in the Multiplexer Type Id parameter. icon Inputs/Outputs coarn.png Semiconductor Module Context is a valid ActiveX reference to a Semiconductor Module context object. cstr.png Switch Name is the switch name in the pin ma

### Set Switch Session

Associates an open switch session with the switch name of the type you specify in the **Multiplexer Type Id** parameter.

[IMAGE alt='icon' src='setswitchsession-vi.png']

#### Inputs/Outputs

| Semiconductor Module Context — is a valid ActiveX reference to a Semiconductor Module context object. Switch Name — is the switch name in the pin map file for the corresponding session. Session Data — is the switch session for the switch name. Use the variant data type to properly store different types of sessions. error in (no error) — describes error conditions that occur before this VI or function runs. The default is no error. If an error occurred before this VI or function runs, the VI or function passes the error in value to error out. This VI or function runs normally only if no error occurred before this VI or function runs. If an error occurs while this VI or function runs, it runs normally and sets its own error status in error out. Multiplexer Type Id — specifies the type ID for the multiplexer in the pin map file. When you add a multiplexer to the pin map file, you can define a type ID for the multiplexer, such as the driver name. Multiplexers in the pin map that do not specify a type ID have a default ID of NIGenericMultiplexer. Leave this parameter unwired to use the default value. Semiconductor Module Context Out — returns the Semiconductor Module Context parameter unchanged. error out — contains error information. If error in indicates that an error occurred before this VI or function ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Switching

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/switching/switching-mnu.html language=enus -->
## TOPIC 00237: Switching

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/switching/switching-mnu.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/switching/switching-mnu.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Switching VIs to store and return switch sessions, return the names of all switches defined in the pin map, and access a switched pin. icon

### Switching

Use the Switching VIs to store and return switch sessions, return the names of all switches defined in the pin map, and access a switched pin.

[IMAGE alt='icon' src='switching-mnu.png']

- [Get All Switch Names](../../../../../menus/categories/ni-semiconductormodule/pinmap/switching/getswitchnames-vi.html) Returns the names of all switches of the type you specify in the Multiplexer Type Id parameter in the Semiconductor Module context. You can use switch names to open driver sessions.
- [Set Switch Session](../../../../../menus/categories/ni-semiconductormodule/pinmap/switching/setswitchsession-vi.html) Associates an open switch session with the switch name of the type you specify in the Multiplexer Type Id parameter.
- [Get All Switch Sessions](../../../../../menus/categories/ni-semiconductormodule/pinmap/switching/getswitchsessions-vi.html) Returns all sessions for switches of the type you specify in the Multiplexer Type Id parameter in the Semiconductor Module context.
- [Pin to Switch Sessions](../../../../../menus/categories/ni-semiconductormodule/pinmap/switching/pintoswitchsessions-vi.html) Returns the switch sessions, switch routes, and new Semiconductor Module context objects required to access a switched pin. You must always close references to the Semiconductor Module contexts, even if you do not use them in your code module.

Parent topic:

Code Module Development

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/tagprovider/tsm-inputdataid-ctl.html language=enus -->
## TOPIC 00238: Input Data Id

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/tagprovider/tsm-inputdataid-ctl.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/tagprovider/tsm-inputdataid-ctl.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains a list of input data IDs for the linked sequence file(s). Displays only input data IDs on Semiconductor steps whose code module is set to the current VI. icon Data type cdaqmxscale.png Input Data Id Contains a list of input data IDs for the linked sequence file(s). Displays only input data

### Input Data Id

Contains a list of input data IDs for the linked sequence file(s). Displays only input data IDs on Semiconductor steps whose code module is set to the current VI.

[IMAGE alt='icon' src='tsm-inputdataid-ctl.png']

#### Data type

| Input Data Id — Contains a list of input data IDs for the linked sequence file(s). Displays only input data IDs on Semiconductor steps whose code module is set to the current VI. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/tagprovider/tsm-pin-ctl.html language=enus -->
## TOPIC 00239: Pin

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/tagprovider/tsm-pin-ctl.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/tagprovider/tsm-pin-ctl.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains a list of pins for the linked sequence file(s). icon Data type cdaqmxscale.png Pin Contains a list of pins for the linked sequence file(s).

### Pin

Contains a list of pins for the linked sequence file(s).

[IMAGE alt='icon' src='tsm-pin-ctl.png']

#### Data type

| Pin — Contains a list of pins for the linked sequence file(s). |
| --- |

Parent topic:

Code Module Development

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/tagprovider/tsm-publisheddataid-ctl.html language=enus -->
## TOPIC 00240: Published Data Id

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/tagprovider/tsm-publisheddataid-ctl.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/tagprovider/tsm-publisheddataid-ctl.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains a list of published data IDs for the linked sequence file(s). Displays only published data IDs for tests on a Semiconductor Multi Test step whose code module is set to the current VI. icon Data type cdaqmxscale.png Published Data Id Contains a list of published data IDs for the linked seque

### Published Data Id

Contains a list of published data IDs for the linked sequence file(s). Displays only published data IDs for tests on a Semiconductor Multi Test step whose code module is set to the current VI.

[IMAGE alt='icon' src='tsm-publisheddataid-ctl.png']

#### Data type

| Published Data Id — Contains a list of published data IDs for the linked sequence file(s). Displays only published data IDs for tests on a Semiconductor Multi Test step whose code module is set to the current VI. |
| --- |

Parent topic:

Code Module Development

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/tagprovider/tsm-relay-ctl.html language=enus -->
## TOPIC 00241: Relay

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/tagprovider/tsm-relay-ctl.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/tagprovider/tsm-relay-ctl.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains a list of relays for the linked sequence file(s). icon Data type cdaqmxscale.png Relay Contains a list of relays for the linked sequence file(s).

### Relay

Contains a list of relays for the linked sequence file(s).

[IMAGE alt='icon' src='tsm-relay-ctl.png']

#### Data type

| Relay — Contains a list of relays for the linked sequence file(s). |
| --- |

Parent topic:

Relay Driver

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/tagprovider/tsm-relayconfiguration-ctl.html language=enus -->
## TOPIC 00242: Relay Configuration

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/tagprovider/tsm-relayconfiguration-ctl.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/tagprovider/tsm-relayconfiguration-ctl.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains a list of relay configurations for the linked sequence file(s). icon Data type cdaqmxscale.png Relay Configuration Contains a list of relay configurations for the linked sequence file(s).

### Relay Configuration

Contains a list of relay configurations for the linked sequence file(s).

[IMAGE alt='icon' src='tsm-relayconfiguration-ctl.png']

#### Data type

| Relay Configuration — Contains a list of relay configurations for the linked sequence file(s). |
| --- |

Parent topic:

Relay Driver

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=menus/categories/ni-semiconductormodule/pinmap/tagprovider/tsm-specification-ctl.html language=enus -->
## TOPIC 00243: Specification

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `menus/categories/ni-semiconductormodule/pinmap/tagprovider/tsm-specification-ctl.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/menus/categories/ni-semiconductormodule/pinmap/tagprovider/tsm-specification-ctl.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains a list of specifications for the linked sequence file(s). icon Data type cdaqmxscale.png Specification Contains a list of specifications for the linked sequence file(s).

### Specification

Contains a list of specifications for the linked sequence file(s).

[IMAGE alt='icon' src='tsm-specification-ctl.png']

#### Data type

| Specification — Contains a list of specifications for the linked sequence file(s). |
| --- |

Parent topic:

Specifications

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=Obsolete_VIs.html language=enus -->
## TOPIC 00244: Obsolete VIs (TSM)

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `Obsolete_VIs.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/Obsolete_VIs.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `topic`
- source_description: The following VIs are now obsolete. NI supports these VIs but recommends updating files for future compatibility. Note: Because the name of some of the VIs remains the same, verify the filename of the VI to ensure you are using the updated version of the VI. Obsolete VIPreferred VI 2 Pins to NI-RFPM

### Obsolete VIs (TSM)

The following VIs are now obsolete. NI supports these VIs but recommends updating files for future compatibility.

Note: Because the name of some of the VIs remains the same, verify the filename of the VI to ensure you are using the updated version of the VI.

| Obsolete VI | Preferred VI |
| --- | --- |
| 2 Pins to NI-RFPM Sessions2PinsToNIRFPMSessions.vi | 2 Pins to NI-RFPM Sessions2PinsToNIRFPMSessionsWithPaths.vi |
| Create Multisite Data For Analog OutputCreateMultisiteDataForAnalogOutput.vi | Create Multisite Data For Analog OutputCreateMultisiteDataForDAQmxAnalogOutput.vi |
| Create Multisite Digital WaveformsCreateMultisiteDigitalWaveforms.vi | Create Multisite Digital WaveformsCreateMultisiteDigitalWaveformsWithContext.vi |
| Get All NI-DCPower Instrument NamesGetAllNIDCPowerInstrumentNames.vi | Get All NI-DCPower Resource StringsGetAllNIDCPowerResourceStrings.vi |
| Get All NI-RFPM De-embedding DataGetAllNIRFPMDeembeddingData.vi | Get All NI-RFPM De-embedding DataGetAllNIRFPMDeembeddingDataWithPaths.vi |
| Get Session and Channel IndexGetSessionAndChannelIndex.vi | Get Session and Channel IndexGetSessionAndChannelIndexWithContext.vi |
| Pins to NI-HSDIO Channel MasksPinsToNIHSDIOChannelMasks.vi | Get NI-HSDIO Channel MasksPinsToNIHSDIOChannelMasksWithContext.vi |
| Pin(s) to NI-RFPM SessionsPinsToNIRFPMSessions.vi | Pin(s) to NI-RFPM SessionsPinsToNIRFPMSessionsWithPaths.vi |
| Publish DataPublishData.vi | Publish DataPublishDataWithContext.vi |
| Rearrange Digital Multisite WaveformsRearrangeDigitalMultisiteWaveforms.vi | Rearrange Digital Multisite WaveformsRearrangeDigitalMultisiteWaveformsWithContext.vi |
| Set NI-DCPower SessionSetNIDCPowerSession.vi | Set NI-DCPower Session with Resource StringSetNIDCPowerSessionWithResourceString.vi |

<!--NI_TOPIC bundle=tsm-labview-code-module-api-ref path=Using_NIDaqmx_with_TSM.html language=enus -->
## TOPIC 00245: Using NI-DAQmx with TSM

- bundle_id: `tsm-labview-code-module-api-ref`
- source_path: `Using_NIDaqmx_with_TSM.html`
- source_url: https://docs-be.ni.com/bundle/tsm-labview-code-module-api-ref/raw/resource/enus/Using_NIDaqmx_with_TSM.html
- document_id: `tsm-labview-code-module-api-ref`
- page_type: `leaf`
- content_type: `topic`
- source_description: Refer to the following pin map, process setup, analog input, analog output, and process cleanup suggestions when you use NI-DAQmx with TSM. Pin Map The TSM pin map defines NI-DAQmx tasks instead of NI-DAQmx instruments to support channel expansion. Each task in the pin map uses a channelList attribu

### Using NI-DAQmx with TSM

Refer to the following pin map, process setup, analog input, analog output, and process cleanup suggestions when you use NI-DAQmx with TSM.

#### Pin Map

The TSM pin map defines NI-DAQmx tasks instead of NI-DAQmx instruments to support channel expansion. Each task in the pin map uses a channelList attribute, which can contain channels from one or more NI-DAQmx instruments.

- Channel names consist of a device identifier and a slash (/) followed by a channel identifier.
- Channel ranges are specified using a colon between two channel numbers.
- Lists of channel names and ranges are separated using commas.
- Example: dev1/ai0:1, dev1/ai2

Each task also uses a taskType attribute. Multiple tasks can use the same task type. Pin queries that refer to tasks of more than one task type return an error.

#### Process Setup

Use the TSM Get All NI-DAQmx Task Names VI to return the task names and channel lists defined by the pin map.

Use the NI-DAQmx API to create and set up tasks. For best performance, start tasks in the process setup of the test program and store them using the Set NI-DAQmx Task VI.

Figure 1.

[IMAGE alt='image' src='images/tsm_nidaqmx_process_setup.png']

#### Analog Input

Use the TSM Pin(s) to NI-DAQmx Task(s) VI to perform pin queries. Connect the Channel Lists output to the ChannelsToRead property of a DAQmx Read property node, and use the DAQmx Read VI to read data.

Use the TSM Publish Data VI to publish measurement data to Semiconductor Multi Test step type instances for all sites.

Figure 2.

[IMAGE alt='image' src='images/tsm_nidaqmx_analog_input.png']

#### Analog Output

Use the TSM Pin(s) to NI-DAQmx Task(s) VI to perform pin queries. Use the TSM Create Multisite Data for Analog Output VI to write data to the correct channels.

You can specify per-pin or per-site input data. Use the Idle Value input to specify values for channels not connected to sites.

Figure 3.

[IMAGE alt='image' src='images/tsm_nidaqmx_analog_output.png']

#### Process Cleanup

Use the TSM Get All NI-DAQmx Tasks VI to return tasks of a specified type, or all tasks by passing an empty string. Use the NI-DAQmx API to stop and clear all tasks.

Figure 4.

[IMAGE alt='image' src='images/tsm_nidaqmx_cleanup.png']
