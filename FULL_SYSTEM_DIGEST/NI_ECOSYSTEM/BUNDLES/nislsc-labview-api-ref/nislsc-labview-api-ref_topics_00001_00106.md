# NI DOCUMENT BUNDLE: nislsc-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=nislsc-labview-api-ref start=1 end=106 -->
<!--NI_TOPIC bundle=nislsc-labview-api-ref path=menus/categories/measurement/slsc-mnu.html language=enus -->
## TOPIC 00001: NI-SLSC

- bundle_id: `nislsc-labview-api-ref`
- source_path: `menus/categories/measurement/slsc-mnu.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/menus/categories/measurement/slsc-mnu.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This help file contains information about using the SLSC VIs. icon

### NI-SLSC

This help file contains information about using the SLSC VIs.

[IMAGE alt='icon' src='slsc-mnu.png']

- [Initialize Session VI](../../../vi-lib/slsc/initialize-session-vi.html) Initializes an SLSC session.
- [Set Device Property VI](../../../vi-lib/slsc/set-device-property-vi.html) Sets the value of the specified device property for one or more devices to the provided value.
- [Set Phys Chan Property VI](../../../vi-lib/slsc/set-phys-chan-property-vi.html) Sets the value of the specified physical channel property for one or more physical channels to the provided value. Device-defined properties will not be written until a commit is called.
- [Commit Properties VI](../../../vi-lib/slsc/commit-properties-vi.html) Commits all properties with pending changes to hardware, for the specified resource(s). If you set a property multiple times between commits, only the last value will be committed.
- [Execute Command VI](../../../vi-lib/slsc/execute-command-vi.html) Executes the specified command on one or multiple devices or physical channels.
- [Close VI](../../../vi-lib/slsc/close-vi.html) Closes an SLSC session or an open SLSC command/property reference.
- [SLSC Session Property Node](../../../vi-lib/slsc/mergevis/slsc-session-property-node-vi.html) A Property Node with the SLSC Session class preselected. Property nodes may be used to access properties that are defined by the SLSC driver, but cannot be used to access properties that are defined by SLSC devices.
- [Get Device Property VI](../../../vi-lib/slsc/get-device-property-vi.html) Gets the value of the specified device property from one or more devices. You can use an array instance of this VI to get a scalar property from multiple devices with a single call to the VI.
- [Get Phys Chan Property VI](../../../vi-lib/slsc/get-phys-chan-property-vi.html) Gets the value of the specified physical channel property from one or more physical channels. You can use an array instance of this VI to get a scalar property from multiple devices with a single call to the VI.
- [Session Configuration](../../../menus/categories/measurement/slsc/sessionconfig-mnu.html) Use the Session Configuration VIs to manage sessions to devices in the SLSC system by connecting, disconnecting, reserving, and unreserving devices as well as aborting sessions.
- [NVMEM Access](../../../menus/categories/measurement/slsc/nvmem-mnu.html) Use the low-level NVMEM Access VIs to access data stored in SLSC modules' non-volatile memory. SLSC modules divide their non-volatile memory into fixed-size NVMEM areas, which are specified by name, such as "Mod1/capabilities". NVMEM areas are double-buffered to protect against data loss if an error or power loss occurs during a write. All SLSC modules support a set of standard NVMEM areas, and some may support vendor-defined areas as well. All SLSC modules also have a special "raw" pseudo-area that directly accesses the non-volatile memory, bypassing NVMEM area lookup and double-buffering.
- [Register Access](../../../menus/categories/measurement/slsc/register-mnu.html) Use the low-level Register Access VIs to access module registers. This palette displays the VIs that allow a LabVIEW application/library to directly read and write module registers.
- [Flatten Names VI](../../../vi-lib/slsc/flatten-names-vi.html) Converts an array of names into a comma-delimited list of names.
- [Unflatten Names VI](../../../vi-lib/slsc/unflatten-names-vi.html) Converts a comma-delimited list of names into an array of names. If the list contains colon-delimited ranges, they will be expanded.
- [Scaling](../../../menus/categories/measurement/slsc/scaling-mnu.html) Use the Scaling VIs to read or write scaling parameters and equations.
- [System Setup](../../../menus/categories/measurement/slsc/systemsetup-mnu.html) Use the System Setup VIs to update the local configuration file by adding, removing and renaming devices. Additionally, this palette displays VIs to reset devices and log in and out of an SLSC chassis. Use the System Node to read system properties such as the devices installed on the system. Use the Get Chassis IP or Hostname VI to get the IP or hostname of a chassis. Use the Update Chassis Firmware VI to update the firmware of the chassis.
- [API Reflection](../../../menus/categories/measurement/slsc/apireflection-mnu.html) Use the API Reflection VIs to read property and command information at run time.
- [Generic Property & Command Access](../../../menus/categories/measurement/slsc/generic-mnu.html) Use the Generic Property & Command VIs to access module properties and commands without choosing a resource type at design time. Whereas the VIs on the SLSC VIs palette allow you to omit the resource name in order to use the session defaults, the Generic Property & Command VIs automatically determine the resource type at run time based on the given resource name.

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=menus/categories/measurement/slsc/apireflection-mnu.html language=enus -->
## TOPIC 00002: API Reflection

- bundle_id: `nislsc-labview-api-ref`
- source_path: `menus/categories/measurement/slsc/apireflection-mnu.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/menus/categories/measurement/slsc/apireflection-mnu.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the API Reflection VIs to read property and command information at run time. icon

### API Reflection

Use the API Reflection VIs to read property and command information at run time.

[IMAGE alt='icon' src='apireflection-mnu.png']

- [Open Command VI](../../../../vi-lib/slsc/open-command-vi.html) Opens a reference to a command on the given resource. This allows the application to programmatically get information about the command at run time.
- [SLSC Command Property Node](../../../../vi-lib/slsc/mergevis/slsc-command-property-node-vi.html) A Property Node with the SLSC Command class preselected. You must open the property using one of the Open Command VIs before you can use SLSC Command Property Node to query information about the command.
- [Open Property VI](../../../../vi-lib/slsc/open-property-vi.html) Opens a reference to a property on the given resource. This allows the application to programmatically get information about the command at run time.
- [SLSC Property Property Node](../../../../vi-lib/slsc/mergevis/slsc-property-property-node-vi.html) A Property Node with the SLSC Property class preselected. You must open the property using one of the Open Property VIs before you can use SLSC Property Property Node to query information about the property.
- [Close VI](../../../../vi-lib/slsc/close-vi.html) Closes an SLSC session or an open SLSC command/property reference.

Parent topic:

NI-SLSC

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=menus/categories/measurement/slsc/generic-mnu.html language=enus -->
## TOPIC 00003: Generic Property & Command Access

- bundle_id: `nislsc-labview-api-ref`
- source_path: `menus/categories/measurement/slsc/generic-mnu.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/menus/categories/measurement/slsc/generic-mnu.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Generic Property & Command VIs to access module properties and commands without choosing a resource type at design time. Whereas the VIs on the SLSC VIs palette allow you to omit the resource name in order to use the session defaults, the Generic Property & Command VIs automatically determin

### Generic Property & Command Access

Use the Generic Property & Command VIs to access module properties and commands without choosing a resource type at design time. Whereas the VIs on the SLSC VIs palette allow you to omit the resource name in order to use the session defaults, the Generic Property & Command VIs automatically determine the resource type at run time based on the given resource name.

[IMAGE alt='icon' src='generic-mnu.png']

- [Get Generic Property VI](../../../../vi-lib/slsc/get-generic-property-vi.html) Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource. You can use an array instance of this VI to get a scalar property from multiple devices with a single call to the VI.
- [Set Generic Property VI](../../../../vi-lib/slsc/set-generic-property-vi.html) Sets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource.
- [Commit Properties (Generic) VI](../../../../vi-lib/slsc/commit-properties-generic-vi.html) Commits all properties with pending changes to hardware, for the specified resource(s). If you set a property multiple times between commits, only the last value will be committed.
- [Execute Generic Command VI](../../../../vi-lib/slsc/execute-generic-command-vi.html) Executes the specified command on one or multiple devices or physical channels.
- [Generic API Reflection](../../../../menus/categories/measurement/slsc/genericapireflection-mnu.html) Use the Generic API Reflection VIs to read property and command information at run time without choosing a resource type at design time. Whereas the VIs on the API Reflection VIs palette allow you to omit the resource name in order to use the session defaults, the Generic API Reflection VIs automatically determine the resource type at run time based on the given resource name.

Parent topic:

NI-SLSC

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=menus/categories/measurement/slsc/genericapireflection-mnu.html language=enus -->
## TOPIC 00004: Generic API Reflection

- bundle_id: `nislsc-labview-api-ref`
- source_path: `menus/categories/measurement/slsc/genericapireflection-mnu.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/menus/categories/measurement/slsc/genericapireflection-mnu.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Generic API Reflection VIs to read property and command information at run time without choosing a resource type at design time. Whereas the VIs on the API Reflection VIs palette allow you to omit the resource name in order to use the session defaults, the Generic API Reflection VIs automati

### Generic API Reflection

Use the Generic API Reflection VIs to read property and command information at run time without choosing a resource type at design time. Whereas the VIs on the API Reflection VIs palette allow you to omit the resource name in order to use the session defaults, the Generic API Reflection VIs automatically determine the resource type at run time based on the given resource name.

[IMAGE alt='icon' src='genericapireflection-mnu.png']

- [Open Generic Command VI](../../../../vi-lib/slsc/open-generic-command-vi.html) Opens a reference to a command on the given resource. This allows the application to programmatically get information about the command at run time, but requires you to know the proper resource string.
- [Open Generic Property VI](../../../../vi-lib/slsc/open-generic-property-vi.html) Opens a reference to a property on the given resource. This allows the application to programmatically get information about the command at run time, but requires you to know the proper resource string.
- [SLSC Command Property Node](../../../../vi-lib/slsc/mergevis/slsc-command-property-node-vi.html) A Property Node with the SLSC Command class preselected. You must open the property using one of the Open Command VIs before you can use SLSC Command Property Node to query information about the command.
- [Close VI](../../../../vi-lib/slsc/close-vi.html) Closes an SLSC session or an open SLSC command/property reference.
- [SLSC Property Property Node](../../../../vi-lib/slsc/mergevis/slsc-property-property-node-vi.html) A Property Node with the SLSC Property class preselected. You must open the property using one of the Open Property VIs before you can use SLSC Property Property Node to query information about the property.

Parent topic:

Generic Property & Command Access

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=menus/categories/measurement/slsc/scaling-mnu.html language=enus -->
## TOPIC 00005: Scaling

- bundle_id: `nislsc-labview-api-ref`
- source_path: `menus/categories/measurement/slsc/scaling-mnu.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/menus/categories/measurement/slsc/scaling-mnu.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Scaling VIs to read or write scaling parameters and equations. icon

### Scaling

Use the Scaling VIs to read or write scaling parameters and equations.

[IMAGE alt='icon' src='scaling-mnu.png']

- [Get Scaling Parameters VI](../../../../vi-lib/slsc/get-scaling-parameters-vi.html) Gets scaling parameters from a scale.
- [Set Scaling Parameters VI](../../../../vi-lib/slsc/set-scaling-parameters-vi.html) Sets scaling parameters for a scale.
- [Get Scaling Equation VI](../../../../vi-lib/slsc/get-scaling-equation-vi.html) Gets a scaling equation from a user-defined scale.
- [Set Scaling Equation VI](../../../../vi-lib/slsc/set-scaling-equation-vi.html) Sets the scaling equation for a user-defined scale.
- [Commit Scaling for Devices VI](../../../../vi-lib/slsc/commit-scaling-for-devices-vi.html) Commits all scaling parameters with pending changes to all physical channels that the devices contain. If you set scaling parameters multiple times between commits, this VI commits only the last value of the scaling parameters.

Parent topic:

NI-SLSC

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=menus/categories/measurement/slsc/sessionconfig-mnu.html language=enus -->
## TOPIC 00006: Session Configuration

- bundle_id: `nislsc-labview-api-ref`
- source_path: `menus/categories/measurement/slsc/sessionconfig-mnu.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/menus/categories/measurement/slsc/sessionconfig-mnu.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Session Configuration VIs to manage sessions to devices in the SLSC system by connecting, disconnecting, reserving, and unreserving devices as well as aborting sessions. icon

### Session Configuration

Use the Session Configuration VIs to manage sessions to devices in the SLSC system by connecting, disconnecting, reserving, and unreserving devices as well as aborting sessions.

[IMAGE alt='icon' src='sessionconfig-mnu.png']

- [Connect to Devices VI](../../../../vi-lib/slsc/connect-to-devices-vi.html) Opens network connections for the specified device(s), sharing connections to the same SLSC chassis. For each device that is provided, this VI uses the local configuration file and mDNS to look up the corresponding chassis and its hostname or IP address. If a chassis has multiple hostnames and/or IP addresses, this VI tries connecting using each one, until one succeeds or all have failed. If the connect timeout expires before a connection is successfully established, an error is returned.
- [Connect to Chassis by IP Address or Hostname VI](../../../../vi-lib/slsc/connect-to-chassis-by-ip-address-or-hostname-vi.html) Opens a network connection for a chassis by IP address or hostname. This VI shares network connections to the same chassis. If you cannot find the chassis via mDNS, ensure that the chassis is in the local configuration file. If the connect timeout expires before a connection is successfully established, this VI returns an error.
- [Disconnect from Devices VI](../../../../vi-lib/slsc/disconnect-from-devices-vi.html) Closes network connections for the specified devices. When multiple devices share a network connection because they are in the same SLSC chassis, the network connection will remain open until the last device is disconnected.
- [Reserve Devices VI](../../../../vi-lib/slsc/reserve-devices-vi.html) Reserves one or multiple devices to prevent other sessions from access the devices. You must reserve a device before using it.
- [Unreserve Devices VI](../../../../vi-lib/slsc/unreserve-devices-vi.html) Unreserves the specified device(s), allowing other sessions to access them.
- [Abort Session VI](../../../../vi-lib/slsc/abort-session-vi.html) Attempts to cancel a VI that blocks on network communications such as Connect to Devices or Add Network Chassis, making it wake up and return an error. After aborting the session, the session reference remains valid, but VIs that access network connections will return errors. To recover from an aborted session, close it and initialize a new one. Some operations, such as DNS lookups, cannot be aborted.

Parent topic:

NI-SLSC

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=menus/categories/measurement/slsc/systemsetup-mnu.html language=enus -->
## TOPIC 00007: System Setup

- bundle_id: `nislsc-labview-api-ref`
- source_path: `menus/categories/measurement/slsc/systemsetup-mnu.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/menus/categories/measurement/slsc/systemsetup-mnu.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the System Setup VIs to update the local configuration file by adding, removing and renaming devices. Additionally, this palette displays VIs to reset devices and log in and out of an SLSC chassis. Use the System Node to read system properties such as the devices installed on the system. Use the

### System Setup

Use the System Setup VIs to update the local configuration file by adding, removing and renaming devices. Additionally, this palette displays VIs to reset devices and log in and out of an SLSC chassis. Use the System Node to read system properties such as the devices installed on the system. Use the Get Chassis IP or Hostname VI to get the IP or hostname of a chassis. Use the Update Chassis Firmware VI to update the firmware of the chassis.

[IMAGE alt='icon' src='systemsetup-mnu.png']

- [Reset Devices VI](../../../../vi-lib/slsc/reset-devices-vi.html) Resets devices to their default state. This VI sends the specified devices a hardware reset signal, reinitializes module registers to their initial value, and rereads the module's non-volatile memory. If you specify a chassis, this VI resets all of the modules in the chassis. To reboot the chassis, use the Restart VI provided by the NI System Configuration API.
- [Add Network Chassis VI](../../../../vi-lib/slsc/add-network-chassis-vi.html) Adds the specified network chassis to the local configuration file. This VI connects to the specified network chassis, downloads information about the chassis and its modules, and adds the chassis and modules to the local configuration file. If the chassis has already been added, calling this function again refreshes the modules.
- [Remove Chassis VI](../../../../vi-lib/slsc/remove-chassis-vi.html) Removes the specified chassis from the local configuration file. Note that if the system and the SLSC chassis are on the same network subnet, then the SLSC driver will discover the chassis via mDNS and it will continue to show up in SLSC I/O controls, the Sys.Devices property, etc.
- [Rename Device VI](../../../../vi-lib/slsc/rename-device-vi.html) Renames the specified device to the new device name on the remote device and in the local configuration file. When renaming a chassis, the hostname of the chassis will be changed on the chassis, but it will not be updated in the local configuration file. After the network is expected to reflect the new hostname, call Add Network Chassis to update the hostname in the local configuration file.
- [SLSC System Property Node](../../../../vi-lib/slsc/mergevis/slsc-system-property-node-vi.html) A Property Node with the SLSC System class preselected. This can be used to query which devices are available on the system, without initializing a session.
- [Log In VI](../../../../vi-lib/slsc/log-in-vi.html) Saves login credentials for an SLSC chassis on the local system. When the SLSC driver opens a network connection to an SLSC chassis, it checks whether there are any saved login credentials for this chassis. If so, the SLSC driver uses the saved login credentials. Otherwise, the SLSC driver tries default credentials with anonymous as the username and an empty string as the password.
- [Log Out VI](../../../../vi-lib/slsc/log-out-vi.html) Deletes any saved credentials for this chassis.
- [Get Chassis IP or Hostname VI](../../../../vi-lib/slsc/get-chassis-ip-or-hostname-vi.html) Gets the IP address or hostname of the chassis.
- [Get Module Name VI](../../../../vi-lib/slsc/get-module-name-vi.html) Gets the name of a module on the chassis.
- [Rename Chassis and All Connected Modules VI](../../../../vi-lib/slsc/rename-chassis-and-all-connected-modules-vi.html) Renames the chassis and all modules that connect to the chassis.
- [Update Chassis Firmware VI](../../../../vi-lib/slsc/update-chassis-firmware-vi.html) Updates the firmware of the chassis.

Parent topic:

NI-SLSC

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/abort-session-vi.html language=enus -->
## TOPIC 00008: Abort Session VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/abort-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/abort-session-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Attempts to cancel a VI that blocks on network communications such as Connect to Devices or Add Network Chassis, making it wake up and return an error. After aborting the session, the session reference remains valid, but VIs that access network connections will return errors. To recover from an abor

### Abort Session VI

Attempts to cancel a VI that blocks on network communications such as Connect to Devices or Add Network Chassis, making it wake up and return an error. After aborting the session, the session reference remains valid, but VIs that access network connections will return errors. To recover from an aborted session, close it and initialize a new one. Some operations, such as DNS lookups, cannot be aborted.

[IMAGE alt='icon' src='abort-session-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Session Configuration

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/add-network-chassis-vi.html language=enus -->
## TOPIC 00009: Add Network Chassis VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/add-network-chassis-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/add-network-chassis-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified network chassis to the local configuration file. This VI connects to the specified network chassis, downloads information about the chassis and its modules, and adds the chassis and modules to the local configuration file. If the chassis has already been added, calling this functi

### Add Network Chassis VI

Adds the specified network chassis to the local configuration file. This VI connects to the specified network chassis, downloads information about the chassis and its modules, and adds the chassis and modules to the local configuration file. If the chassis has already been added, calling this function again refreshes the modules.

[IMAGE alt='icon' src='add-network-chassis-vi.png']

#### Inputs/Outputs

| password — password specifies the password for accessing the device. username — username specifies the username for accessing the device. session in — session in specifies the session to access for the given action. chassis IP address/hostname — chassis IP address/hostname specifies the IP address or hostname of the chassis to add to the system. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. connect timeout (60 sec) — connect timeout (60 sec) specifies the maximum amount of time, in seconds, to wait when connecting to the specified resource. This VI returns an error if timeout expires. Set connect timeout to -1 to use the value of the Session.TCPIP.ConnectTimeout property. session out — session out is a copy of the session in reference. chassis out — chassis out indicates the name of the chassis added to the system and configuration file. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

System Setup

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/commit-nvmem-areas-vi.html language=enus -->
## TOPIC 00010: Commit NVMEM Areas VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/commit-nvmem-areas-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/commit-nvmem-areas-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Commits pending changes to hardware for the specified NVMEM area(s). If you set the same address multiple times between commits, only the last value will be committed. icon Inputs/Outputs cgenclassrntag.png session in session in specifies the session to access for the given action. cgenclassrntag.pn

### Commit NVMEM Areas VI

Commits pending changes to hardware for the specified NVMEM area(s). If you set the same address multiple times between commits, only the last value will be committed.

[IMAGE alt='icon' src='commit-nvmem-areas-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. NVMEM areas — NVMEM areas specifies the non-volatile memory area(s) to access. If you do not specify this parameter, the session default NVMEM areas will be used. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Commit NVMEM VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/commit-nvmem-for-devices-vi.html language=enus -->
## TOPIC 00011: Commit NVMEM for Devices VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/commit-nvmem-for-devices-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/commit-nvmem-for-devices-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Commits pending changes to hardware for all NVMEM areas on the specified device(s). If you set the same address multiple times between commits, only the last value will be committed. icon Inputs/Outputs cgenclassrntag.png session in session in specifies the session to access for the given action. cg

### Commit NVMEM for Devices VI

Commits pending changes to hardware for all NVMEM areas on the specified device(s). If you set the same address multiple times between commits, only the last value will be committed.

[IMAGE alt='icon' src='commit-nvmem-for-devices-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. devices — devices specifies the name(s) of the device(s) to access. For multiple devices, use a comma-delimited list. If you do not specify this parameter, the session default devices will be used. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Commit NVMEM VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/commit-nvmem-for-session-vi.html language=enus -->
## TOPIC 00012: Commit NVMEM for Session VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/commit-nvmem-for-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/commit-nvmem-for-session-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Commits pending changes to hardware for all NVMEM areas for all modules in the session. If the session has any chassis reserved, this VI/function skips over them. If you set the same address multiple times between commits, only the last value will be committed. icon Inputs/Outputs cgenclassrntag.png

### Commit NVMEM for Session VI

Commits pending changes to hardware for all NVMEM areas for all modules in the session. If the session has any chassis reserved, this VI/function skips over them. If you set the same address multiple times between commits, only the last value will be committed.

[IMAGE alt='icon' src='commit-nvmem-for-session-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Commit NVMEM VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/commit-nvmem-vi.html language=enus -->
## TOPIC 00013: Commit NVMEM VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/commit-nvmem-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/commit-nvmem-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Commits pending changes to hardware for non-volatile memory. If you set the same address multiple times between commits, only the last value will be committed. icon

### Commit NVMEM VI

Commits pending changes to hardware for non-volatile memory. If you set the same address multiple times between commits, only the last value will be committed.

[IMAGE alt='icon' src='commit-nvmem-vi.png']

- [Commit NVMEM Areas VI](../../vi-lib/slsc/commit-nvmem-areas-vi.html) Commits pending changes to hardware for the specified NVMEM area(s). If you set the same address multiple times between commits, only the last value will be committed.
- [Commit NVMEM for Devices VI](../../vi-lib/slsc/commit-nvmem-for-devices-vi.html) Commits pending changes to hardware for all NVMEM areas on the specified device(s). If you set the same address multiple times between commits, only the last value will be committed.
- [Commit NVMEM for Session VI](../../vi-lib/slsc/commit-nvmem-for-session-vi.html) Commits pending changes to hardware for all NVMEM areas for all modules in the session. If the session has any chassis reserved, this VI/function skips over them. If you set the same address multiple times between commits, only the last value will be committed.

Parent topic:

NVMEM Access

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/commit-properties-for-phys-chans-vi.html language=enus -->
## TOPIC 00014: Commit Properties for Phys Chans VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/commit-properties-for-phys-chans-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/commit-properties-for-phys-chans-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Commits all physical channel properties with pending changes to hardware, for the specified physical channel(s). If you set a property multiple times between commits, only the last value will be committed. icon Inputs/Outputs cgenclassrntag.png session in session in specifies the session to access f

### Commit Properties for Phys Chans VI

Commits all physical channel properties with pending changes to hardware, for the specified physical channel(s). If you set a property multiple times between commits, only the last value will be committed.

[IMAGE alt='icon' src='commit-properties-for-phys-chans-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. physical channels — physical channels specifies the physical channel(s) to access. For multiple physical channels, use a comma-delimited list or colon-delimited range of physical channels. Example: "Mod1/load0:2" If you do not specify this parameter, the session default physical channels will be used. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Commit Properties VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/commit-properties-for-session-vi.html language=enus -->
## TOPIC 00015: Commit Properties for Session VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/commit-properties-for-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/commit-properties-for-session-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Commits all device and physical channel properties with pending changes to hardware, for all devices and physical channels used by the session. If you set a property multiple times between commits, only the last value will be committed. icon Inputs/Outputs cgenclassrntag.png session in session in sp

### Commit Properties for Session VI

Commits all device and physical channel properties with pending changes to hardware, for all devices and physical channels used by the session. If you set a property multiple times between commits, only the last value will be committed.

[IMAGE alt='icon' src='commit-properties-for-session-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Commit Properties VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/commit-properties-generic-vi.html language=enus -->
## TOPIC 00016: Commit Properties (Generic) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/commit-properties-generic-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/commit-properties-generic-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Commits all properties with pending changes to hardware, for the specified resource(s). If you set a property multiple times between commits, only the last value will be committed. icon Inputs/Outputs cgenclassrntag.png session in session in specifies the session to access for the given action. cstr

### Commit Properties (Generic) VI

Commits all properties with pending changes to hardware, for the specified resource(s). If you set a property multiple times between commits, only the last value will be committed.

[IMAGE alt='icon' src='commit-properties-generic-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. resources — resources is a comma-delimited list specifying the names of the resources to access. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Generic Property & Command Access

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/commit-properties-vi.html language=enus -->
## TOPIC 00017: Commit Properties VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/commit-properties-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/commit-properties-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Commits all properties with pending changes to hardware, for the specified resource(s). If you set a property multiple times between commits, only the last value will be committed. icon

### Commit Properties VI

Commits all properties with pending changes to hardware, for the specified resource(s). If you set a property multiple times between commits, only the last value will be committed.

[IMAGE alt='icon' src='commit-properties-vi.png']

- [Commit Properties for Devices VI](../../vi-lib/slsc/commit-properties-for-devices-vi.html) Commits all device or physical channels properties with pending changes to hardware, for the specified device(s) and the physical channels that they contain. If you set a property multiple times between commits, only the last value will be committed.
- [Commit Properties for Phys Chans VI](../../vi-lib/slsc/commit-properties-for-phys-chans-vi.html) Commits all physical channel properties with pending changes to hardware, for the specified physical channel(s). If you set a property multiple times between commits, only the last value will be committed.
- [Commit Properties for Session VI](../../vi-lib/slsc/commit-properties-for-session-vi.html) Commits all device and physical channel properties with pending changes to hardware, for all devices and physical channels used by the session. If you set a property multiple times between commits, only the last value will be committed.

Parent topic:

NI-SLSC

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/connect-to-chassis-by-ip-address-or-hostname-vi.html language=enus -->
## TOPIC 00018: Connect to Chassis by IP Address or Hostname VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/connect-to-chassis-by-ip-address-or-hostname-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/connect-to-chassis-by-ip-address-or-hostname-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a network connection for a chassis by IP address or hostname. This VI shares network connections to the same chassis. If you cannot find the chassis via mDNS, ensure that the chassis is in the local configuration file. If the connect timeout expires before a connection is successfully establis

### Connect to Chassis by IP Address or Hostname VI

Opens a network connection for a chassis by IP address or hostname. This VI shares network connections to the same chassis. If you cannot find the chassis via mDNS, ensure that the chassis is in the local configuration file. If the connect timeout expires before a connection is successfully established, this VI returns an error.

[IMAGE alt='icon' src='connect-to-chassis-by-ip-address-or-hostname-vi.png']

#### Inputs/Outputs

| password — password specifies the password for accessing the chassis. username — username specifies the username for accessing the chassis. session in — session in specifies the session to access for the given action. chassis IP address/hostname — chassis IP address/hostname specifies the IP address or hostname of the chassis to add to the system. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. connect timeout (60 sec) — connect timeout (60 sec) specifies the maximum amount of time, in seconds, to wait when connecting to the specified resource. This VI returns an error if timeout expires. Set connect timeout to -1 to use the value of the Session.TCPIP.ConnectTimeout property. session out — session out is a copy of the session in reference. chassis out — chassis out indicates the name of the chassis added to the system and configuration file. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Session Configuration

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/disconnect-from-devices-vi.html language=enus -->
## TOPIC 00019: Disconnect from Devices VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/disconnect-from-devices-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/disconnect-from-devices-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes network connections for the specified devices. When multiple devices share a network connection because they are in the same SLSC chassis, the network connection will remain open until the last device is disconnected. icon Inputs/Outputs cgenclassrntag.png session in session in specifies the

### Disconnect from Devices VI

Closes network connections for the specified devices. When multiple devices share a network connection because they are in the same SLSC chassis, the network connection will remain open until the last device is disconnected.

[IMAGE alt='icon' src='disconnect-from-devices-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. devices — devices specifies the name(s) of the device(s) to access. For multiple devices, use a comma-delimited list. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Session Configuration

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/execute-command-vi.html language=enus -->
## TOPIC 00020: Execute Command VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/execute-command-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/execute-command-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Executes the specified command on one or multiple devices or physical channels. Property commitment and command execution are in a single round-trip network transaction. If any properties have pending changes for the devices or physical channels, this VI automatically commits the properties before e

### Execute Command VI

Executes the specified command on one or multiple devices or physical channels.

Property commitment and command execution are in a single round-trip network transaction. If any properties have pending changes for the devices or physical channels, this VI automatically commits the properties before executing command.

[IMAGE alt='icon' src='execute-command-vi.png']

- [Execute Device Command VI](../../vi-lib/slsc/execute-device-command-vi.html) Executes the specified command on one or multiple devices.
- [Execute Phys Chan Command VI](../../vi-lib/slsc/execute-phys-chan-command-vi.html) Executes the specified command on one or multiple physical channels.

Parent topic:

NI-SLSC

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/execute-device-command-vi.html language=enus -->
## TOPIC 00021: Execute Device Command VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/execute-device-command-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/execute-device-command-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Executes the specified command on one or multiple devices. icon Inputs/Outputs cgenclassrntag.png session in session in specifies the session to access for the given action. cgenclassrntag.png devices devices specifies the name(s) of the device(s) to access. For multiple devices, use a comma-delimit

### Execute Device Command VI

Executes the specified command on one or multiple devices.

[IMAGE alt='icon' src='execute-device-command-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. devices — devices specifies the name(s) of the device(s) to access. For multiple devices, use a comma-delimited list. If you do not specify this parameter, the session default devices will be used. command — command specifies the name of the command to access. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. timeout (10 sec) — timeout (10 sec) specifies the maximum amount of time, in seconds, to wait for the command to complete. If another command is already running, this VI waits for the running command to complete but still starts counting timeout. This VI returns an error if timeout expires. session out — session out is a copy of the session in reference. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Execute Command VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/execute-generic-command-vi.html language=enus -->
## TOPIC 00022: Execute Generic Command VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/execute-generic-command-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/execute-generic-command-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Executes the specified command on one or multiple devices or physical channels. Property commitment and command execution are in a single round-trip network transaction. If any properties have pending changes for the devices or physical channels, this VI automatically commits the properties before e

### Execute Generic Command VI

Executes the specified command on one or multiple devices or physical channels.

Property commitment and command execution are in a single round-trip network transaction. If any properties have pending changes for the devices or physical channels, this VI automatically commits the properties before executing command.

[IMAGE alt='icon' src='execute-generic-command-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. resources — resources is a comma-delimited list specifying the names of the resources to access. A resource can be a device or a physical channel. command — command specifies the name of the command to access. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. timeout (10 sec) — timeout (10 sec) specifies the maximum amount of time, in seconds, to wait for the operation to complete. This VI returns an error if the time elapses. session out — session out is a copy of the session in reference. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Generic Property & Command Access

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/flatten-names-device-vi.html language=enus -->
## TOPIC 00023: Flatten Names (Device) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/flatten-names-device-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/flatten-names-device-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts an array of device names into a comma-delimited list of device names. Example: ["Mod1","Mod2","Mod3"] -> "Mod1,Mod2,Mod3". icon Inputs/Outputs c1dgenclassrntag.png names in names in is the array of device, area, or channel names to be changed to a list. cerrcodeclst.png error in (no error)

### Flatten Names (Device) VI

Converts an array of device names into a comma-delimited list of device names. Example: ["Mod1","Mod2","Mod3"] -> "Mod1,Mod2,Mod3".

[IMAGE alt='icon' src='flatten-names-device-vi.png']

#### Inputs/Outputs

| names in — names in is the array of device, area, or channel names to be changed to a list. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. names out — names out is the list of device, area, or channel names. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Flatten Names VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/flatten-names-nvmem-area-vi.html language=enus -->
## TOPIC 00024: Flatten Names (NVMEM Area) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/flatten-names-nvmem-area-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/flatten-names-nvmem-area-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts an array of NVMEM areas into a comma-delimited list of NVMEM areas. Example: ["Mod1/capabilities","Mod1/identification"] -> "Mod1/capabilities,Mod1/identification". icon Inputs/Outputs c1dgenclassrntag.png names in names in is the array of device, area, or channel names to be changed to a l

### Flatten Names (NVMEM Area) VI

Converts an array of NVMEM areas into a comma-delimited list of NVMEM areas. Example: ["Mod1/capabilities","Mod1/identification"] -> "Mod1/capabilities,Mod1/identification".

[IMAGE alt='icon' src='flatten-names-nvmem-area-vi.png']

#### Inputs/Outputs

| names in — names in is the array of device, area, or channel names to be changed to a list. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. names out — names out is the list of device, area, or channel names. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Flatten Names VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/flatten-names-string-vi.html language=enus -->
## TOPIC 00025: Flatten Names (String) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/flatten-names-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/flatten-names-string-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts an array of strings into a comma-delimited list of strings. If the array contains physical channel-style names with consecutive numeric suffixes, they will be collapsed into a colon-delimited range. Example: ["Mod1","Mod1/load0","Mod1/capabilities"] -> ["Mod1,Mod1/load0,Mod1/capabilities"].

### Flatten Names (String) VI

Converts an array of strings into a comma-delimited list of strings. If the array contains physical channel-style names with consecutive numeric suffixes, they will be collapsed into a colon-delimited range. Example: ["Mod1","Mod1/load0","Mod1/capabilities"] -> ["Mod1,Mod1/load0,Mod1/capabilities"].

[IMAGE alt='icon' src='flatten-names-string-vi.png']

#### Inputs/Outputs

| names in — names in is the array of device, area, or channel names to be changed to a list. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. names out — names out is the list of device, area, or channel names. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Flatten Names VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/flatten-names-vi.html language=enus -->
## TOPIC 00026: Flatten Names VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/flatten-names-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/flatten-names-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts an array of names into a comma-delimited list of names. icon

### Flatten Names VI

Converts an array of names into a comma-delimited list of names.

[IMAGE alt='icon' src='flatten-names-vi.png']

- [Flatten Names (Device) VI](../../vi-lib/slsc/flatten-names-device-vi.html) Converts an array of device names into a comma-delimited list of device names. Example: ["Mod1","Mod2","Mod3"] -> "Mod1,Mod2,Mod3".
- [Flatten Names (NVMEM Area) VI](../../vi-lib/slsc/flatten-names-nvmem-area-vi.html) Converts an array of NVMEM areas into a comma-delimited list of NVMEM areas. Example: ["Mod1/capabilities","Mod1/identification"] -> "Mod1/capabilities,Mod1/identification".
- [Flatten Names (Phys Chan) VI](../../vi-lib/slsc/flatten-names-phys-chan-vi.html) Converts an array of physical channels into a comma-delimited list of physical channels. If the array contains physical channel-style names with consecutive numeric suffixes, they will be collapsed into a colon-delimited range. Example: ["Mod1/load0","Mod1/load1","Mod1/load2","Mod2/load0"] -> "Mod1/load0:2,Mod2/load0".
- [Flatten Names (String) VI](../../vi-lib/slsc/flatten-names-string-vi.html) Converts an array of strings into a comma-delimited list of strings. If the array contains physical channel-style names with consecutive numeric suffixes, they will be collapsed into a colon-delimited range. Example: ["Mod1","Mod1/load0","Mod1/capabilities"] -> ["Mod1,Mod1/load0,Mod1/capabilities"].

Parent topic:

NI-SLSC

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-chassis-ip-or-hostname-vi.html language=enus -->
## TOPIC 00027: Get Chassis IP or Hostname VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-chassis-ip-or-hostname-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-chassis-ip-or-hostname-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the IP address or hostname of the chassis. icon Inputs/Outputs cgenclassrntag.png session in session in specifies the session to access. cgenclassrntag.png chassis chassis specifies the chassis to get IP address or hostname. cerrcodeclst.png error in (no error) error in (no error) describes err

### Get Chassis IP or Hostname VI

Gets the IP address or hostname of the chassis.

[IMAGE alt='icon' src='get-chassis-ip-or-hostname-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access. chassis — chassis specifies the chassis to get IP address or hostname. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. chassis IP address/hostname — chassis IP address/hostname returns the IP address or hostname of the chassis. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

System Setup

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-device-property-1d-bool-vi.html language=enus -->
## TOPIC 00028: Get Device Property (1D Bool) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-device-property-1d-bool-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-device-property-1d-bool-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of the specified device property from one or more devices. This VI is primarily intended to be used to access device properties that are defined by SLSC devices. It can also be used to access device properties that are defined by the SLSC driver, such as Dev.SerialNum, but in most cas

### Get Device Property (1D Bool) VI

Gets the value of the specified device property from one or more devices.

This VI is primarily intended to be used to access device properties that are defined by SLSC devices. It can also be used to access device properties that are defined by the SLSC driver, such as Dev.SerialNum, but in most cases using the SLSC Session Property Node with the ActiveDevice parameter is preferable because the property node automatically uses the correct data type.

[IMAGE alt='icon' src='get-device-property-1d-bool-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. devices — devices specifies the name(s) of the device(s) to access. For multiple devices, use a comma-delimited list. If you do not specify this parameter, the session default devices will be used. property — property specifies the name of the property to access. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. property value — property value contains the data read from the given property. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Device Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-device-property-1d-dbl-vi.html language=enus -->
## TOPIC 00029: Get Device Property (1D DBL) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-device-property-1d-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-device-property-1d-dbl-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of the specified device property from one or more devices. This VI is primarily intended to be used to access device properties that are defined by SLSC devices. It can also be used to access device properties that are defined by the SLSC driver, such as Dev.SerialNum, but in most cas

### Get Device Property (1D DBL) VI

Gets the value of the specified device property from one or more devices.

This VI is primarily intended to be used to access device properties that are defined by SLSC devices. It can also be used to access device properties that are defined by the SLSC driver, such as Dev.SerialNum, but in most cases using the SLSC Session Property Node with the ActiveDevice parameter is preferable because the property node automatically uses the correct data type.

[IMAGE alt='icon' src='get-device-property-1d-dbl-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. devices — devices specifies the name(s) of the device(s) to access. For multiple devices, use a comma-delimited list. If you do not specify this parameter, the session default devices will be used. property — property specifies the name of the property to access. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. property value — property value contains the data read from the given property. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Device Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-device-property-1d-i32-vi.html language=enus -->
## TOPIC 00030: Get Device Property (1D I32) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-device-property-1d-i32-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-device-property-1d-i32-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of the specified device property from one or more devices. This VI is primarily intended to be used to access device properties that are defined by SLSC devices. It can also be used to access device properties that are defined by the SLSC driver, such as Dev.SerialNum, but in most cas

### Get Device Property (1D I32) VI

Gets the value of the specified device property from one or more devices.

This VI is primarily intended to be used to access device properties that are defined by SLSC devices. It can also be used to access device properties that are defined by the SLSC driver, such as Dev.SerialNum, but in most cases using the SLSC Session Property Node with the ActiveDevice parameter is preferable because the property node automatically uses the correct data type.

[IMAGE alt='icon' src='get-device-property-1d-i32-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. devices — devices specifies the name(s) of the device(s) to access. For multiple devices, use a comma-delimited list. If you do not specify this parameter, the session default devices will be used. property — property specifies the name of the property to access. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. property value — property value contains the data read from the given property. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Device Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-device-property-1d-string-vi.html language=enus -->
## TOPIC 00031: Get Device Property (1D String) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-device-property-1d-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-device-property-1d-string-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of the specified device property from one or more devices. This VI is primarily intended to be used to access device properties that are defined by SLSC devices. It can also be used to access device properties that are defined by the SLSC driver, such as Dev.SerialNum, but in most cas

### Get Device Property (1D String) VI

Gets the value of the specified device property from one or more devices.

This VI is primarily intended to be used to access device properties that are defined by SLSC devices. It can also be used to access device properties that are defined by the SLSC driver, such as Dev.SerialNum, but in most cases using the SLSC Session Property Node with the ActiveDevice parameter is preferable because the property node automatically uses the correct data type.

[IMAGE alt='icon' src='get-device-property-1d-string-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. devices — devices specifies the name(s) of the device(s) to access. For multiple devices, use a comma-delimited list. If you do not specify this parameter, the session default devices will be used. property — property specifies the name of the property to access. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. property value — property value contains the data read from the given property. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Device Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-device-property-i32-vi.html language=enus -->
## TOPIC 00032: Get Device Property (I32) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-device-property-i32-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-device-property-i32-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of the specified device property from one or more devices. This VI is primarily intended to be used to access device properties that are defined by SLSC devices. It can also be used to access device properties that are defined by the SLSC driver, such as Dev.SerialNum, but in most cas

### Get Device Property (I32) VI

Gets the value of the specified device property from one or more devices.

This VI is primarily intended to be used to access device properties that are defined by SLSC devices. It can also be used to access device properties that are defined by the SLSC driver, such as Dev.SerialNum, but in most cases using the SLSC Session Property Node with the ActiveDevice parameter is preferable because the property node automatically uses the correct data type.

[IMAGE alt='icon' src='get-device-property-i32-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. devices — devices specifies the name(s) of the device(s) to access. For multiple devices, use a comma-delimited list. If you do not specify this parameter, the session default devices will be used. property — property specifies the name of the property to access. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. property value — property value contains the data read from the given property. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Device Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-device-property-i64-vi.html language=enus -->
## TOPIC 00033: Get Device Property (I64) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-device-property-i64-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-device-property-i64-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of the specified device property from one or more devices. This VI is primarily intended to be used to access device properties that are defined by SLSC devices. It can also be used to access device properties that are defined by the SLSC driver, such as Dev.SerialNum, but in most cas

### Get Device Property (I64) VI

Gets the value of the specified device property from one or more devices.

This VI is primarily intended to be used to access device properties that are defined by SLSC devices. It can also be used to access device properties that are defined by the SLSC driver, such as Dev.SerialNum, but in most cases using the SLSC Session Property Node with the ActiveDevice parameter is preferable because the property node automatically uses the correct data type.

[IMAGE alt='icon' src='get-device-property-i64-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. devices — devices specifies the name(s) of the device(s) to access. For multiple devices, use a comma-delimited list. If you do not specify this parameter, the session default devices will be used. property — property specifies the name of the property to access. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. property value — property value contains the data read from the given property. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Device Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-device-property-vi.html language=enus -->
## TOPIC 00034: Get Device Property VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-device-property-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-device-property-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of the specified device property from one or more devices. You can use an array instance of this VI to get a scalar property from multiple devices with a single call to the VI. This VI is primarily intended to be used to access device properties that are defined by SLSC devices. It ca

### Get Device Property VI

Gets the value of the specified device property from one or more devices. You can use an array instance of this VI to get a scalar property from multiple devices with a single call to the VI.

This VI is primarily intended to be used to access device properties that are defined by SLSC devices. It can also be used to access device properties that are defined by the SLSC driver, such as Dev.SerialNum, but in most cases using the SLSC Session Property Node with the ActiveDevice parameter is preferable because the property node automatically uses the correct data type.

[IMAGE alt='icon' src='get-device-property-vi.png']

- [Get Device Property (Bool) VI](../../vi-lib/slsc/get-device-property-bool-vi.html) Gets the value of the specified device property from one or more devices.
- [Get Device Property (DBL) VI](../../vi-lib/slsc/get-device-property-dbl-vi.html) Gets the value of the specified device property from one or more devices.
- [Get Device Property (I32) VI](../../vi-lib/slsc/get-device-property-i32-vi.html) Gets the value of the specified device property from one or more devices.
- [Get Device Property (I64) VI](../../vi-lib/slsc/get-device-property-i64-vi.html) Gets the value of the specified device property from one or more devices.
- [Get Device Property (String) VI](../../vi-lib/slsc/get-device-property-string-vi.html) Gets the value of the specified device property from one or more devices.
- [Get Device Property (U32) VI](../../vi-lib/slsc/get-device-property-u32-vi.html) Gets the value of the specified device property from one or more devices.
- [Get Device Property (U64) VI](../../vi-lib/slsc/get-device-property-u64-vi.html) Gets the value of the specified device property from one or more devices.
- [Get Device Property (1D Bool) VI](../../vi-lib/slsc/get-device-property-1d-bool-vi.html) Gets the value of the specified device property from one or more devices.
- [Get Device Property (1D DBL) VI](../../vi-lib/slsc/get-device-property-1d-dbl-vi.html) Gets the value of the specified device property from one or more devices.
- [Get Device Property (1D I32) VI](../../vi-lib/slsc/get-device-property-1d-i32-vi.html) Gets the value of the specified device property from one or more devices.
- [Get Device Property (1D I64) VI](../../vi-lib/slsc/get-device-property-1d-i64-vi.html) Gets the value of the specified device property from one or more devices.
- [Get Device Property (1D String) VI](../../vi-lib/slsc/get-device-property-1d-string-vi.html) Gets the value of the specified device property from one or more devices.
- [Get Device Property (1D U32) VI](../../vi-lib/slsc/get-device-property-1d-u32-vi.html) Gets the value of the specified device property from one or more devices.
- [Get Device Property (1D U64) VI](../../vi-lib/slsc/get-device-property-1d-u64-vi.html) Gets the value of the specified device property from one or more devices.

Parent topic:

NI-SLSC

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-generic-property-1d-bool-vi.html language=enus -->
## TOPIC 00035: Get Generic Property (1D Bool) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-generic-property-1d-bool-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-generic-property-1d-bool-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource. icon Inputs/Outputs cgenclassrntag.png session in session in specifies the session to access for

### Get Generic Property (1D Bool) VI

Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource.

[IMAGE alt='icon' src='get-generic-property-1d-bool-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. resources — resources is a comma-delimited list specifying the names of the resources to access. property — property specifies the name of the property to access. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. property value — property value contains the data read from the given property. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Generic Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-generic-property-1d-i32-vi.html language=enus -->
## TOPIC 00036: Get Generic Property (1D I32) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-generic-property-1d-i32-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-generic-property-1d-i32-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource. icon Inputs/Outputs cgenclassrntag.png session in session in specifies the session to access for

### Get Generic Property (1D I32) VI

Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource.

[IMAGE alt='icon' src='get-generic-property-1d-i32-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. resources — resources is a comma-delimited list specifying the names of the resources to access. property — property specifies the name of the property to access. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. property value — property value contains the data read from the given property. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Generic Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-generic-property-1d-i64-vi.html language=enus -->
## TOPIC 00037: Get Generic Property (1D I64) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-generic-property-1d-i64-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-generic-property-1d-i64-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource. icon Inputs/Outputs cgenclassrntag.png session in session in specifies the session to access for

### Get Generic Property (1D I64) VI

Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource.

[IMAGE alt='icon' src='get-generic-property-1d-i64-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. resources — resources is a comma-delimited list specifying the names of the resources to access. property — property specifies the name of the property to access. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. property value — property value contains the data read from the given property. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Generic Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-generic-property-1d-string-vi.html language=enus -->
## TOPIC 00038: Get Generic Property (1D String) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-generic-property-1d-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-generic-property-1d-string-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource. icon Inputs/Outputs cgenclassrntag.png session in session in specifies the session to access for

### Get Generic Property (1D String) VI

Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource.

[IMAGE alt='icon' src='get-generic-property-1d-string-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. resources — resources is a comma-delimited list specifying the names of the resources to access. property — property specifies the name of the property to access. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. property value — property value contains the data read from the given property. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Generic Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-generic-property-1d-u32-vi.html language=enus -->
## TOPIC 00039: Get Generic Property (1D U32) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-generic-property-1d-u32-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-generic-property-1d-u32-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource. icon Inputs/Outputs cgenclassrntag.png session in session in specifies the session to access for

### Get Generic Property (1D U32) VI

Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource.

[IMAGE alt='icon' src='get-generic-property-1d-u32-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. resources — resources is a comma-delimited list specifying the names of the resources to access. property — property specifies the name of the property to access. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. property value — property value contains the data read from the given property. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Generic Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-generic-property-1d-u64-vi.html language=enus -->
## TOPIC 00040: Get Generic Property (1D U64) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-generic-property-1d-u64-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-generic-property-1d-u64-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource. icon Inputs/Outputs cgenclassrntag.png session in session in specifies the session to access for

### Get Generic Property (1D U64) VI

Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource.

[IMAGE alt='icon' src='get-generic-property-1d-u64-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. resources — resources is a comma-delimited list specifying the names of the resources to access. property — property specifies the name of the property to access. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. property value — property value contains the data read from the given property. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Generic Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-generic-property-bool-vi.html language=enus -->
## TOPIC 00041: Get Generic Property (Bool) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-generic-property-bool-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-generic-property-bool-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource. icon Inputs/Outputs cgenclassrntag.png session in session in specifies the session to access for

### Get Generic Property (Bool) VI

Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource.

[IMAGE alt='icon' src='get-generic-property-bool-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. resources — resources is a comma-delimited list specifying the names of the resources to access. property — property specifies the name of the property to access. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. property value — property value contains the data read from the given property. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Generic Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-generic-property-dbl-vi.html language=enus -->
## TOPIC 00042: Get Generic Property (DBL) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-generic-property-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-generic-property-dbl-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource. icon Inputs/Outputs cgenclassrntag.png session in session in specifies the session to access for

### Get Generic Property (DBL) VI

Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource.

[IMAGE alt='icon' src='get-generic-property-dbl-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. resources — resources is a comma-delimited list specifying the names of the resources to access. property — property specifies the name of the property to access. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. property value — property value contains the data read from the given property. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Generic Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-generic-property-string-vi.html language=enus -->
## TOPIC 00043: Get Generic Property (String) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-generic-property-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-generic-property-string-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource. icon Inputs/Outputs cgenclassrntag.png session in session in specifies the session to access for

### Get Generic Property (String) VI

Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource.

[IMAGE alt='icon' src='get-generic-property-string-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. resources — resources is a comma-delimited list specifying the names of the resources to access. property — property specifies the name of the property to access. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. property value — property value contains the data read from the given property. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Generic Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-generic-property-u32-vi.html language=enus -->
## TOPIC 00044: Get Generic Property (U32) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-generic-property-u32-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-generic-property-u32-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource. icon Inputs/Outputs cgenclassrntag.png session in session in specifies the session to access for

### Get Generic Property (U32) VI

Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource.

[IMAGE alt='icon' src='get-generic-property-u32-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. resources — resources is a comma-delimited list specifying the names of the resources to access. property — property specifies the name of the property to access. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. property value — property value contains the data read from the given property. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Generic Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-generic-property-u64-vi.html language=enus -->
## TOPIC 00045: Get Generic Property (U64) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-generic-property-u64-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-generic-property-u64-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource. icon Inputs/Outputs cgenclassrntag.png session in session in specifies the session to access for

### Get Generic Property (U64) VI

Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource.

[IMAGE alt='icon' src='get-generic-property-u64-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. resources — resources is a comma-delimited list specifying the names of the resources to access. property — property specifies the name of the property to access. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. property value — property value contains the data read from the given property. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Generic Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-generic-property-vi.html language=enus -->
## TOPIC 00046: Get Generic Property VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-generic-property-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-generic-property-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource. You can use an array instance of this VI to get a scalar property from multiple devices with a si

### Get Generic Property VI

Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource. You can use an array instance of this VI to get a scalar property from multiple devices with a single call to the VI.

In addition to resource aliases like $DefaultDevices, this VI supports:

- $Session: can be used to get/set session properties such as Session.DefaultDevices.
- $System: can be used to get system properties such as Sys.Devices.

[IMAGE alt='icon' src='get-generic-property-vi.png']

- [Get Generic Property (Bool) VI](../../vi-lib/slsc/get-generic-property-bool-vi.html) Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource.
- [Get Generic Property (DBL) VI](../../vi-lib/slsc/get-generic-property-dbl-vi.html) Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource.
- [Get Generic Property (I32) VI](../../vi-lib/slsc/get-generic-property-i32-vi.html) Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource.
- [Get Generic Property (I64) VI](../../vi-lib/slsc/get-generic-property-i64-vi.html) Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource.
- [Get Generic Property (String) VI](../../vi-lib/slsc/get-generic-property-string-vi.html) Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource.
- [Get Generic Property (U32) VI](../../vi-lib/slsc/get-generic-property-u32-vi.html) Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource.
- [Get Generic Property (U64) VI](../../vi-lib/slsc/get-generic-property-u64-vi.html) Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource.
- [Get Generic Property (1D Bool) VI](../../vi-lib/slsc/get-generic-property-1d-bool-vi.html) Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource.
- [Get Generic Property (1D DBL) VI](../../vi-lib/slsc/get-generic-property-1d-dbl-vi.html) Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource.
- [Get Generic Property (1D I32) VI](../../vi-lib/slsc/get-generic-property-1d-i32-vi.html) Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource.
- [Get Generic Property (1D I64) VI](../../vi-lib/slsc/get-generic-property-1d-i64-vi.html) Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource.
- [Get Generic Property (1D String) VI](../../vi-lib/slsc/get-generic-property-1d-string-vi.html) Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource.
- [Get Generic Property (1D U32) VI](../../vi-lib/slsc/get-generic-property-1d-u32-vi.html) Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource.
- [Get Generic Property (1D U64) VI](../../vi-lib/slsc/get-generic-property-1d-u64-vi.html) Gets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource.

Parent topic:

Generic Property & Command Access

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-module-name-vi.html language=enus -->
## TOPIC 00047: Get Module Name VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-module-name-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-module-name-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of a module on the chassis. icon Inputs/Outputs cgenclassrntag.png session in session in specifies the session to access. cgenclassrntag.png chassis chassis specifies the chassis to get the module name. cu32.png slot number slot number specifies the slot number of the module. cerrcodec

### Get Module Name VI

Gets the name of a module on the chassis.

[IMAGE alt='icon' src='get-module-name-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access. chassis — chassis specifies the chassis to get the module name. slot number — slot number specifies the slot number of the module. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. module — module returns the name of the module. module present? — module present? returns whether modules exist on the chassis. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

System Setup

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-nvmem-bytes-vi.html language=enus -->
## TOPIC 00048: Get NVMEM Bytes VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-nvmem-bytes-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-nvmem-bytes-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the specified number of bytes (data size) starting at the given data address in the specified NVMEM area. icon Inputs/Outputs cgenclassrntag.png session in session in specifies the session to access for the given action. cgenclassrntag.png NVMEM area NVMEM area specifies the the non-volatile m

### Get NVMEM Bytes VI

Reads the specified number of bytes (**data size**) starting at the given **data address** in the specified **NVMEM area**.

[IMAGE alt='icon' src='get-nvmem-bytes-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. NVMEM area — NVMEM area specifies the the non-volatile memory area to access. This must include both the device name and NVMEM area name, such as "Mod1/capabilities." If you do not specify this parameter, the session default NVMEM areas will be used. data address — data address specifies the starting address to begin accessing data. data size — data size The number of bytes to read from the data address within the given NVMEM area. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. NVMEM area out — NVMEM area out is a copy of the nvmem area resource. next data address — next data address is data address + data size. This may be convenient when accessing contiguous fields. data out — data out contains the data read from data address. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NVMEM Access

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-phys-chan-property-1d-dbl-vi.html language=enus -->
## TOPIC 00049: Get Phys Chan Property (1D DBL) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-phys-chan-property-1d-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-phys-chan-property-1d-dbl-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of the specified physical channel property from one or more physical channels. This VI is primarily intended to be used to access physical channel properties that are defined by SLSC devices. It can also be used to access physical channel properties that are defined by the SLSC driver

### Get Phys Chan Property (1D DBL) VI

Gets the value of the specified physical channel property from one or more physical channels.

This VI is primarily intended to be used to access physical channel properties that are defined by SLSC devices. It can also be used to access physical channel properties that are defined by the SLSC driver, such as PhysChan.Commands, but in most cases using the SLSC Session Property Node with the ActivePhysChan parameter is preferable because the property node automatically uses the correct data type.

[IMAGE alt='icon' src='get-phys-chan-property-1d-dbl-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. physical channels — physical channels specifies the physical channel(s) to access. For multiple physical channels, use a comma-delimited list or colon-delimited range of physical channels. Example: "Mod1/load0:2" If you do not specify this parameter, the session default physical channels will be used. property — property specifies the name of the property to access. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. property value — property value contains the data read from the given property. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Phys Chan Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-phys-chan-property-1d-string-vi.html language=enus -->
## TOPIC 00050: Get Phys Chan Property (1D String) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-phys-chan-property-1d-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-phys-chan-property-1d-string-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of the specified physical channel property from one or more physical channels. This VI is primarily intended to be used to access physical channel properties that are defined by SLSC devices. It can also be used to access physical channel properties that are defined by the SLSC driver

### Get Phys Chan Property (1D String) VI

Gets the value of the specified physical channel property from one or more physical channels.

This VI is primarily intended to be used to access physical channel properties that are defined by SLSC devices. It can also be used to access physical channel properties that are defined by the SLSC driver, such as PhysChan.Commands, but in most cases using the SLSC Session Property Node with the ActivePhysChan parameter is preferable because the property node automatically uses the correct data type.

[IMAGE alt='icon' src='get-phys-chan-property-1d-string-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. physical channels — physical channels specifies the physical channel(s) to access. For multiple physical channels, use a comma-delimited list or colon-delimited range of physical channels. Example: "Mod1/load0:2" If you do not specify this parameter, the session default physical channels will be used. property — property specifies the name of the property to access. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. property value — property value contains the data read from the given property. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Phys Chan Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-phys-chan-property-1d-u32-vi.html language=enus -->
## TOPIC 00051: Get Phys Chan Property (1D U32) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-phys-chan-property-1d-u32-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-phys-chan-property-1d-u32-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of the specified physical channel property from one or more physical channels. This VI is primarily intended to be used to access physical channel properties that are defined by SLSC devices. It can also be used to access physical channel properties that are defined by the SLSC driver

### Get Phys Chan Property (1D U32) VI

Gets the value of the specified physical channel property from one or more physical channels.

This VI is primarily intended to be used to access physical channel properties that are defined by SLSC devices. It can also be used to access physical channel properties that are defined by the SLSC driver, such as PhysChan.Commands, but in most cases using the SLSC Session Property Node with the ActivePhysChan parameter is preferable because the property node automatically uses the correct data type.

[IMAGE alt='icon' src='get-phys-chan-property-1d-u32-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. physical channels — physical channels specifies the physical channel(s) to access. For multiple physical channels, use a comma-delimited list or colon-delimited range of physical channels. Example: "Mod1/load0:2" If you do not specify this parameter, the session default physical channels will be used. property — property specifies the name of the property to access. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. property value — property value contains the data read from the given property. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Phys Chan Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-phys-chan-property-1d-u64-vi.html language=enus -->
## TOPIC 00052: Get Phys Chan Property (1D U64) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-phys-chan-property-1d-u64-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-phys-chan-property-1d-u64-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of the specified physical channel property from one or more physical channels. This VI is primarily intended to be used to access physical channel properties that are defined by SLSC devices. It can also be used to access physical channel properties that are defined by the SLSC driver

### Get Phys Chan Property (1D U64) VI

Gets the value of the specified physical channel property from one or more physical channels.

This VI is primarily intended to be used to access physical channel properties that are defined by SLSC devices. It can also be used to access physical channel properties that are defined by the SLSC driver, such as PhysChan.Commands, but in most cases using the SLSC Session Property Node with the ActivePhysChan parameter is preferable because the property node automatically uses the correct data type.

[IMAGE alt='icon' src='get-phys-chan-property-1d-u64-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. physical channels — physical channels specifies the physical channel(s) to access. For multiple physical channels, use a comma-delimited list or colon-delimited range of physical channels. Example: "Mod1/load0:2" If you do not specify this parameter, the session default physical channels will be used. property — property specifies the name of the property to access. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. property value — property value contains the data read from the given property. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Phys Chan Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-phys-chan-property-string-vi.html language=enus -->
## TOPIC 00053: Get Phys Chan Property (String) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-phys-chan-property-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-phys-chan-property-string-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of the specified physical channel property from one or more physical channels. This VI is primarily intended to be used to access physical channel properties that are defined by SLSC devices. It can also be used to access physical channel properties that are defined by the SLSC driver

### Get Phys Chan Property (String) VI

Gets the value of the specified physical channel property from one or more physical channels.

This VI is primarily intended to be used to access physical channel properties that are defined by SLSC devices. It can also be used to access physical channel properties that are defined by the SLSC driver, such as PhysChan.Commands, but in most cases using the SLSC Session Property Node with the ActivePhysChan parameter is preferable because the property node automatically uses the correct data type.

[IMAGE alt='icon' src='get-phys-chan-property-string-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. physical channels — physical channels specifies the physical channel(s) to access. For multiple physical channels, use a comma-delimited list or colon-delimited range of physical channels. Example: "Mod1/load0:2" If you do not specify this parameter, the session default physical channels will be used. property — property specifies the name of the property to access. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. property value — property value contains the data read from the given property. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Phys Chan Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-phys-chan-property-u32-vi.html language=enus -->
## TOPIC 00054: Get Phys Chan Property (U32) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-phys-chan-property-u32-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-phys-chan-property-u32-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of the specified physical channel property from one or more physical channels. This VI is primarily intended to be used to access physical channel properties that are defined by SLSC devices. It can also be used to access physical channel properties that are defined by the SLSC driver

### Get Phys Chan Property (U32) VI

Gets the value of the specified physical channel property from one or more physical channels.

This VI is primarily intended to be used to access physical channel properties that are defined by SLSC devices. It can also be used to access physical channel properties that are defined by the SLSC driver, such as PhysChan.Commands, but in most cases using the SLSC Session Property Node with the ActivePhysChan parameter is preferable because the property node automatically uses the correct data type.

[IMAGE alt='icon' src='get-phys-chan-property-u32-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. physical channels — physical channels specifies the physical channel(s) to access. For multiple physical channels, use a comma-delimited list or colon-delimited range of physical channels. Example: "Mod1/load0:2" If you do not specify this parameter, the session default physical channels will be used. property — property specifies the name of the property to access. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. property value — property value contains the data read from the given property. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Phys Chan Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-phys-chan-property-u64-vi.html language=enus -->
## TOPIC 00055: Get Phys Chan Property (U64) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-phys-chan-property-u64-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-phys-chan-property-u64-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of the specified physical channel property from one or more physical channels. This VI is primarily intended to be used to access physical channel properties that are defined by SLSC devices. It can also be used to access physical channel properties that are defined by the SLSC driver

### Get Phys Chan Property (U64) VI

Gets the value of the specified physical channel property from one or more physical channels.

This VI is primarily intended to be used to access physical channel properties that are defined by SLSC devices. It can also be used to access physical channel properties that are defined by the SLSC driver, such as PhysChan.Commands, but in most cases using the SLSC Session Property Node with the ActivePhysChan parameter is preferable because the property node automatically uses the correct data type.

[IMAGE alt='icon' src='get-phys-chan-property-u64-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. physical channels — physical channels specifies the physical channel(s) to access. For multiple physical channels, use a comma-delimited list or colon-delimited range of physical channels. Example: "Mod1/load0:2" If you do not specify this parameter, the session default physical channels will be used. property — property specifies the name of the property to access. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. property value — property value contains the data read from the given property. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Phys Chan Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-phys-chan-property-vi.html language=enus -->
## TOPIC 00056: Get Phys Chan Property VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-phys-chan-property-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-phys-chan-property-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value of the specified physical channel property from one or more physical channels. You can use an array instance of this VI to get a scalar property from multiple devices with a single call to the VI. This VI is primarily intended to be used to access physical channel properties that are

### Get Phys Chan Property VI

Gets the value of the specified physical channel property from one or more physical channels. You can use an array instance of this VI to get a scalar property from multiple devices with a single call to the VI.

This VI is primarily intended to be used to access physical channel properties that are defined by SLSC devices. It can also be used to access physical channel properties that are defined by the SLSC driver, such as PhysChan.Commands, but in most cases using the SLSC Session Property Node with the ActivePhysChan parameter is preferable because the property node automatically uses the correct data type.

[IMAGE alt='icon' src='get-phys-chan-property-vi.png']

- [Get Phys Chan Property (Bool) VI](../../vi-lib/slsc/get-phys-chan-property-bool-vi.html) Gets the value of the specified physical channel property from one or more physical channels.
- [Get Phys Chan Property (DBL) VI](../../vi-lib/slsc/get-phys-chan-property-dbl-vi.html) Gets the value of the specified physical channel property from one or more physical channels.
- [Get Phys Chan Property (I32) VI](../../vi-lib/slsc/get-phys-chan-property-i32-vi.html) Gets the value of the specified physical channel property from one or more physical channels.
- [Get Phys Chan Property (I64) VI](../../vi-lib/slsc/get-phys-chan-property-i64-vi.html) Gets the value of the specified physical channel property from one or more physical channels.
- [Get Phys Chan Property (String) VI](../../vi-lib/slsc/get-phys-chan-property-string-vi.html) Gets the value of the specified physical channel property from one or more physical channels.
- [Get Phys Chan Property (U32) VI](../../vi-lib/slsc/get-phys-chan-property-u32-vi.html) Gets the value of the specified physical channel property from one or more physical channels.
- [Get Phys Chan Property (U64) VI](../../vi-lib/slsc/get-phys-chan-property-u64-vi.html) Gets the value of the specified physical channel property from one or more physical channels.
- [Get Phys Chan Property (1D Bool) VI](../../vi-lib/slsc/get-phys-chan-property-1d-bool-vi.html) Gets the value of the specified physical channel property from one or more physical channels.
- [Get Phys Chan Property (1D DBL) VI](../../vi-lib/slsc/get-phys-chan-property-1d-dbl-vi.html) Gets the value of the specified physical channel property from one or more physical channels.
- [Get Phys Chan Property (1D I32) VI](../../vi-lib/slsc/get-phys-chan-property-1d-i32-vi.html) Gets the value of the specified physical channel property from one or more physical channels.
- [Get Phys Chan Property (1D I64) VI](../../vi-lib/slsc/get-phys-chan-property-1d-i64-vi.html) Gets the value of the specified physical channel property from one or more physical channels.
- [Get Phys Chan Property (1D String) VI](../../vi-lib/slsc/get-phys-chan-property-1d-string-vi.html) Gets the value of the specified physical channel property from one or more physical channels.
- [Get Phys Chan Property (1D U32) VI](../../vi-lib/slsc/get-phys-chan-property-1d-u32-vi.html) Gets the value of the specified physical channel property from one or more physical channels.
- [Get Phys Chan Property (1D U64) VI](../../vi-lib/slsc/get-phys-chan-property-1d-u64-vi.html) Gets the value of the specified physical channel property from one or more physical channels.

Parent topic:

NI-SLSC

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-scaling-equation-vi.html language=enus -->
## TOPIC 00057: Get Scaling Equation VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-scaling-equation-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-scaling-equation-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a scaling equation from a user-defined scale. icon Inputs/Outputs cgenclassrntag.png session in session in specifies the session to access. cgenclassrntag.png physical channel physical channel specifies the physical channel that contains the scaling equation. cerrcodeclst.png error in (no error

### Get Scaling Equation VI

Gets a scaling equation from a user-defined scale.

[IMAGE alt='icon' src='get-scaling-equation-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access. physical channel — physical channel specifies the physical channel that contains the scaling equation. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. physical channel out — physical channel out returns the physical channel that contains the scaling equation. equation — equation returns the scaling equation this VI reads from the physical channel. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Scaling

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-scaling-parameters-linear-vi.html language=enus -->
## TOPIC 00058: Get Scaling Parameters (Linear) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-scaling-parameters-linear-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-scaling-parameters-linear-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets scaling parameters from a linear scale that uses the equation y = mx + b, where x is a pre-scaled value and y is a scaled value. icon Inputs/Outputs cgenclassrntag.png session in session in specifies the session to access. cgenclassrntag.png physical channel physical channel specifies the physi

### Get Scaling Parameters (Linear) VI

Gets scaling parameters from a linear scale that uses the equation *y = mx + b*, where *x* is a pre-scaled value and *y* is a scaled value.

[IMAGE alt='icon' src='get-scaling-parameters-linear-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access. physical channel — physical channel specifies the physical channel that contains the scaling equation. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. physical channel out — physical channel out returns the physical channel that contains the scaling equation. slope — slope returns the slope, or m, of the linear equation. intercept — intercept returns the intercept, or b, of the linear equation. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Scaling Parameters VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-scaling-parameters-polynomial-vi.html language=enus -->
## TOPIC 00059: Get Scaling Parameters (Polynomial) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-scaling-parameters-polynomial-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-scaling-parameters-polynomial-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets scaling parameters from a polynomial scale that uses an nth order polynomial equation. A polynomial scale contains both a polynomial to convert pre-scaled values to scaled values and a polynomial to convert scaled values to pre-scaled values. icon Inputs/Outputs cgenclassrntag.png session in se

### Get Scaling Parameters (Polynomial) VI

Gets scaling parameters from a polynomial scale that uses an *n*th order polynomial equation. A polynomial scale contains both a polynomial to convert pre-scaled values to scaled values and a polynomial to convert scaled values to pre-scaled values.

[IMAGE alt='icon' src='get-scaling-parameters-polynomial-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access. physical channel — physical channel specifies the physical channel that contains the scaling equation. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. physical channel out — physical channel out returns the physical channel that contains the scaling equation. forward coefficients — forward coefficients returns an array of coefficients for the polynomial that converts pre-scaled values to scaled values. Each element of the array corresponds to a term of the equation. For example, if forward coefficients is [1, 3, 6, 9], the equation is y = 9x3 + 6x2 + 3x + 1. reverse coefficients — reverse coefficients returns an array of coefficients for the polynomial that converts scaled values to pre-scaled values. Each element of the array corresponds to a term of the equation. For example, if reverse coefficients is [1, 3, 6, 9], the equation is y = 9x3 + 6x2 + 3x + 1. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Scaling Parameters VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-scaling-parameters-table-vi.html language=enus -->
## TOPIC 00060: Get Scaling Parameters (Table) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-scaling-parameters-table-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-scaling-parameters-table-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets scaling parameters from a table scale that maps an array of pre-scaled values to an array of corresponding scaled values. icon Inputs/Outputs cgenclassrntag.png session in session in specifies the session to access. cgenclassrntag.png physical channel physical channel specifies the physical cha

### Get Scaling Parameters (Table) VI

Gets scaling parameters from a table scale that maps an array of pre-scaled values to an array of corresponding scaled values.

[IMAGE alt='icon' src='get-scaling-parameters-table-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access. physical channel — physical channel specifies the physical channel that contains the scaling equation. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. physical channel out — physical channel out returns the physical channel that contains the scaling equation. scaled values — scaled values returns an array of scaled values. pre-scaled values — pre-scaled values returns an array of values to scale. error out — error out contains error information. This output provides standard error out functionality. coercion — coercion returns the method of coercing values that fall between the values in the table. Interpolate (0) The scale uses linear interpolation to coerce pre-scaled values to scaled values. RoundToNearest (1) The scale rounds a pre-scaled value to the nearest scaled value in the table. Strict (2) The scale reports an error if any value in pre-scaled values is not in scaled values. |  |
| --- | --- |
| Interpolate (0) | The scale uses linear interpolation to coerce pre-scaled values to scaled values. |
| RoundToNearest (1) | The scale rounds a pre-scaled value to the nearest scaled value in the table. |
| Strict (2) | The scale reports an error if any value in pre-scaled values is not in scaled values. |

Parent topic:

Get Scaling Parameters VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-scaling-parameters-user-defined-vi.html language=enus -->
## TOPIC 00061: Get Scaling Parameters (User Defined) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-scaling-parameters-user-defined-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-scaling-parameters-user-defined-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets scaling parameters from a user-defined scale. icon Inputs/Outputs cgenclassrntag.png session in session in specifies the session to access. cgenclassrntag.png physical channel physical channel specifies the physical channel that contains the scaling equation. cerrcodeclst.png error in (no error

### Get Scaling Parameters (User Defined) VI

Gets scaling parameters from a user-defined scale.

[IMAGE alt='icon' src='get-scaling-parameters-user-defined-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access. physical channel — physical channel specifies the physical channel that contains the scaling equation. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. physical channel out — physical channel out returns the physical channel that contains the scaling equation. parameter names — parameter names returns the names of the scaling parameters. parameter values — parameter values returns the values of the scaling parameters. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Get Scaling Parameters VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/get-scaling-parameters-vi.html language=enus -->
## TOPIC 00062: Get Scaling Parameters VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/get-scaling-parameters-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/get-scaling-parameters-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets scaling parameters from a scale. icon

### Get Scaling Parameters VI

Gets scaling parameters from a scale.

[IMAGE alt='icon' src='get-scaling-parameters-vi.png']

- [Get Scaling Parameters (Linear) VI](../../vi-lib/slsc/get-scaling-parameters-linear-vi.html) Gets scaling parameters from a linear scale that uses the equation y = mx + b , where x is a pre-scaled value and y is a scaled value.
- [Get Scaling Parameters (Polynomial) VI](../../vi-lib/slsc/get-scaling-parameters-polynomial-vi.html) Gets scaling parameters from a polynomial scale that uses an n th order polynomial equation. A polynomial scale contains both a polynomial to convert pre-scaled values to scaled values and a polynomial to convert scaled values to pre-scaled values.
- [Get Scaling Parameters (Table) VI](../../vi-lib/slsc/get-scaling-parameters-table-vi.html) Gets scaling parameters from a table scale that maps an array of pre-scaled values to an array of corresponding scaled values.
- [Get Scaling Parameters (User Defined) VI](../../vi-lib/slsc/get-scaling-parameters-user-defined-vi.html) Gets scaling parameters from a user-defined scale.

Parent topic:

Scaling

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/initialize-session-vi.html language=enus -->
## TOPIC 00063: Initialize Session VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/initialize-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/initialize-session-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes an SLSC session. icon

### Initialize Session VI

Initializes an SLSC session.

[IMAGE alt='icon' src='initialize-session-vi.png']

- [Initialize Session with Devices VI](../../vi-lib/slsc/initialize-session-with-devices-vi.html) Initializes an SLSC session with one or multiple devices. The session opens network connections for devices. If reservation access is set to Read Only or Read/Write , the session also reserves the devices.
- [Initialize Session with NVMEM Areas VI](../../vi-lib/slsc/initialize-session-with-nvmem-areas-vi.html) Initializes an SLSC session with one or multiple NVMEM areas. The session opens network connections for NVMEM areas. If reservation access is set to Read Only or Read/Write , the session also reserves the devices.
- [Initialize Session with Phys Chans VI](../../vi-lib/slsc/initialize-session-with-phys-chans-vi.html) Initializes an SLSC session with one or multiple physical channels. The session opens network connections for devices that correspond to the physical channels. If reservation access is set to Read Only or Read/Write , the session also reserves the devices.
- [Initialize Session without Resources VI](../../vi-lib/slsc/initialize-session-without-resources-vi.html) Initializes an SLSC session without specifying any resources or opening any network connections. Use Initialize Session without Resources if you need to set session properties that control network timeouts or the ability to programmatically abort blocking network operations.

Parent topic:

NI-SLSC

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/initialize-session-with-devices-vi.html language=enus -->
## TOPIC 00064: Initialize Session with Devices VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/initialize-session-with-devices-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/initialize-session-with-devices-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes an SLSC session with one or multiple devices. The session opens network connections for devices. If reservation access is set to Read Only or Read/Write, the session also reserves the devices. This VI saves the specified device names in the Session.DefaultDevices property as the default

### Initialize Session with Devices VI

Initializes an SLSC session with one or multiple devices. The session opens network connections for devices. If **reservation access** is set to **Read Only** or **Read/Write**, the session also reserves the devices.

This VI saves the specified device names in the **Session.DefaultDevices** property as the default devices of the session. You may change the session default devices by setting the **Session.DefaultDevices** property.

You cannot use the Abort Session VI to cancel any blocking network operations performed by this VI. If you need to programmatically abort blocking network operations, use the Initialize Session without Resources instance of the Initialize Session VI to obtain a session reference, then use the Connect to Devices VI to open network connections for the devices and the Reserve Devices VI to reserve the devices.

[IMAGE alt='icon' src='initialize-session-with-devices-vi.png']

#### Inputs/Outputs

| devices — devices specifies the name(s) of the device(s) to access. For multiple devices, use a comma-delimited list. reservation access (Read/Write) — reservation access (Read/Write) specifies how you plan to access the session. The default is Read/Write. reservation group — reservation group allows sharing read/write reservations. When multiple sessions attempt to simultaneously reserve the same devices for read/write access, the reservation succeeds if they have the same reservation group. Reservation fails if they do not have the same reservation group. If you specify an empty string or do not specify this parameter, only one session can reserve the devices for read/write access at a time. Read-only reservations may share devices without specifying a reservation group. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. connect timeout (60 sec) — connect timeout (60 sec) specifies the maximum amount of time, in seconds, to wait when connecting to the specified resource. This VI returns an error if timeout expires. reservation timeout (5 sec) — reservation timeout (5 sec) specifies the maximum amount of time, in seconds, to wait to reserve a device that has been reserved by other sessions. The default is 5. If you set reservation timeout to -1, reservation timeout uses the value of the Session.ReservationTimeout property. If reservation_timeout is greater than 0 and reservation access is Read/Write, a deadlock may occur when multiple sessions that use the same group name try to reserve multiple devices. The following table shows a deadlock condition that occurs when two sessions try to reserve two modules. session 1 session 2 Reserve module 1 Reserve module 2 Try to reserve module 2 Try to reserve module 1 Wait for module 2 Wait for module 1 Both session 1 and session 2 return errors when timeout expires. To avoid the deadlock, ensure that session 1 and session 2 reserve modules in the same order. If session 1 reserves module 1 first and then reserves module 2, ensure that session 2 also reserves module 1 first and then reserves module 2. session out — session out is a reference to the newly created session. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| session 1 | session 2 |
| Reserve module 1 | Reserve module 2 |
| Try to reserve module 2 | Try to reserve module 1 |
| Wait for module 2 | Wait for module 1 |

Parent topic:

Initialize Session VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/initialize-session-with-nvmem-areas-vi.html language=enus -->
## TOPIC 00065: Initialize Session with NVMEM Areas VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/initialize-session-with-nvmem-areas-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/initialize-session-with-nvmem-areas-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes an SLSC session with one or multiple NVMEM areas. The session opens network connections for NVMEM areas. If reservation access is set to Read Only or Read/Write, the session also reserves the devices. This VI saves the specified NVMEM area names in the Session.DefaultNVMEMAreas property

### Initialize Session with NVMEM Areas VI

Initializes an SLSC session with one or multiple NVMEM areas. The session opens network connections for NVMEM areas. If **reservation access** is set to **Read Only** or **Read/Write**, the session also reserves the devices.

This VI saves the specified NVMEM area names in the **Session.DefaultNVMEMAreas** property as the default NVMEM areas of the session. This VI also saves the corresponding device names in the **Session.DefaultDevices** property as the default device of the session. You may change the session default NVMEM areas or session default devices by setting the **Session.DefaultNVMEMAreas property** or the **Session.DefaultDevices** property.

You cannot use the Abort Session VI to cancel any blocking network operations performed by this VI. If you need to programmatically abort blocking network operations, use the Initialize Session without Resources instance of the Initialize Session VI to obtain a session reference, then use the Connect to Devices VI to open network connections for the devices and the Reserve Devices VI to reserve the devices.

[IMAGE alt='icon' src='initialize-session-with-nvmem-areas-vi.png']

#### Inputs/Outputs

| NVMEM areas — NVMEM areas specifies the non-volatile memory area(s) to access. reservation access (Read/Write) — reservation access (Read/Write) specifies how you plan to access the session. The default is Read/Write. reservation group — reservation group allows sharing read/write reservations. When multiple sessions attempt to simultaneously reserve the same devices for read/write access, the reservation succeeds if they have the same reservation group. Reservation fails if they do not have the same reservation group. If you specify an empty string or do not specify this parameter, only one session can reserve the devices for read/write access at a time. Read-only reservations may share devices without specifying a reservation group. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. connect timeout (60 sec) — connect timeout (60 sec) specifies the maximum amount of time, in seconds, to wait when connecting to the specified resource. This VI returns an error if timeout expires. reservation timeout (5 sec) — reservation timeout (5 sec) specifies the maximum amount of time, in seconds, to wait to reserve a device that has been reserved by other sessions. The default is 5. If you set reservation timeout to -1, reservation timeout uses the value of the Session.ReservationTimeout property. If reservation_timeout is greater than 0 and reservation access is Read/Write, a deadlock may occur when multiple sessions that use the same group name try to reserve multiple devices. The following table shows a deadlock condition that occurs when two sessions try to reserve two modules. session 1 session 2 Reserve module 1 Reserve module 2 Try to reserve module 2 Try to reserve module 1 Wait for module 2 Wait for module 1 Both session 1 and session 2 return errors when timeout expires. To avoid the deadlock, ensure that session 1 and session 2 reserve modules in the same order. If session 1 reserves module 1 first and then reserves module 2, ensure that session 2 also reserves module 1 first and then reserves module 2. session out — session out is a reference to the newly created session. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| session 1 | session 2 |
| Reserve module 1 | Reserve module 2 |
| Try to reserve module 2 | Try to reserve module 1 |
| Wait for module 2 | Wait for module 1 |

Parent topic:

Initialize Session VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/initialize-session-with-phys-chans-vi.html language=enus -->
## TOPIC 00066: Initialize Session with Phys Chans VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/initialize-session-with-phys-chans-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/initialize-session-with-phys-chans-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes an SLSC session with one or multiple physical channels. The session opens network connections for devices that correspond to the physical channels. If reservation access is set to Read Only or Read/Write, the session also reserves the devices. This VI saves the specified physical channel

### Initialize Session with Phys Chans VI

Initializes an SLSC session with one or multiple physical channels. The session opens network connections for devices that correspond to the physical channels. If **reservation access** is set to **Read Only** or **Read/Write**, the session also reserves the devices.

This VI saves the specified physical channel names in the **Session.DefaultPhysChans** property as the default physical channels of the session. This VI also saves the corresponding device names in the **Session.DefaultDevices** property as the defaults device of the session. You may change the session default physical channels or session default devices by setting the **Session.DefaultPhysChans** property or **Session.DefaultDevices property**.

You cannot use the Abort Session VI to cancel any blocking network operations performed by this VI. If you need to programmatically abort blocking network operations, use the Initialize Session without Resources instance of the Initialize Session VI to obtain a session reference, then use the Connect to Devices VI to open network connections for the devices and the Reserve Devices VI to reserve the devices.

[IMAGE alt='icon' src='initialize-session-with-phys-chans-vi.png']

#### Inputs/Outputs

| physical channels — physical channels specifies the physical channel(s) to access. For multiple physical channels, use a comma-delimited list or colon-delimited range of physical channels. Example: "Mod1/load0:2" reservation access (Read/Write) — reservation access (Read/Write) specifies how you plan to access the session. The default is Read/Write. reservation group — reservation group allows sharing read/write reservations. When multiple sessions attempt to simultaneously reserve the same devices for read/write access, the reservation succeeds if they have the same reservation group. Reservation fails if they do not have the same reservation group. If you specify an empty string or do not specify this parameter, only one session can reserve the devices for read/write access at a time. Read-only reservations may share devices without specifying a reservation group. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. connect timeout (60 sec) — connect timeout (60 sec) specifies the maximum amount of time, in seconds, to wait when connecting to the specified resource. This VI returns an error if timeout expires. reservation timeout (5 sec) — reservation timeout (5 sec) specifies the maximum amount of time, in seconds, to wait to reserve a device that has been reserved by other sessions. The default is 5. If you set reservation timeout to -1, reservation timeout uses the value of the Session.ReservationTimeout property. If reservation_timeout is greater than 0 and reservation access is Read/Write, a deadlock may occur when multiple sessions that use the same group name try to reserve multiple devices. The following table shows a deadlock condition that occurs when two sessions try to reserve two modules. session 1 session 2 Reserve module 1 Reserve module 2 Try to reserve module 2 Try to reserve module 1 Wait for module 2 Wait for module 1 Both session 1 and session 2 return errors when timeout expires. To avoid the deadlock, ensure that session 1 and session 2 reserve modules in the same order. If session 1 reserves module 1 first and then reserves module 2, ensure that session 2 also reserves module 1 first and then reserves module 2. session out — session out is a reference to the newly created session. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| session 1 | session 2 |
| Reserve module 1 | Reserve module 2 |
| Try to reserve module 2 | Try to reserve module 1 |
| Wait for module 2 | Wait for module 1 |

Parent topic:

Initialize Session VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/initialize-session-without-resources-vi.html language=enus -->
## TOPIC 00067: Initialize Session without Resources VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/initialize-session-without-resources-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/initialize-session-without-resources-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes an SLSC session without specifying any resources or opening any network connections. Use Initialize Session without Resources if you need to set session properties that control network timeouts or the ability to programmatically abort blocking network operations. icon Inputs/Outputs cerr

### Initialize Session without Resources VI

Initializes an SLSC session without specifying any resources or opening any network connections. Use Initialize Session without Resources if you need to set session properties that control network timeouts or the ability to programmatically abort blocking network operations.

[IMAGE alt='icon' src='initialize-session-without-resources-vi.png']

#### Inputs/Outputs

| error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a reference to the newly created session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Initialize Session VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/log-in-vi.html language=enus -->
## TOPIC 00068: Log In VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/log-in-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/log-in-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves login credentials for an SLSC chassis on the local system. When the SLSC driver opens a network connection to an SLSC chassis, it checks whether there are any saved login credentials for this chassis. If so, the SLSC driver uses the saved login credentials. Otherwise, the SLSC driver tries def

### Log In VI

Saves login credentials for an SLSC chassis on the local system. When the SLSC driver opens a network connection to an SLSC chassis, it checks whether there are any saved login credentials for this chassis. If so, the SLSC driver uses the saved login credentials. Otherwise, the SLSC driver tries default credentials with anonymous as the username and an empty string as the password.

This VI opens a new network connection to the chassis to test the new credentials before it saves them, and closes it afterward. Log In does not reuse or affect cached network connections, nor does it cache the new network connection.

If you set **save credentials to disk?** to TRUE, this VI saves the credentials in a platform-specific disk location and format. If saved credentials exist in memory, they are deleted.

- (Windows) SLSC stores credentials in your Windows Credential Manager vault. The credentials are encrypted with your Windows login information. You can view, manage, or delete your credentials via Control Panel » User Accounts » Credential Manager .
- (NI Linux Real-Time) SLSC stores credentials in a cleartext JSON file in /home/lvuser/.config/nislsc/loginCache . Each SLSC chassis has a separate file.
- (Phar Lap ETS) SLSC stores credentials in a cleartext JSON file in c:\ni‑rt\system\niwebcer\nislsc\loginCache . Each SLSC chassis has a separate file. This path is not accessible over FTP. It is accessible via WebDAV and from VIs deployed to the RT target.

If you set **save credentials to disk?** to FALSE, this VI saves the credentials in the memory of the calling process. If saved credentials exist on disk, they are deleted. On Windows, exiting the application process clears in-memory credentials. On Phar Lap ETS, restarting the RT target clears in-memory credentials.

[IMAGE alt='icon' src='log-in-vi.png']

#### Inputs/Outputs

| password — password specifies the password for accessing the device. username — username specifies the username for accessing the device. session in — session in specifies the session to access for the given action. chassis — chassis specifies the chassis. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. connect timeout (60 sec) — connect timeout (60 sec) specifies the maximum amount of time, in seconds, to wait when connecting to the specified resource. This VI returns an error if timeout expires. Set connect timeout to -1 to use the value of the Session.TCPIP.ConnectTimeout property. save credentials to disk? (F) — save credentials to disk? (F) if TRUE, saves login credentials to a platform-specific disk location. If FALSE (default), credentials are stored in the memory of the calling process. session out — session out is a copy of the session in reference. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

System Setup

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/log-out-vi.html language=enus -->
## TOPIC 00069: Log Out VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/log-out-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/log-out-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes any saved credentials for this chassis. icon Inputs/Outputs cgenclassrntag.png session in session in specifies the session to access for the given action. cgenclassrntag.png chassis chassis specifies the chassis. cerrcodeclst.png error in (no error) error in (no error) describes error condit

### Log Out VI

Deletes any saved credentials for this chassis.

[IMAGE alt='icon' src='log-out-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. chassis — chassis specifies the chassis. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

System Setup

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/mergevis/slsc-command-property-node-vi.html language=enus -->
## TOPIC 00070: SLSC Command Property Node

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/mergevis/slsc-command-property-node-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/mergevis/slsc-command-property-node-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A Property Node with the SLSC Command class preselected. You must open the property using one of the Open Command VIs before you can use SLSC Command Property Node to query information about the command. icon Inputs/Outputs cgenclassrntag.png command command specifies the command to open a reference

### SLSC Command Property Node

A Property Node with the SLSC Command class preselected. You must open the property using one of the Open Command VIs before you can use SLSC Command Property Node to query information about the command.

[IMAGE alt='icon' src='slsc-command-property-node-vi.png']

#### Inputs/Outputs

| command — command specifies the command to open a reference to. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. command out — command out specifies the command referenced by the opened session. error out — error out contains error information. This output provides standard error out functionality. Property — property 1..n are examples of properties you want to get (read). |
| --- |

Parent topic:

API Reflection

Parent topic:

Generic API Reflection

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/mergevis/slsc-property-property-node-vi.html language=enus -->
## TOPIC 00071: SLSC Property Property Node

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/mergevis/slsc-property-property-node-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/mergevis/slsc-property-property-node-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A Property Node with the SLSC Property class preselected. You must open the property using one of the Open Property VIs before you can use SLSC Property Property Node to query information about the property. icon Inputs/Outputs cgenclassrntag.png property property specifies the property to open a re

### SLSC Property Property Node

A Property Node with the SLSC Property class preselected. You must open the property using one of the Open Property VIs before you can use SLSC Property Property Node to query information about the property.

[IMAGE alt='icon' src='slsc-property-property-node-vi.png']

#### Inputs/Outputs

| property — property specifies the property to open a reference to on the given device. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. property out — property out specifies the property referenced by the opened session. error out — error out contains error information. This output provides standard error out functionality. Property — property 1..n are examples of properties you want to get (read). |
| --- |

Parent topic:

API Reflection

Parent topic:

Generic API Reflection

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/mergevis/slsc-session-property-node-nvmem-area-vi.html language=enus -->
## TOPIC 00072: SLSC Session Property Node (NVMEM Area)

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/mergevis/slsc-session-property-node-nvmem-area-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/mergevis/slsc-session-property-node-nvmem-area-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A Property Node with the SLSC Session class and ActiveNVMEMArea property preselected. Property nodes may be used to access properties that are defined by the SLSC driver, but cannot be used to access properties that are defined by SLSC devices. icon Inputs/Outputs cgenclassrntag.png session session

### SLSC Session Property Node (NVMEM Area)

A Property Node with the SLSC Session class and ActiveNVMEMArea property preselected. Property nodes may be used to access properties that are defined by the SLSC driver, but cannot be used to access properties that are defined by SLSC devices.

[IMAGE alt='icon' src='slsc-session-property-node-nvmem-area-vi.png']

#### Inputs/Outputs

| session — session specifies the session to access for the given action. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. NVMEM Area:Active NVMEM Area — NVMEM Area:Active NVMEM Area contains error information. This output provides standard error out functionality. session out — session out is a copy of the session in reference. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NVMEM Access

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/mergevis/slsc-session-property-node-vi.html language=enus -->
## TOPIC 00073: SLSC Session Property Node

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/mergevis/slsc-session-property-node-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/mergevis/slsc-session-property-node-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A Property Node with the SLSC Session class preselected. Property nodes may be used to access properties that are defined by the SLSC driver, but cannot be used to access properties that are defined by SLSC devices. icon Inputs/Outputs cgenclassrntag.png session session specifies the session to acce

### SLSC Session Property Node

A Property Node with the SLSC Session class preselected. Property nodes may be used to access properties that are defined by the SLSC driver, but cannot be used to access properties that are defined by SLSC devices.

[IMAGE alt='icon' src='slsc-session-property-node-vi.png']

#### Inputs/Outputs

| session — session specifies the session to access for the given action. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. error out — error out contains error information. This output provides standard error out functionality. Property — property 1..n are examples of properties you want to get (read). |
| --- |

Parent topic:

NI-SLSC

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/mergevis/slsc-system-property-node-vi.html language=enus -->
## TOPIC 00074: SLSC System Property Node

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/mergevis/slsc-system-property-node-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/mergevis/slsc-system-property-node-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A Property Node with the SLSC System class preselected. This can be used to query which devices are available on the system, without initializing a session. icon Inputs/Outputs cerrcodeclst.png error in (no error) error in (no error) describes error conditions that occur before this node runs. This

### SLSC System Property Node

A Property Node with the SLSC System class preselected. This can be used to query which devices are available on the system, without initializing a session.

[IMAGE alt='icon' src='slsc-system-property-node-vi.png']

#### Inputs/Outputs

| error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. Property — property 1..n are examples of properties you want to get (read). |
| --- |

Parent topic:

System Setup

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/open-command-vi.html language=enus -->
## TOPIC 00075: Open Command VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/open-command-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/open-command-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a reference to a command on the given resource. This allows the application to programmatically get information about the command at run time. icon

### Open Command VI

Opens a reference to a command on the given resource. This allows the application to programmatically get information about the command at run time.

[IMAGE alt='icon' src='open-command-vi.png']

- [Open Device Command VI](../../vi-lib/slsc/open-device-command-vi.html) Opens a reference to a device command. This allows the application to programmatically get information about the command at run time.
- [Open Phys Chan Command VI](../../vi-lib/slsc/open-phys-chan-command-vi.html) Opens a reference to a physical channel command. This allows the application to programmatically get information about the command at run time.

Parent topic:

API Reflection

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/open-device-command-vi.html language=enus -->
## TOPIC 00076: Open Device Command VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/open-device-command-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/open-device-command-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a reference to a device command. This allows the application to programmatically get information about the command at run time. icon Inputs/Outputs cgenclassrntag.png session in session in specifies the session to access for the given action. cgenclassrntag.png device device specifies the devi

### Open Device Command VI

Opens a reference to a device command. This allows the application to programmatically get information about the command at run time.

[IMAGE alt='icon' src='open-device-command-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. device — device specifies the device where the property is located. command in — command in specifies the command to open a reference to. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. command out — command out specifies the command referenced by the opened session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Open Command VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/open-property-vi.html language=enus -->
## TOPIC 00077: Open Property VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/open-property-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/open-property-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a reference to a property on the given resource. This allows the application to programmatically get information about the command at run time. icon

### Open Property VI

Opens a reference to a property on the given resource. This allows the application to programmatically get information about the command at run time.

[IMAGE alt='icon' src='open-property-vi.png']

- [Open Device Property VI](../../vi-lib/slsc/open-device-property-vi.html) Opens a reference to a device property. This allows the application to programmatically get information about the property at run time.
- [Open Phys Chan Property VI](../../vi-lib/slsc/open-phys-chan-property-vi.html) Opens a reference to a physical channel property. This allows the application to programmatically get information about the property at run time.
- [Open Driver-Defined Property VI](../../vi-lib/slsc/open-driver-defined-property-vi.html) Opens a reference to a driver-defined property. This allows the application to programmatically get information about the property at run time. The SLSC Property I/O control does not display driver-defined properties, but you can type them into the I/O control or use System » API Reflection properties such as Sys.DeviceProperties to query their names.

Parent topic:

API Reflection

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/read-register-u16-vi.html language=enus -->
## TOPIC 00078: Read Register (U16) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/read-register-u16-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/read-register-u16-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads 16 bits from the given register address of the specified device. icon Inputs/Outputs cgenclassrntag.png session in session in specifies the session to access for the given action. cgenclassrntag.png device device specifies the name of the device to access. cu32.png register address register ad

### Read Register (U16) VI

Reads 16 bits from the given **register address** of the specified **device**.

[IMAGE alt='icon' src='read-register-u16-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. device — device specifies the name of the device to access. register address — register address specifies the address to access. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. device out — device out indicates the name of the device the operation was applied to. next register address — next register address next register address is register address + 1. Depending on the module's register map, this may or may not be convenient when accessing consecutive registers. data out — data out contains the data read from register address. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Read Register VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/reserve-devices-vi.html language=enus -->
## TOPIC 00079: Reserve Devices VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/reserve-devices-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/reserve-devices-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reserves one or multiple devices to prevent other sessions from access the devices. You must reserve a device before using it. To reserve a device that has been reserved by another session with Read/Write access, you can close the session, unreserve the device, or use the same reservation group name

### Reserve Devices VI

Reserves one or multiple devices to prevent other sessions from access the devices. You must reserve a device before using it.

To reserve a device that has been reserved by another session with Read/Write access, you can close the session, unreserve the device, or use the same reservation group name as that of the device. You can directly reserve a device that has been reserved by another session with Read Only access.

[IMAGE alt='icon' src='reserve-devices-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. devices — devices specifies the name(s) of the device(s) to access. For multiple devices, use a comma-delimited list. reservation access (Read/Write) — reservation access (Read/Write) specifies how you plan to access the session. The default is Read/Write. reservation group — reservation group allows sharing read/write reservations. When multiple sessions attempt to simultaneously reserve the same devices for read/write access, the reservation succeeds if they have the same reservation group. Reservation fails if they do not have the same reservation group. If you specify an empty string or do not specify this parameter, only one session can reserve the devices for read/write access at a time. Read-only reservations may share devices without specifying a reservation group. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. reservation timeout (5 sec) — reservation timeout (5 sec) specifies the maximum amount of time, in seconds, to wait to reserve a device that has been reserved by other sessions. The default is 5. If you set reservation timeout to -1, reservation timeout uses the value of the Session.ReservationTimeout property. If reservation_timeout is greater than 0 and reservation access is Read/Write, a deadlock may occur when multiple sessions that use the same group name try to reserve multiple devices. The following table shows a deadlock condition that occurs when two sessions try to reserve two modules. session 1 session 2 Reserve module 1 Reserve module 2 Try to reserve module 2 Try to reserve module 1 Wait for module 2 Wait for module 1 Both session 1 and session 2 return errors when timeout expires. To avoid the deadlock, ensure that session 1 and session 2 reserve modules in the same order. If session 1 reserves module 1 first and then reserves module 2, ensure that session 2 also reserves module 1 first and then reserves module 2. session out — session out is a copy of the session in reference. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| session 1 | session 2 |
| Reserve module 1 | Reserve module 2 |
| Try to reserve module 2 | Try to reserve module 1 |
| Wait for module 2 | Wait for module 1 |

Parent topic:

Session Configuration

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/reset-devices-vi.html language=enus -->
## TOPIC 00080: Reset Devices VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/reset-devices-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/reset-devices-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets devices to their default state. This VI sends the specified devices a hardware reset signal, reinitializes module registers to their initial value, and rereads the module's non-volatile memory. If you specify a chassis, this VI resets all of the modules in the chassis. To reboot the chassis,

### Reset Devices VI

Resets devices to their default state. This VI sends the specified devices a hardware reset signal, reinitializes module registers to their initial value, and rereads the module's non-volatile memory. If you specify a chassis, this VI resets all of the modules in the chassis. To reboot the chassis, use the Restart VI provided by the NI System Configuration API.

[IMAGE alt='icon' src='reset-devices-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. devices — devices specifies the name(s) of the device(s) to access. For multiple devices, use a comma-delimited list. If you do not specify this parameter, the session default devices will be used. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

System Setup

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/set-device-property-1d-i64-vi.html language=enus -->
## TOPIC 00081: Set Device Property (1D I64) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/set-device-property-1d-i64-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/set-device-property-1d-i64-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of the specified device property for one or more devices to the provided value. Device-defined properties will not be written until a commit is called. If the property is defined by the SLSC driver, the change takes effect immediately. If the property is defined by the device(s), the

### Set Device Property (1D I64) VI

Sets the value of the specified device property for one or more devices to the provided value.

Device-defined properties will not be written until a commit is called. If the property is defined by the SLSC driver, the change takes effect immediately. If the property is defined by the device(s), the change takes effect when properties are committed for the device(s). If you set a property multiple times between commits, only the last value will be committed.

To set a property for multiple devices, specify a comma-delimited list of devices and use an array version of this VI.

[IMAGE alt='icon' src='set-device-property-1d-i64-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. devices — devices specifies the name(s) of the device(s) to access. For multiple devices, use a comma-delimited list. If you do not specify this parameter, the session default devices will be used. property — property specifies the name of the property to access. property value — property value contains the data to write to the given property. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Set Device Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/set-device-property-bool-vi.html language=enus -->
## TOPIC 00082: Set Device Property (Bool) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/set-device-property-bool-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/set-device-property-bool-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of the specified device property for one or more devices to the provided value. Device-defined properties will not be written until a commit is called. If the property is defined by the SLSC driver, the change takes effect immediately. If the property is defined by the device(s), the

### Set Device Property (Bool) VI

Sets the value of the specified device property for one or more devices to the provided value.

Device-defined properties will not be written until a commit is called. If the property is defined by the SLSC driver, the change takes effect immediately. If the property is defined by the device(s), the change takes effect when properties are committed for the device(s). If you set a property multiple times between commits, only the last value will be committed.

To set a property for multiple devices, specify a comma-delimited list of devices and use an array version of this VI.

[IMAGE alt='icon' src='set-device-property-bool-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. devices — devices specifies the name(s) of the device(s) to access. For multiple devices, use a comma-delimited list. If you do not specify this parameter, the session default devices will be used. property — property specifies the name of the property to access. property value — property value contains the data to write to the given property. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Set Device Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/set-device-property-i32-vi.html language=enus -->
## TOPIC 00083: Set Device Property (I32) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/set-device-property-i32-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/set-device-property-i32-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of the specified device property for one or more devices to the provided value. Device-defined properties will not be written until a commit is called. If the property is defined by the SLSC driver, the change takes effect immediately. If the property is defined by the device(s), the

### Set Device Property (I32) VI

Sets the value of the specified device property for one or more devices to the provided value.

Device-defined properties will not be written until a commit is called. If the property is defined by the SLSC driver, the change takes effect immediately. If the property is defined by the device(s), the change takes effect when properties are committed for the device(s). If you set a property multiple times between commits, only the last value will be committed.

To set a property for multiple devices, specify a comma-delimited list of devices and use an array version of this VI.

[IMAGE alt='icon' src='set-device-property-i32-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. devices — devices specifies the name(s) of the device(s) to access. For multiple devices, use a comma-delimited list. If you do not specify this parameter, the session default devices will be used. property — property specifies the name of the property to access. property value — property value contains the data to write to the given property. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Set Device Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/set-device-property-u64-vi.html language=enus -->
## TOPIC 00084: Set Device Property (U64) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/set-device-property-u64-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/set-device-property-u64-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of the specified device property for one or more devices to the provided value. Device-defined properties will not be written until a commit is called. If the property is defined by the SLSC driver, the change takes effect immediately. If the property is defined by the device(s), the

### Set Device Property (U64) VI

Sets the value of the specified device property for one or more devices to the provided value.

Device-defined properties will not be written until a commit is called. If the property is defined by the SLSC driver, the change takes effect immediately. If the property is defined by the device(s), the change takes effect when properties are committed for the device(s). If you set a property multiple times between commits, only the last value will be committed.

To set a property for multiple devices, specify a comma-delimited list of devices and use an array version of this VI.

[IMAGE alt='icon' src='set-device-property-u64-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. devices — devices specifies the name(s) of the device(s) to access. For multiple devices, use a comma-delimited list. If you do not specify this parameter, the session default devices will be used. property — property specifies the name of the property to access. property value — property value contains the data to write to the given property. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Set Device Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/set-generic-property-1d-bool-vi.html language=enus -->
## TOPIC 00085: Set Generic Property (1D Bool) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/set-generic-property-1d-bool-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/set-generic-property-1d-bool-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource. To set a property for multiple devices, specify a comma-delimited list of devices and use an arra

### Set Generic Property (1D Bool) VI

Sets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource.

To set a property for multiple devices, specify a comma-delimited list of devices and use an array version of this VI.

[IMAGE alt='icon' src='set-generic-property-1d-bool-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. resources — resources is a comma-delimited list specifying the names of the resources to access. property — property specifies the name of the property to access. property value — property value contains the data to write to the given property. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Set Generic Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/set-generic-property-bool-vi.html language=enus -->
## TOPIC 00086: Set Generic Property (Bool) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/set-generic-property-bool-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/set-generic-property-bool-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource. To set a property for multiple devices, specify a comma-delimited list of devices and use an arra

### Set Generic Property (Bool) VI

Sets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource.

To set a property for multiple devices, specify a comma-delimited list of devices and use an array version of this VI.

[IMAGE alt='icon' src='set-generic-property-bool-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. resources — resources is a comma-delimited list specifying the names of the resources to access. property — property specifies the name of the property to access. property value — property value contains the data to write to the given property. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Set Generic Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/set-generic-property-i32-vi.html language=enus -->
## TOPIC 00087: Set Generic Property (I32) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/set-generic-property-i32-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/set-generic-property-i32-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource. To set a property for multiple devices, specify a comma-delimited list of devices and use an arra

### Set Generic Property (I32) VI

Sets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource.

To set a property for multiple devices, specify a comma-delimited list of devices and use an array version of this VI.

[IMAGE alt='icon' src='set-generic-property-i32-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. resources — resources is a comma-delimited list specifying the names of the resources to access. property — property specifies the name of the property to access. property value — property value contains the data to write to the given property. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Set Generic Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/set-generic-property-i64-vi.html language=enus -->
## TOPIC 00088: Set Generic Property (I64) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/set-generic-property-i64-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/set-generic-property-i64-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource. To set a property for multiple devices, specify a comma-delimited list of devices and use an arra

### Set Generic Property (I64) VI

Sets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource.

To set a property for multiple devices, specify a comma-delimited list of devices and use an array version of this VI.

[IMAGE alt='icon' src='set-generic-property-i64-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. resources — resources is a comma-delimited list specifying the names of the resources to access. property — property specifies the name of the property to access. property value — property value contains the data to write to the given property. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Set Generic Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/set-generic-property-string-vi.html language=enus -->
## TOPIC 00089: Set Generic Property (String) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/set-generic-property-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/set-generic-property-string-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource. To set a property for multiple devices, specify a comma-delimited list of devices and use an arra

### Set Generic Property (String) VI

Sets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource.

To set a property for multiple devices, specify a comma-delimited list of devices and use an array version of this VI.

[IMAGE alt='icon' src='set-generic-property-string-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. resources — resources is a comma-delimited list specifying the names of the resources to access. property — property specifies the name of the property to access. property value — property value contains the data to write to the given property. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Set Generic Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/set-generic-property-u32-vi.html language=enus -->
## TOPIC 00090: Set Generic Property (U32) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/set-generic-property-u32-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/set-generic-property-u32-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource. To set a property for multiple devices, specify a comma-delimited list of devices and use an arra

### Set Generic Property (U32) VI

Sets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource.

To set a property for multiple devices, specify a comma-delimited list of devices and use an array version of this VI.

[IMAGE alt='icon' src='set-generic-property-u32-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. resources — resources is a comma-delimited list specifying the names of the resources to access. property — property specifies the name of the property to access. property value — property value contains the data to write to the given property. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Set Generic Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/set-generic-property-u64-vi.html language=enus -->
## TOPIC 00091: Set Generic Property (U64) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/set-generic-property-u64-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/set-generic-property-u64-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource. To set a property for multiple devices, specify a comma-delimited list of devices and use an arra

### Set Generic Property (U64) VI

Sets the value of the specified device property for one or more resources. This is flexible for devices, NVMEM, physical channels, and so on, but requires that you know the exact string of the resource.

To set a property for multiple devices, specify a comma-delimited list of devices and use an array version of this VI.

[IMAGE alt='icon' src='set-generic-property-u64-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. resources — resources is a comma-delimited list specifying the names of the resources to access. property — property specifies the name of the property to access. property value — property value contains the data to write to the given property. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Set Generic Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/set-nvmem-bytes-vi.html language=enus -->
## TOPIC 00092: Set NVMEM Bytes VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/set-nvmem-bytes-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/set-nvmem-bytes-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the bytes of data to be written to the data address in the specified NVMEM area. If you set the same address multiple times between commits, only the last value will be committed. Some areas in the NVMEM of an SLSC module may be protected. You need to specify a serial number and password to wri

### Set NVMEM Bytes VI

Sets the bytes of **data** to be written to the **data address** in the specified **NVMEM area**. If you set the same address multiple times between commits, only the last value will be committed. Some areas in the NVMEM of an SLSC module may be protected. You need to specify a serial number and password to write to protected areas.

[IMAGE alt='icon' src='set-nvmem-bytes-vi.png']

#### Inputs/Outputs

| password — password specifies the password of the NVMEM area. Do not specify this input if the NVMEM area is not protected. serial number — serial number specifies the serial number of the hardware. Do not specify this input if the NVMEM area is not protected. session in — session in specifies the session to access for the given action. NVMEM area — NVMEM area specifies the the non-volatile memory area to access. This must include both the device name and NVMEM area name, such as "Mod1/capabilities." If you do not specify this parameter, the session default NVMEM areas will be used. data address — data address specifies the starting address to begin accessing data. data — data specifies the data to write to the module memory. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. NVMEM area out — NVMEM area out is a copy of the nvmem area resource. next data address — next data address is data address + data size. This may be convenient when accessing contiguous fields. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NVMEM Access

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/set-phys-chan-property-1d-bool-vi.html language=enus -->
## TOPIC 00093: Set Phys Chan Property (1D Bool) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/set-phys-chan-property-1d-bool-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/set-phys-chan-property-1d-bool-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of the specified physical channel property for one or more physical channels to the provided value. Device-defined properties will not be written until a commit is called. To set a property for multiple physical channels, specify a comma-delimited list of physical channels and use an

### Set Phys Chan Property (1D Bool) VI

Sets the value of the specified physical channel property for one or more physical channels to the provided value. Device-defined properties will not be written until a commit is called.

To set a property for multiple physical channels, specify a comma-delimited list of physical channels and use an array version of this VI.

[IMAGE alt='icon' src='set-phys-chan-property-1d-bool-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. physical channels — physical channels specifies the physical channel(s) to access. For multiple physical channels, use a comma-delimited list or colon-delimited range of physical channels. Example: "Mod1/load0:2" If you do not specify this parameter, the session default physical channels will be used. property — property specifies the name of the property to access. property value — property value contains the data to write to the given property. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Set Phys Chan Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/set-phys-chan-property-1d-dbl-vi.html language=enus -->
## TOPIC 00094: Set Phys Chan Property (1D DBL) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/set-phys-chan-property-1d-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/set-phys-chan-property-1d-dbl-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of the specified physical channel property for one or more physical channels to the provided value. Device-defined properties will not be written until a commit is called. To set a property for multiple physical channels, specify a comma-delimited list of physical channels and use an

### Set Phys Chan Property (1D DBL) VI

Sets the value of the specified physical channel property for one or more physical channels to the provided value. Device-defined properties will not be written until a commit is called.

To set a property for multiple physical channels, specify a comma-delimited list of physical channels and use an array version of this VI.

[IMAGE alt='icon' src='set-phys-chan-property-1d-dbl-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. physical channels — physical channels specifies the physical channel(s) to access. For multiple physical channels, use a comma-delimited list or colon-delimited range of physical channels. Example: "Mod1/load0:2" If you do not specify this parameter, the session default physical channels will be used. property — property specifies the name of the property to access. property value — property value contains the data to write to the given property. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Set Phys Chan Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/set-phys-chan-property-1d-string-vi.html language=enus -->
## TOPIC 00095: Set Phys Chan Property (1D String) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/set-phys-chan-property-1d-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/set-phys-chan-property-1d-string-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of the specified physical channel property for one or more physical channels to the provided value. Device-defined properties will not be written until a commit is called. To set a property for multiple physical channels, specify a comma-delimited list of physical channels and use an

### Set Phys Chan Property (1D String) VI

Sets the value of the specified physical channel property for one or more physical channels to the provided value. Device-defined properties will not be written until a commit is called.

To set a property for multiple physical channels, specify a comma-delimited list of physical channels and use an array version of this VI.

[IMAGE alt='icon' src='set-phys-chan-property-1d-string-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. physical channels — physical channels specifies the physical channel(s) to access. For multiple physical channels, use a comma-delimited list or colon-delimited range of physical channels. Example: "Mod1/load0:2" If you do not specify this parameter, the session default physical channels will be used. property — property specifies the name of the property to access. property value — property value contains the data to write to the given property. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Set Phys Chan Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/set-phys-chan-property-string-vi.html language=enus -->
## TOPIC 00096: Set Phys Chan Property (String) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/set-phys-chan-property-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/set-phys-chan-property-string-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of the specified physical channel property for one or more physical channels to the provided value. Device-defined properties will not be written until a commit is called. To set a property for multiple physical channels, specify a comma-delimited list of physical channels and use an

### Set Phys Chan Property (String) VI

Sets the value of the specified physical channel property for one or more physical channels to the provided value. Device-defined properties will not be written until a commit is called.

To set a property for multiple physical channels, specify a comma-delimited list of physical channels and use an array version of this VI.

[IMAGE alt='icon' src='set-phys-chan-property-string-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. physical channels — physical channels specifies the physical channel(s) to access. For multiple physical channels, use a comma-delimited list or colon-delimited range of physical channels. Example: "Mod1/load0:2" If you do not specify this parameter, the session default physical channels will be used. property — property specifies the name of the property to access. property value — property value contains the data to write to the given property. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Set Phys Chan Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/set-phys-chan-property-u32-vi.html language=enus -->
## TOPIC 00097: Set Phys Chan Property (U32) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/set-phys-chan-property-u32-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/set-phys-chan-property-u32-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of the specified physical channel property for one or more physical channels to the provided value. Device-defined properties will not be written until a commit is called. To set a property for multiple physical channels, specify a comma-delimited list of physical channels and use an

### Set Phys Chan Property (U32) VI

Sets the value of the specified physical channel property for one or more physical channels to the provided value. Device-defined properties will not be written until a commit is called.

To set a property for multiple physical channels, specify a comma-delimited list of physical channels and use an array version of this VI.

[IMAGE alt='icon' src='set-phys-chan-property-u32-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. physical channels — physical channels specifies the physical channel(s) to access. For multiple physical channels, use a comma-delimited list or colon-delimited range of physical channels. Example: "Mod1/load0:2" If you do not specify this parameter, the session default physical channels will be used. property — property specifies the name of the property to access. property value — property value contains the data to write to the given property. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Set Phys Chan Property VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/set-scaling-parameters-table-vi.html language=enus -->
## TOPIC 00098: Set Scaling Parameters (Table) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/set-scaling-parameters-table-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/set-scaling-parameters-table-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets scaling parameters for a table scale that maps an array of pre-scaled values to an array of corresponding scaled values. icon Inputs/Outputs cstr.png password password specifies the password of the NVMEM area. Do not specify this input if the NVMEM area is not protected. cstr.png serial number

### Set Scaling Parameters (Table) VI

Sets scaling parameters for a table scale that maps an array of pre-scaled values to an array of corresponding scaled values.

[IMAGE alt='icon' src='set-scaling-parameters-table-vi.png']

#### Inputs/Outputs

| password — password specifies the password of the NVMEM area. Do not specify this input if the NVMEM area is not protected. serial number — serial number specifies the serial number of the hardware. Do not specify this input if the NVMEM area is not protected. session in — session in specifies the session to access. physical channel — physical channel specifies the physical channel that contains the scaling equation. scaled values — scaled values specifies an array of scaled values. The array size of scaled values must equal that of pre-scaled values. pre-scaled values — pre-scaled values specifies an array of values to scale. The array size of pre-scaled values must equal that of scaled values. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. coercion — coercion specifies the method of coercing values that fall between the values in the table. Interpolate (0) The scale uses linear interpolation to coerce pre-scaled values to scaled values. RoundToNearest (1) The scale rounds a pre-scaled value to the nearest scaled value in the table. Strict (2) The scale reports an error if any value in pre-scaled values is not in scaled values. session out — session out is a copy of the session in reference. physical channel out — physical channel out returns the physical channel that contains the scaling equation. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Interpolate (0) | The scale uses linear interpolation to coerce pre-scaled values to scaled values. |
| RoundToNearest (1) | The scale rounds a pre-scaled value to the nearest scaled value in the table. |
| Strict (2) | The scale reports an error if any value in pre-scaled values is not in scaled values. |

Parent topic:

Set Scaling Parameters VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/set-scaling-parameters-vi.html language=enus -->
## TOPIC 00099: Set Scaling Parameters VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/set-scaling-parameters-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/set-scaling-parameters-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets scaling parameters for a scale. icon

### Set Scaling Parameters VI

Sets scaling parameters for a scale.

[IMAGE alt='icon' src='set-scaling-parameters-vi.png']

- [Set Scaling Parameters (Linear) VI](../../vi-lib/slsc/set-scaling-parameters-linear-vi.html) Sets scaling parameters for a linear scale that uses the equation y = mx + b , where x is a pre-scaled value and y is a scaled value.
- [Set Scaling Parameters (Polynomial) VI](../../vi-lib/slsc/set-scaling-parameters-polynomial-vi.html) Sets scaling parameters for a polynomial scale that uses an n th order polynomial equation. A polynomial scale contains both a polynomial to convert pre-scaled values to scaled values and a polynomial to convert scaled values to pre-scaled values.
- [Set Scaling Parameters (Table) VI](../../vi-lib/slsc/set-scaling-parameters-table-vi.html) Sets scaling parameters for a table scale that maps an array of pre-scaled values to an array of corresponding scaled values.
- [Set Scaling Parameters (User Defined) VI](../../vi-lib/slsc/set-scaling-parameters-user-defined-vi.html) Sets scaling parameters for a user-defined scale.

Parent topic:

Scaling

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/unflatten-names-device-vi.html language=enus -->
## TOPIC 00100: Unflatten Names (Device) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/unflatten-names-device-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/unflatten-names-device-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a comma-delimited list of device names into an array of device names. icon Inputs/Outputs cgenclassrntag.png names in names in is the comma-delimited list of device, area, or channel names to be changed to an array. cerrcodeclst.png error in (no error) error in (no error) describes error co

### Unflatten Names (Device) VI

Converts a comma-delimited list of device names into an array of device names.

[IMAGE alt='icon' src='unflatten-names-device-vi.png']

#### Inputs/Outputs

| names in — names in is the comma-delimited list of device, area, or channel names to be changed to an array. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. names out — names out is the array of device, area, or channel names. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Unflatten Names VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/unflatten-names-nvmem-area-vi.html language=enus -->
## TOPIC 00101: Unflatten Names (NVMEM Area) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/unflatten-names-nvmem-area-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/unflatten-names-nvmem-area-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a comma-delimited list of NVMEM Areas into an array of NVMEM Areas. Example: "Mod1/capabilities,Mod1/identification" -> ["Mod1/capabilities","Mod1/identification"]. icon Inputs/Outputs cgenclassrntag.png names in names in is the comma-delimited list of device, area, or channel names to be c

### Unflatten Names (NVMEM Area) VI

Converts a comma-delimited list of NVMEM Areas into an array of NVMEM Areas. Example: "Mod1/capabilities,Mod1/identification" -> ["Mod1/capabilities","Mod1/identification"].

[IMAGE alt='icon' src='unflatten-names-nvmem-area-vi.png']

#### Inputs/Outputs

| names in — names in is the comma-delimited list of device, area, or channel names to be changed to an array. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. names out — names out is the array of device, area, or channel names. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Unflatten Names VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/update-chassis-firmware-vi.html language=enus -->
## TOPIC 00102: Update Chassis Firmware VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/update-chassis-firmware-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/update-chassis-firmware-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Updates the firmware of the chassis. icon Inputs/Outputs cstr.png password password specifies the password for accessing the chassis. cstr.png username username specifies the username for accessing the chassis. cgenclassrntag.png session in session in specifies the session to access. cgenclassrntag.

### Update Chassis Firmware VI

Updates the firmware of the chassis.

[IMAGE alt='icon' src='update-chassis-firmware-vi.png']

#### Inputs/Outputs

| password — password specifies the password for accessing the chassis. username — username specifies the username for accessing the chassis. session in — session in specifies the session to access. chassis — chassis specifies the chassis to update firmware. firmware path — firmware path specifies the path of the firmware. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. connect timeout (10 sec) — connect timeout (10 sec) specifies the maximum amount of time, in seconds, to wait when connecting to the chassis. This VI returns an error if timeout expires. session out — session out is a copy of the session in reference. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

System Setup

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/write-register-u16-vi.html language=enus -->
## TOPIC 00103: Write Register (U16) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/write-register-u16-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/write-register-u16-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes 16 bits of data to the register address of the specified device. icon Inputs/Outputs cgenclassrntag.png session in session in specifies the session to access for the given action. cgenclassrntag.png device device specifies the name of the device to access. cu32.png register address register a

### Write Register (U16) VI

Writes 16 bits of **data** to the **register address** of the specified **device**.

[IMAGE alt='icon' src='write-register-u16-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. device — device specifies the name of the device to access. register address — register address specifies the address to access. data — data specifies the data to write to the module register address. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. device out — device out indicates the name of the device the operation was applied to. next register address — next register address next register address is register address + 1. Depending on the module's register map, this may or may not be convenient when accessing consecutive registers. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Write Register VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/write-register-u32-vi.html language=enus -->
## TOPIC 00104: Write Register (U32) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/write-register-u32-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/write-register-u32-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes 32 bits of data to the register address of the specified device. icon Inputs/Outputs cgenclassrntag.png session in session in specifies the session to access for the given action. cgenclassrntag.png device device specifies the name of the device to access. cu32.png register address register a

### Write Register (U32) VI

Writes 32 bits of **data** to the **register address** of the specified **device**.

[IMAGE alt='icon' src='write-register-u32-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. device — device specifies the name of the device to access. register address — register address specifies the address to access. data — data specifies the data to write to the module register address. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. device out — device out indicates the name of the device the operation was applied to. next register address — next register address next register address is register address + 1. Depending on the module's register map, this may or may not be convenient when accessing consecutive registers. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Write Register VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/write-register-u64-vi.html language=enus -->
## TOPIC 00105: Write Register (U64) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/write-register-u64-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/write-register-u64-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes 64 bits of data to the register address of the specified device. icon Inputs/Outputs cgenclassrntag.png session in session in specifies the session to access for the given action. cgenclassrntag.png device device specifies the name of the device to access. cu32.png register address register a

### Write Register (U64) VI

Writes 64 bits of **data** to the **register address** of the specified **device**.

[IMAGE alt='icon' src='write-register-u64-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. device — device specifies the name of the device to access. register address — register address specifies the address to access. data — data specifies the data to write to the module register address. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. device out — device out indicates the name of the device the operation was applied to. next register address — next register address next register address is register address + 1. Depending on the module's register map, this may or may not be convenient when accessing consecutive registers. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Write Register VI

<!--NI_TOPIC bundle=nislsc-labview-api-ref path=vi-lib/slsc/write-register-u8-vi.html language=enus -->
## TOPIC 00106: Write Register (U8) VI

- bundle_id: `nislsc-labview-api-ref`
- source_path: `vi-lib/slsc/write-register-u8-vi.html`
- source_url: https://docs-be.ni.com/bundle/nislsc-labview-api-ref/raw/resource/enus/vi-lib/slsc/write-register-u8-vi.html
- document_id: `nislsc-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes 8 bits of data to the register address of the specified device. icon Inputs/Outputs cgenclassrntag.png session in session in specifies the session to access for the given action. cgenclassrntag.png device device specifies the name of the device to access. cu32.png register address register ad

### Write Register (U8) VI

Writes 8 bits of **data** to the **register address** of the specified **device**.

[IMAGE alt='icon' src='write-register-u8-vi.png']

#### Inputs/Outputs

| session in — session in specifies the session to access for the given action. device — device specifies the name of the device to access. register address — register address specifies the address to access. data — data specifies the data to write to the module register address. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. session out — session out is a copy of the session in reference. device out — device out indicates the name of the device the operation was applied to. next register address — next register address next register address is register address + 1. Depending on the module's register map, this may or may not be convenient when accessing consecutive registers. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Write Register VI
